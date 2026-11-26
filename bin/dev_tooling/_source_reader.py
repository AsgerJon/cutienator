"""SourceReader finds the code of a function in Qt's own source."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import re
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

from . import HeaderFolder, HeaderReader

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, FrozenSet, List, Optional, Set, Tuple

  Record = Dict[str, Any]
  Shorthands = Dict[str, List[Tuple[Tuple[str, ...], str]]]
  Stretches = List[Tuple[int, int, str]]
  Scopes = Tuple[Stretches, Stretches]


class SourceReader:
  """
  Finds, in Qt's own source, the code of a function that Qt's library
  carries under no name.

    source = SourceReader()
    source.setSourceFolder('/here/qt-everywhere-src-6.12.0/qtbase')
    found = source.findDefinitions('QtWidgets', 'QListModel::at')
    found[0]['text']        # 'QListWidgetItem *QListModel::at(int row)...'

  Terms
  -----

  - Qt's source is what Qt is built from: the files Qt gives out under
    its own licence, among them one '.cpp' file for most header files.
  - A definition is a function written out with its body of code, as
    Qt's 'qlistwidget.cpp' has 'QListModel::at'.
  - A part folder is the folder of the source that holds one part of
    Qt: 'src/corelib' for QtCore, 'src/gui' for QtGui, 'src/widgets'
    for QtWidgets.

  You provide
  -----------

  - 'setSourceFolder': the folder 'qtbase' of Qt's source, of exactly
    the Qt that is installed.
  - 'setHeaderReaders': the 'HeaderReader' of each part, for the
    shorthands its header files define. Needed by 'hasCode' only.

  What to expect
  --------------

  - Nothing is read until a definition is asked for. The '.cpp' files
    of a part are then read once and kept.
  - A definition is found by how Qt writes one: its name stands at the
    start of a line, and the curly bracket that opens its body and the
    one that closes it each stand at the start of a line of their own.
    A function written another way is not found.
  - Nothing here says whether the code found can be compiled apart
    from the file it stands in. The one who takes it finds that out.
  - A name is found as C++ reads it, in the namespace it is written
    in: 'Quick3DScreenRayCaster::Quick3DScreenRayCaster', written inside
    'namespace Qt3DRender {', 'namespace Render {' and
    'namespace Quick {', is found as
    'Qt3DRender::Render::Quick::Quick3DScreenRayCaster::...' as well,
    and as each namespace around it would give it, and as each
    'using namespace' line before it would; see 'findScopes'.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  A line of the file that pulls another file in.
  __include_line__ = re.compile(r'^\s*#\s*include\s+([<"])([^>"]+)[>"]')

  #  The name of a function with its class in front, right before the
  #  bracket that opens what it takes, as 'QListModel::at(' and
  #  'QSize::operator+=('.
  __named_code__ = re.compile(
      r'((?:[A-Za-z_]\w*\s*::\s*)+(?:operator\s*(?:\(\s*\)|\[\s*\]'
      r'|[^\s\w(\[]+|\s[^(;{}]+?)|~?[A-Za-z_]\w*))\s*\(')
  #  A line for the preprocessor, with the lines it goes on to.
  __preprocessor_line__ = re.compile(r'^[ \t]*#(?:[^\n]*\\\n)*[^\n]*', re.M)
  #  A word, as 'const' or 'Q_DECL_NOTHROW'.
  __plain_word__ = re.compile(r'[A-Za-z_]\w*')
  #  What a constructor makes before its code: a base or a member, by
  #  its name, as 'QObject' or 'QtPrivate::QSlotObjectBase'.
  __made_name__ = re.compile(
      r'(?:::\s*)?[A-Za-z_]\w*(?:\s*::\s*[A-Za-z_]\w*)*')
  #  What only an expression or a statement holds, and never the words
  #  in front of the name of a defined function.
  __no_words_in_front__ = re.compile(
      r'[(){};=,.!?|+\-/%^~]|\b(?:return|case|else|delete|new|throw'
      r'|goto|if|while|for|switch|do|using|typedef|friend|emit)\b')
  #  A line of a '.cpp' file that defines a shorthand taking arguments,
  #  the same as 'HeaderReader.getShorthands' reads in a header file.
  __shorthand_line__ = re.compile(
      r'^[ \t]*#[ \t]*define[ \t]+([A-Za-z_]\w*)\(([^)]*)\)'
      r'((?:.*\\\n)*.*)', re.M)
  #  A comment, either kind.
  __comment__ = re.compile(r'/\*.*?\*/|//[^\n]*', re.S)
  #  A name right before a bracket: a shorthand where one is defined
  #  under that name.
  __called_name__ = re.compile(r'\b([A-Za-z_]\w*)\s*\(')
  #  What may hold a curly bracket that opens or closes nothing: a
  #  comment, a text, a letter.
  __no_code__ = re.compile(
      r'//[^\n]*|/\*.*?\*/|"(?:\\.|[^"\\\n])*"|\'(?:\\.|[^\'\\\n])\'',
      re.S)
  #  What opens or closes a namespace or another pair of curly brackets,
  #  and what takes a namespace in: 'namespace QV4::Compiler {', '{',
  #  '}' and 'using namespace QV4;'. A namespace without a name, as
  #  'namespace {', is a pair of curly brackets like any other.
  __scope_mark__ = re.compile(
      r'\b(?:inline\s+)?namespace\s+'
      r'([A-Za-z_]\w*(?:\s*::\s*[A-Za-z_]\w*)*)\s*\{'
      r'|\busing\s+namespace\s+(?:::\s*)?'
      r'([A-Za-z_]\w*(?:\s*::\s*[A-Za-z_]\w*)*)\s*;'
      r'|[{}]')

  #  Private Variables
  __source_folder__ = None  # type: Optional[str]
  __found_definitions__ = None  # type: Optional[Dict[str, Any]]
  __named_functions__ = None  # type: Optional[Dict[str, Any]]
  __header_readers__ = None  # type: Optional[Tuple[HeaderReader, ...]]
  __header_shorthands__ = None  # type: Optional[Shorthands]

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getSourceFolder(self) -> str:
    """
    Gives the folder 'qtbase' of Qt's source.

    Provided by you, through 'setSourceFolder'.

    Raises
    ------

    MissingVariable
      'setSourceFolder' has not been called.
    """
    if self.__source_folder__ is None:
      raise MissingVariable(self, '__source_folder__', str)
    return self.__source_folder__

  def getPartFolder(self, partName: str) -> str:
    """
    Gives the folder of the source that holds one part of Qt.

    Raises
    ------

    LookupError
      No folder is known for that part, or the source has none.
    """
    folder = os.path.join(
        self.getSourceFolder(), HeaderFolder.getPartPlace(partName))
    if not os.path.isdir(folder):
      infoSpec = """Qt's source has no folder '%s'."""
      raise LookupError(infoSpec % folder)
    return folder

  def getSourceFiles(self, partName: str) -> Tuple[str, ...]:
    """Gives the full path of every '.cpp' file of a part, in
    alphabetical order."""
    found = []
    for folder, _, names in os.walk(self.getPartFolder(partName)):
      for name in names:
        if name.endswith('.cpp'):
          found.append(os.path.join(folder, name))
    return (*sorted(found),)

  def getHeaderReaders(self) -> Tuple[HeaderReader, ...]:
    """
    Gives the 'HeaderReader' of each part whose header files' shorthands
    are written out.

    Provided by you, through 'setHeaderReaders'.

    Raises
    ------

    MissingVariable
      'setHeaderReaders' has not been called.
    """
    if self.__header_readers__ is None:
      raise MissingVariable(self, '__header_readers__', tuple)
    return self.__header_readers__

  def _getHeaderShorthands(self) -> Shorthands:
    """Gives every shorthand the header files of the parts define, as
    'HeaderReader.getShorthands' reads them, by name."""
    if self.__header_shorthands__ is not None:
      return self.__header_shorthands__
    found = dict()  # type: Shorthands
    for headerReader in self.getHeaderReaders():
      for headerPath in headerReader.getHeaderPaths():
        for name, taken, text in HeaderReader.getShorthands(headerPath):
          found.setdefault(name, []).append((taken, text))
    self.__header_shorthands__ = found
    return found

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setSourceFolder(self, sourceFolder: str) -> None:
    """
    Tells where Qt's source lies.

    Parameters
    ----------

    sourceFolder : str
      The folder 'qtbase' of Qt's source, which holds 'src'.

    Raises
    ------

    TypeException
      The path is not text.

    FileNotFoundError
      There is no such folder, or it holds no 'src'.
    """
    if not isinstance(sourceFolder, str):
      raise TypeException('sourceFolder', sourceFolder, str)
    sourceFolder = os.path.abspath(sourceFolder)
    if not os.path.isdir(os.path.join(sourceFolder, 'src')):
      infoSpec = """There is no folder 'src' in '%s'."""
      raise FileNotFoundError(infoSpec % sourceFolder)
    self.__source_folder__ = sourceFolder
    self.__found_definitions__ = None
    self.__named_functions__ = None

  def setHeaderReaders(self, *headerReaders: HeaderReader) -> None:
    """
    Tells whose header files define the shorthands 'hasCode' writes
    out: one 'HeaderReader' per part, set up as for a reading. Their
    header files are read for '#define' lines only, by
    'HeaderReader.getShorthands'.

    Raises
    ------

    TypeException
      One of them is no 'HeaderReader'.

    ValueError
      None was given.
    """
    if not headerReaders:
      raise ValueError("'setHeaderReaders' was given no 'HeaderReader'.")
    for headerReader in headerReaders:
      if not isinstance(headerReader, HeaderReader):
        raise TypeException('headerReader', headerReader, HeaderReader)
    self.__header_readers__ = (*headerReaders,)
    self.__header_shorthands__ = None
    self.__named_functions__ = None

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def _readShorthands(cls, text: str) -> Shorthands:
    """Gives the shorthands a '.cpp' file defines, by name, read as
    'HeaderReader.getShorthands' reads those of a header file."""
    found = dict()  # type: Shorthands
    for match in cls.__shorthand_line__.finditer(text):
      body = cls.__comment__.sub(' ', match.group(3).replace('\\\n', ' '))
      taken = (*(one.strip() for one in match.group(2).split(',')),)
      found.setdefault(match.group(1), []).append(
          (taken, ' '.join(body.split())))
    return found

  @staticmethod
  def _cutCall(text: str, opened: int) -> Tuple[List[str], int]:
    """
    Gives what a call writes between its brackets, cut at the commas
    that stand in no other brackets, and where the call ends.

    Parameters
    ----------

    text : str
      The text holding the call.

    opened : int
      Where in the text the bracket opening the call stands.
    """
    depth, start, found = 0, opened + 1, []  # type: int, int, List[str]
    for index in range(opened, len(text)):
      letter = text[index]
      if letter in '([{':
        depth += 1
      elif letter in ')]}':
        depth -= 1
        if depth == 0:
          found.append(text[start:index].strip())
          return found, index + 1
      elif letter == ',' and depth == 1:
        found.append(text[start:index].strip())
        start = index + 1
    return found, len(text)

  @staticmethod
  def _fillIn(taken: Tuple[str, ...], text: str, given: List[str]) -> str:
    """
    Gives the text of a shorthand with what a call gave put in for what
    it takes, as the compiler does: '#X' becomes a string, 'A ## B'
    joins two words into one, and '__VA_ARGS__' stands for whatever was
    given after the named arguments.
    """
    named = [one for one in taken if one and one != '...']
    extra = given[len(named):]
    for word, value in zip(named, given):
      #  '#X' alone: the '#' of 'A ## X' joins, and makes no string.
      text = re.sub(r'(?<!#)#(?!#)\s*%s\b' % re.escape(word), '""', text)
      text = re.sub(r'\b%s\b' % re.escape(word),
                    lambda _, value=value: value, text)
    if taken and taken[-1] == '...':
      text = re.sub(r'(?<!#)#(?!#)\s*__VA_ARGS__\b', '""', text)
      text = text.replace('__VA_ARGS__', ', '.join(extra))
    return re.sub(r'\s*##\s*', '', text)

  @staticmethod
  def _fits(taken: Tuple[str, ...], given: List[str]) -> bool:
    """Says whether a call gives as many arguments as a shorthand
    takes: none for '()', any number more for '...'."""
    if taken == ('',):
      return given == ['']
    if taken and taken[-1] == '...':
      return len(given) >= len(taken) - 1
    return len(given) == len(taken)

  def _writeOut(self, text: str, shorthands: Shorthands) -> str:
    """
    Gives what the shorthands used in a text stand for, with what each
    call gave put in. A shorthand used inside the text of another is
    written out too, as the compiler does, and never inside its own
    text, so this ends. The text itself is not part of what is given.

    Parameters
    ----------

    text : str
      Code with no comments in it.

    shorthands : Shorthands
      Every shorthand known where the text stands, by name.
    """
    out = []  # type: List[str]
    waiting = [(text, frozenset())]  # type: List[Tuple[str, FrozenSet]]
    while waiting:
      here, inside = waiting.pop()
      for match in self.__called_name__.finditer(here):
        name = match.group(1)
        if name not in shorthands or name in inside:
          continue
        given, _ = self._cutCall(here, match.end() - 1)
        for taken, body in shorthands[name]:
          if not self._fits(taken, given):
            continue
          made = self._fillIn(taken, body, given)
          out.append(made)
          waiting.append((made, inside | {name}))
    return '\n'.join(out)

  def _findCodeNames(self, path: str, shorthands: Shorthands) -> Set[str]:
    """Gives every name of a function with its class that stands right
    before a bracket in one file of code, with its shorthands written
    out, each name without blanks."""
    with open(path, errors='replace') as code:
      text = code.read().replace('\r', '')
    known = dict()  # type: Shorthands
    for name, forms in shorthands.items():
      known[name] = [*forms]
    for name, forms in self._readShorthands(text).items():
      known.setdefault(name, []).extend(forms)
    written = self._writeOut(self.__comment__.sub(' ', text), known)
    #  A name in the file as each namespace around it would give it;
    #  see 'qualifyName'. What the shorthands stand for stands nowhere.
    scopes = self.findScopes(text)
    found = set()  # type: Set[str]
    for match in self.__named_code__.finditer(text):
      found.update(self.qualifyName(
          ''.join(match.group(1).split()), scopes, match.start(1)))
    found.update(self.__named_code__.findall(written))
    return {''.join(one.split()) for one in found}
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _splitArguments(text: str) -> List[str]:
    """Gives the arguments written between the brackets of a function,
    cut at the commas that stand in no other brackets."""
    found, depth, start = [], 0, 0
    for index, letter in enumerate(text):
      if letter in '<([{':
        depth += 1
      elif letter in '>)]}':
        depth -= 1
      elif letter == ',' and depth == 0:
        found.append(text[start:index].strip())
        start = index + 1
    last = text[start:].strip()
    if last and last != 'void':
      found.append(last)
    return found

  @classmethod
  def findScopes(cls, text: str) -> Scopes:
    """
    Gives the namespaces of a file of code, and the namespaces it takes
    in with 'using namespace', each with the stretch of the text it
    holds for, so that 'qualifyName' can say what a name written at a
    place of the file stands for.

    Read from the curly brackets alone, those in comments, texts and
    letters passed over. A namespace written in two steps at once, as
    'namespace QV4::Compiler {', is one stretch named 'QV4::Compiler'.
    A namespace without a name, as 'namespace {', adds nothing to a
    name. A 'using namespace' line holds to the end of the namespace or
    the curly brackets it stands in.

    Parameters
    ----------

    text : str
      The whole file, as it is written.

    Returns
    -------

    Scopes
      The namespaces, each as its start, its end and its full name, as
      (1200, 98000, 'Qt3DRender::Render'); then the namespaces taken
      in, each as its start, its end and its name, as
      (300, 98000, 'QV4').
    """
    blank = cls.__no_code__.sub(
        lambda found: re.sub(r'[^\n]', ' ', found.group(0)), text)
    #  Each open pair of curly brackets: the name of the namespace it
    #  opens, '' for any other, and where its inside starts.
    opened = []  # type: List[Tuple[str, int]]
    spaces = []  # type: List[Tuple[int, int, str]]
    used = []  # type: List[List[Any]]
    for mark in cls.__scope_mark__.finditer(blank):
      named, taken = mark.group(1), mark.group(2)
      if named is not None:
        opened.append((''.join(named.split()), mark.end()))
      elif taken is not None:
        used.append([mark.start(), len(blank), ''.join(taken.split()),
                     len(opened)])
      elif mark.group(0) == '{':
        opened.append(('', mark.end()))
      elif opened:
        depth = len(opened)
        name, start = opened.pop()
        if name:
          path = [one for one, _ in opened if one]
          spaces.append((start, mark.start(), '::'.join([*path, name])))
        for entry in used:
          if entry[3] >= depth and entry[1] == len(blank):
            entry[1] = mark.start()
    while opened:
      name, start = opened.pop()
      if name:
        path = [one for one, _ in opened if one]
        spaces.append((start, len(blank), '::'.join([*path, name])))
    taken = [(start, end, name) for start, end, name, _ in used]
    return spaces, taken

  @staticmethod
  def qualifyName(name: str, scopes: Scopes, place: int) -> List[str]:
    """
    Gives the full names a name written at a place of a file may stand
    for: the name as written, then with each namespace around the place
    in front, the innermost first, as C++ looks a name up, then with
    each namespace taken in before the place in front.

    'QNode::id' written inside 'namespace Qt3DCore {' gives
    ['QNode::id', 'Qt3DCore::QNode::id'].

    Parameters
    ----------

    name : str
      The name as written, as 'QNode::id'.

    scopes : Scopes
      What 'findScopes' gave for the file.

    place : int
      Where in the text of the file the name is written.
    """
    spaces, taken = scopes
    found = [name]
    inner = ''
    for start, end, path in spaces:
      if start <= place < end and len(path) > len(inner):
        inner = path
    parts = inner.split('::') if inner else []
    for count in range(len(parts), 0, -1):
      found.append('%s::%s' % ('::'.join(parts[:count]), name))
    for start, end, path in taken:
      if start <= place < end:
        found.append('%s::%s' % (path, name))
    return [*dict.fromkeys(found)]

  def _findIncludes(self, lines: List[str]) -> Tuple[str, ...]:
    """
    Gives the lines by which a file of the source pulls other files
    in, together with the '#if', '#elif', '#else' and '#endif' they
    stand under: Qt pulls some files in on one system only, and what
    is taken along has to ask the same question. An '#if' with no such
    line under it is left out, and so is a file that only exists
    while Qt is built.
    """
    kept = []  # type: List[str]
    #  Qt indents such a line here and there, as ' #if QT_CONFIG(...)'.
    directive = re.compile(r'^\s*#\s*(if|ifdef|ifndef|elif|else|endif)\b')
    commented = False
    for line in lines:
      #  A line that begins inside a comment pulls nothing in, whatever
      #  it looks like: Qt's 'qdbusmessage.cpp' has an '#endif' in one.
      began = commented
      commented = HeaderReader._endsInComment(line, commented)
      if began:
        continue
      match = self.__include_line__.match(line)
      if match is not None:
        name = match.group(2)
        made = os.path.basename(name).startswith('moc_')
        if name.endswith('.moc') or made:
          continue
        kept.append(line.strip())
      elif directive.match(line) is not None:
        #  A line going on in the next one is not followed here; Qt
        #  writes none above the lines that pull files in.
        kept.append(line.split('//')[0].strip())
    opening = ('#if', '#ifdef', '#ifndef')
    while True:
      #  Take out each '#if' to '#endif' that holds no line of ours.
      for index in range(len(kept) - 1):
        if not ''.join(kept[index].split()).startswith(opening):
          continue
        end = index + 1
        while end < len(kept):
          word = ''.join(kept[end].split())
          if word.startswith('#include') or word.startswith(opening):
            end = -1
            break
          if word.startswith('#endif'):
            break
          end += 1
        if 0 < end < len(kept):
          del kept[index:end + 1]
          break
      else:
        break
    #  Every '#if' that is left has its '#endif', or what is taken
    #  along would not compile.
    depth = 0
    for line in kept:
      word = ''.join(line.split())
      if word.startswith(opening):
        depth += 1
      elif word.startswith('#endif'):
        depth -= 1
      if depth < 0:
        break
    if depth:
      infoSpec = """The '#if' and '#endif' lines of a file of Qt's source
      do not pair up as they were read: %s"""
      raise ValueError(' '.join((infoSpec % ' | '.join(kept)).split()))
    return (*kept,)

  @classmethod
  def _blankOut(cls, text: str) -> str:
    """
    Gives a text of code with its comments, texts, letters and lines
    for the preprocessor made blanks, each of their letters a space and
    each of their line breaks kept. Every place of it is the same place
    of the text, and every bracket left in it is one of the code.
    """
    def blank(found: Any) -> str:
      return re.sub(r'[^\n]', ' ', found.group(0))
    text = cls.__no_code__.sub(blank, text)
    return cls.__preprocessor_line__.sub(blank, text)

  @classmethod
  def _keepFirstBranches(cls, text: str, code: str) -> str:
    """
    Gives 'code', the text made blanks by '_blankOut', with the lines of
    every branch of an '#if' but the first made blanks as well: those
    after an '#elif' or an '#else', up to its '#endif'. Qt may open a
    bracket in each branch, as 'if (format == GL_BGRA) {' and 'if
    (format == GL_BGRA8_EXT) {' in 'texturehelper.cpp', of which the
    compiler sees one; counted in both, the code would never close.
    Only where a body ends is read from it: a definition standing in a
    later branch is still found in 'code'.
    """
    lines = text.split('\n')
    asked = re.compile(r'[ \t]*#[ \t]*(if|ifdef|ifndef|elif|else|endif)\b')
    plain = cls.__no_code__.sub(
        lambda found: re.sub(r'[^\n]', ' ', found.group(0)), text)
    skipping = []  # type: List[bool]
    kept = list(code)
    place = 0
    for line, seen in zip(lines, plain.split('\n')):
      word = asked.match(seen)
      if word is not None:
        if word.group(1).startswith('if'):
          skipping.append(False)
        elif word.group(1) == 'endif':
          if skipping:
            skipping.pop()
        elif skipping:
          skipping[-1] = True
      elif any(skipping):
        for index in range(place, place + len(line)):
          kept[index] = ' '
      place += len(line) + 1
    return ''.join(kept)

  @staticmethod
  def _skipBalanced(code: str, opened: int) -> int:
    """Gives the place just after the bracket that closes the one at
    'opened', counting '(', '[' and '{' alike, in code made blanks of
    comments and texts; the end of the code where none does."""
    depth = 0
    for index in range(opened, len(code)):
      letter = code[index]
      if letter in '([{':
        depth += 1
      elif letter in ')]}':
        depth -= 1
        if not depth:
          return index + 1
    return len(code)

  @classmethod
  def _findBody(
      cls,
      code: str,
      after: int,
      kept: Optional[str] = None,
  ) -> Optional[Tuple[str, int]]:
    """
    Says how a function is defined after the ')' that closes what it
    takes, which stands just before 'after': 'body', with the place
    just after the '}' closing its code, or 'default', with the place
    just after the ';' of its '= default;'. None where what follows
    makes no definition, as the ';' of a call or of a declaration.

    Between the ')' and the code may stand: words, each with what it
    takes in brackets, as 'const', 'noexcept(false)', 'override' or
    Qt's 'Q_DECL_NOTHROW'; '&' and '&&'; attributes in '[[ ]]'; the
    type given back after '->'; and, for a constructor, ':' and the
    bases and members it makes, each with what it hands them in '( )'
    or '{ }'. The '{' of the code may stand anywhere: on the line of
    the name, alone on a line, or with the code on one line.
    """
    size = len(code)

    def skipBlanks(index: int) -> int:
      while index < size and code[index].isspace():
        index += 1
      return index

    index = skipBlanks(after)
    while index < size:
      if code.startswith('[[', index):
        index = skipBlanks(cls._skipBalanced(code, index))
      elif code.startswith('&&', index):
        index = skipBlanks(index + 2)
      elif code[index] == '&':
        index = skipBlanks(index + 1)
      elif code.startswith('->', index):
        index += 2
        while index < size and code[index] not in '{;=':
          if code[index] in '([':
            index = cls._skipBalanced(code, index)
          else:
            index += 1
      else:
        word = cls.__plain_word__.match(code, index)
        if word is None:
          break
        index = skipBlanks(word.end())
        if index < size and code[index] == '(':
          index = skipBlanks(cls._skipBalanced(code, index))
    if index >= size:
      return None
    if code[index] == '=':
      found = re.compile(r'=\s*default\s*;').match(code, index)
      return None if found is None else ('default', found.end())
    if code[index] == ':' and not code.startswith('::', index):
      index += 1
      while True:
        index = skipBlanks(index)
        made = cls.__made_name__.match(code, index)
        if made is None:
          return None
        index = skipBlanks(made.end())
        if index < size and code[index] == '<':
          #  The template arguments of a base, as 'QList<int>(...)'.
          depth = 0
          while index < size:
            if code[index] == '<':
              depth += 1
            elif code[index] == '>':
              depth -= 1
              if not depth:
                index += 1
                break
            elif code[index] in ';{':
              return None
            index += 1
          index = skipBlanks(index)
        if index >= size or code[index] not in '({':
          return None
        index = skipBlanks(cls._skipBalanced(code, index))
        if code.startswith('...', index):
          index = skipBlanks(index + 3)
        if index < size and code[index] == ',':
          index += 1
          continue
        break
    if index < size and code[index] == '{':
      #  Where the code ends is counted in the first branch of every
      #  '#if', 'kept', when the '{' stands in one.
      if kept is not None and kept[index] == '{':
        return 'body', cls._skipBalanced(kept, index)
      return 'body', cls._skipBalanced(code, index)
    return None

  @classmethod
  def _isWordsInFront(cls, text: str) -> bool:
    """Says whether a text may stand in front of the name of a defined
    function: the type it gives and words such as 'static', 'inline' or
    Qt's 'Q_NEVER_INLINE', and nothing that only an expression or a
    statement holds, as the '= ' of an assignment or a 'return'."""
    text = re.sub(r'\[\[.*?\]\]', ' ', text)
    while True:
      shorter = re.sub(r'<[^<>]*>', ' ', text)
      if shorter == text:
        break
      text = shorter
    if cls.__no_words_in_front__.search(text):
      return False
    return not re.search(r'(?<!:):(?!:)', text)

  @classmethod
  def _findHeadStart(cls, code: str, place: int) -> Optional[int]:
    """
    Gives where a definition whose name stands at 'place' begins: with
    the type it gives and the words in front of it, on the line of the
    name and on the lines right above, as Qt writes 'QString' alone on
    the line above 'QLocale::name() const'. A blank line, or a line
    that holds more than such words, ends what belongs to it. None
    where the text in front of the name on its own line is more than
    such words: the name is then in an expression, as in 'x = f()'.
    """
    lineStart = code.rfind('\n', 0, place) + 1
    #  Code on one line, as a shorthand writes it, ends a statement or a
    #  body before the name: the words in front start after that.
    ended = max(code.rfind(one, lineStart, place) for one in ';{}')
    prefix = code[max(lineStart, ended + 1):place]
    if not cls._isWordsInFront(prefix):
      return None
    start = place - len(prefix.lstrip())
    if ended >= lineStart:
      return start
    while lineStart > 0:
      aboveEnd = lineStart - 1
      aboveStart = code.rfind('\n', 0, aboveEnd) + 1
      above = code[aboveStart:aboveEnd]
      if not above.strip() or not cls._isWordsInFront(above):
        break
      start = aboveStart + len(above) - len(above.lstrip())
      lineStart = aboveStart
    return start

  @staticmethod
  def _pairsConditions(text: str) -> bool:
    """Says whether the '#if' lines of a text close inside it, and its
    '#else' and '#elif' lines stand under an '#if' of its own."""
    depth = 0
    for line in text.split('\n'):
      word = re.match(r'\s*#\s*(if|ifdef|ifndef|elif|else|endif)\b', line)
      if word is None:
        continue
      if word.group(1).startswith('if'):
        depth += 1
      elif word.group(1) == 'endif':
        depth -= 1
        if depth < 0:
          return False
      elif not depth:
        return False
    return depth == 0

  def _scanDefinitions(
      self,
      code: str,
      text: str,
      kept: Optional[str] = None,
  ) -> List[Record]:
    """
    Gives every definition of a function with its class in front of
    its name that a text of code holds, operators among them, however
    the text is laid out: 'name', without blanks, as
    'QSize::operator+='; 'place', where the name stands; 'start' and
    'end', where the definition begins and ends; 'kind', 'body' or
    'default'; and 'taken', what it takes as written. 'code' is the
    text made blanks of comments and texts, see '_blankOut'; 'kept',
    where given, the same with every branch of an '#if' but the first
    made blanks as well, where the end of a body is counted; see
    '_keepFirstBranches'.
    """
    found = []  # type: List[Record]
    index = 0
    while True:
      match = self.__named_code__.search(code, index)
      if match is None:
        return found
      opened = match.end() - 1
      closes = self._skipBalanced(code, opened)
      shape = self._findBody(code, closes, kept)
      start = None if shape is None else self._findHeadStart(
          code, match.start(1))
      if shape is None or start is None:
        index = match.end()
        continue
      kind, end = shape
      if not self._pairsConditions(text[start:end]):
        #  A definition across an '#if' of the file, as one standing in
        #  each branch of an '#if' and '#else', is no whole of its own.
        index = match.end()
        continue
      found.append(dict(
          name=''.join(match.group(1).split()), place=match.start(1),
          start=start, end=end, kind=kind,
          taken=text[opened + 1:closes - 1],
          const=bool(re.match(r'\s*const\b', code[closes:closes + 40])),
      ))
      #  What stands inside the code is no definition of its own.
      index = end

  def _writeOutEach(
      self,
      code: str,
      shorthands: Shorthands,
  ) -> List[Tuple[int, str]]:
    """Gives, for each use of a shorthand in code made blanks of its
    comments, texts and lines for the preprocessor, where the use
    stands and what it stands for, with every shorthand used inside
    that written out as well; see '_writeOut'."""
    out = []  # type: List[Tuple[int, str]]
    for match in self.__called_name__.finditer(code):
      name = match.group(1)
      if name not in shorthands:
        continue
      given, _ = self._cutCall(code, match.end() - 1)
      for taken, body in shorthands[name]:
        if not self._fits(taken, given):
          continue
        made = self._fillIn(taken, body, given)
        inner = dict(shorthands)
        inner.pop(name)
        out.append((match.start(1), '\n'.join(
            (made, self._writeOut(made, inner)))))
    return out

  def _readFile(self, path: str) -> List[Record]:
    """
    Gives every definition one '.cpp' file holds of a function with its
    class in front of its name, operators among them, however the code
    is laid out, and every one that a shorthand used in the file writes,
    as 'IMPLEMENT_ACCESSORS(radioDelegate)' in 'qqstylekitcontrols.cpp'
    writes 'QQStyleKitControls::set_radioDelegate'. One with '= default'
    is one too: its text is then that line.
    """
    with open(path, errors='replace') as file:
      text = file.read().replace('\r', '')
    lines = text.split('\n')
    try:
      includes = self._findIncludes(lines)
    except ValueError as valueError:
      raise ValueError('%s: %s' % (path, valueError)) from valueError
    scopes = self.findScopes(text)
    code = self._blankOut(text)

    def lineOf(place: int) -> int:
      return text.count('\n', 0, place) + 1

    def record(
        scanned: Record, written: str, place: int, line: int) -> Record:
      return dict(
          name=scanned['name'], path=path, line=line,
          names=(*self.qualifyName(scanned['name'], scopes, place),),
          usings=(*(
              one for start, end, one in scopes[1]
              if start <= place < end),),
          arguments=self._splitArguments(scanned['taken']),
          const=scanned['const'], kind=scanned['kind'],
          text=written, includes=(*includes,),
      )

    found = []  # type: List[Record]
    kept = self._keepFirstBranches(text, code)
    for scanned in self._scanDefinitions(code, text, kept):
      found.append(record(
          scanned, text[scanned['start']:scanned['end']],
          scanned['place'], lineOf(scanned['start'])))
    known = dict()  # type: Shorthands
    for name, forms in self._getHeaderShorthands().items():
      known[name] = [*forms]
    for name, forms in self._readShorthands(text).items():
      known.setdefault(name, []).extend(forms)
    for place, made in self._writeOutEach(code, known):
      madeCode = self._blankOut(made)
      for scanned in self._scanDefinitions(madeCode, made):
        found.append(record(
            scanned, made[scanned['start']:scanned['end']], place,
            lineOf(place)))
    return found

  def _createDefinitions(self, partName: str) -> None:
    """Reads every '.cpp' file of a part and keeps what it holds."""
    byName = dict()  # type: Dict[str, List[Record]]
    for path in self.getSourceFiles(partName):
      for definition in self._readFile(path):
        #  Under every full name it may stand for; see 'qualifyName'.
        for name in definition['names']:
          byName.setdefault(name, []).append(definition)
    if self.__found_definitions__ is None:
      self.__found_definitions__ = dict()
    self.__found_definitions__[partName] = byName

  def findDefinitions(self, partName: str, name: str) -> List[Record]:
    """
    Gives every definition of a function of one name in the source of
    one part: one for each form the function has there.

    Parameters
    ----------

    partName : str
      The part of Qt, as 'QtWidgets'.

    name : str
      The name as C++ writes it with its class, as 'QListModel::at',
      'QListModel::QListModel' or 'QListModel::~QListModel'.

    Returns
    -------

    List[Record]
      Each with 'name'; 'path' and 'line', where it stands; 'text', the
      whole definition as Qt wrote it; 'arguments', what it takes, each
      as written; 'const', whether it promises to change nothing; and
      'includes', the lines by which its file pulls other files in,
      with the '#if' lines they stand under.
      Empty when the source has none.
    """
    found = self.__found_definitions__
    if found is None or partName not in found:
      self._createDefinitions(partName)
    #  Kept without blanks, as 'QFoo::operatorQString' for the name the
    #  compiler gives as 'QFoo::operator QString'.
    name = ''.join(name.split())
    return [*self.__found_definitions__[partName].get(name, ())]

  @staticmethod
  def getConditions(path: str, line: int) -> Tuple[str, ...]:
    """
    Gives what the '#if' lines around a line of a '.cpp' file of Qt's
    source ask, outermost first, as '#if QT_CONFIG(tooltip)' asks
    'QT_CONFIG(tooltip)'. They are read from the text of the file the
    way 'HeaderReader.getConditions' reads those of a header file, by
    that very reading: the lines say the same in either kind of file.

    Parameters
    ----------

    path : str
      The full path of the '.cpp' file, as a definition names it under
      'path'.

    line : int
      The number of the line, the first line of the file being 1.
    """
    return HeaderReader.getConditions(path, line)

  def hasCode(self, partName: str, name: str) -> bool:
    """
    Says whether Qt's source writes code under the name of a function:
    whether the name, with its class in front, stands right before a
    bracket in any file of code of the part. The files of code are
    those ending in '.cpp', and those ending in '.mm', in which Qt
    writes for Apple's systems.

    Qt declares some functions and writes code for them nowhere, as
    the constructor of 'QStandardPaths', which is there only so that
    nobody can make one. Such a function is in no Qt on any system.

    This is a look at the text. It finds a name wherever it is written
    before a bracket, a call among them, so a yes does not say that a
    definition was found; a no says that there is none.

    The text looked at is the file as written and, beside it, what the
    shorthands it uses stand for. Qt writes the code of some functions
    through a shorthand: 'qcoreevent.cpp' has the line
    'Q_IMPL_EVENT_COMMON(QChildEvent)', and only what it stands for
    holds 'QChildEvent::~QChildEvent('. A file knows the shorthands of
    the header files of the parts, as 'HeaderReader.getShorthands'
    reads them, and its own.

    The name is looked for exactly as given. A class Qt writes in more
    than one way, as 'QLatin1String', which Qt's source also writes as
    'QLatin1StringView', is asked once for each way.

    Parameters
    ----------

    partName : str
      The part of Qt, as 'QtCore'.

    name : str
      The name as C++ writes it with its class, as
      'QStandardPaths::QStandardPaths' or 'QGlyphRun::operator+'.

    Raises
    ------

    MissingVariable
      'setHeaderReaders' has not been called.
    """
    kept = self.__named_functions__
    if kept is None:
      kept = self.__named_functions__ = dict()
    if partName not in kept:
      shorthands = self._getHeaderShorthands()
      names = set()  # type: Set[str]
      for folder, _, files in os.walk(self.getPartFolder(partName)):
        for file in files:
          if not file.endswith(('.cpp', '.mm')):
            continue
          names.update(self._findCodeNames(
              os.path.join(folder, file), shorthands))
      kept[partName] = frozenset(names)
    return True if ''.join(name.split()) in kept[partName] else False
