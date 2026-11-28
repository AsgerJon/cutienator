"""
QDeclarativeGeoRouteQuery binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qdeclarativegeoroutemodel_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativeGeoRouteQuery to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDateTime, QMetaObject
  from ..QtPositioning import QGeoCoordinate, QGeoRectangle
  from . import QGeoRouteRequest
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDateTime = WAIT['QDateTime']
  QGeoCoordinate = WAIT['QGeoCoordinate']
  QGeoRectangle = WAIT['QGeoRectangle']
  QGeoRouteRequest = WAIT['QGeoRouteRequest']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDeclarativeGeoRouteQuery(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QDeclarativeGeoRouteQuery: a plain Python object
  standing in front of one C++ QDeclarativeGeoRouteQuery.

  It is built on the cute 'QObject', as Qt's QDeclarativeGeoRouteQuery is
  built on Qt's QObject, and has everything that class has. It is built on
  the cute 'QQmlParserStatus' as well, as Qt's QDeclarativeGeoRouteQuery is
  built on Qt's QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativeGeoRouteQuery that has a ritual and that
  Python can call so far, 43 names in all: 'metaObject', 'tr', 'classBegin',
  'componentComplete', 'routeRequest', 'setNumberAlternativeRoutes',
  'numberAlternativeRoutes', 'waypoints', 'setWaypoints', 'excludedAreas',
  'setExcludedAreas', 'addWaypoint', 'removeWaypoint', 'clearWaypoints',
  'addExcludedArea', 'removeExcludedArea', 'clearExcludedAreas',
  'setFeatureWeight', 'featureWeight', 'resetFeatureWeights',
  'setTravelModes', 'travelModes', 'setSegmentDetail', 'segmentDetail',
  'setManeuverDetail', 'maneuverDetail', 'setRouteOptimizations',
  'routeOptimizations', 'setDepartureTime', 'departureTime',
  'numberAlternativeRoutesChanged', 'travelModesChanged',
  'routeOptimizationsChanged', 'waypointsChanged', 'excludedAreasChanged',
  'featureTypesChanged', 'maneuverDetailChanged', 'segmentDetailChanged',
  'queryDetailsChanged', 'departureTimeChanged',
  'excludedAreaCoordinateChanged', 'waypointChanged', 'doCoordinateChanged'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDeclarativeGeoRouteQuery::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QDeclarativeGeoRouteQuery::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDeclarativeGeoRouteQuery::~QDeclarativeGeoRouteQuery()': the
    destructor: Python never removes a C++ QDeclarativeGeoRouteQuery.
  - Qt's 'QList<int> QDeclarativeGeoRouteQuery::featureTypes() const': gives
    a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 51 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDeclarativeGeoRouteQuery is created at the first use, not by
    'QDeclarativeGeoRouteQuery(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativeGeoRouteQuery.
  - Qt tells when it has removed the C++ QDeclarativeGeoRouteQuery. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDeclarativeGeoRouteQuery that has no cute function
    yet, 'featureTypes', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QDeclarativeGeoRouteQuery, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class FeatureType(CuteFlags):
    """
    The flags enum 'QDeclarativeGeoRouteQuery::FeatureType' of Qt, with the
    10 names Qt gives in it. Qt names the type of its combinations
    'QDeclarativeGeoRouteQuery::FeatureTypes'.
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
    The flags enum 'QDeclarativeGeoRouteQuery::FeatureWeight' of Qt, with the
    5 names Qt gives in it. Qt names the type of its combinations
    'QDeclarativeGeoRouteQuery::FeatureWeights'.
    """

    NeutralFeatureWeight = 0x0
    PreferFeatureWeight = 0x1
    RequireFeatureWeight = 0x2
    AvoidFeatureWeight = 0x4
    DisallowFeatureWeight = 0x8

  FeatureWeights = FeatureWeight

  class ManeuverDetail(CuteFlags):
    """
    The flags enum 'QDeclarativeGeoRouteQuery::ManeuverDetail' of Qt, with
    the 2 names Qt gives in it. Qt names the type of its combinations
    'QDeclarativeGeoRouteQuery::ManeuverDetails'.
    """

    NoManeuvers = 0x0
    BasicManeuvers = 0x1

  ManeuverDetails = ManeuverDetail

  class RouteOptimization(CuteFlags):
    """
    The flags enum 'QDeclarativeGeoRouteQuery::RouteOptimization' of Qt, with
    the 4 names Qt gives in it. Qt names the type of its combinations
    'QDeclarativeGeoRouteQuery::RouteOptimizations'.
    """

    ShortestRoute = 0x1
    FastestRoute = 0x2
    MostEconomicRoute = 0x4
    MostScenicRoute = 0x8

  RouteOptimizations = RouteOptimization

  class SegmentDetail(CuteFlags):
    """
    The flags enum 'QDeclarativeGeoRouteQuery::SegmentDetail' of Qt, with the
    2 names Qt gives in it. Qt names the type of its combinations
    'QDeclarativeGeoRouteQuery::SegmentDetails'.
    """

    NoSegmentData = 0x0
    BasicSegmentData = 0x1

  SegmentDetails = SegmentDetail

  class TravelMode(CuteFlags):
    """
    The flags enum 'QDeclarativeGeoRouteQuery::TravelMode' of Qt, with the 5
    names Qt gives in it. Qt names the type of its combinations
    'QDeclarativeGeoRouteQuery::TravelModes'.
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

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QDeclarativeGeoRouteQuery::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativeGeoRouteQuery::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QDeclarativeGeoRouteQuery2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativeGeoRouteQuery'

  #  Qt's QDeclarativeGeoRouteQuery is built on more than one class. The part
  #  of a C++ QDeclarativeGeoRouteQuery that belongs to a class after the
  #  first begins somewhere inside the object, and the ritual named for that
  #  class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus':
          'ritual_cast_QDeclarativeGeoRouteQuery_QQmlParserStatus',
  }

  #  A C++ QDeclarativeGeoRouteQuery Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativeGeoRouteQuery'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDeclarativeGeoRouteQuery::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDeclarativeGeoRouteQuery::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QDeclarativeGeoRouteQuery10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def routeRequest(self) -> QGeoRouteRequest:
    """
    Calls Qt's 'QGeoRouteRequest QDeclarativeGeoRouteQuery::routeRequest()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#routeRequest

    Returns
    -------

    QGeoRouteRequest
      A new cute QGeoRouteRequest around the copy Qt gave back. Python owns
      it.
    """
    #  QGeoRouteRequest QDeclarativeGeoRouteQuery::routeRequest() const
    address = self.uglySide.call(
        'ritual_ZNK25QDeclarativeGeoRouteQuery12routeRequestEv',
    )
    from . import QGeoRouteRequest
    return QGeoRouteRequest._cuteOwning(address)

  def numberAlternativeRoutes(self) -> int:
    """
    Calls Qt's 'int QDeclarativeGeoRouteQuery::numberAlternativeRoutes()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html
    """
    #  int QDeclarativeGeoRouteQuery::numberAlternativeRoutes() const
    return self.uglySide.call(
        'ritual_ZNK25QDeclarativeGeoRouteQuery23numberAlternativeRoutesEv',
    )

  def waypoints(self) -> QList[QGeoCoordinate]:
    """
    Calls Qt's 'QList<QGeoCoordinate> QDeclarativeGeoRouteQuery::waypoints()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#waypoints

    Returns
    -------

    QList[QGeoCoordinate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGeoCoordinate> QDeclarativeGeoRouteQuery::waypoints() const
    address = self.uglySide.call(
        'ritual_ZNK25QDeclarativeGeoRouteQuery9waypointsEv',
    )
    from ..QtPositioning import QGeoCoordinate
    return QList[QGeoCoordinate]._cuteOwning(address)

  def excludedAreas(self) -> QList[QGeoRectangle]:
    """
    Calls Qt's 'QList<QGeoRectangle>
    QDeclarativeGeoRouteQuery::excludedAreas() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#excludedAreas

    Returns
    -------

    QList[QGeoRectangle]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGeoRectangle> QDeclarativeGeoRouteQuery::excludedAreas() const
    address = self.uglySide.call(
        'ritual_ZNK25QDeclarativeGeoRouteQuery13excludedAreasEv',
    )
    from ..QtPositioning import QGeoRectangle
    return QList[QGeoRectangle]._cuteOwning(address)

  def travelModes(self) -> TravelModes:
    """
    Calls Qt's 'TravelModes QDeclarativeGeoRouteQuery::travelModes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#travelModes

    Returns
    -------

    TravelModes
      The value standing for the combination Qt gave back.
    """
    #  TravelModes QDeclarativeGeoRouteQuery::travelModes() const
    return QDeclarativeGeoRouteQuery.TravelModes(self.uglySide.call(
        'ritual_ZNK25QDeclarativeGeoRouteQuery11travelModesEv',
    ))

  def segmentDetail(self) -> SegmentDetail:
    """
    Calls Qt's 'SegmentDetail QDeclarativeGeoRouteQuery::segmentDetail()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#segmentDetail

    Returns
    -------

    SegmentDetail
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SegmentDetail(number)'
      gives.
    """
    #  SegmentDetail QDeclarativeGeoRouteQuery::segmentDetail() const
    return QDeclarativeGeoRouteQuery.SegmentDetail(self.uglySide.call(
        'ritual_ZNK25QDeclarativeGeoRouteQuery13segmentDetailEv',
    ))

  def maneuverDetail(self) -> ManeuverDetail:
    """
    Calls Qt's 'ManeuverDetail QDeclarativeGeoRouteQuery::maneuverDetail()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#maneuverDetail

    Returns
    -------

    ManeuverDetail
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ManeuverDetail(number)'
      gives.
    """
    #  ManeuverDetail QDeclarativeGeoRouteQuery::maneuverDetail() const
    return QDeclarativeGeoRouteQuery.ManeuverDetail(self.uglySide.call(
        'ritual_ZNK25QDeclarativeGeoRouteQuery14maneuverDetailEv',
    ))

  def routeOptimizations(self) -> RouteOptimizations:
    """
    Calls Qt's 'RouteOptimizations
    QDeclarativeGeoRouteQuery::routeOptimizations() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#routeOptimizations

    Returns
    -------

    RouteOptimizations
      The value standing for the combination Qt gave back.
    """
    #  RouteOptimizations QDeclarativeGeoRouteQuery::routeOptimizations()
    #      const
    return QDeclarativeGeoRouteQuery.RouteOptimizations(self.uglySide.call(
        'ritual_ZNK25QDeclarativeGeoRouteQuery18routeOptimizationsEv',
    ))

  def departureTime(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDeclarativeGeoRouteQuery::departureTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#departureTime

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDeclarativeGeoRouteQuery::departureTime() const
    address = self.uglySide.call(
        'ritual_ZNK25QDeclarativeGeoRouteQuery13departureTimeEv',
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setNumberAlternativeRoutes(self, numberAlternativeRoutes: int) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoRouteQuery::setNumberAlternativeRoutes(int
    numberAlternativeRoutes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html

    Parameters
    ----------

    numberAlternativeRoutes : int
      Passed on as it is.
    """
    #  void QDeclarativeGeoRouteQuery::setNumberAlternativeRoutes(int
    #      numberAlternativeRoutes)
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteQuery26setNumberAlternativeRoutesEi',
        numberAlternativeRoutes,
    )

  @overload(QList[QGeoCoordinate])
  def setWaypoints(self, value: QList[QGeoCoordinate]) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteQuery::setWaypoints(const
    QList<QGeoCoordinate> &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#setWaypoints

    Parameters
    ----------

    value : QList[QGeoCoordinate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDeclarativeGeoRouteQuery::setWaypoints(const
    #      QList<QGeoCoordinate> &value)
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteQuery12setWaypointsERK5QListI14QGeo'
        'CoordinateE',
        self._valueOf(value),
    )

  @overload(QList[QGeoRectangle])
  def setExcludedAreas(self, value: QList[QGeoRectangle]) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteQuery::setExcludedAreas(const
    QList<QGeoRectangle> &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#setExcludedAreas

    Parameters
    ----------

    value : QList[QGeoRectangle]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDeclarativeGeoRouteQuery::setExcludedAreas(const
    #      QList<QGeoRectangle> &value)
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteQuery16setExcludedAreasERK5QListI13'
        'QGeoRectangleE',
        self._valueOf(value),
    )

  @overload(FeatureType, FeatureWeight)
  def setFeatureWeight(
      self,
      featureType: FeatureType,
      featureWeight: FeatureWeight,
  ) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteQuery::setFeatureWeight(FeatureType
    featureType, FeatureWeight featureWeight)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#setFeatureWeight

    Parameters
    ----------

    featureType : FeatureType
      Passed on as its number.

    featureWeight : FeatureWeight
      Passed on as its number.
    """
    #  void QDeclarativeGeoRouteQuery::setFeatureWeight(FeatureType
    #      featureType, FeatureWeight featureWeight)
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteQuery16setFeatureWeightENS_11Featur'
        'eTypeENS_13FeatureWeightE',
        featureType.value, featureWeight.value,
    )

  @overload(TravelModes)
  def setTravelModes(self, travelModes: TravelModes) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteQuery::setTravelModes(TravelModes
    travelModes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#setTravelModes

    Parameters
    ----------

    travelModes : TravelModes
      Passed on as its number.
    """
    #  void QDeclarativeGeoRouteQuery::setTravelModes(TravelModes
    #      travelModes)
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteQuery14setTravelModesE6QFlagsINS_10'
        'TravelModeEE',
        travelModes.value,
    )

  @overload(SegmentDetail)
  def setSegmentDetail(self, segmentDetail: SegmentDetail) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoRouteQuery::setSegmentDetail(SegmentDetail
    segmentDetail)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#setSegmentDetail

    Parameters
    ----------

    segmentDetail : SegmentDetail
      Passed on as its number.
    """
    #  void QDeclarativeGeoRouteQuery::setSegmentDetail(SegmentDetail
    #      segmentDetail)
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteQuery16setSegmentDetailENS_13Segmen'
        'tDetailE',
        segmentDetail.value,
    )

  @overload(ManeuverDetail)
  def setManeuverDetail(self, maneuverDetail: ManeuverDetail) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoRouteQuery::setManeuverDetail(ManeuverDetail
    maneuverDetail)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#setManeuverDetail

    Parameters
    ----------

    maneuverDetail : ManeuverDetail
      Passed on as its number.
    """
    #  void QDeclarativeGeoRouteQuery::setManeuverDetail(ManeuverDetail
    #      maneuverDetail)
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteQuery17setManeuverDetailENS_14Maneu'
        'verDetailE',
        maneuverDetail.value,
    )

  @overload(RouteOptimizations)
  def setRouteOptimizations(self, optimization: RouteOptimizations) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoRouteQuery::setRouteOptimizations(RouteOptimizations
    optimization)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html

    Parameters
    ----------

    optimization : RouteOptimizations
      Passed on as its number.
    """
    #  void QDeclarativeGeoRouteQuery::setRouteOptimizations(
    #      RouteOptimizations optimization)
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteQuery21setRouteOptimizationsE6QFlag'
        'sINS_17RouteOptimizationEE',
        optimization.value,
    )

  @overload(QDateTime)
  def setDepartureTime(self, departureTime: QDateTime) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteQuery::setDepartureTime(const
    QDateTime &departureTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#setDepartureTime

    Parameters
    ----------

    departureTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QDeclarativeGeoRouteQuery::setDepartureTime(const QDateTime
    #      &departureTime)
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteQuery16setDepartureTimeERK9QDateTim'
        'e',
        self._valueOf(departureTime),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QDeclarativeGeoRouteQuery::QDeclarativeGeoRouteQuery(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDeclarativeGeoRouteQuery::QDeclarativeGeoRouteQuery(QObject *parent)
    self._noteCreation(QDeclarativeGeoRouteQuery, lambda: Rituals.call(
        'ritual_ZN25QDeclarativeGeoRouteQueryC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QGeoRouteRequest)
  @overload(QGeoRouteRequest, QObject)
  @overload(QGeoRouteRequest, NoneType)
  def __init__(
      self,
      request: QGeoRouteRequest,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QDeclarativeGeoRouteQuery::QDeclarativeGeoRouteQuery(const
    QGeoRouteRequest &request, QObject *parent)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html

    Parameters
    ----------

    request : QGeoRouteRequest
      Passed on as a value: Qt reads the C++ QGeoRouteRequest, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDeclarativeGeoRouteQuery::QDeclarativeGeoRouteQuery(const
    #      QGeoRouteRequest &request, QObject *parent)
    self._noteCreation(QDeclarativeGeoRouteQuery, lambda: Rituals.call(
        'ritual_ZN25QDeclarativeGeoRouteQueryC1ERK16QGeoRouteRequestP7QObje'
        'ct',
        self._valueOf(request), self._addressOf(parent, 'QObject'),
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

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteQuery::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#classBegin
    """
    #  void QDeclarativeGeoRouteQuery::classBegin()
    ritual = 'ritual_ZN25QDeclarativeGeoRouteQuery10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QDeclarativeGeoRouteQuery10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteQuery::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#componentComplete
    """
    #  void QDeclarativeGeoRouteQuery::componentComplete()
    ritual = 'ritual_ZN25QDeclarativeGeoRouteQuery17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QDeclarativeGeoRouteQuery17componentCompleteEv')
    self.uglySide.call(ritual)

  @overload(QGeoCoordinate)
  def addWaypoint(self, w: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteQuery::addWaypoint(const
    QGeoCoordinate &w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#addWaypoint

    Parameters
    ----------

    w : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QDeclarativeGeoRouteQuery::addWaypoint(const QGeoCoordinate &w)
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteQuery11addWaypointERK14QGeoCoordina'
        'te',
        self._valueOf(w),
    )

  @overload(QGeoCoordinate)
  def removeWaypoint(self, waypoint: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteQuery::removeWaypoint(const
    QGeoCoordinate &waypoint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#removeWaypoint

    Parameters
    ----------

    waypoint : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QDeclarativeGeoRouteQuery::removeWaypoint(const QGeoCoordinate
    #      &waypoint)
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteQuery14removeWaypointERK14QGeoCoord'
        'inate',
        self._valueOf(waypoint),
    )

  def clearWaypoints(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteQuery::clearWaypoints()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#clearWaypoints
    """
    #  void QDeclarativeGeoRouteQuery::clearWaypoints()
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteQuery14clearWaypointsEv',
    )

  @overload(QGeoRectangle)
  def addExcludedArea(self, area: QGeoRectangle) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteQuery::addExcludedArea(const
    QGeoRectangle &area)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#addExcludedArea

    Parameters
    ----------

    area : QGeoRectangle
      Passed on as a value: Qt reads the C++ QGeoRectangle, which stays
      Python's own.
    """
    #  void QDeclarativeGeoRouteQuery::addExcludedArea(const QGeoRectangle
    #      &area)
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteQuery15addExcludedAreaERK13QGeoRect'
        'angle',
        self._valueOf(area),
    )

  @overload(QGeoRectangle)
  def removeExcludedArea(self, area: QGeoRectangle) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteQuery::removeExcludedArea(const
    QGeoRectangle &area)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#removeExcludedArea

    Parameters
    ----------

    area : QGeoRectangle
      Passed on as a value: Qt reads the C++ QGeoRectangle, which stays
      Python's own.
    """
    #  void QDeclarativeGeoRouteQuery::removeExcludedArea(const QGeoRectangle
    #      &area)
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteQuery18removeExcludedAreaERK13QGeoR'
        'ectangle',
        self._valueOf(area),
    )

  def clearExcludedAreas(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteQuery::clearExcludedAreas()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#clearExcludedAreas
    """
    #  void QDeclarativeGeoRouteQuery::clearExcludedAreas()
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteQuery18clearExcludedAreasEv',
    )

  @overload(FeatureType)
  def featureWeight(self, featureType: FeatureType) -> int:
    """
    Calls Qt's 'int QDeclarativeGeoRouteQuery::featureWeight(FeatureType
    featureType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#featureWeight

    Parameters
    ----------

    featureType : FeatureType
      Passed on as its number.
    """
    #  int QDeclarativeGeoRouteQuery::featureWeight(FeatureType featureType)
    return self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteQuery13featureWeightENS_11FeatureTy'
        'peE',
        featureType.value,
    )

  def resetFeatureWeights(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteQuery::resetFeatureWeights()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#resetFeatureWeights
    """
    #  void QDeclarativeGeoRouteQuery::resetFeatureWeights()
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteQuery19resetFeatureWeightsEv',
    )

  def numberAlternativeRoutesChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoRouteQuery::numberAlternativeRoutesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html
    """
    #  void QDeclarativeGeoRouteQuery::numberAlternativeRoutesChanged()
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteQuery30numberAlternativeRoutesChang'
        'edEv',
    )

  def travelModesChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteQuery::travelModesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#travelModesChanged
    """
    #  void QDeclarativeGeoRouteQuery::travelModesChanged()
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteQuery18travelModesChangedEv',
    )

  def routeOptimizationsChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteQuery::routeOptimizationsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html
    """
    #  void QDeclarativeGeoRouteQuery::routeOptimizationsChanged()
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteQuery25routeOptimizationsChangedEv',
    )

  def waypointsChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteQuery::waypointsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#waypointsChanged
    """
    #  void QDeclarativeGeoRouteQuery::waypointsChanged()
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteQuery16waypointsChangedEv',
    )

  def excludedAreasChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteQuery::excludedAreasChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html
    """
    #  void QDeclarativeGeoRouteQuery::excludedAreasChanged()
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteQuery20excludedAreasChangedEv',
    )

  def featureTypesChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteQuery::featureTypesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#featureTypesChanged
    """
    #  void QDeclarativeGeoRouteQuery::featureTypesChanged()
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteQuery19featureTypesChangedEv',
    )

  def maneuverDetailChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteQuery::maneuverDetailChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html
    """
    #  void QDeclarativeGeoRouteQuery::maneuverDetailChanged()
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteQuery21maneuverDetailChangedEv',
    )

  def segmentDetailChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteQuery::segmentDetailChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html
    """
    #  void QDeclarativeGeoRouteQuery::segmentDetailChanged()
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteQuery20segmentDetailChangedEv',
    )

  def queryDetailsChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteQuery::queryDetailsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#queryDetailsChanged
    """
    #  void QDeclarativeGeoRouteQuery::queryDetailsChanged()
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteQuery19queryDetailsChangedEv',
    )

  def departureTimeChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteQuery::departureTimeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html
    """
    #  void QDeclarativeGeoRouteQuery::departureTimeChanged()
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteQuery20departureTimeChangedEv',
    )

  def excludedAreaCoordinateChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoRouteQuery::excludedAreaCoordinateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html
    """
    #  void QDeclarativeGeoRouteQuery::excludedAreaCoordinateChanged()
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteQuery29excludedAreaCoordinateChange'
        'dEv',
    )

  def waypointChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteQuery::waypointChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#waypointChanged
    """
    #  void QDeclarativeGeoRouteQuery::waypointChanged()
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteQuery15waypointChangedEv',
    )

  def doCoordinateChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteQuery::doCoordinateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutequery.html#doCoordinateChanged
    """
    #  void QDeclarativeGeoRouteQuery::doCoordinateChanged()
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteQuery19doCoordinateChangedEv',
    )

  @staticmethod
  def featureTypes(*__, **_) -> Never:
    """
    Qt's 'QList<int> QDeclarativeGeoRouteQuery::featureTypes() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativeGeoRouteQuery.featureTypes' has no cute function yet. "
        "Qt's 'QList<int> QDeclarativeGeoRouteQuery::featureTypes() const': "
        "gives a type Python has no way to take yet.")
