"""
QDeclarativeGeoMapQuickItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qdeclarativegeomapquickitem_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativeGeoMapQuickItem to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
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
  from ..QtPositioning import QGeoCoordinate, QGeoShape
  from . import QDeclarativeGeoMap, QGeoMap, QGeoMapViewportChangeEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeclarativeGeoMap = WAIT['QDeclarativeGeoMap']
  QGeoCoordinate = WAIT['QGeoCoordinate']
  QGeoMap = WAIT['QGeoMap']
  QGeoMapViewportChangeEvent = WAIT['QGeoMapViewportChangeEvent']
  QGeoShape = WAIT['QGeoShape']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDeclarativeGeoMapQuickItem(QDeclarativeGeoMapItemBase):
  """
  The cute side of Qt's QDeclarativeGeoMapQuickItem: a plain Python object
  standing in front of one C++ QDeclarativeGeoMapQuickItem.

  It is built on the cute 'QDeclarativeGeoMapItemBase', as Qt's
  QDeclarativeGeoMapQuickItem is built on Qt's QDeclarativeGeoMapItemBase,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativeGeoMapQuickItem that has a ritual and
  that Python can call so far, 23 names in all: 'metaObject', 'tr', 'setMap',
  'setCoordinate', 'coordinate', 'setSourceItem', 'sourceItem',
  'setAnchorPoint', 'anchorPoint', 'setZoomLevel', 'zoomLevel', 'geoShape',
  'setGeoShape', 'contains', 'coordinateChanged', 'sourceItemChanged',
  'anchorPointChanged', 'zoomLevelChanged', 'geometryChange', 'updatePolish',
  'afterChildrenChanged', 'afterViewportChanged', 'scaleFactor'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDeclarativeGeoMapQuickItem::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QDeclarativeGeoMapQuickItem::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDeclarativeGeoMapQuickItem::~QDeclarativeGeoMapQuickItem()': the
    destructor: Python never removes a C++ QDeclarativeGeoMapQuickItem.

  What has no ritual
  ------------------

  2 of the 29 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDeclarativeGeoMapQuickItem is created at the first use, not by
    'QDeclarativeGeoMapQuickItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativeGeoMapQuickItem.
  - Qt tells when it has removed the C++ QDeclarativeGeoMapQuickItem. Every
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
    Calls Qt's 'QString QDeclarativeGeoMapQuickItem::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapquickitem.html#tr

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
    #  QString QDeclarativeGeoMapQuickItem::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN27QDeclarativeGeoMapQuickItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativeGeoMapQuickItem'

  #  A C++ QDeclarativeGeoMapQuickItem Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativeGeoMapQuickItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDeclarativeGeoMapQuickItem::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapquickitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDeclarativeGeoMapQuickItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QDeclarativeGeoMapQuickItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def anchorPoint(self) -> QPointF:
    """
    Calls Qt's 'QPointF QDeclarativeGeoMapQuickItem::anchorPoint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapquickitem.html#anchorPoint

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QDeclarativeGeoMapQuickItem::anchorPoint() const
    address = self.uglySide.call(
        'ritual_ZNK27QDeclarativeGeoMapQuickItem11anchorPointEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def zoomLevel(self) -> float:
    """
    Calls Qt's 'qreal QDeclarativeGeoMapQuickItem::zoomLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapquickitem.html#zoomLevel
    """
    #  qreal QDeclarativeGeoMapQuickItem::zoomLevel() const
    return self.uglySide.call(
        'ritual_ZNK27QDeclarativeGeoMapQuickItem9zoomLevelEv',
    )

  def geoShape(self) -> QGeoShape:
    """
    Calls Qt's 'const QGeoShape &QDeclarativeGeoMapQuickItem::geoShape()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapquickitem.html#geoShape

    Returns
    -------

    QGeoShape
      A new cute QGeoShape around the copy Qt gave back. Python owns it.
    """
    #  const QGeoShape &QDeclarativeGeoMapQuickItem::geoShape() const
    ritual = 'ritual_ZNK27QDeclarativeGeoMapQuickItem8geoShapeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK27QDeclarativeGeoMapQuickItem8geoShapeEv'
    address = self.uglySide.call(ritual)
    from ..QtPositioning import QGeoShape
    return QGeoShape._cuteOwning(address)

  @overload(QPointF)
  def contains(self, point: QPointF) -> bool:
    """
    Calls Qt's 'bool QDeclarativeGeoMapQuickItem::contains(const QPointF
    &point) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapquickitem.html#contains

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QDeclarativeGeoMapQuickItem::contains(const QPointF &point) const
    ritual = 'ritual_ZNK27QDeclarativeGeoMapQuickItem8containsERK7QPointF'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK27QDeclarativeGeoMapQuickItem8containsERK7QPointF')
    return self.uglySide.call(ritual, self._valueOf(point, 'QPointF'))

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
    Calls Qt's 'void QDeclarativeGeoMapQuickItem::setMap(QDeclarativeGeoMap
    *quickMap, QGeoMap *map)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapquickitem.html#setMap

    Parameters
    ----------

    quickMap : Optional[QDeclarativeGeoMap]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    map : Optional[QGeoMap]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeGeoMapQuickItem::setMap(QDeclarativeGeoMap *quickMap,
    #      QGeoMap *map)
    ritual = (
        'ritual_ZN27QDeclarativeGeoMapQuickItem6setMapEP18QDeclarativeGeoMa'
        'pP7QGeoMap')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QDeclarativeGeoMapQuickItem6setMapEP18QDeclarativ'
          'eGeoMapP7QGeoMap')
    self.uglySide.call(
        ritual, self._addressOf(quickMap), self._addressOf(map),
    )

  @overload(QGeoCoordinate)
  def setCoordinate(self, coordinate: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapQuickItem::setCoordinate(const
    QGeoCoordinate &coordinate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapquickitem.html#setCoordinate

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QDeclarativeGeoMapQuickItem::setCoordinate(const QGeoCoordinate
    #      &coordinate)
    self.uglySide.call(
        'ritual_ZN27QDeclarativeGeoMapQuickItem13setCoordinateERK14QGeoCoor'
        'dinate',
        self._valueOf(coordinate),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setSourceItem(self, sourceItem: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapQuickItem::setSourceItem(QQuickItem
    *sourceItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapquickitem.html#setSourceItem

    Parameters
    ----------

    sourceItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeGeoMapQuickItem::setSourceItem(QQuickItem
    #      *sourceItem)
    self.uglySide.call(
        'ritual_ZN27QDeclarativeGeoMapQuickItem13setSourceItemEP10QQuickIte'
        'm',
        self._addressOf(sourceItem),
    )

  @overload(QPointF)
  def setAnchorPoint(self, anchorPoint: QPointF) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapQuickItem::setAnchorPoint(const
    QPointF &anchorPoint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapquickitem.html#setAnchorPoint

    Parameters
    ----------

    anchorPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QDeclarativeGeoMapQuickItem::setAnchorPoint(const QPointF
    #      &anchorPoint)
    self.uglySide.call(
        'ritual_ZN27QDeclarativeGeoMapQuickItem14setAnchorPointERK7QPointF',
        self._valueOf(anchorPoint, 'QPointF'),
    )

  @overload(float)
  def setZoomLevel(self, zoomLevel: float) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapQuickItem::setZoomLevel(qreal
    zoomLevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapquickitem.html#setZoomLevel

    Parameters
    ----------

    zoomLevel : float
      Passed on as it is.
    """
    #  void QDeclarativeGeoMapQuickItem::setZoomLevel(qreal zoomLevel)
    self.uglySide.call(
        'ritual_ZN27QDeclarativeGeoMapQuickItem12setZoomLevelEd', zoomLevel,
    )

  @overload(QGeoShape)
  def setGeoShape(self, shape: QGeoShape) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapQuickItem::setGeoShape(const QGeoShape
    &shape)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapquickitem.html#setGeoShape

    Parameters
    ----------

    shape : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.
    """
    #  void QDeclarativeGeoMapQuickItem::setGeoShape(const QGeoShape &shape)
    ritual = (
        'ritual_ZN27QDeclarativeGeoMapQuickItem11setGeoShapeERK9QGeoShape')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QDeclarativeGeoMapQuickItem11setGeoShapeERK9QGeoS'
          'hape')
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
    'QDeclarativeGeoMapQuickItem::QDeclarativeGeoMapQuickItem(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapquickitem.html

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDeclarativeGeoMapQuickItem::QDeclarativeGeoMapQuickItem(QQuickItem
    #      *parent)
    self._noteCreation(QDeclarativeGeoMapQuickItem, lambda: Rituals.call(
        'ritual_ZN27QDeclarativeGeoMapQuickItemC1EP10QQuickItem',
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

  def coordinate(self) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QDeclarativeGeoMapQuickItem::coordinate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapquickitem.html#coordinate

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QDeclarativeGeoMapQuickItem::coordinate()
    address = self.uglySide.call(
        'ritual_ZN27QDeclarativeGeoMapQuickItem10coordinateEv',
    )
    from ..QtPositioning import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  def sourceItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QDeclarativeGeoMapQuickItem::sourceItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapquickitem.html#sourceItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QDeclarativeGeoMapQuickItem::sourceItem()
    address = self.uglySide.call(
        'ritual_ZN27QDeclarativeGeoMapQuickItem10sourceItemEv',
    )
    return QQuickItem._cuteAt(address)

  def coordinateChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapQuickItem::coordinateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapquickitem.html#coordinateChanged
    """
    #  void QDeclarativeGeoMapQuickItem::coordinateChanged()
    self.uglySide.call(
        'ritual_ZN27QDeclarativeGeoMapQuickItem17coordinateChangedEv',
    )

  def sourceItemChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapQuickItem::sourceItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapquickitem.html#sourceItemChanged
    """
    #  void QDeclarativeGeoMapQuickItem::sourceItemChanged()
    self.uglySide.call(
        'ritual_ZN27QDeclarativeGeoMapQuickItem17sourceItemChangedEv',
    )

  def anchorPointChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapQuickItem::anchorPointChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapquickitem.html
    """
    #  void QDeclarativeGeoMapQuickItem::anchorPointChanged()
    self.uglySide.call(
        'ritual_ZN27QDeclarativeGeoMapQuickItem18anchorPointChangedEv',
    )

  def zoomLevelChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapQuickItem::zoomLevelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapquickitem.html#zoomLevelChanged
    """
    #  void QDeclarativeGeoMapQuickItem::zoomLevelChanged()
    self.uglySide.call(
        'ritual_ZN27QDeclarativeGeoMapQuickItem16zoomLevelChangedEv',
    )

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapQuickItem::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapquickitem.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QDeclarativeGeoMapQuickItem::geometryChange(const QRectF
    #      &newGeometry, const QRectF &oldGeometry)
    ritual = (
        'ritual_ZN27QDeclarativeGeoMapQuickItem14geometryChangeERK6QRectFS2'
        '_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QDeclarativeGeoMapQuickItem14geometryChangeERK6QR'
          'ectFS2_')
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapQuickItem::updatePolish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapquickitem.html#updatePolish
    """
    #  void QDeclarativeGeoMapQuickItem::updatePolish()
    ritual = 'ritual_ZN27QDeclarativeGeoMapQuickItem12updatePolishEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QDeclarativeGeoMapQuickItem12updatePolishEv'
    self.uglySide.call(ritual)

  def afterChildrenChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapQuickItem::afterChildrenChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapquickitem.html
    """
    #  void QDeclarativeGeoMapQuickItem::afterChildrenChanged()
    ritual = 'ritual_ZN27QDeclarativeGeoMapQuickItem20afterChildrenChangedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QDeclarativeGeoMapQuickItem20afterChildrenChanged'
          'Ev')
    self.uglySide.call(ritual)

  @overload(QGeoMapViewportChangeEvent)
  def afterViewportChanged(self, event: QGeoMapViewportChangeEvent) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapQuickItem::afterViewportChanged(const
    QGeoMapViewportChangeEvent &event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapquickitem.html

    Parameters
    ----------

    event : QGeoMapViewportChangeEvent
      Passed on as a value: Qt reads the C++ QGeoMapViewportChangeEvent,
      which stays Python's own.
    """
    #  void QDeclarativeGeoMapQuickItem::afterViewportChanged(const
    #      QGeoMapViewportChangeEvent &event)
    ritual = (
        'ritual_ZN27QDeclarativeGeoMapQuickItem20afterViewportChangedERK26Q'
        'GeoMapViewportChangeEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QDeclarativeGeoMapQuickItem20afterViewportChanged'
          'ERK26QGeoMapViewportChangeEvent')
    self.uglySide.call(ritual, self._valueOf(event))

  def scaleFactor(self) -> float:
    """
    Calls Qt's 'qreal QDeclarativeGeoMapQuickItem::scaleFactor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapquickitem.html#scaleFactor
    """
    #  qreal QDeclarativeGeoMapQuickItem::scaleFactor()
    return self.uglySide.call(
        'ritual_ZN27QDeclarativeGeoMapQuickItem11scaleFactorEv',
    )
