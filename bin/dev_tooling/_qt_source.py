"""QtSource finds the code of a function in Qt's own source."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import re
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

from . import QtPart

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, FrozenSet, List, Optional, Set, Tuple

  Record = Dict[str, Any]
  Shorthands = Dict[str, List[Tuple[Tuple[str, ...], str]]]


class QtSource:
  """
  Finds, in Qt's own source, the code of a function that Qt's library
  carries under no name.

    source = QtSource()
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
  - 'setQtParts': the 'QtPart' of each part, for the
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
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  Where each part of Qt lies in the folder 'qtbase'.
  __part_folders__ = dict(
      QtCore='src/corelib', QtGui='src/gui', QtWidgets='src/widgets',
  )
  #  A line that opens a definition: it starts at the edge, and a name
  #  with '::' in it stands right before a bracket.
  __opening_line__ = re.compile(
      r'^(?![\s#/}{]).*?\b((?:[A-Za-z_]\w*::)+~?[A-Za-z_]\w*)\s*\(')
  #  A line of the file that pulls another file in.
  __include_line__ = re.compile(r'^\s*#\s*include\s+([<"])([^>"]+)[>"]')

  #  The name of a function with its class in front, right before the
  #  bracket that opens what it takes, as 'QListModel::at(' and
  #  'QSize::operator+=('.
  __named_code__ = re.compile(
      r'((?:[A-Za-z_]\w*\s*::\s*)+(?:operator\s*(?:\(\s*\)|\[\s*\]'
      r'|[^\s\w(\[]+|\s[^(;{}]+?)|~?[A-Za-z_]\w*))\s*\(')
  #  A line of a '.cpp' file that defines a shorthand taking arguments,
  #  the same as 'QtPart.getShorthands' reads in a header file.
  __shorthand_line__ = re.compile(
      r'^[ \t]*#[ \t]*define[ \t]+([A-Za-z_]\w*)\(([^)]*)\)'
      r'((?:.*\\\n)*.*)', re.M)
  #  A comment, either kind.
  __comment__ = re.compile(r'/\*.*?\*/|//[^\n]*', re.S)
  #  A name right before a bracket: a shorthand where one is defined
  #  under that name.
  __called_name__ = re.compile(r'\b([A-Za-z_]\w*)\s*\(')

  #  Private Variables
  __source_folder__ = None  # type: Optional[str]
  __found_definitions__ = None  # type: Optional[Dict[str, Any]]
  __named_functions__ = None  # type: Optional[Dict[str, Any]]
  __qt_parts__ = None  # type: Optional[Tuple[QtPart, ...]]
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
    if partName not in self.__part_folders__:
      infoSpec = """No folder of Qt's source is known for the part '%s'."""
      raise LookupError(infoSpec % partName)
    folder = os.path.join(
        self.getSourceFolder(), self.__part_folders__[partName])
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

  def getQtParts(self) -> Tuple[QtPart, ...]:
    """
    Gives the 'QtPart' of each part whose header files' shorthands
    are written out.

    Provided by you, through 'setQtParts'.

    Raises
    ------

    MissingVariable
      'setQtParts' has not been called.
    """
    if self.__qt_parts__ is None:
      raise MissingVariable(self, '__qt_parts__', tuple)
    return self.__qt_parts__

  def _getHeaderShorthands(self) -> Shorthands:
    """Gives every shorthand the header files of the parts define, as
    'QtPart.getShorthands' reads them, by name."""
    if self.__header_shorthands__ is not None:
      return self.__header_shorthands__
    found = dict()  # type: Shorthands
    for qtPart in self.getQtParts():
      for headerPath in qtPart.getHeaderPaths():
        for name, taken, text in QtPart.getShorthands(headerPath):
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

  def setQtParts(self, *qtParts: QtPart) -> None:
    """
    Tells whose header files define the shorthands 'hasCode' writes
    out: one 'QtPart' per part, set up as for a reading. Their
    header files are read for '#define' lines only, by
    'QtPart.getShorthands'.

    Raises
    ------

    TypeException
      One of them is no 'QtPart'.

    ValueError
      None was given.
    """
    if not qtParts:
      raise ValueError("'setQtParts' was given no 'QtPart'.")
    for qtPart in qtParts:
      if not isinstance(qtPart, QtPart):
        raise TypeException('qtPart', qtPart, QtPart)
    self.__qt_parts__ = (*qtParts,)
    self.__header_shorthands__ = None
    self.__named_functions__ = None

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def _readShorthands(cls, text: str) -> Shorthands:
    """Gives the shorthands a '.cpp' file defines, by name, read as
    'QtPart.getShorthands' reads those of a header file."""
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
      text = re.sub(r'#\s*%s\b' % re.escape(word), '""', text)
      text = re.sub(r'\b%s\b' % re.escape(word),
                    lambda _, value=value: value, text)
    if taken and taken[-1] == '...':
      text = re.sub(r'#\s*__VA_ARGS__\b', '""', text)
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
    found = set(self.__named_code__.findall(text))
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
    for line in lines:
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

  def _readFile(self, path: str) -> List[Record]:
    """Gives every definition one '.cpp' file holds that is written
    the way Qt writes one."""
    with open(path, errors='replace') as file:
      lines = file.read().split('\n')
    try:
      includes = self._findIncludes(lines)
    except ValueError as valueError:
      raise ValueError('%s: %s' % (path, valueError)) from valueError
    found = []
    for index, line in enumerate(lines):
      match = self.__opening_line__.match(line)
      if match is None or line.rstrip().endswith(';'):
        continue
      #  The body: from the line that is just '{' to the next line that
      #  is just '}'. Before the '{' nothing may end a statement.
      opens = index
      while opens < len(lines) and lines[opens].rstrip() != '{':
        if lines[opens].rstrip().endswith((';', '}')):
          opens = len(lines)
          break
        opens += 1
      if opens >= len(lines):
        continue
      closes = opens
      while closes < len(lines) and lines[closes].rstrip() != '}':
        closes += 1
      if closes >= len(lines):
        continue
      #  What stands above the name and belongs to it: the type the
      #  function gives, where Qt writes that on a line of its own.
      first = index
      while first > 0:
        above = lines[first - 1].strip()
        if not above or above.endswith((';', '}', '{', ':')):
          break
        if above.startswith(('#', '//', '/*', '*')) or above.endswith('*/'):
          break
        first -= 1
      head = ' '.join(lines[index:opens])
      inside = head[match.end():]
      depth, end = 1, 0
      for end, letter in enumerate(inside):
        depth += 1 if letter == '(' else -1 if letter == ')' else 0
        if depth == 0:
          break
      after = inside[end + 1:]
      found.append(dict(
          name=match.group(1), path=path, line=first + 1,
          arguments=self._splitArguments(inside[:end]),
          const=True if re.match(r'\s*const\b', after) else False,
          text='\n'.join(lines[first:closes + 1]),
          includes=(*includes,),
      ))
    return found

  def _createDefinitions(self, partName: str) -> None:
    """Reads every '.cpp' file of a part and keeps what it holds."""
    byName = dict()  # type: Dict[str, List[Record]]
    for path in self.getSourceFiles(partName):
      for definition in self._readFile(path):
        byName.setdefault(definition['name'], []).append(definition)
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
    return [*self.__found_definitions__[partName].get(name, ())]

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
    the header files of the parts, as 'QtPart.getShorthands'
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
      'setQtParts' has not been called.
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
