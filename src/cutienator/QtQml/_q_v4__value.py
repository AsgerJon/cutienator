"""
QV4::Value binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4value_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QV4::Value to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Value(QV4.StaticValue):
  """
  The cute side of Qt's QV4::Value: a plain Python object standing in front
  of one C++ QV4::Value.

  It is built on the cute 'QV4::StaticValue', as Qt's QV4::Value is built on
  Qt's QV4::StaticValue, and has everything that class has.

  C++ hands a QV4::Value around as a copy, so every C++ QV4::Value behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::Value that has a ritual and that Python can
  call so far, 40 names in all: 'fromStaticValue', 'undefined', 'isString',
  'isStringOrSymbol', 'isSymbol', 'isObject', 'isFunctionObject',
  'stringValue', 'stringOrSymbolValue', 'symbolValue', 'objectValue',
  'fromHeapObject', 'toUInt16', 'toInt32', 'toUInt32', 'toLength', 'toIndex',
  'toBoolean', 'toBooleanImpl', 'toInteger', 'convertedToNumber', 'toNumber',
  'toNumberImpl', 'toQStringNoThrow', 'toQString', 'toString',
  'toPropertyKey', 'toObject', 'isPrimitive', 'fromReturnedValue',
  'sameValue', 'sameValueZero', 'mark', 'emptyValue', 'fromBoolean',
  'fromInt32', 'undefinedValue', 'nullValue', 'fromDouble', 'fromUInt32'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'ManagedPtr QV4::Value::managed() const': gives 'Managed', which has
    no cute class yet.
  - Qt's 'QString QV4::Value::toQString(bool *ok) const': takes a number to
    change where it is.
  - Qt's 'uint QV4::Value::asArrayLength(bool *ok) const': takes a number to
    change where it is.
  - Qt's 'Value &QV4::Value::operator=(const ScopedValue &v)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'Value &QV4::Value::operator=(ReturnedValue v)': assignment: Python
    binds a name and has no operator for it.
  - Qt's 'Value &QV4::Value::operator=(ManagedPtr m)': assignment: Python
    binds a name and has no operator for it.
  - Qt's 'Value &QV4::Value::operator=(HeapBasePtr o)': assignment: Python
    binds a name and has no operator for it.
  - Qt's 'QV4::Value::~Value()': the destructor: Python removes its C++
    QV4::Value by it, and has no other use for it.

  What has no ritual
  ------------------

  6 of the 60 functions Qt declares: 5 a template; 1 the compiler refuses its
  ritual as it would be written here.

  What to expect
  --------------

  - The C++ QV4::Value is created at the first use, not by 'QV4::Value(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::Value back gives a copy the ritual made for
    Python, in a new cute QV4::Value.
  - Each name of Qt's QV4::Value that has no cute function yet,
    'asArrayLength', 'as_', 'cast', 'heapObject', 'managed', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QV4.StaticValue)
  def fromStaticValue(staticValue: QV4.StaticValue) -> Value:
    """
    Calls Qt's 'Value QV4::Value::fromStaticValue(StaticValue staticValue)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#fromStaticValue

    Parameters
    ----------

    staticValue : QV4.StaticValue
      Passed on as a value: Qt reads the C++ QV4::StaticValue, which stays
      Python's own.

    Returns
    -------

    Value
      A new cute QV4::Value around the copy Qt gave back. Python owns it.
    """
    #  Value QV4::Value::fromStaticValue(StaticValue staticValue)
    address = Rituals.call(
        'ritual_ZN3QV45Value15fromStaticValueENS_11StaticValueE',
        CuteMixin._valueOf(staticValue),
    )
    return Value._cuteOwning(address)

  @staticmethod
  def undefined() -> Value:
    """
    Calls Qt's 'Value QV4::Value::undefined()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#undefined

    Returns
    -------

    Value
      A new cute QV4::Value around the copy Qt gave back. Python owns it.
    """
    #  Value QV4::Value::undefined()
    address = Rituals.call('ritual_ZN3QV45Value9undefinedEv')
    return Value._cuteOwning(address)

  @staticmethod
  @overload(WAIT['QV4.Heap.Base'])
  @overload(NoneType)
  def fromHeapObject(m: Optional[QV4.Heap.Base]) -> Value:
    """
    Calls Qt's 'Value QV4::Value::fromHeapObject(HeapBasePtr m)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#fromHeapObject

    Parameters
    ----------

    m : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Value
      A new cute QV4::Value around the copy Qt gave back. Python owns it.
    """
    #  Value QV4::Value::fromHeapObject(HeapBasePtr m)
    address = Rituals.call(
        'ritual_ZN3QV45Value14fromHeapObjectEPNS_4Heap4BaseE',
        CuteMixin._addressOf(m),
    )
    return Value._cuteOwning(address)

  @staticmethod
  @overload(THIS)
  def toBooleanImpl(val: Value) -> bool:
    """
    Calls Qt's 'bool QV4::Value::toBooleanImpl(Value val)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#toBooleanImpl

    Parameters
    ----------

    val : Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  bool QV4::Value::toBooleanImpl(Value val)
    return Rituals.call(
        'ritual_ZN3QV45Value13toBooleanImplES0_', CuteMixin._valueOf(val),
    )

  @staticmethod
  @overload(THIS)
  def toNumberImpl(v: Value) -> float:
    """
    Calls Qt's 'double QV4::Value::toNumberImpl(Value v)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#toNumberImpl

    Parameters
    ----------

    v : Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  double QV4::Value::toNumberImpl(Value v)
    return Rituals.call(
        'ritual_ZN3QV45Value12toNumberImplES0_', CuteMixin._valueOf(v),
    )

  @overload()
  def toNumberImpl(self) -> float:
    """
    Calls Qt's 'double QV4::Value::toNumberImpl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#toNumberImpl
    """
    #  double QV4::Value::toNumberImpl() const
    return self.uglySide.call('ritual_ZNK3QV45Value12toNumberImplEv')

  @staticmethod
  @overload(int)
  def fromReturnedValue(val: int) -> Value:
    """
    Calls Qt's 'Value QV4::Value::fromReturnedValue(ReturnedValue val)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#fromReturnedValue

    Parameters
    ----------

    val : int
      Passed on as it is.

    Returns
    -------

    Value
      A new cute QV4::Value around the copy Qt gave back. Python owns it.
    """
    #  Value QV4::Value::fromReturnedValue(ReturnedValue val)
    address = Rituals.call('ritual_ZN3QV45Value17fromReturnedValueEy', val)
    return Value._cuteOwning(address)

  @staticmethod
  def emptyValue() -> Value:
    """
    Calls Qt's 'Value QV4::Value::emptyValue()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#emptyValue

    Returns
    -------

    Value
      A new cute QV4::Value around the copy Qt gave back. Python owns it.
    """
    #  Value QV4::Value::emptyValue()
    address = Rituals.call('ritual_ZN3QV45Value10emptyValueEv')
    return Value._cuteOwning(address)

  @staticmethod
  @overload(bool)
  def fromBoolean(b: bool) -> Value:
    """
    Calls Qt's 'Value QV4::Value::fromBoolean(bool b)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#fromBoolean

    Parameters
    ----------

    b : bool
      Passed on as it is.

    Returns
    -------

    Value
      A new cute QV4::Value around the copy Qt gave back. Python owns it.
    """
    #  Value QV4::Value::fromBoolean(bool b)
    address = Rituals.call('ritual_ZN3QV45Value11fromBooleanEb', b)
    return Value._cuteOwning(address)

  @staticmethod
  @overload(int)
  def fromInt32(i: int) -> Value:
    """
    Calls Qt's 'Value QV4::Value::fromInt32(int i)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#fromInt32

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    Value
      A new cute QV4::Value around the copy Qt gave back. Python owns it.
    """
    #  Value QV4::Value::fromInt32(int i)
    address = Rituals.call('ritual_ZN3QV45Value9fromInt32Ei', i)
    return Value._cuteOwning(address)

  @staticmethod
  def undefinedValue() -> Value:
    """
    Calls Qt's 'Value QV4::Value::undefinedValue()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#undefinedValue

    Returns
    -------

    Value
      A new cute QV4::Value around the copy Qt gave back. Python owns it.
    """
    #  Value QV4::Value::undefinedValue()
    address = Rituals.call('ritual_ZN3QV45Value14undefinedValueEv')
    return Value._cuteOwning(address)

  @staticmethod
  def nullValue() -> Value:
    """
    Calls Qt's 'Value QV4::Value::nullValue()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#nullValue

    Returns
    -------

    Value
      A new cute QV4::Value around the copy Qt gave back. Python owns it.
    """
    #  Value QV4::Value::nullValue()
    address = Rituals.call('ritual_ZN3QV45Value9nullValueEv')
    return Value._cuteOwning(address)

  @staticmethod
  @overload(float)
  def fromDouble(d: float) -> Value:
    """
    Calls Qt's 'Value QV4::Value::fromDouble(double d)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#fromDouble

    Parameters
    ----------

    d : float
      Passed on as it is.

    Returns
    -------

    Value
      A new cute QV4::Value around the copy Qt gave back. Python owns it.
    """
    #  Value QV4::Value::fromDouble(double d)
    address = Rituals.call('ritual_ZN3QV45Value10fromDoubleEd', d)
    return Value._cuteOwning(address)

  @staticmethod
  @overload(int)
  def fromUInt32(i: int) -> Value:
    """
    Calls Qt's 'Value QV4::Value::fromUInt32(uint i)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#fromUInt32

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    Value
      A new cute QV4::Value around the copy Qt gave back. Python owns it.
    """
    #  Value QV4::Value::fromUInt32(uint i)
    address = Rituals.call('ritual_ZN3QV45Value10fromUInt32Ej', i)
    return Value._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Value'

  #  Qt's '~QV4::Value()'. Naming it makes this a value class: Python owns
  #  every C++ QV4::Value behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV45ValueD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isString(self) -> bool:
    """
    Calls Qt's 'bool QV4::Value::isString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#isString
    """
    #  bool QV4::Value::isString() const
    return self.uglySide.call('ritual_ZNK3QV45Value8isStringEv')

  def isStringOrSymbol(self) -> bool:
    """
    Calls Qt's 'bool QV4::Value::isStringOrSymbol() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#isStringOrSymbol
    """
    #  bool QV4::Value::isStringOrSymbol() const
    return self.uglySide.call('ritual_ZNK3QV45Value16isStringOrSymbolEv')

  def isSymbol(self) -> bool:
    """
    Calls Qt's 'bool QV4::Value::isSymbol() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#isSymbol
    """
    #  bool QV4::Value::isSymbol() const
    return self.uglySide.call('ritual_ZNK3QV45Value8isSymbolEv')

  def isObject(self) -> bool:
    """
    Calls Qt's 'bool QV4::Value::isObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#isObject
    """
    #  bool QV4::Value::isObject() const
    return self.uglySide.call('ritual_ZNK3QV45Value8isObjectEv')

  def isFunctionObject(self) -> bool:
    """
    Calls Qt's 'bool QV4::Value::isFunctionObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#isFunctionObject
    """
    #  bool QV4::Value::isFunctionObject() const
    return self.uglySide.call('ritual_ZNK3QV45Value16isFunctionObjectEv')

  def stringValue(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::Value::stringValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#stringValue

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::Value::stringValue() const
    address = self.uglySide.call('ritual_ZNK3QV45Value11stringValueEv')
    return QV4.String._cuteAt(address)

  def stringOrSymbolValue(self) -> Optional[QV4.StringOrSymbol]:
    """
    Calls Qt's 'StringOrSymbol *QV4::Value::stringOrSymbolValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#stringOrSymbolValue

    Returns
    -------

    Optional[QV4.StringOrSymbol]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  StringOrSymbol *QV4::Value::stringOrSymbolValue() const
    address = self.uglySide.call(
        'ritual_ZNK3QV45Value19stringOrSymbolValueEv',
    )
    return QV4.StringOrSymbol._cuteAt(address)

  def symbolValue(self) -> Optional[QV4.Symbol]:
    """
    Calls Qt's 'Symbol *QV4::Value::symbolValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#symbolValue

    Returns
    -------

    Optional[QV4.Symbol]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Symbol *QV4::Value::symbolValue() const
    address = self.uglySide.call('ritual_ZNK3QV45Value11symbolValueEv')
    return QV4.Symbol._cuteAt(address)

  def objectValue(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::Value::objectValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#objectValue

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::Value::objectValue() const
    address = self.uglySide.call('ritual_ZNK3QV45Value11objectValueEv')
    return QV4.Object._cuteAt(address)

  def toUInt16(self) -> int:
    """
    Calls Qt's 'int QV4::Value::toUInt16() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#toUInt16
    """
    #  int QV4::Value::toUInt16() const
    return self.uglySide.call('ritual_ZNK3QV45Value8toUInt16Ev')

  @overload()
  def toInt32(self) -> int:
    """
    Calls Qt's 'int QV4::Value::toInt32() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#toInt32
    """
    #  int QV4::Value::toInt32() const
    return self.uglySide.call('ritual_ZNK3QV45Value7toInt32Ev')

  @staticmethod
  @overload(float)
  def toInt32(d: float) -> int:
    """
    Calls Qt's 'int QV4::Value::toInt32(double d)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#toInt32

    Parameters
    ----------

    d : float
      Passed on as it is.
    """
    #  int QV4::Value::toInt32(double d)
    return Rituals.call('ritual_ZN3QV45Value7toInt32Ed', d)

  @overload()
  def toUInt32(self) -> int:
    """
    Calls Qt's 'unsigned int QV4::Value::toUInt32() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#toUInt32
    """
    #  unsigned int QV4::Value::toUInt32() const
    return self.uglySide.call('ritual_ZNK3QV45Value8toUInt32Ev')

  @staticmethod
  @overload(float)
  def toUInt32(d: float) -> int:
    """
    Calls Qt's 'unsigned int QV4::Value::toUInt32(double d)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#toUInt32

    Parameters
    ----------

    d : float
      Passed on as it is.
    """
    #  unsigned int QV4::Value::toUInt32(double d)
    return Rituals.call('ritual_ZN3QV45Value8toUInt32Ed', d)

  def toLength(self) -> int:
    """
    Calls Qt's 'qint64 QV4::Value::toLength() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#toLength
    """
    #  qint64 QV4::Value::toLength() const
    return self.uglySide.call('ritual_ZNK3QV45Value8toLengthEv')

  def toIndex(self) -> int:
    """
    Calls Qt's 'qint64 QV4::Value::toIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#toIndex
    """
    #  qint64 QV4::Value::toIndex() const
    return self.uglySide.call('ritual_ZNK3QV45Value7toIndexEv')

  def toBoolean(self) -> bool:
    """
    Calls Qt's 'bool QV4::Value::toBoolean() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#toBoolean
    """
    #  bool QV4::Value::toBoolean() const
    return self.uglySide.call('ritual_ZNK3QV45Value9toBooleanEv')

  @overload()
  def toInteger(self) -> float:
    """
    Calls Qt's 'double QV4::Value::toInteger() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#toInteger
    """
    #  double QV4::Value::toInteger() const
    return self.uglySide.call('ritual_ZNK3QV45Value9toIntegerEv')

  @staticmethod
  @overload(float)
  def toInteger(d: float) -> float:
    """
    Calls Qt's 'double QV4::Value::toInteger(double d)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#toInteger

    Parameters
    ----------

    d : float
      Passed on as it is.
    """
    #  double QV4::Value::toInteger(double d)
    return Rituals.call('ritual_ZN3QV45Value9toIntegerEd', d)

  def convertedToNumber(self) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Value::convertedToNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#convertedToNumber
    """
    #  ReturnedValue QV4::Value::convertedToNumber() const
    return self.uglySide.call('ritual_ZNK3QV45Value17convertedToNumberEv')

  def toNumber(self) -> float:
    """
    Calls Qt's 'double QV4::Value::toNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#toNumber
    """
    #  double QV4::Value::toNumber() const
    return self.uglySide.call('ritual_ZNK3QV45Value8toNumberEv')

  def toQStringNoThrow(self) -> str:
    """
    Calls Qt's 'QString QV4::Value::toQStringNoThrow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#toQStringNoThrow

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::Value::toQStringNoThrow() const
    return self.uglySide.call('ritual_ZNK3QV45Value16toQStringNoThrowEv')

  def toQString(self) -> str:
    """
    Calls Qt's 'QString QV4::Value::toQString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#toQString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::Value::toQString() const
    return self.uglySide.call('ritual_ZNK3QV45Value9toQStringEv')

  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def toString(
      self,
      e: Optional[QV4.ExecutionEngine],
  ) -> Optional[QV4.Heap.String]:
    """
    Calls Qt's 'Heap::String *QV4::Value::toString(ExecutionEngine *e)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#toString

    Parameters
    ----------

    e : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::String *QV4::Value::toString(ExecutionEngine *e) const
    address = self.uglySide.call(
        'ritual_ZNK3QV45Value8toStringEPNS_15ExecutionEngineE',
        self._addressOf(e),
    )
    return QV4.Heap.String._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], THIS)
  @overload(NoneType, THIS)
  def toString(
      e: Optional[QV4.ExecutionEngine],
      val: Value,
  ) -> Optional[QV4.Heap.String]:
    """
    Calls Qt's 'Heap::String *QV4::Value::toString(ExecutionEngine *e, Value
    val)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#toString

    Parameters
    ----------

    e : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    val : Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    Returns
    -------

    Optional[QV4.Heap.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::String *QV4::Value::toString(ExecutionEngine *e, Value val)
    address = Rituals.call(
        'ritual_ZN3QV45Value8toStringEPNS_15ExecutionEngineES0_',
        CuteMixin._addressOf(e), CuteMixin._valueOf(val),
    )
    return QV4.Heap.String._cuteAt(address)

  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def toPropertyKey(
      self,
      e: Optional[QV4.ExecutionEngine],
  ) -> QV4.PropertyKey:
    """
    Calls Qt's 'QV4::PropertyKey QV4::Value::toPropertyKey(ExecutionEngine
    *e) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#toPropertyKey

    Parameters
    ----------

    e : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QV4.PropertyKey
      A new cute QV4::PropertyKey around the copy Qt gave back. Python owns
      it.
    """
    #  QV4::PropertyKey QV4::Value::toPropertyKey(ExecutionEngine *e) const
    address = self.uglySide.call(
        'ritual_ZNK3QV45Value13toPropertyKeyEPNS_15ExecutionEngineE',
        self._addressOf(e),
    )
    return QV4.PropertyKey._cuteOwning(address)

  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def toObject(
      self,
      e: Optional[QV4.ExecutionEngine],
  ) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'Heap::Object *QV4::Value::toObject(ExecutionEngine *e)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#toObject

    Parameters
    ----------

    e : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Object *QV4::Value::toObject(ExecutionEngine *e) const
    address = self.uglySide.call(
        'ritual_ZNK3QV45Value8toObjectEPNS_15ExecutionEngineE',
        self._addressOf(e),
    )
    return QV4.Heap.Object._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], THIS)
  @overload(NoneType, THIS)
  def toObject(
      e: Optional[QV4.ExecutionEngine],
      val: Value,
  ) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'Heap::Object *QV4::Value::toObject(ExecutionEngine *e, Value
    val)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#toObject

    Parameters
    ----------

    e : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    val : Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Object *QV4::Value::toObject(ExecutionEngine *e, Value val)
    address = Rituals.call(
        'ritual_ZN3QV45Value8toObjectEPNS_15ExecutionEngineES0_',
        CuteMixin._addressOf(e), CuteMixin._valueOf(val),
    )
    return QV4.Heap.Object._cuteAt(address)

  def isPrimitive(self) -> bool:
    """
    Calls Qt's 'bool QV4::Value::isPrimitive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#isPrimitive
    """
    #  bool QV4::Value::isPrimitive() const
    return self.uglySide.call('ritual_ZNK3QV45Value11isPrimitiveEv')

  @overload(THIS)
  def sameValue(self, other: Value) -> bool:
    """
    Calls Qt's 'bool QV4::Value::sameValue(Value other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#sameValue

    Parameters
    ----------

    other : Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  bool QV4::Value::sameValue(Value other) const
    return self.uglySide.call(
        'ritual_ZNK3QV45Value9sameValueES0_', self._valueOf(other),
    )

  @overload(THIS)
  def sameValueZero(self, other: Value) -> bool:
    """
    Calls Qt's 'bool QV4::Value::sameValueZero(Value other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#sameValueZero

    Parameters
    ----------

    other : Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  bool QV4::Value::sameValueZero(Value other) const
    return self.uglySide.call(
        'ritual_ZNK3QV45Value13sameValueZeroES0_', self._valueOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload(WAIT['QV4.MarkStack'])
  @overload(NoneType)
  def mark(self, markStack: Optional[QV4.MarkStack]) -> None:
    """
    Calls Qt's 'void QV4::Value::mark(MarkStack *markStack)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-value.html#mark

    Parameters
    ----------

    markStack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Value::mark(MarkStack *markStack)
    self.uglySide.call(
        'ritual_ZN3QV45Value4markEPNS_9MarkStackE',
        self._addressOf(markStack),
    )

  @staticmethod
  def asArrayLength(*__, **_) -> Never:
    """
    Qt's 'uint QV4::Value::asArrayLength(bool *ok) const': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QV4.Value.asArrayLength' has no cute function yet. Qt's 'uint "
        "QV4::Value::asArrayLength(bool *ok) const': takes a number to "
        "change where it is.")

  @staticmethod
  def as_(*__, **_) -> Never:
    """
    Qt's 'QV4::Value::as': a template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QV4.Value.as_' has no cute function yet. Qt's 'QV4::Value::as': a "
        "template: a pattern and no single function.")

  @staticmethod
  def cast(*__, **_) -> Never:
    """
    Qt's 'QV4::Value::cast': a template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QV4.Value.cast' has no cute function yet. Qt's "
        "'QV4::Value::cast': a template: a pattern and no single function.")

  @staticmethod
  def heapObject(*__, **_) -> Never:
    """
    Qt's 'Value::HeapBasePtr QV4::Value::heapObject() const': the compiler
    refuses its ritual as it would be written here: use of undeclared
    identifier 'Value'.
    """
    raise NotImplementedError(
        "'QV4.Value.heapObject' has no cute function yet. Qt's "
        "'Value::HeapBasePtr QV4::Value::heapObject() const': the compiler "
        "refuses its ritual as it would be written here: use of undeclared "
        "identifier 'Value'.")

  @staticmethod
  def managed(*__, **_) -> Never:
    """
    Qt's 'ManagedPtr QV4::Value::managed() const': gives 'Managed', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.Value.managed' has no cute function yet. Qt's 'ManagedPtr "
        "QV4::Value::managed() const': gives 'Managed', which has no cute "
        "class yet.")
