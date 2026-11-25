"""
TestCuteMixin tests how a cute object hands its C++ object to a ritual,
and how one is made around what a ritual gave back.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from cutienator.cute import CuteMixin
from cutienator.QtCore import QObject, QSize
from cutienator.occult import Rituals


class TestCuteMixin(BaseTest):
  """
  Tests the helpers of 'CuteMixin' that say who owns a C++ object:
  '_addressOf', '_valueOf', '_cuteAt' and '_cuteOwning'. The rituals
  are called for real; 'setUpClass' builds the shared object of rituals
  when a ritual file is newer than it.
  """

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

  def test_the_part_of_a_cute_class(self) -> None:
    """A cute class is of the part of Qt whose package holds it, and so
    is a class of a program built on it, and the Ugly of an object of
    it runs rituals as that part sees them. A class on 'CuteMixin'
    alone is of no part."""

    class Program(QObject):
      """A class of a program, written on a cute class."""

    self.assertEqual(QObject._getPartName(), 'QtCore')
    self.assertEqual(QSize._getPartName(), 'QtCore')
    self.assertEqual(Program._getPartName(), 'QtCore')
    self.assertIsNone(CuteMixin._getPartName())
    self.assertEqual(QSize(1, 2).uglySide.getPartName(), 'QtCore')
    self.assertEqual(QObject().uglySide.getPartName(), 'QtCore')

  def test_value_of_keeps_the_object_python_s_own(self) -> None:
    """'_valueOf' gives the address and changes nothing."""
    size = QSize(3, 4)
    address = CuteMixin._valueOf(size)
    self.assertEqual(address, size.uglySide.getAddress())
    self.assertIs(size.uglySide.isOwned(), True)

  def test_address_of_gives_the_object_up(self) -> None:
    """Handed to Qt by its address, a C++ object is Python's no more."""
    size = QSize(3, 4)
    address = CuteMixin._addressOf(size)
    self.assertEqual(address, size.uglySide.getAddress())
    self.assertIs(size.uglySide.isOwned(), False)
    self.assertEqual(size.width(), 3)

  def test_address_of_none_is_none(self) -> None:
    """None stands for no object, and stays None."""
    self.assertIsNone(CuteMixin._addressOf(None))

  def test_address_of_an_object_python_never_owned(self) -> None:
    """A QObject is handed over by its address as before."""
    cuteObject = QObject()
    address = CuteMixin._addressOf(cuteObject)
    self.assertEqual(address, cuteObject.uglySide.getAddress())
    self.assertIs(cuteObject.uglySide.isOwned(), False)

  def test_cute_owning_makes_an_owning_cute_object(self) -> None:
    """Around a copy a ritual made, '_cuteOwning' gives a cute object
    that owns it."""
    address = Rituals.call('ritual_ZN5QSizeC1Eii', 7, 8)
    size = QSize._cuteOwning(address)
    self.assertIsInstance(size, QSize)
    self.assertEqual((size.width(), size.height()), (7, 8))
    self.assertIs(size.uglySide.isOwned(), True)
    self.assertEqual(size.uglySide.getAddress(), address)

  def test_cute_owning_is_for_value_classes_alone(self) -> None:
    """A class naming no delete ritual owns no C++ object."""
    address = QObject().uglySide.getAddress()
    with self.assertRaises(TypeError):
      QObject._cuteOwning(address)

  def test_cute_at_owns_nothing(self) -> None:
    """What Qt hands out by its address is never Python's own."""
    address = Rituals.call('ritual_ZN5QSizeC1Eii', 1, 2)
    size = QSize._cuteAt(address)
    self.assertIs(size.uglySide.isOwned(), False)
    self.assertEqual(size.width(), 1)
    Rituals.call('ritual_ZN5QSizeD1Ev', address)
