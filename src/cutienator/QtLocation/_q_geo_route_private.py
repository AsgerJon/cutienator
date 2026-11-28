"""
QGeoRoutePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeoroute_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QGeoRoutePrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList, QMap, QSharedData
from . import QGeoRouteRequest

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QVariant
  from ..QtPositioning import QGeoCoordinate, QGeoRectangle
  from . import QGeoRoute, QGeoRouteSegment
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoCoordinate = WAIT['QGeoCoordinate']
  QGeoRectangle = WAIT['QGeoRectangle']
  QGeoRoute = WAIT['QGeoRoute']
  QGeoRouteSegment = WAIT['QGeoRouteSegment']
  QVariant = WAIT['QVariant']


class QGeoRoutePrivate(QSharedData):
  """
  The cute side of Qt's QGeoRoutePrivate: a plain Python object standing in
  front of one C++ QGeoRoutePrivate.

  It is built on the cute 'QSharedData', as Qt's QGeoRoutePrivate is built on
  Qt's QSharedData, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoRoutePrivate that has a ritual and that Python
  can call so far, 26 names in all: 'setId', 'id', 'setRequest', 'request',
  'setBounds', 'bounds', 'setTravelTime', 'travelTime', 'setDistance',
  'distance', 'setTravelMode', 'travelMode', 'setPath', 'path',
  'setFirstSegment', 'firstSegment', 'segmentsCount', 'segments',
  'setRouteLegs', 'routeLegs', 'setExtendedAttributes', 'extendedAttributes',
  'setLegIndex', 'legIndex', 'setContainingRoute', 'containingRoute'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QGeoRoutePrivate::operator==(const QGeoRoutePrivate &other)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'bool QGeoRoutePrivate::equals(const QGeoRoutePrivate &other)
    const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 29 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QGeoRoutePrivate is created at the first use, not by
    'QGeoRoutePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoRoutePrivate.
  - Each name of Qt's QGeoRoutePrivate that has no cute function yet,
    'equals', 'forEachSegment', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoRoutePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def id(self) -> str:
    """
    Calls Qt's 'QString QGeoRoutePrivate::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorouteprivate.html#id

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoRoutePrivate::id() const
    return self.uglySide.call('ritual_ZNK16QGeoRoutePrivate2idEv')

  def request(self) -> QGeoRouteRequest:
    """
    Calls Qt's 'QGeoRouteRequest QGeoRoutePrivate::request() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorouteprivate.html#request

    Returns
    -------

    QGeoRouteRequest
      A new cute QGeoRouteRequest around the copy Qt gave back. Python owns
      it.
    """
    #  QGeoRouteRequest QGeoRoutePrivate::request() const
    address = self.uglySide.call('ritual_ZNK16QGeoRoutePrivate7requestEv')
    return QGeoRouteRequest._cuteOwning(address)

  def bounds(self) -> QGeoRectangle:
    """
    Calls Qt's 'QGeoRectangle QGeoRoutePrivate::bounds() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorouteprivate.html#bounds

    Returns
    -------

    QGeoRectangle
      A new cute QGeoRectangle around the copy Qt gave back. Python owns it.
    """
    #  QGeoRectangle QGeoRoutePrivate::bounds() const
    address = self.uglySide.call('ritual_ZNK16QGeoRoutePrivate6boundsEv')
    from ..QtPositioning import QGeoRectangle
    return QGeoRectangle._cuteOwning(address)

  def travelTime(self) -> int:
    """
    Calls Qt's 'int QGeoRoutePrivate::travelTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorouteprivate.html#travelTime
    """
    #  int QGeoRoutePrivate::travelTime() const
    return self.uglySide.call('ritual_ZNK16QGeoRoutePrivate10travelTimeEv')

  def distance(self) -> float:
    """
    Calls Qt's 'qreal QGeoRoutePrivate::distance() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorouteprivate.html#distance
    """
    #  qreal QGeoRoutePrivate::distance() const
    return self.uglySide.call('ritual_ZNK16QGeoRoutePrivate8distanceEv')

  def travelMode(self) -> QGeoRouteRequest.TravelMode:
    """
    Calls Qt's 'QGeoRouteRequest::TravelMode QGeoRoutePrivate::travelMode()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorouteprivate.html#travelMode

    Returns
    -------

    QGeoRouteRequest.TravelMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QGeoRouteRequest.TravelMode(number)' gives.
    """
    #  QGeoRouteRequest::TravelMode QGeoRoutePrivate::travelMode() const
    return QGeoRouteRequest.TravelMode(self.uglySide.call(
        'ritual_ZNK16QGeoRoutePrivate10travelModeEv',
    ))

  def path(self) -> QList[QGeoCoordinate]:
    """
    Calls Qt's 'QList<QGeoCoordinate> QGeoRoutePrivate::path() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorouteprivate.html#path

    Returns
    -------

    QList[QGeoCoordinate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGeoCoordinate> QGeoRoutePrivate::path() const
    address = self.uglySide.call('ritual_ZNK16QGeoRoutePrivate4pathEv')
    from ..QtPositioning import QGeoCoordinate
    return QList[QGeoCoordinate]._cuteOwning(address)

  def firstSegment(self) -> QGeoRouteSegment:
    """
    Calls Qt's 'QGeoRouteSegment QGeoRoutePrivate::firstSegment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorouteprivate.html#firstSegment

    Returns
    -------

    QGeoRouteSegment
      A new cute QGeoRouteSegment around the copy Qt gave back. Python owns
      it.
    """
    #  QGeoRouteSegment QGeoRoutePrivate::firstSegment() const
    address = self.uglySide.call(
        'ritual_ZNK16QGeoRoutePrivate12firstSegmentEv',
    )
    from . import QGeoRouteSegment
    return QGeoRouteSegment._cuteOwning(address)

  def segmentsCount(self) -> int:
    """
    Calls Qt's 'int QGeoRoutePrivate::segmentsCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorouteprivate.html#segmentsCount
    """
    #  int QGeoRoutePrivate::segmentsCount() const
    return self.uglySide.call(
        'ritual_ZNK16QGeoRoutePrivate13segmentsCountEv',
    )

  def segments(self) -> QList[QGeoRouteSegment]:
    """
    Calls Qt's 'QList<QGeoRouteSegment> QGeoRoutePrivate::segments() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorouteprivate.html#segments

    Returns
    -------

    QList[QGeoRouteSegment]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGeoRouteSegment> QGeoRoutePrivate::segments() const
    address = self.uglySide.call('ritual_ZNK16QGeoRoutePrivate8segmentsEv')
    from . import QGeoRouteSegment
    return QList[QGeoRouteSegment]._cuteOwning(address)

  def routeLegs(self) -> QList[QGeoRoute]:
    """
    Calls Qt's 'QList<QGeoRoute> QGeoRoutePrivate::routeLegs() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorouteprivate.html#routeLegs

    Returns
    -------

    QList[QGeoRoute]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGeoRoute> QGeoRoutePrivate::routeLegs() const
    address = self.uglySide.call('ritual_ZNK16QGeoRoutePrivate9routeLegsEv')
    from . import QGeoRoute
    return QList[QGeoRoute]._cuteOwning(address)

  def extendedAttributes(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap QGeoRoutePrivate::extendedAttributes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorouteprivate.html#extendedAttributes

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap QGeoRoutePrivate::extendedAttributes() const
    address = self.uglySide.call(
        'ritual_ZNK16QGeoRoutePrivate18extendedAttributesEv',
    )
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  def legIndex(self) -> int:
    """
    Calls Qt's 'int QGeoRoutePrivate::legIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorouteprivate.html#legIndex
    """
    #  int QGeoRoutePrivate::legIndex() const
    return self.uglySide.call('ritual_ZNK16QGeoRoutePrivate8legIndexEv')

  def containingRoute(self) -> QGeoRoute:
    """
    Calls Qt's 'QGeoRoute QGeoRoutePrivate::containingRoute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorouteprivate.html#containingRoute

    Returns
    -------

    QGeoRoute
      A new cute QGeoRoute around the copy Qt gave back. Python owns it.
    """
    #  QGeoRoute QGeoRoutePrivate::containingRoute() const
    address = self.uglySide.call(
        'ritual_ZNK16QGeoRoutePrivate15containingRouteEv',
    )
    from . import QGeoRoute
    return QGeoRoute._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setId(self, id: str) -> None:
    """
    Calls Qt's 'void QGeoRoutePrivate::setId(const QString &id)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorouteprivate.html#setId

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGeoRoutePrivate::setId(const QString &id)
    self.uglySide.call('ritual_ZN16QGeoRoutePrivate5setIdERK7QString', id)

  @overload(QGeoRouteRequest)
  def setRequest(self, request: QGeoRouteRequest) -> None:
    """
    Calls Qt's 'void QGeoRoutePrivate::setRequest(const QGeoRouteRequest
    &request)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorouteprivate.html#setRequest

    Parameters
    ----------

    request : QGeoRouteRequest
      Passed on as a value: Qt reads the C++ QGeoRouteRequest, which stays
      Python's own.
    """
    #  void QGeoRoutePrivate::setRequest(const QGeoRouteRequest &request)
    self.uglySide.call(
        'ritual_ZN16QGeoRoutePrivate10setRequestERK16QGeoRouteRequest',
        self._valueOf(request),
    )

  @overload(QGeoRectangle)
  def setBounds(self, bounds: QGeoRectangle) -> None:
    """
    Calls Qt's 'void QGeoRoutePrivate::setBounds(const QGeoRectangle
    &bounds)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorouteprivate.html#setBounds

    Parameters
    ----------

    bounds : QGeoRectangle
      Passed on as a value: Qt reads the C++ QGeoRectangle, which stays
      Python's own.
    """
    #  void QGeoRoutePrivate::setBounds(const QGeoRectangle &bounds)
    self.uglySide.call(
        'ritual_ZN16QGeoRoutePrivate9setBoundsERK13QGeoRectangle',
        self._valueOf(bounds),
    )

  @overload(int)
  def setTravelTime(self, travelTime: int) -> None:
    """
    Calls Qt's 'void QGeoRoutePrivate::setTravelTime(int travelTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorouteprivate.html#setTravelTime

    Parameters
    ----------

    travelTime : int
      Passed on as it is.
    """
    #  void QGeoRoutePrivate::setTravelTime(int travelTime)
    self.uglySide.call(
        'ritual_ZN16QGeoRoutePrivate13setTravelTimeEi', travelTime,
    )

  @overload(float)
  def setDistance(self, distance: float) -> None:
    """
    Calls Qt's 'void QGeoRoutePrivate::setDistance(qreal distance)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorouteprivate.html#setDistance

    Parameters
    ----------

    distance : float
      Passed on as it is.
    """
    #  void QGeoRoutePrivate::setDistance(qreal distance)
    self.uglySide.call(
        'ritual_ZN16QGeoRoutePrivate11setDistanceEd', distance,
    )

  @overload(QGeoRouteRequest.TravelMode)
  def setTravelMode(self, mode: QGeoRouteRequest.TravelMode) -> None:
    """
    Calls Qt's 'void
    QGeoRoutePrivate::setTravelMode(QGeoRouteRequest::TravelMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorouteprivate.html#setTravelMode

    Parameters
    ----------

    mode : QGeoRouteRequest.TravelMode
      Passed on as its number.
    """
    #  void QGeoRoutePrivate::setTravelMode(QGeoRouteRequest::TravelMode
    #      mode)
    self.uglySide.call(
        'ritual_ZN16QGeoRoutePrivate13setTravelModeEN16QGeoRouteRequest10Tr'
        'avelModeE',
        mode.value,
    )

  @overload(QList[QGeoCoordinate])
  def setPath(self, path: QList[QGeoCoordinate]) -> None:
    """
    Calls Qt's 'void QGeoRoutePrivate::setPath(const QList<QGeoCoordinate>
    &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorouteprivate.html#setPath

    Parameters
    ----------

    path : QList[QGeoCoordinate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QGeoRoutePrivate::setPath(const QList<QGeoCoordinate> &path)
    self.uglySide.call(
        'ritual_ZN16QGeoRoutePrivate7setPathERK5QListI14QGeoCoordinateE',
        self._valueOf(path),
    )

  @overload(QGeoRouteSegment)
  def setFirstSegment(self, firstSegment: QGeoRouteSegment) -> None:
    """
    Calls Qt's 'void QGeoRoutePrivate::setFirstSegment(const QGeoRouteSegment
    &firstSegment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorouteprivate.html#setFirstSegment

    Parameters
    ----------

    firstSegment : QGeoRouteSegment
      Passed on as a value: Qt reads the C++ QGeoRouteSegment, which stays
      Python's own.
    """
    #  void QGeoRoutePrivate::setFirstSegment(const QGeoRouteSegment
    #      &firstSegment)
    self.uglySide.call(
        'ritual_ZN16QGeoRoutePrivate15setFirstSegmentERK16QGeoRouteSegment',
        self._valueOf(firstSegment),
    )

  @overload(QList[QGeoRoute])
  def setRouteLegs(self, legs: QList[QGeoRoute]) -> None:
    """
    Calls Qt's 'void QGeoRoutePrivate::setRouteLegs(const QList<QGeoRoute>
    &legs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorouteprivate.html#setRouteLegs

    Parameters
    ----------

    legs : QList[QGeoRoute]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QGeoRoutePrivate::setRouteLegs(const QList<QGeoRoute> &legs)
    self.uglySide.call(
        'ritual_ZN16QGeoRoutePrivate12setRouteLegsERK5QListI9QGeoRouteE',
        self._valueOf(legs),
    )

  @overload(QMap[str, QVariant])
  def setExtendedAttributes(
      self,
      extendedAttributes: QMap[str, QVariant],
  ) -> None:
    """
    Calls Qt's 'void QGeoRoutePrivate::setExtendedAttributes(const
    QVariantMap &extendedAttributes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorouteprivate.html#setExtendedAttributes

    Parameters
    ----------

    extendedAttributes : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QGeoRoutePrivate::setExtendedAttributes(const QVariantMap
    #      &extendedAttributes)
    self.uglySide.call(
        'ritual_ZN16QGeoRoutePrivate21setExtendedAttributesERK4QMapI7QStrin'
        'g8QVariantE',
        self._valueOf(extendedAttributes),
    )

  @overload(int)
  def setLegIndex(self, idx: int) -> None:
    """
    Calls Qt's 'void QGeoRoutePrivate::setLegIndex(int idx)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorouteprivate.html#setLegIndex

    Parameters
    ----------

    idx : int
      Passed on as it is.
    """
    #  void QGeoRoutePrivate::setLegIndex(int idx)
    self.uglySide.call('ritual_ZN16QGeoRoutePrivate11setLegIndexEi', idx)

  @overload(QGeoRoute)
  def setContainingRoute(self, route: QGeoRoute) -> None:
    """
    Calls Qt's 'void QGeoRoutePrivate::setContainingRoute(const QGeoRoute
    &route)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeorouteprivate.html#setContainingRoute

    Parameters
    ----------

    route : QGeoRoute
      Passed on as a value: Qt reads the C++ QGeoRoute, which stays Python's
      own.
    """
    #  void QGeoRoutePrivate::setContainingRoute(const QGeoRoute &route)
    self.uglySide.call(
        'ritual_ZN16QGeoRoutePrivate18setContainingRouteERK9QGeoRoute',
        self._valueOf(route),
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
  def equals(*__, **_) -> Never:
    """
    Qt's 'bool QGeoRoutePrivate::equals(const QGeoRoutePrivate &other)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoRoutePrivate.equals' has no cute function yet. Qt's 'bool "
        "QGeoRoutePrivate::equals(const QGeoRoutePrivate &other) const': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def forEachSegment(*__, **_) -> Never:
    """
    Qt's 'QGeoRoutePrivate::forEachSegment': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QGeoRoutePrivate.forEachSegment' has no cute function yet. Qt's "
        "'QGeoRoutePrivate::forEachSegment': a template: a pattern and no "
        "single function.")
