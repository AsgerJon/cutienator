"""
QCustomSeriesCanvasRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qcustomseriescanvasrenderer.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QCustomSeries
  from ..QtCanvasPainter import QCanvasPainter, QCanvasPainterItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCanvasPainter = WAIT['QCanvasPainter']
  QCanvasPainterItem = WAIT['QCanvasPainterItem']
  QCustomSeries = WAIT['QCustomSeries']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCustomSeriesCanvasRenderer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCustomSeriesCanvasRenderer: a plain Python object
  standing in front of one C++ QCustomSeriesCanvasRenderer.

  What exists
  -----------

  Every function of Qt's QCustomSeriesCanvasRenderer that has a ritual and
  that Python can call so far, 4 names in all: 'initializeResources',
  'synchronizeData', 'canvasPrePaint', 'canvasPaint'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCustomSeriesCanvasRenderer::~QCustomSeriesCanvasRenderer()': the
    destructor: Python never removes a C++ QCustomSeriesCanvasRenderer.

  What has no ritual
  ------------------

  4 of the 10 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QCustomSeriesCanvasRenderer is created at the first use, not by
    'QCustomSeriesCanvasRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCustomSeriesCanvasRenderer.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCustomSeriesCanvasRenderer'

  #  A C++ QCustomSeriesCanvasRenderer Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCustomSeriesCanvasRenderer'

  #  The functions Qt calls itself that QCustomSeriesCanvasRenderer is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'initializeResources': (
          ('_ZN27QCustomSeriesCanvasRenderer19initializeResourcesEP13QCusto'
           'mSeriesP14QCanvasPainter',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGraphs:QCustomSeries'),
               ('address', 'address', 'QtCanvasPainter:QCanvasPainter'),
           )),
      ),
      'synchronizeData': (
          ('_ZN27QCustomSeriesCanvasRenderer15synchronizeDataEP13QCustomSer'
           'iesP18QCanvasPainterItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGraphs:QCustomSeries'),
               ('address', 'address', 'QtCanvasPainter:QCanvasPainterItem'),
           )),
      ),
      'canvasPrePaint': (
          ('_ZN27QCustomSeriesCanvasRenderer14canvasPrePaintEP14QCanvasPain'
           'ter',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCanvasPainter:QCanvasPainter'),
           )),
      ),
      'canvasPaint': (
          ('_ZN27QCustomSeriesCanvasRenderer11canvasPaintEP14QCanvasPainter',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCanvasPainter:QCanvasPainter'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QCustomSeriesCanvasRenderer::QCustomSeriesCanvasRenderer()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustomseriescanvasrenderer.html
    """
    #  QCustomSeriesCanvasRenderer::QCustomSeriesCanvasRenderer()
    self._noteCreation(QCustomSeriesCanvasRenderer, lambda: Rituals.call(
        'ritual_ZN27QCustomSeriesCanvasRendererC1Ev',
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

  @overload(QCustomSeries, QCanvasPainter)
  @overload(QCustomSeries, NoneType)
  @overload(NoneType, QCanvasPainter)
  @overload(NoneType, NoneType)
  def initializeResources(
      self,
      series: Optional[QCustomSeries],
      p: Optional[QCanvasPainter],
  ) -> None:
    """
    Calls Qt's 'void
    QCustomSeriesCanvasRenderer::initializeResources(QCustomSeries *series,
    QCanvasPainter *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustomseriescanvasrenderer.html

    Parameters
    ----------

    series : Optional[QCustomSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    p : Optional[QCanvasPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCustomSeriesCanvasRenderer::initializeResources(QCustomSeries
    #      *series, QCanvasPainter *p)
    ritual = (
        'ritual_ZN27QCustomSeriesCanvasRenderer19initializeResourcesEP13QCu'
        'stomSeriesP14QCanvasPainter')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QCustomSeriesCanvasRenderer19initializeResourcesE'
          'P13QCustomSeriesP14QCanvasPainter')
    self.uglySide.call(ritual, self._addressOf(series), self._addressOf(p))

  @overload(QCustomSeries, QCanvasPainterItem)
  @overload(QCustomSeries, NoneType)
  @overload(NoneType, QCanvasPainterItem)
  @overload(NoneType, NoneType)
  def synchronizeData(
      self,
      series: Optional[QCustomSeries],
      item: Optional[QCanvasPainterItem],
  ) -> None:
    """
    Calls Qt's 'void
    QCustomSeriesCanvasRenderer::synchronizeData(QCustomSeries *series,
    QCanvasPainterItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustomseriescanvasrenderer.html#synchronizeData

    Parameters
    ----------

    series : Optional[QCustomSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QCanvasPainterItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCustomSeriesCanvasRenderer::synchronizeData(QCustomSeries
    #      *series, QCanvasPainterItem *item)
    ritual = (
        'ritual_ZN27QCustomSeriesCanvasRenderer15synchronizeDataEP13QCustom'
        'SeriesP18QCanvasPainterItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QCustomSeriesCanvasRenderer15synchronizeDataEP13Q'
          'CustomSeriesP18QCanvasPainterItem')
    self.uglySide.call(
        ritual, self._addressOf(series), self._addressOf(item),
    )

  @overload(QCanvasPainter)
  @overload(NoneType)
  def canvasPrePaint(self, p: Optional[QCanvasPainter]) -> None:
    """
    Calls Qt's 'void
    QCustomSeriesCanvasRenderer::canvasPrePaint(QCanvasPainter *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustomseriescanvasrenderer.html#canvasPrePaint

    Parameters
    ----------

    p : Optional[QCanvasPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCustomSeriesCanvasRenderer::canvasPrePaint(QCanvasPainter *p)
    ritual = (
        'ritual_ZN27QCustomSeriesCanvasRenderer14canvasPrePaintEP14QCanvasP'
        'ainter')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QCustomSeriesCanvasRenderer14canvasPrePaintEP14QC'
          'anvasPainter')
    self.uglySide.call(ritual, self._addressOf(p))

  @overload(QCanvasPainter)
  @overload(NoneType)
  def canvasPaint(self, p: Optional[QCanvasPainter]) -> None:
    """
    Calls Qt's 'void QCustomSeriesCanvasRenderer::canvasPaint(QCanvasPainter
    *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustomseriescanvasrenderer.html#canvasPaint

    Parameters
    ----------

    p : Optional[QCanvasPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCustomSeriesCanvasRenderer::canvasPaint(QCanvasPainter *p)
    self.uglySide.call(
        'ritual_ZN27QCustomSeriesCanvasRenderer11canvasPaintEP14QCanvasPain'
        'ter',
        self._addressOf(p),
    )
