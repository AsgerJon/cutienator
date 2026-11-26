"""PackageGenerator writes the package of one part of Qt: the file that
says which cute classes the part has, and in which file each is."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import textwrap
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

from . import DependencyTree
from ._class_generator import ClassGenerator
from .class_tables import ENUM_SPACES, LISTED_FIRST

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Dict, List, Optional, Tuple

  Key = Tuple[str, str]
  Entries = Tuple[Tuple[str, str], ...]


class PackageGenerator:
  """
  Writes the package of one part of Qt, the '__init__.py' of its folder
  in cutienator, as 'cutienator/QtWidgets/__init__.py'. The package
  says every name the part has, and in which file each is: the cute
  classes, and the names Qt has for the kinds of list that hold one, as
  'QObjectList'. A class is brought in the first time it is asked for,
  with the files it needs and no others, so bringing in the package
  costs nothing.

    generator = PackageGenerator()
    generator.setDependencyTree(tree)
    generator.setPartName('QtWidgets')
    generator.setCuteNames(('QtCore', 'QObject'), ...)
    generator.setWorkFolder('/some/folder/cutienator')
    generator.getEntries()       # (('QWidget', '_q_widget'), ...)
    generator.getPackageText()   # the text of the file
    generator.write()            # writes '.../QtWidgets/__init__.py'

  You provide
  -----------

  - 'setDependencyTree': the tree of the parts of Qt. Required.
  - 'setPartName': the part of Qt, as 'QtWidgets'. Required.
  - 'setCuteNames': every class of Qt that has, or is about to get, a
    cute class, each by its part and its name, as for 'ClassGenerator'.
    Required.
  - 'setWorkFolder': the folder of the package 'cutienator'. Required.

  What it writes
  --------------

  - '__all__', every name of the part, in the order of 'getEntries'.
  - Under 'if TYPE_CHECKING:', the import of each, for a type checker.
    Python never runs those lines.
  - Under 'else:', '__class_files__', the file of each name, and a
    '__getattr__' of the module that brings in that file the first time
    the name is asked for, as 'from cutienator.QtWidgets import
    QWidget', and keeps what it gave.

  What to expect
  --------------

  - The names come in this order: first those of 'LISTED_FIRST', which
    no generator of classes writes; then each cute class Qt writes in
    no class, in the order the tree makes them; then the names of the
    lists. A class Qt writes inside another is not listed: it is found
    through the class around it.
  - The docstring of a package written before is kept as it is, since
    a person may have chosen its example. A new package gets one.
  - 'getStaleFiles' names each file of a class in the folder that the
    package no longer lists. Nothing is removed.
  - The getters decide and write nothing. Only 'write' touches a file,
    and it replaces the file whole.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Private Variables
  __dependency_tree__ = None  # type: Optional[DependencyTree]
  __part_name__ = None  # type: Optional[str]
  __cute_names__ = None  # type: Optional[Tuple[Key, ...]]
  __work_folder__ = None  # type: Optional[str]
  __package_entries__ = None  # type: Optional[Entries]

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getDependencyTree(self) -> DependencyTree:
    """
    Gives the tree of the parts of Qt.

    Provided by you, through 'setDependencyTree'.

    Raises
    ------

    MissingVariable
      'setDependencyTree' has not been called.
    """
    if self.__dependency_tree__ is None:
      raise MissingVariable(self, '__dependency_tree__', DependencyTree)
    return self.__dependency_tree__

  def getPartName(self) -> str:
    """
    Gives the part of Qt, as 'QtWidgets'.

    Provided by you, through 'setPartName'.

    Raises
    ------

    MissingVariable
      'setPartName' has not been called.
    """
    if self.__part_name__ is None:
      raise MissingVariable(self, '__part_name__', str)
    return self.__part_name__

  def getCuteNames(self) -> Tuple[Key, ...]:
    """
    Gives every class of Qt that has, or is about to get, a cute class,
    each by its part and its name.

    Provided by you, through 'setCuteNames'.

    Raises
    ------

    MissingVariable
      'setCuteNames' has not been called.
    """
    if self.__cute_names__ is None:
      raise MissingVariable(self, '__cute_names__', tuple)
    return self.__cute_names__

  def getWorkFolder(self) -> str:
    """
    Gives the folder of the package 'cutienator'.

    Provided by you, through 'setWorkFolder'.

    Raises
    ------

    MissingVariable
      'setWorkFolder' has not been called.
    """
    if self.__work_folder__ is None:
      raise MissingVariable(self, '__work_folder__', str)
    return self.__work_folder__

  def getPackageFolder(self) -> str:
    """Gives the folder of the package of the part, in cutienator, as
    '.../cutienator/QtWidgets'."""
    return os.path.join(self.getWorkFolder(), self.getPartName())

  def getPackageFile(self) -> str:
    """Gives the path of the file 'write' writes, the '__init__.py' of
    the package of the part."""
    return os.path.join(self.getPackageFolder(), '__init__.py')

  def _createClassGenerator(self, className: str) -> ClassGenerator:
    """Gives a 'ClassGenerator' of a class of the part, set up as this
    generator is."""
    generator = ClassGenerator()
    generator.setDependencyTree(self.getDependencyTree())
    generator.setPartName(self.getPartName())
    generator.setClassName(className)
    generator.setCuteNames(*self.getCuteNames())
    return generator

  def getClassNames(self) -> Tuple[str, ...]:
    """
    Gives the cute classes of the part that Qt writes in no class, in
    the order the tree makes them: those the package lists. A class Qt
    writes inside another is found through that class.
    """
    tree, partName = self.getDependencyTree(), self.getPartName()
    cuteKeys = {*self.getCuteNames()}
    return (*(
        name for part, name in tree.getMakeOrder()
        if part == partName and '::' not in name
        and (part, name) in cuteKeys),)

  def _createViewer(self) -> ClassGenerator:
    """Gives a 'ClassGenerator' of the part, of no class, which says what
    a name of Qt is, a class or a namespace; see 'CuteName'."""
    viewer = ClassGenerator()
    viewer.setDependencyTree(self.getDependencyTree())
    viewer.setPartName(self.getPartName())
    viewer.setCuteNames(*self.getCuteNames())
    return viewer

  def getSpaceClasses(self) -> Dict[str, Tuple[str, ...]]:
    """
    Gives, for each namespace of the part, the cute classes Qt writes
    right inside it and inside no class, in the order the tree makes
    them: {'Qt3DCore': ('Qt3DCore::QNode', 'Qt3DCore::QEntity', ...)}.
    """
    tree, partName = self.getDependencyTree(), self.getPartName()
    cuteKeys, viewer = {*self.getCuteNames()}, self._createViewer()
    found = dict()  # type: Dict[str, List[str]]
    for part, name in tree.getMakeOrder():
      if part != partName or '::' not in name or (
          (part, name) not in cuteKeys):
        continue
      cuteName = viewer.getCuteName(name)
      if not cuteName.isNested():
        found.setdefault(cuteName.getSpaceName(), []).append(name)
    return {space: (*names,) for space, names in found.items()}

  def getSpaceNames(self) -> Tuple[str, ...]:
    """
    Gives every namespace of the part that is a package, in alphabetical
    order: each that holds a cute class, each namespace around those,
    as 'QV4' around 'QV4::Heap', and each whose enums the table
    'ENUM_SPACES' names, as 'Qt'.
    """
    spaces = [*self.getSpaceClasses()]
    enumSpaces = ENUM_SPACES.get(self.getPartName(), ())
    spaces.extend(name for name, _ in enumSpaces)
    found = set()
    for space in spaces:
      pieces = space.split('::')
      found.update('::'.join(pieces[:n]) for n in range(1, len(pieces) + 1))
    return (*sorted(found),)

  def getSpaceFile(self, spaceName: str) -> str:
    """Gives the path of the '__init__.py' of the package of a namespace
    of the part, as '.../cutienator/QtQml/QV4/Heap/__init__.py'."""
    return os.path.join(
        self.getPackageFolder(), *spaceName.split('::'), '__init__.py')

  def getEntries(self) -> Entries:
    """
    Gives every name the package lists, each with the stem of its file,
    as ('QWidget', '_q_widget'), in the order written.

    Decided for you, at the first call, and kept.
    """
    if self.__package_entries__ is not None:
      return self.__package_entries__
    entries = [*LISTED_FIRST.get(self.getPartName(), ())]
    generators = [
        self._createClassGenerator(name) for name in self.getClassNames()]
    for generator in generators:
      className = generator.getClassName()
      entries.append((className, generator.getFileStem(className)))
    #  A kind of list Qt gave a name is found in the file of its class.
    for generator in generators:
      stem = generator.getFileStem(generator.getClassName())
      entries.extend((name, stem) for name in generator.getNamedLists())
    self.__package_entries__ = (*entries,)
    return self.__package_entries__

  def getHeading(self) -> List[str]:
    """
    Gives the lines at the top of the file, its docstring through the
    line 'from __future__ import annotations'.

    The heading of a package written before is kept as it is, since a
    person may have chosen its example. A new package gets one naming
    its first two classes.
    """
    marker = 'from __future__ import annotations'
    packageFile = self.getPackageFile()
    if os.path.isfile(packageFile):
      with open(packageFile) as file:
        held = file.read()
      if marker in held:
        return held[:held.index(marker) + len(marker)].split('\n')
    partName = self.getPartName()
    infoSpec = """The 'cutienator.%s' package provides the cute classes of
    the part of Qt named %s, under the name PySide6 has for it."""
    info = ' '.join((infoSpec % (partName, partName)).split())
    lines = ['"""', *textwrap.wrap(info, 72)]
    named = [name for name, _ in self.getEntries()][:2]
    if named:
      lines.extend(('', '  from cutienator.%s import %s' % (
          partName, ', '.join(named))))
    infoSpec = """A class is brought in the first time it is asked for,
    with the files it needs and no others. So bringing in the package
    costs nothing, and a program pays for the classes it uses."""
    lines.extend(('', *textwrap.wrap(' '.join(infoSpec.split()), 72)))
    lines.extend((
        '"""', '#  Apache-2.0 license',
        '#  Copyright (c) 2026 Asger Jon Vistisen', marker))
    return lines

  def getPackageText(self) -> str:
    """
    Gives the whole text of the file, without writing it.

    Raises
    ------

    ValueError
      The part has no name to list.
    """
    files, partName = self.getEntries(), self.getPartName()
    if not files:
      infoSpec = """The part '%s' has no cute class to list."""
      raise ValueError(infoSpec % partName)
    lines = ['', 'import importlib', 'from typing import TYPE_CHECKING', '']
    spaces = [n for n in self.getSpaceNames() if '::' not in n]
    lines.append('__all__ = (')
    lines.extend("    '%s'," % name for name, _ in files)
    lines.extend("    '%s'," % name for name in spaces)
    lines.extend((')', ''))
    #  The cute things, for whoever reads the file without running it.
    lines.append('if TYPE_CHECKING:  # pragma: no cover, no mutate')
    lines.append('  from typing import Any, List')
    lines.append('')
    lines.extend(
        '  from .%s import %s' % (stem, name) for name, stem in files)
    lines.extend('  from . import %s' % name for name in spaces)
    #  The ugly things, for Python when it runs.
    lines.extend((
        'else:',
        '  #  Where each class is: the file that is brought in the first',
        '  #  time the class is asked for.', '  __class_files__ = {'))
    lines.extend("      '%s': '%s'," % pair for pair in files)
    lines.append('  }')
    if spaces:
      lines.extend((
          '  #  The namespaces of the part, each a package of its own.',
          '  __space_packages__ = (%s)' % ''.join(
              "'%s', " % name for name in spaces).rstrip()))
    lines.extend((
        '', '',
        '  def __getattr__(name: str) -> Any:',
        '    """',
        '    Brings in a class of this part the first time it is asked for,',
        "    as by 'from cutienator.%s import %s'. Python calls" % (
            partName, files[-1][0]),
        '    this for a name the package does not hold yet. The file of the',
        '    class is brought in, which brings in the files that class'
        ' needs',
        '    and no others, and the class is kept here for the next time.',
        '',
        '    Raises',
        '    ------',
        '',
        '    AttributeError',
        '      The part has no class of that name.',
        '    """',
        *(() if not spaces else (
            '    if name in __space_packages__:',
            "      value = importlib.import_module('.%s' % name, __name__)",
            '      globals()[name] = value',
            '      return value',
        )),
        '    try:',
        '      fileName = __class_files__[name]',
        '    except KeyError:',
        "      infoSpec = \"\"\"module '%s' has no attribute '%s'\"\"\"",
        '      raise AttributeError(infoSpec % (__name__, name)) from None',
        "    module = importlib.import_module('.%s' % fileName, __name__)",
        '    value = getattr(module, name)',
        '    globals()[name] = value',
        '    return value',
        '', '',
        '  def __dir__() -> List[str]:',
        '    """Names every class of the part, brought in or not."""',
        '    return [*__all__]',
    ))
    heading = '\n'.join(self.getHeading())
    return '%s\n%s\n' % (heading, '\n'.join(lines))

  def getSpaceText(self, spaceName: str) -> str:
    """
    Gives the whole text of the '__init__.py' of the package of one
    namespace of the part, without writing it. The package holds the
    cute classes Qt writes right inside the namespace, each brought in
    from its file in the folder of the part the first time it is asked
    for, as 'Qt3DCore.QEntity'; the namespaces right inside it, each a
    package of its own; and, for a namespace of 'ENUM_SPACES', its
    enums and the names of their members, as 'Qt.AlignLeft'.

    Raises
    ------

    ValueError
      The part has no such namespace.
    """
    if spaceName not in self.getSpaceNames():
      infoSpec = """The part '%s' has no namespace '%s'."""
      raise ValueError(infoSpec % (self.getPartName(), spaceName))
    partName, depth = self.getPartName(), spaceName.count('::') + 1
    dotted, up = spaceName.replace('::', '.'), '.' * (depth + 1)
    viewer = self._createViewer()
    files = [
        (viewer.getCuteName(name).getPythonName(), viewer.getFileStem(name))
        for name in self.getSpaceClasses().get(spaceName, ())]
    inner = [
        name.rpartition('::')[2] for name in self.getSpaceNames()
        if name.rpartition('::')[0] == spaceName]
    enumStem = dict(ENUM_SPACES.get(partName, ())).get(spaceName, '')
    outermost = spaceName.split('::')[0]
    example = '%s.%s' % (dotted, files[0][0]) if files else ''
    lines = [
        '"""',
        "The namespace '%s' of Qt, a package of 'cutienator.%s':" % (
            spaceName, partName),
        'what Qt writes inside it, under the names C++ has for it.',
        '',
        '  from cutienator.%s import %s' % (partName, outermost),
        *(('  %s' % example,) if example else ()),
        '',
        'A class is brought in the first time it is asked for.',
        '"""',
        '#  Apache-2.0 license',
        '#  Copyright (c) 2026 Asger Jon Vistisen',
        '#  Written by dev_tooling.PackageGenerator. Changes made here are',
        '#  lost.',
        'from __future__ import annotations',
        '',
        'import importlib',
        'from typing import TYPE_CHECKING',
        '',
    ]
    if enumStem:
      lines.extend((
          'from %s%s import %s as _Enums' % (up, enumStem, outermost),
          '',
          '#  The enums of the namespace, and the names of their',
          '#  members, as names of the package itself, where C++ has',
          "#  them: 'Qt.AlignLeft'.",
          'globals().update({',
          '    name: value for name, value in _Enums.__dict__.items()',
          "    if not name.startswith('_')})",
          '',
      ))
    lines.append('__all__ = (')
    lines.extend("    '%s'," % name for name, _ in files)
    lines.extend("    '%s'," % name for name in inner)
    lines.extend((')', ''))
    lines.append('if TYPE_CHECKING:  # pragma: no cover, no mutate')
    lines.append('  from typing import Any, List')
    lines.append('')
    lines.extend(
        '  from %s%s import %s' % (up, stem, name) for name, stem in files)
    lines.extend('  from . import %s' % name for name in inner)
    lines.extend((
        'else:',
        '  #  Where each class is: the file in the folder of the part',
        '  #  that is brought in the first time the class is asked for.',
        '  __class_files__ = {'))
    lines.extend("      '%s': '%s'," % pair for pair in files)
    lines.extend((
        '  }',
        '  #  The namespaces right inside this one, each a package.',
        '  __space_packages__ = (%s)' % ''.join(
            "'%s', " % name for name in inner).rstrip(),
        '', '',
        '  def __getattr__(name: str) -> Any:',
        '    """',
        '    Brings in a class or a namespace of this namespace the',
        "    first time it is asked for, as by '%s'. Python calls" % (
            example or 'from cutienator.%s import %s' % (
                partName, outermost)),
        '    this for a'
        ' name the package does not hold yet, and what it gives is kept',
        '    here for the next time.',
        '',
        '    Raises',
        '    ------',
        '',
        '    AttributeError',
        '      The namespace has nothing of that name.',
        '    """',
        '    if name in __space_packages__:',
        "      value = importlib.import_module('.%s' % name, __name__)",
        '    else:',
        '      try:',
        '        fileName = __class_files__[name]',
        '      except KeyError:',
        "        infoSpec = \"\"\"module '%s' has no attribute '%s'\"\"\"",
        '        raise AttributeError(infoSpec % (__name__, name))'
        ' from None',
        "      module = importlib.import_module("
        "'%s%%s' %% fileName, __name__)" % up,
        '      value = getattr(module, name)',
        '    globals()[name] = value',
        '    return value',
        '', '',
        '  def __dir__() -> List[str]:',
        '    """Names everything of the namespace, brought in or not."""',
        '    return [*__all__]',
    ))
    return '%s\n' % '\n'.join(lines)

  def getStaleFiles(self) -> Tuple[str, ...]:
    """
    Gives the full path of each file of a class in the folder of the
    package that the package no longer lists, in alphabetical order.
    Nothing is removed; a file of a class the dev tooling no longer
    writes stays until a person removes it.
    """
    folder = self.getPackageFolder()
    if not os.path.isdir(folder):
      return ()
    known = {'%s.py' % stem for _, stem in self.getEntries()}
    return (*(
        os.path.join(folder, name) for name in sorted(os.listdir(folder))
        if name.startswith('_q') and name.endswith('.py')
        and name not in known),)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setDependencyTree(self, dependencyTree: DependencyTree) -> None:
    """
    Sets the tree of the parts of Qt.

    Raises
    ------

    TypeException
      The tree is not a 'DependencyTree'.
    """
    if not isinstance(dependencyTree, DependencyTree):
      raise TypeException('dependencyTree', dependencyTree, DependencyTree)
    self.__dependency_tree__ = dependencyTree
    self.__package_entries__ = None

  def setPartName(self, partName: str) -> None:
    """
    Sets the part of Qt, as 'QtWidgets'.

    Raises
    ------

    TypeException
      The name is not a text.
    """
    if not isinstance(partName, str):
      raise TypeException('partName', partName, str)
    self.__part_name__ = partName
    self.__package_entries__ = None

  def setCuteNames(self, *cuteKeys: Key) -> None:
    """Sets every class of Qt that has, or is about to get, a cute class,
    each by its part and its name."""
    self.__cute_names__ = (*cuteKeys,)
    self.__package_entries__ = None

  def setWorkFolder(self, workFolder: str) -> None:
    """
    Sets the folder of the package 'cutienator'.

    Raises
    ------

    FileNotFoundError
      There is no folder there.
    """
    if not os.path.isdir(workFolder):
      raise FileNotFoundError("There is no folder at '%s'." % workFolder)
    self.__work_folder__ = workFolder

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def write(self) -> str:
    """
    Writes the package of the part, replacing the file written before,
    and makes its folder when there is none.

    Returns
    -------

    str
      The full path of the file, which now exists.
    """
    text = self.getPackageText()
    spaces = {name: self.getSpaceText(name) for name in self.getSpaceNames()}
    os.makedirs(self.getPackageFolder(), exist_ok=True)
    with open(self.getPackageFile(), 'w') as file:
      file.write(text)
    for spaceName, spaceText in spaces.items():
      spaceFile = self.getSpaceFile(spaceName)
      os.makedirs(os.path.dirname(spaceFile), exist_ok=True)
      with open(spaceFile, 'w') as file:
        file.write(spaceText)
    return self.getPackageFile()
