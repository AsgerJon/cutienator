"""
PointRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/pointrenderer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means PointRenderer to be private: it declares the class in a header it
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

  from ..QtCore import QMetaObject, QPointF
  from ..QtGui import QEventPoint, QHoverEvent
  from . import QAbstractSeries, QXYSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractSeries = WAIT['QtGraphs:QAbstractSeries']
  QEventPoint = WAIT['QEventPoint']
  QHoverEvent = WAIT['QHoverEvent']
  QXYSeries = WAIT['QtGraphs:QXYSeries']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PointRenderer(QQuickItem):
  """
  The cute side of Qt's PointRenderer: a plain Python object standing in
  front of one C++ PointRenderer.

  It is built on the cute 'QQuickItem', as Qt's PointRenderer is built on
  Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's PointRenderer that has a ritual and that Python can
  call so far, 15 names in all: 'metaObject', 'resetShapePathCount',
  'synchronizeData', 'updateSeries', 'seriesAboutToBeRemoved',
  'handleHoverMove', 'reverseRenderCoordinates', 'defaultSize',
  'hidePointDelegates', 'onSingleTapped', 'onDoubleTapped',
  'onPressedChanged', 'adjustPressedPointIndexForRemoval',
  'adjustPressedPointIndexForInsertion', 'forgetPressedPoint'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *PointRenderer::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int PointRenderer::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'PointRenderer::~PointRenderer()': the destructor: Python never
    removes a C++ PointRenderer.
  - Qt's 'void PointRenderer::paintSnapshot(const PaintSnapshot &snapshot,
    QCanvasPainter *p)': takes a type Python has no way to hand over yet.
  - Qt's 'QList<PointPaintData> PointRenderer::paintSnapshot() const': gives
    a type Python has no way to take yet.
  - Qt's 'void PointRenderer::afterUpdate(QList<QAbstractSeries *>
    &cleanupSeries)': takes a type Python has no way to hand over yet.
  - Qt's 'SeriesStyle PointRenderer::getSeriesStyle(PointGroup *group)':
    names 'PointRenderer::PointGroup', which has no cute class yet.
  - Qt's 'void PointRenderer::calculateRenderCoordinates(AxisRenderer
    *axisRenderer, QAbstractSeries *series, qreal origX, qreal origY, qreal
    *renderX, qreal *renderY)': takes a number to change where it is.
  - Qt's 'void PointRenderer::reverseRenderCoordinates(AxisRenderer
    *axisRenderer, QAbstractSeries *series, qreal renderX, qreal renderY,
    qreal *origX, qreal *origY)': takes a number to change where it is.
  - Qt's 'void PointRenderer::destroyGroupMarkers(PointGroup *group,
    qsizetype keepCount)': names 'PointRenderer::PointGroup', which has no
    cute class yet.

  What has no ritual
  ------------------

  11 of the 36 functions Qt declares: 6 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 3 leans on
  'PointRenderer; 2 not a gap.

  What to expect
  --------------

  - The C++ PointRenderer is created at the first use, not by
    'PointRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ PointRenderer.
  - Qt tells when it has removed the C++ PointRenderer. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's PointRenderer that has no cute function yet,
    '__init__', 'afterPolish', 'afterUpdate', 'calculateRenderCoordinates',
    'destroyGroupMarkers', 'getSeriesStyle', 'handlePolish', 'paintSnapshot',
    'updateLegendData', 'updateLineSeries', 'updatePointDelegate',
    'updateScatterSeries', 'updateSplineSeries', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside PointRenderer, each a class in here as in
  #  C++.

  class PointPaintData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's PointRenderer::PointPaintData: a plain Python
    object standing in front of one C++ PointRenderer::PointPaintData.

    C++ hands a PointRenderer::PointPaintData around as a copy, so every C++
    PointRenderer::PointPaintData behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's PointRenderer::PointPaintData yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'PointRenderer::PointPaintData::~PointPaintData()': the
      destructor: Python removes its C++ PointRenderer::PointPaintData by it,
      and has no other use for it.

    What to expect
    --------------

    - The C++ PointRenderer::PointPaintData is created at the first use, not
      by 'PointRenderer::PointPaintData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a PointRenderer::PointPaintData back gives a copy the
      ritual made for Python, in a new cute PointRenderer::PointPaintData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'PointRenderer::PointPaintData'

    #  Qt's '~PointRenderer::PointPaintData()'. Naming it makes this a value
    #  class: Python owns every C++ PointRenderer::PointPaintData behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN13PointRenderer14PointPaintDataD1Ev'

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
  __qt_class__ = 'PointRenderer'

  #  A C++ PointRenderer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_PointRenderer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *PointRenderer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/pointrenderer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *PointRenderer::metaObject() const
    address = self.uglySide.call('ritual_ZNK13PointRenderer10metaObjectEv')
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
    Qt's 'PointRenderer::PointRenderer(QGraphsView *graph, bool
    clipPlotArea)': leans on 'PointRenderer::qt_metacall(QMetaObject::Call,
    int, void**)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'PointRenderer.__init__' has no cute function yet. Qt's "
        "'PointRenderer::PointRenderer(QGraphsView *graph, bool "
        "clipPlotArea)': leans on "
        "'PointRenderer::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  def resetShapePathCount(self) -> None:
    """
    Calls Qt's 'void PointRenderer::resetShapePathCount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/pointrenderer.html#resetShapePathCount
    """
    #  void PointRenderer::resetShapePathCount()
    self.uglySide.call('ritual_ZN13PointRenderer19resetShapePathCountEv')

  def synchronizeData(self) -> None:
    """
    Calls Qt's 'void PointRenderer::synchronizeData()'.

    Qt's own words: https://doc.qt.io/qt-6/pointrenderer.html#synchronizeData
    """
    #  void PointRenderer::synchronizeData()
    self.uglySide.call('ritual_ZN13PointRenderer15synchronizeDataEv')

  @overload(QXYSeries)
  @overload(NoneType)
  def updateSeries(self, series: Optional[QXYSeries]) -> None:
    """
    Calls Qt's 'void PointRenderer::updateSeries(QXYSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/pointrenderer.html#updateSeries

    Parameters
    ----------

    series : Optional[QXYSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void PointRenderer::updateSeries(QXYSeries *series)
    self.uglySide.call(
        'ritual_ZN13PointRenderer12updateSeriesEP9QXYSeries',
        self._addressOf(series),
    )

  @overload(QAbstractSeries)
  @overload(NoneType)
  def seriesAboutToBeRemoved(
      self,
      series: Optional[QAbstractSeries],
  ) -> None:
    """
    Calls Qt's 'void PointRenderer::seriesAboutToBeRemoved(QAbstractSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/pointrenderer.html#seriesAboutToBeRemoved

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void PointRenderer::seriesAboutToBeRemoved(QAbstractSeries *series)
    self.uglySide.call(
        'ritual_ZN13PointRenderer22seriesAboutToBeRemovedEP15QAbstractSerie'
        's',
        self._addressOf(series),
    )

  @overload(QHoverEvent)
  @overload(NoneType)
  def handleHoverMove(self, event: Optional[QHoverEvent]) -> bool:
    """
    Calls Qt's 'bool PointRenderer::handleHoverMove(QHoverEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/pointrenderer.html#handleHoverMove

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool PointRenderer::handleHoverMove(QHoverEvent *event)
    return self.uglySide.call(
        'ritual_ZN13PointRenderer15handleHoverMoveEP11QHoverEvent',
        self._addressOf(event),
    )

  @overload(QAbstractSeries, float, float)
  @overload(NoneType, float, float)
  def reverseRenderCoordinates(
      self,
      series: Optional[QAbstractSeries],
      x: float,
      y: float,
  ) -> QPointF:
    """
    Calls Qt's 'QPointF
    PointRenderer::reverseRenderCoordinates(QAbstractSeries *series, qreal x,
    qreal y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/pointrenderer.html#reverseRenderCoordinates

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF PointRenderer::reverseRenderCoordinates(QAbstractSeries
    #      *series, qreal x, qreal y)
    address = self.uglySide.call(
        'ritual_ZN13PointRenderer24reverseRenderCoordinatesEP15QAbstractSer'
        'iesdd',
        self._addressOf(series), x, y,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload()
  @overload(QXYSeries)
  @overload(NoneType)
  def defaultSize(self, series: Optional[QXYSeries] = None) -> float:
    """
    Calls Qt's 'qreal PointRenderer::defaultSize(QXYSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/pointrenderer.html#defaultSize

    Parameters
    ----------

    series : Optional[QXYSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  qreal PointRenderer::defaultSize(QXYSeries *series)
    return self.uglySide.call(
        'ritual_ZN13PointRenderer11defaultSizeEP9QXYSeries',
        self._addressOf(series),
    )

  @overload(QXYSeries)
  @overload(NoneType)
  def hidePointDelegates(self, series: Optional[QXYSeries]) -> None:
    """
    Calls Qt's 'void PointRenderer::hidePointDelegates(QXYSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/pointrenderer.html#hidePointDelegates

    Parameters
    ----------

    series : Optional[QXYSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void PointRenderer::hidePointDelegates(QXYSeries *series)
    self.uglySide.call(
        'ritual_ZN13PointRenderer18hidePointDelegatesEP9QXYSeries',
        self._addressOf(series),
    )

  @overload(QEventPoint, Qt.MouseButton)
  def onSingleTapped(
      self,
      eventPoint: QEventPoint,
      button: Qt.MouseButton,
  ) -> None:
    """
    Calls Qt's 'void PointRenderer::onSingleTapped(QEventPoint eventPoint,
    Qt::MouseButton button)'.

    Qt's own words: https://doc.qt.io/qt-6/pointrenderer.html#onSingleTapped

    Parameters
    ----------

    eventPoint : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.

    button : Qt.MouseButton
      Passed on as its number.
    """
    #  void PointRenderer::onSingleTapped(QEventPoint eventPoint,
    #      Qt::MouseButton button)
    self.uglySide.call(
        'ritual_ZN13PointRenderer14onSingleTappedE11QEventPointN2Qt11MouseB'
        'uttonE',
        self._valueOf(eventPoint), button.value,
    )

  @overload(QEventPoint, Qt.MouseButton)
  def onDoubleTapped(
      self,
      eventPoint: QEventPoint,
      button: Qt.MouseButton,
  ) -> None:
    """
    Calls Qt's 'void PointRenderer::onDoubleTapped(QEventPoint eventPoint,
    Qt::MouseButton button)'.

    Qt's own words: https://doc.qt.io/qt-6/pointrenderer.html#onDoubleTapped

    Parameters
    ----------

    eventPoint : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.

    button : Qt.MouseButton
      Passed on as its number.
    """
    #  void PointRenderer::onDoubleTapped(QEventPoint eventPoint,
    #      Qt::MouseButton button)
    self.uglySide.call(
        'ritual_ZN13PointRenderer14onDoubleTappedE11QEventPointN2Qt11MouseB'
        'uttonE',
        self._valueOf(eventPoint), button.value,
    )

  def onPressedChanged(self) -> None:
    """
    Calls Qt's 'void PointRenderer::onPressedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/pointrenderer.html#onPressedChanged
    """
    #  void PointRenderer::onPressedChanged()
    self.uglySide.call('ritual_ZN13PointRenderer16onPressedChangedEv')

  @overload(QXYSeries, int, int)
  @overload(NoneType, int, int)
  def adjustPressedPointIndexForRemoval(
      self,
      series: Optional[QXYSeries],
      removedIndex: int,
      removedCount: int,
  ) -> None:
    """
    Calls Qt's 'void
    PointRenderer::adjustPressedPointIndexForRemoval(QXYSeries *series,
    qsizetype removedIndex, qsizetype removedCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/pointrenderer.html

    Parameters
    ----------

    series : Optional[QXYSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    removedIndex : int
      Passed on as it is.

    removedCount : int
      Passed on as it is.
    """
    #  void PointRenderer::adjustPressedPointIndexForRemoval(QXYSeries
    #      *series, qsizetype removedIndex, qsizetype removedCount)
    self.uglySide.call(
        'ritual_ZN13PointRenderer33adjustPressedPointIndexForRemovalEP9QXYS'
        'eriesxx',
        self._addressOf(series), removedIndex, removedCount,
    )

  @overload(QXYSeries, int, int)
  @overload(NoneType, int, int)
  def adjustPressedPointIndexForInsertion(
      self,
      series: Optional[QXYSeries],
      insertedIndex: int,
      insertedCount: int,
  ) -> None:
    """
    Calls Qt's 'void
    PointRenderer::adjustPressedPointIndexForInsertion(QXYSeries *series,
    qsizetype insertedIndex, qsizetype insertedCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/pointrenderer.html

    Parameters
    ----------

    series : Optional[QXYSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    insertedIndex : int
      Passed on as it is.

    insertedCount : int
      Passed on as it is.
    """
    #  void PointRenderer::adjustPressedPointIndexForInsertion(QXYSeries
    #      *series, qsizetype insertedIndex, qsizetype insertedCount)
    self.uglySide.call(
        'ritual_ZN13PointRenderer35adjustPressedPointIndexForInsertionEP9QX'
        'YSeriesxx',
        self._addressOf(series), insertedIndex, insertedCount,
    )

  @overload(QXYSeries)
  @overload(NoneType)
  def forgetPressedPoint(self, series: Optional[QXYSeries]) -> None:
    """
    Calls Qt's 'void PointRenderer::forgetPressedPoint(QXYSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/pointrenderer.html#forgetPressedPoint

    Parameters
    ----------

    series : Optional[QXYSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void PointRenderer::forgetPressedPoint(QXYSeries *series)
    self.uglySide.call(
        'ritual_ZN13PointRenderer18forgetPressedPointEP9QXYSeries',
        self._addressOf(series),
    )

  @staticmethod
  def afterPolish(*__, **_) -> Never:
    """
    Qt's 'void PointRenderer::afterPolish(QList<QAbstractSeries *>
    &cleanupSeries)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'QGraphs2DPointRendererAfterPolish'.
    """
    raise NotImplementedError(
        "'PointRenderer.afterPolish' has no cute function yet. Qt's 'void "
        "PointRenderer::afterPolish(QList<QAbstractSeries *> "
        "&cleanupSeries)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'QGraphs2DPointRendererAfterPolish'.")

  @staticmethod
  def afterUpdate(*__, **_) -> Never:
    """
    Qt's 'void PointRenderer::afterUpdate(QList<QAbstractSeries *>
    &cleanupSeries)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'PointRenderer.afterUpdate' has no cute function yet. Qt's 'void "
        "PointRenderer::afterUpdate(QList<QAbstractSeries *> "
        "&cleanupSeries)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def calculateRenderCoordinates(*__, **_) -> Never:
    """
    Qt's 'void PointRenderer::calculateRenderCoordinates(AxisRenderer
    *axisRenderer, QAbstractSeries *series, qreal origX, qreal origY, qreal
    *renderX, qreal *renderY)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'PointRenderer.calculateRenderCoordinates' has no cute function "
        "yet. Qt's 'void "
        "PointRenderer::calculateRenderCoordinates(AxisRenderer "
        "*axisRenderer, QAbstractSeries *series, qreal origX, qreal origY, "
        "qreal *renderX, qreal *renderY)': takes a number to change where "
        "it is.")

  @staticmethod
  def destroyGroupMarkers(*__, **_) -> Never:
    """
    Qt's 'void PointRenderer::destroyGroupMarkers(PointGroup *group,
    qsizetype keepCount)': names 'PointRenderer::PointGroup', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'PointRenderer.destroyGroupMarkers' has no cute function yet. Qt's "
        "'void PointRenderer::destroyGroupMarkers(PointGroup *group, "
        "qsizetype keepCount)': names 'PointRenderer::PointGroup', which "
        "has no cute class yet.")

  @staticmethod
  def getSeriesStyle(*__, **_) -> Never:
    """
    Qt's 'SeriesStyle PointRenderer::getSeriesStyle(PointGroup *group)':
    names 'PointRenderer::PointGroup', which has no cute class yet.
    """
    raise NotImplementedError(
        "'PointRenderer.getSeriesStyle' has no cute function yet. Qt's "
        "'SeriesStyle PointRenderer::getSeriesStyle(PointGroup *group)': "
        "names 'PointRenderer::PointGroup', which has no cute class yet.")

  @staticmethod
  def handlePolish(*__, **_) -> Never:
    """
    Qt's 'void PointRenderer::handlePolish(QXYSeries *series)': leans on
    'PointRenderer::updateLegendData(QXYSeries*, QLegendData&)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'PointRenderer.handlePolish' has no cute function yet. Qt's 'void "
        "PointRenderer::handlePolish(QXYSeries *series)': leans on "
        "'PointRenderer::updateLegendData(QXYSeries*, QLegendData&)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def paintSnapshot(*__, **_) -> Never:
    """
    - Qt's 'void PointRenderer::paintSnapshot(const PaintSnapshot &snapshot,
      QCanvasPainter *p)': takes a type Python has no way to hand over yet.
    - Qt's 'QList<PointPaintData> PointRenderer::paintSnapshot() const':
      gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'PointRenderer.paintSnapshot' has no cute function yet. Qt's 'void "
        "PointRenderer::paintSnapshot(const PaintSnapshot &snapshot, "
        "QCanvasPainter *p)': takes a type Python has no way to hand over "
        "yet. Qt's 'QList<PointPaintData> PointRenderer::paintSnapshot() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def updateLegendData(*__, **_) -> Never:
    """
    Qt's 'void PointRenderer::updateLegendData(QXYSeries *series, QLegendData
    &legendData)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: member access into
    incomplete type 'QXYSeriesPrivate'.
    """
    raise NotImplementedError(
        "'PointRenderer.updateLegendData' has no cute function yet. Qt's "
        "'void PointRenderer::updateLegendData(QXYSeries *series, "
        "QLegendData &legendData)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: "
        "member access into incomplete type 'QXYSeriesPrivate'.")

  @staticmethod
  def updateLineSeries(*__, **_) -> Never:
    """
    Qt's 'void PointRenderer::updateLineSeries(QLineSeries *line, QLegendData
    &legendData)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'QGraphs2DPointRendererUpdateLineSeries_entry'.
    """
    raise NotImplementedError(
        "'PointRenderer.updateLineSeries' has no cute function yet. Qt's "
        "'void PointRenderer::updateLineSeries(QLineSeries *line, "
        "QLegendData &legendData)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier "
        "'QGraphs2DPointRendererUpdateLineSeries_entry'.")

  @staticmethod
  def updatePointDelegate(*__, **_) -> Never:
    """
    Qt's 'void PointRenderer::updatePointDelegate(QXYSeries *series,
    PointGroup *group, qsizetype pointIndex, qreal x, qreal y)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'TAG_POINT_SELECTED'.
    """
    raise NotImplementedError(
        "'PointRenderer.updatePointDelegate' has no cute function yet. Qt's "
        "'void PointRenderer::updatePointDelegate(QXYSeries *series, "
        "PointGroup *group, qsizetype pointIndex, qreal x, qreal y)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'TAG_POINT_SELECTED'.")

  @staticmethod
  def updateScatterSeries(*__, **_) -> Never:
    """
    Qt's 'void PointRenderer::updateScatterSeries(QScatterSeries *scatter,
    QLegendData &legendData)': Qt's library has no name for it, and its code
    in Qt's source does not compile apart from its file: use of undeclared
    identifier 'QGraphs2DPointRendererUpdateScatterSeries_entry'.
    """
    raise NotImplementedError(
        "'PointRenderer.updateScatterSeries' has no cute function yet. Qt's "
        "'void PointRenderer::updateScatterSeries(QScatterSeries *scatter, "
        "QLegendData &legendData)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier "
        "'QGraphs2DPointRendererUpdateScatterSeries_entry'.")

  @staticmethod
  def updateSplineSeries(*__, **_) -> Never:
    """
    Qt's 'void PointRenderer::updateSplineSeries(QSplineSeries *spline,
    QLegendData &legendData)': Qt's library has no name for it, and its code
    in Qt's source does not compile apart from its file: use of undeclared
    identifier 'QGraphs2DPointRendererUpdateSplineSeries_entry'.
    """
    raise NotImplementedError(
        "'PointRenderer.updateSplineSeries' has no cute function yet. Qt's "
        "'void PointRenderer::updateSplineSeries(QSplineSeries *spline, "
        "QLegendData &legendData)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier "
        "'QGraphs2DPointRendererUpdateSplineSeries_entry'.")
