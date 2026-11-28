"""
AreaChartItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/areachartitem_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means AreaChartItem to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtWidgets import QGraphicsItem
from . import ChartItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF, QRectF
  from ..QtGui import QPainter, QPainterPath
  from ..QtWidgets import QGraphicsSceneHoverEvent, QGraphicsSceneMouseEvent
  from ..QtWidgets import QStyleOptionGraphicsItem, QWidget
  from . import ChartPresenter, LineChartItem, QAreaSeries, QLineSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  ChartPresenter = WAIT['ChartPresenter']
  LineChartItem = WAIT['LineChartItem']
  QAreaSeries = WAIT['QtCharts:QAreaSeries']
  QGraphicsSceneHoverEvent = WAIT['QGraphicsSceneHoverEvent']
  QGraphicsSceneMouseEvent = WAIT['QGraphicsSceneMouseEvent']
  QLineSeries = WAIT['QtCharts:QLineSeries']
  QPainter = WAIT['QPainter']
  QPointF = WAIT['QPointF']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class AreaChartItem(ChartItem):
  """
  The cute side of Qt's AreaChartItem: a plain Python object standing in
  front of one C++ AreaChartItem.

  It is built on the cute 'ChartItem', as Qt's AreaChartItem is built on Qt's
  ChartItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's AreaChartItem that has a ritual and that Python can
  call so far, 25 names in all: 'metaObject', 'tr', 'boundingRect', 'paint',
  'shape', 'upperLineItem', 'lowerLineItem', 'updatePath', 'setPresenter',
  'series', 'setUpperSeries', 'setLowerSeries', 'mousePressEvent',
  'hoverEnterEvent', 'hoverLeaveEvent', 'mouseReleaseEvent',
  'mouseDoubleClickEvent', 'clicked', 'hovered', 'pressed', 'released',
  'doubleClicked', 'handleUpdated', 'handleDomainUpdated',
  'fixEdgeSeriesDomain'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *AreaChartItem::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int AreaChartItem::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'AreaChartItem::~AreaChartItem()': the destructor: Python never
    removes a C++ AreaChartItem.

  What has no ritual
  ------------------

  2 of the 31 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ AreaChartItem is created at the first use, not by
    'AreaChartItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ AreaChartItem.
  - Qt tells when it has removed the C++ AreaChartItem. Every call on the
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
    Calls Qt's 'QString AreaChartItem::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/areachartitem.html#tr

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
    #  QString AreaChartItem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13AreaChartItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'AreaChartItem'

  #  A C++ AreaChartItem Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_AreaChartItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *AreaChartItem::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/areachartitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *AreaChartItem::metaObject() const
    address = self.uglySide.call('ritual_ZNK13AreaChartItem10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF AreaChartItem::boundingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/areachartitem.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF AreaChartItem::boundingRect() const
    ritual = 'ritual_ZNK13AreaChartItem12boundingRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13AreaChartItem12boundingRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def shape(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath AreaChartItem::shape() const'.

    Qt's own words: https://doc.qt.io/qt-6/areachartitem.html#shape

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath AreaChartItem::shape() const
    ritual = 'ritual_ZNK13AreaChartItem5shapeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13AreaChartItem5shapeEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  def upperLineItem(self) -> Optional[LineChartItem]:
    """
    Calls Qt's 'LineChartItem *AreaChartItem::upperLineItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/areachartitem.html#upperLineItem

    Returns
    -------

    Optional[LineChartItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  LineChartItem *AreaChartItem::upperLineItem() const
    address = self.uglySide.call(
        'ritual_ZNK13AreaChartItem13upperLineItemEv',
    )
    from . import LineChartItem
    return LineChartItem._cuteAt(address)

  def lowerLineItem(self) -> Optional[LineChartItem]:
    """
    Calls Qt's 'LineChartItem *AreaChartItem::lowerLineItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/areachartitem.html#lowerLineItem

    Returns
    -------

    Optional[LineChartItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  LineChartItem *AreaChartItem::lowerLineItem() const
    address = self.uglySide.call(
        'ritual_ZNK13AreaChartItem13lowerLineItemEv',
    )
    from . import LineChartItem
    return LineChartItem._cuteAt(address)

  def series(self) -> Optional[QAreaSeries]:
    """
    Calls Qt's 'QAreaSeries *AreaChartItem::series() const'.

    Qt's own words: https://doc.qt.io/qt-6/areachartitem.html#series

    Returns
    -------

    Optional[QAreaSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAreaSeries *AreaChartItem::series() const
    address = self.uglySide.call('ritual_ZNK13AreaChartItem6seriesEv')
    from . import QAreaSeries
    return QAreaSeries._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(ChartPresenter)
  @overload(NoneType)
  def setPresenter(self, presenter: Optional[ChartPresenter]) -> None:
    """
    Calls Qt's 'void AreaChartItem::setPresenter(ChartPresenter *presenter)'.

    Qt's own words: https://doc.qt.io/qt-6/areachartitem.html#setPresenter

    Parameters
    ----------

    presenter : Optional[ChartPresenter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void AreaChartItem::setPresenter(ChartPresenter *presenter)
    ritual = 'ritual_ZN13AreaChartItem12setPresenterEP14ChartPresenter'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13AreaChartItem12setPresenterEP14ChartPresenter'
    self.uglySide.call(ritual, self._addressOf(presenter))

  @overload(QLineSeries)
  @overload(NoneType)
  def setUpperSeries(self, series: Optional[QLineSeries]) -> None:
    """
    Calls Qt's 'void AreaChartItem::setUpperSeries(QLineSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/areachartitem.html#setUpperSeries

    Parameters
    ----------

    series : Optional[QLineSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void AreaChartItem::setUpperSeries(QLineSeries *series)
    self.uglySide.call(
        'ritual_ZN13AreaChartItem14setUpperSeriesEP11QLineSeries',
        self._addressOf(series),
    )

  @overload(QLineSeries)
  @overload(NoneType)
  def setLowerSeries(self, series: Optional[QLineSeries]) -> None:
    """
    Calls Qt's 'void AreaChartItem::setLowerSeries(QLineSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/areachartitem.html#setLowerSeries

    Parameters
    ----------

    series : Optional[QLineSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void AreaChartItem::setLowerSeries(QLineSeries *series)
    self.uglySide.call(
        'ritual_ZN13AreaChartItem14setLowerSeriesEP11QLineSeries',
        self._addressOf(series),
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

  @overload(QAreaSeries)
  @overload(NoneType)
  @overload(QAreaSeries, QGraphicsItem)
  @overload(QAreaSeries, NoneType)
  @overload(NoneType, QGraphicsItem)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      areaSeries: Optional[QAreaSeries],
      item: Optional[QGraphicsItem] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'AreaChartItem::AreaChartItem(QAreaSeries
    *areaSeries, QGraphicsItem *item)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/areachartitem.html#AreaChartItem

    Parameters
    ----------

    areaSeries : Optional[QAreaSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  AreaChartItem::AreaChartItem(QAreaSeries *areaSeries, QGraphicsItem
    #      *item)
    self._noteCreation(AreaChartItem, lambda: Rituals.call(
        'ritual_ZN13AreaChartItemC1EP11QAreaSeriesP13QGraphicsItem',
        self._addressOf(areaSeries), self._addressOf(item, 'QGraphicsItem'),
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
    Calls Qt's 'void AreaChartItem::paint(QPainter *painter, const
    QStyleOptionGraphicsItem *option, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/areachartitem.html#paint

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
    #  void AreaChartItem::paint(QPainter *painter, const
    #      QStyleOptionGraphicsItem *option, QWidget *widget)
    ritual = (
        'ritual_ZN13AreaChartItem5paintEP8QPainterPK24QStyleOptionGraphicsI'
        'temP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13AreaChartItem5paintEP8QPainterPK24QStyleOptionGra'
          'phicsItemP7QWidget')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._addressOf(option),
        self._addressOf(widget),
    )

  def updatePath(self) -> None:
    """
    Calls Qt's 'void AreaChartItem::updatePath()'.

    Qt's own words: https://doc.qt.io/qt-6/areachartitem.html#updatePath
    """
    #  void AreaChartItem::updatePath()
    self.uglySide.call('ritual_ZN13AreaChartItem10updatePathEv')

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mousePressEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void AreaChartItem::mousePressEvent(QGraphicsSceneMouseEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/areachartitem.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void AreaChartItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
    ritual = (
        'ritual_ZN13AreaChartItem15mousePressEventEP24QGraphicsSceneMouseEv'
        'ent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13AreaChartItem15mousePressEventEP24QGraphicsSceneM'
          'ouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverEnterEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void AreaChartItem::hoverEnterEvent(QGraphicsSceneHoverEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/areachartitem.html#hoverEnterEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void AreaChartItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
    ritual = (
        'ritual_ZN13AreaChartItem15hoverEnterEventEP24QGraphicsSceneHoverEv'
        'ent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13AreaChartItem15hoverEnterEventEP24QGraphicsSceneH'
          'overEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverLeaveEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void AreaChartItem::hoverLeaveEvent(QGraphicsSceneHoverEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/areachartitem.html#hoverLeaveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void AreaChartItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
    ritual = (
        'ritual_ZN13AreaChartItem15hoverLeaveEventEP24QGraphicsSceneHoverEv'
        'ent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13AreaChartItem15hoverLeaveEventEP24QGraphicsSceneH'
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
    AreaChartItem::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/areachartitem.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void AreaChartItem::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)
    ritual = (
        'ritual_ZN13AreaChartItem17mouseReleaseEventEP24QGraphicsSceneMouse'
        'Event')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13AreaChartItem17mouseReleaseEventEP24QGraphicsScen'
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
    AreaChartItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/areachartitem.html#mouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void AreaChartItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
    #      *event)
    ritual = (
        'ritual_ZN13AreaChartItem21mouseDoubleClickEventEP24QGraphicsSceneM'
        'ouseEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13AreaChartItem21mouseDoubleClickEventEP24QGraphics'
          'SceneMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QPointF)
  def clicked(self, point: QPointF) -> None:
    """
    Calls Qt's 'void AreaChartItem::clicked(const QPointF &point)'.

    Qt's own words: https://doc.qt.io/qt-6/areachartitem.html#clicked

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void AreaChartItem::clicked(const QPointF &point)
    self.uglySide.call(
        'ritual_ZN13AreaChartItem7clickedERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(QPointF, bool)
  def hovered(self, point: QPointF, state: bool) -> None:
    """
    Calls Qt's 'void AreaChartItem::hovered(const QPointF &point, bool
    state)'.

    Qt's own words: https://doc.qt.io/qt-6/areachartitem.html#hovered

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    state : bool
      Passed on as it is.
    """
    #  void AreaChartItem::hovered(const QPointF &point, bool state)
    self.uglySide.call(
        'ritual_ZN13AreaChartItem7hoveredERK7QPointFb',
        self._valueOf(point, 'QPointF'), state,
    )

  @overload(QPointF)
  def pressed(self, point: QPointF) -> None:
    """
    Calls Qt's 'void AreaChartItem::pressed(const QPointF &point)'.

    Qt's own words: https://doc.qt.io/qt-6/areachartitem.html#pressed

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void AreaChartItem::pressed(const QPointF &point)
    self.uglySide.call(
        'ritual_ZN13AreaChartItem7pressedERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(QPointF)
  def released(self, point: QPointF) -> None:
    """
    Calls Qt's 'void AreaChartItem::released(const QPointF &point)'.

    Qt's own words: https://doc.qt.io/qt-6/areachartitem.html#released

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void AreaChartItem::released(const QPointF &point)
    self.uglySide.call(
        'ritual_ZN13AreaChartItem8releasedERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(QPointF)
  def doubleClicked(self, point: QPointF) -> None:
    """
    Calls Qt's 'void AreaChartItem::doubleClicked(const QPointF &point)'.

    Qt's own words: https://doc.qt.io/qt-6/areachartitem.html#doubleClicked

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void AreaChartItem::doubleClicked(const QPointF &point)
    self.uglySide.call(
        'ritual_ZN13AreaChartItem13doubleClickedERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  def handleUpdated(self) -> None:
    """
    Calls Qt's 'void AreaChartItem::handleUpdated()'.

    Qt's own words: https://doc.qt.io/qt-6/areachartitem.html#handleUpdated
    """
    #  void AreaChartItem::handleUpdated()
    self.uglySide.call('ritual_ZN13AreaChartItem13handleUpdatedEv')

  def handleDomainUpdated(self) -> None:
    """
    Calls Qt's 'void AreaChartItem::handleDomainUpdated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/areachartitem.html#handleDomainUpdated
    """
    #  void AreaChartItem::handleDomainUpdated()
    ritual = 'ritual_ZN13AreaChartItem19handleDomainUpdatedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13AreaChartItem19handleDomainUpdatedEv'
    self.uglySide.call(ritual)

  @overload(LineChartItem)
  @overload(NoneType)
  def fixEdgeSeriesDomain(self, edgeSeries: Optional[LineChartItem]) -> None:
    """
    Calls Qt's 'void AreaChartItem::fixEdgeSeriesDomain(LineChartItem
    *edgeSeries)'.

    Qt's own words:
    https://doc.qt.io/qt-6/areachartitem.html#fixEdgeSeriesDomain

    Parameters
    ----------

    edgeSeries : Optional[LineChartItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void AreaChartItem::fixEdgeSeriesDomain(LineChartItem *edgeSeries)
    self.uglySide.call(
        'ritual_ZN13AreaChartItem19fixEdgeSeriesDomainEP13LineChartItem',
        self._addressOf(edgeSeries),
    )
