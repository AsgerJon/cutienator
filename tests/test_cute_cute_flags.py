"""
TestCuteCuteFlags tests 'CuteFlags', the one base of every flags enum of
Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import copy
import pickle

from worktoy.keenum import Kee
from worktoy.waitaminute.dispatch import DispatchException
from worktoy.work_test import BaseTest

from cutienator.cute import CuteFlags, CuteNum, DoorNumber


class _Align(CuteFlags):
  """Flags of module level, as Qt's 'Qt::AlignmentFlag' is, so that
  'pickle' finds them."""
  AlignLeft = 0x1
  AlignRight = 0x2
  AlignTop = 0x20
  AlignLeading = 0x1
  AlignCenter = 0x84


class _Small(CuteFlags, number='unsigned char'):
  """Flags of an unsigned number of 8 bits."""
  First = 0x1
  Last = 0x80


class _Signed(CuteFlags, number='signed char'):
  """Flags of a signed number of 8 bits."""
  Top = 0x80


class _Mode(CuteNum):
  """An enum with a member of the number of one of '_Align'."""
  One = Kee[int](1)


class TestCuteCuteFlags(BaseTest):
  """
  Tests 'CuteFlags': the values a flags class has from its body, how a
  value is made, the class as the collection of its named values, what
  a signature takes in place of a value, and the values themselves:
  their bits, text, equality and that nothing changes them.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE CLASS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_each_name_is_a_value(self) -> None:
    """Each name of the body is a value of the class; two names of one
    number are one value, named by the first."""
    self.assertIsInstance(_Align.AlignLeft, _Align)
    self.assertIs(_Align.AlignLeading, _Align.AlignLeft)
    self.assertEqual(_Align.AlignLeft.name, 'AlignLeft')
    self.assertEqual(_Align.AlignCenter.value, 0x84)

  def test_null_is_the_value_of_no_flag(self) -> None:
    """Every flags class has 'NULL', the value 0."""
    self.assertEqual((_Align.NULL.value, _Align.NULL.name), (0, 'NULL'))
    self.assertIs(_Align(), _Align.NULL)
    self.assertIs(_Align(0), _Align.NULL)

  def test_the_number_of_the_class(self) -> None:
    """A flags class keeps the bits and the sign of its C++ number."""
    self.assertEqual((_Align.__flag_bits__, _Align.__flag_signed__),
                     (32, True))
    self.assertEqual((_Small.__flag_bits__, _Small.__flag_signed__),
                     (8, False))

  def test_flags_on_flags_are_refused(self) -> None:
    """A flags class built on one with flags of its own is refused."""
    with self.assertRaises(TypeError) as caught:

      class _More(_Align):
        AlignBottom = 0x40

    self.assertIn("'_More' is built on '_Align'", str(caught.exception))

  def test_the_class_holds_its_named_values(self) -> None:
    """The class goes through its named values, each once, in order,
    counts them, and holds each value of its own class."""
    self.assertEqual([*_Align], [
        _Align.AlignLeft, _Align.AlignRight, _Align.AlignTop,
        _Align.AlignCenter])
    self.assertEqual(len(_Align), 4)
    self.assertIn(_Align.AlignTop, _Align)
    self.assertIn(_Align(0x21), _Align)
    self.assertNotIn(0x20, _Align)
    self.assertNotIn(_Small.First, _Align)

  def test_a_flag_name_is_never_rebound(self) -> None:
    """The name of a flag cannot be bound to anything else, nor removed;
    any other name of the class can."""
    with self.assertRaises(AttributeError):
      _Align.AlignTop = 5
    with self.assertRaises(AttributeError):
      del _Align.AlignTop
    _Align.note = 'free'
    self.assertEqual(_Align.note, 'free')
    del _Align.note
    self.assertFalse(hasattr(_Align, 'note'))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  MAKING A VALUE   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_a_value_of_a_number(self) -> None:
    """Any number is a value, made once, with no name unless one was
    declared."""
    both = _Align(0x21)
    self.assertIs(_Align(0x21), both)
    self.assertIsNone(both.name)
    self.assertIs(_Align(0x2), _Align.AlignRight)

  def test_a_bool_is_no_number_of_flags(self) -> None:
    """A 'bool' is refused."""
    for number in (True, False):
      with self.subTest(number=number):
        with self.assertRaises(TypeError):
          _Align(number)

  def test_a_value_of_a_name(self) -> None:
    """A name gives its value, 'NULL' too; a name of no flag raises."""
    self.assertIs(_Align('AlignTop'), _Align.AlignTop)
    self.assertIs(_Align('NULL'), _Align.NULL)
    with self.assertRaises(ValueError) as caught:
      _Align('AlignBottom')
    self.assertIn("no flag named 'AlignBottom'", str(caught.exception))

  def test_a_value_of_the_class_is_itself(self) -> None:
    """A value handed back gives itself; one of other flags does not."""
    self.assertIs(_Align(_Align.AlignTop), _Align.AlignTop)
    with self.assertRaises((TypeError, DispatchException)):
      _Align(_Small.First)

  def test_a_value_of_no_known_kind_is_refused(self) -> None:
    """What is neither a number, a name nor a value is refused."""
    with self.assertRaises((TypeError, DispatchException)):
      _Align(1.5)

  def test_numbers_wrap_into_the_number_of_the_class(self) -> None:
    """A number is brought into the C++ number, as C++ itself does."""
    self.assertIs(_Small(0x181), _Small(0x81))
    self.assertEqual(_Small(-1).value, 0xff)
    self.assertEqual(_Signed(0x80).value, -0x80)
    self.assertIs(_Signed(0x80), _Signed.Top)
    self.assertEqual(_Align(0xffffffff).value, -1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  WHAT A SIGNATURE TAKES   # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_what_a_signature_takes_in_place_of_a_value(self) -> None:
    """A number or a name of a named value is taken as it; a door
    number, a number of no name, a name of none, or what is neither, is
    not."""
    self.assertIs(_Align.__cast_as__(0x20), _Align.AlignTop)
    self.assertIs(_Align.__cast_as__('AlignTop'), _Align.AlignTop)
    _Align(0x23)
    for value in (DoorNumber(0x20), 0x23, 0x400, 'AlignBottom', 1.0,
                  None):
      with self.subTest(value=value):
        self.assertIs(_Align.__cast_as__(value), NotImplemented)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  BITS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_bits_of_two_values(self) -> None:
    """Or, and, exclusive or and not give values of the class."""
    left, top = _Align.AlignLeft, _Align.AlignTop
    self.assertIs(left | top, _Align(0x21))
    self.assertIs((left | top) & top, top)
    self.assertIs((left | top) ^ left, top)
    self.assertIs(~_Align.NULL, _Align(-1))

  def test_bits_with_what_is_no_value_of_the_class(self) -> None:
    """Bits with a number or other flags are refused."""
    for other in (0x20, _Small.First, _Mode.One):
      with self.subTest(other=other):
        for operate in (lambda a, b: a | b, lambda a, b: a & b,
                        lambda a, b: a ^ b):
          with self.assertRaises(TypeError):
            operate(_Align.AlignLeft, other)

  def test_a_value_holds_another(self) -> None:
    """A value holds another of its class when it has each of its bits;
    'NULL' is held by 'NULL' alone; what is of another class never."""
    both = _Align.AlignLeft | _Align.AlignTop
    self.assertIn(_Align.AlignTop, both)
    self.assertNotIn(_Align.AlignRight, both)
    self.assertIn(_Align.NULL, _Align.NULL)
    self.assertNotIn(_Align.NULL, both)
    self.assertNotIn(0x1, both)

  def test_truth_and_number(self) -> None:
    """A value is true when it has a bit, and is its number as 'int'."""
    self.assertIs(bool(_Align.NULL), False)
    self.assertIs(bool(_Align.AlignTop), True)
    self.assertEqual(int(_Align.AlignCenter), 0x84)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  EQUALITY AND NUMBERS   # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_a_value_is_itself(self) -> None:
    """Among flags and members of enums, a value is equal to itself
    alone."""
    self.assertEqual(_Align.AlignLeft, _Align.AlignLeft)
    self.assertNotEqual(_Align.AlignLeft, _Small.First)
    self.assertNotEqual(_Align.AlignLeft, _Mode.One)

  def test_a_value_is_its_number(self) -> None:
    """Among numbers, a value is equal to its number, but never to a
    'bool', and hashes as its number; it adds as its number."""
    self.assertEqual(_Align.AlignTop, 0x20)
    self.assertNotEqual(_Align.AlignLeft, True)
    self.assertNotEqual(_Align.NULL, False)
    self.assertEqual(hash(_Align.AlignTop), hash(0x20))
    self.assertEqual(_Align.AlignTop + 1, 0x21)
    self.assertEqual(1 + _Align.AlignTop, 0x21)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTHING CHANGES A VALUE  # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_a_value_is_never_changed(self) -> None:
    """Setting or removing anything of a value raises."""
    with self.assertRaises(AttributeError):
      _Align.AlignTop.value = 3
    with self.assertRaises(AttributeError):
      del _Align.AlignTop.name

  def test_a_value_copied_or_stored_is_itself(self) -> None:
    """A copy, a deep copy, and a value read back from 'pickle', are the
    value itself."""
    both = _Align(0x21)
    for value in (_Align.AlignTop, both):
      with self.subTest(value=value):
        self.assertIs(copy.copy(value), value)
        self.assertIs(copy.deepcopy(value), value)
        self.assertIs(pickle.loads(pickle.dumps(value)), value)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  TEXT   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_text_of_a_value(self) -> None:
    """A named value by its name; a combination by the names of its
    single bits, and what no name covers in hexadecimal."""
    self.assertEqual(str(_Align.AlignTop), '<_Align>.AlignTop')
    self.assertEqual(repr(_Align.AlignTop), '<_Align>.AlignTop')
    self.assertEqual(str(_Align(0x21)), '<_Align>.AlignLeft|AlignTop')
    self.assertEqual(str(_Align(0x1100)), '<_Align>.0x1100')
    self.assertEqual(
        str(_Align(0x123)), '<_Align>.AlignLeft|AlignRight|AlignTop|0x100')
    self.assertEqual(str(_Signed(-1)), '<_Signed>.Top|0x7f')
