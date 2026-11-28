"""
QLocationUtils binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/6.12.0/QtPositioning/private/qlocationutils_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QLocationUtils to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QGeoSatelliteInfo

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QByteArrayView, QTime
  from . import QGeoCoordinate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QByteArrayView = WAIT['QByteArrayView']
  QGeoCoordinate = WAIT['QGeoCoordinate']
  QTime = WAIT['QTime']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLocationUtils(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLocationUtils: a plain Python object standing in
  front of one C++ QLocationUtils.

  C++ hands a QLocationUtils around as a copy, so every C++ QLocationUtils
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLocationUtils that has a ritual and that Python can
  call so far, 24 names in all: 'isValidLat', 'isValidLong', 'clipLat',
  'wrapLong', 'azimuthToCardinalDirection4', 'azimuthToCardinalDirection8',
  'azimuthToCardinalDirection16', 'wrapLongExt', 'mirrorAzimuthX',
  'mirrorAzimuthY', 'radians', 'degrees', 'earthMeanRadius',
  'earthMeanCircumference', 'mercatorMaxLatitude', 'antipodalPoint',
  'mapLeftLongitude', 'mapRightLongitude', 'metersPerPixel',
  'getNmeaSentenceType', 'getSatelliteSystem',
  'getSatelliteSystemBySatelliteId', 'hasValidNmeaChecksum', 'getNmeaTime'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QLocationUtils::split_double(double input, float *hipart,
    float *lopart)': takes a number to change where it is.
  - Qt's 'bool QLocationUtils::getPosInfoFromNmea(QByteArrayView bv,
    QGeoPositionInfo *info, double uere, bool *hasFix)': takes a number to
    change where it is.
  - Qt's 'QNmeaSatelliteInfoSource::SatelliteInfoParseStatus
    QLocationUtils::getSatInfoFromNmea(QByteArrayView bv,
    QList<QGeoSatelliteInfo> &infos, QGeoSatelliteInfo::SatelliteSystem
    &system)': takes a type Python has no way to hand over yet.
  - Qt's 'QGeoSatelliteInfo::SatelliteSystem
    QLocationUtils::getSatInUseFromNmea(QByteArrayView bv, QList<int>
    &pnrsInUse)': takes a type Python has no way to hand over yet.
  - Qt's 'bool QLocationUtils::getNmeaLatLong(const QByteArray &latString,
    char latDirection, const QByteArray &lngString, char lngDirection, double
    *lat, double *lon)': takes a single letter as C has it.
  - Qt's 'QLocationUtils::~QLocationUtils()': the destructor: Python removes
    its C++ QLocationUtils by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QLocationUtils is created at the first use, not by
    'QLocationUtils(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLocationUtils back gives a copy the ritual made for
    Python, in a new cute QLocationUtils.
  - Each name of Qt's QLocationUtils that has no cute function yet,
    'getNmeaLatLong', 'getPosInfoFromNmea', 'getSatInUseFromNmea',
    'getSatInfoFromNmea', 'split_double', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QLocationUtils, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class CardinalDirection(CuteNum):
    """
    The enum 'QLocationUtils::CardinalDirection' of Qt, with the 16 names Qt
    gives in it.
    """

    CardinalN = Kee[int](0)
    CardinalE = Kee[int](1)
    CardinalS = Kee[int](2)
    CardinalW = Kee[int](3)
    CardinalNE = Kee[int](4)
    CardinalSE = Kee[int](5)
    CardinalSW = Kee[int](6)
    CardinalNW = Kee[int](7)
    CardinalNNE = Kee[int](8)
    CardinalENE = Kee[int](9)
    CardinalESE = Kee[int](10)
    CardinalSSE = Kee[int](11)
    CardinalSSW = Kee[int](12)
    CardinalWSW = Kee[int](13)
    CardinalWNW = Kee[int](14)
    CardinalNNW = Kee[int](15)

  class NmeaSentence(CuteNum):
    """
    The enum 'QLocationUtils::NmeaSentence' of Qt, with the 8 names Qt gives
    in it.
    """

    NmeaSentenceInvalid = Kee[int](0)
    NmeaSentenceGGA = Kee[int](1)
    NmeaSentenceGSA = Kee[int](2)
    NmeaSentenceGLL = Kee[int](3)
    NmeaSentenceRMC = Kee[int](4)
    NmeaSentenceVTG = Kee[int](5)
    NmeaSentenceZDA = Kee[int](6)
    NmeaSentenceGSV = Kee[int](7)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(float)
  def isValidLat(lat: float) -> bool:
    """
    Calls Qt's 'bool QLocationUtils::isValidLat(double lat)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocationutils.html#isValidLat

    Parameters
    ----------

    lat : float
      Passed on as it is.
    """
    #  bool QLocationUtils::isValidLat(double lat)
    return Rituals.call('ritual_ZN14QLocationUtils10isValidLatEd', lat)

  @staticmethod
  @overload(float)
  def isValidLong(lng: float) -> bool:
    """
    Calls Qt's 'bool QLocationUtils::isValidLong(double lng)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocationutils.html#isValidLong

    Parameters
    ----------

    lng : float
      Passed on as it is.
    """
    #  bool QLocationUtils::isValidLong(double lng)
    return Rituals.call('ritual_ZN14QLocationUtils11isValidLongEd', lng)

  @staticmethod
  @overload(float)
  @overload(float, float)
  def clipLat(lat: float, clipValue: float = 90.0) -> float:
    """
    Calls Qt's 'double QLocationUtils::clipLat(double lat, double
    clipValue)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocationutils.html#clipLat

    Parameters
    ----------

    lat : float
      Passed on as it is.

    clipValue : float
      Passed on as it is. May be left out, as in Qt: it is then 90.0.
    """
    #  double QLocationUtils::clipLat(double lat, double clipValue)
    return Rituals.call(
        'ritual_ZN14QLocationUtils7clipLatEdd', lat, clipValue,
    )

  @staticmethod
  @overload(float)
  def wrapLong(lng: float) -> float:
    """
    Calls Qt's 'double QLocationUtils::wrapLong(double lng)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocationutils.html#wrapLong

    Parameters
    ----------

    lng : float
      Passed on as it is.
    """
    #  double QLocationUtils::wrapLong(double lng)
    return Rituals.call('ritual_ZN14QLocationUtils8wrapLongEd', lng)

  @staticmethod
  @overload(float)
  def azimuthToCardinalDirection4(azimuth: float) -> CardinalDirection:
    """
    Calls Qt's 'CardinalDirection
    QLocationUtils::azimuthToCardinalDirection4(double azimuth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocationutils.html#azimuthToCardinalDirection4

    Parameters
    ----------

    azimuth : float
      Passed on as it is.

    Returns
    -------

    CardinalDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'CardinalDirection(number)' gives.
    """
    #  CardinalDirection QLocationUtils::azimuthToCardinalDirection4(double
    #      azimuth)
    return QLocationUtils.CardinalDirection(Rituals.call(
        'ritual_ZN14QLocationUtils27azimuthToCardinalDirection4Ed', azimuth,
    ))

  @staticmethod
  @overload(float)
  def azimuthToCardinalDirection8(azimuth: float) -> CardinalDirection:
    """
    Calls Qt's 'CardinalDirection
    QLocationUtils::azimuthToCardinalDirection8(double azimuth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocationutils.html#azimuthToCardinalDirection8

    Parameters
    ----------

    azimuth : float
      Passed on as it is.

    Returns
    -------

    CardinalDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'CardinalDirection(number)' gives.
    """
    #  CardinalDirection QLocationUtils::azimuthToCardinalDirection8(double
    #      azimuth)
    return QLocationUtils.CardinalDirection(Rituals.call(
        'ritual_ZN14QLocationUtils27azimuthToCardinalDirection8Ed', azimuth,
    ))

  @staticmethod
  @overload(float)
  def azimuthToCardinalDirection16(azimuth: float) -> CardinalDirection:
    """
    Calls Qt's 'CardinalDirection
    QLocationUtils::azimuthToCardinalDirection16(double azimuth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocationutils.html#azimuthToCardinalDirection16

    Parameters
    ----------

    azimuth : float
      Passed on as it is.

    Returns
    -------

    CardinalDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'CardinalDirection(number)' gives.
    """
    #  CardinalDirection QLocationUtils::azimuthToCardinalDirection16(double
    #      azimuth)
    return QLocationUtils.CardinalDirection(Rituals.call(
        'ritual_ZN14QLocationUtils28azimuthToCardinalDirection16Ed', azimuth,
    ))

  @staticmethod
  @overload(float)
  def wrapLongExt(lng: float) -> float:
    """
    Calls Qt's 'double QLocationUtils::wrapLongExt(double lng)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocationutils.html#wrapLongExt

    Parameters
    ----------

    lng : float
      Passed on as it is.
    """
    #  double QLocationUtils::wrapLongExt(double lng)
    return Rituals.call('ritual_ZN14QLocationUtils11wrapLongExtEd', lng)

  @staticmethod
  @overload(float)
  def mirrorAzimuthX(azimuth: float) -> float:
    """
    Calls Qt's 'double QLocationUtils::mirrorAzimuthX(double azimuth)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocationutils.html#mirrorAzimuthX

    Parameters
    ----------

    azimuth : float
      Passed on as it is.
    """
    #  double QLocationUtils::mirrorAzimuthX(double azimuth)
    return Rituals.call(
        'ritual_ZN14QLocationUtils14mirrorAzimuthXEd', azimuth,
    )

  @staticmethod
  @overload(float)
  def mirrorAzimuthY(azimuth: float) -> float:
    """
    Calls Qt's 'double QLocationUtils::mirrorAzimuthY(double azimuth)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocationutils.html#mirrorAzimuthY

    Parameters
    ----------

    azimuth : float
      Passed on as it is.
    """
    #  double QLocationUtils::mirrorAzimuthY(double azimuth)
    return Rituals.call(
        'ritual_ZN14QLocationUtils14mirrorAzimuthYEd', azimuth,
    )

  @staticmethod
  @overload(float)
  def radians(degrees: float) -> float:
    """
    Calls Qt's 'double QLocationUtils::radians(double degrees)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocationutils.html#radians

    Parameters
    ----------

    degrees : float
      Passed on as it is.
    """
    #  double QLocationUtils::radians(double degrees)
    return Rituals.call('ritual_ZN14QLocationUtils7radiansEd', degrees)

  @staticmethod
  @overload(float)
  def degrees(radians: float) -> float:
    """
    Calls Qt's 'double QLocationUtils::degrees(double radians)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocationutils.html#degrees

    Parameters
    ----------

    radians : float
      Passed on as it is.
    """
    #  double QLocationUtils::degrees(double radians)
    return Rituals.call('ritual_ZN14QLocationUtils7degreesEd', radians)

  @staticmethod
  def earthMeanRadius() -> float:
    """
    Calls Qt's 'double QLocationUtils::earthMeanRadius()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocationutils.html#earthMeanRadius
    """
    #  double QLocationUtils::earthMeanRadius()
    return Rituals.call('ritual_ZN14QLocationUtils15earthMeanRadiusEv')

  @staticmethod
  def earthMeanCircumference() -> float:
    """
    Calls Qt's 'double QLocationUtils::earthMeanCircumference()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocationutils.html#earthMeanCircumference
    """
    #  double QLocationUtils::earthMeanCircumference()
    return Rituals.call(
        'ritual_ZN14QLocationUtils22earthMeanCircumferenceEv',
    )

  @staticmethod
  def mercatorMaxLatitude() -> float:
    """
    Calls Qt's 'double QLocationUtils::mercatorMaxLatitude()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocationutils.html#mercatorMaxLatitude
    """
    #  double QLocationUtils::mercatorMaxLatitude()
    return Rituals.call('ritual_ZN14QLocationUtils19mercatorMaxLatitudeEv')

  @staticmethod
  @overload(QGeoCoordinate)
  def antipodalPoint(p: QGeoCoordinate) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QLocationUtils::antipodalPoint(const
    QGeoCoordinate &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocationutils.html#antipodalPoint

    Parameters
    ----------

    p : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QLocationUtils::antipodalPoint(const QGeoCoordinate &p)
    address = Rituals.call(
        'ritual_ZN14QLocationUtils14antipodalPointERK14QGeoCoordinate',
        CuteMixin._valueOf(p),
    )
    from . import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  @staticmethod
  @overload(float)
  def mapLeftLongitude(centerLongitude: float) -> float:
    """
    Calls Qt's 'double QLocationUtils::mapLeftLongitude(double
    centerLongitude)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocationutils.html#mapLeftLongitude

    Parameters
    ----------

    centerLongitude : float
      Passed on as it is.
    """
    #  double QLocationUtils::mapLeftLongitude(double centerLongitude)
    return Rituals.call(
        'ritual_ZN14QLocationUtils16mapLeftLongitudeEd', centerLongitude,
    )

  @staticmethod
  @overload(float)
  def mapRightLongitude(centerLongitude: float) -> float:
    """
    Calls Qt's 'double QLocationUtils::mapRightLongitude(double
    centerLongitude)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocationutils.html#mapRightLongitude

    Parameters
    ----------

    centerLongitude : float
      Passed on as it is.
    """
    #  double QLocationUtils::mapRightLongitude(double centerLongitude)
    return Rituals.call(
        'ritual_ZN14QLocationUtils17mapRightLongitudeEd', centerLongitude,
    )

  @staticmethod
  @overload(float, QGeoCoordinate)
  def metersPerPixel(zoomLevel: float, coordinate: QGeoCoordinate) -> float:
    """
    Calls Qt's 'qreal QLocationUtils::metersPerPixel(qreal zoomLevel, const
    QGeoCoordinate &coordinate)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocationutils.html#metersPerPixel

    Parameters
    ----------

    zoomLevel : float
      Passed on as it is.

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  qreal QLocationUtils::metersPerPixel(qreal zoomLevel, const
    #      QGeoCoordinate &coordinate)
    return Rituals.call(
        'ritual_ZN14QLocationUtils14metersPerPixelEdRK14QGeoCoordinate',
        zoomLevel, CuteMixin._valueOf(coordinate),
    )

  @staticmethod
  @overload(QByteArrayView)
  def getNmeaSentenceType(bv: QByteArrayView) -> NmeaSentence:
    """
    Calls Qt's 'NmeaSentence
    QLocationUtils::getNmeaSentenceType(QByteArrayView bv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocationutils.html#getNmeaSentenceType

    Parameters
    ----------

    bv : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    Returns
    -------

    NmeaSentence
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'NmeaSentence(number)'
      gives.
    """
    #  NmeaSentence QLocationUtils::getNmeaSentenceType(QByteArrayView bv)
    return QLocationUtils.NmeaSentence(Rituals.call(
        'ritual_ZN14QLocationUtils19getNmeaSentenceTypeE14QByteArrayView',
        CuteMixin._valueOf(bv),
    ))

  @staticmethod
  @overload(QByteArrayView)
  def getSatelliteSystem(
      bv: QByteArrayView,
  ) -> QGeoSatelliteInfo.SatelliteSystem:
    """
    Calls Qt's 'QGeoSatelliteInfo::SatelliteSystem
    QLocationUtils::getSatelliteSystem(QByteArrayView bv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocationutils.html#getSatelliteSystem

    Parameters
    ----------

    bv : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    Returns
    -------

    QGeoSatelliteInfo.SatelliteSystem
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QGeoSatelliteInfo.SatelliteSystem(number)' gives.
    """
    #  QGeoSatelliteInfo::SatelliteSystem
    #      QLocationUtils::getSatelliteSystem(QByteArrayView bv)
    return QGeoSatelliteInfo.SatelliteSystem(Rituals.call(
        'ritual_ZN14QLocationUtils18getSatelliteSystemE14QByteArrayView',
        CuteMixin._valueOf(bv),
    ))

  @staticmethod
  @overload(int)
  def getSatelliteSystemBySatelliteId(
      satId: int,
  ) -> QGeoSatelliteInfo.SatelliteSystem:
    """
    Calls Qt's 'QGeoSatelliteInfo::SatelliteSystem
    QLocationUtils::getSatelliteSystemBySatelliteId(int satId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocationutils.html

    Parameters
    ----------

    satId : int
      Passed on as it is.

    Returns
    -------

    QGeoSatelliteInfo.SatelliteSystem
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QGeoSatelliteInfo.SatelliteSystem(number)' gives.
    """
    #  QGeoSatelliteInfo::SatelliteSystem
    #      QLocationUtils::getSatelliteSystemBySatelliteId(int satId)
    return QGeoSatelliteInfo.SatelliteSystem(Rituals.call(
        'ritual_ZN14QLocationUtils31getSatelliteSystemBySatelliteIdEi',
        satId,
    ))

  @staticmethod
  @overload(QByteArrayView)
  def hasValidNmeaChecksum(bv: QByteArrayView) -> bool:
    """
    Calls Qt's 'bool QLocationUtils::hasValidNmeaChecksum(QByteArrayView
    bv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocationutils.html#hasValidNmeaChecksum

    Parameters
    ----------

    bv : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  bool QLocationUtils::hasValidNmeaChecksum(QByteArrayView bv)
    return Rituals.call(
        'ritual_ZN14QLocationUtils20hasValidNmeaChecksumE14QByteArrayView',
        CuteMixin._valueOf(bv),
    )

  @staticmethod
  @overload(QByteArray, QTime)
  @overload(QByteArray, NoneType)
  def getNmeaTime(bytes: QByteArray, time: Optional[QTime]) -> bool:
    """
    Calls Qt's 'bool QLocationUtils::getNmeaTime(const QByteArray &bytes,
    QTime *time)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocationutils.html#getNmeaTime

    Parameters
    ----------

    bytes : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    time : Optional[QTime]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QLocationUtils::getNmeaTime(const QByteArray &bytes, QTime *time)
    return Rituals.call(
        'ritual_ZN14QLocationUtils11getNmeaTimeERK10QByteArrayP5QTime',
        CuteMixin._valueOf(bytes), CuteMixin._addressOf(time),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLocationUtils'

  #  Qt's '~QLocationUtils()'. Naming it makes this a value class: Python
  #  owns every C++ QLocationUtils behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QLocationUtilsD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
  def getNmeaLatLong(*__, **_) -> Never:
    """
    Qt's 'bool QLocationUtils::getNmeaLatLong(const QByteArray &latString,
    char latDirection, const QByteArray &lngString, char lngDirection, double
    *lat, double *lon)': takes a single letter as C has it.
    """
    raise NotImplementedError(
        "'QLocationUtils.getNmeaLatLong' has no cute function yet. Qt's "
        "'bool QLocationUtils::getNmeaLatLong(const QByteArray &latString, "
        "char latDirection, const QByteArray &lngString, char lngDirection, "
        "double *lat, double *lon)': takes a single letter as C has it.")

  @staticmethod
  def getPosInfoFromNmea(*__, **_) -> Never:
    """
    Qt's 'bool QLocationUtils::getPosInfoFromNmea(QByteArrayView bv,
    QGeoPositionInfo *info, double uere, bool *hasFix)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QLocationUtils.getPosInfoFromNmea' has no cute function yet. Qt's "
        "'bool QLocationUtils::getPosInfoFromNmea(QByteArrayView bv, "
        "QGeoPositionInfo *info, double uere, bool *hasFix)': takes a "
        "number to change where it is.")

  @staticmethod
  def getSatInUseFromNmea(*__, **_) -> Never:
    """
    Qt's 'QGeoSatelliteInfo::SatelliteSystem
    QLocationUtils::getSatInUseFromNmea(QByteArrayView bv, QList<int>
    &pnrsInUse)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QLocationUtils.getSatInUseFromNmea' has no cute function yet. "
        "Qt's 'QGeoSatelliteInfo::SatelliteSystem "
        "QLocationUtils::getSatInUseFromNmea(QByteArrayView bv, QList<int> "
        "&pnrsInUse)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def getSatInfoFromNmea(*__, **_) -> Never:
    """
    Qt's 'QNmeaSatelliteInfoSource::SatelliteInfoParseStatus
    QLocationUtils::getSatInfoFromNmea(QByteArrayView bv,
    QList<QGeoSatelliteInfo> &infos, QGeoSatelliteInfo::SatelliteSystem
    &system)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QLocationUtils.getSatInfoFromNmea' has no cute function yet. Qt's "
        "'QNmeaSatelliteInfoSource::SatelliteInfoParseStatus "
        "QLocationUtils::getSatInfoFromNmea(QByteArrayView bv, "
        "QList<QGeoSatelliteInfo> &infos, "
        "QGeoSatelliteInfo::SatelliteSystem &system)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def split_double(*__, **_) -> Never:
    """
    Qt's 'void QLocationUtils::split_double(double input, float *hipart,
    float *lopart)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QLocationUtils.split_double' has no cute function yet. Qt's 'void "
        "QLocationUtils::split_double(double input, float *hipart, float "
        "*lopart)': takes a number to change where it is.")
