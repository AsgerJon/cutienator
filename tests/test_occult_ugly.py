"""
TestOccultUgly tests 'Ugly', which stands for one C++ object on behalf
of its cute side.
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
  from typing import Any

#  Addresses no real object has, one for each test that needs one.
_FAKE = 0x7ead0000


class _CuteSide:
  """A stand-in for a cute object, which an 'Ugly' only refers to."""


class TestOccultUgly(BaseTest):
  """
  Tests 'Ugly': its address and how it is found by it, its part, its
  cute side, owning and watching the C++ object, and calling a ritual
  on it.

  What to know before adding a test
  ---------------------------------

  - Most tests replace 'Rituals.call' and 'Rituals.callFrom' for their
    own length, and use made-up addresses ('_address'), so each sees
    the ritual an 'Ugly' would run, and nothing is run.
  - One test watches a real QObject made and removed by the rituals of
    QtCore, so it needs the target file of QtCore built, as every test
    of a cute class does.
  - An 'Ugly' removes its object, or its watcher, when it is collected.
    A test of that drops the last reference and collects.
  """

  __count__ = 0

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def _address(cls) -> int:
    """A made-up address, another for each call."""
    cls.__count__ += 1
    return _FAKE + 16 * cls.__count__

  def _calls(self) -> Any:
    """Replaces 'Rituals.call' and 'Rituals.callFrom' for the test, and
    gives both stand-ins."""
    call = mock.patch.object(Rituals, 'call').start()
    callFrom = mock.patch.object(Rituals, 'callFrom').start()
    self.addCleanup(mock.patch.stopall)
    return call, callFrom

  def _ugly(self) -> Ugly:
    """An 'Ugly' of a made-up address."""
    ugly = Ugly()
    ugly.setAddress(self._address())
    return ugly

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE ADDRESS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_address(self) -> None:
    """The address is set once, and found back by it."""
    ugly = Ugly()
    address = self._address()
    ugly.setAddress(address)
    self.assertEqual(ugly.getAddress(), address)
    self.assertIs(Ugly.at(address), ugly)

  def test_no_address_yet(self) -> None:
    """Before an address is set, asking for it raises."""
    with self.assertRaises(MissingVariable):
      Ugly().getAddress()

  def test_an_address_must_be_a_positive_int(self) -> None:
    """An address that is no 'int', or a 'bool', is refused, and so is
    one below one."""
    for address in ('0x10', 1.0, True, None):
      with self.subTest(address=address):
        with self.assertRaises(TypeException):
          Ugly().setAddress(address)
    for address in (0, -16):
      with self.subTest(address=address):
        with self.assertRaises(ValueError):
          Ugly().setAddress(address)

  def test_an_address_is_set_once(self) -> None:
    """An 'Ugly' does not move to another object, naming both."""
    ugly = self._ugly()
    other = self._address()
    with self.assertRaises(RuntimeError) as caught:
      ugly.setAddress(other)
    self.assertIn(hex(ugly.getAddress()), str(caught.exception))
    self.assertIn(hex(other), str(caught.exception))

  def test_an_address_of_no_ugly(self) -> None:
    """Looking up an address no 'Ugly' stands for raises, naming it."""
    address = self._address()
    with self.assertRaises(LookupError) as caught:
      Ugly.at(address)
    self.assertIn(hex(address), str(caught.exception))

  def test_an_ugly_collected_is_found_no_more(self) -> None:
    """Once its 'Ugly' is collected, its address finds nothing."""
    ugly = self._ugly()
    address = ugly.getAddress()
    del ugly
    gc.collect()
    with self.assertRaises(LookupError):
      Ugly.at(address)

  def test_more_addresses_of_one_object(self) -> None:
    """An object known by more addresses, as one of several bases, is
    found by each."""
    ugly = self._ugly()
    other = self._address()
    ugly.addPartAddress(other)
    self.assertIs(Ugly.at(other), ugly)
    self.assertNotEqual(ugly.getAddress(), other)

  def test_more_addresses_refused(self) -> None:
    """Another address must be a positive 'int', after the first."""
    for address in ('x', False):
      with self.subTest(address=address):
        with self.assertRaises(TypeException):
          self._ugly().addPartAddress(address)
    with self.assertRaises(ValueError):
      self._ugly().addPartAddress(0)
    with self.assertRaises(MissingVariable):
      Ugly().addPartAddress(self._address())

  def test_str_and_repr(self) -> None:
    """'str' and 'repr' say where the object is, or that it is not yet
    known."""
    self.assertEqual(str(Ugly()), '<Ugly with no address yet>')
    ugly = self._ugly()
    said = '<Ugly of the C++ object at %s>' % hex(ugly.getAddress())
    self.assertEqual(str(ugly), said)
    self.assertEqual(repr(ugly), said)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE PART AND THE CUTE SIDE   # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_part(self) -> None:
    """No part until set; a part is a 'str', set once."""
    ugly = self._ugly()
    self.assertIsNone(ugly.getPartName())
    ugly.setPartName('QtGraphs')
    self.assertEqual(ugly.getPartName(), 'QtGraphs')
    with self.assertRaises(TypeException):
      self._ugly().setPartName(7)
    with self.assertRaises(RuntimeError) as caught:
      ugly.setPartName('QtCharts')
    self.assertIn("the part 'QtGraphs'", str(caught.exception))

  def test_the_part_comes_before_the_delete_ritual(self) -> None:
    """A part set after the delete ritual is refused, saying so."""
    self._calls()
    ugly = self._ugly()
    ugly.setDeleteRitual('ritual_drop')
    with self.assertRaises(RuntimeError) as caught:
      ugly.setPartName('QtGraphs')
    self.assertIn('the delete ritual', str(caught.exception))

  def test_the_cute_side(self) -> None:
    """The cute side is kept without keeping it alive; once it is gone,
    asking for it raises."""
    ugly = self._ugly()
    with self.assertRaises(MissingVariable):
      ugly.getCuteSide()
    cute = _CuteSide()
    ugly.setCuteSide(cute)
    self.assertIs(ugly.getCuteSide(), cute)
    del cute
    gc.collect()
    with self.assertRaises(RuntimeError) as caught:
      ugly.getCuteSide()
    self.assertIn('no longer exists', str(caught.exception))

  def test_ours(self) -> None:
    """An object is no object of a class of ours until said."""
    ugly = self._ugly()
    self.assertIs(ugly.isOurs(), False)
    ugly.setOurs()
    self.assertIs(ugly.isOurs(), True)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OWNING   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_an_object_owned_is_removed_when_collected(self) -> None:
    """An object Python owns is removed by its delete ritual once its
    'Ugly' is collected, and not before."""
    call, callFrom = self._calls()
    ugly = self._ugly()
    address = ugly.getAddress()
    self.assertIs(ugly.isOwned(), False)
    self.assertIsNone(ugly.getDeleteRitual())
    ugly.setDeleteRitual('ritual_ZN6QCutieD1Ev')
    self.assertIs(ugly.isOwned(), True)
    self.assertEqual(ugly.getDeleteRitual(), 'ritual_ZN6QCutieD1Ev')
    call.assert_not_called()
    del ugly
    gc.collect()
    call.assert_called_once_with('ritual_ZN6QCutieD1Ev', address)
    callFrom.assert_not_called()

  def test_an_object_of_a_part_is_removed_from_it(self) -> None:
    """An object of a part set is removed by the ritual of that part."""
    call, callFrom = self._calls()
    ugly = self._ugly()
    address = ugly.getAddress()
    ugly.setPartName('QtGraphs')
    ugly.setDeleteRitual('ritual_drop_QBarSeries')
    del ugly
    gc.collect()
    callFrom.assert_called_once_with(
        'QtGraphs', 'ritual_drop_QBarSeries', address)
    call.assert_not_called()

  def test_an_object_disowned_is_not_removed(self) -> None:
    """An object disowned is left to Qt; disowning one never owned is
    nothing."""
    call, _ = self._calls()
    ugly = self._ugly()
    ugly.disown()
    ugly.setDeleteRitual('ritual_ZN6QCutieD1Ev')
    ugly.disown()
    self.assertIs(ugly.isOwned(), False)
    del ugly
    gc.collect()
    call.assert_not_called()

  def test_the_delete_ritual_refused(self) -> None:
    """A delete ritual that is no 'str', one with no address, and a
    second one, are refused."""
    self._calls()
    with self.assertRaises(TypeException):
      self._ugly().setDeleteRitual(None)
    with self.assertRaises(MissingVariable):
      Ugly().setDeleteRitual('ritual_drop')
    ugly = self._ugly()
    ugly.setDeleteRitual('ritual_drop')
    ugly.disown()
    with self.assertRaises(RuntimeError) as caught:
      ugly.setDeleteRitual('ritual_drop')
    self.assertIn('set once', str(caught.exception))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  WATCHING   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_an_object_not_watched_is_never_gone(self) -> None:
    """An object not watched is never said to be gone, and Qt is not
    asked."""
    call, _ = self._calls()
    ugly = self._ugly()
    self.assertIs(ugly.isWatched(), False)
    self.assertIs(ugly.isGone(), False)
    call.assert_not_called()

  def test_watching_an_object(self) -> None:
    """Qt is asked to watch the object, once; whether it is gone is
    asked of the watcher; the watcher is removed when the 'Ugly' is
    collected."""
    call, _ = self._calls()
    watcher = self._address()
    call.return_value = watcher
    ugly = self._ugly()
    address = ugly.getAddress()
    ugly.watch()
    call.assert_called_once_with(Ugly.__watch_make_ritual__, address)
    self.assertIs(ugly.isWatched(), True)
    call.return_value = False
    with self.assertRaises(RuntimeError) as caught:
      ugly.watch()
    self.assertIn('already watches', str(caught.exception))
    call.reset_mock()
    self.assertIs(ugly.isGone(), False)
    call.assert_called_once_with(Ugly.__watch_ask_ritual__, watcher)
    call.reset_mock()
    del ugly
    gc.collect()
    call.assert_called_once_with(Ugly.__watch_drop_ritual__, watcher)

  def test_an_object_qt_removed(self) -> None:
    """Once Qt has removed it, its address is refused, and so is a
    lookup by it."""
    call, _ = self._calls()
    call.return_value = self._address()
    ugly = self._ugly()
    address = ugly.getAddress()
    ugly.watch()
    call.return_value = True
    with self.assertRaises(RuntimeError) as caught:
      ugly.getAddress()
    self.assertIn('Qt has removed the C++ object', str(caught.exception))
    with self.assertRaises(LookupError) as caught:
      Ugly.at(address)
    self.assertIn('another object', str(caught.exception))

  def test_watching_needs_an_address(self) -> None:
    """Watching an object of no address raises."""
    self._calls()
    with self.assertRaises(MissingVariable):
      Ugly().watch()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CALLING  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_calling_a_ritual_on_the_object(self) -> None:
    """A ritual is run on the address, with what is handed after it, in
    the part set, or found by its name."""
    call, callFrom = self._calls()
    call.return_value = 'from call'
    callFrom.return_value = 'from callFrom'
    ugly = self._ugly()
    address = ugly.getAddress()
    self.assertEqual(ugly.call('ritual_size', 3), 'from call')
    call.assert_called_once_with('ritual_size', address, 3)
    ugly.setPartName('QtGraphs')
    self.assertEqual(ugly.call('ritual_size', 4), 'from callFrom')
    callFrom.assert_called_once_with('QtGraphs', 'ritual_size', address, 4)

  def test_a_real_qobject_watched_and_removed(self) -> None:
    """A QObject made by its ritual, watched, then removed by its
    destructor: the 'Ugly' sees it is gone."""
    address = Rituals.call('ritual_ZN7QObjectC1EPS_', None)
    ugly = Ugly()
    ugly.setAddress(address)
    ugly.watch()
    self.assertIs(ugly.isGone(), False)
    self.assertEqual(ugly.getAddress(), address)
    Rituals.call('ritual_ZN7QObjectD1Ev', address)
    self.assertIs(ugly.isGone(), True)
    with self.assertRaises(RuntimeError):
      ugly.getAddress()
