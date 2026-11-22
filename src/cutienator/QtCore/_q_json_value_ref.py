"""
QJsonValueRef binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qjsonvalue.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QJsonValue, QJsonValueConstRef

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QJsonArray, QJsonObject, QLatin1String, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonArray = WAIT['QJsonArray']
  QJsonObject = WAIT['QJsonObject']
  QLatin1String = WAIT['QLatin1String']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QJsonValueRef(QJsonValueConstRef):
  """
  The cute side of Qt's QJsonValueRef: a plain Python object standing in
  front of one C++ QJsonValueRef.

  It is built on the cute 'QJsonValueConstRef', as Qt's QJsonValueRef is
  built on Qt's QJsonValueConstRef, and has everything that class has.

  C++ hands a QJsonValueRef around as a copy, so every C++ QJsonValueRef
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QJsonValueRef that has a ritual and that Python can
  call so far, 20 names in all: 'toVariant', 'type', 'isNull', 'isBool',
  'isDouble', 'isString', 'isArray', 'isObject', 'isUndefined', 'toBool',
  'toInt', 'toInteger', 'toDouble', 'toString', 'toStringView', 'toArray',
  'toObject', '__getitem__', '__eq__', '__ne__'. It can be made from Python,
  in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QJsonValue QJsonValueRef::operator QJsonValue() const': an operator
    Python has no name for.
  - Qt's 'bool operator==(const QJsonValueConstRef &lhs, const QJsonValueRef
    &rhs)': takes in Python what 'bool operator==(const QJsonValueRef &lhs,
    const QJsonValueConstRef &rhs)' takes.
  - Qt's 'bool operator!=(const QJsonValueConstRef &lhs, const QJsonValueRef
    &rhs)': takes in Python what 'bool operator!=(const QJsonValueRef &lhs,
    const QJsonValueConstRef &rhs)' takes.
  - Qt's 'QJsonValueRef::~QJsonValueRef()': the destructor: Python removes
    its C++ QJsonValueRef by it, and has no other use for it.

  What has no ritual
  ------------------

  4 of the 35 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 2 private.

  What to expect
  --------------

  - The C++ QJsonValueRef is created at the first use, not by
    'QJsonValueRef(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QJsonValueRef back gives a copy the ritual made for
    Python, in a new cute QJsonValueRef.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QJsonValueRef'

  #  Qt's '~QJsonValueRef()'. Naming it makes this a value class: Python owns
  #  every C++ QJsonValueRef behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QJsonValueRefD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toVariant(self) -> QVariant:
    """
    Calls Qt's 'QVariant QJsonValueRef::toVariant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueref.html#toVariant

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QJsonValueRef::toVariant() const
    address = self.uglySide.call('ritual_ZNK13QJsonValueRef9toVariantEv')
    from . import QVariant
    return QVariant._cuteOwning(address)

  def type(self) -> QJsonValue.Type:
    """
    Calls Qt's 'QJsonValue::Type QJsonValueRef::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueref.html#type

    Returns
    -------

    QJsonValue.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QJsonValue.Type(number)'
      gives.
    """
    #  QJsonValue::Type QJsonValueRef::type() const
    return QJsonValue.Type(self.uglySide.call(
        'ritual_ZNK13QJsonValueRef4typeEv',
    ))

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QJsonValueRef::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueref.html#isNull
    """
    #  bool QJsonValueRef::isNull() const
    return self.uglySide.call('ritual_ZNK13QJsonValueRef6isNullEv')

  def isBool(self) -> bool:
    """
    Calls Qt's 'bool QJsonValueRef::isBool() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueref.html#isBool
    """
    #  bool QJsonValueRef::isBool() const
    return self.uglySide.call('ritual_ZNK13QJsonValueRef6isBoolEv')

  def isDouble(self) -> bool:
    """
    Calls Qt's 'bool QJsonValueRef::isDouble() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueref.html#isDouble
    """
    #  bool QJsonValueRef::isDouble() const
    return self.uglySide.call('ritual_ZNK13QJsonValueRef8isDoubleEv')

  def isString(self) -> bool:
    """
    Calls Qt's 'bool QJsonValueRef::isString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueref.html#isString
    """
    #  bool QJsonValueRef::isString() const
    return self.uglySide.call('ritual_ZNK13QJsonValueRef8isStringEv')

  def isArray(self) -> bool:
    """
    Calls Qt's 'bool QJsonValueRef::isArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueref.html#isArray
    """
    #  bool QJsonValueRef::isArray() const
    return self.uglySide.call('ritual_ZNK13QJsonValueRef7isArrayEv')

  def isObject(self) -> bool:
    """
    Calls Qt's 'bool QJsonValueRef::isObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueref.html#isObject
    """
    #  bool QJsonValueRef::isObject() const
    return self.uglySide.call('ritual_ZNK13QJsonValueRef8isObjectEv')

  def isUndefined(self) -> bool:
    """
    Calls Qt's 'bool QJsonValueRef::isUndefined() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueref.html#isUndefined
    """
    #  bool QJsonValueRef::isUndefined() const
    return self.uglySide.call('ritual_ZNK13QJsonValueRef11isUndefinedEv')

  @overload()
  @overload(bool)
  def toBool(self, defaultValue: bool = False) -> bool:
    """
    Calls Qt's 'bool QJsonValueRef::toBool(bool defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueref.html#toBool

    Parameters
    ----------

    defaultValue : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  bool QJsonValueRef::toBool(bool defaultValue) const
    return self.uglySide.call(
        'ritual_ZNK13QJsonValueRef6toBoolEb', defaultValue,
    )

  @overload()
  @overload(int)
  def toInt(self, defaultValue: int = 0) -> int:
    """
    Calls Qt's 'int QJsonValueRef::toInt(int defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueref.html#toInt

    Parameters
    ----------

    defaultValue : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  int QJsonValueRef::toInt(int defaultValue) const
    return self.uglySide.call(
        'ritual_ZNK13QJsonValueRef5toIntEi', defaultValue,
    )

  @overload()
  @overload(int)
  def toInteger(self, defaultValue: int = 0) -> int:
    """
    Calls Qt's 'qint64 QJsonValueRef::toInteger(qint64 defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueref.html#toInteger

    Parameters
    ----------

    defaultValue : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  qint64 QJsonValueRef::toInteger(qint64 defaultValue) const
    return self.uglySide.call(
        'ritual_ZNK13QJsonValueRef9toIntegerEx', defaultValue,
    )

  @overload()
  @overload(float)
  def toDouble(self, defaultValue: float = 0.0) -> float:
    """
    Calls Qt's 'double QJsonValueRef::toDouble(double defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueref.html#toDouble

    Parameters
    ----------

    defaultValue : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  double QJsonValueRef::toDouble(double defaultValue) const
    return self.uglySide.call(
        'ritual_ZNK13QJsonValueRef8toDoubleEd', defaultValue,
    )

  @overload()
  @overload(str)
  def toString(self, defaultValue: str = '') -> str:
    """
    Calls Qt's 'QString QJsonValueRef::toString(const QString &defaultValue)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueref.html#toString

    Parameters
    ----------

    defaultValue : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QJsonValueRef::toString(const QString &defaultValue) const
    return self.uglySide.call(
        'ritual_ZNK13QJsonValueRef8toStringERK7QString', defaultValue,
    )

  @overload()
  @overload(str)
  def toStringView(self, defaultValue: str = '') -> str:
    """
    Calls Qt's 'QAnyStringView QJsonValueRef::toStringView(QAnyStringView
    defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueref.html#toStringView

    Parameters
    ----------

    defaultValue : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QAnyStringView QJsonValueRef::toStringView(QAnyStringView
    #      defaultValue) const
    return self.uglySide.call(
        'ritual_ZNK13QJsonValueRef12toStringViewE14QAnyStringView',
        defaultValue,
    )

  def toArray(self) -> QJsonArray:
    """
    Calls Qt's 'QJsonArray QJsonValueRef::toArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueref.html#toArray

    Returns
    -------

    QJsonArray
      A new cute QJsonArray around the copy Qt gave back. Python owns it.
    """
    #  QJsonArray QJsonValueRef::toArray() const
    address = self.uglySide.call('ritual_ZNK13QJsonValueRef7toArrayEv')
    from . import QJsonArray
    return QJsonArray._cuteOwning(address)

  def toObject(self) -> QJsonObject:
    """
    Calls Qt's 'QJsonObject QJsonValueRef::toObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueref.html#toObject

    Returns
    -------

    QJsonObject
      A new cute QJsonObject around the copy Qt gave back. Python owns it.
    """
    #  QJsonObject QJsonValueRef::toObject() const
    address = self.uglySide.call('ritual_ZNK13QJsonValueRef8toObjectEv')
    from . import QJsonObject
    return QJsonObject._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def __getitem__(self, key: str) -> QJsonValue:
    """
    Calls Qt's 'const QJsonValue QJsonValueRef::operator[](QStringView key)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueref.html#operator[]

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QJsonValue
      A new cute QJsonValue around the copy Qt gave back. Python owns it.
    """
    #  const QJsonValue QJsonValueRef::operator[](QStringView key) const
    address = self.uglySide.call(
        'ritual_ZNK13QJsonValueRefixE11QStringView', key,
    )
    return QJsonValue._cuteOwning(address)

  @overload(QLatin1String)
  def __getitem__(self, key: QLatin1String) -> QJsonValue:
    """
    Calls Qt's 'const QJsonValue QJsonValueRef::operator[](QLatin1StringView
    key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueref.html#operator[]

    Parameters
    ----------

    key : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    Returns
    -------

    QJsonValue
      A new cute QJsonValue around the copy Qt gave back. Python owns it.
    """
    #  const QJsonValue QJsonValueRef::operator[](QLatin1StringView key)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13QJsonValueRefixE13QLatin1String', self._valueOf(key),
    )
    return QJsonValue._cuteOwning(address)

  @overload(int)
  def __getitem__(self, i: int) -> QJsonValue:
    """
    Calls Qt's 'const QJsonValue QJsonValueRef::operator[](qsizetype i)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueref.html#operator[]

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QJsonValue
      A new cute QJsonValue around the copy Qt gave back. Python owns it.
    """
    #  const QJsonValue QJsonValueRef::operator[](qsizetype i) const
    address = self.uglySide.call('ritual_ZNK13QJsonValueRefixEx', i)
    return QJsonValue._cuteOwning(address)

  @overload(THIS)
  def __eq__(self, rhs: QJsonValueRef) -> bool:
    """
    Calls Qt's 'bool operator==(const QJsonValueRef &lhs, const QJsonValueRef
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueref.html#operator==

    Parameters
    ----------

    rhs : QJsonValueRef
      Passed on as a value: Qt reads the C++ QJsonValueRef, which stays
      Python's own.
    """
    #  bool operator==(const QJsonValueRef &lhs, const QJsonValueRef &rhs)
    return Rituals.call(
        'ritual_ZeqRK13QJsonValueRefS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QJsonValueConstRef)
  def __eq__(self, rhs: QJsonValueConstRef) -> bool:
    """
    Calls Qt's 'bool operator==(const QJsonValueRef &lhs, const
    QJsonValueConstRef &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueref.html#operator==

    Parameters
    ----------

    rhs : QJsonValueConstRef
      Passed on as a value: Qt reads the C++ QJsonValueConstRef, which stays
      Python's own.
    """
    #  bool operator==(const QJsonValueRef &lhs, const QJsonValueConstRef
    #      &rhs)
    return Rituals.call(
        'ritual_ZeqRK13QJsonValueRefRK18QJsonValueConstRef',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QJsonValueRef) -> bool:
    """
    Calls Qt's 'bool operator!=(const QJsonValueRef &lhs, const QJsonValueRef
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueref.html#operator!=

    Parameters
    ----------

    rhs : QJsonValueRef
      Passed on as a value: Qt reads the C++ QJsonValueRef, which stays
      Python's own.
    """
    #  bool operator!=(const QJsonValueRef &lhs, const QJsonValueRef &rhs)
    return Rituals.call(
        'ritual_ZneRK13QJsonValueRefS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QJsonValueConstRef)
  def __ne__(self, rhs: QJsonValueConstRef) -> bool:
    """
    Calls Qt's 'bool operator!=(const QJsonValueRef &lhs, const
    QJsonValueConstRef &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueref.html#operator!=

    Parameters
    ----------

    rhs : QJsonValueConstRef
      Passed on as a value: Qt reads the C++ QJsonValueConstRef, which stays
      Python's own.
    """
    #  bool operator!=(const QJsonValueRef &lhs, const QJsonValueConstRef
    #      &rhs)
    return Rituals.call(
        'ritual_ZneRK13QJsonValueRefRK18QJsonValueConstRef',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __init__(self, a0: QJsonValueRef) -> None:
    """
    Notes what was given, for Qt's 'QJsonValueRef::QJsonValueRef(const
    QJsonValueRef &a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueref.html#QJsonValueRef

    Parameters
    ----------

    a0 : QJsonValueRef
      Passed on as a value: Qt reads the C++ QJsonValueRef, which stays
      Python's own.
    """
    #  QJsonValueRef::QJsonValueRef(const QJsonValueRef &a0)
    self._noteCreation(QJsonValueRef, lambda: Rituals.call(
        'ritual_ZN13QJsonValueRefC1ERKS_', self._valueOf(a0),
    ))

  @overload(QJsonArray, int)
  @overload(NoneType, int)
  def __init__(self, array: Optional[QJsonArray], idx: int) -> None:
    """
    Notes what was given, for Qt's 'QJsonValueRef::QJsonValueRef(QJsonArray
    *array, qsizetype idx)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueref.html#QJsonValueRef

    Parameters
    ----------

    array : Optional[QJsonArray]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    idx : int
      Passed on as it is.
    """
    #  QJsonValueRef::QJsonValueRef(QJsonArray *array, qsizetype idx)
    self._noteCreation(QJsonValueRef, lambda: Rituals.call(
        'ritual_ZN13QJsonValueRefC1EP10QJsonArrayx',
        self._addressOf(array), idx,
    ))

  @overload(QJsonObject, int)
  def __init__(self, object: Optional[QJsonObject], idx: int) -> None:
    """
    Notes what was given, for Qt's 'QJsonValueRef::QJsonValueRef(QJsonObject
    *object, qsizetype idx)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueref.html#QJsonValueRef

    Parameters
    ----------

    object : Optional[QJsonObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    idx : int
      Passed on as it is.
    """
    #  QJsonValueRef::QJsonValueRef(QJsonObject *object, qsizetype idx)
    self._noteCreation(QJsonValueRef, lambda: Rituals.call(
        'ritual_ZN13QJsonValueRefC1EP11QJsonObjectx',
        self._addressOf(object), idx,
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
