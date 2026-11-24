"""RitualTester verifies the ritual file a RitualGenerator wrote."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import json
import os
import re
import subprocess
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

from . import HeaderFolder, HeaderReader, RitualGenerator

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

  - 'setInstalledFolder': the folder of an installed Qt of the version
    read, as 'tmp/scratch/kit/qt_linux/6.12.0/gcc_64', which holds
    'include', 'lib' and 'mkspecs'. Every ritual file is compiled
    against that Qt and nothing else. Once, for every 'RitualTester'.
    Required.
  - 'setRitualGenerator': the generator whose ritual file is to be
    verified, with its three setters called and 'write' done. Required.

  What it checks
  --------------

  1. The ritual file on disk is what the generator would write now,
     and so is the rows file beside it, which reads back as the rows
     the generator decided.
  2. 'clang++' compiles it against the header files of the installed
     Qt, and finds every Qt function it calls in that Qt's shared
     objects. A ritual handing a Qt function a wrong type does not
     compile, and neither does one calling a function that Qt declares
     and offers nowhere.
  3. The target file offers the rituals the generator says it wrote,
     and nothing besides. A ritual that stands between Qt's own '#if'
     lines is rightly missing where one of them does not hold for the
     installed Qt; the compiler of that Qt is asked which hold. Any
     other ritual has to be there.
  4. Every ritual is named after a function the class really has, as
     the record of the class has it.
  5. Every function the header declares for the class is accounted
     for: written, or not written with a reason. One more is expected
     for a class C++ can copy that declares no destructor: the
     destructor the compiler writes for it.

  What to expect
  --------------

  - 'test' takes one to three seconds, most of it compiling.
  - No Qt that the generator read is used here: only the installed Qt
    given to 'setInstalledFolder', as a user's machine has one.
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

  #  The folder of the installed Qt every ritual file is compiled
  #  against, and what its compiler said of each '#if' asked so far:
  #  whether it holds. Kept for every 'RitualTester'.
  __installed_folder__ = None  # type: Optional[str]
  __held_conditions__ = dict()  # type: Dict[str, bool]
  #  What Qt keeps of the system and the compiler it is built for, in
  #  the folder 'mkspecs' of an installed Qt. The tests run on Linux.
  __spec_name__ = 'linux-g++'

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

  @classmethod
  def getInstalledFolder(cls) -> str:
    """
    Gives the folder of the installed Qt every ritual file is compiled
    against, as 'tmp/scratch/kit/qt_linux/6.12.0/gcc_64'.

    Provided by you, through 'setInstalledFolder'.

    Raises
    ------

    MissingVariable
      'setInstalledFolder' has not been called.
    """
    if cls.__installed_folder__ is None:
      raise MissingVariable(cls, '__installed_folder__', str)
    return cls.__installed_folder__

  @classmethod
  def setInstalledFolder(cls, installedFolder: str) -> None:
    """
    Tells which installed Qt the ritual files are compiled and linked
    against. It has to be of the version the header files were read
    from.

    Raises
    ------

    TypeException
      The path is not text.

    FileNotFoundError
      The folder lacks 'include', 'lib' or 'mkspecs', or holds no
      header files of the version read.
    """
    if not isinstance(installedFolder, str):
      raise TypeException('installedFolder', installedFolder, str)
    installedFolder = os.path.abspath(installedFolder)
    version = HeaderReader.getQtVersion()
    for needed in ('include', 'lib', 'mkspecs',
                   os.path.join('include', 'QtCore', version)):
      if not os.path.isdir(os.path.join(installedFolder, needed)):
        infoSpec = """'%s' is no folder of an installed Qt %s: it has no
        '%s'."""
        info = infoSpec % (installedFolder, version, needed)
        raise FileNotFoundError(' '.join(info.split()))
    cls.__installed_folder__ = installedFolder
    cls.__held_conditions__ = dict()

  def getIncludeFolders(self) -> Tuple[str, ...]:
    """
    Gives the folders the compiler looks in for header files, all in
    the installed Qt: its 'include'; for each part, the four folders a
    header file Qt calls private pulls others in from, as
    'include/QtCore', 'include/QtCore/6.12.0', its 'QtCore' and the
    'private' in that; and 'mkspecs/linux-g++', where Qt keeps
    'qplatformdefs.h'.
    """
    folder = self.getInstalledFolder()
    include = os.path.join(folder, 'include')
    version = HeaderReader.getQtVersion()
    found = [include]
    #  The parts in the order of the alphabet, as the generator reads
    #  them; for a part of 'HeaderReader.getOwnOrderParts' in the order
    #  it sees them, its own first: the compiler takes the first file
    #  it finds by a name, and two parts may each have one, as
    #  'private/qabstractseries_p.h' of QtCharts and of QtGraphs.
    generator = self.getRitualGenerator()
    order = ()  # type: Tuple[str, ...]
    if generator.getPartName() in HeaderReader.getOwnOrderParts():
      order = generator.getDependencyTree().getPartOrder(
          generator.getPartName())
    names = sorted(os.listdir(include))
    names = [
        *(name for name in order if name in names),
        *(name for name in names if name not in order)]
    for name in names:
      versioned = os.path.join(include, name, version)
      if os.path.isdir(os.path.join(versioned, name)):
        found.append(os.path.join(include, name))
        found.append(versioned)
        found.append(os.path.join(versioned, name))
        found.append(os.path.join(versioned, name, 'private'))
    found.append(os.path.join(folder, 'mkspecs', self.__spec_name__))
    return (*found,)

  def _findHeld(self, conditions: Set[str]) -> Dict[str, bool]:
    """
    Gives, for each '#if' condition, whether it holds for the installed
    Qt: its preprocessor reads every one once, after the header files
    that answer them, the public and the private one, of the part of
    the class, of every part it needs, and of every part whose switch
    a condition asks, and says which lines it kept. The answers are
    kept for every 'RitualTester'.

    Those parts only: a header file of a part sees no other, and Qt
    refuses some parts in one file, as QtGraphs with QtCharts.

    Raises
    ------

    RuntimeError
      The preprocessor refused the conditions. Its message is kept.
    """
    kept = self.__held_conditions__
    asked = sorted(c for c in conditions if c not in kept)
    if asked:
      generator = self.getRitualGenerator()
      tree = generator.getDependencyTree()
      held = {reader.getPartName() for reader in tree.getHeaderReaders()}
      wanted, at = [generator.getPartName()], 0
      while at < len(wanted):
        try:
          needs = HeaderFolder.getPartNeeds(wanted[at])
        except LookupError:
          needs = ()
        wanted.extend(need for need in needs if need not in wanted)
        at += 1
      wanted.reverse()
      folder = HeaderReader.getHeaderFolder()
      for condition in asked:
        for switch in re.findall(r'QT_CONFIG\((\w+)\)', condition):
          owner = folder.getSwitchOwner(switch)
          if owner is not None and owner[0] not in wanted:
            wanted.append(owner[0])
      lines = []  # type: List[str]
      version = HeaderReader.getQtVersion()
      for partName in wanted:
        if partName not in held:
          continue
        lines.append('#include <%s/%s>' % (
            partName, HeaderFolder.getGlobalHeader(partName)))
        if not HeaderFolder.getPrivateGlobalHeader(partName):
          #  A part with no private switches of its own, as QtXml.
          continue
        lines.append('#include <%s/%s/%s/private/%s>' % (
            partName, version, partName,
            HeaderFolder.getPrivateGlobalHeader(partName)))
      for index, condition in enumerate(asked):
        lines.extend((
            '#if %s' % condition, 'cutienator_held_%d' % index, '#endif'))
      command = (
          'clang++', '-std=c++17', '-x', 'c++', '-E', '-P',
          *('-I%s' % one for one in self.getIncludeFolders()), '-')
      done = subprocess.run(
          command, input='\n'.join(lines), capture_output=True, text=True)
      if done.returncode:
        infoSpec = """The preprocessor of the installed Qt refused the
        '#if' lines asked of it: %s"""
        info = infoSpec % ' '.join(done.stderr.split())[:1200]
        raise RuntimeError(' '.join(info.split()))
      for index, condition in enumerate(asked):
        found = re.search(r'\bcutienator_held_%d\b' % index, done.stdout)
        kept[condition] = found is not None
    return {condition: kept[condition] for condition in conditions}

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
    were read with: see 'HeaderReader.getCompilerCommand'. A header may
    give a class other functions for another compiler or another
    standard, as Qt's 'qfloat16.h' does, and a ritual written from what
    one of them read would then not compile with the other. Header
    files and shared objects are those of the installed Qt.

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
      '-I' with each folder of 'getIncludeFolders';
      the path of the ritual file;
      '-o' with the path of the target file;
      '-Wl,-rpath,' with the folder of the installed Qt's shared
      objects, so the target file finds them there;
      the installed Qt's shared object of each part of the tree, in
      the order the part of the class sees them, its own first: a name
      two parts offer, as a function of QtGraphs' 'QBarSeries' and of
      QtCharts' one, is found in the first.
    """
    generator = self.getRitualGenerator()
    tree = generator.getDependencyTree()
    partNames = tree.getPartOrder(generator.getPartName())
    library = os.path.join(self.getInstalledFolder(), 'lib')
    return (
        'clang++', '-std=c++17', '-shared', '-fPIC', '-O2',
        '-fno-access-control', '-fvisibility-inlines-hidden',
        '-Wl,--version-script=%s' % self.getOfferFile(),
        '-Wl,--no-undefined',
        *('-I%s' % folder for folder in self.getIncludeFolders()),
        generator.getRitualFile(),
        '-o', self.getTargetFile(),
        '-Wl,-rpath,%s' % library,
        *(path for path in (
            os.path.join(library, 'lib%s.so.6' % partName.replace(
                'Qt', 'Qt6', 1)) for partName in partNames)
          #  A part that is header files alone, as QtQmlIntegration,
          #  has no shared object.
          if os.path.isfile(path)),
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
      start = len('ritual_own') if kind == 'own' else len('ritual')
      if name[start:] not in compilerNames:
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
      answered = [' '.join(r['function'].split()) for r in counting]
      answered.extend(' '.join(n.split()) for n, _ in notWritten)
      twice = sorted({n for n in answered if answered.count(n) > 1})
      if twice:
        info = '%s Answered more than once: %s.' % (info, '; '.join(twice))
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
    #  A ritual between '#if' lines is rightly missing where one of them
    #  does not hold for the installed Qt, and so is every ritual of a
    #  file whose class stands under one that does not hold.
    wholeFile = generator.getFileConditions()
    asked = {*wholeFile}
    for ritual in written:
      asked.update(ritual.get('conditions', ()))
    held = self._findHeld(asked)
    fileHolds = all(held[one] for one in wholeFile)
    for ritual in written:
      name = ritual['ritualName']
      if name in offered:
        continue
      if not fileHolds:
        continue
      if not all(held[one] for one in ritual.get('conditions', ())):
        continue
      infoSpec = """The ritual '%s' was written, and the target file does
      not offer it, though every '#if' line around it holds for the
      installed Qt."""
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
    generator = self.getRitualGenerator()
    tree, partName = generator.getDependencyTree(), generator.getPartName()
    record = tree.getClassRecord(className, partName)
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
    copyable = tree.getClassKey(className, partName) in (
        tree.getCopyableNames())
    if not declaresDestructor and copyable:
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
