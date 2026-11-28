"""
QBlitterPaintEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qpaintengine_blitter_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QBlitterPaintEngine to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QPaintEngine, QRasterPaintEngine

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPoint, QPointF, QRect, QRectF
  from . import QBlittablePlatformPixmap, QBrush, QColor, QImage
  from . import QPaintDevice, QPainterPath, QPainterState, QPixmap, QSpanData
  from . import QStaticTextItem, QTextItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBlittablePlatformPixmap = WAIT['QBlittablePlatformPixmap']
  QBrush = WAIT['QBrush']
  QColor = WAIT['QColor']
  QImage = WAIT['QImage']
  QPaintDevice = WAIT['QPaintDevice']
  QPainterPath = WAIT['QPainterPath']
  QPainterState = WAIT['QPainterState']
  QPixmap = WAIT['QPixmap']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QRect = WAIT['QRect']
  QRectF = WAIT['QRectF']
  QSpanData = WAIT['QSpanData']
  QStaticTextItem = WAIT['QStaticTextItem']
  QTextItem = WAIT['QTextItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBlitterPaintEngine(QRasterPaintEngine):
  """
  The cute side of Qt's QBlitterPaintEngine: a plain Python object standing
  in front of one C++ QBlitterPaintEngine.

  It is built on the cute 'QRasterPaintEngine', as Qt's QBlitterPaintEngine
  is built on Qt's QRasterPaintEngine, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBlitterPaintEngine that has a ritual and that
  Python can call so far, 23 names in all: 'type', 'begin', 'end',
  'fillRect', 'drawRects', 'drawPixmap', 'setState', 'clipEnabledChanged',
  'penChanged', 'brushChanged', 'opacityChanged', 'compositionModeChanged',
  'renderHintsChanged', 'transformChanged', 'drawPolygon', 'fillPath',
  'fillPolygon', 'drawEllipse', 'drawImage', 'drawTiledPixmap',
  'drawTextItem', 'drawPoints', 'drawStaticTextItem'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QBlitterPaintEnginePrivate *QBlitterPaintEngine::d_func()': gives
    'QBlitterPaintEnginePrivate', which has no cute class yet.
  - Qt's 'const QBlitterPaintEnginePrivate *QBlitterPaintEngine::d_func()
    const': gives 'QBlitterPaintEnginePrivate', which has no cute class yet.
  - Qt's 'void QBlitterPaintEngine::fill(const QVectorPath &path, const
    QBrush &brush)': takes a type Python has no way to hand over yet.
  - Qt's 'void QBlitterPaintEngine::stroke(const QVectorPath &path, const
    QPen &pen)': takes a type Python has no way to hand over yet.
  - Qt's 'bool QBlitterPaintEngine::drawCachedGlyphs(int numGlyphs, const
    glyph_t *glyphs, const QFixedPoint *positions, QFontEngine *fontEngine)':
    names 'glyph_t', which has no cute class yet.

  What to expect
  --------------

  - The C++ QBlitterPaintEngine is created at the first use, not by
    'QBlitterPaintEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBlitterPaintEngine.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBlitterPaintEngine'

  #  A C++ QBlitterPaintEngine Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBlitterPaintEngine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QPaintEngine.Type:
    """
    Calls Qt's 'QPaintEngine::Type QBlitterPaintEngine::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qblitterpaintengine.html#type

    Returns
    -------

    QPaintEngine.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPaintEngine.Type(number)' gives.
    """
    #  QPaintEngine::Type QBlitterPaintEngine::type() const
    ritual = 'ritual_ZNK19QBlitterPaintEngine4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QBlitterPaintEngine4typeEv'
    return QPaintEngine.Type(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPainterState)
  @overload(NoneType)
  def setState(self, s: Optional[QPainterState]) -> None:
    """
    Calls Qt's 'void QBlitterPaintEngine::setState(QPainterState *s)'.

    Qt's own words: https://doc.qt.io/qt-6/qblitterpaintengine.html#setState

    Parameters
    ----------

    s : Optional[QPainterState]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBlitterPaintEngine::setState(QPainterState *s)
    ritual = 'ritual_ZN19QBlitterPaintEngine8setStateEP13QPainterState'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QBlitterPaintEngine8setStateEP13QPainterState'
    self.uglySide.call(ritual, self._addressOf(s))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QBlittablePlatformPixmap)
  @overload(NoneType)
  def __init__(self, p: Optional[QBlittablePlatformPixmap]) -> None:
    """
    Notes what was given, for Qt's
    'QBlitterPaintEngine::QBlitterPaintEngine(QBlittablePlatformPixmap *p)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qblitterpaintengine.html#QBlitterPaintEngine

    Parameters
    ----------

    p : Optional[QBlittablePlatformPixmap]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QBlitterPaintEngine::QBlitterPaintEngine(QBlittablePlatformPixmap *p)
    self._noteCreation(QBlitterPaintEngine, lambda: Rituals.call(
        'ritual_ZN19QBlitterPaintEngineC1EP24QBlittablePlatformPixmap',
        self._addressOf(p),
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

  @overload(QPaintDevice)
  @overload(NoneType)
  def begin(self, pdev: Optional[QPaintDevice]) -> bool:
    """
    Calls Qt's 'bool QBlitterPaintEngine::begin(QPaintDevice *pdev)'.

    Qt's own words: https://doc.qt.io/qt-6/qblitterpaintengine.html#begin

    Parameters
    ----------

    pdev : Optional[QPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QBlitterPaintEngine::begin(QPaintDevice *pdev)
    ritual = 'ritual_ZN19QBlitterPaintEngine5beginEP12QPaintDevice'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QBlitterPaintEngine5beginEP12QPaintDevice'
    return self.uglySide.call(ritual, self._addressOf(pdev, 'QPaintDevice'))

  def end(self) -> bool:
    """
    Calls Qt's 'bool QBlitterPaintEngine::end()'.

    Qt's own words: https://doc.qt.io/qt-6/qblitterpaintengine.html#end
    """
    #  bool QBlitterPaintEngine::end()
    ritual = 'ritual_ZN19QBlitterPaintEngine3endEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QBlitterPaintEngine3endEv'
    return self.uglySide.call(ritual)

  @overload(QRectF, QBrush)
  def fillRect(self, rect: QRectF, brush: QBrush) -> None:
    """
    Calls Qt's 'void QBlitterPaintEngine::fillRect(const QRectF &rect, const
    QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qblitterpaintengine.html#fillRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QBlitterPaintEngine::fillRect(const QRectF &rect, const QBrush
    #      &brush)
    ritual = 'ritual_ZN19QBlitterPaintEngine8fillRectERK6QRectFRK6QBrush'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QBlitterPaintEngine8fillRectERK6QRectFRK6QBrush')
    self.uglySide.call(ritual, self._valueOf(rect), self._valueOf(brush))

  @overload(QRectF, QColor)
  def fillRect(self, rect: QRectF, color: QColor) -> None:
    """
    Calls Qt's 'void QBlitterPaintEngine::fillRect(const QRectF &rect, const
    QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qblitterpaintengine.html#fillRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QBlitterPaintEngine::fillRect(const QRectF &rect, const QColor
    #      &color)
    ritual = 'ritual_ZN19QBlitterPaintEngine8fillRectERK6QRectFRK6QColor'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QBlitterPaintEngine8fillRectERK6QRectFRK6QColor')
    self.uglySide.call(ritual, self._valueOf(rect), self._valueOf(color))

  @overload(QRect, int)
  @overload(NoneType, int)
  def drawRects(self, rects: Optional[QRect], rectCount: int) -> None:
    """
    Calls Qt's 'void QBlitterPaintEngine::drawRects(const QRect *rects, int
    rectCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qblitterpaintengine.html#drawRects

    Parameters
    ----------

    rects : Optional[QRect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rectCount : int
      Passed on as it is.
    """
    #  void QBlitterPaintEngine::drawRects(const QRect *rects, int rectCount)
    ritual = 'ritual_ZN19QBlitterPaintEngine9drawRectsEPK5QRecti'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QBlitterPaintEngine9drawRectsEPK5QRecti'
    self.uglySide.call(ritual, self._addressOf(rects), rectCount)

  @overload(QRectF, int)
  def drawRects(self, rects: Optional[QRectF], rectCount: int) -> None:
    """
    Calls Qt's 'void QBlitterPaintEngine::drawRects(const QRectF *rects, int
    rectCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qblitterpaintengine.html#drawRects

    Parameters
    ----------

    rects : Optional[QRectF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rectCount : int
      Passed on as it is.
    """
    #  void QBlitterPaintEngine::drawRects(const QRectF *rects, int
    #      rectCount)
    ritual = 'ritual_ZN19QBlitterPaintEngine9drawRectsEPK6QRectFi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QBlitterPaintEngine9drawRectsEPK6QRectFi'
    self.uglySide.call(ritual, self._addressOf(rects), rectCount)

  @overload(QPointF, QPixmap)
  def drawPixmap(self, p: QPointF, pm: QPixmap) -> None:
    """
    Calls Qt's 'void QBlitterPaintEngine::drawPixmap(const QPointF &p, const
    QPixmap &pm)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblitterpaintengine.html#drawPixmap

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    pm : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  void QBlitterPaintEngine::drawPixmap(const QPointF &p, const QPixmap
    #      &pm)
    ritual = (
        'ritual_ZN19QBlitterPaintEngine10drawPixmapERK7QPointFRK7QPixmap')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QBlitterPaintEngine10drawPixmapERK7QPointFRK7QPix'
          'map')
    self.uglySide.call(
        ritual, self._valueOf(p, 'QPointF'), self._valueOf(pm),
    )

  @overload(QRectF, QPixmap, QRectF)
  def drawPixmap(self, r: QRectF, pm: QPixmap, sr: QRectF) -> None:
    """
    Calls Qt's 'void QBlitterPaintEngine::drawPixmap(const QRectF &r, const
    QPixmap &pm, const QRectF &sr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblitterpaintengine.html#drawPixmap

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    pm : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    sr : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QBlitterPaintEngine::drawPixmap(const QRectF &r, const QPixmap
    #      &pm, const QRectF &sr)
    ritual = (
        'ritual_ZN19QBlitterPaintEngine10drawPixmapERK6QRectFRK7QPixmapS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QBlitterPaintEngine10drawPixmapERK6QRectFRK7QPixm'
          'apS2_')
    self.uglySide.call(
        ritual, self._valueOf(r), self._valueOf(pm), self._valueOf(sr),
    )

  def clipEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QBlitterPaintEngine::clipEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblitterpaintengine.html#clipEnabledChanged
    """
    #  void QBlitterPaintEngine::clipEnabledChanged()
    ritual = 'ritual_ZN19QBlitterPaintEngine18clipEnabledChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QBlitterPaintEngine18clipEnabledChangedEv'
    self.uglySide.call(ritual)

  def penChanged(self) -> None:
    """
    Calls Qt's 'void QBlitterPaintEngine::penChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblitterpaintengine.html#penChanged
    """
    #  void QBlitterPaintEngine::penChanged()
    ritual = 'ritual_ZN19QBlitterPaintEngine10penChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QBlitterPaintEngine10penChangedEv'
    self.uglySide.call(ritual)

  def brushChanged(self) -> None:
    """
    Calls Qt's 'void QBlitterPaintEngine::brushChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblitterpaintengine.html#brushChanged
    """
    #  void QBlitterPaintEngine::brushChanged()
    ritual = 'ritual_ZN19QBlitterPaintEngine12brushChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QBlitterPaintEngine12brushChangedEv'
    self.uglySide.call(ritual)

  def opacityChanged(self) -> None:
    """
    Calls Qt's 'void QBlitterPaintEngine::opacityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblitterpaintengine.html#opacityChanged
    """
    #  void QBlitterPaintEngine::opacityChanged()
    ritual = 'ritual_ZN19QBlitterPaintEngine14opacityChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QBlitterPaintEngine14opacityChangedEv'
    self.uglySide.call(ritual)

  def compositionModeChanged(self) -> None:
    """
    Calls Qt's 'void QBlitterPaintEngine::compositionModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblitterpaintengine.html#compositionModeChanged
    """
    #  void QBlitterPaintEngine::compositionModeChanged()
    ritual = 'ritual_ZN19QBlitterPaintEngine22compositionModeChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QBlitterPaintEngine22compositionModeChangedEv'
    self.uglySide.call(ritual)

  def renderHintsChanged(self) -> None:
    """
    Calls Qt's 'void QBlitterPaintEngine::renderHintsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblitterpaintengine.html#renderHintsChanged
    """
    #  void QBlitterPaintEngine::renderHintsChanged()
    ritual = 'ritual_ZN19QBlitterPaintEngine18renderHintsChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QBlitterPaintEngine18renderHintsChangedEv'
    self.uglySide.call(ritual)

  def transformChanged(self) -> None:
    """
    Calls Qt's 'void QBlitterPaintEngine::transformChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblitterpaintengine.html#transformChanged
    """
    #  void QBlitterPaintEngine::transformChanged()
    ritual = 'ritual_ZN19QBlitterPaintEngine16transformChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QBlitterPaintEngine16transformChangedEv'
    self.uglySide.call(ritual)

  @overload(QPointF, int, QPaintEngine.PolygonDrawMode)
  @overload(NoneType, int, QPaintEngine.PolygonDrawMode)
  def drawPolygon(
      self,
      points: Optional[QPointF],
      pointCount: int,
      mode: QPaintEngine.PolygonDrawMode,
  ) -> None:
    """
    Calls Qt's 'void QBlitterPaintEngine::drawPolygon(const QPointF *points,
    int pointCount, PolygonDrawMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblitterpaintengine.html#drawPolygon

    Parameters
    ----------

    points : Optional[QPointF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pointCount : int
      Passed on as it is.

    mode : QPaintEngine.PolygonDrawMode
      Passed on as its number.
    """
    #  void QBlitterPaintEngine::drawPolygon(const QPointF *points, int
    #      pointCount, PolygonDrawMode mode)
    ritual = (
        'ritual_ZN19QBlitterPaintEngine11drawPolygonEPK7QPointFiN12QPaintEn'
        'gine15PolygonDrawModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QBlitterPaintEngine11drawPolygonEPK7QPointFiN12QP'
          'aintEngine15PolygonDrawModeE')
    self.uglySide.call(
        ritual, self._addressOf(points, 'QPointF'), pointCount, mode.value,
    )

  @overload(QPoint, int, QPaintEngine.PolygonDrawMode)
  def drawPolygon(
      self,
      points: Optional[QPoint],
      pointCount: int,
      mode: QPaintEngine.PolygonDrawMode,
  ) -> None:
    """
    Calls Qt's 'void QBlitterPaintEngine::drawPolygon(const QPoint *points,
    int pointCount, PolygonDrawMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblitterpaintengine.html#drawPolygon

    Parameters
    ----------

    points : Optional[QPoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pointCount : int
      Passed on as it is.

    mode : QPaintEngine.PolygonDrawMode
      Passed on as its number.
    """
    #  void QBlitterPaintEngine::drawPolygon(const QPoint *points, int
    #      pointCount, PolygonDrawMode mode)
    ritual = (
        'ritual_ZN19QBlitterPaintEngine11drawPolygonEPK6QPointiN12QPaintEng'
        'ine15PolygonDrawModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QBlitterPaintEngine11drawPolygonEPK6QPointiN12QPa'
          'intEngine15PolygonDrawModeE')
    self.uglySide.call(
        ritual, self._addressOf(points), pointCount, mode.value,
    )

  @overload(QPainterPath, QSpanData)
  @overload(QPainterPath, NoneType)
  def fillPath(
      self,
      path: QPainterPath,
      fillData: Optional[QSpanData],
  ) -> None:
    """
    Calls Qt's 'void QBlitterPaintEngine::fillPath(const QPainterPath &path,
    QSpanData *fillData)'.

    Qt's own words: https://doc.qt.io/qt-6/qblitterpaintengine.html#fillPath

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    fillData : Optional[QSpanData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBlitterPaintEngine::fillPath(const QPainterPath &path, QSpanData
    #      *fillData)
    ritual = (
        'ritual_ZN19QBlitterPaintEngine8fillPathERK12QPainterPathP9QSpanDat'
        'a')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QBlitterPaintEngine8fillPathERK12QPainterPathP9QS'
          'panData')
    self.uglySide.call(
        ritual, self._valueOf(path), self._addressOf(fillData),
    )

  @overload(QPointF, int, QPaintEngine.PolygonDrawMode)
  @overload(NoneType, int, QPaintEngine.PolygonDrawMode)
  def fillPolygon(
      self,
      points: Optional[QPointF],
      pointCount: int,
      mode: QPaintEngine.PolygonDrawMode,
  ) -> None:
    """
    Calls Qt's 'void QBlitterPaintEngine::fillPolygon(const QPointF *points,
    int pointCount, PolygonDrawMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblitterpaintengine.html#fillPolygon

    Parameters
    ----------

    points : Optional[QPointF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pointCount : int
      Passed on as it is.

    mode : QPaintEngine.PolygonDrawMode
      Passed on as its number.
    """
    #  void QBlitterPaintEngine::fillPolygon(const QPointF *points, int
    #      pointCount, PolygonDrawMode mode)
    ritual = (
        'ritual_ZN19QBlitterPaintEngine11fillPolygonEPK7QPointFiN12QPaintEn'
        'gine15PolygonDrawModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QBlitterPaintEngine11fillPolygonEPK7QPointFiN12QP'
          'aintEngine15PolygonDrawModeE')
    self.uglySide.call(
        ritual, self._addressOf(points, 'QPointF'), pointCount, mode.value,
    )

  @overload(QRectF)
  def drawEllipse(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QBlitterPaintEngine::drawEllipse(const QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblitterpaintengine.html#drawEllipse

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QBlitterPaintEngine::drawEllipse(const QRectF &rect)
    ritual = 'ritual_ZN19QBlitterPaintEngine11drawEllipseERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QBlitterPaintEngine11drawEllipseERK6QRectF'
    self.uglySide.call(ritual, self._valueOf(rect))

  @overload(QPointF, QImage)
  def drawImage(self, p: QPointF, img: QImage) -> None:
    """
    Calls Qt's 'void QBlitterPaintEngine::drawImage(const QPointF &p, const
    QImage &img)'.

    Qt's own words: https://doc.qt.io/qt-6/qblitterpaintengine.html#drawImage

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    img : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QBlitterPaintEngine::drawImage(const QPointF &p, const QImage
    #      &img)
    ritual = 'ritual_ZN19QBlitterPaintEngine9drawImageERK7QPointFRK6QImage'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QBlitterPaintEngine9drawImageERK7QPointFRK6QImage')
    self.uglySide.call(
        ritual, self._valueOf(p, 'QPointF'), self._valueOf(img),
    )

  @overload(QRectF, QImage, QRectF)
  @overload(QRectF, QImage, QRectF, Qt.ImageConversionFlags)
  def drawImage(
      self,
      r: QRectF,
      pm: QImage,
      sr: QRectF,
      flags: Qt.ImageConversionFlags = Qt.ImageConversionFlags.AutoColor,
  ) -> None:
    """
    Calls Qt's 'void QBlitterPaintEngine::drawImage(const QRectF &r, const
    QImage &pm, const QRectF &sr, Qt::ImageConversionFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qblitterpaintengine.html#drawImage

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    pm : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    sr : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    flags : Qt.ImageConversionFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ImageConversionFlags.AutoColor.
    """
    #  void QBlitterPaintEngine::drawImage(const QRectF &r, const QImage &pm,
    #      const QRectF &sr, Qt::ImageConversionFlags flags)
    ritual = (
        'ritual_ZN19QBlitterPaintEngine9drawImageERK6QRectFRK6QImageS2_6QFl'
        'agsIN2Qt19ImageConversionFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QBlitterPaintEngine9drawImageERK6QRectFRK6QImageS'
          '2_6QFlagsIN2Qt19ImageConversionFlagEE')
    self.uglySide.call(
        ritual,
        self._valueOf(r), self._valueOf(pm), self._valueOf(sr), flags.value,
    )

  @overload(QRectF, QPixmap, QPointF)
  def drawTiledPixmap(self, r: QRectF, pm: QPixmap, sr: QPointF) -> None:
    """
    Calls Qt's 'void QBlitterPaintEngine::drawTiledPixmap(const QRectF &r,
    const QPixmap &pm, const QPointF &sr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblitterpaintengine.html#drawTiledPixmap

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    pm : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    sr : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QBlitterPaintEngine::drawTiledPixmap(const QRectF &r, const
    #      QPixmap &pm, const QPointF &sr)
    ritual = (
        'ritual_ZN19QBlitterPaintEngine15drawTiledPixmapERK6QRectFRK7QPixma'
        'pRK7QPointF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QBlitterPaintEngine15drawTiledPixmapERK6QRectFRK7'
          'QPixmapRK7QPointF')
    self.uglySide.call(
        ritual,
        self._valueOf(r), self._valueOf(pm), self._valueOf(sr, 'QPointF'),
    )

  @overload(QPointF, QTextItem)
  def drawTextItem(self, p: QPointF, textItem: QTextItem) -> None:
    """
    Calls Qt's 'void QBlitterPaintEngine::drawTextItem(const QPointF &p,
    const QTextItem &textItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblitterpaintengine.html#drawTextItem

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    textItem : QTextItem
      Passed on as a value: Qt reads the C++ QTextItem, which stays Python's
      own.
    """
    #  void QBlitterPaintEngine::drawTextItem(const QPointF &p, const
    #      QTextItem &textItem)
    ritual = (
        'ritual_ZN19QBlitterPaintEngine12drawTextItemERK7QPointFRK9QTextIte'
        'm')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QBlitterPaintEngine12drawTextItemERK7QPointFRK9QT'
          'extItem')
    self.uglySide.call(
        ritual, self._valueOf(p, 'QPointF'), self._valueOf(textItem),
    )

  @overload(QPointF, int)
  @overload(NoneType, int)
  def drawPoints(self, points: Optional[QPointF], pointCount: int) -> None:
    """
    Calls Qt's 'void QBlitterPaintEngine::drawPoints(const QPointF *points,
    int pointCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblitterpaintengine.html#drawPoints

    Parameters
    ----------

    points : Optional[QPointF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pointCount : int
      Passed on as it is.
    """
    #  void QBlitterPaintEngine::drawPoints(const QPointF *points, int
    #      pointCount)
    ritual = 'ritual_ZN19QBlitterPaintEngine10drawPointsEPK7QPointFi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QBlitterPaintEngine10drawPointsEPK7QPointFi'
    self.uglySide.call(
        ritual, self._addressOf(points, 'QPointF'), pointCount,
    )

  @overload(QPoint, int)
  def drawPoints(self, points: Optional[QPoint], pointCount: int) -> None:
    """
    Calls Qt's 'void QBlitterPaintEngine::drawPoints(const QPoint *points,
    int pointCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblitterpaintengine.html#drawPoints

    Parameters
    ----------

    points : Optional[QPoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pointCount : int
      Passed on as it is.
    """
    #  void QBlitterPaintEngine::drawPoints(const QPoint *points, int
    #      pointCount)
    ritual = 'ritual_ZN19QBlitterPaintEngine10drawPointsEPK6QPointi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QBlitterPaintEngine10drawPointsEPK6QPointi'
    self.uglySide.call(ritual, self._addressOf(points), pointCount)

  @overload(QStaticTextItem)
  @overload(NoneType)
  def drawStaticTextItem(self, a0: Optional[QStaticTextItem]) -> None:
    """
    Calls Qt's 'void QBlitterPaintEngine::drawStaticTextItem(QStaticTextItem
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblitterpaintengine.html#drawStaticTextItem

    Parameters
    ----------

    a0 : Optional[QStaticTextItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBlitterPaintEngine::drawStaticTextItem(QStaticTextItem *a0)
    ritual = (
        'ritual_ZN19QBlitterPaintEngine18drawStaticTextItemEP15QStaticTextI'
        'tem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QBlitterPaintEngine18drawStaticTextItemEP15QStati'
          'cTextItem')
    self.uglySide.call(ritual, self._addressOf(a0))
