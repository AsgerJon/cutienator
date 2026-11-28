"""
QGeoServiceProvider binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qgeoserviceprovider.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QMap, QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QLocale, QMetaObject, QVariant
  from ..QtQml import QQmlEngine
  from . import QGeoCodingManager, QGeoMappingManager, QGeoRoutingManager
  from . import QPlaceManager
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLocale = WAIT['QLocale']
  QQmlEngine = WAIT['QQmlEngine']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeoServiceProvider(QObject):
  """
  The cute side of Qt's QGeoServiceProvider: a plain Python object standing
  in front of one C++ QGeoServiceProvider.

  It is built on the cute 'QObject', as Qt's QGeoServiceProvider is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoServiceProvider that has a ritual and that
  Python can call so far, 28 names in all: 'metaObject', 'tr',
  'availableServiceProviders', 'routingFeatures', 'geocodingFeatures',
  'mappingFeatures', 'placesFeatures', 'navigationFeatures',
  'geocodingManager', 'mappingManager', 'routingManager', 'placeManager',
  'error', 'errorString', 'mappingError', 'mappingErrorString',
  'geocodingError', 'geocodingErrorString', 'routingError',
  'routingErrorString', 'placesError', 'placesErrorString',
  'navigationError', 'navigationErrorString', 'setParameters', 'setLocale',
  'setAllowExperimental', 'setQmlEngine'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGeoServiceProvider::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QGeoServiceProvider::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QGeoServiceProvider::~QGeoServiceProvider()': the destructor:
    Python never removes a C++ QGeoServiceProvider.

  What has no ritual
  ------------------

  2 of the 34 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QGeoServiceProvider is created at the first use, not by
    'QGeoServiceProvider(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoServiceProvider.
  - Qt tells when it has removed the C++ QGeoServiceProvider. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QGeoServiceProvider, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Error(CuteNum):
    """
    The enum 'QGeoServiceProvider::Error' of Qt, with the 6 names Qt gives in
    it.
    """

    NoError = Kee[int](0)
    NotSupportedError = Kee[int](1)
    UnknownParameterError = Kee[int](2)
    MissingRequiredParameterError = Kee[int](3)
    ConnectionError = Kee[int](4)
    LoaderError = Kee[int](5)

  class GeocodingFeature(CuteFlags):
    """
    The flags enum 'QGeoServiceProvider::GeocodingFeature' of Qt, with the 6
    names Qt gives in it. Qt names the type of its combinations
    'QGeoServiceProvider::GeocodingFeatures'.
    """

    NoGeocodingFeatures = 0x0
    OnlineGeocodingFeature = 0x1
    OfflineGeocodingFeature = 0x2
    ReverseGeocodingFeature = 0x4
    LocalizedGeocodingFeature = 0x8
    AnyGeocodingFeatures = -1

  GeocodingFeatures = GeocodingFeature

  class MappingFeature(CuteFlags):
    """
    The flags enum 'QGeoServiceProvider::MappingFeature' of Qt, with the 5
    names Qt gives in it. Qt names the type of its combinations
    'QGeoServiceProvider::MappingFeatures'.
    """

    NoMappingFeatures = 0x0
    OnlineMappingFeature = 0x1
    OfflineMappingFeature = 0x2
    LocalizedMappingFeature = 0x4
    AnyMappingFeatures = -1

  MappingFeatures = MappingFeature

  class NavigationFeature(CuteFlags):
    """
    The flags enum 'QGeoServiceProvider::NavigationFeature' of Qt, with the 4
    names Qt gives in it. Qt names the type of its combinations
    'QGeoServiceProvider::NavigationFeatures'.
    """

    NoNavigationFeatures = 0x0
    OnlineNavigationFeature = 0x1
    OfflineNavigationFeature = 0x2
    AnyNavigationFeatures = -1

  NavigationFeatures = NavigationFeature

  class PlacesFeature(CuteFlags):
    """
    The flags enum 'QGeoServiceProvider::PlacesFeature' of Qt, with the 13
    names Qt gives in it. Qt names the type of its combinations
    'QGeoServiceProvider::PlacesFeatures'.
    """

    NoPlacesFeatures = 0x0
    OnlinePlacesFeature = 0x1
    OfflinePlacesFeature = 0x2
    SavePlaceFeature = 0x4
    RemovePlaceFeature = 0x8
    SaveCategoryFeature = 0x10
    RemoveCategoryFeature = 0x20
    PlaceRecommendationsFeature = 0x40
    SearchSuggestionsFeature = 0x80
    LocalizedPlacesFeature = 0x100
    NotificationsFeature = 0x200
    PlaceMatchingFeature = 0x400
    AnyPlacesFeatures = -1

  PlacesFeatures = PlacesFeature

  class RoutingFeature(CuteFlags):
    """
    The flags enum 'QGeoServiceProvider::RoutingFeature' of Qt, with the 8
    names Qt gives in it. Qt names the type of its combinations
    'QGeoServiceProvider::RoutingFeatures'.
    """

    NoRoutingFeatures = 0x0
    OnlineRoutingFeature = 0x1
    OfflineRoutingFeature = 0x2
    LocalizedRoutingFeature = 0x4
    RouteUpdatesFeature = 0x8
    AlternativeRoutesFeature = 0x10
    ExcludeAreasRoutingFeature = 0x20
    AnyRoutingFeatures = -1

  RoutingFeatures = RoutingFeature

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
    Calls Qt's 'QString QGeoServiceProvider::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoserviceprovider.html#tr

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
    #  QString QGeoServiceProvider::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QGeoServiceProvider2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def availableServiceProviders() -> QStringList:
    """
    Calls Qt's 'QStringList
    QGeoServiceProvider::availableServiceProviders()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoserviceprovider.html#availableServiceProviders

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QGeoServiceProvider::availableServiceProviders()
    address = Rituals.call(
        'ritual_ZN19QGeoServiceProvider25availableServiceProvidersEv',
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoServiceProvider'

  #  A C++ QGeoServiceProvider Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoServiceProvider'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGeoServiceProvider::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoserviceprovider.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGeoServiceProvider::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QGeoServiceProvider10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def routingFeatures(self) -> RoutingFeatures:
    """
    Calls Qt's 'RoutingFeatures QGeoServiceProvider::routingFeatures()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoserviceprovider.html#routingFeatures

    Returns
    -------

    RoutingFeatures
      The value standing for the combination Qt gave back.
    """
    #  RoutingFeatures QGeoServiceProvider::routingFeatures() const
    return QGeoServiceProvider.RoutingFeatures(self.uglySide.call(
        'ritual_ZNK19QGeoServiceProvider15routingFeaturesEv',
    ))

  def geocodingFeatures(self) -> GeocodingFeatures:
    """
    Calls Qt's 'GeocodingFeatures QGeoServiceProvider::geocodingFeatures()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoserviceprovider.html#geocodingFeatures

    Returns
    -------

    GeocodingFeatures
      The value standing for the combination Qt gave back.
    """
    #  GeocodingFeatures QGeoServiceProvider::geocodingFeatures() const
    return QGeoServiceProvider.GeocodingFeatures(self.uglySide.call(
        'ritual_ZNK19QGeoServiceProvider17geocodingFeaturesEv',
    ))

  def mappingFeatures(self) -> MappingFeatures:
    """
    Calls Qt's 'MappingFeatures QGeoServiceProvider::mappingFeatures()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoserviceprovider.html#mappingFeatures

    Returns
    -------

    MappingFeatures
      The value standing for the combination Qt gave back.
    """
    #  MappingFeatures QGeoServiceProvider::mappingFeatures() const
    return QGeoServiceProvider.MappingFeatures(self.uglySide.call(
        'ritual_ZNK19QGeoServiceProvider15mappingFeaturesEv',
    ))

  def placesFeatures(self) -> PlacesFeatures:
    """
    Calls Qt's 'PlacesFeatures QGeoServiceProvider::placesFeatures() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoserviceprovider.html#placesFeatures

    Returns
    -------

    PlacesFeatures
      The value standing for the combination Qt gave back.
    """
    #  PlacesFeatures QGeoServiceProvider::placesFeatures() const
    return QGeoServiceProvider.PlacesFeatures(self.uglySide.call(
        'ritual_ZNK19QGeoServiceProvider14placesFeaturesEv',
    ))

  def navigationFeatures(self) -> NavigationFeatures:
    """
    Calls Qt's 'NavigationFeatures QGeoServiceProvider::navigationFeatures()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoserviceprovider.html#navigationFeatures

    Returns
    -------

    NavigationFeatures
      The value standing for the combination Qt gave back.
    """
    #  NavigationFeatures QGeoServiceProvider::navigationFeatures() const
    return QGeoServiceProvider.NavigationFeatures(self.uglySide.call(
        'ritual_ZNK19QGeoServiceProvider18navigationFeaturesEv',
    ))

  def geocodingManager(self) -> Optional[QGeoCodingManager]:
    """
    Calls Qt's 'QGeoCodingManager *QGeoServiceProvider::geocodingManager()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoserviceprovider.html#geocodingManager

    Returns
    -------

    Optional[QGeoCodingManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoCodingManager *QGeoServiceProvider::geocodingManager() const
    address = self.uglySide.call(
        'ritual_ZNK19QGeoServiceProvider16geocodingManagerEv',
    )
    from . import QGeoCodingManager
    return QGeoCodingManager._cuteAt(address)

  def mappingManager(self) -> Optional[QGeoMappingManager]:
    """
    Calls Qt's 'QGeoMappingManager *QGeoServiceProvider::mappingManager()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoserviceprovider.html#mappingManager

    Returns
    -------

    Optional[QGeoMappingManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoMappingManager *QGeoServiceProvider::mappingManager() const
    address = self.uglySide.call(
        'ritual_ZNK19QGeoServiceProvider14mappingManagerEv',
    )
    from . import QGeoMappingManager
    return QGeoMappingManager._cuteAt(address)

  def routingManager(self) -> Optional[QGeoRoutingManager]:
    """
    Calls Qt's 'QGeoRoutingManager *QGeoServiceProvider::routingManager()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoserviceprovider.html#routingManager

    Returns
    -------

    Optional[QGeoRoutingManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoRoutingManager *QGeoServiceProvider::routingManager() const
    address = self.uglySide.call(
        'ritual_ZNK19QGeoServiceProvider14routingManagerEv',
    )
    from . import QGeoRoutingManager
    return QGeoRoutingManager._cuteAt(address)

  def placeManager(self) -> Optional[QPlaceManager]:
    """
    Calls Qt's 'QPlaceManager *QGeoServiceProvider::placeManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoserviceprovider.html#placeManager

    Returns
    -------

    Optional[QPlaceManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlaceManager *QGeoServiceProvider::placeManager() const
    address = self.uglySide.call(
        'ritual_ZNK19QGeoServiceProvider12placeManagerEv',
    )
    from . import QPlaceManager
    return QPlaceManager._cuteAt(address)

  def error(self) -> Error:
    """
    Calls Qt's 'Error QGeoServiceProvider::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoserviceprovider.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QGeoServiceProvider::error() const
    return QGeoServiceProvider.Error(self.uglySide.call(
        'ritual_ZNK19QGeoServiceProvider5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QGeoServiceProvider::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoserviceprovider.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoServiceProvider::errorString() const
    return self.uglySide.call(
        'ritual_ZNK19QGeoServiceProvider11errorStringEv',
    )

  def mappingError(self) -> Error:
    """
    Calls Qt's 'Error QGeoServiceProvider::mappingError() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoserviceprovider.html#mappingError

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QGeoServiceProvider::mappingError() const
    return QGeoServiceProvider.Error(self.uglySide.call(
        'ritual_ZNK19QGeoServiceProvider12mappingErrorEv',
    ))

  def mappingErrorString(self) -> str:
    """
    Calls Qt's 'QString QGeoServiceProvider::mappingErrorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoserviceprovider.html#mappingErrorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoServiceProvider::mappingErrorString() const
    return self.uglySide.call(
        'ritual_ZNK19QGeoServiceProvider18mappingErrorStringEv',
    )

  def geocodingError(self) -> Error:
    """
    Calls Qt's 'Error QGeoServiceProvider::geocodingError() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoserviceprovider.html#geocodingError

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QGeoServiceProvider::geocodingError() const
    return QGeoServiceProvider.Error(self.uglySide.call(
        'ritual_ZNK19QGeoServiceProvider14geocodingErrorEv',
    ))

  def geocodingErrorString(self) -> str:
    """
    Calls Qt's 'QString QGeoServiceProvider::geocodingErrorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoserviceprovider.html#geocodingErrorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoServiceProvider::geocodingErrorString() const
    return self.uglySide.call(
        'ritual_ZNK19QGeoServiceProvider20geocodingErrorStringEv',
    )

  def routingError(self) -> Error:
    """
    Calls Qt's 'Error QGeoServiceProvider::routingError() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoserviceprovider.html#routingError

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QGeoServiceProvider::routingError() const
    return QGeoServiceProvider.Error(self.uglySide.call(
        'ritual_ZNK19QGeoServiceProvider12routingErrorEv',
    ))

  def routingErrorString(self) -> str:
    """
    Calls Qt's 'QString QGeoServiceProvider::routingErrorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoserviceprovider.html#routingErrorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoServiceProvider::routingErrorString() const
    return self.uglySide.call(
        'ritual_ZNK19QGeoServiceProvider18routingErrorStringEv',
    )

  def placesError(self) -> Error:
    """
    Calls Qt's 'Error QGeoServiceProvider::placesError() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoserviceprovider.html#placesError

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QGeoServiceProvider::placesError() const
    return QGeoServiceProvider.Error(self.uglySide.call(
        'ritual_ZNK19QGeoServiceProvider11placesErrorEv',
    ))

  def placesErrorString(self) -> str:
    """
    Calls Qt's 'QString QGeoServiceProvider::placesErrorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoserviceprovider.html#placesErrorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoServiceProvider::placesErrorString() const
    return self.uglySide.call(
        'ritual_ZNK19QGeoServiceProvider17placesErrorStringEv',
    )

  def navigationError(self) -> Error:
    """
    Calls Qt's 'Error QGeoServiceProvider::navigationError() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoserviceprovider.html#navigationError

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QGeoServiceProvider::navigationError() const
    return QGeoServiceProvider.Error(self.uglySide.call(
        'ritual_ZNK19QGeoServiceProvider15navigationErrorEv',
    ))

  def navigationErrorString(self) -> str:
    """
    Calls Qt's 'QString QGeoServiceProvider::navigationErrorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoserviceprovider.html#navigationErrorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoServiceProvider::navigationErrorString() const
    return self.uglySide.call(
        'ritual_ZNK19QGeoServiceProvider21navigationErrorStringEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMap[str, QVariant])
  def setParameters(self, parameters: QMap[str, QVariant]) -> None:
    """
    Calls Qt's 'void QGeoServiceProvider::setParameters(const QVariantMap
    &parameters)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoserviceprovider.html#setParameters

    Parameters
    ----------

    parameters : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QGeoServiceProvider::setParameters(const QVariantMap &parameters)
    self.uglySide.call(
        'ritual_ZN19QGeoServiceProvider13setParametersERK4QMapI7QString8QVa'
        'riantE',
        self._valueOf(parameters),
    )

  @overload(QLocale)
  def setLocale(self, locale: QLocale) -> None:
    """
    Calls Qt's 'void QGeoServiceProvider::setLocale(const QLocale &locale)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoserviceprovider.html#setLocale

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QGeoServiceProvider::setLocale(const QLocale &locale)
    self.uglySide.call(
        'ritual_ZN19QGeoServiceProvider9setLocaleERK7QLocale',
        self._valueOf(locale),
    )

  @overload(bool)
  def setAllowExperimental(self, allow: bool) -> None:
    """
    Calls Qt's 'void QGeoServiceProvider::setAllowExperimental(bool allow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoserviceprovider.html#setAllowExperimental

    Parameters
    ----------

    allow : bool
      Passed on as it is.
    """
    #  void QGeoServiceProvider::setAllowExperimental(bool allow)
    self.uglySide.call(
        'ritual_ZN19QGeoServiceProvider20setAllowExperimentalEb', allow,
    )

  @overload(QQmlEngine)
  @overload(NoneType)
  def setQmlEngine(self, engine: Optional[QQmlEngine]) -> None:
    """
    Calls Qt's 'void QGeoServiceProvider::setQmlEngine(QQmlEngine *engine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoserviceprovider.html#setQmlEngine

    Parameters
    ----------

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGeoServiceProvider::setQmlEngine(QQmlEngine *engine)
    self.uglySide.call(
        'ritual_ZN19QGeoServiceProvider12setQmlEngineEP10QQmlEngine',
        self._addressOf(engine),
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

  @overload(str, QMap[str, QVariant])
  @overload(str, QMap[str, QVariant], bool)
  def __init__(
      self,
      providerName: str,
      parameters: QMap[str, QVariant],
      allowExperimental: bool = False,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGeoServiceProvider::QGeoServiceProvider(const QString &providerName,
    const QVariantMap &parameters, bool allowExperimental)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoserviceprovider.html#QGeoServiceProvider

    Parameters
    ----------

    providerName : str
      Passed on as it is: a QString is made of it for the call.

    parameters : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    allowExperimental : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  QGeoServiceProvider::QGeoServiceProvider(const QString &providerName,
    #      const QVariantMap &parameters, bool allowExperimental)
    self._noteCreation(QGeoServiceProvider, lambda: Rituals.call(
        'ritual_ZN19QGeoServiceProviderC1ERK7QStringRK4QMapIS0_8QVariantEb',
        providerName, self._valueOf(parameters), allowExperimental,
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
