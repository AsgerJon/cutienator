"""
ScatterChartItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/scatterchartitem_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means ScatterChartItem to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtWidgets import QGraphicsItem
from . import XYChart

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF
  from ..QtGui import QBrush, QPainter, QPen
  from ..QtWidgets import QGraphicsSceneHoverEvent, QGraphicsSceneMouseEvent
  from ..QtWidgets import QStyleOptionGraphicsItem, QWidget
  from . import QScatterSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QGraphicsSceneHoverEvent = WAIT['QGraphicsSceneHoverEvent']
  QGraphicsSceneMouseEvent = WAIT['QGraphicsSceneMouseEvent']
  QPainter = WAIT['QPainter']
  QPen = WAIT['QPen']
  QScatterSeries = WAIT['QtCharts:QScatterSeries']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ScatterChartItem(XYChart):
  """
  The cute side of Qt's ScatterChartItem: a plain Python object standing in
  front of one C++ ScatterChartItem.

  It is built on the cute 'XYChart', as Qt's ScatterChartItem is built on
  Qt's XYChart, and has everything that class has.

  What exists
  -----------

  Every function of Qt's ScatterChartItem that has a ritual and that Python
  can call so far, 23 names in all: 'metaObject', 'tr', 'boundingRect',
  'paint', 'setPen', 'setBrush', 'markerSelected', 'markerHovered',
  'markerPressed', 'markerReleased', 'markerDoubleClicked',
  'handleMarkerMouseReleaseEvent', 'setMousePressed', 'mousePressed',
  'handleSeriesUpdated', 'createPoints', 'deletePoints', 'resizeMarker',
  'updateGeometry', 'mousePressEvent', 'hoverMoveEvent', 'mouseReleaseEvent',
  'mouseDoubleClickEvent'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *ScatterChartItem::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int ScatterChartItem::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 28 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ ScatterChartItem is created at the first use, not by
    'ScatterChartItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ ScatterChartItem.
  - Qt tells when it has removed the C++ ScatterChartItem. Every call on the
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
    Calls Qt's 'QString ScatterChartItem::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/scatterchartitem.html#tr

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
    #  QString ScatterChartItem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16ScatterChartItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'ScatterChartItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *ScatterChartItem::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/scatterchartitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *ScatterChartItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16ScatterChartItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF ScatterChartItem::boundingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/scatterchartitem.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF ScatterChartItem::boundingRect() const
    ritual = 'ritual_ZNK16ScatterChartItem12boundingRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16ScatterChartItem12boundingRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPen)
  def setPen(self, pen: QPen) -> None:
    """
    Calls Qt's 'void ScatterChartItem::setPen(const QPen &pen)'.

    Qt's own words: https://doc.qt.io/qt-6/scatterchartitem.html#setPen

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void ScatterChartItem::setPen(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN16ScatterChartItem6setPenERK4QPen', self._valueOf(pen),
    )

  @overload(QBrush)
  def setBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void ScatterChartItem::setBrush(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/scatterchartitem.html#setBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void ScatterChartItem::setBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN16ScatterChartItem8setBrushERK6QBrush',
        self._valueOf(brush),
    )

  @overload()
  @overload(bool)
  def setMousePressed(self, pressed: bool = True) -> None:
    """
    Calls Qt's 'void ScatterChartItem::setMousePressed(bool pressed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterchartitem.html#setMousePressed

    Parameters
    ----------

    pressed : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void ScatterChartItem::setMousePressed(bool pressed)
    self.uglySide.call(
        'ritual_ZN16ScatterChartItem15setMousePressedEb', pressed,
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

  @overload(QScatterSeries)
  @overload(NoneType)
  @overload(QScatterSeries, QGraphicsItem)
  @overload(QScatterSeries, NoneType)
  @overload(NoneType, QGraphicsItem)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      series: Optional[QScatterSeries],
      item: Optional[QGraphicsItem] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'ScatterChartItem::ScatterChartItem(QScatterSeries *series, QGraphicsItem
    *item)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterchartitem.html#ScatterChartItem

    Parameters
    ----------

    series : Optional[QScatterSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  ScatterChartItem::ScatterChartItem(QScatterSeries *series,
    #      QGraphicsItem *item)
    self._noteCreation(ScatterChartItem, lambda: Rituals.call(
        'ritual_ZN16ScatterChartItemC1EP14QScatterSeriesP13QGraphicsItem',
        self._addressOf(series), self._addressOf(item, 'QGraphicsItem'),
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

  @overload(QPainter, QStyleOptionGraphicsItem, QWidget)
  @overload(QPainter, QStyleOptionGraphicsItem, NoneType)
  @overload(QPainter, NoneType, QWidget)
  @overload(QPainter, NoneType, NoneType)
  @overload(NoneType, QStyleOptionGraphicsItem, QWidget)
  @overload(NoneType, QStyleOptionGraphicsItem, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  def paint(
      self,
      painter: Optional[QPainter],
      option: Optional[QStyleOptionGraphicsItem],
      widget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void ScatterChartItem::paint(QPainter *painter, const
    QStyleOptionGraphicsItem *option, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/scatterchartitem.html#paint

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    option : Optional[QStyleOptionGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ScatterChartItem::paint(QPainter *painter, const
    #      QStyleOptionGraphicsItem *option, QWidget *widget)
    ritual = (
        'ritual_ZN16ScatterChartItem5paintEP8QPainterPK24QStyleOptionGraphi'
        'csItemP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16ScatterChartItem5paintEP8QPainterPK24QStyleOption'
          'GraphicsItemP7QWidget')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._addressOf(option),
        self._addressOf(widget),
    )

  @overload(QGraphicsItem)
  @overload(NoneType)
  def markerSelected(self, item: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void ScatterChartItem::markerSelected(QGraphicsItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterchartitem.html#markerSelected

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ScatterChartItem::markerSelected(QGraphicsItem *item)
    self.uglySide.call(
        'ritual_ZN16ScatterChartItem14markerSelectedEP13QGraphicsItem',
        self._addressOf(item, 'QGraphicsItem'),
    )

  @overload(QGraphicsItem, bool)
  @overload(NoneType, bool)
  def markerHovered(
      self,
      item: Optional[QGraphicsItem],
      state: bool,
  ) -> None:
    """
    Calls Qt's 'void ScatterChartItem::markerHovered(QGraphicsItem *item,
    bool state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterchartitem.html#markerHovered

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    state : bool
      Passed on as it is.
    """
    #  void ScatterChartItem::markerHovered(QGraphicsItem *item, bool state)
    self.uglySide.call(
        'ritual_ZN16ScatterChartItem13markerHoveredEP13QGraphicsItemb',
        self._addressOf(item, 'QGraphicsItem'), state,
    )

  @overload(QGraphicsItem)
  @overload(NoneType)
  def markerPressed(self, item: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void ScatterChartItem::markerPressed(QGraphicsItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterchartitem.html#markerPressed

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ScatterChartItem::markerPressed(QGraphicsItem *item)
    self.uglySide.call(
        'ritual_ZN16ScatterChartItem13markerPressedEP13QGraphicsItem',
        self._addressOf(item, 'QGraphicsItem'),
    )

  @overload(QGraphicsItem)
  @overload(NoneType)
  def markerReleased(self, item: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void ScatterChartItem::markerReleased(QGraphicsItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterchartitem.html#markerReleased

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ScatterChartItem::markerReleased(QGraphicsItem *item)
    self.uglySide.call(
        'ritual_ZN16ScatterChartItem14markerReleasedEP13QGraphicsItem',
        self._addressOf(item, 'QGraphicsItem'),
    )

  @overload(QGraphicsItem)
  @overload(NoneType)
  def markerDoubleClicked(self, item: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void ScatterChartItem::markerDoubleClicked(QGraphicsItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterchartitem.html#markerDoubleClicked

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ScatterChartItem::markerDoubleClicked(QGraphicsItem *item)
    self.uglySide.call(
        'ritual_ZN16ScatterChartItem19markerDoubleClickedEP13QGraphicsItem',
        self._addressOf(item, 'QGraphicsItem'),
    )

  @overload(QGraphicsItem)
  @overload(NoneType)
  def handleMarkerMouseReleaseEvent(
      self,
      item: Optional[QGraphicsItem],
  ) -> None:
    """
    Calls Qt's 'void
    ScatterChartItem::handleMarkerMouseReleaseEvent(QGraphicsItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterchartitem.html

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ScatterChartItem::handleMarkerMouseReleaseEvent(QGraphicsItem
    #      *item)
    self.uglySide.call(
        'ritual_ZN16ScatterChartItem29handleMarkerMouseReleaseEventEP13QGra'
        'phicsItem',
        self._addressOf(item, 'QGraphicsItem'),
    )

  def mousePressed(self) -> bool:
    """
    Calls Qt's 'bool ScatterChartItem::mousePressed()'.

    Qt's own words: https://doc.qt.io/qt-6/scatterchartitem.html#mousePressed
    """
    #  bool ScatterChartItem::mousePressed()
    return self.uglySide.call('ritual_ZN16ScatterChartItem12mousePressedEv')

  def handleSeriesUpdated(self) -> None:
    """
    Calls Qt's 'void ScatterChartItem::handleSeriesUpdated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterchartitem.html#handleSeriesUpdated
    """
    #  void ScatterChartItem::handleSeriesUpdated()
    ritual = 'ritual_ZN16ScatterChartItem19handleSeriesUpdatedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16ScatterChartItem19handleSeriesUpdatedEv'
    self.uglySide.call(ritual)

  @overload(int)
  def createPoints(self, count: int) -> None:
    """
    Calls Qt's 'void ScatterChartItem::createPoints(int count)'.

    Qt's own words: https://doc.qt.io/qt-6/scatterchartitem.html#createPoints

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void ScatterChartItem::createPoints(int count)
    self.uglySide.call('ritual_ZN16ScatterChartItem12createPointsEi', count)

  @overload(int)
  def deletePoints(self, count: int) -> None:
    """
    Calls Qt's 'void ScatterChartItem::deletePoints(int count)'.

    Qt's own words: https://doc.qt.io/qt-6/scatterchartitem.html#deletePoints

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void ScatterChartItem::deletePoints(int count)
    self.uglySide.call('ritual_ZN16ScatterChartItem12deletePointsEi', count)

  @overload(QGraphicsItem, int)
  @overload(NoneType, int)
  def resizeMarker(self, marker: Optional[QGraphicsItem], size: int) -> None:
    """
    Calls Qt's 'void ScatterChartItem::resizeMarker(QGraphicsItem *marker,
    const int size)'.

    Qt's own words: https://doc.qt.io/qt-6/scatterchartitem.html#resizeMarker

    Parameters
    ----------

    marker : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    size : int
      Passed on as it is.
    """
    #  void ScatterChartItem::resizeMarker(QGraphicsItem *marker, const int
    #      size)
    self.uglySide.call(
        'ritual_ZN16ScatterChartItem12resizeMarkerEP13QGraphicsItemi',
        self._addressOf(marker, 'QGraphicsItem'), size,
    )

  def updateGeometry(self) -> None:
    """
    Calls Qt's 'void ScatterChartItem::updateGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterchartitem.html#updateGeometry
    """
    #  void ScatterChartItem::updateGeometry()
    ritual = 'ritual_ZN16ScatterChartItem14updateGeometryEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16ScatterChartItem14updateGeometryEv'
    self.uglySide.call(ritual)

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mousePressEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void
    ScatterChartItem::mousePressEvent(QGraphicsSceneMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterchartitem.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ScatterChartItem::mousePressEvent(QGraphicsSceneMouseEvent
    #      *event)
    ritual = (
        'ritual_ZN16ScatterChartItem15mousePressEventEP24QGraphicsSceneMous'
        'eEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16ScatterChartItem15mousePressEventEP24QGraphicsSce'
          'neMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverMoveEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void
    ScatterChartItem::hoverMoveEvent(QGraphicsSceneHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterchartitem.html#hoverMoveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ScatterChartItem::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
    ritual = (
        'ritual_ZN16ScatterChartItem14hoverMoveEventEP24QGraphicsSceneHover'
        'Event')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16ScatterChartItem14hoverMoveEventEP24QGraphicsScen'
          'eHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void
    ScatterChartItem::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterchartitem.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ScatterChartItem::mouseReleaseEvent(QGraphicsSceneMouseEvent
    #      *event)
    ritual = (
        'ritual_ZN16ScatterChartItem17mouseReleaseEventEP24QGraphicsSceneMo'
        'useEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16ScatterChartItem17mouseReleaseEventEP24QGraphicsS'
          'ceneMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void
    ScatterChartItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterchartitem.html#mouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ScatterChartItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
    #      *event)
    ritual = (
        'ritual_ZN16ScatterChartItem21mouseDoubleClickEventEP24QGraphicsSce'
        'neMouseEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16ScatterChartItem21mouseDoubleClickEventEP24QGraph'
          'icsSceneMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))
