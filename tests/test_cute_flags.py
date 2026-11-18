"""
TestCuteFlags tests 'CuteFlags', the base of the flags enums of Qt, with
its namespace and its hook.
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
from worktoy.waitaminute.meta import ClaimedName
from worktoy.work_test import BaseTest

from cutienator.cute import CuteFlags, CuteNum, DoorNumber


class AlignmentFlag(CuteFlags):
  """Stands in for 'Qt::AlignmentFlag', written as its header."""
  AlignLeft = 0x0001
  AlignLeading = AlignLeft
  AlignRight = 0x0002
  AlignHCenter = 0x0004
  AlignHorizontal_Mask = AlignLeft | AlignRight | AlignHCenter
  AlignTop = 0x0020
  AlignVCenter = 0x0080
  AlignCenter = AlignVCenter | AlignHCenter


class KeyboardModifier(CuteFlags, number='unsigned int'):
  """Stands in for 'Qt::KeyboardModifier', which has no sign."""
  NoModifier = 0x00000000
  ShiftModifier = 0x02000000
  ControlModifier = 0x04000000
  KeyboardModifierMask = 0xfe000000


class Filter(CuteFlags):
  """Stands in for 'QDir::Filter', which holds a number below 0."""
  Dirs = 0x001
  Files = 0x002
  NoFilter = -1


class TabFeature(CuteFlags):
  """Stands in for a flags enum where Qt calls no flag 'None'."""
  NULL = 0x00
  HasFrame = 0x01


class DialogCode(CuteNum):
  """An enum whose member has the number of 'AlignLeft'."""
  Accepted = Kee[int](1)


class Label(BaseObject):
  """Takes a value of 'AlignmentFlag'."""

  @overload(AlignmentFlag)
  def setAlignment(self, alignment: AlignmentFlag) -> str:
    return str(alignment)


A, K = AlignmentFlag, KeyboardModifier


class TestCuteFlags(BaseTest):
  """
  Tests what a flags class based on 'CuteFlags' does: values made when
  asked for, the operators, 'NULL', tolerance toward numbers, and what
  a class body and a signature take and refuse.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  TESTS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_a_flag_is_a_value_of_its_class(self) -> None:
    """Each name holds a value, with its number and its name."""
    self.assertIsInstance(A.AlignLeft, A)
    self.assertEqual(A.AlignLeft.value, 1)
    self.assertEqual(A.AlignLeft.name, 'AlignLeft')
    self.assertEqual(int(A.AlignCenter), 0x84)
    self.assertEqual(str(A.AlignLeft), '<AlignmentFlag>.AlignLeft')

  def test_two_names_for_one_number_are_one_value(self) -> None:
    """The second name holds the value of the first."""
    self.assertIs(A.AlignLeading, A.AlignLeft)
    self.assertEqual(A.AlignLeading.name, 'AlignLeft')

  def test_names_of_several_bits(self) -> None:
    """A mask and a named combination hold their numbers."""
    self.assertEqual(A.AlignHorizontal_Mask.value, 0x07)
    self.assertIs(A.AlignCenter, A.AlignVCenter | A.AlignHCenter)

  def test_the_values_qt_named_are_listed_once(self) -> None:
    """Going through the class gives each named value once, in order."""
    names = [flags.name for flags in A]
    expected = [
      'AlignLeft', 'AlignRight', 'AlignHCenter', 'AlignHorizontal_Mask',
      'AlignTop', 'AlignVCenter', 'AlignCenter',
    ]
    self.assertEqual(names, expected)
    self.assertEqual(len(A), 7)

  def test_null_is_in_every_class(self) -> None:
    """'NULL' is the value of no flag, whether Qt names it or not."""
    self.assertEqual(A.NULL.value, 0)
    self.assertEqual(A.NULL.name, 'NULL')
    self.assertIs(A(), A.NULL)
    self.assertIs(K.NULL, K.NoModifier)
    self.assertEqual(K.NULL.name, 'NoModifier')
    self.assertIs(TabFeature.NULL, TabFeature())
    self.assertIs(A('NULL'), A.NULL)
    self.assertIsNot(A.NULL, K.NULL)

  def test_null_is_not_listed_unless_qt_names_it(self) -> None:
    """Only a zero that the body names is gone through."""
    self.assertNotIn('NULL', [flags.name for flags in A])
    names = [flags.name for flags in TabFeature]
    self.assertEqual(names, ['NULL', 'HasFrame'])

  def test_a_value_is_made_when_asked_for_and_kept(self) -> None:
    """One number is one object."""
    both = A.AlignLeft | A.AlignTop
    self.assertEqual(both.value, 0x21)
    self.assertIsNone(both.name)
    self.assertIs(A(0x21), both)
    self.assertIs(A.AlignTop | A.AlignLeft, both)
    self.assertEqual(str(both), '<AlignmentFlag>.AlignLeft|AlignTop')

  def test_a_bit_qt_never_named_is_kept(self) -> None:
    """Such a bit shows as a number in the text."""
    odd = A(0x200) | A.AlignLeft
    self.assertEqual(odd.value, 0x201)
    self.assertEqual(str(odd), '<AlignmentFlag>.AlignLeft|0x200')

  def test_the_operators_stay_in_the_class(self) -> None:
    """'|', '&', '^' and '~' give values of the class."""
    both = A.AlignLeft | A.AlignTop
    self.assertIs(both & A.AlignLeft, A.AlignLeft)
    self.assertIs(both ^ A.AlignTop, A.AlignLeft)
    self.assertIs(both & ~A.AlignLeft, A.AlignTop)
    self.assertIs(A.AlignLeft & A.AlignTop, A.NULL)

  def test_in_and_truth(self) -> None:
    """'in' asks for every bit; only 'NULL' is falsy."""
    both = A.AlignLeft | A.AlignTop
    self.assertIn(A.AlignTop, both)
    self.assertNotIn(A.AlignRight, both)
    self.assertNotIn(A.NULL, both)
    self.assertIn(A.NULL, A.NULL)
    self.assertTrue(both & A.AlignTop)
    self.assertFalse(both & A.AlignRight)
    self.assertFalse(A.NULL)

  def test_the_other_bits_of_a_number_without_a_sign(self) -> None:
    """'~' stays within 32 bits and above 0."""
    others = ~K.ShiftModifier
    self.assertEqual(others.value, 0xfdffffff)
    self.assertEqual(K.KeyboardModifierMask.value, 0xfe000000)
    self.assertIs(~K.NULL, K(0xffffffff))

  def test_the_other_bits_of_a_number_with_a_sign(self) -> None:
    """With a sign, every bit set is -1, as in C++."""
    self.assertEqual(Filter.NoFilter.value, -1)
    self.assertIs(~Filter.NULL, Filter.NoFilter)
    self.assertIs(Filter(0xffffffff), Filter.NoFilter)
    self.assertEqual((~Filter.Dirs).value, -2)

  def test_calling_the_class(self) -> None:
    """A number, a name, a value of the class, or nothing."""
    self.assertIs(A(1), A.AlignLeft)
    self.assertIs(A('AlignTop'), A.AlignTop)
    self.assertIs(A(A.AlignTop), A.AlignTop)
    self.assertIs(A(), A.NULL)

  def test_what_calling_the_class_refuses(self) -> None:
    """A 'bool', a name it lacks, and a value of another class."""
    with self.assertRaises(TypeError):
      A(True)
    with self.assertRaises(ValueError):
      A('Nope')
    with self.assertRaises(TypeError):
      A(K.ShiftModifier)

  def test_two_classes_and_bare_numbers_do_not_mix(self) -> None:
    """The operators take two values of one class and nothing else."""
    with self.assertRaises(TypeError):
      _ = A.AlignLeft | K.ShiftModifier
    with self.assertRaises(TypeError):
      _ = A.AlignLeft | 2
    with self.assertRaises(TypeError):
      _ = 2 & A.AlignLeft

  def test_a_value_is_no_number(self) -> None:
    """A is A: a value is not an 'int'."""
    self.assertNotIsInstance(A.AlignLeft, int)

  def test_a_value_is_equal_to_its_number(self) -> None:
    """Tolerance: '==' and '+' answer for the number."""
    both = A.AlignLeft | A.AlignTop
    self.assertTrue(both == 0x21)
    self.assertTrue(0x21 == both)
    self.assertFalse(both == 0x20)
    self.assertEqual(hash(both), hash(0x21))
    self.assertIn(both, {0x21})
    self.assertEqual({both: 'found'}[0x21], 'found')
    self.assertIs(type(both + 1), int)
    self.assertEqual(1 + both, 0x22)

  def test_among_values_a_is_a(self) -> None:
    """Values of two classes, and a value and a member, are never
    equal."""
    self.assertTrue(A.AlignLeft == A.AlignLeft)
    self.assertFalse(A.AlignLeft == A.AlignRight)
    self.assertFalse(A.NULL == K.NULL)
    self.assertFalse(A.AlignLeft == DialogCode.Accepted)
    self.assertFalse(A.AlignLeft == True)  # noqa: E712
    self.assertFalse(A.AlignLeft == None)  # noqa: E711

  def test_a_value_is_never_changed(self) -> None:
    """Neither a value nor the name of a flag on its class."""
    with self.assertRaises(AttributeError):
      A.AlignLeft.value = 5
    with self.assertRaises(AttributeError):
      del A.AlignLeft.name
    with self.assertRaises(AttributeError):
      A.AlignLeft = 5
    with self.assertRaises(AttributeError):
      del A.AlignLeft
    self.assertEqual(A.AlignLeft.value, 1)

  def test_a_copy_and_a_pickle_give_the_value_itself(self) -> None:
    """A named value and a combination both come back as they were."""
    both = A.AlignLeft | A.AlignTop
    self.assertIs(copy.copy(both), both)
    self.assertIs(copy.deepcopy(both), both)
    self.assertIs(pickle.loads(pickle.dumps(both)), both)
    self.assertIs(pickle.loads(pickle.dumps(A.AlignTop)), A.AlignTop)

  def test_is_it_a_value_of_the_class(self) -> None:
    """'in' on the class asks whether something is a value of it."""
    self.assertIn(A.AlignLeft | A.AlignTop, A)
    self.assertNotIn(K.ShiftModifier, A)
    self.assertNotIn(1, A)

  def test_a_name_twice_is_refused(self) -> None:
    """A second number for one name fails at its line."""
    with self.assertRaises(SyntaxError):
      class Twice(CuteFlags):
        One = 1
        One = 2

  def test_a_flag_and_a_plain_value_at_one_name(self) -> None:
    """Either order fails at the second line."""
    with self.assertRaises(SyntaxError):
      class PlainAfter(CuteFlags):
        One = 1
        One = 'text'
    with self.assertRaises(SyntaxError):
      class PlainBefore(CuteFlags):
        One = 'text'
        One = 1

  def test_a_flag_deleted_in_the_body_is_refused(self) -> None:
    """worktoy refuses the class as it is made."""
    with self.assertRaises(ClaimedName):
      class Deleted(CuteFlags):
        One = 1
        del One

  def test_null_is_zero(self) -> None:
    """'NULL' bound to another number fails at its line."""
    with self.assertRaises(SyntaxError):
      class WrongNull(CuteFlags):
        NULL = 1

  def test_what_is_no_flag_in_a_body(self) -> None:
    """A number under a dunder name, a 'bool' and a method stay what
    they are."""

    class Mixed(CuteFlags):
      __some_setting__ = 7
      truth = True
      One = 1

      def describe(self) -> str:
        return 'I am %s' % self

    self.assertEqual(Mixed.__some_setting__, 7)
    self.assertIs(Mixed.truth, True)
    self.assertEqual(len(Mixed), 1)
    self.assertEqual(Mixed.One.describe(), 'I am <Mixed>.One')

  def test_a_c_number_the_class_does_not_know(self) -> None:
    """The class statement fails before its body runs."""
    with self.assertRaises(ValueError):
      class Wide(CuteFlags, number='long'):
        One = 1

  def test_the_c_numbers_a_class_may_be(self) -> None:
    """How many bits, and a sign or none, decide what '~' gives."""

    class Small(CuteFlags, number='unsigned char'):
      One = 1

    class Large(CuteFlags, number='long long'):
      One = 1

    self.assertEqual((~Small.One).value, 0xfe)
    self.assertEqual((~Large.One).value, -2)
    self.assertEqual(Large(1 << 40).value, 1 << 40)

  def test_a_flags_class_is_not_built_on_another(self) -> None:
    """A class built on a flags class that has flags is refused."""
    with self.assertRaises(TypeError):
      class More(AlignmentFlag):
        Extra = 0x1000

  def test_what_a_cast_takes_and_refuses(self) -> None:
    """A number or a name Qt gave a name; no other number, and none
    that came through a door."""
    self.assertIs(typeCast(A, 0x84), A.AlignCenter)
    self.assertIs(typeCast(A, 'AlignTop'), A.AlignTop)
    self.assertIs(typeCast(A, 0), A.NULL)
    A(0x21)
    with self.assertRaises(TypeCastException):
      typeCast(A, 0x21)
    with self.assertRaises(TypeCastException):
      typeCast(A, 'Nope')
    with self.assertRaises(TypeCastException):
      typeCast(A, DoorNumber(1))
    with self.assertRaises(TypeCastException):
      typeCast(A, K.ShiftModifier)

  def test_a_signature_naming_the_class(self) -> None:
    """It takes a value, and a number or a name Qt gave a name."""
    label = Label()
    both = A.AlignLeft | A.AlignTop
    taken = label.setAlignment(A.AlignLeft)
    self.assertEqual(taken, '<AlignmentFlag>.AlignLeft')
    taken = label.setAlignment(both)
    self.assertEqual(taken, '<AlignmentFlag>.AlignLeft|AlignTop')
    taken = label.setAlignment(0x84)
    self.assertEqual(taken, '<AlignmentFlag>.AlignCenter')
    taken = label.setAlignment('AlignTop')
    self.assertEqual(taken, '<AlignmentFlag>.AlignTop')
    self.assertEqual(label.setAlignment(A.NULL), '<AlignmentFlag>.NULL')

  def test_what_a_signature_refuses(self) -> None:
    """A number Qt gave no name, and a value of another class."""
    label = Label()
    with self.assertRaises(DispatchException):
      label.setAlignment(0x40000)
    with self.assertRaises(DispatchException):
      label.setAlignment(K.ShiftModifier)
    taken = label.setAlignment(A(0x40000))
    self.assertEqual(taken, '<AlignmentFlag>.0x40000')
