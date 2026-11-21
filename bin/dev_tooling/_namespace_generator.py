"""NamespaceGenerator writes the cute file of a namespace of Qt."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import textwrap
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

from . import DependencyTree, QtPart, EnumGenerator

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import List, Optional, Tuple

  Names = Tuple[str, ...]


class NamespaceGenerator:
  """
  Writes the Python file of a namespace of Qt that holds enums, as
  'Qt': a class with one name for each enum Qt writes in the namespace.

    generator = NamespaceGenerator()
    generator.setDependencyTree(tree)
    generator.setNamespaceName('Qt')
    generator.setWorkFolder('src/cutienator')
    generator.write()                 # src/cutienator/QtCore/_qt.py

  What to expect
  --------------

  - A namespace holds no objects, so the class is never made into one.
    It is the owner of its enums: 'Qt.AlignmentFlag' is the class that
    'EnumGenerator' writes for 'Qt::AlignmentFlag'.
  - The file pulls each enum in from the file 'EnumGenerator' writes
    for it, so those files have to be written as well; 'getEnumNames'
    lists them.
  - Where Qt names a type for the combinations of a flags enum, as
    'Qt::Alignment', that name holds the same class.
  - The enums of the namespace have to lie in one part of Qt; the file
    goes into the folder of that part.
  - Functions that Qt writes in the namespace are not in the file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Private Variables
  __dependency_tree__ = None  # type: Optional[DependencyTree]
  __namespace_name__ = None  # type: Optional[str]
  __work_folder__ = None  # type: Optional[str]

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getDependencyTree(self) -> DependencyTree:
    """Gives the tree the enums are taken from."""
    if self.__dependency_tree__ is None:
      raise MissingVariable(self, '__dependency_tree__', DependencyTree)
    return self.__dependency_tree__

  def getNamespaceName(self) -> str:
    """Gives the full name of the namespace, as 'Qt'."""
    if self.__namespace_name__ is None:
      raise MissingVariable(self, '__namespace_name__', str)
    return self.__namespace_name__

  def getWorkFolder(self) -> str:
    """Gives the folder of the cutienator package."""
    if self.__work_folder__ is None:
      raise MissingVariable(self, '__work_folder__', str)
    return self.__work_folder__

  def getEnumGenerator(self, enumName: str) -> EnumGenerator:
    """Gives a generator for one enum, with the same tree and folder."""
    generator = EnumGenerator()
    generator.setDependencyTree(self.getDependencyTree())
    generator.setEnumName(enumName)
    generator.setWorkFolder(self.getWorkFolder())
    return generator

  def getEnumNames(self) -> Names:
    """
    Gives the full name of each enum the file holds, in alphabetical
    order: every enum Qt writes directly in the namespace that
    'EnumGenerator' does not refuse.

    Raises
    ------

    ValueError
      Qt writes no such enum in the namespace.
    """
    tree, namespaceName = self.getDependencyTree(), self.getNamespaceName()
    enumNames = []  # type: List[str]
    for enumName in tree.getEnumRecordNames():
      record = tree.getEnumRecord(enumName)
      if record['insideClass'] or record['ownerName'] != namespaceName:
        continue
      if self.getEnumGenerator(enumName).findRefusal() is None:
        enumNames.append(enumName)
    if not enumNames:
      infoSpec = """Qt writes no enum in a namespace named '%s'."""
      raise ValueError(infoSpec % namespaceName)
    return (*enumNames,)

  def getPartName(self) -> str:
    """
    Gives the part of Qt the enums of the namespace lie in, as 'QtCore'.

    Raises
    ------

    ValueError
      The enums of the namespace lie in more than one part.
    """
    tree = self.getDependencyTree()
    partNames = set()
    for enumName in self.getEnumNames():
      partNames.add(tree.getEnumRecord(enumName)['partName'])
    if len(partNames) > 1:
      infoSpec = """The enums of the namespace '%s' lie in more than one
      part of Qt: %s."""
      found = ', '.join(sorted(partNames))
      info = infoSpec % (self.getNamespaceName(), found)
      raise ValueError(' '.join(info.split()))
    return partNames.pop()

  def getFileStem(self) -> str:
    """Gives the name of the file without its ending, as '_qt'."""
    return '_%s' % EnumGenerator.getStem(self.getNamespaceName())

  def getNamespaceFile(self) -> str:
    """
    Gives the full path of the file, as '/some/folder/QtCore/_qt.py'.
    Having the path does not mean the file is there; 'write' makes it.
    """
    name = '%s.py' % self.getFileStem()
    return os.path.join(self.getWorkFolder(), self.getPartName(), name)

  def getNamespaceText(self) -> str:
    """Gives the whole text of the file, without writing it."""
    namespaceName = self.getNamespaceName()
    ownName = namespaceName.split('::')[-1]
    #  Each enum is a class written inside the namespace, as C++ has it:
    #  'Qt.AlignmentFlag'.
    joinedNames, bindings, flagsCount = [], [], 0
    bases = set()
    for enumName in self.getEnumNames():
      generator = self.getEnumGenerator(enumName)
      enumOwnName = generator.getOwnName()
      joinedNames.append(enumName)
      bases.add('CuteFlags' if generator.isFlags() else 'CuteNum')
      if bindings:
        bindings.append('')
      bindings.extend(generator.getNestedLines())
      flagsName = generator.getFlagsName()
      if flagsName is None:
        continue
      flagsOwner, _, flagsOwnName = flagsName.rpartition('::')
      if flagsOwner == namespaceName:
        bindings.append('')
        bindings.append('  %s = %s' % (flagsOwnName, enumOwnName))
        flagsCount += 1
    imports = []
    if 'CuteNum' in bases:
      imports.extend(('from worktoy.keenum import Kee', ''))
    imports.append('from ..cute import %s' % ', '.join(sorted(bases)))
    infoSpec = """Written by dev_tooling.NamespaceGenerator from the
    records of Qt %s. Changes made here are lost."""
    heading = ' '.join((infoSpec % QtPart.getQtVersion()).split())
    infoSpec = """The namespace '%s' of Qt, which holds no objects. It
    holds the %d enums Qt writes in it, each under its name, and the %d
    names Qt has for the combinations of a flags enum, each holding the
    class of that enum. It is never made into an object."""
    about = infoSpec % (namespaceName, len(joinedNames), flagsCount)
    about = ' '.join(about.split())
    infoSpec = """%s stands for the namespace '%s' of Qt."""
    lines = [
      '"""',
      infoSpec % (ownName, namespaceName),
      '"""',
      '#  Apache-2.0 license',
      '#  Copyright (c) 2026 Asger Jon Vistisen',
      *('#  %s' % line for line in textwrap.wrap(heading, 73)),
      'from __future__ import annotations',
      '',
      *imports,
      '',
      '',
      'class %s:' % ownName,
      '  """',
      *('  %s' % line for line in textwrap.wrap(about, 75)),
      '  """',
      '',
      *bindings,
    ]
    return '%s\n' % '\n'.join(lines)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setDependencyTree(self, dependencyTree: DependencyTree) -> None:
    """Tells the generator which tree to take the enums from."""
    if not isinstance(dependencyTree, DependencyTree):
      raise TypeException('dependencyTree', dependencyTree, DependencyTree)
    self.__dependency_tree__ = dependencyTree

  def setNamespaceName(self, namespaceName: str) -> None:
    """Tells the generator which namespace to write, as 'Qt'."""
    if not isinstance(namespaceName, str):
      raise TypeException('namespaceName', namespaceName, str)
    self.__namespace_name__ = namespaceName

  def setWorkFolder(self, workFolder: str) -> None:
    """
    Tells the generator where the cutienator package is, as
    'src/cutienator'.

    Raises
    ------

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
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def write(self) -> Names:
    """
    Writes the file of the namespace, replacing the one written before.
    Its enums are classes written inside it, so they have no files.

    Returns
    -------

    Names
      The full path of the file written.
    """
    namespaceFile = self.getNamespaceFile()
    with open(namespaceFile, 'w') as file:
      file.write(self.getNamespaceText())
    return (namespaceFile,)
