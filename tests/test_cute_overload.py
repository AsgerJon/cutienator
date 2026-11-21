"""
TestCuteOverload tests 'CuteOverload', which a cute class body gets when
it reads the name 'overload'.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS, ARGS
from worktoy.dispatch import overload
from worktoy.waitaminute import TypeException
from worktoy.work_test import BaseTest

from cutienator.cute import CuteOverload, WaitingOverload, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any


class TestCuteOverload(BaseTest):
  """
  Tests 'CuteOverload' on its own, called by its own name, the way the
  namespace of a cute class hands it to a body under the name
  'overload'. Two things are tested: that a signature with nothing late
  in it gives exactly what worktoy's 'overload' gives, and what a
  signature with a 'WAIT' in it gives and refuses, alone and in a
  stack of decorators on one function.

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
        self.assertEqual(waitingOverload.getSignatures(), (entries,))
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
  #  SHARING A FUNCTION   # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_signatures_of_one_stack_share_the_function(self) -> None:
    """A waiting signature shares its function with the other plain
    signatures of its stack, whichever is written on top. The signatures
    come in the order worktoy takes them: the lowest decorator first."""
    wait, other = WAIT['SharedLate'], WAIT['SharedOther']
    function = self._someFunction

    def waiting() -> Any:
      return CuteOverload(wait)(function)

    stacks = dict(
        waitingAbovePlain=(
            CuteOverload(wait)(CuteOverload(int)(function)),
            ((int,), (wait,))),
        plainAboveWaiting=(
            CuteOverload(int)(waiting()), ((wait,), (int,))),
        waitingAboveWaiting=(
            CuteOverload(other)(waiting()), ((wait,), (other,))),
        waitingAboveTwoPlain=(
            CuteOverload(wait, int)(
                CuteOverload(str)(CuteOverload(int)(function))),
            ((int,), (str,), (wait, int))),
        waitingAboveNoEntry=(
            CuteOverload(wait)(CuteOverload()(function)), ((), (wait,))),
        noEntryAboveWaiting=(
            CuteOverload()(waiting()), ((wait,), ())),
        waitingAboveTHIS=(
            CuteOverload(wait)(CuteOverload(THIS)(function)),
            ((THIS,), (wait,))),
    )
    for name, (stack, signatures) in stacks.items():
      with self.subTest(stack=name):
        self.assertIsInstance(stack, WaitingOverload)
        self.assertEqual(stack.getSignatures(), signatures)
        self.assertIs(stack.getFunction(), function)
        self.assertEqual(stack.getMethodKinds(), ())

  def test_method_kinds_anywhere_in_a_stack_are_kept(self) -> None:
    """A kind written anywhere in a stack that waits is noted: below
    worktoy's record, between two decorators, or below them all."""
    wait = WAIT['StackKindLate']
    function = self._someFunction
    for kind in (staticmethod, classmethod):
      stacks = dict(
          belowThePlainOne=CuteOverload(wait)(
              CuteOverload(int)(kind(function))),
          betweenWaitingAndPlain=CuteOverload(wait)(
              kind(CuteOverload(int)(function))),
          betweenPlainAndWaiting=CuteOverload(int)(
              kind(CuteOverload(wait)(function))),
          belowTheWaitingOne=CuteOverload(int)(
              CuteOverload(wait)(kind(function))),
      )
      for name, stack in stacks.items():
        with self.subTest(kind=kind.__name__, stack=name):
          self.assertEqual(stack.getMethodKinds(), (kind,))
          self.assertIs(stack.getFunction(), function)
          self.assertEqual(len(stack.getSignatures()), 2)

  def test_other_roles_do_not_share_with_a_waiting_signature(self) -> None:
    """A waiting signature shares its function with plain signatures
    only: a fallback, a finalizer, 'overload.flex' and a signature
    ending in 'ARGS' are refused in a stack that waits."""
    wait = WAIT['RoleLate']
    function = self._someFunction

    def waiting() -> Any:
      return CuteOverload(wait)(function)

    attempts = dict(
        fallbackAboveWaiting=lambda: CuteOverload.fallback(waiting()),
        finalizeAboveWaiting=lambda: CuteOverload.finalize(waiting()),
        flexAboveWaiting=lambda: CuteOverload.flex(int, str)(waiting()),
        argsAboveWaiting=lambda: CuteOverload(int, ARGS)(waiting()),
        argsOfAClassAboveWaiting=lambda: CuteOverload(ARGS[int])(waiting()),
        waitingAboveFallback=lambda: CuteOverload(wait)(
            CuteOverload.fallback(function)),
        waitingAboveFinalizer=lambda: CuteOverload(wait)(
            CuteOverload.finalize(CuteOverload(int)(function))),
        waitingAboveFlex=lambda: CuteOverload(wait)(
            CuteOverload.flex(int, str)(function)),
        waitingAboveFlexOfOne=lambda: CuteOverload(wait)(
            CuteOverload.flex(int)(function)),
        waitingAboveFlexOfFour=lambda: CuteOverload(wait)(
            CuteOverload.flex(int, str, float, bytes)(
                CuteOverload(int)(function))),
        waitingAboveArgs=lambda: CuteOverload(wait)(
            CuteOverload(int, ARGS)(CuteOverload(int)(function))),
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
