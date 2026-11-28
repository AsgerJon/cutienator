"""
CandlestickChartItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/candlestickchartitem_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means CandlestickChartItem to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtWidgets import QGraphicsItem
from . import ChartItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF
  from ..QtGui import QPainter
  from ..QtWidgets import QStyleOptionGraphicsItem, QWidget
  from . import Candlestick, CandlestickAnimation, QCandlestickSeries
  from . import QCandlestickSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  Candlestick = WAIT['Candlestick']
  CandlestickAnimation = WAIT['CandlestickAnimation']
  QCandlestickSeries = WAIT['QCandlestickSeries']
  QCandlestickSet = WAIT['QCandlestickSet']
  QPainter = WAIT['QPainter']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class CandlestickChartItem(ChartItem):
  """
  The cute side of Qt's CandlestickChartItem: a plain Python object standing
  in front of one C++ CandlestickChartItem.

  It is built on the cute 'ChartItem', as Qt's CandlestickChartItem is built
  on Qt's ChartItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's CandlestickChartItem that has a ritual and that
  Python can call so far, 17 names in all: 'metaObject', 'tr',
  'setAnimation', 'boundingRect', 'paint', 'handleDomainUpdated',
  'handleLayoutUpdated', 'handleCandlesticksUpdated',
  'handleCandlestickSeriesChange', 'handleCandlestickSetsAdd',
  'handleCandlestickSetsRemove', 'handleDataStructureChanged',
  'updateCandlestickGeometry', 'updateCandlestickAppearance', 'addTimestamp',
  'removeTimestamp', 'updateTimePeriod'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *CandlestickChartItem::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int CandlestickChartItem::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'CandlestickChartItem::~CandlestickChartItem()': the destructor:
    Python never removes a C++ CandlestickChartItem.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ CandlestickChartItem is created at the first use, not by
    'CandlestickChartItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ CandlestickChartItem.
  - Qt tells when it has removed the C++ CandlestickChartItem. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString CandlestickChartItem::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/candlestickchartitem.html#tr

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
    #  QString CandlestickChartItem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20CandlestickChartItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'CandlestickChartItem'

  #  A C++ CandlestickChartItem Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_CandlestickChartItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *CandlestickChartItem::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/candlestickchartitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *CandlestickChartItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20CandlestickChartItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF CandlestickChartItem::boundingRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/candlestickchartitem.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF CandlestickChartItem::boundingRect() const
    ritual = 'ritual_ZNK20CandlestickChartItem12boundingRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20CandlestickChartItem12boundingRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(CandlestickAnimation)
  @overload(NoneType)
  def setAnimation(self, animation: Optional[CandlestickAnimation]) -> None:
    """
    Calls Qt's 'void CandlestickChartItem::setAnimation(CandlestickAnimation
    *animation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/candlestickchartitem.html#setAnimation

    Parameters
    ----------

    animation : Optional[CandlestickAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void CandlestickChartItem::setAnimation(CandlestickAnimation
    #      *animation)
    self.uglySide.call(
        'ritual_ZN20CandlestickChartItem12setAnimationEP20CandlestickAnimat'
        'ion',
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

  @overload(QCandlestickSeries)
  @overload(NoneType)
  @overload(QCandlestickSeries, QGraphicsItem)
  @overload(QCandlestickSeries, NoneType)
  @overload(NoneType, QGraphicsItem)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      series: Optional[QCandlestickSeries],
      item: Optional[QGraphicsItem] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'CandlestickChartItem::CandlestickChartItem(QCandlestickSeries *series,
    QGraphicsItem *item)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/candlestickchartitem.html#CandlestickChartItem

    Parameters
    ----------

    series : Optional[QCandlestickSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  CandlestickChartItem::CandlestickChartItem(QCandlestickSeries *series,
    #      QGraphicsItem *item)
    self._noteCreation(CandlestickChartItem, lambda: Rituals.call(
        'ritual_ZN20CandlestickChartItemC1EP18QCandlestickSeriesP13QGraphic'
        'sItem',
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
    Calls Qt's 'void CandlestickChartItem::paint(QPainter *painter, const
    QStyleOptionGraphicsItem *option, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/candlestickchartitem.html#paint

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
    #  void CandlestickChartItem::paint(QPainter *painter, const
    #      QStyleOptionGraphicsItem *option, QWidget *widget)
    ritual = (
        'ritual_ZN20CandlestickChartItem5paintEP8QPainterPK24QStyleOptionGr'
        'aphicsItemP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20CandlestickChartItem5paintEP8QPainterPK24QStyleOp'
          'tionGraphicsItemP7QWidget')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._addressOf(option),
        self._addressOf(widget),
    )

  def handleDomainUpdated(self) -> None:
    """
    Calls Qt's 'void CandlestickChartItem::handleDomainUpdated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/candlestickchartitem.html#handleDomainUpdated
    """
    #  void CandlestickChartItem::handleDomainUpdated()
    ritual = 'ritual_ZN20CandlestickChartItem19handleDomainUpdatedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20CandlestickChartItem19handleDomainUpdatedEv'
    self.uglySide.call(ritual)

  def handleLayoutUpdated(self) -> None:
    """
    Calls Qt's 'void CandlestickChartItem::handleLayoutUpdated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/candlestickchartitem.html#handleLayoutUpdated
    """
    #  void CandlestickChartItem::handleLayoutUpdated()
    self.uglySide.call(
        'ritual_ZN20CandlestickChartItem19handleLayoutUpdatedEv',
    )

  def handleCandlesticksUpdated(self) -> None:
    """
    Calls Qt's 'void CandlestickChartItem::handleCandlesticksUpdated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/candlestickchartitem.html
    """
    #  void CandlestickChartItem::handleCandlesticksUpdated()
    self.uglySide.call(
        'ritual_ZN20CandlestickChartItem25handleCandlesticksUpdatedEv',
    )

  def handleCandlestickSeriesChange(self) -> None:
    """
    Calls Qt's 'void CandlestickChartItem::handleCandlestickSeriesChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/candlestickchartitem.html
    """
    #  void CandlestickChartItem::handleCandlestickSeriesChange()
    self.uglySide.call(
        'ritual_ZN20CandlestickChartItem29handleCandlestickSeriesChangeEv',
    )

  @overload(QList[QCandlestickSet])
  def handleCandlestickSetsAdd(self, sets: QList[QCandlestickSet]) -> None:
    """
    Calls Qt's 'void CandlestickChartItem::handleCandlestickSetsAdd(const
    QList<QCandlestickSet *> &sets)'.

    Qt's own words:
    https://doc.qt.io/qt-6/candlestickchartitem.html#handleCandlestickSetsAdd

    Parameters
    ----------

    sets : QList[QCandlestickSet]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void CandlestickChartItem::handleCandlestickSetsAdd(const
    #      QList<QCandlestickSet *> &sets)
    self.uglySide.call(
        'ritual_ZN20CandlestickChartItem24handleCandlestickSetsAddERK5QList'
        'IP15QCandlestickSetE',
        self._valueOf(sets),
    )

  @overload(QList[QCandlestickSet])
  def handleCandlestickSetsRemove(
      self,
      sets: QList[QCandlestickSet],
  ) -> None:
    """
    Calls Qt's 'void CandlestickChartItem::handleCandlestickSetsRemove(const
    QList<QCandlestickSet *> &sets)'.

    Qt's own words:
    https://doc.qt.io/qt-6/candlestickchartitem.html

    Parameters
    ----------

    sets : QList[QCandlestickSet]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void CandlestickChartItem::handleCandlestickSetsRemove(const
    #      QList<QCandlestickSet *> &sets)
    self.uglySide.call(
        'ritual_ZN20CandlestickChartItem27handleCandlestickSetsRemoveERK5QL'
        'istIP15QCandlestickSetE',
        self._valueOf(sets),
    )

  def handleDataStructureChanged(self) -> None:
    """
    Calls Qt's 'void CandlestickChartItem::handleDataStructureChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/candlestickchartitem.html
    """
    #  void CandlestickChartItem::handleDataStructureChanged()
    self.uglySide.call(
        'ritual_ZN20CandlestickChartItem26handleDataStructureChangedEv',
    )

  @overload(Candlestick, int)
  @overload(NoneType, int)
  def updateCandlestickGeometry(
      self,
      item: Optional[Candlestick],
      index: int,
  ) -> bool:
    """
    Calls Qt's 'bool
    CandlestickChartItem::updateCandlestickGeometry(Candlestick *item, int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/candlestickchartitem.html

    Parameters
    ----------

    item : Optional[Candlestick]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.
    """
    #  bool CandlestickChartItem::updateCandlestickGeometry(Candlestick
    #      *item, int index)
    return self.uglySide.call(
        'ritual_ZN20CandlestickChartItem25updateCandlestickGeometryEP11Cand'
        'lesticki',
        self._addressOf(item), index,
    )

  @overload(Candlestick, QCandlestickSet)
  @overload(Candlestick, NoneType)
  @overload(NoneType, QCandlestickSet)
  @overload(NoneType, NoneType)
  def updateCandlestickAppearance(
      self,
      item: Optional[Candlestick],
      set: Optional[QCandlestickSet],
  ) -> None:
    """
    Calls Qt's 'void
    CandlestickChartItem::updateCandlestickAppearance(Candlestick *item,
    QCandlestickSet *set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/candlestickchartitem.html

    Parameters
    ----------

    item : Optional[Candlestick]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    set : Optional[QCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void CandlestickChartItem::updateCandlestickAppearance(Candlestick
    #      *item, QCandlestickSet *set)
    self.uglySide.call(
        'ritual_ZN20CandlestickChartItem27updateCandlestickAppearanceEP11Ca'
        'ndlestickP15QCandlestickSet',
        self._addressOf(item), self._addressOf(set),
    )

  @overload(float)
  def addTimestamp(self, timestamp: float) -> None:
    """
    Calls Qt's 'void CandlestickChartItem::addTimestamp(qreal timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/candlestickchartitem.html#addTimestamp

    Parameters
    ----------

    timestamp : float
      Passed on as it is.
    """
    #  void CandlestickChartItem::addTimestamp(qreal timestamp)
    self.uglySide.call(
        'ritual_ZN20CandlestickChartItem12addTimestampEd', timestamp,
    )

  @overload(float)
  def removeTimestamp(self, timestamp: float) -> None:
    """
    Calls Qt's 'void CandlestickChartItem::removeTimestamp(qreal timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/candlestickchartitem.html#removeTimestamp

    Parameters
    ----------

    timestamp : float
      Passed on as it is.
    """
    #  void CandlestickChartItem::removeTimestamp(qreal timestamp)
    self.uglySide.call(
        'ritual_ZN20CandlestickChartItem15removeTimestampEd', timestamp,
    )

  def updateTimePeriod(self) -> None:
    """
    Calls Qt's 'void CandlestickChartItem::updateTimePeriod()'.

    Qt's own words:
    https://doc.qt.io/qt-6/candlestickchartitem.html#updateTimePeriod
    """
    #  void CandlestickChartItem::updateTimePeriod()
    self.uglySide.call('ritual_ZN20CandlestickChartItem16updateTimePeriodEv')
