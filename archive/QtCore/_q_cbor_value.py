"""
QCborValue binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qcborvalue.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QByteArray, QCborArray, QCborMap, QCborParserError, QDateTime
  from . import QJsonValue, QLatin1String, QRegularExpression, QUrl, QUuid
  from . import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QCborArray = WAIT['QCborArray']
  QCborMap = WAIT['QCborMap']
  QCborParserError = WAIT['QCborParserError']
  QDateTime = WAIT['QDateTime']
  QJsonValue = WAIT['QJsonValue']
  QLatin1String = WAIT['QLatin1String']
  QRegularExpression = WAIT['QRegularExpression']
  QUrl = WAIT['QUrl']
  QUuid = WAIT['QUuid']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCborValue(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCborValue: a plain Python object standing in front
  of one C++ QCborValue.

  C++ hands a QCborValue around as a copy, so every C++ QCborValue behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCborValue that has a ritual and that Python can
  call so far, 52 names in all: 'type', 'isInteger', 'isByteArray',
  'isString', 'isArray', 'isMap', 'isTag', 'isFalse', 'isTrue', 'isBool',
  'isNull', 'isUndefined', 'isDouble', 'isDateTime', 'isUrl',
  'isRegularExpression', 'isUuid', 'isInvalid', 'isContainer',
  'isSimpleType', 'toInteger', 'toBool', 'toDouble', 'taggedValue',
  'toByteArray', 'toString', 'toStringView', 'toDateTime', 'toUrl',
  'toRegularExpression', 'toUuid', 'toArray', 'toMap', '__getitem__',
  'compare', 'fromVariant', 'toVariant', 'fromJsonValue', 'toJsonValue',
  'fromCbor', 'toCbor', 'toDiagnosticNotation', '__eq__', '__ne__', '__lt__',
  '__gt__', '__le__', '__ge__', 'dispose', 'value_helper', 'fp_helper',
  'isTag_helper'. It can be made from Python, in 16 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCborValue::QCborValue(unsigned int u)': takes in Python what
    'QCborValue::QCborValue(int i)' takes.
  - Qt's 'QCborValue::QCborValue(qint64 i)': takes in Python what
    'QCborValue::QCborValue(int i)' takes.
  - Qt's 'QCborValue::QCborValue(QCborSimpleType st)': names the enum
    'QCborSimpleType', whose class cannot be named here.
  - Qt's 'QCborValue::QCborValue(QStringView s)': takes in Python what
    'QCborValue::QCborValue(const QString &s)' takes.
  - Qt's 'QCborValue::QCborValue(QCborTag tag, const QCborValue
    &taggedValue)': names the enum 'QCborTag', whose class cannot be named
    here.
  - Qt's 'QCborValue::QCborValue(QCborKnownTags t_, const QCborValue &tv)':
    names the enum 'QCborKnownTags', whose class cannot be named here.
  - Qt's 'QCborValue::~QCborValue()': the destructor: Python removes its C++
    QCborValue by it, and has no other use for it.
  - Qt's 'bool QCborValue::isSimpleType(QCborSimpleType st) const': names the
    enum 'QCborSimpleType', whose class cannot be named here.
  - Qt's 'QCborSimpleType QCborValue::toSimpleType(QCborSimpleType
    defaultValue) const': names the enum 'QCborSimpleType', whose class
    cannot be named here.
  - Qt's 'QCborTag QCborValue::tag(QCborTag defaultValue) const': names the
    enum 'QCborTag', whose class cannot be named here.
  - Qt's 'QCborValueRef QCborValue::operator[](qint64 key)': takes in Python
    what 'const QCborValue QCborValue::operator[](qint64 key) const' takes.
  - Qt's 'QCborValueRef QCborValue::operator[](QLatin1StringView key)': takes
    in Python what 'const QCborValue QCborValue::operator[](QLatin1StringView
    key) const' takes.
  - Qt's 'QCborValueRef QCborValue::operator[](const QString &key)': takes in
    Python what 'const QCborValue QCborValue::operator[](const QString &key)
    const' takes.
  - Qt's 'Type QCborValue::type_helper(QCborSimpleType st)': names the enum
    'QCborSimpleType', whose class cannot be named here.

  What has no ritual
  ------------------

  14 of the 101 functions Qt declares: 10 takes or gives a type that cannot
  be passed yet; 2 declared and nowhere to be found; 1 a template; 1
  forbidden.

  What to expect
  --------------

  - The C++ QCborValue is created at the first use, not by 'QCborValue(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCborValue back gives a copy the ritual made for
    Python, in a new cute QCborValue.
  """

  #  The enums Qt writes inside QCborValue, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class DiagnosticNotationOption(CuteFlags):
    """
    The flags enum 'QCborValue::DiagnosticNotationOption' of Qt, with the 3
    names Qt gives in it. Qt names the type of its combinations
    'QCborValue::DiagnosticNotationOptions'.
    """

    Compact = 0x0
    LineWrapped = 0x1
    ExtendedFormat = 0x2

  DiagnosticNotationOptions = DiagnosticNotationOption

  class EncodingOption(CuteFlags):
    """
    The flags enum 'QCborValue::EncodingOption' of Qt, with the 5 names Qt
    gives in it. Qt names the type of its combinations
    'QCborValue::EncodingOptions'.
    """

    SortKeysInMaps = 0x1
    UseFloat = 0x2
    UseFloat16 = 0x6
    UseIntegers = 0x8
    NoTransformation = 0x0

  EncodingOptions = EncodingOption

  class Type(CuteNum):
    """
    The enum 'QCborValue::Type' of Qt, with the 17 names Qt gives in it.
    """

    Integer = Kee[int](0)
    ByteArray = Kee[int](64)
    String = Kee[int](96)
    Array = Kee[int](128)
    Map = Kee[int](160)
    Tag = Kee[int](192)
    SimpleType = Kee[int](256)
    FALSE = Kee[int](276)
    TRUE = Kee[int](277)
    Null = Kee[int](278)
    Undefined = Kee[int](279)
    Double = Kee[int](514)
    DateTime = Kee[int](65536)
    Url = Kee[int](65568)
    RegularExpression = Kee[int](65571)
    Uuid = Kee[int](65573)
    Invalid = Kee[int](-1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QVariant)
  def fromVariant(variant: QVariant) -> QCborValue:
    """
    Calls Qt's 'QCborValue QCborValue::fromVariant(const QVariant &variant)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#fromVariant

    Parameters
    ----------

    variant : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  QCborValue QCborValue::fromVariant(const QVariant &variant)
    address = Rituals.call(
        'ritual_ZN10QCborValue11fromVariantERK8QVariant',
        CuteMixin._valueOf(variant),
    )
    return QCborValue._cuteOwning(address)

  @staticmethod
  @overload(QJsonValue)
  def fromJsonValue(v: QJsonValue) -> QCborValue:
    """
    Calls Qt's 'QCborValue QCborValue::fromJsonValue(const QJsonValue &v)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#fromJsonValue

    Parameters
    ----------

    v : QJsonValue
      Passed on as a value: Qt reads the C++ QJsonValue, which stays Python's
      own.

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  QCborValue QCborValue::fromJsonValue(const QJsonValue &v)
    address = Rituals.call(
        'ritual_ZN10QCborValue13fromJsonValueERK10QJsonValue',
        CuteMixin._valueOf(v),
    )
    return QCborValue._cuteOwning(address)

  @staticmethod
  @overload(QByteArray)
  @overload(QByteArray, QCborParserError)
  @overload(QByteArray, NoneType)
  def fromCbor(
      ba: QByteArray,
      error: Optional[QCborParserError] = None,
  ) -> QCborValue:
    """
    Calls Qt's 'QCborValue QCborValue::fromCbor(const QByteArray &ba,
    QCborParserError *error)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#fromCbor

    Parameters
    ----------

    ba : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    error : Optional[QCborParserError]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  QCborValue QCborValue::fromCbor(const QByteArray &ba, QCborParserError
    #      *error)
    address = Rituals.call(
        'ritual_ZN10QCborValue8fromCborERK10QByteArrayP16QCborParserError',
        CuteMixin._valueOf(ba), CuteMixin._addressOf(error),
    )
    return QCborValue._cuteOwning(address)

  @staticmethod
  @overload(str, int)
  @overload(NoneType, int)
  @overload(str, int, QCborParserError)
  @overload(str, int, NoneType)
  @overload(NoneType, int, QCborParserError)
  @overload(NoneType, int, NoneType)
  def fromCbor(
      data: Optional[str],
      len: int,
      error: Optional[QCborParserError] = None,
  ) -> QCborValue:
    """
    Calls Qt's 'QCborValue QCborValue::fromCbor(const char *data, qsizetype
    len, QCborParserError *error)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#fromCbor

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.

    error : Optional[QCborParserError]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  QCborValue QCborValue::fromCbor(const char *data, qsizetype len,
    #      QCborParserError *error)
    address = Rituals.call(
        'ritual_ZN10QCborValue8fromCborEPKcxP16QCborParserError',
        CuteMixin._bytesOf(data), len, CuteMixin._addressOf(error),
    )
    return QCborValue._cuteOwning(address)

  @staticmethod
  @overload(Type)
  def isTag_helper(tt: Type) -> bool:
    """
    Calls Qt's 'bool QCborValue::isTag_helper(Type tt)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#isTag_helper

    Parameters
    ----------

    tt : Type
      Passed on as its number.
    """
    #  bool QCborValue::isTag_helper(Type tt)
    return Rituals.call(
        'ritual_ZN10QCborValue12isTag_helperENS_4TypeE', tt.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCborValue'

  #  Qt's '~QCborValue()'. Naming it makes this a value class: Python owns
  #  every C++ QCborValue behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QCborValueD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> Type:
    """
    Calls Qt's 'Type QCborValue::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QCborValue::type() const
    return QCborValue.Type(self.uglySide.call(
        'ritual_ZNK10QCborValue4typeEv',
    ))

  def isInteger(self) -> bool:
    """
    Calls Qt's 'bool QCborValue::isInteger() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#isInteger
    """
    #  bool QCborValue::isInteger() const
    return self.uglySide.call('ritual_ZNK10QCborValue9isIntegerEv')

  def isByteArray(self) -> bool:
    """
    Calls Qt's 'bool QCborValue::isByteArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#isByteArray
    """
    #  bool QCborValue::isByteArray() const
    return self.uglySide.call('ritual_ZNK10QCborValue11isByteArrayEv')

  def isString(self) -> bool:
    """
    Calls Qt's 'bool QCborValue::isString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#isString
    """
    #  bool QCborValue::isString() const
    return self.uglySide.call('ritual_ZNK10QCborValue8isStringEv')

  def isArray(self) -> bool:
    """
    Calls Qt's 'bool QCborValue::isArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#isArray
    """
    #  bool QCborValue::isArray() const
    return self.uglySide.call('ritual_ZNK10QCborValue7isArrayEv')

  def isMap(self) -> bool:
    """
    Calls Qt's 'bool QCborValue::isMap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#isMap
    """
    #  bool QCborValue::isMap() const
    return self.uglySide.call('ritual_ZNK10QCborValue5isMapEv')

  def isTag(self) -> bool:
    """
    Calls Qt's 'bool QCborValue::isTag() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#isTag
    """
    #  bool QCborValue::isTag() const
    return self.uglySide.call('ritual_ZNK10QCborValue5isTagEv')

  def isFalse(self) -> bool:
    """
    Calls Qt's 'bool QCborValue::isFalse() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#isFalse
    """
    #  bool QCborValue::isFalse() const
    return self.uglySide.call('ritual_ZNK10QCborValue7isFalseEv')

  def isTrue(self) -> bool:
    """
    Calls Qt's 'bool QCborValue::isTrue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#isTrue
    """
    #  bool QCborValue::isTrue() const
    return self.uglySide.call('ritual_ZNK10QCborValue6isTrueEv')

  def isBool(self) -> bool:
    """
    Calls Qt's 'bool QCborValue::isBool() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#isBool
    """
    #  bool QCborValue::isBool() const
    return self.uglySide.call('ritual_ZNK10QCborValue6isBoolEv')

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QCborValue::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#isNull
    """
    #  bool QCborValue::isNull() const
    return self.uglySide.call('ritual_ZNK10QCborValue6isNullEv')

  def isUndefined(self) -> bool:
    """
    Calls Qt's 'bool QCborValue::isUndefined() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#isUndefined
    """
    #  bool QCborValue::isUndefined() const
    return self.uglySide.call('ritual_ZNK10QCborValue11isUndefinedEv')

  def isDouble(self) -> bool:
    """
    Calls Qt's 'bool QCborValue::isDouble() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#isDouble
    """
    #  bool QCborValue::isDouble() const
    return self.uglySide.call('ritual_ZNK10QCborValue8isDoubleEv')

  def isDateTime(self) -> bool:
    """
    Calls Qt's 'bool QCborValue::isDateTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#isDateTime
    """
    #  bool QCborValue::isDateTime() const
    return self.uglySide.call('ritual_ZNK10QCborValue10isDateTimeEv')

  def isUrl(self) -> bool:
    """
    Calls Qt's 'bool QCborValue::isUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#isUrl
    """
    #  bool QCborValue::isUrl() const
    return self.uglySide.call('ritual_ZNK10QCborValue5isUrlEv')

  def isRegularExpression(self) -> bool:
    """
    Calls Qt's 'bool QCborValue::isRegularExpression() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborvalue.html#isRegularExpression
    """
    #  bool QCborValue::isRegularExpression() const
    return self.uglySide.call(
        'ritual_ZNK10QCborValue19isRegularExpressionEv',
    )

  def isUuid(self) -> bool:
    """
    Calls Qt's 'bool QCborValue::isUuid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#isUuid
    """
    #  bool QCborValue::isUuid() const
    return self.uglySide.call('ritual_ZNK10QCborValue6isUuidEv')

  def isInvalid(self) -> bool:
    """
    Calls Qt's 'bool QCborValue::isInvalid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#isInvalid
    """
    #  bool QCborValue::isInvalid() const
    return self.uglySide.call('ritual_ZNK10QCborValue9isInvalidEv')

  def isContainer(self) -> bool:
    """
    Calls Qt's 'bool QCborValue::isContainer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#isContainer
    """
    #  bool QCborValue::isContainer() const
    return self.uglySide.call('ritual_ZNK10QCborValue11isContainerEv')

  def isSimpleType(self) -> bool:
    """
    Calls Qt's 'bool QCborValue::isSimpleType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#isSimpleType
    """
    #  bool QCborValue::isSimpleType() const
    return self.uglySide.call('ritual_ZNK10QCborValue12isSimpleTypeEv')

  @overload()
  @overload(int)
  def toInteger(self, defaultValue: int = 0) -> int:
    """
    Calls Qt's 'qint64 QCborValue::toInteger(qint64 defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#toInteger

    Parameters
    ----------

    defaultValue : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  qint64 QCborValue::toInteger(qint64 defaultValue) const
    return self.uglySide.call(
        'ritual_ZNK10QCborValue9toIntegerEx', defaultValue,
    )

  @overload()
  @overload(bool)
  def toBool(self, defaultValue: bool = False) -> bool:
    """
    Calls Qt's 'bool QCborValue::toBool(bool defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#toBool

    Parameters
    ----------

    defaultValue : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  bool QCborValue::toBool(bool defaultValue) const
    return self.uglySide.call(
        'ritual_ZNK10QCborValue6toBoolEb', defaultValue,
    )

  @overload()
  @overload(float)
  def toDouble(self, defaultValue: float = 0.0) -> float:
    """
    Calls Qt's 'double QCborValue::toDouble(double defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#toDouble

    Parameters
    ----------

    defaultValue : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  double QCborValue::toDouble(double defaultValue) const
    return self.uglySide.call(
        'ritual_ZNK10QCborValue8toDoubleEd', defaultValue,
    )

  @overload()
  @overload(THIS)
  def taggedValue(
      self,
      defaultValue: Optional[QCborValue] = None,
  ) -> QCborValue:
    """
    Calls Qt's 'QCborValue QCborValue::taggedValue(const QCborValue
    &defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#taggedValue

    Parameters
    ----------

    defaultValue : Optional[QCborValue]
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own. May be left out, as in Qt: a new 'QCborValue()' is then passed on.

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  QCborValue QCborValue::taggedValue(const QCborValue &defaultValue)
    #      const
    if defaultValue is None:
      defaultValue = QCborValue()
    address = self.uglySide.call(
        'ritual_ZNK10QCborValue11taggedValueERKS_',
        self._valueOf(defaultValue),
    )
    return QCborValue._cuteOwning(address)

  @overload()
  @overload(QByteArray)
  def toByteArray(
      self,
      defaultValue: Optional[QByteArray] = None,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray QCborValue::toByteArray(const QByteArray
    &defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#toByteArray

    Parameters
    ----------

    defaultValue : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QCborValue::toByteArray(const QByteArray &defaultValue)
    #      const
    if defaultValue is None:
      from . import QByteArray
      defaultValue = QByteArray()
    address = self.uglySide.call(
        'ritual_ZNK10QCborValue11toByteArrayERK10QByteArray',
        self._valueOf(defaultValue),
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  @overload()
  @overload(str)
  def toString(self, defaultValue: str = '') -> str:
    """
    Calls Qt's 'QString QCborValue::toString(const QString &defaultValue)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#toString

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
    #  QString QCborValue::toString(const QString &defaultValue) const
    return self.uglySide.call(
        'ritual_ZNK10QCborValue8toStringERK7QString', defaultValue,
    )

  @overload()
  @overload(str)
  def toStringView(self, defaultValue: str = '') -> str:
    """
    Calls Qt's 'QAnyStringView QCborValue::toStringView(QAnyStringView
    defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#toStringView

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
    #  QAnyStringView QCborValue::toStringView(QAnyStringView defaultValue)
    #      const
    return self.uglySide.call(
        'ritual_ZNK10QCborValue12toStringViewE14QAnyStringView',
        defaultValue,
    )

  @overload()
  @overload(QDateTime)
  def toDateTime(
      self,
      defaultValue: Optional[QDateTime] = None,
  ) -> QDateTime:
    """
    Calls Qt's 'QDateTime QCborValue::toDateTime(const QDateTime
    &defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#toDateTime

    Parameters
    ----------

    defaultValue : Optional[QDateTime]
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own. May be left out, as in Qt: a new 'QDateTime()' is then passed on.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QCborValue::toDateTime(const QDateTime &defaultValue) const
    if defaultValue is None:
      from . import QDateTime
      defaultValue = QDateTime()
    address = self.uglySide.call(
        'ritual_ZNK10QCborValue10toDateTimeERK9QDateTime',
        self._valueOf(defaultValue),
    )
    from . import QDateTime
    return QDateTime._cuteOwning(address)

  @overload()
  @overload(QUrl)
  def toUrl(self, defaultValue: Optional[QUrl] = None) -> QUrl:
    """
    Calls Qt's 'QUrl QCborValue::toUrl(const QUrl &defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#toUrl

    Parameters
    ----------

    defaultValue : Optional[QUrl]
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
      May be left out, as in Qt: a new 'QUrl()' is then passed on.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QCborValue::toUrl(const QUrl &defaultValue) const
    if defaultValue is None:
      from . import QUrl
      defaultValue = QUrl()
    address = self.uglySide.call(
        'ritual_ZNK10QCborValue5toUrlERK4QUrl', self._valueOf(defaultValue),
    )
    from . import QUrl
    return QUrl._cuteOwning(address)

  @overload()
  @overload(QRegularExpression)
  def toRegularExpression(
      self,
      defaultValue: Optional[QRegularExpression] = None,
  ) -> QRegularExpression:
    """
    Calls Qt's 'QRegularExpression QCborValue::toRegularExpression(const
    QRegularExpression &defaultValue) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborvalue.html#toRegularExpression

    Parameters
    ----------

    defaultValue : Optional[QRegularExpression]
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own. May be left out, as in Qt: a new 'QRegularExpression()'
      is then passed on.

    Returns
    -------

    QRegularExpression
      A new cute QRegularExpression around the copy Qt gave back. Python owns
      it.
    """
    #  QRegularExpression QCborValue::toRegularExpression(const
    #      QRegularExpression &defaultValue) const
    if defaultValue is None:
      from . import QRegularExpression
      defaultValue = QRegularExpression()
    address = self.uglySide.call(
        'ritual_ZNK10QCborValue19toRegularExpressionERK18QRegularExpression',
        self._valueOf(defaultValue),
    )
    from . import QRegularExpression
    return QRegularExpression._cuteOwning(address)

  @overload()
  @overload(QUuid)
  def toUuid(self, defaultValue: Optional[QUuid] = None) -> QUuid:
    """
    Calls Qt's 'QUuid QCborValue::toUuid(const QUuid &defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#toUuid

    Parameters
    ----------

    defaultValue : Optional[QUuid]
      Passed on as a value: Qt reads the C++ QUuid, which stays Python's own.
      May be left out, as in Qt: a new 'QUuid()' is then passed on.

    Returns
    -------

    QUuid
      A new cute QUuid around the copy Qt gave back. Python owns it.
    """
    #  QUuid QCborValue::toUuid(const QUuid &defaultValue) const
    if defaultValue is None:
      from . import QUuid
      defaultValue = QUuid()
    address = self.uglySide.call(
        'ritual_ZNK10QCborValue6toUuidERK5QUuid',
        self._valueOf(defaultValue),
    )
    from . import QUuid
    return QUuid._cuteOwning(address)

  @overload()
  def toArray(self) -> QCborArray:
    """
    Calls Qt's 'QCborArray QCborValue::toArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#toArray

    Returns
    -------

    QCborArray
      A new cute QCborArray around the copy Qt gave back. Python owns it.
    """
    #  QCborArray QCborValue::toArray() const
    address = self.uglySide.call('ritual_ZNK10QCborValue7toArrayEv')
    from . import QCborArray
    return QCborArray._cuteOwning(address)

  @overload(QCborArray)
  def toArray(self, defaultValue: QCborArray) -> QCborArray:
    """
    Calls Qt's 'QCborArray QCborValue::toArray(const QCborArray
    &defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#toArray

    Parameters
    ----------

    defaultValue : QCborArray
      Passed on as a value: Qt reads the C++ QCborArray, which stays Python's
      own.

    Returns
    -------

    QCborArray
      A new cute QCborArray around the copy Qt gave back. Python owns it.
    """
    #  QCborArray QCborValue::toArray(const QCborArray &defaultValue) const
    address = self.uglySide.call(
        'ritual_ZNK10QCborValue7toArrayERK10QCborArray',
        self._valueOf(defaultValue),
    )
    from . import QCborArray
    return QCborArray._cuteOwning(address)

  @overload()
  def toMap(self) -> QCborMap:
    """
    Calls Qt's 'QCborMap QCborValue::toMap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#toMap

    Returns
    -------

    QCborMap
      A new cute QCborMap around the copy Qt gave back. Python owns it.
    """
    #  QCborMap QCborValue::toMap() const
    address = self.uglySide.call('ritual_ZNK10QCborValue5toMapEv')
    from . import QCborMap
    return QCborMap._cuteOwning(address)

  @overload(QCborMap)
  def toMap(self, defaultValue: QCborMap) -> QCborMap:
    """
    Calls Qt's 'QCborMap QCborValue::toMap(const QCborMap &defaultValue)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#toMap

    Parameters
    ----------

    defaultValue : QCborMap
      Passed on as a value: Qt reads the C++ QCborMap, which stays Python's
      own.

    Returns
    -------

    QCborMap
      A new cute QCborMap around the copy Qt gave back. Python owns it.
    """
    #  QCborMap QCborValue::toMap(const QCborMap &defaultValue) const
    address = self.uglySide.call(
        'ritual_ZNK10QCborValue5toMapERK8QCborMap',
        self._valueOf(defaultValue),
    )
    from . import QCborMap
    return QCborMap._cuteOwning(address)

  @overload(THIS)
  def compare(self, other: QCborValue) -> int:
    """
    Calls Qt's 'int QCborValue::compare(const QCborValue &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#compare

    Parameters
    ----------

    other : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  int QCborValue::compare(const QCborValue &other) const
    return self.uglySide.call(
        'ritual_ZNK10QCborValue7compareERKS_', self._valueOf(other),
    )

  def toVariant(self) -> QVariant:
    """
    Calls Qt's 'QVariant QCborValue::toVariant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#toVariant

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QCborValue::toVariant() const
    address = self.uglySide.call('ritual_ZNK10QCborValue9toVariantEv')
    from . import QVariant
    return QVariant._cuteOwning(address)

  def toJsonValue(self) -> QJsonValue:
    """
    Calls Qt's 'QJsonValue QCborValue::toJsonValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#toJsonValue

    Returns
    -------

    QJsonValue
      A new cute QJsonValue around the copy Qt gave back. Python owns it.
    """
    #  QJsonValue QCborValue::toJsonValue() const
    address = self.uglySide.call('ritual_ZNK10QCborValue11toJsonValueEv')
    from . import QJsonValue
    return QJsonValue._cuteOwning(address)

  @overload()
  @overload(EncodingOptions)
  def toCbor(
      self,
      opt: EncodingOptions = EncodingOptions.NoTransformation,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray QCborValue::toCbor(EncodingOptions opt) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#toCbor

    Parameters
    ----------

    opt : EncodingOptions
      Passed on as its number. May be left out, as in Qt: it is then
      EncodingOptions.NoTransformation.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QCborValue::toCbor(EncodingOptions opt) const
    address = self.uglySide.call(
        'ritual_ZNK10QCborValue6toCborE6QFlagsINS_14EncodingOptionEE',
        opt.value,
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  @overload()
  @overload(DiagnosticNotationOptions)
  def toDiagnosticNotation(
      self,
      opts: DiagnosticNotationOptions = DiagnosticNotationOptions.Compact,
  ) -> str:
    """
    Calls Qt's 'QString
    QCborValue::toDiagnosticNotation(DiagnosticNotationOptions opts) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborvalue.html#toDiagnosticNotation

    Parameters
    ----------

    opts : DiagnosticNotationOptions
      Passed on as its number. May be left out, as in Qt: it is then
      DiagnosticNotationOptions.Compact.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCborValue::toDiagnosticNotation(DiagnosticNotationOptions
    #      opts) const
    return self.uglySide.call(
        'ritual_ZNK10QCborValue20toDiagnosticNotationE6QFlagsINS_24Diagnost'
        'icNotationOptionEE',
        opts.value,
    )

  def value_helper(self) -> int:
    """
    Calls Qt's 'qint64 QCborValue::value_helper() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#value_helper
    """
    #  qint64 QCborValue::value_helper() const
    return self.uglySide.call('ritual_ZNK10QCborValue12value_helperEv')

  def fp_helper(self) -> float:
    """
    Calls Qt's 'double QCborValue::fp_helper() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#fp_helper
    """
    #  double QCborValue::fp_helper() const
    return self.uglySide.call('ritual_ZNK10QCborValue9fp_helperEv')

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
  def __getitem__(self, key: str) -> QCborValue:
    """
    Calls Qt's 'const QCborValue QCborValue::operator[](const QString &key)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#operator[]

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  const QCborValue QCborValue::operator[](const QString &key) const
    address = self.uglySide.call('ritual_ZNK10QCborValueixERK7QString', key)
    return QCborValue._cuteOwning(address)

  @overload(QLatin1String)
  def __getitem__(self, key: QLatin1String) -> QCborValue:
    """
    Calls Qt's 'const QCborValue QCborValue::operator[](QLatin1StringView
    key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#operator[]

    Parameters
    ----------

    key : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  const QCborValue QCborValue::operator[](QLatin1StringView key) const
    address = self.uglySide.call(
        'ritual_ZNK10QCborValueixE13QLatin1String', self._valueOf(key),
    )
    return QCborValue._cuteOwning(address)

  @overload(int)
  def __getitem__(self, key: int) -> QCborValue:
    """
    Calls Qt's 'const QCborValue QCborValue::operator[](qint64 key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#operator[]

    Parameters
    ----------

    key : int
      Passed on as it is.

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  const QCborValue QCborValue::operator[](qint64 key) const
    address = self.uglySide.call('ritual_ZNK10QCborValueixEx', key)
    return QCborValue._cuteOwning(address)

  @overload(THIS)
  def __eq__(self, rhs: QCborValue) -> bool:
    """
    Calls Qt's 'bool operator==(const QCborValue &lhs, const QCborValue
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#operator==

    Parameters
    ----------

    rhs : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  bool operator==(const QCborValue &lhs, const QCborValue &rhs)
    return Rituals.call(
        'ritual_ZeqRK10QCborValueS1_',
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
  def __ne__(self, rhs: QCborValue) -> bool:
    """
    Calls Qt's 'bool operator!=(const QCborValue &lhs, const QCborValue
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#operator!=

    Parameters
    ----------

    rhs : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  bool operator!=(const QCborValue &lhs, const QCborValue &rhs)
    return Rituals.call(
        'ritual_ZneRK10QCborValueS1_',
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

  @overload(THIS)
  def __lt__(self, rhs: QCborValue) -> bool:
    """
    Calls Qt's 'bool operator<(const QCborValue &lhs, const QCborValue
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#operator<

    Parameters
    ----------

    rhs : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  bool operator<(const QCborValue &lhs, const QCborValue &rhs)
    return Rituals.call(
        'ritual_ZltRK10QCborValueS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __lt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __gt__(self, rhs: QCborValue) -> bool:
    """
    Calls Qt's 'bool operator>(const QCborValue &lhs, const QCborValue
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#operator>

    Parameters
    ----------

    rhs : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  bool operator>(const QCborValue &lhs, const QCborValue &rhs)
    return Rituals.call(
        'ritual_ZgtRK10QCborValueS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __gt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __le__(self, rhs: QCborValue) -> bool:
    """
    Calls Qt's 'bool operator<=(const QCborValue &lhs, const QCborValue
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#operator<=

    Parameters
    ----------

    rhs : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  bool operator<=(const QCborValue &lhs, const QCborValue &rhs)
    return Rituals.call(
        'ritual_ZleRK10QCborValueS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __le__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ge__(self, rhs: QCborValue) -> bool:
    """
    Calls Qt's 'bool operator>=(const QCborValue &lhs, const QCborValue
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#operator>=

    Parameters
    ----------

    rhs : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  bool operator>=(const QCborValue &lhs, const QCborValue &rhs)
    return Rituals.call(
        'ritual_ZgeRK10QCborValueS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ge__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QCborValue::QCborValue()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#QCborValue
    """
    #  QCborValue::QCborValue()
    self._noteCreation(QCborValue, lambda: Rituals.call(
        'ritual_ZN10QCborValueC1Ev',
    ))

  @overload(Type)
  def __init__(self, t_: Type) -> None:
    """
    Notes what was given, for Qt's 'QCborValue::QCborValue(Type t_)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#QCborValue

    Parameters
    ----------

    t_ : Type
      Passed on as its number.
    """
    #  QCborValue::QCborValue(Type t_)
    self._noteCreation(QCborValue, lambda: Rituals.call(
        'ritual_ZN10QCborValueC1ENS_4TypeE', t_.value,
    ))

  @overload(bool)
  def __init__(self, b_: bool) -> None:
    """
    Notes what was given, for Qt's 'QCborValue::QCborValue(bool b_)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#QCborValue

    Parameters
    ----------

    b_ : bool
      Passed on as it is.
    """
    #  QCborValue::QCborValue(bool b_)
    self._noteCreation(QCborValue, lambda: Rituals.call(
        'ritual_ZN10QCborValueC1Eb', b_,
    ))

  @overload(int)
  def __init__(self, i: int) -> None:
    """
    Notes what was given, for Qt's 'QCborValue::QCborValue(int i)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#QCborValue

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  QCborValue::QCborValue(int i)
    self._noteCreation(QCborValue, lambda: Rituals.call(
        'ritual_ZN10QCborValueC1Ei', i,
    ))

  @overload(float)
  def __init__(self, v: float) -> None:
    """
    Notes what was given, for Qt's 'QCborValue::QCborValue(double v)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#QCborValue

    Parameters
    ----------

    v : float
      Passed on as it is.
    """
    #  QCborValue::QCborValue(double v)
    self._noteCreation(QCborValue, lambda: Rituals.call(
        'ritual_ZN10QCborValueC1Ed', v,
    ))

  @overload(QByteArray)
  def __init__(self, ba: QByteArray) -> None:
    """
    Notes what was given, for Qt's 'QCborValue::QCborValue(const QByteArray
    &ba)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#QCborValue

    Parameters
    ----------

    ba : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QCborValue::QCborValue(const QByteArray &ba)
    self._noteCreation(QCborValue, lambda: Rituals.call(
        'ritual_ZN10QCborValueC1ERK10QByteArray', self._valueOf(ba),
    ))

  @overload(str)
  def __init__(self, s: str) -> None:
    """
    Notes what was given, for Qt's 'QCborValue::QCborValue(const QString
    &s)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#QCborValue

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QCborValue::QCborValue(const QString &s)
    self._noteCreation(QCborValue, lambda: Rituals.call(
        'ritual_ZN10QCborValueC1ERK7QString', s,
    ))

  @overload(QLatin1String)
  def __init__(self, s: QLatin1String) -> None:
    """
    Notes what was given, for Qt's 'QCborValue::QCborValue(QLatin1StringView
    s)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#QCborValue

    Parameters
    ----------

    s : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  QCborValue::QCborValue(QLatin1StringView s)
    self._noteCreation(QCborValue, lambda: Rituals.call(
        'ritual_ZN10QCborValueC1E13QLatin1String', self._valueOf(s),
    ))

  @overload(NoneType)
  def __init__(self, s: Optional[str]) -> None:
    """
    Notes what was given, for Qt's 'QCborValue::QCborValue(const char *s)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#QCborValue

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  QCborValue::QCborValue(const char *s)
    self._noteCreation(QCborValue, lambda: Rituals.call(
        'ritual_ZN10QCborValueC1EPKc', self._bytesOf(s),
    ))

  @overload(QCborArray)
  def __init__(self, a: QCborArray) -> None:
    """
    Notes what was given, for Qt's 'QCborValue::QCborValue(const QCborArray
    &a)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#QCborValue

    Parameters
    ----------

    a : QCborArray
      Passed on as a value: Qt reads the C++ QCborArray, which stays Python's
      own.
    """
    #  QCborValue::QCborValue(const QCborArray &a)
    self._noteCreation(QCborValue, lambda: Rituals.call(
        'ritual_ZN10QCborValueC1ERK10QCborArray', self._valueOf(a),
    ))

  @overload(QCborMap)
  def __init__(self, m: QCborMap) -> None:
    """
    Notes what was given, for Qt's 'QCborValue::QCborValue(const QCborMap
    &m)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#QCborValue

    Parameters
    ----------

    m : QCborMap
      Passed on as a value: Qt reads the C++ QCborMap, which stays Python's
      own.
    """
    #  QCborValue::QCborValue(const QCborMap &m)
    self._noteCreation(QCborValue, lambda: Rituals.call(
        'ritual_ZN10QCborValueC1ERK8QCborMap', self._valueOf(m),
    ))

  @overload(QDateTime)
  def __init__(self, dt: QDateTime) -> None:
    """
    Notes what was given, for Qt's 'QCborValue::QCborValue(const QDateTime
    &dt)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#QCborValue

    Parameters
    ----------

    dt : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  QCborValue::QCborValue(const QDateTime &dt)
    self._noteCreation(QCborValue, lambda: Rituals.call(
        'ritual_ZN10QCborValueC1ERK9QDateTime', self._valueOf(dt),
    ))

  @overload(QUrl)
  def __init__(self, url: QUrl) -> None:
    """
    Notes what was given, for Qt's 'QCborValue::QCborValue(const QUrl &url)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#QCborValue

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  QCborValue::QCborValue(const QUrl &url)
    self._noteCreation(QCborValue, lambda: Rituals.call(
        'ritual_ZN10QCborValueC1ERK4QUrl', self._valueOf(url),
    ))

  @overload(QRegularExpression)
  def __init__(self, rx: QRegularExpression) -> None:
    """
    Notes what was given, for Qt's 'QCborValue::QCborValue(const
    QRegularExpression &rx)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#QCborValue

    Parameters
    ----------

    rx : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  QCborValue::QCborValue(const QRegularExpression &rx)
    self._noteCreation(QCborValue, lambda: Rituals.call(
        'ritual_ZN10QCborValueC1ERK18QRegularExpression', self._valueOf(rx),
    ))

  @overload(QUuid)
  def __init__(self, uuid: QUuid) -> None:
    """
    Notes what was given, for Qt's 'QCborValue::QCborValue(const QUuid
    &uuid)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#QCborValue

    Parameters
    ----------

    uuid : QUuid
      Passed on as a value: Qt reads the C++ QUuid, which stays Python's own.
    """
    #  QCborValue::QCborValue(const QUuid &uuid)
    self._noteCreation(QCborValue, lambda: Rituals.call(
        'ritual_ZN10QCborValueC1ERK5QUuid', self._valueOf(uuid),
    ))

  @overload(THIS)
  def __init__(self, other: QCborValue) -> None:
    """
    Notes what was given, for Qt's 'QCborValue::QCborValue(const QCborValue
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#QCborValue

    Parameters
    ----------

    other : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  QCborValue::QCborValue(const QCborValue &other)
    self._noteCreation(QCborValue, lambda: Rituals.call(
        'ritual_ZN10QCborValueC1ERKS_', self._valueOf(other),
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

  def dispose(self) -> None:
    """
    Calls Qt's 'void QCborValue::dispose()'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalue.html#dispose
    """
    #  void QCborValue::dispose()
    self.uglySide.call('ritual_ZN10QCborValue7disposeEv')


#  Qt's 'QList<QCborValue>': the list of QCborValue, which
#  'QList[QCborValue]' gives. It is made here, so that there is one as soon
#  as there can be a QCborValue.
QList.createKind(
    QCborValue, 'value',
    make='ritual_list_make_QCborValue',
    add='ritual_list_add_QCborValue',
    size='ritual_list_size_QCborValue',
    at='ritual_list_at_QCborValue',
    drop='ritual_list_drop_QCborValue',
)
