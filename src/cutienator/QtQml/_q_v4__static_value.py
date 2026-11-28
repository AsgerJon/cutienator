"""
QV4::StaticValue binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4staticvalue_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::StaticValue to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class StaticValue(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::StaticValue: a plain Python object standing in
  front of one C++ QV4::StaticValue.

  C++ hands a QV4::StaticValue around as a copy, so every C++
  QV4::StaticValue behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::StaticValue that has a ritual and that Python
  can call so far, 52 names in all: 'rawValue', 'setRawValue', 'valueOffset',
  'tagOffset', 'tagValue', 'setTagValue', 'value', 'tag', 'setTag', 'int_32',
  'setInt_32', 'uint_32', 'setEmpty', 'tagBitMask', 'type', 'quickType',
  'isEmpty', 'isNull', 'isBoolean', 'isInteger', 'isNullOrUndefined',
  'isUndefined', 'isDouble', 'isNumber', 'isManagedOrUndefined', 'isManaged',
  'isIntOrBool', 'integerCompatible', 'bothDouble', 'isNaN', 'isPositiveInt',
  'doubleValue', 'setDouble', 'isInt32', 'asDouble', 'booleanValue',
  'integerValue', 'tryIntegerConversion', 'toBoolean', 'toInt32',
  'asReturnedValue', 'fromReturnedValue', 'emptyValue', 'fromBoolean',
  'fromInt32', 'undefinedValue', 'nullValue', 'fromDouble', 'fromUInt32',
  'toInteger', 'toUInt32', 'setM'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'StaticValue &QV4::StaticValue::operator=(ReturnedValue v)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'HeapBasePtr QV4::StaticValue::m() const': gives 'Heap::Base', which
    has no cute class yet.
  - Qt's 'QV4::StaticValue::~StaticValue()': the destructor: Python removes
    its C++ QV4::StaticValue by it, and has no other use for it.

  What has no ritual
  ------------------

  8 of the 68 functions Qt declares: 6 a template; 2 takes or gives a type
  that cannot be passed yet.

  What to expect
  --------------

  - The C++ QV4::StaticValue is created at the first use, not by
    'QV4::StaticValue(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::StaticValue back gives a copy the ritual made
    for Python, in a new cute QV4::StaticValue.
  - Each name of Qt's QV4::StaticValue that has no cute function yet,
    'asValue', 'data_ptr', 'm', 'movePointerBits', 'rawValueRef',
    'retrievePointerBits', 'storePointerBits', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QV4::StaticValue, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class PointerShift(CuteNum):
    """
    The enum 'QV4::StaticValue::PointerShift' of Qt, with the 3 names Qt
    gives in it.
    """

    Top1Shift = Kee[int](0)
    Upper3Shift = Kee[int](0)
    Lower5Shift = Kee[int](0)

  class QuickType(CuteNum, scoped=True):
    """
    The enum 'QV4::StaticValue::QuickType' of Qt, with the 9 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Managed = Kee[int](0)
    Empty = Kee[int](65536)
    Null = Kee[int](196608)
    Boolean = Kee[int](229376)
    Integer = Kee[int](245760)
    PlusInf = Kee[int](344064)
    MinusInf = Kee[int](2147827712)
    NaN = Kee[int](868352)
    MinusNaN = Kee[int](2148352000)

  class TagBit(CuteNum, scoped=True):
    """
    The enum 'QV4::StaticValue::TagBit' of Qt, with the 7 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    SpecialNegative = Kee[int](-2147483648)
    SpecialQNaN = Kee[int](524288)
    Special = Kee[int](262144)
    IntCompat = Kee[int](131072)
    Unmanaged = Kee[int](65536)
    IntOrBool = Kee[int](32768)
    Number = Kee[int](16384)

  class Type(CuteNum):
    """
    The enum 'QV4::StaticValue::Type' of Qt, with the 7 names Qt gives in it.
    """

    Managed_Type = Kee[int](0)
    Double_Type = Kee[int](1)
    Undefined_Type = Kee[int](2)
    Empty_Type = Kee[int](65536)
    Null_Type = Kee[int](196608)
    Boolean_Type = Kee[int](229376)
    Integer_Type = Kee[int](245760)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def valueOffset() -> int:
    """
    Calls Qt's 'int QV4::StaticValue::valueOffset()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#valueOffset
    """
    #  int QV4::StaticValue::valueOffset()
    return Rituals.call('ritual_ZN3QV411StaticValue11valueOffsetEv')

  @staticmethod
  def tagOffset() -> int:
    """
    Calls Qt's 'int QV4::StaticValue::tagOffset()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#tagOffset
    """
    #  int QV4::StaticValue::tagOffset()
    return Rituals.call('ritual_ZN3QV411StaticValue9tagOffsetEv')

  @staticmethod
  @overload(int, int)
  def tagValue(tag: int, value: int) -> int:
    """
    Calls Qt's 'quint64 QV4::StaticValue::tagValue(quint32 tag, quint32
    value)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#tagValue

    Parameters
    ----------

    tag : int
      Passed on as it is.

    value : int
      Passed on as it is.
    """
    #  quint64 QV4::StaticValue::tagValue(quint32 tag, quint32 value)
    return Rituals.call('ritual_ZN3QV411StaticValue8tagValueEjj', tag, value)

  @staticmethod
  @overload(TagBit)
  def tagBitMask(bit: TagBit) -> int:
    """
    Calls Qt's 'quint64 QV4::StaticValue::tagBitMask(TagBit bit)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#tagBitMask

    Parameters
    ----------

    bit : TagBit
      Passed on as its number.
    """
    #  quint64 QV4::StaticValue::tagBitMask(TagBit bit)
    return Rituals.call(
        'ritual_ZN3QV411StaticValue10tagBitMaskENS0_6TagBitE', bit.value,
    )

  @staticmethod
  @overload(THIS, THIS)
  def bothDouble(a: StaticValue, b: StaticValue) -> bool:
    """
    Calls Qt's 'bool QV4::StaticValue::bothDouble(StaticValue a, StaticValue
    b)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#bothDouble

    Parameters
    ----------

    a : StaticValue
      Passed on as a value: Qt reads the C++ QV4::StaticValue, which stays
      Python's own.

    b : StaticValue
      Passed on as a value: Qt reads the C++ QV4::StaticValue, which stays
      Python's own.
    """
    #  bool QV4::StaticValue::bothDouble(StaticValue a, StaticValue b)
    return Rituals.call(
        'ritual_ZN3QV411StaticValue10bothDoubleES0_S0_',
        CuteMixin._valueOf(a), CuteMixin._valueOf(b),
    )

  @staticmethod
  @overload(int)
  def fromReturnedValue(val: int) -> StaticValue:
    """
    Calls Qt's 'StaticValue QV4::StaticValue::fromReturnedValue(ReturnedValue
    val)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-staticvalue.html#fromReturnedValue

    Parameters
    ----------

    val : int
      Passed on as it is.

    Returns
    -------

    StaticValue
      A new cute QV4::StaticValue around the copy Qt gave back. Python owns
      it.
    """
    #  StaticValue QV4::StaticValue::fromReturnedValue(ReturnedValue val)
    address = Rituals.call(
        'ritual_ZN3QV411StaticValue17fromReturnedValueEy', val,
    )
    return StaticValue._cuteOwning(address)

  @staticmethod
  def emptyValue() -> StaticValue:
    """
    Calls Qt's 'StaticValue QV4::StaticValue::emptyValue()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#emptyValue

    Returns
    -------

    StaticValue
      A new cute QV4::StaticValue around the copy Qt gave back. Python owns
      it.
    """
    #  StaticValue QV4::StaticValue::emptyValue()
    address = Rituals.call('ritual_ZN3QV411StaticValue10emptyValueEv')
    return StaticValue._cuteOwning(address)

  @staticmethod
  @overload(bool)
  def fromBoolean(b: bool) -> StaticValue:
    """
    Calls Qt's 'StaticValue QV4::StaticValue::fromBoolean(bool b)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#fromBoolean

    Parameters
    ----------

    b : bool
      Passed on as it is.

    Returns
    -------

    StaticValue
      A new cute QV4::StaticValue around the copy Qt gave back. Python owns
      it.
    """
    #  StaticValue QV4::StaticValue::fromBoolean(bool b)
    address = Rituals.call('ritual_ZN3QV411StaticValue11fromBooleanEb', b)
    return StaticValue._cuteOwning(address)

  @staticmethod
  @overload(int)
  def fromInt32(i: int) -> StaticValue:
    """
    Calls Qt's 'StaticValue QV4::StaticValue::fromInt32(int i)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#fromInt32

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    StaticValue
      A new cute QV4::StaticValue around the copy Qt gave back. Python owns
      it.
    """
    #  StaticValue QV4::StaticValue::fromInt32(int i)
    address = Rituals.call('ritual_ZN3QV411StaticValue9fromInt32Ei', i)
    return StaticValue._cuteOwning(address)

  @staticmethod
  def undefinedValue() -> StaticValue:
    """
    Calls Qt's 'StaticValue QV4::StaticValue::undefinedValue()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-staticvalue.html#undefinedValue

    Returns
    -------

    StaticValue
      A new cute QV4::StaticValue around the copy Qt gave back. Python owns
      it.
    """
    #  StaticValue QV4::StaticValue::undefinedValue()
    address = Rituals.call('ritual_ZN3QV411StaticValue14undefinedValueEv')
    return StaticValue._cuteOwning(address)

  @staticmethod
  def nullValue() -> StaticValue:
    """
    Calls Qt's 'StaticValue QV4::StaticValue::nullValue()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#nullValue

    Returns
    -------

    StaticValue
      A new cute QV4::StaticValue around the copy Qt gave back. Python owns
      it.
    """
    #  StaticValue QV4::StaticValue::nullValue()
    address = Rituals.call('ritual_ZN3QV411StaticValue9nullValueEv')
    return StaticValue._cuteOwning(address)

  @staticmethod
  @overload(float)
  def fromDouble(d: float) -> StaticValue:
    """
    Calls Qt's 'StaticValue QV4::StaticValue::fromDouble(double d)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#fromDouble

    Parameters
    ----------

    d : float
      Passed on as it is.

    Returns
    -------

    StaticValue
      A new cute QV4::StaticValue around the copy Qt gave back. Python owns
      it.
    """
    #  StaticValue QV4::StaticValue::fromDouble(double d)
    address = Rituals.call('ritual_ZN3QV411StaticValue10fromDoubleEd', d)
    return StaticValue._cuteOwning(address)

  @staticmethod
  @overload(int)
  def fromUInt32(i: int) -> StaticValue:
    """
    Calls Qt's 'StaticValue QV4::StaticValue::fromUInt32(uint i)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#fromUInt32

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    StaticValue
      A new cute QV4::StaticValue around the copy Qt gave back. Python owns
      it.
    """
    #  StaticValue QV4::StaticValue::fromUInt32(uint i)
    address = Rituals.call('ritual_ZN3QV411StaticValue10fromUInt32Ej', i)
    return StaticValue._cuteOwning(address)

  @staticmethod
  @overload(float)
  def toInteger(d: float) -> float:
    """
    Calls Qt's 'double QV4::StaticValue::toInteger(double d)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#toInteger

    Parameters
    ----------

    d : float
      Passed on as it is.
    """
    #  double QV4::StaticValue::toInteger(double d)
    return Rituals.call('ritual_ZN3QV411StaticValue9toIntegerEd', d)

  @staticmethod
  @overload(float)
  def toUInt32(d: float) -> int:
    """
    Calls Qt's 'unsigned int QV4::StaticValue::toUInt32(double d)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#toUInt32

    Parameters
    ----------

    d : float
      Passed on as it is.
    """
    #  unsigned int QV4::StaticValue::toUInt32(double d)
    return Rituals.call('ritual_ZN3QV411StaticValue8toUInt32Ed', d)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::StaticValue'

  #  Qt's '~QV4::StaticValue()'. Naming it makes this a value class: Python
  #  owns every C++ QV4::StaticValue behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN3QV411StaticValueD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def rawValue(self) -> int:
    """
    Calls Qt's 'quint64 QV4::StaticValue::rawValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#rawValue
    """
    #  quint64 QV4::StaticValue::rawValue() const
    return self.uglySide.call('ritual_ZNK3QV411StaticValue8rawValueEv')

  def value(self) -> int:
    """
    Calls Qt's 'quint32 QV4::StaticValue::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#value
    """
    #  quint32 QV4::StaticValue::value() const
    return self.uglySide.call('ritual_ZNK3QV411StaticValue5valueEv')

  def tag(self) -> int:
    """
    Calls Qt's 'quint32 QV4::StaticValue::tag() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#tag
    """
    #  quint32 QV4::StaticValue::tag() const
    return self.uglySide.call('ritual_ZNK3QV411StaticValue3tagEv')

  def int_32(self) -> int:
    """
    Calls Qt's 'int QV4::StaticValue::int_32() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#int_32
    """
    #  int QV4::StaticValue::int_32() const
    return self.uglySide.call('ritual_ZNK3QV411StaticValue6int_32Ev')

  def uint_32(self) -> int:
    """
    Calls Qt's 'uint QV4::StaticValue::uint_32() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#uint_32
    """
    #  uint QV4::StaticValue::uint_32() const
    return self.uglySide.call('ritual_ZNK3QV411StaticValue7uint_32Ev')

  def type(self) -> Type:
    """
    Calls Qt's 'Type QV4::StaticValue::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QV4::StaticValue::type() const
    return StaticValue.Type(self.uglySide.call(
        'ritual_ZNK3QV411StaticValue4typeEv',
    ))

  def quickType(self) -> int:
    """
    Calls Qt's 'quint64 QV4::StaticValue::quickType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#quickType
    """
    #  quint64 QV4::StaticValue::quickType() const
    return self.uglySide.call('ritual_ZNK3QV411StaticValue9quickTypeEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QV4::StaticValue::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#isEmpty
    """
    #  bool QV4::StaticValue::isEmpty() const
    return self.uglySide.call('ritual_ZNK3QV411StaticValue7isEmptyEv')

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QV4::StaticValue::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#isNull
    """
    #  bool QV4::StaticValue::isNull() const
    return self.uglySide.call('ritual_ZNK3QV411StaticValue6isNullEv')

  def isBoolean(self) -> bool:
    """
    Calls Qt's 'bool QV4::StaticValue::isBoolean() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#isBoolean
    """
    #  bool QV4::StaticValue::isBoolean() const
    return self.uglySide.call('ritual_ZNK3QV411StaticValue9isBooleanEv')

  def isInteger(self) -> bool:
    """
    Calls Qt's 'bool QV4::StaticValue::isInteger() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#isInteger
    """
    #  bool QV4::StaticValue::isInteger() const
    return self.uglySide.call('ritual_ZNK3QV411StaticValue9isIntegerEv')

  def isNullOrUndefined(self) -> bool:
    """
    Calls Qt's 'bool QV4::StaticValue::isNullOrUndefined() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-staticvalue.html#isNullOrUndefined
    """
    #  bool QV4::StaticValue::isNullOrUndefined() const
    return self.uglySide.call(
        'ritual_ZNK3QV411StaticValue17isNullOrUndefinedEv',
    )

  def isUndefined(self) -> bool:
    """
    Calls Qt's 'bool QV4::StaticValue::isUndefined() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#isUndefined
    """
    #  bool QV4::StaticValue::isUndefined() const
    return self.uglySide.call('ritual_ZNK3QV411StaticValue11isUndefinedEv')

  def isDouble(self) -> bool:
    """
    Calls Qt's 'bool QV4::StaticValue::isDouble() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#isDouble
    """
    #  bool QV4::StaticValue::isDouble() const
    return self.uglySide.call('ritual_ZNK3QV411StaticValue8isDoubleEv')

  def isNumber(self) -> bool:
    """
    Calls Qt's 'bool QV4::StaticValue::isNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#isNumber
    """
    #  bool QV4::StaticValue::isNumber() const
    return self.uglySide.call('ritual_ZNK3QV411StaticValue8isNumberEv')

  def isManagedOrUndefined(self) -> bool:
    """
    Calls Qt's 'bool QV4::StaticValue::isManagedOrUndefined() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-staticvalue.html#isManagedOrUndefined
    """
    #  bool QV4::StaticValue::isManagedOrUndefined() const
    return self.uglySide.call(
        'ritual_ZNK3QV411StaticValue20isManagedOrUndefinedEv',
    )

  def isManaged(self) -> bool:
    """
    Calls Qt's 'bool QV4::StaticValue::isManaged() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#isManaged
    """
    #  bool QV4::StaticValue::isManaged() const
    return self.uglySide.call('ritual_ZNK3QV411StaticValue9isManagedEv')

  def isIntOrBool(self) -> bool:
    """
    Calls Qt's 'bool QV4::StaticValue::isIntOrBool() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#isIntOrBool
    """
    #  bool QV4::StaticValue::isIntOrBool() const
    return self.uglySide.call('ritual_ZNK3QV411StaticValue11isIntOrBoolEv')

  @overload()
  def integerCompatible(self) -> bool:
    """
    Calls Qt's 'bool QV4::StaticValue::integerCompatible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-staticvalue.html#integerCompatible
    """
    #  bool QV4::StaticValue::integerCompatible() const
    return self.uglySide.call(
        'ritual_ZNK3QV411StaticValue17integerCompatibleEv',
    )

  @staticmethod
  @overload(THIS, THIS)
  def integerCompatible(a: StaticValue, b: StaticValue) -> bool:
    """
    Calls Qt's 'bool QV4::StaticValue::integerCompatible(StaticValue a,
    StaticValue b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-staticvalue.html#integerCompatible

    Parameters
    ----------

    a : StaticValue
      Passed on as a value: Qt reads the C++ QV4::StaticValue, which stays
      Python's own.

    b : StaticValue
      Passed on as a value: Qt reads the C++ QV4::StaticValue, which stays
      Python's own.
    """
    #  bool QV4::StaticValue::integerCompatible(StaticValue a, StaticValue b)
    return Rituals.call(
        'ritual_ZN3QV411StaticValue17integerCompatibleES0_S0_',
        CuteMixin._valueOf(a), CuteMixin._valueOf(b),
    )

  def isNaN(self) -> bool:
    """
    Calls Qt's 'bool QV4::StaticValue::isNaN() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#isNaN
    """
    #  bool QV4::StaticValue::isNaN() const
    return self.uglySide.call('ritual_ZNK3QV411StaticValue5isNaNEv')

  def isPositiveInt(self) -> bool:
    """
    Calls Qt's 'bool QV4::StaticValue::isPositiveInt() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#isPositiveInt
    """
    #  bool QV4::StaticValue::isPositiveInt() const
    return self.uglySide.call('ritual_ZNK3QV411StaticValue13isPositiveIntEv')

  def doubleValue(self) -> float:
    """
    Calls Qt's 'double QV4::StaticValue::doubleValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#doubleValue
    """
    #  double QV4::StaticValue::doubleValue() const
    return self.uglySide.call('ritual_ZNK3QV411StaticValue11doubleValueEv')

  def asDouble(self) -> float:
    """
    Calls Qt's 'double QV4::StaticValue::asDouble() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#asDouble
    """
    #  double QV4::StaticValue::asDouble() const
    return self.uglySide.call('ritual_ZNK3QV411StaticValue8asDoubleEv')

  def booleanValue(self) -> bool:
    """
    Calls Qt's 'bool QV4::StaticValue::booleanValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#booleanValue
    """
    #  bool QV4::StaticValue::booleanValue() const
    return self.uglySide.call('ritual_ZNK3QV411StaticValue12booleanValueEv')

  def integerValue(self) -> int:
    """
    Calls Qt's 'int QV4::StaticValue::integerValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#integerValue
    """
    #  int QV4::StaticValue::integerValue() const
    return self.uglySide.call('ritual_ZNK3QV411StaticValue12integerValueEv')

  def toBoolean(self) -> bool:
    """
    Calls Qt's 'bool QV4::StaticValue::toBoolean() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#toBoolean
    """
    #  bool QV4::StaticValue::toBoolean() const
    return self.uglySide.call('ritual_ZNK3QV411StaticValue9toBooleanEv')

  @overload()
  def toInt32(self) -> int:
    """
    Calls Qt's 'int QV4::StaticValue::toInt32() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#toInt32
    """
    #  int QV4::StaticValue::toInt32() const
    return self.uglySide.call('ritual_ZNK3QV411StaticValue7toInt32Ev')

  @staticmethod
  @overload(float)
  def toInt32(d: float) -> int:
    """
    Calls Qt's 'int QV4::StaticValue::toInt32(double d)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#toInt32

    Parameters
    ----------

    d : float
      Passed on as it is.
    """
    #  int QV4::StaticValue::toInt32(double d)
    return Rituals.call('ritual_ZN3QV411StaticValue7toInt32Ed', d)

  def asReturnedValue(self) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::StaticValue::asReturnedValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-staticvalue.html#asReturnedValue
    """
    #  ReturnedValue QV4::StaticValue::asReturnedValue() const
    return self.uglySide.call(
        'ritual_ZNK3QV411StaticValue15asReturnedValueEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setRawValue(self, raw: int) -> None:
    """
    Calls Qt's 'void QV4::StaticValue::setRawValue(quint64 raw)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#setRawValue

    Parameters
    ----------

    raw : int
      Passed on as it is.
    """
    #  void QV4::StaticValue::setRawValue(quint64 raw)
    self.uglySide.call('ritual_ZN3QV411StaticValue11setRawValueEy', raw)

  @overload(int, int)
  def setTagValue(self, tag: int, value: int) -> None:
    """
    Calls Qt's 'void QV4::StaticValue::setTagValue(quint32 tag, quint32
    value)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#setTagValue

    Parameters
    ----------

    tag : int
      Passed on as it is.

    value : int
      Passed on as it is.
    """
    #  void QV4::StaticValue::setTagValue(quint32 tag, quint32 value)
    self.uglySide.call(
        'ritual_ZN3QV411StaticValue11setTagValueEjj', tag, value,
    )

  @overload(int)
  def setTag(self, tag: int) -> None:
    """
    Calls Qt's 'void QV4::StaticValue::setTag(quint32 tag)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#setTag

    Parameters
    ----------

    tag : int
      Passed on as it is.
    """
    #  void QV4::StaticValue::setTag(quint32 tag)
    self.uglySide.call('ritual_ZN3QV411StaticValue6setTagEj', tag)

  @overload(int)
  def setInt_32(self, i: int) -> None:
    """
    Calls Qt's 'void QV4::StaticValue::setInt_32(int i)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#setInt_32

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  void QV4::StaticValue::setInt_32(int i)
    self.uglySide.call('ritual_ZN3QV411StaticValue9setInt_32Ei', i)

  def setEmpty(self) -> None:
    """
    Calls Qt's 'void QV4::StaticValue::setEmpty()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#setEmpty
    """
    #  void QV4::StaticValue::setEmpty()
    self.uglySide.call('ritual_ZN3QV411StaticValue8setEmptyEv')

  @overload(float)
  def setDouble(self, d: float) -> None:
    """
    Calls Qt's 'void QV4::StaticValue::setDouble(double d)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#setDouble

    Parameters
    ----------

    d : float
      Passed on as it is.
    """
    #  void QV4::StaticValue::setDouble(double d)
    self.uglySide.call('ritual_ZN3QV411StaticValue9setDoubleEd', d)

  @overload(WAIT['QV4.Heap.Base'])
  @overload(NoneType)
  def setM(self, b: Optional[QV4.Heap.Base]) -> None:
    """
    Calls Qt's 'void QV4::StaticValue::setM(HeapBasePtr b)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#setM

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::StaticValue::setM(HeapBasePtr b)
    self.uglySide.call(
        'ritual_ZN3QV411StaticValue4setMEPNS_4Heap4BaseE',
        self._addressOf(b),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QV4::StaticValue::StaticValue()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#StaticValue
    """
    #  QV4::StaticValue::StaticValue()
    self._noteCreation(StaticValue, lambda: Rituals.call(
        'ritual_ZN3QV411StaticValueC1Ev',
    ))

  @overload(int)
  def __init__(self, val: int) -> None:
    """
    Notes what was given, for Qt's 'QV4::StaticValue::StaticValue(quint64
    val)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#StaticValue

    Parameters
    ----------

    val : int
      Passed on as it is.
    """
    #  QV4::StaticValue::StaticValue(quint64 val)
    self._noteCreation(StaticValue, lambda: Rituals.call(
        'ritual_ZN3QV411StaticValueC1Ey', val,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def isInt32(self) -> bool:
    """
    Calls Qt's 'bool QV4::StaticValue::isInt32()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#isInt32
    """
    #  bool QV4::StaticValue::isInt32()
    return self.uglySide.call('ritual_ZN3QV411StaticValue7isInt32Ev')

  @staticmethod
  @overload(float)
  def isInt32(d: float) -> bool:
    """
    Calls Qt's 'bool QV4::StaticValue::isInt32(double d)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-staticvalue.html#isInt32

    Parameters
    ----------

    d : float
      Passed on as it is.
    """
    #  bool QV4::StaticValue::isInt32(double d)
    return Rituals.call('ritual_ZN3QV411StaticValue7isInt32Ed', d)

  def tryIntegerConversion(self) -> bool:
    """
    Calls Qt's 'bool QV4::StaticValue::tryIntegerConversion()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-staticvalue.html#tryIntegerConversion
    """
    #  bool QV4::StaticValue::tryIntegerConversion()
    return self.uglySide.call(
        'ritual_ZN3QV411StaticValue20tryIntegerConversionEv',
    )

  @staticmethod
  def asValue(*__, **_) -> Never:
    """
    Qt's 'QV4::StaticValue::asValue': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QV4.StaticValue.asValue' has no cute function yet. Qt's "
        "'QV4::StaticValue::asValue': a template: a pattern and no single "
        "function.")

  @staticmethod
  def data_ptr(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue *QV4::StaticValue::data_ptr()': takes or gives a type
    that cannot be passed yet: QV4::ReturnedValue *.
    """
    raise NotImplementedError(
        "'QV4.StaticValue.data_ptr' has no cute function yet. Qt's "
        "'ReturnedValue *QV4::StaticValue::data_ptr()': takes or gives a "
        "type that cannot be passed yet: QV4::ReturnedValue *.")

  @staticmethod
  def m(*__, **_) -> Never:
    """
    Qt's 'HeapBasePtr QV4::StaticValue::m() const': gives 'Heap::Base', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.StaticValue.m' has no cute function yet. Qt's 'HeapBasePtr "
        "QV4::StaticValue::m() const': gives 'Heap::Base', which has no "
        "cute class yet.")

  @staticmethod
  def movePointerBits(*__, **_) -> Never:
    """
    Qt's 'QV4::StaticValue::movePointerBits': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QV4.StaticValue.movePointerBits' has no cute function yet. Qt's "
        "'QV4::StaticValue::movePointerBits': a template: a pattern and no "
        "single function.")

  @staticmethod
  def rawValueRef(*__, **_) -> Never:
    """
    Qt's 'quint64 &QV4::StaticValue::rawValueRef()': takes or gives a type
    that cannot be passed yet: quint64 &.
    """
    raise NotImplementedError(
        "'QV4.StaticValue.rawValueRef' has no cute function yet. Qt's "
        "'quint64 &QV4::StaticValue::rawValueRef()': takes or gives a type "
        "that cannot be passed yet: quint64 &.")

  @staticmethod
  def retrievePointerBits(*__, **_) -> Never:
    """
    Qt's 'QV4::StaticValue::retrievePointerBits': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QV4.StaticValue.retrievePointerBits' has no cute function yet. "
        "Qt's 'QV4::StaticValue::retrievePointerBits': a template: a "
        "pattern and no single function.")

  @staticmethod
  def storePointerBits(*__, **_) -> Never:
    """
    Qt's 'QV4::StaticValue::storePointerBits': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QV4.StaticValue.storePointerBits' has no cute function yet. Qt's "
        "'QV4::StaticValue::storePointerBits': a template: a pattern and no "
        "single function.")
