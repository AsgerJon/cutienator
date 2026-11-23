"""
QJsonValueConstRef binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qjsonvalue.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QJsonValue

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


class QJsonValueConstRef(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QJsonValueConstRef: a plain Python object standing in
  front of one C++ QJsonValueConstRef.

  C++ hands a QJsonValueConstRef around as a copy, so every C++
  QJsonValueConstRef behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QJsonValueConstRef that has a ritual and that Python
  can call so far, 30 names in all: 'toVariant', 'type', 'isNull', 'isBool',
  'isDouble', 'isString', 'isArray', 'isObject', 'isUndefined', 'toBool',
  'toInt', 'toInteger', 'toDouble', 'toString', 'toStringView', 'toArray',
  'toObject', '__getitem__', '__eq__', '__ne__', 'concreteType',
  'concreteBool', 'concreteInt', 'concreteDouble', 'concreteString',
  'concreteStringView', 'concrete', 'objectKey', 'objectKeyView', 'rebind'.
  It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QJsonValue QJsonValueConstRef::operator QJsonValue() const': an
    operator Python has no name for.
  - Qt's 'bool operator==(const QJsonValue &lhs, const QJsonValueConstRef
    &rhs)': takes in Python what 'bool operator==(const QJsonValueConstRef
    &lhs, const QJsonValue &rhs)' takes.
  - Qt's 'bool operator!=(const QJsonValue &lhs, const QJsonValueConstRef
    &rhs)': takes in Python what 'bool operator!=(const QJsonValueConstRef
    &lhs, const QJsonValue &rhs)' takes.
  - Qt's 'QJsonValueConstRef::~QJsonValueConstRef()': the destructor: Python
    removes its C++ QJsonValueConstRef by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 44 functions Qt declares: 1 forbidden.

  What to expect
  --------------

  - The C++ QJsonValueConstRef is created at the first use, not by
    'QJsonValueConstRef(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QJsonValueConstRef back gives a copy the ritual made
    for Python, in a new cute QJsonValueConstRef.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS)
  def concreteType(self_: QJsonValueConstRef) -> QJsonValue.Type:
    """
    Calls Qt's 'QJsonValue::Type
    QJsonValueConstRef::concreteType(QJsonValueConstRef self_)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsonvalueconstref.html#concreteType

    Parameters
    ----------

    self_ : QJsonValueConstRef
      Passed on as a value: Qt reads the C++ QJsonValueConstRef, which stays
      Python's own.

    Returns
    -------

    QJsonValue.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QJsonValue.Type(number)'
      gives.
    """
    #  QJsonValue::Type QJsonValueConstRef::concreteType(QJsonValueConstRef
    #      self_)
    return QJsonValue.Type(Rituals.call(
        'ritual_ZN18QJsonValueConstRef12concreteTypeES_',
        CuteMixin._valueOf(self_),
    ))

  @staticmethod
  @overload(THIS, bool)
  def concreteBool(self_: QJsonValueConstRef, defaultValue: bool) -> bool:
    """
    Calls Qt's 'bool QJsonValueConstRef::concreteBool(QJsonValueConstRef
    self_, bool defaultValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsonvalueconstref.html#concreteBool

    Parameters
    ----------

    self_ : QJsonValueConstRef
      Passed on as a value: Qt reads the C++ QJsonValueConstRef, which stays
      Python's own.

    defaultValue : bool
      Passed on as it is.
    """
    #  bool QJsonValueConstRef::concreteBool(QJsonValueConstRef self_, bool
    #      defaultValue)
    return Rituals.call(
        'ritual_ZN18QJsonValueConstRef12concreteBoolES_b',
        CuteMixin._valueOf(self_), defaultValue,
    )

  @staticmethod
  @overload(THIS, int, bool)
  def concreteInt(
      self_: QJsonValueConstRef,
      defaultValue: int,
      clamp: bool,
  ) -> int:
    """
    Calls Qt's 'qint64 QJsonValueConstRef::concreteInt(QJsonValueConstRef
    self_, qint64 defaultValue, bool clamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsonvalueconstref.html#concreteInt

    Parameters
    ----------

    self_ : QJsonValueConstRef
      Passed on as a value: Qt reads the C++ QJsonValueConstRef, which stays
      Python's own.

    defaultValue : int
      Passed on as it is.

    clamp : bool
      Passed on as it is.
    """
    #  qint64 QJsonValueConstRef::concreteInt(QJsonValueConstRef self_,
    #      qint64 defaultValue, bool clamp)
    return Rituals.call(
        'ritual_ZN18QJsonValueConstRef11concreteIntES_xb',
        CuteMixin._valueOf(self_), defaultValue, clamp,
    )

  @staticmethod
  @overload(THIS, float)
  def concreteDouble(
      self_: QJsonValueConstRef,
      defaultValue: float,
  ) -> float:
    """
    Calls Qt's 'double QJsonValueConstRef::concreteDouble(QJsonValueConstRef
    self_, double defaultValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsonvalueconstref.html#concreteDouble

    Parameters
    ----------

    self_ : QJsonValueConstRef
      Passed on as a value: Qt reads the C++ QJsonValueConstRef, which stays
      Python's own.

    defaultValue : float
      Passed on as it is.
    """
    #  double QJsonValueConstRef::concreteDouble(QJsonValueConstRef self_,
    #      double defaultValue)
    return Rituals.call(
        'ritual_ZN18QJsonValueConstRef14concreteDoubleES_d',
        CuteMixin._valueOf(self_), defaultValue,
    )

  @staticmethod
  @overload(THIS, str)
  def concreteString(self_: QJsonValueConstRef, defaultValue: str) -> str:
    """
    Calls Qt's 'QString QJsonValueConstRef::concreteString(QJsonValueConstRef
    self_, const QString &defaultValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsonvalueconstref.html#concreteString

    Parameters
    ----------

    self_ : QJsonValueConstRef
      Passed on as a value: Qt reads the C++ QJsonValueConstRef, which stays
      Python's own.

    defaultValue : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QJsonValueConstRef::concreteString(QJsonValueConstRef self_,
    #      const QString &defaultValue)
    return Rituals.call(
        'ritual_ZN18QJsonValueConstRef14concreteStringES_RK7QString',
        CuteMixin._valueOf(self_), defaultValue,
    )

  @staticmethod
  @overload(THIS, str)
  def concreteStringView(
      self_: QJsonValueConstRef,
      defaultValue: str,
  ) -> str:
    """
    Calls Qt's 'QAnyStringView
    QJsonValueConstRef::concreteStringView(QJsonValueConstRef self_,
    QAnyStringView defaultValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsonvalueconstref.html#concreteStringView

    Parameters
    ----------

    self_ : QJsonValueConstRef
      Passed on as a value: Qt reads the C++ QJsonValueConstRef, which stays
      Python's own.

    defaultValue : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QAnyStringView
    #      QJsonValueConstRef::concreteStringView(QJsonValueConstRef self_,
    #      QAnyStringView defaultValue)
    return Rituals.call(
        'ritual_ZN18QJsonValueConstRef18concreteStringViewES_14QAnyStringVi'
        'ew',
        CuteMixin._valueOf(self_), defaultValue,
    )

  @staticmethod
  @overload(THIS)
  def concrete(self_: QJsonValueConstRef) -> QJsonValue:
    """
    Calls Qt's 'QJsonValue QJsonValueConstRef::concrete(QJsonValueConstRef
    self_)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueconstref.html#concrete

    Parameters
    ----------

    self_ : QJsonValueConstRef
      Passed on as a value: Qt reads the C++ QJsonValueConstRef, which stays
      Python's own.

    Returns
    -------

    QJsonValue
      A new cute QJsonValue around the copy Qt gave back. Python owns it.
    """
    #  QJsonValue QJsonValueConstRef::concrete(QJsonValueConstRef self_)
    address = Rituals.call(
        'ritual_ZN18QJsonValueConstRef8concreteES_',
        CuteMixin._valueOf(self_),
    )
    return QJsonValue._cuteOwning(address)

  @staticmethod
  @overload(THIS)
  def objectKey(self_: QJsonValueConstRef) -> str:
    """
    Calls Qt's 'QString QJsonValueConstRef::objectKey(QJsonValueConstRef
    self_)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueconstref.html#objectKey

    Parameters
    ----------

    self_ : QJsonValueConstRef
      Passed on as a value: Qt reads the C++ QJsonValueConstRef, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QJsonValueConstRef::objectKey(QJsonValueConstRef self_)
    return Rituals.call(
        'ritual_ZN18QJsonValueConstRef9objectKeyES_',
        CuteMixin._valueOf(self_),
    )

  @overload()
  def objectKey(self) -> str:
    """
    Calls Qt's 'QString QJsonValueConstRef::objectKey() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueconstref.html#objectKey

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QJsonValueConstRef::objectKey() const
    return self.uglySide.call('ritual_ZNK18QJsonValueConstRef9objectKeyEv')

  @staticmethod
  @overload(THIS)
  def objectKeyView(self_: QJsonValueConstRef) -> str:
    """
    Calls Qt's 'QAnyStringView
    QJsonValueConstRef::objectKeyView(QJsonValueConstRef self_)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsonvalueconstref.html#objectKeyView

    Parameters
    ----------

    self_ : QJsonValueConstRef
      Passed on as a value: Qt reads the C++ QJsonValueConstRef, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QAnyStringView QJsonValueConstRef::objectKeyView(QJsonValueConstRef
    #      self_)
    return Rituals.call(
        'ritual_ZN18QJsonValueConstRef13objectKeyViewES_',
        CuteMixin._valueOf(self_),
    )

  @overload()
  def objectKeyView(self) -> str:
    """
    Calls Qt's 'QAnyStringView QJsonValueConstRef::objectKeyView() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsonvalueconstref.html#objectKeyView

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QAnyStringView QJsonValueConstRef::objectKeyView() const
    return self.uglySide.call(
        'ritual_ZNK18QJsonValueConstRef13objectKeyViewEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QJsonValueConstRef'

  #  Qt's '~QJsonValueConstRef()'. Naming it makes this a value class: Python
  #  owns every C++ QJsonValueConstRef behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QJsonValueConstRefD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toVariant(self) -> QVariant:
    """
    Calls Qt's 'QVariant QJsonValueConstRef::toVariant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueconstref.html#toVariant

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QJsonValueConstRef::toVariant() const
    address = self.uglySide.call(
        'ritual_ZNK18QJsonValueConstRef9toVariantEv',
    )
    from . import QVariant
    return QVariant._cuteOwning(address)

  def type(self) -> QJsonValue.Type:
    """
    Calls Qt's 'QJsonValue::Type QJsonValueConstRef::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueconstref.html#type

    Returns
    -------

    QJsonValue.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QJsonValue.Type(number)'
      gives.
    """
    #  QJsonValue::Type QJsonValueConstRef::type() const
    return QJsonValue.Type(self.uglySide.call(
        'ritual_ZNK18QJsonValueConstRef4typeEv',
    ))

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QJsonValueConstRef::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueconstref.html#isNull
    """
    #  bool QJsonValueConstRef::isNull() const
    return self.uglySide.call('ritual_ZNK18QJsonValueConstRef6isNullEv')

  def isBool(self) -> bool:
    """
    Calls Qt's 'bool QJsonValueConstRef::isBool() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueconstref.html#isBool
    """
    #  bool QJsonValueConstRef::isBool() const
    return self.uglySide.call('ritual_ZNK18QJsonValueConstRef6isBoolEv')

  def isDouble(self) -> bool:
    """
    Calls Qt's 'bool QJsonValueConstRef::isDouble() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueconstref.html#isDouble
    """
    #  bool QJsonValueConstRef::isDouble() const
    return self.uglySide.call('ritual_ZNK18QJsonValueConstRef8isDoubleEv')

  def isString(self) -> bool:
    """
    Calls Qt's 'bool QJsonValueConstRef::isString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueconstref.html#isString
    """
    #  bool QJsonValueConstRef::isString() const
    return self.uglySide.call('ritual_ZNK18QJsonValueConstRef8isStringEv')

  def isArray(self) -> bool:
    """
    Calls Qt's 'bool QJsonValueConstRef::isArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueconstref.html#isArray
    """
    #  bool QJsonValueConstRef::isArray() const
    return self.uglySide.call('ritual_ZNK18QJsonValueConstRef7isArrayEv')

  def isObject(self) -> bool:
    """
    Calls Qt's 'bool QJsonValueConstRef::isObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueconstref.html#isObject
    """
    #  bool QJsonValueConstRef::isObject() const
    return self.uglySide.call('ritual_ZNK18QJsonValueConstRef8isObjectEv')

  def isUndefined(self) -> bool:
    """
    Calls Qt's 'bool QJsonValueConstRef::isUndefined() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsonvalueconstref.html#isUndefined
    """
    #  bool QJsonValueConstRef::isUndefined() const
    return self.uglySide.call(
        'ritual_ZNK18QJsonValueConstRef11isUndefinedEv',
    )

  @overload()
  @overload(bool)
  def toBool(self, defaultValue: bool = False) -> bool:
    """
    Calls Qt's 'bool QJsonValueConstRef::toBool(bool defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueconstref.html#toBool

    Parameters
    ----------

    defaultValue : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  bool QJsonValueConstRef::toBool(bool defaultValue) const
    return self.uglySide.call(
        'ritual_ZNK18QJsonValueConstRef6toBoolEb', defaultValue,
    )

  @overload()
  @overload(int)
  def toInt(self, defaultValue: int = 0) -> int:
    """
    Calls Qt's 'int QJsonValueConstRef::toInt(int defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueconstref.html#toInt

    Parameters
    ----------

    defaultValue : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  int QJsonValueConstRef::toInt(int defaultValue) const
    return self.uglySide.call(
        'ritual_ZNK18QJsonValueConstRef5toIntEi', defaultValue,
    )

  @overload()
  @overload(int)
  def toInteger(self, defaultValue: int = 0) -> int:
    """
    Calls Qt's 'qint64 QJsonValueConstRef::toInteger(qint64 defaultValue)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueconstref.html#toInteger

    Parameters
    ----------

    defaultValue : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  qint64 QJsonValueConstRef::toInteger(qint64 defaultValue) const
    return self.uglySide.call(
        'ritual_ZNK18QJsonValueConstRef9toIntegerEx', defaultValue,
    )

  @overload()
  @overload(float)
  def toDouble(self, defaultValue: float = 0.0) -> float:
    """
    Calls Qt's 'double QJsonValueConstRef::toDouble(double defaultValue)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueconstref.html#toDouble

    Parameters
    ----------

    defaultValue : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  double QJsonValueConstRef::toDouble(double defaultValue) const
    return self.uglySide.call(
        'ritual_ZNK18QJsonValueConstRef8toDoubleEd', defaultValue,
    )

  @overload()
  @overload(str)
  def toString(self, defaultValue: str = '') -> str:
    """
    Calls Qt's 'QString QJsonValueConstRef::toString(const QString
    &defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueconstref.html#toString

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
    #  QString QJsonValueConstRef::toString(const QString &defaultValue)
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QJsonValueConstRef8toStringERK7QString', defaultValue,
    )

  @overload()
  @overload(str)
  def toStringView(self, defaultValue: str = '') -> str:
    """
    Calls Qt's 'QAnyStringView
    QJsonValueConstRef::toStringView(QAnyStringView defaultValue) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsonvalueconstref.html#toStringView

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
    #  QAnyStringView QJsonValueConstRef::toStringView(QAnyStringView
    #      defaultValue) const
    return self.uglySide.call(
        'ritual_ZNK18QJsonValueConstRef12toStringViewE14QAnyStringView',
        defaultValue,
    )

  def toArray(self) -> QJsonArray:
    """
    Calls Qt's 'QJsonArray QJsonValueConstRef::toArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueconstref.html#toArray

    Returns
    -------

    QJsonArray
      A new cute QJsonArray around the copy Qt gave back. Python owns it.
    """
    #  QJsonArray QJsonValueConstRef::toArray() const
    address = self.uglySide.call('ritual_ZNK18QJsonValueConstRef7toArrayEv')
    from . import QJsonArray
    return QJsonArray._cuteOwning(address)

  def toObject(self) -> QJsonObject:
    """
    Calls Qt's 'QJsonObject QJsonValueConstRef::toObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueconstref.html#toObject

    Returns
    -------

    QJsonObject
      A new cute QJsonObject around the copy Qt gave back. Python owns it.
    """
    #  QJsonObject QJsonValueConstRef::toObject() const
    address = self.uglySide.call('ritual_ZNK18QJsonValueConstRef8toObjectEv')
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
    Calls Qt's 'const QJsonValue QJsonValueConstRef::operator[](QStringView
    key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueconstref.html#operator[]

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QJsonValue
      A new cute QJsonValue around the copy Qt gave back. Python owns it.
    """
    #  const QJsonValue QJsonValueConstRef::operator[](QStringView key) const
    address = self.uglySide.call(
        'ritual_ZNK18QJsonValueConstRefixE11QStringView', key,
    )
    return QJsonValue._cuteOwning(address)

  @overload(QLatin1String)
  def __getitem__(self, key: QLatin1String) -> QJsonValue:
    """
    Calls Qt's 'const QJsonValue
    QJsonValueConstRef::operator[](QLatin1StringView key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueconstref.html#operator[]

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
    #  const QJsonValue QJsonValueConstRef::operator[](QLatin1StringView key)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QJsonValueConstRefixE13QLatin1String',
        self._valueOf(key),
    )
    return QJsonValue._cuteOwning(address)

  @overload(int)
  def __getitem__(self, i: int) -> QJsonValue:
    """
    Calls Qt's 'const QJsonValue QJsonValueConstRef::operator[](qsizetype i)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueconstref.html#operator[]

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QJsonValue
      A new cute QJsonValue around the copy Qt gave back. Python owns it.
    """
    #  const QJsonValue QJsonValueConstRef::operator[](qsizetype i) const
    address = self.uglySide.call('ritual_ZNK18QJsonValueConstRefixEx', i)
    return QJsonValue._cuteOwning(address)

  @overload(THIS)
  def __eq__(self, rhs: QJsonValueConstRef) -> bool:
    """
    Calls Qt's 'bool operator==(const QJsonValueConstRef &lhs, const
    QJsonValueConstRef &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueconstref.html#operator==

    Parameters
    ----------

    rhs : QJsonValueConstRef
      Passed on as a value: Qt reads the C++ QJsonValueConstRef, which stays
      Python's own.
    """
    #  bool operator==(const QJsonValueConstRef &lhs, const
    #      QJsonValueConstRef &rhs)
    return Rituals.call(
        'ritual_ZeqRK18QJsonValueConstRefS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QJsonValue)
  def __eq__(self, rhs: QJsonValue) -> bool:
    """
    Calls Qt's 'bool operator==(const QJsonValueConstRef &lhs, const
    QJsonValue &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueconstref.html#operator==

    Parameters
    ----------

    rhs : QJsonValue
      Passed on as a value: Qt reads the C++ QJsonValue, which stays Python's
      own.
    """
    #  bool operator==(const QJsonValueConstRef &lhs, const QJsonValue &rhs)
    return Rituals.call(
        'ritual_ZeqRK18QJsonValueConstRefRK10QJsonValue',
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
  def __ne__(self, rhs: QJsonValueConstRef) -> bool:
    """
    Calls Qt's 'bool operator!=(const QJsonValueConstRef &lhs, const
    QJsonValueConstRef &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueconstref.html#operator!=

    Parameters
    ----------

    rhs : QJsonValueConstRef
      Passed on as a value: Qt reads the C++ QJsonValueConstRef, which stays
      Python's own.
    """
    #  bool operator!=(const QJsonValueConstRef &lhs, const
    #      QJsonValueConstRef &rhs)
    return Rituals.call(
        'ritual_ZneRK18QJsonValueConstRefS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QJsonValue)
  def __ne__(self, rhs: QJsonValue) -> bool:
    """
    Calls Qt's 'bool operator!=(const QJsonValueConstRef &lhs, const
    QJsonValue &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueconstref.html#operator!=

    Parameters
    ----------

    rhs : QJsonValue
      Passed on as a value: Qt reads the C++ QJsonValue, which stays Python's
      own.
    """
    #  bool operator!=(const QJsonValueConstRef &lhs, const QJsonValue &rhs)
    return Rituals.call(
        'ritual_ZneRK18QJsonValueConstRefRK10QJsonValue',
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
  def __init__(self, a0: QJsonValueConstRef) -> None:
    """
    Notes what was given, for Qt's
    'QJsonValueConstRef::QJsonValueConstRef(const QJsonValueConstRef &a0)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsonvalueconstref.html#QJsonValueConstRef

    Parameters
    ----------

    a0 : QJsonValueConstRef
      Passed on as a value: Qt reads the C++ QJsonValueConstRef, which stays
      Python's own.
    """
    #  QJsonValueConstRef::QJsonValueConstRef(const QJsonValueConstRef &a0)
    self._noteCreation(QJsonValueConstRef, lambda: Rituals.call(
        'ritual_ZN18QJsonValueConstRefC1ERKS_', self._valueOf(a0),
    ))

  @overload(QJsonArray, int)
  @overload(NoneType, int)
  def __init__(self, array: Optional[QJsonArray], idx: int) -> None:
    """
    Notes what was given, for Qt's
    'QJsonValueConstRef::QJsonValueConstRef(QJsonArray *array, qsizetype
    idx)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsonvalueconstref.html#QJsonValueConstRef

    Parameters
    ----------

    array : Optional[QJsonArray]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    idx : int
      Passed on as it is.
    """
    #  QJsonValueConstRef::QJsonValueConstRef(QJsonArray *array, qsizetype
    #      idx)
    self._noteCreation(QJsonValueConstRef, lambda: Rituals.call(
        'ritual_ZN18QJsonValueConstRefC1EP10QJsonArrayx',
        self._addressOf(array), idx,
    ))

  @overload(QJsonObject, int)
  def __init__(self, object: Optional[QJsonObject], idx: int) -> None:
    """
    Notes what was given, for Qt's
    'QJsonValueConstRef::QJsonValueConstRef(QJsonObject *object, qsizetype
    idx)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsonvalueconstref.html#QJsonValueConstRef

    Parameters
    ----------

    object : Optional[QJsonObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    idx : int
      Passed on as it is.
    """
    #  QJsonValueConstRef::QJsonValueConstRef(QJsonObject *object, qsizetype
    #      idx)
    self._noteCreation(QJsonValueConstRef, lambda: Rituals.call(
        'ritual_ZN18QJsonValueConstRefC1EP11QJsonObjectx',
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

  @overload(THIS)
  def rebind(self, other: QJsonValueConstRef) -> None:
    """
    Calls Qt's 'void QJsonValueConstRef::rebind(QJsonValueConstRef other)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalueconstref.html#rebind

    Parameters
    ----------

    other : QJsonValueConstRef
      Passed on as a value: Qt reads the C++ QJsonValueConstRef, which stays
      Python's own.
    """
    #  void QJsonValueConstRef::rebind(QJsonValueConstRef other)
    self.uglySide.call(
        'ritual_ZN18QJsonValueConstRef6rebindES_', self._valueOf(other),
    )
