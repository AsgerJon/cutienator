"""
TestQMap tests the maps of Qt: 'QMap[int, QVariant]', 'QHash[int,
QByteArray]' and their like, each a cute class of its own, and the
functions of Qt that take or give one.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import subprocess
import sys

from worktoy.waitaminute.dispatch import DispatchException
from worktoy.work_test import BaseTest

import cutienator
from cutienator.QtCore import QByteArray, QHash, QMap, QVariant
from cutienator.QtCore import QVariantHash, QVariantMap
from cutienator.QtGui import QStandardItemModel
from cutienator.cute import CuteMap
from cutienator.occult import Rituals

#  A function taking a map to QVariant, called with an empty dict
#  before QVariant is brought in. It runs in a Python of its own, since
#  this file brings QVariant in at its top.
EMPTY_BEFORE = """
import sys

from cutienator.QtGui import QStandardItemModel

model = QStandardItemModel(1, 1)
file = 'cutienator.QtCore._q_variant'
print('QVariant brought in:', file in sys.modules)
taken = model.setItemData(model.index(0, 0), {})
print('the empty dict went through:', taken)
print('QVariant brought in:', file in sys.modules)
"""


class TestQMap(BaseTest):
  """None of these needs an application."""

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def setUpClass(cls) -> None:
    """Builds the shared object of rituals when a ritual file is newer."""
    super().setUpClass()
    if Rituals.isStale():
      Rituals.summon()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  TESTS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_each_kind_is_a_class(self) -> None:
    """'QMap[int, QVariant]' is a class built on QMap, one class each
    time it is asked for, and no QHash."""
    kind = QMap[int, QVariant]
    self.assertTrue(issubclass(kind, QMap))
    self.assertTrue(issubclass(kind, CuteMap))
    self.assertFalse(issubclass(kind, QHash))
    self.assertIs(kind, QMap[int, QVariant])
    self.assertEqual(kind.__name__, 'QMap[int, QVariant]')
    self.assertIsNot(kind, QMap[str, QVariant])

  def test_the_names_qt_has_for_a_kind(self) -> None:
    """The kinds Qt named go by that name."""
    self.assertIs(QMap[str, QVariant], QVariantMap)
    self.assertIs(QHash[str, QVariant], QVariantHash)
    self.assertEqual(QVariantMap.__name__, 'QVariantMap')

  def test_what_qt_has_no_map_of(self) -> None:
    """A kind Qt has no code for is refused where it is asked for."""
    wrong = (
        (float, QVariant), (int, dict), (int, int), (QVariant, QVariant),
        (int,), int, (int, QVariant, QVariant),
    )
    for pair in wrong:
      with self.subTest(pair=pair):
        with self.assertRaises(TypeError):
          QMap[pair]
    with self.assertRaises(TypeError):
      QHash[int, QVariant]
    with self.assertRaises(TypeError):
      QVariantMap[str, QVariant]
    with self.assertRaises(TypeError):
      QMap()
    with self.assertRaises(TypeError):
      CuteMap[int, QVariant]

  def test_a_map_reads_as_a_dict(self) -> None:
    """'len', 'in', a key, 'for' and the keys, values and items, and
    'insert' puts a value into the C++ map."""
    found = QVariantMap({'b': QVariant('second'), 'a': QVariant('first')})
    found.insert('c', QVariant('third'))
    self.assertEqual(len(found), 3)
    self.assertIn('a', found)
    self.assertNotIn('z', found)
    self.assertNotIn(1, found)
    self.assertEqual(found['b'].toString(), 'second')
    self.assertEqual([*found], ['a', 'b', 'c'])
    self.assertEqual(found.keys(), ['a', 'b', 'c'])
    texts = [value.toString() for value in found.values()]
    self.assertEqual(texts, ['first', 'second', 'third'])
    self.assertEqual([key for key, _ in found.items()], ['a', 'b', 'c'])
    self.assertEqual(len(QVariantMap()), 0)

  def test_a_key_the_map_does_not_have(self) -> None:
    """'[key]' raises, and Qt's own 'value' gives a value made from
    nothing."""
    found = QVariantMap({'a': QVariant('first')})
    with self.assertRaises(KeyError):
      found['z']
    self.assertFalse(found.value('z').isValid())
    self.assertTrue(found.value('a').isValid())

  def test_a_map_holds_its_own_kind(self) -> None:
    """A key or a value of another class is refused on the line that
    hands it over."""
    with self.assertRaises(TypeError) as context:
      QVariantMap({1: QVariant('a')})
    self.assertIn("has 'str' for its keys", str(context.exception))
    with self.assertRaises(TypeError) as context:
      QVariantMap({'a': 'text'})
    self.assertIn("holds 'QVariant'", str(context.exception))
    with self.assertRaises(TypeError):
      QMap[int, QVariant]({True: QVariant('a')})
    with self.assertRaises(TypeError):
      QVariantMap().insert('a', 1)
    with self.assertRaises(TypeError):
      QVariantMap().contains(1)

  def test_a_function_takes_a_map_and_gives_one(self) -> None:
    """'setItemData' takes a 'QMap[int, QVariant]', and 'itemData'
    gives a new one that Python owns."""
    model = QStandardItemModel(1, 1)
    index = model.index(0, 0)
    roles = QMap[int, QVariant]({0: QVariant('shown')})
    self.assertTrue(model.setItemData(index, roles))
    found = model.itemData(index)
    self.assertIsInstance(found, QMap[int, QVariant])
    self.assertTrue(found.uglySide.isOwned())
    self.assertIn(0, found)
    self.assertEqual(found[0].toString(), 'shown')

  def test_a_dict_of_python_is_made_into_one(self) -> None:
    """A function taking a map of Qt takes a dict of Python whose
    every key and value fits, and no other."""
    model = QStandardItemModel(1, 1)
    index = model.index(0, 0)
    self.assertTrue(model.setItemData(index, {0: QVariant('by dict')}))
    self.assertEqual(model.itemData(index)[0].toString(), 'by dict')
    self.assertTrue(model.setItemData(index, {}))
    with self.assertRaises(DispatchException):
      model.setItemData(index, {'zero': QVariant('wrong key')})
    with self.assertRaises(DispatchException):
      model.setItemData(index, {0: 'wrong value'})

  def test_a_function_gives_a_hash(self) -> None:
    """'roleNames' gives a 'QHash[int, QByteArray]': the names Qt has
    for the roles of a model."""
    names = QStandardItemModel().roleNames()
    self.assertIsInstance(names, QHash[int, QByteArray])
    self.assertIn(0, names)
    self.assertIsInstance(names[0], QByteArray)
    self.assertEqual(names[0].size(), len('display'))
    self.assertEqual(sorted(names.keys()), sorted(names))

  def test_an_empty_dict_before_what_it_holds(self) -> None:
    """A function taking a map to QVariant takes an empty dict before
    a QVariant was ever made: the map brings its file in itself."""
    packageFolder = os.path.dirname(os.path.abspath(cutienator.__file__))
    environment = dict(os.environ)
    known = environment.get('PYTHONPATH', '')
    folders = [os.path.dirname(packageFolder), *known.split(os.pathsep)]
    environment['PYTHONPATH'] = os.pathsep.join(f for f in folders if f)
    done = subprocess.run(
        (sys.executable, '-B', '-c', EMPTY_BEFORE),
        capture_output=True, text=True, env=environment, timeout=120,
    )
    self.assertEqual(done.returncode, 0, done.stderr)
    expected = [
        'QVariant brought in: False',
        'the empty dict went through: True',
        'QVariant brought in: True',
    ]
    self.assertEqual(done.stdout.strip().split('\n'), expected)
