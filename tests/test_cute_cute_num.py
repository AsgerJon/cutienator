"""
TestCuteCuteNum tests 'CuteNum', the one base of every enum of Qt that
is no flags enum.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import pickle

from worktoy.keenum import Kee
from worktoy.work_test import BaseTest

from cutienator.cute import CuteFlags, CuteNum, DoorNumber


class _Direction(CuteNum):
  """An enum of module level, so that 'pickle' finds it."""
  Forward = Kee[int](0)
  Backward = Kee[int](1)


class _Rotation(CuteNum):
  """A second enum with a member of the number of one of '_Direction'."""
  Clockwise = Kee[int](1)


class _Option(CuteFlags):
  """Flags with a value of the number of one of '_Direction'."""
  Wide = 0x1


class TestCuteCuteNum(BaseTest):
  """
  Tests 'CuteNum': a member is itself among members and flags, its
  number among numbers, adds as its number, is stored and read back as
  itself, and what a signature naming the enum takes in its place.
  """

  def test_a_member_is_itself(self) -> None:
    """Among members and flags, a member is equal to itself alone."""
    self.assertEqual(_Direction.Backward, _Direction.Backward)
    self.assertNotEqual(_Direction.Backward, _Direction.Forward)
    self.assertNotEqual(_Direction.Backward, _Rotation.Clockwise)
    self.assertNotEqual(_Direction.Backward, _Option.Wide)

  def test_a_member_is_its_number(self) -> None:
    """Among numbers, a member is equal to its number, but never to a
    'bool', and hashes as its number."""
    self.assertEqual(_Direction.Backward, 1)
    self.assertNotEqual(_Direction.Backward, 2)
    self.assertNotEqual(_Direction.Backward, True)
    self.assertNotEqual(_Direction.Forward, False)
    self.assertEqual(hash(_Direction.Backward), hash(1))
    self.assertIn(1, {_Direction.Backward})

  def test_a_member_adds_as_its_number(self) -> None:
    """A member plus a number, either way round, is a plain number."""
    self.assertEqual(_Direction.Backward + 2, 3)
    self.assertEqual(2 + _Direction.Backward, 3)

  def test_a_member_is_stored_and_read_back(self) -> None:
    """A member, named or not, comes back from 'pickle' as itself."""
    for member in (_Direction.Backward, _Direction(7)):
      with self.subTest(member=member):
        self.assertIs(pickle.loads(pickle.dumps(member)), member)

  def test_what_a_signature_takes_in_place_of_a_member(self) -> None:
    """A number of a member, or its name, is taken as the member; a door
    number, and a number of no member, are not."""
    self.assertIs(_Direction.__cast_as__(1), _Direction.Backward)
    self.assertIs(_Direction.__cast_as__('Forward'), _Direction.Forward)
    self.assertIs(
        _Direction.__cast_as__(DoorNumber(1)), NotImplemented)
    self.assertIs(_Direction.__cast_as__(9), NotImplemented)
