"""
QGeoMapType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeomaptype_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QGeoMapType to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QMap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray, QVariant
  from . import QGeoCameraCapabilities
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QGeoCameraCapabilities = WAIT['QGeoCameraCapabilities']
  QVariant = WAIT['QVariant']


class QGeoMapType(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGeoMapType: a plain Python object standing in front
  of one C++ QGeoMapType.

  C++ hands a QGeoMapType around as a copy, so every C++ QGeoMapType behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGeoMapType that has a ritual and that Python can
  call so far, 12 names in all: '__eq__', '__ne__', 'style', 'name',
  'description', 'mobile', 'night', 'mapId', 'pluginName',
  'cameraCapabilities', 'metadata', 'isEqual'. It can be made from Python, in
  3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoMapType::QGeoMapType(QGeoMapType &&other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QGeoMapType::~QGeoMapType()': the destructor: Python removes its
    C++ QGeoMapType by it, and has no other use for it.
  - Qt's 'QGeoMapType &QGeoMapType::operator=(const QGeoMapType &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QGeoMapType &QGeoMapType::operator=(QGeoMapType &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QGeoMapType::swap(QGeoMapType &other)': takes a type Python
    has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 23 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QGeoMapType is created at the first use, not by
    'QGeoMapType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoMapType back gives a copy the ritual made for
    Python, in a new cute QGeoMapType.
  - Each name of Qt's QGeoMapType that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QGeoMapType, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class MapStyle(CuteNum):
    """
    The enum 'QGeoMapType::MapStyle' of Qt, with the 12 names Qt gives in it.
    """

    NoMap = Kee[int](0)
    StreetMap = Kee[int](1)
    SatelliteMapDay = Kee[int](2)
    SatelliteMapNight = Kee[int](3)
    TerrainMap = Kee[int](4)
    HybridMap = Kee[int](5)
    TransitMap = Kee[int](6)
    GrayStreetMap = Kee[int](7)
    PedestrianMap = Kee[int](8)
    CarNavigationMap = Kee[int](9)
    CycleMap = Kee[int](10)
    CustomMap = Kee[int](100)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoMapType'

  #  Qt's '~QGeoMapType()'. Naming it makes this a value class: Python owns
  #  every C++ QGeoMapType behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QGeoMapTypeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def style(self) -> MapStyle:
    """
    Calls Qt's 'MapStyle QGeoMapType::style() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaptype.html#style

    Returns
    -------

    MapStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'MapStyle(number)' gives.
    """
    #  MapStyle QGeoMapType::style() const
    return QGeoMapType.MapStyle(self.uglySide.call(
        'ritual_ZNK11QGeoMapType5styleEv',
    ))

  def name(self) -> str:
    """
    Calls Qt's 'QString QGeoMapType::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaptype.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoMapType::name() const
    return self.uglySide.call('ritual_ZNK11QGeoMapType4nameEv')

  def description(self) -> str:
    """
    Calls Qt's 'QString QGeoMapType::description() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaptype.html#description

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoMapType::description() const
    return self.uglySide.call('ritual_ZNK11QGeoMapType11descriptionEv')

  def mobile(self) -> bool:
    """
    Calls Qt's 'bool QGeoMapType::mobile() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaptype.html#mobile
    """
    #  bool QGeoMapType::mobile() const
    return self.uglySide.call('ritual_ZNK11QGeoMapType6mobileEv')

  def night(self) -> bool:
    """
    Calls Qt's 'bool QGeoMapType::night() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaptype.html#night
    """
    #  bool QGeoMapType::night() const
    return self.uglySide.call('ritual_ZNK11QGeoMapType5nightEv')

  def mapId(self) -> int:
    """
    Calls Qt's 'int QGeoMapType::mapId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaptype.html#mapId
    """
    #  int QGeoMapType::mapId() const
    return self.uglySide.call('ritual_ZNK11QGeoMapType5mapIdEv')

  def pluginName(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QGeoMapType::pluginName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaptype.html#pluginName

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QGeoMapType::pluginName() const
    address = self.uglySide.call('ritual_ZNK11QGeoMapType10pluginNameEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def cameraCapabilities(self) -> QGeoCameraCapabilities:
    """
    Calls Qt's 'QGeoCameraCapabilities QGeoMapType::cameraCapabilities()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomaptype.html#cameraCapabilities

    Returns
    -------

    QGeoCameraCapabilities
      A new cute QGeoCameraCapabilities around the copy Qt gave back. Python
      owns it.
    """
    #  QGeoCameraCapabilities QGeoMapType::cameraCapabilities() const
    address = self.uglySide.call(
        'ritual_ZNK11QGeoMapType18cameraCapabilitiesEv',
    )
    from . import QGeoCameraCapabilities
    return QGeoCameraCapabilities._cuteOwning(address)

  def metadata(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap QGeoMapType::metadata() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaptype.html#metadata

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap QGeoMapType::metadata() const
    address = self.uglySide.call('ritual_ZNK11QGeoMapType8metadataEv')
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  @overload(THIS)
  def isEqual(self, other: QGeoMapType) -> bool:
    """
    Calls Qt's 'bool QGeoMapType::isEqual(const QGeoMapType &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaptype.html#isEqual

    Parameters
    ----------

    other : QGeoMapType
      Passed on as a value: Qt reads the C++ QGeoMapType, which stays
      Python's own.
    """
    #  bool QGeoMapType::isEqual(const QGeoMapType &other) const
    return self.uglySide.call(
        'ritual_ZNK11QGeoMapType7isEqualERKS_', self._valueOf(other),
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
  def __eq__(self, rhs: QGeoMapType) -> bool:
    """
    Calls Qt's 'bool operator==(const QGeoMapType &lhs, const QGeoMapType
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaptype.html#operator==

    Parameters
    ----------

    rhs : QGeoMapType
      Passed on as a value: Qt reads the C++ QGeoMapType, which stays
      Python's own.
    """
    #  bool operator==(const QGeoMapType &lhs, const QGeoMapType &rhs)
    return Rituals.call(
        'ritual_ZeqRK11QGeoMapTypeS1_',
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
  def __ne__(self, rhs: QGeoMapType) -> bool:
    """
    Calls Qt's 'bool operator!=(const QGeoMapType &lhs, const QGeoMapType
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaptype.html#operator!=

    Parameters
    ----------

    rhs : QGeoMapType
      Passed on as a value: Qt reads the C++ QGeoMapType, which stays
      Python's own.
    """
    #  bool operator!=(const QGeoMapType &lhs, const QGeoMapType &rhs)
    return Rituals.call(
        'ritual_ZneRK11QGeoMapTypeS1_',
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
    Notes what was given, for Qt's 'QGeoMapType::QGeoMapType()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaptype.html#QGeoMapType
    """
    #  QGeoMapType::QGeoMapType()
    self._noteCreation(QGeoMapType, lambda: Rituals.call(
        'ritual_ZN11QGeoMapTypeC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QGeoMapType) -> None:
    """
    Notes what was given, for Qt's 'QGeoMapType::QGeoMapType(const
    QGeoMapType &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaptype.html#QGeoMapType

    Parameters
    ----------

    other : QGeoMapType
      Passed on as a value: Qt reads the C++ QGeoMapType, which stays
      Python's own.
    """
    #  QGeoMapType::QGeoMapType(const QGeoMapType &other)
    self._noteCreation(QGeoMapType, lambda: Rituals.call(
        'ritual_ZN11QGeoMapTypeC1ERKS_', self._valueOf(other),
    ))

  @overload(
      MapStyle, str, str, bool, bool, int, QByteArray,
      QGeoCameraCapabilities, QMap[str, QVariant],
  )
  def __init__(
      self,
      style: MapStyle,
      name: str,
      description: str,
      mobile: bool,
      night: bool,
      mapId: int,
      pluginName: QByteArray,
      cameraCapabilities: QGeoCameraCapabilities,
      metadata: QMap[str, QVariant],
  ) -> None:
    """
    Notes what was given, for Qt's 'QGeoMapType::QGeoMapType(MapStyle style,
    const QString &name, const QString &description, bool mobile, bool night,
    int mapId, const QByteArray &pluginName, const QGeoCameraCapabilities
    &cameraCapabilities, const QVariantMap &metadata)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaptype.html#QGeoMapType

    Parameters
    ----------

    style : MapStyle
      Passed on as its number.

    name : str
      Passed on as it is: a QString is made of it for the call.

    description : str
      Passed on as it is: a QString is made of it for the call.

    mobile : bool
      Passed on as it is.

    night : bool
      Passed on as it is.

    mapId : int
      Passed on as it is.

    pluginName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    cameraCapabilities : QGeoCameraCapabilities
      Passed on as a value: Qt reads the C++ QGeoCameraCapabilities, which
      stays Python's own.

    metadata : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  QGeoMapType::QGeoMapType(MapStyle style, const QString &name, const
    #      QString &description, bool mobile, bool night, int mapId, const
    #      QByteArray &pluginName, const QGeoCameraCapabilities
    #      &cameraCapabilities, const QVariantMap &metadata)
    self._noteCreation(QGeoMapType, lambda: Rituals.call(
        'ritual_ZN11QGeoMapTypeC1ENS_8MapStyleERK7QStringS3_bbiRK10QByteArr'
        'ayRK22QGeoCameraCapabilitiesRK4QMapIS1_8QVariantE',
        style.value, name, description, mobile, night, mapId,
        self._valueOf(pluginName), self._valueOf(cameraCapabilities),
        self._valueOf(metadata),
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

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QGeoMapType::swap(QGeoMapType &other)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoMapType.swap' has no cute function yet. Qt's 'void "
        "QGeoMapType::swap(QGeoMapType &other)': takes a type Python has no "
        "way to hand over yet.")


#  Qt's 'QList<QGeoMapType>': the list of QGeoMapType, which
#  'QList[QGeoMapType]' gives. It is made here, so that there is one as soon
#  as there can be a QGeoMapType.
QList.createKind(
    QGeoMapType, 'value',
    make='ritual_list_make_QGeoMapType',
    add='ritual_list_add_QGeoMapType',
    size='ritual_list_size_QGeoMapType',
    at='ritual_list_at_QGeoMapType',
    drop='ritual_list_drop_QGeoMapType',
)
