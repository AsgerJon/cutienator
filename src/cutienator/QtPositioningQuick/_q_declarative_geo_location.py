"""
QDeclarativeGeoLocation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioningQuick/6.12.0/QtPositioningQuick/private/qdeclarativegeolocation_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativeGeoLocation to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QMap, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from ..QtPositioning import QGeoCoordinate, QGeoLocation, QGeoShape
  from . import QDeclarativeGeoAddress
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeclarativeGeoAddress = WAIT['QDeclarativeGeoAddress']
  QGeoCoordinate = WAIT['QGeoCoordinate']
  QGeoLocation = WAIT['QGeoLocation']
  QGeoShape = WAIT['QGeoShape']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDeclarativeGeoLocation(QObject):
  """
  The cute side of Qt's QDeclarativeGeoLocation: a plain Python object
  standing in front of one C++ QDeclarativeGeoLocation.

  It is built on the cute 'QObject', as Qt's QDeclarativeGeoLocation is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativeGeoLocation that has a ritual and that
  Python can call so far, 17 names in all: 'metaObject', 'tr', 'location',
  'setLocation', 'address', 'setAddress', 'coordinate', 'setCoordinate',
  'boundingShape', 'setBoundingShape', 'extendedAttributes',
  'setExtendedAttributes', 'setLocationInternal',
  '_qt_property_m_address_offset', '_qt_property_m_boundingShape_offset',
  '_qt_property_m_coordinate_offset',
  '_qt_property_m_extendedAttributes_offset'. It can be made from Python, in
  2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDeclarativeGeoLocation::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QDeclarativeGeoLocation::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDeclarativeGeoLocation::~QDeclarativeGeoLocation()': the
    destructor: Python never removes a C++ QDeclarativeGeoLocation.
  - Qt's 'QBindable<QDeclarativeGeoAddress *>
    QDeclarativeGeoLocation::bindableAddress()': gives a type Python has no
    way to take yet.
  - Qt's 'QBindable<QGeoCoordinate>
    QDeclarativeGeoLocation::bindableCoordinate()': gives a type Python has
    no way to take yet.
  - Qt's 'QBindable<QGeoShape>
    QDeclarativeGeoLocation::bindableBoundingShape()': gives a type Python
    has no way to take yet.
  - Qt's 'QBindable<QVariantMap>
    QDeclarativeGeoLocation::bindableExtendedAttributes()': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 28 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDeclarativeGeoLocation is created at the first use, not by
    'QDeclarativeGeoLocation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativeGeoLocation.
  - Qt tells when it has removed the C++ QDeclarativeGeoLocation. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDeclarativeGeoLocation that has no cute function yet,
    'bindableAddress', 'bindableBoundingShape', 'bindableCoordinate',
    'bindableExtendedAttributes', holds a function that raises
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
    Calls Qt's 'QString QDeclarativeGeoLocation::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeolocation.html#tr

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
    #  QString QDeclarativeGeoLocation::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QDeclarativeGeoLocation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def _qt_property_m_address_offset() -> int:
    """
    Calls Qt's 'size_t
    QDeclarativeGeoLocation::_qt_property_m_address_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeolocation.html
    """
    #  size_t QDeclarativeGeoLocation::_qt_property_m_address_offset()
    return Rituals.call(
        'ritual_ZN23QDeclarativeGeoLocation29_qt_property_m_address_offsetE'
        'v',
    )

  @staticmethod
  def _qt_property_m_boundingShape_offset() -> int:
    """
    Calls Qt's 'size_t
    QDeclarativeGeoLocation::_qt_property_m_boundingShape_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeolocation.html
    """
    #  size_t QDeclarativeGeoLocation::_qt_property_m_boundingShape_offset()
    return Rituals.call(
        'ritual_ZN23QDeclarativeGeoLocation35_qt_property_m_boundingShape_o'
        'ffsetEv',
    )

  @staticmethod
  def _qt_property_m_coordinate_offset() -> int:
    """
    Calls Qt's 'size_t
    QDeclarativeGeoLocation::_qt_property_m_coordinate_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeolocation.html
    """
    #  size_t QDeclarativeGeoLocation::_qt_property_m_coordinate_offset()
    return Rituals.call(
        'ritual_ZN23QDeclarativeGeoLocation32_qt_property_m_coordinate_offs'
        'etEv',
    )

  @staticmethod
  def _qt_property_m_extendedAttributes_offset() -> int:
    """
    Calls Qt's 'size_t
    QDeclarativeGeoLocation::_qt_property_m_extendedAttributes_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeolocation.html
    """
    #  size_t
    #      QDeclarativeGeoLocation::_qt_property_m_extendedAttributes_offset(
    #      )
    return Rituals.call(
        'ritual_ZN23QDeclarativeGeoLocation40_qt_property_m_extendedAttribu'
        'tes_offsetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativeGeoLocation'

  #  A C++ QDeclarativeGeoLocation Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativeGeoLocation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDeclarativeGeoLocation::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeolocation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDeclarativeGeoLocation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QDeclarativeGeoLocation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def location(self) -> QGeoLocation:
    """
    Calls Qt's 'QGeoLocation QDeclarativeGeoLocation::location() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeolocation.html#location

    Returns
    -------

    QGeoLocation
      A new cute QGeoLocation around the copy Qt gave back. Python owns it.
    """
    #  QGeoLocation QDeclarativeGeoLocation::location() const
    address = self.uglySide.call(
        'ritual_ZNK23QDeclarativeGeoLocation8locationEv',
    )
    from ..QtPositioning import QGeoLocation
    return QGeoLocation._cuteOwning(address)

  def address(self) -> Optional[QDeclarativeGeoAddress]:
    """
    Calls Qt's 'QDeclarativeGeoAddress *QDeclarativeGeoLocation::address()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeolocation.html#address

    Returns
    -------

    Optional[QDeclarativeGeoAddress]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDeclarativeGeoAddress *QDeclarativeGeoLocation::address() const
    address = self.uglySide.call(
        'ritual_ZNK23QDeclarativeGeoLocation7addressEv',
    )
    from . import QDeclarativeGeoAddress
    return QDeclarativeGeoAddress._cuteAt(address)

  def coordinate(self) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QDeclarativeGeoLocation::coordinate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeolocation.html#coordinate

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QDeclarativeGeoLocation::coordinate() const
    address = self.uglySide.call(
        'ritual_ZNK23QDeclarativeGeoLocation10coordinateEv',
    )
    from ..QtPositioning import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  def boundingShape(self) -> QGeoShape:
    """
    Calls Qt's 'QGeoShape QDeclarativeGeoLocation::boundingShape() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeolocation.html#boundingShape

    Returns
    -------

    QGeoShape
      A new cute QGeoShape around the copy Qt gave back. Python owns it.
    """
    #  QGeoShape QDeclarativeGeoLocation::boundingShape() const
    address = self.uglySide.call(
        'ritual_ZNK23QDeclarativeGeoLocation13boundingShapeEv',
    )
    from ..QtPositioning import QGeoShape
    return QGeoShape._cuteOwning(address)

  def extendedAttributes(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap QDeclarativeGeoLocation::extendedAttributes()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeolocation.html#extendedAttributes

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap QDeclarativeGeoLocation::extendedAttributes() const
    address = self.uglySide.call(
        'ritual_ZNK23QDeclarativeGeoLocation18extendedAttributesEv',
    )
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGeoLocation)
  def setLocation(self, src: QGeoLocation) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoLocation::setLocation(const QGeoLocation
    &src)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeolocation.html#setLocation

    Parameters
    ----------

    src : QGeoLocation
      Passed on as a value: Qt reads the C++ QGeoLocation, which stays
      Python's own.
    """
    #  void QDeclarativeGeoLocation::setLocation(const QGeoLocation &src)
    self.uglySide.call(
        'ritual_ZN23QDeclarativeGeoLocation11setLocationERK12QGeoLocation',
        self._valueOf(src),
    )

  @overload(QDeclarativeGeoAddress)
  @overload(NoneType)
  def setAddress(self, address: Optional[QDeclarativeGeoAddress]) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoLocation::setAddress(QDeclarativeGeoAddress *address)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeolocation.html#setAddress

    Parameters
    ----------

    address : Optional[QDeclarativeGeoAddress]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeGeoLocation::setAddress(QDeclarativeGeoAddress
    #      *address)
    self.uglySide.call(
        'ritual_ZN23QDeclarativeGeoLocation10setAddressEP22QDeclarativeGeoA'
        'ddress',
        self._addressOf(address),
    )

  @overload(QGeoCoordinate)
  def setCoordinate(self, coordinate: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoLocation::setCoordinate(const
    QGeoCoordinate coordinate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeolocation.html#setCoordinate

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QDeclarativeGeoLocation::setCoordinate(const QGeoCoordinate
    #      coordinate)
    self.uglySide.call(
        'ritual_ZN23QDeclarativeGeoLocation13setCoordinateE14QGeoCoordinate',
        self._valueOf(coordinate),
    )

  @overload(QGeoShape)
  def setBoundingShape(self, boundingShape: QGeoShape) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoLocation::setBoundingShape(const
    QGeoShape &boundingShape)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeolocation.html#setBoundingShape

    Parameters
    ----------

    boundingShape : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.
    """
    #  void QDeclarativeGeoLocation::setBoundingShape(const QGeoShape
    #      &boundingShape)
    self.uglySide.call(
        'ritual_ZN23QDeclarativeGeoLocation16setBoundingShapeERK9QGeoShape',
        self._valueOf(boundingShape),
    )

  @overload(QMap[str, QVariant])
  def setExtendedAttributes(self, attributes: QMap[str, QVariant]) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoLocation::setExtendedAttributes(const
    QVariantMap &attributes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeolocation.html#setExtendedAttributes

    Parameters
    ----------

    attributes : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QDeclarativeGeoLocation::setExtendedAttributes(const QVariantMap
    #      &attributes)
    self.uglySide.call(
        'ritual_ZN23QDeclarativeGeoLocation21setExtendedAttributesERK4QMapI'
        '7QString8QVariantE',
        self._valueOf(attributes),
    )

  @overload(QGeoLocation)
  def setLocationInternal(self, src: QGeoLocation) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoLocation::setLocationInternal(const
    QGeoLocation &src)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeolocation.html#setLocationInternal

    Parameters
    ----------

    src : QGeoLocation
      Passed on as a value: Qt reads the C++ QGeoLocation, which stays
      Python's own.
    """
    #  void QDeclarativeGeoLocation::setLocationInternal(const QGeoLocation
    #      &src)
    self.uglySide.call(
        'ritual_ZN23QDeclarativeGeoLocation19setLocationInternalERK12QGeoLo'
        'cation',
        self._valueOf(src),
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
    'QDeclarativeGeoLocation::QDeclarativeGeoLocation(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeolocation.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDeclarativeGeoLocation::QDeclarativeGeoLocation(QObject *parent)
    self._noteCreation(QDeclarativeGeoLocation, lambda: Rituals.call(
        'ritual_ZN23QDeclarativeGeoLocationC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QGeoLocation)
  @overload(QGeoLocation, QObject)
  @overload(QGeoLocation, NoneType)
  def __init__(
      self,
      src: QGeoLocation,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QDeclarativeGeoLocation::QDeclarativeGeoLocation(const QGeoLocation
    &src, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeolocation.html

    Parameters
    ----------

    src : QGeoLocation
      Passed on as a value: Qt reads the C++ QGeoLocation, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDeclarativeGeoLocation::QDeclarativeGeoLocation(const QGeoLocation
    #      &src, QObject *parent)
    self._noteCreation(QDeclarativeGeoLocation, lambda: Rituals.call(
        'ritual_ZN23QDeclarativeGeoLocationC1ERK12QGeoLocationP7QObject',
        self._valueOf(src), self._addressOf(parent, 'QObject'),
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
  def bindableAddress(*__, **_) -> Never:
    """
    Qt's 'QBindable<QDeclarativeGeoAddress *>
    QDeclarativeGeoLocation::bindableAddress()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativeGeoLocation.bindableAddress' has no cute function "
        "yet. Qt's 'QBindable<QDeclarativeGeoAddress *> "
        "QDeclarativeGeoLocation::bindableAddress()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def bindableBoundingShape(*__, **_) -> Never:
    """
    Qt's 'QBindable<QGeoShape>
    QDeclarativeGeoLocation::bindableBoundingShape()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativeGeoLocation.bindableBoundingShape' has no cute "
        "function yet. Qt's 'QBindable<QGeoShape> "
        "QDeclarativeGeoLocation::bindableBoundingShape()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def bindableCoordinate(*__, **_) -> Never:
    """
    Qt's 'QBindable<QGeoCoordinate>
    QDeclarativeGeoLocation::bindableCoordinate()': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativeGeoLocation.bindableCoordinate' has no cute function "
        "yet. Qt's 'QBindable<QGeoCoordinate> "
        "QDeclarativeGeoLocation::bindableCoordinate()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def bindableExtendedAttributes(*__, **_) -> Never:
    """
    Qt's 'QBindable<QVariantMap>
    QDeclarativeGeoLocation::bindableExtendedAttributes()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativeGeoLocation.bindableExtendedAttributes' has no cute "
        "function yet. Qt's 'QBindable<QVariantMap> "
        "QDeclarativeGeoLocation::bindableExtendedAttributes()': gives a "
        "type Python has no way to take yet.")
