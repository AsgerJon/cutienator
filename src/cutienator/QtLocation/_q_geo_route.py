"""
QGeoRoute binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qgeoroute.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QMap
from . import QGeoRouteRequest

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QVariant
  from ..QtPositioning import QGeoCoordinate, QGeoRectangle
  from . import QGeoRouteSegment
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoCoordinate = WAIT['QGeoCoordinate']
  QGeoRectangle = WAIT['QGeoRectangle']
  QGeoRouteSegment = WAIT['QGeoRouteSegment']
  QVariant = WAIT['QVariant']


class QGeoRoute(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGeoRoute: a plain Python object standing in front of
  one C++ QGeoRoute.

  C++ hands a QGeoRoute around as a copy, so every C++ QGeoRoute behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGeoRoute that has a ritual and that Python can call
  so far, 29 names in all: '__eq__', '__ne__', 'setRouteId', 'routeId',
  'setRequest', 'request', 'setBounds', 'bounds', 'setFirstRouteSegment',
  'firstRouteSegment', 'segmentsCount', 'segments', 'setTravelTime',
  'travelTime', 'setDistance', 'distance', 'setTravelMode', 'travelMode',
  'setPath', 'path', 'setRouteLegs', 'routeLegs', 'setExtendedAttributes',
  'extendedAttributes', 'setLegIndex', 'legIndex', 'setOverallRoute',
  'overallRoute', 'isEqual'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoRoute::QGeoRoute(QGeoRoute &&other)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QGeoRoute::~QGeoRoute()': the destructor: Python removes its C++
    QGeoRoute by it, and has no other use for it.
  - Qt's 'QGeoRoute &QGeoRoute::operator=(const QGeoRoute &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QGeoRoute &QGeoRoute::operator=(QGeoRoute &&other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'void QGeoRoute::swap(QGeoRoute &other)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QExplicitlySharedDataPointer<QGeoRoutePrivate> &QGeoRoute::d()':
    gives a type Python has no way to take yet.
  - Qt's 'const QExplicitlySharedDataPointer<QGeoRoutePrivate>
    &QGeoRoute::const_d() const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  3 of the 41 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QGeoRoute is created at the first use, not by 'QGeoRoute(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoRoute back gives a copy the ritual made for
    Python, in a new cute QGeoRoute.
  - Each name of Qt's QGeoRoute that has no cute function yet, 'const_d',
    'd', 'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoRoute'

  #  Qt's '~QGeoRoute()'. Naming it makes this a value class: Python owns
  #  every C++ QGeoRoute behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QGeoRouteD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def routeId(self) -> str:
    """
    Calls Qt's 'QString QGeoRoute::routeId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroute.html#routeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoRoute::routeId() const
    return self.uglySide.call('ritual_ZNK9QGeoRoute7routeIdEv')

  def request(self) -> QGeoRouteRequest:
    """
    Calls Qt's 'QGeoRouteRequest QGeoRoute::request() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroute.html#request

    Returns
    -------

    QGeoRouteRequest
      A new cute QGeoRouteRequest around the copy Qt gave back. Python owns
      it.
    """
    #  QGeoRouteRequest QGeoRoute::request() const
    address = self.uglySide.call('ritual_ZNK9QGeoRoute7requestEv')
    return QGeoRouteRequest._cuteOwning(address)

  def bounds(self) -> QGeoRectangle:
    """
    Calls Qt's 'QGeoRectangle QGeoRoute::bounds() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroute.html#bounds

    Returns
    -------

    QGeoRectangle
      A new cute QGeoRectangle around the copy Qt gave back. Python owns it.
    """
    #  QGeoRectangle QGeoRoute::bounds() const
    address = self.uglySide.call('ritual_ZNK9QGeoRoute6boundsEv')
    from ..QtPositioning import QGeoRectangle
    return QGeoRectangle._cuteOwning(address)

  def firstRouteSegment(self) -> QGeoRouteSegment:
    """
    Calls Qt's 'QGeoRouteSegment QGeoRoute::firstRouteSegment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroute.html#firstRouteSegment

    Returns
    -------

    QGeoRouteSegment
      A new cute QGeoRouteSegment around the copy Qt gave back. Python owns
      it.
    """
    #  QGeoRouteSegment QGeoRoute::firstRouteSegment() const
    address = self.uglySide.call('ritual_ZNK9QGeoRoute17firstRouteSegmentEv')
    from . import QGeoRouteSegment
    return QGeoRouteSegment._cuteOwning(address)

  def segmentsCount(self) -> int:
    """
    Calls Qt's 'qsizetype QGeoRoute::segmentsCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroute.html#segmentsCount
    """
    #  qsizetype QGeoRoute::segmentsCount() const
    return self.uglySide.call('ritual_ZNK9QGeoRoute13segmentsCountEv')

  def segments(self) -> QList[QGeoRouteSegment]:
    """
    Calls Qt's 'QList<QGeoRouteSegment> QGeoRoute::segments() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroute.html#segments

    Returns
    -------

    QList[QGeoRouteSegment]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGeoRouteSegment> QGeoRoute::segments() const
    address = self.uglySide.call('ritual_ZNK9QGeoRoute8segmentsEv')
    from . import QGeoRouteSegment
    return QList[QGeoRouteSegment]._cuteOwning(address)

  def travelTime(self) -> int:
    """
    Calls Qt's 'int QGeoRoute::travelTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroute.html#travelTime
    """
    #  int QGeoRoute::travelTime() const
    return self.uglySide.call('ritual_ZNK9QGeoRoute10travelTimeEv')

  def distance(self) -> float:
    """
    Calls Qt's 'qreal QGeoRoute::distance() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroute.html#distance
    """
    #  qreal QGeoRoute::distance() const
    return self.uglySide.call('ritual_ZNK9QGeoRoute8distanceEv')

  def travelMode(self) -> QGeoRouteRequest.TravelMode:
    """
    Calls Qt's 'QGeoRouteRequest::TravelMode QGeoRoute::travelMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroute.html#travelMode

    Returns
    -------

    QGeoRouteRequest.TravelMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QGeoRouteRequest.TravelMode(number)' gives.
    """
    #  QGeoRouteRequest::TravelMode QGeoRoute::travelMode() const
    return QGeoRouteRequest.TravelMode(self.uglySide.call(
        'ritual_ZNK9QGeoRoute10travelModeEv',
    ))

  def path(self) -> QList[QGeoCoordinate]:
    """
    Calls Qt's 'QList<QGeoCoordinate> QGeoRoute::path() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroute.html#path

    Returns
    -------

    QList[QGeoCoordinate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGeoCoordinate> QGeoRoute::path() const
    address = self.uglySide.call('ritual_ZNK9QGeoRoute4pathEv')
    from ..QtPositioning import QGeoCoordinate
    return QList[QGeoCoordinate]._cuteOwning(address)

  def routeLegs(self) -> QList[QGeoRoute]:
    """
    Calls Qt's 'QList<QGeoRoute> QGeoRoute::routeLegs() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroute.html#routeLegs

    Returns
    -------

    QList[QGeoRoute]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGeoRoute> QGeoRoute::routeLegs() const
    address = self.uglySide.call('ritual_ZNK9QGeoRoute9routeLegsEv')
    return QList[QGeoRoute]._cuteOwning(address)

  def extendedAttributes(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap QGeoRoute::extendedAttributes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroute.html#extendedAttributes

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap QGeoRoute::extendedAttributes() const
    address = self.uglySide.call(
        'ritual_ZNK9QGeoRoute18extendedAttributesEv',
    )
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  def legIndex(self) -> int:
    """
    Calls Qt's 'int QGeoRoute::legIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroute.html#legIndex
    """
    #  int QGeoRoute::legIndex() const
    return self.uglySide.call('ritual_ZNK9QGeoRoute8legIndexEv')

  def overallRoute(self) -> QGeoRoute:
    """
    Calls Qt's 'QGeoRoute QGeoRoute::overallRoute() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroute.html#overallRoute

    Returns
    -------

    QGeoRoute
      A new cute QGeoRoute around the copy Qt gave back. Python owns it.
    """
    #  QGeoRoute QGeoRoute::overallRoute() const
    address = self.uglySide.call('ritual_ZNK9QGeoRoute12overallRouteEv')
    return QGeoRoute._cuteOwning(address)

  @overload(THIS)
  def isEqual(self, other: QGeoRoute) -> bool:
    """
    Calls Qt's 'bool QGeoRoute::isEqual(const QGeoRoute &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroute.html#isEqual

    Parameters
    ----------

    other : QGeoRoute
      Passed on as a value: Qt reads the C++ QGeoRoute, which stays Python's
      own.
    """
    #  bool QGeoRoute::isEqual(const QGeoRoute &other) const
    return self.uglySide.call(
        'ritual_ZNK9QGeoRoute7isEqualERKS_', self._valueOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setRouteId(self, id: str) -> None:
    """
    Calls Qt's 'void QGeoRoute::setRouteId(const QString &id)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroute.html#setRouteId

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGeoRoute::setRouteId(const QString &id)
    self.uglySide.call('ritual_ZN9QGeoRoute10setRouteIdERK7QString', id)

  @overload(QGeoRouteRequest)
  def setRequest(self, request: QGeoRouteRequest) -> None:
    """
    Calls Qt's 'void QGeoRoute::setRequest(const QGeoRouteRequest &request)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroute.html#setRequest

    Parameters
    ----------

    request : QGeoRouteRequest
      Passed on as a value: Qt reads the C++ QGeoRouteRequest, which stays
      Python's own.
    """
    #  void QGeoRoute::setRequest(const QGeoRouteRequest &request)
    self.uglySide.call(
        'ritual_ZN9QGeoRoute10setRequestERK16QGeoRouteRequest',
        self._valueOf(request),
    )

  @overload(QGeoRectangle)
  def setBounds(self, bounds: QGeoRectangle) -> None:
    """
    Calls Qt's 'void QGeoRoute::setBounds(const QGeoRectangle &bounds)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroute.html#setBounds

    Parameters
    ----------

    bounds : QGeoRectangle
      Passed on as a value: Qt reads the C++ QGeoRectangle, which stays
      Python's own.
    """
    #  void QGeoRoute::setBounds(const QGeoRectangle &bounds)
    self.uglySide.call(
        'ritual_ZN9QGeoRoute9setBoundsERK13QGeoRectangle',
        self._valueOf(bounds),
    )

  @overload(QGeoRouteSegment)
  def setFirstRouteSegment(self, routeSegment: QGeoRouteSegment) -> None:
    """
    Calls Qt's 'void QGeoRoute::setFirstRouteSegment(const QGeoRouteSegment
    &routeSegment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroute.html#setFirstRouteSegment

    Parameters
    ----------

    routeSegment : QGeoRouteSegment
      Passed on as a value: Qt reads the C++ QGeoRouteSegment, which stays
      Python's own.
    """
    #  void QGeoRoute::setFirstRouteSegment(const QGeoRouteSegment
    #      &routeSegment)
    self.uglySide.call(
        'ritual_ZN9QGeoRoute20setFirstRouteSegmentERK16QGeoRouteSegment',
        self._valueOf(routeSegment),
    )

  @overload(int)
  def setTravelTime(self, secs: int) -> None:
    """
    Calls Qt's 'void QGeoRoute::setTravelTime(int secs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroute.html#setTravelTime

    Parameters
    ----------

    secs : int
      Passed on as it is.
    """
    #  void QGeoRoute::setTravelTime(int secs)
    self.uglySide.call('ritual_ZN9QGeoRoute13setTravelTimeEi', secs)

  @overload(float)
  def setDistance(self, distance: float) -> None:
    """
    Calls Qt's 'void QGeoRoute::setDistance(qreal distance)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroute.html#setDistance

    Parameters
    ----------

    distance : float
      Passed on as it is.
    """
    #  void QGeoRoute::setDistance(qreal distance)
    self.uglySide.call('ritual_ZN9QGeoRoute11setDistanceEd', distance)

  @overload(QGeoRouteRequest.TravelMode)
  def setTravelMode(self, mode: QGeoRouteRequest.TravelMode) -> None:
    """
    Calls Qt's 'void QGeoRoute::setTravelMode(QGeoRouteRequest::TravelMode
    mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroute.html#setTravelMode

    Parameters
    ----------

    mode : QGeoRouteRequest.TravelMode
      Passed on as its number.
    """
    #  void QGeoRoute::setTravelMode(QGeoRouteRequest::TravelMode mode)
    self.uglySide.call(
        'ritual_ZN9QGeoRoute13setTravelModeEN16QGeoRouteRequest10TravelMode'
        'E',
        mode.value,
    )

  @overload(QList[QGeoCoordinate])
  def setPath(self, path: QList[QGeoCoordinate]) -> None:
    """
    Calls Qt's 'void QGeoRoute::setPath(const QList<QGeoCoordinate> &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroute.html#setPath

    Parameters
    ----------

    path : QList[QGeoCoordinate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QGeoRoute::setPath(const QList<QGeoCoordinate> &path)
    self.uglySide.call(
        'ritual_ZN9QGeoRoute7setPathERK5QListI14QGeoCoordinateE',
        self._valueOf(path),
    )

  @overload(QList[WAIT['QGeoRoute']])
  def setRouteLegs(self, legs: QList[QGeoRoute]) -> None:
    """
    Calls Qt's 'void QGeoRoute::setRouteLegs(const QList<QGeoRoute> &legs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroute.html#setRouteLegs

    Parameters
    ----------

    legs : QList[QGeoRoute]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QGeoRoute::setRouteLegs(const QList<QGeoRoute> &legs)
    self.uglySide.call(
        'ritual_ZN9QGeoRoute12setRouteLegsERK5QListIS_E',
        self._valueOf(legs),
    )

  @overload(QMap[str, QVariant])
  def setExtendedAttributes(
      self,
      extendedAttributes: QMap[str, QVariant],
  ) -> None:
    """
    Calls Qt's 'void QGeoRoute::setExtendedAttributes(const QVariantMap
    &extendedAttributes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroute.html#setExtendedAttributes

    Parameters
    ----------

    extendedAttributes : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QGeoRoute::setExtendedAttributes(const QVariantMap
    #      &extendedAttributes)
    self.uglySide.call(
        'ritual_ZN9QGeoRoute21setExtendedAttributesERK4QMapI7QString8QVaria'
        'ntE',
        self._valueOf(extendedAttributes),
    )

  @overload(int)
  def setLegIndex(self, idx: int) -> None:
    """
    Calls Qt's 'void QGeoRoute::setLegIndex(int idx)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroute.html#setLegIndex

    Parameters
    ----------

    idx : int
      Passed on as it is.
    """
    #  void QGeoRoute::setLegIndex(int idx)
    self.uglySide.call('ritual_ZN9QGeoRoute11setLegIndexEi', idx)

  @overload(THIS)
  def setOverallRoute(self, route: QGeoRoute) -> None:
    """
    Calls Qt's 'void QGeoRoute::setOverallRoute(const QGeoRoute &route)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroute.html#setOverallRoute

    Parameters
    ----------

    route : QGeoRoute
      Passed on as a value: Qt reads the C++ QGeoRoute, which stays Python's
      own.
    """
    #  void QGeoRoute::setOverallRoute(const QGeoRoute &route)
    self.uglySide.call(
        'ritual_ZN9QGeoRoute15setOverallRouteERKS_', self._valueOf(route),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QGeoRoute) -> bool:
    """
    Calls Qt's 'bool operator==(const QGeoRoute &lhs, const QGeoRoute &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroute.html#operator==

    Parameters
    ----------

    rhs : QGeoRoute
      Passed on as a value: Qt reads the C++ QGeoRoute, which stays Python's
      own.
    """
    #  bool operator==(const QGeoRoute &lhs, const QGeoRoute &rhs)
    return Rituals.call(
        'ritual_ZeqRK9QGeoRouteS1_',
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
  def __ne__(self, rhs: QGeoRoute) -> bool:
    """
    Calls Qt's 'bool operator!=(const QGeoRoute &lhs, const QGeoRoute &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroute.html#operator!=

    Parameters
    ----------

    rhs : QGeoRoute
      Passed on as a value: Qt reads the C++ QGeoRoute, which stays Python's
      own.
    """
    #  bool operator!=(const QGeoRoute &lhs, const QGeoRoute &rhs)
    return Rituals.call(
        'ritual_ZneRK9QGeoRouteS1_',
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
    Notes what was given, for Qt's 'QGeoRoute::QGeoRoute()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroute.html#QGeoRoute
    """
    #  QGeoRoute::QGeoRoute()
    self._noteCreation(QGeoRoute, lambda: Rituals.call(
        'ritual_ZN9QGeoRouteC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QGeoRoute) -> None:
    """
    Notes what was given, for Qt's 'QGeoRoute::QGeoRoute(const QGeoRoute
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroute.html#QGeoRoute

    Parameters
    ----------

    other : QGeoRoute
      Passed on as a value: Qt reads the C++ QGeoRoute, which stays Python's
      own.
    """
    #  QGeoRoute::QGeoRoute(const QGeoRoute &other)
    self._noteCreation(QGeoRoute, lambda: Rituals.call(
        'ritual_ZN9QGeoRouteC1ERKS_', self._valueOf(other),
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
  def const_d(*__, **_) -> Never:
    """
    Qt's 'const QExplicitlySharedDataPointer<QGeoRoutePrivate>
    &QGeoRoute::const_d() const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGeoRoute.const_d' has no cute function yet. Qt's 'const "
        "QExplicitlySharedDataPointer<QGeoRoutePrivate> "
        "&QGeoRoute::const_d() const': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def d(*__, **_) -> Never:
    """
    Qt's 'QExplicitlySharedDataPointer<QGeoRoutePrivate> &QGeoRoute::d()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGeoRoute.d' has no cute function yet. Qt's "
        "'QExplicitlySharedDataPointer<QGeoRoutePrivate> &QGeoRoute::d()': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QGeoRoute::swap(QGeoRoute &other)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoRoute.swap' has no cute function yet. Qt's 'void "
        "QGeoRoute::swap(QGeoRoute &other)': takes a type Python has no way "
        "to hand over yet.")


#  Qt's 'QList<QGeoRoute>': the list of QGeoRoute, which 'QList[QGeoRoute]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QGeoRoute.
QList.createKind(
    QGeoRoute, 'value',
    make='ritual_list_make_QGeoRoute',
    add='ritual_list_add_QGeoRoute',
    size='ritual_list_size_QGeoRoute',
    at='ritual_list_at_QGeoRoute',
    drop='ritual_list_drop_QGeoRoute',
)
