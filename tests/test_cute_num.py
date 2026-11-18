"""
TestCuteNum tests 'CuteNum', the base of the enums of Qt, and 'Cute', its
metaclass.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import copy
import pickle

from worktoy.dispatch import overload
from worktoy.keenum import Kee
from worktoy.mcls import BaseObject
from worktoy.utilities import typeCast
from worktoy.waitaminute.dispatch import DispatchException
from worktoy.waitaminute.dispatch import TypeCastException
from worktoy.waitaminute.keenum import KeeDuplicate, KeeResolveError
from worktoy.waitaminute.keenum import KeeWriteOnceError
from worktoy.work_test import BaseTest

from cutienator.cute import CuteNum, CuteFlags, Cute, DoorNumber


class AspectRatioMode(CuteNum):
  """Stands in for 'Qt::AspectRatioMode'."""
  IgnoreAspectRatio = Kee[int](0)
  KeepAspectRatio = Kee[int](1)
  KeepAspectRatioByExpanding = Kee[int](2)


class EventType(CuteNum):
  """Stands in for 'QEvent::Type', which Qt opens to the programmer."""
  NULL = Kee[int](0)
  Timer = Kee[int](1)
  User = Kee[int](1000)
  MaxUser = Kee[int](65535)


class Key(CuteNum):
  """Stands in for 'Qt::Key', with two names that differ by case."""
  Key_Escape = Kee[int](0x01000000)
  Key_Dead_a = Kee[int](0x01001280)
  Key_Dead_A = Kee[int](0x01001281)


class Country(CuteNum):
  """Stands in for 'QLocale::Country': two names for one number."""
  Curacao = Kee[int](62)
  CuraSao = Kee[int](62)


class SimpleType(CuteNum):
  """Stands in for 'QCborSimpleType', whose names are words of Python."""
  FALSE = Kee[int](20)
  TRUE = Kee[int](21)
  Null = Kee[int](22)


class DialogCode(CuteNum):
  """Stands in for 'QDialog::DialogCode'."""
  Rejected = Kee[int](0)
  Accepted = Kee[int](1)


class OneFlag(CuteFlags):
  """A flags class whose flag has the number of 'Accepted'."""
  First = 0x1


class Painter(BaseObject):
  """Takes a member of 'AspectRatioMode'."""

  @overload(AspectRatioMode)
  def scale(self, mode: AspectRatioMode) -> str:
    return mode.name


class TestCuteNum(BaseTest):
  """
  Tests what an enum based on 'CuteNum' does: names as Qt writes them,
  members without a name, tolerance toward numbers, and what a
  signature naming the enum takes.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  TESTS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_names_are_written_as_qt_writes_them(self) -> None:
    """Mixed case names are members, in the order written."""
    names = [member.name for member in AspectRatioMode]
    expected = [
      'IgnoreAspectRatio',
      'KeepAspectRatio',
      'KeepAspectRatioByExpanding',
    ]
    self.assertEqual(names, expected)
    self.assertEqual(AspectRatioMode.KeepAspectRatio.value, 1)

  def test_text_names_the_root_and_the_enum(self) -> None:
    """The text of an enum says 'CuteNum', of a member its enum."""
    expected = "<CuteNum 'AspectRatioMode': 3 members>"
    self.assertEqual(str(AspectRatioMode), expected)
    member = AspectRatioMode.KeepAspectRatio
    self.assertEqual(str(member), '<AspectRatioMode>.KeepAspectRatio')

  def test_the_words_of_c_stand_in_for_those_of_python(self) -> None:
    """'NULL', 'TRUE' and 'FALSE' are names like any other."""
    self.assertEqual(EventType.NULL.value, 0)
    self.assertEqual(SimpleType.TRUE.value, 21)
    self.assertEqual(SimpleType.FALSE.value, 20)
    self.assertIsNot(SimpleType.Null, SimpleType.TRUE)

  def test_a_member_by_its_number_and_by_its_name(self) -> None:
    """Calling the enum with a number or a name gives the member."""
    keep = AspectRatioMode.KeepAspectRatio
    self.assertIs(AspectRatioMode(1), keep)
    self.assertIs(AspectRatioMode('KeepAspectRatio'), keep)
    self.assertIs(AspectRatioMode('keepaspectratio'), keep)

  def test_names_that_differ_by_case_alone(self) -> None:
    """Both are members, each found by its own name."""
    self.assertEqual(Key.Key_Dead_a.value, 0x01001280)
    self.assertEqual(Key.Key_Dead_A.value, 0x01001281)
    self.assertIs(Key('Key_Dead_a'), Key.Key_Dead_a)
    self.assertIs(Key('Key_Dead_A'), Key.Key_Dead_A)

  def test_another_case_where_one_name_fits(self) -> None:
    """A name in another case is found when only one name fits it."""
    self.assertIs(Key('key_escape'), Key.Key_Escape)
    with self.assertRaises(KeeResolveError):
      Key('KEY_DEAD_A')

  def test_the_same_name_twice_is_refused(self) -> None:
    """A body binding one name to two members is refused."""
    with self.assertRaises(KeeDuplicate):
      class Twice(CuteNum):
        One = Kee[int](1)
        One = Kee[int](2)

  def test_a_number_qt_gave_no_name_is_a_member(self) -> None:
    """Calling the enum with such a number gives a member without a
    name, and the same one every time."""
    custom = EventType(1001)
    self.assertIsInstance(custom, EventType)
    self.assertEqual(custom.value, 1001)
    self.assertIs(EventType(1001), custom)
    self.assertIs(EventType(EventType.User + 1), custom)
    self.assertIn(custom, EventType)
    self.assertEqual(str(custom), '<EventType>.1001')
    self.assertTrue(EventType.isNameless(custom))
    self.assertFalse(EventType.isNameless(EventType.Timer))

  def test_a_member_without_a_name_is_not_listed(self) -> None:
    """Going through the enum gives the members Qt named."""
    EventType(2002)
    names = [member.name for member in EventType]
    self.assertEqual(names, ['NULL', 'Timer', 'User', 'MaxUser'])
    self.assertEqual(len(EventType), 4)

  def test_the_named_stay_as_they_were(self) -> None:
    """A number Qt named still gives the named member."""
    self.assertIs(EventType(1), EventType.Timer)
    self.assertFalse(Cute.isNameless(EventType, EventType(1)))

  def test_only_a_number_gets_a_member_without_a_name(self) -> None:
    """A text, a 'bool' and a number for the root are still refused."""
    with self.assertRaises(KeeResolveError):
      EventType('nope')
    with self.assertRaises(KeeResolveError):
      EventType(True)
    with self.assertRaises(KeeResolveError):
      EventType(1.5)
    with self.assertRaises(KeeResolveError):
      CuteNum(5)

  def test_a_member_is_no_number(self) -> None:
    """A is A: a member is not an 'int'."""
    self.assertNotIsInstance(DialogCode.Accepted, int)

  def test_a_member_is_equal_to_its_number(self) -> None:
    """Tolerance: '==' answers for the number, both ways round."""
    self.assertTrue(DialogCode.Accepted == 1)
    self.assertTrue(1 == DialogCode.Accepted)
    self.assertFalse(DialogCode.Accepted == 0)
    self.assertTrue(DialogCode.Accepted != 0)
    self.assertTrue(EventType(1001) == 1001)

  def test_the_hash_follows_the_number(self) -> None:
    """A list, a set and a dictionary agree about a member."""
    accepted = DialogCode.Accepted
    self.assertEqual(hash(accepted), hash(1))
    self.assertIn(accepted, [1, 2])
    self.assertIn(accepted, {1, 2})
    self.assertEqual({accepted: 'found'}[1], 'found')
    self.assertEqual({1: 'found'}[accepted], 'found')

  def test_a_member_plus_a_number_is_a_plain_number(self) -> None:
    """Tolerance: '+' answers for the number, both ways round."""
    self.assertIs(type(EventType.User + 1), int)
    self.assertEqual(EventType.User + 1, 1001)
    self.assertEqual(1 + EventType.User, 1001)
    self.assertEqual(EventType.User + EventType.Timer, 1001)

  def test_among_members_a_is_a(self) -> None:
    """Two members are equal only when they are one."""
    accepted = DialogCode.Accepted
    self.assertTrue(accepted == accepted)
    self.assertFalse(accepted == DialogCode.Rejected)
    self.assertFalse(accepted == AspectRatioMode.KeepAspectRatio)
    self.assertFalse(Country.Curacao == Country.CuraSao)
    self.assertTrue(Country.Curacao == 62 and Country.CuraSao == 62)
    self.assertEqual(len({accepted: 1, AspectRatioMode(1): 2}), 2)

  def test_a_member_is_not_equal_to_a_value_of_flags(self) -> None:
    """A member and flags of one number are two things."""
    self.assertFalse(DialogCode.Accepted == OneFlag.First)
    self.assertFalse(OneFlag.First == DialogCode.Accepted)

  def test_what_is_no_number_of_a_member(self) -> None:
    """A 'bool', None and a text are not equal to a member."""
    accepted = DialogCode.Accepted
    self.assertFalse(accepted == True)  # noqa: E712
    self.assertFalse(accepted == None)  # noqa: E711
    self.assertFalse(accepted == 'Accepted')

  def test_order_and_minus_are_not_answered(self) -> None:
    """Tolerance covers '==' and '+', and nothing else."""
    with self.assertRaises(TypeError):
      _ = 300 >= EventType.User
    with self.assertRaises(TypeError):
      _ = EventType.User - 1

  def test_a_member_is_never_changed(self) -> None:
    """Writing to a member is refused, as worktoy refuses it."""
    with self.assertRaises(KeeWriteOnceError):
      DialogCode.Accepted.name = 'other'

  def test_a_copy_and_a_pickle_give_the_member_itself(self) -> None:
    """A named member and one without a name both come back as they
    were."""
    named, custom = EventType.Timer, EventType(3003)
    self.assertIs(copy.deepcopy(named), named)
    self.assertIs(pickle.loads(pickle.dumps(named)), named)
    self.assertIs(pickle.loads(pickle.dumps(custom)), custom)
    alias = Country.CuraSao
    self.assertIs(pickle.loads(pickle.dumps(alias)), alias)

  def test_what_a_cast_takes(self) -> None:
    """A number or a name Qt gave a name becomes the member."""
    keep = AspectRatioMode.KeepAspectRatio
    self.assertIs(typeCast(AspectRatioMode, 1), keep)
    self.assertIs(typeCast(AspectRatioMode, 'KeepAspectRatio'), keep)
    self.assertIs(typeCast(AspectRatioMode, keep), keep)

  def test_what_a_cast_refuses(self) -> None:
    """A number Qt gave no name, and one that came through a door."""
    with self.assertRaises(TypeCastException):
      typeCast(AspectRatioMode, 77)
    with self.assertRaises(TypeCastException):
      typeCast(AspectRatioMode, DoorNumber(1))
    with self.assertRaises(TypeCastException):
      typeCast(AspectRatioMode, DialogCode.Accepted)

  def test_a_signature_naming_the_enum(self) -> None:
    """It takes a member, and a number or a name Qt gave a name."""
    painter = Painter()
    keep = AspectRatioMode.KeepAspectRatio
    self.assertEqual(painter.scale(keep), 'KeepAspectRatio')
    self.assertEqual(painter.scale(1), 'KeepAspectRatio')
    self.assertEqual(painter.scale('IgnoreAspectRatio'), 'IgnoreAspectRatio')

  def test_a_number_without_a_name_is_said_out_loud(self) -> None:
    """A signature refuses it bare and takes it as a member."""
    painter = Painter()
    with self.assertRaises(DispatchException):
      painter.scale(77)
    self.assertEqual(painter.scale(AspectRatioMode(77)), '77')

  def test_a_member_of_another_enum_is_refused(self) -> None:
    """A signature naming one enum takes no member of another."""
    with self.assertRaises(DispatchException):
      Painter().scale(DialogCode.Accepted)
