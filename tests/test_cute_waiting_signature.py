"""
TestCuteWaitingSignature tests 'WaitingSignature', one signature of a
class body that names a late class.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.waitaminute import MissingVariable, TypeException
from worktoy.work_test import BaseTest

from cutienator.cute import WAIT, WaitingSignature


def _resize(self, width: int) -> None:
  """A function a signature may belong to."""


class TestCuteWaitingSignature(BaseTest):
  """
  Tests 'WaitingSignature' on its own: what it is told and gives back,
  what it refuses, and its text. How a class body makes one and how it
  is settled is tested in 'TestCuteCuteSpace' and 'TestCuteMetaCute'.
  """

  def test_entries_and_function(self) -> None:
    """The entries and the function told are given back; entries told
    again replace those before."""
    late = WAIT['QLater']
    waiting = WaitingSignature()
    waiting.setSignatureEntries(int, late)
    waiting.setFunction(_resize)
    self.assertEqual(waiting.getSignatureEntries(), (int, late))
    self.assertIs(waiting.getFunction(), _resize)
    waiting.setSignatureEntries(late)
    self.assertEqual(waiting.getSignatureEntries(), (late,))

  def test_nothing_told_is_refused_when_asked(self) -> None:
    """Asking for entries or a function never told raises."""
    for ask in (WaitingSignature().getSignatureEntries,
                WaitingSignature().getFunction):
      with self.subTest(ask=ask):
        with self.assertRaises(MissingVariable):
          ask()

  def test_what_it_refuses(self) -> None:
    """No entry at all, and a function that cannot be called, are
    refused."""
    with self.assertRaises(ValueError):
      WaitingSignature().setSignatureEntries()
    with self.assertRaises(TypeException):
      WaitingSignature().setFunction('resize')

  def test_its_text(self) -> None:
    """It names its function and its entries, each by its name or its
    text; without a function it says so, and a function without a name
    shows as '?'."""
    waiting = WaitingSignature()
    self.assertEqual(str(waiting), '<WaitingSignature with no function yet>')
    waiting.setFunction(_resize)
    self.assertEqual(
        str(waiting), "<WaitingSignature of '_resize', waiting as ()>")
    waiting.setSignatureEntries(int, WAIT['QLater'])
    said = "<WaitingSignature of '_resize', waiting as (int, " \
           "WAIT['QLater'])>"
    self.assertEqual(str(waiting), said)
    self.assertEqual(repr(waiting), said)
    waiting.setFunction(print.__call__)
    self.assertIn("of '__call__'", str(waiting))

    class Nameless:
      def __call__(self) -> None:
        """Called, and with no name."""

    waiting.setFunction(Nameless())
    self.assertIn("of '?'", str(waiting))
