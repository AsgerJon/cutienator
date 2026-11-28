"""
QDeclarativePolygonMapItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qdeclarativepolygonmapitem_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativePolygonMapItem to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
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


class QDeclarativePolygonMapItem(QDeclarativeGeoMapItemBase):
  """
  The cute side of Qt's QDeclarativePolygonMapItem: a plain Python object
  standing in front of one C++ QDeclarativePolygonMapItem.

  It is built on the cute 'QDeclarativeGeoMapItemBase', as Qt's
  QDeclarativePolygonMapItem is built on Qt's QDeclarativeGeoMapItemBase, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativePolygonMapItem that has a ritual and
  that Python can call so far, 21 names in all: 'metaObject', 'tr', 'setMap',
  'updateMapItemPaintNode', 'addCoordinate', 'removeCoordinate', 'path',
  'setPath', 'color', 'setColor', 'border', 'contains', 'geoShape',
  'setGeoShape', 'pathChanged', 'colorChanged', 'markSourceDirtyAndUpdate',
  'onLinePropertiesChanged', 'afterViewportChanged', 'geometryChange',
  'updatePolish'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDeclarativePolygonMapItem::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QDeclarativePolygonMapItem::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDeclarativePolygonMapItem::~QDeclarativePolygonMapItem()': the
    destructor: Python never removes a C++ QDeclarativePolygonMapItem.

  What has no ritual
  ------------------

  2 of the 27 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDeclarativePolygonMapItem is created at the first use, not by
    'QDeclarativePolygonMapItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativePolygonMapItem.
  - Qt tells when it has removed the C++ QDeclarativePolygonMapItem. Every
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
    Calls Qt's 'QString QDeclarativePolygonMapItem::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativepolygonmapitem.html#tr

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
    #  QString QDeclarativePolygonMapItem::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QDeclarativePolygonMapItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativePolygonMapItem'

  #  A C++ QDeclarativePolygonMapItem Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativePolygonMapItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDeclarativePolygonMapItem::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDeclarativePolygonMapItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QDeclarativePolygonMapItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def path(self) -> QList[QGeoCoordinate]:
    """
    Calls Qt's 'QList<QGeoCoordinate> QDeclarativePolygonMapItem::path()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitem.html#path

    Returns
    -------

    QList[QGeoCoordinate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGeoCoordinate> QDeclarativePolygonMapItem::path() const
    address = self.uglySide.call(
        'ritual_ZNK26QDeclarativePolygonMapItem4pathEv',
    )
    from ..QtPositioning import QGeoCoordinate
    return QList[QGeoCoordinate]._cuteOwning(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QDeclarativePolygonMapItem::color() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitem.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QDeclarativePolygonMapItem::color() const
    address = self.uglySide.call(
        'ritual_ZNK26QDeclarativePolygonMapItem5colorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload(QPointF)
  def contains(self, point: QPointF) -> bool:
    """
    Calls Qt's 'bool QDeclarativePolygonMapItem::contains(const QPointF
    &point) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitem.html#contains

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QDeclarativePolygonMapItem::contains(const QPointF &point) const
    ritual = 'ritual_ZNK26QDeclarativePolygonMapItem8containsERK7QPointF'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK26QDeclarativePolygonMapItem8containsERK7QPointF')
    return self.uglySide.call(ritual, self._valueOf(point, 'QPointF'))

  def geoShape(self) -> QGeoShape:
    """
    Calls Qt's 'const QGeoShape &QDeclarativePolygonMapItem::geoShape()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitem.html#geoShape

    Returns
    -------

    QGeoShape
      A new cute QGeoShape around the copy Qt gave back. Python owns it.
    """
    #  const QGeoShape &QDeclarativePolygonMapItem::geoShape() const
    ritual = 'ritual_ZNK26QDeclarativePolygonMapItem8geoShapeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QDeclarativePolygonMapItem8geoShapeEv'
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
    Calls Qt's 'void QDeclarativePolygonMapItem::setMap(QDeclarativeGeoMap
    *quickMap, QGeoMap *map)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitem.html#setMap

    Parameters
    ----------

    quickMap : Optional[QDeclarativeGeoMap]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    map : Optional[QGeoMap]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativePolygonMapItem::setMap(QDeclarativeGeoMap *quickMap,
    #      QGeoMap *map)
    ritual = (
        'ritual_ZN26QDeclarativePolygonMapItem6setMapEP18QDeclarativeGeoMap'
        'P7QGeoMap')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QDeclarativePolygonMapItem6setMapEP18QDeclarative'
          'GeoMapP7QGeoMap')
    self.uglySide.call(
        ritual, self._addressOf(quickMap), self._addressOf(map),
    )

  @overload(QList[QGeoCoordinate])
  def setPath(self, value: QList[QGeoCoordinate]) -> None:
    """
    Calls Qt's 'void QDeclarativePolygonMapItem::setPath(const
    QList<QGeoCoordinate> &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitem.html#setPath

    Parameters
    ----------

    value : QList[QGeoCoordinate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDeclarativePolygonMapItem::setPath(const QList<QGeoCoordinate>
    #      &value)
    self.uglySide.call(
        'ritual_ZN26QDeclarativePolygonMapItem7setPathERK5QListI14QGeoCoord'
        'inateE',
        self._valueOf(value),
    )

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QDeclarativePolygonMapItem::setColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitem.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QDeclarativePolygonMapItem::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN26QDeclarativePolygonMapItem8setColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QGeoShape)
  def setGeoShape(self, shape: QGeoShape) -> None:
    """
    Calls Qt's 'void QDeclarativePolygonMapItem::setGeoShape(const QGeoShape
    &shape)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitem.html#setGeoShape

    Parameters
    ----------

    shape : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.
    """
    #  void QDeclarativePolygonMapItem::setGeoShape(const QGeoShape &shape)
    ritual = (
        'ritual_ZN26QDeclarativePolygonMapItem11setGeoShapeERK9QGeoShape')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QDeclarativePolygonMapItem11setGeoShapeERK9QGeoSh'
          'ape')
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
    'QDeclarativePolygonMapItem::QDeclarativePolygonMapItem(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitem.html

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDeclarativePolygonMapItem::QDeclarativePolygonMapItem(QQuickItem
    #      *parent)
    self._noteCreation(QDeclarativePolygonMapItem, lambda: Rituals.call(
        'ritual_ZN26QDeclarativePolygonMapItemC1EP10QQuickItem',
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
    *QDeclarativePolygonMapItem::updateMapItemPaintNode(QSGNode *a0,
    UpdatePaintNodeData *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitem.html

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
    #  QSGNode *QDeclarativePolygonMapItem::updateMapItemPaintNode(QSGNode
    #      *a0, UpdatePaintNodeData *a1)
    ritual = (
        'ritual_ZN26QDeclarativePolygonMapItem22updateMapItemPaintNodeEP7QS'
        'GNodePN10QQuickItem19UpdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QDeclarativePolygonMapItem22updateMapItemPaintNod'
          'eEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(a0, 'QSGNode'), self._addressOf(a1),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)

  @overload(QGeoCoordinate)
  def addCoordinate(self, coordinate: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QDeclarativePolygonMapItem::addCoordinate(const
    QGeoCoordinate &coordinate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitem.html#addCoordinate

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QDeclarativePolygonMapItem::addCoordinate(const QGeoCoordinate
    #      &coordinate)
    self.uglySide.call(
        'ritual_ZN26QDeclarativePolygonMapItem13addCoordinateERK14QGeoCoord'
        'inate',
        self._valueOf(coordinate),
    )

  @overload(QGeoCoordinate)
  def removeCoordinate(self, coordinate: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QDeclarativePolygonMapItem::removeCoordinate(const
    QGeoCoordinate &coordinate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitem.html#removeCoordinate

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QDeclarativePolygonMapItem::removeCoordinate(const QGeoCoordinate
    #      &coordinate)
    self.uglySide.call(
        'ritual_ZN26QDeclarativePolygonMapItem16removeCoordinateERK14QGeoCo'
        'ordinate',
        self._valueOf(coordinate),
    )

  def border(self) -> Optional[QDeclarativeMapLineProperties]:
    """
    Calls Qt's 'QDeclarativeMapLineProperties
    *QDeclarativePolygonMapItem::border()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitem.html#border

    Returns
    -------

    Optional[QDeclarativeMapLineProperties]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDeclarativeMapLineProperties *QDeclarativePolygonMapItem::border()
    address = self.uglySide.call(
        'ritual_ZN26QDeclarativePolygonMapItem6borderEv',
    )
    from . import QDeclarativeMapLineProperties
    return QDeclarativeMapLineProperties._cuteAt(address)

  def pathChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePolygonMapItem::pathChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitem.html#pathChanged
    """
    #  void QDeclarativePolygonMapItem::pathChanged()
    self.uglySide.call(
        'ritual_ZN26QDeclarativePolygonMapItem11pathChangedEv',
    )

  @overload(QColor)
  def colorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QDeclarativePolygonMapItem::colorChanged(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitem.html#colorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QDeclarativePolygonMapItem::colorChanged(const QColor &color)
    self.uglySide.call(
        'ritual_ZN26QDeclarativePolygonMapItem12colorChangedERK6QColor',
        self._valueOf(color),
    )

  def markSourceDirtyAndUpdate(self) -> None:
    """
    Calls Qt's 'void QDeclarativePolygonMapItem::markSourceDirtyAndUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitem.html
    """
    #  void QDeclarativePolygonMapItem::markSourceDirtyAndUpdate()
    self.uglySide.call(
        'ritual_ZN26QDeclarativePolygonMapItem24markSourceDirtyAndUpdateEv',
    )

  def onLinePropertiesChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePolygonMapItem::onLinePropertiesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitem.html
    """
    #  void QDeclarativePolygonMapItem::onLinePropertiesChanged()
    self.uglySide.call(
        'ritual_ZN26QDeclarativePolygonMapItem23onLinePropertiesChangedEv',
    )

  @overload(QGeoMapViewportChangeEvent)
  def afterViewportChanged(self, event: QGeoMapViewportChangeEvent) -> None:
    """
    Calls Qt's 'void QDeclarativePolygonMapItem::afterViewportChanged(const
    QGeoMapViewportChangeEvent &event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitem.html

    Parameters
    ----------

    event : QGeoMapViewportChangeEvent
      Passed on as a value: Qt reads the C++ QGeoMapViewportChangeEvent,
      which stays Python's own.
    """
    #  void QDeclarativePolygonMapItem::afterViewportChanged(const
    #      QGeoMapViewportChangeEvent &event)
    ritual = (
        'ritual_ZN26QDeclarativePolygonMapItem20afterViewportChangedERK26QG'
        'eoMapViewportChangeEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QDeclarativePolygonMapItem20afterViewportChangedE'
          'RK26QGeoMapViewportChangeEvent')
    self.uglySide.call(ritual, self._valueOf(event))

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QDeclarativePolygonMapItem::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitem.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QDeclarativePolygonMapItem::geometryChange(const QRectF
    #      &newGeometry, const QRectF &oldGeometry)
    ritual = (
        'ritual_ZN26QDeclarativePolygonMapItem14geometryChangeERK6QRectFS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QDeclarativePolygonMapItem14geometryChangeERK6QRe'
          'ctFS2_')
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QDeclarativePolygonMapItem::updatePolish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitem.html#updatePolish
    """
    #  void QDeclarativePolygonMapItem::updatePolish()
    ritual = 'ritual_ZN26QDeclarativePolygonMapItem12updatePolishEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QDeclarativePolygonMapItem12updatePolishEv'
    self.uglySide.call(ritual)
