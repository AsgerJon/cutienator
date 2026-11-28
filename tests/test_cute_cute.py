"""
TestCuteCute tests 'Cute', the metaclass of the enums of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee
from worktoy.waitaminute.keenum import KeeResolveError
from worktoy.work_test import BaseTest

from cutienator.cute import Cute, CuteNum


class TestCuteCute(BaseTest):
  """
  Tests 'Cute': the names of an enum, finding a member by its name in
  any case or as written, and a member Qt gave no name, as C++ allows
  any number of the enum's type.

  What to know before adding a test
  ---------------------------------

  - Each test declares its enums in its own body, as the generator
    writes them: 'Kee[int](n)' at each name.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _enum() -> type:
    """An enum with a name in two cases, and a third name."""

    class Answer(CuteNum):
      Ok = Kee[int](1)
      OK = Kee[int](2)
      Cancel = Kee[int](4)

    return Answer

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  TESTS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_it_is_the_metaclass_of_an_enum(self) -> None:
    """An enum of Qt is made by 'Cute'."""
    self.assertIsInstance(self._enum(), Cute)

  def test_the_names_of_an_enum(self) -> None:
    """Each name Qt wrote, with its member, in order."""
    Answer = self._enum()
    self.assertEqual(Answer.getShortNames(), dict(
        Ok=Answer.Ok, OK=Answer.OK, Cancel=Answer.Cancel))

  def test_a_member_by_its_name_as_written(self) -> None:
    """A name is found as written first, so two names differing in case
    give each its own member."""
    Answer = self._enum()
    self.assertIs(Answer('Ok'), Answer.Ok)
    self.assertIs(Answer('OK'), Answer.OK)

  def test_a_member_by_its_name_in_any_case(self) -> None:
    """A name no member has as written is found in any case, unless two
    members share it."""
    Answer = self._enum()
    self.assertIs(Answer('cancel'), Answer.Cancel)
    self.assertIs(Answer('CANCEL'), Answer.Cancel)
    with self.assertRaises(KeeResolveError):
      Answer('ok')

  def test_a_member_by_its_number(self) -> None:
    """A number of a member gives that member."""
    Answer = self._enum()
    self.assertIs(Answer(4), Answer.Cancel)

  def test_a_number_qt_gave_no_name(self) -> None:
    """A number no member has gives a member of its own, named as the
    number, made once; it is nameless, and a named member is not."""
    Answer = self._enum()
    five = Answer(5)
    self.assertIsInstance(five, Answer)
    self.assertEqual((five.value, five.name), (5, '5'))
    self.assertIs(Answer(5), five)
    self.assertIs(Answer.isNameless(five), True)
    self.assertIs(Answer.isNameless(Answer.Ok), False)
    self.assertNotIn(five, [*Answer])

  def test_what_is_no_number_nor_name_is_refused(self) -> None:
    """What is neither a member's name nor a whole number is refused, and
    so is a number for an enum with no members, or one of other values."""
    Answer = self._enum()
    for identifier in ('Gone', 2.5, None):
      with self.subTest(identifier=identifier):
        with self.assertRaises(KeeResolveError):
          Answer(identifier)

    class Empty(CuteNum):
      pass

    with self.assertRaises(KeeResolveError):
      Empty(3)

    class Word(CuteNum):
      Hello = Kee[str]('hello')

    with self.assertRaises(KeeResolveError):
      Word(3)

  def test_a_class_with_no_table_of_nameless_members(self) -> None:
    """A class whose table of nameless members was never made holds no
    such member; every enum 'Cute' makes has one from the start."""

    class Unmade:
      __nameless_members__ = None

    self.assertIs(Cute.isNameless(Unmade, self._enum().Ok), False)
    self.assertIsInstance(self._enum().__nameless_members__, dict)
