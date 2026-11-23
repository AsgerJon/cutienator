"""QtPart reads every header file of one part of Qt."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

from . import HeaderFile, HeaderFolder

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import (Any, Dict, FrozenSet, Iterator, List, Optional, Set,
                      Tuple)

  Record = Dict[str, Any]
  HeaderFiles = Tuple[HeaderFile, ...]
  Paths = Tuple[str, ...]
  Place = Tuple[Optional[str], Optional[int]]


class QtPart:
  """
  Reads every header file of one part of Qt, as 'QtCore', in a single
  run of the compiler, and keeps what each header file holds.

    qtPart = QtPart()
    qtPart.setPartName('QtCore')
    qtPart.setWorkFolder('/some/folder')
    qtPart.read()                               # two to three minutes
    for headerFile in qtPart.getHeaderFiles():  # 286 of them
      headerFile.getContents()                  # a tuple of records

  Terms
  -----

  - A part of Qt is one of the pieces Qt comes in, as 'QtCore'. It has
    a folder of its own in Qt's header folder.
  - A header file is a text file in that folder ending in '.h'. It is
    source code: what Qt's developers wrote.
  - The own list of a part is the file named as the part itself, as
    'QtCore/QtCore'. It pulls in the header files that are meant to be
    used directly, in an order that works.
  - A top-level thing is something a header file declares outside of
    everything else: a class, a function, a namespace, another name for
    a type. What a class or a namespace holds is inside it.
  - A record is what the compiler wrote down about one top-level thing,
    as JSON turned into Python.
  - A place is a file and a line in it.
  - A reading is the finished result for one part: a folder in the work
    folder, named as the part, with one record file per header file.
  - The stamp is a small file written last into a reading. It says
    which Qt the reading was made from and what each header file gave.

  You provide
  -----------

  - 'setHeaderFolder': the 'HeaderFolder' that makes, from Qt's source,
    the folder Qt's header files are read in. Once, for every
    'QtPart'. Required.
  - 'setPartName': the part of Qt to read. Required.
  - 'setWorkFolder': an existing folder to keep readings in. Required.

  Found for you
  -------------

  - 'getQtHeaderFolder' and 'getQtVersion': from Qt's source, through
    the 'HeaderFolder'. No Qt that is installed is asked.
  - 'getHeaderPaths': every header file lying right in the folder of
    the part.
  - 'getHeaderFiles': one 'HeaderFile' per header file, once the part
    has been read.
  - 'getIncludeLines': the lines of C++ that pull a header file in.
  - 'getSignalLines': the lines of a header file that declare signals,
    read from its text.
  - 'getQtSharedObject': the compiled Qt code of this part, of the Qt
    installed on the machine, asked of Qt's own program 'qmake6'. It
    is for compiling against, and 'getOfferedNames' lists the names it
    offers.

  What to expect
  --------------

  - 'read' is the only method that takes time. It compiles nothing: the
    compiler reads the text and writes down what it read, and that is
    cut into one record per top-level thing.
  - All or nothing. A reading is put in place only when the whole part
    was read and every check passed. A failure raises, says why, and
    leaves an earlier reading as it was.
  - A reading stays in the work folder. 'getHeaderFiles' works in a
    later Python without reading again, for as long as Qt is the same.
  - After Qt changed, 'getHeaderFiles' refuses and says to read again.
  - Macros, '#include' lines and comments are not in the records: the
    compiler writes none of them down.
  - The compiler writes the file and line of a place only when they
    differ from the place it wrote just before. Records are kept with
    every file and line written out, so that each can be read alone.
    That is the one change made to what the compiler wrote.
  - In the work folder the names of the part, of the part followed by
    '.unfinished' and of the part followed by '.previous' belong to this
    class, which removes folders of those names.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _run(*command: str) -> str:
    """
    Runs one program to its end and gives what it printed.

    Parameters
    ----------

    *command : str
      The program, then each of its arguments, one per entry.

    Raises
    ------

    FileNotFoundError
      The program is not installed on this machine.

    RuntimeError
      The program ran and reported a failure; its message is included.
    """
    try:
      done = subprocess.run(command, capture_output=True, text=True)
    except FileNotFoundError as fileNotFoundError:
      infoSpec = """The program '%s' is needed and is not installed."""
      raise FileNotFoundError(infoSpec % command[0]) from fileNotFoundError
    if done.returncode:
      infoSpec = """The program '%s' failed: %s"""
      raise RuntimeError(infoSpec % (command[0], done.stderr.strip()))
    return done.stdout

  @staticmethod
  def _fillPlaces(node: Any, lastPlace: List[Any]) -> None:
    """
    Writes out, in every place of a record, the file and the line the
    compiler left out.

    The compiler writes the file and line of a place only when they
    differ from those of the place it wrote just before. Cut out of the
    report, a record would have places saying too little.

    Parameters
    ----------

    node : Any
      A record, or a part of one. It is changed where it stands.

    lastPlace : List[Any]
      The file and the line of the place written just before 'node'. It
      is kept up to date as the places of 'node' go by, in the order
      the compiler wrote them.
    """
    if isinstance(node, dict):
      if 'offset' in node and 'col' in node and 'tokLen' in node:
        if 'file' in node:
          lastPlace[0], lastPlace[1] = node['file'], node['line']
        elif 'line' in node:
          lastPlace[1] = node['line']
        others = {
            key: value for key, value in node.items()
            if key not in ('offset', 'file', 'line')
        }
        offset = node['offset']
        node.clear()
        node['offset'] = offset
        node['file'], node['line'] = lastPlace[0], lastPlace[1]
        node.update(others)
        return
      for value in node.values():
        if isinstance(value, (dict, list)):
          QtPart._fillPlaces(value, lastPlace)
    elif isinstance(node, list):
      for value in node:
        if isinstance(value, (dict, list)):
          QtPart._fillPlaces(value, lastPlace)

  @staticmethod
  def _getPlace(record: Record) -> Place:
    """
    Gives the place a record stands on, once its places are filled in.

    For a thing a macro wrote, that is where the macro is used, not
    where the macro is defined.
    """
    place = record.get('loc', dict())
    place = place.get('expansionLoc', place)
    return place.get('file'), place.get('line')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The 'HeaderFolder' that makes the folder Qt's header files are
  #  read in, and what is taken from it: where that folder is and which
  #  version of Qt it is made from. Kept for every 'QtPart'.
  __header_folder__ = None  # type: Optional[HeaderFolder]
  __qt_header_folder__ = None  # type: Optional[str]
  __qt_version__ = None  # type: Optional[str]
  #  Where the Qt installed on the machine keeps its shared objects.
  #  Asked of 'qmake6' once, and kept for every 'QtPart'.
  __qt_shared_object_folder__ = None  # type: Optional[str]
  #  The lines of each header file read so far on which Qt declares
  #  signals, kept for every 'QtPart'.
  __signal_lines__ = dict()  # type: Dict[str, FrozenSet[int]]
  #  A line that defines a shorthand taking arguments, with the lines it
  #  goes on to after a backslash: the name, what it takes, and the
  #  text it stands for.
  __shorthand_line__ = re.compile(
      r'^[ \t]*#[ \t]*define[ \t]+([A-Za-z_]\w*)\(([^)]*)\)'
      r'((?:.*\\\n)*.*)', re.M)
  #  The shorthands of each header file read so far, kept for every
  #  'QtPart'.
  __read_shorthands__ = dict()  # type: Dict[str, Tuple[Any, ...]]

  #  How the compiler lays out its report. A top-level thing opens with
  #  a line of four spaces and a bracket, and closes the same way. The
  #  place of the thing itself is its entry 'loc', six spaces in.
  __thing_opens__ = b'    {\n'
  __thing_closes__ = (b'    },\n', b'    }\n')
  __place_opens__ = b'      "loc": {\n'
  __place_empty__ = b'      "loc": {},\n'
  __place_closes__ = b'      },\n'

  #  The line after one ending like this names the file a header was
  #  pulled in from. That is no place of its own.
  __included_from__ = b'"includedFrom": {\n'

  #  The file and the line of a place, as the compiler writes them.
  __file_key__ = re.compile(rb'^ *"file": (".*"),?\n$')
  __line_key__ = re.compile(rb'^ *"line": (\d+),?\n$')

  #  A line of C++ pulling a header file in by its place in Qt's header
  #  folder, as the own list of a part has them.
  __include_line__ = re.compile(r'^#include <(\S+\.h)>$')

  #  Fallback Variables

  #  Private Variables
  __part_name__ = None  # type: Optional[str]
  __work_folder__ = None  # type: Optional[str]
  __header_files__ = None  # type: Optional[HeaderFiles]
  __named_header_paths__ = None  # type: Optional[Paths]
  __offered_names__ = None  # type: Optional[FrozenSet[str]]
  __found_pullers__ = None  # type: Optional[Dict[str, Optional[str]]]
  __with_private__ = False
  __own_list_paths__ = None  # type: Optional[FrozenSet[str]]
  #  The header files a reading leaves out, each by its name with the
  #  reason given for it; see 'setLeftOutHeaders'.
  __left_out_headers__ = None  # type: Optional[Dict[str, str]]

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def getHeaderFolder(cls) -> HeaderFolder:
    """
    Gives the 'HeaderFolder' that makes, from Qt's source, the folder
    Qt's header files are read in.

    Provided by you, through 'setHeaderFolder', once for every
    'QtPart'.

    Raises
    ------

    MissingVariable
      'setHeaderFolder' has not been called.
    """
    if cls.__header_folder__ is None:
      raise MissingVariable(cls, '__header_folder__', HeaderFolder)
    return cls.__header_folder__

  @classmethod
  def setHeaderFolder(cls, headerFolder: HeaderFolder) -> None:
    """
    Tells where Qt's header files are read: in the folder a
    'HeaderFolder' makes from Qt's source. Every 'QtPart' reads there,
    and no Qt that is installed is asked where its header files are or
    which version it is.

    Raises
    ------

    TypeException
      It is no 'HeaderFolder'.
    """
    if not isinstance(headerFolder, HeaderFolder):
      raise TypeException('headerFolder', headerFolder, HeaderFolder)
    cls.__header_folder__ = headerFolder
    cls.__qt_header_folder__ = None
    cls.__qt_version__ = None

  @classmethod
  def _createQtHeaderFolder(cls, ) -> None:
    """Has the 'HeaderFolder' make its folder, where that has not been
    done from this very source, and remembers where the folder is."""
    headerFolder = cls.getHeaderFolder()
    if not headerFolder.isMade():
      headerFolder.make()
    cls.__qt_header_folder__ = headerFolder.getFolder()

  @classmethod
  def getQtHeaderFolder(cls, **kwargs) -> str:
    """
    Gives the folder in which the compiler finds Qt's header files.

    Found for you: it is the folder the 'HeaderFolder' makes from Qt's
    source, laid out the way the header folder of an installed Qt is.
    It is made at the first call where it is not there yet. You pass
    nothing; the keyword is for the method's own use.

    Raises
    ------

    MissingVariable
      'setHeaderFolder' has not been called.
    """
    if cls.__qt_header_folder__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      cls._createQtHeaderFolder()
      return cls.getQtHeaderFolder(_recursion=True)
    return cls.__qt_header_folder__

  @classmethod
  def _createQtVersion(cls, ) -> None:
    """Takes the version of Qt from its source and remembers it."""
    cls.__qt_version__ = cls.getHeaderFolder().getQtVersion()

  @classmethod
  def getQtVersion(cls, **kwargs) -> str:
    """
    Gives the version of Qt that is read, as '6.12.0'.

    Found for you: Qt's source names its own version, and the
    'HeaderFolder' reads it there. You pass nothing; the keyword is for
    the method's own use.

    Raises
    ------

    MissingVariable
      'setHeaderFolder' has not been called.
    """
    if cls.__qt_version__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      cls._createQtVersion()
      return cls.getQtVersion(_recursion=True)
    return cls.__qt_version__

  @classmethod
  def _createQtSharedObjectFolder(cls, ) -> None:
    """Asks 'qmake6' where Qt keeps its shared objects and remembers it."""
    answer = cls._run('qmake6', '-query', 'QT_INSTALL_LIBS')
    cls.__qt_shared_object_folder__ = answer.strip()

  @classmethod
  def getQtSharedObjectFolder(cls, **kwargs) -> str:
    """
    Gives the folder where Qt keeps its shared objects, as '/usr/lib'.

    Found for you: there is no setter. The first call asks Qt's own
    program 'qmake6', and the answer is kept for every 'QtPart'. You
    pass nothing; the keyword is for the method's own use.

    Raises
    ------

    FileNotFoundError
      'qmake6' is not installed.

    RuntimeError
      'qmake6' ran and reported a failure; its message is included.
    """
    if cls.__qt_shared_object_folder__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      cls._createQtSharedObjectFolder()
      return cls.getQtSharedObjectFolder(_recursion=True)
    return cls.__qt_shared_object_folder__

  def getQtSharedObject(self) -> str:
    """
    Gives the Qt shared object holding the compiled code of this part,
    as '/usr/lib/libQt6Core.so.6' for 'QtCore'.

    Found for you, from the name of the part. A ritual file calling
    into this part is compiled against it.

    Raises
    ------

    FileNotFoundError
      The shared object is not where it is expected to be.
    """
    name = 'lib%s.so.6' % self.getPartName().replace('Qt', 'Qt6', 1)
    path = os.path.join(self.getQtSharedObjectFolder(), name)
    if not os.path.isfile(path):
      infoSpec = """The part '%s' was expected to have its Qt shared
      object at '%s', and there is no such file."""
      info = infoSpec % (self.getPartName(), path)
      raise FileNotFoundError(' '.join(info.split()))
    return path

  @classmethod
  def getSignalLines(cls, headerPath: str) -> FrozenSet[int]:
    """
    Gives the lines of a header file on which Qt declares signals,
    read from the text of the file alone.

    Qt writes the signals of a class under a line 'Q_SIGNALS:' or
    'signals:', up to the next line that opens another section of the
    class, as 'public:' and 'private Q_SLOTS:', or the line that closes
    the class. A function marked 'Q_SIGNAL' by itself counts as well.
    The compiler does not report which functions are signals, and
    Qt's own list of them is made when Qt is built, so it is no part
    of Qt's source.

    Parameters
    ----------

    headerPath : str
      The full path of the header file, as a record names it under
      'loc'.

    Returns
    -------

    FrozenSet[int]
      The numbers of those lines, the first line of the file being 1.
    """
    kept = cls.__signal_lines__
    if headerPath in kept:
      return kept[headerPath]
    with open(headerPath, errors='replace') as file:
      text = file.read().replace('\r', '')
    #  Comments go, and the lines keep their numbers.
    text = re.sub(
        r'/\*.*?\*/', lambda found: '\n' * found.group(0).count('\n'),
        text, flags=re.S)
    opens = re.compile(r'^\s*(?:Q_SIGNALS|signals)\s*:')
    closes = re.compile(
        r'^\s*(?:(?:public|protected|private)\b[^;()]*:\s*$'
        r'|(?:Q_SLOTS|slots)\s*:|\};)')
    found, inside = set(), False  # type: Set[int], bool
    for number, line in enumerate(text.split('\n'), 1):
      line = re.sub(r'//.*$', '', line)
      if opens.match(line):
        inside = True
      elif closes.match(line):
        inside = False
      elif inside or re.search(r'\bQ_SIGNAL\b', line):
        found.add(number)
    kept[headerPath] = frozenset(found)
    return kept[headerPath]

  @classmethod
  def getShorthands(cls, headerPath: str) -> Tuple[Any, ...]:
    """
    Gives the shorthands a header file defines, read from its text
    alone. C++ calls them macros.

    A shorthand is a line '#define NAME(...)' and the lines it goes on
    to after a backslash. Where code writes 'NAME(...)', the compiler
    reads the text of the shorthand in its place, with what was written
    between the brackets put in for its arguments. Qt writes the code of
    some functions that way: 'qcoreevent.h' defines
    'Q_IMPL_EVENT_COMMON(Class)', whose text holds
    'Class::~Class() = default;', and 'qcoreevent.cpp' writes
    'Q_IMPL_EVENT_COMMON(QChildEvent)'. Only a shorthand with brackets
    after its name is read; one without, as '#define QT_NO_CAST', is
    left out.

    Parameters
    ----------

    headerPath : str
      The full path of the header file.

    Returns
    -------

    Tuple[Any, ...]
      One 'Tuple[str, Tuple[str, ...], str]' per shorthand, in the
      order the file defines them: the name, the names of what it
      takes, and the text it stands for, without comments and as one
      line.
    """
    kept = cls.__read_shorthands__
    if headerPath in kept:
      return kept[headerPath]
    with open(headerPath, errors='replace') as file:
      text = file.read().replace('\r', '')
    found = []
    for match in cls.__shorthand_line__.finditer(text):
      body = match.group(3).replace('\\\n', ' ')
      body = re.sub(r'/\*.*?\*/', ' ', body)
      body = re.sub(r'//.*$', '', body)
      taken = (*(one.strip() for one in match.group(2).split(',')),)
      found.append((match.group(1), taken, ' '.join(body.split())))
    kept[headerPath] = (*found,)
    return kept[headerPath]

  def getMarkedNames(self) -> FrozenSet[str]:
    """
    Gives the names of the functions and values that the header files
    of the part declare with Qt's mark for use from outside Qt in
    front, as 'Q_CORE_EXPORT', read from the text of the files. It is
    for what stands outside of every class: a class says by its own
    declaration whether it is marked. 'Q_AUTOTEST_EXPORT' is no such
    mark: it holds only in a Qt built for Qt's own tests.

    Returns
    -------

    FrozenSet[str]
      The bare names, without a namespace and without what a function
      takes.
    """
    marked = re.compile(
        r'^\s*(?:(?:\[\[nodiscard\]\]|Q_DECL_\w+|Q_REQUIRED_RESULT|'
        r'extern|constexpr|inline)\s+)*Q_(?:CORE|GUI|WIDGETS)_EXPORT\b'
        r'[^;{(=]*?\b([A-Za-z_]\w*)\s*(?:\(|;|=|\[)', re.M)
    found = set()  # type: Set[str]
    for headerPath in self.getHeaderPaths():
      with open(headerPath, errors='replace') as file:
        found.update(marked.findall(file.read()))
    return frozenset(found)

  def getPartName(self) -> str:
    """
    Gives the part of Qt this object reads, as 'QtCore'.

    Provided by you, through 'setPartName'. Nothing fills it in for you.

    Raises
    ------

    MissingVariable
      'setPartName' has not been called.
    """
    if self.__part_name__ is None:
      raise MissingVariable(self, '__part_name__', str)
    return self.__part_name__

  def getWorkFolder(self) -> str:
    """
    Gives the folder readings are kept in.

    Provided by you, through 'setWorkFolder'. Nothing fills it in for
    you.

    Raises
    ------

    MissingVariable
      'setWorkFolder' has not been called.
    """
    if self.__work_folder__ is None:
      raise MissingVariable(self, '__work_folder__', str)
    return self.__work_folder__

  def getPartFolder(self) -> str:
    """
    Gives the folder holding the header files of the part, as
    '/some/folder/headers/QtCore'.

    Found for you: the folder named as the part in the folder the
    'HeaderFolder' made.

    Raises
    ------

    LookupError
      That folder has no folder of that name, so Qt's source has no
      such part.
    """
    partFolder = os.path.join(self.getQtHeaderFolder(), self.getPartName())
    if not os.path.isdir(partFolder):
      infoSpec = """Qt's source has no part named '%s':
      there is no folder '%s'."""
      info = infoSpec % (self.getPartName(), partFolder)
      raise LookupError(' '.join(info.split()))
    return partFolder

  def getHeaderPaths(self) -> Paths:
    """
    Gives the full path of every header file of the part.

    Found for you: every file ending in '.h' that lies right in the
    folder of the part, in alphabetical order. The folders inside it are
    left alone; they hold Qt's private headers.

    Returns
    -------

    Paths
      A 'Tuple[str, ...]'. For 'QtCore' of Qt 6.12.0 it holds 286.
    """
    partFolder = self.getPartFolder()
    found = sorted(
        os.path.join(partFolder, name) for name in os.listdir(partFolder)
        if name.endswith('.h')
        and os.path.isfile(os.path.join(partFolder, name))
    )
    if self.hasPrivate():
      #  Qt calls these private. That is no concern of cutienator.
      privateFolder = self.getPrivateFolder()
      found.extend(sorted(
          os.path.join(privateFolder, name)
          for name in os.listdir(privateFolder)
          if name.endswith('.h')
          and os.path.isfile(os.path.join(privateFolder, name))
      ))
    return (*found,)

  def hasPrivate(self) -> bool:
    """Says whether the headers Qt calls private are read as well;
    'setPrivate' says so."""
    return True if self.__with_private__ else False

  def getPrivateFolder(self) -> str:
    """
    Gives the folder of the headers of the part that Qt calls private,
    as '/usr/include/qt6/QtWidgets/6.12.0/QtWidgets/private'.
    """
    partName = self.getPartName()
    return os.path.join(
        self.getPartFolder(), self.getQtVersion(), partName, 'private')

  def getPrivateIncludeFolders(self) -> Paths:
    """
    Gives the folders the compiler has to look in beside the header
    folder for a header Qt calls private to be read: such a header
    pulls others in as '"qglobal.h"', as '<private/qobject_p.h>' and
    as '<QtCore/private/qobject_p.h>'. For each part of Qt that has
    such headers it is four folders, as '/usr/include/qt6/QtCore',
    '/usr/include/qt6/QtCore/6.12.0',
    '/usr/include/qt6/QtCore/6.12.0/QtCore' and the folder 'private'
    in that one, for a file of Qt's source that names such a header
    barely, as '"qlistwidget_p.h"'.
    """
    headerFolder, version = self.getQtHeaderFolder(), self.getQtVersion()
    found = []
    for name in sorted(os.listdir(headerFolder)):
      folder = os.path.join(headerFolder, name, version)
      if os.path.isdir(os.path.join(folder, name)):
        found.append(os.path.join(headerFolder, name))
        found.append(folder)
        found.append(os.path.join(folder, name))
        found.append(os.path.join(folder, name, 'private'))
    #  Some of those headers name 'qplatformdefs.h', which Qt keeps
    #  with what it knows of the system and the compiler it is built
    #  for, in its source as 'mkspecs/linux-g++'.
    found.append(self.getHeaderFolder().getSpecFolder())
    return (*found,)

  def getCompilerCommand(self) -> Tuple[str, ...]:
    """
    Gives the start of every 'clang++' command this class runs.

    Found for you. Each run adds what it wants done to it.

    Returns
    -------

    Tuple[str, ...]
      One argument per entry: 'clang++', then
      '-x c++ -std=c++17', to read C++ of the 2017 standard;
      '-fPIC', which Qt's headers insist on;
      '-I' with the folder of Qt's headers.
    """
    private = ()  # type: Tuple[str, ...]
    if self.hasPrivate():
      private = (*('-I%s' % f for f in self.getPrivateIncludeFolders()),)
    return (
        'clang++', '-x', 'c++', '-std=c++17', '-fPIC',
        '-I%s' % self.getQtHeaderFolder(), *private,
    )

  def getReadingFolder(self) -> str:
    """
    Gives the folder of the reading of this part: the folder named as
    the part in the work folder.

    Found for you. Having the path does not mean a reading is there;
    'isRead' says whether one is.
    """
    return os.path.join(self.getWorkFolder(), self.getPartName())

  def getStampFile(self) -> str:
    """
    Gives the path of the stamp of the reading: 'reading.json' in the
    folder of the reading.

    Found for you. The stamp is written last, so a reading with a stamp
    is a finished one.
    """
    return os.path.join(self.getReadingFolder(), 'reading.json')

  def isRead(self) -> bool:
    """
    Says whether a finished reading of the part, made from the Qt that
    is installed now, is in the work folder.

    When it is False, call 'read'.
    """
    stampFile = self.getStampFile()
    if not os.path.isfile(stampFile):
      return False
    with open(stampFile) as file:
      stamp = json.load(file)
    return stamp.get('qtVersion') == self.getQtVersion()

  def getStamp(self) -> Dict[str, Any]:
    """
    Gives what the stamp of the reading says.

    Written for you by 'read', and loaded here.

    Returns
    -------

    Dict[str, Any]
      'partName' and 'qtVersion': what was read, from which Qt.
      'compiler': the version of the compiler that read it.
      'feed': the lines of C++ the compiler was handed.
      'seconds': how long the reading took.
      'topLevelThings': how many the compiler reported in all.
      'keptRecords': how many of those lie in a header file of the part.
      'withoutPlace': how many lie nowhere; the compiler made those up.
      'inOtherFiles': how many lie in files of other parts, or outside
      Qt. Those are passed over.
      'compilerSaid': warnings of the compiler, '' for none.
      'headerFiles': for each header file by its name, whether it was
      'read', how many 'records' it gave and, when the compiler refused
      it, its 'complaint'.

    Raises
    ------

    FileNotFoundError
      The part has not been read into the work folder.

    RuntimeError
      The reading was made from another version of Qt than the one
      installed now, or of other header files than the part has now.
    """
    stampFile = self.getStampFile()
    partName = self.getPartName()
    if not os.path.isfile(stampFile):
      infoSpec = """The part '%s' has not been read into '%s'. Call
      'read' first."""
      info = infoSpec % (partName, self.getWorkFolder())
      raise FileNotFoundError(' '.join(info.split()))
    with open(stampFile) as file:
      stamp = json.load(file)
    qtVersion = self.getQtVersion()
    if stamp.get('qtVersion') != qtVersion:
      infoSpec = """The reading of '%s' in '%s' was made from Qt %s, and
      Qt is now %s. Call 'read' again."""
      info = infoSpec % (
          partName, self.getReadingFolder(), stamp.get('qtVersion'),
          qtVersion,
      )
      raise RuntimeError(' '.join(info.split()))
    names = sorted(os.path.basename(path) for path in self.getHeaderPaths())
    if sorted(stamp.get('headerFiles', ())) != names:
      infoSpec = """The reading of '%s' in '%s' was made of other header
      files than the part has now. Call 'read' again."""
      info = infoSpec % (partName, self.getReadingFolder())
      raise RuntimeError(' '.join(info.split()))
    return stamp

  def _createHeaderFiles(self, ) -> None:
    """Makes one 'HeaderFile' per header file from the stamp."""
    stamp = self.getStamp()
    partFolder = self.getPartFolder()
    readingFolder = self.getReadingFolder()
    headerFiles = []
    for name, entry in sorted(stamp['headerFiles'].items()):
      headerFile = HeaderFile()
      headerPath = os.path.join(partFolder, name)
      if not os.path.isfile(headerPath) and self.hasPrivate():
        headerPath = os.path.join(self.getPrivateFolder(), name)
      headerFile.setHeaderPath(headerPath)
      recordPath = os.path.join(readingFolder, '%s.jsonl' % name)
      headerFile.setRecordPath(recordPath)
      headerFile.setRead(entry['read'])
      headerFile.setComplaint(entry['complaint'])
      headerFile.setRecordCount(entry['records'])
      headerFiles.append(headerFile)
    self.__header_files__ = (*headerFiles,)

  def getHeaderFiles(self, **kwargs) -> HeaderFiles:
    """
    Gives one 'HeaderFile' per header file of the part, in alphabetical
    order. Iterate through them and ask each for its contents.

    Made for you from the reading in the work folder. Nothing is read
    again and no records are loaded until a 'HeaderFile' is asked for
    its contents. You pass nothing; the keyword is for the method's own
    use.

    Returns
    -------

    HeaderFiles
      A 'Tuple[HeaderFile, ...]'. For 'QtCore' of Qt 6.12.0 it holds
      286.

    Raises
    ------

    FileNotFoundError
      The part has not been read into the work folder. Call 'read'.

    RuntimeError
      The reading was made from another Qt than the one installed now.
      Call 'read' again.
    """
    if self.__header_files__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      self._createHeaderFiles()
      return self.getHeaderFiles(_recursion=True)
    return self.__header_files__

  def _createOfferedNames(self, ) -> None:
    """Asks the program 'nm' what the Qt shared object of the part offers."""
    sharedObject = self.getQtSharedObject()
    listed = self._run('nm', '-D', '--defined-only', sharedObject)
    offered = set()
    for line in listed.splitlines():
      words = line.split()
      if len(words) >= 3:
        offered.add(words[-1].partition('@')[0])
    self.__offered_names__ = frozenset(offered)

  def getOfferedNames(self, **kwargs) -> FrozenSet[str]:
    """
    Gives the name of everything the Qt shared object of the part offers
    to others, each as the compiler names it: '_ZNK7QObject6threadEv'
    for 'QObject::thread() const'.

    Found for you, at the first call, by the program 'nm', and kept. You
    pass nothing; the keyword is for the method's own use.

    A function that a header only declares can be called only when a
    shared object offers it. Qt's headers declare a few that none
    offers, as 'QEvent::qt_check_for_QGADGET_macro()'.

    Returns
    -------

    FrozenSet[str]
      The names. For 'QtCore' of Qt 6.12.0 it holds several thousand.

    Raises
    ------

    FileNotFoundError
      The program 'nm' is not installed.
    """
    if self.__offered_names__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      self._createOfferedNames()
      return self.getOfferedNames(_recursion=True)
    return self.__offered_names__

  def _createNamedHeaderPaths(self, ) -> None:
    """Finds the header files of the part that a line names outright."""
    partName = self.getPartName()
    ownList = os.path.join(self.getPartFolder(), partName)
    lines = self.getStamp()['feed'].splitlines()
    if os.path.isfile(ownList):
      with open(ownList) as file:
        lines.extend(file.read().splitlines())
    headerFolder = self.getQtHeaderFolder()
    named = set()
    for line in lines:
      match = self.__include_line__.match(line.strip())
      if match is not None:
        named.add(os.path.join(headerFolder, match.group(1)))
    named = (*(p for p in self.getHeaderPaths() if p in named),)
    if os.path.isfile(ownList) and not named:
      infoSpec = """The own list of the part '%s', the file '%s', names
      none of the header files of the part. Lines such as '#include
      <%s/name.h>' were expected in it."""
      info = infoSpec % (partName, ownList, partName)
      raise RuntimeError(' '.join(info.split()))
    self.__named_header_paths__ = named

  def getNamedHeaderPaths(self, **kwargs) -> Paths:
    """
    Gives the header files of the part that are meant to be pulled in by
    a line of their own, in alphabetical order.

    Found for you, at the first call, and kept: the header files that a
    line of the part's own list names, and those the reading pulled in
    by a line of their own on top of that list. You pass nothing; the
    keyword is for the method's own use.

    A header file of the part that is not among them is reached through
    another header file only. Some of those refuse to be pulled in
    alone: 'qobjectdefs_impl.h' stops the compiler with 'Do not include
    qobjectdefs_impl.h directly'.

    Returns
    -------

    Paths
      A 'Tuple[str, ...]' of full paths. For 'QtCore' of Qt 6.12.0 it
      holds 255 of the 286 header files.

    Raises
    ------

    FileNotFoundError
      The part has not been read into the work folder. Call 'read'.

    RuntimeError
      The own list of the part names none of its header files.
    """
    if self.__named_header_paths__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      self._createNamedHeaderPaths()
      return self.getNamedHeaderPaths(_recursion=True)
    return self.__named_header_paths__

  def getIncludeLines(self, headerPath: str) -> str:
    """
    Gives the lines of C++ that pull one header file of the part in, for
    a file of ours that needs what the header file declares.

    Found for you. For a header file among 'getNamedHeaderPaths' it is
    the one line naming it, as '#include <QtCore/qobject.h>'. For any
    other it is the one line naming the nearest header file among
    'getNamedHeaderPaths' that pulled it in when the part was read:
    'QtGui/qaccessible_base.h' is named by no line and pulled in by
    'QtGui/qaccessible.h', so its line is '#include
    <QtGui/qaccessible.h>'.

    It is never every line the reading handed the compiler. Those name
    header files that only some systems have, as
    'QtGui/qvulkaninstance.h', which Qt's package for macOS lacks, and a
    file of ours has to compile on every system.

    Parameters
    ----------

    headerPath : str
      The full path of a header file of the part, as 'getHeaderPaths'
      gives it.

    Returns
    -------

    str
      The lines, each ending in a line break.

    Raises
    ------

    LookupError
      The part has no header file at that path, or no record of the
      reading says which named header file pulled it in.
    """
    if headerPath not in self.getHeaderPaths():
      infoSpec = """The part '%s' has no header file at '%s'."""
      info = infoSpec % (self.getPartName(), headerPath)
      raise LookupError(' '.join(info.split()))
    named = self.getNamedHeaderPaths()
    reached, passed = headerPath, []  # type: str, List[str]
    while reached not in named:
      passed.append(reached)
      reached = self._findPuller(reached)
      if reached is None or reached in passed:
        infoSpec = """No line names the header file '%s' of the part
        '%s', and the records of the reading do not lead from it to a
        header file that a line names: they lead through %s."""
        info = infoSpec % (headerPath, self.getPartName(), passed)
        raise LookupError(' '.join(info.split()))
    if reached in self._getOwnListPaths():
      return self._getIncludeLine(reached)
    #  A header file the own list of the part does not name was read on
    #  top of that list, and may need what the list pulls in: most of
    #  the headers Qt calls private do.
    partName = self.getPartName()
    ownLine = '#include <%s/%s>\n' % (partName, partName)
    return '%s%s' % (ownLine, self._getIncludeLine(reached))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setPartName(self, partName: str) -> None:
    """
    Tells which part of Qt to read.

    Required. Calling it again makes this object stand for another part.

    Parameters
    ----------

    partName : str
      The part by Qt's own name, which is the name of its folder in
      Qt's header folder, as 'QtCore', 'QtGui' or 'QtWidgets'.

    Raises
    ------

    TypeException
      'partName' is not text.

    ValueError
      'partName' is empty, or is a path and not a name.
    """
    if not isinstance(partName, str):
      raise TypeException('partName', partName, str)
    if not partName or os.path.basename(partName) != partName:
      infoSpec = """The name of a part of Qt is one word, as 'QtCore',
      but received '%s'."""
      raise ValueError(' '.join((infoSpec % partName).split()))
    self.__part_name__ = partName
    self.__header_files__ = None
    self.__named_header_paths__ = None
    self.__offered_names__ = None
    self.__found_pullers__ = None

  def setPrivate(self, withPrivate: bool) -> None:
    """
    Tells whether the headers Qt calls private are read as well, and
    the classes in them count as classes of the part.

    Optional; without it they are left alone. Set it before the part is
    read or asked anything.
    """
    self.__with_private__ = True if withPrivate else False
    self.__header_files__ = None
    self.__named_header_paths__ = None

  def setLeftOutHeaders(self, reason: str, *names: str) -> None:
    """
    Tells 'read' to leave some header files of the part unread, and
    why. The reading notes each as not read, with the reason, as it
    notes a header file the compiler refused.

    Optional, and only 'read' goes by it. It is for what cannot be
    seen from one machine: Qt's package for one system holds header
    files its packages for the others lack, as
    'qeventdispatcher_glib_p.h', and no class of such a file can be in
    a package that has to compile on every system. Some of them pull
    in files of the system whose words break Qt's own header files
    read after them. No record of such a file is kept, also when a
    header file that is read pulls it in, so the tree knows no class
    of it. Calling this again replaces what was told before.

    Parameters
    ----------

    reason : str
      Why they are left out, as it is to stand in the reading.

    *names : str
      The names of the header files, as 'qeventdispatcher_glib_p.h'.

    Raises
    ------

    TypeException
      The reason or a name is not text.
    """
    if not isinstance(reason, str):
      raise TypeException('reason', reason, str)
    for name in names:
      if not isinstance(name, str):
        raise TypeException('name', name, str)
    self.__left_out_headers__ = {name: reason for name in names}

  def getLeftOutHeaders(self) -> Dict[str, str]:
    """Gives the header files 'read' is told to leave unread, each by
    its name with the reason; 'setLeftOutHeaders' provides them. It is
    empty when nothing was told."""
    return dict(self.__left_out_headers__ or dict())

  def setWorkFolder(self, workFolder: str) -> None:
    """
    Tells where readings are kept.

    Required. One work folder serves every part: each reading gets a
    folder of its own in it, named as the part. Calling this again
    replaces the folder given before.

    Parameters
    ----------

    workFolder : str
      The path of a folder that exists. A path may be relative to where
      Python was started; it is kept in full. A reading of 'QtCore'
      fills about 250 MB.

    Raises
    ------

    TypeException
      'workFolder' is not text.

    FileNotFoundError
      There is no folder at the path.
    """
    if not isinstance(workFolder, str):
      raise TypeException('workFolder', workFolder, str)
    workFolder = os.path.abspath(workFolder)
    if not os.path.isdir(workFolder):
      infoSpec = """There is no folder at '%s'."""
      raise FileNotFoundError(infoSpec % workFolder)
    self.__work_folder__ = workFolder
    self.__header_files__ = None
    self.__named_header_paths__ = None

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __str__(self) -> str:
    """Says which part this is and which setters are still to be called."""
    clsName = type(self).__name__
    unset = [
        setter for setter, value in (
            ('setPartName', self.__part_name__),
            ('setWorkFolder', self.__work_folder__),
        ) if value is None
    ]
    if unset:
      infoSpec = """<%s still waiting for: %s>"""
      return infoSpec % (clsName, ', '.join(unset))
    infoSpec = """<%s '%s' kept in '%s'>"""
    return infoSpec % (clsName, self.__part_name__, self.__work_folder__)

  __repr__ = __str__

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _getOwnListPaths(self) -> FrozenSet[str]:
    """Gives the header files the own list of the part names outright,
    as 'QtCore/QtCore' names 'QtCore/qobject.h'. A part without such a
    list has none."""
    if self.__own_list_paths__ is None:
      partName = self.getPartName()
      ownList = os.path.join(self.getPartFolder(), partName)
      headerFolder, found = self.getQtHeaderFolder(), set()
      if os.path.isfile(ownList):
        with open(ownList) as file:
          for line in file.read().splitlines():
            match = self.__include_line__.match(line.strip())
            if match is not None:
              found.add(os.path.join(headerFolder, match.group(1)))
      self.__own_list_paths__ = frozenset(found)
    return self.__own_list_paths__

  def _findPuller(self, headerPath: str) -> Optional[str]:
    """
    Gives the path of the file that pulled a header file of the part in
    when the part was read, as the compiler wrote it down beside the
    first place it names in that header file, or None when the header
    file is none of the part or no record says.
    """
    if self.__found_pullers__ is None:
      self.__found_pullers__ = dict()
    if headerPath in self.__found_pullers__:
      return self.__found_pullers__[headerPath]
    found = None  # type: Optional[str]
    for headerFile in self.getHeaderFiles():
      if headerFile.getHeaderPath() != headerPath:
        continue
      if not headerFile.wasRead():
        break
      waiting = [*headerFile.getContents()]  # type: List[Any]
      while waiting and found is None:
        node = waiting.pop()
        if isinstance(node, list):
          waiting.extend(node)
        elif isinstance(node, dict):
          if node.get('file') == headerPath and 'includedFrom' in node:
            found = node['includedFrom'].get('file')
          else:
            waiting.extend(node.values())
      break
    self.__found_pullers__[headerPath] = found
    return found

  def _getIncludeLine(self, headerPath: str) -> str:
    """Gives the line of C++ that pulls one header file in."""
    relative = os.path.relpath(headerPath, self.getQtHeaderFolder())
    return '#include <%s>\n' % relative

  def _runCompiler(self, feed: str, *arguments: str) -> Any:
    """
    Hands the compiler some lines of C++ and gives how the run went.

    Parameters
    ----------

    feed : str
      The lines of C++ for the compiler to read.

    *arguments : str
      What to add to the start of the command, saying what to do.

    Returns
    -------

    Any
      The finished run, a 'subprocess.CompletedProcess'. A run the
      compiler refused is given too, not raised.

    Raises
    ------

    FileNotFoundError
      'clang++' is not installed.
    """
    command = (*self.getCompilerCommand(), *arguments, '-')
    try:
      return subprocess.run(
          command, input=feed, capture_output=True, text=True,
      )
    except FileNotFoundError as fileNotFoundError:
      infoSpec = """The program 'clang++' is needed and is not
      installed."""
      info = ' '.join(infoSpec.split())
      raise FileNotFoundError(info) from fileNotFoundError

  def _listFilesRead(self, feed: str) -> Set[str]:
    """
    Gives every file the compiler reads when handed some lines of C++,
    each as its real path. This run only follows the '#include' lines,
    which takes about a second.

    Raises
    ------

    RuntimeError
      The compiler refused the lines, or its list of files could not be
      made sense of.
    """
    if not feed:
      return set()
    done = self._runCompiler(feed, '-M')
    if done.returncode:
      infoSpec = """The compiler could not follow the '#include' lines
      of the part '%s': %s"""
      info = infoSpec % (self.getPartName(), done.stderr.strip())
      raise RuntimeError(info)
    filesRead = set()
    for word in done.stdout.replace('\\\n', ' ').split()[1:]:
      if not os.path.isfile(word):
        infoSpec = """The compiler listed '%s' among the files it read,
        and there is no such file."""
        raise RuntimeError(' '.join((infoSpec % word).split()))
      filesRead.add(os.path.realpath(word))
    return filesRead

  def _findComplaint(
      self,
      feed: str,
      known: str = '',
      *arguments: str,
  ) -> str:
    """
    Has the compiler read some lines of C++ without writing anything
    down, and gives what it complained about, or '' when it took them
    without a word.

    A header file may say by a '#warning' line of its own that it is
    not to be pulled in, as 'qstringconverter_base_deprecated.h' does.
    The compiler reads it all the same and passes the words on. Those
    words count as a complaint here, so such a header file is left out
    of the reading, and every file of ours compiles without them.

    Parameters
    ----------

    feed : str
      The lines of C++ for the compiler to read.

    known : str
      What the compiler says of the lines the feed begins with, which
      is no complaint about the line added to them.

    *arguments : str
      What more to tell the compiler, as '-include-pch' and the path of
      a precompiled header for the lines to stand on.
    """
    done = self._runCompiler(feed, *arguments, '-fsyntax-only')
    if done.returncode:
      return done.stderr.strip() or 'The compiler refused it wordlessly.'
    knownLines = known.splitlines()
    warned = [
        line for line in done.stderr.splitlines()
        if '[-W#warnings]' in line and line not in knownLines
    ]
    return '\n'.join(warned)

  def _planFeed(self) -> Tuple[str, Dict[str, str]]:
    """
    Works out the lines of C++ to hand the compiler, so that it reads as
    many of the header files as can be read.

    The own list of the part comes first. Each header file the own list
    does not reach is then tried on top of it, alone. Those the compiler
    takes without a word are added. Those it refuses are tried once
    more on top of everything added so far: a header file may lean on
    another without pulling it in, as 'qfusionstyle_p_p.h' leans on
    'qfusionstyle_p.h'. That goes on until a round adds none. What is
    still refused then is left out, with what the compiler said, and so
    are the header files that warn for being pulled in, and those
    'setLeftOutHeaders' named.

    The compiler reads the lines so far once in each round, and writes
    down what it made of them, as a precompiled header in the work
    folder. Every trial of the round starts from that, so a trial costs
    the reading of one header file and not of the whole part. The
    precompiled header is removed when the round is over.

    Returns
    -------

    Tuple[str, Dict[str, str]]
      The lines of C++, and why each header file is left out, by the
      path of the header file.

    Raises
    ------

    RuntimeError
      The compiler refused the lines so far, which it had taken one by
      one. The message holds what it said.
    """
    partName = self.getPartName()
    feed = ''
    if os.path.isfile(os.path.join(self.getPartFolder(), partName)):
      feed = '#include <%s/%s>\n' % (partName, partName)
    filesRead = self._listFilesRead(feed)
    toldLeftOut = self.getLeftOutHeaders()
    complaints = dict()  # type: Dict[str, str]
    leftOut = []  # type: List[str]
    for headerPath in self.getHeaderPaths():
      if os.path.realpath(headerPath) in filesRead:
        continue
      name = os.path.basename(headerPath)
      if name in toldLeftOut:
        complaints[headerPath] = toldLeftOut[name]
      else:
        leftOut.append(headerPath)
    while leftOut:
      with tempfile.TemporaryDirectory(dir=self.getWorkFolder()) as folder:
        feedHeader = os.path.join(folder, 'feed.pch')
        made = self._runCompiler(
            feed, '-x', 'c++-header', '-fpch-instantiate-templates',
            '-o', feedHeader)
        if made.returncode:
          infoSpec = """The compiler refused the header files of the
          part '%s' read together, which it took one by one: %s"""
          info = infoSpec % (partName, made.stderr[:1200])
          raise RuntimeError(' '.join(info.split()))

        def findComplaint(headerPath: str) -> str:
          return self._findComplaint(
              self._getIncludeLine(headerPath), '', '-include-pch',
              feedHeader)

        with ThreadPoolExecutor(max_workers=os.cpu_count() or 1) as pool:
          said = (*pool.map(findComplaint, leftOut),)
      refused = []
      for headerPath, complaint in zip(leftOut, said):
        if complaint:
          complaints[headerPath] = complaint
          refused.append(headerPath)
        else:
          complaints.pop(headerPath, None)
          feed += self._getIncludeLine(headerPath)
      if len(refused) == len(leftOut):
        break
      leftOut = refused
    return feed, complaints

  def _cutReport(
      self,
      feed: str,
      tally: Dict[str, Any],
  ) -> Iterator[Tuple[str, Record]]:
    """
    Has the compiler read the lines of C++ and write down everything it
    read, and cuts that report into records while it is being written.

    The report of one part is one to four gigabytes of text, mostly
    about files that are not Qt's. It is never held whole: each line is
    looked at once, and only the top-level things lying in a header
    file of the part are kept.

    Parameters
    ----------

    feed : str
      The lines of C++ for the compiler to read.

    tally : Dict[str, Any]
      Filled in while cutting: 'topLevelThings', 'keptRecords',
      'withoutPlace' and 'inOtherFiles' count the top-level things, and
      'compilerSaid' holds the warnings of the compiler.

    Returns
    -------

    Iterator[Tuple[str, Record]]
      For each kept top-level thing, the path of the header file it
      lies in and its record, with every place filled in.

    Raises
    ------

    FileNotFoundError
      'clang++' is not installed.

    RuntimeError
      The compiler refused the lines, or the report is not laid out the
      way this method expects.
    """
    #  A header file 'setLeftOutHeaders' named gives no record, also
    #  when another header file pulls it in.
    toldLeftOut = self.getLeftOutHeaders()
    wanted = {
        os.path.realpath(path): path for path in self.getHeaderPaths()
        if os.path.basename(path) not in toldLeftOut
    }
    realPaths = dict()  # type: Dict[str, str]
    thingOpens = self.__thing_opens__
    thingCloses = self.__thing_closes__
    placeOpens = self.__place_opens__
    placeEmpty = self.__place_empty__
    placeCloses = self.__place_closes__
    includedFrom = self.__included_from__
    fileKey, lineKey = self.__file_key__, self.__line_key__
    fillPlaces, getPlace = self._fillPlaces, self._getPlace
    for key in ('topLevelThings', 'keptRecords', 'withoutPlace',
                'inOtherFiles'):
      tally[key] = 0
    command = (
        *self.getCompilerCommand(), '-fsyntax-only',
        '-Xclang', '-ast-dump=json', '-',
    )
    #  The file and line of the place the compiler wrote last, tracked
    #  the way the compiler tracks them itself.
    lastFile, lastLine = None, None
    namesNoPlace = False
    #  The lines of the thing being read, or None between two things.
    thing = None  # type: Optional[List[bytes]]
    #  0: its place is not known yet, 1: it is kept, 2: it is passed over
    fate = 0
    placeOpen = False
    before = (None, None)  # type: Place
    where = (None, None)  # type: Place
    headerPath = ''
    with tempfile.TemporaryFile() as complaints:
      try:
        compiler = subprocess.Popen(
            command, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
            stderr=complaints, bufsize=1 << 20,
        )
      except FileNotFoundError as fileNotFoundError:
        infoSpec = """The program 'clang++' is needed and is not
        installed."""
        info = ' '.join(infoSpec.split())
        raise FileNotFoundError(info) from fileNotFoundError
      try:
        compiler.stdin.write(feed.encode())
        compiler.stdin.close()
        for line in compiler.stdout:
          if namesNoPlace:
            namesNoPlace = False
          elif b'"file": ' in line:
            match = fileKey.match(line)
            if match:
              lastFile = json.loads(match.group(1))
          elif b'"line": ' in line:
            match = lineKey.match(line)
            if match:
              lastLine = int(match.group(1))
          elif line.endswith(includedFrom):
            namesNoPlace = True
          if thing is None:
            if line == thingOpens:
              thing, fate, placeOpen = [line], 0, False
              before = (lastFile, lastLine)
              tally['topLevelThings'] += 1
            continue
          if fate == 2:
            if line in thingCloses:
              thing = None
            continue
          thing.append(line)
          if fate == 0:
            if line == placeEmpty:
              fate = 2
              tally['withoutPlace'] += 1
            elif line == placeOpens:
              placeOpen = True
            elif placeOpen and line == placeCloses:
              if lastFile is None:
                infoSpec = """The compiler gave a place before it named
                any file."""
                raise RuntimeError(' '.join(infoSpec.split()))
              if lastFile not in realPaths:
                realPaths[lastFile] = os.path.realpath(lastFile)
              headerPath = wanted.get(realPaths[lastFile], '')
              if headerPath:
                fate, where = 1, (lastFile, lastLine)
              else:
                fate = 2
                tally['inOtherFiles'] += 1
            continue
          if line not in thingCloses:
            continue
          record = json.loads(b''.join(thing).rstrip(b',\n'))
          lastPlace = [before[0], before[1]]
          fillPlaces(record, lastPlace)
          if (lastPlace[0], lastPlace[1]) != (lastFile, lastLine):
            infoSpec = """Lost track of the places in the report of the
            compiler, at '%s' line %s."""
            info = infoSpec % (lastFile, lastLine)
            raise RuntimeError(' '.join(info.split()))
          if getPlace(record) != where:
            infoSpec = """A record cut from the report of the compiler
            does not stand where it was found, at '%s' line %s."""
            raise RuntimeError(' '.join((infoSpec % where).split()))
          tally['keptRecords'] += 1
          thing = None
          yield headerPath, record
        returnCode = compiler.wait()
      finally:
        if compiler.poll() is None:
          compiler.kill()
          compiler.wait()
        compiler.stdout.close()
      complaints.seek(0)
      said = complaints.read().decode(errors='replace').strip()
    if returnCode:
      infoSpec = """The compiler could not read the header files of the
      part '%s': %s"""
      raise RuntimeError(infoSpec % (self.getPartName(), said))
    if thing is not None:
      infoSpec = """The report of the compiler ended in the middle of a
      top-level thing."""
      raise RuntimeError(' '.join(infoSpec.split()))
    tally['compilerSaid'] = said

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def read(self) -> None:
    """
    Reads every header file of the part, from scratch, and puts the
    reading in the work folder.

    This is the one compiler run that writes everything down. It takes
    two to three minutes for a part as big as 'QtCore'. Nothing of an
    earlier reading is used. An earlier reading is replaced at the very
    end, and only when this one finished and every check passed.

    The checks: the compiler ended without an error; every record
    stands in the header file and on the line it was found at; and
    every header file of the part is accounted for, as read or as
    refused with what the compiler said.

    Raises
    ------

    MissingVariable
      'setHeaderFolder', 'setPartName' or 'setWorkFolder' has not been
      called.

    LookupError
      Qt's source has no such part, or the part has no header files.

    FileNotFoundError
      'clang++' is not installed.

    RuntimeError
      The compiler refused the header files, a check did not pass, or
      the work folder holds a folder named as the part that this class
      did not make. The message says which.
    """
    began = time.time()
    partName = self.getPartName()
    readingFolder = self.getReadingFolder()
    if os.path.exists(readingFolder) and not os.path.isfile(
        self.getStampFile()):
      infoSpec = """'%s' is there already and is no reading made by this
      class, so it is not replaced. Move it, or set another work
      folder."""
      raise RuntimeError(' '.join((infoSpec % readingFolder).split()))
    headerPaths = self.getHeaderPaths()
    if not headerPaths:
      infoSpec = """The part '%s' has no header files in '%s'."""
      info = infoSpec % (partName, self.getPartFolder())
      raise LookupError(info)
    feed, complaints = self._planFeed()
    filesRead = self._listFilesRead(feed)
    version = self._run('clang++', '--version').splitlines()[0]

    unfinished = '%s.unfinished' % readingFolder
    if os.path.isdir(unfinished):
      shutil.rmtree(unfinished)
    os.mkdir(unfinished)
    finished = False
    try:
      tally = dict()  # type: Dict[str, Any]
      counts = {headerPath: 0 for headerPath in headerPaths}
      for headerPath, record in self._cutReport(feed, tally):
        name = '%s.jsonl' % os.path.basename(headerPath)
        with open(os.path.join(unfinished, name), 'a') as file:
          file.write(json.dumps(record, separators=(',', ':')))
          file.write('\n')
        counts[headerPath] += 1
      entries = dict()
      toldLeftOut = self.getLeftOutHeaders()
      for headerPath in headerPaths:
        wasRead = os.path.realpath(headerPath) in filesRead
        if os.path.basename(headerPath) in toldLeftOut:
          #  Pulled in by another header file or not: none of its
          #  records was kept.
          wasRead = False
          complaints[headerPath] = toldLeftOut[os.path.basename(headerPath)]
        if not wasRead and headerPath not in complaints:
          infoSpec = """The header file '%s' was neither read nor
          refused by the compiler."""
          raise RuntimeError(' '.join((infoSpec % headerPath).split()))
        entries[os.path.basename(headerPath)] = dict(
            read=wasRead, records=counts[headerPath],
            complaint=complaints.get(headerPath, ''),
        )
      stamp = dict(
          partName=partName, qtVersion=self.getQtVersion(),
          compiler=version, feed=feed,
          seconds=round(time.time() - began, 1), **tally,
          headerFiles=entries,
      )
      with open(os.path.join(unfinished, 'reading.json'), 'w') as file:
        json.dump(stamp, file, indent=2)
      finished = True
    finally:
      if not finished:
        shutil.rmtree(unfinished)
    previous = '%s.previous' % readingFolder
    if os.path.isdir(previous):
      shutil.rmtree(previous)
    if os.path.isdir(readingFolder):
      os.rename(readingFolder, previous)
    os.rename(unfinished, readingFolder)
    if os.path.isdir(previous):
      shutil.rmtree(previous)
    self.__header_files__ = None
