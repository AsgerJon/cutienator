"""EnumGenerator writes the cute file of one enum of Qt."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import keyword
import os
import textwrap
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

from . import DependencyTree, HeaderReader
from .class_tables import PYTHON_WORDS

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, Optional, Tuple

  Record = Dict[str, Any]
  Members = Tuple[Tuple[str, int], ...]


class EnumGenerator:
  """
  Writes the class of one enum of Qt: a class based on 'CuteNum', or on
  'CuteFlags' for an enum Qt combines into flags, holding every name Qt
  gives in the enum with its number. The class is written inside the
  class or namespace Qt writes the enum inside, where C++, PySide6 and
  PyQt have it, as 'Qt.AlignmentFlag' and 'QWidget.RenderFlag'.

    generator = EnumGenerator()
    generator.setDependencyTree(tree)
    generator.setPartName('QtCore')
    generator.setEnumName('Qt::AlignmentFlag')
    generator.getNestedLines()    # the lines of 'class AlignmentFlag'

  What to expect
  --------------

  - It writes no file. 'ClassGenerator' puts the lines into the body of
    the class Qt writes the enum inside, and 'NamespaceGenerator' into
    the body of a namespace. The class is named as Qt names the enum,
    and has no other name anywhere.
  - The names are written as Qt writes them, in its order. Where a
    name is a word of Python, the word of C stands in: 'NULL', 'TRUE',
    'FALSE'.
  - An enum is a flags enum when Qt names a type for its combinations,
    as 'Qt::Alignment' for 'Qt::AlignmentFlag'. Its numbers are written
    as Qt mostly writes them, in base 16.
  - A flags class says which C++ number it is when that is not 'int'.
    The header says it for some enums; for the others it follows from
    the numbers, as the compiler has it: no sign when a number needs
    the last bit.
  - An enum that code outside its class may not use, or whose numbers
    the compiler did not write down as whole numbers, is refused;
    'findRefusal' says why.
  - The numbers are what the compiler wrote down when the headers were
    read. 'EnumTester' asks the compiler again and compares.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def getStem(cppName: str) -> str:
    """
    Gives a name of Qt in small letters, with an underscore before each
    word: 'QMessageBox' gives 'q_message_box', and 'Qt' gives 'qt'.
    """
    stem = []
    for letter in cppName.replace('::', '__'):
      if letter.isupper() and stem and stem[-1] != '_':
        stem.append('_')
      stem.append(letter.lower())
    return ''.join(stem)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The C++ numbers a flags class may be, as 'CuteFlagsSpace' has them:
  #  how many bits, and whether there is a sign.
  __number_layouts__ = {
    'signed char'       : (8, True),
    'unsigned char'     : (8, False),
    'short'             : (16, True),
    'unsigned short'    : (16, False),
    'int'               : (32, True),
    'unsigned int'      : (32, False),
    'long long'         : (64, True),
    'unsigned long long': (64, False),
  }

  #  Private Variables
  __dependency_tree__ = None  # type: Optional[DependencyTree]
  __enum_name__ = None  # type: Optional[str]
  __part_name__ = None  # type: Optional[str]
  __work_folder__ = None  # type: Optional[str]

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getDependencyTree(self) -> DependencyTree:
    """Gives the tree the enum is taken from; see 'setDependencyTree'."""
    if self.__dependency_tree__ is None:
      raise MissingVariable(self, '__dependency_tree__', DependencyTree)
    return self.__dependency_tree__

  def getEnumName(self) -> str:
    """Gives the full name of the enum, as 'Qt::AlignmentFlag'."""
    if self.__enum_name__ is None:
      raise MissingVariable(self, '__enum_name__', str)
    return self.__enum_name__

  def getWorkFolder(self) -> str:
    """Gives the folder of the cutienator package; see 'setWorkFolder'."""
    if self.__work_folder__ is None:
      raise MissingVariable(self, '__work_folder__', str)
    return self.__work_folder__

  def getEnumRecord(self) -> Record:
    """
    Gives what the tree says of the enum; see
    'DependencyTree.getEnumRecord'.

    Raises
    ------

    ValueError
      The tree holds no enum of that name with names in it.
    """
    return self.getDependencyTree().getEnumRecord(
        self.getEnumName(), self.getPartName())

  def getPartName(self) -> str:
    """
    Gives the part of Qt the enum is written in, as 'QtCore'; every
    name the generator meets is seen from it, as 'DependencyTree' has
    it. Provided by you, through 'setPartName'.

    Raises
    ------

    MissingVariable
      'setPartName' has not been called.
    """
    if self.__part_name__ is None:
      raise MissingVariable(self, '__part_name__', str)
    return self.__part_name__

  def getOwnerName(self) -> str:
    """
    Gives the class or namespace Qt writes the enum inside, as 'Qt' or
    'QPainter', or '' for an enum written inside nothing.
    """
    return self.getEnumRecord()['ownerName']

  def getOwnName(self) -> str:
    """Gives the name of the enum without its owner: 'AlignmentFlag'."""
    return self.getEnumRecord()['ownName']

  def getFlagsName(self) -> Optional[str]:
    """
    Gives the full name Qt has for the combinations of the enum, as
    'Qt::Alignment' for 'Qt::AlignmentFlag', or None for an enum Qt
    does not combine.

    Found for you among the other names for types that the tree keeps:
    Qt declares such a name as 'QFlags' of the enum.
    """
    wanted = 'QFlags<%s>' % self.getEnumName()
    aliasTypes = self.getDependencyTree().getAliasTypes(self.getPartName())
    for aliasName in sorted(aliasTypes):
      if aliasTypes[aliasName] == wanted:
        return aliasName
    return None

  def isFlags(self) -> bool:
    """Says whether Qt combines the names of the enum into flags."""
    return False if self.getFlagsName() is None else True

  def getNumberName(self) -> str:
    """
    Gives the C++ number the names of the enum are kept as, in the
    words the rows files of the rituals use, as 'int' or 'unsigned
    int'.

    Found for you: the number the header fixes for the enum, as the
    compiler reads it, or else what follows from the numbers.

    Raises
    ------

    ValueError
      The header fixes a C++ number that is not the same on every
      system, as 'long'.
    """
    enumName = self.getEnumName()
    fixedTypes = self.getDependencyTree().getEnumTypes(self.getPartName())
    if enumName in fixedTypes:
      numberName = fixedTypes[enumName][1]
      if numberName not in self.__number_layouts__:
        infoSpec = """The enum '%s' is kept as the C++ number '%s', which
        is not one a flags class may be."""
        info = infoSpec % (enumName, numberName)
        raise ValueError(' '.join(info.split()))
      return numberName
    numbers = [number for _, number in self.getEnumRecord()['members']]
    low, high = min(numbers), max(numbers)
    if low < 0:
      fits = -(1 << 31) <= low and high < (1 << 31)
      return 'int' if fits else 'long long'
    if high < (1 << 31):
      return 'int'
    return 'unsigned int' if high < (1 << 32) else 'unsigned long long'

  def getMembers(self) -> Members:
    """
    Gives each name of the enum as the file writes it, with its number,
    in the order Qt writes them.

    Raises
    ------

    ValueError
      A name is a word of Python that no word stands in for, or two
      names would be written alike.
    """
    enumName, members, seen = self.getEnumName(), [], set()
    for name, number in self.getEnumRecord()['members']:
      if keyword.iskeyword(name):
        if name not in PYTHON_WORDS:
          infoSpec = """'%s::%s' is a word of Python, and no word is
          decided to stand in for it."""
          info = infoSpec % (enumName, name)
          raise ValueError(' '.join(info.split()))
        name = PYTHON_WORDS[name]
      if name in seen:
        infoSpec = """Two names of '%s' would both be written '%s'."""
        raise ValueError(infoSpec % (enumName, name))
      seen.add(name)
      members.append((name, number))
    return (*members,)

  def findRefusal(self) -> Optional[str]:
    """
    Says why the enum is not written, or gives None for one that is.

    Returns
    -------

    Optional[str]
      'not for others' for an enum written where code outside its class
      may not use it, 'numbers not known' for one whose numbers the
      compiler did not write down as whole numbers, or None.
    """
    record = self.getEnumRecord()
    if record['access'] != 'public':
      return 'not for others'
    if record['unsure'] is not None:
      return 'numbers not known'
    return None

  def _getHeading(self) -> str:
    """Says who wrote a file, from what, and that it is written anew."""
    headerPath = self.getEnumRecord()['headerPath']
    relative = os.path.relpath(headerPath, HeaderReader.getQtHeaderFolder())
    infoSpec = """Written by dev_tooling.EnumGenerator from the records
    of %s, Qt %s. Changes made here are lost."""
    info = infoSpec % (relative, HeaderReader.getQtVersion())
    return ' '.join(info.split())

  def _getMemberLine(self, name: str, number: int) -> str:
    """Gives the line of the class body that declares one name."""
    if not self.isFlags():
      line = '  %s = Kee[int](%d)' % (name, number)
      if len(line) > 77:
        line = '  %s = Kee[int](\n      %d)' % (name, number)
      return line
    written = hex(number) if number >= 0 else str(number)
    return '  %s = %s' % (name, written)

  def getNestedLines(self, width: int = 77) -> List[str]:
    """
    Gives the class of the enum as the lines that stand in the body of
    the class or namespace Qt writes the enum inside, where C++,
    PySide6 and PyQt have it: 'QCalendarWidget.VerticalHeaderFormat'.
    """
    enumName, ownName = self.getEnumName(), self.getOwnName()
    refusal = self.findRefusal()
    if refusal is not None:
      infoSpec = """The enum '%s' is not written: %s."""
      raise ValueError(infoSpec % (enumName, refusal))
    members, flagsName = self.getMembers(), self.getFlagsName()
    if flagsName is None:
      kind, statement = 'enum', 'CuteNum'
    else:
      kind, statement = 'flags enum', 'CuteFlags'
      numberName = self.getNumberName()
      if numberName != 'int':
        statement = """CuteFlags, number='%s'""" % numberName
    scoped = True if self.getEnumRecord()['scoped'] else False
    if scoped:
      statement = '%s, scoped=True' % statement
    infoSpec = """The %s '%s' of Qt, with the %d names Qt gives in it."""
    about = infoSpec % (kind, enumName, len(members))
    if flagsName is not None:
      infoSpec = """%s Qt names the type of its combinations '%s'."""
      about = infoSpec % (about, flagsName)
    if scoped:
      infoSpec = """%s C++ keeps these names inside the enum, so the
      class that holds the enum does not have them."""
      about = ' '.join((infoSpec % about).split())
    lines = ['  class %s(%s):' % (ownName, statement)]
    wrapped = textwrap.wrap(about, width - 4)
    if len(wrapped) == 1 and len(wrapped[0]) <= width - 10:
      lines.append('    """%s"""' % wrapped[0])
    else:
      lines.append('    """')
      lines.extend('    %s' % line for line in wrapped)
      lines.append('    """')
    lines.append('')
    for name, number in members:
      written = self._getMemberLine(name, number)
      lines.extend('  %s' % line for line in written.split('\n'))
    return lines

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setDependencyTree(self, dependencyTree: DependencyTree) -> None:
    """
    Tells the generator which tree to take the enum from.

    Required before everything else. Calling it again replaces the tree
    given before.

    Raises
    ------

    TypeException
      'dependencyTree' is not a 'DependencyTree'.
    """
    if not isinstance(dependencyTree, DependencyTree):
      raise TypeException('dependencyTree', dependencyTree, DependencyTree)
    self.__dependency_tree__ = dependencyTree

  def setEnumName(self, enumName: str) -> None:
    """
    Tells the generator which enum to write, by its full name, as
    'Qt::AlignmentFlag'.

    Raises
    ------

    TypeException
      'enumName' is not text.
    """
    if not isinstance(enumName, str):
      raise TypeException('enumName', enumName, str)
    self.__enum_name__ = enumName

  def setPartName(self, partName: str) -> None:
    """
    Tells the generator which part of Qt the enum is written in, as
    'QtCore': two parts may each write an enum by one name.

    Raises
    ------

    TypeException
      'partName' is not text.
    """
    if not isinstance(partName, str):
      raise TypeException('partName', partName, str)
    self.__part_name__ = partName

  def setWorkFolder(self, workFolder: str) -> None:
    """
    Tells the generator where the cutienator package is, as
    'src/cutienator'. The file is written into the folder of its part
    of Qt inside it, which has to exist.

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __str__(self) -> str:
    try:
      enumName = self.getEnumName()
    except MissingVariable:
      return '<EnumGenerator, no enum named yet>'
    return '<EnumGenerator of %s>' % enumName

  __repr__ = __str__

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
