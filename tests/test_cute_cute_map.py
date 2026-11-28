"""
TestCuteCuteMap tests 'CuteMap', what the cute QMap and the cute QHash
have in common.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import sys
import types
import weakref
from typing import TYPE_CHECKING
from unittest import mock

from worktoy.work_test import BaseTest

from cutienator.cute import CuteMap, CuteMixin, MetaCute, WAIT
from cutienator.occult import Rituals, Ugly

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict

#  Addresses no real object has, one for each object that needs one.
_FAKE = 0x7eaf0000

#  The rituals of a made-up map, by their role.
_RITUALS = dict(
    make='map_make', put='map_put', size='map_size', key='map_key',
    value='map_value', has='map_has', get='map_get', drop='map_drop',
)


class TestCuteCuteMap(BaseTest):
  """
  Tests 'CuteMap' through a made-up root, 'FakeMap', standing for a
  made-up class of Qt 'QFakeMap': the class of each kind, completing a
  kind named before its class of values was brought in, and a map read
  as a dict of Python reads.

  What to know before adding a test
  ---------------------------------

  - Each test has a fresh record of the classes 'MetaCute' made, and a
    root, 'self.root', with no kinds yet. 'self.Item' is a made-up
    value class, crossing as a copy, and 'self.Thing' a made-up class
    crossing by its address.
  - No ritual is run. 'Rituals.call' runs the rituals of the map on a
    dict of Python per made-up address, in 'self.maps'. The value Qt
    makes from nothing, for a key a map does not have, is at
    'self.blank'.
  - A part of Qt named 'QtFake' is found as the package
    'cutienator.QtFake', a module put in 'sys.modules', and 'QtEmpty'
    as one with no classes. Bringing in 'Later' from 'QtFake' completes
    the kind of maps from 'int' to it; 'Hollow' completes nothing.
  """

  __count__ = 0

  def setUp(self) -> None:
    """A fresh record of the classes made, a root, two value classes,
    the rituals of the map, and the made-up parts."""
    super().setUp()
    for name in ('__made_classes__', '__waiting_fields__'):
      patcher = mock.patch.object(MetaCute, name, dict())
      patcher.start()
      self.addCleanup(patcher.stop)

    class FakeMap(CuteMap):
      __map_pattern__ = 'QFakeMap'

    class Item(CuteMixin, metaclass=MetaCute):
      __qt_class__ = 'Item'
      __delete_ritual__ = 'item_drop'

    class Thing(CuteMixin, metaclass=MetaCute):
      __qt_class__ = 'Thing'

    self.root, self.Item, self.Thing = FakeMap, Item, Thing
    self.maps = dict()  # type: Dict[int, Dict[Any, Any]]
    self.blank = self._address()
    self.seen = []
    for patcher in (
        mock.patch.object(Rituals, 'call', self._call),
        mock.patch.object(Rituals, 'getComponents',
                          return_value=('QtEmpty', 'QtFake')),
        mock.patch.object(
            Ugly, '__by_address__', weakref.WeakValueDictionary()),
        mock.patch.dict(sys.modules, {
            'cutienator.QtFake': self._fakePart(),
            'cutienator.QtEmpty': self._emptyPart(),
        }),
    ):
      patcher.start()
      self.addCleanup(patcher.stop)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def _address(cls) -> int:
    """A made-up address, another for each call."""
    cls.__count__ += 1
    return _FAKE + 64 * cls.__count__

  def _call(self, name: str, *args: Any) -> Any:
    """Runs a ritual of the made-up map on 'self.maps'; any other ritual
    gives None."""
    self.seen.append(name)
    if name == 'map_make':
      address = self._address()
      self.maps[address] = dict()
      return address
    if not name.startswith('map_'):
      return None
    pairs = self.maps[args[0]]
    if name == 'map_put':
      pairs[args[1]] = args[2]
    elif name == 'map_size':
      return len(pairs)
    elif name == 'map_key':
      return [*pairs][args[1]]
    elif name == 'map_value':
      return [*pairs.values()][args[1]]
    elif name == 'map_has':
      return args[1] in pairs
    elif name == 'map_get':
      return pairs.get(args[1], self.blank)
    return None

  def _fakePart(self) -> types.ModuleType:
    """The made-up part 'QtFake': bringing in 'Later' completes a kind,
    bringing in 'Hollow' does not."""
    part = types.ModuleType('cutienator.QtFake')
    part.__class_files__ = dict(Later='_later', Hollow='_hollow')
    test = self

    def bringIn(name: str) -> type:
      if name not in part.__class_files__:
        raise AttributeError(name)

      class Brought(CuteMixin, metaclass=MetaCute):
        __qt_class__ = name

      Brought.__name__ = name
      if name == 'Later':
        test.root.createKind(int, Brought, 'value', **_RITUALS)
      setattr(part, name, Brought)
      return Brought

    part.__getattr__ = bringIn
    return part

  @staticmethod
  def _emptyPart() -> types.ModuleType:
    """The made-up part 'QtEmpty', with no classes."""
    part = types.ModuleType('cutienator.QtEmpty')
    part.__class_files__ = dict()
    return part

  def _items(self) -> type:
    """The kind of maps from 'int' to 'Item', completed."""
    return self.root.createKind(int, self.Item, 'value', **_RITUALS)

  def _made(self, cls: type) -> Any:
    """An object of a value class, its C++ object made at a made-up
    address."""
    cute = cls()
    address = self._address()
    cute._noteCreation(cls, lambda: address)
    self.assertEqual(cute.uglySide.getAddress(), address)
    return cute

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  ROOTS AND KINDS  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_root_of_a_class(self) -> None:
    """A root is its own; a kind is of its root; 'CuteMap' is of none."""
    kind = self._items()
    self.assertIs(self.root._getRoot(), self.root)
    self.assertIs(kind._getRoot(), self.root)
    with self.assertRaises(TypeError) as caught:
      CuteMap._getRoot()
    self.assertIn("'CuteMap' stands for no class of Qt",
                  str(caught.exception))

  def test_each_root_keeps_its_kinds(self) -> None:
    """The table of kinds is made at the first asking, on the root, and
    a kind reads its root's; another root has its own."""

    class OtherMap(CuteMap):
      __map_pattern__ = 'QOtherMap'

    kinds = self.root._getKinds()
    self.assertEqual(kinds, {})
    self.assertIs(self.root._getKinds(), kinds)
    kind = self._items()
    self.assertIs(kind._getKinds(), kinds)
    self.assertEqual(kinds, {('int', 'Item'): kind})
    self.assertEqual(OtherMap._getKinds(), {})

  def test_the_kind_of_a_class(self) -> None:
    """A kind is its own, and a class built on it is of it; a root is
    of no kind."""
    kind = self._items()

    class Mine(kind):
      pass

    self.assertIs(kind._getKind(), kind)
    self.assertIs(Mine._getKind(), kind)
    with self.assertRaises(TypeError) as caught:
      self.root._getKind()
    self.assertIn("'FakeMap' alone says nothing", str(caught.exception))

  def test_a_kind_by_its_classes(self) -> None:
    """'createKind' makes the class of a kind, named as it is asked for,
    standing for the class of Qt with Qt's name of the key class; the
    root gives it by its classes."""
    kind = self._items()
    self.assertIs(self.root[int, self.Item], kind)
    self.assertEqual(kind.__name__, 'FakeMap[int, Item]')
    self.assertEqual(kind.__qt_class__, 'QFakeMap<int, Item>')
    self.assertIs(kind.__key_class__, int)
    self.assertIs(kind.__value_class__, self.Item)
    self.assertEqual(kind.__value_crossing__, 'value')
    self.assertEqual(kind.__map_rituals__, _RITUALS)
    self.assertEqual(kind.__delete_ritual__, 'map_drop')
    texts = self.root.createKind(str, self.Item, 'value', **_RITUALS)
    self.assertEqual(texts.__qt_class__, 'QFakeMap<QString, Item>')
    self.assertIs(self.root[str, self.Item], texts)

  def test_a_kind_with_the_name_qt_has_for_it(self) -> None:
    """A kind Qt has a name for is called by it."""
    kind = self.root.createKind(
        str, self.Item, 'value', name='QItemMap', **_RITUALS)
    self.assertEqual(kind.__name__, 'QItemMap')
    self.assertEqual(kind.__qualname__, 'QItemMap')
    self.assertIs(self.root[str, self.Item], kind)

  def test_a_kind_named_before_its_class(self) -> None:
    """A 'WAIT' for the class of the values gives the class of the kind
    by the name alone, the same each time; 'createKind' completes that
    class."""
    named = self.root[int, WAIT['Item']]
    self.assertIs(self.root[int, WAIT['Item']], named)
    self.assertIsNone(named.__value_class__)
    self.assertEqual(named.__value_name__, 'Item')
    self.assertIs(self._items(), named)
    self.assertIs(named.__value_class__, self.Item)
    self.assertIs(self.root[int, self.Item], named)

  def test_what_qt_has_no_map_of(self) -> None:
    """No pair, a key of no kind, a value with no name or of no class,
    a class no kind holds, or one of the same name, are refused; and a
    kind is no root."""
    kind = self._items()

    class Item(CuteMixin, metaclass=MetaCute):
      __qt_class__ = 'Other'

    for asked in (int, (int, self.Item, str), (float, self.Item),
                  (int, 5), (int, len), (int, self.Thing), (int, Item)):
      with self.subTest(asked=asked):
        with self.assertRaises(TypeError) as caught:
          self.root[asked]
        self.assertIn("Qt has no 'FakeMap[", str(caught.exception))
    with self.assertRaises(TypeError) as caught:
      kind[int, self.Item]
    self.assertIn('is the class of one kind of map already',
                  str(caught.exception))

  def test_a_kind_is_completed_by_bringing_in_its_class(self) -> None:
    """A kind named by its class's name alone brings that class in from
    the first part that has it, which completes it."""
    named = self.root[int, WAIT['Later']]
    self.assertIs(named._getMadeKind(), named)
    self.assertEqual(named.__value_class__.__name__, 'Later')
    self.assertIs(named._getMadeKind(), named)

  def test_a_kind_nothing_completes(self) -> None:
    """A kind whose class no part has, or whose class's file completes
    no kind, is refused when it is used."""
    for name in ('Nowhere', 'Hollow'):
      with self.subTest(name=name):
        named = self.root[int, WAIT[name]]
        with self.assertRaises(TypeError) as caught:
          named._getMadeKind()
        self.assertIn("Qt has no 'FakeMap[int, %s]'" % name,
                      str(caught.exception))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  MAPS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_an_empty_map(self) -> None:
    """A map of nothing, its C++ map made at the first use."""
    empty = self._items()()
    self.assertNotIn('map_make', self.seen)
    self.assertEqual(len(empty), 0)
    self.assertEqual(self.seen.count('map_make'), 1)
    self.assertEqual([*empty], [])
    self.assertEqual(str(empty), 'FakeMap[int, Item]({})')
    self.assertEqual(repr(empty), str(empty))
    self.assertEqual(empty.uglySide.getDeleteRitual(), 'map_drop')

  def test_a_map_of_a_dict(self) -> None:
    """A map made of a dict reads as the dict: its length, its keys in
    order, 'in', '[key]', its values and its items."""
    first, other = self._made(self.Item), self._made(self.Item)
    roles = self._items()({1: first, 2: other})
    self.assertEqual(roles.__kept_pairs__, [(1, first), (2, other)])
    self.assertEqual(len(roles), 2)
    self.assertIsNone(roles.__kept_pairs__)
    self.assertEqual([*roles], [1, 2])
    self.assertEqual(roles.keys(), [1, 2])
    self.assertIn(1, roles)
    self.assertNotIn(3, roles)
    at = first.uglySide.getAddress()
    self.assertEqual(roles[1].uglySide.getAddress(), at)
    self.assertIsInstance(roles[1], self.Item)
    self.assertEqual([v.uglySide.getAddress() for v in roles.values()],
                     [at, other.uglySide.getAddress()])
    self.assertEqual([k for k, _ in roles.items()], [1, 2])
    self.assertTrue(str(roles).startswith('FakeMap[int, Item]({1: '))

  def test_putting_a_value_in(self) -> None:
    """'insert' puts a value at a key, in the place of the one there."""
    roles = self._items()()
    first, other = self._made(self.Item), self._made(self.Item)
    roles.insert(1, first)
    roles.insert(1, other)
    self.assertEqual(len(roles), 1)
    self.assertEqual(roles[1].uglySide.getAddress(),
                     other.uglySide.getAddress())

  def test_a_key_the_map_does_not_have(self) -> None:
    """'[key]' raises KeyError; 'value' gives what Qt makes from
    nothing."""
    roles = self._items()()
    with self.assertRaises(KeyError):
      roles[9]
    self.assertEqual(roles.value(9).uglySide.getAddress(), self.blank)

  def test_keys_of_another_class(self) -> None:
    """A key of another class, a 'bool' too, is refused where it is
    handed over, and is in no map."""
    kind = self._items()
    item = self._made(self.Item)
    with self.assertRaises(TypeError) as caught:
      kind({True: item})
    self.assertIn("has 'int' for its keys and nothing else, but was "
                  "handed 'bool'", str(caught.exception))
    roles = kind()
    with self.assertRaises(TypeError):
      roles.insert('one', item)
    self.assertNotIn('one', roles)
    with self.assertRaises(KeyError):
      roles['one']

  def test_values_of_another_class(self) -> None:
    """A value of another class is refused where it is handed over."""
    with self.assertRaises(TypeError) as caught:
      self._items()({1: 'one'})
    self.assertIn("holds 'Item' and nothing else, but was handed 'str'",
                  str(caught.exception))

  def test_values_crossing_by_their_address(self) -> None:
    """A value crossing by its address is handed over by it, Python
    owning it no more, and read back as the object itself."""
    kind = self.root.createKind(int, self.Thing, 'address', **_RITUALS)
    thing = self._made(self.Thing)
    things = kind({1: thing})
    self.assertIs(things[1], thing)

  def test_a_root_makes_no_map(self) -> None:
    """A root is of no kind, so it makes no map."""
    with self.assertRaises(TypeError):
      self.root()

  def test_a_dict_in_the_place_of_a_map(self) -> None:
    """A kind takes a dict whose every key and value fits, and nothing
    else; a root takes nothing."""
    kind = self._items()
    item = self._made(self.Item)
    self.assertIs(self.root.__cast_as__({}), NotImplemented)
    self.assertIs(kind.__cast_as__([1]), NotImplemented)
    self.assertIs(kind.__cast_as__({1: 'one'}), NotImplemented)
    made = kind.__cast_as__({1: item})
    self.assertIsInstance(made, kind)
    self.assertEqual(len(made), 1)

  def test_a_map_a_ritual_made_for_python(self) -> None:
    """A map around a C++ map a ritual made is Python's, and its kind is
    completed first."""
    named = self.root[int, WAIT['Later']]
    address = self._address()
    self.maps[address] = dict()
    owned = named._cuteOwning(address)
    self.assertIsInstance(owned, named)
    self.assertEqual(owned.uglySide.getAddress(), address)
    self.assertEqual(owned.uglySide.getDeleteRitual(), 'map_drop')
    self.assertEqual(len(owned), 0)
