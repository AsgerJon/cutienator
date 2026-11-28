"""
TestCuteCuteFlagsHook tests 'CuteFlagsHook', which takes the flags out
of the body of a flags class.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.waitaminute.meta import HookException
from worktoy.work_test import BaseTest

from cutienator.cute import CuteFlags


class TestCuteCuteFlagsHook(BaseTest):
  """
  Tests 'CuteFlagsHook' through class statements: a number bound at a
  name is a flag, anything else stays in the body, and a name is never
  both.
  """

  def test_the_numbers_of_the_body_are_flags(self) -> None:
    """Each number bound is a flag; a dunder and anything that is no
    plain 'int' stay in the body as they are."""

    class Option(CuteFlags):
      """The options."""
      Wide = 0x1
      Tall = 0x2
      label = 'not a flag'
      truth = True

    self.assertIsInstance(Option.Wide, Option)
    self.assertEqual(Option.label, 'not a flag')
    self.assertIs(Option.truth, True)
    self.assertEqual(Option.__doc__, 'The options.')

  def test_a_plain_value_then_a_flag_is_refused(self) -> None:
    """A name bound to a plain value and then to a number raises."""
    with self.assertRaises((SyntaxError, HookException)) as caught:

      class Option(CuteFlags):
        Wide = 'plain'
        Wide = 0x1

    self.assertIn("'Option.Wide' is bound to a plain value",
                  str(caught.exception))

  def test_a_flag_then_a_plain_value_is_refused(self) -> None:
    """A flag bound then to a plain value raises."""
    with self.assertRaises((SyntaxError, HookException)) as caught:

      class Option(CuteFlags):
        Wide = 0x1
        Wide = 'plain'

    self.assertIn("'Option.Wide' is a flag", str(caught.exception))

  def test_the_number_is_checked_before_the_body(self) -> None:
    """A class statement naming a C++ number no flags class has fails
    before its body runs."""
    ran = []
    with self.assertRaises(ValueError) as caught:

      class Option(CuteFlags, number='float'):
        ran.append('body')
        Wide = 0x1

    self.assertEqual(ran, [])
    self.assertIn("'float'", str(caught.exception))
