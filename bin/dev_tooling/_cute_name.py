"""CuteName is a name of Qt, of a class or an enum, as the cute side of
cutienator writes it."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, Optional

  Record = Dict[str, Any]


class CuteName:
  """
  A name of Qt, of a class or an enum, as the cute side of cutienator
  writes it. What the name is made of needs nothing else:

    name = CuteName()
    name.setName('QMetaObject::Connection')
    name.getParts()
    #  {'full': 'QMetaObject::Connection', 'own': 'Connection',
    #   'owner': 'QMetaObject', 'outermost': 'QMetaObject',
    #   'dotted': 'QMetaObject.Connection', 'depth': 1}
    name.getPythonName()   # 'Connection'
    name.getDottedName()   # 'QMetaObject.Connection'

  How the cute class being written names it depends on that class, and
  is asked of the 'ClassGenerator' writing it, the viewer, given with
  'setViewer': whether it has a cute class ('isCute'), how a signature
  and an annotation write it ('findClassEntry', 'findEnumEntry'), and
  where it is found ('findWhere'). What the file then needs, the
  viewer is told, as an owner to bring in.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Private Variables
  __qt_name__ = None  # type: Optional[str]
  __viewer__ = None  # type: Any

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getName(self) -> str:
    """
    Gives the full name, as Qt writes it, as 'QMetaObject::Connection'.

    Provided by you, through 'setName'.

    Raises
    ------

    MissingVariable
      'setName' has not been called.
    """
    if self.__qt_name__ is None:
      raise MissingVariable(self, '__qt_name__', str)
    return self.__qt_name__

  def getViewer(self) -> Any:
    """
    Gives the 'ClassGenerator' of the cute class the name is seen from.

    Provided by you, through 'setViewer'.

    Raises
    ------

    MissingVariable
      'setViewer' has not been called.
    """
    if self.__viewer__ is None:
      raise MissingVariable(self, '__viewer__', object)
    return self.__viewer__

  def getParts(self) -> Record:
    """
    Gives what the name is made of: 'full', the name as Qt writes it;
    'own', its last name; 'owner', the class Qt writes it inside, or '';
    'outermost', the first name; 'dotted', the name as Python reaches it
    from the top of a file; 'depth', how many classes deep it stands.
    """
    full = self.getName()
    return dict(
        full=full, own=self.getPythonName(), owner=self.getOwnerName(),
        outermost=full.split('::')[0], dotted=self.getDottedName(),
        depth=full.count('::'))

  def getPythonName(self) -> str:
    """Gives the name the cute class has in Python: 'QSize' for 'QSize',
    and 'Connection' for 'QMetaObject::Connection'."""
    return self.getName().rpartition('::')[2]

  def getDottedName(self) -> str:
    """Gives the name by which Python reaches the cute class from the top
    of its file, as C++, PySide6 and PyQt have it: 'QSize' for 'QSize',
    and 'QMetaObject.Connection' for 'QMetaObject::Connection'."""
    return self.getName().replace('::', '.')

  def getOwnerName(self) -> str:
    """Gives the class Qt writes the name inside, as 'QMetaObject' for
    'QMetaObject::Connection', or '' for one written inside none."""
    return self.getName().rpartition('::')[0]

  def isNested(self) -> bool:
    """Says whether Qt writes the name inside a class."""
    return True if '::' in self.getName() else False

  def isCute(self) -> bool:
    """Says whether the name, seen from the part of the viewer, stands
    for a class that has, or is about to get, a cute class."""
    return self.getViewer()._isCute(self.getName())

  def findClassEntry(self) -> Optional[Record]:
    """
    Says how the body of the viewer names the cute class of the class
    of Qt this name stands for.

    Returns
    -------

    Optional[Record]
      None for a class that has no cute class. Else 'entry': what
      stands for it in a signature, as 'THIS' or 'QEvent'; 'name': how
      an annotation writes it; 'late': whether it is a late class;
      'bring': the class whose file holds it, or ''; 'hint': the class
      a type checker has to be shown for the annotation, or '';
      'holder': what a function writes to reach the class. Or the
      reason, in words, when the class cannot be named from here.
    """
    viewer, otherName = self.getViewer(), self.getName()
    className = viewer.getClassName()
    if otherName == className:
      name = viewer.getDottedName()
      return dict(
          entry='THIS', name=name, late=False, bring='', hint='',
          holder=name)
    if not self.isCute():
      return None
    mine, theirs = className.split('::')[0], otherName.split('::')[0]
    if className.startswith('%s::' % otherName):
      #  A class this one is written inside is made after it, in this
      #  very file, so it waits and nothing is brought in for it.
      if '::' in otherName:
        return 'names a class it is written two deep inside'
      return dict(
          entry=otherName, name=otherName, late=True, bring='', hint='',
          holder=otherName)
    ownerName = self.getOwnerName()
    if not ownerName:
      #  A class this one is not built on is a late class: its file is
      #  brought in by the program that uses it, not by this one. A
      #  class that holds an enum or a class this one names is brought
      #  in for that already.
      late = otherName not in viewer._getBuiltOn() and (
          otherName not in (viewer.__owners__ or ()))
      if mine == theirs:
        late = True
      return dict(
          entry=otherName, name=otherName, late=late, bring=otherName,
          hint=otherName, holder=otherName)
    name = self.getPythonName()
    dotted = self.getDottedName()
    if ownerName == className:
      #  A class written inside this one stands in the body under its
      #  own name. A function reaches it through the class.
      return dict(
          entry=name, name=name, late=False, bring='', hint='',
          holder=dotted)
    if mine == theirs:
      #  Written inside the same class as this one, beside it or deeper:
      #  a class body does not see the names of the body around it.
      infoSpec = """names '%s', which stands beside this class inside
      '%s' and cannot be named from here"""
      return ' '.join((infoSpec % (otherName, mine)).split())
    for depth in range(1, otherName.count('::') + 1):
      if not viewer._isCute('::'.join(otherName.split('::')[:depth])):
        return None
    #  A class written inside another class is reached through that
    #  class, as Qt writes it, so the file of that class is brought in.
    viewer._note('owners', theirs)
    return dict(
        entry=dotted, name=dotted, late=False, bring='', hint='',
        holder=dotted)

  def findEnumEntry(self, flags: bool) -> Optional[Record]:
    """
    Says how the body of the viewer names the class of the enum of Qt
    this name stands for, as 'Qt::WindowType'.

    Parameters
    ----------

    flags : bool
      Whether the combinations of the enum are meant, which Qt names
      apart, as 'Qt::WindowFlags'.

    Returns
    -------

    Optional[Record]
      None for an enum the body cannot name. Else 'entry': the class as
      a signature writes it, as 'Qt.WindowFlags' or 'QPalette.ColorRole';
      'shown': the class as an annotation writes it, as
      'QPalette.ColorRole'; 'owner': the class it is reached through,
      or '' for the namespace 'Qt', for an enum of the class being
      written and for one brought in from its own file; 'generator':
      the 'EnumGenerator' of the enum.
    """
    viewer, enumName = self.getViewer(), self.getName()
    tree = viewer.getDependencyTree()
    try:
      record = tree.getEnumRecord(enumName, viewer.getPartName())
    except ValueError:
      return None
    generator = viewer._getEnumGenerator(enumName)
    if generator.findRefusal() is not None:
      return None
    ownName, ownerName = record['ownName'], record['ownerName']
    if flags:
      flagsName = generator.getFlagsName()
      if flagsName is None:
        return None
      ownName = flagsName.rpartition('::')[2]
    if ownerName == viewer.getClassName():
      return dict(
          entry=ownName, shown=ownName, owner='', generator=generator,
          own=True)
    if ownerName == 'Qt':
      viewer._note('namespace', 'Qt')
      entry = 'Qt.%s' % ownName
      return dict(entry=entry, shown=entry, owner='', generator=generator)
    if not record['insideClass']:
      return None
    if not viewer._isCute(ownerName):
      return None
    className = viewer.getClassName()
    if ownerName.split('::')[0] == className.split('::')[0]:
      #  An enum of the class this one is written inside, or of a class
      #  beside it: a class body does not see the names of the body
      #  around it, and that class is not made yet.
      return None
    #  The enum stands inside its class, as Qt writes it, so the file of
    #  that class is brought in for it.
    viewer._note('owners', ownerName.split('::')[0])
    entry = '%s.%s' % (viewer.getDottedName(ownerName), ownName)
    return dict(
        entry=entry, shown=entry, owner=ownerName, generator=generator)

  def findWhere(self, how: str) -> Optional[str]:
    """
    Says where the cute class or enum this name stands for is found,
    when Qt hands it to a function as 'how' says, as 'QtGui:QPaintEvent'
    or 'QtCore:Qt.FocusPolicy', for the function that receives it from
    C++. Gives '' for a number and None when there is no cute class or
    enum for it.
    """
    viewer, what = self.getViewer(), self.getName()
    if how in ('number', 'nothing', 'text'):
      return ''
    #  The combinations of an enum are values of the class of the enum.
    listed = how in ('enum', 'flags')
    holder = what.rpartition('::')[0] if listed else what
    if not viewer._isCute(holder) and holder != 'Qt':
      return None
    if not listed and not self.isCute():
      return None
    partName = 'QtCore' if holder == 'Qt' else viewer.getPartName(
        holder.split('::')[0])
    return '%s:%s' % (partName, what.replace('::', '.'))


  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setName(self, qtName: str) -> None:
    """
    Sets the full name, as Qt writes it, as 'QMetaObject::Connection'.

    Raises
    ------

    TypeException
      The name is not a text.
    """
    if not isinstance(qtName, str):
      raise TypeException('qtName', qtName, str)
    self.__qt_name__ = qtName

  def setViewer(self, viewer: Any) -> None:
    """Sets the 'ClassGenerator' of the cute class the name is seen
    from."""
    self.__viewer__ = viewer
