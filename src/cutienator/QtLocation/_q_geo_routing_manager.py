"""
QGeoRoutingManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qgeoroutingmanager.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QLocale, QObject
from . import QGeoRouteReply, QGeoRouteRequest

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtPositioning import QGeoCoordinate
  from . import QGeoRoute, QGeoRoutingManagerEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoCoordinate = WAIT['QGeoCoordinate']
  QGeoRoute = WAIT['QGeoRoute']
  QGeoRoutingManagerEngine = WAIT['QGeoRoutingManagerEngine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeoRoutingManager(QObject):
  """
  The cute side of Qt's QGeoRoutingManager: a plain Python object standing in
  front of one C++ QGeoRoutingManager.

  It is built on the cute 'QObject', as Qt's QGeoRoutingManager is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoRoutingManager that has a ritual and that Python
  can call so far, 18 names in all: 'metaObject', 'tr', 'managerName',
  'managerVersion', 'calculateRoute', 'updateRoute', 'supportedTravelModes',
  'supportedFeatureTypes', 'supportedFeatureWeights',
  'supportedRouteOptimizations', 'supportedSegmentDetails',
  'supportedManeuverDetails', 'setLocale', 'locale', 'setMeasurementSystem',
  'measurementSystem', 'finished', 'errorOccurred'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGeoRoutingManager::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QGeoRoutingManager::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QGeoRoutingManager::~QGeoRoutingManager()': the destructor: Python
    never removes a C++ QGeoRoutingManager.

  What has no ritual
  ------------------

  4 of the 26 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QGeoRoutingManager is created at the first use, not by
    'QGeoRoutingManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoRoutingManager.
  - Qt tells when it has removed the C++ QGeoRoutingManager. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

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
    Calls Qt's 'QString QGeoRoutingManager::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutingmanager.html#tr

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
    #  QString QGeoRoutingManager::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QGeoRoutingManager2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoRoutingManager'

  #  A C++ QGeoRoutingManager Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoRoutingManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGeoRoutingManager::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutingmanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGeoRoutingManager::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QGeoRoutingManager10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def managerName(self) -> str:
    """
    Calls Qt's 'QString QGeoRoutingManager::managerName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanager.html#managerName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoRoutingManager::managerName() const
    return self.uglySide.call(
        'ritual_ZNK18QGeoRoutingManager11managerNameEv',
    )

  def managerVersion(self) -> int:
    """
    Calls Qt's 'int QGeoRoutingManager::managerVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanager.html#managerVersion
    """
    #  int QGeoRoutingManager::managerVersion() const
    return self.uglySide.call(
        'ritual_ZNK18QGeoRoutingManager14managerVersionEv',
    )

  def supportedTravelModes(self) -> QGeoRouteRequest.TravelModes:
    """
    Calls Qt's 'QGeoRouteRequest::TravelModes
    QGeoRoutingManager::supportedTravelModes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanager.html#supportedTravelModes

    Returns
    -------

    QGeoRouteRequest.TravelModes
      The value standing for the combination Qt gave back.
    """
    #  QGeoRouteRequest::TravelModes
    #      QGeoRoutingManager::supportedTravelModes() const
    return QGeoRouteRequest.TravelModes(self.uglySide.call(
        'ritual_ZNK18QGeoRoutingManager20supportedTravelModesEv',
    ))

  def supportedFeatureTypes(self) -> QGeoRouteRequest.FeatureTypes:
    """
    Calls Qt's 'QGeoRouteRequest::FeatureTypes
    QGeoRoutingManager::supportedFeatureTypes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanager.html#supportedFeatureTypes

    Returns
    -------

    QGeoRouteRequest.FeatureTypes
      The value standing for the combination Qt gave back.
    """
    #  QGeoRouteRequest::FeatureTypes
    #      QGeoRoutingManager::supportedFeatureTypes() const
    return QGeoRouteRequest.FeatureTypes(self.uglySide.call(
        'ritual_ZNK18QGeoRoutingManager21supportedFeatureTypesEv',
    ))

  def supportedFeatureWeights(self) -> QGeoRouteRequest.FeatureWeights:
    """
    Calls Qt's 'QGeoRouteRequest::FeatureWeights
    QGeoRoutingManager::supportedFeatureWeights() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanager.html#supportedFeatureWeights

    Returns
    -------

    QGeoRouteRequest.FeatureWeights
      The value standing for the combination Qt gave back.
    """
    #  QGeoRouteRequest::FeatureWeights
    #      QGeoRoutingManager::supportedFeatureWeights() const
    return QGeoRouteRequest.FeatureWeights(self.uglySide.call(
        'ritual_ZNK18QGeoRoutingManager23supportedFeatureWeightsEv',
    ))

  def supportedRouteOptimizations(
      self,
  ) -> QGeoRouteRequest.RouteOptimizations:
    """
    Calls Qt's 'QGeoRouteRequest::RouteOptimizations
    QGeoRoutingManager::supportedRouteOptimizations() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanager.html

    Returns
    -------

    QGeoRouteRequest.RouteOptimizations
      The value standing for the combination Qt gave back.
    """
    #  QGeoRouteRequest::RouteOptimizations
    #      QGeoRoutingManager::supportedRouteOptimizations() const
    return QGeoRouteRequest.RouteOptimizations(self.uglySide.call(
        'ritual_ZNK18QGeoRoutingManager27supportedRouteOptimizationsEv',
    ))

  def supportedSegmentDetails(self) -> QGeoRouteRequest.SegmentDetails:
    """
    Calls Qt's 'QGeoRouteRequest::SegmentDetails
    QGeoRoutingManager::supportedSegmentDetails() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanager.html#supportedSegmentDetails

    Returns
    -------

    QGeoRouteRequest.SegmentDetails
      The value standing for the combination Qt gave back.
    """
    #  QGeoRouteRequest::SegmentDetails
    #      QGeoRoutingManager::supportedSegmentDetails() const
    return QGeoRouteRequest.SegmentDetails(self.uglySide.call(
        'ritual_ZNK18QGeoRoutingManager23supportedSegmentDetailsEv',
    ))

  def supportedManeuverDetails(self) -> QGeoRouteRequest.ManeuverDetails:
    """
    Calls Qt's 'QGeoRouteRequest::ManeuverDetails
    QGeoRoutingManager::supportedManeuverDetails() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanager.html#supportedManeuverDetails

    Returns
    -------

    QGeoRouteRequest.ManeuverDetails
      The value standing for the combination Qt gave back.
    """
    #  QGeoRouteRequest::ManeuverDetails
    #      QGeoRoutingManager::supportedManeuverDetails() const
    return QGeoRouteRequest.ManeuverDetails(self.uglySide.call(
        'ritual_ZNK18QGeoRoutingManager24supportedManeuverDetailsEv',
    ))

  def locale(self) -> QLocale:
    """
    Calls Qt's 'QLocale QGeoRoutingManager::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutingmanager.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QGeoRoutingManager::locale() const
    address = self.uglySide.call('ritual_ZNK18QGeoRoutingManager6localeEv')
    return QLocale._cuteOwning(address)

  def measurementSystem(self) -> QLocale.MeasurementSystem:
    """
    Calls Qt's 'QLocale::MeasurementSystem
    QGeoRoutingManager::measurementSystem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanager.html#measurementSystem

    Returns
    -------

    QLocale.MeasurementSystem
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QLocale.MeasurementSystem(number)' gives.
    """
    #  QLocale::MeasurementSystem QGeoRoutingManager::measurementSystem()
    #      const
    return QLocale.MeasurementSystem(self.uglySide.call(
        'ritual_ZNK18QGeoRoutingManager17measurementSystemEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QLocale)
  def setLocale(self, locale: QLocale) -> None:
    """
    Calls Qt's 'void QGeoRoutingManager::setLocale(const QLocale &locale)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutingmanager.html#setLocale

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QGeoRoutingManager::setLocale(const QLocale &locale)
    self.uglySide.call(
        'ritual_ZN18QGeoRoutingManager9setLocaleERK7QLocale',
        self._valueOf(locale),
    )

  @overload(QLocale.MeasurementSystem)
  def setMeasurementSystem(self, system: QLocale.MeasurementSystem) -> None:
    """
    Calls Qt's 'void
    QGeoRoutingManager::setMeasurementSystem(QLocale::MeasurementSystem
    system)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanager.html#setMeasurementSystem

    Parameters
    ----------

    system : QLocale.MeasurementSystem
      Passed on as its number.
    """
    #  void QGeoRoutingManager::setMeasurementSystem(QLocale::
    #      MeasurementSystem system)
    self.uglySide.call(
        'ritual_ZN18QGeoRoutingManager20setMeasurementSystemEN7QLocale17Mea'
        'surementSystemE',
        system.value,
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

  @overload(QGeoRoutingManagerEngine)
  @overload(NoneType)
  @overload(QGeoRoutingManagerEngine, QObject)
  @overload(QGeoRoutingManagerEngine, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      engine: Optional[QGeoRoutingManagerEngine],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGeoRoutingManager::QGeoRoutingManager(QGeoRoutingManagerEngine *engine,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanager.html#QGeoRoutingManager

    Parameters
    ----------

    engine : Optional[QGeoRoutingManagerEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGeoRoutingManager::QGeoRoutingManager(QGeoRoutingManagerEngine
    #      *engine, QObject *parent)
    self._noteCreation(QGeoRoutingManager, lambda: Rituals.call(
        'ritual_ZN18QGeoRoutingManagerC1EP24QGeoRoutingManagerEngineP7QObje'
        'ct',
        self._addressOf(engine), self._addressOf(parent, 'QObject'),
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

  @overload(QGeoRouteRequest)
  def calculateRoute(
      self,
      request: QGeoRouteRequest,
  ) -> Optional[QGeoRouteReply]:
    """
    Calls Qt's 'QGeoRouteReply *QGeoRoutingManager::calculateRoute(const
    QGeoRouteRequest &request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanager.html#calculateRoute

    Parameters
    ----------

    request : QGeoRouteRequest
      Passed on as a value: Qt reads the C++ QGeoRouteRequest, which stays
      Python's own.

    Returns
    -------

    Optional[QGeoRouteReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoRouteReply *QGeoRoutingManager::calculateRoute(const
    #      QGeoRouteRequest &request)
    address = self.uglySide.call(
        'ritual_ZN18QGeoRoutingManager14calculateRouteERK16QGeoRouteRequest',
        self._valueOf(request),
    )
    return QGeoRouteReply._cuteAt(address)

  @overload(QGeoRoute, QGeoCoordinate)
  def updateRoute(
      self,
      route: QGeoRoute,
      position: QGeoCoordinate,
  ) -> Optional[QGeoRouteReply]:
    """
    Calls Qt's 'QGeoRouteReply *QGeoRoutingManager::updateRoute(const
    QGeoRoute &route, const QGeoCoordinate &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanager.html#updateRoute

    Parameters
    ----------

    route : QGeoRoute
      Passed on as a value: Qt reads the C++ QGeoRoute, which stays Python's
      own.

    position : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.

    Returns
    -------

    Optional[QGeoRouteReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoRouteReply *QGeoRoutingManager::updateRoute(const QGeoRoute
    #      &route, const QGeoCoordinate &position)
    address = self.uglySide.call(
        'ritual_ZN18QGeoRoutingManager11updateRouteERK9QGeoRouteRK14QGeoCoo'
        'rdinate',
        self._valueOf(route), self._valueOf(position),
    )
    return QGeoRouteReply._cuteAt(address)

  @overload(QGeoRouteReply)
  @overload(NoneType)
  def finished(self, reply: Optional[QGeoRouteReply]) -> None:
    """
    Calls Qt's 'void QGeoRoutingManager::finished(QGeoRouteReply *reply)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutingmanager.html#finished

    Parameters
    ----------

    reply : Optional[QGeoRouteReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGeoRoutingManager::finished(QGeoRouteReply *reply)
    self.uglySide.call(
        'ritual_ZN18QGeoRoutingManager8finishedEP14QGeoRouteReply',
        self._addressOf(reply),
    )

  @overload(QGeoRouteReply, QGeoRouteReply.Error)
  @overload(NoneType, QGeoRouteReply.Error)
  @overload(QGeoRouteReply, QGeoRouteReply.Error, str)
  @overload(NoneType, QGeoRouteReply.Error, str)
  def errorOccurred(
      self,
      reply: Optional[QGeoRouteReply],
      error: QGeoRouteReply.Error,
      errorString: str = '',
  ) -> None:
    """
    Calls Qt's 'void QGeoRoutingManager::errorOccurred(QGeoRouteReply *reply,
    QGeoRouteReply::Error error, const QString &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanager.html#errorOccurred

    Parameters
    ----------

    reply : Optional[QGeoRouteReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    error : QGeoRouteReply.Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QGeoRoutingManager::errorOccurred(QGeoRouteReply *reply,
    #      QGeoRouteReply::Error error, const QString &errorString)
    self.uglySide.call(
        'ritual_ZN18QGeoRoutingManager13errorOccurredEP14QGeoRouteReplyNS0_'
        '5ErrorERK7QString',
        self._addressOf(reply), error.value, errorString,
    )
