"""RitualTester verifies the ritual file a RitualGenerator wrote."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import json
import os
import subprocess
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

from . import HeaderReader, RitualGenerator

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, List, Optional, Set, Tuple

  Record = Dict[str, Any]
  Faults = Tuple[str, ...]


class RitualTester:
  """
  Verifies the ritual file a 'RitualGenerator' wrote. This is the
  tester side of the tooling. It takes nothing the generator says on
  trust: it compiles the file, looks at what came out, and reads the
  record of the class itself.

    tester = RitualTester()
    tester.setRitualGenerator(generator)   # after 'generator.write()'
    tester.test()
    tester.passed()      # True when no fault was found
    tester.getFaults()   # each fault, in words

  Terms
  -----

  - A fault is one thing found wrong, said in a sentence.
  - The target file is the shared object the ritual file is compiled
    into, beside the ritual file, as 'libq_object.so'.
  - The offer file is one line beside the ritual file, written by
    'test', telling 'clang++' that the target file may offer rituals to
    others and nothing else.

  You provide
  -----------

  - 'setRitualGenerator': the generator whose ritual file is to be
    verified, with its three setters called and 'write' done. Required.

  What it checks
  --------------

  1. The ritual file on disk is what the generator would write now,
     and so is the rows file beside it, which reads back as the rows
     the generator decided.
  2. 'clang++' compiles it against Qt's own headers, and finds every Qt
     function it calls in Qt's shared objects. A ritual handing a Qt
     function a wrong type does not compile, and neither does one
     calling a function that Qt declares and offers nowhere.
  3. The target file offers exactly the rituals the generator says it
     wrote: none missing, none besides.
  4. Every ritual is named after a function the class really has, as
     the record of the class has it.
  5. Every function the header declares for the class is accounted
     for: written, or not written with a reason. One more is expected
     for a class C++ can copy that declares no destructor: the
     destructor the compiler writes for it.

  What to expect
  --------------

  - 'test' takes one to three seconds, most of it compiling.
  - A fault is never raised. It is listed, and 'passed' is then False.
    'test' raises only when it cannot test at all.
  - What is not checked yet: that calling a ritual does what calling
    the Qt function does. That needs the same steps run both ways and
    compared.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _run(*command: str) -> Tuple[int, str, str]:
    """
    Runs one program to its end and gives its return code, what it
    printed and what it complained about. A failure is given, not
    raised.

    Raises
    ------

    FileNotFoundError
      The program is not installed on this machine.
    """
    try:
      done = subprocess.run(command, capture_output=True, text=True)
    except FileNotFoundError as fileNotFoundError:
      infoSpec = """The program '%s' is needed and is not installed."""
      raise FileNotFoundError(infoSpec % command[0]) from fileNotFoundError
    return done.returncode, done.stdout, done.stderr

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  What the compiler calls the functions of a class, templates among
  #  them. Kept here on its own, apart from what the generator knows.
  __counted_kinds__ = (
      'CXXConstructorDecl', 'CXXDestructorDecl', 'CXXMethodDecl',
      'CXXConversionDecl', 'FunctionTemplateDecl',
  )

  #  What the offer file says, in the words of the program that puts the
  #  target file together: offer the names beginning with 'ritual' to
  #  others, and keep every other name inside.
  __offer_text__ = '{ global: ritual*; local: *; };\n'

  #  Fallback Variables

  #  Private Variables
  __ritual_generator__ = None  # type: Optional[RitualGenerator]
  __found_faults__ = None  # type: Optional[Faults]
  __compiler_said__ = None  # type: Optional[str]
  __offered_names__ = None  # type: Optional[Tuple[str, ...]]

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getRitualGenerator(self) -> RitualGenerator:
    """
    Gives the generator whose ritual file is verified.

    Provided by you, through 'setRitualGenerator'. Nothing fills it in
    for you.

    Raises
    ------

    MissingVariable
      'setRitualGenerator' has not been called.
    """
    if self.__ritual_generator__ is None:
      raise MissingVariable(self, '__ritual_generator__', RitualGenerator)
    return self.__ritual_generator__

  def getTargetFile(self) -> str:
    """
    Gives the full path of the target file: 'lib', the name of the
    ritual file without its ending, and '.so', beside the ritual file.

    Found for you. Having the path does not mean the file is there;
    'test' makes it.
    """
    generator = self.getRitualGenerator()
    name = 'lib%s.so' % generator.getFileStem()
    return os.path.join(generator.getWorkFolder(), name)

  def getOfferFile(self) -> str:
    """
    Gives the full path of the offer file: the name of the ritual file
    without its ending, and '.offers', beside the ritual file.

    Found for you. The offer file is one line telling 'clang++' which names
    the target file may offer to others: those beginning with 'ritual',
    and no other. Code of Qt's own that the compiler copies into the
    target file while compiling a ritual then stays inside it, unseen.
    Having the path does not mean the file is there; 'test' writes it.
    """
    generator = self.getRitualGenerator()
    name = '%s.offers' % generator.getFileStem()
    return os.path.join(generator.getWorkFolder(), name)

  def getCommand(self) -> Tuple[str, ...]:
    """
    Gives the exact 'clang++' command 'test' compiles with, without
    running it.

    Found for you. The compiler and its '-std' are those the headers
    were read with: see 'HeaderReader.getCompilerCommand'. A header may give
    a class other functions for another compiler or another standard,
    as Qt's 'qfloat16.h' does, and a ritual written from what one of
    them read would then not compile with the other.

    Returns
    -------

    Tuple[str, ...]
      One argument per entry: 'clang++', then
      '-std=c++17', the standard the headers were read by;
      '-shared', to make a shared object and not a program;
      '-fPIC', so the code can sit at any address;
      '-O2', so the compiler tidies the result;
      '-fno-access-control', so the compiler lets a ritual call a
      function C++ marks 'private' or 'protected';
      '-fvisibility-inlines-hidden', so Qt's inline code leaves no
      names of its own in the target file;
      '-Wl,--version-script=' with the path of the offer file, so the
      target file offers nothing but rituals;
      '-Wl,--no-undefined', so a ritual calling a function that no Qt
      shared object offers stops the build, and not the first program
      that opens the target file;
      '-I' with the folder of Qt's headers;
      the path of the ritual file;
      '-o' with the path of the target file;
      the Qt shared object of each part of the dependency tree.
    """
    generator = self.getRitualGenerator()
    headerReaders = generator.getDependencyTree().getHeaderReaders()
    return (
        'clang++', '-std=c++17', '-shared', '-fPIC', '-O2',
        '-fno-access-control', '-fvisibility-inlines-hidden',
        '-Wl,--version-script=%s' % self.getOfferFile(),
        '-Wl,--no-undefined',
        '-I%s' % HeaderReader.getQtHeaderFolder(),
        *generator.getPrivateArguments(), generator.getRitualFile(),
        '-o', self.getTargetFile(),
        *(reader.getQtSharedObject() for reader in headerReaders),
    )

  def _createFaults(self, ) -> None:
    """Runs every check and keeps the faults found."""
    generator = self.getRitualGenerator()
    ritualFile = generator.getRitualFile()
    className = generator.getClassName()
    self.__compiler_said__ = ''
    self.__offered_names__ = ()
    if not os.path.isfile(ritualFile):
      infoSpec = """There is no ritual file at '%s'. Call 'write' on the
      generator first."""
      raise FileNotFoundError(' '.join((infoSpec % ritualFile).split()))
    faults = []  # type: List[str]
    with open(ritualFile) as file:
      onDisk = file.read()
    if onDisk != generator.getRitualText():
      infoSpec = """The ritual file '%s' is not what the generator would
      write now. It was changed by hand, or written from other
      records."""
      faults.append(' '.join((infoSpec % ritualFile).split()))
    rowsFile = generator.getRowsFile()
    onDisk = None  # type: Optional[str]
    if os.path.isfile(rowsFile):
      with open(rowsFile) as file:
        onDisk = file.read()
    if onDisk != generator.getRowsText():
      infoSpec = """The rows file '%s' is not what the generator would
      write now. It is missing, was changed by hand, or was written from
      other records."""
      faults.append(' '.join((infoSpec % rowsFile).split()))
    else:
      #  What the file says has to be read back as the rows themselves.
      try:
        held = json.loads(onDisk)['rows']
      except (ValueError, KeyError) as exception:
        infoSpec = """The rows file '%s' cannot be read back: %s"""
        faults.append(infoSpec % (rowsFile, exception))
      else:
        rows = generator.getRows()
        if held != {name: [*row] for name, row in rows.items()}:
          infoSpec = """The rows file '%s' reads back as other rows
          than the generator decided."""
          faults.append(' '.join((infoSpec % rowsFile).split()))
    written = generator.getWritten()
    notWritten = generator.getNotWritten()
    names = [ritual['ritualName'] for ritual in written]
    for name in sorted({n for n in names if names.count(n) > 1}):
      infoSpec = """The generator wrote two rituals named '%s'."""
      faults.append(infoSpec % name)
    counted, compilerNames = self._countFunctions(className)
    #  Three kinds of ritual stand for no function of the header by
    #  themselves: the one giving where a part of an object is, the one
    #  handing a Python function over, and the one running just the
    #  class's own function, which is named after that function.
    apart = ('cast', 'take', 'own', 'list', 'map')
    for ritual in written:
      name, kind = ritual['ritualName'], ritual['kind']
      if kind in ('cast', 'take', 'list', 'map'):
        continue
      if ritual.get('fromText'):
        #  Read from the text of the header file: the compiler reported
        #  no function for it, so there is no name to hold it against.
        continue
      if ritual.get('compilerName', '') not in compilerNames:
        infoSpec = """The ritual '%s' is named after no function the
        class '%s' has."""
        faults.append(' '.join((infoSpec % (name, className)).split()))
    counting = [r for r in written if r['kind'] not in apart]
    accounted = len(counting) + len(notWritten)
    if accounted != counted:
      infoSpec = """The header declares %d functions for the class '%s',
      and the generator accounts for %d: %d written and %d not."""
      info = infoSpec % (
          counted, className, accounted, len(counting), len(notWritten),
      )
      faults.append(' '.join(info.split()))
    with open(self.getOfferFile(), 'w') as file:
      file.write(self.__offer_text__)
    returnCode, _, complained = self._run(*self.getCommand())
    self.__compiler_said__ = complained.strip()
    if returnCode:
      infoSpec = """'clang++' does not compile the ritual file '%s'. It said:
      %s"""
      faults.append(infoSpec % (ritualFile, complained.strip()))
      self.__found_faults__ = (*faults,)
      return
    offered = self._listOffered()
    self.__offered_names__ = (*sorted(offered),)
    for name in sorted({*names} - offered):
      infoSpec = """The ritual '%s' was written, and the target file does
      not offer it."""
      faults.append(' '.join((infoSpec % name).split()))
    for name in sorted(offered - {*names}):
      infoSpec = """The target file offers '%s', which is no ritual the
      generator wrote."""
      faults.append(' '.join((infoSpec % name).split()))
    self.__found_faults__ = (*faults,)

  def getFaults(self, **kwargs) -> Faults:
    """
    Gives each fault the checks found, in words.

    Found for you: the checks are run at the first call, as 'test'
    does, and the answer kept. You pass nothing; the keyword is for the
    method's own use.

    Returns
    -------

    Faults
      A 'Tuple[str, ...]', one sentence per fault. It is empty when
      every check passed.

    Raises
    ------

    MissingVariable
      'setRitualGenerator' has not been called.

    FileNotFoundError
      The ritual file has not been written, or 'clang++' or 'nm' is not
      installed.
    """
    if self.__found_faults__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      self._createFaults()
      return self.getFaults(_recursion=True)
    return self.__found_faults__

  def getCompilerSaid(self) -> str:
    """
    Gives what 'clang++' printed while compiling: its warnings when it
    compiled, its refusal when it did not, and '' when it said nothing.
    """
    self.getFaults()
    return self.__compiler_said__

  def getOfferedNames(self) -> Tuple[str, ...]:
    """
    Gives the name of everything the target file offers, in
    alphabetical order, as the program 'nm' lists it. It is empty when
    the ritual file did not compile.
    """
    self.getFaults()
    return self.__offered_names__

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setRitualGenerator(self, ritualGenerator: RitualGenerator) -> None:
    """
    Tells the tester which generator's ritual file to verify.

    Required. Calling it again forgets what was found before.

    Parameters
    ----------

    ritualGenerator : RitualGenerator
      A generator with its dependency tree, class name and work folder
      set. Its 'write' must be done before 'test'.

    Raises
    ------

    TypeException
      'ritualGenerator' is not a 'RitualGenerator'.
    """
    if not isinstance(ritualGenerator, RitualGenerator):
      raise TypeException(
          'ritualGenerator', ritualGenerator, RitualGenerator)
    self.__ritual_generator__ = ritualGenerator
    self.__found_faults__ = None
    self.__compiler_said__ = None
    self.__offered_names__ = None

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __str__(self) -> str:
    """Says what is tested and, once tested, how many faults there are."""
    clsName = type(self).__name__
    if self.__ritual_generator__ is None:
      return '<%s still waiting for: setRitualGenerator>' % clsName
    className = self.__ritual_generator__.getClassName()
    if self.__found_faults__ is None:
      return "<%s of the class '%s', not tested yet>" % (clsName, className)
    count = len(self.__found_faults__)
    return "<%s of the class '%s': %d faults>" % (clsName, className, count)

  __repr__ = __str__

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _countFunctions(self, className: str) -> Tuple[int, Set[str]]:
    """
    Reads the record of a class without the help of the generator, and
    gives how many functions the header declares for it, and the
    compiler's own name of each one that has such a name.

    A class C++ can copy that declares no destructor counts one more:
    the destructor the compiler writes for it, under the name the
    compiler gives a destructor, as '_ZN5QSizeD1Ev' for 'QSize'.
    """
    tree = self.getRitualGenerator().getDependencyTree()
    record = tree.getClassRecord(className)
    count, compilerNames = 0, set()  # type: int, Set[str]
    declaresDestructor = False
    for member in record.get('inner', ()):
      if member.get('kind') == 'FriendDecl':
        #  An operator Qt writes inside the class with 'friend' in front
        #  counts as a function declared for the class.
        for friend in member.get('inner', ()):
          if not isinstance(friend, dict) or friend.get('isImplicit'):
            continue
          if friend.get('kind') != 'FunctionDecl':
            continue
          if not friend.get('name', '').startswith('operator'):
            continue
          count += 1
          if 'mangledName' in friend:
            compilerNames.add(friend['mangledName'])
        continue
      if member.get('kind') not in self.__counted_kinds__:
        continue
      if member.get('isImplicit'):
        continue
      count += 1
      if member['kind'] == 'CXXDestructorDecl':
        declaresDestructor = True
      if 'mangledName' in member:
        compilerNames.add(member['mangledName'])
    if not declaresDestructor and className in tree.getCopyableNames():
      count += 1
      words = className.split('::')
      lengths = ''.join('%d%s' % (len(word), word) for word in words)
      compilerNames.add('_ZN%sD1Ev' % lengths)
    return count, compilerNames

  def _listOffered(self) -> Set[str]:
    """
    Gives the name of every function the target file offers, as the
    program 'nm' lists them.

    Raises
    ------

    RuntimeError
      'nm' could not read the target file; its message is included.
    """
    targetFile = self.getTargetFile()
    command = ('nm', '-D', '--defined-only', targetFile)
    returnCode, printed, complained = self._run(*command)
    if returnCode:
      infoSpec = """The program 'nm' could not read '%s': %s"""
      raise RuntimeError(infoSpec % (targetFile, complained.strip()))
    offered = set()  # type: Set[str]
    for line in printed.splitlines():
      words = line.split()
      if len(words) >= 3 and words[-2] in ('T', 't', 'W', 'w'):
        offered.add(words[-1].partition('@')[0])
    return offered

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

  def test(self) -> Faults:
    """
    Runs every check afresh and gives the faults found.

    Returns
    -------

    Faults
      A 'Tuple[str, ...]', one sentence per fault. It is empty when
      every check passed.

    Raises
    ------

    MissingVariable
      'setRitualGenerator' has not been called.

    FileNotFoundError
      The ritual file has not been written, or 'clang++' or 'nm' is not
      installed.
    """
    self.__found_faults__ = None
    return self.getFaults()

  def passed(self) -> bool:
    """Says whether every check passed: 'getFaults' is empty."""
    return not self.getFaults()
