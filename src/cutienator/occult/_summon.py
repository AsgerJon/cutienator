"""Summon compiles ritual files into one shared object."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
import threading
from concurrent.futures import ThreadPoolExecutor
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

from . import System
from ._exorcist import Exorcist

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, Optional, Tuple

  Paths = Tuple[str, ...]


class Summon:
  """
  Compiles ritual files into one shared object by running 'clang++'.

    build = Summon()
    build.setRitualFiles('/here/q_object.cpp', '/here/q_byte_array.cpp')
    build.setTargetFile('/here/libexample.so')
    build.setQtSharedObjects('/usr/lib/libQt6Core.so.6')
    build.run()

  Terms
  -----

  - A ritual is one function of ours that Python can call, and that
    calls one Qt function, as 'QObject::parent()'.
  - A ritual file is a C++ file we write, holding rituals. It is named
    for what it provides, not for the language it is written in.
  - The target file is the one shared object the build writes. It
    offers every ritual of the ritual files.
  - An object file is what 'clang++' makes of one ritual file by
    itself. The object files are then joined into the target file.
    They are kept, in the object folder, from one build to the next.
  - The common header is one header the build writes: every '#include'
    line of the ritual files, each once.
  - The precompiled header is what 'clang++' makes of the common header
    by reading it once. Each ritual file is compiled with it, and so
    reads none of Qt's headers again. Reading them is nine tenths of
    the work of compiling a ritual file.
  - A Qt shared object is one of Qt's own compiled files, which the
    rituals call into.

  You provide
  -----------

  Three things, each through its own setter, in any order. All three are
  required before 'run'.

  - 'setRitualFiles': the ritual files to compile.
  - 'setTargetFile': the target file to write.
  - 'setQtSharedObjects': the Qt shared objects the rituals call into.

  Two more are optional:

  - 'setComponents': the parts of Qt the ritual files are of, as 'QtCore'.
    With it 'clang++' also looks in the folders of the headers Qt calls
    private, which a ritual file may name; see
    'getPrivateIncludeFolders'.
  - 'setStaticDependencies': what a static library of Qt among the Qt
    shared objects needs beside it on the line that joins the target
    file, as 'System.readStaticDependencies' reads it.

  Found for you
  -------------

  Three things, which have no setter. Each is asked of Qt's own program
  'qmake6' the first time it is needed, and then remembered for every
  'Summon', since Qt is installed in one place.

  - 'getQtHeaderFolder': where Qt keeps its headers.
  - 'getQtSharedObjectFolder': where Qt keeps its shared objects.
  - 'getQtProgramFolder': where Qt keeps its programs.
  - 'getQtVersion': which Qt that is, as '6.12.0'.

  Two more follow from what you provide: 'getObjectFolder', the folder
  'demons' beside the target file, and 'getJobCount', how many ritual
  files are compiled at the same time, which is as many as the machine
  has processors unless 'setJobCount' says otherwise.

  What differs between Linux, macOS and Windows is not written here. The
  build asks 'System.getHere()' for it: the name of a Qt shared object
  and some of what 'clang++' is told.

  What to expect
  --------------

  - Nothing is compiled until 'run' is called.
  - Each ritual file is compiled by itself, several at the same time,
    and only when it has to be: when it has no object file, when it
    changed after its object file was made, or when Qt or what
    'clang++' is told is no longer what it was when the object files
    were made.
  - A build that compiles any ritual file first makes the precompiled
    header, which takes some seconds, and removes it when it ends: it
    is some 60 MB, and the next build may be of other ritual files.
    The common header is kept, so that what 'clang++' says of it can
    be looked up.
  - So the first build takes those seconds and then about a fifth of a
    second for each ritual file, shared among the processors, and a
    build after one ritual file changed takes those seconds again.
  - A setter refuses a wrong value at once: one that is not text, or a
    path that leads nowhere.
  - A getter whose setter was never called raises 'MissingVariable',
    naming what is missing.
  - 'getPrecompileCommand', 'getCompileCommand' and 'getLinkCommand'
    give the exact 'clang++' commands without running them.
  - 'print(build)' lists the setters still to be called.
  - What 'clang++' refuses costs only what fails. A ritual file it
    refuses is compiled again as a copy without the items its errors
    point at, as 'Exorcist' finds them, until the copy compiles; a
    refused join of the object files leaves out what the linker named
    as needing what no library offers, and joins them again. A ritual
    that needs nothing that failed stays in the target file. What was
    left out, and why, is kept in the left-out file beside the target
    file; see 'getLeftOutFile' and 'getLeftOut'. A refused common
    header makes every ritual file compile without the precompiled
    header, by reading its own headers.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _run(*command: str) -> str:
    """
    Runs one program to its end and gives what it printed.

    Every program this class needs, 'clang++' and 'qmake6', is run through
    here, so a failure always carries the program's own message. The
    program has finished by the time this returns: nothing is left
    running, and there is nothing to close. No more programs run
    through here at the same time than the machine has processors,
    also when several builds run at once, as 'Rituals.summon' runs
    those of several parts of Qt.

    On Windows a command of 'clang++' longer than '__long_command__'
    letters is handed over in a file, as 'clang++ @file', which
    'clang++' reads as if each line stood on the command: Windows
    starts no program whose command is longer than 32767 letters, and
    the link of a part of Qt with a thousand ritual files is. Linux
    and macOS take commands of some million letters, and get theirs
    as they are, so whatever runs in the place of 'clang++' there
    sees every word.

    Parameters
    ----------

    *command : str
      The program, then each of its arguments, one per entry.

    Returns
    -------

    str
      What the program printed.

    Raises
    ------

    FileNotFoundError
      The program is not installed on this machine.

    RuntimeError
      The program ran and reported a failure; its message is included.
      Or the system did not start it, though it is installed; what the
      system said is included.
    """
    if shutil.which(command[0]) is None:
      infoSpec = """The program '%s' is needed and is not installed."""
      raise FileNotFoundError(infoSpec % command[0])
    told = None  # type: Optional[str]
    length = sum(len(word) + 3 for word in command)
    tooLong = length > Summon.__long_command__
    if tooLong and os.name == 'nt' and (
        os.path.basename(command[0]).startswith('clang')):
      #  One word to a line, between quotes, as 'clang++' reads a file
      #  of them when told '--rsp-quoting=posix', on any system.
      handle, told = tempfile.mkstemp(prefix='cutienator-', suffix='.txt')
      with os.fdopen(handle, 'w', encoding='utf-8') as file:
        for word in command[1:]:
          word = word.replace('\\', '\\\\').replace('"', '\\"')
          file.write('"%s"\n' % word)
      command = (command[0], '--rsp-quoting=posix', '@%s' % told)
    try:
      with Summon.__program_slots__:
        done = subprocess.run(command, capture_output=True, text=True)
    except OSError as osError:
      infoSpec = """The system did not start the program '%s': %s"""
      raise RuntimeError(infoSpec % (command[0], osError)) from osError
    finally:
      if told is not None:
        os.remove(told)
    if done.returncode:
      infoSpec = """The program '%s' failed: %s"""
      raise RuntimeError(infoSpec % (command[0], done.stderr.strip()))
    return done.stdout

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  One slot for each processor of the machine; a program run through
  #  '_run' holds one while it runs.
  __program_slots__ = threading.BoundedSemaphore(os.cpu_count() or 1)
  #  How many letters a command may have on Windows before it is handed
  #  over in a file; see '_run'. Windows refuses more than 32767.
  __long_command__ = 8000
  #  The standards a ritual file may ask for besides 'c++17'; see
  #  'getRitualStandard'.
  __other_standards__ = ('c++20',)
  #  How many times a refused ritual file is compiled again without
  #  more of its items, and the object files joined again without more,
  #  before what still fails is left out whole, or the join refused.
  __exorcism_rounds__ = 12
  __link_rounds__ = 12
  __qt_header_folder__: Optional[str] = None
  __qt_shared_object_folder__: Optional[str] = None
  __qt_program_folder__: Optional[str] = None
  __qt_version__: Optional[str] = None
  __qt_module_folder__: Optional[str] = None

  #  Fallback Variables

  #  Private Variables
  __ritual_files__ = None
  __target_file__ = None
  __qt_shared_objects__ = None
  __static_dependencies__ = ()
  __job_count__ = None
  __include_parts__ = None
  #  What 'getPrivateIncludeFolders' found, kept until 'setComponents'.
  __private_include_folders__ = None
  #  Whether the ritual files are compiled without the precompiled
  #  header: while 'run' compiles after 'clang++' refused the common
  #  header, and after the precompiled header is removed.
  __without_precompiled__ = False

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def _createQtHeaderFolder(cls, ) -> None:
    """Asks 'qmake6' where Qt keeps its headers and remembers it."""
    answer = cls._run('qmake6', '-query', 'QT_INSTALL_HEADERS')
    cls.__qt_header_folder__ = answer.strip()

  @classmethod
  def getQtHeaderFolder(cls, **kwargs) -> str:
    """
    Gives the folder where Qt keeps its headers, as '/usr/include/qt6'.

    Found for you: there is no setter. The first call asks Qt's own
    program 'qmake6', and the answer is remembered on the class for every
    'Summon'. Call it on the class or on an instance, with no arguments;
    the keyword is for the method's own use.

    Returns
    -------

    str
      The full path of the folder.

    Raises
    ------

    FileNotFoundError
      'qmake6' is not installed, which usually means Qt's development
      files are not either.

    RuntimeError
      'qmake6' ran and reported a failure; its message is included.
    """
    if cls.__qt_header_folder__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      cls._createQtHeaderFolder()
      return cls.getQtHeaderFolder(_recursion=True)
    return cls.__qt_header_folder__

  @classmethod
  def _createQtSharedObjectFolder(cls, ) -> None:
    """
    Asks 'qmake6' where Qt keeps its shared objects and remembers it.
    Where 'qmake6' is not there, as on a machine with Qt and without its
    development files, the folder is found among the usual folders of
    'System.getUsualQtFolders': the first that holds the shared object
    of QtCore.

    Raises
    ------

    FileNotFoundError
      There is no 'qmake6', and no usual folder holds the shared object
      of QtCore. The message names every folder looked in.
    """
    try:
      answer = cls._run('qmake6', '-query', 'QT_INSTALL_LIBS')
    except FileNotFoundError:
      system = System.getHere()
      coreName = system.getQtFileName('QtCore')
      looked = system.getUsualQtFolders()
      for folder in looked:
        if os.path.exists(os.path.join(folder, coreName)):
          cls.__qt_shared_object_folder__ = folder
          return
      infoSpec = """No Qt is found here. 'qmake6' is not installed to say
      where Qt is, and none of the usual folders holds '%s': %s. Install
      Qt %s, from Qt's own installer or the system's packages."""
      info = infoSpec % (
          coreName, ', '.join(looked) or 'none is there', '6.12')
      raise FileNotFoundError(' '.join(info.split())) from None
    cls.__qt_shared_object_folder__ = answer.strip()

  @classmethod
  def getQtSharedObjectFolder(cls, **kwargs) -> str:
    """
    Gives the folder where Qt keeps its shared objects, as '/usr/lib'.

    Found for you: there is no setter. The first call asks Qt's own
    program 'qmake6', and the answer is remembered on the class for every
    'Summon'. Call it on the class or on an instance, with no arguments;
    the keyword is for the method's own use.

    Join it with a file name to get a path for 'setQtSharedObjects':
    'os.path.join(folder, "libQt6Core.so.6")'.

    Returns
    -------

    str
      The full path of the folder.

    Raises
    ------

    FileNotFoundError
      'qmake6' is not installed, which usually means Qt's development
      files are not either.

    RuntimeError
      'qmake6' ran and reported a failure; its message is included.
    """
    if cls.__qt_shared_object_folder__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      cls._createQtSharedObjectFolder()
      return cls.getQtSharedObjectFolder(_recursion=True)
    return cls.__qt_shared_object_folder__

  @classmethod
  def _createQtVersion(cls, ) -> None:
    """Asks 'qmake6' which Qt it belongs to and remembers it."""
    answer = cls._run('qmake6', '-query', 'QT_VERSION')
    cls.__qt_version__ = answer.strip()

  @classmethod
  def getQtVersion(cls, **kwargs) -> str:
    """
    Gives the version of the Qt the rituals are built against, as
    '6.12.0'.

    Found for you: there is no setter. The first call asks Qt's own
    program 'qmake6', and the answer is remembered on the class for every
    'Summon'. You pass nothing; the keyword is for the method's own use.

    The build keeps it beside the object files. An object file made
    against another Qt is made again.

    Raises
    ------

    FileNotFoundError
      'qmake6' is not installed.
    """
    if cls.__qt_version__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      cls._createQtVersion()
      return cls.getQtVersion(_recursion=True)
    return cls.__qt_version__

  @classmethod
  def _createQtProgramFolder(cls, ) -> None:
    """
    Asks 'qmake6' where Qt keeps its programs and remembers it. Where
    'qmake6' is not there, it is the folder 'bin' beside the folder of
    the shared objects, as Qt's own installer lays it out.
    """
    try:
      answer = cls._run('qmake6', '-query', 'QT_INSTALL_BINS')
    except FileNotFoundError:
      folder = os.path.dirname(cls.getQtSharedObjectFolder())
      cls.__qt_program_folder__ = os.path.join(folder, 'bin')
      return
    cls.__qt_program_folder__ = answer.strip()

  @classmethod
  def getQtProgramFolder(cls, **kwargs) -> str:
    """
    Gives the folder where Qt keeps its programs, as '/usr/lib/qt6/bin'.
    'qmake6' itself is one of them.

    Found for you: there is no setter. The first call asks Qt's own
    program 'qmake6', and the answer is remembered on the class for every
    'Summon'. Call it on the class or on an instance, with no arguments;
    the keyword is for the method's own use.

    No build needs it. On Windows it is also the folder of Qt's shared
    objects themselves, which 'Windows.prepareOpening' tells Python of.

    Returns
    -------

    str
      The full path of the folder.

    Raises
    ------

    FileNotFoundError
      'qmake6' is not installed, which usually means Qt's development
      files are not either.

    RuntimeError
      'qmake6' ran and reported a failure; its message is included.
    """
    if cls.__qt_program_folder__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      cls._createQtProgramFolder()
      return cls.getQtProgramFolder(_recursion=True)
    return cls.__qt_program_folder__

  @classmethod
  def _createQtModuleFolder(cls, ) -> None:
    """Asks 'qmake6' where Qt keeps what it knows of itself, and
    remembers its folder 'mkspecs/modules'."""
    answer = cls._run('qmake6', '-query', 'QT_HOST_DATA')
    folder = os.path.join(answer.strip(), 'mkspecs', 'modules')
    if not os.path.isdir(folder):
      infoSpec = """Qt's folder '%s' is not there. It holds a file for
      each part of Qt, naming the parts that part needs, and every Qt
      with 'qmake6' installs it."""
      raise FileNotFoundError(' '.join((infoSpec % folder).split()))
    cls.__qt_module_folder__ = folder

  @classmethod
  def getQtModuleFolder(cls, **kwargs) -> str:
    """
    Gives the folder where Qt describes each of its parts for 'qmake6',
    as '/usr/lib/qt6/mkspecs/modules': a file 'qt_lib_core.pri' for
    QtCore and 'qt_lib_core_private.pri' for its private side, and so
    on for every part. Each names the parts that part needs. See
    'Rituals.readQtModules'.

    Found for you: there is no setter. The first call asks Qt's own
    program 'qmake6', and the answer is remembered on the class for every
    'Summon'. Call it on the class or on an instance, with no arguments;
    the keyword is for the method's own use.

    Returns
    -------

    str
      The full path of the folder.

    Raises
    ------

    FileNotFoundError
      'qmake6' is not installed, or the Qt it belongs to has no such
      folder.

    RuntimeError
      'qmake6' ran and reported a failure; its message is included.
    """
    if cls.__qt_module_folder__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      cls._createQtModuleFolder()
      return cls.getQtModuleFolder(_recursion=True)
    return cls.__qt_module_folder__

  def getRitualFiles(self) -> Paths:
    """
    Gives the ritual files this build compiles: the C++ files we write,
    holding the plainly named functions the target file will offer.

    Provided by you, through 'setRitualFiles'. Nothing fills it in for
    you.

    Returns
    -------

    Paths
      A 'Tuple[str, ...]' of full paths, in the order you gave them.

    Raises
    ------

    MissingVariable
      'setRitualFiles' has not been called on this build.
    """
    if self.__ritual_files__ is None:
      raise MissingVariable(self, '__ritual_files__', tuple)
    return self.__ritual_files__

  def getTargetFile(self) -> str:
    """
    Gives the shared object this build writes.

    Provided by you, through 'setTargetFile'. Nothing fills it in for
    you. Having the path does not mean the file is there: it exists once
    'run' has been called.

    Returns
    -------

    str
      The full path of the file.

    Raises
    ------

    MissingVariable
      'setTargetFile' has not been called on this build.
    """
    if self.__target_file__ is None:
      raise MissingVariable(self, '__target_file__', str)
    return self.__target_file__

  def getQtSharedObjects(self, **kwargs) -> Paths:
    """
    Gives the Qt shared objects the target file will call into.

    Provided by you, through 'setQtSharedObjects'. Nothing fills it in
    for you: the build does not work out which of Qt's files your C++
    files use.

    Returns
    -------

    Paths
      A 'Tuple[str, ...]' of full paths, in the order you gave them. It
      is empty when you said the rituals call into nothing of Qt.

    Raises
    ------

    MissingVariable
      'setQtSharedObjects' has not been called on this build.
    """
    if self.__qt_shared_objects__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      self.setQtSharedObjects()
      return self.getQtSharedObjects(_recursion=True)
    return self.__qt_shared_objects__

  def getStaticDependencies(self) -> Paths:
    """Gives what 'setStaticDependencies' set: the words the line
    joining the target file takes after the Qt shared objects, for a
    static library of Qt among them. Empty when none was set."""
    return self.__static_dependencies__

  def getObjectFolder(self) -> str:
    """
    Gives the folder the object files are kept in.

    Found for you: the folder 'demons' beside the target file: what
    the rituals summon. Having the path does not mean the folder is
    there; 'run' makes it.

    Raises
    ------

    MissingVariable
      'setTargetFile' has not been called on this build.
    """
    return os.path.join(os.path.dirname(self.getTargetFile()), 'demons')

  def getObjectFile(self, ritualFile: str) -> str:
    """
    Gives the object file of one ritual file: the same name with the
    ending '.o', in the object folder. A ritual file lying in the
    folder of a part of Qt, as 'QtCoreRituals', has its object file in
    the folder of that part in the object folder: 'QtCoreDemons'.

    Parameters
    ----------

    ritualFile : str
      The path of a ritual file, as '/here/QtCoreRituals/q_object.cpp'.
    """
    partFolder = os.path.basename(os.path.dirname(ritualFile))
    if partFolder.endswith('Rituals') and partFolder != 'Rituals':
      stem = os.path.splitext(os.path.basename(ritualFile))[0]
      demons = '%sDemons' % partFolder[:-len('Rituals')]
      return os.path.join(self.getObjectFolder(), demons, '%s.o' % stem)
    stem = os.path.splitext(os.path.basename(ritualFile))[0]
    return os.path.join(self.getObjectFolder(), '%s.o' % stem)

  def _getTargetStem(self) -> str:
    """Gives the name of the target file without its ending, as
    'libcutienator_QtCore': the files of this build in the object
    folder are named after it, since the builds of several target
    files share that folder."""
    return os.path.splitext(os.path.basename(self.getTargetFile()))[0]

  def getCommonHeaderFile(self) -> str:
    """
    Gives the path of the common header: the name of the target file
    with '.common.h', in the object folder, as
    'libcutienator_QtCore.common.h'. 'run' writes it before it compiles
    any ritual file, and leaves it there.
    """
    return os.path.join(
        self.getObjectFolder(), '%s.common.h' % self._getTargetStem())

  def getCommonHeaderText(self) -> str:
    """
    Gives the text of the common header: every line of the ritual files
    that begins with '#include' and stands under no '#if', each once,
    in the order they are first met. It is read off the ritual files as
    they are now.

    Raises
    ------

    MissingVariable
      'setRitualFiles' has not been called on this build.
    """
    lines = []
    for ritualFile in self.getRitualFiles():
      depth = 0
      with open(ritualFile, encoding='utf-8') as file:
        for line in file:
          line = line.strip()
          if not line.startswith('#'):
            continue
          word = line[1:].strip()
          if word.startswith('if'):
            depth += 1
          elif word.startswith('endif'):
            depth -= 1
          elif depth == 0 and line.startswith('#include'):
            #  A line under an '#if' is for some systems only, and
            #  stays with its ritual file.
            if line not in lines:
              lines.append(line)
    return ''.join('%s\n' % line for line in lines)

  def getRitualStandard(self, ritualFile: str) -> str:
    """
    Gives the standard of C++ one ritual file is compiled by: 'c++17',
    the standard Qt's headers were read by, unless the comment the file
    begins with holds the line '//  Summon: -std=c++20'. A file whose
    code from Qt's source compiles only so says it, as the Bluetooth
    files of Windows do: Qt's C++/WinRT code waits with coroutines,
    which 'clang++' has only from C++20 on, where Microsoft's compiler,
    which Qt is built with, has them in C++17 as well.

    Parameters
    ----------

    ritualFile : str
      The path of the ritual file.

    Raises
    ------

    ValueError
      The line names another standard than 'c++20'.

    FileNotFoundError
      The ritual file is not there.
    """
    marker = '//  Summon: '
    with open(ritualFile, encoding='utf-8') as file:
      for line in file:
        if not line.startswith('//'):
          break
        if not line.startswith(marker):
          continue
        said = line[len(marker):].strip()
        if said not in ('-std=%s' % s for s in self.__other_standards__):
          infoSpec = """The ritual file '%s' asks 'Summon' for '%s', but
          the only standard a ritual file may ask for is %s."""
          raise ValueError(' '.join((infoSpec % (
              ritualFile, said, ', '.join(
                  "'-std=%s'" % s for s in self.__other_standards__),
          )).split()))
        return said[len('-std='):]
    return 'c++17'

  def getPrecompiledHeaderFile(self) -> str:
    """
    Gives the path of the precompiled header: the name of the target
    file with '.common.pch', in the object folder. The file is there
    only while 'run' compiles.
    """
    return os.path.join(
        self.getObjectFolder(), '%s.common.pch' % self._getTargetStem())

  def getToldFile(self) -> str:
    """
    Gives the file in the object folder that says what the object files
    of this build were made with: the Qt, and what 'clang++' was told.
    It is the name of the target file with '.told.txt'. 'run' writes it
    once every object file is made.
    """
    return os.path.join(
        self.getObjectFolder(), '%s.told.txt' % self._getTargetStem())

  def getToldText(self) -> str:
    """
    Gives what the object files are made with as this build has it: the
    version of Qt, the command 'clang++' is run by for the precompiled
    header, and the one for a ritual file, with the name of the file
    left open.
    """
    precompile = ' '.join(self.getPrecompileCommand())
    command = ' '.join(self._getCompileCommand(
        'RITUAL_FILE', self.getObjectFile('RITUAL_FILE'), 'c++17'))
    return 'Qt %s\n%s\n%s\n' % (self.getQtVersion(), precompile, command)

  def getLeftOutFile(self) -> str:
    """
    Gives the left-out file of this build: the name of the target file
    with '.left_out.json' in the place of its ending, beside it, as
    'libcutienator_QtCore.left_out.json'. It is there when something of
    the ritual files was left out, and says what and why; see
    'getRecord'. It goes where the target file goes: 'Rituals' reads it
    when the target file is opened.
    """
    return self.getLeftOutFileOf(self.getTargetFile())

  @staticmethod
  def getLeftOutFileOf(targetFile: str) -> str:
    """Gives the left-out file of a target file, as 'getLeftOutFile'
    names it."""
    return '%s.left_out.json' % os.path.splitext(targetFile)[0]

  def getExorcisedFile(self, ritualFile: str) -> str:
    """
    Gives the copy of one ritual file that is compiled without what was
    dropped of it: beside its object file, with '.exorcised' before the
    ending of the ritual file, as 'q_object.exorcised.cpp'. Its object
    file is that of the ritual file.
    """
    objectFile = self.getObjectFile(ritualFile)
    ending = os.path.splitext(ritualFile)[1]
    return '%s.exorcised%s' % (os.path.splitext(objectFile)[0], ending)

  @staticmethod
  def _getRecordKey(ritualFile: str) -> str:
    """Gives the name a ritual file has in the left-out file: its
    folder and its name, as 'QtCoreRituals/q_object.cpp'."""
    folder, name = os.path.split(os.path.normpath(ritualFile))
    return '%s/%s' % (os.path.basename(folder), name)

  def getRecord(self) -> Dict[str, Any]:
    """
    Gives what the left-out file says, or an empty record when there is
    none.

    Returns
    -------

    Dict[str, Any]
      'about', what the file is; 'common header', what 'clang++' said
      when it refused the common header, or None; 'ritual files', for
      each ritual file something of which was left out, under its name
      of '_getRecordKey', what 'Exorcist.getRecord' gives: 'dropped',
      the items dropped with why; 'whole', why the whole file was left
      out, or None; 'leftOut', each ritual left out, with the function
      it calls and why.
    """
    record = {
        'about': [
            "What 'Summon' left out of the target file beside this file,",
            'because the compiler or the linker refused it on this',
            'machine, and why. Each ritual left out raises',
            'NotImplementedError when it is called; every other ritual is',
            'in the target file.',
        ],
        'common header': None,
        'ritual files': dict(),
    }
    leftOutFile = self.getLeftOutFile()
    if os.path.isfile(leftOutFile):
      with open(leftOutFile, encoding='utf-8') as file:
        record.update(json.load(file))
    return record

  @staticmethod
  def readLeftOut(leftOutFile: str) -> Dict[str, Tuple[str, str]]:
    """
    Gives each ritual a left-out file names, with the function it calls
    and why it was left out. Empty when there is no such file.
    """
    if not os.path.isfile(leftOutFile):
      return dict()
    with open(leftOutFile, encoding='utf-8') as file:
      record = json.load(file)
    leftOut = dict()
    for entry in record.get('ritual files', {}).values():
      for name, (function, reason) in entry.get('leftOut', {}).items():
        leftOut[name] = (function, reason)
    return leftOut

  def getLeftOut(self) -> Dict[str, Tuple[str, str]]:
    """Gives each ritual left out of the target file, with the
    function it calls and why, as the left-out file says it."""
    return self.readLeftOut(self.getLeftOutFile())

  def getJobCount(self) -> int:
    """
    Gives how many ritual files are compiled at the same time.

    Found for you: as many as the machine has processors. 'setJobCount'
    says otherwise.
    """
    if self.__job_count__ is None:
      return os.cpu_count() or 1
    return self.__job_count__

  def getComponents(self) -> Paths:
    """
    Gives the parts of Qt whose private headers the ritual files may
    name, as 'QtCore'. Provided by you, through 'setComponents'; none
    when it was not called.
    """
    return self.__include_parts__ or ()

  def getPrivateIncludeFolders(self) -> Paths:
    """
    Gives every folder 'clang++' has to look in for the headers Qt
    calls private: what 'System.getPrivateFolders' gives for each part
    of 'getComponents', leaving out a folder that is not there; and,
    when there are any, after them those of every other part of the
    Qt of this machine. A header Qt calls private of one part may pull
    in one of a part that has no ritual files, as that of QtStateMachine
    pulls in 'private/qtscxmlglobal-config_p.h' of QtScxmlGlobal, a
    part of header files alone.

    Found at the first call and kept, since every command of the
    build names them, until 'setComponents' is called again.
    """
    if self.__private_include_folders__ is not None:
      return self.__private_include_folders__
    system = System.getHere()
    headerFolder = self.getQtHeaderFolder()
    qtFolder, version = self.getQtSharedObjectFolder(), self.getQtVersion()
    found = []
    for part in self.getComponents():
      for folder in system.getPrivateFolders(
          headerFolder, qtFolder, version, part):
        if os.path.isdir(folder) and folder not in found:
          found.append(folder)
    if found:
      others = sorted(
          name for name in os.listdir(headerFolder)
          if name.startswith('Qt') and name not in self.getComponents())
      for part in others:
        for folder in system.getPrivateFolders(
            headerFolder, qtFolder, version, part):
          if os.path.isdir(folder) and folder not in found:
            found.append(folder)
      #  Some of those headers name 'qplatformdefs.h', which Qt keeps
      #  with what it knows of the system and the compiler it was
      #  built for, as '/usr/lib/qt6/mkspecs/linux-g++'.
      found.append(os.path.join(
          self._run('qmake6', '-query', 'QT_HOST_DATA').strip(),
          'mkspecs', self._run('qmake6', '-query', 'QMAKE_SPEC').strip()))
    self.__private_include_folders__ = (*found,)
    return self.__private_include_folders__

  def getStaleRitualFiles(self) -> Paths:
    """
    Gives the ritual files that have to be compiled: each one that has
    no object file, or that changed after its object file was made.
    When Qt, or what 'clang++' is told, is no longer what the object
    files were made with, that is every ritual file.

    Returns
    -------

    Paths
      A 'Tuple[str, ...]' of full paths, in the order you gave them.
    """
    ritualFiles = self.getRitualFiles()
    toldFile, told = self.getToldFile(), None
    if os.path.isfile(toldFile):
      with open(toldFile) as file:
        told = file.read()
    if told != self.getToldText():
      return ritualFiles
    stale = []
    for ritualFile in ritualFiles:
      objectFile = self.getObjectFile(ritualFile)
      if not os.path.isfile(objectFile):
        stale.append(ritualFile)
      elif os.path.getmtime(objectFile) < os.path.getmtime(ritualFile):
        stale.append(ritualFile)
    return (*stale,)

  def getPrecompileCommand(self) -> Paths:
    """
    Gives the exact 'clang++' command that makes the precompiled header
    of the common header, without running it.

    It holds everything 'getCompileCommand' tells 'clang++' of how to
    compile. 'clang++' refuses a precompiled header made by another
    '-std', another '-O' or other flags than the ritual file it is used
    for.

    Returns
    -------

    Paths
      A 'Tuple[str, ...]', one argument per entry: 'clang++', then
      '-std=c++17', '-O2', '-fno-access-control' and
      '-DQT_USE_QSTRINGBUILDER', as for a ritual file;
      what the system adds for the compiler, as for a ritual file;
      '-I' with the folder of Qt's headers;
      '-fpch-instantiate-templates', so the templates the headers use
      are worked out here, once, and not again for every ritual file.
      Without it a ritual file is compiled three times faster than
      with no precompiled header, with it twenty times;
      '-x' and 'c++-header', which say that the file is a header to
      precompile;
      the path of the common header;
      '-o' with the path of the precompiled header.

    Raises
    ------

    MissingVariable
      'setTargetFile' has not been called on this build.

    FileNotFoundError
      'qmake6' is not installed.

    NotImplementedError
      Python runs on a system that 'System' has no subclass for.
    """
    system = System.getHere()
    qtFolder = self.getQtSharedObjectFolder()
    return (
        'clang++', '-std=c++17', '-O2', '-fno-access-control',
        '-DQT_USE_QSTRINGBUILDER',
        *system.getCompilerFlags(qtFolder),
        '-I%s' % self.getQtHeaderFolder(),
        *('-I%s' % f for f in self.getPrivateIncludeFolders()),
        '-fpch-instantiate-templates', '-x', 'c++-header',
        self.getCommonHeaderFile(),
        '-o', self.getPrecompiledHeaderFile(),
    )

  def getCompileCommand(self, ritualFile: str) -> Paths:
    """
    Gives the exact 'clang++' command that makes the object file of one
    ritual file, without running it. It runs only while the precompiled
    header is there: after the command 'getPrecompileCommand' gives.

    The compiler and its '-std' are those that read Qt's headers when
    the ritual files were generated. A header may give a class other
    functions for another compiler or another standard, as Qt's
    'qfloat16.h' does, and a ritual written from what one of them read
    would then not compile with the other.

    Parameters
    ----------

    ritualFile : str
      The path of the ritual file.

    Returns
    -------

    Paths
      A 'Tuple[str, ...]', one argument per entry: 'clang++', then
      '-std=c++17', the standard the headers were read by;
      '-O2', so the compiler tidies the result;
      '-fno-access-control', so the compiler lets a ritual call a
      function C++ marks 'private' or 'protected'. C++ means by those
      that only the class itself, or a class built on it, may call the
      function; cutienator takes every function Qt has;
      '-DQT_USE_QSTRINGBUILDER', as Qt is told when it builds itself.
      Some of Qt's headers hold inline code that compiles only so, as
      the constructor in QtQuick's 'qsgcurvestrokenode_p_p.h', which
      adds two 'QStringView's. It has to be on the command line: the
      precompiled header is read before anything a ritual file says;
      '-c', to make an object file and join nothing yet;
      what the system adds for the compiler, which on Linux is '-fPIC'
      and the two '-fvisibility' flags. 'getCompilerFlags' of 'Linux',
      'MacOS' and 'Windows' says what each is for;
      '-I' with the folder of Qt's headers;
      '-include-pch' with the path of the precompiled header, which
      'clang++' then reads before the ritual file. The headers the
      ritual file names are in it already, and are not read again;
      the path of the ritual file;
      '-o' with the path of its object file.
      A ritual file that asks for another standard, as
      'getRitualStandard' reads it, is compiled with that '-std' and
      without the precompiled header, which 'clang++' refuses for
      another standard than its own: such a file reads its headers
      itself, through its own '#include' lines.

    Raises
    ------

    MissingVariable
      'setTargetFile' has not been called on this build.

    FileNotFoundError
      'qmake6' is not installed, or the ritual file is not there.

    ValueError
      The ritual file asks for a standard 'getRitualStandard' does not
      know.

    NotImplementedError
      Python runs on a system that 'System' has no subclass for.
    """
    objectFile = self.getObjectFile(ritualFile)
    standard = self.getRitualStandard(ritualFile)
    return self._getCompileCommand(ritualFile, objectFile, standard)

  def _getCompileCommand(
      self,
      ritualFile: str,
      objectFile: str,
      standard: str,
  ) -> Paths:
    """Gives the command of 'getCompileCommand' for a ritual file and
    its object file, compiled by the given standard, as 'c++17'."""
    system = System.getHere()
    qtFolder = self.getQtSharedObjectFolder()
    if self.__without_precompiled__:
      precompiled = ()
    elif standard == 'c++17' and not ritualFile.endswith('.mm'):
      #  A file of Objective-C++ cannot use a header precompiled as C++.
      precompiled = ('-include-pch', self.getPrecompiledHeaderFile())
    else:
      precompiled = ()
    return (
        'clang++', '-std=%s' % standard, '-O2', '-fno-access-control',
        '-DQT_USE_QSTRINGBUILDER', '-c',
        *system.getCompilerFlags(qtFolder),
        '-I%s' % self.getQtHeaderFolder(),
        *('-I%s' % f for f in self.getPrivateIncludeFolders()),
        *precompiled, ritualFile,
        '-o', objectFile,
    )

  def getLinkCommand(self) -> Paths:
    """
    Gives the exact 'clang++' command that joins the object files into
    the target file, without running it.

    Returns
    -------

    Paths
      A 'Tuple[str, ...]', one argument per entry: 'clang++', then
      '-shared', to make a shared object and not a program;
      what the system adds for the compiler and then for the linker,
      which on Linux is '-fPIC', the two '-fvisibility' flags,
      '-Wl,--no-undefined' and '-Wl,-rpath,' with the folder of Qt's
      shared objects. 'getCompilerFlags' and 'getLinkerFlags' of
      'Linux', 'MacOS' and 'Windows' say what each is for;
      the path of the object file of each ritual file;
      '-o' with the path of the target file;
      the path of each Qt shared object the target file calls into;
      what 'setStaticDependencies' set, as '-lole32', for a static
      library of Qt among them.

    Raises
    ------

    MissingVariable
      One of the three setters has not been called; the message names
      the missing value.

    FileNotFoundError
      'qmake6' is not installed.

    NotImplementedError
      Python runs on a system that 'System' has no subclass for.
    """
    system = System.getHere()
    qtFolder = self.getQtSharedObjectFolder()
    ritualFiles = self.getRitualFiles()
    return (
        'clang++', '-shared',
        *system.getCompilerFlags(qtFolder),
        *system.getLinkerFlags(qtFolder),
        *(self.getObjectFile(ritualFile) for ritualFile in ritualFiles),
        '-o', self.getTargetFile(), *self.getQtSharedObjects(),
        *self.getStaticDependencies(),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setRitualFiles(self, *ritualFiles: str) -> None:
    """
    Tells the build which files hold the rituals: the plainly named
    functions the target file will offer to Python, each calling one Qt
    function. They are the C++ files we write ourselves, as
    'q_object.cpp', never Qt's own.

    Required before 'run'. Calling it again replaces the files given
    before.

    Parameters
    ----------

    *ritualFiles : str
      The path of each ritual file, one argument per file and at least
      one. A path may be relative to where Python was started; it is
      kept in full. Each file must exist already.

    Raises
    ------

    ValueError
      Called with no path at all.

    TypeException
      A path is not text.

    FileNotFoundError
      A path leads to no file.
    """
    if not ritualFiles:
      infoSpec = """A build needs at least one ritual file, and no path
      was given."""
      raise ValueError(' '.join(infoSpec.split()))
    for ritualFile in ritualFiles:
      if not isinstance(ritualFile, str):
        raise TypeException('ritualFile', ritualFile, str)
      if not os.path.isfile(ritualFile):
        infoSpec = """There is no ritual file at '%s'."""
        raise FileNotFoundError(infoSpec % ritualFile)
    self.__ritual_files__ = (
        *(os.path.abspath(path) for path in ritualFiles),
    )

  def setComponents(self, *components: str) -> None:
    """
    Tells the build which parts of Qt the ritual files are of, as
    'QtCore', so that it looks in the folders of their private headers
    too. Optional: without it only Qt's header folder is looked in.
    """
    for component in components:
      if not isinstance(component, str):
        raise TypeException('component', component, str)
    self.__include_parts__ = (*components,)
    self.__private_include_folders__ = None

  def setJobCount(self, jobCount: int) -> None:
    """
    Tells the build how many ritual files to compile at the same time.

    Optional. Without it the build compiles as many at once as the
    machine has processors.

    Parameters
    ----------

    jobCount : int
      1 or more.

    Raises
    ------

    TypeException
      'jobCount' is not an 'int'.

    ValueError
      'jobCount' is less than 1.
    """
    if not isinstance(jobCount, int) or isinstance(jobCount, bool):
      raise TypeException('jobCount', jobCount, int)
    if jobCount < 1:
      infoSpec = """A build compiles 1 ritual file at a time or more,
      but received %d."""
      raise ValueError(' '.join((infoSpec % jobCount).split()))
    self.__job_count__ = jobCount

  def setTargetFile(self, targetFile: str) -> None:
    """
    Tells the build which shared object to write.

    Required before 'run', which creates the file and replaces one
    already there. Calling this again replaces the path given before.

    Parameters
    ----------

    targetFile : str
      The path of the one file to write, as 'libexample.so'. A path may
      be relative to where Python was started; it is kept in full. The
      folder it lies in must exist already; the file need not.

    Raises
    ------

    TypeException
      The path is not text.

    FileNotFoundError
      The folder the file would lie in does not exist.
    """
    if not isinstance(targetFile, str):
      raise TypeException('targetFile', targetFile, str)
    targetFile = os.path.abspath(targetFile)
    folder = os.path.dirname(targetFile)
    if not os.path.isdir(folder):
      infoSpec = """The target file '%s' would lie in a folder that does
      not exist."""
      raise FileNotFoundError(' '.join((infoSpec % targetFile).split()))
    self.__target_file__ = targetFile

  def setQtSharedObjects(self, *qtSharedObjects: str) -> None:
    """
    Tells the build which of Qt's shared objects the rituals call into.

    Required before 'run', even when the answer is none: call it with no
    arguments then. Calling it again replaces the paths given before.

    Name the file holding each Qt class the ritual files include: 'QObject'
    is in 'libQt6Core.so.6', 'QWidget' in 'libQt6Widgets.so.6'. Those
    files lie in the folder 'getQtSharedObjectFolder' gives. The names
    are those of Linux; 'System.getHere().getQtFileName("QtCore")' gives
    the name on the system Python runs on.

    Parameters
    ----------

    *qtSharedObjects : str
      The path of each Qt shared object, one argument per file, as
      '/usr/lib/libQt6Core.so.6'. A path may be relative to where Python
      was started; it is kept in full. Each file must exist.

    Raises
    ------

    TypeException
      A path is not text.

    FileNotFoundError
      A path leads to no file.
    """
    for qtSharedObject in qtSharedObjects:
      if not isinstance(qtSharedObject, str):
        raise TypeException('qtSharedObject', qtSharedObject, str)
      if not os.path.isfile(qtSharedObject):
        infoSpec = """There is no Qt shared object at '%s'."""
        raise FileNotFoundError(infoSpec % qtSharedObject)
    self.__qt_shared_objects__ = (
        *(os.path.abspath(f) for f in qtSharedObjects),
    )

  def setStaticDependencies(self, *words: str) -> None:
    """
    Tells the build what a static library of Qt among its Qt shared
    objects needs beside it, as ActiveQt's 'Qt6AxContainer.lib' needs
    'Qt6AxBase.lib' and Windows' own '-lole32'. A shared object brings
    the libraries it calls into by itself; a static library does not.

    Optional; without it the build takes none. Calling it again
    replaces the words given before.

    Parameters
    ----------

    *words : str
      One argument of the joining line per entry, kept as given: a
      path, a '-l' flag, or '-framework' and a name as two entries.

    Raises
    ------

    TypeException
      A word is not text.
    """
    for word in words:
      if not isinstance(word, str):
        raise TypeException('word', word, str)
    self.__static_dependencies__ = (*words,)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __str__(self) -> str:
    """Says which setters are still to be called, or what will be made."""
    clsName = type(self).__name__
    unset = [
        setter for setter, value in (
            ('setRitualFiles', self.__ritual_files__),
            ('setTargetFile', self.__target_file__),
            ('setQtSharedObjects', self.__qt_shared_objects__),
        ) if value is None
    ]
    if unset:
      infoSpec = """<%s still waiting for: %s>"""
      return infoSpec % (clsName, ', '.join(unset))
    infoSpec = """<%s of %d ritual files into '%s'>"""
    count = len(self.__ritual_files__)
    return infoSpec % (clsName, count, self.__target_file__)

  __repr__ = __str__

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  def _precompile(self) -> None:
    """
    Writes the common header and makes the precompiled header of it.

    Raises
    ------

    RuntimeError
      'clang++' refused the common header. What it said is included,
      and names the line of the common header it stopped at.
    """
    commonHeader = self.getCommonHeaderFile()
    with open(commonHeader, 'w', encoding='utf-8') as file:
      file.write(self.getCommonHeaderText())
    try:
      self._run(*self.getPrecompileCommand())
    except RuntimeError as runtimeError:
      infoSpec = """'clang++' refused the common header '%s', which
      holds every '#include' line of the ritual files."""
      info = ' '.join((infoSpec % commonHeader).split())
      raise RuntimeError('%s %s' % (info, runtimeError)) from runtimeError

  def _compile(self, ritualFile: str) -> Optional[str]:
    """
    Makes the object file of one ritual file.

    Returns
    -------

    Optional[str]
      None when 'clang++' made it. Else what 'clang++' said, with the
      ritual file named in front.
    """
    try:
      self._run(*self.getCompileCommand(ritualFile))
    except RuntimeError as runtimeError:
      return '%s: %s' % (ritualFile, runtimeError)
    return None

  def _writeRecord(self, record: Dict[str, Any]) -> None:
    """Writes the left-out file, or removes it when nothing was left
    out and the common header was not refused."""
    leftOutFile = self.getLeftOutFile()
    if not record['ritual files'] and record['common header'] is None:
      if os.path.isfile(leftOutFile):
        os.remove(leftOutFile)
      return
    with open(leftOutFile, 'w', encoding='utf-8') as file:
      json.dump(record, file, indent=2, sort_keys=True)
      file.write('\n')

  def _compileCopy(self, ritualFile: str, copyFile: str) -> Optional[str]:
    """
    Makes the object file of a ritual file from its copy without what
    was dropped, as '_compile' does of the ritual file, and with every
    error said, not the first twenty, each with every place a template
    of it was asked for, not the first ten. The folder of the ritual file is
    searched first for a header named between quotes, as it is for the
    ritual file itself.

    Returns
    -------

    Optional[str]
      None when 'clang++' made it. Else what 'clang++' said.
    """
    command = list(self._getCompileCommand(
        copyFile, self.getObjectFile(ritualFile),
        self.getRitualStandard(ritualFile)))
    command[1:1] = [
        '-ferror-limit=0', '-ftemplate-backtrace-limit=0', '-iquote',
        os.path.dirname(ritualFile)]
    try:
      self._run(*command)
    except RuntimeError as runtimeError:
      return str(runtimeError)
    return None

  def _createExorcist(
      self,
      ritualFile: str,
      record: Dict[str, Any],
  ) -> Exorcist:
    """Gives an Exorcist of a ritual file, which drops again what the
    record says an earlier build dropped of it. A record that no longer
    fits the ritual file is not taken."""
    exorcist = Exorcist()
    exorcist.setRitualFile(ritualFile)
    entry = record['ritual files'].get(self._getRecordKey(ritualFile))
    if entry is not None:
      try:
        exorcist.setRecord(entry)
      except ValueError:
        exorcist.setRitualFile(ritualFile)
    return exorcist

  def _findByTrial(
      self,
      ritualFile: str,
      exorcist: Exorcist,
  ) -> Optional[Tuple[str, str, int, int]]:
    """
    Finds, by compiling the copy with items left out, one item whose
    absence leaves no error that no line is blamed for: as an error in
    a template 'clang++' worked out at the end of the file, without
    saying which ritual asked for it. The rituals and the functions of
    the Cute class are tried first, by halves; then also the Cute
    class, Qt's code and the '#include' lines that may go. Nothing is
    dropped here.

    Returns
    -------

    Optional[Tuple[str, str, int, int]]
      The item, as 'Exorcist.getItems' gives it; None when leaving out
      all of them does not help either.
    """
    copyFile = self.getExorcisedFile(ritualFile)

    def clears(items: Tuple) -> bool:
      with open(copyFile, 'w', encoding='utf-8') as file:
        file.write(exorcist.getCopyText(*items))
      said = self._compileCopy(ritualFile, copyFile)
      if said is None:
        return True
      return not exorcist.readBlame(said, copyFile, *items)[1]

    for wide in (False, True):
      candidates = exorcist.getCandidates(wide)
      if candidates and clears(candidates):
        break
    else:
      return None
    #  Leaving out the first 'high' clears it, the first 'low' does not:
    #  the last of the first 'high' is one the errors come from.
    low, high = 0, len(candidates)
    while high - low > 1:
      middle = (low + high) // 2
      if clears(candidates[:middle]):
        high = middle
      else:
        low = middle
    return candidates[high - 1]

  def _exorcise(
      self,
      ritualFile: str,
      exorcist: Exorcist,
      said: Optional[str],
      compiledFile: str,
  ) -> None:
    """
    Compiles a ritual file from its copy until the copy compiles: each
    round the Exorcist drops what the errors point at, and the copy
    without it is compiled. Where errors point at nothing, the item
    they come from is found by trial; see '_findByTrial'. Where no
    trial finds one either, or after '__exorcism_rounds__' rounds, the
    whole file is left out, and its copy is empty.

    Parameters
    ----------

    ritualFile : str
      The ritual file.

    exorcist : Exorcist
      The Exorcist of the ritual file, with what is dropped already.

    said : Optional[str]
      What 'clang++' said when it refused the file last; None to begin
      with compiling the copy as the Exorcist has it now.

    compiledFile : str
      The file 'clang++' refused: the ritual file, or its copy.

    Raises
    ------

    RuntimeError
      'clang++' refused even the empty copy, as when a flag it is told
      is wrong. What it said is included.
    """
    copyFile = self.getExorcisedFile(ritualFile)
    rounds = 0
    while True:
      if said is not None:
        rounds += 1
        if exorcist.getWholeReason() is not None:
          infoSpec = """'clang++' refused the empty copy '%s' of the
          ritual file '%s'."""
          info = ' '.join((infoSpec % (copyFile, ritualFile)).split())
          raise RuntimeError('%s %s' % (info, said))
        blamed, unblamed = exorcist.readBlame(said, compiledFile)
        errors = Exorcist.readCompilerErrors(said)
        first = errors[0]['text'] if errors else said.strip()[-500:]
        if rounds > self.__exorcism_rounds__:
          exorcist.dropWhole(
              'the compiler still refused the file on this machine after '
              '%d rounds: %s' % (self.__exorcism_rounds__, first))
        elif blamed:
          for item, reason in blamed:
            exorcist.drop(item, reason)
        else:
          found = self._findByTrial(ritualFile, exorcist)
          if found is None:
            exorcist.dropWhole(
                'the compiler refused the file on this machine at what '
                'no ritual of it holds alone: %s' % first)
          else:
            exorcist.drop(found, (
                'the compiler refused it on this machine, as compiling '
                'the file without it showed: %s' % unblamed[0]))
      with open(copyFile, 'w', encoding='utf-8') as file:
        file.write(exorcist.getCopyText())
      compiledFile = copyFile
      said = self._compileCopy(ritualFile, copyFile)
      if said is None:
        return

  def _link(
      self,
      exorcists: Dict[str, Exorcist],
      record: Dict[str, Any],
  ) -> None:
    """
    Joins the object files into the target file. When the linker
    refuses, what it named as needing what no library offers is
    dropped from the ritual file of that object file, the copy is
    compiled, and the object files are joined again, at most
    '__link_rounds__' times. The precompiled header is gone by now, so
    a copy is compiled reading its own headers.

    Raises
    ------

    RuntimeError
      The linker refused and named no object file of these ritual
      files, as when a Qt shared object is not there; or it still
      refused after the last round. What it said is included.
    """
    byName = dict()
    for ritualFile in self.getRitualFiles():
      name = os.path.basename(self.getObjectFile(ritualFile))
      byName.setdefault(name, []).append(ritualFile)
    rounds = 0
    while True:
      try:
        self._run(*self.getLinkCommand())
        return
      except RuntimeError as runtimeError:
        refusal = runtimeError
      rounds += 1
      blamed = dict()
      for objectName, blame in Exorcist.readLinkerRefusal(str(refusal)):
        for ritualFile in byName.get(objectName, ()):
          blamed.setdefault(ritualFile, []).append(blame)
      if not blamed or rounds > self.__link_rounds__:
        infoSpec = """'clang++' could not join the object files into '%s',
        and %s."""
        info = infoSpec % (self.getTargetFile(), (
            'named no object file of the ritual files' if not blamed
            else 'still refused after %d rounds' % self.__link_rounds__))
        raise RuntimeError('%s %s' % (' '.join(info.split()), refusal))
      self.__without_precompiled__ = True
      for ritualFile, blames in blamed.items():
        exorcist = exorcists.get(ritualFile)
        if exorcist is None:
          exorcist = self._createExorcist(ritualFile, record)
          exorcists[ritualFile] = exorcist
        if not exorcist.blameLinker(blames):
          exorcist.dropWhole(
              'the linker refused the file on this machine at what no '
              "ritual of it holds alone: it needs '%s'" % blames[0][1])
        self._exorcise(ritualFile, exorcist, None, ritualFile)

  def run(self) -> str:
    """
    Compiles the ritual files into the target file, leaving out what
    'clang++' refuses on this machine and nothing else.

    This is the only method that compiles. All three setters must have
    been called first. When 'getStaleRitualFiles' names any ritual
    file, the common header is written and the precompiled header made
    of it; each ritual file named is compiled into its object file,
    'getJobCount' of them at the same time. A ritual file 'clang++'
    refuses is compiled again from its copy without what the errors
    point at, as 'Exorcist' finds it, until the copy compiles. Then the
    precompiled header is removed, and the object files of all the
    ritual files are joined into the target file, again without what
    the linker refuses, if it does. What was left out, and why, is
    written to the left-out file; see 'getLeftOut'. The precompiled
    header takes some seconds, a ritual file about a fifth of a second,
    a copy compiled again some seconds, and joining about one.

    Returns
    -------

    str
      The full path of the target file, which now exists.

    Raises
    ------

    MissingVariable
      One of the three setters has not been called; the message names
      the missing value.

    ValueError
      Two ritual files have one name, and so one object file.

    FileNotFoundError
      'clang++' or 'qmake6' is not installed.

    RuntimeError
      'clang++' refused even an empty copy of a ritual file, or could
      not join the object files for what no ritual file holds, as a Qt
      shared object that is not there. Its own message is included.
      Every ritual file it did compile keeps its object file.
    """
    ritualFiles = self.getRitualFiles()
    objectFiles = [self.getObjectFile(f) for f in ritualFiles]
    for objectFile in objectFiles:
      if objectFiles.count(objectFile) > 1:
        infoSpec = """Two ritual files would be compiled into '%s'. Give
        each ritual file a name of its own."""
        raise ValueError(' '.join((infoSpec % objectFile).split()))
    os.makedirs(self.getObjectFolder(), exist_ok=True)
    for objectFile in objectFiles:
      #  The object files of each part of Qt lie in a folder of its own.
      os.makedirs(os.path.dirname(objectFile), exist_ok=True)
    toldFile, toldText = self.getToldFile(), self.getToldText()
    stale = self.getStaleRitualFiles()
    record = self.getRecord()
    if len(stale) == len(ritualFiles):
      #  Every object file is made anew. Until all of them are, nothing
      #  says what the ones lying there were made with, and nothing of
      #  what an earlier build left out holds.
      if os.path.isfile(toldFile):
        os.remove(toldFile)
      record['ritual files'] = dict()
      record['common header'] = None
    for ritualFile in stale:
      record['ritual files'].pop(self._getRecordKey(ritualFile), None)
    exorcists = dict()  # type: Dict[str, Exorcist]
    self.__without_precompiled__ = False
    try:
      if stale:
        precompiledHeader = self.getPrecompiledHeaderFile()
        try:
          try:
            self._precompile()
          except RuntimeError as runtimeError:
            #  Every ritual file then reads its own headers, and one
            #  naming a header that fails is refused at its line.
            self.__without_precompiled__ = True
            record['common header'] = str(runtimeError)
          with ThreadPoolExecutor(max_workers=self.getJobCount()) as pool:
            said = dict(zip(stale, pool.map(self._compile, stale)))
            refused = [f for f in stale if said[f]]
            for ritualFile in refused:
              exorcists[ritualFile] = self._createExorcist(
                  ritualFile, record)
            #  Each refused ritual file is compiled again from its copy
            #  while the precompiled header is still there, first as it
            #  is, for every error and the whole of each, which the
            #  first compile does not say.
            list(pool.map(
                lambda f: self._exorcise(f, exorcists[f], None, f),
                refused))
        finally:
          if os.path.isfile(precompiledHeader):
            os.remove(precompiledHeader)
      with open(toldFile, 'w') as file:
        file.write(toldText)
      self._link(exorcists, record)
    finally:
      self.__without_precompiled__ = False
      for ritualFile, exorcist in exorcists.items():
        record['ritual files'][self._getRecordKey(ritualFile)] = (
            exorcist.getRecord())
      self._writeRecord(record)
    return self.getTargetFile()
