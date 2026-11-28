"""
QDeclarativeGeoServiceProviderRequirements binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qdeclarativegeoserviceprovider_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativeGeoServiceProviderRequirements to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QDeclarativeGeoServiceProvider

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QGeoServiceProvider
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoServiceProvider = WAIT['QGeoServiceProvider']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDeclarativeGeoServiceProviderRequirements(QObject):
  """
  The cute side of Qt's QDeclarativeGeoServiceProviderRequirements: a plain
  Python object standing in front of one C++
  QDeclarativeGeoServiceProviderRequirements.

  It is built on the cute 'QObject', as Qt's
  QDeclarativeGeoServiceProviderRequirements is built on Qt's QObject, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativeGeoServiceProviderRequirements that has
  a ritual and that Python can call so far, 9 names in all: 'metaObject',
  'tr', 'mappingRequirements', 'routingRequirements',
  'geocodingRequirements', 'placesRequirements', 'navigationRequirements',
  'matches', 'requirementsChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDeclarativeGeoServiceProviderRequirements::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QDeclarativeGeoServiceProviderRequirements::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void
    QDeclarativeGeoServiceProviderRequirements::qt_qmlMarker_uncreatable()':
    one of Qt's own inner workings.
  - Qt's 'QDeclarativeGeoServiceProviderRequirements::
    ~QDeclarativeGeoServiceProviderRequirements()': the destructor: Python
    never removes a C++ QDeclarativeGeoServiceProviderRequirements.
  - Qt's 'void
    QDeclarativeGeoServiceProviderRequirements::setMappingRequirements(const
    QDeclarativeGeoServiceProvider::MappingFeatures &features)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void
    QDeclarativeGeoServiceProviderRequirements::setRoutingRequirements(const
    QDeclarativeGeoServiceProvider::RoutingFeatures &features)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void
    QDeclarativeGeoServiceProviderRequirements::setGeocodingRequirements(
    const QDeclarativeGeoServiceProvider::GeocodingFeatures &features)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void
    QDeclarativeGeoServiceProviderRequirements::setPlacesRequirements(const
    QDeclarativeGeoServiceProvider::PlacesFeatures &features)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void
    QDeclarativeGeoServiceProviderRequirements::setNavigationRequirements(
    const QDeclarativeGeoServiceProvider::NavigationFeatures &features)':
    takes a type Python has no way to hand over yet.
  - Qt's 'bool QDeclarativeGeoServiceProviderRequirements::operator==(const
    QDeclarativeGeoServiceProviderRequirements &rhs) const': takes a type
    Python has no way to hand over yet.
  - Qt's 'void
    QDeclarativeGeoServiceProviderRequirements::mappingRequirementsChanged(
    const QDeclarativeGeoServiceProvider::MappingFeatures &features)': takes
    a type Python has no way to hand over yet.
  - Qt's 'void
    QDeclarativeGeoServiceProviderRequirements::routingRequirementsChanged(
    const QDeclarativeGeoServiceProvider::RoutingFeatures &features)': takes
    a type Python has no way to hand over yet.
  - Qt's 'void
    QDeclarativeGeoServiceProviderRequirements::geocodingRequirementsChanged(
    const QDeclarativeGeoServiceProvider::GeocodingFeatures &features)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void
    QDeclarativeGeoServiceProviderRequirements::placesRequirementsChanged(
    const QDeclarativeGeoServiceProvider::PlacesFeatures &features)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QDeclarativeGeoServiceProviderRequirements::
    navigationRequirementsChanged(const
    QDeclarativeGeoServiceProvider::NavigationFeatures &features)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 27 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDeclarativeGeoServiceProviderRequirements is created at the
    first use, not by 'QDeclarativeGeoServiceProviderRequirements(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativeGeoServiceProviderRequirements.
  - Qt tells when it has removed the C++
    QDeclarativeGeoServiceProviderRequirements. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QDeclarativeGeoServiceProviderRequirements that has no
    cute function yet, 'geocodingRequirementsChanged',
    'mappingRequirementsChanged', 'navigationRequirementsChanged',
    'placesRequirementsChanged', 'routingRequirementsChanged',
    'setGeocodingRequirements', 'setMappingRequirements',
    'setNavigationRequirements', 'setPlacesRequirements',
    'setRoutingRequirements', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QDeclarativeGeoServiceProviderRequirements::tr(const
    char *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceproviderrequirements.html#tr

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
    #  QString QDeclarativeGeoServiceProviderRequirements::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN42QDeclarativeGeoServiceProviderRequirements2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativeGeoServiceProviderRequirements'

  #  A C++ QDeclarativeGeoServiceProviderRequirements Python makes is of a
  #  C++ class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativeGeoServiceProviderRequirements'

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
    *QDeclarativeGeoServiceProviderRequirements::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceproviderrequirements.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QDeclarativeGeoServiceProviderRequirements::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK42QDeclarativeGeoServiceProviderRequirements10metaObject'
        'Ev',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def mappingRequirements(
      self,
  ) -> QDeclarativeGeoServiceProvider.MappingFeatures:
    """
    Calls Qt's 'QDeclarativeGeoServiceProvider::MappingFeatures
    QDeclarativeGeoServiceProviderRequirements::mappingRequirements() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceproviderrequirements.html

    Returns
    -------

    QDeclarativeGeoServiceProvider.MappingFeatures
      The value standing for the combination Qt gave back.
    """
    #  QDeclarativeGeoServiceProvider::MappingFeatures
    #      QDeclarativeGeoServiceProviderRequirements::mappingRequirements()
    #      const
    return QDeclarativeGeoServiceProvider.MappingFeatures(self.uglySide.call(
        'ritual_ZNK42QDeclarativeGeoServiceProviderRequirements19mappingReq'
        'uirementsEv',
    ))

  def routingRequirements(
      self,
  ) -> QDeclarativeGeoServiceProvider.RoutingFeatures:
    """
    Calls Qt's 'QDeclarativeGeoServiceProvider::RoutingFeatures
    QDeclarativeGeoServiceProviderRequirements::routingRequirements() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceproviderrequirements.html

    Returns
    -------

    QDeclarativeGeoServiceProvider.RoutingFeatures
      The value standing for the combination Qt gave back.
    """
    #  QDeclarativeGeoServiceProvider::RoutingFeatures
    #      QDeclarativeGeoServiceProviderRequirements::routingRequirements()
    #      const
    return QDeclarativeGeoServiceProvider.RoutingFeatures(self.uglySide.call(
        'ritual_ZNK42QDeclarativeGeoServiceProviderRequirements19routingReq'
        'uirementsEv',
    ))

  def geocodingRequirements(
      self,
  ) -> QDeclarativeGeoServiceProvider.GeocodingFeatures:
    """
    Calls Qt's 'QDeclarativeGeoServiceProvider::GeocodingFeatures
    QDeclarativeGeoServiceProviderRequirements::geocodingRequirements()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceproviderrequirements.html

    Returns
    -------

    QDeclarativeGeoServiceProvider.GeocodingFeatures
      The value standing for the combination Qt gave back.
    """
    #  QDeclarativeGeoServiceProvider::GeocodingFeatures
    #      QDeclarativeGeoServiceProviderRequirements::geocodingRequirements(
    #      ) const
    return QDeclarativeGeoServiceProvider.GeocodingFeatures(
        self.uglySide.call(
            'ritual_ZNK42QDeclarativeGeoServiceProviderRequirements21geocod'
            'ingRequirementsEv',
        ))

  def placesRequirements(
      self,
  ) -> QDeclarativeGeoServiceProvider.PlacesFeatures:
    """
    Calls Qt's 'QDeclarativeGeoServiceProvider::PlacesFeatures
    QDeclarativeGeoServiceProviderRequirements::placesRequirements() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceproviderrequirements.html

    Returns
    -------

    QDeclarativeGeoServiceProvider.PlacesFeatures
      The value standing for the combination Qt gave back.
    """
    #  QDeclarativeGeoServiceProvider::PlacesFeatures
    #      QDeclarativeGeoServiceProviderRequirements::placesRequirements()
    #      const
    return QDeclarativeGeoServiceProvider.PlacesFeatures(self.uglySide.call(
        'ritual_ZNK42QDeclarativeGeoServiceProviderRequirements18placesRequ'
        'irementsEv',
    ))

  def navigationRequirements(
      self,
  ) -> QDeclarativeGeoServiceProvider.NavigationFeatures:
    """
    Calls Qt's 'QDeclarativeGeoServiceProvider::NavigationFeatures
    QDeclarativeGeoServiceProviderRequirements::navigationRequirements()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceproviderrequirements.html

    Returns
    -------

    QDeclarativeGeoServiceProvider.NavigationFeatures
      The value standing for the combination Qt gave back.
    """
    #  QDeclarativeGeoServiceProvider::NavigationFeatures
    #      QDeclarativeGeoServiceProviderRequirements::
    #      navigationRequirements() const
    return QDeclarativeGeoServiceProvider.NavigationFeatures(
        self.uglySide.call(
            'ritual_ZNK42QDeclarativeGeoServiceProviderRequirements22naviga'
            'tionRequirementsEv',
        ))

  @overload(QGeoServiceProvider)
  @overload(NoneType)
  def matches(self, provider: Optional[QGeoServiceProvider]) -> bool:
    """
    Calls Qt's 'bool
    QDeclarativeGeoServiceProviderRequirements::matches(const
    QGeoServiceProvider *provider) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceproviderrequirements.html

    Parameters
    ----------

    provider : Optional[QGeoServiceProvider]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDeclarativeGeoServiceProviderRequirements::matches(const
    #      QGeoServiceProvider *provider) const
    return self.uglySide.call(
        'ritual_ZNK42QDeclarativeGeoServiceProviderRequirements7matchesEPK1'
        '9QGeoServiceProvider',
        self._addressOf(provider),
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QDeclarativeGeoServiceProviderRequirements::
    QDeclarativeGeoServiceProviderRequirements(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceproviderrequirements.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDeclarativeGeoServiceProviderRequirements::
    #      QDeclarativeGeoServiceProviderRequirements(QObject *parent)
    self._noteCreation(
        QDeclarativeGeoServiceProviderRequirements, lambda: Rituals.call(
            'ritual_ZN42QDeclarativeGeoServiceProviderRequirementsC1EP7QObj'
            'ect',
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

  def requirementsChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoServiceProviderRequirements::requirementsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoserviceproviderrequirements.html
    """
    #  void QDeclarativeGeoServiceProviderRequirements::requirementsChanged()
    self.uglySide.call(
        'ritual_ZN42QDeclarativeGeoServiceProviderRequirements19requirement'
        'sChangedEv',
    )

  @staticmethod
  def geocodingRequirementsChanged(*__, **_) -> Never:
    """
    Qt's 'void
    QDeclarativeGeoServiceProviderRequirements::geocodingRequirementsChanged(
    const QDeclarativeGeoServiceProvider::GeocodingFeatures &features)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDeclarativeGeoServiceProviderRequirements.geocodingRequirementsCh"
        "anged' has no cute function yet. Qt's 'void "
        "QDeclarativeGeoServiceProviderRequirements::geocodingRequirementsCh"
        "anged(const QDeclarativeGeoServiceProvider::GeocodingFeatures "
        "&features)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def mappingRequirementsChanged(*__, **_) -> Never:
    """
    Qt's 'void
    QDeclarativeGeoServiceProviderRequirements::mappingRequirementsChanged(
    const QDeclarativeGeoServiceProvider::MappingFeatures &features)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDeclarativeGeoServiceProviderRequirements.mappingRequirementsChan"
        "ged' has no cute function yet. Qt's 'void "
        "QDeclarativeGeoServiceProviderRequirements::mappingRequirementsChan"
        "ged(const QDeclarativeGeoServiceProvider::MappingFeatures "
        "&features)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def navigationRequirementsChanged(*__, **_) -> Never:
    """
    Qt's 'void QDeclarativeGeoServiceProviderRequirements::
    navigationRequirementsChanged(const
    QDeclarativeGeoServiceProvider::NavigationFeatures &features)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDeclarativeGeoServiceProviderRequirements.navigationRequirementsC"
        "hanged' has no cute function yet. Qt's 'void "
        "QDeclarativeGeoServiceProviderRequirements::navigationRequirementsC"
        "hanged(const QDeclarativeGeoServiceProvider::NavigationFeatures "
        "&features)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def placesRequirementsChanged(*__, **_) -> Never:
    """
    Qt's 'void
    QDeclarativeGeoServiceProviderRequirements::placesRequirementsChanged(
    const QDeclarativeGeoServiceProvider::PlacesFeatures &features)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDeclarativeGeoServiceProviderRequirements.placesRequirementsChang"
        "ed' has no cute function yet. Qt's 'void "
        "QDeclarativeGeoServiceProviderRequirements::placesRequirementsChang"
        "ed(const QDeclarativeGeoServiceProvider::PlacesFeatures "
        "&features)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def routingRequirementsChanged(*__, **_) -> Never:
    """
    Qt's 'void
    QDeclarativeGeoServiceProviderRequirements::routingRequirementsChanged(
    const QDeclarativeGeoServiceProvider::RoutingFeatures &features)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDeclarativeGeoServiceProviderRequirements.routingRequirementsChan"
        "ged' has no cute function yet. Qt's 'void "
        "QDeclarativeGeoServiceProviderRequirements::routingRequirementsChan"
        "ged(const QDeclarativeGeoServiceProvider::RoutingFeatures "
        "&features)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setGeocodingRequirements(*__, **_) -> Never:
    """
    Qt's 'void
    QDeclarativeGeoServiceProviderRequirements::setGeocodingRequirements(
    const QDeclarativeGeoServiceProvider::GeocodingFeatures &features)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDeclarativeGeoServiceProviderRequirements.setGeocodingRequirement"
        "s' has no cute function yet. Qt's 'void "
        "QDeclarativeGeoServiceProviderRequirements::setGeocodingRequirement"
        "s(const QDeclarativeGeoServiceProvider::GeocodingFeatures "
        "&features)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setMappingRequirements(*__, **_) -> Never:
    """
    Qt's 'void
    QDeclarativeGeoServiceProviderRequirements::setMappingRequirements(const
    QDeclarativeGeoServiceProvider::MappingFeatures &features)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDeclarativeGeoServiceProviderRequirements.setMappingRequirements'"
        " has no cute function yet. Qt's 'void "
        "QDeclarativeGeoServiceProviderRequirements::setMappingRequirements("
        "const QDeclarativeGeoServiceProvider::MappingFeatures &features)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def setNavigationRequirements(*__, **_) -> Never:
    """
    Qt's 'void
    QDeclarativeGeoServiceProviderRequirements::setNavigationRequirements(
    const QDeclarativeGeoServiceProvider::NavigationFeatures &features)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDeclarativeGeoServiceProviderRequirements.setNavigationRequiremen"
        "ts' has no cute function yet. Qt's 'void "
        "QDeclarativeGeoServiceProviderRequirements::setNavigationRequiremen"
        "ts(const QDeclarativeGeoServiceProvider::NavigationFeatures "
        "&features)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setPlacesRequirements(*__, **_) -> Never:
    """
    Qt's 'void
    QDeclarativeGeoServiceProviderRequirements::setPlacesRequirements(const
    QDeclarativeGeoServiceProvider::PlacesFeatures &features)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDeclarativeGeoServiceProviderRequirements.setPlacesRequirements' "
        "has no cute function yet. Qt's 'void "
        "QDeclarativeGeoServiceProviderRequirements::setPlacesRequirements(c"
        "onst QDeclarativeGeoServiceProvider::PlacesFeatures &features)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def setRoutingRequirements(*__, **_) -> Never:
    """
    Qt's 'void
    QDeclarativeGeoServiceProviderRequirements::setRoutingRequirements(const
    QDeclarativeGeoServiceProvider::RoutingFeatures &features)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDeclarativeGeoServiceProviderRequirements.setRoutingRequirements'"
        " has no cute function yet. Qt's 'void "
        "QDeclarativeGeoServiceProviderRequirements::setRoutingRequirements("
        "const QDeclarativeGeoServiceProvider::RoutingFeatures &features)': "
        "takes a type Python has no way to hand over yet.")
