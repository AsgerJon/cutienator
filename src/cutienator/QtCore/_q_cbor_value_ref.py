"""
QCborValueRef binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qcborvalue.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QCborValue, QCborValueConstRef

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QByteArray, QCborArray, QCborMap, QDateTime, QJsonValue
  from . import QRegularExpression, QUrl, QUuid, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QCborArray = WAIT['QCborArray']
  QCborMap = WAIT['QCborMap']
  QDateTime = WAIT['QDateTime']
  QRegularExpression = WAIT['QRegularExpression']
  QUrl = WAIT['QUrl']
  QUuid = WAIT['QUuid']


class QCborValueRef(QCborValueConstRef):
  """
  The cute side of Qt's QCborValueRef: a plain Python object standing in
  front of one C++ QCborValueRef.

  It is built on the cute 'QCborValueConstRef', as Qt's QCborValueRef is
  built on Qt's QCborValueConstRef, and has everything that class has.

  C++ hands a QCborValueRef around as a copy, so every C++ QCborValueRef
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCborValueRef that has a ritual and that Python can
  call so far, 37 names in all: 'type', 'isInteger', 'isByteArray',
  'isString', 'isArray', 'isMap', 'isTag', 'isFalse', 'isTrue', 'isBool',
  'isNull', 'isUndefined', 'isDouble', 'isDateTime', 'isUrl',
  'isRegularExpression', 'isUuid', 'isInvalid', 'isContainer',
  'isSimpleType', 'taggedValue', 'toInteger', 'toBool', 'toDouble',
  'toByteArray', 'toString', 'toDateTime', 'toUrl', 'toRegularExpression',
  'toUuid', 'toArray', 'toMap', 'compare', 'toVariant', 'toJsonValue',
  'toCbor', 'toDiagnosticNotation'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCborValueRef QCborValueRef::operator[](qint64 key)': an operator,
    which is not reflected yet.
  - Qt's 'QCborValueRef QCborValueRef::operator[](QLatin1StringView key)': an
    operator, which is not reflected yet.
  - Qt's 'QCborValueRef QCborValueRef::operator[](const QString &key)': an
    operator, which is not reflected yet.
  - Qt's 'QCborValue QCborValueRef::operator QCborValue() const': an
    operator, which is not reflected yet.
  - Qt's 'bool QCborValueRef::isSimpleType(QCborSimpleType st) const': names
    the enum 'QCborSimpleType', whose class cannot be named here.
  - Qt's 'QCborSimpleType QCborValueRef::toSimpleType(QCborSimpleType
    defaultValue) const': names the enum 'QCborSimpleType', whose class
    cannot be named here.
  - Qt's 'QCborTag QCborValueRef::tag(QCborTag defaultValue) const': names
    the enum 'QCborTag', whose class cannot be named here.
  - Qt's 'const QCborValue QCborValueRef::operator[](const QString &key)
    const': an operator, which is not reflected yet.
  - Qt's 'const QCborValue QCborValueRef::operator[](QLatin1StringView key)
    const': an operator, which is not reflected yet.
  - Qt's 'const QCborValue QCborValueRef::operator[](qint64 key) const': an
    operator, which is not reflected yet.
  - Qt's 'QCborValueRef::~QCborValueRef()': the destructor: Python removes
    its C++ QCborValueRef by it, and has no other use for it.

  What has no ritual
  ------------------

  14 of the 65 functions Qt declares: 9 private; 5 takes or gives a type that
  cannot be passed yet.

  What to expect
  --------------

  - The C++ QCborValueRef is created at the first use, not by
    'QCborValueRef(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCborValueRef back gives a copy the ritual made for
    Python, in a new cute QCborValueRef.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCborValueRef'

  #  Qt's '~QCborValueRef()'. Naming it makes this a value class: Python owns
  #  every C++ QCborValueRef behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QCborValueRefD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QCborValue.Type:
    """
    Calls Qt's 'QCborValue::Type QCborValueRef::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#type

    Returns
    -------

    QCborValue.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QCborValue.Type(number)'
      gives.
    """
    #  QCborValue::Type QCborValueRef::type() const
    return QCborValue.Type(self.uglySide.call(
        'ritual_ZNK13QCborValueRef4typeEv',
    ))

  def isInteger(self) -> bool:
    """
    Calls Qt's 'bool QCborValueRef::isInteger() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#isInteger
    """
    #  bool QCborValueRef::isInteger() const
    return self.uglySide.call('ritual_ZNK13QCborValueRef9isIntegerEv')

  def isByteArray(self) -> bool:
    """
    Calls Qt's 'bool QCborValueRef::isByteArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#isByteArray
    """
    #  bool QCborValueRef::isByteArray() const
    return self.uglySide.call('ritual_ZNK13QCborValueRef11isByteArrayEv')

  def isString(self) -> bool:
    """
    Calls Qt's 'bool QCborValueRef::isString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#isString
    """
    #  bool QCborValueRef::isString() const
    return self.uglySide.call('ritual_ZNK13QCborValueRef8isStringEv')

  def isArray(self) -> bool:
    """
    Calls Qt's 'bool QCborValueRef::isArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#isArray
    """
    #  bool QCborValueRef::isArray() const
    return self.uglySide.call('ritual_ZNK13QCborValueRef7isArrayEv')

  def isMap(self) -> bool:
    """
    Calls Qt's 'bool QCborValueRef::isMap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#isMap
    """
    #  bool QCborValueRef::isMap() const
    return self.uglySide.call('ritual_ZNK13QCborValueRef5isMapEv')

  def isTag(self) -> bool:
    """
    Calls Qt's 'bool QCborValueRef::isTag() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#isTag
    """
    #  bool QCborValueRef::isTag() const
    return self.uglySide.call('ritual_ZNK13QCborValueRef5isTagEv')

  def isFalse(self) -> bool:
    """
    Calls Qt's 'bool QCborValueRef::isFalse() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#isFalse
    """
    #  bool QCborValueRef::isFalse() const
    return self.uglySide.call('ritual_ZNK13QCborValueRef7isFalseEv')

  def isTrue(self) -> bool:
    """
    Calls Qt's 'bool QCborValueRef::isTrue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#isTrue
    """
    #  bool QCborValueRef::isTrue() const
    return self.uglySide.call('ritual_ZNK13QCborValueRef6isTrueEv')

  def isBool(self) -> bool:
    """
    Calls Qt's 'bool QCborValueRef::isBool() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#isBool
    """
    #  bool QCborValueRef::isBool() const
    return self.uglySide.call('ritual_ZNK13QCborValueRef6isBoolEv')

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QCborValueRef::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#isNull
    """
    #  bool QCborValueRef::isNull() const
    return self.uglySide.call('ritual_ZNK13QCborValueRef6isNullEv')

  def isUndefined(self) -> bool:
    """
    Calls Qt's 'bool QCborValueRef::isUndefined() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#isUndefined
    """
    #  bool QCborValueRef::isUndefined() const
    return self.uglySide.call('ritual_ZNK13QCborValueRef11isUndefinedEv')

  def isDouble(self) -> bool:
    """
    Calls Qt's 'bool QCborValueRef::isDouble() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#isDouble
    """
    #  bool QCborValueRef::isDouble() const
    return self.uglySide.call('ritual_ZNK13QCborValueRef8isDoubleEv')

  def isDateTime(self) -> bool:
    """
    Calls Qt's 'bool QCborValueRef::isDateTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#isDateTime
    """
    #  bool QCborValueRef::isDateTime() const
    return self.uglySide.call('ritual_ZNK13QCborValueRef10isDateTimeEv')

  def isUrl(self) -> bool:
    """
    Calls Qt's 'bool QCborValueRef::isUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#isUrl
    """
    #  bool QCborValueRef::isUrl() const
    return self.uglySide.call('ritual_ZNK13QCborValueRef5isUrlEv')

  def isRegularExpression(self) -> bool:
    """
    Calls Qt's 'bool QCborValueRef::isRegularExpression() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborvalueref.html#isRegularExpression
    """
    #  bool QCborValueRef::isRegularExpression() const
    return self.uglySide.call(
        'ritual_ZNK13QCborValueRef19isRegularExpressionEv',
    )

  def isUuid(self) -> bool:
    """
    Calls Qt's 'bool QCborValueRef::isUuid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#isUuid
    """
    #  bool QCborValueRef::isUuid() const
    return self.uglySide.call('ritual_ZNK13QCborValueRef6isUuidEv')

  def isInvalid(self) -> bool:
    """
    Calls Qt's 'bool QCborValueRef::isInvalid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#isInvalid
    """
    #  bool QCborValueRef::isInvalid() const
    return self.uglySide.call('ritual_ZNK13QCborValueRef9isInvalidEv')

  def isContainer(self) -> bool:
    """
    Calls Qt's 'bool QCborValueRef::isContainer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#isContainer
    """
    #  bool QCborValueRef::isContainer() const
    return self.uglySide.call('ritual_ZNK13QCborValueRef11isContainerEv')

  def isSimpleType(self) -> bool:
    """
    Calls Qt's 'bool QCborValueRef::isSimpleType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#isSimpleType
    """
    #  bool QCborValueRef::isSimpleType() const
    return self.uglySide.call('ritual_ZNK13QCborValueRef12isSimpleTypeEv')

  @overload()
  @overload(QCborValue)
  def taggedValue(
      self,
      defaultValue: Optional[QCborValue] = None,
  ) -> QCborValue:
    """
    Calls Qt's 'QCborValue QCborValueRef::taggedValue(const QCborValue
    &defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#taggedValue

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
    #  QCborValue QCborValueRef::taggedValue(const QCborValue &defaultValue)
    #      const
    if defaultValue is None:
      defaultValue = QCborValue()
    address = self.uglySide.call(
        'ritual_ZNK13QCborValueRef11taggedValueERK10QCborValue',
        self._valueOf(defaultValue),
    )
    return QCborValue._cuteOwning(address)

  @overload()
  @overload(int)
  def toInteger(self, defaultValue: int = 0) -> int:
    """
    Calls Qt's 'qint64 QCborValueRef::toInteger(qint64 defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#toInteger

    Parameters
    ----------

    defaultValue : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  qint64 QCborValueRef::toInteger(qint64 defaultValue) const
    return self.uglySide.call(
        'ritual_ZNK13QCborValueRef9toIntegerEx', defaultValue,
    )

  @overload()
  @overload(bool)
  def toBool(self, defaultValue: bool = False) -> bool:
    """
    Calls Qt's 'bool QCborValueRef::toBool(bool defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#toBool

    Parameters
    ----------

    defaultValue : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  bool QCborValueRef::toBool(bool defaultValue) const
    return self.uglySide.call(
        'ritual_ZNK13QCborValueRef6toBoolEb', defaultValue,
    )

  @overload()
  @overload(float)
  def toDouble(self, defaultValue: float = 0.0) -> float:
    """
    Calls Qt's 'double QCborValueRef::toDouble(double defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#toDouble

    Parameters
    ----------

    defaultValue : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  double QCborValueRef::toDouble(double defaultValue) const
    return self.uglySide.call(
        'ritual_ZNK13QCborValueRef8toDoubleEd', defaultValue,
    )

  @overload()
  @overload(QByteArray)
  def toByteArray(
      self,
      defaultValue: Optional[QByteArray] = None,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray QCborValueRef::toByteArray(const QByteArray
    &defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#toByteArray

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
    #  QByteArray QCborValueRef::toByteArray(const QByteArray &defaultValue)
    #      const
    if defaultValue is None:
      from . import QByteArray
      defaultValue = QByteArray()
    address = self.uglySide.call(
        'ritual_ZNK13QCborValueRef11toByteArrayERK10QByteArray',
        self._valueOf(defaultValue),
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  @overload()
  @overload(str)
  def toString(self, defaultValue: str = '') -> str:
    """
    Calls Qt's 'QString QCborValueRef::toString(const QString &defaultValue)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#toString

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
    #  QString QCborValueRef::toString(const QString &defaultValue) const
    return self.uglySide.call(
        'ritual_ZNK13QCborValueRef8toStringERK7QString', defaultValue,
    )

  @overload()
  @overload(QDateTime)
  def toDateTime(
      self,
      defaultValue: Optional[QDateTime] = None,
  ) -> QDateTime:
    """
    Calls Qt's 'QDateTime QCborValueRef::toDateTime(const QDateTime
    &defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#toDateTime

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
    #  QDateTime QCborValueRef::toDateTime(const QDateTime &defaultValue)
    #      const
    if defaultValue is None:
      from . import QDateTime
      defaultValue = QDateTime()
    address = self.uglySide.call(
        'ritual_ZNK13QCborValueRef10toDateTimeERK9QDateTime',
        self._valueOf(defaultValue),
    )
    from . import QDateTime
    return QDateTime._cuteOwning(address)

  @overload()
  @overload(QUrl)
  def toUrl(self, defaultValue: Optional[QUrl] = None) -> QUrl:
    """
    Calls Qt's 'QUrl QCborValueRef::toUrl(const QUrl &defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#toUrl

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
    #  QUrl QCborValueRef::toUrl(const QUrl &defaultValue) const
    if defaultValue is None:
      from . import QUrl
      defaultValue = QUrl()
    address = self.uglySide.call(
        'ritual_ZNK13QCborValueRef5toUrlERK4QUrl',
        self._valueOf(defaultValue),
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
    Calls Qt's 'QRegularExpression QCborValueRef::toRegularExpression(const
    QRegularExpression &defaultValue) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborvalueref.html#toRegularExpression

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
    #  QRegularExpression QCborValueRef::toRegularExpression(const
    #      QRegularExpression &defaultValue) const
    if defaultValue is None:
      from . import QRegularExpression
      defaultValue = QRegularExpression()
    address = self.uglySide.call(
        'ritual_ZNK13QCborValueRef19toRegularExpressionERK18QRegularExpress'
        'ion',
        self._valueOf(defaultValue),
    )
    from . import QRegularExpression
    return QRegularExpression._cuteOwning(address)

  @overload()
  @overload(QUuid)
  def toUuid(self, defaultValue: Optional[QUuid] = None) -> QUuid:
    """
    Calls Qt's 'QUuid QCborValueRef::toUuid(const QUuid &defaultValue)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#toUuid

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
    #  QUuid QCborValueRef::toUuid(const QUuid &defaultValue) const
    if defaultValue is None:
      from . import QUuid
      defaultValue = QUuid()
    address = self.uglySide.call(
        'ritual_ZNK13QCborValueRef6toUuidERK5QUuid',
        self._valueOf(defaultValue),
    )
    from . import QUuid
    return QUuid._cuteOwning(address)

  @overload()
  def toArray(self) -> QCborArray:
    """
    Calls Qt's 'QCborArray QCborValueRef::toArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#toArray

    Returns
    -------

    QCborArray
      A new cute QCborArray around the copy Qt gave back. Python owns it.
    """
    #  QCborArray QCborValueRef::toArray() const
    address = self.uglySide.call('ritual_ZNK13QCborValueRef7toArrayEv')
    from . import QCborArray
    return QCborArray._cuteOwning(address)

  @overload(QCborArray)
  def toArray(self, a: QCborArray) -> QCborArray:
    """
    Calls Qt's 'QCborArray QCborValueRef::toArray(const QCborArray &a)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#toArray

    Parameters
    ----------

    a : QCborArray
      Passed on as a value: Qt reads the C++ QCborArray, which stays Python's
      own.

    Returns
    -------

    QCborArray
      A new cute QCborArray around the copy Qt gave back. Python owns it.
    """
    #  QCborArray QCborValueRef::toArray(const QCborArray &a) const
    address = self.uglySide.call(
        'ritual_ZNK13QCborValueRef7toArrayERK10QCborArray', self._valueOf(a),
    )
    from . import QCborArray
    return QCborArray._cuteOwning(address)

  @overload()
  def toMap(self) -> QCborMap:
    """
    Calls Qt's 'QCborMap QCborValueRef::toMap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#toMap

    Returns
    -------

    QCborMap
      A new cute QCborMap around the copy Qt gave back. Python owns it.
    """
    #  QCborMap QCborValueRef::toMap() const
    address = self.uglySide.call('ritual_ZNK13QCborValueRef5toMapEv')
    from . import QCborMap
    return QCborMap._cuteOwning(address)

  @overload(QCborMap)
  def toMap(self, m: QCborMap) -> QCborMap:
    """
    Calls Qt's 'QCborMap QCborValueRef::toMap(const QCborMap &m) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#toMap

    Parameters
    ----------

    m : QCborMap
      Passed on as a value: Qt reads the C++ QCborMap, which stays Python's
      own.

    Returns
    -------

    QCborMap
      A new cute QCborMap around the copy Qt gave back. Python owns it.
    """
    #  QCborMap QCborValueRef::toMap(const QCborMap &m) const
    address = self.uglySide.call(
        'ritual_ZNK13QCborValueRef5toMapERK8QCborMap', self._valueOf(m),
    )
    from . import QCborMap
    return QCborMap._cuteOwning(address)

  @overload(QCborValue)
  def compare(self, other: QCborValue) -> int:
    """
    Calls Qt's 'int QCborValueRef::compare(const QCborValue &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#compare

    Parameters
    ----------

    other : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  int QCborValueRef::compare(const QCborValue &other) const
    return self.uglySide.call(
        'ritual_ZNK13QCborValueRef7compareERK10QCborValue',
        self._valueOf(other),
    )

  def toVariant(self) -> QVariant:
    """
    Calls Qt's 'QVariant QCborValueRef::toVariant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#toVariant

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QCborValueRef::toVariant() const
    address = self.uglySide.call('ritual_ZNK13QCborValueRef9toVariantEv')
    from . import QVariant
    return QVariant._cuteOwning(address)

  def toJsonValue(self) -> QJsonValue:
    """
    Calls Qt's 'QJsonValue QCborValueRef::toJsonValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#toJsonValue

    Returns
    -------

    QJsonValue
      A new cute QJsonValue around the copy Qt gave back. Python owns it.
    """
    #  QJsonValue QCborValueRef::toJsonValue() const
    address = self.uglySide.call('ritual_ZNK13QCborValueRef11toJsonValueEv')
    from . import QJsonValue
    return QJsonValue._cuteOwning(address)

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

  @overload(THIS)
  def __init__(self, a0: QCborValueRef) -> None:
    """
    Notes what was given, for Qt's 'QCborValueRef::QCborValueRef(const
    QCborValueRef &a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#QCborValueRef

    Parameters
    ----------

    a0 : QCborValueRef
      Passed on as a value: Qt reads the C++ QCborValueRef, which stays
      Python's own.
    """
    #  QCborValueRef::QCborValueRef(const QCborValueRef &a0)
    self._noteCreation(QCborValueRef, lambda: Rituals.call(
        'ritual_ZN13QCborValueRefC1ERKS_', self._valueOf(a0),
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
  @overload(QCborValue.EncodingOptions)
  def toCbor(
      self,
      opt: QCborValue.EncodingOptions = (
          QCborValue.EncodingOptions.NoTransformation),
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray QCborValueRef::toCbor(QCborValue::EncodingOptions
    opt)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueref.html#toCbor

    Parameters
    ----------

    opt : QCborValue.EncodingOptions
      Passed on as its number. May be left out, as in Qt: it is then
      QCborValue.EncodingOptions.NoTransformation.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QCborValueRef::toCbor(QCborValue::EncodingOptions opt)
    address = self.uglySide.call(
        'ritual_ZN13QCborValueRef6toCborE6QFlagsIN10QCborValue14EncodingOpt'
        'ionEE',
        opt.value,
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  @overload()
  @overload(QCborValue.DiagnosticNotationOptions)
  def toDiagnosticNotation(
      self,
      opt: QCborValue.DiagnosticNotationOptions = (
          QCborValue.DiagnosticNotationOptions.Compact),
  ) -> str:
    """
    Calls Qt's 'QString
    QCborValueRef::toDiagnosticNotation(QCborValue::DiagnosticNotationOptions
    opt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborvalueref.html#toDiagnosticNotation

    Parameters
    ----------

    opt : QCborValue.DiagnosticNotationOptions
      Passed on as its number. May be left out, as in Qt: it is then
      QCborValue.DiagnosticNotationOptions.Compact.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCborValueRef::toDiagnosticNotation(QCborValue::
    #      DiagnosticNotationOptions opt)
    return self.uglySide.call(
        'ritual_ZN13QCborValueRef20toDiagnosticNotationE6QFlagsIN10QCborVal'
        'ue24DiagnosticNotationOptionEE',
        opt.value,
    )
