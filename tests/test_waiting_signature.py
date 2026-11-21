"""
TestWaitingSignature tests 'WaitingSignature', which holds one
signature naming a late class, and its function, until that class is
made.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException
from worktoy.work_test import BaseTest

from cutienator.cute import WaitingSignature, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any


class TestWaitingSignature(BaseTest):
  """
  Tests 'WaitingSignature' on its own. It only holds two things, so the
  tests are about its setters and getters: what each takes, what each
  refuses, and what is missing before a setter is called.

  No test here makes a cute class, so none has to mind the names
  'MetaCute' keeps.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _someFunction(thing: Any) -> Any:
    """A function for a 'WaitingSignature' to hold. It is never called."""
    return thing

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  BEFORE THE SETTERS   # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_getters_refuse_before_their_setters(self) -> None:
    """Each getter raises 'MissingVariable' until its setter is called."""
    waitingSignature = WaitingSignature()
    getters = (
        waitingSignature.getSignatureEntries,
        waitingSignature.getFunction,
    )
    for getter in getters:
      with self.subTest(getter=getter.__name__):
        with self.assertRaises(MissingVariable):
          getter()

  def test_cannot_be_called(self) -> None:
    """A 'WaitingSignature' is no function and cannot be called."""
    waitingSignature = WaitingSignature()
    waitingSignature.setFunction(self._someFunction)
    self.assertFalse(callable(waitingSignature))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE SIGNATURE ENTRIES  # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_entries_are_kept_in_order(self) -> None:
    """The entries come back as given, in the order given."""
    wait = WAIT['EntryLate']
    waitingSignature = WaitingSignature()
    waitingSignature.setSignatureEntries(int, wait, str)
    self.assertEqual(
        waitingSignature.getSignatureEntries(), (int, wait, str))

  def test_entries_given_again_replace(self) -> None:
    """Setting the entries again replaces the ones given before."""
    wait = WAIT['AgainLate']
    waitingSignature = WaitingSignature()
    waitingSignature.setSignatureEntries(wait)
    waitingSignature.setSignatureEntries(int)
    self.assertEqual(waitingSignature.getSignatureEntries(), (int,))

  def test_no_entry_at_all_is_refused(self) -> None:
    """A signature without entries is refused, and nothing is set."""
    waitingSignature = WaitingSignature()
    with self.assertRaises(ValueError):
      waitingSignature.setSignatureEntries()
    with self.assertRaises(MissingVariable):
      waitingSignature.getSignatureEntries()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE FUNCTION   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_function_is_kept(self) -> None:
    """The function comes back as given."""
    waitingSignature = WaitingSignature()
    waitingSignature.setFunction(self._someFunction)
    self.assertIs(waitingSignature.getFunction(), self._someFunction)

  def test_what_cannot_be_called_is_refused(self) -> None:
    """'setFunction' refuses what cannot be called."""
    waitingSignature = WaitingSignature()
    for wrong in (7, 'someFunction', None, [len]):
      with self.subTest(wrong=type(wrong).__name__):
        with self.assertRaises(TypeException):
          waitingSignature.setFunction(wrong)
    with self.assertRaises(MissingVariable):
      waitingSignature.getFunction()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  ITS TEXT   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_text_before_and_after(self) -> None:
    """The text names the function and the signature once it has them."""
    waitingSignature = WaitingSignature()
    self.assertIn('no function yet', str(waitingSignature))
    waitingSignature.setFunction(self._someFunction)
    waitingSignature.setSignatureEntries(int, WAIT['ShownLate'])
    shown = str(waitingSignature)
    for part in ('_someFunction', 'int', "WAIT['ShownLate']"):
      with self.subTest(part=part):
        self.assertIn(part, shown)
    self.assertEqual(repr(waitingSignature), shown)
