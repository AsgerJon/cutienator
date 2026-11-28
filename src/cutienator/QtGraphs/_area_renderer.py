"""
AreaRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/arearenderer_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means AreaRenderer to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QAbstractSeries, QAreaSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractSeries = WAIT['QtGraphs:QAbstractSeries']
  QAreaSeries = WAIT['QtGraphs:QAreaSeries']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class AreaRenderer(QQuickItem):
  """
  The cute side of Qt's AreaRenderer: a plain Python object standing in front
  of one C++ AreaRenderer.

  It is built on the cute 'QQuickItem', as Qt's AreaRenderer is built on Qt's
  QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's AreaRenderer that has a ritual and that Python can
  call so far, 5 names in all: 'metaObject', 'resetShapePathCount',
  'synchronizeData', 'updateSeries', 'seriesAboutToBeRemoved'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *AreaRenderer::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int AreaRenderer::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'AreaRenderer::~AreaRenderer()': the destructor: Python never
    removes a C++ AreaRenderer.
  - Qt's 'PaintSnapshot AreaRenderer::paintSnapshot() const': gives a type
    Python has no way to take yet.
  - Qt's 'void AreaRenderer::paintSnapshot(const PaintSnapshot &snapshot,
    QCanvasPainter *p)': takes a type Python has no way to hand over yet.
  - Qt's 'void AreaRenderer::afterUpdate(QList<QAbstractSeries *>
    &cleanupSeries)': takes a type Python has no way to hand over yet.
  - Qt's 'SeriesStyle AreaRenderer::getSeriesStyle(PointGroup *group)': names
    'AreaRenderer::PointGroup', which has no cute class yet.
  - Qt's 'void AreaRenderer::calculateRenderCoordinates(QAreaSeries *series,
    qreal origX, qreal origY, qreal *renderX, qreal *renderY) const': takes a
    number to change where it is.
  - Qt's 'void AreaRenderer::calculateAxisCoordinates(QAreaSeries *series,
    qreal origX, qreal origY, qreal *axisX, qreal *axisY) const': takes a
    number to change where it is.

  What has no ritual
  ------------------

  11 of the 25 functions Qt declares: 6 leans on 'AreaRenderer; 3 Qt's
  library has no name for it, and its code in Qt's source does not compile
  apart from its file; 2 not a gap.

  What to expect
  --------------

  - The C++ AreaRenderer is created at the first use, not by
    'AreaRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ AreaRenderer.
  - Qt tells when it has removed the C++ AreaRenderer. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's AreaRenderer that has no cute function yet, '__init__',
    'afterPolish', 'afterUpdate', 'calculateAxisCoordinates',
    'calculateRenderCoordinates', 'getSeriesStyle', 'handleHoverMove',
    'handlePolish', 'onDoubleTapped', 'onPressedChanged', 'onSingleTapped',
    'paintSnapshot', 'pointInArea', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside AreaRenderer, each a class in here as in
  #  C++.

  class AreaPaintData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's AreaRenderer::AreaPaintData: a plain Python object
    standing in front of one C++ AreaRenderer::AreaPaintData.

    C++ hands a AreaRenderer::AreaPaintData around as a copy, so every C++
    AreaRenderer::AreaPaintData behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's AreaRenderer::AreaPaintData yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'AreaRenderer::AreaPaintData::~AreaPaintData()': the destructor:
      Python removes its C++ AreaRenderer::AreaPaintData by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ AreaRenderer::AreaPaintData is created at the first use, not by
      'AreaRenderer::AreaPaintData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a AreaRenderer::AreaPaintData back gives a copy the
      ritual made for Python, in a new cute AreaRenderer::AreaPaintData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'AreaRenderer::AreaPaintData'

    #  Qt's '~AreaRenderer::AreaPaintData()'. Naming it makes this a value
    #  class: Python owns every C++ AreaRenderer::AreaPaintData behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN12AreaRenderer13AreaPaintDataD1Ev'

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
  __qt_class__ = 'AreaRenderer'

  #  A C++ AreaRenderer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_AreaRenderer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *AreaRenderer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/arearenderer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *AreaRenderer::metaObject() const
    address = self.uglySide.call('ritual_ZNK12AreaRenderer10metaObjectEv')
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
    Qt's 'AreaRenderer::AreaRenderer(QGraphsView *graph, bool clipPlotArea)':
    leans on 'AreaRenderer::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'AreaRenderer.__init__' has no cute function yet. Qt's "
        "'AreaRenderer::AreaRenderer(QGraphsView *graph, bool "
        "clipPlotArea)': leans on "
        "'AreaRenderer::qt_metacall(QMetaObject::Call, int, void**)', which "
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

  def resetShapePathCount(self) -> None:
    """
    Calls Qt's 'void AreaRenderer::resetShapePathCount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/arearenderer.html#resetShapePathCount
    """
    #  void AreaRenderer::resetShapePathCount()
    self.uglySide.call('ritual_ZN12AreaRenderer19resetShapePathCountEv')

  def synchronizeData(self) -> None:
    """
    Calls Qt's 'void AreaRenderer::synchronizeData()'.

    Qt's own words: https://doc.qt.io/qt-6/arearenderer.html#synchronizeData
    """
    #  void AreaRenderer::synchronizeData()
    self.uglySide.call('ritual_ZN12AreaRenderer15synchronizeDataEv')

  @overload(QAreaSeries)
  @overload(NoneType)
  def updateSeries(self, series: Optional[QAreaSeries]) -> None:
    """
    Calls Qt's 'void AreaRenderer::updateSeries(QAreaSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/arearenderer.html#updateSeries

    Parameters
    ----------

    series : Optional[QAreaSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void AreaRenderer::updateSeries(QAreaSeries *series)
    self.uglySide.call(
        'ritual_ZN12AreaRenderer12updateSeriesEP11QAreaSeries',
        self._addressOf(series),
    )

  @overload(QAbstractSeries)
  @overload(NoneType)
  def seriesAboutToBeRemoved(
      self,
      series: Optional[QAbstractSeries],
  ) -> None:
    """
    Calls Qt's 'void AreaRenderer::seriesAboutToBeRemoved(QAbstractSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/arearenderer.html#seriesAboutToBeRemoved

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void AreaRenderer::seriesAboutToBeRemoved(QAbstractSeries *series)
    self.uglySide.call(
        'ritual_ZN12AreaRenderer22seriesAboutToBeRemovedEP15QAbstractSeries',
        self._addressOf(series),
    )

  @staticmethod
  def afterPolish(*__, **_) -> Never:
    """
    Qt's 'void AreaRenderer::afterPolish(QList<QAbstractSeries *>
    &cleanupSeries)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'QGraphs2DAreaRendereAfterPolish'.
    """
    raise NotImplementedError(
        "'AreaRenderer.afterPolish' has no cute function yet. Qt's 'void "
        "AreaRenderer::afterPolish(QList<QAbstractSeries *> "
        "&cleanupSeries)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'QGraphs2DAreaRendereAfterPolish'.")

  @staticmethod
  def afterUpdate(*__, **_) -> Never:
    """
    Qt's 'void AreaRenderer::afterUpdate(QList<QAbstractSeries *>
    &cleanupSeries)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'AreaRenderer.afterUpdate' has no cute function yet. Qt's 'void "
        "AreaRenderer::afterUpdate(QList<QAbstractSeries *> "
        "&cleanupSeries)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def calculateAxisCoordinates(*__, **_) -> Never:
    """
    Qt's 'void AreaRenderer::calculateAxisCoordinates(QAreaSeries *series,
    qreal origX, qreal origY, qreal *axisX, qreal *axisY) const': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'AreaRenderer.calculateAxisCoordinates' has no cute function yet. "
        "Qt's 'void AreaRenderer::calculateAxisCoordinates(QAreaSeries "
        "*series, qreal origX, qreal origY, qreal *axisX, qreal *axisY) "
        "const': takes a number to change where it is.")

  @staticmethod
  def calculateRenderCoordinates(*__, **_) -> Never:
    """
    Qt's 'void AreaRenderer::calculateRenderCoordinates(QAreaSeries *series,
    qreal origX, qreal origY, qreal *renderX, qreal *renderY) const': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'AreaRenderer.calculateRenderCoordinates' has no cute function "
        "yet. Qt's 'void "
        "AreaRenderer::calculateRenderCoordinates(QAreaSeries *series, "
        "qreal origX, qreal origY, qreal *renderX, qreal *renderY) const': "
        "takes a number to change where it is.")

  @staticmethod
  def getSeriesStyle(*__, **_) -> Never:
    """
    Qt's 'SeriesStyle AreaRenderer::getSeriesStyle(PointGroup *group)': names
    'AreaRenderer::PointGroup', which has no cute class yet.
    """
    raise NotImplementedError(
        "'AreaRenderer.getSeriesStyle' has no cute function yet. Qt's "
        "'SeriesStyle AreaRenderer::getSeriesStyle(PointGroup *group)': "
        "names 'AreaRenderer::PointGroup', which has no cute class yet.")

  @staticmethod
  def handleHoverMove(*__, **_) -> Never:
    """
    Qt's 'bool AreaRenderer::handleHoverMove(QHoverEvent *event)': leans on
    'AreaRenderer::pointInArea(QPoint, QAreaSeries*) const', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'AreaRenderer.handleHoverMove' has no cute function yet. Qt's "
        "'bool AreaRenderer::handleHoverMove(QHoverEvent *event)': leans on "
        "'AreaRenderer::pointInArea(QPoint, QAreaSeries*) const', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def handlePolish(*__, **_) -> Never:
    """
    Qt's 'void AreaRenderer::handlePolish(QAreaSeries *series)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier
    'QGraphs2DAreaRendererCalculateSeriesU'.
    """
    raise NotImplementedError(
        "'AreaRenderer.handlePolish' has no cute function yet. Qt's 'void "
        "AreaRenderer::handlePolish(QAreaSeries *series)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier "
        "'QGraphs2DAreaRendererCalculateSeriesU'.")

  @staticmethod
  def onDoubleTapped(*__, **_) -> Never:
    """
    Qt's 'void AreaRenderer::onDoubleTapped(QEventPoint eventPoint,
    Qt::MouseButton button)': leans on 'AreaRenderer::pointInArea(QPoint,
    QAreaSeries*) const', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AreaRenderer.onDoubleTapped' has no cute function yet. Qt's 'void "
        "AreaRenderer::onDoubleTapped(QEventPoint eventPoint, "
        "Qt::MouseButton button)': leans on "
        "'AreaRenderer::pointInArea(QPoint, QAreaSeries*) const', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def onPressedChanged(*__, **_) -> Never:
    """
    Qt's 'void AreaRenderer::onPressedChanged()': leans on
    'AreaRenderer::pointInArea(QPoint, QAreaSeries*) const', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'AreaRenderer.onPressedChanged' has no cute function yet. Qt's "
        "'void AreaRenderer::onPressedChanged()': leans on "
        "'AreaRenderer::pointInArea(QPoint, QAreaSeries*) const', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def onSingleTapped(*__, **_) -> Never:
    """
    Qt's 'void AreaRenderer::onSingleTapped(QEventPoint eventPoint,
    Qt::MouseButton button)': leans on 'AreaRenderer::pointInArea(QPoint,
    QAreaSeries*) const', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AreaRenderer.onSingleTapped' has no cute function yet. Qt's 'void "
        "AreaRenderer::onSingleTapped(QEventPoint eventPoint, "
        "Qt::MouseButton button)': leans on "
        "'AreaRenderer::pointInArea(QPoint, QAreaSeries*) const', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def paintSnapshot(*__, **_) -> Never:
    """
    - Qt's 'PaintSnapshot AreaRenderer::paintSnapshot() const': gives a type
      Python has no way to take yet.
    - Qt's 'void AreaRenderer::paintSnapshot(const PaintSnapshot &snapshot,
      QCanvasPainter *p)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'AreaRenderer.paintSnapshot' has no cute function yet. Qt's "
        "'PaintSnapshot AreaRenderer::paintSnapshot() const': gives a type "
        "Python has no way to take yet. Qt's 'void "
        "AreaRenderer::paintSnapshot(const PaintSnapshot &snapshot, "
        "QCanvasPainter *p)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def pointInArea(*__, **_) -> Never:
    """
    Qt's 'bool AreaRenderer::pointInArea(QPoint pt, QAreaSeries *series)
    const': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'QGraphs2DAreaRenderePointInArea'.
    """
    raise NotImplementedError(
        "'AreaRenderer.pointInArea' has no cute function yet. Qt's 'bool "
        "AreaRenderer::pointInArea(QPoint pt, QAreaSeries *series) const': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'QGraphs2DAreaRenderePointInArea'.")
