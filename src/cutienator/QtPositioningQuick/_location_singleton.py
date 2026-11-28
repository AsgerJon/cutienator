"""
LocationSingleton binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioningQuick/6.12.0/QtPositioningQuick/private/locationsingleton_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means LocationSingleton to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF, QVariant
  from ..QtPositioning import QGeoCircle, QGeoCoordinate, QGeoPath
  from ..QtPositioning import QGeoPolygon, QGeoRectangle, QGeoShape
  from ..QtQml import QJSValue
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoCoordinate = WAIT['QGeoCoordinate']
  QGeoShape = WAIT['QGeoShape']
  QJSValue = WAIT['QJSValue']
  QPointF = WAIT['QPointF']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class LocationSingleton(QObject):
  """
  The cute side of Qt's LocationSingleton: a plain Python object standing in
  front of one C++ LocationSingleton.

  It is built on the cute 'QObject', as Qt's LocationSingleton is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's LocationSingleton that has a ritual and that Python
  can call so far, 14 names in all: 'metaObject', 'tr', 'coordinate',
  'shape', 'rectangle', 'circle', 'path', 'polygon', 'shapeToCircle',
  'shapeToRectangle', 'shapeToPath', 'shapeToPolygon', 'mercatorToCoord',
  'coordToMercator'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *LocationSingleton::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int LocationSingleton::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void LocationSingleton::qt_qmlMarker_singleton()': one of Qt's own
    inner workings.

  What has no ritual
  ------------------

  2 of the 28 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ LocationSingleton is created at the first use, not by
    'LocationSingleton(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ LocationSingleton.
  - Qt tells when it has removed the C++ LocationSingleton. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString LocationSingleton::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/locationsingleton.html#tr

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
    #  QString LocationSingleton::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17LocationSingleton2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'LocationSingleton'

  #  A C++ LocationSingleton Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_LocationSingleton'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *LocationSingleton::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/locationsingleton.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *LocationSingleton::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17LocationSingleton10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload()
  def coordinate(self) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate LocationSingleton::coordinate() const'.

    Qt's own words: https://doc.qt.io/qt-6/locationsingleton.html#coordinate

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate LocationSingleton::coordinate() const
    address = self.uglySide.call(
        'ritual_ZNK17LocationSingleton10coordinateEv',
    )
    from ..QtPositioning import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  @overload(float, float, float)
  def coordinate(
      self,
      latitude: float,
      longitude: float,
      altitude: float,
  ) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate LocationSingleton::coordinate(double latitude,
    double longitude, double altitude) const'.

    Qt's own words: https://doc.qt.io/qt-6/locationsingleton.html#coordinate

    Parameters
    ----------

    latitude : float
      Passed on as it is.

    longitude : float
      Passed on as it is.

    altitude : float
      Passed on as it is.

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate LocationSingleton::coordinate(double latitude, double
    #      longitude, double altitude) const
    address = self.uglySide.call(
        'ritual_ZNK17LocationSingleton10coordinateEddd',
        latitude, longitude, altitude,
    )
    from ..QtPositioning import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  def shape(self) -> QGeoShape:
    """
    Calls Qt's 'QGeoShape LocationSingleton::shape() const'.

    Qt's own words: https://doc.qt.io/qt-6/locationsingleton.html#shape

    Returns
    -------

    QGeoShape
      A new cute QGeoShape around the copy Qt gave back. Python owns it.
    """
    #  QGeoShape LocationSingleton::shape() const
    address = self.uglySide.call('ritual_ZNK17LocationSingleton5shapeEv')
    from ..QtPositioning import QGeoShape
    return QGeoShape._cuteOwning(address)

  @overload()
  def rectangle(self) -> QGeoRectangle:
    """
    Calls Qt's 'QGeoRectangle LocationSingleton::rectangle() const'.

    Qt's own words: https://doc.qt.io/qt-6/locationsingleton.html#rectangle

    Returns
    -------

    QGeoRectangle
      A new cute QGeoRectangle around the copy Qt gave back. Python owns it.
    """
    #  QGeoRectangle LocationSingleton::rectangle() const
    address = self.uglySide.call('ritual_ZNK17LocationSingleton9rectangleEv')
    from ..QtPositioning import QGeoRectangle
    return QGeoRectangle._cuteOwning(address)

  @overload(QGeoCoordinate, float, float)
  def rectangle(
      self,
      center: QGeoCoordinate,
      width: float,
      height: float,
  ) -> QGeoRectangle:
    """
    Calls Qt's 'QGeoRectangle LocationSingleton::rectangle(const
    QGeoCoordinate &center, double width, double height) const'.

    Qt's own words: https://doc.qt.io/qt-6/locationsingleton.html#rectangle

    Parameters
    ----------

    center : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.

    width : float
      Passed on as it is.

    height : float
      Passed on as it is.

    Returns
    -------

    QGeoRectangle
      A new cute QGeoRectangle around the copy Qt gave back. Python owns it.
    """
    #  QGeoRectangle LocationSingleton::rectangle(const QGeoCoordinate
    #      &center, double width, double height) const
    address = self.uglySide.call(
        'ritual_ZNK17LocationSingleton9rectangleERK14QGeoCoordinatedd',
        self._valueOf(center), width, height,
    )
    from ..QtPositioning import QGeoRectangle
    return QGeoRectangle._cuteOwning(address)

  @overload(QGeoCoordinate, QGeoCoordinate)
  def rectangle(
      self,
      topLeft: QGeoCoordinate,
      bottomRight: QGeoCoordinate,
  ) -> QGeoRectangle:
    """
    Calls Qt's 'QGeoRectangle LocationSingleton::rectangle(const
    QGeoCoordinate &topLeft, const QGeoCoordinate &bottomRight) const'.

    Qt's own words: https://doc.qt.io/qt-6/locationsingleton.html#rectangle

    Parameters
    ----------

    topLeft : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.

    bottomRight : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.

    Returns
    -------

    QGeoRectangle
      A new cute QGeoRectangle around the copy Qt gave back. Python owns it.
    """
    #  QGeoRectangle LocationSingleton::rectangle(const QGeoCoordinate
    #      &topLeft, const QGeoCoordinate &bottomRight) const
    address = self.uglySide.call(
        'ritual_ZNK17LocationSingleton9rectangleERK14QGeoCoordinateS2_',
        self._valueOf(topLeft), self._valueOf(bottomRight),
    )
    from ..QtPositioning import QGeoRectangle
    return QGeoRectangle._cuteOwning(address)

  @overload(QList[QVariant])
  def rectangle(self, coordinates: QList[QVariant]) -> QGeoRectangle:
    """
    Calls Qt's 'QGeoRectangle LocationSingleton::rectangle(const QVariantList
    &coordinates) const'.

    Qt's own words: https://doc.qt.io/qt-6/locationsingleton.html#rectangle

    Parameters
    ----------

    coordinates : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QGeoRectangle
      A new cute QGeoRectangle around the copy Qt gave back. Python owns it.
    """
    #  QGeoRectangle LocationSingleton::rectangle(const QVariantList
    #      &coordinates) const
    address = self.uglySide.call(
        'ritual_ZNK17LocationSingleton9rectangleERK5QListI8QVariantE',
        self._valueOf(coordinates),
    )
    from ..QtPositioning import QGeoRectangle
    return QGeoRectangle._cuteOwning(address)

  @overload()
  def circle(self) -> QGeoCircle:
    """
    Calls Qt's 'QGeoCircle LocationSingleton::circle() const'.

    Qt's own words: https://doc.qt.io/qt-6/locationsingleton.html#circle

    Returns
    -------

    QGeoCircle
      A new cute QGeoCircle around the copy Qt gave back. Python owns it.
    """
    #  QGeoCircle LocationSingleton::circle() const
    address = self.uglySide.call('ritual_ZNK17LocationSingleton6circleEv')
    from ..QtPositioning import QGeoCircle
    return QGeoCircle._cuteOwning(address)

  @overload(QGeoCoordinate)
  @overload(QGeoCoordinate, float)
  def circle(
      self,
      center: QGeoCoordinate,
      radius: float = -1.0,
  ) -> QGeoCircle:
    """
    Calls Qt's 'QGeoCircle LocationSingleton::circle(const QGeoCoordinate
    &center, qreal radius) const'.

    Qt's own words: https://doc.qt.io/qt-6/locationsingleton.html#circle

    Parameters
    ----------

    center : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.

    radius : float
      Passed on as it is. May be left out, as in Qt: it is then -1.0.

    Returns
    -------

    QGeoCircle
      A new cute QGeoCircle around the copy Qt gave back. Python owns it.
    """
    #  QGeoCircle LocationSingleton::circle(const QGeoCoordinate &center,
    #      qreal radius) const
    address = self.uglySide.call(
        'ritual_ZNK17LocationSingleton6circleERK14QGeoCoordinated',
        self._valueOf(center), radius,
    )
    from ..QtPositioning import QGeoCircle
    return QGeoCircle._cuteOwning(address)

  @overload()
  def path(self) -> QGeoPath:
    """
    Calls Qt's 'QGeoPath LocationSingleton::path() const'.

    Qt's own words: https://doc.qt.io/qt-6/locationsingleton.html#path

    Returns
    -------

    QGeoPath
      A new cute QGeoPath around the copy Qt gave back. Python owns it.
    """
    #  QGeoPath LocationSingleton::path() const
    address = self.uglySide.call('ritual_ZNK17LocationSingleton4pathEv')
    from ..QtPositioning import QGeoPath
    return QGeoPath._cuteOwning(address)

  @overload(QJSValue)
  @overload(QJSValue, float)
  def path(self, value: QJSValue, width: float = 0.0) -> QGeoPath:
    """
    Calls Qt's 'QGeoPath LocationSingleton::path(const QJSValue &value, qreal
    width) const'.

    Qt's own words: https://doc.qt.io/qt-6/locationsingleton.html#path

    Parameters
    ----------

    value : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.

    width : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    Returns
    -------

    QGeoPath
      A new cute QGeoPath around the copy Qt gave back. Python owns it.
    """
    #  QGeoPath LocationSingleton::path(const QJSValue &value, qreal width)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17LocationSingleton4pathERK8QJSValued',
        self._valueOf(value), width,
    )
    from ..QtPositioning import QGeoPath
    return QGeoPath._cuteOwning(address)

  @overload()
  def polygon(self) -> QGeoPolygon:
    """
    Calls Qt's 'QGeoPolygon LocationSingleton::polygon() const'.

    Qt's own words: https://doc.qt.io/qt-6/locationsingleton.html#polygon

    Returns
    -------

    QGeoPolygon
      A new cute QGeoPolygon around the copy Qt gave back. Python owns it.
    """
    #  QGeoPolygon LocationSingleton::polygon() const
    address = self.uglySide.call('ritual_ZNK17LocationSingleton7polygonEv')
    from ..QtPositioning import QGeoPolygon
    return QGeoPolygon._cuteOwning(address)

  @overload(QList[QVariant])
  def polygon(self, value: QList[QVariant]) -> QGeoPolygon:
    """
    Calls Qt's 'QGeoPolygon LocationSingleton::polygon(const QVariantList
    &value) const'.

    Qt's own words: https://doc.qt.io/qt-6/locationsingleton.html#polygon

    Parameters
    ----------

    value : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QGeoPolygon
      A new cute QGeoPolygon around the copy Qt gave back. Python owns it.
    """
    #  QGeoPolygon LocationSingleton::polygon(const QVariantList &value)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17LocationSingleton7polygonERK5QListI8QVariantE',
        self._valueOf(value),
    )
    from ..QtPositioning import QGeoPolygon
    return QGeoPolygon._cuteOwning(address)

  @overload(QList[QVariant], QList[QVariant])
  def polygon(
      self,
      perimeter: QList[QVariant],
      holes: QList[QVariant],
  ) -> QGeoPolygon:
    """
    Calls Qt's 'QGeoPolygon LocationSingleton::polygon(const QVariantList
    &perimeter, const QVariantList &holes) const'.

    Qt's own words: https://doc.qt.io/qt-6/locationsingleton.html#polygon

    Parameters
    ----------

    perimeter : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    holes : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QGeoPolygon
      A new cute QGeoPolygon around the copy Qt gave back. Python owns it.
    """
    #  QGeoPolygon LocationSingleton::polygon(const QVariantList &perimeter,
    #      const QVariantList &holes) const
    address = self.uglySide.call(
        'ritual_ZNK17LocationSingleton7polygonERK5QListI8QVariantES4_',
        self._valueOf(perimeter), self._valueOf(holes),
    )
    from ..QtPositioning import QGeoPolygon
    return QGeoPolygon._cuteOwning(address)

  @overload(QGeoShape)
  def shapeToCircle(self, shape: QGeoShape) -> QGeoCircle:
    """
    Calls Qt's 'QGeoCircle LocationSingleton::shapeToCircle(const QGeoShape
    &shape) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/locationsingleton.html#shapeToCircle

    Parameters
    ----------

    shape : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.

    Returns
    -------

    QGeoCircle
      A new cute QGeoCircle around the copy Qt gave back. Python owns it.
    """
    #  QGeoCircle LocationSingleton::shapeToCircle(const QGeoShape &shape)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17LocationSingleton13shapeToCircleERK9QGeoShape',
        self._valueOf(shape),
    )
    from ..QtPositioning import QGeoCircle
    return QGeoCircle._cuteOwning(address)

  @overload(QGeoShape)
  def shapeToRectangle(self, shape: QGeoShape) -> QGeoRectangle:
    """
    Calls Qt's 'QGeoRectangle LocationSingleton::shapeToRectangle(const
    QGeoShape &shape) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/locationsingleton.html#shapeToRectangle

    Parameters
    ----------

    shape : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.

    Returns
    -------

    QGeoRectangle
      A new cute QGeoRectangle around the copy Qt gave back. Python owns it.
    """
    #  QGeoRectangle LocationSingleton::shapeToRectangle(const QGeoShape
    #      &shape) const
    address = self.uglySide.call(
        'ritual_ZNK17LocationSingleton16shapeToRectangleERK9QGeoShape',
        self._valueOf(shape),
    )
    from ..QtPositioning import QGeoRectangle
    return QGeoRectangle._cuteOwning(address)

  @overload(QGeoShape)
  def shapeToPath(self, shape: QGeoShape) -> QGeoPath:
    """
    Calls Qt's 'QGeoPath LocationSingleton::shapeToPath(const QGeoShape
    &shape) const'.

    Qt's own words: https://doc.qt.io/qt-6/locationsingleton.html#shapeToPath

    Parameters
    ----------

    shape : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.

    Returns
    -------

    QGeoPath
      A new cute QGeoPath around the copy Qt gave back. Python owns it.
    """
    #  QGeoPath LocationSingleton::shapeToPath(const QGeoShape &shape) const
    address = self.uglySide.call(
        'ritual_ZNK17LocationSingleton11shapeToPathERK9QGeoShape',
        self._valueOf(shape),
    )
    from ..QtPositioning import QGeoPath
    return QGeoPath._cuteOwning(address)

  @overload(QGeoShape)
  def shapeToPolygon(self, shape: QGeoShape) -> QGeoPolygon:
    """
    Calls Qt's 'QGeoPolygon LocationSingleton::shapeToPolygon(const QGeoShape
    &shape) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/locationsingleton.html#shapeToPolygon

    Parameters
    ----------

    shape : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.

    Returns
    -------

    QGeoPolygon
      A new cute QGeoPolygon around the copy Qt gave back. Python owns it.
    """
    #  QGeoPolygon LocationSingleton::shapeToPolygon(const QGeoShape &shape)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17LocationSingleton14shapeToPolygonERK9QGeoShape',
        self._valueOf(shape),
    )
    from ..QtPositioning import QGeoPolygon
    return QGeoPolygon._cuteOwning(address)

  @overload(QPointF)
  def mercatorToCoord(self, mercator: QPointF) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate LocationSingleton::mercatorToCoord(const
    QPointF &mercator) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/locationsingleton.html#mercatorToCoord

    Parameters
    ----------

    mercator : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate LocationSingleton::mercatorToCoord(const QPointF
    #      &mercator) const
    address = self.uglySide.call(
        'ritual_ZNK17LocationSingleton15mercatorToCoordERK7QPointF',
        self._valueOf(mercator, 'QPointF'),
    )
    from ..QtPositioning import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  @overload(QGeoCoordinate)
  def coordToMercator(self, coord: QGeoCoordinate) -> QPointF:
    """
    Calls Qt's 'QPointF LocationSingleton::coordToMercator(const
    QGeoCoordinate &coord) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/locationsingleton.html#coordToMercator

    Parameters
    ----------

    coord : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF LocationSingleton::coordToMercator(const QGeoCoordinate
    #      &coord) const
    address = self.uglySide.call(
        'ritual_ZNK17LocationSingleton15coordToMercatorERK14QGeoCoordinate',
        self._valueOf(coord),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

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
    'LocationSingleton::LocationSingleton(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/locationsingleton.html#LocationSingleton

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  LocationSingleton::LocationSingleton(QObject *parent)
    self._noteCreation(LocationSingleton, lambda: Rituals.call(
        'ritual_ZN17LocationSingletonC1EP7QObject',
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
