"""
TestCuteMetaCuteFlags tests 'MetaCuteFlags', the metaclass of the flags
classes of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from cutienator.cute import CuteFlags, CuteFlagsSpace, MetaCuteFlags


class TestCuteMetaCuteFlags(BaseTest):
  """
  Tests 'MetaCuteFlags': the namespace a flags class's body runs in,
  and the names it gives the class holding it.
  """

  def test_it_is_the_metaclass_of_a_flags_class(self) -> None:
    """A flags class is made by 'MetaCuteFlags', its body run in a
    'CuteFlagsSpace'."""

    class Option(CuteFlags):
      Wide = 0x1

    self.assertIsInstance(Option, MetaCuteFlags)
    self.assertIsInstance(
        MetaCuteFlags.__prepare__('Option', (CuteFlags,)), CuteFlagsSpace)

  def test_the_names_given_to_the_holder(self) -> None:
    """Each name the body declared, with its value, in order; 'NULL' only
    when declared."""

    class Option(CuteFlags):
      Wide = 0x1
      Broad = 0x1
      Tall = 0x2

    self.assertEqual(Option.getShortNames(), dict(
        Wide=Option.Wide, Broad=Option.Wide, Tall=Option.Tall))

    class Choice(CuteFlags):
      NULL = 0
      Some = 0x4

    self.assertEqual([*Choice.getShortNames()], ['NULL', 'Some'])
