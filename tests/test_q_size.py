"""
TestQSize tests the cute 'QSize' against Qt itself, through the rituals.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import gc
from typing import TYPE_CHECKING
from unittest import mock

from worktoy.waitaminute.dispatch import DispatchException
from worktoy.work_test import BaseTest

from cutienator.QtCore import QSize, QObject
from cutienator.occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Callable, List


class TestQSize(BaseTest):
  """
  Tests the cute 'QSize', the first value class: every function of it,
  and that Python owns the C++ QSize behind each cute one. Nothing is
  faked. Each test makes real C++ objects and calls real Qt functions.

  What to know before adding a test
  ---------------------------------

  - The rituals are called for real; 'setUpClass' builds the shared
    object of rituals when a ritual file is newer than it.
  - Whether a C++ QSize was removed is seen by watching 'Rituals.call'
    for the delete ritual. The watching has to start before the cute
    QSize is used, since an Ugly keeps the 'Rituals.call' it met.
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

  def _raisedBy(self, make: Callable) -> BaseException:
    """Calls 'make', which is expected to raise, and gives what it
    raised."""
    try:
      make()
    except Exception as exception:
      return exception
    self.fail('Nothing was raised.')

  @staticmethod
  def _watchCalls(called: List[Any]) -> Any:
    """Gives a stand-in for 'Rituals.call' that notes each call in
    'called', as the name and what was passed, and then makes it."""
    realCall = Rituals.call

    def watching(name: str, *args: Any) -> Any:
      called.append((name, *args))
      return realCall(name, *args)

    return mock.patch.object(Rituals, 'call', watching)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  TESTS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_made_with_a_width_and_a_height(self) -> None:
    """'QSize(3, 4)' is three wide and four high."""
    size = QSize(3, 4)
    self.assertEqual((size.width(), size.height()), (3, 4))
    self.assertIs(size.isValid(), True)
    self.assertIs(size.isNull(), False)
    self.assertIs(size.isEmpty(), False)

  def test_made_with_nothing_is_not_valid(self) -> None:
    """Qt makes 'QSize()' with -1 for both, which is not valid."""
    size = QSize()
    self.assertEqual((size.width(), size.height()), (-1, -1))
    self.assertIs(size.isValid(), False)
    self.assertIs(size.isEmpty(), True)
    self.assertIs(QSize(0, 0).isNull(), True)

  def test_creation_refuses_what_is_no_size(self) -> None:
    """One number, text or three numbers make no QSize."""
    for wrong in ((3,), ('3', '4'), (1, 2, 3), (None, None)):
      with self.subTest(wrong=wrong):
        raised = self._raisedBy(lambda: QSize(*wrong))
        self.assertIsInstance(raised, DispatchException)

  def test_setters_change_the_cpp_object(self) -> None:
    """'setWidth' and 'setHeight' are read back by the getters."""
    size = QSize(3, 4)
    self.assertIsNone(size.setWidth(30))
    self.assertIsNone(size.setHeight(40))
    self.assertEqual((size.width(), size.height()), (30, 40))

  def test_transpose_swaps_in_place(self) -> None:
    """'transpose' swaps width and height of the object itself."""
    size = QSize(3, 4)
    self.assertIsNone(size.transpose())
    self.assertEqual((size.width(), size.height()), (4, 3))

  def test_transposed_gives_a_new_size(self) -> None:
    """'transposed' leaves the object alone and gives another one."""
    size = QSize(3, 4)
    other = size.transposed()
    self.assertIsNot(other, size)
    self.assertIsInstance(other, QSize)
    self.assertEqual((other.width(), other.height()), (4, 3))
    self.assertEqual((size.width(), size.height()), (3, 4))

  def test_expanded_and_bounded_take_a_size(self) -> None:
    """The larger, and the smaller, of two sizes in each direction."""
    size, other = QSize(3, 4), QSize(5, 1)
    wide = size.expandedTo(other)
    small = size.boundedTo(other)
    self.assertEqual((wide.width(), wide.height()), (5, 4))
    self.assertEqual((small.width(), small.height()), (3, 1))
    self.assertEqual((other.width(), other.height()), (5, 1))

  def test_scaled_both_ways(self) -> None:
    """'scaled' takes two numbers or a size, and the number of a
    'Qt::AspectRatioMode': 0 ignores the shape, 1 keeps it."""
    size = QSize(3, 4)
    free = size.scaled(10, 10, 0)
    kept = size.scaled(QSize(30, 30), 1)
    self.assertEqual((free.width(), free.height()), (10, 10))
    self.assertEqual((kept.width(), kept.height()), (22, 30))
    self.assertEqual((size.width(), size.height()), (3, 4))

  def test_scale_changes_in_place(self) -> None:
    """'scale' does to the object itself what 'scaled' gives back."""
    size = QSize(3, 4)
    self.assertIsNone(size.scale(10, 10, 0))
    self.assertEqual((size.width(), size.height()), (10, 10))
    self.assertIsNone(size.scale(QSize(30, 60), 1))
    self.assertEqual((size.width(), size.height()), (30, 30))

  def test_a_size_is_taken_where_a_size_is_declared_only(self) -> None:
    """A QObject, a number and None are refused where a QSize goes."""
    size = QSize(3, 4)
    for wrong in (QObject(), 5, None, (5, 1)):
      with self.subTest(wrong=wrong):
        raised = self._raisedBy(lambda: size.expandedTo(wrong))
        self.assertIsInstance(raised, DispatchException)

  def test_python_owns_what_it_makes(self) -> None:
    """The C++ QSize behind 'QSize(3, 4)' is removed with it, once."""
    called = []  # type: List[Any]
    with self._watchCalls(called):
      size = QSize(3, 4)
      address = size.uglySide.getAddress()
      self.assertIs(size.uglySide.isOwned(), True)
      del size
      gc.collect()
    removed = [c for c in called if c[0] == 'ritual_ZN5QSizeD1Ev']
    self.assertEqual(removed, [('ritual_ZN5QSizeD1Ev', address)])

  def test_python_owns_what_qt_gives_back(self) -> None:
    """A QSize a function gave back is a copy of Python's own."""
    called = []  # type: List[Any]
    with self._watchCalls(called):
      size = QSize(3, 4)
      other = size.transposed()
      self.assertIs(other.uglySide.isOwned(), True)
      address = other.uglySide.getAddress()
      self.assertNotEqual(address, size.uglySide.getAddress())
      del other
      gc.collect()
      removed = [c for c in called if c[0] == 'ritual_ZN5QSizeD1Ev']
      self.assertEqual(removed, [('ritual_ZN5QSizeD1Ev', address)])
      self.assertEqual(size.width(), 3)

  def test_a_size_never_used_makes_no_cpp_object(self) -> None:
    """The C++ QSize is made at the first use, so none is removed for a
    cute QSize that was never used."""
    called = []  # type: List[Any]
    with self._watchCalls(called):
      size = QSize(3, 4)
      del size
      gc.collect()
    self.assertEqual(called, [])

  def test_passing_a_size_keeps_it_python_s_own(self) -> None:
    """Qt reads a QSize it is handed as a value; Python still owns it."""
    size, other = QSize(3, 4), QSize(5, 1)
    size.expandedTo(other)
    self.assertIs(other.uglySide.isOwned(), True)
    self.assertIs(size.uglySide.isOwned(), True)

  def test_nothing_is_removed_as_the_program_ends(self) -> None:
    """The watch removing the C++ QSize does not run at exit."""
    size = QSize(3, 4)
    self.assertIs(size.uglySide.__delete_watch__.atexit, False)
