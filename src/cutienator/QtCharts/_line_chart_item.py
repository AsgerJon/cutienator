"""
LineChartItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/linechartitem_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means LineChartItem to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtWidgets import QGraphicsItem
from . import QChart, XYChart

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF
  from ..QtGui import QPainter, QPainterPath
  from ..QtWidgets import QGraphicsSceneHoverEvent, QGraphicsSceneMouseEvent
  from ..QtWidgets import QStyleOptionGraphicsItem, QWidget
  from . import QLineSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGraphicsSceneHoverEvent = WAIT['QGraphicsSceneHoverEvent']
  QGraphicsSceneMouseEvent = WAIT['QGraphicsSceneMouseEvent']
  QLineSeries = WAIT['QtCharts:QLineSeries']
  QPainter = WAIT['QPainter']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class LineChartItem(XYChart):
  """
  The cute side of Qt's LineChartItem: a plain Python object standing in
  front of one C++ LineChartItem.

  It is built on the cute 'XYChart', as Qt's LineChartItem is built on Qt's
  XYChart, and has everything that class has.

  What exists
  -----------

  Every function of Qt's LineChartItem that has a ritual and that Python can
  call so far, 16 names in all: 'metaObject', 'tr', 'boundingRect', 'paint',
  'shape', 'path', 'handleSeriesUpdated', 'updateGeometry',
  'mousePressEvent', 'hoverEnterEvent', 'hoverMoveEvent', 'hoverLeaveEvent',
  'mouseReleaseEvent', 'mouseDoubleClickEvent', 'suppressPoints',
  'forceChartType'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *LineChartItem::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int LineChartItem::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'LineChartItem::~LineChartItem()': the destructor: Python never
    removes a C++ LineChartItem.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ LineChartItem is created at the first use, not by
    'LineChartItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ LineChartItem.
  - Qt tells when it has removed the C++ LineChartItem. Every call on the
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
    Calls Qt's 'QString LineChartItem::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/linechartitem.html#tr

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
    #  QString LineChartItem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13LineChartItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'LineChartItem'

  #  A C++ LineChartItem Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_LineChartItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *LineChartItem::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/linechartitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *LineChartItem::metaObject() const
    address = self.uglySide.call('ritual_ZNK13LineChartItem10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF LineChartItem::boundingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/linechartitem.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF LineChartItem::boundingRect() const
    ritual = 'ritual_ZNK13LineChartItem12boundingRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13LineChartItem12boundingRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def shape(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath LineChartItem::shape() const'.

    Qt's own words: https://doc.qt.io/qt-6/linechartitem.html#shape

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath LineChartItem::shape() const
    ritual = 'ritual_ZNK13LineChartItem5shapeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13LineChartItem5shapeEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  def path(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath LineChartItem::path() const'.

    Qt's own words: https://doc.qt.io/qt-6/linechartitem.html#path

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath LineChartItem::path() const
    address = self.uglySide.call('ritual_ZNK13LineChartItem4pathEv')
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

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

  @overload(QLineSeries)
  @overload(NoneType)
  @overload(QLineSeries, QGraphicsItem)
  @overload(QLineSeries, NoneType)
  @overload(NoneType, QGraphicsItem)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      series: Optional[QLineSeries],
      item: Optional[QGraphicsItem] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'LineChartItem::LineChartItem(QLineSeries
    *series, QGraphicsItem *item)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/linechartitem.html#LineChartItem

    Parameters
    ----------

    series : Optional[QLineSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  LineChartItem::LineChartItem(QLineSeries *series, QGraphicsItem *item)
    self._noteCreation(LineChartItem, lambda: Rituals.call(
        'ritual_ZN13LineChartItemC1EP11QLineSeriesP13QGraphicsItem',
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
    Calls Qt's 'void LineChartItem::paint(QPainter *painter, const
    QStyleOptionGraphicsItem *option, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/linechartitem.html#paint

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
    #  void LineChartItem::paint(QPainter *painter, const
    #      QStyleOptionGraphicsItem *option, QWidget *widget)
    ritual = (
        'ritual_ZN13LineChartItem5paintEP8QPainterPK24QStyleOptionGraphicsI'
        'temP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13LineChartItem5paintEP8QPainterPK24QStyleOptionGra'
          'phicsItemP7QWidget')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._addressOf(option),
        self._addressOf(widget),
    )

  def handleSeriesUpdated(self) -> None:
    """
    Calls Qt's 'void LineChartItem::handleSeriesUpdated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/linechartitem.html#handleSeriesUpdated
    """
    #  void LineChartItem::handleSeriesUpdated()
    ritual = 'ritual_ZN13LineChartItem19handleSeriesUpdatedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13LineChartItem19handleSeriesUpdatedEv'
    self.uglySide.call(ritual)

  def updateGeometry(self) -> None:
    """
    Calls Qt's 'void LineChartItem::updateGeometry()'.

    Qt's own words: https://doc.qt.io/qt-6/linechartitem.html#updateGeometry
    """
    #  void LineChartItem::updateGeometry()
    ritual = 'ritual_ZN13LineChartItem14updateGeometryEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13LineChartItem14updateGeometryEv'
    self.uglySide.call(ritual)

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mousePressEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void LineChartItem::mousePressEvent(QGraphicsSceneMouseEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/linechartitem.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void LineChartItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
    ritual = (
        'ritual_ZN13LineChartItem15mousePressEventEP24QGraphicsSceneMouseEv'
        'ent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13LineChartItem15mousePressEventEP24QGraphicsSceneM'
          'ouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverEnterEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void LineChartItem::hoverEnterEvent(QGraphicsSceneHoverEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/linechartitem.html#hoverEnterEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void LineChartItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
    ritual = (
        'ritual_ZN13LineChartItem15hoverEnterEventEP24QGraphicsSceneHoverEv'
        'ent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13LineChartItem15hoverEnterEventEP24QGraphicsSceneH'
          'overEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverMoveEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void LineChartItem::hoverMoveEvent(QGraphicsSceneHoverEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/linechartitem.html#hoverMoveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void LineChartItem::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
    ritual = (
        'ritual_ZN13LineChartItem14hoverMoveEventEP24QGraphicsSceneHoverEve'
        'nt')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13LineChartItem14hoverMoveEventEP24QGraphicsSceneHo'
          'verEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverLeaveEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void LineChartItem::hoverLeaveEvent(QGraphicsSceneHoverEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/linechartitem.html#hoverLeaveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void LineChartItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
    ritual = (
        'ritual_ZN13LineChartItem15hoverLeaveEventEP24QGraphicsSceneHoverEv'
        'ent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13LineChartItem15hoverLeaveEventEP24QGraphicsSceneH'
          'overEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void
    LineChartItem::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/linechartitem.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void LineChartItem::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)
    ritual = (
        'ritual_ZN13LineChartItem17mouseReleaseEventEP24QGraphicsSceneMouse'
        'Event')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13LineChartItem17mouseReleaseEventEP24QGraphicsScen'
          'eMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void
    LineChartItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/linechartitem.html#mouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void LineChartItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
    #      *event)
    ritual = (
        'ritual_ZN13LineChartItem21mouseDoubleClickEventEP24QGraphicsSceneM'
        'ouseEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13LineChartItem21mouseDoubleClickEventEP24QGraphics'
          'SceneMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  def suppressPoints(self) -> None:
    """
    Calls Qt's 'void LineChartItem::suppressPoints()'.

    Qt's own words: https://doc.qt.io/qt-6/linechartitem.html#suppressPoints
    """
    #  void LineChartItem::suppressPoints()
    self.uglySide.call('ritual_ZN13LineChartItem14suppressPointsEv')

  @overload(QChart.ChartType)
  def forceChartType(self, chartType: QChart.ChartType) -> None:
    """
    Calls Qt's 'void LineChartItem::forceChartType(QChart::ChartType
    chartType)'.

    Qt's own words: https://doc.qt.io/qt-6/linechartitem.html#forceChartType

    Parameters
    ----------

    chartType : QChart.ChartType
      Passed on as its number.
    """
    #  void LineChartItem::forceChartType(QChart::ChartType chartType)
    self.uglySide.call(
        'ritual_ZN13LineChartItem14forceChartTypeEN6QChart9ChartTypeE',
        chartType.value,
    )
