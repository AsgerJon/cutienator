"""
TestUgly tests what 'Ugly' does about owning a C++ object, and about
having Qt watch one.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import gc
from typing import TYPE_CHECKING
from unittest import mock

from worktoy.waitaminute import MissingVariable, TypeException
from worktoy.work_test import BaseTest

from cutienator.occult import Rituals, Ugly

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List


class TestUgly(BaseTest):
  """
  Tests the owning side of 'Ugly': which C++ object is removed when its
  Ugly goes, and which is left as it is. And the watching side: what
  an Ugly does once Qt says its C++ object is gone.

  No C++ runs here. 'Rituals.call' is replaced by a stand-in that notes
  what it was called with, and the addresses are made-up numbers. The
  stand-in gives 0x9000 as the address of every watcher made, and
  answers 'self.gone' when a watcher is asked whether its object is
  gone.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setUp(self) -> None:
    """Replaces 'Rituals.call' by a stand-in for the time of a test."""
    super().setUp()
    self.called = []  # type: List[Any]
    self.gone = False

    def noting(name: str, *args: Any) -> Any:
      self.called.append((name, *args))
      if name == Ugly.__watch_make_ritual__:
        return 0x9000
      if name == Ugly.__watch_ask_ritual__:
        return self.gone
      return None

    def notingFrom(partName: str, name: str, *args: Any) -> Any:
      self.called.append(('seen from %s' % partName, name, *args))
      return None

    patcher = mock.patch.object(Rituals, 'call', noting)
    patcher.start()
    self.addCleanup(patcher.stop)
    patcher = mock.patch.object(Rituals, 'callFrom', notingFrom)
    patcher.start()
    self.addCleanup(patcher.stop)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  TESTS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_an_ugly_owns_nothing_until_told(self) -> None:
    """A C++ object is left as it is when its Ugly goes."""
    ugly = Ugly()
    ugly.setAddress(0x1000)
    self.assertIs(ugly.isOwned(), False)
    self.assertIsNone(ugly.getDeleteRitual())
    del ugly
    gc.collect()
    self.assertEqual(self.called, [])

  def test_an_owned_object_is_removed_with_its_ugly(self) -> None:
    """The delete ritual runs once, with the address, as the Ugly goes."""
    ugly = Ugly()
    ugly.setAddress(0x2000)
    ugly.setDeleteRitual('ritual_ZN5QSizeD1Ev')
    self.assertIs(ugly.isOwned(), True)
    self.assertEqual(ugly.getDeleteRitual(), 'ritual_ZN5QSizeD1Ev')
    self.assertEqual(self.called, [])
    del ugly
    gc.collect()
    self.assertEqual(self.called, [('ritual_ZN5QSizeD1Ev', 0x2000)])

  def test_a_disowned_object_is_left_as_it_is(self) -> None:
    """After 'disown' the Ugly goes without removing anything."""
    ugly = Ugly()
    ugly.setAddress(0x3000)
    ugly.setDeleteRitual('ritual_ZN5QSizeD1Ev')
    ugly.disown()
    self.assertIs(ugly.isOwned(), False)
    self.assertIsNone(ugly.getDeleteRitual())
    del ugly
    gc.collect()
    self.assertEqual(self.called, [])

  def test_disown_does_nothing_where_nothing_is_owned(self) -> None:
    """'disown' on an Ugly that owns nothing changes nothing."""
    ugly = Ugly()
    ugly.setAddress(0x4000)
    self.assertIsNone(ugly.disown())
    self.assertIs(ugly.isOwned(), False)

  def test_owning_is_not_taken_back(self) -> None:
    """A delete ritual is set once, also after 'disown'."""
    ugly = Ugly()
    ugly.setAddress(0x5000)
    ugly.setDeleteRitual('ritual_ZN5QSizeD1Ev')
    with self.assertRaises(RuntimeError):
      ugly.setDeleteRitual('ritual_ZN5QSizeD1Ev')
    ugly.disown()
    with self.assertRaises(RuntimeError):
      ugly.setDeleteRitual('ritual_ZN5QSizeD1Ev')
    self.assertIs(ugly.isOwned(), False)

  def test_owning_needs_the_address_first(self) -> None:
    """Without an address there is nothing to remove."""
    with self.assertRaises(MissingVariable):
      Ugly().setDeleteRitual('ritual_ZN5QSizeD1Ev')

  def test_the_delete_ritual_is_named_in_text(self) -> None:
    """Anything but text for the name of the ritual is refused."""
    ugly = Ugly()
    ugly.setAddress(0x6000)
    with self.assertRaises(TypeException):
      ugly.setDeleteRitual(None)
    self.assertIs(ugly.isOwned(), False)

  def test_nothing_is_removed_as_the_program_ends(self) -> None:
    """The watch on an owned object does not run at exit."""
    ugly = Ugly()
    ugly.setAddress(0x7000)
    ugly.setDeleteRitual('ritual_ZN5QSizeD1Ev')
    self.assertIs(ugly.__delete_watch__.atexit, False)
    ugly.disown()

  def test_nothing_is_watched_until_told(self) -> None:
    """Without 'watch' no ritual is asked, and nothing is ever gone."""
    ugly = Ugly()
    ugly.setAddress(0x1100)
    self.assertIs(ugly.isWatched(), False)
    self.assertIs(ugly.isGone(), False)
    self.assertEqual(ugly.getAddress(), 0x1100)
    self.assertEqual(self.called, [])

  def test_watch_makes_a_watcher_of_the_object(self) -> None:
    """'watch' has the make ritual run on the address, once."""
    ugly = Ugly()
    ugly.setAddress(0x1200)
    self.assertIsNone(ugly.watch())
    self.assertIs(ugly.isWatched(), True)
    self.assertEqual(self.called, [(Ugly.__watch_make_ritual__, 0x1200)])
    with self.assertRaises(RuntimeError):
      ugly.watch()
    made = [c for c in self.called if c[0] == Ugly.__watch_make_ritual__]
    self.assertEqual(len(made), 1)

  def test_watch_needs_the_address_first(self) -> None:
    """Without an address there is nothing to watch."""
    with self.assertRaises(MissingVariable):
      Ugly().watch()
    self.assertEqual(self.called, [])

  def test_a_watched_object_is_asked_about(self) -> None:
    """'isGone' gives what the watcher answers."""
    ugly = Ugly()
    ugly.setAddress(0x1300)
    ugly.watch()
    self.assertIs(ugly.isGone(), False)
    self.gone = True
    self.assertIs(ugly.isGone(), True)
    asked = (Ugly.__watch_ask_ritual__, 0x9000)
    self.assertEqual(self.called[1:], [asked, asked])

  def test_no_address_is_given_of_what_is_gone(self) -> None:
    """Once Qt has removed the object, 'getAddress' and 'call' raise,
    and the ritual asked for does not run."""
    ugly = Ugly()
    ugly.setAddress(0x1400)
    ugly.watch()
    self.assertEqual(ugly.getAddress(), 0x1400)
    ugly.call('ritual_of_a_test', 5)
    self.assertIn(('ritual_of_a_test', 0x1400, 5), self.called)
    self.gone = True
    del self.called[:]
    with self.assertRaises(RuntimeError):
      ugly.getAddress()
    with self.assertRaises(RuntimeError):
      ugly.call('ritual_of_a_test', 5)
    names = {name for name, *_ in self.called}
    self.assertEqual(names, {Ugly.__watch_ask_ritual__})

  def test_at_finds_no_ugly_of_what_is_gone(self) -> None:
    """'Ugly.at' gives the Ugly of a living object, and none of one
    that Qt has removed: what is at the address then is another."""
    ugly = Ugly()
    ugly.setAddress(0x1500)
    ugly.watch()
    self.assertIs(Ugly.at(0x1500), ugly)
    self.gone = True
    with self.assertRaises(LookupError):
      Ugly.at(0x1500)

  def test_the_watcher_is_removed_with_its_ugly(self) -> None:
    """The drop ritual runs once, on the watcher, as the Ugly goes, and
    not as the program ends."""
    ugly = Ugly()
    ugly.setAddress(0x1600)
    ugly.watch()
    del self.called[:]
    del ugly
    gc.collect()
    self.assertEqual(self.called, [(Ugly.__watch_drop_ritual__, 0x9000)])

  def test_an_ugly_of_a_part_runs_rituals_as_it_sees_them(self) -> None:
    """Told its part, an Ugly runs each ritual through 'callFrom', and
    so removes its C++ object, as that part sees the rituals."""
    ugly = Ugly()
    ugly.setPartName('QtGraphs')
    self.assertEqual(ugly.getPartName(), 'QtGraphs')
    ugly.setAddress(0x1700)
    ugly.call('ritual_ZNK10QBarSeries5countEv', 3)
    ugly.setDeleteRitual('ritual_ZN10QBarSeriesD1Ev')
    del ugly
    gc.collect()
    self.assertEqual(self.called, [
        ('seen from QtGraphs', 'ritual_ZNK10QBarSeries5countEv', 0x1700, 3),
        ('seen from QtGraphs', 'ritual_ZN10QBarSeriesD1Ev', 0x1700),
    ])

  def test_an_ugly_of_no_part_runs_rituals_through_call(self) -> None:
    """Without a part, an Ugly runs a ritual with 'call', which finds
    only a ritual one part has."""
    ugly = Ugly()
    self.assertIsNone(ugly.getPartName())
    ugly.setAddress(0x1800)
    ugly.call('ritual_ZNK5QSize5widthEv')
    self.assertEqual(self.called, [('ritual_ZNK5QSize5widthEv', 0x1800)])

  def test_the_part_is_set_once_and_first(self) -> None:
    """A second part, a part after the delete ritual, and a part that
    is no text are refused."""
    ugly = Ugly()
    ugly.setPartName('QtCore')
    with self.assertRaises(RuntimeError):
      ugly.setPartName('QtGui')
    later = Ugly()
    later.setAddress(0x1900)
    later.setDeleteRitual('ritual_ZN5QSizeD1Ev')
    with self.assertRaises(RuntimeError):
      later.setPartName('QtCore')
    later.disown()
    with self.assertRaises(TypeException):
      Ugly().setPartName(None)
