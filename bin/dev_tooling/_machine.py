"""Machine says what the system the dev tooling runs on calls things."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import contextlib
import os
import platform
import subprocess
import tempfile
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Dict, Iterator, Optional, Sequence, Set, Tuple

  Words = Tuple[str, ...]


class Machine:
  """
  Says what the system the dev tooling runs on calls the things the
  tooling asks for: the folder of Qt's source with 'qplatformdefs.h'
  for it, what 'clang++' is told there, and the program that turns the
  compiler's own name of a function back into C++.

    Machine.getSpecName()       # 'linux-g++' on Linux
    Machine.getCompilerFlags()  # ('-fPIC',) on Linux
    Machine.getDemangler()      # ('c++filt',) on Linux
    Machine.getLibraryName('q_object')  # 'libq_object.so' on Linux
    Machine.listOffered(path)   # the names a built library offers
    with Machine.handOver(command) as words:   # a long command, as
      subprocess.run(words)                    # Windows takes it

  Everything is called on the class: a run of the tooling has one
  machine.

  Terms
  -----

  - The system is the one Python runs on, as 'platform.system()' names
    it: 'Linux', 'Darwin' for macOS, and 'Windows'.
  - On Windows the reader and the generator compile as MinGW does, not
    as Visual Studio does: the generator reads the compiler's own
    names of functions the way Linux and macOS write them, as
    '_ZNK7QObject6threadEv', and Visual Studio writes them otherwise,
    as '?thread@QObject@@QEBAPEAVQThread@@XZ'. For that, 'clang++'
    finds the header files of MinGW through the 'gcc' of MinGW in
    'PATH'. The tester builds as cutienator's 'Build' does there, for
    the Qt of Visual Studio, and does not ask this class how.

  What to expect
  --------------

  - On a system none of the three, every getter raises
    'NotImplementedError', naming the system.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The folder in Qt's source 'mkspecs' of each system: what Qt keeps
  #  of the system and the compiler it is built for, as
  #  'qplatformdefs.h'. On Windows that of 'clang++' as MinGW.
  __spec_names__ = dict(
      Linux='linux-g++', Darwin='macx-clang', Windows='win32-clang-g++',
  )  # type: Dict[str, str]

  #  What 'clang++' is told on each system beside what it is told on
  #  every one. Qt's headers insist on '-fPIC' where there is such a
  #  thing; on Windows 'clang++' is told to compile as MinGW does.
  __compiler_flags__ = dict(
      Linux=('-fPIC',), Darwin=('-fPIC',),
      Windows=('--target=x86_64-w64-windows-gnu',),
  )  # type: Dict[str, Words]

  #  The program that turns the compiler's own name of a function back
  #  into C++. LLVM's comes with 'clang++' on Windows. That of macOS
  #  drops a '_' in front of each name unless told '-n', since names
  #  in an object file of macOS carry one more; the names the
  #  generator reads have none, as on the other systems.
  __demanglers__ = dict(
      Linux=('c++filt',), Darwin=('c++filt', '-n'),
      Windows=('llvm-cxxfilt',),
  )  # type: Dict[str, Words]

  #  The file name of a shared object built from a ritual file, from
  #  the name of the ritual file without its ending.
  __library_names__ = dict(
      Linux='lib%s.so', Darwin='lib%s.dylib', Windows='%s.dll',
  )  # type: Dict[str, str]

  #  The length of a command, in letters, above which Windows gets it
  #  in a file: see 'handOver'. The same as cutienator's 'Build' uses.
  __long_command__ = 8000

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def getSystemName(cls) -> str:
    """
    Gives the system the tooling runs on: 'Linux', 'Darwin' or
    'Windows'.

    Raises
    ------

    NotImplementedError
      It is none of the three.
    """
    system = platform.system()
    if system not in cls.__spec_names__:
      infoSpec = """The dev tooling runs on Linux, macOS and Windows, and
      Python says this system is '%s'."""
      raise NotImplementedError(' '.join((infoSpec % system).split()))
    return system

  @classmethod
  def getSpecName(cls) -> str:
    """Gives the folder in Qt's source 'mkspecs' of the system, as
    'linux-g++' on Linux and 'macx-clang' on macOS, where Qt keeps its
    'qplatformdefs.h' for it."""
    return cls.__spec_names__[cls.getSystemName()]

  @classmethod
  def getCompilerFlags(cls) -> Words:
    """Gives what 'clang++' is told on the system beside what it is told
    on every one, as ('-fPIC',) on Linux."""
    return cls.__compiler_flags__[cls.getSystemName()]

  @classmethod
  def getDemangler(cls) -> Words:
    """Gives the program, with what it is told, that reads the
    compiler's own names of functions, one to a line, and writes each
    back as C++, as ('c++filt',) on Linux."""
    return cls.__demanglers__[cls.getSystemName()]

  @classmethod
  def getLibraryName(cls, stem: str) -> str:
    """Gives the file name of the shared object built from a ritual
    file, from its name without the ending: 'libq_object.so' on Linux,
    'libq_object.dylib' on macOS and 'q_object.dll' on Windows."""
    return cls.__library_names__[cls.getSystemName()] % stem

  @classmethod
  def listOffered(cls, path: str) -> Set[str]:
    """
    Gives the name of every function a built shared object offers to
    others, as the compiler names it, as '_ZNK7QObject6threadEv'.

    Found by the program 'nm': on Linux 'nm -D --defined-only', on
    macOS 'nm -gU', which writes each name with a '_' more in front. On
    Windows a DLL keeps what it offers in a table of its own, which
    LLVM's 'llvm-readobj --coff-exports' lists, a name to a line, as
    'Name: ritual_ZNK7QObject6threadEv'.

    Raises
    ------

    RuntimeError
      'nm' or 'llvm-readobj' could not read the file; its message is
      included.
    """
    system = cls.getSystemName()
    if system == 'Linux':
      command = ('nm', '-D', '--defined-only', path)
    elif system == 'Darwin':
      command = ('nm', '-gU', path)
    else:
      command = ('llvm-readobj', '--coff-exports', path)
    done = subprocess.run(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        universal_newlines=True)
    if done.returncode:
      infoSpec = """The program '%s' could not read '%s': %s"""
      raise RuntimeError(
          infoSpec % (command[0], path, done.stderr.strip()))
    offered = set()  # type: Set[str]
    if system == 'Windows':
      for line in done.stdout.splitlines():
        words = line.split()
        if len(words) == 2 and words[0] == 'Name:':
          offered.add(words[1])
      return offered
    for line in done.stdout.splitlines():
      words = line.split()
      if len(words) < 3 or words[-2] not in ('T', 't', 'W', 'w'):
        continue
      name = words[-1].partition('@')[0]
      if system == 'Darwin' and name.startswith('_'):
        name = name[1:]
      offered.add(name)
    return offered

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  @contextlib.contextmanager
  def handOver(cls, command: Sequence[str]) -> Iterator[Words]:
    """
    Gives the command to start, in the 'with' it opens, as the system
    takes it: on Windows a command of 'clang++' longer than
    '__long_command__' letters goes in a file, as 'clang++ @file', the
    way cutienator's 'Build' hands it over; anywhere else the command
    as it is. The file is removed when the 'with' ends, so the program
    has to have ended by then.

    Windows starts no program whose command is longer than 32767
    letters, and says so as a 'FileNotFoundError' ('[WinError 206]'),
    as if the program were missing. The commands of the reader, the
    tree and the generator name the folders of every part Qt calls
    private, some 57000 letters.

    Parameters
    ----------

    command : Sequence[str]
      The program, then each of its arguments, one per entry.
    """
    words = (*command,)
    told = None  # type: Optional[str]
    tooLong = sum(len(word) + 3 for word in words) > cls.__long_command__
    if tooLong and cls.getSystemName() == 'Windows' and (
        os.path.basename(words[0]).startswith('clang')):
      #  One word to a line, between quotes, as 'clang++' reads a file
      #  of them when told '--rsp-quoting=posix', on any system.
      handle, told = tempfile.mkstemp(prefix='dev-tooling-', suffix='.txt')
      with os.fdopen(handle, 'w', encoding='utf-8') as file:
        for word in words[1:]:
          word = word.replace('\\', '\\\\').replace('"', '\\"')
          file.write('"%s"\n' % word)
      words = (words[0], '--rsp-quoting=posix', '@%s' % told)
    try:
      yield words
    finally:
      if told is not None:
        os.remove(told)
