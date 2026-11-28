"""
QJSManagedValue binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/qjsmanagedvalue.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QStringList
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDateTime, QMetaObject, QObject, QRegularExpression
  from ..QtCore import QUrl, QVariant
  from . import QJSEngine, QJSPrimitiveValue, QJSValue
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJSEngine = WAIT['QJSEngine']
  QJSPrimitiveValue = WAIT['QJSPrimitiveValue']
  QJSValue = WAIT['QJSValue']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QJSManagedValue(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QJSManagedValue: a plain Python object standing in
  front of one C++ QJSManagedValue.

  What exists
  -----------

  Every function of Qt's QJSManagedValue that has a ritual and that Python
  can call so far, 41 names in all: 'engine', 'type', 'isUndefined',
  'isBoolean', 'isNumber', 'isString', 'isObject', 'isSymbol', 'isFunction',
  'isInteger', 'isNull', 'isRegularExpression', 'isArray', 'isUrl',
  'isVariant', 'isQObject', 'isQMetaObject', 'isDate', 'isError',
  'isJsMetaType', 'toString', 'toNumber', 'toBoolean', 'toPrimitive',
  'toJSValue', 'toVariant', 'toInteger', 'toRegularExpression', 'toUrl',
  'toQObject', 'toQMetaObject', 'toDateTime', 'hasProperty',
  'hasOwnProperty', 'property', 'setProperty', 'deleteProperty', 'call',
  'callWithInstance', 'callAsConstructor', 'jsMetaMembers'. It can be made
  from Python, in 6 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QJSManagedValue::~QJSManagedValue()': the destructor: Python never
    removes a C++ QJSManagedValue.
  - Qt's 'QJSManagedValue::QJSManagedValue(QJSManagedValue &&other)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QJSManagedValue &QJSManagedValue::operator=(QJSManagedValue
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'bool QJSManagedValue::equals(const QJSManagedValue &other) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'bool QJSManagedValue::strictlyEquals(const QJSManagedValue &other)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'QJSManagedValue QJSManagedValue::prototype() const': gives a type
    Python has no way to take yet.
  - Qt's 'void QJSManagedValue::setPrototype(const QJSManagedValue
    &prototype)': takes a type Python has no way to hand over yet.
  - Qt's 'QJSManagedValue QJSManagedValue::jsMetaType() const': gives a type
    Python has no way to take yet.
  - Qt's 'QJSManagedValue QJSManagedValue::jsMetaInstantiate(const
    QJSValueList &values) const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 63 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QJSManagedValue is created at the first use, not by
    'QJSManagedValue(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QJSManagedValue.
  - Each name of Qt's QJSManagedValue that has no cute function yet,
    'equals', 'jsMetaInstantiate', 'jsMetaType', 'prototype', 'setPrototype',
    'strictlyEquals', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QJSManagedValue, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum):
    """
    The enum 'QJSManagedValue::Type' of Qt, with the 7 names Qt gives in it.
    """

    Undefined = Kee[int](0)
    Boolean = Kee[int](1)
    Number = Kee[int](2)
    String = Kee[int](3)
    Object = Kee[int](4)
    Symbol = Kee[int](5)
    Function = Kee[int](6)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QJSManagedValue'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def engine(self) -> Optional[QJSEngine]:
    """
    Calls Qt's 'QJSEngine *QJSManagedValue::engine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#engine

    Returns
    -------

    Optional[QJSEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QJSEngine *QJSManagedValue::engine() const
    address = self.uglySide.call('ritual_ZNK15QJSManagedValue6engineEv')
    from . import QJSEngine
    return QJSEngine._cuteAt(address)

  def type(self) -> Type:
    """
    Calls Qt's 'Type QJSManagedValue::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QJSManagedValue::type() const
    return QJSManagedValue.Type(self.uglySide.call(
        'ritual_ZNK15QJSManagedValue4typeEv',
    ))

  def isUndefined(self) -> bool:
    """
    Calls Qt's 'bool QJSManagedValue::isUndefined() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#isUndefined
    """
    #  bool QJSManagedValue::isUndefined() const
    return self.uglySide.call('ritual_ZNK15QJSManagedValue11isUndefinedEv')

  def isBoolean(self) -> bool:
    """
    Calls Qt's 'bool QJSManagedValue::isBoolean() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#isBoolean
    """
    #  bool QJSManagedValue::isBoolean() const
    return self.uglySide.call('ritual_ZNK15QJSManagedValue9isBooleanEv')

  def isNumber(self) -> bool:
    """
    Calls Qt's 'bool QJSManagedValue::isNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#isNumber
    """
    #  bool QJSManagedValue::isNumber() const
    return self.uglySide.call('ritual_ZNK15QJSManagedValue8isNumberEv')

  def isString(self) -> bool:
    """
    Calls Qt's 'bool QJSManagedValue::isString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#isString
    """
    #  bool QJSManagedValue::isString() const
    return self.uglySide.call('ritual_ZNK15QJSManagedValue8isStringEv')

  def isObject(self) -> bool:
    """
    Calls Qt's 'bool QJSManagedValue::isObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#isObject
    """
    #  bool QJSManagedValue::isObject() const
    return self.uglySide.call('ritual_ZNK15QJSManagedValue8isObjectEv')

  def isSymbol(self) -> bool:
    """
    Calls Qt's 'bool QJSManagedValue::isSymbol() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#isSymbol
    """
    #  bool QJSManagedValue::isSymbol() const
    return self.uglySide.call('ritual_ZNK15QJSManagedValue8isSymbolEv')

  def isFunction(self) -> bool:
    """
    Calls Qt's 'bool QJSManagedValue::isFunction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#isFunction
    """
    #  bool QJSManagedValue::isFunction() const
    return self.uglySide.call('ritual_ZNK15QJSManagedValue10isFunctionEv')

  def isInteger(self) -> bool:
    """
    Calls Qt's 'bool QJSManagedValue::isInteger() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#isInteger
    """
    #  bool QJSManagedValue::isInteger() const
    return self.uglySide.call('ritual_ZNK15QJSManagedValue9isIntegerEv')

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QJSManagedValue::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#isNull
    """
    #  bool QJSManagedValue::isNull() const
    return self.uglySide.call('ritual_ZNK15QJSManagedValue6isNullEv')

  def isRegularExpression(self) -> bool:
    """
    Calls Qt's 'bool QJSManagedValue::isRegularExpression() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsmanagedvalue.html#isRegularExpression
    """
    #  bool QJSManagedValue::isRegularExpression() const
    return self.uglySide.call(
        'ritual_ZNK15QJSManagedValue19isRegularExpressionEv',
    )

  def isArray(self) -> bool:
    """
    Calls Qt's 'bool QJSManagedValue::isArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#isArray
    """
    #  bool QJSManagedValue::isArray() const
    return self.uglySide.call('ritual_ZNK15QJSManagedValue7isArrayEv')

  def isUrl(self) -> bool:
    """
    Calls Qt's 'bool QJSManagedValue::isUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#isUrl
    """
    #  bool QJSManagedValue::isUrl() const
    return self.uglySide.call('ritual_ZNK15QJSManagedValue5isUrlEv')

  def isVariant(self) -> bool:
    """
    Calls Qt's 'bool QJSManagedValue::isVariant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#isVariant
    """
    #  bool QJSManagedValue::isVariant() const
    return self.uglySide.call('ritual_ZNK15QJSManagedValue9isVariantEv')

  def isQObject(self) -> bool:
    """
    Calls Qt's 'bool QJSManagedValue::isQObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#isQObject
    """
    #  bool QJSManagedValue::isQObject() const
    return self.uglySide.call('ritual_ZNK15QJSManagedValue9isQObjectEv')

  def isQMetaObject(self) -> bool:
    """
    Calls Qt's 'bool QJSManagedValue::isQMetaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#isQMetaObject
    """
    #  bool QJSManagedValue::isQMetaObject() const
    return self.uglySide.call('ritual_ZNK15QJSManagedValue13isQMetaObjectEv')

  def isDate(self) -> bool:
    """
    Calls Qt's 'bool QJSManagedValue::isDate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#isDate
    """
    #  bool QJSManagedValue::isDate() const
    return self.uglySide.call('ritual_ZNK15QJSManagedValue6isDateEv')

  def isError(self) -> bool:
    """
    Calls Qt's 'bool QJSManagedValue::isError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#isError
    """
    #  bool QJSManagedValue::isError() const
    return self.uglySide.call('ritual_ZNK15QJSManagedValue7isErrorEv')

  def isJsMetaType(self) -> bool:
    """
    Calls Qt's 'bool QJSManagedValue::isJsMetaType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#isJsMetaType
    """
    #  bool QJSManagedValue::isJsMetaType() const
    return self.uglySide.call('ritual_ZNK15QJSManagedValue12isJsMetaTypeEv')

  def toString(self) -> str:
    """
    Calls Qt's 'QString QJSManagedValue::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QJSManagedValue::toString() const
    return self.uglySide.call('ritual_ZNK15QJSManagedValue8toStringEv')

  def toNumber(self) -> float:
    """
    Calls Qt's 'double QJSManagedValue::toNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#toNumber
    """
    #  double QJSManagedValue::toNumber() const
    return self.uglySide.call('ritual_ZNK15QJSManagedValue8toNumberEv')

  def toBoolean(self) -> bool:
    """
    Calls Qt's 'bool QJSManagedValue::toBoolean() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#toBoolean
    """
    #  bool QJSManagedValue::toBoolean() const
    return self.uglySide.call('ritual_ZNK15QJSManagedValue9toBooleanEv')

  def toPrimitive(self) -> QJSPrimitiveValue:
    """
    Calls Qt's 'QJSPrimitiveValue QJSManagedValue::toPrimitive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#toPrimitive

    Returns
    -------

    QJSPrimitiveValue
      A new cute QJSPrimitiveValue around the copy Qt gave back. Python owns
      it.
    """
    #  QJSPrimitiveValue QJSManagedValue::toPrimitive() const
    address = self.uglySide.call(
        'ritual_ZNK15QJSManagedValue11toPrimitiveEv',
    )
    from . import QJSPrimitiveValue
    return QJSPrimitiveValue._cuteOwning(address)

  def toJSValue(self) -> QJSValue:
    """
    Calls Qt's 'QJSValue QJSManagedValue::toJSValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#toJSValue

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QJSManagedValue::toJSValue() const
    address = self.uglySide.call('ritual_ZNK15QJSManagedValue9toJSValueEv')
    from . import QJSValue
    return QJSValue._cuteOwning(address)

  def toVariant(self) -> QVariant:
    """
    Calls Qt's 'QVariant QJSManagedValue::toVariant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#toVariant

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QJSManagedValue::toVariant() const
    address = self.uglySide.call('ritual_ZNK15QJSManagedValue9toVariantEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def toInteger(self) -> int:
    """
    Calls Qt's 'int QJSManagedValue::toInteger() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#toInteger
    """
    #  int QJSManagedValue::toInteger() const
    return self.uglySide.call('ritual_ZNK15QJSManagedValue9toIntegerEv')

  def toRegularExpression(self) -> QRegularExpression:
    """
    Calls Qt's 'QRegularExpression QJSManagedValue::toRegularExpression()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsmanagedvalue.html#toRegularExpression

    Returns
    -------

    QRegularExpression
      A new cute QRegularExpression around the copy Qt gave back. Python owns
      it.
    """
    #  QRegularExpression QJSManagedValue::toRegularExpression() const
    address = self.uglySide.call(
        'ritual_ZNK15QJSManagedValue19toRegularExpressionEv',
    )
    from ..QtCore import QRegularExpression
    return QRegularExpression._cuteOwning(address)

  def toUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QJSManagedValue::toUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#toUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QJSManagedValue::toUrl() const
    address = self.uglySide.call('ritual_ZNK15QJSManagedValue5toUrlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def toQObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QJSManagedValue::toQObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#toQObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QJSManagedValue::toQObject() const
    address = self.uglySide.call('ritual_ZNK15QJSManagedValue9toQObjectEv')
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def toQMetaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QJSManagedValue::toQMetaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#toQMetaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QJSManagedValue::toQMetaObject() const
    address = self.uglySide.call(
        'ritual_ZNK15QJSManagedValue13toQMetaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def toDateTime(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QJSManagedValue::toDateTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#toDateTime

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QJSManagedValue::toDateTime() const
    address = self.uglySide.call('ritual_ZNK15QJSManagedValue10toDateTimeEv')
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  @overload(str)
  def hasProperty(self, name: str) -> bool:
    """
    Calls Qt's 'bool QJSManagedValue::hasProperty(const QString &name)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#hasProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QJSManagedValue::hasProperty(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK15QJSManagedValue11hasPropertyERK7QString', name,
    )

  @overload(int)
  def hasProperty(self, arrayIndex: int) -> bool:
    """
    Calls Qt's 'bool QJSManagedValue::hasProperty(quint32 arrayIndex) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#hasProperty

    Parameters
    ----------

    arrayIndex : int
      Passed on as it is.
    """
    #  bool QJSManagedValue::hasProperty(quint32 arrayIndex) const
    return self.uglySide.call(
        'ritual_ZNK15QJSManagedValue11hasPropertyEj', arrayIndex,
    )

  @overload(str)
  def hasOwnProperty(self, name: str) -> bool:
    """
    Calls Qt's 'bool QJSManagedValue::hasOwnProperty(const QString &name)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsmanagedvalue.html#hasOwnProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QJSManagedValue::hasOwnProperty(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK15QJSManagedValue14hasOwnPropertyERK7QString', name,
    )

  @overload(int)
  def hasOwnProperty(self, arrayIndex: int) -> bool:
    """
    Calls Qt's 'bool QJSManagedValue::hasOwnProperty(quint32 arrayIndex)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsmanagedvalue.html#hasOwnProperty

    Parameters
    ----------

    arrayIndex : int
      Passed on as it is.
    """
    #  bool QJSManagedValue::hasOwnProperty(quint32 arrayIndex) const
    return self.uglySide.call(
        'ritual_ZNK15QJSManagedValue14hasOwnPropertyEj', arrayIndex,
    )

  @overload(str)
  def property(self, name: str) -> QJSValue:
    """
    Calls Qt's 'QJSValue QJSManagedValue::property(const QString &name)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#property

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QJSManagedValue::property(const QString &name) const
    address = self.uglySide.call(
        'ritual_ZNK15QJSManagedValue8propertyERK7QString', name,
    )
    from . import QJSValue
    return QJSValue._cuteOwning(address)

  @overload(int)
  def property(self, arrayIndex: int) -> QJSValue:
    """
    Calls Qt's 'QJSValue QJSManagedValue::property(quint32 arrayIndex)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#property

    Parameters
    ----------

    arrayIndex : int
      Passed on as it is.

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QJSManagedValue::property(quint32 arrayIndex) const
    address = self.uglySide.call(
        'ritual_ZNK15QJSManagedValue8propertyEj', arrayIndex,
    )
    from . import QJSValue
    return QJSValue._cuteOwning(address)

  @overload(QList[QJSValue])
  def call(self, arguments: QList[QJSValue]) -> QJSValue:
    """
    Calls Qt's 'QJSValue QJSManagedValue::call(const QJSValueList &arguments)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#call

    Parameters
    ----------

    arguments : QList[QJSValue]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QJSManagedValue::call(const QJSValueList &arguments) const
    address = self.uglySide.call(
        'ritual_ZNK15QJSManagedValue4callERK5QListI8QJSValueE',
        self._valueOf(arguments),
    )
    from . import QJSValue
    return QJSValue._cuteOwning(address)

  @overload(QJSValue, QList[QJSValue])
  def callWithInstance(
      self,
      instance: QJSValue,
      arguments: QList[QJSValue],
  ) -> QJSValue:
    """
    Calls Qt's 'QJSValue QJSManagedValue::callWithInstance(const QJSValue
    &instance, const QJSValueList &arguments) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsmanagedvalue.html#callWithInstance

    Parameters
    ----------

    instance : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.

    arguments : QList[QJSValue]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QJSManagedValue::callWithInstance(const QJSValue &instance,
    #      const QJSValueList &arguments) const
    address = self.uglySide.call(
        'ritual_ZNK15QJSManagedValue16callWithInstanceERK8QJSValueRK5QListI'
        'S0_E',
        self._valueOf(instance), self._valueOf(arguments),
    )
    from . import QJSValue
    return QJSValue._cuteOwning(address)

  @overload(QList[QJSValue])
  def callAsConstructor(self, arguments: QList[QJSValue]) -> QJSValue:
    """
    Calls Qt's 'QJSValue QJSManagedValue::callAsConstructor(const
    QJSValueList &arguments) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsmanagedvalue.html#callAsConstructor

    Parameters
    ----------

    arguments : QList[QJSValue]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QJSManagedValue::callAsConstructor(const QJSValueList
    #      &arguments) const
    address = self.uglySide.call(
        'ritual_ZNK15QJSManagedValue17callAsConstructorERK5QListI8QJSValueE',
        self._valueOf(arguments),
    )
    from . import QJSValue
    return QJSValue._cuteOwning(address)

  def jsMetaMembers(self) -> QStringList:
    """
    Calls Qt's 'QStringList QJSManagedValue::jsMetaMembers() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#jsMetaMembers

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QJSManagedValue::jsMetaMembers() const
    address = self.uglySide.call(
        'ritual_ZNK15QJSManagedValue13jsMetaMembersEv',
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, QJSValue)
  def setProperty(self, name: str, value: QJSValue) -> None:
    """
    Calls Qt's 'void QJSManagedValue::setProperty(const QString &name, const
    QJSValue &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#setProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QJSManagedValue::setProperty(const QString &name, const QJSValue
    #      &value)
    self.uglySide.call(
        'ritual_ZN15QJSManagedValue11setPropertyERK7QStringRK8QJSValue',
        name, self._valueOf(value),
    )

  @overload(int, QJSValue)
  def setProperty(self, arrayIndex: int, value: QJSValue) -> None:
    """
    Calls Qt's 'void QJSManagedValue::setProperty(quint32 arrayIndex, const
    QJSValue &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalue.html#setProperty

    Parameters
    ----------

    arrayIndex : int
      Passed on as it is.

    value : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QJSManagedValue::setProperty(quint32 arrayIndex, const QJSValue
    #      &value)
    self.uglySide.call(
        'ritual_ZN15QJSManagedValue11setPropertyEjRK8QJSValue',
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QJSManagedValue::QJSManagedValue()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsmanagedvalue.html#QJSManagedValue
    """
    #  QJSManagedValue::QJSManagedValue()
    self._noteCreation(QJSManagedValue, lambda: Rituals.call(
        'ritual_ZN15QJSManagedValueC1Ev',
    ))

  @overload(QJSValue, QJSEngine)
  @overload(QJSValue, NoneType)
  def __init__(self, value: QJSValue, engine: Optional[QJSEngine]) -> None:
    """
    Notes what was given, for Qt's 'QJSManagedValue::QJSManagedValue(QJSValue
    value, QJSEngine *engine)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsmanagedvalue.html#QJSManagedValue

    Parameters
    ----------

    value : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.

    engine : Optional[QJSEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QJSManagedValue::QJSManagedValue(QJSValue value, QJSEngine *engine)
    self._noteCreation(QJSManagedValue, lambda: Rituals.call(
        'ritual_ZN15QJSManagedValueC1E8QJSValueP9QJSEngine',
        self._valueOf(value), self._addressOf(engine),
    ))

  @overload(QJSPrimitiveValue, QJSEngine)
  @overload(QJSPrimitiveValue, NoneType)
  def __init__(
      self,
      value: QJSPrimitiveValue,
      engine: Optional[QJSEngine],
  ) -> None:
    """
    Notes what was given, for Qt's 'QJSManagedValue::QJSManagedValue(const
    QJSPrimitiveValue &value, QJSEngine *engine)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsmanagedvalue.html#QJSManagedValue

    Parameters
    ----------

    value : QJSPrimitiveValue
      Passed on as a value: Qt reads the C++ QJSPrimitiveValue, which stays
      Python's own.

    engine : Optional[QJSEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QJSManagedValue::QJSManagedValue(const QJSPrimitiveValue &value,
    #      QJSEngine *engine)
    self._noteCreation(QJSManagedValue, lambda: Rituals.call(
        'ritual_ZN15QJSManagedValueC1ERK17QJSPrimitiveValueP9QJSEngine',
        self._valueOf(value), self._addressOf(engine),
    ))

  @overload(QVariant, QJSEngine)
  @overload(QVariant, NoneType)
  def __init__(self, variant: QVariant, engine: Optional[QJSEngine]) -> None:
    """
    Notes what was given, for Qt's 'QJSManagedValue::QJSManagedValue(const
    QVariant &variant, QJSEngine *engine)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsmanagedvalue.html#QJSManagedValue

    Parameters
    ----------

    variant : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    engine : Optional[QJSEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QJSManagedValue::QJSManagedValue(const QVariant &variant, QJSEngine
    #      *engine)
    self._noteCreation(QJSManagedValue, lambda: Rituals.call(
        'ritual_ZN15QJSManagedValueC1ERK8QVariantP9QJSEngine',
        self._valueOf(variant), self._addressOf(engine),
    ))

  @overload(str, QJSEngine)
  @overload(str, NoneType)
  def __init__(self, string: str, engine: Optional[QJSEngine]) -> None:
    """
    Notes what was given, for Qt's 'QJSManagedValue::QJSManagedValue(const
    QString &string, QJSEngine *engine)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsmanagedvalue.html#QJSManagedValue

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    engine : Optional[QJSEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QJSManagedValue::QJSManagedValue(const QString &string, QJSEngine
    #      *engine)
    self._noteCreation(QJSManagedValue, lambda: Rituals.call(
        'ritual_ZN15QJSManagedValueC1ERK7QStringP9QJSEngine',
        string, self._addressOf(engine),
    ))

  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def __init__(self, engine: Optional[QV4.ExecutionEngine]) -> None:
    """
    Notes what was given, for Qt's
    'QJSManagedValue::QJSManagedValue(QV4::ExecutionEngine *engine)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsmanagedvalue.html#QJSManagedValue

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QJSManagedValue::QJSManagedValue(QV4::ExecutionEngine *engine)
    self._noteCreation(QJSManagedValue, lambda: Rituals.call(
        'ritual_ZN15QJSManagedValueC1EPN3QV415ExecutionEngineE',
        self._addressOf(engine),
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
    Calls Qt's 'bool QJSManagedValue::deleteProperty(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsmanagedvalue.html#deleteProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QJSManagedValue::deleteProperty(const QString &name)
    return self.uglySide.call(
        'ritual_ZN15QJSManagedValue14deletePropertyERK7QString', name,
    )

  @overload(int)
  def deleteProperty(self, arrayIndex: int) -> bool:
    """
    Calls Qt's 'bool QJSManagedValue::deleteProperty(quint32 arrayIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsmanagedvalue.html#deleteProperty

    Parameters
    ----------

    arrayIndex : int
      Passed on as it is.
    """
    #  bool QJSManagedValue::deleteProperty(quint32 arrayIndex)
    return self.uglySide.call(
        'ritual_ZN15QJSManagedValue14deletePropertyEj', arrayIndex,
    )

  @staticmethod
  def equals(*__, **_) -> Never:
    """
    Qt's 'bool QJSManagedValue::equals(const QJSManagedValue &other) const':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QJSManagedValue.equals' has no cute function yet. Qt's 'bool "
        "QJSManagedValue::equals(const QJSManagedValue &other) const': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def jsMetaInstantiate(*__, **_) -> Never:
    """
    Qt's 'QJSManagedValue QJSManagedValue::jsMetaInstantiate(const
    QJSValueList &values) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QJSManagedValue.jsMetaInstantiate' has no cute function yet. Qt's "
        "'QJSManagedValue QJSManagedValue::jsMetaInstantiate(const "
        "QJSValueList &values) const': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def jsMetaType(*__, **_) -> Never:
    """
    Qt's 'QJSManagedValue QJSManagedValue::jsMetaType() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QJSManagedValue.jsMetaType' has no cute function yet. Qt's "
        "'QJSManagedValue QJSManagedValue::jsMetaType() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def prototype(*__, **_) -> Never:
    """
    Qt's 'QJSManagedValue QJSManagedValue::prototype() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QJSManagedValue.prototype' has no cute function yet. Qt's "
        "'QJSManagedValue QJSManagedValue::prototype() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def setPrototype(*__, **_) -> Never:
    """
    Qt's 'void QJSManagedValue::setPrototype(const QJSManagedValue
    &prototype)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QJSManagedValue.setPrototype' has no cute function yet. Qt's "
        "'void QJSManagedValue::setPrototype(const QJSManagedValue "
        "&prototype)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def strictlyEquals(*__, **_) -> Never:
    """
    Qt's 'bool QJSManagedValue::strictlyEquals(const QJSManagedValue &other)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QJSManagedValue.strictlyEquals' has no cute function yet. Qt's "
        "'bool QJSManagedValue::strictlyEquals(const QJSManagedValue "
        "&other) const': takes a type Python has no way to hand over yet.")
