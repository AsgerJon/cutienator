"""
QDeclarativeCircleMapItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qdeclarativecirclemapitem_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativeCircleMapItem to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickItem
from . import QDeclarativeGeoMapItemBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF, QRectF
  from ..QtGui import QColor
  from ..QtPositioning import QGeoCoordinate, QGeoShape
  from ..QtQuick import QSGNode
  from . import QDeclarativeGeoMap, QDeclarativeMapLineProperties, QGeoMap
  from . import QGeoMapViewportChangeEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QDeclarativeGeoMap = WAIT['QDeclarativeGeoMap']
  QGeoCoordinate = WAIT['QGeoCoordinate']
  QGeoMap = WAIT['QGeoMap']
  QGeoMapViewportChangeEvent = WAIT['QGeoMapViewportChangeEvent']
  QGeoShape = WAIT['QGeoShape']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']
  QSGNode = WAIT['QSGNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDeclarativeCircleMapItem(QDeclarativeGeoMapItemBase):
  """
  The cute side of Qt's QDeclarativeCircleMapItem: a plain Python object
  standing in front of one C++ QDeclarativeCircleMapItem.

  It is built on the cute 'QDeclarativeGeoMapItemBase', as Qt's
  QDeclarativeCircleMapItem is built on Qt's QDeclarativeGeoMapItemBase, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativeCircleMapItem that has a ritual and that
  Python can call so far, 22 names in all: 'metaObject', 'tr', 'setMap',
  'updateMapItemPaintNode', 'center', 'setCenter', 'radius', 'setRadius',
  'color', 'setColor', 'border', 'contains', 'geoShape', 'setGeoShape',
  'centerChanged', 'radiusChanged', 'colorChanged', 'geometryChange',
  'updatePolish', 'markSourceDirtyAndUpdate', 'onLinePropertiesChanged',
  'afterViewportChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDeclarativeCircleMapItem::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QDeclarativeCircleMapItem::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDeclarativeCircleMapItem::~QDeclarativeCircleMapItem()': the
    destructor: Python never removes a C++ QDeclarativeCircleMapItem.

  What has no ritual
  ------------------

  3 of the 29 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QDeclarativeCircleMapItem is created at the first use, not by
    'QDeclarativeCircleMapItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativeCircleMapItem.
  - Qt tells when it has removed the C++ QDeclarativeCircleMapItem. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QDeclarativeCircleMapItem::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativecirclemapitem.html#tr

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
    #  QString QDeclarativeCircleMapItem::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QDeclarativeCircleMapItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativeCircleMapItem'

  #  A C++ QDeclarativeCircleMapItem Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativeCircleMapItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDeclarativeCircleMapItem::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDeclarativeCircleMapItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QDeclarativeCircleMapItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def radius(self) -> float:
    """
    Calls Qt's 'qreal QDeclarativeCircleMapItem::radius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitem.html#radius
    """
    #  qreal QDeclarativeCircleMapItem::radius() const
    return self.uglySide.call(
        'ritual_ZNK25QDeclarativeCircleMapItem6radiusEv',
    )

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QDeclarativeCircleMapItem::color() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitem.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QDeclarativeCircleMapItem::color() const
    address = self.uglySide.call(
        'ritual_ZNK25QDeclarativeCircleMapItem5colorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload(QPointF)
  def contains(self, point: QPointF) -> bool:
    """
    Calls Qt's 'bool QDeclarativeCircleMapItem::contains(const QPointF
    &point) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitem.html#contains

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QDeclarativeCircleMapItem::contains(const QPointF &point) const
    ritual = 'ritual_ZNK25QDeclarativeCircleMapItem8containsERK7QPointF'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QDeclarativeCircleMapItem8containsERK7QPointF')
    return self.uglySide.call(ritual, self._valueOf(point, 'QPointF'))

  def geoShape(self) -> QGeoShape:
    """
    Calls Qt's 'const QGeoShape &QDeclarativeCircleMapItem::geoShape()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitem.html#geoShape

    Returns
    -------

    QGeoShape
      A new cute QGeoShape around the copy Qt gave back. Python owns it.
    """
    #  const QGeoShape &QDeclarativeCircleMapItem::geoShape() const
    ritual = 'ritual_ZNK25QDeclarativeCircleMapItem8geoShapeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QDeclarativeCircleMapItem8geoShapeEv'
    address = self.uglySide.call(ritual)
    from ..QtPositioning import QGeoShape
    return QGeoShape._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDeclarativeGeoMap, QGeoMap)
  @overload(QDeclarativeGeoMap, NoneType)
  @overload(NoneType, QGeoMap)
  @overload(NoneType, NoneType)
  def setMap(
      self,
      quickMap: Optional[QDeclarativeGeoMap],
      map: Optional[QGeoMap],
  ) -> None:
    """
    Calls Qt's 'void QDeclarativeCircleMapItem::setMap(QDeclarativeGeoMap
    *quickMap, QGeoMap *map)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitem.html#setMap

    Parameters
    ----------

    quickMap : Optional[QDeclarativeGeoMap]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    map : Optional[QGeoMap]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeCircleMapItem::setMap(QDeclarativeGeoMap *quickMap,
    #      QGeoMap *map)
    ritual = (
        'ritual_ZN25QDeclarativeCircleMapItem6setMapEP18QDeclarativeGeoMapP'
        '7QGeoMap')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QDeclarativeCircleMapItem6setMapEP18QDeclarativeG'
          'eoMapP7QGeoMap')
    self.uglySide.call(
        ritual, self._addressOf(quickMap), self._addressOf(map),
    )

  @overload(QGeoCoordinate)
  def setCenter(self, center: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QDeclarativeCircleMapItem::setCenter(const
    QGeoCoordinate &center)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitem.html#setCenter

    Parameters
    ----------

    center : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QDeclarativeCircleMapItem::setCenter(const QGeoCoordinate
    #      &center)
    self.uglySide.call(
        'ritual_ZN25QDeclarativeCircleMapItem9setCenterERK14QGeoCoordinate',
        self._valueOf(center),
    )

  @overload(float)
  def setRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QDeclarativeCircleMapItem::setRadius(qreal radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitem.html#setRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QDeclarativeCircleMapItem::setRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN25QDeclarativeCircleMapItem9setRadiusEd', radius,
    )

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QDeclarativeCircleMapItem::setColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitem.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QDeclarativeCircleMapItem::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN25QDeclarativeCircleMapItem8setColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QGeoShape)
  def setGeoShape(self, shape: QGeoShape) -> None:
    """
    Calls Qt's 'void QDeclarativeCircleMapItem::setGeoShape(const QGeoShape
    &shape)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitem.html#setGeoShape

    Parameters
    ----------

    shape : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.
    """
    #  void QDeclarativeCircleMapItem::setGeoShape(const QGeoShape &shape)
    ritual = 'ritual_ZN25QDeclarativeCircleMapItem11setGeoShapeERK9QGeoShape'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QDeclarativeCircleMapItem11setGeoShapeERK9QGeoSha'
          'pe')
    self.uglySide.call(ritual, self._valueOf(shape))

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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QDeclarativeCircleMapItem::QDeclarativeCircleMapItem(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitem.html

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDeclarativeCircleMapItem::QDeclarativeCircleMapItem(QQuickItem
    #      *parent)
    self._noteCreation(QDeclarativeCircleMapItem, lambda: Rituals.call(
        'ritual_ZN25QDeclarativeCircleMapItemC1EP10QQuickItem',
        self._addressOf(parent),
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

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updateMapItemPaintNode(
      self,
      a0: Optional[QSGNode],
      a1: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode
    *QDeclarativeCircleMapItem::updateMapItemPaintNode(QSGNode *a0,
    UpdatePaintNodeData *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitem.html

    Parameters
    ----------

    a0 : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItem.UpdatePaintNodeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QDeclarativeCircleMapItem::updateMapItemPaintNode(QSGNode
    #      *a0, UpdatePaintNodeData *a1)
    ritual = (
        'ritual_ZN25QDeclarativeCircleMapItem22updateMapItemPaintNodeEP7QSG'
        'NodePN10QQuickItem19UpdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QDeclarativeCircleMapItem22updateMapItemPaintNode'
          'EP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(a0, 'QSGNode'), self._addressOf(a1),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)

  def center(self) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QDeclarativeCircleMapItem::center()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitem.html#center

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QDeclarativeCircleMapItem::center()
    address = self.uglySide.call(
        'ritual_ZN25QDeclarativeCircleMapItem6centerEv',
    )
    from ..QtPositioning import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  def border(self) -> Optional[QDeclarativeMapLineProperties]:
    """
    Calls Qt's 'QDeclarativeMapLineProperties
    *QDeclarativeCircleMapItem::border()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitem.html#border

    Returns
    -------

    Optional[QDeclarativeMapLineProperties]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDeclarativeMapLineProperties *QDeclarativeCircleMapItem::border()
    address = self.uglySide.call(
        'ritual_ZN25QDeclarativeCircleMapItem6borderEv',
    )
    from . import QDeclarativeMapLineProperties
    return QDeclarativeMapLineProperties._cuteAt(address)

  @overload(QGeoCoordinate)
  def centerChanged(self, center: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QDeclarativeCircleMapItem::centerChanged(const
    QGeoCoordinate &center)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitem.html#centerChanged

    Parameters
    ----------

    center : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QDeclarativeCircleMapItem::centerChanged(const QGeoCoordinate
    #      &center)
    self.uglySide.call(
        'ritual_ZN25QDeclarativeCircleMapItem13centerChangedERK14QGeoCoordi'
        'nate',
        self._valueOf(center),
    )

  @overload(float)
  def radiusChanged(self, radius: float) -> None:
    """
    Calls Qt's 'void QDeclarativeCircleMapItem::radiusChanged(qreal radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitem.html#radiusChanged

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QDeclarativeCircleMapItem::radiusChanged(qreal radius)
    self.uglySide.call(
        'ritual_ZN25QDeclarativeCircleMapItem13radiusChangedEd', radius,
    )

  @overload(QColor)
  def colorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QDeclarativeCircleMapItem::colorChanged(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitem.html#colorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QDeclarativeCircleMapItem::colorChanged(const QColor &color)
    self.uglySide.call(
        'ritual_ZN25QDeclarativeCircleMapItem12colorChangedERK6QColor',
        self._valueOf(color),
    )

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QDeclarativeCircleMapItem::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitem.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QDeclarativeCircleMapItem::geometryChange(const QRectF
    #      &newGeometry, const QRectF &oldGeometry)
    ritual = (
        'ritual_ZN25QDeclarativeCircleMapItem14geometryChangeERK6QRectFS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QDeclarativeCircleMapItem14geometryChangeERK6QRec'
          'tFS2_')
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QDeclarativeCircleMapItem::updatePolish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitem.html#updatePolish
    """
    #  void QDeclarativeCircleMapItem::updatePolish()
    ritual = 'ritual_ZN25QDeclarativeCircleMapItem12updatePolishEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QDeclarativeCircleMapItem12updatePolishEv'
    self.uglySide.call(ritual)

  def markSourceDirtyAndUpdate(self) -> None:
    """
    Calls Qt's 'void QDeclarativeCircleMapItem::markSourceDirtyAndUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitem.html
    """
    #  void QDeclarativeCircleMapItem::markSourceDirtyAndUpdate()
    self.uglySide.call(
        'ritual_ZN25QDeclarativeCircleMapItem24markSourceDirtyAndUpdateEv',
    )

  def onLinePropertiesChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeCircleMapItem::onLinePropertiesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitem.html
    """
    #  void QDeclarativeCircleMapItem::onLinePropertiesChanged()
    self.uglySide.call(
        'ritual_ZN25QDeclarativeCircleMapItem23onLinePropertiesChangedEv',
    )

  @overload(QGeoMapViewportChangeEvent)
  def afterViewportChanged(self, event: QGeoMapViewportChangeEvent) -> None:
    """
    Calls Qt's 'void QDeclarativeCircleMapItem::afterViewportChanged(const
    QGeoMapViewportChangeEvent &event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitem.html

    Parameters
    ----------

    event : QGeoMapViewportChangeEvent
      Passed on as a value: Qt reads the C++ QGeoMapViewportChangeEvent,
      which stays Python's own.
    """
    #  void QDeclarativeCircleMapItem::afterViewportChanged(const
    #      QGeoMapViewportChangeEvent &event)
    ritual = (
        'ritual_ZN25QDeclarativeCircleMapItem20afterViewportChangedERK26QGe'
        'oMapViewportChangeEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QDeclarativeCircleMapItem20afterViewportChangedER'
          'K26QGeoMapViewportChangeEvent')
    self.uglySide.call(ritual, self._valueOf(event))
