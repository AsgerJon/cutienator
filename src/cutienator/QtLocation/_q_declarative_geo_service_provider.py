"""
QDeclarativeGeoServiceProvider binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qdeclarativegeoserviceprovider_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativeGeoServiceProvider to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from ..QtCore import QMap, QObject, QStringList
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from . import QDeclarativeGeoServiceProviderRequirements
  from . import QGeoServiceProvider
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeclarativeGeoServiceProviderRequirements = WAIT['QDeclarativeGeoServiceProviderRequirements']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDeclarativeGeoServiceProvider(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QDeclarativeGeoServiceProvider: a plain Python object
  standing in front of one C++ QDeclarativeGeoServiceProvider.

  It is built on the cute 'QObject', as Qt's QDeclarativeGeoServiceProvider
  is built on Qt's QObject, and has everything that class has. It is built on
  the cute 'QQmlParserStatus' as well, as Qt's QDeclarativeGeoServiceProvider
  is built on Qt's QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativeGeoServiceProvider that has a ritual and
  that Python can call so far, 25 names in all: 'metaObject', 'tr',
  'classBegin', 'componentComplete', 'setName', 'name', 'parameterMap',
  'availableServiceProviders', 'requirements', 'setRequirements',
  'preferred', 'setPreferred', 'sharedGeoServiceProvider', 'locales',
  'setLocales', 'isAttached', 'setAllowExperimental', 'allowExperimental',
  'nameChanged', 'localesChanged', 'attached', 'preferredChanged',
  'allowExperimentalChanged', 'parametersReady', 'tryAttach'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDeclarativeGeoServiceProvider::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QDeclarativeGeoServiceProvider::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDeclarativeGeoServiceProvider::~QDeclarativeGeoServiceProvider()':
    the destructor: Python never removes a C++
    QDeclarativeGeoServiceProvider.
  - Qt's 'QQmlListProperty<QDeclarativePluginParameter>
    QDeclarativeGeoServiceProvider::parameters()': gives a type Python has no
    way to take yet.
  - Qt's 'bool QDeclarativeGeoServiceProvider::supportsRouting(const
    RoutingFeatures &feature) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'bool QDeclarativeGeoServiceProvider::supportsGeocoding(const
    GeocodingFeatures &feature) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'bool QDeclarativeGeoServiceProvider::supportsMapping(const
    MappingFeatures &feature) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'bool QDeclarativeGeoServiceProvider::supportsPlaces(const
    PlacesFeatures &feature) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'bool QDeclarativeGeoServiceProvider::supportsNavigation(const
    NavigationFeature &feature) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QDeclarativeGeoServiceProvider::parameter_append(
    QQmlListProperty<QDeclarativePluginParameter> *prop,
    QDeclarativePluginParameter *mapObject)': names
    'QQmlListProperty<QDeclarativePluginParameter>', which has no cute class
    yet.
  - Qt's 'qsizetype QDeclarativeGeoServiceProvider::parameter_count(
    QQmlListProperty<QDeclarativePluginParameter> *prop)': names
    'QQmlListProperty<QDeclarativePluginParameter>', which has no cute class
    yet.
  - Qt's 'QDeclarativePluginParameter
    *QDeclarativeGeoServiceProvider::parameter_at(
    QQmlListProperty<QDeclarativePluginParameter> *prop, qsizetype index)':
    names 'QQmlListProperty<QDeclarativePluginParameter>', which has no cute
    class yet.
  - Qt's 'void QDeclarativeGeoServiceProvider::parameter_clear(
    QQmlListProperty<QDeclarativePluginParameter> *prop)': names
    'QQmlListProperty<QDeclarativePluginParameter>', which has no cute class
    yet.

  What has no ritual
  ------------------

  4 of the 43 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QDeclarativeGeoServiceProvider is created at the first use, not
    by 'QDeclarativeGeoServiceProvider(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativeGeoServiceProvider.
  - Qt tells when it has removed the C++ QDeclarativeGeoServiceProvider.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDeclarativeGeoServiceProvider that has no cute
    function yet, 'parameter_append', 'parameter_at', 'parameter_clear',
    'parameter_count', 'parameters', 'supportsGeocoding', 'supportsMapping',
    'supportsNavigation', 'supportsPlaces', 'supportsRouting', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QDeclarativeGeoServiceProvider, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class GeocodingFeature(CuteFlags):
    """
    The flags enum 'QDeclarativeGeoServiceProvider::GeocodingFeature' of Qt,
    with the 6 names Qt gives in it. Qt names the type of its combinations
    'QDeclarativeGeoServiceProvider::GeocodingFeatures'.
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
    The flags enum 'QDeclarativeGeoServiceProvider::MappingFeature' of Qt,
    with the 5 names Qt gives in it. Qt names the type of its combinations
    'QDeclarativeGeoServiceProvider::MappingFeatures'.
    """

    NoMappingFeatures = 0x0
    OnlineMappingFeature = 0x1
    OfflineMappingFeature = 0x2
    LocalizedMappingFeature = 0x4
    AnyMappingFeatures = -1

  MappingFeatures = MappingFeature

  class NavigationFeature(CuteFlags):
    """
    The flags enum 'QDeclarativeGeoServiceProvider::NavigationFeature' of Qt,
    with the 4 names Qt gives in it. Qt names the type of its combinations
    'QDeclarativeGeoServiceProvider::NavigationFeatures'.
    """

    NoNavigationFeatures = 0x0
    OnlineNavigationFeature = 0x1
    OfflineNavigationFeature = 0x2
    AnyNavigationFeatures = -1

  NavigationFeatures = NavigationFeature

  class PlacesFeature(CuteFlags):
    """
    The flags enum 'QDeclarativeGeoServiceProvider::PlacesFeature' of Qt,
    with the 13 names Qt gives in it. Qt names the type of its combinations
    'QDeclarativeGeoServiceProvider::PlacesFeatures'.
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
    The flags enum 'QDeclarativeGeoServiceProvider::RoutingFeature' of Qt,
    with the 8 names Qt gives in it. Qt names the type of its combinations
    'QDeclarativeGeoServiceProvider::RoutingFeatures'.
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
    Calls Qt's 'QString QDeclarativeGeoServiceProvider::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceprovider.html#tr

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
    #  QString QDeclarativeGeoServiceProvider::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN30QDeclarativeGeoServiceProvider2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativeGeoServiceProvider'

  #  Qt's QDeclarativeGeoServiceProvider is built on more than one class. The
  #  part of a C++ QDeclarativeGeoServiceProvider that belongs to a class
  #  after the first begins somewhere inside the object, and the ritual named
  #  for that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus':
          'ritual_cast_QDeclarativeGeoServiceProvider_QQmlParserStatus',
  }

  #  A C++ QDeclarativeGeoServiceProvider Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativeGeoServiceProvider'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QDeclarativeGeoServiceProvider::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceprovider.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDeclarativeGeoServiceProvider::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK30QDeclarativeGeoServiceProvider10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QDeclarativeGeoServiceProvider::name() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceprovider.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativeGeoServiceProvider::name() const
    return self.uglySide.call(
        'ritual_ZNK30QDeclarativeGeoServiceProvider4nameEv',
    )

  def parameterMap(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap QDeclarativeGeoServiceProvider::parameterMap()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceprovider.html#parameterMap

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap QDeclarativeGeoServiceProvider::parameterMap() const
    address = self.uglySide.call(
        'ritual_ZNK30QDeclarativeGeoServiceProvider12parameterMapEv',
    )
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  def requirements(
      self,
  ) -> Optional[QDeclarativeGeoServiceProviderRequirements]:
    """
    Calls Qt's 'QDeclarativeGeoServiceProviderRequirements
    *QDeclarativeGeoServiceProvider::requirements() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceprovider.html#requirements

    Returns
    -------

    Optional[QDeclarativeGeoServiceProviderRequirements]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDeclarativeGeoServiceProviderRequirements
    #      *QDeclarativeGeoServiceProvider::requirements() const
    address = self.uglySide.call(
        'ritual_ZNK30QDeclarativeGeoServiceProvider12requirementsEv',
    )
    from . import QDeclarativeGeoServiceProviderRequirements
    return QDeclarativeGeoServiceProviderRequirements._cuteAt(address)

  def preferred(self) -> QStringList:
    """
    Calls Qt's 'QStringList QDeclarativeGeoServiceProvider::preferred()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceprovider.html#preferred

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QDeclarativeGeoServiceProvider::preferred() const
    address = self.uglySide.call(
        'ritual_ZNK30QDeclarativeGeoServiceProvider9preferredEv',
    )
    return QStringList._cuteOwning(address)

  def sharedGeoServiceProvider(self) -> Optional[QGeoServiceProvider]:
    """
    Calls Qt's 'QGeoServiceProvider
    *QDeclarativeGeoServiceProvider::sharedGeoServiceProvider() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceprovider.html

    Returns
    -------

    Optional[QGeoServiceProvider]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoServiceProvider
    #      *QDeclarativeGeoServiceProvider::sharedGeoServiceProvider() const
    address = self.uglySide.call(
        'ritual_ZNK30QDeclarativeGeoServiceProvider24sharedGeoServiceProvid'
        'erEv',
    )
    from . import QGeoServiceProvider
    return QGeoServiceProvider._cuteAt(address)

  def locales(self) -> QStringList:
    """
    Calls Qt's 'QStringList QDeclarativeGeoServiceProvider::locales() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceprovider.html#locales

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QDeclarativeGeoServiceProvider::locales() const
    address = self.uglySide.call(
        'ritual_ZNK30QDeclarativeGeoServiceProvider7localesEv',
    )
    return QStringList._cuteOwning(address)

  def isAttached(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativeGeoServiceProvider::isAttached() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceprovider.html#isAttached
    """
    #  bool QDeclarativeGeoServiceProvider::isAttached() const
    return self.uglySide.call(
        'ritual_ZNK30QDeclarativeGeoServiceProvider10isAttachedEv',
    )

  def allowExperimental(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativeGeoServiceProvider::allowExperimental()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceprovider.html
    """
    #  bool QDeclarativeGeoServiceProvider::allowExperimental() const
    return self.uglySide.call(
        'ritual_ZNK30QDeclarativeGeoServiceProvider17allowExperimentalEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoServiceProvider::setName(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceprovider.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeGeoServiceProvider::setName(const QString &name)
    self.uglySide.call(
        'ritual_ZN30QDeclarativeGeoServiceProvider7setNameERK7QString', name,
    )

  @overload(QDeclarativeGeoServiceProviderRequirements)
  @overload(NoneType)
  def setRequirements(
      self,
      req: Optional[QDeclarativeGeoServiceProviderRequirements],
  ) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoServiceProvider::setRequirements(
    QDeclarativeGeoServiceProviderRequirements *req)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceprovider.html

    Parameters
    ----------

    req : Optional[QDeclarativeGeoServiceProviderRequirements]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeGeoServiceProvider::setRequirements(
    #      QDeclarativeGeoServiceProviderRequirements *req)
    self.uglySide.call(
        'ritual_ZN30QDeclarativeGeoServiceProvider15setRequirementsEP42QDec'
        'larativeGeoServiceProviderRequirements',
        self._addressOf(req),
    )

  @overload(QStringList)
  def setPreferred(self, val: QStringList) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoServiceProvider::setPreferred(const
    QStringList &val)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceprovider.html#setPreferred

    Parameters
    ----------

    val : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDeclarativeGeoServiceProvider::setPreferred(const QStringList
    #      &val)
    self.uglySide.call(
        'ritual_ZN30QDeclarativeGeoServiceProvider12setPreferredERK5QListI7'
        'QStringE',
        self._valueOf(val),
    )

  @overload(QStringList)
  def setLocales(self, locales: QStringList) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoServiceProvider::setLocales(const
    QStringList &locales)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceprovider.html#setLocales

    Parameters
    ----------

    locales : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDeclarativeGeoServiceProvider::setLocales(const QStringList
    #      &locales)
    self.uglySide.call(
        'ritual_ZN30QDeclarativeGeoServiceProvider10setLocalesERK5QListI7QS'
        'tringE',
        self._valueOf(locales),
    )

  @overload(bool)
  def setAllowExperimental(self, allow: bool) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoServiceProvider::setAllowExperimental(bool allow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceprovider.html

    Parameters
    ----------

    allow : bool
      Passed on as it is.
    """
    #  void QDeclarativeGeoServiceProvider::setAllowExperimental(bool allow)
    self.uglySide.call(
        'ritual_ZN30QDeclarativeGeoServiceProvider20setAllowExperimentalEb',
        allow,
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
    'QDeclarativeGeoServiceProvider::QDeclarativeGeoServiceProvider(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceprovider.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDeclarativeGeoServiceProvider::QDeclarativeGeoServiceProvider(QObject
    #      *parent)
    self._noteCreation(QDeclarativeGeoServiceProvider, lambda: Rituals.call(
        'ritual_ZN30QDeclarativeGeoServiceProviderC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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
    Calls Qt's 'void QDeclarativeGeoServiceProvider::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceprovider.html#classBegin
    """
    #  void QDeclarativeGeoServiceProvider::classBegin()
    ritual = 'ritual_ZN30QDeclarativeGeoServiceProvider10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN30QDeclarativeGeoServiceProvider10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoServiceProvider::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceprovider.html
    """
    #  void QDeclarativeGeoServiceProvider::componentComplete()
    ritual = 'ritual_ZN30QDeclarativeGeoServiceProvider17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QDeclarativeGeoServiceProvider17componentComplete'
          'Ev')
    self.uglySide.call(ritual)

  def availableServiceProviders(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    QDeclarativeGeoServiceProvider::availableServiceProviders()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceprovider.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList
    #      QDeclarativeGeoServiceProvider::availableServiceProviders()
    address = self.uglySide.call(
        'ritual_ZN30QDeclarativeGeoServiceProvider25availableServiceProvide'
        'rsEv',
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def nameChanged(self, name: str) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoServiceProvider::nameChanged(const
    QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceprovider.html#nameChanged

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeGeoServiceProvider::nameChanged(const QString &name)
    self.uglySide.call(
        'ritual_ZN30QDeclarativeGeoServiceProvider11nameChangedERK7QString',
        name,
    )

  def localesChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoServiceProvider::localesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceprovider.html#localesChanged
    """
    #  void QDeclarativeGeoServiceProvider::localesChanged()
    self.uglySide.call(
        'ritual_ZN30QDeclarativeGeoServiceProvider14localesChangedEv',
    )

  def attached(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoServiceProvider::attached()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceprovider.html#attached
    """
    #  void QDeclarativeGeoServiceProvider::attached()
    self.uglySide.call(
        'ritual_ZN30QDeclarativeGeoServiceProvider8attachedEv',
    )

  @overload(QStringList)
  def preferredChanged(self, preferences: QStringList) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoServiceProvider::preferredChanged(const
    QStringList &preferences)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceprovider.html

    Parameters
    ----------

    preferences : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDeclarativeGeoServiceProvider::preferredChanged(const
    #      QStringList &preferences)
    self.uglySide.call(
        'ritual_ZN30QDeclarativeGeoServiceProvider16preferredChangedERK5QLi'
        'stI7QStringE',
        self._valueOf(preferences),
    )

  @overload(bool)
  def allowExperimentalChanged(self, allow: bool) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoServiceProvider::allowExperimentalChanged(bool allow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceprovider.html

    Parameters
    ----------

    allow : bool
      Passed on as it is.
    """
    #  void QDeclarativeGeoServiceProvider::allowExperimentalChanged(bool
    #      allow)
    self.uglySide.call(
        'ritual_ZN30QDeclarativeGeoServiceProvider24allowExperimentalChange'
        'dEb',
        allow,
    )

  def parametersReady(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativeGeoServiceProvider::parametersReady()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceprovider.html
    """
    #  bool QDeclarativeGeoServiceProvider::parametersReady()
    return self.uglySide.call(
        'ritual_ZN30QDeclarativeGeoServiceProvider15parametersReadyEv',
    )

  def tryAttach(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoServiceProvider::tryAttach()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceprovider.html#tryAttach
    """
    #  void QDeclarativeGeoServiceProvider::tryAttach()
    self.uglySide.call(
        'ritual_ZN30QDeclarativeGeoServiceProvider9tryAttachEv',
    )

  @staticmethod
  def parameter_append(*__, **_) -> Never:
    """
    Qt's 'void QDeclarativeGeoServiceProvider::parameter_append(
    QQmlListProperty<QDeclarativePluginParameter> *prop,
    QDeclarativePluginParameter *mapObject)': names
    'QQmlListProperty<QDeclarativePluginParameter>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QDeclarativeGeoServiceProvider.parameter_append' has no cute "
        "function yet. Qt's 'void "
        "QDeclarativeGeoServiceProvider::parameter_append(QQmlListProperty<Q"
        "DeclarativePluginParameter> *prop, QDeclarativePluginParameter "
        "*mapObject)': names "
        "'QQmlListProperty<QDeclarativePluginParameter>', which has no cute "
        "class yet.")

  @staticmethod
  def parameter_at(*__, **_) -> Never:
    """
    Qt's 'QDeclarativePluginParameter
    *QDeclarativeGeoServiceProvider::parameter_at(
    QQmlListProperty<QDeclarativePluginParameter> *prop, qsizetype index)':
    names 'QQmlListProperty<QDeclarativePluginParameter>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QDeclarativeGeoServiceProvider.parameter_at' has no cute function "
        "yet. Qt's 'QDeclarativePluginParameter "
        "*QDeclarativeGeoServiceProvider::parameter_at(QQmlListProperty<QDec"
        "larativePluginParameter> *prop, qsizetype index)': names "
        "'QQmlListProperty<QDeclarativePluginParameter>', which has no cute "
        "class yet.")

  @staticmethod
  def parameter_clear(*__, **_) -> Never:
    """
    Qt's 'void QDeclarativeGeoServiceProvider::parameter_clear(
    QQmlListProperty<QDeclarativePluginParameter> *prop)': names
    'QQmlListProperty<QDeclarativePluginParameter>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QDeclarativeGeoServiceProvider.parameter_clear' has no cute "
        "function yet. Qt's 'void "
        "QDeclarativeGeoServiceProvider::parameter_clear(QQmlListProperty<QD"
        "eclarativePluginParameter> *prop)': names "
        "'QQmlListProperty<QDeclarativePluginParameter>', which has no cute "
        "class yet.")

  @staticmethod
  def parameter_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype QDeclarativeGeoServiceProvider::parameter_count(
    QQmlListProperty<QDeclarativePluginParameter> *prop)': names
    'QQmlListProperty<QDeclarativePluginParameter>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QDeclarativeGeoServiceProvider.parameter_count' has no cute "
        "function yet. Qt's 'qsizetype "
        "QDeclarativeGeoServiceProvider::parameter_count(QQmlListProperty<QD"
        "eclarativePluginParameter> *prop)': names "
        "'QQmlListProperty<QDeclarativePluginParameter>', which has no cute "
        "class yet.")

  @staticmethod
  def parameters(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QDeclarativePluginParameter>
    QDeclarativeGeoServiceProvider::parameters()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativeGeoServiceProvider.parameters' has no cute function "
        "yet. Qt's 'QQmlListProperty<QDeclarativePluginParameter> "
        "QDeclarativeGeoServiceProvider::parameters()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def supportsGeocoding(*__, **_) -> Never:
    """
    Qt's 'bool QDeclarativeGeoServiceProvider::supportsGeocoding(const
    GeocodingFeatures &feature) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QDeclarativeGeoServiceProvider.supportsGeocoding' has no cute "
        "function yet. Qt's 'bool "
        "QDeclarativeGeoServiceProvider::supportsGeocoding(const "
        "GeocodingFeatures &feature) const': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def supportsMapping(*__, **_) -> Never:
    """
    Qt's 'bool QDeclarativeGeoServiceProvider::supportsMapping(const
    MappingFeatures &feature) const': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QDeclarativeGeoServiceProvider.supportsMapping' has no cute "
        "function yet. Qt's 'bool "
        "QDeclarativeGeoServiceProvider::supportsMapping(const "
        "MappingFeatures &feature) const': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def supportsNavigation(*__, **_) -> Never:
    """
    Qt's 'bool QDeclarativeGeoServiceProvider::supportsNavigation(const
    NavigationFeature &feature) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QDeclarativeGeoServiceProvider.supportsNavigation' has no cute "
        "function yet. Qt's 'bool "
        "QDeclarativeGeoServiceProvider::supportsNavigation(const "
        "NavigationFeature &feature) const': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def supportsPlaces(*__, **_) -> Never:
    """
    Qt's 'bool QDeclarativeGeoServiceProvider::supportsPlaces(const
    PlacesFeatures &feature) const': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QDeclarativeGeoServiceProvider.supportsPlaces' has no cute "
        "function yet. Qt's 'bool "
        "QDeclarativeGeoServiceProvider::supportsPlaces(const "
        "PlacesFeatures &feature) const': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def supportsRouting(*__, **_) -> Never:
    """
    Qt's 'bool QDeclarativeGeoServiceProvider::supportsRouting(const
    RoutingFeatures &feature) const': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QDeclarativeGeoServiceProvider.supportsRouting' has no cute "
        "function yet. Qt's 'bool "
        "QDeclarativeGeoServiceProvider::supportsRouting(const "
        "RoutingFeatures &feature) const': takes a type Python has no way "
        "to hand over yet.")
