"""
QGeoRouteRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qgeorouterequest.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QDateTime
  from ..QtPositioning import QGeoCoordinate, QGeoRectangle
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDateTime = WAIT['QDateTime']
  QGeoCoordinate = WAIT['QGeoCoordinate']
  QGeoRectangle = WAIT['QGeoRectangle']


class QGeoRouteRequest(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGeoRouteRequest: a plain Python object standing in
  front of one C++ QGeoRouteRequest.

  C++ hands a QGeoRouteRequest around as a copy, so every C++
  QGeoRouteRequest behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGeoRouteRequest that has a ritual and that Python
  can call so far, 21 names in all: '__eq__', '__ne__', 'setWaypoints',
  'waypoints', 'setExcludeAreas', 'excludeAreas',
  'setNumberAlternativeRoutes', 'numberAlternativeRoutes', 'setTravelModes',
  'travelModes', 'setFeatureWeight', 'featureWeight', 'setRouteOptimization',
  'routeOptimization', 'setSegmentDetail', 'segmentDetail',
  'setManeuverDetail', 'maneuverDetail', 'setDepartureTime', 'departureTime',
  'isEqual'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoRouteRequest::QGeoRouteRequest(QGeoRouteRequest &&other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QGeoRouteRequest::~QGeoRouteRequest()': the destructor: Python
    removes its C++ QGeoRouteRequest by it, and has no other use for it.
  - Qt's 'QGeoRouteRequest &QGeoRouteRequest::operator=(const
    QGeoRouteRequest &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QGeoRouteRequest &QGeoRouteRequest::operator=(QGeoRouteRequest
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'void QGeoRouteRequest::swap(QGeoRouteRequest &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QList<FeatureType> QGeoRouteRequest::featureTypes() const': gives a
    type Python has no way to take yet.

  What to expect
  --------------

  - The C++ QGeoRouteRequest is created at the first use, not by
    'QGeoRouteRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoRouteRequest back gives a copy the ritual made
    for Python, in a new cute QGeoRouteRequest.
  - Each name of Qt's QGeoRouteRequest that has no cute function yet,
    'featureTypes', 'swap', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QGeoRouteRequest, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class FeatureType(CuteFlags):
    """
    The flags enum 'QGeoRouteRequest::FeatureType' of Qt, with the 10 names
    Qt gives in it. Qt names the type of its combinations
    'QGeoRouteRequest::FeatureTypes'.
    """

    NoFeature = 0x0
    TollFeature = 0x1
    HighwayFeature = 0x2
    PublicTransitFeature = 0x4
    FerryFeature = 0x8
    TunnelFeature = 0x10
    DirtRoadFeature = 0x20
    ParksFeature = 0x40
    MotorPoolLaneFeature = 0x80
    TrafficFeature = 0x100

  FeatureTypes = FeatureType

  class FeatureWeight(CuteFlags):
    """
    The flags enum 'QGeoRouteRequest::FeatureWeight' of Qt, with the 5 names
    Qt gives in it. Qt names the type of its combinations
    'QGeoRouteRequest::FeatureWeights'.
    """

    NeutralFeatureWeight = 0x0
    PreferFeatureWeight = 0x1
    RequireFeatureWeight = 0x2
    AvoidFeatureWeight = 0x4
    DisallowFeatureWeight = 0x8

  FeatureWeights = FeatureWeight

  class ManeuverDetail(CuteFlags):
    """
    The flags enum 'QGeoRouteRequest::ManeuverDetail' of Qt, with the 2 names
    Qt gives in it. Qt names the type of its combinations
    'QGeoRouteRequest::ManeuverDetails'.
    """

    NoManeuvers = 0x0
    BasicManeuvers = 0x1

  ManeuverDetails = ManeuverDetail

  class RouteOptimization(CuteFlags):
    """
    The flags enum 'QGeoRouteRequest::RouteOptimization' of Qt, with the 4
    names Qt gives in it. Qt names the type of its combinations
    'QGeoRouteRequest::RouteOptimizations'.
    """

    ShortestRoute = 0x1
    FastestRoute = 0x2
    MostEconomicRoute = 0x4
    MostScenicRoute = 0x8

  RouteOptimizations = RouteOptimization

  class SegmentDetail(CuteFlags):
    """
    The flags enum 'QGeoRouteRequest::SegmentDetail' of Qt, with the 2 names
    Qt gives in it. Qt names the type of its combinations
    'QGeoRouteRequest::SegmentDetails'.
    """

    NoSegmentData = 0x0
    BasicSegmentData = 0x1

  SegmentDetails = SegmentDetail

  class TravelMode(CuteFlags):
    """
    The flags enum 'QGeoRouteRequest::TravelMode' of Qt, with the 5 names Qt
    gives in it. Qt names the type of its combinations
    'QGeoRouteRequest::TravelModes'.
    """

    CarTravel = 0x1
    PedestrianTravel = 0x2
    BicycleTravel = 0x4
    PublicTransitTravel = 0x8
    TruckTravel = 0x10

  TravelModes = TravelMode

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoRouteRequest'

  #  Qt's '~QGeoRouteRequest()'. Naming it makes this a value class: Python
  #  owns every C++ QGeoRouteRequest behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QGeoRouteRequestD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def waypoints(self) -> QList[QGeoCoordinate]:
    """
    Calls Qt's 'QList<QGeoCoordinate> QGeoRouteRequest::waypoints() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorouterequest.html#waypoints

    Returns
    -------

    QList[QGeoCoordinate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGeoCoordinate> QGeoRouteRequest::waypoints() const
    address = self.uglySide.call('ritual_ZNK16QGeoRouteRequest9waypointsEv')
    from ..QtPositioning import QGeoCoordinate
    return QList[QGeoCoordinate]._cuteOwning(address)

  def excludeAreas(self) -> QList[QGeoRectangle]:
    """
    Calls Qt's 'QList<QGeoRectangle> QGeoRouteRequest::excludeAreas() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorouterequest.html#excludeAreas

    Returns
    -------

    QList[QGeoRectangle]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGeoRectangle> QGeoRouteRequest::excludeAreas() const
    address = self.uglySide.call(
        'ritual_ZNK16QGeoRouteRequest12excludeAreasEv',
    )
    from ..QtPositioning import QGeoRectangle
    return QList[QGeoRectangle]._cuteOwning(address)

  def numberAlternativeRoutes(self) -> int:
    """
    Calls Qt's 'int QGeoRouteRequest::numberAlternativeRoutes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorouterequest.html#numberAlternativeRoutes
    """
    #  int QGeoRouteRequest::numberAlternativeRoutes() const
    return self.uglySide.call(
        'ritual_ZNK16QGeoRouteRequest23numberAlternativeRoutesEv',
    )

  def travelModes(self) -> TravelModes:
    """
    Calls Qt's 'TravelModes QGeoRouteRequest::travelModes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorouterequest.html#travelModes

    Returns
    -------

    TravelModes
      The value standing for the combination Qt gave back.
    """
    #  TravelModes QGeoRouteRequest::travelModes() const
    return QGeoRouteRequest.TravelModes(self.uglySide.call(
        'ritual_ZNK16QGeoRouteRequest11travelModesEv',
    ))

  @overload(FeatureType)
  def featureWeight(self, featureType: FeatureType) -> FeatureWeight:
    """
    Calls Qt's 'FeatureWeight QGeoRouteRequest::featureWeight(FeatureType
    featureType) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorouterequest.html#featureWeight

    Parameters
    ----------

    featureType : FeatureType
      Passed on as its number.

    Returns
    -------

    FeatureWeight
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FeatureWeight(number)'
      gives.
    """
    #  FeatureWeight QGeoRouteRequest::featureWeight(FeatureType featureType)
    #      const
    return QGeoRouteRequest.FeatureWeight(self.uglySide.call(
        'ritual_ZNK16QGeoRouteRequest13featureWeightENS_11FeatureTypeE',
        featureType.value,
    ))

  def routeOptimization(self) -> RouteOptimizations:
    """
    Calls Qt's 'RouteOptimizations QGeoRouteRequest::routeOptimization()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorouterequest.html#routeOptimization

    Returns
    -------

    RouteOptimizations
      The value standing for the combination Qt gave back.
    """
    #  RouteOptimizations QGeoRouteRequest::routeOptimization() const
    return QGeoRouteRequest.RouteOptimizations(self.uglySide.call(
        'ritual_ZNK16QGeoRouteRequest17routeOptimizationEv',
    ))

  def segmentDetail(self) -> SegmentDetail:
    """
    Calls Qt's 'SegmentDetail QGeoRouteRequest::segmentDetail() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorouterequest.html#segmentDetail

    Returns
    -------

    SegmentDetail
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SegmentDetail(number)'
      gives.
    """
    #  SegmentDetail QGeoRouteRequest::segmentDetail() const
    return QGeoRouteRequest.SegmentDetail(self.uglySide.call(
        'ritual_ZNK16QGeoRouteRequest13segmentDetailEv',
    ))

  def maneuverDetail(self) -> ManeuverDetail:
    """
    Calls Qt's 'ManeuverDetail QGeoRouteRequest::maneuverDetail() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorouterequest.html#maneuverDetail

    Returns
    -------

    ManeuverDetail
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ManeuverDetail(number)'
      gives.
    """
    #  ManeuverDetail QGeoRouteRequest::maneuverDetail() const
    return QGeoRouteRequest.ManeuverDetail(self.uglySide.call(
        'ritual_ZNK16QGeoRouteRequest14maneuverDetailEv',
    ))

  def departureTime(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QGeoRouteRequest::departureTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorouterequest.html#departureTime

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QGeoRouteRequest::departureTime() const
    address = self.uglySide.call(
        'ritual_ZNK16QGeoRouteRequest13departureTimeEv',
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  @overload(THIS)
  def isEqual(self, other: QGeoRouteRequest) -> bool:
    """
    Calls Qt's 'bool QGeoRouteRequest::isEqual(const QGeoRouteRequest &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorouterequest.html#isEqual

    Parameters
    ----------

    other : QGeoRouteRequest
      Passed on as a value: Qt reads the C++ QGeoRouteRequest, which stays
      Python's own.
    """
    #  bool QGeoRouteRequest::isEqual(const QGeoRouteRequest &other) const
    return self.uglySide.call(
        'ritual_ZNK16QGeoRouteRequest7isEqualERKS_', self._valueOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QGeoCoordinate])
  def setWaypoints(self, waypoints: QList[QGeoCoordinate]) -> None:
    """
    Calls Qt's 'void QGeoRouteRequest::setWaypoints(const
    QList<QGeoCoordinate> &waypoints)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorouterequest.html#setWaypoints

    Parameters
    ----------

    waypoints : QList[QGeoCoordinate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QGeoRouteRequest::setWaypoints(const QList<QGeoCoordinate>
    #      &waypoints)
    self.uglySide.call(
        'ritual_ZN16QGeoRouteRequest12setWaypointsERK5QListI14QGeoCoordinat'
        'eE',
        self._valueOf(waypoints),
    )

  @overload(QList[QGeoRectangle])
  def setExcludeAreas(self, areas: QList[QGeoRectangle]) -> None:
    """
    Calls Qt's 'void QGeoRouteRequest::setExcludeAreas(const
    QList<QGeoRectangle> &areas)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorouterequest.html#setExcludeAreas

    Parameters
    ----------

    areas : QList[QGeoRectangle]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QGeoRouteRequest::setExcludeAreas(const QList<QGeoRectangle>
    #      &areas)
    self.uglySide.call(
        'ritual_ZN16QGeoRouteRequest15setExcludeAreasERK5QListI13QGeoRectan'
        'gleE',
        self._valueOf(areas),
    )

  @overload(int)
  def setNumberAlternativeRoutes(self, alternatives: int) -> None:
    """
    Calls Qt's 'void QGeoRouteRequest::setNumberAlternativeRoutes(int
    alternatives)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorouterequest.html#setNumberAlternativeRoutes

    Parameters
    ----------

    alternatives : int
      Passed on as it is.
    """
    #  void QGeoRouteRequest::setNumberAlternativeRoutes(int alternatives)
    self.uglySide.call(
        'ritual_ZN16QGeoRouteRequest26setNumberAlternativeRoutesEi',
        alternatives,
    )

  @overload(TravelModes)
  def setTravelModes(self, travelModes: TravelModes) -> None:
    """
    Calls Qt's 'void QGeoRouteRequest::setTravelModes(TravelModes
    travelModes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorouterequest.html#setTravelModes

    Parameters
    ----------

    travelModes : TravelModes
      Passed on as its number.
    """
    #  void QGeoRouteRequest::setTravelModes(TravelModes travelModes)
    self.uglySide.call(
        'ritual_ZN16QGeoRouteRequest14setTravelModesE6QFlagsINS_10TravelMod'
        'eEE',
        travelModes.value,
    )

  @overload(FeatureType, FeatureWeight)
  def setFeatureWeight(
      self,
      featureType: FeatureType,
      featureWeight: FeatureWeight,
  ) -> None:
    """
    Calls Qt's 'void QGeoRouteRequest::setFeatureWeight(FeatureType
    featureType, FeatureWeight featureWeight)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorouterequest.html#setFeatureWeight

    Parameters
    ----------

    featureType : FeatureType
      Passed on as its number.

    featureWeight : FeatureWeight
      Passed on as its number.
    """
    #  void QGeoRouteRequest::setFeatureWeight(FeatureType featureType,
    #      FeatureWeight featureWeight)
    self.uglySide.call(
        'ritual_ZN16QGeoRouteRequest16setFeatureWeightENS_11FeatureTypeENS_'
        '13FeatureWeightE',
        featureType.value, featureWeight.value,
    )

  @overload(RouteOptimizations)
  def setRouteOptimization(self, optimization: RouteOptimizations) -> None:
    """
    Calls Qt's 'void
    QGeoRouteRequest::setRouteOptimization(RouteOptimizations optimization)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorouterequest.html#setRouteOptimization

    Parameters
    ----------

    optimization : RouteOptimizations
      Passed on as its number.
    """
    #  void QGeoRouteRequest::setRouteOptimization(RouteOptimizations
    #      optimization)
    self.uglySide.call(
        'ritual_ZN16QGeoRouteRequest20setRouteOptimizationE6QFlagsINS_17Rou'
        'teOptimizationEE',
        optimization.value,
    )

  @overload(SegmentDetail)
  def setSegmentDetail(self, segmentDetail: SegmentDetail) -> None:
    """
    Calls Qt's 'void QGeoRouteRequest::setSegmentDetail(SegmentDetail
    segmentDetail)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorouterequest.html#setSegmentDetail

    Parameters
    ----------

    segmentDetail : SegmentDetail
      Passed on as its number.
    """
    #  void QGeoRouteRequest::setSegmentDetail(SegmentDetail segmentDetail)
    self.uglySide.call(
        'ritual_ZN16QGeoRouteRequest16setSegmentDetailENS_13SegmentDetailE',
        segmentDetail.value,
    )

  @overload(ManeuverDetail)
  def setManeuverDetail(self, maneuverDetail: ManeuverDetail) -> None:
    """
    Calls Qt's 'void QGeoRouteRequest::setManeuverDetail(ManeuverDetail
    maneuverDetail)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorouterequest.html#setManeuverDetail

    Parameters
    ----------

    maneuverDetail : ManeuverDetail
      Passed on as its number.
    """
    #  void QGeoRouteRequest::setManeuverDetail(ManeuverDetail
    #      maneuverDetail)
    self.uglySide.call(
        'ritual_ZN16QGeoRouteRequest17setManeuverDetailENS_14ManeuverDetail'
        'E',
        maneuverDetail.value,
    )

  @overload(QDateTime)
  def setDepartureTime(self, departureTime: QDateTime) -> None:
    """
    Calls Qt's 'void QGeoRouteRequest::setDepartureTime(const QDateTime
    &departureTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorouterequest.html#setDepartureTime

    Parameters
    ----------

    departureTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QGeoRouteRequest::setDepartureTime(const QDateTime
    #      &departureTime)
    self.uglySide.call(
        'ritual_ZN16QGeoRouteRequest16setDepartureTimeERK9QDateTime',
        self._valueOf(departureTime),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QGeoRouteRequest) -> bool:
    """
    Calls Qt's 'bool operator==(const QGeoRouteRequest &lhs, const
    QGeoRouteRequest &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorouterequest.html#operator==

    Parameters
    ----------

    rhs : QGeoRouteRequest
      Passed on as a value: Qt reads the C++ QGeoRouteRequest, which stays
      Python's own.
    """
    #  bool operator==(const QGeoRouteRequest &lhs, const QGeoRouteRequest
    #      &rhs)
    return Rituals.call(
        'ritual_ZeqRK16QGeoRouteRequestS1_',
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
  def __ne__(self, rhs: QGeoRouteRequest) -> bool:
    """
    Calls Qt's 'bool operator!=(const QGeoRouteRequest &lhs, const
    QGeoRouteRequest &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorouterequest.html#operator!=

    Parameters
    ----------

    rhs : QGeoRouteRequest
      Passed on as a value: Qt reads the C++ QGeoRouteRequest, which stays
      Python's own.
    """
    #  bool operator!=(const QGeoRouteRequest &lhs, const QGeoRouteRequest
    #      &rhs)
    return Rituals.call(
        'ritual_ZneRK16QGeoRouteRequestS1_',
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

  @overload(QList[QGeoCoordinate])
  def __init__(self, waypoints: QList[QGeoCoordinate]) -> None:
    """
    Notes what was given, for Qt's 'QGeoRouteRequest::QGeoRouteRequest(const
    QList<QGeoCoordinate> &waypoints)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorouterequest.html#QGeoRouteRequest

    Parameters
    ----------

    waypoints : QList[QGeoCoordinate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  QGeoRouteRequest::QGeoRouteRequest(const QList<QGeoCoordinate>
    #      &waypoints)
    self._noteCreation(QGeoRouteRequest, lambda: Rituals.call(
        'ritual_ZN16QGeoRouteRequestC1ERK5QListI14QGeoCoordinateE',
        self._valueOf(waypoints),
    ))

  @overload(QGeoCoordinate, QGeoCoordinate)
  def __init__(
      self,
      origin: QGeoCoordinate,
      destination: QGeoCoordinate,
  ) -> None:
    """
    Notes what was given, for Qt's 'QGeoRouteRequest::QGeoRouteRequest(const
    QGeoCoordinate &origin, const QGeoCoordinate &destination)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorouterequest.html#QGeoRouteRequest

    Parameters
    ----------

    origin : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.

    destination : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  QGeoRouteRequest::QGeoRouteRequest(const QGeoCoordinate &origin, const
    #      QGeoCoordinate &destination)
    self._noteCreation(QGeoRouteRequest, lambda: Rituals.call(
        'ritual_ZN16QGeoRouteRequestC1ERK14QGeoCoordinateS2_',
        self._valueOf(origin), self._valueOf(destination),
    ))

  @overload(THIS)
  def __init__(self, other: QGeoRouteRequest) -> None:
    """
    Notes what was given, for Qt's 'QGeoRouteRequest::QGeoRouteRequest(const
    QGeoRouteRequest &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorouterequest.html#QGeoRouteRequest

    Parameters
    ----------

    other : QGeoRouteRequest
      Passed on as a value: Qt reads the C++ QGeoRouteRequest, which stays
      Python's own.
    """
    #  QGeoRouteRequest::QGeoRouteRequest(const QGeoRouteRequest &other)
    self._noteCreation(QGeoRouteRequest, lambda: Rituals.call(
        'ritual_ZN16QGeoRouteRequestC1ERKS_', self._valueOf(other),
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
  def featureTypes(*__, **_) -> Never:
    """
    Qt's 'QList<FeatureType> QGeoRouteRequest::featureTypes() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGeoRouteRequest.featureTypes' has no cute function yet. Qt's "
        "'QList<FeatureType> QGeoRouteRequest::featureTypes() const': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QGeoRouteRequest::swap(QGeoRouteRequest &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoRouteRequest.swap' has no cute function yet. Qt's 'void "
        "QGeoRouteRequest::swap(QGeoRouteRequest &other)': takes a type "
        "Python has no way to hand over yet.")
