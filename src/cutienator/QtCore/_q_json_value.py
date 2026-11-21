"""
QJsonValue binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qjsonvalue.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QJsonDocument

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QByteArray, QByteArrayView, QJsonArray, QJsonObject
  from . import QJsonParseError, QLatin1String, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArrayView = WAIT['QByteArrayView']
  QJsonArray = WAIT['QJsonArray']
  QJsonObject = WAIT['QJsonObject']
  QJsonParseError = WAIT['QJsonParseError']
  QLatin1String = WAIT['QLatin1String']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QJsonValue(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QJsonValue: a plain Python object standing in front
  of one C++ QJsonValue.

  C++ hands a QJsonValue around as a copy, so every C++ QJsonValue behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QJsonValue that has a ritual and that Python can
  call so far, 20 names in all: 'fromVariant', 'toVariant', 'fromJson',
  'toJson', 'type', 'isNull', 'isBool', 'isDouble', 'isString', 'isArray',
  'isObject', 'isUndefined', 'toBool', 'toInt', 'toInteger', 'toDouble',
  'toString', 'toStringView', 'toArray', 'toObject'. It can be made from
  Python, in 10 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QJsonValue::QJsonValue(qint64 v)': takes in Python what
    'QJsonValue::QJsonValue(int n)' takes.
  - Qt's 'QJsonValue::~QJsonValue()': the destructor: Python removes its C++
    QJsonValue by it, and has no other use for it.
  - Qt's 'const QJsonValue QJsonValue::operator[](const QString &key) const':
    an operator, which is not reflected yet.
  - Qt's 'const QJsonValue QJsonValue::operator[](QStringView key) const': an
    operator, which is not reflected yet.
  - Qt's 'const QJsonValue QJsonValue::operator[](QLatin1StringView key)
    const': an operator, which is not reflected yet.
  - Qt's 'const QJsonValue QJsonValue::operator[](qsizetype i) const': an
    operator, which is not reflected yet.

  What has no ritual
  ------------------

  7 of the 46 functions Qt declares: 6 takes or gives a type that cannot be
  passed yet; 1 forbidden.

  What to expect
  --------------

  - The C++ QJsonValue is created at the first use, not by 'QJsonValue(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QJsonValue back gives a copy the ritual made for
    Python, in a new cute QJsonValue.
  """

  #  The enums Qt writes inside QJsonValue, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum):
    """The enum 'QJsonValue::Type' of Qt, with the 7 names Qt gives in it."""

    Null = Kee[int](0)
    Bool = Kee[int](1)
    Double = Kee[int](2)
    String = Kee[int](3)
    Array = Kee[int](4)
    Object = Kee[int](5)
    Undefined = Kee[int](128)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QVariant)
  def fromVariant(variant: QVariant) -> QJsonValue:
    """
    Calls Qt's 'QJsonValue QJsonValue::fromVariant(const QVariant &variant)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#fromVariant

    Parameters
    ----------

    variant : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QJsonValue
      A new cute QJsonValue around the copy Qt gave back. Python owns it.
    """
    #  QJsonValue QJsonValue::fromVariant(const QVariant &variant)
    address = Rituals.call(
        'ritual_ZN10QJsonValue11fromVariantERK8QVariant',
        CuteMixin._valueOf(variant),
    )
    return QJsonValue._cuteOwning(address)

  @staticmethod
  @overload(QByteArrayView)
  @overload(QByteArrayView, QJsonParseError)
  @overload(QByteArrayView, NoneType)
  def fromJson(
      json: QByteArrayView,
      error: Optional[QJsonParseError] = None,
  ) -> QJsonValue:
    """
    Calls Qt's 'QJsonValue QJsonValue::fromJson(QByteArrayView json,
    QJsonParseError *error)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#fromJson

    Parameters
    ----------

    json : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    error : Optional[QJsonParseError]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QJsonValue
      A new cute QJsonValue around the copy Qt gave back. Python owns it.
    """
    #  QJsonValue QJsonValue::fromJson(QByteArrayView json, QJsonParseError
    #      *error)
    address = Rituals.call(
        'ritual_ZN10QJsonValue8fromJsonE14QByteArrayViewP15QJsonParseError',
        CuteMixin._valueOf(json), CuteMixin._addressOf(error),
    )
    return QJsonValue._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QJsonValue'

  #  Qt's '~QJsonValue()'. Naming it makes this a value class: Python owns
  #  every C++ QJsonValue behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QJsonValueD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toVariant(self) -> QVariant:
    """
    Calls Qt's 'QVariant QJsonValue::toVariant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#toVariant

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QJsonValue::toVariant() const
    address = self.uglySide.call('ritual_ZNK10QJsonValue9toVariantEv')
    from . import QVariant
    return QVariant._cuteOwning(address)

  @overload()
  @overload(QJsonDocument.JsonFormat)
  def toJson(
      self,
      format: QJsonDocument.JsonFormat = QJsonDocument.JsonFormat.Indented,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray QJsonValue::toJson(JsonFormat format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#toJson

    Parameters
    ----------

    format : QJsonDocument.JsonFormat
      Passed on as its number. May be left out, as in Qt: it is then
      QJsonDocument.JsonFormat.Indented.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QJsonValue::toJson(JsonFormat format) const
    address = self.uglySide.call(
        'ritual_ZNK10QJsonValue6toJsonEN13QJsonDocument10JsonFormatE',
        format.value,
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def type(self) -> Type:
    """
    Calls Qt's 'Type QJsonValue::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QJsonValue::type() const
    return QJsonValue.Type(self.uglySide.call(
        'ritual_ZNK10QJsonValue4typeEv',
    ))

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QJsonValue::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#isNull
    """
    #  bool QJsonValue::isNull() const
    return self.uglySide.call('ritual_ZNK10QJsonValue6isNullEv')

  def isBool(self) -> bool:
    """
    Calls Qt's 'bool QJsonValue::isBool() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#isBool
    """
    #  bool QJsonValue::isBool() const
    return self.uglySide.call('ritual_ZNK10QJsonValue6isBoolEv')

  def isDouble(self) -> bool:
    """
    Calls Qt's 'bool QJsonValue::isDouble() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#isDouble
    """
    #  bool QJsonValue::isDouble() const
    return self.uglySide.call('ritual_ZNK10QJsonValue8isDoubleEv')

  def isString(self) -> bool:
    """
    Calls Qt's 'bool QJsonValue::isString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#isString
    """
    #  bool QJsonValue::isString() const
    return self.uglySide.call('ritual_ZNK10QJsonValue8isStringEv')

  def isArray(self) -> bool:
    """
    Calls Qt's 'bool QJsonValue::isArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#isArray
    """
    #  bool QJsonValue::isArray() const
    return self.uglySide.call('ritual_ZNK10QJsonValue7isArrayEv')

  def isObject(self) -> bool:
    """
    Calls Qt's 'bool QJsonValue::isObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#isObject
    """
    #  bool QJsonValue::isObject() const
    return self.uglySide.call('ritual_ZNK10QJsonValue8isObjectEv')

  def isUndefined(self) -> bool:
    """
    Calls Qt's 'bool QJsonValue::isUndefined() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#isUndefined
    """
    #  bool QJsonValue::isUndefined() const
    return self.uglySide.call('ritual_ZNK10QJsonValue11isUndefinedEv')

  @overload()
  @overload(bool)
  def toBool(self, defaultValue: bool = False) -> bool:
    """
    Calls Qt's 'bool QJsonValue::toBool(bool defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#toBool

    Parameters
    ----------

    defaultValue : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  bool QJsonValue::toBool(bool defaultValue) const
    return self.uglySide.call(
        'ritual_ZNK10QJsonValue6toBoolEb', defaultValue,
    )

  @overload()
  @overload(int)
  def toInt(self, defaultValue: int = 0) -> int:
    """
    Calls Qt's 'int QJsonValue::toInt(int defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#toInt

    Parameters
    ----------

    defaultValue : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  int QJsonValue::toInt(int defaultValue) const
    return self.uglySide.call('ritual_ZNK10QJsonValue5toIntEi', defaultValue)

  @overload()
  @overload(int)
  def toInteger(self, defaultValue: int = 0) -> int:
    """
    Calls Qt's 'qint64 QJsonValue::toInteger(qint64 defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#toInteger

    Parameters
    ----------

    defaultValue : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  qint64 QJsonValue::toInteger(qint64 defaultValue) const
    return self.uglySide.call(
        'ritual_ZNK10QJsonValue9toIntegerEx', defaultValue,
    )

  @overload()
  @overload(float)
  def toDouble(self, defaultValue: float = 0.0) -> float:
    """
    Calls Qt's 'double QJsonValue::toDouble(double defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#toDouble

    Parameters
    ----------

    defaultValue : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  double QJsonValue::toDouble(double defaultValue) const
    return self.uglySide.call(
        'ritual_ZNK10QJsonValue8toDoubleEd', defaultValue,
    )

  @overload()
  def toString(self) -> str:
    """
    Calls Qt's 'QString QJsonValue::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QJsonValue::toString() const
    return self.uglySide.call('ritual_ZNK10QJsonValue8toStringEv')

  @overload(str)
  def toString(self, defaultValue: str) -> str:
    """
    Calls Qt's 'QString QJsonValue::toString(const QString &defaultValue)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#toString

    Parameters
    ----------

    defaultValue : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QJsonValue::toString(const QString &defaultValue) const
    return self.uglySide.call(
        'ritual_ZNK10QJsonValue8toStringERK7QString', defaultValue,
    )

  @overload()
  @overload(str)
  def toStringView(self, defaultValue: str = '') -> str:
    """
    Calls Qt's 'QAnyStringView QJsonValue::toStringView(QAnyStringView
    defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#toStringView

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
    #  QAnyStringView QJsonValue::toStringView(QAnyStringView defaultValue)
    #      const
    return self.uglySide.call(
        'ritual_ZNK10QJsonValue12toStringViewE14QAnyStringView',
        defaultValue,
    )

  @overload()
  def toArray(self) -> QJsonArray:
    """
    Calls Qt's 'QJsonArray QJsonValue::toArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#toArray

    Returns
    -------

    QJsonArray
      A new cute QJsonArray around the copy Qt gave back. Python owns it.
    """
    #  QJsonArray QJsonValue::toArray() const
    address = self.uglySide.call('ritual_ZNK10QJsonValue7toArrayEv')
    from . import QJsonArray
    return QJsonArray._cuteOwning(address)

  @overload(QJsonArray)
  def toArray(self, defaultValue: QJsonArray) -> QJsonArray:
    """
    Calls Qt's 'QJsonArray QJsonValue::toArray(const QJsonArray
    &defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#toArray

    Parameters
    ----------

    defaultValue : QJsonArray
      Passed on as a value: Qt reads the C++ QJsonArray, which stays Python's
      own.

    Returns
    -------

    QJsonArray
      A new cute QJsonArray around the copy Qt gave back. Python owns it.
    """
    #  QJsonArray QJsonValue::toArray(const QJsonArray &defaultValue) const
    address = self.uglySide.call(
        'ritual_ZNK10QJsonValue7toArrayERK10QJsonArray',
        self._valueOf(defaultValue),
    )
    from . import QJsonArray
    return QJsonArray._cuteOwning(address)

  @overload()
  def toObject(self) -> QJsonObject:
    """
    Calls Qt's 'QJsonObject QJsonValue::toObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#toObject

    Returns
    -------

    QJsonObject
      A new cute QJsonObject around the copy Qt gave back. Python owns it.
    """
    #  QJsonObject QJsonValue::toObject() const
    address = self.uglySide.call('ritual_ZNK10QJsonValue8toObjectEv')
    from . import QJsonObject
    return QJsonObject._cuteOwning(address)

  @overload(QJsonObject)
  def toObject(self, defaultValue: QJsonObject) -> QJsonObject:
    """
    Calls Qt's 'QJsonObject QJsonValue::toObject(const QJsonObject
    &defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#toObject

    Parameters
    ----------

    defaultValue : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.

    Returns
    -------

    QJsonObject
      A new cute QJsonObject around the copy Qt gave back. Python owns it.
    """
    #  QJsonObject QJsonValue::toObject(const QJsonObject &defaultValue)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10QJsonValue8toObjectERK11QJsonObject',
        self._valueOf(defaultValue),
    )
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(Type)
  def __init__(self, a0: Type = Type.Null) -> None:
    """
    Notes what was given, for Qt's 'QJsonValue::QJsonValue(Type a0)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#QJsonValue

    Parameters
    ----------

    a0 : Type
      Passed on as its number. May be left out, as in Qt: it is then
      Type.Null.
    """
    #  QJsonValue::QJsonValue(Type a0)
    self._noteCreation(QJsonValue, lambda: Rituals.call(
        'ritual_ZN10QJsonValueC1ENS_4TypeE', a0.value,
    ))

  @overload(bool)
  def __init__(self, b: bool) -> None:
    """
    Notes what was given, for Qt's 'QJsonValue::QJsonValue(bool b)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#QJsonValue

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  QJsonValue::QJsonValue(bool b)
    self._noteCreation(QJsonValue, lambda: Rituals.call(
        'ritual_ZN10QJsonValueC1Eb', b,
    ))

  @overload(float)
  def __init__(self, n: float) -> None:
    """
    Notes what was given, for Qt's 'QJsonValue::QJsonValue(double n)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#QJsonValue

    Parameters
    ----------

    n : float
      Passed on as it is.
    """
    #  QJsonValue::QJsonValue(double n)
    self._noteCreation(QJsonValue, lambda: Rituals.call(
        'ritual_ZN10QJsonValueC1Ed', n,
    ))

  @overload(int)
  def __init__(self, n: int) -> None:
    """
    Notes what was given, for Qt's 'QJsonValue::QJsonValue(int n)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#QJsonValue

    Parameters
    ----------

    n : int
      Passed on as it is.
    """
    #  QJsonValue::QJsonValue(int n)
    self._noteCreation(QJsonValue, lambda: Rituals.call(
        'ritual_ZN10QJsonValueC1Ei', n,
    ))

  @overload(str)
  def __init__(self, s: str) -> None:
    """
    Notes what was given, for Qt's 'QJsonValue::QJsonValue(const QString
    &s)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#QJsonValue

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QJsonValue::QJsonValue(const QString &s)
    self._noteCreation(QJsonValue, lambda: Rituals.call(
        'ritual_ZN10QJsonValueC1ERK7QString', s,
    ))

  @overload(QLatin1String)
  def __init__(self, s: QLatin1String) -> None:
    """
    Notes what was given, for Qt's 'QJsonValue::QJsonValue(QLatin1StringView
    s)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#QJsonValue

    Parameters
    ----------

    s : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  QJsonValue::QJsonValue(QLatin1StringView s)
    self._noteCreation(QJsonValue, lambda: Rituals.call(
        'ritual_ZN10QJsonValueC1E13QLatin1String', self._valueOf(s),
    ))

  @overload(NoneType)
  def __init__(self, s: Optional[str]) -> None:
    """
    Notes what was given, for Qt's 'QJsonValue::QJsonValue(const char *s)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#QJsonValue

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  QJsonValue::QJsonValue(const char *s)
    self._noteCreation(QJsonValue, lambda: Rituals.call(
        'ritual_ZN10QJsonValueC1EPKc', self._bytesOf(s),
    ))

  @overload(QJsonArray)
  def __init__(self, a: QJsonArray) -> None:
    """
    Notes what was given, for Qt's 'QJsonValue::QJsonValue(const QJsonArray
    &a)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#QJsonValue

    Parameters
    ----------

    a : QJsonArray
      Passed on as a value: Qt reads the C++ QJsonArray, which stays Python's
      own.
    """
    #  QJsonValue::QJsonValue(const QJsonArray &a)
    self._noteCreation(QJsonValue, lambda: Rituals.call(
        'ritual_ZN10QJsonValueC1ERK10QJsonArray', self._valueOf(a),
    ))

  @overload(QJsonObject)
  def __init__(self, o: QJsonObject) -> None:
    """
    Notes what was given, for Qt's 'QJsonValue::QJsonValue(const QJsonObject
    &o)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#QJsonValue

    Parameters
    ----------

    o : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  QJsonValue::QJsonValue(const QJsonObject &o)
    self._noteCreation(QJsonValue, lambda: Rituals.call(
        'ritual_ZN10QJsonValueC1ERK11QJsonObject', self._valueOf(o),
    ))

  @overload(THIS)
  def __init__(self, other: QJsonValue) -> None:
    """
    Notes what was given, for Qt's 'QJsonValue::QJsonValue(const QJsonValue
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsonvalue.html#QJsonValue

    Parameters
    ----------

    other : QJsonValue
      Passed on as a value: Qt reads the C++ QJsonValue, which stays Python's
      own.
    """
    #  QJsonValue::QJsonValue(const QJsonValue &other)
    self._noteCreation(QJsonValue, lambda: Rituals.call(
        'ritual_ZN10QJsonValueC1ERKS_', self._valueOf(other),
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
