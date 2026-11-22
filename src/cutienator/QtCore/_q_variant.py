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
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QHash, QList, QMap, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QBitArray, QByteArray, QChar, QDate, QDateTime, QEasingCurve
  from . import QJsonArray, QJsonDocument, QJsonObject, QJsonValue
  from . import QLatin1String, QLine, QLineF, QLocale, QMetaType, QModelIndex
  from . import QPartialOrdering, QPersistentModelIndex, QPoint, QPointF
  from . import QRect, QRectF, QRegularExpression, QSize, QSizeF, QTime, QUrl
  from . import QUuid
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBitArray = WAIT['QBitArray']
  QByteArray = WAIT['QByteArray']
  QChar = WAIT['QChar']
  QDate = WAIT['QDate']
  QDateTime = WAIT['QDateTime']
  QEasingCurve = WAIT['QEasingCurve']
  QJsonArray = WAIT['QJsonArray']
  QJsonDocument = WAIT['QJsonDocument']
  QJsonObject = WAIT['QJsonObject']
  QJsonValue = WAIT['QJsonValue']
  QLatin1String = WAIT['QLatin1String']
  QLine = WAIT['QLine']
  QLineF = WAIT['QLineF']
  QLocale = WAIT['QLocale']
  QMetaType = WAIT['QMetaType']
  QModelIndex = WAIT['QModelIndex']
  QPersistentModelIndex = WAIT['QPersistentModelIndex']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QRect = WAIT['QRect']
  QRectF = WAIT['QRectF']
  QRegularExpression = WAIT['QRegularExpression']
  QSize = WAIT['QSize']
  QSizeF = WAIT['QSizeF']
  QTime = WAIT['QTime']
  QUrl = WAIT['QUrl']
  QUuid = WAIT['QUuid']

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
  so far, 50 names in all: 'userType', 'typeId', 'typeName', 'metaType',
  'canConvert', 'convert', 'canView', 'isValid', 'isNull', 'clear', 'detach',
  'isDetached', 'toBool', 'toByteArray', 'toBitArray', 'toString',
  'toStringList', 'toChar', 'toDate', 'toTime', 'toDateTime', 'toList',
  'toMap', 'toHash', 'toPoint', 'toPointF', 'toRect', 'toSize', 'toSizeF',
  'toLine', 'toLineF', 'toRectF', 'toLocale', 'toRegularExpression',
  'toEasingCurve', 'toUuid', 'toUrl', 'toJsonValue', 'toJsonObject',
  'toJsonArray', 'toJsonDocument', 'toModelIndex', 'toPersistentModelIndex',
  'type', 'typeToName', 'nameToType', 'setValue', 'compare', '__eq__',
  '__ne__'. It can be made from Python, in 38 ways; see '__init__'.

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

  What has no ritual
  ------------------

  68 of the 170 functions Qt declares: 31 takes or gives a type that cannot
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

  #  The enums Qt writes inside QVariant, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class Type(CuteNum):
    """The enum 'QVariant::Type' of Qt, with the 60 names Qt gives in it."""

    Invalid = Kee[int](0)
    Bool = Kee[int](1)
    Int = Kee[int](2)
    UInt = Kee[int](3)
    LongLong = Kee[int](4)
    ULongLong = Kee[int](5)
    Double = Kee[int](6)
    Char = Kee[int](7)
    Map = Kee[int](8)
    List = Kee[int](9)
    String = Kee[int](10)
    StringList = Kee[int](11)
    ByteArray = Kee[int](12)
    BitArray = Kee[int](13)
    Date = Kee[int](14)
    Time = Kee[int](15)
    DateTime = Kee[int](16)
    Url = Kee[int](17)
    Locale = Kee[int](18)
    Rect = Kee[int](19)
    RectF = Kee[int](20)
    Size = Kee[int](21)
    SizeF = Kee[int](22)
    Line = Kee[int](23)
    LineF = Kee[int](24)
    Point = Kee[int](25)
    PointF = Kee[int](26)
    RegularExpression = Kee[int](44)
    Hash = Kee[int](28)
    EasingCurve = Kee[int](29)
    Uuid = Kee[int](30)
    ModelIndex = Kee[int](42)
    PersistentModelIndex = Kee[int](50)
    LastCoreType = Kee[int](63)
    Font = Kee[int](4096)
    Pixmap = Kee[int](4097)
    Brush = Kee[int](4098)
    Color = Kee[int](4099)
    Palette = Kee[int](4100)
    Image = Kee[int](4102)
    Polygon = Kee[int](4103)
    Region = Kee[int](4104)
    Bitmap = Kee[int](4105)
    Cursor = Kee[int](4106)
    KeySequence = Kee[int](4107)
    Pen = Kee[int](4108)
    TextLength = Kee[int](4109)
    TextFormat = Kee[int](4110)
    Transform = Kee[int](4112)
    Matrix4x4 = Kee[int](4113)
    Vector2D = Kee[int](4114)
    Vector3D = Kee[int](4115)
    Vector4D = Kee[int](4116)
    Quaternion = Kee[int](4117)
    PolygonF = Kee[int](4118)
    Icon = Kee[int](4101)
    LastGuiType = Kee[int](4119)
    SizePolicy = Kee[int](8192)
    UserType = Kee[int](65536)
    LastType = Kee[int](4294967295)

  #  The classes Qt writes inside QVariant, each a class in here as in C++.

  class Private(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QVariant::Private: a plain Python object standing
    in front of one C++ QVariant::Private.

    C++ hands a QVariant::Private around as a copy, so every C++
    QVariant::Private behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QVariant::Private that has a ritual and that
    Python can call so far, 1 name in all: 'type'. It can be made from
    Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'bool QVariant::Private::canUseInternalSpace(const
      QtPrivate::QMetaTypeInterface *type)': names
      'QtPrivate::QMetaTypeInterface', which has no cute class yet.
    - Qt's 'const QtPrivate::QMetaTypeInterface
      *QVariant::Private::typeInterface() const': gives
      'QtPrivate::QMetaTypeInterface', which has no cute class yet.
    - Qt's 'QVariant::Private::~Private()': the destructor: Python removes
      its C++ QVariant::Private by it, and has no other use for it.

    What has no ritual
    ------------------

    6 of the 11 functions Qt declares: 4 a template; 1 declared and nowhere
    to be found; 1 takes or gives a type that cannot be passed yet.

    What to expect
    --------------

    - The C++ QVariant::Private is created at the first use, not by
      'QVariant::Private(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QVariant::Private back gives a copy the ritual made
      for Python, in a new cute QVariant::Private.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QVariant::Private'

    #  Qt's '~QVariant::Private()'. Naming it makes this a value class:
    #  Python owns every C++ QVariant::Private behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = 'ritual_ZN8QVariant7PrivateD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def type(self) -> QMetaType:
      """
      Calls Qt's 'QMetaType QVariant::Private::type() const'.

      Qt's own words: https://doc.qt.io/qt-6/qvariant-private.html#type

      Returns
      -------

      QMetaType
        A new cute QMetaType around the copy Qt gave back. Python owns it.
      """
      #  QMetaType QVariant::Private::type() const
      address = self.uglySide.call('ritual_ZNK8QVariant7Private4typeEv')
      from . import QMetaType
      return QMetaType._cuteOwning(address)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QVariant::Private::Private()', which is
      called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qvariant-private.html#Private
      """
      #  QVariant::Private::Private()
      self._noteCreation(QVariant.Private, lambda: Rituals.call(
          'ritual_ZN8QVariant7PrivateC1Ev',
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class PrivateShared(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QVariant::PrivateShared: a plain Python object
    standing in front of one C++ QVariant::PrivateShared.

    C++ hands a QVariant::PrivateShared around as a copy, so every C++
    QVariant::PrivateShared behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QVariant::PrivateShared yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QVariant::PrivateShared::~PrivateShared()': the destructor:
      Python removes its C++ QVariant::PrivateShared by it, and has no other
      use for it.

    What has no ritual
    ------------------

    7 of the 8 functions Qt declares: 4 declared and nowhere to be found; 2
    takes or gives a type that cannot be passed yet; 1 private.

    What to expect
    --------------

    - The C++ QVariant::PrivateShared is created at the first use, not by
      'QVariant::PrivateShared(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QVariant::PrivateShared back gives a copy the
      ritual made for Python, in a new cute QVariant::PrivateShared.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QVariant::PrivateShared'

    #  Qt's '~QVariant::PrivateShared()'. Naming it makes this a value class:
    #  Python owns every C++ QVariant::PrivateShared behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN8QVariant13PrivateSharedD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    return QVariant.Type(Rituals.call(
        'ritual_ZN8QVariant10nameToTypeEPKc', CuteMixin._bytesOf(name),
    ))

  @staticmethod
  @overload(THIS, THIS)
  def compare(lhs: QVariant, rhs: QVariant) -> QPartialOrdering:
    """
    Calls Qt's 'QPartialOrdering QVariant::compare(const QVariant &lhs, const
    QVariant &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#compare

    Parameters
    ----------

    lhs : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    rhs : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QPartialOrdering
      A new cute QPartialOrdering around the copy Qt gave back. Python owns
      it.
    """
    #  QPartialOrdering QVariant::compare(const QVariant &lhs, const QVariant
    #      &rhs)
    address = Rituals.call(
        'ritual_ZN8QVariant7compareERKS_S1_',
        CuteMixin._valueOf(lhs), CuteMixin._valueOf(rhs),
    )
    from . import QPartialOrdering
    return QPartialOrdering._cuteOwning(address)

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

  def metaType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QVariant::metaType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#metaType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QVariant::metaType() const
    address = self.uglySide.call('ritual_ZNK8QVariant8metaTypeEv')
    from . import QMetaType
    return QMetaType._cuteOwning(address)

  @overload(QMetaType)
  def canConvert(self, targetType: QMetaType) -> bool:
    """
    Calls Qt's 'bool QVariant::canConvert(QMetaType targetType) const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#canConvert

    Parameters
    ----------

    targetType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  bool QVariant::canConvert(QMetaType targetType) const
    return self.uglySide.call(
        'ritual_ZNK8QVariant10canConvertE9QMetaType',
        self._valueOf(targetType),
    )

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

  @overload(QMetaType)
  def canView(self, targetType: QMetaType) -> bool:
    """
    Calls Qt's 'bool QVariant::canView(QMetaType targetType) const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#canView

    Parameters
    ----------

    targetType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  bool QVariant::canView(QMetaType targetType) const
    return self.uglySide.call(
        'ritual_ZNK8QVariant7canViewE9QMetaType', self._valueOf(targetType),
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
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def toBitArray(self) -> QBitArray:
    """
    Calls Qt's 'QBitArray QVariant::toBitArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#toBitArray

    Returns
    -------

    QBitArray
      A new cute QBitArray around the copy Qt gave back. Python owns it.
    """
    #  QBitArray QVariant::toBitArray() const
    address = self.uglySide.call('ritual_ZNK8QVariant10toBitArrayEv')
    from . import QBitArray
    return QBitArray._cuteOwning(address)

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

  def toStringList(self) -> QStringList:
    """
    Calls Qt's 'QStringList QVariant::toStringList() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#toStringList

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QVariant::toStringList() const
    address = self.uglySide.call('ritual_ZNK8QVariant12toStringListEv')
    return QStringList._cuteOwning(address)

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
    from . import QChar
    return QChar._cuteOwning(address)

  def toDate(self) -> QDate:
    """
    Calls Qt's 'QDate QVariant::toDate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#toDate

    Returns
    -------

    QDate
      A new cute QDate around the copy Qt gave back. Python owns it.
    """
    #  QDate QVariant::toDate() const
    address = self.uglySide.call('ritual_ZNK8QVariant6toDateEv')
    from . import QDate
    return QDate._cuteOwning(address)

  def toTime(self) -> QTime:
    """
    Calls Qt's 'QTime QVariant::toTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#toTime

    Returns
    -------

    QTime
      A new cute QTime around the copy Qt gave back. Python owns it.
    """
    #  QTime QVariant::toTime() const
    address = self.uglySide.call('ritual_ZNK8QVariant6toTimeEv')
    from . import QTime
    return QTime._cuteOwning(address)

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
    from . import QDateTime
    return QDateTime._cuteOwning(address)

  def toList(self) -> QList[QVariant]:
    """
    Calls Qt's 'QList<QVariant> QVariant::toList() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#toList

    Returns
    -------

    QList[QVariant]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QVariant> QVariant::toList() const
    address = self.uglySide.call('ritual_ZNK8QVariant6toListEv')
    return QList[QVariant]._cuteOwning(address)

  def toMap(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QMap<QString, QVariant> QVariant::toMap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#toMap

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QMap<QString, QVariant> QVariant::toMap() const
    address = self.uglySide.call('ritual_ZNK8QVariant5toMapEv')
    return QMap[str, QVariant]._cuteOwning(address)

  def toHash(self) -> QHash[str, QVariant]:
    """
    Calls Qt's 'QHash<QString, QVariant> QVariant::toHash() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#toHash

    Returns
    -------

    QHash[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<QString, QVariant> QVariant::toHash() const
    address = self.uglySide.call('ritual_ZNK8QVariant6toHashEv')
    return QHash[str, QVariant]._cuteOwning(address)

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
    from . import QPoint
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
    from . import QPointF
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
    from . import QRect
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
    from . import QSize
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
    from . import QSizeF
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
    from . import QLine
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
    from . import QLineF
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
    from . import QRectF
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
    from . import QLocale
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
    from . import QRegularExpression
    return QRegularExpression._cuteOwning(address)

  def toEasingCurve(self) -> QEasingCurve:
    """
    Calls Qt's 'QEasingCurve QVariant::toEasingCurve() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#toEasingCurve

    Returns
    -------

    QEasingCurve
      A new cute QEasingCurve around the copy Qt gave back. Python owns it.
    """
    #  QEasingCurve QVariant::toEasingCurve() const
    address = self.uglySide.call('ritual_ZNK8QVariant13toEasingCurveEv')
    from . import QEasingCurve
    return QEasingCurve._cuteOwning(address)

  def toUuid(self) -> QUuid:
    """
    Calls Qt's 'QUuid QVariant::toUuid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#toUuid

    Returns
    -------

    QUuid
      A new cute QUuid around the copy Qt gave back. Python owns it.
    """
    #  QUuid QVariant::toUuid() const
    address = self.uglySide.call('ritual_ZNK8QVariant6toUuidEv')
    from . import QUuid
    return QUuid._cuteOwning(address)

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
    from . import QUrl
    return QUrl._cuteOwning(address)

  def toJsonValue(self) -> QJsonValue:
    """
    Calls Qt's 'QJsonValue QVariant::toJsonValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#toJsonValue

    Returns
    -------

    QJsonValue
      A new cute QJsonValue around the copy Qt gave back. Python owns it.
    """
    #  QJsonValue QVariant::toJsonValue() const
    address = self.uglySide.call('ritual_ZNK8QVariant11toJsonValueEv')
    from . import QJsonValue
    return QJsonValue._cuteOwning(address)

  def toJsonObject(self) -> QJsonObject:
    """
    Calls Qt's 'QJsonObject QVariant::toJsonObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#toJsonObject

    Returns
    -------

    QJsonObject
      A new cute QJsonObject around the copy Qt gave back. Python owns it.
    """
    #  QJsonObject QVariant::toJsonObject() const
    address = self.uglySide.call('ritual_ZNK8QVariant12toJsonObjectEv')
    from . import QJsonObject
    return QJsonObject._cuteOwning(address)

  def toJsonArray(self) -> QJsonArray:
    """
    Calls Qt's 'QJsonArray QVariant::toJsonArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#toJsonArray

    Returns
    -------

    QJsonArray
      A new cute QJsonArray around the copy Qt gave back. Python owns it.
    """
    #  QJsonArray QVariant::toJsonArray() const
    address = self.uglySide.call('ritual_ZNK8QVariant11toJsonArrayEv')
    from . import QJsonArray
    return QJsonArray._cuteOwning(address)

  def toJsonDocument(self) -> QJsonDocument:
    """
    Calls Qt's 'QJsonDocument QVariant::toJsonDocument() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#toJsonDocument

    Returns
    -------

    QJsonDocument
      A new cute QJsonDocument around the copy Qt gave back. Python owns it.
    """
    #  QJsonDocument QVariant::toJsonDocument() const
    address = self.uglySide.call('ritual_ZNK8QVariant14toJsonDocumentEv')
    from . import QJsonDocument
    return QJsonDocument._cuteOwning(address)

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
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  def toPersistentModelIndex(self) -> QPersistentModelIndex:
    """
    Calls Qt's 'QPersistentModelIndex QVariant::toPersistentModelIndex()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvariant.html#toPersistentModelIndex

    Returns
    -------

    QPersistentModelIndex
      A new cute QPersistentModelIndex around the copy Qt gave back. Python
      owns it.
    """
    #  QPersistentModelIndex QVariant::toPersistentModelIndex() const
    address = self.uglySide.call(
        'ritual_ZNK8QVariant22toPersistentModelIndexEv',
    )
    from . import QPersistentModelIndex
    return QPersistentModelIndex._cuteOwning(address)

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
    return QVariant.Type(self.uglySide.call('ritual_ZNK8QVariant4typeEv'))

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

  @overload(THIS)
  def __eq__(self, rhs: QVariant) -> bool:
    """
    Calls Qt's 'bool operator==(const QVariant &lhs, const QVariant &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#operator==

    Parameters
    ----------

    rhs : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool operator==(const QVariant &lhs, const QVariant &rhs)
    return Rituals.call(
        'ritual_ZeqRK8QVariantS1_',
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
  def __ne__(self, rhs: QVariant) -> bool:
    """
    Calls Qt's 'bool operator!=(const QVariant &lhs, const QVariant &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#operator!=

    Parameters
    ----------

    rhs : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool operator!=(const QVariant &lhs, const QVariant &rhs)
    return Rituals.call(
        'ritual_ZneRK8QVariantS1_',
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

  @overload(QDate)
  def __init__(self, date: QDate) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(QDate date)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    date : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.
    """
    #  QVariant::QVariant(QDate date)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1E5QDate', self._valueOf(date),
    ))

  @overload(QTime)
  def __init__(self, time: QTime) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(QTime time)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    time : QTime
      Passed on as a value: Qt reads the C++ QTime, which stays Python's own.
    """
    #  QVariant::QVariant(QTime time)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1E5QTime', self._valueOf(time),
    ))

  @overload(QBitArray)
  def __init__(self, bitarray: QBitArray) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(const QBitArray
    &bitarray)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    bitarray : QBitArray
      Passed on as a value: Qt reads the C++ QBitArray, which stays Python's
      own.
    """
    #  QVariant::QVariant(const QBitArray &bitarray)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1ERK9QBitArray', self._valueOf(bitarray),
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

  @overload(QHash[str, WAIT['QVariant']])
  def __init__(self, hash: QHash[str, QVariant]) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(const QHash<QString,
    QVariant> &hash)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    hash : QHash[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  QVariant::QVariant(const QHash<QString, QVariant> &hash)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1ERK5QHashI7QStringS_E', self._valueOf(hash),
    ))

  @overload(QJsonArray)
  def __init__(self, jsonArray: QJsonArray) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(const QJsonArray
    &jsonArray)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    jsonArray : QJsonArray
      Passed on as a value: Qt reads the C++ QJsonArray, which stays Python's
      own.
    """
    #  QVariant::QVariant(const QJsonArray &jsonArray)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1ERK10QJsonArray', self._valueOf(jsonArray),
    ))

  @overload(QJsonObject)
  def __init__(self, jsonObject: QJsonObject) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(const QJsonObject
    &jsonObject)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    jsonObject : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  QVariant::QVariant(const QJsonObject &jsonObject)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1ERK11QJsonObject', self._valueOf(jsonObject),
    ))

  @overload(QList[WAIT['QVariant']])
  def __init__(self, list: QList[QVariant]) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(const QList<QVariant>
    &list)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    list : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  QVariant::QVariant(const QList<QVariant> &list)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1ERK5QListIS_E', self._valueOf(list),
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

  @overload(QMap[str, WAIT['QVariant']])
  def __init__(self, map: QMap[str, QVariant]) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(const QMap<QString,
    QVariant> &map)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    map : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  QVariant::QVariant(const QMap<QString, QVariant> &map)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1ERK4QMapI7QStringS_E', self._valueOf(map),
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

  @overload(QStringList)
  def __init__(self, stringlist: QStringList) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(const QStringList
    &stringlist)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    stringlist : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  QVariant::QVariant(const QStringList &stringlist)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1ERK5QListI7QStringE', self._valueOf(stringlist),
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

  @overload(QJsonValue)
  def __init__(self, jsonValue: QJsonValue) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(const QJsonValue
    &jsonValue)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    jsonValue : QJsonValue
      Passed on as a value: Qt reads the C++ QJsonValue, which stays Python's
      own.
    """
    #  QVariant::QVariant(const QJsonValue &jsonValue)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1ERK10QJsonValue', self._valueOf(jsonValue),
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

  @overload(QUuid)
  def __init__(self, uuid: QUuid) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(QUuid uuid)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    uuid : QUuid
      Passed on as a value: Qt reads the C++ QUuid, which stays Python's own.
    """
    #  QVariant::QVariant(QUuid uuid)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1E5QUuid', self._valueOf(uuid),
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

  @overload(QEasingCurve)
  def __init__(self, easing: QEasingCurve) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(const QEasingCurve
    &easing)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    easing : QEasingCurve
      Passed on as a value: Qt reads the C++ QEasingCurve, which stays
      Python's own.
    """
    #  QVariant::QVariant(const QEasingCurve &easing)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1ERK12QEasingCurve', self._valueOf(easing),
    ))

  @overload(QJsonDocument)
  def __init__(self, jsonDocument: QJsonDocument) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(const QJsonDocument
    &jsonDocument)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    jsonDocument : QJsonDocument
      Passed on as a value: Qt reads the C++ QJsonDocument, which stays
      Python's own.
    """
    #  QVariant::QVariant(const QJsonDocument &jsonDocument)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1ERK13QJsonDocument',
        self._valueOf(jsonDocument),
    ))

  @overload(QPersistentModelIndex)
  def __init__(self, modelIndex: QPersistentModelIndex) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(const
    QPersistentModelIndex &modelIndex)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    modelIndex : QPersistentModelIndex
      Passed on as a value: Qt reads the C++ QPersistentModelIndex, which
      stays Python's own.
    """
    #  QVariant::QVariant(const QPersistentModelIndex &modelIndex)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1ERK21QPersistentModelIndex',
        self._valueOf(modelIndex),
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

  @overload(QLatin1String)
  def __init__(self, string: QLatin1String) -> None:
    """
    Notes what was given, for Qt's 'QVariant::QVariant(QLatin1StringView
    string)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#QVariant

    Parameters
    ----------

    string : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  QVariant::QVariant(QLatin1StringView string)
    self._noteCreation(QVariant, lambda: Rituals.call(
        'ritual_ZN8QVariantC1E13QLatin1String', self._valueOf(string),
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

  @overload(QMetaType)
  def convert(self, type: QMetaType) -> bool:
    """
    Calls Qt's 'bool QVariant::convert(QMetaType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qvariant.html#convert

    Parameters
    ----------

    type : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  bool QVariant::convert(QMetaType type)
    return self.uglySide.call(
        'ritual_ZN8QVariant7convertE9QMetaType', self._valueOf(type),
    )

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


#  Qt's 'QList<QVariant>': the list of QVariant, which 'QList[QVariant]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QVariant. Qt has a name of its own for it.
QVariantList = QList.createKind(
    QVariant, 'value',
    name='QVariantList',
    make='ritual_list_make_QVariant',
    add='ritual_list_add_QVariant',
    size='ritual_list_size_QVariant',
    at='ritual_list_at_QVariant',
    drop='ritual_list_drop_QVariant',
)


#  Qt's 'QMap<QString, QVariant>': the QMap from text to QVariant, which
#  'QMap[str, QVariant]' gives. It is completed here, in the file of the
#  class of its values. Qt has a name of its own for it.
QVariantMap = QMap.createKind(
    str, QVariant, 'value',
    name='QVariantMap',
    make='ritual_map_make_QMap_QString_QVariant',
    put='ritual_map_put_QMap_QString_QVariant',
    size='ritual_map_size_QMap_QString_QVariant',
    key='ritual_map_key_QMap_QString_QVariant',
    value='ritual_map_value_QMap_QString_QVariant',
    has='ritual_map_has_QMap_QString_QVariant',
    get='ritual_map_get_QMap_QString_QVariant',
    drop='ritual_map_drop_QMap_QString_QVariant',
)


#  Qt's 'QHash<QString, QVariant>': the QHash from text to QVariant, which
#  'QHash[str, QVariant]' gives. It is completed here, in the file of the
#  class of its values. Qt has a name of its own for it.
QVariantHash = QHash.createKind(
    str, QVariant, 'value',
    name='QVariantHash',
    make='ritual_map_make_QHash_QString_QVariant',
    put='ritual_map_put_QHash_QString_QVariant',
    size='ritual_map_size_QHash_QString_QVariant',
    key='ritual_map_key_QHash_QString_QVariant',
    value='ritual_map_value_QHash_QString_QVariant',
    has='ritual_map_has_QHash_QString_QVariant',
    get='ritual_map_get_QHash_QString_QVariant',
    drop='ritual_map_drop_QHash_QString_QVariant',
)


#  Qt's 'QMap<int, QVariant>': the QMap from a number to QVariant, which
#  'QMap[int, QVariant]' gives. It is completed here, in the file of the
#  class of its values.
QMap.createKind(
    int, QVariant, 'value',
    make='ritual_map_make_QMap_int_QVariant',
    put='ritual_map_put_QMap_int_QVariant',
    size='ritual_map_size_QMap_int_QVariant',
    key='ritual_map_key_QMap_int_QVariant',
    value='ritual_map_value_QMap_int_QVariant',
    has='ritual_map_has_QMap_int_QVariant',
    get='ritual_map_get_QMap_int_QVariant',
    drop='ritual_map_drop_QMap_int_QVariant',
)
