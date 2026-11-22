"""
CuteMap is what the cute QMap and the cute QHash have in common.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, Iterator, List, Optional, Tuple


class CuteMap(CuteMixin, metaclass=MetaCute):
  """
  The maps of Qt: QMap and QHash, each standing for a value at each of
  its keys. Qt has one class of map for each kind of key and value, and
  so has cutienator: 'QMap[int, QVariant]' is the class of the maps
  from a number to a QVariant, which C++ writes 'QMap<int, QVariant>'.

    roles = QMap[int, QVariant]({1: QVariant('a')})
    len(roles), roles[1], 1 in roles
    for key in roles: ...
    roles.insert(2, QVariant('b'))

  You never use this class by name. It holds what 'QMap' and 'QHash'
  share, which in Qt are two classes with nothing in common but their
  functions: neither is built on the other, and neither is here.

  Terms
  -----

  - A kind is one class of map: the QMaps from a number to a QVariant
    are one kind, the QHashes from a number to a QByteArray another.
    C++ has compiled code for the kinds its own functions hand around,
    and for no others.
  - A root is 'QMap' or 'QHash' itself, which is of no kind.

  What to expect
  --------------

  - A key is an 'int' or a 'str', as its kind says, and a value is of
    the class its kind holds. Anything else is refused with
    'TypeError', on the line that hands it over.
  - 'QMap[...]' with what Qt has no map of raises 'TypeError'.
  - A function of Qt that takes a map takes a dict of Python as well:
    the map of Qt is made from it, every key and value checked, and the
    call is refused when one does not fit.
  - A function of Qt that gives a map gives an object of the class of
    its kind. It reads as a dict of Python reads: 'len', '[key]', 'in'
    and 'for', which goes through the keys. It is a copy, which Python
    owns: changing it changes nothing in Qt.
  - '[key]' raises 'KeyError' for a key the map does not have. Qt's
    own 'value(key)' gives a value made from nothing for such a key,
    and so does 'value' here.
  - A map never waits for the class of its values. 'QMap[int,
    QVariant]' is the class of that kind from the line that names it,
    also where QVariant is still a 'WAIT', and brings the file of
    QVariant in itself the first time it needs it. So an empty dict
    goes through a function that takes such a map whether or not the
    program ever made a QVariant.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  In a root: the class of Qt it stands for, 'QMap' or 'QHash'. The
  #  class that names it in its own body is a root.
  __map_pattern__: Optional[str] = None
  #  In a root: the class of each kind collected so far, under the name
  #  of its key class and the name of its value class.
  __map_kinds__: Optional[Dict[Tuple[str, str], type]] = None
  #  In the class of a kind: the class of its keys, 'int' or 'str'; the
  #  name of the class of its values, as 'QVariant'; that class, once
  #  its file is brought in; how one value crosses to C++ ('value' or
  #  'address'); and the rituals of the map, under 'make', 'put',
  #  'size', 'key', 'value', 'has', 'get' and 'drop'.
  __key_class__: Optional[type] = None
  __value_name__: Optional[str] = None
  __value_class__: Optional[type] = None
  __value_crossing__: Optional[str] = None
  __map_rituals__: Optional[Dict[str, str]] = None

  #  Fallback Variables

  #  Private Variables
  #  What a map was made of, kept until its C++ map is made.
  __kept_pairs__: Optional[list] = None

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def _getRoot(cls) -> type:
    """
    Gives the root a class of maps is built on: 'QMap' or 'QHash'.

    Raises
    ------

    TypeError
      The class is 'CuteMap' itself, which stands for no class of Qt.
    """
    for one in cls.__mro__:
      if one.__dict__.get('__map_pattern__', None) is not None:
        return one
    infoSpec = """'%s' stands for no class of Qt. The maps of Qt are
    'QMap' and 'QHash'."""
    raise TypeError(' '.join((infoSpec % cls.__name__).split()))

  @classmethod
  def _getKinds(cls) -> Dict[Tuple[str, str], type]:
    """Gives the classes of the kinds of one root collected so far.
    Kept on the root itself: 'QMap' and 'QHash' have a table each."""
    root = cls._getRoot()
    if root.__dict__.get('__map_kinds__', None) is None:
      type.__setattr__(root, '__map_kinds__', dict())
    return root.__dict__['__map_kinds__']

  @classmethod
  def _getKind(cls) -> type:
    """
    Gives the class of the kind a class of maps is of: the class
    itself, or the class of a kind it is built on.

    Raises
    ------

    TypeError
      The class is a root, which is of no kind.
    """
    for one in cls.__mro__:
      if one.__dict__.get('__value_name__', None) is not None:
        return one
    infoSpec = """A map is of one kind, as QMap[int, QVariant]({...}).
    '%s' alone says nothing of what the map holds."""
    raise TypeError(' '.join((infoSpec % cls.__name__).split()))

  @classmethod
  def _getMadeKind(cls) -> type:
    """
    Gives the class of the kind a class of maps is of, completed: it
    knows the class of its values and its rituals.

    A kind a class body named before the class of its values was
    brought in knows only the name of that class. The file of the class
    is brought in here, and ends with 'createKind', which completes the
    kind.

    Raises
    ------

    TypeError
      The class is a root. Or no part of Qt has a class of the name, or
      its file completes no such kind: Qt has no map of it.
    """
    kind = cls._getKind()
    if kind.__value_class__ is None:
      name = kind.__value_name__
      for partName in Rituals.getQtParts():
        package = importlib.import_module('..%s' % partName, __package__)
        if name in package.__class_files__:
          getattr(package, name)
          break
    if kind.__value_class__ is None:
      infoSpec = """Qt has no '%s' that cutienator knows."""
      raise TypeError(infoSpec % kind.__name__)
    return kind

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def __class_getitem__(cls, pair: Any) -> Any:
    """
    Gives the class of the maps of one kind: 'QMap[int, QVariant]'.

    Parameters
    ----------

    pair : Any
      The class of the keys, 'int' or 'str', and the class of the
      values: a cute class, or a 'WAIT' for one that is not brought in
      yet. The class of the kind is then given by the name alone, and
      completed later.

    Raises
    ------

    TypeError
      Qt has no such map that cutienator knows, or the class
      subscripted is the class of a kind already.
    """
    root = cls._getRoot()
    if cls is not root:
      infoSpec = """'%s' is the class of one kind of map already."""
      raise TypeError(infoSpec % cls.__name__)
    infoSpec = """Qt has no '%s[%s]' that cutienator knows."""
    if not isinstance(pair, tuple) or len(pair) != 2:
      raise TypeError(infoSpec % (cls.__name__, pair))
    key, value = pair
    late = isinstance(value, WAIT)
    if late:
      valueName = value.getWaitingName()
    else:
      valueName = getattr(value, '__name__', None)
    keyName = getattr(key, '__name__', None)
    shown = '%s, %s' % (keyName, valueName)
    if key is not int and key is not str:
      raise TypeError(infoSpec % (cls.__name__, shown))
    if not isinstance(valueName, str):
      raise TypeError(infoSpec % (cls.__name__, shown))
    if not late and not isinstance(value, type):
      raise TypeError(infoSpec % (cls.__name__, shown))
    kinds = cls._getKinds()
    if (keyName, valueName) not in kinds and late:
      kinds[keyName, valueName] = cls._createNamedKind(key, valueName)
    try:
      kind = kinds[keyName, valueName]
    except KeyError:
      raise TypeError(infoSpec % (cls.__name__, shown)) from None
    if not late and kind.__value_class__ is not value:
      #  Another class of the same name, as one of a program.
      raise TypeError(infoSpec % (cls.__name__, shown))
    return kind

  @classmethod
  def __cast_as__(cls, value: Any) -> Any:
    """
    Says what a signature naming one kind of map takes in the place of
    a map of that kind: a dict of Python whose every key and value
    fits. worktoy asks this when a call hands a function something
    else than a map of the kind.

    Returns
    -------

    Any
      A new map of the kind made of the dict, or 'NotImplemented' for
      anything else, and for a dict with a key or a value the kind does
      not hold.
    """
    if cls.__value_name__ is None or not isinstance(value, dict):
      return NotImplemented
    try:
      return cls(value)
    except TypeError:
      return NotImplemented

  def __len__(self) -> int:
    """Gives how many keys the map has."""
    return self.size()

  def __contains__(self, key: Any) -> bool:
    """Says whether the map has a key. What is no key of the kind is in
    no map of it."""
    try:
      return self.contains(key)
    except TypeError:
      return False

  def __getitem__(self, key: Any) -> Any:
    """
    Gives the value at a key.

    Raises
    ------

    KeyError
      The map has no such key.
    """
    if key not in self:
      raise KeyError(key)
    return self.value(key)

  def __iter__(self) -> Iterator:
    """Gives the keys, in the order Qt keeps them."""
    yield from self.keys()

  def __str__(self) -> str:
    """Shows the map as it is made: its kind, its keys and values."""
    shown = ', '.join('%r: %s' % pair for pair in self.items())
    return '%s({%s})' % (self._getKind().__name__, shown)

  __repr__ = __str__

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def _createNamedKind(cls, key: type, valueName: str) -> type:
    """Makes the class of the maps of one kind by its key class and the
    name of its value class alone. 'createKind' completes it."""
    root = cls._getRoot()
    pattern = root.__dict__['__map_pattern__']
    keyName = dict(int='int', str='QString')[key.__name__]
    space = dict(
        __qt_class__='%s<%s, %s>' % (pattern, keyName, valueName),
        __key_class__=key, __value_name__=valueName,
    )
    kindName = '%s[%s, %s]' % (root.__name__, key.__name__, valueName)
    return type(root)(kindName, (root,), space)

  @classmethod
  def createKind(
      cls,
      keyClass: type,
      valueClass: type,
      crossing: str,
      name: Optional[str] = None,
      **rituals: str,
  ) -> type:
    """
    Completes the class of the maps of one kind, making it first when
    no class body named it yet. The class files the dev tooling writes
    call this at their end, on 'QMap' or on 'QHash', for a class some
    map of Qt holds as its values.

    Parameters
    ----------

    keyClass : type
      The class of the keys: 'int' or 'str'.

    valueClass : type
      The cute class of the values.

    crossing : str
      How one value crosses to C++: 'value' for a copy, 'address' for
      the address of an object.

    name : Optional[str]
      The name Qt has for the kind, as 'QVariantMap'. Without one the
      class is named as it is asked for: 'QMap[int, QVariant]'.

    **rituals : str
      The rituals of the map: 'make', 'put', 'size', 'key', 'value',
      'has', 'get' and 'drop'. Two of them are named 'key' and 'value',
      which is why the two classes above are not.

    Returns
    -------

    type
      The class of the kind, which 'QMap[keyClass, valueClass]' gives.
    """
    kinds = cls._getKinds()
    names = (keyClass.__name__, valueClass.__name__)
    try:
      kind = kinds[names]
    except KeyError:
      kind = cls._createNamedKind(keyClass, valueClass.__name__)
      kinds[names] = kind
    type.__setattr__(kind, '__value_class__', valueClass)
    type.__setattr__(kind, '__value_crossing__', crossing)
    type.__setattr__(kind, '__map_rituals__', rituals)
    type.__setattr__(kind, '__delete_ritual__', rituals['drop'])
    if name is not None:
      type.__setattr__(kind, '__name__', name)
      type.__setattr__(kind, '__qualname__', name)
    return kind

  @classmethod
  def _cuteOwning(cls, address: int) -> Any:
    """Gives a new map around a C++ map a ritual made for Python, as
    'CuteMixin._cuteOwning' does, completing the kind first if need
    be."""
    cls._getMadeKind()
    return super()._cuteOwning(address)

  @overload()
  def __init__(self) -> None:
    """Makes an empty map. The C++ map is made at the first use."""
    kind = self._getMadeKind()
    make = kind.__map_rituals__['make']
    self._noteCreation(kind, lambda: Rituals.call(make))

  @overload(dict)
  def __init__(self, pairs: dict) -> None:
    """
    Makes a map of the keys and values of a dict of Python. Each is
    checked here, on the line that makes the map. The C++ map is made
    at the first use.

    Raises
    ------

    TypeError
      A key or a value is not of what the kind holds.
    """
    kind = self._getMadeKind()
    rituals = kind.__map_rituals__
    handed = [
        (self._handKey(key), self._handValue(value))
        for key, value in pairs.items()
    ]

    def create() -> int:
      """Makes the C++ map and puts each pair in."""
      address = Rituals.call(rituals['make'])
      for key, value in handed:
        Rituals.call(rituals['put'], address, key, value)
      self.__kept_pairs__ = None
      return address

    #  What was handed over for a value is the address of its C++
    #  object, so the pairs are kept until the C++ map is made.
    self.__kept_pairs__ = [*pairs.items()]
    self._noteCreation(kind, create)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _handKey(self, key: Any) -> Any:
    """
    Gives a key as the rituals of the map take it, and refuses one the
    kind does not have.

    Raises
    ------

    TypeError
      The key is not of the class of the keys. A 'bool' is no 'int'
      here.
    """
    kind = self._getKind()
    wanted = kind.__key_class__
    if isinstance(key, wanted) and not isinstance(key, bool):
      return key
    infoSpec = """A '%s' has '%s' for its keys and nothing else, but
    was handed '%s'."""
    info = infoSpec % (kind.__name__, wanted.__name__, type(key).__name__)
    raise TypeError(' '.join(info.split()))

  def _handValue(self, value: Any) -> Any:
    """
    Turns a value into what the rituals of the map take in its place,
    and refuses one the kind does not hold.

    Raises
    ------

    TypeError
      The value is not of what the kind holds.
    """
    kind = self._getMadeKind()
    wanted, crossing = kind.__value_class__, kind.__value_crossing__
    if not isinstance(value, wanted):
      infoSpec = """A '%s' holds '%s' and nothing else, but was handed
      '%s'."""
      info = infoSpec % (
          kind.__name__, wanted.__name__, type(value).__name__)
      raise TypeError(' '.join(info.split()))
    if crossing == 'value':
      return CuteMixin._valueOf(value)
    return CuteMixin._addressOf(value)

  def _takeValue(self, given: Any) -> Any:
    """Turns what a ritual of the map gives for a value into the value:
    a new cute object around a copy, or the cute object standing for
    an address."""
    kind = self._getMadeKind()
    wanted = kind.__value_class__
    if kind.__value_crossing__ == 'value':
      return wanted._cuteOwning(given)
    return wanted._cuteAt(given)

  def _call(self, role: str, *args: Any) -> Any:
    """Runs one ritual of the map on the C++ map."""
    ritual = self._getMadeKind().__map_rituals__[role]
    return self.uglySide.call(ritual, *args)

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

  def size(self) -> int:
    """Calls Qt's 'size() const': how many keys the map has."""
    return self._call('size')

  def contains(self, key: Any) -> bool:
    """
    Calls Qt's 'contains(const Key &key) const'.

    Raises
    ------

    TypeError
      The key is not of the class of the keys.
    """
    return self._call('has', self._handKey(key))

  def value(self, key: Any) -> Any:
    """
    Calls Qt's 'value(const Key &key) const'. For a key the map does
    not have, Qt gives a value made from nothing; '[key]' raises
    'KeyError' there.

    Raises
    ------

    TypeError
      The key is not of the class of the keys.
    """
    return self._takeValue(self._call('get', self._handKey(key)))

  def insert(self, key: Any, value: Any) -> None:
    """
    Calls Qt's 'insert(const Key &key, const T &value)': puts a value
    at a key, in the place of the one that was there.

    Raises
    ------

    TypeError
      The key or the value is not of what the kind holds.
    """
    self._call('put', self._handKey(key), self._handValue(value))

  def keys(self) -> List[Any]:
    """Gives the keys as a list of Python, in the order Qt keeps
    them."""
    return [self._call('key', place) for place in range(self.size())]

  def values(self) -> List[Any]:
    """Gives the values as a list of Python, in the order of 'keys'."""
    return [
        self._takeValue(self._call('value', place))
        for place in range(self.size())
    ]

  def items(self) -> List[Tuple[Any, Any]]:
    """Gives each key with its value, in the order of 'keys'."""
    return [*zip(self.keys(), self.values())]
