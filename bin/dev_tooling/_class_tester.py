"""ClassTester verifies the Python file of a cute class that
'ClassGenerator' wrote."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import ast
import os
import subprocess
import sys
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

from . import ClassGenerator

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Dict, List, Optional, Tuple

  Faults = Tuple[str, ...]


class ClassTester:
  """
  Verifies the file of a cute class that a 'ClassGenerator' wrote. This
  is the tester side of the tooling. It takes nothing the generator
  says on trust: it reads the file as Python reads it, compares what it
  calls with the rows of the rituals, and has a Python of its own make
  the class.

    tester = ClassTester()
    tester.setClassGenerator(generator)    # after 'generator.write()'
    tester.test()
    tester.passed()      # True when no fault was found
    tester.getFaults()   # each fault, in words

  Terms
  -----

  - A fault is one thing found wrong, said in a sentence.
  - A ritual and a row are as 'RitualGenerator' explains them.

  You provide
  -----------

  - 'setClassGenerator': the generator whose file is to be verified,
    with its four setters called and 'write' done. Required.

  What it checks
  --------------

  1. The file on disk is what the generator would write now, and so is
     the file of each enum Qt writes inside the class.
  2. The file is Python as Python 3.7 reads it, and no line of it is
     longer than 77 letters.
  3. Every ritual the file calls is one the ritual file of the class
     has, and is handed as many things as its row says it takes.
  4. Every ritual of the class is accounted for: the file calls it, or
     the generator lists it as left out with a reason. None is both.
  5. No two functions of one name are given the same signature.
  6. A Python of its own brings in the file, in the package the file
     lies in, and finds the class there.

  What to expect
  --------------

  - A fault is never raised. It is listed, and 'passed' is then False.
    'test' raises only when it cannot test at all.
  - Check 6 needs every file the class file brings in to be there, so
    the classes it names are written before it is tested.
  - What is not checked: that calling a function does what calling the
    Qt function does.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables

  #  Fallback Variables

  #  Private Variables
  __class_generator__ = None  # type: Optional[ClassGenerator]
  __found_faults__ = None  # type: Optional[Faults]

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getClassGenerator(self) -> ClassGenerator:
    """
    Gives the generator whose file is verified.

    Provided by you, through 'setClassGenerator'.

    Raises
    ------

    MissingVariable
      'setClassGenerator' has not been called.
    """
    if self.__class_generator__ is None:
      raise MissingVariable(self, '__class_generator__', ClassGenerator)
    return self.__class_generator__

  def getFaults(self) -> Faults:
    """
    Gives the faults the last 'test' found, each as a sentence.

    Raises
    ------

    MissingVariable
      'test' has not been called.
    """
    if self.__found_faults__ is None:
      raise MissingVariable(self, '__found_faults__', tuple)
    return self.__found_faults__

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setClassGenerator(self, classGenerator: ClassGenerator) -> None:
    """
    Tells the tester which generator's file to verify.

    Required. Calling it again forgets the faults found before.

    Raises
    ------

    TypeException
      'classGenerator' is not a 'ClassGenerator'.
    """
    if not isinstance(classGenerator, ClassGenerator):
      raise TypeException('classGenerator', classGenerator, ClassGenerator)
    self.__class_generator__ = classGenerator
    self.__found_faults__ = None

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __str__(self) -> str:
    """Says which class this is for, or that the setter is still due."""
    clsName = type(self).__name__
    if self.__class_generator__ is None:
      return '<%s still waiting for: setClassGenerator>' % clsName
    className = self.__class_generator__.getClassName()
    return "<%s of the class '%s'>" % (clsName, className)

  __repr__ = __str__

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _checkFiles(self, faults: List[str]) -> Optional[str]:
    """
    Compares the file of the class, and of each enum inside it, with
    what the generators would write now.

    Returns
    -------

    Optional[str]
      The text of the class file as it is on disk, or None when it
      holds something else than the generator would write.
    """
    generator = self.getClassGenerator()
    classFile = generator.getClassFile()
    if not os.path.isfile(classFile):
      infoSpec = """There is no file at '%s'. Call 'write' on the
      generator first."""
      raise FileNotFoundError(' '.join((infoSpec % classFile).split()))
    with open(classFile) as file:
      onDisk = file.read()
    if onDisk != generator.getClassText():
      infoSpec = """The file '%s' is not what the generator would write
      now. It was changed by hand, or written from other records."""
      faults.append(' '.join((infoSpec % classFile).split()))
      return None
    return onDisk

  def _checkText(self, text: str, faults: List[str]) -> Optional[ast.AST]:
    """
    Reads the file as Python 3.7 reads it and measures its lines.

    Returns
    -------

    Optional[ast.AST]
      What Python made of the file, or None when it is no Python.
    """
    classFile = self.getClassGenerator().getClassFile()
    for number, line in enumerate(text.split('\n'), 1):
      if len(line) > 77:
        infoSpec = """Line %d of '%s' is %d letters long, and no line is
        to be longer than 77."""
        info = infoSpec % (number, classFile, len(line))
        faults.append(' '.join(info.split()))
    try:
      return ast.parse(text, classFile, feature_version=(3, 7))
    except SyntaxError as syntaxError:
      infoSpec = """'%s' is not Python as Python 3.7 reads it: %s"""
      faults.append(infoSpec % (classFile, syntaxError))
      return None

  @staticmethod
  def _findCalls(tree: ast.AST) -> List[Tuple[str, int, bool]]:
    """
    Gives every call of a ritual the file makes: the name of the
    ritual, how many things it is handed, and whether it is called on
    the ugly side of an object, which hands the address of the object
    over as well.
    """
    found = []  # type: List[Tuple[str, int, bool]]
    for node in ast.walk(tree):
      if not isinstance(node, ast.Call) or not node.args:
        continue
      function = node.func
      if not isinstance(function, ast.Attribute):
        continue
      if function.attr not in ('call', '_callAs'):
        continue
      #  'self._callAs' is handed the class of Qt before the ritual, and
      #  the address of the object as 'self.uglySide.call' is.
      asPart = function.attr == '_callAs'
      taken = node.args[1:] if asPart else node.args
      if not taken:
        continue
      first = taken[0]
      if not isinstance(first, ast.Constant):
        continue
      if not isinstance(first.value, str):
        continue
      handed = 0
      for arg in taken[1:]:
        #  The texts a program was started with are handed over as two
        #  things, by one argument with a star.
        handed += 2 if isinstance(arg, ast.Starred) else 1
      holder = function.value
      onObject = asPart or isinstance(holder, ast.Attribute) and (
          holder.attr == 'uglySide')
      found.append((first.value, handed, onObject))
    return found

  def _checkCalls(self, tree: ast.AST, faults: List[str]) -> None:
    """Compares the rituals the file calls with the rituals of the
    class and their rows, and with what the generator left out."""
    generator = self.getClassGenerator()
    className = generator.getClassName()
    plans = dict()  # type: Dict[str, Tuple[str, ...]]
    shown = dict()  # type: Dict[str, str]
    #  The file holds the class and every class Qt writes inside it.
    everyOne = generator.getAllGenerators()
    named = []  # type: List[str]
    for one in everyOne:
      for plan in one.getRitualGenerator().getWritten():
        if plan['kind'] == 'cast':
          #  No function of Qt: the class names it for the class it is
          #  built on after the first, when that one has a cute class.
          if plan['baseName'] in one.getFurtherBaseNames():
            named.append(plan['ritualName'])
          continue
        plans[plan['ritualName']] = plan['row']
        shown[plan['function']] = plan['ritualName']
    texts = {
        node.value for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }
    for ritualName in named:
      if ritualName not in texts:
        infoSpec = """The file of '%s' does not name the ritual '%s',
        which gives where a part of an object is."""
        faults.append(' '.join((infoSpec % (className, ritualName)).split()))
    called = set()
    for ritualName, handed, onObject in self._findCalls(tree):
      called.add(ritualName)
      if ritualName not in plans:
        infoSpec = """The file of '%s' calls the ritual '%s', which the
        ritual file of the class does not have."""
        info = infoSpec % (className, ritualName)
        faults.append(' '.join(info.split()))
        continue
      taken = len(plans[ritualName]) - 1
      if handed + (1 if onObject else 0) != taken:
        infoSpec = """The file of '%s' hands the ritual '%s' %d things,
        and its row says it takes %d."""
        info = infoSpec % (
            className, ritualName, handed + (1 if onObject else 0), taken)
        faults.append(' '.join(info.split()))
    leftOut = set()
    listed = [pair for one in everyOne for pair in one.getLeftOut()]
    for function, _ in listed:
      if function not in shown:
        infoSpec = """The generator lists '%s' as left out, and the class
        '%s' has no ritual for it."""
        faults.append(' '.join((infoSpec % (function, className)).split()))
        continue
      leftOut.add(shown[function])
    for ritualName in sorted({*plans} - called - leftOut):
      infoSpec = """The ritual '%s' is neither called by the file of '%s'
      nor listed as left out."""
      info = infoSpec % (ritualName, className)
      faults.append(' '.join(info.split()))
    for ritualName in sorted(called & leftOut):
      infoSpec = """The ritual '%s' is called by the file of '%s' and
      listed as left out as well."""
      info = infoSpec % (ritualName, className)
      faults.append(' '.join(info.split()))

  def _checkSignatures(self, faults: List[str]) -> None:
    """Looks for two functions of one name given the same signature."""
    generator = self.getClassGenerator()
    taken = dict()  # type: Dict[Tuple, str]
    functions = [
        (one.getClassName(), function)
        for one in generator.getAllGenerators()
        for function in one.getFunctions()
    ]
    for holderName, function in functions:
      pairs = zip(function['signatures'], function['signatureKeys'])
      for signature, known in pairs:
        #  A signature goes by the classes it takes, whatever names the
        #  file writes them by.
        key = (holderName, function['pythonName'], known)
        if key in taken:
          infoSpec = """'%s' and '%s' are both given the signature (%s)
          at the name '%s'."""
          info = infoSpec % (
              taken[key], function['plan']['function'],
              ', '.join(signature), function['pythonName'],
          )
          faults.append(' '.join(info.split()))
        taken[key] = function['plan']['function']

  def _checkMaking(self, faults: List[str]) -> None:
    """Has a Python of its own bring in the file and find the class."""
    generator = self.getClassGenerator()
    workFolder = generator.getWorkFolder()
    packageName = os.path.basename(workFolder)
    moduleName = '%s.%s.%s' % (
        packageName, generator.getPartName(), generator.getFileStem())
    pythonName = generator.getPythonName()
    codeSpec = """import importlib
module = importlib.import_module(%r)
for dotted, qtName in %r:
  cls = module
  for name in dotted.split('.'):
    cls = getattr(cls, name)
  assert cls.__qt_class__ == qtName, cls.__qt_class__
  assert cls.__qualname__ == dotted, cls.__qualname__
"""
    #  The class, and each class Qt writes inside it, where C++ has it.
    expected = [
        (one.getDottedName(), one.getClassName())
        for one in generator.getAllGenerators()
    ]
    code = codeSpec % (moduleName, expected)
    environment = dict(os.environ)
    known = environment.get('PYTHONPATH', '')
    folders = [os.path.dirname(workFolder), *known.split(os.pathsep)]
    environment['PYTHONPATH'] = os.pathsep.join(f for f in folders if f)
    done = subprocess.run(
        (sys.executable, '-B', '-c', code), capture_output=True,
        text=True, env=environment,
    )
    if done.returncode:
      said = done.stderr.strip().splitlines()
      infoSpec = """A Python of its own does not make the class '%s' from
      '%s'. It said: %s"""
      info = infoSpec % (
          pythonName, generator.getClassFile(), said[-1] if said else '',
      )
      faults.append(' '.join(info.split()))

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
    Runs every check and gives the faults found.

    Returns
    -------

    Faults
      A 'Tuple[str, ...]', each fault as a sentence. It is empty when
      nothing was found wrong.

    Raises
    ------

    MissingVariable
      'setClassGenerator' has not been called.

    FileNotFoundError
      The generator has written no file yet.
    """
    faults = []  # type: List[str]
    text = self._checkFiles(faults)
    if text is not None:
      tree = self._checkText(text, faults)
      if tree is not None:
        self._checkCalls(tree, faults)
        self._checkSignatures(faults)
        self._checkMaking(faults)
    self.__found_faults__ = (*faults,)
    return self.__found_faults__

  def passed(self) -> bool:
    """Says whether the last 'test' found no fault."""
    return False if self.getFaults() else True
