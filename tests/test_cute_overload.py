"""
TestCuteOverload tests 'CuteOverload', which a cute class body gets when
it reads the name 'overload'.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.waitaminute import TypeException
from worktoy.work_test import BaseTest

from cutienator import CuteOverload, WaitingOverload, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any


class TestCuteOverload(BaseTest):
  """
  Tests 'CuteOverload' on its own, called by its own name, the way the
  namespace of a cute class hands it to a body under the name
  'overload'. Two things are tested: that a signature with nothing late
  in it gives exactly what worktoy's 'overload' gives, and what a
  signature with a 'WAIT' in it gives and refuses.

  No test here makes a cute class, and a 'WAIT' in no class body is
  noted nowhere, so none has to mind the names 'MetaCute' keeps.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _someFunction(self: Any, thing: Any) -> Any:
    """A function to decorate. It is never called."""
    return thing

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTHING LATE IN THE SIGNATURE  # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_calling_it_gives_a_decorator(self) -> None:
    """Calling it gives a decorator and never a 'CuteOverload' object."""
    wait = WAIT['DecoratorLate']
    for entries in ((int,), (int, str), (THIS,), (wait,), (int, wait)):
      with self.subTest(entries=[str(entry) for entry in entries]):
        decorator = CuteOverload(*entries)
        self.assertNotIsInstance(decorator, CuteOverload)
        self.assertTrue(callable(decorator))

  def test_classes_only_give_worktoys_record(self) -> None:
    """With classes and 'THIS' only, the result is worktoy's own record."""
    for entries in ((int,), (int, str), (THIS,), ()):
      with self.subTest(entries=[str(entry) for entry in entries]):
        record = CuteOverload(*entries)(self._someFunction)
        self.assertIsInstance(record, overload)
        signatures = [sig.getRawTypes() for sig, _ in record]
        self.assertEqual(signatures, [entries])

  def test_classes_only_are_checked_as_worktoy_checks(self) -> None:
    """A wrong entry is refused on the line, as by worktoy's 'overload'."""
    with self.subTest(wrong='text where a class belongs'):
      with self.assertRaises(TypeException):
        CuteOverload(int, 'str')
    with self.subTest(wrong='None where a class belongs'):
      with self.assertRaises(TypeError):
        CuteOverload(None)

  def test_stacking_classes_only_works_as_in_worktoy(self) -> None:
    """Two signatures with nothing late may share one function."""
    record = CuteOverload(int)(CuteOverload(str)(self._someFunction))
    self.assertIsInstance(record, overload)
    signatures = [sig.getRawTypes() for sig, _ in record]
    self.assertEqual(sorted(signatures, key=repr), [(int,), (str,)])

  def test_fallback_finalize_and_flex_are_worktoys(self) -> None:
    """The three other roles give what worktoy's own give."""
    with self.subTest(role='fallback'):
      record = CuteOverload.fallback(self._someFunction)
      self.assertIsInstance(record, overload)
      self.assertTrue(record.isFallback())
    with self.subTest(role='finalize'):
      record = CuteOverload.finalize(self._someFunction)
      self.assertIsInstance(record, overload)
      self.assertTrue(record.isFinalizer())
    with self.subTest(role='flex'):
      record = CuteOverload.flex(int, str)(self._someFunction)
      self.assertIsInstance(record, overload)
      signatures = [sig.getRawTypes() for sig, _ in record]
      bothOrders = [(int, str), (str, int)]
      self.assertEqual(sorted(signatures, key=repr), bothOrders)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  A WAIT IN THE SIGNATURE  # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_a_wait_gives_a_waiting_overload(self) -> None:
    """With a WAIT among the entries, the result holds them and waits."""
    wait = WAIT['HeldLate']
    for entries in ((wait,), (int, wait), (wait, THIS, str)):
      with self.subTest(entries=[str(entry) for entry in entries]):
        waitingOverload = CuteOverload(*entries)(self._someFunction)
        self.assertIsInstance(waitingOverload, WaitingOverload)
        self.assertNotIsInstance(waitingOverload, overload)
        self.assertEqual(waitingOverload.getSignatureEntries(), entries)
        self.assertIs(waitingOverload.getFunction(), self._someFunction)
        self.assertEqual(waitingOverload.getMethodKinds(), ())

  def test_method_kinds_below_are_taken_off_and_kept(self) -> None:
    """A kind written below the decorator is noted, and taken off."""
    wait = WAIT['KindBelowLate']
    for kind in (staticmethod, classmethod):
      with self.subTest(kind=kind.__name__):
        waitingOverload = CuteOverload(wait)(kind(self._someFunction))
        self.assertEqual(waitingOverload.getMethodKinds(), (kind,))
        self.assertIs(waitingOverload.getFunction(), self._someFunction)

  def test_entries_beside_a_wait_are_still_checked(self) -> None:
    """Beside a WAIT, an entry that is no class is refused on the line."""
    wait = WAIT['BesideLate']
    with self.subTest(wrong='text where a class belongs'):
      with self.assertRaises(TypeException):
        CuteOverload(wait, 'str')
    with self.subTest(wrong='None where a class belongs'):
      with self.assertRaises(TypeError):
        CuteOverload(None, wait)

  def test_what_cannot_be_called_is_refused(self) -> None:
    """A waiting signature above something that is no function is refused."""
    wait = WAIT['UncallableLate']
    for wrong in (7, 'someFunction', staticmethod(7)):
      with self.subTest(wrong=type(wrong).__name__):
        with self.assertRaises(TypeException):
          CuteOverload(wait)(wrong)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  A FUNCTION OF ITS OWN  # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_sharing_a_function_is_refused(self) -> None:
    """A waiting signature shares its function with no other decorator."""
    wait, other = WAIT['SharedLate'], WAIT['SharedOther']

    def waiting() -> Any:
      return CuteOverload(wait)(self._someFunction)

    def plain() -> Any:
      return CuteOverload(int)(self._someFunction)

    attempts = dict(
        waitingAbovePlain=lambda: CuteOverload(wait)(plain()),
        plainAboveWaiting=lambda: CuteOverload(int)(waiting()),
        waitingAboveWaiting=lambda: CuteOverload(other)(waiting()),
        kindInBetween=lambda: CuteOverload(int)(staticmethod(waiting())),
        fallbackAboveWaiting=lambda: CuteOverload.fallback(waiting()),
        finalizeAboveWaiting=lambda: CuteOverload.finalize(waiting()),
        flexAboveWaiting=lambda: CuteOverload.flex(int, str)(waiting()),
    )
    #  The refusal asked for is the one 'CuteOverload' words itself, a
    #  plain 'TypeError'. Without it worktoy would still stumble over the
    #  'WaitingOverload' further on and raise its own 'TypeException',
    #  which says nothing of why. That one must not pass for it.
    for attempt, make in attempts.items():
      with self.subTest(attempt=attempt):
        with self.assertRaises(TypeError) as caught:
          make()
        self.assertIs(type(caught.exception), TypeError)
        self.assertIn('function', str(caught.exception))

  def test_flex_with_a_wait_is_refused(self) -> None:
    """'overload.flex' takes no WAIT, wherever it stands."""
    wait = WAIT['FlexLate']
    for entries in ((wait,), (int, wait), (wait, int, str)):
      with self.subTest(entries=[str(entry) for entry in entries]):
        with self.assertRaises(TypeError) as caught:
          CuteOverload.flex(*entries)
        self.assertIs(type(caught.exception), TypeError)
        self.assertIn("WAIT['FlexLate']", str(caught.exception))
