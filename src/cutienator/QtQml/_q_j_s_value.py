"""
QJSValue binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/qjsvalue.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QHash, QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QDateTime, QLatin1String, QMetaObject, QObject
  from ..QtCore import QVariant
  from . import QJSPrimitiveValue
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLatin1String = WAIT['QLatin1String']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QJSValue(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QJSValue: a plain Python object standing in front of
  one C++ QJSValue.

  C++ hands a QJSValue around as a copy, so every C++ QJSValue behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QJSValue that has a ritual and that Python can call
  so far, 38 names in all: 'isBool', 'isNumber', 'isNull', 'isString',
  'isUndefined', 'isVariant', 'isQObject', 'isQMetaObject', 'isObject',
  'isDate', 'isRegExp', 'isArray', 'isError', 'isUrl', 'toString',
  'toNumber', 'toInt', 'toUInt', 'toBool', 'toVariant', 'toPrimitive',
  'toQObject', 'toQMetaObject', 'toDateTime', 'equals', 'strictlyEquals',
  'prototype', 'setPrototype', 'property', 'setProperty', 'hasProperty',
  'hasOwnProperty', 'deleteProperty', 'isCallable', 'call',
  'callWithInstance', 'callAsConstructor', 'errorType'. It can be made from
  Python, in 8 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QJSValue::~QJSValue()': the destructor: Python removes its C++
    QJSValue by it, and has no other use for it.
  - Qt's 'QJSValue::QJSValue(QJSValue &&other)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QJSValue &QJSValue::operator=(QJSValue &&other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QJSValue::QJSValue(uint value)': takes in Python what
    'QJSValue::QJSValue(int value)' takes.
  - Qt's 'QJSValue &QJSValue::operator=(const QJSValue &other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QJSValue::QJSValue(QJSPrimitiveValue &&value)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QJSValue::QJSValue(QJSManagedValue &&value)': takes a type Python
    has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 57 functions Qt declares: 1 forbidden.

  What to expect
  --------------

  - The C++ QJSValue is created at the first use, not by 'QJSValue(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QJSValue back gives a copy the ritual made for
    Python, in a new cute QJSValue.
  """

  #  The enums Qt writes inside QJSValue, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class ErrorType(CuteNum):
    """
    The enum 'QJSValue::ErrorType' of Qt, with the 8 names Qt gives in it.
    """

    NoError = Kee[int](0)
    GenericError = Kee[int](1)
    EvalError = Kee[int](2)
    RangeError = Kee[int](3)
    ReferenceError = Kee[int](4)
    SyntaxError = Kee[int](5)
    TypeError = Kee[int](6)
    URIError = Kee[int](7)

  class ObjectConversionBehavior(CuteNum):
    """
    The enum 'QJSValue::ObjectConversionBehavior' of Qt, with the 2 names Qt
    gives in it.
    """

    ConvertJSObjects = Kee[int](0)
    RetainJSObjects = Kee[int](1)

  class SpecialValue(CuteNum):
    """
    The enum 'QJSValue::SpecialValue' of Qt, with the 2 names Qt gives in it.
    """

    NullValue = Kee[int](0)
    UndefinedValue = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QJSValue'

  #  Qt's '~QJSValue()'. Naming it makes this a value class: Python owns
  #  every C++ QJSValue behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8QJSValueD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isBool(self) -> bool:
    """
    Calls Qt's 'bool QJSValue::isBool() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#isBool
    """
    #  bool QJSValue::isBool() const
    return self.uglySide.call('ritual_ZNK8QJSValue6isBoolEv')

  def isNumber(self) -> bool:
    """
    Calls Qt's 'bool QJSValue::isNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#isNumber
    """
    #  bool QJSValue::isNumber() const
    return self.uglySide.call('ritual_ZNK8QJSValue8isNumberEv')

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QJSValue::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#isNull
    """
    #  bool QJSValue::isNull() const
    return self.uglySide.call('ritual_ZNK8QJSValue6isNullEv')

  def isString(self) -> bool:
    """
    Calls Qt's 'bool QJSValue::isString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#isString
    """
    #  bool QJSValue::isString() const
    return self.uglySide.call('ritual_ZNK8QJSValue8isStringEv')

  def isUndefined(self) -> bool:
    """
    Calls Qt's 'bool QJSValue::isUndefined() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#isUndefined
    """
    #  bool QJSValue::isUndefined() const
    return self.uglySide.call('ritual_ZNK8QJSValue11isUndefinedEv')

  def isVariant(self) -> bool:
    """
    Calls Qt's 'bool QJSValue::isVariant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#isVariant
    """
    #  bool QJSValue::isVariant() const
    return self.uglySide.call('ritual_ZNK8QJSValue9isVariantEv')

  def isQObject(self) -> bool:
    """
    Calls Qt's 'bool QJSValue::isQObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#isQObject
    """
    #  bool QJSValue::isQObject() const
    return self.uglySide.call('ritual_ZNK8QJSValue9isQObjectEv')

  def isQMetaObject(self) -> bool:
    """
    Calls Qt's 'bool QJSValue::isQMetaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#isQMetaObject
    """
    #  bool QJSValue::isQMetaObject() const
    return self.uglySide.call('ritual_ZNK8QJSValue13isQMetaObjectEv')

  def isObject(self) -> bool:
    """
    Calls Qt's 'bool QJSValue::isObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#isObject
    """
    #  bool QJSValue::isObject() const
    return self.uglySide.call('ritual_ZNK8QJSValue8isObjectEv')

  def isDate(self) -> bool:
    """
    Calls Qt's 'bool QJSValue::isDate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#isDate
    """
    #  bool QJSValue::isDate() const
    return self.uglySide.call('ritual_ZNK8QJSValue6isDateEv')

  def isRegExp(self) -> bool:
    """
    Calls Qt's 'bool QJSValue::isRegExp() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#isRegExp
    """
    #  bool QJSValue::isRegExp() const
    return self.uglySide.call('ritual_ZNK8QJSValue8isRegExpEv')

  def isArray(self) -> bool:
    """
    Calls Qt's 'bool QJSValue::isArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#isArray
    """
    #  bool QJSValue::isArray() const
    return self.uglySide.call('ritual_ZNK8QJSValue7isArrayEv')

  def isError(self) -> bool:
    """
    Calls Qt's 'bool QJSValue::isError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#isError
    """
    #  bool QJSValue::isError() const
    return self.uglySide.call('ritual_ZNK8QJSValue7isErrorEv')

  def isUrl(self) -> bool:
    """
    Calls Qt's 'bool QJSValue::isUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#isUrl
    """
    #  bool QJSValue::isUrl() const
    return self.uglySide.call('ritual_ZNK8QJSValue5isUrlEv')

  def toString(self) -> str:
    """
    Calls Qt's 'QString QJSValue::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QJSValue::toString() const
    return self.uglySide.call('ritual_ZNK8QJSValue8toStringEv')

  def toNumber(self) -> float:
    """
    Calls Qt's 'double QJSValue::toNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#toNumber
    """
    #  double QJSValue::toNumber() const
    return self.uglySide.call('ritual_ZNK8QJSValue8toNumberEv')

  def toInt(self) -> int:
    """
    Calls Qt's 'qint32 QJSValue::toInt() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#toInt
    """
    #  qint32 QJSValue::toInt() const
    return self.uglySide.call('ritual_ZNK8QJSValue5toIntEv')

  def toUInt(self) -> int:
    """
    Calls Qt's 'quint32 QJSValue::toUInt() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#toUInt
    """
    #  quint32 QJSValue::toUInt() const
    return self.uglySide.call('ritual_ZNK8QJSValue6toUIntEv')

  def toBool(self) -> bool:
    """
    Calls Qt's 'bool QJSValue::toBool() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#toBool
    """
    #  bool QJSValue::toBool() const
    return self.uglySide.call('ritual_ZNK8QJSValue6toBoolEv')

  @overload()
  def toVariant(self) -> QVariant:
    """
    Calls Qt's 'QVariant QJSValue::toVariant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#toVariant

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QJSValue::toVariant() const
    address = self.uglySide.call('ritual_ZNK8QJSValue9toVariantEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(ObjectConversionBehavior)
  def toVariant(self, behavior: ObjectConversionBehavior) -> QVariant:
    """
    Calls Qt's 'QVariant QJSValue::toVariant(ObjectConversionBehavior
    behavior) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#toVariant

    Parameters
    ----------

    behavior : ObjectConversionBehavior
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QJSValue::toVariant(ObjectConversionBehavior behavior) const
    address = self.uglySide.call(
        'ritual_ZNK8QJSValue9toVariantENS_24ObjectConversionBehaviorE',
        behavior.value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def toPrimitive(self) -> QJSPrimitiveValue:
    """
    Calls Qt's 'QJSPrimitiveValue QJSValue::toPrimitive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#toPrimitive

    Returns
    -------

    QJSPrimitiveValue
      A new cute QJSPrimitiveValue around the copy Qt gave back. Python owns
      it.
    """
    #  QJSPrimitiveValue QJSValue::toPrimitive() const
    address = self.uglySide.call('ritual_ZNK8QJSValue11toPrimitiveEv')
    from . import QJSPrimitiveValue
    return QJSPrimitiveValue._cuteOwning(address)

  def toQObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QJSValue::toQObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#toQObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QJSValue::toQObject() const
    address = self.uglySide.call('ritual_ZNK8QJSValue9toQObjectEv')
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def toQMetaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QJSValue::toQMetaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#toQMetaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QJSValue::toQMetaObject() const
    address = self.uglySide.call('ritual_ZNK8QJSValue13toQMetaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def toDateTime(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QJSValue::toDateTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#toDateTime

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QJSValue::toDateTime() const
    address = self.uglySide.call('ritual_ZNK8QJSValue10toDateTimeEv')
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  @overload(THIS)
  def equals(self, other: QJSValue) -> bool:
    """
    Calls Qt's 'bool QJSValue::equals(const QJSValue &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#equals

    Parameters
    ----------

    other : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  bool QJSValue::equals(const QJSValue &other) const
    return self.uglySide.call(
        'ritual_ZNK8QJSValue6equalsERKS_', self._valueOf(other),
    )

  @overload(THIS)
  def strictlyEquals(self, other: QJSValue) -> bool:
    """
    Calls Qt's 'bool QJSValue::strictlyEquals(const QJSValue &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#strictlyEquals

    Parameters
    ----------

    other : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  bool QJSValue::strictlyEquals(const QJSValue &other) const
    return self.uglySide.call(
        'ritual_ZNK8QJSValue14strictlyEqualsERKS_', self._valueOf(other),
    )

  def prototype(self) -> QJSValue:
    """
    Calls Qt's 'QJSValue QJSValue::prototype() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#prototype

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QJSValue::prototype() const
    address = self.uglySide.call('ritual_ZNK8QJSValue9prototypeEv')
    return QJSValue._cuteOwning(address)

  @overload(str)
  def property(self, name: str) -> QJSValue:
    """
    Calls Qt's 'QJSValue QJSValue::property(const QString &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#property

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QJSValue::property(const QString &name) const
    address = self.uglySide.call(
        'ritual_ZNK8QJSValue8propertyERK7QString', name,
    )
    return QJSValue._cuteOwning(address)

  @overload(int)
  def property(self, arrayIndex: int) -> QJSValue:
    """
    Calls Qt's 'QJSValue QJSValue::property(quint32 arrayIndex) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#property

    Parameters
    ----------

    arrayIndex : int
      Passed on as it is.

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QJSValue::property(quint32 arrayIndex) const
    address = self.uglySide.call(
        'ritual_ZNK8QJSValue8propertyEj', arrayIndex,
    )
    return QJSValue._cuteOwning(address)

  @overload(str)
  def hasProperty(self, name: str) -> bool:
    """
    Calls Qt's 'bool QJSValue::hasProperty(const QString &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#hasProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QJSValue::hasProperty(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK8QJSValue11hasPropertyERK7QString', name,
    )

  @overload(str)
  def hasOwnProperty(self, name: str) -> bool:
    """
    Calls Qt's 'bool QJSValue::hasOwnProperty(const QString &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#hasOwnProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QJSValue::hasOwnProperty(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK8QJSValue14hasOwnPropertyERK7QString', name,
    )

  def isCallable(self) -> bool:
    """
    Calls Qt's 'bool QJSValue::isCallable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#isCallable
    """
    #  bool QJSValue::isCallable() const
    return self.uglySide.call('ritual_ZNK8QJSValue10isCallableEv')

  @overload(QList[WAIT['QJSValue']])
  def call(self, args: QList[QJSValue]) -> QJSValue:
    """
    Calls Qt's 'QJSValue QJSValue::call(const QJSValueList &args) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#call

    Parameters
    ----------

    args : QList[QJSValue]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QJSValue::call(const QJSValueList &args) const
    address = self.uglySide.call(
        'ritual_ZNK8QJSValue4callERK5QListIS_E', self._valueOf(args),
    )
    return QJSValue._cuteOwning(address)

  @overload(THIS, QList[WAIT['QJSValue']])
  def callWithInstance(
      self,
      instance: QJSValue,
      args: QList[QJSValue],
  ) -> QJSValue:
    """
    Calls Qt's 'QJSValue QJSValue::callWithInstance(const QJSValue &instance,
    const QJSValueList &args) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#callWithInstance

    Parameters
    ----------

    instance : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.

    args : QList[QJSValue]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QJSValue::callWithInstance(const QJSValue &instance, const
    #      QJSValueList &args) const
    address = self.uglySide.call(
        'ritual_ZNK8QJSValue16callWithInstanceERKS_RK5QListIS_E',
        self._valueOf(instance), self._valueOf(args),
    )
    return QJSValue._cuteOwning(address)

  @overload(QList[WAIT['QJSValue']])
  def callAsConstructor(self, args: QList[QJSValue]) -> QJSValue:
    """
    Calls Qt's 'QJSValue QJSValue::callAsConstructor(const QJSValueList
    &args) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#callAsConstructor

    Parameters
    ----------

    args : QList[QJSValue]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QJSValue::callAsConstructor(const QJSValueList &args) const
    address = self.uglySide.call(
        'ritual_ZNK8QJSValue17callAsConstructorERK5QListIS_E',
        self._valueOf(args),
    )
    return QJSValue._cuteOwning(address)

  def errorType(self) -> ErrorType:
    """
    Calls Qt's 'ErrorType QJSValue::errorType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#errorType

    Returns
    -------

    ErrorType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ErrorType(number)' gives.
    """
    #  ErrorType QJSValue::errorType() const
    return QJSValue.ErrorType(self.uglySide.call(
        'ritual_ZNK8QJSValue9errorTypeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def setPrototype(self, prototype: QJSValue) -> None:
    """
    Calls Qt's 'void QJSValue::setPrototype(const QJSValue &prototype)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#setPrototype

    Parameters
    ----------

    prototype : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QJSValue::setPrototype(const QJSValue &prototype)
    self.uglySide.call(
        'ritual_ZN8QJSValue12setPrototypeERKS_', self._valueOf(prototype),
    )

  @overload(str, THIS)
  def setProperty(self, name: str, value: QJSValue) -> None:
    """
    Calls Qt's 'void QJSValue::setProperty(const QString &name, const
    QJSValue &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#setProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QJSValue::setProperty(const QString &name, const QJSValue &value)
    self.uglySide.call(
        'ritual_ZN8QJSValue11setPropertyERK7QStringRKS_',
        name, self._valueOf(value),
    )

  @overload(int, THIS)
  def setProperty(self, arrayIndex: int, value: QJSValue) -> None:
    """
    Calls Qt's 'void QJSValue::setProperty(quint32 arrayIndex, const QJSValue
    &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#setProperty

    Parameters
    ----------

    arrayIndex : int
      Passed on as it is.

    value : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QJSValue::setProperty(quint32 arrayIndex, const QJSValue &value)
    self.uglySide.call(
        'ritual_ZN8QJSValue11setPropertyEjRKS_',
        arrayIndex, self._valueOf(value),
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
  @overload(SpecialValue)
  def __init__(
      self,
      value: SpecialValue = SpecialValue.UndefinedValue,
  ) -> None:
    """
    Notes what was given, for Qt's 'QJSValue::QJSValue(SpecialValue value)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#QJSValue

    Parameters
    ----------

    value : SpecialValue
      Passed on as its number. May be left out, as in Qt: it is then
      SpecialValue.UndefinedValue.
    """
    #  QJSValue::QJSValue(SpecialValue value)
    self._noteCreation(QJSValue, lambda: Rituals.call(
        'ritual_ZN8QJSValueC1ENS_12SpecialValueE', value.value,
    ))

  @overload(THIS)
  def __init__(self, other: QJSValue) -> None:
    """
    Notes what was given, for Qt's 'QJSValue::QJSValue(const QJSValue
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#QJSValue

    Parameters
    ----------

    other : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  QJSValue::QJSValue(const QJSValue &other)
    self._noteCreation(QJSValue, lambda: Rituals.call(
        'ritual_ZN8QJSValueC1ERKS_', self._valueOf(other),
    ))

  @overload(bool)
  def __init__(self, value: bool) -> None:
    """
    Notes what was given, for Qt's 'QJSValue::QJSValue(bool value)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#QJSValue

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  QJSValue::QJSValue(bool value)
    self._noteCreation(QJSValue, lambda: Rituals.call(
        'ritual_ZN8QJSValueC1Eb', value,
    ))

  @overload(int)
  def __init__(self, value: int) -> None:
    """
    Notes what was given, for Qt's 'QJSValue::QJSValue(int value)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#QJSValue

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  QJSValue::QJSValue(int value)
    self._noteCreation(QJSValue, lambda: Rituals.call(
        'ritual_ZN8QJSValueC1Ei', value,
    ))

  @overload(float)
  def __init__(self, value: float) -> None:
    """
    Notes what was given, for Qt's 'QJSValue::QJSValue(double value)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#QJSValue

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  QJSValue::QJSValue(double value)
    self._noteCreation(QJSValue, lambda: Rituals.call(
        'ritual_ZN8QJSValueC1Ed', value,
    ))

  @overload(str)
  def __init__(self, value: str) -> None:
    """
    Notes what was given, for Qt's 'QJSValue::QJSValue(const QString
    &value)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#QJSValue

    Parameters
    ----------

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QJSValue::QJSValue(const QString &value)
    self._noteCreation(QJSValue, lambda: Rituals.call(
        'ritual_ZN8QJSValueC1ERK7QString', value,
    ))

  @overload(QLatin1String)
  def __init__(self, value: QLatin1String) -> None:
    """
    Notes what was given, for Qt's 'QJSValue::QJSValue(const QLatin1String
    &value)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#QJSValue

    Parameters
    ----------

    value : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  QJSValue::QJSValue(const QLatin1String &value)
    self._noteCreation(QJSValue, lambda: Rituals.call(
        'ritual_ZN8QJSValueC1ERK13QLatin1String', self._valueOf(value),
    ))

  @overload(NoneType)
  def __init__(self, str: Optional[str]) -> None:
    """
    Notes what was given, for Qt's 'QJSValue::QJSValue(const char *str)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#QJSValue

    Parameters
    ----------

    str : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  QJSValue::QJSValue(const char *str)
    self._noteCreation(QJSValue, lambda: Rituals.call(
        'ritual_ZN8QJSValueC1EPKc', self._bytesOf(str),
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

  @overload(str)
  def deleteProperty(self, name: str) -> bool:
    """
    Calls Qt's 'bool QJSValue::deleteProperty(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsvalue.html#deleteProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QJSValue::deleteProperty(const QString &name)
    return self.uglySide.call(
        'ritual_ZN8QJSValue14deletePropertyERK7QString', name,
    )


#  Qt's 'QList<QJSValue>': the list of QJSValue, which 'QList[QJSValue]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QJSValue. Qt has a name of its own for it.
QJSValueList = QList.createKind(
    QJSValue, 'value',
    name='QJSValueList',
    make='ritual_list_make_QJSValue',
    add='ritual_list_add_QJSValue',
    size='ritual_list_size_QJSValue',
    at='ritual_list_at_QJSValue',
    drop='ritual_list_drop_QJSValue',
)


#  Qt's 'QHash<QString, QJSValue>': the QHash from text to QJSValue, which
#  'QHash[str, QJSValue]' gives. It is completed here, in the file of the
#  class of its values.
QHash.createKind(
    str, QJSValue, 'value',
    make='ritual_map_make_QHash_QString_QJSValue',
    put='ritual_map_put_QHash_QString_QJSValue',
    size='ritual_map_size_QHash_QString_QJSValue',
    key='ritual_map_key_QHash_QString_QJSValue',
    value='ritual_map_value_QHash_QString_QJSValue',
    has='ritual_map_has_QHash_QString_QJSValue',
    get='ritual_map_get_QHash_QString_QJSValue',
    drop='ritual_map_drop_QHash_QString_QJSValue',
)
