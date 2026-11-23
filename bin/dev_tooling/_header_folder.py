"""HeaderFolder makes, from Qt's source alone, the folder in which the
compiler finds Qt's header files."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import re
import shutil
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, List, Optional, Tuple


class HeaderFolder:
  """
  Makes, from Qt's source alone, the folder in which the compiler finds
  Qt's header files. No Qt that is installed anywhere is asked anything.

    headerFolder = HeaderFolder()
    headerFolder.setSourceFolder('/here/qt-everywhere-src-6.12.0/qtbase')
    headerFolder.setFolder('/some/folder/headers')
    headerFolder.make()
    headerFolder.getFolder()       # '/some/folder/headers'
    headerFolder.getQtVersion()    # '6.12.0'

  Why it is needed
  ----------------

  Qt's header files pull each other in by names such as
  'QtCore/qstring.h'. In Qt's source that file lies at
  'src/corelib/text/qstring.h', so the compiler cannot find it by the
  name it is asked for. And every header file asks which parts of Qt
  are in, as '#if QT_CONFIG(tooltip)', which no file of the source
  answers. When Qt itself is built, its build makes a folder that mends
  both. This class makes such a folder too, and it is laid out the way
  the header folder of an installed Qt is, so that what reads the one
  can read the other.

  Terms
  -----

  - Qt's source is what Qt is built from, as Qt's makers give it out.
    It is the same for every system.
  - A part of Qt is one of the pieces Qt comes in: QtCore, QtGui,
    QtWidgets, QtDBus. QtDBus is here because header files of QtGui
    pull its header files in.
  - A pointer is an entry of the folder that stands for a file of the
    source: a symbolic link. No header file is copied.
  - A switch names something a build of Qt may leave in or out, as
    'tooltip'. Qt's source names them all in its 'configure.cmake'
    files. A list of switches is a header file that says of each
    whether it is in.

  You provide
  -----------

  - 'setSourceFolder': the folder 'qtbase' of Qt's source.
  - 'setFolder': where the folder is to be made. It is made anew by
    'make', so it must be a folder of its own.

  What to expect
  --------------

  - 'make' fills the folder with, for each part: a pointer to every
    header file of the part, under the name and in the folder an
    installed Qt has it; one small file for each class, named as the
    class, that pulls in the header file of that class; the file named
    as the part, which pulls in every header file meant for direct
    use on every system; and the lists of switches.
  - In the lists every switch is in, so that the compiler skips
    nothing Qt can have. The few that name the shape of a build, and
    contradict another switch when both are in, are out: see
    'getLeftOutSwitches'.
  - The compiler still reads as the system it runs on. A line Qt
    writes for another system alone stays unread.
  - Header files that Qt's build makes by running a program, as
    'qvulkanfunctions.h', are not in the folder. A header file pulling
    one in is refused by the compiler, which says so.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  Where each part of Qt lies in the folder 'qtbase', and the word it
  #  has in the names Qt's build makes, as 'Q_CORE_EXPORT'.
  __part_folders__ = dict(
      QtCore='src/corelib', QtGui='src/gui', QtWidgets='src/widgets',
      QtDBus='src/dbus',
  )
  __part_words__ = dict(
      QtCore='CORE', QtGui='GUI', QtWidgets='WIDGETS', QtDBus='DBUS',
  )
  #  The header file of each part that brings in its list of switches.
  __global_headers__ = dict(
      QtCore='qglobal.h', QtGui='qtguiglobal.h',
      QtWidgets='qtwidgetsglobal.h', QtDBus='qtdbusglobal.h',
  )
  #  The parts each part is built on: its file '...Depends' pulls
  #  those in.
  __part_needs__ = dict(
      QtCore=(), QtGui=('QtCore',), QtWidgets=('QtCore', 'QtGui'),
      QtDBus=('QtCore',),
  )
  #  Switches that are out while every other switch is in, because
  #  each contradicts another one when both are in. 'static' names the
  #  shape of a build, against 'shared'. The four of OpenGL ES are the
  #  other of two kinds of OpenGL that Qt's source says exclude each
  #  other; the kind for desktops is the one that is in.
  __left_out_switches__ = (
      'static', 'opengles2', 'opengles3', 'opengles31', 'opengles32',
  )
  #  What Qt keeps of the system and the compiler it is built for, as
  #  'qplatformdefs.h'. The compiler here reads as Linux.
  __spec_name__ = 'linux-g++'
  #  The file written last into the folder. It says what the folder
  #  was made from, and marks the folder as one made here.
  __stamp_name__ = 'made_by_header_folder.txt'
  #  The three ways Qt's source declares a switch.
  __switch_line__ = re.compile(
      r'^qt_feature(?:_deprecated|_alias)?\("([^"]+)"(.*?)^\)',
      re.S | re.M)
  #  A line of a 'CMakeLists.txt' that names the header files of one of
  #  the folders an installed Qt keeps apart, as 'qpa'.
  __filter_line__ = re.compile(r'\b([A-Z]+)_HEADER_FILTERS\s+"([^"]+)"')
  #  A line that declares a class by its name and does not end there.
  #  Between the word 'class' and the name Qt writes marks of its own,
  #  as 'Q_CORE_EXPORT' and 'QT6_ONLY(Q_CORE_EXPORT)'.
  __class_line__ = re.compile(
      r'^(?:template\s*<[^;{]*>\s*)?(?:class|struct)\s+'
      r'(?:Q[A-Z0-9_]+(?:\([^()]*\))?\s+)*(Q[A-Za-z0-9_]+)\b(?![^;{]*;)')
  #  A line that gives a type another name, which Qt's build treats as
  #  it treats a class.
  __alias_lines__ = (
      re.compile(r'^typedef\s+[^;{}()]*?\b(Q[A-Za-z0-9_]+)\s*;'),
      re.compile(r'^using\s+(Q[A-Za-z0-9_]+)\s*='),
  )
  #  Lines by which Qt declares the classes that walk through a list
  #  or a map, each with the names it gives them.
  __walker_lines__ = (
      (re.compile(r'^Q_DECLARE_SEQUENTIAL_ITERATOR\((\w+)\)'),
       ('Q%sIterator',)),
      (re.compile(r'^Q_DECLARE_MUTABLE_SEQUENTIAL_ITERATOR\((\w+)\)'),
       ('QMutable%sIterator',)),
      (re.compile(r'^Q_DECLARE_ASSOCIATIVE_ITERATOR\((\w+)\)'),
       ('Q%sIterator',)),
      (re.compile(r'^Q_DECLARE_MUTABLE_ASSOCIATIVE_ITERATOR\((\w+)\)'),
       ('QMutable%sIterator',)),
  )
  __named_class__ = re.compile(r'^\s*#\s*pragma\s+qt_class\((\w+)\)')
  #  Where a 'CMakeLists.txt' of the source begins to list files of a
  #  part: for all of it, or, with 'CONDITION', for where that holds.
  __sources_call__ = re.compile(
      r'^qt_internal_(?:add_module|extend_target)\(\s*(\w+)', re.M)
  #  The words a condition of such a list may be made of and still hold
  #  on every system: the switches of Qt, which are all in here, and
  #  the words that join them.
  __everywhere_word__ = re.compile(r'^(?:QT_FEATURE_\w+|AND|OR|NOT)$')

  #  Private Variables
  __source_folder__ = None  # type: Optional[str]
  __made_folder__ = None  # type: Optional[str]
  __qt_version__ = None  # type: Optional[str]

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

  def getFolder(self) -> str:
    """
    Gives the folder that is made.

    Provided by you, through 'setFolder'. Whether it has been made yet
    is said by 'isMade'.

    Raises
    ------

    MissingVariable
      'setFolder' has not been called.
    """
    if self.__made_folder__ is None:
      raise MissingVariable(self, '__made_folder__', str)
    return self.__made_folder__

  def getPartNames(self) -> Tuple[str, ...]:
    """Gives the parts of Qt the folder is made for."""
    return (*self.__part_folders__,)

  def getPartFolder(self, partName: str) -> str:
    """
    Gives the folder of the source that holds one part of Qt, as
    'src/corelib' in the source folder for 'QtCore'.

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

  def getQtVersion(self, **kwargs) -> str:
    """
    Gives the version of Qt its source is, as '6.12.0'.

    Found for you: the source names it in its file '.cmake.conf'. You
    pass nothing; the keyword is for the method's own use.

    Raises
    ------

    LookupError
      The file names no version.
    """
    if self.__qt_version__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      path = os.path.join(self.getSourceFolder(), '.cmake.conf')
      with open(path) as file:
        found = re.search(
            r'QT_REPO_MODULE_VERSION\s+"(\d+\.\d+\.\d+)"', file.read())
      if found is None:
        infoSpec = """'%s' names no version of Qt."""
        raise LookupError(infoSpec % path)
      self.__qt_version__ = found.group(1)
      return self.getQtVersion(_recursion=True)
    return self.__qt_version__

  def getSpecFolder(self) -> str:
    """Gives the folder of the source with what Qt keeps of the system
    and the compiler it is built for, among it 'qplatformdefs.h', which
    some header files Qt calls private pull in. The compiler here reads
    as Linux, so it is the one for Linux."""
    return os.path.join(
        self.getSourceFolder(), 'mkspecs', self.__spec_name__)

  def getLeftOutSwitches(self) -> Tuple[str, ...]:
    """Gives the switches the lists say are out, while every other
    switch is in. They name the shape of a build, as 'static', and not
    a thing Qt can have."""
    return (*self.__left_out_switches__,)

  def getStampFile(self) -> str:
    """Gives the path of the file written last into the folder."""
    return os.path.join(self.getFolder(), self.__stamp_name__)

  def getStamp(self) -> str:
    """Gives what the stamp of a folder made from this source says:
    the source folder and the version of Qt."""
    return 'made from %s, Qt %s\n' % (
        self.getSourceFolder(), self.getQtVersion())

  def isMade(self) -> bool:
    """Says whether the folder has been made from this very source: it
    carries the stamp this source gives."""
    try:
      with open(self.getStampFile()) as file:
        return True if file.read() == self.getStamp() else False
    except OSError:
      return False

  def getHeaderFiles(self, partName: str) -> Tuple[str, ...]:
    """
    Gives the full path of every header file of one part in the
    source, in alphabetical order of their names. The header files
    under a folder 'doc' are examples for Qt's documentation and are
    left out. Of two header files with one name the first in
    alphabetical order of their paths is kept, as Qt's own build
    keeps one.
    """
    root = self.getPartFolder(partName)
    byName = dict()  # type: Dict[str, str]
    for here, _, names in sorted(os.walk(root)):
      if 'doc' in os.path.relpath(here, root).split(os.sep):
        continue
      for name in sorted(names):
        if name.endswith('.h') and name not in byName:
          byName[name] = os.path.join(here, name)
    return (*(byName[name] for name in sorted(byName)),)

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
    self.__qt_version__ = None

  def setFolder(self, folder: str) -> None:
    """
    Tells where the folder is to be made.

    Parameters
    ----------

    folder : str
      A folder of its own. It need not exist. If it does, it has to be
      empty or to carry the stamp of a folder made here, since 'make'
      removes what is in it.

    Raises
    ------

    TypeException
      The path is not text.

    FileExistsError
      The folder holds something and carries no stamp of ours.
    """
    if not isinstance(folder, str):
      raise TypeException('folder', folder, str)
    folder = os.path.abspath(folder)
    if os.path.isdir(folder) and os.listdir(folder):
      if not os.path.isfile(os.path.join(folder, self.__stamp_name__)):
        infoSpec = """'%s' holds files and was not made here, so it is
        not made anew."""
        raise FileExistsError(' '.join((infoSpec % folder).split()))
    self.__made_folder__ = folder

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _findSwitches(self, path: str) -> Tuple[List[str], List[str]]:
    """Gives the switches one 'configure.cmake' of the source declares:
    those it marks PUBLIC, and those it marks PRIVATE. A switch may be
    both. What is no letter and no digit in a name becomes '_', as
    Qt's build writes it."""
    public, private = [], []  # type: List[str], List[str]
    if not os.path.isfile(path):
      #  A part with no switches of its own, as QtDBus, has no such
      #  file: what it can have is switched for Qt as a whole.
      return public, private
    with open(path) as file:
      text = file.read()
    for found in self.__switch_line__.finditer(text):
      name = re.sub(r'[^A-Za-z0-9_]', '_', found.group(1))
      if re.search(r'\bPUBLIC\b', found.group(2)):
        public.append(name)
      if re.search(r'\bPRIVATE\b', found.group(2)):
        private.append(name)
    return public, private

  def _writeList(self, path: str, names: List[str], *lines: str) -> None:
    """Writes one list of switches: every switch is in, but for those
    of 'getLeftOutSwitches'. The lines given stand above them."""
    word = re.sub(r'[^A-Za-z0-9]', '_', os.path.basename(path)).upper()
    out = ['#ifndef CUTIENATOR_%s' % word, '#define CUTIENATOR_%s' % word]
    out.extend(lines)
    for name in names:
      value = -1 if name in self.__left_out_switches__ else 1
      out.append('#define QT_FEATURE_%s %d' % (name, value))
    out.append('#endif')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as file:
      file.write('%s\n' % '\n'.join(out))

  def _findFilters(self, partName: str) -> List[Tuple[str, Any]]:
    """Gives, for one part, the folders an installed Qt keeps apart,
    each with the pattern of the header files that go into it, as the
    part's 'CMakeLists.txt' names them: 'qpa' and 'rhi' for QtGui."""
    path = os.path.join(self.getPartFolder(partName), 'CMakeLists.txt')
    with open(path) as file:
      text = file.read()
    found = []  # type: List[Tuple[str, Any]]
    for match in self.__filter_line__.finditer(text):
      pattern = match.group(2).replace('\\\\', '\\')
      found.append((match.group(1).lower(), re.compile(pattern)))
    return found

  def _findInnerFolder(self, name: str, filters: List[Any]) -> str:
    """Gives the folder inside the part's own that a header file goes
    into: 'private' for one ending in '_p.h', 'qpa' and the like for
    one a pattern names, and '' for one meant for everybody."""
    for folder, pattern in filters:
      if pattern.search(name):
        return folder
    return 'private' if name.endswith('_p.h') else ''

  def _findEverywhereHeaders(self, partName: str) -> Any:
    """
    Gives the names of the header files of a part that Qt's source
    lists for every system: in the part's 'CMakeLists.txt' they stand
    in the list of the part itself, or in one whose 'CONDITION' names
    nothing but switches of Qt. A header file listed only under a
    condition that names a system, as 'WIN32' or 'ANDROID', is for
    that system, and one listed nowhere is not known to be for all.

    Only these go into the file named as the part, as Qt's own build
    puts only the header files of the system it builds for into it.
    The others still lie in the folder, each to be read by itself.
    """
    path = os.path.join(self.getPartFolder(partName), 'CMakeLists.txt')
    with open(path) as file:
      text = file.read()
    target = partName[len('Qt'):]
    found = set()  # type: Any
    for call in self.__sources_call__.finditer(text):
      if call.group(1) != target:
        continue
      depth, end = 0, len(text)
      for index in range(call.start(), len(text)):
        letter = text[index]
        depth += 1 if letter == '(' else -1 if letter == ')' else 0
        if depth == 0 and letter == ')':
          end = index
          break
      block = text[call.end():end]
      block = re.sub(r'#[^\n]*', '', block)
      head = block.split('SOURCES')[0]
      if 'CONDITION' in head:
        asked = head.split('CONDITION', 1)[1]
        words = re.findall(r'[A-Za-z_][A-Za-z0-9_]*', asked)
        if not all(self.__everywhere_word__.match(word) for word in words):
          continue
      found.update(
          os.path.basename(name)
          for name in re.findall(r'[\w/+.-]+\.h\b', block))
    return found

  def _findClassNames(self, path: str) -> List[str]:
    """
    Gives the classes one header file is the header file of: those it
    declares outside of everything else, and those it names with
    '#pragma qt_class(...)'. Reading stops where the header file says
    '#pragma qt_sync_stop_processing', as Qt's own build stops there.
    """
    with open(path, errors='replace') as file:
      text = file.read()
    text = re.sub(r'/\*.*?\*/', ' ', text, flags=re.S)
    found, depth = [], 0  # type: List[str], int
    for line in text.split('\n'):
      line = re.sub(r'//.*$', '', line)
      named = self.__named_class__.match(line)
      if named is not None:
        if named.group(1) not in found:
          found.append(named.group(1))
        continue
      if 'qt_sync_stop_processing' in line:
        break
      if line.lstrip().startswith('#'):
        continue
      if depth == 0:
        names = []  # type: List[str]
        declared = self.__class_line__.match(line)
        if declared is not None:
          names.append(declared.group(1))
        for pattern in self.__alias_lines__:
          named = pattern.match(line)
          if named is not None:
            names.append(named.group(1))
        for pattern, shapes in self.__walker_lines__:
          named = pattern.match(line)
          if named is not None:
            names.extend(shape % named.group(1) for shape in shapes)
        found.extend(name for name in names if name not in found)
      depth += line.count('{') - line.count('}')
    return found

  def _fillFromPattern(self, pattern: str, target: str,
                       **words: str) -> None:
    """Writes one file from a pattern that lies in Qt's source, with
    each '@word@' of the pattern filled in."""
    with open(os.path.join(self.getSourceFolder(), pattern)) as file:
      text = file.read()
    for word, value in words.items():
      text = text.replace('@%s@' % word, value)
    left = re.search(r'@\w+@', text)
    if left is not None:
      infoSpec = """The pattern '%s' of Qt's source has '%s', which
      nothing fills in."""
      info = infoSpec % (pattern, left.group(0))
      raise LookupError(' '.join(info.split()))
    with open(target, 'w') as file:
      file.write(text)

  def _makePart(self, partName: str) -> None:
    """Makes the folder of one part: the pointers, the files named as
    classes, the file named as the part, and the lists of switches."""
    version = self.getQtVersion()
    target = os.path.join(self.getFolder(), partName)
    inner = os.path.join(target, version, partName)
    os.makedirs(os.path.join(inner, 'private'), exist_ok=True)
    filters = self._findFilters(partName)
    everywhere = self._findEverywhereHeaders(partName)
    #  The header file a part is built with, as 'qt_pch.h', is named in
    #  its 'CMakeLists.txt' after 'PRECOMPILED_HEADER'. It is for the
    #  building of Qt alone and is no header file of Qt for anyone
    #  else, so the folder has none.
    listPath = os.path.join(self.getPartFolder(partName), 'CMakeLists.txt')
    with open(listPath) as file:
      buildOnly = {
          os.path.basename(name) for name in re.findall(
              r'PRECOMPILED_HEADER\s+"([^"]+)"', file.read())}
    direct, classFiles = [], dict()  # type: List[Any], Dict[str, str]
    for path in self.getHeaderFiles(partName):
      name = os.path.basename(path)
      if name in buildOnly:
        continue
      folder = self._findInnerFolder(name, filters)
      if folder:
        os.makedirs(os.path.join(inner, folder), exist_ok=True)
        os.symlink(path, os.path.join(inner, folder, name))
        continue
      os.symlink(path, os.path.join(target, name))
      with open(path, errors='replace') as file:
        text = file.read()
      #  The rule of Qt's own build for the file named as the part: a
      #  header file meant for everybody whose name has no '_', and
      #  that does not say 'qt_no_master_include'. Here it also has to
      #  be one Qt's source lists for every system.
      wanted = name in everywhere and '_' not in name
      if wanted and 'qt_no_master_include' not in text:
        required = re.search(
            r'^ *QT_REQUIRE_CONFIG\((\w+)\);?$', text, re.M)
        direct.append((name, required.group(1) if required else ''))
      for className in self._findClassNames(path):
        classFiles.setdefault(className, name)
    for className, name in sorted(classFiles.items()):
      with open(os.path.join(target, className), 'w') as file:
        file.write('#include <%s/%s>\n' % (partName, name))
    needs = self.__part_needs__[partName]
    with open(os.path.join(target, '%sDepends' % partName), 'w') as file:
      file.write(''.join('#include <%s/%s>\n' % (n, n) for n in needs))
    with open(os.path.join(target, partName), 'w') as file:
      file.write('#include <%s/%sDepends>\n' % (partName, partName))
      #  What a switch of the part is set to is known only once this
      #  header file of the part has been read.
      file.write('#include <%s/%s>\n' % (
          partName, self.__global_headers__[partName]))
      for name, switch in direct:
        line = '#include <%s/%s>\n' % (partName, name)
        if switch:
          #  A header file that is all of one switch of Qt is pulled
          #  in only where that switch is in, as Qt's build has it.
          line = '#if QT_CONFIG(%s)\n%s#endif\n' % (switch, line)
        file.write(line)
    low, word = partName.lower(), self.__part_words__[partName]
    public, private = self._findSwitches(
        os.path.join(self.getPartFolder(partName), 'configure.cmake'))
    self._writeList(os.path.join(target, '%s-config.h' % low), public)
    self._writeList(
        os.path.join(inner, 'private', '%s-config_p.h' % low), private)
    self._fillFromPattern(
        'cmake/modulecppexports.h.in',
        os.path.join(target, '%sexports.h' % low),
        header_base_name_upper='%sEXPORTS' % low.upper(),
        module_define_infix=word)
    major, minor, patch = (int(one) for one in version.split('.'))
    with open(os.path.join(target, '%sversion.h' % low), 'w') as file:
      file.write('#define %s_VERSION_STR "%s"\n' % (low.upper(), version))
      file.write('#define %s_VERSION 0x%02x%02x%02x\n' % (
          low.upper(), major, minor, patch))

  def make(self) -> None:
    """
    Makes the folder, anew when it is there already.

    Raises
    ------

    FileExistsError
      The folder holds something and carries no stamp of ours.
    """
    folder = self.getFolder()
    if os.path.isdir(folder) and os.listdir(folder):
      if not os.path.isfile(self.getStampFile()):
        infoSpec = """'%s' holds files and was not made here, so it is
        not made anew."""
        raise FileExistsError(' '.join((infoSpec % folder).split()))
      shutil.rmtree(folder)
    os.makedirs(folder, exist_ok=True)
    for partName in self.getPartNames():
      self._makePart(partName)
    #  The switches of Qt as a whole, and the two files Qt keeps with
    #  QtCore for all of it.
    version = self.getQtVersion()
    major, minor, patch = version.split('.')
    core = os.path.join(folder, 'QtCore')
    public, private = self._findSwitches(
        os.path.join(self.getSourceFolder(), 'configure.cmake'))
    self._writeList(
        os.path.join(core, 'qconfig.h'), public,
        '#define QT_VERSION_STR "%s"' % version,
        '#define QT_VERSION_MAJOR %s' % major,
        '#define QT_VERSION_MINOR %s' % minor,
        '#define QT_VERSION_PATCH %s' % patch,
        #  With this the word 'Q_CORE_EXPORT' and its like leave a mark
        #  the compiler writes down, so what Qt marks can be told.
        '#define QT_VISIBILITY_AVAILABLE')
    self._writeList(os.path.join(
        core, version, 'QtCore', 'private', 'qconfig_p.h'), private)
    self._fillFromPattern(
        'src/corelib/global/qtdeprecationdefinitions.h.in',
        os.path.join(core, 'qtdeprecationdefinitions.h'),
        #  Qt's own values, as its 'src/corelib/CMakeLists.txt' sets
        #  them: nothing Qt has deprecated since 5.0 is taken away, and
        #  all of it carries its notice.
        QT_DISABLE_DEPRECATED_UP_TO='0x050000',
        QT_WARN_DEPRECATED_UP_TO='0x070000')
    with open(self.getStampFile(), 'w') as file:
      file.write(self.getStamp())

  def __str__(self) -> str:
    """Says what the folder is made from and whether it is made."""
    clsName = type(self).__name__
    if self.__source_folder__ is None or self.__made_folder__ is None:
      return '<%s still waiting for its two folders>' % clsName
    state = 'made' if self.isMade() else 'not made yet'
    return '<%s %s from %s, %s>' % (
        clsName, self.getFolder(), self.getSourceFolder(), state)

  __repr__ = __str__
