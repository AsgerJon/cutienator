"""
QMetaType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qmetatype.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QByteArrayView, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArrayView = WAIT['QByteArrayView']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMetaType(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMetaType: a plain Python object standing in front of
  one C++ QMetaType.

  C++ hands a QMetaType around as a copy, so every C++ QMetaType behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMetaType that has a ritual and that Python can call
  so far, 30 names in all: 'type', 'typeName', 'sizeOf', 'typeFlags',
  'metaObjectForType', 'isRegistered', 'registerType', 'id', 'rawId',
  'alignOf', 'flags', 'metaObject', 'name', 'isDefaultConstructible',
  'isCopyConstructible', 'isMoveConstructible', 'isDestructible',
  'isEqualityComparable', 'isOrdered', 'hasRegisteredDataStreamOperators',
  'underlyingType', 'fromName', 'hasRegisteredDebugStreamOperator',
  'canConvert', 'canView', 'hasRegisteredConverterFunction',
  'hasRegisteredMutableViewFunction', 'unregisterConverterFunction',
  'unregisterMutableViewFunction', 'unregisterMetaType'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMetaType::QMetaType(const QtPrivate::QMetaTypeInterface *d)':
    names 'QtPrivate::QMetaTypeInterface', which has no cute class yet.
  - Qt's 'bool QMetaType::isValid(Qt::Disambiguated_t a0) const': names
    'Qt::Disambiguated_t', which has no cute class yet.
  - Qt's 'bool QMetaType::isRegistered(Qt::Disambiguated_t a0) const': names
    'Qt::Disambiguated_t', which has no cute class yet.
  - Qt's 'qsizetype QMetaType::sizeOf() const': another kind of method than
    most functions of its name, and one name is one kind of method.
  - Qt's 'bool QMetaType::hasRegisteredDebugStreamOperator(int typeId)':
    another kind of method than most functions of its name, and one name is
    one kind of method.
  - Qt's 'const QtPrivate::QMetaTypeInterface *QMetaType::iface()': gives
    'QtPrivate::QMetaTypeInterface', which has no cute class yet.
  - Qt's 'const QtPrivate::QMetaTypeInterface *QMetaType::iface() const':
    gives 'QtPrivate::QMetaTypeInterface', which has no cute class yet.
  - Qt's 'QMetaType::~QMetaType()': the destructor: Python removes its C++
    QMetaType by it, and has no other use for it.

  What has no ritual
  ------------------

  43 of the 83 functions Qt declares: 25 takes or gives a type that cannot be
  passed yet; 12 a template; 6 private.

  What to expect
  --------------

  - The C++ QMetaType is created at the first use, not by 'QMetaType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMetaType back gives a copy the ritual made for
    Python, in a new cute QMetaType.
  """

  #  The enums Qt writes inside QMetaType, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum):
    """The enum 'QMetaType::Type' of Qt, with the 92 names Qt gives in it."""

    Bool = Kee[int](1)
    Int = Kee[int](2)
    UInt = Kee[int](3)
    LongLong = Kee[int](4)
    ULongLong = Kee[int](5)
    Double = Kee[int](6)
    Long = Kee[int](32)
    Short = Kee[int](33)
    Char = Kee[int](34)
    Char16 = Kee[int](56)
    Char32 = Kee[int](57)
    ULong = Kee[int](35)
    UShort = Kee[int](36)
    UChar = Kee[int](37)
    Float = Kee[int](38)
    SChar = Kee[int](40)
    Nullptr = Kee[int](51)
    QCborSimpleType = Kee[int](52)
    Void = Kee[int](43)
    VoidStar = Kee[int](31)
    QChar = Kee[int](7)
    QString = Kee[int](10)
    QByteArray = Kee[int](12)
    QBitArray = Kee[int](13)
    QDate = Kee[int](14)
    QTime = Kee[int](15)
    QDateTime = Kee[int](16)
    QUrl = Kee[int](17)
    QLocale = Kee[int](18)
    QRect = Kee[int](19)
    QRectF = Kee[int](20)
    QSize = Kee[int](21)
    QSizeF = Kee[int](22)
    QLine = Kee[int](23)
    QLineF = Kee[int](24)
    QPoint = Kee[int](25)
    QPointF = Kee[int](26)
    QEasingCurve = Kee[int](29)
    QUuid = Kee[int](30)
    QVariant = Kee[int](41)
    QRegularExpression = Kee[int](44)
    QJsonValue = Kee[int](45)
    QJsonObject = Kee[int](46)
    QJsonArray = Kee[int](47)
    QJsonDocument = Kee[int](48)
    QCborValue = Kee[int](53)
    QCborArray = Kee[int](54)
    QCborMap = Kee[int](55)
    Float16 = Kee[int](63)
    QModelIndex = Kee[int](42)
    QPersistentModelIndex = Kee[int](50)
    QObjectStar = Kee[int](39)
    QVariantMap = Kee[int](8)
    QVariantList = Kee[int](9)
    QVariantHash = Kee[int](28)
    QVariantPair = Kee[int](58)
    QByteArrayList = Kee[int](49)
    QStringList = Kee[int](11)
    QFont = Kee[int](4096)
    QPixmap = Kee[int](4097)
    QBrush = Kee[int](4098)
    QColor = Kee[int](4099)
    QPalette = Kee[int](4100)
    QIcon = Kee[int](4101)
    QImage = Kee[int](4102)
    QPolygon = Kee[int](4103)
    QRegion = Kee[int](4104)
    QBitmap = Kee[int](4105)
    QCursor = Kee[int](4106)
    QKeySequence = Kee[int](4107)
    QPen = Kee[int](4108)
    QTextLength = Kee[int](4109)
    QTextFormat = Kee[int](4110)
    QTransform = Kee[int](4112)
    QMatrix4x4 = Kee[int](4113)
    QVector2D = Kee[int](4114)
    QVector3D = Kee[int](4115)
    QVector4D = Kee[int](4116)
    QQuaternion = Kee[int](4117)
    QPolygonF = Kee[int](4118)
    QColorSpace = Kee[int](4119)
    QSizePolicy = Kee[int](8192)
    FirstCoreType = Kee[int](1)
    LastCoreType = Kee[int](63)
    FirstGuiType = Kee[int](4096)
    LastGuiType = Kee[int](4119)
    FirstWidgetsType = Kee[int](8192)
    LastWidgetsType = Kee[int](8192)
    HighestInternalId = Kee[int](8192)
    QReal = Kee[int](6)
    UnknownType = Kee[int](0)
    User = Kee[int](65536)

  class TypeFlag(CuteFlags):
    """
    The flags enum 'QMetaType::TypeFlag' of Qt, with the 17 names Qt gives in
    it. Qt names the type of its combinations 'QMetaType::TypeFlags'.
    """

    NeedsConstruction = 0x1
    NeedsDestruction = 0x2
    RelocatableType = 0x4
    MovableType = 0x4
    PointerToQObject = 0x8
    IsEnumeration = 0x10
    SharedPointerToQObject = 0x20
    WeakPointerToQObject = 0x40
    TrackingPointerToQObject = 0x80
    IsUnsignedEnumeration = 0x100
    IsGadget = 0x200
    PointerToGadget = 0x400
    IsPointer = 0x800
    IsQmlList = 0x1000
    IsConst = 0x2000
    NeedsCopyConstruction = 0x4000
    NeedsMoveConstruction = 0x8000

  TypeFlags = TypeFlag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  def type(typeName: Optional[str]) -> int:
    """
    Calls Qt's 'int QMetaType::type(const char *typeName)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#type

    Parameters
    ----------

    typeName : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  int QMetaType::type(const char *typeName)
    return Rituals.call(
        'ritual_ZN9QMetaType4typeEPKc', CuteMixin._bytesOf(typeName),
    )

  @staticmethod
  @overload(int)
  def typeName(type: int) -> Optional[str]:
    """
    Calls Qt's 'const char *QMetaType::typeName(int type)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#typeName

    Parameters
    ----------

    type : int
      Passed on as it is.

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QMetaType::typeName(int type)
    chars = Rituals.call('ritual_ZN9QMetaType8typeNameEi', type)
    return None if chars is None else chars.decode()

  @staticmethod
  @overload(int)
  def sizeOf(type: int) -> int:
    """
    Calls Qt's 'int QMetaType::sizeOf(int type)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#sizeOf

    Parameters
    ----------

    type : int
      Passed on as it is.
    """
    #  int QMetaType::sizeOf(int type)
    return Rituals.call('ritual_ZN9QMetaType6sizeOfEi', type)

  @staticmethod
  @overload(int)
  def typeFlags(type: int) -> TypeFlags:
    """
    Calls Qt's 'TypeFlags QMetaType::typeFlags(int type)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#typeFlags

    Parameters
    ----------

    type : int
      Passed on as it is.

    Returns
    -------

    TypeFlags
      The value standing for the combination Qt gave back.
    """
    #  TypeFlags QMetaType::typeFlags(int type)
    return QMetaType.TypeFlags(Rituals.call(
        'ritual_ZN9QMetaType9typeFlagsEi', type,
    ))

  @staticmethod
  @overload(int)
  def metaObjectForType(type: int) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QMetaType::metaObjectForType(int type)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#metaObjectForType

    Parameters
    ----------

    type : int
      Passed on as it is.

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QMetaType::metaObjectForType(int type)
    address = Rituals.call('ritual_ZN9QMetaType17metaObjectForTypeEi', type)
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  @staticmethod
  @overload(int)
  def isRegistered(type: int) -> bool:
    """
    Calls Qt's 'bool QMetaType::isRegistered(int type)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#isRegistered

    Parameters
    ----------

    type : int
      Passed on as it is.
    """
    #  bool QMetaType::isRegistered(int type)
    return Rituals.call('ritual_ZN9QMetaType12isRegisteredEi', type)

  @staticmethod
  @overload(QByteArrayView)
  def fromName(name: QByteArrayView) -> QMetaType:
    """
    Calls Qt's 'QMetaType QMetaType::fromName(QByteArrayView name)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#fromName

    Parameters
    ----------

    name : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QMetaType::fromName(QByteArrayView name)
    address = Rituals.call(
        'ritual_ZN9QMetaType8fromNameE14QByteArrayView',
        CuteMixin._valueOf(name),
    )
    return QMetaType._cuteOwning(address)

  @staticmethod
  @overload(THIS, THIS)
  def canConvert(fromType: QMetaType, toType: QMetaType) -> bool:
    """
    Calls Qt's 'bool QMetaType::canConvert(QMetaType fromType, QMetaType
    toType)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#canConvert

    Parameters
    ----------

    fromType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    toType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  bool QMetaType::canConvert(QMetaType fromType, QMetaType toType)
    return Rituals.call(
        'ritual_ZN9QMetaType10canConvertES_S_',
        CuteMixin._valueOf(fromType), CuteMixin._valueOf(toType),
    )

  @staticmethod
  @overload(THIS, THIS)
  def canView(fromType: QMetaType, toType: QMetaType) -> bool:
    """
    Calls Qt's 'bool QMetaType::canView(QMetaType fromType, QMetaType
    toType)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#canView

    Parameters
    ----------

    fromType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    toType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  bool QMetaType::canView(QMetaType fromType, QMetaType toType)
    return Rituals.call(
        'ritual_ZN9QMetaType7canViewES_S_',
        CuteMixin._valueOf(fromType), CuteMixin._valueOf(toType),
    )

  @staticmethod
  @overload(THIS, THIS)
  def hasRegisteredConverterFunction(
      fromType: QMetaType,
      toType: QMetaType,
  ) -> bool:
    """
    Calls Qt's 'bool QMetaType::hasRegisteredConverterFunction(QMetaType
    fromType, QMetaType toType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetatype.html#hasRegisteredConverterFunction

    Parameters
    ----------

    fromType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    toType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  bool QMetaType::hasRegisteredConverterFunction(QMetaType fromType,
    #      QMetaType toType)
    return Rituals.call(
        'ritual_ZN9QMetaType30hasRegisteredConverterFunctionES_S_',
        CuteMixin._valueOf(fromType), CuteMixin._valueOf(toType),
    )

  @staticmethod
  @overload(THIS, THIS)
  def hasRegisteredMutableViewFunction(
      fromType: QMetaType,
      toType: QMetaType,
  ) -> bool:
    """
    Calls Qt's 'bool QMetaType::hasRegisteredMutableViewFunction(QMetaType
    fromType, QMetaType toType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetatype.html#hasRegisteredMutableViewFunction

    Parameters
    ----------

    fromType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    toType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  bool QMetaType::hasRegisteredMutableViewFunction(QMetaType fromType,
    #      QMetaType toType)
    return Rituals.call(
        'ritual_ZN9QMetaType32hasRegisteredMutableViewFunctionES_S_',
        CuteMixin._valueOf(fromType), CuteMixin._valueOf(toType),
    )

  @staticmethod
  @overload(THIS, THIS)
  def unregisterConverterFunction(from_: QMetaType, to: QMetaType) -> None:
    """
    Calls Qt's 'void QMetaType::unregisterConverterFunction(QMetaType from,
    QMetaType to)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetatype.html#unregisterConverterFunction

    Parameters
    ----------

    from_ : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    to : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  void QMetaType::unregisterConverterFunction(QMetaType from, QMetaType
    #      to)
    Rituals.call(
        'ritual_ZN9QMetaType27unregisterConverterFunctionES_S_',
        CuteMixin._valueOf(from_), CuteMixin._valueOf(to),
    )

  @staticmethod
  @overload(THIS, THIS)
  def unregisterMutableViewFunction(from_: QMetaType, to: QMetaType) -> None:
    """
    Calls Qt's 'void QMetaType::unregisterMutableViewFunction(QMetaType from,
    QMetaType to)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetatype.html#unregisterMutableViewFunction

    Parameters
    ----------

    from_ : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    to : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  void QMetaType::unregisterMutableViewFunction(QMetaType from,
    #      QMetaType to)
    Rituals.call(
        'ritual_ZN9QMetaType29unregisterMutableViewFunctionES_S_',
        CuteMixin._valueOf(from_), CuteMixin._valueOf(to),
    )

  @staticmethod
  @overload(THIS)
  def unregisterMetaType(type: QMetaType) -> None:
    """
    Calls Qt's 'void QMetaType::unregisterMetaType(QMetaType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#unregisterMetaType

    Parameters
    ----------

    type : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  void QMetaType::unregisterMetaType(QMetaType type)
    Rituals.call(
        'ritual_ZN9QMetaType18unregisterMetaTypeES_',
        CuteMixin._valueOf(type),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMetaType'

  #  Qt's '~QMetaType()'. Naming it makes this a value class: Python owns
  #  every C++ QMetaType behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QMetaTypeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(int)
  def id(self, a0: int = 0) -> int:
    """
    Calls Qt's 'int QMetaType::id(int a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#id

    Parameters
    ----------

    a0 : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  int QMetaType::id(int a0) const
    return self.uglySide.call('ritual_ZNK9QMetaType2idEi', a0)

  def rawId(self) -> int:
    """
    Calls Qt's 'int QMetaType::rawId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#rawId
    """
    #  int QMetaType::rawId() const
    return self.uglySide.call('ritual_ZNK9QMetaType5rawIdEv')

  def alignOf(self) -> int:
    """
    Calls Qt's 'qsizetype QMetaType::alignOf() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#alignOf
    """
    #  qsizetype QMetaType::alignOf() const
    return self.uglySide.call('ritual_ZNK9QMetaType7alignOfEv')

  def flags(self) -> TypeFlags:
    """
    Calls Qt's 'TypeFlags QMetaType::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#flags

    Returns
    -------

    TypeFlags
      The value standing for the combination Qt gave back.
    """
    #  TypeFlags QMetaType::flags() const
    return QMetaType.TypeFlags(self.uglySide.call(
        'ritual_ZNK9QMetaType5flagsEv',
    ))

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QMetaType::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QMetaType::metaObject() const
    address = self.uglySide.call('ritual_ZNK9QMetaType10metaObjectEv')
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def name(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QMetaType::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#name

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QMetaType::name() const
    chars = self.uglySide.call('ritual_ZNK9QMetaType4nameEv')
    return None if chars is None else chars.decode()

  def isDefaultConstructible(self) -> bool:
    """
    Calls Qt's 'bool QMetaType::isDefaultConstructible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetatype.html#isDefaultConstructible
    """
    #  bool QMetaType::isDefaultConstructible() const
    return self.uglySide.call(
        'ritual_ZNK9QMetaType22isDefaultConstructibleEv',
    )

  def isCopyConstructible(self) -> bool:
    """
    Calls Qt's 'bool QMetaType::isCopyConstructible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#isCopyConstructible
    """
    #  bool QMetaType::isCopyConstructible() const
    return self.uglySide.call('ritual_ZNK9QMetaType19isCopyConstructibleEv')

  def isMoveConstructible(self) -> bool:
    """
    Calls Qt's 'bool QMetaType::isMoveConstructible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#isMoveConstructible
    """
    #  bool QMetaType::isMoveConstructible() const
    return self.uglySide.call('ritual_ZNK9QMetaType19isMoveConstructibleEv')

  def isDestructible(self) -> bool:
    """
    Calls Qt's 'bool QMetaType::isDestructible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#isDestructible
    """
    #  bool QMetaType::isDestructible() const
    return self.uglySide.call('ritual_ZNK9QMetaType14isDestructibleEv')

  def isEqualityComparable(self) -> bool:
    """
    Calls Qt's 'bool QMetaType::isEqualityComparable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetatype.html#isEqualityComparable
    """
    #  bool QMetaType::isEqualityComparable() const
    return self.uglySide.call('ritual_ZNK9QMetaType20isEqualityComparableEv')

  def isOrdered(self) -> bool:
    """
    Calls Qt's 'bool QMetaType::isOrdered() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#isOrdered
    """
    #  bool QMetaType::isOrdered() const
    return self.uglySide.call('ritual_ZNK9QMetaType9isOrderedEv')

  def hasRegisteredDataStreamOperators(self) -> bool:
    """
    Calls Qt's 'bool QMetaType::hasRegisteredDataStreamOperators() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetatype.html#hasRegisteredDataStreamOperators
    """
    #  bool QMetaType::hasRegisteredDataStreamOperators() const
    return self.uglySide.call(
        'ritual_ZNK9QMetaType32hasRegisteredDataStreamOperatorsEv',
    )

  def underlyingType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QMetaType::underlyingType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#underlyingType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QMetaType::underlyingType() const
    address = self.uglySide.call('ritual_ZNK9QMetaType14underlyingTypeEv')
    return QMetaType._cuteOwning(address)

  def hasRegisteredDebugStreamOperator(self) -> bool:
    """
    Calls Qt's 'bool QMetaType::hasRegisteredDebugStreamOperator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetatype.html#hasRegisteredDebugStreamOperator
    """
    #  bool QMetaType::hasRegisteredDebugStreamOperator() const
    return self.uglySide.call(
        'ritual_ZNK9QMetaType32hasRegisteredDebugStreamOperatorEv',
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def __init__(self, type: int) -> None:
    """
    Notes what was given, for Qt's 'QMetaType::QMetaType(int type)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#QMetaType

    Parameters
    ----------

    type : int
      Passed on as it is.
    """
    #  QMetaType::QMetaType(int type)
    self._noteCreation(QMetaType, lambda: Rituals.call(
        'ritual_ZN9QMetaTypeC1Ei', type,
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QMetaType::QMetaType()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#QMetaType
    """
    #  QMetaType::QMetaType()
    self._noteCreation(QMetaType, lambda: Rituals.call(
        'ritual_ZN9QMetaTypeC1Ev',
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

  def registerType(self) -> None:
    """
    Calls Qt's 'void QMetaType::registerType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#registerType
    """
    #  void QMetaType::registerType() const
    self.uglySide.call('ritual_ZNK9QMetaType12registerTypeEv')
