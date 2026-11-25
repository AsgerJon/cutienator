"""
TestOperators tests the operators of Qt on the class files the dev
tooling wrote, against Qt itself: each stands under the name Python has
for it, and behaves as an operator of Python does.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.work_test import BaseTest

from cutienator.QtCore import QDate, QPoint, QPointF, QRect, QSize
from cutienator.QtGui import QMatrix4x4, QVector3D, QVector4D
from cutienator.occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Tuple


class TestOperators(BaseTest):
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

  @staticmethod
  def _xy(point: Any) -> Tuple[Any, Any]:
    """Gives the two numbers of a point."""
    return point.x(), point.y()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  TESTS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_an_operator_gives_a_new_object(self) -> None:
    """'a + b', 'a - b', 'a * 3', 'a / 2' and '-a' give a new point and
    leave both sides as they were."""
    a, b = QPoint(1, 2), QPoint(10, 20)
    self.assertEqual(self._xy(a + b), (11, 22))
    self.assertEqual(self._xy(b - a), (9, 18))
    self.assertEqual(self._xy(a * 3), (3, 6))
    self.assertEqual(self._xy(b / 2), (5, 10))
    self.assertEqual(self._xy(-a), (-1, -2))
    self.assertEqual(self._xy(a), (1, 2))
    self.assertEqual(self._xy(b), (10, 20))
    self.assertIsInstance(a + b, QPoint)
    self.assertEqual(self._xy(QPointF(1, 2) + QPointF(.5, .5)), (1.5, 2.5))

  def test_the_object_on_the_right(self) -> None:
    """'3 * a' asks the number first, which cannot, and then the point."""
    self.assertEqual(self._xy(3 * QPoint(1, 2)), (3, 6))
    doubled = 2 * QVector3D(1, 2, 3)
    self.assertEqual((doubled.x(), doubled.y(), doubled.z()), (2, 4, 6))

  def test_an_operator_that_changes_the_object(self) -> None:
    """'a += b' changes 'a' and leaves it the same object."""
    a = kept = QPoint(1, 2)
    a += QPoint(10, 20)
    self.assertIs(a, kept)
    self.assertEqual(self._xy(a), (11, 22))
    a *= 2
    self.assertIs(a, kept)
    self.assertEqual(self._xy(a), (22, 44))

  def test_comparing(self) -> None:
    """'==' and '!=' go by what Qt says, and the orderings sort."""
    self.assertTrue(QPoint(1, 2) == QPoint(1, 2))
    self.assertFalse(QPoint(1, 2) == QPoint(2, 1))
    self.assertTrue(QPoint(1, 2) != QPoint(2, 1))
    self.assertTrue(QSize(1, 2) == QSize(1, 2))
    self.assertIn(QPoint(1, 2), [QPoint(0, 0), QPoint(1, 2)])
    self.assertTrue(QDate(2024, 1, 1) < QDate(2024, 1, 2))
    self.assertFalse(QDate(2024, 1, 1) >= QDate(2024, 1, 2))
    dates = [QDate(2024, 1, 3), QDate(2024, 1, 1), QDate(2024, 1, 2)]
    self.assertEqual([date.day() for date in sorted(dates)], [1, 2, 3])

  def test_what_no_function_takes(self) -> None:
    """Python is told 'NotImplemented', and does what it does for any
    class: '==' is False, an operator raises 'TypeError'."""
    a = QPoint(1, 2)
    self.assertFalse(a == 5)
    self.assertTrue(a != 5)
    self.assertFalse(a == QSize(1, 2))
    wrongCalls = (
        lambda: a + 'text',
        lambda: 'text' + a,
        lambda: a + QSize(1, 1),
        lambda: a * QPoint(1, 1),
        lambda: QDate(2024, 1, 1) < 5,
    )
    for index, call in enumerate(wrongCalls):
      with self.subTest(call=index):
        with self.assertRaises(TypeError):
          call()

  def test_a_class_with_equality_is_not_hashable(self) -> None:
    """Python takes '__hash__' away from a class that defines '==', and
    the cute class writes none: a QPoint can be changed."""
    with self.assertRaises(TypeError):
      hash(QPoint(1, 2))

  def test_operators_of_other_shapes(self) -> None:
    """'&' and '|' of rectangles, and the one operator two classes each
    declare, which has one ritual."""
    both = QRect(0, 0, 10, 10) & QRect(5, 5, 10, 10)
    self.assertEqual((both.x(), both.y(), both.width()), (5, 5, 5))
    either = QRect(0, 0, 10, 10) | QRect(5, 5, 10, 10)
    self.assertEqual((either.x(), either.width()), (0, 15))
    vector = QVector4D(1, 2, 3, 1) * QMatrix4x4()
    self.assertEqual((vector.x(), vector.y(), vector.z()), (1, 2, 3))
    vector = QMatrix4x4() * QVector4D(1, 2, 3, 1)
    self.assertEqual((vector.x(), vector.y(), vector.z()), (1, 2, 3))
