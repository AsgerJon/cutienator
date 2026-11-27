"""DependencyTree says what each Qt class needs before it can be made."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import re
import subprocess
import tempfile
from concurrent.futures import ThreadPoolExecutor
from types import MappingProxyType
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

from . import HeaderFolder, HeaderReader, Machine

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import (
      Any, Dict, FrozenSet, Iterator, List, Mapping, Optional, Set, Tuple)

  Names = Tuple[str, ...]
  Record = Dict[str, Any]
  #  A class of the tree: its part and its name, as ('QtCore', 'QObject').
  Key = Tuple[str, str]
  Keys = Tuple[Key, ...]


def _byName(key: Key) -> Tuple[str, str]:
  """The order classes go in where the alphabet decides: by name, and
  by part among classes of one name."""
  return key[1], key[0]


class DependencyTree:
  """
  The dependency tree of the classes Qt declares: for each class, the
  classes it needs.

    tree = DependencyTree()
    tree.setHeaderReaders(qtCore, qtGui, qtWidgets)  # parts that were read
    tree['QtWidgets']['QWidget']  # the class under its part
    tree.getClasses()            # 770, each after what it is built on
    tree.getParents('QWidget', 'QtWidgets')  # ('QObject', 'QPaintDevice')
    tree.getChildren('QObject', 'QtCore')  # the classes built right on it
    tree.getTakes('QObject', 'QtCore')  # the classes its functions take
    tree.getMakeOrder()          # an order to make Python classes in
    tree.getTakenLater('QObject', 'QtCore')  # those made later
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
  - A class is under its part: ('QtCore', 'QObject'), its key. Two
    parts may each define a class by one name, as QtCharts and QtGraphs
    each a 'QBarSeries'; Qt forbids reading both in one file.
  - A name is seen from a part: every lookup by name says the part,
    as 'getParents("QBarSeries", "QtGraphs")'. The name is looked up as
    a header file of that part sees it: in the part itself first, then
    in the parts it needs, the nearest first, as 'HeaderFolder' has
    them, and then in the other parts, in the order read. Seen from its
    own part, a class is always its own. A name only one part defines
    is the same seen from every part.

  You provide
  -----------

  - 'setHeaderReaders': the parts of Qt to make the tree of, each a
    'HeaderReader' that has been read. Required.

  What to expect
  --------------

  - The tree is made at the first getter, from every record of the
    parts. That takes ten to twenty seconds, and is kept.
  - Every class and struct defined in full is in it, also the ones
    declared inside a class or a namespace, by the name C++ gives them:
    'QMetaObject::Connection'. A class template, as 'QList', is a
    pattern and no class, and is not in it.
  - What gives classes gives keys, as ('QtCore', 'QObject'): a name
    alone may stand for two classes.
  - A class declared private or protected inside another class is left
    out, since it becomes no Python class. 'getLeftOut' names each of
    them.
  - 'Built on' is the tree. It has no rings, which is checked when the
    tree is made; 'getClasses' gives an order with every parent before
    its children. A class can have two parents, as 'QWidget'.
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
  __header_readers__ = None  # type: Optional[Tuple[HeaderReader, ...]]
  __source_reader__ = None  # type: Optional[Any]
  __kept_for_users__ = None  # type: Optional[Dict[str, Dict[Any, Any]]]
  __cute_names__ = None  # type: Optional[FrozenSet[Key]]
  __ordered_names__ = None  # type: Optional[Keys]
  #  The classes each class is built on, as C++ writes them, and those
  #  of them that are classes of the tree.
  __class_parents__ = None  # type: Optional[Dict[Key, Names]]
  __parent_keys__ = None  # type: Optional[Dict[Key, Keys]]
  __class_children__ = None  # type: Optional[Dict[Key, Keys]]
  __class_takes__ = None  # type: Optional[Dict[Key, Keys]]
  __class_gives__ = None  # type: Optional[Dict[Key, Keys]]
  #  The header file each class is defined in.
  __class_places__ = None  # type: Optional[Dict[Key, str]]
  __left_out_names__ = None  # type: Optional[Keys]
  __class_numbers__ = None  # type: Optional[Dict[Key, str]]
  #  The names of classes two or more parts have; see 'getSharedNames'.
  __shared_names__ = None  # type: Optional[FrozenSet[str]]
  #  Each enum, each fixed number type of one, each enum with names in
  #  it, and each second name for a type, under its part as a class is.
  __enum_names__ = None  # type: Optional[FrozenSet[Key]]
  __enum_types__ = None  # type: Optional[Dict[Key, Tuple[str, str]]]
  __enum_records__ = None  # type: Optional[Dict[Key, Record]]
  __alias_types__ = None  # type: Optional[Dict[Key, str]]
  __copyable_names__ = None  # type: Optional[FrozenSet[Key]]
  #  The classes whose header file did not compile among the others
  #  when the compiler was asked what it can copy; see
  #  '_createCopyableNames'.
  __not_asked_copyable__ = None  # type: Optional[FrozenSet[Key]]
  #  Under each part, each class it defines; see '__getitem__'.
  __classes_by_part__ = None  # type: Optional[Dict[str, Dict[str, Record]]]
  #  For each part, the parts a name is looked up in when seen from it,
  #  the part first; and for each part and each kind of name, which
  #  part each name is looked up in; see '_findPart'.
  __part_orders__ = None  # type: Optional[Dict[str, Names]]
  #  For each part, the first parts of its order: itself and the parts
  #  it needs; see 'getNeededParts'.
  __needed_parts__ = None  # type: Optional[Dict[str, Names]]
  __part_scopes__ = None  # type: Optional[Dict[Tuple[str, str], Dict]]
  #  Each class the tree leaves out for an edge case of Qt's source it
  #  has no rule for, with why; see 'getMissedClasses'.
  __missed_classes__ = None  # type: Optional[Dict[str, str]]
  __defined_names__ = None  # type: Optional[FrozenSet[str]]
  #  The header file holding the code of a function, by the compiler's
  #  name of it, under each part whose header file holds it.
  __defined_paths__ = None  # type: Optional[Dict[Key, str]]
  __make_order__ = None  # type: Optional[Keys]
  __make_places__ = None  # type: Optional[Dict[Key, int]]
  __class_rings__ = None  # type: Optional[Tuple[Keys, ...]]

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __getitem__(self, partName: str) -> Mapping[str, Record]:
    """
    Gives the classes one part defines, under their names, as
    'tree["QtWidgets"]["QWidget"]'. Each is a dict: its 'partName',
    its 'headerPath', the classes it is built on as its header names
    them, 'parents', and its 'number' in the reading of the part. A
    name two parts define, as 'QBarSeries' of QtCharts and of QtGraphs,
    is under each of them, and each is a class of the tree.

    Raises
    ------

    KeyError
      The tree has no part of that name.
    """
    self.getClasses()
    if partName not in self.__classes_by_part__:
      infoSpec = """The tree has no part named '%s'."""
      raise KeyError(infoSpec % partName)
    return MappingProxyType(self.__classes_by_part__[partName])

  def __contains__(self, partName: object) -> bool:
    """Says whether the tree has a part of that name, as 'QtCore'."""
    self.getClasses()
    return partName in self.__classes_by_part__

  def __iter__(self) -> Iterator[str]:
    """Goes through the names of the parts, in the order read."""
    self.getClasses()
    return iter([*self.__classes_by_part__])

  def getSourceReader(self) -> Any:
    """Gives the 'SourceReader' the code of a function is looked up in
    where Qt's library has no name for it, or None when no source was
    provided; 'setSourceReader' provides it."""
    return self.__source_reader__

  def setSourceReader(self, sourceReader: Any) -> None:
    """
    Tells where Qt's own source is. Optional. With it, a function
    that Qt's library carries under no name gets its code from there.
    """
    self.__source_reader__ = sourceReader
  def getCuteNames(self) -> FrozenSet[Key]:
    """
    Gives every class of the tree that gets a cute class, by its key,
    as ('QtCore', 'QObject'): those 'setCuteNames' named, or every
    class of the tree when it was not called.
    """
    if self.__cute_names__ is None:
      return frozenset(self.getClasses())
    return self.__cute_names__

  def setCuteNames(self, *cuteKeys: Key) -> None:
    """
    Tells which classes of the tree get a cute class.

    Optional; without it every class of the tree counts as one that
    does. The ritual generator goes by it: a function that takes or
    gives a class with no cute class gets no ritual, since no function
    of Python could call it, and a function Qt calls itself that takes
    such a class is not handed to Python.

    Call it before the generators are asked for their rituals. What
    they kept with the tree is forgotten here, as 'getKept' has it,
    and a generator made before is not to be used after.

    Parameters
    ----------

    *cuteKeys : Key
      The classes, each by its part and its full name, as ('QtCore',
      'QMetaObject::Connection').

    Raises
    ------

    TypeException
      A key is not a pair of texts.

    LookupError
      A key is no class of the tree.

    MissingVariable
      'setHeaderReaders' has not been called.
    """
    known = frozenset(self.getClasses())
    for cuteKey in cuteKeys:
      if not isinstance(cuteKey, tuple) or len(cuteKey) != 2 or not all(
          isinstance(one, str) for one in cuteKey):
        raise TypeException('cuteKey', cuteKey, tuple)
      if cuteKey not in known:
        infoSpec = """%s is to get a cute class, and the tree has no
        class of that name in that part."""
        raise LookupError(' '.join((infoSpec % (cuteKey,)).split()))
    self.__cute_names__ = frozenset(cuteKeys)
    self.__kept_for_users__ = dict()

  def getKept(self, what: str) -> Dict[Any, Any]:
    """
    Gives a dict in which the generators keep what they worked out of
    this tree and would have to work out again: one dict for each
    word, as 'hidden types'.

    The dict is the tree's own. It is new and empty when the parts are
    set, and again when 'setCuteNames' is called. It goes when the
    tree goes, so nothing kept for one tree is ever read for another.

    Parameters
    ----------

    what : str
      A word for what is kept. The same word gives the same dict.

    Raises
    ------

    MissingVariable
      'setHeaderReaders' has not been called on this tree.
    """
    if self.__kept_for_users__ is None:
      raise MissingVariable(self, '__header_readers__', tuple)
    return self.__kept_for_users__.setdefault(what, dict())

  def getHeaderReaders(self) -> Tuple[HeaderReader, ...]:
    """
    Gives the parts of Qt the tree is made of.

    Provided by you, through 'setHeaderReaders'. Nothing fills it in for you.

    Raises
    ------

    MissingVariable
      'setHeaderReaders' has not been called.
    """
    if self.__header_readers__ is None:
      raise MissingVariable(self, '__header_readers__', tuple)
    return self.__header_readers__

  def _createTree(self, ) -> None:
    """Makes the tree from every record of the parts."""
    parents = dict()  # type: Dict[Key, Names]
    taken = dict()  # type: Dict[Key, Set[str]]
    given = dict()  # type: Dict[Key, Set[str]]
    places = dict()  # type: Dict[Key, str]
    numbers = dict()  # type: Dict[Key, str]
    enumNames = set()  # type: Set[Key]
    enumTypes = dict()  # type: Dict[Key, Tuple[str, str]]
    enumRecords = dict()  # type: Dict[Key, Record]
    aliasTypes = dict()  # type: Dict[Key, str]
    definedPaths = dict()  # type: Dict[Key, str]
    leftOut = []  # type: List[Key]
    twice = set()  # type: Set[Key]
    self.__missed_classes__ = dict()
    byPart = dict()  # type: Dict[str, Dict[str, Record]]
    for headerReader in self.getHeaderReaders():
      partName = headerReader.getPartName()
      byPart.setdefault(partName, dict())
      #  Every declaration of a class in this part, and every namespace,
      #  under the number the compiler gave it. Those numbers hold within
      #  one reading, so each part is worked through on its own.
      found = dict(
          entries=dict(), namespaces=dict(), enums=[], aliases=[],
          defined=dict(),
      )  # type: Dict[str, Any]
      for headerFile in headerReader.getHeaderFiles():
        if not headerFile.wasRead():
          #  The reading left it out, with what the compiler said of it,
          #  so it has no records to give.
          continue
        headerPath = headerFile.getHeaderPath()
        for record in headerFile.getContents():
          self._collectEntries(record, '', None, 'public', headerPath, found)
        headerFile.forgetContents()
      for compilerName, headerPath in found['defined'].items():
        definedPaths[(partName, compilerName)] = headerPath
      entries, namespaces = found['entries'], found['namespaces']
      names = dict()  # type: Dict[str, str]
      for entryId in entries:
        self._nameEntry(entryId, entries, namespaces, names)
      #  A class that could not be named is left out, and so is every
      #  class inside it; see 'getMissedClasses'.
      for entryId in [e for e in entries if e not in names]:
        del entries[entryId]
      found['enums'] = [
          one for one in found['enums']
          if one[1] is None or one[1] in names]
      found['aliases'] = [
          one for one in found['aliases']
          if one[1] is None or one[1] in names]
      for prefix, insideId, ownName, fixedType, detail in found['enums']:
        outer = prefix if insideId is None else '%s::' % names[insideId]
        enumKey = (partName, '%s%s' % (outer, ownName))
        enumNames.add(enumKey)
        if fixedType is not None:
          enumTypes[enumKey] = fixedType
        if not detail['members']:
          #  A line that only says the enum exists, with no names in it.
          continue
        enumRecords.setdefault(enumKey, dict(
            partName=partName, ownerName=outer[:-2], ownName=ownName,
            insideClass=False if insideId is None else True, **detail,
        ))
      for prefix, insideId, ownName, cppType in found['aliases']:
        outer = prefix if insideId is None else '%s::' % names[insideId]
        aliasTypes[(partName, '%s%s' % (outer, ownName))] = cppType
      #  Who may use each class that is declared inside another class.
      declared = dict()  # type: Dict[str, str]
      for entryId, entry in entries.items():
        if entry['insideId'] is not None:
          declared.setdefault(names[entryId], entry['access'])
      for entryId, entry in entries.items():
        if not entry['complete']:
          continue
        name = names[entryId]
        key = (partName, name)
        if entry['belongsToId'] in entries and name not in declared:
          infoSpec = """It is defined away from the class it belongs
          to, in '%s', and that class does not declare it."""
          self._missClass(name, infoSpec % entry['headerPath'])
          leftOut.append(key)
          continue
        words = name.split('::')
        outer = ('::'.join(words[:end]) for end in range(1, len(words) + 1))
        if any(declared.get(o, 'public') != 'public' for o in outer):
          leftOut.append(key)
          continue
        #  Each class under its part, as 'tree["QtWidgets"]["QWidget"]'.
        #  Two parts may each define a class of their own by one name,
        #  as QtCharts and QtGraphs each a 'QBarSeries': each is a class
        #  of the tree, under its own part.
        byPart[partName][name] = dict(
            partName=partName, headerPath=entry['headerPath'],
            parents=(*entry['bases'],), number=entryId)
        if key in parents:
          infoSpec = """It is defined in full twice: in '%s' and in
          '%s'."""
          self._missClass(
              name, infoSpec % (places[key], entry['headerPath']))
          twice.add(key)
          continue
        parents[key] = entry['bases']
        taken[key], given[key] = entry['taken'], entry['given']
        places[key] = entry['headerPath']
        numbers[key] = entryId
    for key in twice:
      for kept in (parents, taken, given, places, numbers):
        kept.pop(key, None)
      byPart[key[0]].pop(key[1], None)
      leftOut.append(key)
    self.__classes_by_part__ = byPart
    self.__enum_names__ = frozenset(enumNames)
    self.__enum_types__ = enumTypes
    self.__enum_records__ = enumRecords
    self.__alias_types__ = aliasTypes
    self.__defined_names__ = frozenset(name for _, name in definedPaths)
    self.__defined_paths__ = definedPaths
    self.__part_orders__ = self._orderParts([*byPart])
    self.__part_scopes__ = dict()
    self.__left_out_names__ = (*sorted(leftOut, key=_byName),)
    self.__class_numbers__ = numbers
    #  A class written in a namespace or inside another class may name
    #  the class it is built on short, as 'class ArgumentList: public
    #  Node' in 'QQmlJS::AST': C++ looks the name up in the scopes
    #  around the class first, the nearest first.
    for key in parents:
      partName, name = key
      found = []  # type: List[str]
      for base in parents[key]:
        words = name.split('::')[:-1]
        while words and self._findPart('classes', base, partName) is None:
          spelled = '%s::%s' % ('::'.join(words), base)
          if self._findPart('classes', spelled, partName) is not None:
            base = spelled
            break
          words.pop()
        found.append(base)
      parents[key] = (*found,)
    parentKeys = dict()  # type: Dict[Key, Keys]
    for key in parents:
      inTree = []  # type: List[Key]
      for base in parents[key]:
        holder = self._findPart('classes', base, key[0])
        if holder is not None:
          inTree.append((holder, base))
      parentKeys[key] = (*inTree,)
    takes, gives = dict(), dict()
    for key in parents:
      takes[key] = self._findClasses(taken[key], key)
      gives[key] = self._findClasses(given[key], key)
    children = {key: [] for key in parents}  # type: Dict[Key, List[Key]]
    for key in sorted(parents, key=_byName):
      for parentKey in parentKeys[key]:
        children[parentKey].append(key)
    self.__ordered_names__ = self._orderNames(parentKeys)
    self.__class_parents__ = parents
    self.__parent_keys__ = parentKeys
    self.__class_children__ = {k: (*c,) for k, c in children.items()}
    self.__class_takes__ = takes
    self.__class_gives__ = gives
    self.__class_places__ = places

  def getClasses(self, **kwargs) -> Keys:
    """
    Gives every class of the tree, by its key, as ('QtCore',
    'QObject'), in an order to make them in: each class comes after
    every class it is built on.

    Made for you, at the first call, from the records of the parts, and
    kept. You pass nothing; the keyword is for the method's own use.
    Among classes free to come in any order, the alphabet decides, by
    name and then by part, so the order is the same every time.

    Returns
    -------

    Keys
      A 'Tuple[Tuple[str, str], ...]'. For QtCore, QtGui and QtWidgets
      of Qt 6.12.0 it holds 770.

    Raises
    ------

    MissingVariable
      'setHeaderReaders' has not been called.

    FileNotFoundError
      A part has not been read. Call its 'read' first.

    RuntimeError
      The classes built on each other form a ring. That is not
      expected to happen.
    """
    if self.__ordered_names__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      self._createTree()
      return self.getClasses(_recursion=True)
    return self.__ordered_names__

  def getSharedNames(self) -> FrozenSet[str]:
    """
    Gives the full name of each class two or more parts of the tree
    have, as 'QBarSeries', which QtCharts and QtGraphs both have. A cute
    class of such a name says its part as well; see 'MetaCute'.

    Made for you, at the first call, from 'getClasses', and kept.
    """
    if self.__shared_names__ is None:
      parts = dict()  # type: Dict[str, Set[str]]
      for partName, className in self.getClasses():
        parts.setdefault(className, set()).add(partName)
      self.__shared_names__ = frozenset(
          name for name, holders in parts.items() if len(holders) > 1)
    return self.__shared_names__

  def getClassKey(self, className: str, partName: str) -> Key:
    """
    Gives the class a name stands for, seen from a part, by its key:
    'getClassKey("QObject", "QtWidgets")' gives ('QtCore', 'QObject'),
    and 'getClassKey("QBarSeries", "QtGraphs")' gives ('QtGraphs',
    'QBarSeries').

    Parameters
    ----------

    className : str
      The full name of the class, as 'QMetaObject::Connection'.

    partName : str
      The part the name is seen from; see 'Terms'.

    Raises
    ------

    LookupError
      No part of the tree has a class of that name.
    """
    self.getClasses()
    holder = self._findPart('classes', className, partName)
    if holder is None:
      infoSpec = """The dependency tree has no class named '%s'."""
      raise LookupError(infoSpec % (className,))
    return holder, className

  def hasClass(self, className: str, partName: str) -> bool:
    """Says whether a name stands for a class of the tree, seen from a
    part, as 'getClassKey' has it."""
    self.getClasses()
    return self._findPart('classes', className, partName) is not None

  def getPartOrder(self, partName: str) -> Names:
    """
    Gives the parts a name seen from a part is looked up in, in the
    order looked: the part itself, the parts it needs, the nearest
    first, and then the other parts, in the order read; see 'Terms'.

    Raises
    ------

    LookupError
      The tree has no part of that name.
    """
    self.getClasses()
    if partName not in self.__part_orders__:
      infoSpec = """The tree has no part named '%s'."""
      raise LookupError(infoSpec % partName)
    return self.__part_orders__[partName]

  def getRoots(self) -> Keys:
    """
    Gives the classes built on no class of the tree, in alphabetical
    order. Each is the top of a tree of its own.
    """
    self.getClasses()
    return (*sorted(
        (key for key in self.__parent_keys__
         if not self.__parent_keys__[key]), key=_byName),)

  def getLeftOut(self) -> Keys:
    """
    Gives the classes that are defined in full and are not in the tree,
    in alphabetical order.

    These are the classes declared private or protected inside another
    class, as 'QObject::QPrivateSignal' and 'QEvent::InputEventTag'.
    Only Qt's own code may use the private ones, and only a subclass
    the protected ones, so none of them becomes a Python class.
    """
    self.getClasses()
    return self.__left_out_names__

  def getParents(self, className: str, partName: str) -> Names:
    """
    Gives the classes a class is built on, in the order the header names
    them, each as C++ writes it, seen from the part of the class.

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
    return self._lookUp('__class_parents__', className, partName)

  def getParentKeys(self, className: str, partName: str) -> Keys:
    """Gives those of the classes a class is built on that are classes
    of the tree, by their keys, in the order the header names them."""
    return self._lookUp('__parent_keys__', className, partName)

  def getChildren(self, className: str, partName: str) -> Keys:
    """
    Gives the classes built right on a class, in alphabetical order.

    Raises
    ------

    LookupError
      The tree has no class of that name.
    """
    return self._lookUp('__class_children__', className, partName)

  def getAncestors(self, className: str, partName: str) -> Keys:
    """
    Gives every class of the tree a class is built on, through however
    many steps, in the order to make them in.

    For 'QListWidget' that is 'QObject', 'QPaintDevice', 'QWidget',
    'QFrame', 'QAbstractScrollArea', 'QAbstractItemView' and
    'QListView', each by its key.

    Raises
    ------

    LookupError
      The tree has no class of that name.
    """
    found = set()  # type: Set[Key]
    waiting = [*self.getParentKeys(className, partName)]
    while waiting:
      key = waiting.pop()
      if key in found:
        continue
      found.add(key)
      waiting.extend(self.__parent_keys__[key])
    return (*(k for k in self.getClasses() if k in found),)

  def getDescendants(self, className: str, partName: str) -> Keys:
    """
    Gives every class built on a class, through however many steps, in
    the order to make them in.

    Raises
    ------

    LookupError
      The tree has no class of that name.
    """
    found = set()  # type: Set[Key]
    waiting = [*self.getChildren(className, partName)]
    while waiting:
      key = waiting.pop()
      if key in found:
        continue
      found.add(key)
      waiting.extend(self.__class_children__[key])
    return (*(k for k in self.getClasses() if k in found),)

  def getTakes(self, className: str, partName: str) -> Keys:
    """
    Gives the classes a class takes: every class of the tree named in
    the type of an argument of one of its functions, seen from its
    part, in alphabetical order. The class itself is left out.

    A class named inside a bigger type counts: an argument of type
    'const QList<QObject *> &' takes 'QObject'.

    Raises
    ------

    LookupError
      The tree has no class of that name.
    """
    return self._lookUp('__class_takes__', className, partName)

  def getGives(self, className: str, partName: str) -> Keys:
    """
    Gives the classes a class gives: every class of the tree named in
    the type one of its functions gives back, seen from its part, in
    alphabetical order. The class itself is left out.

    Raises
    ------

    LookupError
      The tree has no class of that name.
    """
    return self._lookUp('__class_gives__', className, partName)

  def _createMakeOrder(self, ) -> None:
    """Finds the rings and the order to make the Python classes in."""
    keys = self.getClasses()
    parentKeys, takes = self.__parent_keys__, self.__class_takes__
    needs = dict()  # type: Dict[Key, Keys]
    for key in keys:
      needs[key] = (*sorted({*parentKeys[key], *takes[key]}, key=_byName),)
    groups = self._findGroups(needs)
    groupOf = {n: at for at, group in enumerate(groups) for n in group}
    groupNeeds = [
        {groupOf[need] for key in group for need in needs[key]} - {at}
        for at, group in enumerate(groups)
    ]
    ordered, placed = [], set()  # type: List[Key], Set[int]
    remaining = sorted(
        range(len(groups)), key=lambda at: _byName(groups[at][0]))
    while remaining:
      ready = [at for at in remaining if groupNeeds[at] <= placed]
      if not ready:
        infoSpec = """The groups of classes needing each other form a ring
        themselves, which cannot be. It is among: %s."""
        info = infoSpec % ', '.join(
            '%s' % (groups[at][0],) for at in remaining[:20])
        raise RuntimeError(' '.join(info.split()))
      for at in ready:
        ordered.extend(self._orderRing(groups[at]))
      placed.update(ready)
      remaining = [at for at in remaining if at not in placed]
    rings = sorted(
        (group for group in groups if len(group) > 1),
        key=lambda group: [_byName(key) for key in group])
    self.__class_rings__ = (*((*ring,) for ring in rings),)
    self.__make_places__ = {key: at for at, key in enumerate(ordered)}
    self.__make_order__ = (*ordered,)

  def getMakeOrder(self, **kwargs) -> Keys:
    """
    Gives every class of the tree, by its key, in an order to make the
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

    Keys
      A 'Tuple[Tuple[str, str], ...]' holding the same classes as
      'getClasses'.

    Raises
    ------

    MissingVariable
      'setHeaderReaders' has not been called.

    FileNotFoundError
      A part has not been read. Call its 'read' first.
    """
    if self.__make_order__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      self._createMakeOrder()
      return self.getMakeOrder(_recursion=True)
    return self.__make_order__

  def getRings(self) -> Tuple[Keys, ...]:
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

    Tuple[Keys, ...]
      For QtCore, QtGui and QtWidgets of Qt 6.12.0 it holds 19 rings of
      95 classes in all, the biggest of 21. A class in no ring is in
      none of the entries.
    """
    self.getMakeOrder()
    return self.__class_rings__

  def getTakenLater(self, className: str, partName: str) -> Keys:
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

    Keys
      It is empty for a class in no ring, and for most classes in one.

    Raises
    ------

    LookupError
      The tree has no class of that name.
    """
    takes = self.getTakes(className, partName)
    key = self.getClassKey(className, partName)
    self.getMakeOrder()
    places = self.__make_places__
    return (*(t for t in takes if places[t] > places[key]),)

  def getPartName(self, className: str, partName: str) -> str:
    """
    Gives the part of Qt the class a name stands for belongs to, seen
    from a part: 'getPartName("QObject", "QtWidgets")' gives 'QtCore'.

    Raises
    ------

    LookupError
      The tree has no class of that name.
    """
    return self.getClassKey(className, partName)[0]

  def getHeaderPath(self, className: str, partName: str) -> str:
    """
    Gives the full path of the header file a class is defined in.

    Raises
    ------

    LookupError
      The tree has no class of that name.
    """
    return self._lookUp('__class_places__', className, partName)

  def getHeaderReader(self, className: str, partName: str) -> HeaderReader:
    """
    Gives the 'HeaderReader' a class belongs to, of the ones you provided.

    Raises
    ------

    LookupError
      The tree has no class of that name.
    """
    owner = self.getPartName(className, partName)
    for headerReader in self.getHeaderReaders():
      if headerReader.getPartName() == owner:
        return headerReader
    raise RuntimeError("The part '%s' is not among the parts." % owner)

  def getClassRecord(self, className: str, partName: str) -> Record:
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
    number = self._lookUp('__class_numbers__', className, partName)
    headerPath = self.getHeaderPath(className, partName)
    headerReader = self.getHeaderReader(className, partName)
    for headerFile in headerReader.getHeaderFiles():
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

  def getEnumNames(self) -> Keys:
    """
    Gives every enum the parts declare, by its part and its full name,
    as ('QtCore', 'Qt::TimerType'), in alphabetical order.

    Kept beside the tree, from the same records. An enum is a list of
    names that each stand for a whole number. A function taking one
    needs nothing made first, so enums take no place in the order.
    """
    self.getClasses()
    return (*sorted(self.__enum_names__, key=_byName),)

  def getEnumTypes(self, partName: str) -> Dict[str, Tuple[str, str]]:
    """
    Gives, for each enum whose declaration says which number type its
    names are kept as, that type, seen from a part: as the header
    writes it, and as the compiler reads it. 'QEvent::Type' is not in
    it; an enum declared as 'enum class Kind : quint8' gives
    ('quint8', 'unsigned char').

    Kept beside the tree, from the same records. An enum that says
    nothing is kept as the compiler sees fit, which is an 'int' for
    every enum that needs no more room.

    Returns
    -------

    Dict[str, Tuple[str, str]]
      Under the full name of the enum, the two spellings of the type.
    """
    return self._seeTable('enumTypes', '__enum_types__', partName)

  def getEnumRecord(self, enumName: str, partName: str) -> Record:
    """
    Gives what the parts say of one enum that has names in it, seen
    from a part.

    Kept beside the tree, from the same records.

    Parameters
    ----------

    enumName : str
      The full name of the enum, as 'Qt::AlignmentFlag'.

    partName : str
      The part the name is seen from; see 'Terms'.

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
    self.getClasses()
    holder = self._findPart('enumRecords', enumName, partName)
    if holder is None:
      infoSpec = """The parts of Qt hold no enum named '%s' that has
      names in it."""
      raise ValueError(' '.join((infoSpec % enumName).split()))
    return dict(self.__enum_records__[(holder, enumName)])

  def getEnumRecordNames(self) -> Keys:
    """
    Gives every enum that has names in it, by its part and its full
    name, in alphabetical order. 'getEnumNames' also lists the enums a
    header only says exist.
    """
    self.getClasses()
    return (*sorted(self.__enum_records__, key=_byName),)

  def _createCopyableNames(self, ) -> None:
    """
    Asks the compiler which classes of the tree it can copy, and keeps
    the answer.

    A small C++ file is written into a folder of its own and compiled
    with 'clang++' to the text it would make an object file of, LLVM's
    IR. Nothing is joined to it and nothing is run: the compiler works
    every answer out itself, and writes them into that text as one
    letter for each class; see '_askCopyable'. The letter says whether
    these two lines of C++ are allowed for anyone: 'new T(other)',
    which makes a copy of another one, and 'delete' of the copy. The
    compiler alone knows that for sure. The records say it for a class
    that declares its copying itself, and leave it open for the many
    classes that let the compiler write it.

    Raises
    ------

    RuntimeError
      'clang++' refused the file, or the object file does not hold one
      letter for each class. What was said is in the message.
    """
    classKeys = self.getClasses()
    #  The folders of the headers Qt calls private, for the file of each
    #  part those of that part, its own first: two parts may each have
    #  a header by one name, as 'private/qabstractseries_p.h'.
    anyPrivate = any(
        reader.hasPrivate() for reader in self.getHeaderReaders())
    private = dict()  # type: Dict[str, List[str]]
    for headerReader in self.getHeaderReaders():
      private[headerReader.getPartName()] = [
          '-I%s' % folder
          for folder in headerReader.getPrivateIncludeFolders()
      ] if anyPrivate else []
    #  One file for the classes of each part, all compiled at once: the
    #  compiler is asked by one core each time.
    byPart = dict()  # type: Dict[str, List[Key]]
    for classKey in classKeys:
      byPart.setdefault(classKey[0], []).append(classKey)
    copyable, refused = set(), set()  # type: Set[Key], Set[Key]
    with ThreadPoolExecutor(os.cpu_count() or 1) as pool:
      for found, left in pool.map(
          lambda keys: self._findCopyable(keys, private[keys[0][0]]),
          byPart.values()):
        copyable.update(found)
        refused.update(left)
    self.__copyable_names__ = frozenset(copyable)
    self.__not_asked_copyable__ = frozenset(refused)

  def _findCopyable(
      self,
      classKeys: List[Key],
      private: List[str],
  ) -> Tuple[Set[Key], Set[Key]]:
    """
    Asks the compiler which of some classes of one part it can copy, as
    '_createCopyableNames' tells, in one file of their header files.
    Gives those it can copy, and those whose header files the compiler
    refused among the others.

    Raises
    ------

    RuntimeError
      The object file does not hold one letter for each class. Where
      'clang++' refuses the file for what no line can be taken out
      for, none of the classes counts as copyable.
    """
    #  The lines that pull in the header file of each class. A class
    #  whose header file no line can pull in counts as not copyable.
    linesOf = dict()  # type: Dict[Key, List[str]]
    includeLines = []  # type: List[str]
    unplaced = set()  # type: Set[Key]
    for classKey in classKeys:
      partName, className = classKey
      headerReader = self.getHeaderReader(className, partName)
      try:
        lines = headerReader.getIncludeLines(
            self.getHeaderPath(className, partName))
      except LookupError:
        unplaced.add(classKey)
        lines = ''
      linesOf[classKey] = [l for l in lines.split('\n') if l.strip()]
      for line in linesOf[classKey]:
        if line not in includeLines:
          includeLines.append(line)
    #  A header file Qt keeps apart may not compile among all the
    #  others, as QtBluetooth's 'qprivatelinearbuffer_p.h', which needs
    #  a size the file pulling it in defines. The lines the compiler
    #  names are taken out, the classes of their header files count as
    #  not copyable, and the file is compiled again.
    blocked, refused = set(), {*unplaced}  # type: Set[str], Set[Key]
    for _ in range(40):
      kept = [l for l in includeLines if l not in blocked]
      lines = [
          *kept,
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
          "//  One letter for each class, in order: '1' when it can be",
          "//  copied, '0' when not.",
          'extern const char cutienatorCopyable[];',
          'const char cutienatorCopyable[] = {',
      ]
      firstClassLine = len(lines) + 1
      lineSpec = "    char('0' + int(CanCopy<%s>::value)),"
      lines.extend(
          "    '0'," if key in refused else lineSpec % key[1]
          for key in classKeys)
      lines.extend(('    0,', '};', ''))
      said, stderr = self._askCopyable(lines, private)
      if said is not None:
        break
      named = {
          int(number) for number in re.findall(
              r'copyable\.cpp:(\d+):', stderr)}
      grown = False
      for number in sorted(named):
        if number <= len(kept):
          line = kept[number - 1]
          if line not in blocked:
            blocked.add(line)
            grown = True
        elif firstClassLine <= number < firstClassLine + len(classKeys):
          key = classKeys[number - firstClassLine]
          if key not in refused:
            refused.add(key)
            grown = True
      for key in classKeys:
        if key not in refused and any(
            line in blocked for line in linesOf[key]):
          refused.add(key)
          grown = True
      if not grown:
        #  The compiler refuses the file for what no line can be taken
        #  out for: none of these classes counts as copyable.
        return set(), {*classKeys}
    else:
      return set(), {*classKeys}
    if len(said) != len(classKeys) + 1 or said.strip(b'01') != b'\x00':
      infoSpec = """Asking the compiler which classes it can copy gave
      %d letters for %d classes, or other letters than '0' and '1'."""
      info = infoSpec % (len(said) - 1, len(classKeys))
      raise RuntimeError(' '.join(info.split()))
    copyable = set()  # type: Set[Key]
    for key, letter in zip(classKeys, said.decode('ascii')):
      if letter == '1':
        copyable.add(key)
    return copyable, refused

  def _askCopyable(
      self,
      lines: List[str],
      private: List[str],
  ) -> Tuple[Optional[bytes], str]:
    """
    Compiles the file of '_createCopyableNames' and gives the letters
    of its array 'cutienatorCopyable', with '' for what the compiler
    said; or None and what the compiler said when it refused the file.

    The letters are read from the text the compiler would make an
    object file of, LLVM's IR ('clang++ -S -emit-llvm'), the same on
    every system, where the array stands as
    '@cutienatorCopyable = constant [4 x i8] c"011\\00"'.

    Raises
    ------

    RuntimeError
      The compiled text holds no such array.
    """
    with tempfile.TemporaryDirectory() as folder:
      sourceFile = os.path.join(folder, 'copyable.cpp')
      compiledFile = os.path.join(folder, 'copyable.ll')
      with open(sourceFile, 'w') as file:
        file.write('\n'.join(lines))
      command = (
          'clang++', '-std=c++17', *Machine.getCompilerFlags(),
          '-S', '-emit-llvm', '-ferror-limit=0',
          '-I%s' % HeaderReader.getQtHeaderFolder(),
          *private, sourceFile, '-o', compiledFile,
      )
      with Machine.handOver(command) as words:
        done = subprocess.run(
            words, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            universal_newlines=True,
        )
      if done.returncode:
        return None, done.stderr
      with open(compiledFile, encoding='utf-8') as file:
        text = file.read()
    found = re.search(
        r'^@cutienatorCopyable = [^\n"]*\bc"([^"]*)"', text, re.M)
    if found is None:
      infoSpec = """Asking the compiler which classes it can copy gave
      no array 'cutienatorCopyable' in the text it compiled."""
      raise RuntimeError(' '.join(infoSpec.split()))
    #  In such a text a letter that is not plain stands as '\' and two
    #  hex digits, as the 0 at the end: '\00'.
    letters = re.sub(
        r'\\([0-9A-Fa-f]{2})', lambda match: chr(int(match.group(1), 16)),
        found.group(1))
    return letters.encode('latin-1'), ''

  def getCopyableNames(self, **kwargs) -> FrozenSet[Key]:
    """
    Gives every class of the tree that C++ can copy, by its key, as
    ('QtCore', 'QSize'). 'QObject' is not among them: Qt forbids
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
    self.getClasses()
    return self.__defined_names__

  def getDefinedPath(
      self,
      compilerName: str,
      partName: str,
  ) -> Optional[str]:
    """
    Gives the full path of the header file that has the body of code
    of a function, by the compiler's own name of the function, seen
    from a part, or None when no header file of the parts has it. Two
    classes of one name in two parts give their functions the same
    names.

    Kept with 'getDefinedNames'. A header declares some functions in a
    class and has their code in another header file, as 'qvariant.h'
    declares 'QVariant::PrivateShared::free' and 'qvariant_p.h' has
    its code. Whoever calls such a function has to pull that other
    header file in.

    Only the part and the parts it needs are looked in, as
    'getNeededParts' gives them: the code of a function seen from a
    part is in a header file that part can pull in. A part it does not
    build on may have code by the same name for a class of its own,
    as QtGraphs has for 'QBarDataItem::QBarDataItem()', which
    QtDataVisualization declares and writes the code of in a '.cpp'.
    """
    self.getClasses()
    holder = self._findPart('defined', compilerName, partName)
    if holder is None or holder not in self.getNeededParts(partName):
      return None
    return self.__defined_paths__[(holder, compilerName)]

  def isDefined(self, compilerName: str, partName: str) -> bool:
    """Says whether a header file has the body of code of a function,
    by the compiler's own name of it, seen from a part, as
    'getDefinedPath' finds it."""
    return self.getDefinedPath(compilerName, partName) is not None

  def getNeededParts(self, partName: str) -> Names:
    """
    Gives the part and the parts it needs, and the parts those need,
    the nearest first, as 'HeaderFolder.getPartNeeds' has them: the
    first parts of 'getPartOrder', before the others.

    Raises
    ------

    LookupError
      The tree has no part of that name.
    """
    self.getPartOrder(partName)
    return self.__needed_parts__[partName]

  def getAliasTypes(self, partName: str) -> Dict[str, str]:
    """
    Gives every other name the parts declare for a type, with the type
    it stands for, seen from a part: 'qsizetype' stands for 'long
    long', and 'QObjectList' for 'QList<QObject *>'.

    Kept beside the tree, from the same records. C++ lets a header
    give a type a second name, and functions then use either.
    """
    return self._seeTable('aliases', '__alias_types__', partName)

  def getSpellings(self, className: str, partName: str) -> Names:
    """
    Gives every name by which C++ code can write a class, its own name
    first.

    The others are of two kinds, both from the records. A name the
    parts give the class, as 'QLatin1StringView' from 'using
    QLatin1StringView = QLatin1String;'. And, for a class written
    inside another class, the same through each class built on that
    other class: 'QStringConverterBase::State' is also written
    'QStringConverter::State', since 'QStringConverter' is built on
    'QStringConverterBase'. Qt's source writes code under such names,
    as 'void QStringConverter::State::clear() noexcept'.

    Parameters
    ----------

    className : str
      The name of the class, with every class around it, as
      'QStringConverterBase::State'.

    partName : str
      The part the name is seen from; see 'Terms'.
    """
    others = dict()  # type: Dict[str, List[str]]
    for alias, cppType in sorted(self.getAliasTypes(partName).items()):
      bare = re.sub(r'^(?:class|struct)\s+', '', cppType.strip())
      others.setdefault(bare, []).append(alias)

    def named(fullName: str) -> List[str]:
      """The class by its full name and by every other name for it."""
      return [fullName, *others.get(fullName, ())]

    words = className.split('::')
    found = [words[0]]  # type: List[str]
    for depth, word in enumerate(words):
      own = '::'.join(words[:depth + 1])
      if depth:
        found = ['%s::%s' % (outer, word) for outer in found]
      found.extend(named(own)[1:])
      if depth < len(words) - 1 and self.hasClass(own, partName):
        for built in self.getDescendants(own, partName):
          found.extend(named(built[1]))
    return (*dict.fromkeys(found),)

  def getTreeText(self, *classKeys: Key) -> str:
    """
    Gives the tree as text, one class per line, each class two spaces
    further in than the class it is built on.

    Parameters
    ----------

    *classKeys : Key
      The classes to start from, each by its key and shown with all
      that is built on it. With none, every root is shown, which is
      the whole tree.

    Returns
    -------

    str
      The lines. A class with two parents stands under each of them.
      What is built on it is shown under its first parent only; under
      the others its line says where to look.

    Raises
    ------

    LookupError
      The tree has no class of one of the keys.
    """
    tops = classKeys or self.getRoots()
    lines = []  # type: List[str]
    for top in tops:
      if top != self.getClassKey(top[1], top[0]):
        infoSpec = """The part '%s' has no class named '%s'."""
        raise LookupError(infoSpec % top)
      self._writeBranch(top, None, 0, lines)
    return '\n'.join(lines)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setHeaderReaders(self, *headerReaders: HeaderReader) -> None:
    """
    Tells which parts of Qt to make the tree of.

    Required. Calling it again forgets the tree made before.

    Parameters
    ----------

    *headerReaders : HeaderReader
      One or more parts, each with its name and work folder set and
      already read. A class built on a class of another part finds its
      parent only when that part is given too: give 'QtCore' and
      'QtGui' along with 'QtWidgets'.

    Raises
    ------

    ValueError
      Called with no part at all.

    TypeException
      An argument is not a 'HeaderReader'.
    """
    if not headerReaders:
      infoSpec = """A dependency tree needs at least one part of Qt, and
      none was given."""
      raise ValueError(' '.join(infoSpec.split()))
    for headerReader in headerReaders:
      if not isinstance(headerReader, HeaderReader):
        raise TypeException('headerReader', headerReader, HeaderReader)
    self.__header_readers__ = (*headerReaders,)
    self.__kept_for_users__ = dict()
    self.__cute_names__ = None
    self.__ordered_names__ = None
    self.__class_parents__ = None
    self.__parent_keys__ = None
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
    self.__defined_paths__ = None
    self.__classes_by_part__ = None
    self.__part_orders__ = None
    self.__needed_parts__ = None
    self.__part_scopes__ = None
    self.__missed_classes__ = None
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
    if self.__header_readers__ is None:
      return '<%s still waiting for: setHeaderReaders>' % clsName
    names = ', '.join(part.getPartName() for part in self.__header_readers__)
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

  def _lookUp(self, tableName: str, className: str, partName: str) -> Any:
    """
    Gives what one of the tables of the tree holds for a class, making
    the tree first when it is not made yet.

    Parameters
    ----------

    tableName : str
      The private variable holding the table, as '__class_parents__'.

    className : str
      The class to look up.

    partName : str
      The part the name is seen from; see 'Terms'.

    Raises
    ------

    LookupError
      The tree has no class of that name.
    """
    return getattr(self, tableName)[self.getClassKey(className, partName)]

  def _orderParts(self, partNames: List[str]) -> Dict[str, Names]:
    """
    Gives, for each part, the parts a name seen from it is looked up
    in, in order: the part itself; the parts it needs, as
    'HeaderFolder.getPartNeeds' has them, and the parts those need,
    the nearest first; and then the other parts, in the order read.
    """
    orders = dict()  # type: Dict[str, Names]
    needed = dict()  # type: Dict[str, Names]
    for partName in partNames:
      order = [partName]  # type: List[str]
      at = 0
      while at < len(order):
        try:
          needs = HeaderFolder.getPartNeeds(order[at])
        except LookupError:
          needs = ()
        order.extend(need for need in needs if need not in order)
        at += 1
      order = [one for one in order if one in partNames]
      needed[partName] = (*order,)
      order.extend(one for one in partNames if one not in order)
      orders[partName] = (*order,)
    self.__needed_parts__ = needed
    return orders

  def _getHolders(self, kind: str) -> Dict[str, Names]:
    """
    Gives, for each name of one kind, the parts that have something by
    that name, in the order read. The kinds: 'classes', 'enumRecords',
    'enumTypes', 'aliases' and 'defined', the names of functions whose
    code a header file holds.
    """
    held = self.__part_scopes__.get((kind, ''))
    if held is not None:
      return held
    if kind == 'classes':
      keys = [
          (partName, name)
          for partName, classes in self.__classes_by_part__.items()
          for name in classes]  # type: List[Key]
    else:
      tables = dict(
          enumRecords=self.__enum_records__, enumTypes=self.__enum_types__,
          aliases=self.__alias_types__, defined=self.__defined_paths__)
      keys = [*tables[kind]]
    place = {name: at for at, name in enumerate(self.__classes_by_part__)}
    collected = dict()  # type: Dict[str, List[str]]
    for partName, name in sorted(keys, key=lambda key: place[key[0]]):
      collected.setdefault(name, []).append(partName)
    held = {name: (*parts,) for name, parts in collected.items()}
    self.__part_scopes__[(kind, '')] = held
    return held

  def _findPart(self, kind: str, name: str, partName: str) -> Optional[str]:
    """
    Gives the part a name of one kind is looked up in, seen from a
    part: of the parts that have something by that name, the one that
    comes first in the order '_orderParts' gives that part. None when
    no part has anything by that name.
    """
    order = self.__part_orders__.get(partName)
    if order is None:
      infoSpec = """A name is seen from the part '%s', which is no part
      of the tree."""
      raise LookupError(' '.join((infoSpec % partName).split()))
    holders = self._getHolders(kind).get(name)
    if not holders:
      return None
    if len(holders) == 1:
      return holders[0]
    return min(holders, key=order.index)

  def _seeTable(
      self,
      kind: str,
      tableName: str,
      partName: str,
  ) -> Dict[str, Any]:
    """Gives a table of the tree kept under keys as it is seen from a
    part: under each name, what the part '_findPart' finds has."""
    self.getClasses()
    kept = self.__part_scopes__.get((kind, partName))
    if kept is None:
      table = getattr(self, tableName)
      kept = {
          name: table[(self._findPart(kind, name, partName), name)]
          for name in self._getHolders(kind)}
      self.__part_scopes__[(kind, partName)] = kept
    return dict(kept)

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
        found['defined'].setdefault(node['mangledName'], headerPath)
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
  ) -> Optional[str]:
    """
    Gives the full name of a declared class, as C++ names it, and keeps
    it in 'names'.

    A class belongs to the class it is written inside. A class defined
    away from the class it belongs to, as 'QMetaObject::Connection' is,
    carries the number of that class instead, and is named after it.

    Gives None, and writes the class down in 'getMissedClasses', when
    it belongs to something that was not read.
    """
    if entryId in names:
      return names[entryId]
    entry = entries[entryId]
    owner = entry['belongsToId'] or entry['insideId']
    if owner is None:
      name = '%s%s' % (entry['prefix'], entry['ownName'])
    elif owner in entries:
      outer = self._nameEntry(owner, entries, namespaces, names)
      if outer is None:
        return None
      name = '%s::%s' % (outer, entry['ownName'])
    elif owner in namespaces:
      name = '%s::%s' % (namespaces[owner], entry['ownName'])
    elif entry['belongsToId'] is not None and entry['insideId'] in entries:
      #  Named first inside a class, in what one of its functions takes,
      #  as 'void setStore(class QHstsStore *store);' in Qt's
      #  'qhsts_p.h': C++ declares such a class in the namespace around
      #  the class, here the file's own.
      name = '%s%s' % (entry['prefix'], entry['ownName'])
    else:
      infoSpec = """It belongs to something that was not read with its
      part of Qt; it is written in '%s'."""
      self._missClass(entry['ownName'], infoSpec % entry['headerPath'])
      return None
    names[entryId] = name
    return name

  def _missClass(self, name: str, reason: str) -> None:
    """Writes down a class the tree leaves out, and why, for
    'getMissedClasses'."""
    if self.__missed_classes__ is None:
      self.__missed_classes__ = dict()
    self.__missed_classes__.setdefault(name, ' '.join(reason.split()))

  def getMissedClasses(self) -> Dict[str, str]:
    """
    Gives each class the tree leaves out for an edge case of Qt's
    source it has no rule for, under its name, with why, as a class
    that two parts each define on their own. They are for a pass by
    hand, class by class: a rule in the tree only where many classes
    share the case.
    """
    self.getClasses()
    return dict(self.__missed_classes__ or ())

  def addMissedClass(self, name: str, reason: str) -> None:
    """
    Writes down a class a generator leaves out, and why, for
    'getMissedClasses', as the classes of a part RitualGenerator's
    probe header leaves out. A name written down before keeps its
    first reason.
    """
    self._missClass(name, reason)

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

  def _findClasses(self, cppTypes: Set[str], itself: Key) -> Keys:
    """
    Gives the classes of the tree named anywhere in some types, seen
    from the part of the class the types belong to, in alphabetical
    order, leaving out that class.
    """
    found = set()  # type: Set[Key]
    for cppType in cppTypes:
      for name in self.__name_pattern__.findall(cppType):
        holder = self._findPart('classes', name, itself[0])
        while name and holder is None:
          name = name.rpartition('::')[0]
          holder = self._findPart('classes', name, itself[0])
        if name and (holder, name) != itself:
          found.add((holder, name))
    return (*sorted(found, key=_byName),)

  def _orderNames(self, parentKeys: Dict[Key, Keys]) -> Keys:
    """
    Puts the classes in an order with every parent before its children,
    the alphabet deciding where the tree leaves a choice.

    Raises
    ------

    RuntimeError
      The classes built on each other form a ring.
    """
    waitingFor = {key: {*parentKeys[key]} for key in parentKeys}
    ordered, placed = [], set()  # type: List[Key], Set[Key]
    remaining = sorted(parentKeys, key=_byName)
    while remaining:
      ready = [n for n in remaining if waitingFor[n] <= placed]
      if not ready:
        infoSpec = """The classes built on each other form a ring, among:
        %s."""
        info = infoSpec % ', '.join('%s' % (key,) for key in remaining[:20])
        raise RuntimeError(' '.join(info.split()))
      ordered.extend(ready)
      placed.update(ready)
      remaining = [n for n in remaining if n not in placed]
    return (*ordered,)

  def _findGroups(self, needs: Dict[Key, Keys]) -> List[List[Key]]:
    """
    Sorts the classes into groups: two classes are in one group when
    each needs the other, straight or through other classes. A group of
    more than one class is a ring.

    Parameters
    ----------

    needs : Dict[Key, Keys]
      For each class, the classes of the tree it is built on or takes,
      in alphabetical order.

    Returns
    -------

    List[List[Key]]
      The groups, each in alphabetical order. Every class is in exactly
      one.
    """
    #  Tarjan's way of finding such groups, written without a function
    #  calling itself, since a chain of classes can be long. 'number' is
    #  when a class was first met, 'lowest' the earliest class it can
    #  get back to, and 'trail' the classes met and not yet grouped.
    number, lowest = dict(), dict()  # type: Dict[Key, int], Dict[Key, int]
    trail, onTrail = [], set()  # type: List[Key], Set[Key]
    groups = []  # type: List[List[Key]]
    for root in sorted(needs, key=_byName):
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
            group = []  # type: List[Key]
            while not group or group[-1] != name:
              group.append(trail.pop())
              onTrail.discard(group[-1])
            groups.append(sorted(group, key=_byName))
          if work:
            above = work[-1][0]
            lowest[above] = min(lowest[above], lowest[name])
    return groups

  def _orderRing(self, ring: List[Key]) -> List[Key]:
    """
    Puts the classes of one ring in an order to make them in.

    No order of a ring has every class after all it takes. A class
    still comes after every class it is built on. Among the classes
    whose parents are placed, the next one is the class that most
    others of the ring are still waiting for, less the number it is
    still waiting for itself. The alphabet decides between equals.

    Parameters
    ----------

    ring : List[Key]
      The classes of one group, in alphabetical order. A group of one
      class is given back as it is.
    """
    if len(ring) < 2:
      return [*ring]
    inside = set(ring)
    parents, takes = self.__parent_keys__, self.__class_takes__
    ordered, placed = [], set()  # type: List[Key], Set[Key]
    while len(ordered) < len(ring):
      best, bestScore = None, 0  # type: Optional[Key], int
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
        if best is None or waiting - wanted < bestScore:
          best, bestScore = name, waiting - wanted
      if best is None:
        infoSpec = """The classes built on each other form a ring, among:
        %s."""
        info = infoSpec % ', '.join('%s' % (key,) for key in ring)
        raise RuntimeError(' '.join(info.split()))
      ordered.append(best)
      placed.add(best)
    return ordered

  def _writeBranch(
      self,
      classKey: Key,
      under: Optional[Key],
      depth: int,
      lines: List[str],
  ) -> None:
    """Writes one class and all that is built on it, as lines of text."""
    known = [*self.__parent_keys__[classKey]]
    others = [p[1] for p in known if p != under]
    line = '%s%s' % ('  ' * depth, classKey[1])
    if under is not None and known and known[0] != under:
      lines.append('%s  (see under %s)' % (line, known[0][1]))
      return
    if others and under is not None:
      line = '%s  (also built on %s)' % (line, ', '.join(others))
    lines.append(line)
    for child in self.__class_children__[classKey]:
      self._writeBranch(child, classKey, depth + 1, lines)

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
