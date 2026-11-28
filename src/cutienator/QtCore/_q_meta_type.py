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
from . import QList, Qt, QtPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QByteArrayView, QDebug, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArrayView = WAIT['QByteArrayView']
  QDebug = WAIT['QDebug']

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
  so far, 36 names in all: 'type', 'typeName', 'sizeOf', 'typeFlags',
  'metaObjectForType', 'isRegistered', 'isValid', 'registerType', 'id',
  'rawId', 'alignOf', 'flags', 'metaObject', 'name',
  'isDefaultConstructible', 'isCopyConstructible', 'isMoveConstructible',
  'isDestructible', 'isEqualityComparable', 'isOrdered',
  'hasRegisteredDataStreamOperators', 'underlyingType', 'fromName', '__eq__',
  '__ne__', '__rlshift__', 'hasRegisteredDebugStreamOperator', 'canConvert',
  'canView', 'hasRegisteredConverterFunction',
  'hasRegisteredMutableViewFunction', 'unregisterConverterFunction',
  'unregisterMutableViewFunction', 'unregisterMetaType', 'iface',
  'registerHelper'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QMetaType::registerNormalizedTypedef(const ::QByteArray
    &normalizedTypeName, QMetaType type)': takes a type Python has no way to
    hand over yet.
  - Qt's 'int QMetaType::type(const ::QByteArray &typeName)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void *QMetaType::create(int type, const void *copy)': names 'void',
    which has no cute class yet.
  - Qt's 'void QMetaType::destroy(int type, void *data)': names 'void', which
    has no cute class yet.
  - Qt's 'void *QMetaType::construct(int type, void *where, const void
    *copy)': names 'void', which has no cute class yet.
  - Qt's 'void QMetaType::destruct(int type, void *where)': names 'void',
    which has no cute class yet.
  - Qt's 'void *QMetaType::create(const void *copy) const': names 'void',
    which has no cute class yet.
  - Qt's 'void QMetaType::destroy(void *data) const': names 'void', which has
    no cute class yet.
  - Qt's 'void *QMetaType::construct(void *where, const void *copy) const':
    names 'void', which has no cute class yet.
  - Qt's 'void QMetaType::destruct(void *data) const': names 'void', which
    has no cute class yet.
  - Qt's 'QPartialOrdering QMetaType::compare(const void *lhs, const void
    *rhs) const': names 'void', which has no cute class yet.
  - Qt's 'bool QMetaType::equals(const void *lhs, const void *rhs) const':
    names 'void', which has no cute class yet.
  - Qt's 'bool QMetaType::save(QDataStream &stream, const void *data) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'bool QMetaType::load(QDataStream &stream, void *data) const': takes
    a type Python has no way to hand over yet.
  - Qt's 'bool QMetaType::save(QDataStream &stream, int type, const void
    *data)': takes a type Python has no way to hand over yet.
  - Qt's 'bool QMetaType::load(QDataStream &stream, int type, void *data)':
    takes a type Python has no way to hand over yet.
  - Qt's 'bool QMetaType::debugStream(QDebug &dbg, const void *rhs)': takes a
    type Python has no way to hand over yet.
  - Qt's 'bool QMetaType::debugStream(QDebug &dbg, const void *rhs, int
    typeId)': takes a type Python has no way to hand over yet.
  - Qt's 'bool QMetaType::convert(QMetaType fromType, const void *from,
    QMetaType toType, void *to)': names 'void', which has no cute class yet.
  - Qt's 'bool QMetaType::view(QMetaType fromType, void *from, QMetaType
    toType, void *to)': names 'void', which has no cute class yet.
  - Qt's 'bool QMetaType::convert(const void *from, int fromTypeId, void *to,
    int toTypeId)': names 'void', which has no cute class yet.
  - Qt's 'bool QMetaType::compare(const void *lhs, const void *rhs, int
    typeId, int *result)': names 'void', which has no cute class yet.
  - Qt's 'bool QMetaType::equals(const void *lhs, const void *rhs, int
    typeId, int *result)': names 'void', which has no cute class yet.
  - Qt's 'bool QMetaType::registerConverterFunction(const ConverterFunction
    &f, QMetaType from, QMetaType to)': takes a type Python has no way to
    hand over yet.
  - Qt's 'bool QMetaType::registerMutableViewFunction(const
    MutableViewFunction &f, QMetaType from, QMetaType to)': takes a type
    Python has no way to hand over yet.
  - Qt's 'const QtPrivate::QMetaTypeInterface *QMetaType::iface() const':
    takes in Python what 'const QtPrivate::QMetaTypeInterface
    *QMetaType::iface()' takes.
  - Qt's 'QMetaType::~QMetaType()': the destructor: Python removes its C++
    QMetaType by it, and has no other use for it.

  What has no ritual
  ------------------

  12 of the 86 functions Qt declares: 12 a template.

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
  - Each name of Qt's QMetaType that has no cute function yet, 'compare',
    'construct', 'convert', 'create', 'debugStream', 'destroy', 'destruct',
    'equals', 'fromType', 'load', 'registerConverter',
    'registerConverterFunction', 'registerConverterImpl',
    'registerMutableView', 'registerMutableViewFunction',
    'registerMutableViewImpl', 'registerNormalizedTypedef', 'save', 'view',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
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

  @overload()
  def sizeOf(self) -> int:
    """
    Calls Qt's 'qsizetype QMetaType::sizeOf() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#sizeOf
    """
    #  qsizetype QMetaType::sizeOf() const
    return self.uglySide.call('ritual_ZNK9QMetaType6sizeOfEv')

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

  @overload(WAIT['Qt.Disambiguated_t'])
  def isRegistered(self, a0: Qt.Disambiguated_t) -> bool:
    """
    Calls Qt's 'bool QMetaType::isRegistered(Qt::Disambiguated_t a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#isRegistered

    Parameters
    ----------

    a0 : Qt.Disambiguated_t
      Passed on as a value: Qt reads the C++ Qt::Disambiguated_t, which stays
      Python's own.
    """
    #  bool QMetaType::isRegistered(Qt::Disambiguated_t a0) const
    return self.uglySide.call(
        'ritual_ZNK9QMetaType12isRegisteredEN2Qt15Disambiguated_tE',
        self._valueOf(a0),
    )

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

  @staticmethod
  @overload(WAIT['QtPrivate.QMetaTypeInterface'])
  @overload(NoneType)
  def registerHelper(iface: Optional[QtPrivate.QMetaTypeInterface]) -> int:
    """
    Calls Qt's 'int QMetaType::registerHelper(const
    QtPrivate::QMetaTypeInterface *iface)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#registerHelper

    Parameters
    ----------

    iface : Optional[QtPrivate.QMetaTypeInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QMetaType::registerHelper(const QtPrivate::QMetaTypeInterface
    #      *iface)
    return Rituals.call(
        'ritual_ZN9QMetaType14registerHelperEPKN9QtPrivate18QMetaTypeInterf'
        'aceE',
        CuteMixin._addressOf(iface),
    )

  @overload()
  def registerHelper(self) -> int:
    """
    Calls Qt's 'int QMetaType::registerHelper() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#registerHelper
    """
    #  int QMetaType::registerHelper() const
    return self.uglySide.call('ritual_ZNK9QMetaType14registerHelperEv')

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

  @overload(WAIT['Qt.Disambiguated_t'])
  def isValid(self, a0: Qt.Disambiguated_t) -> bool:
    """
    Calls Qt's 'bool QMetaType::isValid(Qt::Disambiguated_t a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#isValid

    Parameters
    ----------

    a0 : Qt.Disambiguated_t
      Passed on as a value: Qt reads the C++ Qt::Disambiguated_t, which stays
      Python's own.
    """
    #  bool QMetaType::isValid(Qt::Disambiguated_t a0) const
    return self.uglySide.call(
        'ritual_ZNK9QMetaType7isValidEN2Qt15Disambiguated_tE',
        self._valueOf(a0),
    )

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

  @overload()
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

  @staticmethod
  @overload(WAIT['QtPrivate.QMetaTypeInterface'])
  @overload(NoneType)
  def isDefaultConstructible(
      a0: Optional[QtPrivate.QMetaTypeInterface],
  ) -> bool:
    """
    Calls Qt's 'bool QMetaType::isDefaultConstructible(const
    QtPrivate::QMetaTypeInterface *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetatype.html#isDefaultConstructible

    Parameters
    ----------

    a0 : Optional[QtPrivate.QMetaTypeInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QMetaType::isDefaultConstructible(const
    #      QtPrivate::QMetaTypeInterface *a0)
    return Rituals.call(
        'ritual_ZN9QMetaType22isDefaultConstructibleEPKN9QtPrivate18QMetaTy'
        'peInterfaceE',
        CuteMixin._addressOf(a0),
    )

  @overload()
  def isCopyConstructible(self) -> bool:
    """
    Calls Qt's 'bool QMetaType::isCopyConstructible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#isCopyConstructible
    """
    #  bool QMetaType::isCopyConstructible() const
    return self.uglySide.call('ritual_ZNK9QMetaType19isCopyConstructibleEv')

  @staticmethod
  @overload(WAIT['QtPrivate.QMetaTypeInterface'])
  @overload(NoneType)
  def isCopyConstructible(
      a0: Optional[QtPrivate.QMetaTypeInterface],
  ) -> bool:
    """
    Calls Qt's 'bool QMetaType::isCopyConstructible(const
    QtPrivate::QMetaTypeInterface *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#isCopyConstructible

    Parameters
    ----------

    a0 : Optional[QtPrivate.QMetaTypeInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QMetaType::isCopyConstructible(const
    #      QtPrivate::QMetaTypeInterface *a0)
    return Rituals.call(
        'ritual_ZN9QMetaType19isCopyConstructibleEPKN9QtPrivate18QMetaTypeI'
        'nterfaceE',
        CuteMixin._addressOf(a0),
    )

  @overload()
  def isMoveConstructible(self) -> bool:
    """
    Calls Qt's 'bool QMetaType::isMoveConstructible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#isMoveConstructible
    """
    #  bool QMetaType::isMoveConstructible() const
    return self.uglySide.call('ritual_ZNK9QMetaType19isMoveConstructibleEv')

  @staticmethod
  @overload(WAIT['QtPrivate.QMetaTypeInterface'])
  @overload(NoneType)
  def isMoveConstructible(
      a0: Optional[QtPrivate.QMetaTypeInterface],
  ) -> bool:
    """
    Calls Qt's 'bool QMetaType::isMoveConstructible(const
    QtPrivate::QMetaTypeInterface *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#isMoveConstructible

    Parameters
    ----------

    a0 : Optional[QtPrivate.QMetaTypeInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QMetaType::isMoveConstructible(const
    #      QtPrivate::QMetaTypeInterface *a0)
    return Rituals.call(
        'ritual_ZN9QMetaType19isMoveConstructibleEPKN9QtPrivate18QMetaTypeI'
        'nterfaceE',
        CuteMixin._addressOf(a0),
    )

  @overload()
  def isDestructible(self) -> bool:
    """
    Calls Qt's 'bool QMetaType::isDestructible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#isDestructible
    """
    #  bool QMetaType::isDestructible() const
    return self.uglySide.call('ritual_ZNK9QMetaType14isDestructibleEv')

  @staticmethod
  @overload(WAIT['QtPrivate.QMetaTypeInterface'])
  @overload(NoneType)
  def isDestructible(a0: Optional[QtPrivate.QMetaTypeInterface]) -> bool:
    """
    Calls Qt's 'bool QMetaType::isDestructible(const
    QtPrivate::QMetaTypeInterface *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#isDestructible

    Parameters
    ----------

    a0 : Optional[QtPrivate.QMetaTypeInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QMetaType::isDestructible(const QtPrivate::QMetaTypeInterface
    #      *a0)
    return Rituals.call(
        'ritual_ZN9QMetaType14isDestructibleEPKN9QtPrivate18QMetaTypeInterf'
        'aceE',
        CuteMixin._addressOf(a0),
    )

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

  @overload()
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

  @staticmethod
  @overload(int)
  def hasRegisteredDebugStreamOperator(typeId: int) -> bool:
    """
    Calls Qt's 'bool QMetaType::hasRegisteredDebugStreamOperator(int
    typeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetatype.html#hasRegisteredDebugStreamOperator

    Parameters
    ----------

    typeId : int
      Passed on as it is.
    """
    #  bool QMetaType::hasRegisteredDebugStreamOperator(int typeId)
    return Rituals.call(
        'ritual_ZN9QMetaType32hasRegisteredDebugStreamOperatorEi', typeId,
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

  @overload(THIS)
  def __eq__(self, rhs: QMetaType) -> bool:
    """
    Calls Qt's 'bool operator==(const QMetaType &lhs, const QMetaType &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#operator==

    Parameters
    ----------

    rhs : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  bool operator==(const QMetaType &lhs, const QMetaType &rhs)
    return Rituals.call(
        'ritual_ZeqRK9QMetaTypeS1_',
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
  def __ne__(self, rhs: QMetaType) -> bool:
    """
    Calls Qt's 'bool operator!=(const QMetaType &lhs, const QMetaType &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#operator!=

    Parameters
    ----------

    rhs : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  bool operator!=(const QMetaType &lhs, const QMetaType &rhs)
    return Rituals.call(
        'ritual_ZneRK9QMetaTypeS1_',
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

  @overload(QDebug)
  def __rlshift__(self, d: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug d, QMetaType m)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#operator<<

    Parameters
    ----------

    d : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug d, QMetaType m)
    address = Rituals.call(
        'ritual_Zls6QDebug9QMetaType',
        CuteMixin._valueOf(d), CuteMixin._valueOf(self),
    )
    from . import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

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

  @overload(WAIT['QtPrivate.QMetaTypeInterface'])
  @overload(NoneType)
  def __init__(self, d: Optional[QtPrivate.QMetaTypeInterface]) -> None:
    """
    Notes what was given, for Qt's 'QMetaType::QMetaType(const
    QtPrivate::QMetaTypeInterface *d)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#QMetaType

    Parameters
    ----------

    d : Optional[QtPrivate.QMetaTypeInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QMetaType::QMetaType(const QtPrivate::QMetaTypeInterface *d)
    self._noteCreation(QMetaType, lambda: Rituals.call(
        'ritual_ZN9QMetaTypeC1EPKN9QtPrivate18QMetaTypeInterfaceE',
        self._addressOf(d),
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

  def iface(self) -> Optional[QtPrivate.QMetaTypeInterface]:
    """
    Calls Qt's 'const QtPrivate::QMetaTypeInterface *QMetaType::iface()'.

    Qt's own words: https://doc.qt.io/qt-6/qmetatype.html#iface

    Returns
    -------

    Optional[QtPrivate.QMetaTypeInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QtPrivate::QMetaTypeInterface *QMetaType::iface()
    address = self.uglySide.call('ritual_ZN9QMetaType5ifaceEv')
    return QtPrivate.QMetaTypeInterface._cuteAt(address)

  @staticmethod
  def compare(*__, **_) -> Never:
    """
    - Qt's 'QPartialOrdering QMetaType::compare(const void *lhs, const void
      *rhs) const': names 'void', which has no cute class yet.
    - Qt's 'bool QMetaType::compare(const void *lhs, const void *rhs, int
      typeId, int *result)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaType.compare' has no cute function yet. Qt's "
        "'QPartialOrdering QMetaType::compare(const void *lhs, const void "
        "*rhs) const': names 'void', which has no cute class yet. Qt's "
        "'bool QMetaType::compare(const void *lhs, const void *rhs, int "
        "typeId, int *result)': names 'void', which has no cute class yet.")

  @staticmethod
  def construct(*__, **_) -> Never:
    """
    - Qt's 'void *QMetaType::construct(int type, void *where, const void
      *copy)': names 'void', which has no cute class yet.
    - Qt's 'void *QMetaType::construct(void *where, const void *copy) const':
      names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaType.construct' has no cute function yet. Qt's 'void "
        "*QMetaType::construct(int type, void *where, const void *copy)': "
        "names 'void', which has no cute class yet. Qt's 'void "
        "*QMetaType::construct(void *where, const void *copy) const': names "
        "'void', which has no cute class yet.")

  @staticmethod
  def convert(*__, **_) -> Never:
    """
    - Qt's 'bool QMetaType::convert(QMetaType fromType, const void *from,
      QMetaType toType, void *to)': names 'void', which has no cute class
      yet.
    - Qt's 'bool QMetaType::convert(const void *from, int fromTypeId, void
      *to, int toTypeId)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaType.convert' has no cute function yet. Qt's 'bool "
        "QMetaType::convert(QMetaType fromType, const void *from, QMetaType "
        "toType, void *to)': names 'void', which has no cute class yet. "
        "Qt's 'bool QMetaType::convert(const void *from, int fromTypeId, "
        "void *to, int toTypeId)': names 'void', which has no cute class "
        "yet.")

  @staticmethod
  def create(*__, **_) -> Never:
    """
    - Qt's 'void *QMetaType::create(int type, const void *copy)': names
      'void', which has no cute class yet.
    - Qt's 'void *QMetaType::create(const void *copy) const': names 'void',
      which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaType.create' has no cute function yet. Qt's 'void "
        "*QMetaType::create(int type, const void *copy)': names 'void', "
        "which has no cute class yet. Qt's 'void *QMetaType::create(const "
        "void *copy) const': names 'void', which has no cute class yet.")

  @staticmethod
  def debugStream(*__, **_) -> Never:
    """
    - Qt's 'bool QMetaType::debugStream(QDebug &dbg, const void *rhs)': takes
      a type Python has no way to hand over yet.
    - Qt's 'bool QMetaType::debugStream(QDebug &dbg, const void *rhs, int
      typeId)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMetaType.debugStream' has no cute function yet. Qt's 'bool "
        "QMetaType::debugStream(QDebug &dbg, const void *rhs)': takes a "
        "type Python has no way to hand over yet. Qt's 'bool "
        "QMetaType::debugStream(QDebug &dbg, const void *rhs, int typeId)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def destroy(*__, **_) -> Never:
    """
    - Qt's 'void QMetaType::destroy(int type, void *data)': names 'void',
      which has no cute class yet.
    - Qt's 'void QMetaType::destroy(void *data) const': names 'void', which
      has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaType.destroy' has no cute function yet. Qt's 'void "
        "QMetaType::destroy(int type, void *data)': names 'void', which has "
        "no cute class yet. Qt's 'void QMetaType::destroy(void *data) "
        "const': names 'void', which has no cute class yet.")

  @staticmethod
  def destruct(*__, **_) -> Never:
    """
    - Qt's 'void QMetaType::destruct(int type, void *where)': names 'void',
      which has no cute class yet.
    - Qt's 'void QMetaType::destruct(void *data) const': names 'void', which
      has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaType.destruct' has no cute function yet. Qt's 'void "
        "QMetaType::destruct(int type, void *where)': names 'void', which "
        "has no cute class yet. Qt's 'void QMetaType::destruct(void *data) "
        "const': names 'void', which has no cute class yet.")

  @staticmethod
  def equals(*__, **_) -> Never:
    """
    - Qt's 'bool QMetaType::equals(const void *lhs, const void *rhs) const':
      names 'void', which has no cute class yet.
    - Qt's 'bool QMetaType::equals(const void *lhs, const void *rhs, int
      typeId, int *result)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaType.equals' has no cute function yet. Qt's 'bool "
        "QMetaType::equals(const void *lhs, const void *rhs) const': names "
        "'void', which has no cute class yet. Qt's 'bool "
        "QMetaType::equals(const void *lhs, const void *rhs, int typeId, "
        "int *result)': names 'void', which has no cute class yet.")

  @staticmethod
  def fromType(*__, **_) -> Never:
    """
    Qt's 'QMetaType::fromType': a template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QMetaType.fromType' has no cute function yet. Qt's "
        "'QMetaType::fromType': a template: a pattern and no single "
        "function.")

  @staticmethod
  def load(*__, **_) -> Never:
    """
    - Qt's 'bool QMetaType::load(QDataStream &stream, void *data) const':
      takes a type Python has no way to hand over yet.
    - Qt's 'bool QMetaType::load(QDataStream &stream, int type, void *data)':
      takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMetaType.load' has no cute function yet. Qt's 'bool "
        "QMetaType::load(QDataStream &stream, void *data) const': takes a "
        "type Python has no way to hand over yet. Qt's 'bool "
        "QMetaType::load(QDataStream &stream, int type, void *data)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def registerConverter(*__, **_) -> Never:
    """
    Qt's 'QMetaType::registerConverter': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QMetaType.registerConverter' has no cute function yet. Qt's "
        "'QMetaType::registerConverter': a template: a pattern and no "
        "single function.")

  @staticmethod
  def registerConverterFunction(*__, **_) -> Never:
    """
    Qt's 'bool QMetaType::registerConverterFunction(const ConverterFunction
    &f, QMetaType from, QMetaType to)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QMetaType.registerConverterFunction' has no cute function yet. "
        "Qt's 'bool QMetaType::registerConverterFunction(const "
        "ConverterFunction &f, QMetaType from, QMetaType to)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def registerConverterImpl(*__, **_) -> Never:
    """
    Qt's 'QMetaType::registerConverterImpl': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QMetaType.registerConverterImpl' has no cute function yet. Qt's "
        "'QMetaType::registerConverterImpl': a template: a pattern and no "
        "single function.")

  @staticmethod
  def registerMutableView(*__, **_) -> Never:
    """
    Qt's 'QMetaType::registerMutableView': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QMetaType.registerMutableView' has no cute function yet. Qt's "
        "'QMetaType::registerMutableView': a template: a pattern and no "
        "single function.")

  @staticmethod
  def registerMutableViewFunction(*__, **_) -> Never:
    """
    Qt's 'bool QMetaType::registerMutableViewFunction(const
    MutableViewFunction &f, QMetaType from, QMetaType to)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMetaType.registerMutableViewFunction' has no cute function yet. "
        "Qt's 'bool QMetaType::registerMutableViewFunction(const "
        "MutableViewFunction &f, QMetaType from, QMetaType to)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def registerMutableViewImpl(*__, **_) -> Never:
    """
    Qt's 'QMetaType::registerMutableViewImpl': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QMetaType.registerMutableViewImpl' has no cute function yet. Qt's "
        "'QMetaType::registerMutableViewImpl': a template: a pattern and no "
        "single function.")

  @staticmethod
  def registerNormalizedTypedef(*__, **_) -> Never:
    """
    Qt's 'void QMetaType::registerNormalizedTypedef(const ::QByteArray
    &normalizedTypeName, QMetaType type)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QMetaType.registerNormalizedTypedef' has no cute function yet. "
        "Qt's 'void QMetaType::registerNormalizedTypedef(const ::QByteArray "
        "&normalizedTypeName, QMetaType type)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def save(*__, **_) -> Never:
    """
    - Qt's 'bool QMetaType::save(QDataStream &stream, const void *data)
      const': takes a type Python has no way to hand over yet.
    - Qt's 'bool QMetaType::save(QDataStream &stream, int type, const void
      *data)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMetaType.save' has no cute function yet. Qt's 'bool "
        "QMetaType::save(QDataStream &stream, const void *data) const': "
        "takes a type Python has no way to hand over yet. Qt's 'bool "
        "QMetaType::save(QDataStream &stream, int type, const void *data)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def view(*__, **_) -> Never:
    """
    Qt's 'bool QMetaType::view(QMetaType fromType, void *from, QMetaType
    toType, void *to)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaType.view' has no cute function yet. Qt's 'bool "
        "QMetaType::view(QMetaType fromType, void *from, QMetaType toType, "
        "void *to)': names 'void', which has no cute class yet.")


#  Qt's 'QList<QMetaType>': the list of QMetaType, which 'QList[QMetaType]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QMetaType.
QList.createKind(
    QMetaType, 'value',
    make='ritual_list_make_QMetaType',
    add='ritual_list_add_QMetaType',
    size='ritual_list_size_QMetaType',
    at='ritual_list_at_QMetaType',
    drop='ritual_list_drop_QMetaType',
)
