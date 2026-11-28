"""
PercentBarChartItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/percentbarchartitem_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means PercentBarChartItem to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtWidgets import QGraphicsItem
from . import AbstractBarChartItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF, QRectF
  from . import QAbstractBarSeries, QBarSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractBarSeries = WAIT['QAbstractBarSeries']
  QBarSet = WAIT['QtCharts:QBarSet']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PercentBarChartItem(AbstractBarChartItem):
  """
  The cute side of Qt's PercentBarChartItem: a plain Python object standing
  in front of one C++ PercentBarChartItem.

  It is built on the cute 'AbstractBarChartItem', as Qt's PercentBarChartItem
  is built on Qt's AbstractBarChartItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's PercentBarChartItem that has a ritual and that
  Python can call so far, 10 names in all: 'metaObject', 'tr',
  'generateLabelText', 'handleLabelsPositionChanged', 'positionLabels',
  'calculateLayout', 'initializeLayout', 'markLabelsDirty', 'topLeftPoint',
  'bottomRightPoint'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *PercentBarChartItem::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int PercentBarChartItem::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ PercentBarChartItem is created at the first use, not by
    'PercentBarChartItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ PercentBarChartItem.
  - Qt tells when it has removed the C++ PercentBarChartItem. Every call on
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
    Calls Qt's 'QString PercentBarChartItem::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/percentbarchartitem.html#tr

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
    #  QString PercentBarChartItem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19PercentBarChartItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'PercentBarChartItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *PercentBarChartItem::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/percentbarchartitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *PercentBarChartItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19PercentBarChartItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @overload(QAbstractBarSeries)
  @overload(NoneType)
  @overload(QAbstractBarSeries, QGraphicsItem)
  @overload(QAbstractBarSeries, NoneType)
  @overload(NoneType, QGraphicsItem)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      series: Optional[QAbstractBarSeries],
      item: Optional[QGraphicsItem] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'PercentBarChartItem::PercentBarChartItem(QAbstractBarSeries *series,
    QGraphicsItem *item)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/percentbarchartitem.html#PercentBarChartItem

    Parameters
    ----------

    series : Optional[QAbstractBarSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  PercentBarChartItem::PercentBarChartItem(QAbstractBarSeries *series,
    #      QGraphicsItem *item)
    self._noteCreation(PercentBarChartItem, lambda: Rituals.call(
        'ritual_ZN19PercentBarChartItemC1EP18QAbstractBarSeriesP13QGraphics'
        'Item',
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

  @overload(int, int, float)
  def generateLabelText(self, set: int, category: int, value: float) -> str:
    """
    Calls Qt's 'QString PercentBarChartItem::generateLabelText(int set, int
    category, qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/percentbarchartitem.html#generateLabelText

    Parameters
    ----------

    set : int
      Passed on as it is.

    category : int
      Passed on as it is.

    value : float
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString PercentBarChartItem::generateLabelText(int set, int category,
    #      qreal value)
    ritual = 'ritual_ZN19PercentBarChartItem17generateLabelTextEiid'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19PercentBarChartItem17generateLabelTextEiid'
    return self.uglySide.call(ritual, set, category, value)

  def handleLabelsPositionChanged(self) -> None:
    """
    Calls Qt's 'void PercentBarChartItem::handleLabelsPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/percentbarchartitem.html
    """
    #  void PercentBarChartItem::handleLabelsPositionChanged()
    self.uglySide.call(
        'ritual_ZN19PercentBarChartItem27handleLabelsPositionChangedEv',
    )

  def positionLabels(self) -> None:
    """
    Calls Qt's 'void PercentBarChartItem::positionLabels()'.

    Qt's own words:
    https://doc.qt.io/qt-6/percentbarchartitem.html#positionLabels
    """
    #  void PercentBarChartItem::positionLabels()
    ritual = 'ritual_ZN19PercentBarChartItem14positionLabelsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19PercentBarChartItem14positionLabelsEv'
    self.uglySide.call(ritual)

  def calculateLayout(self) -> QList[QRectF]:
    """
    Calls Qt's 'QList<QRectF> PercentBarChartItem::calculateLayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/percentbarchartitem.html#calculateLayout

    Returns
    -------

    QList[QRectF]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QRectF> PercentBarChartItem::calculateLayout()
    address = self.uglySide.call(
        'ritual_ZN19PercentBarChartItem15calculateLayoutEv',
    )
    from ..QtCore import QRectF
    return QList[QRectF]._cuteOwning(address)

  @overload(int, int, int, bool)
  def initializeLayout(
      self,
      set: int,
      category: int,
      layoutIndex: int,
      resetAnimation: bool,
  ) -> None:
    """
    Calls Qt's 'void PercentBarChartItem::initializeLayout(int set, int
    category, int layoutIndex, bool resetAnimation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/percentbarchartitem.html#initializeLayout

    Parameters
    ----------

    set : int
      Passed on as it is.

    category : int
      Passed on as it is.

    layoutIndex : int
      Passed on as it is.

    resetAnimation : bool
      Passed on as it is.
    """
    #  void PercentBarChartItem::initializeLayout(int set, int category, int
    #      layoutIndex, bool resetAnimation)
    ritual = 'ritual_ZN19PercentBarChartItem16initializeLayoutEiiib'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19PercentBarChartItem16initializeLayoutEiiib'
    self.uglySide.call(ritual, set, category, layoutIndex, resetAnimation)

  @overload(QBarSet, int, int)
  @overload(NoneType, int, int)
  def markLabelsDirty(
      self,
      barset: Optional[QBarSet],
      index: int,
      count: int,
  ) -> None:
    """
    Calls Qt's 'void PercentBarChartItem::markLabelsDirty(QBarSet *barset,
    int index, int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/percentbarchartitem.html#markLabelsDirty

    Parameters
    ----------

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void PercentBarChartItem::markLabelsDirty(QBarSet *barset, int index,
    #      int count)
    ritual = 'ritual_ZN19PercentBarChartItem15markLabelsDirtyEP7QBarSetii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19PercentBarChartItem15markLabelsDirtyEP7QBarSetii')
    self.uglySide.call(ritual, self._addressOf(barset), index, count)

  @overload(int, float, float)
  def topLeftPoint(
      self,
      category: int,
      barWidth: float,
      value: float,
  ) -> QPointF:
    """
    Calls Qt's 'QPointF PercentBarChartItem::topLeftPoint(int category, qreal
    barWidth, qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/percentbarchartitem.html#topLeftPoint

    Parameters
    ----------

    category : int
      Passed on as it is.

    barWidth : float
      Passed on as it is.

    value : float
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF PercentBarChartItem::topLeftPoint(int category, qreal
    #      barWidth, qreal value)
    address = self.uglySide.call(
        'ritual_ZN19PercentBarChartItem12topLeftPointEidd',
        category, barWidth, value,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(int, float, float)
  def bottomRightPoint(
      self,
      category: int,
      barWidth: float,
      value: float,
  ) -> QPointF:
    """
    Calls Qt's 'QPointF PercentBarChartItem::bottomRightPoint(int category,
    qreal barWidth, qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/percentbarchartitem.html#bottomRightPoint

    Parameters
    ----------

    category : int
      Passed on as it is.

    barWidth : float
      Passed on as it is.

    value : float
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF PercentBarChartItem::bottomRightPoint(int category, qreal
    #      barWidth, qreal value)
    address = self.uglySide.call(
        'ritual_ZN19PercentBarChartItem16bottomRightPointEidd',
        category, barWidth, value,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)
