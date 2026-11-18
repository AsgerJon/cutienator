"""Build compiles ritual files into one shared object."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import subprocess
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Tuple, Optional

  Paths = Tuple[str, ...]


class Build:
  """
  Compiles ritual files into one shared object by running 'clang++'.

    build = Build()
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
  - A Qt shared object is one of Qt's own compiled files, which the
    rituals call into.

  You provide
  -----------

  Three things, each through its own setter, in any order. All three are
  required before 'run'.

  - 'setRitualFiles': the ritual files to compile.
  - 'setTargetFile': the target file to write.
  - 'setQtSharedObjects': the Qt shared objects the rituals call into.

  Found for you
  -------------

  Two things, which have no setter. Each is asked of Qt's own program
  'qmake6' the first time it is needed, and then remembered for every
  'Build', since Qt is installed in one place.

  - 'getQtHeaderFolder': where Qt keeps its headers.
  - 'getQtSharedObjectFolder': where Qt keeps its shared objects.

  What to expect
  --------------

  - Nothing is compiled until 'run' is called.
  - A setter refuses a wrong value at once: one that is not text, or a
    path that leads nowhere.
  - A getter whose setter was never called raises 'MissingVariable',
    naming what is missing.
  - 'getCommand' gives the exact 'clang++' command without running it.
  - 'print(build)' lists the setters still to be called.
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
    running, and there is nothing to close.

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __qt_header_folder__: Optional[str] = None
  __qt_shared_object_folder__: Optional[str] = None

  #  Fallback Variables

  #  Private Variables
  __ritual_files__ = None
  __target_file__ = None
  __qt_shared_objects__ = None

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
    'Build'. Call it on the class or on an instance, with no arguments;
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
    """Asks 'qmake6' where Qt keeps its shared objects and remembers it."""
    answer = cls._run('qmake6', '-query', 'QT_INSTALL_LIBS')
    cls.__qt_shared_object_folder__ = answer.strip()

  @classmethod
  def getQtSharedObjectFolder(cls, **kwargs) -> str:
    """
    Gives the folder where Qt keeps its shared objects, as '/usr/lib'.

    Found for you: there is no setter. The first call asks Qt's own
    program 'qmake6', and the answer is remembered on the class for every
    'Build'. Call it on the class or on an instance, with no arguments;
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

  def getCommand(self) -> Paths:
    """
    Gives the exact 'clang++' command that 'run' runs, without running
    it.

    Call it to see what a build will do, or to paste the command into a
    terminal: "' '.join(build.getCommand())". It is put together from
    what you provided through the three setters, and from Qt's header
    folder, which is found for you.

    The compiler and its '-std' are those that read Qt's headers when
    the ritual files were generated. A header may give a class other
    functions for another compiler or another standard, as Qt's
    'qfloat16.h' does, and a ritual written from what one of them read
    would then not compile with the other.

    Returns
    -------

    Paths
      A 'Tuple[str, ...]', one argument per entry: 'clang++', then
      '-std=c++17', the standard the headers were read by;
      '-shared', to make a shared object and not a program;
      '-fPIC', so the code can sit at any address;
      '-O2', so the compiler tidies the result;
      '-fvisibility-inlines-hidden', so Qt's inline code leaves no
      scrambled names in the target file;
      '-Wl,--no-undefined', so a ritual calling a function that no Qt
      shared object offers stops the build here, and not the first
      program that opens the target file;
      '-I' with the folder of Qt's headers;
      the path of each ritual file;
      '-o' with the path of the target file;
      the path of each Qt shared object the target file calls into.

    Raises
    ------

    MissingVariable
      One of the three setters has not been called; the message names
      the missing value.

    FileNotFoundError
      'qmake6' is not installed.
    """
    return (
        'clang++', '-std=c++17', '-shared', '-fPIC', '-O2',
        '-fvisibility-inlines-hidden',
        '-Wl,--no-undefined',
        '-I%s' % self.getQtHeaderFolder(), *self.getRitualFiles(),
        '-o', self.getTargetFile(), *self.getQtSharedObjects(),
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
    files lie in the folder 'getQtSharedObjectFolder' gives.

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

  def run(self) -> str:
    """
    Compiles the ritual files into the target file.

    This is the only method that compiles. All three setters must have
    been called first. It returns when 'clang++' has finished, which takes
    one to three seconds per ritual file that includes Qt's headers.

    Returns
    -------

    str
      The full path of the target file, which now exists.

    Raises
    ------

    MissingVariable
      One of the three setters has not been called; the message names
      the missing value.

    FileNotFoundError
      'clang++' or 'qmake6' is not installed.

    RuntimeError
      'clang++' refused the ritual files. Its own message, with the file
      names and line numbers, is included.
    """
    self._run(*self.getCommand())
    return self.getTargetFile()
