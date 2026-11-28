"""
SplineChartItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/splinechartitem_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means SplineChartItem to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtWidgets import QGraphicsItem
from . import XYChart

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF, QRectF
  from ..QtGui import QPainter, QPainterPath
  from ..QtWidgets import QGraphicsSceneHoverEvent, QGraphicsSceneMouseEvent
  from ..QtWidgets import QStyleOptionGraphicsItem, QWidget
  from . import ChartAnimation, QSplineSeries, SplineAnimation
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGraphicsSceneHoverEvent = WAIT['QGraphicsSceneHoverEvent']
  QGraphicsSceneMouseEvent = WAIT['QGraphicsSceneMouseEvent']
  QPainter = WAIT['QPainter']
  QPointF = WAIT['QPointF']
  QSplineSeries = WAIT['QtCharts:QSplineSeries']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
  QWidget = WAIT['QWidget']
  SplineAnimation = WAIT['SplineAnimation']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class SplineChartItem(XYChart):
  """
  The cute side of Qt's SplineChartItem: a plain Python object standing in
  front of one C++ SplineChartItem.

  It is built on the cute 'XYChart', as Qt's SplineChartItem is built on Qt's
  XYChart, and has everything that class has.

  What exists
  -----------

  Every function of Qt's SplineChartItem that has a ritual and that Python
  can call so far, 19 names in all: 'metaObject', 'tr', 'boundingRect',
  'paint', 'shape', 'setControlGeometryPoints', 'controlGeometryPoints',
  'setAnimation', 'animation', 'handleSeriesUpdated', 'updateGeometry',
  'calculateControlPoints', 'updateChart', 'mousePressEvent',
  'hoverEnterEvent', 'hoverMoveEvent', 'hoverLeaveEvent',
  'mouseReleaseEvent', 'mouseDoubleClickEvent'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *SplineChartItem::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int SplineChartItem::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QList<qreal> SplineChartItem::firstControlPoints(const QList<qreal>
    &list)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 25 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ SplineChartItem is created at the first use, not by
    'SplineChartItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ SplineChartItem.
  - Qt tells when it has removed the C++ SplineChartItem. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's SplineChartItem that has no cute function yet,
    'firstControlPoints', holds a function that raises 'NotImplementedError',
    and its docstring says why.
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
    Calls Qt's 'QString SplineChartItem::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/splinechartitem.html#tr

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
    #  QString SplineChartItem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15SplineChartItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'SplineChartItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *SplineChartItem::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/splinechartitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *SplineChartItem::metaObject() const
    address = self.uglySide.call('ritual_ZNK15SplineChartItem10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF SplineChartItem::boundingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/splinechartitem.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF SplineChartItem::boundingRect() const
    ritual = 'ritual_ZNK15SplineChartItem12boundingRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15SplineChartItem12boundingRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def shape(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath SplineChartItem::shape() const'.

    Qt's own words: https://doc.qt.io/qt-6/splinechartitem.html#shape

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath SplineChartItem::shape() const
    ritual = 'ritual_ZNK15SplineChartItem5shapeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15SplineChartItem5shapeEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  def controlGeometryPoints(self) -> QList[QPointF]:
    """
    Calls Qt's 'QList<QPointF> SplineChartItem::controlGeometryPoints()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/splinechartitem.html#controlGeometryPoints

    Returns
    -------

    QList[QPointF]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QPointF> SplineChartItem::controlGeometryPoints() const
    address = self.uglySide.call(
        'ritual_ZNK15SplineChartItem21controlGeometryPointsEv',
    )
    from ..QtCore import QPointF
    return QList[QPointF]._cuteOwning(address)

  def animation(self) -> Optional[ChartAnimation]:
    """
    Calls Qt's 'ChartAnimation *SplineChartItem::animation() const'.

    Qt's own words: https://doc.qt.io/qt-6/splinechartitem.html#animation

    Returns
    -------

    Optional[ChartAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ChartAnimation *SplineChartItem::animation() const
    ritual = 'ritual_ZNK15SplineChartItem9animationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15SplineChartItem9animationEv'
    address = self.uglySide.call(ritual)
    from . import ChartAnimation
    return ChartAnimation._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QPointF])
  def setControlGeometryPoints(self, points: QList[QPointF]) -> None:
    """
    Calls Qt's 'void SplineChartItem::setControlGeometryPoints(const
    QList<QPointF> &points)'.

    Qt's own words:
    https://doc.qt.io/qt-6/splinechartitem.html#setControlGeometryPoints

    Parameters
    ----------

    points : QList[QPointF]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void SplineChartItem::setControlGeometryPoints(const QList<QPointF>
    #      &points)
    self.uglySide.call(
        'ritual_ZN15SplineChartItem24setControlGeometryPointsERK5QListI7QPo'
        'intFE',
        self._valueOf(points),
    )

  @overload(SplineAnimation)
  @overload(NoneType)
  def setAnimation(self, animation: Optional[SplineAnimation]) -> None:
    """
    Calls Qt's 'void SplineChartItem::setAnimation(SplineAnimation
    *animation)'.

    Qt's own words: https://doc.qt.io/qt-6/splinechartitem.html#setAnimation

    Parameters
    ----------

    animation : Optional[SplineAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void SplineChartItem::setAnimation(SplineAnimation *animation)
    self.uglySide.call(
        'ritual_ZN15SplineChartItem12setAnimationEP15SplineAnimation',
        self._addressOf(animation),
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

  @overload(QSplineSeries)
  @overload(NoneType)
  @overload(QSplineSeries, QGraphicsItem)
  @overload(QSplineSeries, NoneType)
  @overload(NoneType, QGraphicsItem)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      series: Optional[QSplineSeries],
      item: Optional[QGraphicsItem] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'SplineChartItem::SplineChartItem(QSplineSeries *series, QGraphicsItem
    *item)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/splinechartitem.html#SplineChartItem

    Parameters
    ----------

    series : Optional[QSplineSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  SplineChartItem::SplineChartItem(QSplineSeries *series, QGraphicsItem
    #      *item)
    self._noteCreation(SplineChartItem, lambda: Rituals.call(
        'ritual_ZN15SplineChartItemC1EP13QSplineSeriesP13QGraphicsItem',
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
    Calls Qt's 'void SplineChartItem::paint(QPainter *painter, const
    QStyleOptionGraphicsItem *option, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/splinechartitem.html#paint

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
    #  void SplineChartItem::paint(QPainter *painter, const
    #      QStyleOptionGraphicsItem *option, QWidget *widget)
    ritual = (
        'ritual_ZN15SplineChartItem5paintEP8QPainterPK24QStyleOptionGraphic'
        'sItemP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15SplineChartItem5paintEP8QPainterPK24QStyleOptionG'
          'raphicsItemP7QWidget')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._addressOf(option),
        self._addressOf(widget),
    )

  def handleSeriesUpdated(self) -> None:
    """
    Calls Qt's 'void SplineChartItem::handleSeriesUpdated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/splinechartitem.html#handleSeriesUpdated
    """
    #  void SplineChartItem::handleSeriesUpdated()
    ritual = 'ritual_ZN15SplineChartItem19handleSeriesUpdatedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15SplineChartItem19handleSeriesUpdatedEv'
    self.uglySide.call(ritual)

  def updateGeometry(self) -> None:
    """
    Calls Qt's 'void SplineChartItem::updateGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/splinechartitem.html#updateGeometry
    """
    #  void SplineChartItem::updateGeometry()
    ritual = 'ritual_ZN15SplineChartItem14updateGeometryEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15SplineChartItem14updateGeometryEv'
    self.uglySide.call(ritual)

  @overload(QList[QPointF])
  def calculateControlPoints(self, points: QList[QPointF]) -> QList[QPointF]:
    """
    Calls Qt's 'QList<QPointF> SplineChartItem::calculateControlPoints(const
    QList<QPointF> &points)'.

    Qt's own words:
    https://doc.qt.io/qt-6/splinechartitem.html#calculateControlPoints

    Parameters
    ----------

    points : QList[QPointF]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QList[QPointF]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QPointF> SplineChartItem::calculateControlPoints(const
    #      QList<QPointF> &points)
    address = self.uglySide.call(
        'ritual_ZN15SplineChartItem22calculateControlPointsERK5QListI7QPoin'
        'tFE',
        self._valueOf(points),
    )
    from ..QtCore import QPointF
    return QList[QPointF]._cuteOwning(address)

  @overload(QList[QPointF], QList[QPointF], int)
  def updateChart(
      self,
      oldPoints: QList[QPointF],
      newPoints: QList[QPointF],
      index: int,
  ) -> None:
    """
    Calls Qt's 'void SplineChartItem::updateChart(const QList<QPointF>
    &oldPoints, const QList<QPointF> &newPoints, int index)'.

    Qt's own words: https://doc.qt.io/qt-6/splinechartitem.html#updateChart

    Parameters
    ----------

    oldPoints : QList[QPointF]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    newPoints : QList[QPointF]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    index : int
      Passed on as it is.
    """
    #  void SplineChartItem::updateChart(const QList<QPointF> &oldPoints,
    #      const QList<QPointF> &newPoints, int index)
    self.uglySide.call(
        'ritual_ZN15SplineChartItem11updateChartERK5QListI7QPointFES4_i',
        self._valueOf(oldPoints), self._valueOf(newPoints), index,
    )

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mousePressEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void
    SplineChartItem::mousePressEvent(QGraphicsSceneMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/splinechartitem.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void SplineChartItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
    ritual = (
        'ritual_ZN15SplineChartItem15mousePressEventEP24QGraphicsSceneMouse'
        'Event')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15SplineChartItem15mousePressEventEP24QGraphicsScen'
          'eMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverEnterEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void
    SplineChartItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/splinechartitem.html#hoverEnterEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void SplineChartItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
    ritual = (
        'ritual_ZN15SplineChartItem15hoverEnterEventEP24QGraphicsSceneHover'
        'Event')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15SplineChartItem15hoverEnterEventEP24QGraphicsScen'
          'eHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverMoveEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void SplineChartItem::hoverMoveEvent(QGraphicsSceneHoverEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/splinechartitem.html#hoverMoveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void SplineChartItem::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
    ritual = (
        'ritual_ZN15SplineChartItem14hoverMoveEventEP24QGraphicsSceneHoverE'
        'vent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15SplineChartItem14hoverMoveEventEP24QGraphicsScene'
          'HoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverLeaveEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void
    SplineChartItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/splinechartitem.html#hoverLeaveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void SplineChartItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
    ritual = (
        'ritual_ZN15SplineChartItem15hoverLeaveEventEP24QGraphicsSceneHover'
        'Event')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15SplineChartItem15hoverLeaveEventEP24QGraphicsScen'
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
    SplineChartItem::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/splinechartitem.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void SplineChartItem::mouseReleaseEvent(QGraphicsSceneMouseEvent
    #      *event)
    ritual = (
        'ritual_ZN15SplineChartItem17mouseReleaseEventEP24QGraphicsSceneMou'
        'seEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15SplineChartItem17mouseReleaseEventEP24QGraphicsSc'
          'eneMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void
    SplineChartItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/splinechartitem.html#mouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void SplineChartItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
    #      *event)
    ritual = (
        'ritual_ZN15SplineChartItem21mouseDoubleClickEventEP24QGraphicsScen'
        'eMouseEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15SplineChartItem21mouseDoubleClickEventEP24QGraphi'
          'csSceneMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @staticmethod
  def firstControlPoints(*__, **_) -> Never:
    """
    Qt's 'QList<qreal> SplineChartItem::firstControlPoints(const QList<qreal>
    &list)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'SplineChartItem.firstControlPoints' has no cute function yet. "
        "Qt's 'QList<qreal> SplineChartItem::firstControlPoints(const "
        "QList<qreal> &list)': takes a type Python has no way to hand over "
        "yet.")
