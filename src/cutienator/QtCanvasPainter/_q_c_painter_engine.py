"""
QCPainterEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcpainterengine_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QCPainterEngine to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QCanvasPainter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QRectF
  from ..QtGui import QColor, QMatrix4x4, QPainterPath, QTransform
  from . import QCDebugCounters, QCPaint, QCPoint, QCanvasBrush
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCPaint = WAIT['QCPaint']
  QCPoint = WAIT['QCPoint']
  QCanvasBrush = WAIT['QCanvasBrush']
  QColor = WAIT['QColor']
  QMatrix4x4 = WAIT['QMatrix4x4']
  QPainterPath = WAIT['QPainterPath']
  QRectF = WAIT['QRectF']
  QTransform = WAIT['QTransform']


class QCPainterEngine(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCPainterEngine: a plain Python object standing in
  front of one C++ QCPainterEngine.

  C++ hands a QCPainterEngine around as a copy, so every C++ QCPainterEngine
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCPainterEngine that has a ritual and that Python
  can call so far, 73 names in all: 'setCustomMatrix', 'endPaint', 'save',
  'restore', 'setStrokeColor', 'setStrokePaint', 'setFillColor',
  'setFillPaint', 'setLineWidth', 'setLineCap', 'setLineJoin',
  'setGlobalAlpha', 'setGlobalBrightness', 'setGlobalContrast',
  'setGlobalSaturation', 'setFillRule', 'fillRule', 'setCustomStrokeBrush',
  'setCustomFillBrush', 'currentTransform', 'transform', 'setTransform',
  'resetTransform', 'translate', 'scale', 'rotate', 'skew',
  'setBrushTransform', 'createImagePattern', 'beginPath', 'closePath',
  'moveTo', 'lineTo', 'bezierTo', 'quadTo', 'arcTo', 'addArc', 'addRect',
  'addRoundRect', 'addEllipse', 'addCircle', 'addPath', 'setPathWinding',
  'setGlobalCompositeOperation', 'setTextWrapMode', 'setTextLineHeight',
  'setTextAntialias', 'setTextAlignment', 'setTextBaseline',
  'setTextDirection', 'textBoundingBox', 'resetDebugCounters',
  'debugCounters', 'setAntialias', 'setMiterLimit', 'cleanup',
  'releaseUnusedResources', 'handleSetPathWinding', 'handleClosePath',
  'handleMoveTo', 'handleAddPoint', 'tesselateBezier', 'enforceWinding',
  'calculateJoins', 'addButtCapStart', 'addRoundCapStart', 'addButtCapEnd',
  'addRoundCapEnd', 'addVert', 'ensureVertices', 'effectiveTextAlign',
  'getFillPaint', 'updateStateFontVars'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QCPainterEngine::appendCommand(QCCommand command)': names the
    enum 'QCCommand', whose class cannot be named here.
  - Qt's 'void QCPainterEngine::appendCommands(const QCCommand *commands, int
    cCount)': names 'QCCommand', which has no cute class yet.
  - Qt's 'void QCPainterEngine::appendCommandsData(const float *commandsData,
    int dCount, bool ignoreTransform)': names 'float', which has no cute
    class yet.
  - Qt's 'QCPainterEngine::~QCPainterEngine()': the destructor: Python
    removes its C++ QCPainterEngine by it, and has no other use for it.

  What has no ritual
  ------------------

  39 of the 118 functions Qt declares: 25 leans on 'QCPainterRhiRenderer; 12
  Qt's library has no name for it, and its code in Qt's source does not
  compile apart from its file; 2 leans on 'QCPainterEngine.

  What to expect
  --------------

  - The C++ QCPainterEngine is created at the first use, not by
    'QCPainterEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCPainterEngine back gives a copy the ritual made for
    Python, in a new cute QCPainterEngine.
  - Each name of Qt's QCPainterEngine that has no cute function yet,
    'addBevelJoin', 'addRoundJoin', 'appendCommand', 'appendCommands',
    'appendCommandsData', 'appendPainterPath', 'beginPaint',
    'commandsToPaths', 'createImage', 'deleteImage', 'drawImageId',
    'drawImageIdAt', 'expandFill', 'expandStroke', 'fill',
    'fillCachedPathUpdateRequired', 'fillForClear', 'fillPlainRect',
    'fillShapedText', 'fillText', 'getStrokePaint', 'initialize',
    'preparePainterPath', 'removePathGroup', 'renderFilledText', 'reset',
    'resetClipRect', 'setAntialiasingEnabled', 'setClipRect',
    'setDevicePixelRatio', 'setHighQualityStrokingEnabled', 'setStencilClip',
    'setWindingEnforceEnabled', 'stroke', 'strokeCachedPathUpdateRequired',
    'syncDebugCounters', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QCPainterEngine, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class QCPointFlags(CuteNum):
    """
    The enum 'QCPainterEngine::QCPointFlags' of Qt, with the 4 names Qt gives
    in it.
    """

    PointCorner = Kee[int](1)
    PointLeft = Kee[int](2)
    PointBevel = Kee[int](4)
    PointInnerBevel = Kee[int](8)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCPainterEngine'

  #  Qt's '~QCPainterEngine()'. Naming it makes this a value class: Python
  #  owns every C++ QCPainterEngine behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QCPainterEngineD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def fillRule(self) -> QCanvasPainter.FillRule:
    """
    Calls Qt's 'QCanvasPainter::FillRule QCPainterEngine::fillRule() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#fillRule

    Returns
    -------

    QCanvasPainter.FillRule
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QCanvasPainter.FillRule(number)' gives.
    """
    #  QCanvasPainter::FillRule QCPainterEngine::fillRule() const
    return QCanvasPainter.FillRule(self.uglySide.call(
        'ritual_ZNK15QCPainterEngine8fillRuleEv',
    ))

  def currentTransform(self) -> QTransform:
    """
    Calls Qt's 'QTransform QCPainterEngine::currentTransform() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#currentTransform

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QCPainterEngine::currentTransform() const
    address = self.uglySide.call(
        'ritual_ZNK15QCPainterEngine16currentTransformEv',
    )
    from ..QtGui import QTransform
    return QTransform._cuteOwning(address)

  def debugCounters(self) -> QCDebugCounters:
    """
    Calls Qt's 'QCDebugCounters QCPainterEngine::debugCounters() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#debugCounters

    Returns
    -------

    QCDebugCounters
      A new cute QCDebugCounters around the copy Qt gave back. Python owns
      it.
    """
    #  QCDebugCounters QCPainterEngine::debugCounters() const
    address = self.uglySide.call(
        'ritual_ZNK15QCPainterEngine13debugCountersEv',
    )
    from . import QCDebugCounters
    return QCDebugCounters._cuteOwning(address)

  @overload(str)
  def effectiveTextAlign(self, text: str) -> QCanvasPainter.TextAlign:
    """
    Calls Qt's 'QCanvasPainter::TextAlign
    QCPainterEngine::effectiveTextAlign(QStringView text) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#effectiveTextAlign

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QCanvasPainter.TextAlign
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QCanvasPainter.TextAlign(number)' gives.
    """
    #  QCanvasPainter::TextAlign
    #      QCPainterEngine::effectiveTextAlign(QStringView text) const
    return QCanvasPainter.TextAlign(self.uglySide.call(
        'ritual_ZNK15QCPainterEngine18effectiveTextAlignE11QStringView',
        text,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMatrix4x4)
  def setCustomMatrix(self, matrix: QMatrix4x4) -> None:
    """
    Calls Qt's 'void QCPainterEngine::setCustomMatrix(const QMatrix4x4
    &matrix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#setCustomMatrix

    Parameters
    ----------

    matrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  void QCPainterEngine::setCustomMatrix(const QMatrix4x4 &matrix)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine15setCustomMatrixERK10QMatrix4x4',
        self._valueOf(matrix),
    )

  @overload(QColor)
  def setStrokeColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QCPainterEngine::setStrokeColor(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#setStrokeColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QCPainterEngine::setStrokeColor(QColor color)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine14setStrokeColorE6QColor',
        self._valueOf(color),
    )

  @overload(QCPaint)
  def setStrokePaint(self, paint: QCPaint) -> None:
    """
    Calls Qt's 'void QCPainterEngine::setStrokePaint(const QCPaint &paint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#setStrokePaint

    Parameters
    ----------

    paint : QCPaint
      Passed on as a value: Qt reads the C++ QCPaint, which stays Python's
      own.
    """
    #  void QCPainterEngine::setStrokePaint(const QCPaint &paint)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine14setStrokePaintERK7QCPaint',
        self._valueOf(paint),
    )

  @overload(QColor)
  def setFillColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QCPainterEngine::setFillColor(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#setFillColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QCPainterEngine::setFillColor(QColor color)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine12setFillColorE6QColor',
        self._valueOf(color),
    )

  @overload(QCPaint)
  def setFillPaint(self, paint: QCPaint) -> None:
    """
    Calls Qt's 'void QCPainterEngine::setFillPaint(const QCPaint &paint)'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#setFillPaint

    Parameters
    ----------

    paint : QCPaint
      Passed on as a value: Qt reads the C++ QCPaint, which stays Python's
      own.
    """
    #  void QCPainterEngine::setFillPaint(const QCPaint &paint)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine12setFillPaintERK7QCPaint',
        self._valueOf(paint),
    )

  @overload(float)
  def setLineWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QCPainterEngine::setLineWidth(float width)'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#setLineWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QCPainterEngine::setLineWidth(float width)
    self.uglySide.call('ritual_ZN15QCPainterEngine12setLineWidthEf', width)

  @overload(QCanvasPainter.LineCap)
  def setLineCap(self, lineCap: QCanvasPainter.LineCap) -> None:
    """
    Calls Qt's 'void QCPainterEngine::setLineCap(QCanvasPainter::LineCap
    lineCap)'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#setLineCap

    Parameters
    ----------

    lineCap : QCanvasPainter.LineCap
      Passed on as its number.
    """
    #  void QCPainterEngine::setLineCap(QCanvasPainter::LineCap lineCap)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine10setLineCapEN14QCanvasPainter7LineCapE',
        lineCap.value,
    )

  @overload(QCanvasPainter.LineJoin)
  def setLineJoin(self, lineJoin: QCanvasPainter.LineJoin) -> None:
    """
    Calls Qt's 'void QCPainterEngine::setLineJoin(QCanvasPainter::LineJoin
    lineJoin)'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#setLineJoin

    Parameters
    ----------

    lineJoin : QCanvasPainter.LineJoin
      Passed on as its number.
    """
    #  void QCPainterEngine::setLineJoin(QCanvasPainter::LineJoin lineJoin)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine11setLineJoinEN14QCanvasPainter8LineJoin'
        'E',
        lineJoin.value,
    )

  @overload(float)
  def setGlobalAlpha(self, alpha: float) -> None:
    """
    Calls Qt's 'void QCPainterEngine::setGlobalAlpha(float alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#setGlobalAlpha

    Parameters
    ----------

    alpha : float
      Passed on as it is.
    """
    #  void QCPainterEngine::setGlobalAlpha(float alpha)
    self.uglySide.call('ritual_ZN15QCPainterEngine14setGlobalAlphaEf', alpha)

  @overload(float)
  def setGlobalBrightness(self, value: float) -> None:
    """
    Calls Qt's 'void QCPainterEngine::setGlobalBrightness(float value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#setGlobalBrightness

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QCPainterEngine::setGlobalBrightness(float value)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine19setGlobalBrightnessEf', value,
    )

  @overload(float)
  def setGlobalContrast(self, value: float) -> None:
    """
    Calls Qt's 'void QCPainterEngine::setGlobalContrast(float value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#setGlobalContrast

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QCPainterEngine::setGlobalContrast(float value)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine17setGlobalContrastEf', value,
    )

  @overload(float)
  def setGlobalSaturation(self, value: float) -> None:
    """
    Calls Qt's 'void QCPainterEngine::setGlobalSaturation(float value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#setGlobalSaturation

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QCPainterEngine::setGlobalSaturation(float value)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine19setGlobalSaturationEf', value,
    )

  @overload(QCanvasPainter.FillRule)
  def setFillRule(self, fillRule: QCanvasPainter.FillRule) -> None:
    """
    Calls Qt's 'void QCPainterEngine::setFillRule(QCanvasPainter::FillRule
    fillRule)'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#setFillRule

    Parameters
    ----------

    fillRule : QCanvasPainter.FillRule
      Passed on as its number.
    """
    #  void QCPainterEngine::setFillRule(QCanvasPainter::FillRule fillRule)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine11setFillRuleEN14QCanvasPainter8FillRule'
        'E',
        fillRule.value,
    )

  @overload(QCanvasBrush)
  def setCustomStrokeBrush(self, brush: QCanvasBrush) -> None:
    """
    Calls Qt's 'void QCPainterEngine::setCustomStrokeBrush(const QCanvasBrush
    &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#setCustomStrokeBrush

    Parameters
    ----------

    brush : QCanvasBrush
      Passed on as a value: Qt reads the C++ QCanvasBrush, which stays
      Python's own.
    """
    #  void QCPainterEngine::setCustomStrokeBrush(const QCanvasBrush &brush)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine20setCustomStrokeBrushERK12QCanvasBrush',
        self._valueOf(brush),
    )

  @overload(QCanvasBrush)
  def setCustomFillBrush(self, brush: QCanvasBrush) -> None:
    """
    Calls Qt's 'void QCPainterEngine::setCustomFillBrush(const QCanvasBrush
    &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#setCustomFillBrush

    Parameters
    ----------

    brush : QCanvasBrush
      Passed on as a value: Qt reads the C++ QCanvasBrush, which stays
      Python's own.
    """
    #  void QCPainterEngine::setCustomFillBrush(const QCanvasBrush &brush)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine18setCustomFillBrushERK12QCanvasBrush',
        self._valueOf(brush),
    )

  @overload(QTransform)
  def setTransform(self, transform: QTransform) -> None:
    """
    Calls Qt's 'void QCPainterEngine::setTransform(const QTransform
    &transform)'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#setTransform

    Parameters
    ----------

    transform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  void QCPainterEngine::setTransform(const QTransform &transform)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine12setTransformERK10QTransform',
        self._valueOf(transform),
    )

  @overload(QTransform)
  def setBrushTransform(self, transform: QTransform) -> None:
    """
    Calls Qt's 'void QCPainterEngine::setBrushTransform(const QTransform
    &transform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#setBrushTransform

    Parameters
    ----------

    transform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  void QCPainterEngine::setBrushTransform(const QTransform &transform)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine17setBrushTransformERK10QTransform',
        self._valueOf(transform),
    )

  @overload(QCanvasPainter.PathWinding)
  def setPathWinding(self, winding: QCanvasPainter.PathWinding) -> None:
    """
    Calls Qt's 'void
    QCPainterEngine::setPathWinding(QCanvasPainter::PathWinding winding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#setPathWinding

    Parameters
    ----------

    winding : QCanvasPainter.PathWinding
      Passed on as its number.
    """
    #  void QCPainterEngine::setPathWinding(QCanvasPainter::PathWinding
    #      winding)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine14setPathWindingEN14QCanvasPainter11Path'
        'WindingE',
        winding.value,
    )

  @overload(QCanvasPainter.CompositeOperation)
  def setGlobalCompositeOperation(
      self,
      op: QCanvasPainter.CompositeOperation,
  ) -> None:
    """
    Calls Qt's 'void
    QCPainterEngine::setGlobalCompositeOperation(QCanvasPainter::
    CompositeOperation op)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#setGlobalCompositeOperation

    Parameters
    ----------

    op : QCanvasPainter.CompositeOperation
      Passed on as its number.
    """
    #  void QCPainterEngine::setGlobalCompositeOperation(QCanvasPainter::
    #      CompositeOperation op)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine27setGlobalCompositeOperationEN14QCanvas'
        'Painter18CompositeOperationE',
        op.value,
    )

  @overload(QCanvasPainter.WrapMode)
  def setTextWrapMode(self, wrapMode: QCanvasPainter.WrapMode) -> None:
    """
    Calls Qt's 'void
    QCPainterEngine::setTextWrapMode(QCanvasPainter::WrapMode wrapMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#setTextWrapMode

    Parameters
    ----------

    wrapMode : QCanvasPainter.WrapMode
      Passed on as its number.
    """
    #  void QCPainterEngine::setTextWrapMode(QCanvasPainter::WrapMode
    #      wrapMode)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine15setTextWrapModeEN14QCanvasPainter8Wrap'
        'ModeE',
        wrapMode.value,
    )

  @overload(float)
  def setTextLineHeight(self, height: float) -> None:
    """
    Calls Qt's 'void QCPainterEngine::setTextLineHeight(float height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#setTextLineHeight

    Parameters
    ----------

    height : float
      Passed on as it is.
    """
    #  void QCPainterEngine::setTextLineHeight(float height)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine17setTextLineHeightEf', height,
    )

  @overload(float)
  def setTextAntialias(self, antialias: float) -> None:
    """
    Calls Qt's 'void QCPainterEngine::setTextAntialias(float antialias)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#setTextAntialias

    Parameters
    ----------

    antialias : float
      Passed on as it is.
    """
    #  void QCPainterEngine::setTextAntialias(float antialias)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine16setTextAntialiasEf', antialias,
    )

  @overload(QCanvasPainter.TextAlign)
  def setTextAlignment(self, align: QCanvasPainter.TextAlign) -> None:
    """
    Calls Qt's 'void
    QCPainterEngine::setTextAlignment(QCanvasPainter::TextAlign align)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#setTextAlignment

    Parameters
    ----------

    align : QCanvasPainter.TextAlign
      Passed on as its number.
    """
    #  void QCPainterEngine::setTextAlignment(QCanvasPainter::TextAlign
    #      align)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine16setTextAlignmentEN14QCanvasPainter9Tex'
        'tAlignE',
        align.value,
    )

  @overload(QCanvasPainter.TextBaseline)
  def setTextBaseline(self, baseline: QCanvasPainter.TextBaseline) -> None:
    """
    Calls Qt's 'void
    QCPainterEngine::setTextBaseline(QCanvasPainter::TextBaseline baseline)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#setTextBaseline

    Parameters
    ----------

    baseline : QCanvasPainter.TextBaseline
      Passed on as its number.
    """
    #  void QCPainterEngine::setTextBaseline(QCanvasPainter::TextBaseline
    #      baseline)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine15setTextBaselineEN14QCanvasPainter12Tex'
        'tBaselineE',
        baseline.value,
    )

  @overload(QCanvasPainter.TextDirection)
  def setTextDirection(
      self,
      direction: QCanvasPainter.TextDirection,
  ) -> None:
    """
    Calls Qt's 'void
    QCPainterEngine::setTextDirection(QCanvasPainter::TextDirection
    direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#setTextDirection

    Parameters
    ----------

    direction : QCanvasPainter.TextDirection
      Passed on as its number.
    """
    #  void QCPainterEngine::setTextDirection(QCanvasPainter::TextDirection
    #      direction)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine16setTextDirectionEN14QCanvasPainter13Te'
        'xtDirectionE',
        direction.value,
    )

  @overload(float)
  def setAntialias(self, antialias: float) -> None:
    """
    Calls Qt's 'void QCPainterEngine::setAntialias(float antialias)'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#setAntialias

    Parameters
    ----------

    antialias : float
      Passed on as it is.
    """
    #  void QCPainterEngine::setAntialias(float antialias)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine12setAntialiasEf', antialias,
    )

  @overload(float)
  def setMiterLimit(self, limit: float) -> None:
    """
    Calls Qt's 'void QCPainterEngine::setMiterLimit(float limit)'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#setMiterLimit

    Parameters
    ----------

    limit : float
      Passed on as it is.
    """
    #  void QCPainterEngine::setMiterLimit(float limit)
    self.uglySide.call('ritual_ZN15QCPainterEngine13setMiterLimitEf', limit)

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
    Notes what was given, for Qt's 'QCPainterEngine::QCPainterEngine()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#QCPainterEngine
    """
    #  QCPainterEngine::QCPainterEngine()
    self._noteCreation(QCPainterEngine, lambda: Rituals.call(
        'ritual_ZN15QCPainterEngineC1Ev',
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

  def endPaint(self) -> None:
    """
    Calls Qt's 'void QCPainterEngine::endPaint()'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#endPaint
    """
    #  void QCPainterEngine::endPaint()
    self.uglySide.call('ritual_ZN15QCPainterEngine8endPaintEv')

  def save(self) -> None:
    """
    Calls Qt's 'void QCPainterEngine::save()'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#save
    """
    #  void QCPainterEngine::save()
    self.uglySide.call('ritual_ZN15QCPainterEngine4saveEv')

  def restore(self) -> None:
    """
    Calls Qt's 'void QCPainterEngine::restore()'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#restore
    """
    #  void QCPainterEngine::restore()
    self.uglySide.call('ritual_ZN15QCPainterEngine7restoreEv')

  @overload(QTransform)
  def transform(self, transform: QTransform) -> None:
    """
    Calls Qt's 'void QCPainterEngine::transform(const QTransform
    &transform)'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#transform

    Parameters
    ----------

    transform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  void QCPainterEngine::transform(const QTransform &transform)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine9transformERK10QTransform',
        self._valueOf(transform),
    )

  def resetTransform(self) -> None:
    """
    Calls Qt's 'void QCPainterEngine::resetTransform()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#resetTransform
    """
    #  void QCPainterEngine::resetTransform()
    self.uglySide.call('ritual_ZN15QCPainterEngine14resetTransformEv')

  @overload(float, float)
  def translate(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QCPainterEngine::translate(float x, float y)'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#translate

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QCPainterEngine::translate(float x, float y)
    self.uglySide.call('ritual_ZN15QCPainterEngine9translateEff', x, y)

  @overload(float, float)
  def scale(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QCPainterEngine::scale(float x, float y)'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#scale

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QCPainterEngine::scale(float x, float y)
    self.uglySide.call('ritual_ZN15QCPainterEngine5scaleEff', x, y)

  @overload(float)
  def rotate(self, angle: float) -> None:
    """
    Calls Qt's 'void QCPainterEngine::rotate(float angle)'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#rotate

    Parameters
    ----------

    angle : float
      Passed on as it is.
    """
    #  void QCPainterEngine::rotate(float angle)
    self.uglySide.call('ritual_ZN15QCPainterEngine6rotateEf', angle)

  @overload(float)
  @overload(float, float)
  def skew(self, angleX: float, angleY: float = 0.0) -> None:
    """
    Calls Qt's 'void QCPainterEngine::skew(float angleX, float angleY)'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#skew

    Parameters
    ----------

    angleX : float
      Passed on as it is.

    angleY : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  void QCPainterEngine::skew(float angleX, float angleY)
    self.uglySide.call('ritual_ZN15QCPainterEngine4skewEff', angleX, angleY)

  @overload(float, float, float, float, int, float, QColor)
  def createImagePattern(
      self,
      x: float,
      y: float,
      width: float,
      height: float,
      imageId: int,
      angle: float,
      tintColor: QColor,
  ) -> QCPaint:
    """
    Calls Qt's 'QCPaint QCPainterEngine::createImagePattern(float x, float y,
    float width, float height, int imageId, float angle, QColor tintColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#createImagePattern

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    width : float
      Passed on as it is.

    height : float
      Passed on as it is.

    imageId : int
      Passed on as it is.

    angle : float
      Passed on as it is.

    tintColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    Returns
    -------

    QCPaint
      A new cute QCPaint around the copy Qt gave back. Python owns it.
    """
    #  QCPaint QCPainterEngine::createImagePattern(float x, float y, float
    #      width, float height, int imageId, float angle, QColor tintColor)
    address = self.uglySide.call(
        'ritual_ZN15QCPainterEngine18createImagePatternEffffif6QColor',
        x, y, width, height, imageId, angle, self._valueOf(tintColor),
    )
    from . import QCPaint
    return QCPaint._cuteOwning(address)

  def beginPath(self) -> None:
    """
    Calls Qt's 'void QCPainterEngine::beginPath()'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#beginPath
    """
    #  void QCPainterEngine::beginPath()
    self.uglySide.call('ritual_ZN15QCPainterEngine9beginPathEv')

  def closePath(self) -> None:
    """
    Calls Qt's 'void QCPainterEngine::closePath()'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#closePath
    """
    #  void QCPainterEngine::closePath()
    self.uglySide.call('ritual_ZN15QCPainterEngine9closePathEv')

  @overload(float, float)
  def moveTo(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QCPainterEngine::moveTo(float x, float y)'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#moveTo

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QCPainterEngine::moveTo(float x, float y)
    self.uglySide.call('ritual_ZN15QCPainterEngine6moveToEff', x, y)

  @overload(float, float)
  def lineTo(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QCPainterEngine::lineTo(float x, float y)'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#lineTo

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QCPainterEngine::lineTo(float x, float y)
    self.uglySide.call('ritual_ZN15QCPainterEngine6lineToEff', x, y)

  @overload(float, float, float, float, float, float)
  def bezierTo(
      self,
      cp1X: float,
      cp1Y: float,
      cp2X: float,
      cp2Y: float,
      x: float,
      y: float,
  ) -> None:
    """
    Calls Qt's 'void QCPainterEngine::bezierTo(float cp1X, float cp1Y, float
    cp2X, float cp2Y, float x, float y)'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#bezierTo

    Parameters
    ----------

    cp1X : float
      Passed on as it is.

    cp1Y : float
      Passed on as it is.

    cp2X : float
      Passed on as it is.

    cp2Y : float
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QCPainterEngine::bezierTo(float cp1X, float cp1Y, float cp2X,
    #      float cp2Y, float x, float y)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine8bezierToEffffff',
        cp1X, cp1Y, cp2X, cp2Y, x, y,
    )

  @overload(float, float, float, float)
  def quadTo(self, cpX: float, cpY: float, x: float, y: float) -> None:
    """
    Calls Qt's 'void QCPainterEngine::quadTo(float cpX, float cpY, float x,
    float y)'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#quadTo

    Parameters
    ----------

    cpX : float
      Passed on as it is.

    cpY : float
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QCPainterEngine::quadTo(float cpX, float cpY, float x, float y)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine6quadToEffff', cpX, cpY, x, y,
    )

  @overload(float, float, float, float, float)
  def arcTo(
      self,
      x1: float,
      y1: float,
      x2: float,
      y2: float,
      radius: float,
  ) -> None:
    """
    Calls Qt's 'void QCPainterEngine::arcTo(float x1, float y1, float x2,
    float y2, float radius)'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#arcTo

    Parameters
    ----------

    x1 : float
      Passed on as it is.

    y1 : float
      Passed on as it is.

    x2 : float
      Passed on as it is.

    y2 : float
      Passed on as it is.

    radius : float
      Passed on as it is.
    """
    #  void QCPainterEngine::arcTo(float x1, float y1, float x2, float y2,
    #      float radius)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine5arcToEfffff', x1, y1, x2, y2, radius,
    )

  @overload(
      float, float, float, float, float, QCanvasPainter.PathWinding, bool,
  )
  def addArc(
      self,
      x: float,
      y: float,
      radius: float,
      a0: float,
      a1: float,
      direction: QCanvasPainter.PathWinding,
      isConnected: bool,
  ) -> None:
    """
    Calls Qt's 'void QCPainterEngine::addArc(float x, float y, float radius,
    float a0, float a1, QCanvasPainter::PathWinding direction, bool
    isConnected)'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#addArc

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    radius : float
      Passed on as it is.

    a0 : float
      Passed on as it is.

    a1 : float
      Passed on as it is.

    direction : QCanvasPainter.PathWinding
      Passed on as its number.

    isConnected : bool
      Passed on as it is.
    """
    #  void QCPainterEngine::addArc(float x, float y, float radius, float a0,
    #      float a1, QCanvasPainter::PathWinding direction, bool isConnected)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine6addArcEfffffN14QCanvasPainter11PathWind'
        'ingEb',
        x, y, radius, a0, a1, direction.value, isConnected,
    )

  @overload(float, float, float, float)
  def addRect(self, x: float, y: float, width: float, height: float) -> None:
    """
    Calls Qt's 'void QCPainterEngine::addRect(float x, float y, float width,
    float height)'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#addRect

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    width : float
      Passed on as it is.

    height : float
      Passed on as it is.
    """
    #  void QCPainterEngine::addRect(float x, float y, float width, float
    #      height)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine7addRectEffff', x, y, width, height,
    )

  @overload(float, float, float, float, float)
  def addRoundRect(
      self,
      x: float,
      y: float,
      width: float,
      height: float,
      radius: float,
  ) -> None:
    """
    Calls Qt's 'void QCPainterEngine::addRoundRect(float x, float y, float
    width, float height, float radius)'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#addRoundRect

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    width : float
      Passed on as it is.

    height : float
      Passed on as it is.

    radius : float
      Passed on as it is.
    """
    #  void QCPainterEngine::addRoundRect(float x, float y, float width,
    #      float height, float radius)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine12addRoundRectEfffff',
        x, y, width, height, radius,
    )

  @overload(float, float, float, float, float, float, float, float)
  def addRoundRect(
      self,
      x: float,
      y: float,
      width: float,
      height: float,
      radiusTopLeft: float,
      radiusTopRight: float,
      radiusBottomRight: float,
      radiusBottomLeft: float,
  ) -> None:
    """
    Calls Qt's 'void QCPainterEngine::addRoundRect(float x, float y, float
    width, float height, float radiusTopLeft, float radiusTopRight, float
    radiusBottomRight, float radiusBottomLeft)'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#addRoundRect

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    width : float
      Passed on as it is.

    height : float
      Passed on as it is.

    radiusTopLeft : float
      Passed on as it is.

    radiusTopRight : float
      Passed on as it is.

    radiusBottomRight : float
      Passed on as it is.

    radiusBottomLeft : float
      Passed on as it is.
    """
    #  void QCPainterEngine::addRoundRect(float x, float y, float width,
    #      float height, float radiusTopLeft, float radiusTopRight, float
    #      radiusBottomRight, float radiusBottomLeft)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine12addRoundRectEffffffff',
        x, y, width, height, radiusTopLeft, radiusTopRight,
        radiusBottomRight, radiusBottomLeft,
    )

  @overload(float, float, float, float)
  def addEllipse(
      self,
      x: float,
      y: float,
      radiusX: float,
      radiusY: float,
  ) -> None:
    """
    Calls Qt's 'void QCPainterEngine::addEllipse(float x, float y, float
    radiusX, float radiusY)'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#addEllipse

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    radiusX : float
      Passed on as it is.

    radiusY : float
      Passed on as it is.
    """
    #  void QCPainterEngine::addEllipse(float x, float y, float radiusX,
    #      float radiusY)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine10addEllipseEffff',
        x, y, radiusX, radiusY,
    )

  @overload(float, float, float)
  def addCircle(self, x: float, y: float, radius: float) -> None:
    """
    Calls Qt's 'void QCPainterEngine::addCircle(float x, float y, float
    radius)'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#addCircle

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    radius : float
      Passed on as it is.
    """
    #  void QCPainterEngine::addCircle(float x, float y, float radius)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine9addCircleEfff', x, y, radius,
    )

  @overload(QPainterPath)
  def addPath(self, path: QPainterPath) -> None:
    """
    Calls Qt's 'void QCPainterEngine::addPath(const QPainterPath &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#addPath

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.
    """
    #  void QCPainterEngine::addPath(const QPainterPath &path)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine7addPathERK12QPainterPath',
        self._valueOf(path),
    )

  @overload(str, QRectF)
  def textBoundingBox(self, text: str, rect: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF QCPainterEngine::textBoundingBox(const QString &text,
    const QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#textBoundingBox

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QCPainterEngine::textBoundingBox(const QString &text, const
    #      QRectF &rect)
    address = self.uglySide.call(
        'ritual_ZN15QCPainterEngine15textBoundingBoxERK7QStringRK6QRectF',
        text, self._valueOf(rect),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def resetDebugCounters(self) -> None:
    """
    Calls Qt's 'void QCPainterEngine::resetDebugCounters()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#resetDebugCounters
    """
    #  void QCPainterEngine::resetDebugCounters()
    self.uglySide.call('ritual_ZN15QCPainterEngine18resetDebugCountersEv')

  def cleanup(self) -> None:
    """
    Calls Qt's 'void QCPainterEngine::cleanup()'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#cleanup
    """
    #  void QCPainterEngine::cleanup()
    self.uglySide.call('ritual_ZN15QCPainterEngine7cleanupEv')

  def releaseUnusedResources(self) -> None:
    """
    Calls Qt's 'void QCPainterEngine::releaseUnusedResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#releaseUnusedResources
    """
    #  void QCPainterEngine::releaseUnusedResources()
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine22releaseUnusedResourcesEv',
    )

  @overload(QCanvasPainter.PathWinding)
  def handleSetPathWinding(
      self,
      winding: QCanvasPainter.PathWinding,
  ) -> None:
    """
    Calls Qt's 'void
    QCPainterEngine::handleSetPathWinding(QCanvasPainter::PathWinding
    winding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#handleSetPathWinding

    Parameters
    ----------

    winding : QCanvasPainter.PathWinding
      Passed on as its number.
    """
    #  void QCPainterEngine::handleSetPathWinding(QCanvasPainter::PathWinding
    #      winding)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine20handleSetPathWindingEN14QCanvasPainter'
        '11PathWindingE',
        winding.value,
    )

  def handleClosePath(self) -> None:
    """
    Calls Qt's 'void QCPainterEngine::handleClosePath()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#handleClosePath
    """
    #  void QCPainterEngine::handleClosePath()
    self.uglySide.call('ritual_ZN15QCPainterEngine15handleClosePathEv')

  def handleMoveTo(self) -> None:
    """
    Calls Qt's 'void QCPainterEngine::handleMoveTo()'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#handleMoveTo
    """
    #  void QCPainterEngine::handleMoveTo()
    self.uglySide.call('ritual_ZN15QCPainterEngine12handleMoveToEv')

  @overload(float, float, QCPointFlags)
  def handleAddPoint(self, x: float, y: float, flags: QCPointFlags) -> None:
    """
    Calls Qt's 'void QCPainterEngine::handleAddPoint(float x, float y,
    QCPointFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#handleAddPoint

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    flags : QCPointFlags
      Passed on as its number.
    """
    #  void QCPainterEngine::handleAddPoint(float x, float y, QCPointFlags
    #      flags)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine14handleAddPointEffNS_12QCPointFlagsE',
        x, y, flags.value,
    )

  @overload(
      float, float, float, float, float, float, float, float, int,
      QCPointFlags,
  )
  def tesselateBezier(
      self,
      x1: float,
      y1: float,
      x2: float,
      y2: float,
      x3: float,
      y3: float,
      x4: float,
      y4: float,
      level: int,
      flags: QCPointFlags,
  ) -> None:
    """
    Calls Qt's 'void QCPainterEngine::tesselateBezier(float x1, float y1,
    float x2, float y2, float x3, float y3, float x4, float y4, int level,
    QCPointFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#tesselateBezier

    Parameters
    ----------

    x1 : float
      Passed on as it is.

    y1 : float
      Passed on as it is.

    x2 : float
      Passed on as it is.

    y2 : float
      Passed on as it is.

    x3 : float
      Passed on as it is.

    y3 : float
      Passed on as it is.

    x4 : float
      Passed on as it is.

    y4 : float
      Passed on as it is.

    level : int
      Passed on as it is.

    flags : QCPointFlags
      Passed on as its number.
    """
    #  void QCPainterEngine::tesselateBezier(float x1, float y1, float x2,
    #      float y2, float x3, float y3, float x4, float y4, int level,
    #      QCPointFlags flags)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine15tesselateBezierEffffffffiNS_12QCPointF'
        'lagsE',
        x1, y1, x2, y2, x3, y3, x4, y4, level, flags.value,
    )

  @overload(int, int, QCanvasPainter.PathWinding)
  def enforceWinding(
      self,
      pointsOffset: int,
      pointsCount: int,
      winding: QCanvasPainter.PathWinding,
  ) -> None:
    """
    Calls Qt's 'void QCPainterEngine::enforceWinding(int pointsOffset, int
    pointsCount, QCanvasPainter::PathWinding winding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#enforceWinding

    Parameters
    ----------

    pointsOffset : int
      Passed on as it is.

    pointsCount : int
      Passed on as it is.

    winding : QCanvasPainter.PathWinding
      Passed on as its number.
    """
    #  void QCPainterEngine::enforceWinding(int pointsOffset, int
    #      pointsCount, QCanvasPainter::PathWinding winding)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine14enforceWindingEiiN14QCanvasPainter11Pa'
        'thWindingE',
        pointsOffset, pointsCount, winding.value,
    )

  @overload(float, QCanvasPainter.LineJoin, float)
  def calculateJoins(
      self,
      w: float,
      join: QCanvasPainter.LineJoin,
      miterLimit: float,
  ) -> None:
    """
    Calls Qt's 'void QCPainterEngine::calculateJoins(float w,
    QCanvasPainter::LineJoin join, float miterLimit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#calculateJoins

    Parameters
    ----------

    w : float
      Passed on as it is.

    join : QCanvasPainter.LineJoin
      Passed on as its number.

    miterLimit : float
      Passed on as it is.
    """
    #  void QCPainterEngine::calculateJoins(float w, QCanvasPainter::LineJoin
    #      join, float miterLimit)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine14calculateJoinsEfN14QCanvasPainter8Line'
        'JoinEf',
        w, join.value, miterLimit,
    )

  @overload(QCPoint, float, float, float, float, float, float, float)
  def addButtCapStart(
      self,
      p: QCPoint,
      dx: float,
      dy: float,
      w: float,
      d: float,
      aa: float,
      u0: float,
      u1: float,
  ) -> None:
    """
    Calls Qt's 'void QCPainterEngine::addButtCapStart(const QCPoint &p, float
    dx, float dy, float w, float d, float aa, float u0, float u1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#addButtCapStart

    Parameters
    ----------

    p : QCPoint
      Passed on as a value: Qt reads the C++ QCPoint, which stays Python's
      own.

    dx : float
      Passed on as it is.

    dy : float
      Passed on as it is.

    w : float
      Passed on as it is.

    d : float
      Passed on as it is.

    aa : float
      Passed on as it is.

    u0 : float
      Passed on as it is.

    u1 : float
      Passed on as it is.
    """
    #  void QCPainterEngine::addButtCapStart(const QCPoint &p, float dx,
    #      float dy, float w, float d, float aa, float u0, float u1)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine15addButtCapStartERK7QCPointfffffff',
        self._valueOf(p), dx, dy, w, d, aa, u0, u1,
    )

  @overload(QCPoint, float, float, float, int, float, float)
  def addRoundCapStart(
      self,
      p: QCPoint,
      dx: float,
      dy: float,
      w: float,
      capDivs: int,
      u0: float,
      u1: float,
  ) -> None:
    """
    Calls Qt's 'void QCPainterEngine::addRoundCapStart(const QCPoint &p,
    float dx, float dy, float w, int capDivs, float u0, float u1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#addRoundCapStart

    Parameters
    ----------

    p : QCPoint
      Passed on as a value: Qt reads the C++ QCPoint, which stays Python's
      own.

    dx : float
      Passed on as it is.

    dy : float
      Passed on as it is.

    w : float
      Passed on as it is.

    capDivs : int
      Passed on as it is.

    u0 : float
      Passed on as it is.

    u1 : float
      Passed on as it is.
    """
    #  void QCPainterEngine::addRoundCapStart(const QCPoint &p, float dx,
    #      float dy, float w, int capDivs, float u0, float u1)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine16addRoundCapStartERK7QCPointfffiff',
        self._valueOf(p), dx, dy, w, capDivs, u0, u1,
    )

  @overload(QCPoint, float, float, float, float, float, float, float)
  def addButtCapEnd(
      self,
      p: QCPoint,
      dx: float,
      dy: float,
      w: float,
      d: float,
      aa: float,
      u0: float,
      u1: float,
  ) -> None:
    """
    Calls Qt's 'void QCPainterEngine::addButtCapEnd(const QCPoint &p, float
    dx, float dy, float w, float d, float aa, float u0, float u1)'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#addButtCapEnd

    Parameters
    ----------

    p : QCPoint
      Passed on as a value: Qt reads the C++ QCPoint, which stays Python's
      own.

    dx : float
      Passed on as it is.

    dy : float
      Passed on as it is.

    w : float
      Passed on as it is.

    d : float
      Passed on as it is.

    aa : float
      Passed on as it is.

    u0 : float
      Passed on as it is.

    u1 : float
      Passed on as it is.
    """
    #  void QCPainterEngine::addButtCapEnd(const QCPoint &p, float dx, float
    #      dy, float w, float d, float aa, float u0, float u1)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine13addButtCapEndERK7QCPointfffffff',
        self._valueOf(p), dx, dy, w, d, aa, u0, u1,
    )

  @overload(QCPoint, float, float, float, int, float, float)
  def addRoundCapEnd(
      self,
      p: QCPoint,
      dx: float,
      dy: float,
      w: float,
      capDivs: int,
      u0: float,
      u1: float,
  ) -> None:
    """
    Calls Qt's 'void QCPainterEngine::addRoundCapEnd(const QCPoint &p, float
    dx, float dy, float w, int capDivs, float u0, float u1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#addRoundCapEnd

    Parameters
    ----------

    p : QCPoint
      Passed on as a value: Qt reads the C++ QCPoint, which stays Python's
      own.

    dx : float
      Passed on as it is.

    dy : float
      Passed on as it is.

    w : float
      Passed on as it is.

    capDivs : int
      Passed on as it is.

    u0 : float
      Passed on as it is.

    u1 : float
      Passed on as it is.
    """
    #  void QCPainterEngine::addRoundCapEnd(const QCPoint &p, float dx, float
    #      dy, float w, int capDivs, float u0, float u1)
    self.uglySide.call(
        'ritual_ZN15QCPainterEngine14addRoundCapEndERK7QCPointfffiff',
        self._valueOf(p), dx, dy, w, capDivs, u0, u1,
    )

  @overload(float, float, float, float)
  def addVert(self, x: float, y: float, u: float, v: float) -> None:
    """
    Calls Qt's 'void QCPainterEngine::addVert(float x, float y, float u,
    float v)'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#addVert

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    u : float
      Passed on as it is.

    v : float
      Passed on as it is.
    """
    #  void QCPainterEngine::addVert(float x, float y, float u, float v)
    self.uglySide.call('ritual_ZN15QCPainterEngine7addVertEffff', x, y, u, v)

  @overload(int)
  def ensureVertices(self, count: int) -> None:
    """
    Calls Qt's 'void QCPainterEngine::ensureVertices(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#ensureVertices

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QCPainterEngine::ensureVertices(int count)
    self.uglySide.call('ritual_ZN15QCPainterEngine14ensureVerticesEi', count)

  @overload()
  @overload(bool)
  def getFillPaint(self, ignoreTransform: bool = False) -> QCPaint:
    """
    Calls Qt's 'QCPaint QCPainterEngine::getFillPaint(bool ignoreTransform)'.

    Qt's own words: https://doc.qt.io/qt-6/qcpainterengine.html#getFillPaint

    Parameters
    ----------

    ignoreTransform : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    QCPaint
      A new cute QCPaint around the copy Qt gave back. Python owns it.
    """
    #  QCPaint QCPainterEngine::getFillPaint(bool ignoreTransform)
    address = self.uglySide.call(
        'ritual_ZN15QCPainterEngine12getFillPaintEb', ignoreTransform,
    )
    from . import QCPaint
    return QCPaint._cuteOwning(address)

  def updateStateFontVars(self) -> None:
    """
    Calls Qt's 'void QCPainterEngine::updateStateFontVars()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcpainterengine.html#updateStateFontVars
    """
    #  void QCPainterEngine::updateStateFontVars()
    self.uglySide.call('ritual_ZN15QCPainterEngine19updateStateFontVarsEv')

  @staticmethod
  def addBevelJoin(*__, **_) -> Never:
    """
    Qt's 'void QCPainterEngine::addBevelJoin(const QCPoint &p0, const QCPoint
    &p1, float lw, float rw, float lu, float ru)': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'adjustBevel'.
    """
    raise NotImplementedError(
        "'QCPainterEngine.addBevelJoin' has no cute function yet. Qt's "
        "'void QCPainterEngine::addBevelJoin(const QCPoint &p0, const "
        "QCPoint &p1, float lw, float rw, float lu, float ru)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'adjustBevel'.")

  @staticmethod
  def addRoundJoin(*__, **_) -> Never:
    """
    Qt's 'void QCPainterEngine::addRoundJoin(const QCPoint &p0, const QCPoint
    &p1, float lw, float rw, float lu, float ru, int capDivs)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'adjustBevel'.
    """
    raise NotImplementedError(
        "'QCPainterEngine.addRoundJoin' has no cute function yet. Qt's "
        "'void QCPainterEngine::addRoundJoin(const QCPoint &p0, const "
        "QCPoint &p1, float lw, float rw, float lu, float ru, int "
        "capDivs)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'adjustBevel'.")

  @staticmethod
  def appendCommand(*__, **_) -> Never:
    """
    Qt's 'void QCPainterEngine::appendCommand(QCCommand command)': names the
    enum 'QCCommand', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QCPainterEngine.appendCommand' has no cute function yet. Qt's "
        "'void QCPainterEngine::appendCommand(QCCommand command)': names "
        "the enum 'QCCommand', whose class cannot be named here.")

  @staticmethod
  def appendCommands(*__, **_) -> Never:
    """
    Qt's 'void QCPainterEngine::appendCommands(const QCCommand *commands, int
    cCount)': names 'QCCommand', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QCPainterEngine.appendCommands' has no cute function yet. Qt's "
        "'void QCPainterEngine::appendCommands(const QCCommand *commands, "
        "int cCount)': names 'QCCommand', which has no cute class yet.")

  @staticmethod
  def appendCommandsData(*__, **_) -> Never:
    """
    Qt's 'void QCPainterEngine::appendCommandsData(const float *commandsData,
    int dCount, bool ignoreTransform)': names 'float', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QCPainterEngine.appendCommandsData' has no cute function yet. "
        "Qt's 'void QCPainterEngine::appendCommandsData(const float "
        "*commandsData, int dCount, bool ignoreTransform)': names 'float', "
        "which has no cute class yet.")

  @staticmethod
  def appendPainterPath(*__, **_) -> Never:
    """
    - Qt's 'void QCPainterEngine::appendPainterPath(const QCanvasPath &path,
      const QTransform &transform)': Qt's library has no name for it, and its
      code in Qt's source does not compile apart from its file: incomplete
      type 'QCanvasPathPrivate' named in nested name specifier.
    - Qt's 'void QCPainterEngine::appendPainterPath(const QCanvasPath &path,
      qsizetype start, qsizetype count, const QTransform &transform)': Qt's
      library has no name for it, and its code in Qt's source does not
      compile apart from its file: incomplete type 'QCanvasPathPrivate' named
      in nested name specifier.
    """
    raise NotImplementedError(
        "'QCPainterEngine.appendPainterPath' has no cute function yet. Qt's "
        "'void QCPainterEngine::appendPainterPath(const QCanvasPath &path, "
        "const QTransform &transform)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "incomplete type 'QCanvasPathPrivate' named in nested name "
        "specifier. Qt's 'void QCPainterEngine::appendPainterPath(const "
        "QCanvasPath &path, qsizetype start, qsizetype count, const "
        "QTransform &transform)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: "
        "incomplete type 'QCanvasPathPrivate' named in nested name "
        "specifier.")

  @staticmethod
  def beginPaint(*__, **_) -> Never:
    """
    Qt's 'void QCPainterEngine::beginPaint(float logicalWidth, float
    logicalHeight, float dpr)': leans on
    'QCPainterRhiRenderer::setViewport(float, float, float, float)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QCPainterEngine.beginPaint' has no cute function yet. Qt's 'void "
        "QCPainterEngine::beginPaint(float logicalWidth, float "
        "logicalHeight, float dpr)': leans on "
        "'QCPainterRhiRenderer::setViewport(float, float, float, float)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def commandsToPaths(*__, **_) -> Never:
    """
    Qt's 'void QCPainterEngine::commandsToPaths()': leans on
    'QCPainterRhiRenderer::testFlag(QCPainterRhiRenderer::RenderFlag) const',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QCPainterEngine.commandsToPaths' has no cute function yet. Qt's "
        "'void QCPainterEngine::commandsToPaths()': leans on "
        "'QCPainterRhiRenderer::testFlag(QCPainterRhiRenderer::RenderFlag) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def createImage(*__, **_) -> Never:
    """
    Qt's 'int QCPainterEngine::createImage(int width, int height,
    QCanvasPainter::ImageFlags flags, const uchar *data)': leans on
    'QCPainterRhiRenderer::renderCreateTexture(QCTextureFormat, int, int,
    QFlags<QCanvasPainter::ImageFlag>, unsigned char const*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QCPainterEngine.createImage' has no cute function yet. Qt's 'int "
        "QCPainterEngine::createImage(int width, int height, "
        "QCanvasPainter::ImageFlags flags, const uchar *data)': leans on "
        "'QCPainterRhiRenderer::renderCreateTexture(QCTextureFormat, int, "
        "int, QFlags<QCanvasPainter::ImageFlag>, unsigned char const*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def deleteImage(*__, **_) -> Never:
    """
    Qt's 'bool QCPainterEngine::deleteImage(int imageId)': leans on
    'QCPainterRhiRenderer::renderDeleteTexture(int)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCPainterEngine.deleteImage' has no cute function yet. Qt's 'bool "
        "QCPainterEngine::deleteImage(int imageId)': leans on "
        "'QCPainterRhiRenderer::renderDeleteTexture(int)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def drawImageId(*__, **_) -> Never:
    """
    Qt's 'void QCPainterEngine::drawImageId(int imageId, float x, float y,
    float width, float height, QColor tintColor)': leans on
    'QCPainterRhiRenderer::renderFill(QCPaint const&, QCState const&, QRectF
    const&, std::optional<QCRhiUncachedPathDrawArgs>,
    std::optional<QCRhiCachedPathDrawArgs>, QCanvasPainter::FillRule)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QCPainterEngine.drawImageId' has no cute function yet. Qt's 'void "
        "QCPainterEngine::drawImageId(int imageId, float x, float y, float "
        "width, float height, QColor tintColor)': leans on "
        "'QCPainterRhiRenderer::renderFill(QCPaint const&, QCState const&, "
        "QRectF const&, std::optional<QCRhiUncachedPathDrawArgs>, "
        "std::optional<QCRhiCachedPathDrawArgs>, "
        "QCanvasPainter::FillRule)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def drawImageIdAt(*__, **_) -> Never:
    """
    Qt's 'void QCPainterEngine::drawImageIdAt(int imageId, float x, float y,
    float width, float height, float dX, float dY, float dWidth, float
    dHeight, QColor tintColor)': leans on
    'QCPainterRhiRenderer::renderFill(QCPaint const&, QCState const&, QRectF
    const&, std::optional<QCRhiUncachedPathDrawArgs>,
    std::optional<QCRhiCachedPathDrawArgs>, QCanvasPainter::FillRule)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QCPainterEngine.drawImageIdAt' has no cute function yet. Qt's "
        "'void QCPainterEngine::drawImageIdAt(int imageId, float x, float "
        "y, float width, float height, float dX, float dY, float dWidth, "
        "float dHeight, QColor tintColor)': leans on "
        "'QCPainterRhiRenderer::renderFill(QCPaint const&, QCState const&, "
        "QRectF const&, std::optional<QCRhiUncachedPathDrawArgs>, "
        "std::optional<QCRhiCachedPathDrawArgs>, "
        "QCanvasPainter::FillRule)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def expandFill(*__, **_) -> Never:
    """
    Qt's 'void QCPainterEngine::expandFill()': leans on
    'QCPainterRhiRenderer::testFlag(QCPainterRhiRenderer::RenderFlag) const',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QCPainterEngine.expandFill' has no cute function yet. Qt's 'void "
        "QCPainterEngine::expandFill()': leans on "
        "'QCPainterRhiRenderer::testFlag(QCPainterRhiRenderer::RenderFlag) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def expandStroke(*__, **_) -> Never:
    """
    Qt's 'void QCPainterEngine::expandStroke(float w, QCanvasPainter::LineCap
    cap, QCanvasPainter::LineJoin join, float miterLimit)': leans on
    'QCPainterRhiRenderer::testFlag(QCPainterRhiRenderer::RenderFlag) const',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QCPainterEngine.expandStroke' has no cute function yet. Qt's "
        "'void QCPainterEngine::expandStroke(float w, "
        "QCanvasPainter::LineCap cap, QCanvasPainter::LineJoin join, float "
        "miterLimit)': leans on "
        "'QCPainterRhiRenderer::testFlag(QCPainterRhiRenderer::RenderFlag) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def fill(*__, **_) -> Never:
    """
    - Qt's 'void QCPainterEngine::fill(const QCanvasPath &path,
      QCanvasPainter::FillRule fillRule, int pathGroup)': Qt's library has no
      name for it, and its code in Qt's source does not compile apart from
      its file: incomplete type 'QCanvasPathPrivate' named in nested name
      specifier.
    - Qt's 'void QCPainterEngine::fill(QCanvasPainter::FillRule fillRule,
      QCanvasPath *maybePath, int pathGroup, bool cachedPathUpdateRequired)':
      leans on 'QCPainterRhiRenderer::renderFill(QCPaint const&, QCState
      const&, QRectF const&, std::optional<QCRhiUncachedPathDrawArgs>,
      std::optional<QCRhiCachedPathDrawArgs>, QCanvasPainter::FillRule)',
      which Qt's source does not mark for use from outside Qt and has no code
      for that could be taken.
    """
    raise NotImplementedError(
        "'QCPainterEngine.fill' has no cute function yet. Qt's 'void "
        "QCPainterEngine::fill(const QCanvasPath &path, "
        "QCanvasPainter::FillRule fillRule, int pathGroup)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: incomplete type 'QCanvasPathPrivate' named in "
        "nested name specifier. Qt's 'void "
        "QCPainterEngine::fill(QCanvasPainter::FillRule fillRule, "
        "QCanvasPath *maybePath, int pathGroup, bool "
        "cachedPathUpdateRequired)': leans on "
        "'QCPainterRhiRenderer::renderFill(QCPaint const&, QCState const&, "
        "QRectF const&, std::optional<QCRhiUncachedPathDrawArgs>, "
        "std::optional<QCRhiCachedPathDrawArgs>, "
        "QCanvasPainter::FillRule)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def fillCachedPathUpdateRequired(*__, **_) -> Never:
    """
    Qt's 'bool QCPainterEngine::fillCachedPathUpdateRequired(QCanvasPath
    *path, int pathGroup)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: incomplete type
    'QCanvasPathPrivate' named in nested name specifier.
    """
    raise NotImplementedError(
        "'QCPainterEngine.fillCachedPathUpdateRequired' has no cute "
        "function yet. Qt's 'bool "
        "QCPainterEngine::fillCachedPathUpdateRequired(QCanvasPath *path, "
        "int pathGroup)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: incomplete type "
        "'QCanvasPathPrivate' named in nested name specifier.")

  @staticmethod
  def fillForClear(*__, **_) -> Never:
    """
    Qt's 'void QCPainterEngine::fillForClear()': leans on
    'QCPainterRhiRenderer::renderFill(QCPaint const&, QCState const&, QRectF
    const&, std::optional<QCRhiUncachedPathDrawArgs>,
    std::optional<QCRhiCachedPathDrawArgs>, QCanvasPainter::FillRule)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QCPainterEngine.fillForClear' has no cute function yet. Qt's "
        "'void QCPainterEngine::fillForClear()': leans on "
        "'QCPainterRhiRenderer::renderFill(QCPaint const&, QCState const&, "
        "QRectF const&, std::optional<QCRhiUncachedPathDrawArgs>, "
        "std::optional<QCRhiCachedPathDrawArgs>, "
        "QCanvasPainter::FillRule)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def fillPlainRect(*__, **_) -> Never:
    """
    Qt's 'void QCPainterEngine::fillPlainRect(const QCPaint &paint, float x,
    float y, float width, float height)': leans on
    'QCPainterRhiRenderer::renderFill(QCPaint const&, QCState const&, QRectF
    const&, std::optional<QCRhiUncachedPathDrawArgs>,
    std::optional<QCRhiCachedPathDrawArgs>, QCanvasPainter::FillRule)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QCPainterEngine.fillPlainRect' has no cute function yet. Qt's "
        "'void QCPainterEngine::fillPlainRect(const QCPaint &paint, float "
        "x, float y, float width, float height)': leans on "
        "'QCPainterRhiRenderer::renderFill(QCPaint const&, QCState const&, "
        "QRectF const&, std::optional<QCRhiUncachedPathDrawArgs>, "
        "std::optional<QCRhiCachedPathDrawArgs>, "
        "QCanvasPainter::FillRule)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def fillShapedText(*__, **_) -> Never:
    """
    Qt's 'void QCPainterEngine::fillShapedText(QFontEngine *fontEngine, const
    quint32 *glyphIndexes, const QFixedPoint *glyphPositions, int
    glyphCount)': leans on
    'QCPainterRhiRenderer::populateFontFromShapedText(QFontEngine*, unsigned
    int const*, QFixedPoint const*, int,
    QVarLengthArray<QCRhiDistanceFieldGlyphCache::TexturedPoint2D, 256ll>&,
    QVarLengthArray<unsigned int, 384ll>&)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCPainterEngine.fillShapedText' has no cute function yet. Qt's "
        "'void QCPainterEngine::fillShapedText(QFontEngine *fontEngine, "
        "const quint32 *glyphIndexes, const QFixedPoint *glyphPositions, "
        "int glyphCount)': leans on "
        "'QCPainterRhiRenderer::populateFontFromShapedText(QFontEngine*, "
        "unsigned int const*, QFixedPoint const*, int, "
        "QVarLengthArray<QCRhiDistanceFieldGlyphCache::TexturedPoint2D, "
        "256ll>&, QVarLengthArray<unsigned int, 384ll>&)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def fillText(*__, **_) -> Never:
    """
    Qt's 'void QCPainterEngine::fillText(const QString &text, const QRectF
    &rect)': leans on 'QCPainterRhiRenderer::populateFont(QFont const&,
    QRectF const&, QString const&,
    QVarLengthArray<QCRhiDistanceFieldGlyphCache::TexturedPoint2D, 256ll>&,
    QVarLengthArray<unsigned int, 384ll>&)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCPainterEngine.fillText' has no cute function yet. Qt's 'void "
        "QCPainterEngine::fillText(const QString &text, const QRectF "
        "&rect)': leans on 'QCPainterRhiRenderer::populateFont(QFont "
        "const&, QRectF const&, QString const&, "
        "QVarLengthArray<QCRhiDistanceFieldGlyphCache::TexturedPoint2D, "
        "256ll>&, QVarLengthArray<unsigned int, 384ll>&)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def getStrokePaint(*__, **_) -> Never:
    """
    Qt's 'QCPaint QCPainterEngine::getStrokePaint(float *strokeWidth, bool
    ignoreTransform)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'QCPAINTER_ANTIALIAS_MULTIPLIER'.
    """
    raise NotImplementedError(
        "'QCPainterEngine.getStrokePaint' has no cute function yet. Qt's "
        "'QCPaint QCPainterEngine::getStrokePaint(float *strokeWidth, bool "
        "ignoreTransform)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'QCPAINTER_ANTIALIAS_MULTIPLIER'.")

  @staticmethod
  def initialize(*__, **_) -> Never:
    """
    Qt's 'QCContext *QCPainterEngine::initialize(QCPainterRhiRenderer
    *renderer)': leans on
    'QCPainterRhiRenderer::setFlag(QFlags<QCPainterRhiRenderer::RenderFlag>,
    bool)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCPainterEngine.initialize' has no cute function yet. Qt's "
        "'QCContext *QCPainterEngine::initialize(QCPainterRhiRenderer "
        "*renderer)': leans on "
        "'QCPainterRhiRenderer::setFlag(QFlags<QCPainterRhiRenderer::RenderF"
        "lag>, bool)', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

  @staticmethod
  def preparePainterPath(*__, **_) -> Never:
    """
    Qt's 'void QCPainterEngine::preparePainterPath(const QCanvasPath &path,
    bool ignoreTransform)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: incomplete type
    'QCanvasPathPrivate' named in nested name specifier.
    """
    raise NotImplementedError(
        "'QCPainterEngine.preparePainterPath' has no cute function yet. "
        "Qt's 'void QCPainterEngine::preparePainterPath(const QCanvasPath "
        "&path, bool ignoreTransform)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "incomplete type 'QCanvasPathPrivate' named in nested name "
        "specifier.")

  @staticmethod
  def removePathGroup(*__, **_) -> Never:
    """
    Qt's 'void QCPainterEngine::removePathGroup(int pathGroup)': leans on
    'QCPainterRhiRenderer::removePathGroup(int)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCPainterEngine.removePathGroup' has no cute function yet. Qt's "
        "'void QCPainterEngine::removePathGroup(int pathGroup)': leans on "
        "'QCPainterRhiRenderer::removePathGroup(int)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def renderFilledText(*__, **_) -> Never:
    """
    Qt's 'void QCPainterEngine::renderFilledText(int fontTex)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier
    'QCPAINTER_TEXT_VERTEX_INDEX_LIST_REUSE_CAPACITY'.
    """
    raise NotImplementedError(
        "'QCPainterEngine.renderFilledText' has no cute function yet. Qt's "
        "'void QCPainterEngine::renderFilledText(int fontTex)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'QCPAINTER_TEXT_VERTEX_INDEX_LIST_REUSE_CAPACITY'.")

  @staticmethod
  def reset(*__, **_) -> Never:
    """
    Qt's 'void QCPainterEngine::reset()': leans on
    'QCPainterRhiRenderer::setFlag(QFlags<QCPainterRhiRenderer::RenderFlag>,
    bool)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCPainterEngine.reset' has no cute function yet. Qt's 'void "
        "QCPainterEngine::reset()': leans on "
        "'QCPainterRhiRenderer::setFlag(QFlags<QCPainterRhiRenderer::RenderF"
        "lag>, bool)', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

  @staticmethod
  def resetClipRect(*__, **_) -> Never:
    """
    Qt's 'void QCPainterEngine::resetClipRect()': leans on
    'QCPainterRhiRenderer::setFlag(QFlags<QCPainterRhiRenderer::RenderFlag>,
    bool)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCPainterEngine.resetClipRect' has no cute function yet. Qt's "
        "'void QCPainterEngine::resetClipRect()': leans on "
        "'QCPainterRhiRenderer::setFlag(QFlags<QCPainterRhiRenderer::RenderF"
        "lag>, bool)', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

  @staticmethod
  def setAntialiasingEnabled(*__, **_) -> Never:
    """
    Qt's 'void QCPainterEngine::setAntialiasingEnabled(bool enabled)': leans
    on
    'QCPainterRhiRenderer::setFlag(QFlags<QCPainterRhiRenderer::RenderFlag>,
    bool)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCPainterEngine.setAntialiasingEnabled' has no cute function yet. "
        "Qt's 'void QCPainterEngine::setAntialiasingEnabled(bool enabled)': "
        "leans on "
        "'QCPainterRhiRenderer::setFlag(QFlags<QCPainterRhiRenderer::RenderF"
        "lag>, bool)', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

  @staticmethod
  def setClipRect(*__, **_) -> Never:
    """
    Qt's 'void QCPainterEngine::setClipRect(const QRectF &rect)': leans on
    'QCPainterRhiRenderer::setFlag(QFlags<QCPainterRhiRenderer::RenderFlag>,
    bool)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCPainterEngine.setClipRect' has no cute function yet. Qt's 'void "
        "QCPainterEngine::setClipRect(const QRectF &rect)': leans on "
        "'QCPainterRhiRenderer::setFlag(QFlags<QCPainterRhiRenderer::RenderF"
        "lag>, bool)', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

  @staticmethod
  def setDevicePixelRatio(*__, **_) -> Never:
    """
    Qt's 'void QCPainterEngine::setDevicePixelRatio(float ratio)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier
    'QCPAINTER_ANTIALIAS_MULTIPLIER'.
    """
    raise NotImplementedError(
        "'QCPainterEngine.setDevicePixelRatio' has no cute function yet. "
        "Qt's 'void QCPainterEngine::setDevicePixelRatio(float ratio)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'QCPAINTER_ANTIALIAS_MULTIPLIER'.")

  @staticmethod
  def setHighQualityStrokingEnabled(*__, **_) -> Never:
    """
    Qt's 'void QCPainterEngine::setHighQualityStrokingEnabled(bool enabled)':
    leans on
    'QCPainterRhiRenderer::setFlag(QFlags<QCPainterRhiRenderer::RenderFlag>,
    bool)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCPainterEngine.setHighQualityStrokingEnabled' has no cute "
        "function yet. Qt's 'void "
        "QCPainterEngine::setHighQualityStrokingEnabled(bool enabled)': "
        "leans on "
        "'QCPainterRhiRenderer::setFlag(QFlags<QCPainterRhiRenderer::RenderF"
        "lag>, bool)', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

  @staticmethod
  def setStencilClip(*__, **_) -> Never:
    """
    - Qt's 'void QCPainterEngine::setStencilClip(const QList<QRectF>
      &rects)': leans on 'QCPainterRhiRenderer::renderStencil(QCState const&,
      QList<QRectF> const&)', which Qt's source does not mark for use from
      outside Qt and has no code for that could be taken.
    - Qt's 'void QCPainterEngine::setStencilClip(const QVectorPath
      &clipPath)': leans on 'QCPainterRhiRenderer::renderStencil(QCState
      const&, QVectorPath const&)', which Qt's source does not mark for use
      from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCPainterEngine.setStencilClip' has no cute function yet. Qt's "
        "'void QCPainterEngine::setStencilClip(const QList<QRectF> "
        "&rects)': leans on 'QCPainterRhiRenderer::renderStencil(QCState "
        "const&, QList<QRectF> const&)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken. "
        "Qt's 'void QCPainterEngine::setStencilClip(const QVectorPath "
        "&clipPath)': leans on 'QCPainterRhiRenderer::renderStencil(QCState "
        "const&, QVectorPath const&)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setWindingEnforceEnabled(*__, **_) -> Never:
    """
    Qt's 'void QCPainterEngine::setWindingEnforceEnabled(bool enabled)':
    leans on
    'QCPainterRhiRenderer::setFlag(QFlags<QCPainterRhiRenderer::RenderFlag>,
    bool)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCPainterEngine.setWindingEnforceEnabled' has no cute function "
        "yet. Qt's 'void QCPainterEngine::setWindingEnforceEnabled(bool "
        "enabled)': leans on "
        "'QCPainterRhiRenderer::setFlag(QFlags<QCPainterRhiRenderer::RenderF"
        "lag>, bool)', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

  @staticmethod
  def stroke(*__, **_) -> Never:
    """
    - Qt's 'void QCPainterEngine::stroke(const QCanvasPath &path, int
      pathGroup)': Qt's library has no name for it, and its code in Qt's
      source does not compile apart from its file: incomplete type
      'QCanvasPathPrivate' named in nested name specifier.
    - Qt's 'void QCPainterEngine::stroke(QCanvasPath *maybePath, int
      pathGroup, bool cachedPathUpdateRequired)': leans on
      'QCPainterRhiRenderer::renderStroke(QCPaint const&, QCState const&,
      float, std::optional<QCRhiUncachedPathDrawArgs>,
      std::optional<QCRhiCachedPathDrawArgs>)', which Qt's source does not
      mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCPainterEngine.stroke' has no cute function yet. Qt's 'void "
        "QCPainterEngine::stroke(const QCanvasPath &path, int pathGroup)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: incomplete type "
        "'QCanvasPathPrivate' named in nested name specifier. Qt's 'void "
        "QCPainterEngine::stroke(QCanvasPath *maybePath, int pathGroup, "
        "bool cachedPathUpdateRequired)': leans on "
        "'QCPainterRhiRenderer::renderStroke(QCPaint const&, QCState "
        "const&, float, std::optional<QCRhiUncachedPathDrawArgs>, "
        "std::optional<QCRhiCachedPathDrawArgs>)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def strokeCachedPathUpdateRequired(*__, **_) -> Never:
    """
    Qt's 'bool QCPainterEngine::strokeCachedPathUpdateRequired(QCanvasPath
    *path, int pathGroup)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: incomplete type
    'QCanvasPathPrivate' named in nested name specifier.
    """
    raise NotImplementedError(
        "'QCPainterEngine.strokeCachedPathUpdateRequired' has no cute "
        "function yet. Qt's 'bool "
        "QCPainterEngine::strokeCachedPathUpdateRequired(QCanvasPath *path, "
        "int pathGroup)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: incomplete type "
        "'QCanvasPathPrivate' named in nested name specifier.")

  @staticmethod
  def syncDebugCounters(*__, **_) -> Never:
    """
    Qt's 'void QCPainterEngine::syncDebugCounters()': leans on
    'QCPainterRhiRenderer::syncDebugCounters()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCPainterEngine.syncDebugCounters' has no cute function yet. Qt's "
        "'void QCPainterEngine::syncDebugCounters()': leans on "
        "'QCPainterRhiRenderer::syncDebugCounters()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")
