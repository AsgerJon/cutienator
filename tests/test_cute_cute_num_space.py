"""
TestCuteCuteNumSpace tests 'CuteNumSpace', the namespace the body of an
enum of Qt runs in.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee
from worktoy.work_test import BaseTest

from cutienator.cute import Cute, CuteNum, CuteNumSpace


class TestCuteCuteNumSpace(BaseTest):
  """
  Tests 'CuteNumSpace': two names of one enum that differ in case only
  are two members, as Qt has them, where 'KeeSpace' would refuse the
  second.
  """

  def test_the_body_of_an_enum_runs_in_it(self) -> None:
    """'Cute' gives the body of an enum a 'CuteNumSpace'."""
    space = Cute.__prepare__('Answer', (CuteNum,))
    self.assertIsInstance(space, CuteNumSpace)

  def test_names_differing_in_case_are_two_members(self) -> None:
    """'Ok' and 'OK' are two members, each with its own number."""

    class Answer(CuteNum):
      Ok = Kee[int](1)
      OK = Kee[int](2)

    self.assertEqual((Answer.Ok.value, Answer.OK.value), (1, 2))
    self.assertIsNot(Answer.Ok, Answer.OK)

  def test_the_members_of_a_name(self) -> None:
    """The members on record at a name, as written, or none."""
    space = Cute.__prepare__('Answer', (CuteNum,))
    space['Ok'] = Kee[int](1)
    self.assertEqual(len(space.getNumsIgnoringCase('Ok')), 1)
    self.assertEqual(space.getNumsIgnoringCase('OK'), ())
    self.assertEqual(space.getNumsIgnoringCase('Gone'), ())
