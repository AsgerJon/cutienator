"""
TestWaitingOverload tests 'WaitingOverload', which holds a function and
a signature naming a late class until that class is made.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException
from worktoy.work_test import BaseTest

from cutienator import WaitingOverload, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any


class TestWaitingOverload(BaseTest):
  """
  Tests 'WaitingOverload' on its own. It only holds three things, so
  the tests are about its setters and getters: what each takes, what
  each refuses, and what is missing before a setter is called.

  No test here makes a cute class, so none has to mind the names
  'MetaCute' keeps.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _someFunction(thing: Any) -> Any:
    """A function for a 'WaitingOverload' to hold. It is never called."""
    return thing

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  BEFORE THE SETTERS   # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_getters_refuse_before_their_setters(self) -> None:
    """Each getter raises 'MissingVariable' until its setter is called."""
    waitingOverload = WaitingOverload()
    getters = (
        waitingOverload.getSignatureEntries,
        waitingOverload.getFunction,
        waitingOverload.getMethodKinds,
    )
    for getter in getters:
      with self.subTest(getter=getter.__name__):
        with self.assertRaises(MissingVariable):
          getter()

  def test_cannot_be_called(self) -> None:
    """A 'WaitingOverload' is no function and cannot be called."""
    waitingOverload = WaitingOverload()
    waitingOverload.setFunction(self._someFunction)
    self.assertFalse(callable(waitingOverload))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE SIGNATURE ENTRIES  # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_entries_are_kept_in_order(self) -> None:
    """The entries come back as given, in the order given."""
    wait = WAIT['EntryLate']
    waitingOverload = WaitingOverload()
    waitingOverload.setSignatureEntries(int, wait, str)
    self.assertEqual(waitingOverload.getSignatureEntries(), (int, wait, str))

  def test_entries_given_again_replace(self) -> None:
    """Setting the entries again replaces the ones given before."""
    wait = WAIT['AgainLate']
    waitingOverload = WaitingOverload()
    waitingOverload.setSignatureEntries(wait)
    waitingOverload.setSignatureEntries(int)
    self.assertEqual(waitingOverload.getSignatureEntries(), (int,))

  def test_no_entry_at_all_is_refused(self) -> None:
    """A signature without entries is refused, and nothing is set."""
    waitingOverload = WaitingOverload()
    with self.assertRaises(ValueError):
      waitingOverload.setSignatureEntries()
    with self.assertRaises(MissingVariable):
      waitingOverload.getSignatureEntries()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE FUNCTION   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_function_is_kept(self) -> None:
    """The function comes back as given."""
    waitingOverload = WaitingOverload()
    waitingOverload.setFunction(self._someFunction)
    self.assertIs(waitingOverload.getFunction(), self._someFunction)

  def test_what_cannot_be_called_is_refused(self) -> None:
    """'setFunction' refuses what cannot be called."""
    waitingOverload = WaitingOverload()
    for wrong in (7, 'someFunction', None, [len]):
      with self.subTest(wrong=type(wrong).__name__):
        with self.assertRaises(TypeException):
          waitingOverload.setFunction(wrong)
    with self.assertRaises(MissingVariable):
      waitingOverload.getFunction()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE METHOD KINDS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_no_kind_means_an_instance_method(self) -> None:
    """Setting no kind gives an empty tuple, not a missing value."""
    waitingOverload = WaitingOverload()
    waitingOverload.setMethodKinds()
    self.assertEqual(waitingOverload.getMethodKinds(), ())

  def test_kinds_are_kept_in_order(self) -> None:
    """The kinds come back as given, outermost first."""
    waitingOverload = WaitingOverload()
    for kinds in ((staticmethod,), (classmethod,), (classmethod,) * 2):
      with self.subTest(kinds=[kind.__name__ for kind in kinds]):
        waitingOverload.setMethodKinds(*kinds)
        self.assertEqual(waitingOverload.getMethodKinds(), kinds)

  def test_what_is_no_kind_is_refused(self) -> None:
    """'setMethodKinds' takes 'classmethod' and 'staticmethod' only."""
    waitingOverload = WaitingOverload()
    for wrong in (property, int, 'staticmethod', None):
      with self.subTest(wrong=repr(wrong)):
        with self.assertRaises(TypeException):
          waitingOverload.setMethodKinds(staticmethod, wrong)
    with self.assertRaises(MissingVariable):
      waitingOverload.getMethodKinds()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  ITS TEXT   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_text_before_and_after(self) -> None:
    """The text names the function and the signature once it has them."""
    waitingOverload = WaitingOverload()
    self.assertIn('no function yet', str(waitingOverload))
    waitingOverload.setFunction(self._someFunction)
    waitingOverload.setSignatureEntries(int, WAIT['ShownLate'])
    shown = str(waitingOverload)
    for part in ('_someFunction', 'int', "WAIT['ShownLate']"):
      with self.subTest(part=part):
        self.assertIn(part, shown)
    self.assertEqual(repr(waitingOverload), shown)
