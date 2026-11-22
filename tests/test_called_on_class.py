"""
TestCalledOnClass tests the names at which Qt has a function called on
the class beside the functions called on an object, as 'QFile.exists'.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import tempfile
from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.waitaminute.dispatch import DispatchException
from worktoy.work_test import BaseTest

from cutienator.cute import CuteMixin, MetaCute
from cutienator.QtCore import QDate, QFile, QFileInfo, QObject, QTime
from cutienator.QtCore import QMetaObject, QMetaType, QTimer, Qt
from cutienator.occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Optional


class Both(CuteMixin, metaclass=MetaCute):
  """Stands in for a class of Qt with a name that is called both on an
  object and on the class, written as the dev tooling writes one."""

  __qt_class__ = 'Both'

  @overload()
  def tell(self) -> str:
    return 'of the object'

  @overload(int)
  @overload()
  def count(self, step: int = 1) -> Any:
    return 'counted by %d' % step

  @staticmethod
  @overload(str)
  def tell(name: str) -> str:
    return 'of the class: %s' % name

  @staticmethod
  @overload(int, int)
  def tell(first: int, second: int) -> str:
    return 'of the class: %d' % (first + second)

  @staticmethod
  @overload(str)
  def count(name: str) -> str:
    return 'counted for %s' % name


class Heir(Both):
  """Built on the class that has the name."""


class TestCalledOnClass(BaseTest):
  """
  Tests that such a name holds both functions, each written as Qt
  declares it: worktoy reaches the function of an object through an
  object, and the function of the class through the class.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def setUpClass(cls) -> None:
    """Builds the shared object of rituals when a ritual file is newer."""
    super().setUpClass()
    if Rituals.isStale():
      Rituals.build()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  TESTS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_called_on_an_object(self) -> None:
    """Called on an object, the function of the object runs."""
    for cuteClass in (Both, Heir):
      held = cuteClass()
      with self.subTest(cuteClass=cuteClass.__name__):
        self.assertEqual(held.tell(), 'of the object')
        self.assertEqual(held.count(), 'counted by 1')
        self.assertEqual(held.count(4), 'counted by 4')

  def test_called_on_the_class(self) -> None:
    """Called on the class, the function of the class runs."""
    for cuteClass in (Both, Heir):
      with self.subTest(cuteClass=cuteClass.__name__):
        self.assertEqual(cuteClass.tell('name'), 'of the class: name')
        self.assertEqual(cuteClass.tell(2, 3), 'of the class: 5')
        self.assertEqual(cuteClass.count('name'), 'counted for name')

  def test_each_is_reached_its_own_way(self) -> None:
    """worktoy does not consider the function of an object through the
    class, nor the function of the class through an object."""
    held = Heir()
    crossedCalls = (
        lambda: Both.tell(held),
        lambda: Heir.tell(held),
        lambda: held.tell('name'),
        lambda: held.tell(2, 3),
        lambda: held.count('name'),
        lambda: Both.count(4),
    )
    for index, call in enumerate(crossedCalls):
      with self.subTest(call=index):
        with self.assertRaises(DispatchException):
          call()

  def test_what_no_function_takes_is_refused(self) -> None:
    """Neither function takes it, so the call is refused."""
    wrongCalls = (
        lambda: Both.tell(1.5),
        lambda: Both.tell('one', 'two'),
        lambda: Both.tell(1, 2, 3),
        lambda: Both().tell(1.5),
        lambda: Both.count(1.5),
        lambda: Both.count('one', 'two'),
        lambda: Heir.tell(None),
        lambda: QFile.exists('one', 'two'),
        lambda: QDate.isValid(2024, 2),
    )
    for index, call in enumerate(wrongCalls):
      with self.subTest(call=index):
        with self.assertRaises(DispatchException):
          call()

  def test_the_names_of_qt(self) -> None:
    """'QFile.exists', 'QDate.isValid' and the like, each its own way."""
    with tempfile.TemporaryDirectory() as folder:
      there = os.path.join(folder, 'there.txt')
      moved = os.path.join(folder, 'moved.txt')
      with open(there, 'w') as file:
        file.write('text')
      held = QFile(there)
      self.assertTrue(held.exists())
      self.assertTrue(QFile.exists(there))
      self.assertFalse(QFile.exists(moved))
      with self.assertRaises(DispatchException):
        QFile.exists(held)
      with self.assertRaises(DispatchException):
        held.exists(moved)
      self.assertTrue(QFileInfo.exists(there))
      self.assertTrue(QFile.rename(there, moved))
      self.assertTrue(QFile(moved).rename(there))
      self.assertTrue(QFile.remove(there))
      self.assertFalse(os.path.exists(there))
    self.assertTrue(QDate.isValid(2024, 2, 29))
    self.assertFalse(QDate.isValid(2024, 2, 30))
    self.assertFalse(QDate().isValid())
    self.assertTrue(QTime.isValid(1, 2, 3))
    self.assertTrue(QTime(1, 2, 3).isValid())
    with self.assertRaises(DispatchException):
      QFile.exists(7)

  def test_a_member_where_the_class_takes_a_number(self) -> None:
    """The function of the class takes a member of an enum where Qt
    takes its number: 'QMetaType.sizeOf' takes the id of a type."""
    self.assertEqual(QMetaType.sizeOf(QMetaType.Type.Int), 4)
    self.assertEqual(QMetaType.sizeOf(2), 4)

  def test_a_member_for_its_number_both_ways(self) -> None:
    """Such a name has a door for calls on an object and one for calls
    on the class: either way a member of an enum is taken where the
    function takes a number. 'Qt.ItemDataRole.EditRole' has the number
    2."""
    member = Qt.ItemDataRole.EditRole
    for cuteClass in (Both, Heir):
      with self.subTest(cuteClass=cuteClass.__name__):
        self.assertEqual(cuteClass().count(member), 'counted by 2')
        self.assertEqual(cuteClass.tell(member, 1), 'of the class: 3')
        self.assertEqual(cuteClass.tell(1, member), 'of the class: 3')

  def test_a_member_does_not_cross_over(self) -> None:
    """A door tries the call again its own way only: a member does not
    make the function of the class take a call on an object."""
    with self.assertRaises(DispatchException):
      Heir().tell(Qt.ItemDataRole.EditRole, 1)
    with self.assertRaises(DispatchException):
      Both.count(Qt.ItemDataRole.EditRole)

  def test_connecting_both_ways(self) -> None:
    """'QObject.connect' called on the class takes the sender first,
    and called on the receiver it does not take the receiver."""
    sender, receiver = QTimer(), QObject()
    made = QObject.connect(sender, '2timeout()', receiver, '1deleteLater()')
    self.assertIsInstance(made, QMetaObject.Connection)
    self.assertTrue(QObject.disconnect(made))
    made = receiver.connect(sender, '2timeout()', '1deleteLater()')
    self.assertIsInstance(made, QMetaObject.Connection)
    self.assertTrue(QObject.disconnect(
        sender, '2timeout()', receiver, '1deleteLater()'))
    self.assertIsInstance(sender.disconnect(None, None), bool)
