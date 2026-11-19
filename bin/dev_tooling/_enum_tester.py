"""EnumTester verifies the enum files an 'EnumGenerator' wrote."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import subprocess
import tempfile
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

from . import QtPart, EnumGenerator

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Dict, List, Optional, Tuple

  Faults = Tuple[str, ...]
  Generators = Tuple[EnumGenerator, ...]


class EnumTester:
  """
  Verifies the files that 'EnumGenerator' wrote for some enums of Qt.
  This is the tester side of the tooling. It takes nothing the generator
  says on trust: it asks the compiler for every number.

    tester = EnumTester()
    tester.setEnumGenerators(*generators)    # after each 'write()'
    tester.test()
    tester.passed()      # True when no fault was found
    tester.getFaults()   # each fault, in words

  A fault is one thing found wrong, said in a sentence.

  What it checks
  --------------

  1. The file of each enum on disk is what its generator would write
     now.
  2. A small C++ program, compiled by 'clang++' against Qt's own
     headers and run once, prints the number of every name of every
     enum. Each has to be the number the file holds. The generator
     took its numbers from what the compiler wrote down while the
     headers were read; this asks the compiler itself.

  All enums are asked for in one program, so the test takes one run of
  the compiler however many enums it is given.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Private Variables
  __enum_generators__ = None  # type: Optional[Generators]
  __found_faults__ = None  # type: Optional[Faults]

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getEnumGenerators(self) -> Generators:
    """Gives the generators whose files are verified."""
    if self.__enum_generators__ is None:
      raise MissingVariable(self, '__enum_generators__', tuple)
    return self.__enum_generators__

  def getFaults(self) -> Faults:
    """
    Gives each fault 'test' found, in words; nothing when it found none.

    Raises
    ------

    MissingVariable
      'test' has not run.
    """
    if self.__found_faults__ is None:
      raise MissingVariable(self, '__found_faults__', tuple)
    return self.__found_faults__

  def passed(self) -> bool:
    """Says whether 'test' found no fault."""
    return False if self.getFaults() else True

  def getProgramText(self) -> str:
    """
    Gives the C++ program that prints, for every name of every enum, a
    line with its number and its full name, as
    '1 Qt::AlignmentFlag::AlignLeft'.
    """
    includeLines = []  # type: List[str]
    printLines = []  # type: List[str]
    lineSpec = '  std::printf("%%lld %%s\\n", (long long)(%s), "%s");'
    for generator in self.getEnumGenerators():
      record, enumName = generator.getEnumRecord(), generator.getEnumName()
      qtParts = generator.getDependencyTree().getQtParts()
      named = [p for p in qtParts if p.getPartName() == record['partName']]
      qtPart = named[0]
      for line in qtPart.getIncludeLines(record['headerPath']).split('\n'):
        if line.strip() and line not in includeLines:
          includeLines.append(line)
      for name, _ in record['members']:
        fullName = '%s::%s' % (enumName, name)
        printLines.append(lineSpec % (fullName, fullName))
    lines = [
      *includeLines,
      '#include <cstdio>',
      '',
      'int main() {',
      *printLines,
      '  return 0;',
      '}',
      '',
    ]
    return '\n'.join(lines)

  def _askCompiler(self) -> Dict[str, int]:
    """
    Compiles the program, runs it, and gives the number it printed
    under each full name.

    Raises
    ------

    RuntimeError
      'clang++' refused the program, or the program did not run. What
      it said is in the message.
    """
    qtParts = self.getEnumGenerators()[0].getDependencyTree().getQtParts()
    with tempfile.TemporaryDirectory() as folder:
      sourceFile = os.path.join(folder, 'enums.cpp')
      programFile = os.path.join(folder, 'enums')
      with open(sourceFile, 'w') as file:
        file.write(self.getProgramText())
      command = (
          'clang++', '-std=c++17', '-fPIC', '-Wno-deprecated-declarations',
          '-I%s' % QtPart.getQtHeaderFolder(), sourceFile,
          '-o', programFile,
          '-Wl,-rpath,%s' % QtPart.getQtSharedObjectFolder(),
          *(qtPart.getQtSharedObject() for qtPart in qtParts),
      )
      said = ''
      for step in (command, (programFile,)):
        done = subprocess.run(
            step, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            universal_newlines=True,
        )
        if done.returncode:
          infoSpec = """Asking the compiler for the numbers of the enums
          failed at '%s', which said: %s"""
          info = infoSpec % (os.path.basename(step[0]), done.stderr)
          raise RuntimeError(' '.join(info.split()))
        said = done.stdout
    numbers = dict()  # type: Dict[str, int]
    for line in said.split('\n'):
      number, _, fullName = line.partition(' ')
      if fullName:
        numbers[fullName] = int(number)
    return numbers

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setEnumGenerators(self, *enumGenerators: EnumGenerator) -> None:
    """
    Tells the tester which files to verify: those of the given
    generators, each with its three setters called and 'write' done.
    What an earlier 'test' found is forgotten.

    Raises
    ------

    TypeException
      One of them is not an 'EnumGenerator'.

    ValueError
      None is given.
    """
    if not enumGenerators:
      infoSpec = """An enum tester needs at least one generator, and
      none was given."""
      raise ValueError(' '.join(infoSpec.split()))
    for enumGenerator in enumGenerators:
      if not isinstance(enumGenerator, EnumGenerator):
        raise TypeException('enumGenerator', enumGenerator, EnumGenerator)
    self.__enum_generators__ = (*enumGenerators,)
    self.__found_faults__ = None

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test(self) -> Faults:
    """
    Runs both checks and keeps what they found.

    Returns
    -------

    Faults
      Each fault, in words; nothing when there is none.

    Raises
    ------

    RuntimeError
      The compiler could not be asked; see '_askCompiler'.
    """
    faults = []  # type: List[str]
    for generator in self.getEnumGenerators():
      enumName, enumFile = generator.getEnumName(), generator.getEnumFile()
      if not os.path.isfile(enumFile):
        infoSpec = """The enum '%s' has no file at '%s'."""
        faults.append(infoSpec % (enumName, enumFile))
        continue
      with open(enumFile) as file:
        onDisk = file.read()
      if onDisk != generator.getEnumText():
        infoSpec = """The file of the enum '%s' is not what its generator
        would write now."""
        faults.append(' '.join((infoSpec % enumName).split()))
    asked = self._askCompiler()
    for generator in self.getEnumGenerators():
      enumName = generator.getEnumName()
      for name, number in generator.getEnumRecord()['members']:
        fullName = '%s::%s' % (enumName, name)
        if fullName not in asked:
          infoSpec = """The compiler printed no number for '%s'."""
          faults.append(infoSpec % fullName)
        elif (asked[fullName] - number) % (1 << 64):
          infoSpec = """'%s' is %d in the file and %d to the compiler."""
          faults.append(infoSpec % (fullName, number, asked[fullName]))
    self.__found_faults__ = (*faults,)
    return self.__found_faults__
