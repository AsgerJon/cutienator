"""
BarsRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/barsrenderer_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means BarsRenderer to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import Qt
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor, QEventPoint, QHoverEvent
  from ..QtQuick import QQuickText
  from . import QAbstractSeries, QBarSeries, QBarSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractSeries = WAIT['QtGraphs:QAbstractSeries']
  QBarSeries = WAIT['QtGraphs:QBarSeries']
  QBarSet = WAIT['QtGraphs:QBarSet']
  QEventPoint = WAIT['QEventPoint']
  QHoverEvent = WAIT['QHoverEvent']
  QQuickText = WAIT['QQuickText']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class BarsRenderer(QQuickItem):
  """
  The cute side of Qt's BarsRenderer: a plain Python object standing in front
  of one C++ BarsRenderer.

  It is built on the cute 'QQuickItem', as Qt's BarsRenderer is built on Qt's
  QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's BarsRenderer that has a ritual and that Python can
  call so far, 14 names in all: 'metaObject', 'synchronizeData',
  'updateSeries', 'seriesAboutToBeRemoved', 'handleHoverMove', 'getSetColor',
  'getSetSelectedColor', 'getSetBorderColor', 'getSetBorderWidth',
  'generateLabelText', 'positionLabelItem', 'onSingleTapped',
  'onDoubleTapped', 'onPressedChanged'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *BarsRenderer::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int BarsRenderer::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'BarsRenderer::~BarsRenderer()': the destructor: Python never
    removes a C++ BarsRenderer.
  - Qt's 'void BarsRenderer::paintSnapshot(const PaintSnapshot &snapshot,
    QCanvasPainter *p)': takes a type Python has no way to hand over yet.
  - Qt's 'PaintSnapshot BarsRenderer::paintSnapshot() const': gives a type
    Python has no way to take yet.
  - Qt's 'void BarsRenderer::afterUpdate(QList<QAbstractSeries *>
    &cleanupSeries)': takes a type Python has no way to hand over yet.
  - Qt's 'void BarsRenderer::afterPolish(QList<QAbstractSeries *>
    &cleanupSeries)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  9 of the 30 functions Qt declares: 5 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 not a gap;
  2 leans on 'BarsRenderer.

  What to expect
  --------------

  - The C++ BarsRenderer is created at the first use, not by
    'BarsRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ BarsRenderer.
  - Qt tells when it has removed the C++ BarsRenderer. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's BarsRenderer that has no cute function yet, '__init__',
    'afterPolish', 'afterUpdate', 'handlePolish', 'paintSnapshot',
    'updateComponents', 'updateHorizontalBars', 'updateValueLabels',
    'updateVerticalBars', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The classes Qt writes inside BarsRenderer, each a class in here as in
  #  C++.

  class BarSeriesData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's BarsRenderer::BarSeriesData: a plain Python object
    standing in front of one C++ BarsRenderer::BarSeriesData.

    C++ hands a BarsRenderer::BarSeriesData around as a copy, so every C++
    BarsRenderer::BarSeriesData behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's BarsRenderer::BarSeriesData yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'BarsRenderer::BarSeriesData::~BarSeriesData()': the destructor:
      Python removes its C++ BarsRenderer::BarSeriesData by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ BarsRenderer::BarSeriesData is created at the first use, not by
      'BarsRenderer::BarSeriesData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a BarsRenderer::BarSeriesData back gives a copy the
      ritual made for Python, in a new cute BarsRenderer::BarSeriesData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'BarsRenderer::BarSeriesData'

    #  Qt's '~BarsRenderer::BarSeriesData()'. Naming it makes this a value
    #  class: Python owns every C++ BarsRenderer::BarSeriesData behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN12BarsRenderer13BarSeriesDataD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'BarsRenderer'

  #  A C++ BarsRenderer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_BarsRenderer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *BarsRenderer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/barsrenderer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *BarsRenderer::metaObject() const
    address = self.uglySide.call('ritual_ZNK12BarsRenderer10metaObjectEv')
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'BarsRenderer::BarsRenderer(QGraphsView *graph, bool clipPlotArea)':
    leans on 'BarsRenderer::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'BarsRenderer.__init__' has no cute function yet. Qt's "
        "'BarsRenderer::BarsRenderer(QGraphsView *graph, bool "
        "clipPlotArea)': leans on "
        "'BarsRenderer::qt_metacall(QMetaObject::Call, int, void**)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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

  def synchronizeData(self) -> None:
    """
    Calls Qt's 'void BarsRenderer::synchronizeData()'.

    Qt's own words: https://doc.qt.io/qt-6/barsrenderer.html#synchronizeData
    """
    #  void BarsRenderer::synchronizeData()
    self.uglySide.call('ritual_ZN12BarsRenderer15synchronizeDataEv')

  @overload(QBarSeries)
  @overload(NoneType)
  def updateSeries(self, series: Optional[QBarSeries]) -> None:
    """
    Calls Qt's 'void BarsRenderer::updateSeries(QBarSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/barsrenderer.html#updateSeries

    Parameters
    ----------

    series : Optional[QBarSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void BarsRenderer::updateSeries(QBarSeries *series)
    self.uglySide.call(
        'ritual_ZN12BarsRenderer12updateSeriesEP10QBarSeries',
        self._addressOf(series),
    )

  @overload(QAbstractSeries)
  @overload(NoneType)
  def seriesAboutToBeRemoved(
      self,
      series: Optional[QAbstractSeries],
  ) -> None:
    """
    Calls Qt's 'void BarsRenderer::seriesAboutToBeRemoved(QAbstractSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/barsrenderer.html#seriesAboutToBeRemoved

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void BarsRenderer::seriesAboutToBeRemoved(QAbstractSeries *series)
    self.uglySide.call(
        'ritual_ZN12BarsRenderer22seriesAboutToBeRemovedEP15QAbstractSeries',
        self._addressOf(series),
    )

  @overload(QHoverEvent)
  @overload(NoneType)
  def handleHoverMove(self, event: Optional[QHoverEvent]) -> bool:
    """
    Calls Qt's 'bool BarsRenderer::handleHoverMove(QHoverEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/barsrenderer.html#handleHoverMove

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool BarsRenderer::handleHoverMove(QHoverEvent *event)
    return self.uglySide.call(
        'ritual_ZN12BarsRenderer15handleHoverMoveEP11QHoverEvent',
        self._addressOf(event),
    )

  @overload(QBarSeries, QBarSet, int)
  @overload(QBarSeries, NoneType, int)
  @overload(NoneType, QBarSet, int)
  @overload(NoneType, NoneType, int)
  def getSetColor(
      self,
      series: Optional[QBarSeries],
      set: Optional[QBarSet],
      barSerieIndex: int,
  ) -> QColor:
    """
    Calls Qt's 'QColor BarsRenderer::getSetColor(QBarSeries *series, QBarSet
    *set, qsizetype barSerieIndex)'.

    Qt's own words: https://doc.qt.io/qt-6/barsrenderer.html#getSetColor

    Parameters
    ----------

    series : Optional[QBarSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    set : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    barSerieIndex : int
      Passed on as it is.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor BarsRenderer::getSetColor(QBarSeries *series, QBarSet *set,
    #      qsizetype barSerieIndex)
    address = self.uglySide.call(
        'ritual_ZN12BarsRenderer11getSetColorEP10QBarSeriesP7QBarSetx',
        self._addressOf(series), self._addressOf(set), barSerieIndex,
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload(QBarSeries, QBarSet)
  @overload(QBarSeries, NoneType)
  @overload(NoneType, QBarSet)
  @overload(NoneType, NoneType)
  def getSetSelectedColor(
      self,
      series: Optional[QBarSeries],
      set: Optional[QBarSet],
  ) -> QColor:
    """
    Calls Qt's 'QColor BarsRenderer::getSetSelectedColor(QBarSeries *series,
    QBarSet *set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/barsrenderer.html#getSetSelectedColor

    Parameters
    ----------

    series : Optional[QBarSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    set : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor BarsRenderer::getSetSelectedColor(QBarSeries *series, QBarSet
    #      *set)
    address = self.uglySide.call(
        'ritual_ZN12BarsRenderer19getSetSelectedColorEP10QBarSeriesP7QBarSe'
        't',
        self._addressOf(series), self._addressOf(set),
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload(QBarSeries, QBarSet, int)
  @overload(QBarSeries, NoneType, int)
  @overload(NoneType, QBarSet, int)
  @overload(NoneType, NoneType, int)
  def getSetBorderColor(
      self,
      series: Optional[QBarSeries],
      set: Optional[QBarSet],
      barSerieIndex: int,
  ) -> QColor:
    """
    Calls Qt's 'QColor BarsRenderer::getSetBorderColor(QBarSeries *series,
    QBarSet *set, qsizetype barSerieIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/barsrenderer.html#getSetBorderColor

    Parameters
    ----------

    series : Optional[QBarSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    set : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    barSerieIndex : int
      Passed on as it is.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor BarsRenderer::getSetBorderColor(QBarSeries *series, QBarSet
    #      *set, qsizetype barSerieIndex)
    address = self.uglySide.call(
        'ritual_ZN12BarsRenderer17getSetBorderColorEP10QBarSeriesP7QBarSetx',
        self._addressOf(series), self._addressOf(set), barSerieIndex,
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload(QBarSeries, QBarSet)
  @overload(QBarSeries, NoneType)
  @overload(NoneType, QBarSet)
  @overload(NoneType, NoneType)
  def getSetBorderWidth(
      self,
      series: Optional[QBarSeries],
      set: Optional[QBarSet],
  ) -> float:
    """
    Calls Qt's 'qreal BarsRenderer::getSetBorderWidth(QBarSeries *series,
    QBarSet *set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/barsrenderer.html#getSetBorderWidth

    Parameters
    ----------

    series : Optional[QBarSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    set : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qreal BarsRenderer::getSetBorderWidth(QBarSeries *series, QBarSet
    #      *set)
    return self.uglySide.call(
        'ritual_ZN12BarsRenderer17getSetBorderWidthEP10QBarSeriesP7QBarSet',
        self._addressOf(series), self._addressOf(set),
    )

  @overload(QBarSeries, float)
  @overload(NoneType, float)
  def generateLabelText(
      self,
      series: Optional[QBarSeries],
      value: float,
  ) -> str:
    """
    Calls Qt's 'QString BarsRenderer::generateLabelText(QBarSeries *series,
    qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/barsrenderer.html#generateLabelText

    Parameters
    ----------

    series : Optional[QBarSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    value : float
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString BarsRenderer::generateLabelText(QBarSeries *series, qreal
    #      value)
    return self.uglySide.call(
        'ritual_ZN12BarsRenderer17generateLabelTextEP10QBarSeriesd',
        self._addressOf(series), value,
    )

  @overload(QBarSeries, QQuickText, BarSeriesData)
  @overload(QBarSeries, NoneType, BarSeriesData)
  @overload(NoneType, QQuickText, BarSeriesData)
  @overload(NoneType, NoneType, BarSeriesData)
  def positionLabelItem(
      self,
      series: Optional[QBarSeries],
      textItem: Optional[QQuickText],
      d: BarSeriesData,
  ) -> None:
    """
    Calls Qt's 'void BarsRenderer::positionLabelItem(QBarSeries *series,
    QQuickText *textItem, const BarSeriesData &d)'.

    Qt's own words:
    https://doc.qt.io/qt-6/barsrenderer.html#positionLabelItem

    Parameters
    ----------

    series : Optional[QBarSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    textItem : Optional[QQuickText]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    d : BarSeriesData
      Passed on as a value: Qt reads the C++ BarsRenderer::BarSeriesData,
      which stays Python's own.
    """
    #  void BarsRenderer::positionLabelItem(QBarSeries *series, QQuickText
    #      *textItem, const BarSeriesData &d)
    self.uglySide.call(
        'ritual_ZN12BarsRenderer17positionLabelItemEP10QBarSeriesP10QQuickT'
        'extRKNS_13BarSeriesDataE',
        self._addressOf(series), self._addressOf(textItem), self._valueOf(d),
    )

  @overload(QEventPoint, Qt.MouseButton)
  def onSingleTapped(
      self,
      eventPoint: QEventPoint,
      button: Qt.MouseButton,
  ) -> None:
    """
    Calls Qt's 'void BarsRenderer::onSingleTapped(QEventPoint eventPoint,
    Qt::MouseButton button)'.

    Qt's own words: https://doc.qt.io/qt-6/barsrenderer.html#onSingleTapped

    Parameters
    ----------

    eventPoint : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.

    button : Qt.MouseButton
      Passed on as its number.
    """
    #  void BarsRenderer::onSingleTapped(QEventPoint eventPoint,
    #      Qt::MouseButton button)
    self.uglySide.call(
        'ritual_ZN12BarsRenderer14onSingleTappedE11QEventPointN2Qt11MouseBu'
        'ttonE',
        self._valueOf(eventPoint), button.value,
    )

  @overload(QEventPoint, Qt.MouseButton)
  def onDoubleTapped(
      self,
      eventPoint: QEventPoint,
      button: Qt.MouseButton,
  ) -> None:
    """
    Calls Qt's 'void BarsRenderer::onDoubleTapped(QEventPoint eventPoint,
    Qt::MouseButton button)'.

    Qt's own words: https://doc.qt.io/qt-6/barsrenderer.html#onDoubleTapped

    Parameters
    ----------

    eventPoint : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.

    button : Qt.MouseButton
      Passed on as its number.
    """
    #  void BarsRenderer::onDoubleTapped(QEventPoint eventPoint,
    #      Qt::MouseButton button)
    self.uglySide.call(
        'ritual_ZN12BarsRenderer14onDoubleTappedE11QEventPointN2Qt11MouseBu'
        'ttonE',
        self._valueOf(eventPoint), button.value,
    )

  def onPressedChanged(self) -> None:
    """
    Calls Qt's 'void BarsRenderer::onPressedChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/barsrenderer.html#onPressedChanged
    """
    #  void BarsRenderer::onPressedChanged()
    self.uglySide.call('ritual_ZN12BarsRenderer16onPressedChangedEv')

  @staticmethod
  def afterPolish(*__, **_) -> Never:
    """
    Qt's 'void BarsRenderer::afterPolish(QList<QAbstractSeries *>
    &cleanupSeries)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'BarsRenderer.afterPolish' has no cute function yet. Qt's 'void "
        "BarsRenderer::afterPolish(QList<QAbstractSeries *> "
        "&cleanupSeries)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def afterUpdate(*__, **_) -> Never:
    """
    Qt's 'void BarsRenderer::afterUpdate(QList<QAbstractSeries *>
    &cleanupSeries)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'BarsRenderer.afterUpdate' has no cute function yet. Qt's 'void "
        "BarsRenderer::afterUpdate(QList<QAbstractSeries *> "
        "&cleanupSeries)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def handlePolish(*__, **_) -> Never:
    """
    Qt's 'void BarsRenderer::handlePolish(QBarSeries *series, int
    barSeriesIndex, int barSeriesCount)': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: member
    access into incomplete type 'QBarSeriesPrivate'.
    """
    raise NotImplementedError(
        "'BarsRenderer.handlePolish' has no cute function yet. Qt's 'void "
        "BarsRenderer::handlePolish(QBarSeries *series, int barSeriesIndex, "
        "int barSeriesCount)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: member "
        "access into incomplete type 'QBarSeriesPrivate'.")

  @staticmethod
  def paintSnapshot(*__, **_) -> Never:
    """
    - Qt's 'void BarsRenderer::paintSnapshot(const PaintSnapshot &snapshot,
      QCanvasPainter *p)': takes a type Python has no way to hand over yet.
    - Qt's 'PaintSnapshot BarsRenderer::paintSnapshot() const': gives a type
      Python has no way to take yet.
    """
    raise NotImplementedError(
        "'BarsRenderer.paintSnapshot' has no cute function yet. Qt's 'void "
        "BarsRenderer::paintSnapshot(const PaintSnapshot &snapshot, "
        "QCanvasPainter *p)': takes a type Python has no way to hand over "
        "yet. Qt's 'PaintSnapshot BarsRenderer::paintSnapshot() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def updateComponents(*__, **_) -> Never:
    """
    Qt's 'void BarsRenderer::updateComponents(QBarSeries *series)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier
    'QGraphs2DBarsRendererUpdateComponents_entry'.
    """
    raise NotImplementedError(
        "'BarsRenderer.updateComponents' has no cute function yet. Qt's "
        "'void BarsRenderer::updateComponents(QBarSeries *series)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'QGraphs2DBarsRendererUpdateComponents_entry'.")

  @staticmethod
  def updateHorizontalBars(*__, **_) -> Never:
    """
    Qt's 'void BarsRenderer::updateHorizontalBars(QBarSeries *series,
    qsizetype setCount, qsizetype valuesPerSet, int barSeriesIndex, int
    barSeriesCount)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'calculateCategoryTotalValues'.
    """
    raise NotImplementedError(
        "'BarsRenderer.updateHorizontalBars' has no cute function yet. Qt's "
        "'void BarsRenderer::updateHorizontalBars(QBarSeries *series, "
        "qsizetype setCount, qsizetype valuesPerSet, int barSeriesIndex, "
        "int barSeriesCount)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'calculateCategoryTotalValues'.")

  @staticmethod
  def updateValueLabels(*__, **_) -> Never:
    """
    Qt's 'void BarsRenderer::updateValueLabels(QBarSeries *series)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier
    'QGraphs2DBarsRendererUpdateValueLabels_entry'.
    """
    raise NotImplementedError(
        "'BarsRenderer.updateValueLabels' has no cute function yet. Qt's "
        "'void BarsRenderer::updateValueLabels(QBarSeries *series)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'QGraphs2DBarsRendererUpdateValueLabels_entry'.")

  @staticmethod
  def updateVerticalBars(*__, **_) -> Never:
    """
    Qt's 'void BarsRenderer::updateVerticalBars(QBarSeries *series, qsizetype
    setCount, qsizetype valuesPerSet, int barSeriesIndex, int
    barSeriesCount)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'QGraphs2DBarsRendererUpdateVerticalBars_entry'.
    """
    raise NotImplementedError(
        "'BarsRenderer.updateVerticalBars' has no cute function yet. Qt's "
        "'void BarsRenderer::updateVerticalBars(QBarSeries *series, "
        "qsizetype setCount, qsizetype valuesPerSet, int barSeriesIndex, "
        "int barSeriesCount)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier "
        "'QGraphs2DBarsRendererUpdateVerticalBars_entry'.")
