"""DependencyTree says what each Qt class needs before it can be made."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import re
import subprocess
import tempfile
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

from . import QtPart

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, FrozenSet, List, Optional, Set, Tuple

  Names = Tuple[str, ...]
  Record = Dict[str, Any]


class DependencyTree:
  """
  The dependency tree of the classes Qt declares: for each class, the
  classes it needs.

    tree = DependencyTree()
    tree.setQtParts(qtCore, qtGui, qtWidgets)  # parts that were read
    tree.getClassNames()         # 770, each after what it is built on
    tree.getParents('QWidget')   # ('QObject', 'QPaintDevice')
    tree.getChildren('QObject')  # the classes built right on it
    tree.getTakes('QObject')     # the classes its functions take
    tree.getMakeOrder()          # an order to make Python classes in
    tree.getTakenLater('QObject')  # those it takes that are made later
    print(tree.getTreeText())    # the whole tree, indented

  Terms
  -----

  - A class is built on another when it starts out with all the other
    has: 'QWidget' is built on 'QObject'. The other is its parent.
    Python needs a parent to exist before the child can be made.
  - A class takes another when one of its functions has an argument
    whose type names that class: 'QObject' takes 'QThread', through
    'moveToThread(QThread *thread)'.
  - A class gives another when one of its functions gives back a type
    naming that class: 'QObject' gives 'QThread', through 'thread()'.

  You provide
  -----------

  - 'setQtParts': the parts of Qt to make the tree of, each a 'QtPart'
    that has been read. Required.

  What to expect
  --------------

  - The tree is made at the first getter, from every record of the
    parts. That takes ten to twenty seconds, and is kept.
  - Every class and struct defined in full is in it, also the ones
    declared inside a class or a namespace, by the name C++ gives them:
    'QMetaObject::Connection'. A class template, as 'QList', is a
    pattern and no class, and is not in it.
  - A class declared private or protected inside another class is left
    out, since it becomes no Python class. 'getLeftOut' names each of
    them.
  - 'Built on' is the tree. It has no rings, which is checked when the
    tree is made; 'getClassNames' gives an order with every parent
    before its children. A class can have two parents, as 'QWidget'.
  - 'Takes' and 'gives' are kept beside the tree, not in it. They do
    form rings: 'QObject' takes 'QThread', and 'QThread' is built on
    'QObject'. 'getRings' gives the rings. 'getMakeOrder' gives an
    order in which as few classes as it could find take a class made
    later, and 'getTakenLater' names those classes for one class.
  - Private functions, forbidden functions and templates are left out
    of 'takes' and 'gives', since none of them gets a Python method.
  - A parent that is no class of the tree, as the filled-in template
    'QList<QPoint>', is given by 'getParents' as C++ writes it, and
    counts for nothing in the order.
  - Two more things come out of the same records and are kept beside
    the tree: 'getEnumNames', every enum, and 'getAliasTypes', every
    second name a header gives a type.
  - 'getCopyableNames' is the one answer that comes from no record: the
    compiler is asked which classes it can copy.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def hasBody(function: Record) -> bool:
    """
    Says whether a function, as the compiler wrote it down, has its body
    of code right there in the header: written out, or left to the
    compiler with '= default'.

    Parameters
    ----------

    function : Record
      What the compiler wrote down about one function.
    """
    if function.get('explicitlyDefaulted'):
      return True
    for child in function.get('inner', ()):
      if child.get('kind') in ('CompoundStmt', 'CXXTryStmt'):
        return True
    return False

  @staticmethod
  def _findConstant(node: Record) -> Any:
    """
    Gives the number the compiler worked out for what a name of an enum
    is set to, or None when the name is set to nothing.

    The compiler writes that number down at the outermost step of the
    sum, so the first one met on the way in is the one. 'true' and
    'false' are 1 and 0. Anything else it wrote there is given back as
    the text it is, for the caller to refuse.
    """
    for child in node.get('inner', ()):
      if 'value' in child:
        text = str(child['value'])
        if text in ('true', 'false'):
          return 1 if text == 'true' else 0
        try:
          return int(text)
        except ValueError:
          return text
      number = DependencyTree._findConstant(child)
      if number is not None:
        return number
    return None

  @staticmethod
  def _collectEnumMembers(enum: Record) -> Record:
    """
    Gives each name of an enum with its number, in the order written. A
    name set to nothing is one more than the name before it, and the
    first such name is 0, as C++ has it.

    Parameters
    ----------

    enum : Record
      What the compiler wrote down about one enum.

    Returns
    -------

    Record
      'members': the names with their numbers. 'unsure': the text the
      compiler wrote for a name where a whole number was expected, or
      None when every number is one. The numbers of an unsure enum are
      not to be used.
    """
    members, last, unsure = [], -1, None
    for child in enum.get('inner', ()):
      if child.get('kind') != 'EnumConstantDecl':
        continue
      number = DependencyTree._findConstant(child)
      if isinstance(number, str):
        unsure, number = number, None
      if number is None:
        number = last + 1
      last = number
      members.append((child['name'], number))
    return dict(members=(*members,), unsure=unsure)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  What the compiler calls the functions of a class.
  __function_kinds__ = ('CXXMethodDecl', 'CXXConstructorDecl')

  #  What the compiler calls anything that can have a body of code.
  __body_kinds__ = (
      'FunctionDecl', 'CXXMethodDecl', 'CXXConstructorDecl',
      'CXXDestructorDecl', 'CXXConversionDecl',
  )

  #  A name as C++ writes it inside a type, as 'QMetaObject::Connection'.
  __name_pattern__ = re.compile(r'[A-Za-z_]\w*(?:::[A-Za-z_]\w*)*')

  #  Fallback Variables

  #  Private Variables
  __qt_parts__ = None  # type: Optional[Tuple[QtPart, ...]]
  __ordered_names__ = None  # type: Optional[Names]
  __class_parents__ = None  # type: Optional[Dict[str, Names]]
  __class_children__ = None  # type: Optional[Dict[str, Names]]
  __class_takes__ = None  # type: Optional[Dict[str, Names]]
  __class_gives__ = None  # type: Optional[Dict[str, Names]]
  __class_places__ = None  # type: Optional[Dict[str, Tuple[str, str]]]
  __left_out_names__ = None  # type: Optional[Names]
  __class_numbers__ = None  # type: Optional[Dict[str, str]]
  __enum_names__ = None  # type: Optional[Names]
  __enum_types__ = None  # type: Optional[Dict[str, Tuple[str, str]]]
  __enum_records__ = None  # type: Optional[Dict[str, Record]]
  __alias_types__ = None  # type: Optional[Dict[str, str]]
  __copyable_names__ = None  # type: Optional[FrozenSet[str]]
  __defined_names__ = None  # type: Optional[FrozenSet[str]]
  __make_order__ = None  # type: Optional[Names]
  __make_places__ = None  # type: Optional[Dict[str, int]]
  __class_rings__ = None  # type: Optional[Tuple[Names, ...]]

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getQtParts(self) -> Tuple[QtPart, ...]:
    """
    Gives the parts of Qt the tree is made of.

    Provided by you, through 'setQtParts'. Nothing fills it in for you.

    Raises
    ------

    MissingVariable
      'setQtParts' has not been called.
    """
    if self.__qt_parts__ is None:
      raise MissingVariable(self, '__qt_parts__', tuple)
    return self.__qt_parts__

  def _createTree(self, ) -> None:
    """Makes the tree from every record of the parts."""
    parents = dict()  # type: Dict[str, Names]
    taken = dict()  # type: Dict[str, Set[str]]
    given = dict()  # type: Dict[str, Set[str]]
    places = dict()  # type: Dict[str, Tuple[str, str]]
    numbers = dict()  # type: Dict[str, str]
    enumNames = set()  # type: Set[str]
    enumTypes = dict()  # type: Dict[str, Tuple[str, str]]
    enumRecords = dict()  # type: Dict[str, Record]
    aliasTypes = dict()  # type: Dict[str, str]
    definedNames = set()  # type: Set[str]
    leftOut = []  # type: List[str]
    for qtPart in self.getQtParts():
      partName = qtPart.getPartName()
      #  Every declaration of a class in this part, and every namespace,
      #  under the number the compiler gave it. Those numbers hold within
      #  one reading, so each part is worked through on its own.
      found = dict(
          entries=dict(), namespaces=dict(), enums=[], aliases=[],
          defined=definedNames,
      )  # type: Dict[str, Any]
      for headerFile in qtPart.getHeaderFiles():
        if not headerFile.wasRead():
          #  The reading left it out, with what the compiler said of it,
          #  so it has no records to give.
          continue
        headerPath = headerFile.getHeaderPath()
        for record in headerFile.getContents():
          self._collectEntries(record, '', None, 'public', headerPath, found)
        headerFile.forgetContents()
      entries, namespaces = found['entries'], found['namespaces']
      names = dict()  # type: Dict[str, str]
      for entryId in entries:
        self._nameEntry(entryId, entries, namespaces, names)
      for prefix, insideId, ownName, fixedType, detail in found['enums']:
        outer = prefix if insideId is None else '%s::' % names[insideId]
        enumNames.add('%s%s' % (outer, ownName))
        if fixedType is not None:
          enumTypes['%s%s' % (outer, ownName)] = fixedType
        if not detail['members']:
          #  A line that only says the enum exists, with no names in it.
          continue
        enumRecords.setdefault('%s%s' % (outer, ownName), dict(
            partName=partName, ownerName=outer[:-2], ownName=ownName,
            insideClass=False if insideId is None else True, **detail,
        ))
      for prefix, insideId, ownName, cppType in found['aliases']:
        outer = prefix if insideId is None else '%s::' % names[insideId]
        aliasTypes['%s%s' % (outer, ownName)] = cppType
      #  Who may use each class that is declared inside another class.
      declared = dict()  # type: Dict[str, str]
      for entryId, entry in entries.items():
        if entry['insideId'] is not None:
          declared.setdefault(names[entryId], entry['access'])
      for entryId, entry in entries.items():
        if not entry['complete']:
          continue
        name = names[entryId]
        if entry['belongsToId'] in entries and name not in declared:
          infoSpec = """The class '%s' is defined away from the class it
          belongs to, and that class does not declare it."""
          raise RuntimeError(' '.join((infoSpec % name).split()))
        words = name.split('::')
        outer = ('::'.join(words[:end]) for end in range(1, len(words) + 1))
        if any(declared.get(o, 'public') != 'public' for o in outer):
          leftOut.append(name)
          continue
        if name in parents:
          infoSpec = """The class '%s' is defined in full twice: in '%s'
          and in '%s'."""
          info = infoSpec % (name, places[name][1], entry['headerPath'])
          raise RuntimeError(' '.join(info.split()))
        parents[name] = entry['bases']
        taken[name], given[name] = entry['taken'], entry['given']
        places[name] = (partName, entry['headerPath'])
        numbers[name] = entryId
    self.__left_out_names__ = (*sorted(leftOut),)
    self.__class_numbers__ = numbers
    self.__enum_names__ = (*sorted(enumNames),)
    self.__enum_types__ = enumTypes
    self.__enum_records__ = enumRecords
    self.__alias_types__ = aliasTypes
    self.__defined_names__ = frozenset(definedNames)
    takes, gives = dict(), dict()
    for name in parents:
      takes[name] = self._findClasses(taken[name], parents, name)
      gives[name] = self._findClasses(given[name], parents, name)
    children = {name: [] for name in parents}  # type: Dict[str, List[str]]
    for name in sorted(parents):
      for parent in parents[name]:
        if parent in children:
          children[parent].append(name)
    self.__ordered_names__ = self._orderNames(parents)
    self.__class_parents__ = parents
    self.__class_children__ = {n: (*c,) for n, c in children.items()}
    self.__class_takes__ = takes
    self.__class_gives__ = gives
    self.__class_places__ = places

  def getClassNames(self, **kwargs) -> Names:
    """
    Gives the name of every class of the tree, in an order to make them
    in: each class comes after every class it is built on.

    Made for you, at the first call, from the records of the parts, and
    kept. You pass nothing; the keyword is for the method's own use.
    Among classes free to come in any order, the alphabet decides, so
    the order is the same every time.

    Returns
    -------

    Names
      A 'Tuple[str, ...]'. For QtCore, QtGui and QtWidgets of Qt 6.12.0
      it holds 770.

    Raises
    ------

    MissingVariable
      'setQtParts' has not been called.

    FileNotFoundError
      A part has not been read. Call its 'read' first.

    RuntimeError
      A class is defined in full twice, or the classes built on each
      other form a ring. Neither is expected to happen.
    """
    if self.__ordered_names__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      self._createTree()
      return self.getClassNames(_recursion=True)
    return self.__ordered_names__

  def getRoots(self) -> Names:
    """
    Gives the classes built on no class of the tree, in alphabetical
    order. Each is the top of a tree of its own.
    """
    self.getClassNames()
    return (*(
        name for name in sorted(self.__class_parents__)
        if not any(p in self.__class_parents__
                   for p in self.__class_parents__[name])
    ),)

  def getLeftOut(self) -> Names:
    """
    Gives the classes that are defined in full and are not in the tree,
    in alphabetical order.

    These are the classes declared private or protected inside another
    class, as 'QObject::QPrivateSignal' and 'QEvent::InputEventTag'.
    Only Qt's own code may use the private ones, and only a subclass
    the protected ones, so none of them becomes a Python class.
    """
    self.getClassNames()
    return self.__left_out_names__

  def getParents(self, className: str) -> Names:
    """
    Gives the classes a class is built on, in the order the header names
    them, each as C++ writes it.

    Returns
    -------

    Names
      A 'Tuple[str, ...]'. It is empty for a class built on nothing. An
      entry need not be a class of the tree: 'QPolygon' gives
      'QList<QPoint>', a template filled in.

    Raises
    ------

    LookupError
      The tree has no class of that name.
    """
    return self._lookUp('__class_parents__', className)

  def getChildren(self, className: str) -> Names:
    """
    Gives the classes built right on a class, in alphabetical order.

    Raises
    ------

    LookupError
      The tree has no class of that name.
    """
    return self._lookUp('__class_children__', className)

  def getAncestors(self, className: str) -> Names:
    """
    Gives every class of the tree a class is built on, through however
    many steps, in the order to make them in.

    For 'QListWidget' that is 'QObject', 'QPaintDevice', 'QWidget',
    'QFrame', 'QAbstractScrollArea', 'QAbstractItemView' and
    'QListView'.

    Raises
    ------

    LookupError
      The tree has no class of that name.
    """
    found = set()  # type: Set[str]
    waiting = [*self.getParents(className)]
    while waiting:
      name = waiting.pop()
      if name in found or name not in self.__class_parents__:
        continue
      found.add(name)
      waiting.extend(self.__class_parents__[name])
    return (*(n for n in self.getClassNames() if n in found),)

  def getDescendants(self, className: str) -> Names:
    """
    Gives every class built on a class, through however many steps, in
    the order to make them in.

    Raises
    ------

    LookupError
      The tree has no class of that name.
    """
    found = set()  # type: Set[str]
    waiting = [*self.getChildren(className)]
    while waiting:
      name = waiting.pop()
      if name in found:
        continue
      found.add(name)
      waiting.extend(self.__class_children__[name])
    return (*(n for n in self.getClassNames() if n in found),)

  def getTakes(self, className: str) -> Names:
    """
    Gives the classes a class takes: every class of the tree named in
    the type of an argument of one of its functions, in alphabetical
    order. The class itself is left out.

    A class named inside a bigger type counts: an argument of type
    'const QList<QObject *> &' takes 'QObject'.

    Raises
    ------

    LookupError
      The tree has no class of that name.
    """
    return self._lookUp('__class_takes__', className)

  def getGives(self, className: str) -> Names:
    """
    Gives the classes a class gives: every class of the tree named in
    the type one of its functions gives back, in alphabetical order.
    The class itself is left out.

    Raises
    ------

    LookupError
      The tree has no class of that name.
    """
    return self._lookUp('__class_gives__', className)

  def _createMakeOrder(self, ) -> None:
    """Finds the rings and the order to make the Python classes in."""
    names = self.getClassNames()
    parents, takes = self.__class_parents__, self.__class_takes__
    needs = dict()  # type: Dict[str, Names]
    for name in names:
      builtOn = [p for p in parents[name] if p in parents]
      needs[name] = (*sorted({*builtOn, *takes[name]}),)
    groups = self._findGroups(needs)
    groupOf = {n: at for at, group in enumerate(groups) for n in group}
    groupNeeds = [
        {groupOf[need] for name in group for need in needs[name]} - {at}
        for at, group in enumerate(groups)
    ]
    ordered, placed = [], set()  # type: List[str], Set[int]
    remaining = sorted(range(len(groups)), key=lambda at: groups[at][0])
    while remaining:
      ready = [at for at in remaining if groupNeeds[at] <= placed]
      if not ready:
        infoSpec = """The groups of classes needing each other form a ring
        themselves, which cannot be. It is among: %s."""
        info = infoSpec % ', '.join(groups[at][0] for at in remaining[:20])
        raise RuntimeError(' '.join(info.split()))
      for at in ready:
        ordered.extend(self._orderRing(groups[at]))
      placed.update(ready)
      remaining = [at for at in remaining if at not in placed]
    rings = sorted((group for group in groups if len(group) > 1))
    self.__class_rings__ = (*((*ring,) for ring in rings),)
    self.__make_places__ = {name: at for at, name in enumerate(ordered)}
    self.__make_order__ = (*ordered,)

  def getMakeOrder(self, **kwargs) -> Names:
    """
    Gives the name of every class of the tree, in an order to make the
    Python classes in: each class comes after every class it is built
    on, and after every class it takes, wherever that can be done.

    Made for you, at the first call, and kept. You pass nothing; the
    keyword is for the method's own use. It is the same order every
    time.

    Inside a ring it cannot be done for every class: whichever class of
    a ring is made first takes a class that is made later. 'getRings'
    gives the rings, and 'getTakenLater' the classes a class takes that
    come later in this order. The order keeps those cases few. It is
    not proven to keep them fewest: for Qt 6.12.0 it leaves 58, and no
    order leaves fewer than 51.

    Returns
    -------

    Names
      A 'Tuple[str, ...]' holding the same names as 'getClassNames'.

    Raises
    ------

    MissingVariable
      'setQtParts' has not been called.

    FileNotFoundError
      A part has not been read. Call its 'read' first.
    """
    if self.__make_order__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      self._createMakeOrder()
      return self.getMakeOrder(_recursion=True)
    return self.__make_order__

  def getRings(self) -> Tuple[Names, ...]:
    """
    Gives the rings among the classes of the tree, each as its classes
    in alphabetical order.

    Found for you, together with 'getMakeOrder'. Two classes are in one
    ring when each needs the other, straight or through other classes.
    A class needs the classes it is built on and the classes it takes:
    'QThread' is built on 'QObject', and 'QObject' takes 'QThread', so
    both are in one ring.

    Returns
    -------

    Tuple[Names, ...]
      A 'Tuple[Tuple[str, ...], ...]'. For QtCore, QtGui and QtWidgets
      of Qt 6.12.0 it holds 19 rings of 95 classes in all, the biggest
      of 21. A class in no ring is in none of the entries.
    """
    self.getMakeOrder()
    return self.__class_rings__

  def getTakenLater(self, className: str) -> Names:
    """
    Gives the classes a class takes that are made later than the class
    itself, by 'getMakeOrder', in alphabetical order.

    Found for you. These are the classes that do not exist yet when the
    Python class is made, although one of its functions has an argument
    of that type. For 'QObject' that is 'QChildEvent', 'QMetaMethod',
    'QThread', 'QTimerEvent' and 'QVariant'. Every class a class takes
    that is not given here is made before it.

    Returns
    -------

    Names
      A 'Tuple[str, ...]'. It is empty for a class in no ring, and for
      most classes in one.

    Raises
    ------

    LookupError
      The tree has no class of that name.
    """
    takes = self.getTakes(className)
    self.getMakeOrder()
    places = self.__make_places__
    return (*(t for t in takes if places[t] > places[className]),)

  def getPartName(self, className: str) -> str:
    """
    Gives the part of Qt a class belongs to, as 'QtCore'.

    Raises
    ------

    LookupError
      The tree has no class of that name.
    """
    return self._lookUp('__class_places__', className)[0]

  def getHeaderPath(self, className: str) -> str:
    """
    Gives the full path of the header file a class is defined in.

    Raises
    ------

    LookupError
      The tree has no class of that name.
    """
    return self._lookUp('__class_places__', className)[1]

  def getQtPart(self, className: str) -> QtPart:
    """
    Gives the 'QtPart' a class belongs to, of the ones you provided.

    Raises
    ------

    LookupError
      The tree has no class of that name.
    """
    partName = self.getPartName(className)
    for qtPart in self.getQtParts():
      if qtPart.getPartName() == partName:
        return qtPart
    raise RuntimeError("The part '%s' is not among the parts." % partName)

  def getClassRecord(self, className: str) -> Record:
    """
    Gives everything the compiler wrote down about a class: its record,
    untouched, with every function and other member inside it.

    Loaded for you from the reading of its part. Only this one record
    is kept in memory.

    Raises
    ------

    LookupError
      The tree has no class of that name.

    RuntimeError
      The record is not in the header file the tree found it in, so the
      part was read again since the tree was made. Make the tree again.
    """
    number = self._lookUp('__class_numbers__', className)
    headerPath = self.getHeaderPath(className)
    for headerFile in self.getQtPart(className).getHeaderFiles():
      if headerFile.getHeaderPath() != headerPath:
        continue
      waiting = [*headerFile.getContents()]
      headerFile.forgetContents()
      while waiting:
        node = waiting.pop()
        if node.get('id') == number and node.get('completeDefinition'):
          return node
        if node.get('kind') in ('NamespaceDecl', 'CXXRecordDecl'):
          waiting.extend(
              child for child in node.get('inner', ())
              if isinstance(child, dict))
    infoSpec = """The record of the class '%s' is not in '%s' any more.
    Make the dependency tree again."""
    info = infoSpec % (className, headerPath)
    raise RuntimeError(' '.join(info.split()))

  def getEnumNames(self) -> Names:
    """
    Gives the full name of every enum the parts declare, as
    'Qt::TimerType', in alphabetical order.

    Kept beside the tree, from the same records. An enum is a list of
    names that each stand for a whole number. A function taking one
    needs nothing made first, so enums take no place in the order.
    """
    self.getClassNames()
    return self.__enum_names__

  def getEnumTypes(self) -> Dict[str, Tuple[str, str]]:
    """
    Gives, for each enum whose declaration says which number type its
    names are kept as, that type: as the header writes it, and as the
    compiler reads it. 'QEvent::Type' is not in it; an enum declared as
    'enum class Kind : quint8' gives ('quint8', 'unsigned char').

    Kept beside the tree, from the same records. An enum that says
    nothing is kept as the compiler sees fit, which is an 'int' for
    every enum that needs no more room.

    Returns
    -------

    Dict[str, Tuple[str, str]]
      Under the full name of the enum, the two spellings of the type.
    """
    self.getClassNames()
    return dict(self.__enum_types__)

  def getEnumRecord(self, enumName: str) -> Record:
    """
    Gives what the parts say of one enum that has names in it.

    Kept beside the tree, from the same records.

    Parameters
    ----------

    enumName : str
      The full name of the enum, as 'Qt::AlignmentFlag'.

    Returns
    -------

    Record
      A dictionary, a new one each time. 'partName': the part of Qt the
      enum is written in. 'headerPath': the header file. 'ownerName':
      the class or namespace it is written inside, as 'Qt', or '' for
      none. 'ownName': its own name, as 'AlignmentFlag'. 'insideClass':
      whether the owner is a class. 'members': each name of the enum
      with its number, in the order written. 'unsure': None, or what
      the compiler wrote for a name where a whole number was expected;
      the numbers of such an enum are not to be used. 'scoped': whether
      C++ keeps the names inside the enum, as for 'enum class'.
      'access': who may use it where it is written inside a class.

    Raises
    ------

    ValueError
      The parts hold no enum of that name with names in it.
    """
    self.getClassNames()
    try:
      return dict(self.__enum_records__[enumName])
    except KeyError:
      infoSpec = """The parts of Qt hold no enum named '%s' that has
      names in it."""
      raise ValueError(' '.join((infoSpec % enumName).split()))

  def getEnumRecordNames(self) -> Names:
    """
    Gives the full name of every enum that has names in it, in
    alphabetical order. 'getEnumNames' also lists the enums a header
    only says exist.
    """
    self.getClassNames()
    return (*sorted(self.__enum_records__),)

  def _createCopyableNames(self, ) -> None:
    """
    Asks the compiler which classes of the tree it can copy, and keeps
    the answer.

    A small C++ program is written into a folder of its own, compiled
    with 'clang++', run once and thrown away. For each class it prints
    whether these two lines of C++ are allowed for anyone:
    'new T(other)', which makes a copy of another one, and 'delete' of
    the copy. The compiler alone knows that for sure. The records say
    it for a class that declares its copying itself, and leave it open
    for the many classes that let the compiler write it.

    Raises
    ------

    RuntimeError
      'clang++' refused the program, or the program did not run. What
      it said is in the message.
    """
    classNames = self.getClassNames()
    includeLines = []  # type: List[str]
    for className in classNames:
      qtPart = self.getQtPart(className)
      lines = qtPart.getIncludeLines(self.getHeaderPath(className))
      for line in lines.split('\n'):
        if line.strip() and line not in includeLines:
          includeLines.append(line)
    lines = [
        *includeLines,
        '#include <cstdio>',
        '#include <type_traits>',
        '#include <utility>',
        '',
        'template <typename T, typename = void>',
        'struct CanCopy : std::false_type {};',
        '',
        'template <typename T>',
        'struct CanCopy<T, std::void_t<',
        '    decltype(new T(std::declval<const T &>())),',
        '    decltype(delete std::declval<T *>())>> : std::true_type {};',
        '',
        'int main() {',
    ]
    lineSpec = '  std::printf("%%d %%s\\n", int(CanCopy<%s>::value), "%s");'
    lines.extend(lineSpec % (name, name) for name in classNames)
    lines.extend(('  return 0;', '}', ''))
    qtParts = self.getQtParts()
    with tempfile.TemporaryDirectory() as folder:
      sourceFile = os.path.join(folder, 'copyable.cpp')
      programFile = os.path.join(folder, 'copyable')
      with open(sourceFile, 'w') as file:
        file.write('\n'.join(lines))
      command = (
          'clang++', '-std=c++17', '-fPIC',
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
          infoSpec = """Asking the compiler which classes it can copy
          failed at '%s', which said: %s"""
          info = infoSpec % (os.path.basename(step[0]), done.stderr)
          raise RuntimeError(' '.join(info.split()))
        said = done.stdout
    copyable = set()  # type: Set[str]
    for line in said.split('\n'):
      answer, _, name = line.partition(' ')
      if answer == '1':
        copyable.add(name)
    self.__copyable_names__ = frozenset(copyable)

  def getCopyableNames(self, **kwargs) -> FrozenSet[str]:
    """
    Gives the name of every class of the tree that C++ can copy, as
    'QSize' and 'QString'. 'QObject' is not among them: Qt forbids
    copying one.

    Asked of the compiler at the first call, which takes about ten
    seconds, and kept. A function can take such a class as a value, or
    give one back, since a copy of it can be made for Python to hold.
    You pass nothing; the keyword is for the method's own use.

    Raises
    ------

    RuntimeError
      The compiler could not be asked; see '_createCopyableNames'.
    """
    if self.__copyable_names__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      self._createCopyableNames()
      return self.getCopyableNames(_recursion=True)
    return self.__copyable_names__

  def getDefinedNames(self) -> FrozenSet[str]:
    """
    Gives the compiler's own name of every function that has its body of
    code in a header file of the parts, as '_ZNK6QEvent4typeEv' for
    'QEvent::type()'.

    Kept beside the tree, from the same records. Such a function needs
    nothing from Qt's shared objects: whoever calls it gets a copy of
    the code. A function a header only declares has to be offered by a
    shared object, or it cannot be called at all.
    """
    self.getClassNames()
    return self.__defined_names__

  def getAliasTypes(self) -> Dict[str, str]:
    """
    Gives every other name the parts declare for a type, with the type
    it stands for: 'qsizetype' stands for 'long long', and 'QObjectList'
    for 'QList<QObject *>'.

    Kept beside the tree, from the same records. C++ lets a header
    give a type a second name, and functions then use either.
    """
    self.getClassNames()
    return dict(self.__alias_types__)

  def getTreeText(self, *classNames: str) -> str:
    """
    Gives the tree as text, one class per line, each class two spaces
    further in than the class it is built on.

    Parameters
    ----------

    *classNames : str
      The classes to start from, each shown with all that is built on
      it. With none, every root is shown, which is the whole tree.

    Returns
    -------

    str
      The lines. A class with two parents stands under each of them.
      What is built on it is shown under its first parent only; under
      the others its line says where to look.

    Raises
    ------

    LookupError
      The tree has no class of one of the names.
    """
    tops = classNames or self.getRoots()
    lines = []  # type: List[str]
    for top in tops:
      self.getParents(top)
      self._writeBranch(top, None, 0, lines)
    return '\n'.join(lines)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setQtParts(self, *qtParts: QtPart) -> None:
    """
    Tells which parts of Qt to make the tree of.

    Required. Calling it again forgets the tree made before.

    Parameters
    ----------

    *qtParts : QtPart
      One or more parts, each with its name and work folder set and
      already read. A class built on a class of another part finds its
      parent only when that part is given too: give 'QtCore' and
      'QtGui' along with 'QtWidgets'.

    Raises
    ------

    ValueError
      Called with no part at all.

    TypeException
      An argument is not a 'QtPart'.
    """
    if not qtParts:
      infoSpec = """A dependency tree needs at least one part of Qt, and
      none was given."""
      raise ValueError(' '.join(infoSpec.split()))
    for qtPart in qtParts:
      if not isinstance(qtPart, QtPart):
        raise TypeException('qtPart', qtPart, QtPart)
    self.__qt_parts__ = (*qtParts,)
    self.__ordered_names__ = None
    self.__class_parents__ = None
    self.__class_children__ = None
    self.__class_takes__ = None
    self.__class_gives__ = None
    self.__class_places__ = None
    self.__left_out_names__ = None
    self.__class_numbers__ = None
    self.__enum_names__ = None
    self.__enum_types__ = None
    self.__enum_records__ = None
    self.__alias_types__ = None
    self.__copyable_names__ = None
    self.__defined_names__ = None
    self.__make_order__ = None
    self.__make_places__ = None
    self.__class_rings__ = None

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __str__(self) -> str:
    """Says which parts the tree is of, and whether it is made yet."""
    clsName = type(self).__name__
    if self.__qt_parts__ is None:
      return '<%s still waiting for: setQtParts>' % clsName
    names = ', '.join(part.getPartName() for part in self.__qt_parts__)
    if self.__ordered_names__ is None:
      return '<%s of %s, not made yet>' % (clsName, names)
    count = len(self.__ordered_names__)
    return '<%s of %s: %d classes>' % (clsName, names, count)

  __repr__ = __str__

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _lookUp(self, tableName: str, className: str) -> Any:
    """
    Gives what one of the tables of the tree holds for a class, making
    the tree first when it is not made yet.

    Parameters
    ----------

    tableName : str
      The private variable holding the table, as '__class_parents__'.

    className : str
      The class to look up.

    Raises
    ------

    LookupError
      The tree has no class of that name.
    """
    self.getClassNames()
    table = getattr(self, tableName)
    if className not in table:
      infoSpec = """The dependency tree has no class named '%s'."""
      raise LookupError(infoSpec % (className,))
    return table[className]

  def _collectEntries(
      self,
      node: Any,
      prefix: str,
      insideId: Optional[str],
      access: str,
      headerPath: str,
      found: Dict[str, Any],
  ) -> None:
    """
    Notes down every declaration of a class in a record, also the ones
    inside a namespace or inside another class, and every namespace,
    enum and other name for a type met on the way.

    Parameters
    ----------

    node : Any
      A record, or a part of one.

    prefix : str
      The namespaces the node stands in, as 'Qt::', or '' for none.

    insideId : Optional[str]
      The number of the class the node is written inside, or None.

    access : str
      Who may use what is written at this spot of that class.

    headerPath : str
      The header file the record lies in.

    found : Dict[str, Any]
      Filled in. 'entries': for each declaration of a class, under the
      number the compiler gave it, its own name, where it is written,
      the class it belongs to when that is another one than the class
      it is written in, whether it is defined in full, and for a full
      definition its parents and the types its functions take and
      give. 'namespaces': the full name of each namespace, under its
      number. 'enums' and 'aliases': each enum, and each other name
      for a type, with where it is written. An enum comes with the
      number type its declaration fixes for it, or None, and with its
      names and their numbers, whether C++ scopes it, who may use it
      and the header file it lies in.
    """
    if not isinstance(node, dict):
      return
    kind = node.get('kind')
    if kind == 'NamespaceDecl':
      name = '%s%s' % (prefix, node.get('name', ''))
      found['namespaces'][node['id']] = name
      for child in node.get('inner', ()):
        self._collectEntries(
            child, '%s::' % name, None, 'public', headerPath, found,
        )
      return
    if not node.get('name'):
      return
    if kind == 'EnumDecl':
      fixedType = node.get('fixedUnderlyingType')
      if fixedType is not None:
        written = fixedType['qualType']
        fixedType = (written, fixedType.get('desugaredQualType', written))
      detail = dict(
          **self._collectEnumMembers(node),
          scoped=True if node.get('scopedEnumTag') else False,
          access=access, headerPath=headerPath,
      )
      found['enums'].append(
          (prefix, insideId, node['name'], fixedType, detail),
      )
      return
    if kind in ('TypedefDecl', 'TypeAliasDecl'):
      cppType = node['type']
      cppType = cppType.get('desugaredQualType', cppType['qualType'])
      found['aliases'].append((prefix, insideId, node['name'], cppType))
      return
    if kind in self.__body_kinds__:
      if 'mangledName' in node and self.hasBody(node):
        found['defined'].add(node['mangledName'])
      return
    if kind != 'CXXRecordDecl':
      return
    complete = bool(node.get('completeDefinition', False))
    entry = dict(
        ownName=node['name'], prefix=prefix, insideId=insideId,
        belongsToId=node.get('parentDeclContextId'), access=access,
        complete=complete, headerPath=headerPath,
    )
    found['entries'][node['id']] = entry
    if not complete:
      return
    bases = node.get('bases', ())
    entry['bases'] = (*(base['type']['qualType'] for base in bases),)
    entry['taken'], entry['given'] = self._collectTypes(node)
    inner = 'private' if node.get('tagUsed') == 'class' else 'public'
    for child in node.get('inner', ()):
      if child.get('kind') == 'AccessSpecDecl':
        inner = child['access']
        continue
      self._collectEntries(
          child, prefix, node['id'], inner, headerPath, found,
      )

  def _nameEntry(
      self,
      entryId: str,
      entries: Dict[str, Record],
      namespaces: Dict[str, str],
      names: Dict[str, str],
  ) -> str:
    """
    Gives the full name of a declared class, as C++ names it, and keeps
    it in 'names'.

    A class belongs to the class it is written inside. A class defined
    away from the class it belongs to, as 'QMetaObject::Connection' is,
    carries the number of that class instead, and is named after it.

    Raises
    ------

    RuntimeError
      The class belongs to something that was not read.
    """
    if entryId in names:
      return names[entryId]
    entry = entries[entryId]
    owner = entry['belongsToId'] or entry['insideId']
    if owner is None:
      name = '%s%s' % (entry['prefix'], entry['ownName'])
    elif owner in entries:
      outer = self._nameEntry(owner, entries, namespaces, names)
      name = '%s::%s' % (outer, entry['ownName'])
    elif owner in namespaces:
      name = '%s::%s' % (namespaces[owner], entry['ownName'])
    else:
      infoSpec = """The class '%s' in '%s' belongs to something that was
      not read with its part of Qt."""
      info = infoSpec % (entry['ownName'], entry['headerPath'])
      raise RuntimeError(' '.join(info.split()))
    names[entryId] = name
    return name

  def _collectTypes(self, classRecord: Record) -> Tuple[Set[str], Set[str]]:
    """
    Gives the types the functions of a class take, and the types they
    give back, each as C++ writes it. Forbidden functions and
    templates are left out. Private functions are not: a ritual calls
    them like any other.
    """
    taken, given = set(), set()  # type: Set[str], Set[str]
    access = 'public'
    if classRecord.get('tagUsed') == 'class':
      access = 'private'
    for member in classRecord.get('inner', ()):
      kind = member.get('kind')
      if kind == 'AccessSpecDecl':
        access = member['access']
        continue
      if kind not in self.__function_kinds__:
        continue
      if member.get('isImplicit') or member.get('explicitlyDeleted'):
        continue
      for entry in member.get('inner', ()):
        if entry.get('kind') == 'ParmVarDecl':
          taken.add(entry['type']['qualType'])
      if kind == 'CXXMethodDecl':
        whole = member['type']['qualType']
        given.add(whole[:whole.index('(')])
    return taken, given

  def _findClasses(
      self,
      cppTypes: Set[str],
      classes: Dict[str, Any],
      itself: str,
  ) -> Names:
    """
    Gives the classes of the tree named anywhere in some types, in
    alphabetical order, leaving out the class the types belong to.
    """
    found = set()  # type: Set[str]
    for cppType in cppTypes:
      for name in self.__name_pattern__.findall(cppType):
        while name and name not in classes:
          name = name.rpartition('::')[0]
        if name and name != itself:
          found.add(name)
    return (*sorted(found),)

  def _orderNames(self, parents: Dict[str, Names]) -> Names:
    """
    Puts the classes in an order with every parent before its children,
    the alphabet deciding where the tree leaves a choice.

    Raises
    ------

    RuntimeError
      The classes built on each other form a ring.
    """
    waitingFor = {
        name: {parent for parent in parents[name] if parent in parents}
        for name in parents
    }
    ordered, placed = [], set()  # type: List[str], Set[str]
    remaining = sorted(parents)
    while remaining:
      ready = [n for n in remaining if waitingFor[n] <= placed]
      if not ready:
        infoSpec = """The classes built on each other form a ring, among:
        %s."""
        info = infoSpec % ', '.join(remaining[:20])
        raise RuntimeError(' '.join(info.split()))
      ordered.extend(ready)
      placed.update(ready)
      remaining = [n for n in remaining if n not in placed]
    return (*ordered,)

  def _findGroups(self, needs: Dict[str, Names]) -> List[List[str]]:
    """
    Sorts the classes into groups: two classes are in one group when
    each needs the other, straight or through other classes. A group of
    more than one class is a ring.

    Parameters
    ----------

    needs : Dict[str, Names]
      For each class, the classes of the tree it is built on or takes,
      in alphabetical order.

    Returns
    -------

    List[List[str]]
      The groups, each in alphabetical order. Every class is in exactly
      one.
    """
    #  Tarjan's way of finding such groups, written without a function
    #  calling itself, since a chain of classes can be long. 'number' is
    #  when a class was first met, 'lowest' the earliest class it can
    #  get back to, and 'trail' the classes met and not yet grouped.
    number, lowest = dict(), dict()  # type: Dict[str, int], Dict[str, int]
    trail, onTrail = [], set()  # type: List[str], Set[str]
    groups = []  # type: List[List[str]]
    for root in sorted(needs):
      if root in number:
        continue
      work = [(root, 0)]
      while work:
        name, step = work.pop()
        if step == 0:
          number[name] = lowest[name] = len(number)
          trail.append(name)
          onTrail.add(name)
        for at in range(step, len(needs[name])):
          other = needs[name][at]
          if other not in number:
            work.append((name, at + 1))
            work.append((other, 0))
            break
          if other in onTrail:
            lowest[name] = min(lowest[name], number[other])
        else:
          if lowest[name] == number[name]:
            group = []  # type: List[str]
            while not group or group[-1] != name:
              group.append(trail.pop())
              onTrail.discard(group[-1])
            groups.append(sorted(group))
          if work:
            above = work[-1][0]
            lowest[above] = min(lowest[above], lowest[name])
    return groups

  def _orderRing(self, ring: List[str]) -> List[str]:
    """
    Puts the classes of one ring in an order to make them in.

    No order of a ring has every class after all it takes. A class
    still comes after every class it is built on. Among the classes
    whose parents are placed, the next one is the class that most
    others of the ring are still waiting for, less the number it is
    still waiting for itself. The alphabet decides between equals.

    Parameters
    ----------

    ring : List[str]
      The classes of one group, in alphabetical order. A group of one
      class is given back as it is.
    """
    if len(ring) < 2:
      return [*ring]
    inside = set(ring)
    parents, takes = self.__class_parents__, self.__class_takes__
    ordered, placed = [], set()  # type: List[str], Set[str]
    while len(ordered) < len(ring):
      best, bestScore = '', 0
      for name in ring:
        if name in placed:
          continue
        if any(p in inside and p not in placed for p in parents[name]):
          continue
        waiting = sum(
            1 for t in takes[name] if t in inside and t not in placed
        )
        wanted = sum(
            1 for other in ring
            if other not in placed and name in takes[other]
        )
        if not best or waiting - wanted < bestScore:
          best, bestScore = name, waiting - wanted
      if not best:
        infoSpec = """The classes built on each other form a ring, among:
        %s."""
        raise RuntimeError(' '.join((infoSpec % ', '.join(ring)).split()))
      ordered.append(best)
      placed.add(best)
    return ordered

  def _writeBranch(
      self,
      className: str,
      under: Optional[str],
      depth: int,
      lines: List[str],
  ) -> None:
    """Writes one class and all that is built on it, as lines of text."""
    known = [p for p in self.__class_parents__[className]
             if p in self.__class_parents__]
    others = [p for p in known if p != under]
    line = '%s%s' % ('  ' * depth, className)
    if under is not None and known and known[0] != under:
      lines.append('%s  (see under %s)' % (line, known[0]))
      return
    if others and under is not None:
      line = '%s  (also built on %s)' % (line, ', '.join(others))
    lines.append(line)
    for child in self.__class_children__[className]:
      self._writeBranch(child, className, depth + 1, lines)

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
