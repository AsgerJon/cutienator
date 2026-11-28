"""
TestCuteCuteOverload tests 'CuteOverload', what a cute class body gets
when it reads the name 'overload'.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.core.sentinels import ARGS
from worktoy.dispatch import TypeSig, overload
from worktoy.work_test import BaseTest

from cutienator.cute import CuteOverload, WAIT, WaitingOverload


def _resize(self, *args) -> None:
  """A function the decorators decorate."""


def _other(self, *args) -> None:
  """Another function."""


class TestCuteCuteOverload(BaseTest):
  """
  Tests 'CuteOverload' on its own: a signature naming no 'WAIT' is
  worktoy's, one naming a 'WAIT' leaves a 'WaitingOverload', and what
  a waiting stack may not share its function with is refused. How a
  class body reads it and keeps what it leaves is tested in
  'TestCuteCuteSpace'.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PLAIN SIGNATURES   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_a_signature_naming_no_wait_is_worktoys(self) -> None:
    """With no 'WAIT', the decorator gives worktoy's record."""
    record = CuteOverload(int, str)(_resize)
    self.assertIsInstance(record, overload)
    self.assertEqual([sig.getRawTypes() for sig, _ in record], [(int, str)])

  def test_fallback_finalize_and_flex_are_worktoys(self) -> None:
    """'fallback', 'finalize' and 'flex' give worktoy's records."""
    self.assertIs(CuteOverload.fallback(_resize).getFallback(), _resize)
    self.assertIs(CuteOverload.finalize(_resize).getFinalizer(), _resize)
    flexed = CuteOverload.flex(int, str)(_resize)
    self.assertEqual(
        sorted(tuple(t.__name__ for t in sig.getRawTypes())
               for sig, _ in flexed),
        [('int', 'str'), ('str', 'int')])

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  WAITING SIGNATURES   # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_a_signature_naming_a_wait_waits(self) -> None:
    """A signature naming a 'WAIT' leaves a 'WaitingOverload' of the
    function and the signature as written."""
    late = WAIT['QLater']
    waiting = CuteOverload(late, int)(_resize)
    self.assertIsInstance(waiting, WaitingOverload)
    self.assertIs(waiting.getFunction(), _resize)
    self.assertEqual(waiting.getSignatures(), ((late, int),))
    self.assertEqual(waiting.getMethodKinds(), ())

  def test_the_rest_of_a_waiting_signature_is_checked(self) -> None:
    """What no call could match, beside the 'WAIT', is refused where it
    is written."""
    with self.assertRaises(TypeError):
      CuteOverload(WAIT['QLater'], None)

  def test_a_stack_above_a_waiting_signature(self) -> None:
    """More signatures above one that waits are added to it, plain or
    waiting, with the method kinds written between them."""
    late = WAIT['QLater']
    waiting = CuteOverload(late)(_resize)
    stacked = CuteOverload(int)(staticmethod(waiting))
    stacked = CuteOverload(late, str)(stacked)
    self.assertIs(stacked, waiting)
    self.assertEqual(waiting.getSignatures(), ((late,), (int,), (late, str)))
    self.assertEqual(waiting.getMethodKinds(), (staticmethod,))

  def test_a_waiting_signature_of_a_method_kind(self) -> None:
    """A 'staticmethod' or 'classmethod' below the decorator is noted."""
    waiting = CuteOverload(WAIT['QLater'])(classmethod(_resize))
    self.assertEqual(waiting.getMethodKinds(), (classmethod,))
    self.assertIs(waiting.getFunction(), _resize)

  def test_a_waiting_signature_above_plain_ones(self) -> None:
    """A signature naming a 'WAIT' above plain ones takes their function,
    their signatures and their method kind."""
    late = WAIT['QLater']
    record = overload(int)(overload(str, float)(_resize))
    waiting = CuteOverload(late)(record)
    self.assertIs(waiting.getFunction(), _resize)
    self.assertEqual(sorted(waiting.getSignatures(), key=len), [
        (int,), (late,), (str, float)])
    record = overload(int)(classmethod(_resize))
    self.assertEqual(CuteOverload(late)(record).getMethodKinds(),
                     (classmethod,))

  def test_what_a_waiting_signature_may_not_share(self) -> None:
    """Above a fallback, a finalizer, a variadic or flexible signature,
    two functions, or a function worktoy wraps, it is refused."""
    late = WAIT['QLater']
    twoFunctions = overload(int)(_resize)
    twoFunctions._addSigFunc(TypeSig(str), _other)
    shared = (
        overload.fallback(_resize),
        overload.finalize(_resize),
        overload(int, ARGS[int])(_resize),
        overload.flex(int, str, float, bytes)(_resize),
        twoFunctions,
        overload.flex(int, str)(_resize),
        overload.flex(int)(_resize),
    )
    for record in shared:
      with self.subTest(record=record):
        with self.assertRaises(TypeError) as caught:
          CuteOverload(late)(record)
        self.assertIn("WAIT['QLater']", str(caught.exception))

  def test_a_variadic_signature_above_a_waiting_one(self) -> None:
    """A signature ending in 'ARGS' above one that waits is refused."""
    waiting = CuteOverload(WAIT['QLater'])(_resize)
    for entries in ((int, ARGS), (ARGS[int],)):
      with self.subTest(entries=entries):
        with self.assertRaises(TypeError) as caught:
          CuteOverload(*entries)(waiting)
        self.assertIn("ending in 'ARGS'", str(caught.exception))

  def test_a_waiting_stack_shares_with_plain_signatures_only(self) -> None:
    """'fallback', 'finalize' and 'flex' above a waiting stack, and 'flex'
    naming a 'WAIT', are refused."""
    for decorate, name in (
        (CuteOverload.fallback, 'overload.fallback'),
        (CuteOverload.finalize, 'overload.finalize'),
        (CuteOverload.flex(int, str), 'overload.flex'),
    ):
      with self.subTest(name=name):
        waiting = CuteOverload(WAIT['QLater'])(_resize)
        with self.assertRaises(TypeError) as caught:
          decorate(staticmethod(waiting))
        self.assertIn("'%s'" % name, str(caught.exception))
    with self.assertRaises(TypeError) as caught:
      CuteOverload.flex(int, WAIT['QLater'])
    self.assertIn("cannot take WAIT['QLater']", str(caught.exception))
