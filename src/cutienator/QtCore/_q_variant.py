"""
QVariant binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qvariant.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ._q_byte_array import QByteArray
from ._q_char import QChar
from ._q_date_time import QDateTime
from ._q_line import QLine
from ._q_line_f import QLineF
from ._q_locale import QLocale
from ._q_model_index import QModelIndex
from ._q_point import QPoint
from ._q_point_f import QPointF
from ._q_rect import QRect
from ._q_rect_f import QRectF
from ._q_regular_expression import QRegularExpression
from ._q_size import QSize
from ._q_size_f import QSizeF
from ._q_url import QUrl
from ._q_variant_type import Type

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QVariant(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QVariant: a plain Python object standing in front of
  one C++ QVariant.

  C++ hands a QVariant around as a copy, so every C++ QVariant behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QVariant that has a ritual and that Python can call
  so far, 31 names in all: 'userType', 'typeId', 'typeName', 'canConvert',
  'convert', 'isValid', 'isNull', 'clear', 'detach', 'isDetached', 'toBool',
  'toByteArray', 'toString', 'toChar', 'toDateTime', 'toPoint', 'toPointF',
  'toRect', 'toSize', 'toSizeF', 'toLine', 'toLineF', 'toRectF', 'toLocale',
  'toRegularExpression', 'toUrl', 'toModelIndex', 'type', 'typeToName',
  'nameToType', 'setValue'. It can be made from Python, in 23 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVariant::~QVariant()': the destructor: Python removes its C++
    QVariant by it, and has no other use for it.
  - Qt's 'QVariant::QVariant(uint ui)': takes in Python what
    'QVariant::QVariant(int i)' takes.
  - Qt's 'QVariant::QVariant(qlonglong ll)': takes in Python what
    'QVariant::QVariant(int i)' takes.
  - Qt's 'QVariant::QVariant(qulonglong ull)': takes in Python what
    'QVariant::QVariant(int i)' takes.
  - Qt's 'QVariant::QVariant(float f)': takes in Python what
    'QVariant::QVariant(double d)' takes.
  - Qt's 'QVariant::QVariant(QDate date)': names 'QDate', which has no cute
    class yet.
  - Qt's 'QVariant::QVariant(QTime time)': names 'QTime', which has no cute
    class yet.
  - Qt's 'QVariant::QVariant(const QBitArray &bitarray)': names 'QBitArray',
    which has no cute class yet.
  - Qt's 'QVariant::QVariant(const QJsonArray &jsonArray)': names
    'QJsonArray', which has no cute class yet.
  - Qt's 'QVariant::QVariant(const QJsonObject &jsonObject)': names
    'QJsonObject', which has no cute class yet.
  - Qt's 'QVariant::QVariant(const QJsonValue &jsonValue)': names
    'QJsonValue', which has no cute class yet.
  - Qt's 'QVariant::QVariant(QUuid uuid)': names 'QUuid', which has no cute
    class yet.
  - Qt's 'QVariant::QVariant(const QEasingCurve &easing)': names
    'QEasingCurve', which has no cute class yet.
  - Qt's 'QVariant::QVariant(const QJsonDocument &jsonDocument)': names
    'QJsonDocument', which has no cute class yet.
  - Qt's 'QVariant::QVariant(const QPersistentModelIndex &modelIndex)': names
    'QPersistentModelIndex', which has no cute class yet.
  - Qt's 'QVariant::QVariant(QLatin1StringView string)': names
    'QLatin1String', which has no cute class yet.
  - Qt's 'QMetaType QVariant::metaType() const': gives 'QMetaType', which has
    no cute class yet.
  - Qt's 'bool QVariant::canConvert(QMetaType targetType) const': names
    'QMetaType', which has no cute class yet.
  - Qt's 'bool QVariant::convert(QMetaType type)': names 'QMetaType', which
    has no cute class yet.
  - Qt's 'bool QVariant::canView(QMetaType targetType) const': names
    'QMetaType', which has no cute class yet.
  - Qt's 'int QVariant::toInt(bool *ok) const': takes a number to change
    where it is.
  - Qt's 'uint QVariant::toUInt(bool *ok) const': takes a number to change
    where it is.
  - Qt's 'qlonglong QVariant::toLongLong(bool *ok) const': takes a number to
    change where it is.
  - Qt's 'qulonglong QVariant::toULongLong(bool *ok) const': takes a number
    to change where it is.
  - Qt's 'double QVariant::toDouble(bool *ok) const': takes a number to
    change where it is.
  - Qt's 'float QVariant::toFloat(bool *ok) const': takes a number to change
    where it is.
  - Qt's 'qreal QVariant::toReal(bool *ok) const': takes a number to change
    where it is.
  - Qt's 'QBitArray QVariant::toBitArray() const': gives 'QBitArray', which
    has no cute class yet.
  - Qt's 'QDate QVariant::toDate() const': gives 'QDate', which has no cute
    class yet.
  - Qt's 'QTime QVariant::toTime() const': gives 'QTime', which has no cute
    class yet.
  - Qt's 'QEasingCurve QVariant::toEasingCurve() const': gives
    'QEasingCurve', which has no cute class yet.
  - Qt's 'QUuid QVariant::toUuid() const': gives 'QUuid', which has no cute
    class yet.
  - Qt's 'QJsonValue QVariant::toJsonValue() const': gives 'QJsonValue',
    which has no cute class yet.
  - Qt's 'QJsonObject QVariant::toJsonObject() const': gives 'QJsonObject',
    which has no cute class yet.
  - Qt's 'QJsonArray QVariant::toJsonArray() const': gives 'QJsonArray',
    which has no cute class yet.
  - Qt's 'QJsonDocument QVariant::toJsonDocument() const': gives
    'QJsonDocument', which has no cute class yet.
  - Qt's 'QPersistentModelIndex QVariant::toPersistentModelIndex() const':
    gives 'QPersistentModelIndex', which has no cute class yet.
  - Qt's 'QPartialOrdering QVariant::compare(const QVariant &lhs, const
    QVariant &rhs)': gives 'QPartialOrdering', which has no cute class yet.

  What has no ritual
  ------------------

  76 of the 168 functions Qt declares: 39 takes or gives a type that cannot
  be passed yet; 21 a template; 6 forbidden; 5 private; 5 protected.

  What to expect
  --------------

  - The C++ QVariant is created at the first use, not by 'QVariant(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QVariant back gives a copy the ritual made for
    Python, in a new cute QVariant.
  """

  #  The enums Qt writes inside QVariant, and the names Qt has for the
  #  combinations of its flags enums.
  Type = Type

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int)
  def typeToName(typeId: int) -> Optional[str]:
    """
    Calls Qt's 'const char *QVariant::typeToName(int typeId)'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#typeToName

    Parameters
    ----------

    typeId : int
      Passed on as it is.

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QVariant::typeToName(int typeId)
    chars = Rituals.call('ritual_ZN8QVariant10typeToNameEi', typeId)
    return None if chars is None else chars.decode()

  @staticmethod
  @overload(str)
  @overload(NoneType)
  def nameToType(name: Optional[str]) -> Type:
    """
    Calls Qt's 'Type QVariant::nameToType(const char *name)'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#nameToType

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QVariant::nameToType(const char *name)
    return Type(Rituals.call(
        'ritual_ZN8QVariant10nameToTypeEPKc', CuteMixin._bytesOf(name),
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVariant'

  #  Qt's '~QVariant()'. Naming it makes this a value class: Python owns
  #  every C++ QVariant behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8QVariantD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def userType(self) -> int:
    """
    Calls Qt's 'int QVariant::userType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#userType
    """
    #  int QVariant::userType() const
    return self.uglySide.call('ritual_ZNK8QVariant8userTypeEv')

  def typeId(self) -> int:
    """
    Calls Qt's 'int QVariant::typeId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#typeId
    """
    #  int QVariant::typeId() const
    return self.uglySide.call('ritual_ZNK8QVariant6typeIdEv')

  def typeName(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QVariant::typeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#typeName

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QVariant::typeName() const
    chars = self.uglySide.call('ritual_ZNK8QVariant8typeNameEv')
    return None if chars is None else chars.decode()

  @overload(int)
  def canConvert(self, targetTypeId: int) -> bool:
    """
    Calls Qt's 'bool QVariant::canConvert(int targetTypeId) const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#canConvert

    Parameters
    ----------

    targetTypeId : int
      Passed on as it is.
    """
    #  bool QVariant::canConvert(int targetTypeId) const
    return self.uglySide.call(
        'ritual_ZNK8QVariant10canConvertEi', targetTypeId,
    )

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QVariant::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#isValid
    """
    #  bool QVariant::isValid() const
    return self.uglySide.call('ritual_ZNK8QVariant7isValidEv')

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QVariant::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#isNull
    """
    #  bool QVariant::isNull() const
    return self.uglySide.call('ritual_ZNK8QVariant6isNullEv')

  def isDetached(self) -> bool:
    """
    Calls Qt's 'bool QVariant::isDetached() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#isDetached
    """
    #  bool QVariant::isDetached() const
    return self.uglySide.call('ritual_ZNK8QVariant10isDetachedEv')

  def toBool(self) -> bool:
    """
    Calls Qt's 'bool QVariant::toBool() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#toBool
    """
    #  bool QVariant::toBool() const
    return self.uglySide.call('ritual_ZNK8QVariant6toBoolEv')

  def toByteArray(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QVariant::toByteArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#toByteArray

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QVariant::toByteArray() const
    address = self.uglySide.call('ritual_ZNK8QVariant11toByteArrayEv')
    return QByteArray._cuteOwning(address)

  def toString(self) -> str:
    """
    Calls Qt's 'QString QVariant::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QVariant::toString() const
    return self.uglySide.call('ritual_ZNK8QVariant8toStringEv')

  def toChar(self) -> QChar:
    """
    Calls Qt's 'QChar QVariant::toChar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#toChar

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QVariant::toChar() const
    address = self.uglySide.call('ritual_ZNK8QVariant6toCharEv')
    return QChar._cuteOwning(address)

  def toDateTime(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QVariant::toDateTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#toDateTime

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QVariant::toDateTime() const
    address = self.uglySide.call('ritual_ZNK8QVariant10toDateTimeEv')
    return QDateTime._cuteOwning(address)

  def toPoint(self) -> QPoint:
    """
    Calls Qt's 'QPoint QVariant::toPoint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#toPoint

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QVariant::toPoint() const
    address = self.uglySide.call('ritual_ZNK8QVariant7toPointEv')
    return QPoint._cuteOwning(address)

  def toPointF(self) -> QPointF:
    """
    Calls Qt's 'QPointF QVariant::toPointF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#toPointF

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QVariant::toPointF() const
    address = self.uglySide.call('ritual_ZNK8QVariant8toPointFEv')
    return QPointF._cuteOwning(address)

  def toRect(self) -> QRect:
    """
    Calls Qt's 'QRect QVariant::toRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#toRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QVariant::toRect() const
    address = self.uglySide.call('ritual_ZNK8QVariant6toRectEv')
    return QRect._cuteOwning(address)

  def toSize(self) -> QSize:
    """
    Calls Qt's 'QSize QVariant::toSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#toSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QVariant::toSize() const
    address = self.uglySide.call('ritual_ZNK8QVariant6toSizeEv')
    return QSize._cuteOwning(address)

  def toSizeF(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QVariant::toSizeF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#toSizeF

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QVariant::toSizeF() const
    address = self.uglySide.call('ritual_ZNK8QVariant7toSizeFEv')
    return QSizeF._cuteOwning(address)

  def toLine(self) -> QLine:
    """
    Calls Qt's 'QLine QVariant::toLine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#toLine

    Returns
    -------

    QLine
      A new cute QLine around the copy Qt gave back. Python owns it.
    """
    #  QLine QVariant::toLine() const
    address = self.uglySide.call('ritual_ZNK8QVariant6toLineEv')
    return QLine._cuteOwning(address)

  def toLineF(self) -> QLineF:
    """
    Calls Qt's 'QLineF QVariant::toLineF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#toLineF

    Returns
    -------

    QLineF
      A new cute QLineF around the copy Qt gave back. Python owns it.
    """
    #  QLineF QVariant::toLineF() const
    address = self.uglySide.call('ritual_ZNK8QVariant7toLineFEv')
    return QLineF._cuteOwning(address)

  def toRectF(self) -> QRectF:
    """
    Calls Qt's 'QRectF QVariant::toRectF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#toRectF

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QVariant::toRectF() const
    address = self.uglySide.call('ritual_ZNK8QVariant7toRectFEv')
    return QRectF._cuteOwning(address)

  def toLocale(self) -> QLocale:
    """
    Calls Qt's 'QLocale QVariant::toLocale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#toLocale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QVariant::toLocale() const
    address = self.uglySide.call('ritual_ZNK8QVariant8toLocaleEv')
    return QLocale._cuteOwning(address)

  def toRegularExpression(self) -> QRegularExpression:
    """
    Calls Qt's 'QRegularExpression QVariant::toRegularExpression() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#toRegularExpression

    Returns
    -------

    QRegularExpression
      A new cute QRegularExpression around the copy Qt gave back. Python owns
      it.
    """
    #  QRegularExpression QVariant::toRegularExpression() const
    address = self.uglySide.call(
        'ritual_ZNK8QVariant19toRegularExpressionEv',
    )
    return QRegularExpression._cuteOwning(address)

  def toUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QVariant::toUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#toUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QVariant::toUrl() const
    address = self.uglySide.call('ritual_ZNK8QVariant5toUrlEv')
    return QUrl._cuteOwning(address)

  def toModelIndex(self) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QVariant::toModelIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#toModelIndex

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QVariant::toModelIndex() const
    address = self.uglySide.call('ritual_ZNK8QVariant12toModelIndexEv')
    return QModelIndex._cuteOwning(address)

  def type(self) -> Type:
    """
    Calls Qt's 'Type QVariant::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QVariant::type() const
    return Type(self.uglySide.call('ritual_ZNK8QVariant4typeEv'))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def setValue(self, avalue: QVariant) -> None:
    """
    Calls Qt's 'void QVariant::setValue(const QVariant &avalue)'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#setValue

    Parameters
    ----------

    avalue : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QVariant::setValue(const QVariant &avalue)
    self.uglySide.call(
        'ritual_ZN8QVariant8setValueERKS_', self._valueOf(avalue),
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
    Notes what was given, for Qt's 'QVariant::QVariant()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant
    """
    #  QVariant::QVariant()
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QVariant) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(const QVariant
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    other : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  QVariant::QVariant(const QVariant &other)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1ERKS_', self._valueOf(other),
    ))

  @overload(int)
  def __init__(self, i: int) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(int i)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  QVariant::QVariant(int i)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1Ei', i,
    ))

  @overload(bool)
  def __init__(self, b: bool) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(bool b)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  QVariant::QVariant(bool b)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1Eb', b,
    ))

  @overload(float)
  def __init__(self, d: float) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(double d)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    d : float
      Passed on as it is.
    """
    #  QVariant::QVariant(double d)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1Ed', d,
    ))

  @overload(QChar)
  def __init__(self, qchar: QChar) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(QChar qchar)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    qchar : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  QVariant::QVariant(QChar qchar)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1E5QChar', self._valueOf(qchar),
    ))

  @overload(QByteArray)
  def __init__(self, bytearray: QByteArray) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(const QByteArray
    &bytearray)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    bytearray : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QVariant::QVariant(const QByteArray &bytearray)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1ERK10QByteArray', self._valueOf(bytearray),
    ))

  @overload(QDateTime)
  def __init__(self, datetime: QDateTime) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(const QDateTime
    &datetime)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    datetime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  QVariant::QVariant(const QDateTime &datetime)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1ERK9QDateTime', self._valueOf(datetime),
    ))

  @overload(QLocale)
  def __init__(self, locale: QLocale) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(const QLocale
    &locale)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  QVariant::QVariant(const QLocale &locale)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1ERK7QLocale', self._valueOf(locale),
    ))

  @overload(QRegularExpression)
  def __init__(self, re: QRegularExpression) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(const
    QRegularExpression &re)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    re : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  QVariant::QVariant(const QRegularExpression &re)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1ERK18QRegularExpression', self._valueOf(re),
    ))

  @overload(str)
  def __init__(self, string: str) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(const QString
    &string)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QVariant::QVariant(const QString &string)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1ERK7QString', string,
    ))

  @overload(QUrl)
  def __init__(self, url: QUrl) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(const QUrl &url)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  QVariant::QVariant(const QUrl &url)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1ERK4QUrl', self._valueOf(url),
    ))

  @overload(QModelIndex)
  def __init__(self, modelIndex: QModelIndex) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(const QModelIndex
    &modelIndex)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    modelIndex : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  QVariant::QVariant(const QModelIndex &modelIndex)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1ERK11QModelIndex', self._valueOf(modelIndex),
    ))

  @overload(QSize)
  def __init__(self, size: QSize) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(QSize size)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  QVariant::QVariant(QSize size)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1E5QSize', self._valueOf(size),
    ))

  @overload(QSizeF)
  def __init__(self, size: QSizeF) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(QSizeF size)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  QVariant::QVariant(QSizeF size)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1E6QSizeF', self._valueOf(size),
    ))

  @overload(QPoint)
  def __init__(self, pt: QPoint) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(QPoint pt)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    pt : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  QVariant::QVariant(QPoint pt)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1E6QPoint', self._valueOf(pt),
    ))

  @overload(QPointF)
  def __init__(self, pt: QPointF) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(QPointF pt)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    pt : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  QVariant::QVariant(QPointF pt)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1E7QPointF', self._valueOf(pt),
    ))

  @overload(QLine)
  def __init__(self, line: QLine) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(QLine line)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    line : QLine
      Passed on as a value: Qt reads the C++ QLine, which stays Python's own.
    """
    #  QVariant::QVariant(QLine line)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1E5QLine', self._valueOf(line),
    ))

  @overload(QLineF)
  def __init__(self, line: QLineF) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(QLineF line)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    line : QLineF
      Passed on as a value: Qt reads the C++ QLineF, which stays Python's
      own.
    """
    #  QVariant::QVariant(QLineF line)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1E6QLineF', self._valueOf(line),
    ))

  @overload(QRect)
  def __init__(self, rect: QRect) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(QRect rect)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  QVariant::QVariant(QRect rect)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1E5QRect', self._valueOf(rect),
    ))

  @overload(QRectF)
  def __init__(self, rect: QRectF) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(QRectF rect)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  QVariant::QVariant(QRectF rect)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1E6QRectF', self._valueOf(rect),
    ))

  @overload(NoneType)
  def __init__(self, str: Optional[str]) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(const char *str)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    str : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  QVariant::QVariant(const char *str)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1EPKc', self._bytesOf(str),
    ))

  @overload(Type)
  def __init__(self, type: Type) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(Type type)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    type : Type
      Passed on as its number.
    """
    #  QVariant::QVariant(Type type)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1ENS_4TypeE', type.value,
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

  @overload(int)
  def convert(self, targetTypeId: int) -> bool:
    """
    Calls Qt's 'bool QVariant::convert(int targetTypeId)'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#convert

    Parameters
    ----------

    targetTypeId : int
      Passed on as it is.
    """
    #  bool QVariant::convert(int targetTypeId)
    return self.uglySide.call('ritual_ZN8QVariant7convertEi', targetTypeId)

  def clear(self) -> None:
    """
    Calls Qt's 'void QVariant::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#clear
    """
    #  void QVariant::clear()
    self.uglySide.call('ritual_ZN8QVariant5clearEv')

  def detach(self) -> None:
    """
    Calls Qt's 'void QVariant::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#detach
    """
    #  void QVariant::detach()
    self.uglySide.call('ritual_ZN8QVariant6detachEv')
