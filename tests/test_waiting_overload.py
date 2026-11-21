"""
TestWaitingOverload tests 'WaitingOverload', which holds a function and
every signature its stack of '@overload' decorators gives it, when one
of them names a late class.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException
from worktoy.work_test import BaseTest

from cutienator.cute import WaitingOverload, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any


class TestWaitingOverload(BaseTest):
  """
  Tests 'WaitingOverload' on its own. It only holds three things, so
  the tests are about what each setter takes and refuses, and what the
  getters give before and after.

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

  def test_nothing_is_held_at_first(self) -> None:
    """A new one has no signature and no kind, and its function is
    missing."""
    waitingOverload = WaitingOverload()
    self.assertEqual(waitingOverload.getSignatures(), ())
    self.assertEqual(waitingOverload.getMethodKinds(), ())
    with self.assertRaises(MissingVariable):
      waitingOverload.getFunction()

  def test_cannot_be_called(self) -> None:
    """A 'WaitingOverload' is no function and cannot be called."""
    waitingOverload = WaitingOverload()
    waitingOverload.setFunction(self._someFunction)
    self.assertFalse(callable(waitingOverload))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE SIGNATURES   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_signatures_are_kept_in_the_order_added(self) -> None:
    """Each signature comes back as given, the first added first."""
    wait = WAIT['EntryLate']
    waitingOverload = WaitingOverload()
    waitingOverload.addSignature(int)
    waitingOverload.addSignature(int, wait, str)
    expected = ((int,), (int, wait, str))
    self.assertEqual(waitingOverload.getSignatures(), expected)

  def test_no_entry_at_all_is_a_signature(self) -> None:
    """The signature of '@overload()' has no entry, and is kept."""
    waitingOverload = WaitingOverload()
    waitingOverload.addSignature()
    waitingOverload.addSignature(WAIT['EmptyLate'])
    self.assertEqual(waitingOverload.getSignatures()[0], ())
    self.assertEqual(len(waitingOverload.getSignatures()), 2)

  def test_what_the_getter_gives_is_not_the_list_kept(self) -> None:
    """Changing what 'getSignatures' gave changes nothing held."""
    waitingOverload = WaitingOverload()
    waitingOverload.addSignature(int)
    self.assertIsInstance(waitingOverload.getSignatures(), tuple)
    self.assertIsNot(
        waitingOverload.getSignatures(), waitingOverload.getSignatures())

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

  def test_adding_no_kind_changes_nothing(self) -> None:
    """Adding no kind leaves an instance method an instance method."""
    waitingOverload = WaitingOverload()
    waitingOverload.addMethodKinds()
    self.assertEqual(waitingOverload.getMethodKinds(), ())

  def test_kinds_added_later_come_first(self) -> None:
    """A kind added later was written higher in the stack, so it comes
    before the kinds added earlier."""
    waitingOverload = WaitingOverload()
    waitingOverload.addMethodKinds(staticmethod)
    self.assertEqual(waitingOverload.getMethodKinds(), (staticmethod,))
    waitingOverload.addMethodKinds(classmethod, classmethod)
    expected = (classmethod, classmethod, staticmethod)
    self.assertEqual(waitingOverload.getMethodKinds(), expected)

  def test_what_is_no_kind_is_refused(self) -> None:
    """'addMethodKinds' takes 'classmethod' and 'staticmethod' only, and
    adds nothing when one of them is refused."""
    waitingOverload = WaitingOverload()
    for wrong in (property, int, 'staticmethod', None):
      with self.subTest(wrong=repr(wrong)):
        with self.assertRaises(TypeException):
          waitingOverload.addMethodKinds(staticmethod, wrong)
    self.assertEqual(waitingOverload.getMethodKinds(), ())

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  ITS TEXT   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_text_before_and_after(self) -> None:
    """The text names the function and each signature once it has
    them."""
    waitingOverload = WaitingOverload()
    self.assertIn('no function yet', str(waitingOverload))
    waitingOverload.setFunction(self._someFunction)
    waitingOverload.addSignature(int, WAIT['ShownLate'])
    waitingOverload.addSignature()
    shown = str(waitingOverload)
    for part in ('_someFunction', "(int, WAIT['ShownLate'])", '()'):
      with self.subTest(part=part):
        self.assertIn(part, shown)
    self.assertEqual(repr(waitingOverload), shown)
