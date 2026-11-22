"""
QCborValueConstRef binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qcborvalue.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QCborValue

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QByteArray, QCborArray, QCborMap, QDateTime, QJsonValue
  from . import QLatin1String, QRegularExpression, QUrl, QUuid, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QCborArray = WAIT['QCborArray']
  QCborMap = WAIT['QCborMap']
  QDateTime = WAIT['QDateTime']
  QLatin1String = WAIT['QLatin1String']
  QRegularExpression = WAIT['QRegularExpression']
  QUrl = WAIT['QUrl']
  QUuid = WAIT['QUuid']


class QCborValueConstRef(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCborValueConstRef: a plain Python object standing in
  front of one C++ QCborValueConstRef.

  C++ hands a QCborValueConstRef around as a copy, so every C++
  QCborValueConstRef behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCborValueConstRef that has a ritual and that Python
  can call so far, 45 names in all: 'type', 'isInteger', 'isByteArray',
  'isString', 'isArray', 'isMap', 'isTag', 'isFalse', 'isTrue', 'isBool',
  'isNull', 'isUndefined', 'isDouble', 'isDateTime', 'isUrl',
  'isRegularExpression', 'isUuid', 'isInvalid', 'isContainer',
  'isSimpleType', 'taggedValue', 'toInteger', 'toBool', 'toDouble',
  'toByteArray', 'toString', 'toStringView', 'toDateTime', 'toUrl',
  'toRegularExpression', 'toUuid', 'toArray', 'toMap', '__getitem__',
  'compare', 'toVariant', 'toJsonValue', 'toCbor', 'toDiagnosticNotation',
  '__eq__', '__ne__', '__lt__', '__gt__', '__le__', '__ge__'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCborValue QCborValueConstRef::operator QCborValue() const': an
    operator Python has no name for.
  - Qt's 'bool QCborValueConstRef::isSimpleType(QCborSimpleType st) const':
    names the enum 'QCborSimpleType', whose class cannot be named here.
  - Qt's 'QCborSimpleType QCborValueConstRef::toSimpleType(QCborSimpleType
    defaultValue) const': names the enum 'QCborSimpleType', whose class
    cannot be named here.
  - Qt's 'QCborTag QCborValueConstRef::tag(QCborTag defaultValue) const':
    names the enum 'QCborTag', whose class cannot be named here.
  - Qt's 'bool operator==(const QCborValue &lhs, const QCborValueConstRef
    &rhs)': takes in Python what 'bool operator==(const QCborValueConstRef
    &lhs, const QCborValue &rhs)' takes.
  - Qt's 'bool operator!=(const QCborValue &lhs, const QCborValueConstRef
    &rhs)': takes in Python what 'bool operator!=(const QCborValueConstRef
    &lhs, const QCborValue &rhs)' takes.
  - Qt's 'bool operator<(const QCborValue &lhs, const QCborValueConstRef
    &rhs)': takes in Python what 'bool operator>(const QCborValueConstRef
    &lhs, const QCborValue &rhs)' takes.
  - Qt's 'bool operator>(const QCborValue &lhs, const QCborValueConstRef
    &rhs)': takes in Python what 'bool operator<(const QCborValueConstRef
    &lhs, const QCborValue &rhs)' takes.
  - Qt's 'bool operator<=(const QCborValue &lhs, const QCborValueConstRef
    &rhs)': takes in Python what 'bool operator>=(const QCborValueConstRef
    &lhs, const QCborValue &rhs)' takes.
  - Qt's 'bool operator>=(const QCborValue &lhs, const QCborValueConstRef
    &rhs)': takes in Python what 'bool operator<=(const QCborValueConstRef
    &lhs, const QCborValue &rhs)' takes.
  - Qt's 'QCborValueConstRef::~QCborValueConstRef()': the destructor: Python
    removes its C++ QCborValueConstRef by it, and has no other use for it.

  What has no ritual
  ------------------

  17 of the 84 functions Qt declares: 15 protected; 1 forbidden; 1 takes or
  gives a type that cannot be passed yet.

  What to expect
  --------------

  - The C++ QCborValueConstRef is created at the first use, not by
    'QCborValueConstRef(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCborValueConstRef back gives a copy the ritual made
    for Python, in a new cute QCborValueConstRef.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCborValueConstRef'

  #  Qt's '~QCborValueConstRef()'. Naming it makes this a value class: Python
  #  owns every C++ QCborValueConstRef behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QCborValueConstRefD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QCborValue.Type:
    """
    Calls Qt's 'QCborValue::Type QCborValueConstRef::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#type

    Returns
    -------

    QCborValue.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QCborValue.Type(number)'
      gives.
    """
    #  QCborValue::Type QCborValueConstRef::type() const
    return QCborValue.Type(self.uglySide.call(
        'ritual_ZNK18QCborValueConstRef4typeEv',
    ))

  def isInteger(self) -> bool:
    """
    Calls Qt's 'bool QCborValueConstRef::isInteger() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#isInteger
    """
    #  bool QCborValueConstRef::isInteger() const
    return self.uglySide.call('ritual_ZNK18QCborValueConstRef9isIntegerEv')

  def isByteArray(self) -> bool:
    """
    Calls Qt's 'bool QCborValueConstRef::isByteArray() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborvalueconstref.html#isByteArray
    """
    #  bool QCborValueConstRef::isByteArray() const
    return self.uglySide.call(
        'ritual_ZNK18QCborValueConstRef11isByteArrayEv',
    )

  def isString(self) -> bool:
    """
    Calls Qt's 'bool QCborValueConstRef::isString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#isString
    """
    #  bool QCborValueConstRef::isString() const
    return self.uglySide.call('ritual_ZNK18QCborValueConstRef8isStringEv')

  def isArray(self) -> bool:
    """
    Calls Qt's 'bool QCborValueConstRef::isArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#isArray
    """
    #  bool QCborValueConstRef::isArray() const
    return self.uglySide.call('ritual_ZNK18QCborValueConstRef7isArrayEv')

  def isMap(self) -> bool:
    """
    Calls Qt's 'bool QCborValueConstRef::isMap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#isMap
    """
    #  bool QCborValueConstRef::isMap() const
    return self.uglySide.call('ritual_ZNK18QCborValueConstRef5isMapEv')

  def isTag(self) -> bool:
    """
    Calls Qt's 'bool QCborValueConstRef::isTag() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#isTag
    """
    #  bool QCborValueConstRef::isTag() const
    return self.uglySide.call('ritual_ZNK18QCborValueConstRef5isTagEv')

  def isFalse(self) -> bool:
    """
    Calls Qt's 'bool QCborValueConstRef::isFalse() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#isFalse
    """
    #  bool QCborValueConstRef::isFalse() const
    return self.uglySide.call('ritual_ZNK18QCborValueConstRef7isFalseEv')

  def isTrue(self) -> bool:
    """
    Calls Qt's 'bool QCborValueConstRef::isTrue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#isTrue
    """
    #  bool QCborValueConstRef::isTrue() const
    return self.uglySide.call('ritual_ZNK18QCborValueConstRef6isTrueEv')

  def isBool(self) -> bool:
    """
    Calls Qt's 'bool QCborValueConstRef::isBool() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#isBool
    """
    #  bool QCborValueConstRef::isBool() const
    return self.uglySide.call('ritual_ZNK18QCborValueConstRef6isBoolEv')

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QCborValueConstRef::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#isNull
    """
    #  bool QCborValueConstRef::isNull() const
    return self.uglySide.call('ritual_ZNK18QCborValueConstRef6isNullEv')

  def isUndefined(self) -> bool:
    """
    Calls Qt's 'bool QCborValueConstRef::isUndefined() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborvalueconstref.html#isUndefined
    """
    #  bool QCborValueConstRef::isUndefined() const
    return self.uglySide.call(
        'ritual_ZNK18QCborValueConstRef11isUndefinedEv',
    )

  def isDouble(self) -> bool:
    """
    Calls Qt's 'bool QCborValueConstRef::isDouble() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#isDouble
    """
    #  bool QCborValueConstRef::isDouble() const
    return self.uglySide.call('ritual_ZNK18QCborValueConstRef8isDoubleEv')

  def isDateTime(self) -> bool:
    """
    Calls Qt's 'bool QCborValueConstRef::isDateTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#isDateTime
    """
    #  bool QCborValueConstRef::isDateTime() const
    return self.uglySide.call('ritual_ZNK18QCborValueConstRef10isDateTimeEv')

  def isUrl(self) -> bool:
    """
    Calls Qt's 'bool QCborValueConstRef::isUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#isUrl
    """
    #  bool QCborValueConstRef::isUrl() const
    return self.uglySide.call('ritual_ZNK18QCborValueConstRef5isUrlEv')

  def isRegularExpression(self) -> bool:
    """
    Calls Qt's 'bool QCborValueConstRef::isRegularExpression() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborvalueconstref.html#isRegularExpression
    """
    #  bool QCborValueConstRef::isRegularExpression() const
    return self.uglySide.call(
        'ritual_ZNK18QCborValueConstRef19isRegularExpressionEv',
    )

  def isUuid(self) -> bool:
    """
    Calls Qt's 'bool QCborValueConstRef::isUuid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#isUuid
    """
    #  bool QCborValueConstRef::isUuid() const
    return self.uglySide.call('ritual_ZNK18QCborValueConstRef6isUuidEv')

  def isInvalid(self) -> bool:
    """
    Calls Qt's 'bool QCborValueConstRef::isInvalid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#isInvalid
    """
    #  bool QCborValueConstRef::isInvalid() const
    return self.uglySide.call('ritual_ZNK18QCborValueConstRef9isInvalidEv')

  def isContainer(self) -> bool:
    """
    Calls Qt's 'bool QCborValueConstRef::isContainer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborvalueconstref.html#isContainer
    """
    #  bool QCborValueConstRef::isContainer() const
    return self.uglySide.call(
        'ritual_ZNK18QCborValueConstRef11isContainerEv',
    )

  def isSimpleType(self) -> bool:
    """
    Calls Qt's 'bool QCborValueConstRef::isSimpleType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborvalueconstref.html#isSimpleType
    """
    #  bool QCborValueConstRef::isSimpleType() const
    return self.uglySide.call(
        'ritual_ZNK18QCborValueConstRef12isSimpleTypeEv',
    )

  @overload()
  @overload(QCborValue)
  def taggedValue(
      self,
      defaultValue: Optional[QCborValue] = None,
  ) -> QCborValue:
    """
    Calls Qt's 'QCborValue QCborValueConstRef::taggedValue(const QCborValue
    &defaultValue) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborvalueconstref.html#taggedValue

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
    #  QCborValue QCborValueConstRef::taggedValue(const QCborValue
    #      &defaultValue) const
    if defaultValue is None:
      defaultValue = QCborValue()
    address = self.uglySide.call(
        'ritual_ZNK18QCborValueConstRef11taggedValueERK10QCborValue',
        self._valueOf(defaultValue),
    )
    return QCborValue._cuteOwning(address)

  @overload()
  @overload(int)
  def toInteger(self, defaultValue: int = 0) -> int:
    """
    Calls Qt's 'qint64 QCborValueConstRef::toInteger(qint64 defaultValue)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#toInteger

    Parameters
    ----------

    defaultValue : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  qint64 QCborValueConstRef::toInteger(qint64 defaultValue) const
    return self.uglySide.call(
        'ritual_ZNK18QCborValueConstRef9toIntegerEx', defaultValue,
    )

  @overload()
  @overload(bool)
  def toBool(self, defaultValue: bool = False) -> bool:
    """
    Calls Qt's 'bool QCborValueConstRef::toBool(bool defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#toBool

    Parameters
    ----------

    defaultValue : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  bool QCborValueConstRef::toBool(bool defaultValue) const
    return self.uglySide.call(
        'ritual_ZNK18QCborValueConstRef6toBoolEb', defaultValue,
    )

  @overload()
  @overload(float)
  def toDouble(self, defaultValue: float = 0.0) -> float:
    """
    Calls Qt's 'double QCborValueConstRef::toDouble(double defaultValue)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#toDouble

    Parameters
    ----------

    defaultValue : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  double QCborValueConstRef::toDouble(double defaultValue) const
    return self.uglySide.call(
        'ritual_ZNK18QCborValueConstRef8toDoubleEd', defaultValue,
    )

  @overload()
  @overload(QByteArray)
  def toByteArray(
      self,
      defaultValue: Optional[QByteArray] = None,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray QCborValueConstRef::toByteArray(const QByteArray
    &defaultValue) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborvalueconstref.html#toByteArray

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
    #  QByteArray QCborValueConstRef::toByteArray(const QByteArray
    #      &defaultValue) const
    if defaultValue is None:
      from . import QByteArray
      defaultValue = QByteArray()
    address = self.uglySide.call(
        'ritual_ZNK18QCborValueConstRef11toByteArrayERK10QByteArray',
        self._valueOf(defaultValue),
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  @overload()
  @overload(str)
  def toString(self, defaultValue: str = '') -> str:
    """
    Calls Qt's 'QString QCborValueConstRef::toString(const QString
    &defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#toString

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
    #  QString QCborValueConstRef::toString(const QString &defaultValue)
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QCborValueConstRef8toStringERK7QString', defaultValue,
    )

  @overload()
  @overload(str)
  def toStringView(self, defaultValue: str = '') -> str:
    """
    Calls Qt's 'QAnyStringView
    QCborValueConstRef::toStringView(QAnyStringView defaultValue) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborvalueconstref.html#toStringView

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
    #  QAnyStringView QCborValueConstRef::toStringView(QAnyStringView
    #      defaultValue) const
    return self.uglySide.call(
        'ritual_ZNK18QCborValueConstRef12toStringViewE14QAnyStringView',
        defaultValue,
    )

  @overload()
  @overload(QDateTime)
  def toDateTime(
      self,
      defaultValue: Optional[QDateTime] = None,
  ) -> QDateTime:
    """
    Calls Qt's 'QDateTime QCborValueConstRef::toDateTime(const QDateTime
    &defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#toDateTime

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
    #  QDateTime QCborValueConstRef::toDateTime(const QDateTime
    #      &defaultValue) const
    if defaultValue is None:
      from . import QDateTime
      defaultValue = QDateTime()
    address = self.uglySide.call(
        'ritual_ZNK18QCborValueConstRef10toDateTimeERK9QDateTime',
        self._valueOf(defaultValue),
    )
    from . import QDateTime
    return QDateTime._cuteOwning(address)

  @overload()
  @overload(QUrl)
  def toUrl(self, defaultValue: Optional[QUrl] = None) -> QUrl:
    """
    Calls Qt's 'QUrl QCborValueConstRef::toUrl(const QUrl &defaultValue)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#toUrl

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
    #  QUrl QCborValueConstRef::toUrl(const QUrl &defaultValue) const
    if defaultValue is None:
      from . import QUrl
      defaultValue = QUrl()
    address = self.uglySide.call(
        'ritual_ZNK18QCborValueConstRef5toUrlERK4QUrl',
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
    Calls Qt's 'QRegularExpression
    QCborValueConstRef::toRegularExpression(const QRegularExpression
    &defaultValue) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborvalueconstref.html#toRegularExpression

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
    #  QRegularExpression QCborValueConstRef::toRegularExpression(const
    #      QRegularExpression &defaultValue) const
    if defaultValue is None:
      from . import QRegularExpression
      defaultValue = QRegularExpression()
    address = self.uglySide.call(
        'ritual_ZNK18QCborValueConstRef19toRegularExpressionERK18QRegularEx'
        'pression',
        self._valueOf(defaultValue),
    )
    from . import QRegularExpression
    return QRegularExpression._cuteOwning(address)

  @overload()
  @overload(QUuid)
  def toUuid(self, defaultValue: Optional[QUuid] = None) -> QUuid:
    """
    Calls Qt's 'QUuid QCborValueConstRef::toUuid(const QUuid &defaultValue)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#toUuid

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
    #  QUuid QCborValueConstRef::toUuid(const QUuid &defaultValue) const
    if defaultValue is None:
      from . import QUuid
      defaultValue = QUuid()
    address = self.uglySide.call(
        'ritual_ZNK18QCborValueConstRef6toUuidERK5QUuid',
        self._valueOf(defaultValue),
    )
    from . import QUuid
    return QUuid._cuteOwning(address)

  @overload()
  def toArray(self) -> QCborArray:
    """
    Calls Qt's 'QCborArray QCborValueConstRef::toArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#toArray

    Returns
    -------

    QCborArray
      A new cute QCborArray around the copy Qt gave back. Python owns it.
    """
    #  QCborArray QCborValueConstRef::toArray() const
    address = self.uglySide.call('ritual_ZNK18QCborValueConstRef7toArrayEv')
    from . import QCborArray
    return QCborArray._cuteOwning(address)

  @overload(QCborArray)
  def toArray(self, a: QCborArray) -> QCborArray:
    """
    Calls Qt's 'QCborArray QCborValueConstRef::toArray(const QCborArray &a)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#toArray

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
    #  QCborArray QCborValueConstRef::toArray(const QCborArray &a) const
    address = self.uglySide.call(
        'ritual_ZNK18QCborValueConstRef7toArrayERK10QCborArray',
        self._valueOf(a),
    )
    from . import QCborArray
    return QCborArray._cuteOwning(address)

  @overload()
  def toMap(self) -> QCborMap:
    """
    Calls Qt's 'QCborMap QCborValueConstRef::toMap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#toMap

    Returns
    -------

    QCborMap
      A new cute QCborMap around the copy Qt gave back. Python owns it.
    """
    #  QCborMap QCborValueConstRef::toMap() const
    address = self.uglySide.call('ritual_ZNK18QCborValueConstRef5toMapEv')
    from . import QCborMap
    return QCborMap._cuteOwning(address)

  @overload(QCborMap)
  def toMap(self, m: QCborMap) -> QCborMap:
    """
    Calls Qt's 'QCborMap QCborValueConstRef::toMap(const QCborMap &m) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#toMap

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
    #  QCborMap QCborValueConstRef::toMap(const QCborMap &m) const
    address = self.uglySide.call(
        'ritual_ZNK18QCborValueConstRef5toMapERK8QCborMap', self._valueOf(m),
    )
    from . import QCborMap
    return QCborMap._cuteOwning(address)

  @overload(QCborValue)
  def compare(self, other: QCborValue) -> int:
    """
    Calls Qt's 'int QCborValueConstRef::compare(const QCborValue &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#compare

    Parameters
    ----------

    other : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  int QCborValueConstRef::compare(const QCborValue &other) const
    return self.uglySide.call(
        'ritual_ZNK18QCborValueConstRef7compareERK10QCborValue',
        self._valueOf(other),
    )

  def toVariant(self) -> QVariant:
    """
    Calls Qt's 'QVariant QCborValueConstRef::toVariant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#toVariant

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QCborValueConstRef::toVariant() const
    address = self.uglySide.call(
        'ritual_ZNK18QCborValueConstRef9toVariantEv',
    )
    from . import QVariant
    return QVariant._cuteOwning(address)

  def toJsonValue(self) -> QJsonValue:
    """
    Calls Qt's 'QJsonValue QCborValueConstRef::toJsonValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborvalueconstref.html#toJsonValue

    Returns
    -------

    QJsonValue
      A new cute QJsonValue around the copy Qt gave back. Python owns it.
    """
    #  QJsonValue QCborValueConstRef::toJsonValue() const
    address = self.uglySide.call(
        'ritual_ZNK18QCborValueConstRef11toJsonValueEv',
    )
    from . import QJsonValue
    return QJsonValue._cuteOwning(address)

  @overload()
  @overload(QCborValue.EncodingOptions)
  def toCbor(
      self,
      opt: QCborValue.EncodingOptions = (
          QCborValue.EncodingOptions.NoTransformation),
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    QCborValueConstRef::toCbor(QCborValue::EncodingOptions opt) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#toCbor

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
    #  QByteArray QCborValueConstRef::toCbor(QCborValue::EncodingOptions opt)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QCborValueConstRef6toCborE6QFlagsIN10QCborValue14Encod'
        'ingOptionEE',
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
    Calls Qt's 'QString QCborValueConstRef::toDiagnosticNotation(QCborValue::
    DiagnosticNotationOptions opt) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborvalueconstref.html#toDiagnosticNotation

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
    #  QString QCborValueConstRef::toDiagnosticNotation(QCborValue::
    #      DiagnosticNotationOptions opt) const
    return self.uglySide.call(
        'ritual_ZNK18QCborValueConstRef20toDiagnosticNotationE6QFlagsIN10QC'
        'borValue24DiagnosticNotationOptionEE',
        opt.value,
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

  @overload(str)
  def __getitem__(self, key: str) -> QCborValue:
    """
    Calls Qt's 'const QCborValue QCborValueConstRef::operator[](const QString
    &key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#operator[]

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  const QCborValue QCborValueConstRef::operator[](const QString &key)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QCborValueConstRefixERK7QString', key,
    )
    return QCborValue._cuteOwning(address)

  @overload(QLatin1String)
  def __getitem__(self, key: QLatin1String) -> QCborValue:
    """
    Calls Qt's 'const QCborValue
    QCborValueConstRef::operator[](QLatin1StringView key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#operator[]

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
    #  const QCborValue QCborValueConstRef::operator[](QLatin1StringView key)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QCborValueConstRefixE13QLatin1String',
        self._valueOf(key),
    )
    return QCborValue._cuteOwning(address)

  @overload(int)
  def __getitem__(self, key: int) -> QCborValue:
    """
    Calls Qt's 'const QCborValue QCborValueConstRef::operator[](qint64 key)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#operator[]

    Parameters
    ----------

    key : int
      Passed on as it is.

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  const QCborValue QCborValueConstRef::operator[](qint64 key) const
    address = self.uglySide.call('ritual_ZNK18QCborValueConstRefixEx', key)
    return QCborValue._cuteOwning(address)

  @overload(THIS)
  def __eq__(self, rhs: QCborValueConstRef) -> bool:
    """
    Calls Qt's 'bool operator==(const QCborValueConstRef &lhs, const
    QCborValueConstRef &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#operator==

    Parameters
    ----------

    rhs : QCborValueConstRef
      Passed on as a value: Qt reads the C++ QCborValueConstRef, which stays
      Python's own.
    """
    #  bool operator==(const QCborValueConstRef &lhs, const
    #      QCborValueConstRef &rhs)
    return Rituals.call(
        'ritual_ZeqRK18QCborValueConstRefS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QCborValue)
  def __eq__(self, rhs: QCborValue) -> bool:
    """
    Calls Qt's 'bool operator==(const QCborValueConstRef &lhs, const
    QCborValue &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#operator==

    Parameters
    ----------

    rhs : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  bool operator==(const QCborValueConstRef &lhs, const QCborValue &rhs)
    return Rituals.call(
        'ritual_ZeqRK18QCborValueConstRefRK10QCborValue',
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
  def __ne__(self, rhs: QCborValueConstRef) -> bool:
    """
    Calls Qt's 'bool operator!=(const QCborValueConstRef &lhs, const
    QCborValueConstRef &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#operator!=

    Parameters
    ----------

    rhs : QCborValueConstRef
      Passed on as a value: Qt reads the C++ QCborValueConstRef, which stays
      Python's own.
    """
    #  bool operator!=(const QCborValueConstRef &lhs, const
    #      QCborValueConstRef &rhs)
    return Rituals.call(
        'ritual_ZneRK18QCborValueConstRefS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QCborValue)
  def __ne__(self, rhs: QCborValue) -> bool:
    """
    Calls Qt's 'bool operator!=(const QCborValueConstRef &lhs, const
    QCborValue &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#operator!=

    Parameters
    ----------

    rhs : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  bool operator!=(const QCborValueConstRef &lhs, const QCborValue &rhs)
    return Rituals.call(
        'ritual_ZneRK18QCborValueConstRefRK10QCborValue',
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
  def __lt__(self, rhs: QCborValueConstRef) -> bool:
    """
    Calls Qt's 'bool operator<(const QCborValueConstRef &lhs, const
    QCborValueConstRef &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#operator<

    Parameters
    ----------

    rhs : QCborValueConstRef
      Passed on as a value: Qt reads the C++ QCborValueConstRef, which stays
      Python's own.
    """
    #  bool operator<(const QCborValueConstRef &lhs, const QCborValueConstRef
    #      &rhs)
    return Rituals.call(
        'ritual_ZltRK18QCborValueConstRefS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QCborValue)
  def __lt__(self, rhs: QCborValue) -> bool:
    """
    Calls Qt's 'bool operator<(const QCborValueConstRef &lhs, const
    QCborValue &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#operator<

    Parameters
    ----------

    rhs : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  bool operator<(const QCborValueConstRef &lhs, const QCborValue &rhs)
    return Rituals.call(
        'ritual_ZltRK18QCborValueConstRefRK10QCborValue',
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
  def __gt__(self, rhs: QCborValueConstRef) -> bool:
    """
    Calls Qt's 'bool operator>(const QCborValueConstRef &lhs, const
    QCborValueConstRef &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#operator>

    Parameters
    ----------

    rhs : QCborValueConstRef
      Passed on as a value: Qt reads the C++ QCborValueConstRef, which stays
      Python's own.
    """
    #  bool operator>(const QCborValueConstRef &lhs, const QCborValueConstRef
    #      &rhs)
    return Rituals.call(
        'ritual_ZgtRK18QCborValueConstRefS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QCborValue)
  def __gt__(self, rhs: QCborValue) -> bool:
    """
    Calls Qt's 'bool operator>(const QCborValueConstRef &lhs, const
    QCborValue &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#operator>

    Parameters
    ----------

    rhs : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  bool operator>(const QCborValueConstRef &lhs, const QCborValue &rhs)
    return Rituals.call(
        'ritual_ZgtRK18QCborValueConstRefRK10QCborValue',
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
  def __le__(self, rhs: QCborValueConstRef) -> bool:
    """
    Calls Qt's 'bool operator<=(const QCborValueConstRef &lhs, const
    QCborValueConstRef &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#operator<=

    Parameters
    ----------

    rhs : QCborValueConstRef
      Passed on as a value: Qt reads the C++ QCborValueConstRef, which stays
      Python's own.
    """
    #  bool operator<=(const QCborValueConstRef &lhs, const
    #      QCborValueConstRef &rhs)
    return Rituals.call(
        'ritual_ZleRK18QCborValueConstRefS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QCborValue)
  def __le__(self, rhs: QCborValue) -> bool:
    """
    Calls Qt's 'bool operator<=(const QCborValueConstRef &lhs, const
    QCborValue &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#operator<=

    Parameters
    ----------

    rhs : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  bool operator<=(const QCborValueConstRef &lhs, const QCborValue &rhs)
    return Rituals.call(
        'ritual_ZleRK18QCborValueConstRefRK10QCborValue',
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
  def __ge__(self, rhs: QCborValueConstRef) -> bool:
    """
    Calls Qt's 'bool operator>=(const QCborValueConstRef &lhs, const
    QCborValueConstRef &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#operator>=

    Parameters
    ----------

    rhs : QCborValueConstRef
      Passed on as a value: Qt reads the C++ QCborValueConstRef, which stays
      Python's own.
    """
    #  bool operator>=(const QCborValueConstRef &lhs, const
    #      QCborValueConstRef &rhs)
    return Rituals.call(
        'ritual_ZgeRK18QCborValueConstRefS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QCborValue)
  def __ge__(self, rhs: QCborValue) -> bool:
    """
    Calls Qt's 'bool operator>=(const QCborValueConstRef &lhs, const
    QCborValue &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborvalueconstref.html#operator>=

    Parameters
    ----------

    rhs : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  bool operator>=(const QCborValueConstRef &lhs, const QCborValue &rhs)
    return Rituals.call(
        'ritual_ZgeRK18QCborValueConstRefRK10QCborValue',
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

  @overload(THIS)
  def __init__(self, a0: QCborValueConstRef) -> None:
    """
    Notes what was given, for Qt's
    'QCborValueConstRef::QCborValueConstRef(const QCborValueConstRef &a0)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborvalueconstref.html#QCborValueConstRef

    Parameters
    ----------

    a0 : QCborValueConstRef
      Passed on as a value: Qt reads the C++ QCborValueConstRef, which stays
      Python's own.
    """
    #  QCborValueConstRef::QCborValueConstRef(const QCborValueConstRef &a0)
    self._noteCreation(QCborValueConstRef, lambda: Rituals.call(
        'ritual_ZN18QCborValueConstRefC1ERKS_', self._valueOf(a0),
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
