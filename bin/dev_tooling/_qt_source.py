"""QtSource finds the code of a function in Qt's own source."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import re
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, List, Optional, Tuple

  Record = Dict[str, Any]


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
  __include_line__ = re.compile(r'^#\s*include\s+([<"])([^>"]+)[>"]')

  #  Private Variables
  __source_folder__ = None  # type: Optional[str]
  __found_definitions__ = None  # type: Optional[Dict[str, Any]]

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
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
    directive = re.compile(r'^#\s*(if|ifdef|ifndef|elif|else|endif)\b')
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
    return (*kept,)

  def _readFile(self, path: str) -> List[Record]:
    """Gives every definition one '.cpp' file holds that is written
    the way Qt writes one."""
    with open(path, errors='replace') as file:
      lines = file.read().split('\n')
    includes = self._findIncludes(lines)
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
