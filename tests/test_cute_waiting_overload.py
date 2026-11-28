"""
TestCuteWaitingOverload tests 'WaitingOverload', what a stack of
'@overload' decorators leaves at a name of a class body when one of its
signatures names a late class.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.waitaminute import MissingVariable, TypeException
from worktoy.work_test import BaseTest

from cutienator.cute import WAIT, WaitingOverload


def _resize(self, width: int) -> None:
  """A function a stack may decorate."""


class TestCuteWaitingOverload(BaseTest):
  """
  Tests 'WaitingOverload' on its own: the signatures, the function and
  the method kinds it is told, what it refuses, and its text. How a
  class body makes one is tested in 'TestCuteCuteOverload'.
  """

  def test_nothing_told_yet(self) -> None:
    """No signatures and no method kinds at first; asking for a function
    never told raises."""
    waiting = WaitingOverload()
    self.assertEqual(waiting.getSignatures(), ())
    self.assertEqual(waiting.getMethodKinds(), ())
    with self.assertRaises(MissingVariable):
      waiting.getFunction()

  def test_the_signatures_in_the_order_added(self) -> None:
    """Each signature added is kept, the lowest decorator first."""
    late = WAIT['QLater']
    waiting = WaitingOverload()
    waiting.addSignature(int)
    waiting.addSignature(late, int)
    waiting.addSignature()
    self.assertEqual(waiting.getSignatures(), ((int,), (late, int), ()))

  def test_the_function(self) -> None:
    """The function told is given back; one that cannot be called is
    refused."""
    waiting = WaitingOverload()
    waiting.setFunction(_resize)
    self.assertIs(waiting.getFunction(), _resize)
    with self.assertRaises(TypeException):
      waiting.setFunction(None)

  def test_the_method_kinds(self) -> None:
    """Kinds added later stand above those before; anything but
    'classmethod' and 'staticmethod' is refused."""
    waiting = WaitingOverload()
    waiting.addMethodKinds(staticmethod)
    waiting.addMethodKinds(classmethod, staticmethod)
    self.assertEqual(waiting.getMethodKinds(),
                     (classmethod, staticmethod, staticmethod))
    with self.assertRaises(TypeException):
      waiting.addMethodKinds(property)

  def test_its_text(self) -> None:
    """It names its function and each signature; without a function it
    says so, and a function without a name shows as '?'."""
    waiting = WaitingOverload()
    self.assertEqual(str(waiting), '<WaitingOverload with no function yet>')
    waiting.setFunction(_resize)
    waiting.addSignature(int)
    waiting.addSignature(WAIT['QLater'], str)
    said = "<WaitingOverload of '_resize', with (int); " \
           "(WAIT['QLater'], str)>"
    self.assertEqual(str(waiting), said)
    self.assertEqual(repr(waiting), said)

    class Nameless:
      def __call__(self) -> None:
        """Called, and with no name."""

    waiting.setFunction(Nameless())
    self.assertIn("of '?'", str(waiting))
