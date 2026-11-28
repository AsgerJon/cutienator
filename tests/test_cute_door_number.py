"""
TestCuteDoorNumber tests 'DoorNumber', the number of a member of an enum
of Qt on its way into a ritual.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from cutienator.cute import DoorNumber


class TestCuteDoorNumber(BaseTest):
  """
  Tests 'DoorNumber': it is an 'int' of its own class, so a signature
  naming an enum can tell it from a plain number. How the enums and the
  flags refuse it is tested with them, in 'TestCuteCuteNum' and
  'TestCuteCuteFlags'.
  """

  def test_it_is_a_number_of_its_own_class(self) -> None:
    """A 'DoorNumber' is an 'int', equal to its number, and is not a
    plain 'int'."""
    door = DoorNumber(0x21)
    self.assertIsInstance(door, int)
    self.assertIs(type(door), DoorNumber)
    self.assertEqual(door, 0x21)
    self.assertEqual(door | 0x2, 0x23)
    self.assertIs(type(door | 0x2), int)
