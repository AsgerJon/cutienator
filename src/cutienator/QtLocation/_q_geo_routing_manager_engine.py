"""
QGeoRoutingManagerEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qgeoroutingmanagerengine.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QLocale, QMap, QObject
from . import QGeoRouteReply, QGeoRouteRequest

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
  from ..QtPositioning import QGeoCoordinate
  from . import QGeoRoute
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoCoordinate = WAIT['QGeoCoordinate']
  QGeoRoute = WAIT['QGeoRoute']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeoRoutingManagerEngine(QObject):
  """
  The cute side of Qt's QGeoRoutingManagerEngine: a plain Python object
  standing in front of one C++ QGeoRoutingManagerEngine.

  It is built on the cute 'QObject', as Qt's QGeoRoutingManagerEngine is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoRoutingManagerEngine that has a ritual and that
  Python can call so far, 26 names in all: 'metaObject', 'tr', 'managerName',
  'managerVersion', 'calculateRoute', 'updateRoute', 'supportedTravelModes',
  'supportedFeatureTypes', 'supportedFeatureWeights',
  'supportedRouteOptimizations', 'supportedSegmentDetails',
  'supportedManeuverDetails', 'setLocale', 'locale', 'setMeasurementSystem',
  'measurementSystem', 'finished', 'errorOccurred',
  'setSupportedTravelModes', 'setSupportedFeatureTypes',
  'setSupportedFeatureWeights', 'setSupportedRouteOptimizations',
  'setSupportedSegmentDetails', 'setSupportedManeuverDetails',
  'setManagerName', 'setManagerVersion'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGeoRoutingManagerEngine::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QGeoRoutingManagerEngine::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QGeoRoutingManagerEngine::~QGeoRoutingManagerEngine()': the
    destructor: Python never removes a C++ QGeoRoutingManagerEngine.

  What has no ritual
  ------------------

  4 of the 34 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QGeoRoutingManagerEngine is created at the first use, not by
    'QGeoRoutingManagerEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoRoutingManagerEngine.
  - Qt tells when it has removed the C++ QGeoRoutingManagerEngine. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QGeoRoutingManagerEngine::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutingmanagerengine.html#tr

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
    #  QString QGeoRoutingManagerEngine::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QGeoRoutingManagerEngine2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoRoutingManagerEngine'

  #  A C++ QGeoRoutingManagerEngine Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoRoutingManagerEngine'

  #  The functions Qt calls itself that QGeoRoutingManagerEngine is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'calculateRoute': (
          ('_ZN24QGeoRoutingManagerEngine14calculateRouteERK16QGeoRouteRequ'
           'est',
           ('address', 'address', 'QtLocation:QGeoRouteReply'),
           (
               ('address', 'value', 'QtLocation:QGeoRouteRequest'),
           )),
      ),
      'updateRoute': (
          ('_ZN24QGeoRoutingManagerEngine11updateRouteERK9QGeoRouteRK14QGeo'
           'Coordinate',
           ('address', 'address', 'QtLocation:QGeoRouteReply'),
           (
               ('address', 'value', 'QtLocation:QGeoRoute'),
               ('address', 'value', 'QtPositioning:QGeoCoordinate'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGeoRoutingManagerEngine::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanagerengine.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGeoRoutingManagerEngine::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QGeoRoutingManagerEngine10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def managerName(self) -> str:
    """
    Calls Qt's 'QString QGeoRoutingManagerEngine::managerName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanagerengine.html#managerName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoRoutingManagerEngine::managerName() const
    return self.uglySide.call(
        'ritual_ZNK24QGeoRoutingManagerEngine11managerNameEv',
    )

  def managerVersion(self) -> int:
    """
    Calls Qt's 'int QGeoRoutingManagerEngine::managerVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanagerengine.html#managerVersion
    """
    #  int QGeoRoutingManagerEngine::managerVersion() const
    return self.uglySide.call(
        'ritual_ZNK24QGeoRoutingManagerEngine14managerVersionEv',
    )

  def supportedTravelModes(self) -> QGeoRouteRequest.TravelModes:
    """
    Calls Qt's 'QGeoRouteRequest::TravelModes
    QGeoRoutingManagerEngine::supportedTravelModes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanagerengine.html#supportedTravelModes

    Returns
    -------

    QGeoRouteRequest.TravelModes
      The value standing for the combination Qt gave back.
    """
    #  QGeoRouteRequest::TravelModes
    #      QGeoRoutingManagerEngine::supportedTravelModes() const
    return QGeoRouteRequest.TravelModes(self.uglySide.call(
        'ritual_ZNK24QGeoRoutingManagerEngine20supportedTravelModesEv',
    ))

  def supportedFeatureTypes(self) -> QGeoRouteRequest.FeatureTypes:
    """
    Calls Qt's 'QGeoRouteRequest::FeatureTypes
    QGeoRoutingManagerEngine::supportedFeatureTypes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanagerengine.html

    Returns
    -------

    QGeoRouteRequest.FeatureTypes
      The value standing for the combination Qt gave back.
    """
    #  QGeoRouteRequest::FeatureTypes
    #      QGeoRoutingManagerEngine::supportedFeatureTypes() const
    return QGeoRouteRequest.FeatureTypes(self.uglySide.call(
        'ritual_ZNK24QGeoRoutingManagerEngine21supportedFeatureTypesEv',
    ))

  def supportedFeatureWeights(self) -> QGeoRouteRequest.FeatureWeights:
    """
    Calls Qt's 'QGeoRouteRequest::FeatureWeights
    QGeoRoutingManagerEngine::supportedFeatureWeights() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanagerengine.html

    Returns
    -------

    QGeoRouteRequest.FeatureWeights
      The value standing for the combination Qt gave back.
    """
    #  QGeoRouteRequest::FeatureWeights
    #      QGeoRoutingManagerEngine::supportedFeatureWeights() const
    return QGeoRouteRequest.FeatureWeights(self.uglySide.call(
        'ritual_ZNK24QGeoRoutingManagerEngine23supportedFeatureWeightsEv',
    ))

  def supportedRouteOptimizations(
      self,
  ) -> QGeoRouteRequest.RouteOptimizations:
    """
    Calls Qt's 'QGeoRouteRequest::RouteOptimizations
    QGeoRoutingManagerEngine::supportedRouteOptimizations() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanagerengine.html

    Returns
    -------

    QGeoRouteRequest.RouteOptimizations
      The value standing for the combination Qt gave back.
    """
    #  QGeoRouteRequest::RouteOptimizations
    #      QGeoRoutingManagerEngine::supportedRouteOptimizations() const
    return QGeoRouteRequest.RouteOptimizations(self.uglySide.call(
        'ritual_ZNK24QGeoRoutingManagerEngine27supportedRouteOptimizationsE'
        'v',
    ))

  def supportedSegmentDetails(self) -> QGeoRouteRequest.SegmentDetails:
    """
    Calls Qt's 'QGeoRouteRequest::SegmentDetails
    QGeoRoutingManagerEngine::supportedSegmentDetails() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanagerengine.html

    Returns
    -------

    QGeoRouteRequest.SegmentDetails
      The value standing for the combination Qt gave back.
    """
    #  QGeoRouteRequest::SegmentDetails
    #      QGeoRoutingManagerEngine::supportedSegmentDetails() const
    return QGeoRouteRequest.SegmentDetails(self.uglySide.call(
        'ritual_ZNK24QGeoRoutingManagerEngine23supportedSegmentDetailsEv',
    ))

  def supportedManeuverDetails(self) -> QGeoRouteRequest.ManeuverDetails:
    """
    Calls Qt's 'QGeoRouteRequest::ManeuverDetails
    QGeoRoutingManagerEngine::supportedManeuverDetails() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanagerengine.html

    Returns
    -------

    QGeoRouteRequest.ManeuverDetails
      The value standing for the combination Qt gave back.
    """
    #  QGeoRouteRequest::ManeuverDetails
    #      QGeoRoutingManagerEngine::supportedManeuverDetails() const
    return QGeoRouteRequest.ManeuverDetails(self.uglySide.call(
        'ritual_ZNK24QGeoRoutingManagerEngine24supportedManeuverDetailsEv',
    ))

  def locale(self) -> QLocale:
    """
    Calls Qt's 'QLocale QGeoRoutingManagerEngine::locale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanagerengine.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QGeoRoutingManagerEngine::locale() const
    address = self.uglySide.call(
        'ritual_ZNK24QGeoRoutingManagerEngine6localeEv',
    )
    return QLocale._cuteOwning(address)

  def measurementSystem(self) -> QLocale.MeasurementSystem:
    """
    Calls Qt's 'QLocale::MeasurementSystem
    QGeoRoutingManagerEngine::measurementSystem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanagerengine.html#measurementSystem

    Returns
    -------

    QLocale.MeasurementSystem
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QLocale.MeasurementSystem(number)' gives.
    """
    #  QLocale::MeasurementSystem
    #      QGeoRoutingManagerEngine::measurementSystem() const
    return QLocale.MeasurementSystem(self.uglySide.call(
        'ritual_ZNK24QGeoRoutingManagerEngine17measurementSystemEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QLocale)
  def setLocale(self, locale: QLocale) -> None:
    """
    Calls Qt's 'void QGeoRoutingManagerEngine::setLocale(const QLocale
    &locale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanagerengine.html#setLocale

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QGeoRoutingManagerEngine::setLocale(const QLocale &locale)
    self.uglySide.call(
        'ritual_ZN24QGeoRoutingManagerEngine9setLocaleERK7QLocale',
        self._valueOf(locale),
    )

  @overload(QLocale.MeasurementSystem)
  def setMeasurementSystem(self, system: QLocale.MeasurementSystem) -> None:
    """
    Calls Qt's 'void
    QGeoRoutingManagerEngine::setMeasurementSystem(QLocale::MeasurementSystem
    system)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanagerengine.html#setMeasurementSystem

    Parameters
    ----------

    system : QLocale.MeasurementSystem
      Passed on as its number.
    """
    #  void QGeoRoutingManagerEngine::setMeasurementSystem(QLocale::
    #      MeasurementSystem system)
    self.uglySide.call(
        'ritual_ZN24QGeoRoutingManagerEngine20setMeasurementSystemEN7QLocal'
        'e17MeasurementSystemE',
        system.value,
    )

  @overload(QGeoRouteRequest.TravelModes)
  def setSupportedTravelModes(
      self,
      travelModes: QGeoRouteRequest.TravelModes,
  ) -> None:
    """
    Calls Qt's 'void
    QGeoRoutingManagerEngine::setSupportedTravelModes(QGeoRouteRequest::
    TravelModes travelModes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanagerengine.html

    Parameters
    ----------

    travelModes : QGeoRouteRequest.TravelModes
      Passed on as its number.
    """
    #  void QGeoRoutingManagerEngine::setSupportedTravelModes(
    #      QGeoRouteRequest::TravelModes travelModes)
    self.uglySide.call(
        'ritual_ZN24QGeoRoutingManagerEngine23setSupportedTravelModesE6QFla'
        'gsIN16QGeoRouteRequest10TravelModeEE',
        travelModes.value,
    )

  @overload(QGeoRouteRequest.FeatureTypes)
  def setSupportedFeatureTypes(
      self,
      featureTypes: QGeoRouteRequest.FeatureTypes,
  ) -> None:
    """
    Calls Qt's 'void
    QGeoRoutingManagerEngine::setSupportedFeatureTypes(QGeoRouteRequest::
    FeatureTypes featureTypes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanagerengine.html

    Parameters
    ----------

    featureTypes : QGeoRouteRequest.FeatureTypes
      Passed on as its number.
    """
    #  void QGeoRoutingManagerEngine::setSupportedFeatureTypes(
    #      QGeoRouteRequest::FeatureTypes featureTypes)
    self.uglySide.call(
        'ritual_ZN24QGeoRoutingManagerEngine24setSupportedFeatureTypesE6QFl'
        'agsIN16QGeoRouteRequest11FeatureTypeEE',
        featureTypes.value,
    )

  @overload(QGeoRouteRequest.FeatureWeights)
  def setSupportedFeatureWeights(
      self,
      featureWeights: QGeoRouteRequest.FeatureWeights,
  ) -> None:
    """
    Calls Qt's 'void
    QGeoRoutingManagerEngine::setSupportedFeatureWeights(QGeoRouteRequest::
    FeatureWeights featureWeights)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanagerengine.html

    Parameters
    ----------

    featureWeights : QGeoRouteRequest.FeatureWeights
      Passed on as its number.
    """
    #  void QGeoRoutingManagerEngine::setSupportedFeatureWeights(
    #      QGeoRouteRequest::FeatureWeights featureWeights)
    self.uglySide.call(
        'ritual_ZN24QGeoRoutingManagerEngine26setSupportedFeatureWeightsE6Q'
        'FlagsIN16QGeoRouteRequest13FeatureWeightEE',
        featureWeights.value,
    )

  @overload(QGeoRouteRequest.RouteOptimizations)
  def setSupportedRouteOptimizations(
      self,
      optimizations: QGeoRouteRequest.RouteOptimizations,
  ) -> None:
    """
    Calls Qt's 'void
    QGeoRoutingManagerEngine::setSupportedRouteOptimizations(
    QGeoRouteRequest::RouteOptimizations optimizations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanagerengine.html

    Parameters
    ----------

    optimizations : QGeoRouteRequest.RouteOptimizations
      Passed on as its number.
    """
    #  void QGeoRoutingManagerEngine::setSupportedRouteOptimizations(
    #      QGeoRouteRequest::RouteOptimizations optimizations)
    self.uglySide.call(
        'ritual_ZN24QGeoRoutingManagerEngine30setSupportedRouteOptimization'
        'sE6QFlagsIN16QGeoRouteRequest17RouteOptimizationEE',
        optimizations.value,
    )

  @overload(QGeoRouteRequest.SegmentDetails)
  def setSupportedSegmentDetails(
      self,
      segmentDetails: QGeoRouteRequest.SegmentDetails,
  ) -> None:
    """
    Calls Qt's 'void
    QGeoRoutingManagerEngine::setSupportedSegmentDetails(QGeoRouteRequest::
    SegmentDetails segmentDetails)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanagerengine.html

    Parameters
    ----------

    segmentDetails : QGeoRouteRequest.SegmentDetails
      Passed on as its number.
    """
    #  void QGeoRoutingManagerEngine::setSupportedSegmentDetails(
    #      QGeoRouteRequest::SegmentDetails segmentDetails)
    self.uglySide.call(
        'ritual_ZN24QGeoRoutingManagerEngine26setSupportedSegmentDetailsE6Q'
        'FlagsIN16QGeoRouteRequest13SegmentDetailEE',
        segmentDetails.value,
    )

  @overload(QGeoRouteRequest.ManeuverDetails)
  def setSupportedManeuverDetails(
      self,
      maneuverDetails: QGeoRouteRequest.ManeuverDetails,
  ) -> None:
    """
    Calls Qt's 'void
    QGeoRoutingManagerEngine::setSupportedManeuverDetails(QGeoRouteRequest::
    ManeuverDetails maneuverDetails)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanagerengine.html

    Parameters
    ----------

    maneuverDetails : QGeoRouteRequest.ManeuverDetails
      Passed on as its number.
    """
    #  void QGeoRoutingManagerEngine::setSupportedManeuverDetails(
    #      QGeoRouteRequest::ManeuverDetails maneuverDetails)
    self.uglySide.call(
        'ritual_ZN24QGeoRoutingManagerEngine27setSupportedManeuverDetailsE6'
        'QFlagsIN16QGeoRouteRequest14ManeuverDetailEE',
        maneuverDetails.value,
    )

  @overload(str)
  def setManagerName(self, managerName: str) -> None:
    """
    Calls Qt's 'void QGeoRoutingManagerEngine::setManagerName(const QString
    &managerName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanagerengine.html#setManagerName

    Parameters
    ----------

    managerName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGeoRoutingManagerEngine::setManagerName(const QString
    #      &managerName)
    self.uglySide.call(
        'ritual_ZN24QGeoRoutingManagerEngine14setManagerNameERK7QString',
        managerName,
    )

  @overload(int)
  def setManagerVersion(self, managerVersion: int) -> None:
    """
    Calls Qt's 'void QGeoRoutingManagerEngine::setManagerVersion(int
    managerVersion)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanagerengine.html#setManagerVersion

    Parameters
    ----------

    managerVersion : int
      Passed on as it is.
    """
    #  void QGeoRoutingManagerEngine::setManagerVersion(int managerVersion)
    self.uglySide.call(
        'ritual_ZN24QGeoRoutingManagerEngine17setManagerVersionEi',
        managerVersion,
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

  @overload(QMap[str, QVariant])
  @overload(QMap[str, QVariant], QObject)
  @overload(QMap[str, QVariant], NoneType)
  def __init__(
      self,
      parameters: QMap[str, QVariant],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGeoRoutingManagerEngine::QGeoRoutingManagerEngine(const QVariantMap
    &parameters, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanagerengine.html

    Parameters
    ----------

    parameters : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGeoRoutingManagerEngine::QGeoRoutingManagerEngine(const QVariantMap
    #      &parameters, QObject *parent)
    self._noteCreation(QGeoRoutingManagerEngine, lambda: Rituals.call(
        'ritual_ZN24QGeoRoutingManagerEngineC1ERK4QMapI7QString8QVariantEP7'
        'QObject',
        self._valueOf(parameters), self._addressOf(parent, 'QObject'),
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
    Calls Qt's 'QGeoRouteReply
    *QGeoRoutingManagerEngine::calculateRoute(const QGeoRouteRequest
    &request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanagerengine.html#calculateRoute

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
    #  QGeoRouteReply *QGeoRoutingManagerEngine::calculateRoute(const
    #      QGeoRouteRequest &request)
    address = self.uglySide.call(
        'ritual_ZN24QGeoRoutingManagerEngine14calculateRouteERK16QGeoRouteR'
        'equest',
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
    Calls Qt's 'QGeoRouteReply *QGeoRoutingManagerEngine::updateRoute(const
    QGeoRoute &route, const QGeoCoordinate &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanagerengine.html#updateRoute

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
    #  QGeoRouteReply *QGeoRoutingManagerEngine::updateRoute(const QGeoRoute
    #      &route, const QGeoCoordinate &position)
    ritual = (
        'ritual_ZN24QGeoRoutingManagerEngine11updateRouteERK9QGeoRouteRK14Q'
        'GeoCoordinate')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QGeoRoutingManagerEngine11updateRouteERK9QGeoRout'
          'eRK14QGeoCoordinate')
    address = self.uglySide.call(
        ritual, self._valueOf(route), self._valueOf(position),
    )
    return QGeoRouteReply._cuteAt(address)

  @overload(QGeoRouteReply)
  @overload(NoneType)
  def finished(self, reply: Optional[QGeoRouteReply]) -> None:
    """
    Calls Qt's 'void QGeoRoutingManagerEngine::finished(QGeoRouteReply
    *reply)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanagerengine.html#finished

    Parameters
    ----------

    reply : Optional[QGeoRouteReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGeoRoutingManagerEngine::finished(QGeoRouteReply *reply)
    self.uglySide.call(
        'ritual_ZN24QGeoRoutingManagerEngine8finishedEP14QGeoRouteReply',
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
    Calls Qt's 'void QGeoRoutingManagerEngine::errorOccurred(QGeoRouteReply
    *reply, QGeoRouteReply::Error error, const QString &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutingmanagerengine.html#errorOccurred

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
    #  void QGeoRoutingManagerEngine::errorOccurred(QGeoRouteReply *reply,
    #      QGeoRouteReply::Error error, const QString &errorString)
    self.uglySide.call(
        'ritual_ZN24QGeoRoutingManagerEngine13errorOccurredEP14QGeoRouteRep'
        'lyNS0_5ErrorERK7QString',
        self._addressOf(reply), error.value, errorString,
    )
