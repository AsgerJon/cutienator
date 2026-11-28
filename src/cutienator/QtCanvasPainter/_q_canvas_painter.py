"""
QCanvasPainter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/qcanvaspainter.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QCanvasOffscreenCanvas

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF, QRectF, QSize
  from ..QtGui import QColor, QFont, QImage, QPainterPath, QRhiTexture
  from ..QtGui import QTransform
  from . import QCanvasBoxShadow, QCanvasBrush, QCanvasImage
  from . import QCanvasPainterPrivate, QCanvasPath
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCanvasBoxShadow = WAIT['QCanvasBoxShadow']
  QCanvasBrush = WAIT['QCanvasBrush']
  QCanvasImage = WAIT['QCanvasImage']
  QCanvasPath = WAIT['QCanvasPath']
  QColor = WAIT['QColor']
  QFont = WAIT['QFont']
  QImage = WAIT['QImage']
  QPainterPath = WAIT['QPainterPath']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']
  QRhiTexture = WAIT['QRhiTexture']
  QSize = WAIT['QSize']
  QTransform = WAIT['QTransform']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCanvasPainter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCanvasPainter: a plain Python object standing in
  front of one C++ QCanvasPainter.

  What exists
  -----------

  Every function of Qt's QCanvasPainter that has a ritual and that Python can
  call so far, 68 names in all: 'save', 'restore', 'reset', 'setStrokeStyle',
  'setFillStyle', 'setMiterLimit', 'setLineWidth', 'setLineCap',
  'setLineJoin', 'setGlobalAlpha', 'setGlobalCompositeOperation',
  'setGlobalBrightness', 'setGlobalContrast', 'setGlobalSaturation',
  'setFillRule', 'resetTransform', 'setTransform', 'transform', 'translate',
  'rotate', 'skew', 'scale', 'getTransform', 'setClipRect', 'resetClipping',
  'beginPath', 'closePath', 'moveTo', 'lineTo', 'bezierCurveTo',
  'quadraticCurveTo', 'arcTo', 'arc', 'rect', 'roundRect', 'ellipse',
  'circle', 'addPath', 'setPathWinding', 'beginSolidSubPath',
  'beginHoleSubPath', 'fill', 'stroke', 'fillRect', 'clearRect',
  'strokeRect', 'drawBoxShadow', 'drawImage', 'setFont', 'setTextAlign',
  'setTextBaseline', 'setTextDirection', 'setTextWrapMode',
  'setTextLineHeight', 'setTextAntialias', 'fillText', 'textBoundingBox',
  'setAntialias', 'setWindingEnforce', 'setHighQualityStroking', 'addImage',
  'removeImage', 'cleanupResources', 'activeImageMemoryUsage',
  'activeImageCount', 'removePathGroup', 'createCanvas', 'd_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCanvasPainter::~QCanvasPainter()': the destructor: Python never
    removes a C++ QCanvasPainter.
  - Qt's 'void QCanvasPainter::destroyCanvas(QCanvasOffscreenCanvas
    &canvas)': takes a type Python has no way to hand over yet.
  - Qt's 'const QCanvasPainterPrivate *QCanvasPainter::d_func() const': takes
    in Python what 'QCanvasPainterPrivate *QCanvasPainter::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 112 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QCanvasPainter is created at the first use, not by
    'QCanvasPainter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCanvasPainter.
  - Each name of Qt's QCanvasPainter that has no cute function yet,
    'destroyCanvas', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QCanvasPainter, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class CompositeOperation(CuteNum, scoped=True):
    """
    The enum 'QCanvasPainter::CompositeOperation' of Qt, with the 3 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    SourceOver = Kee[int](0)
    SourceAtop = Kee[int](1)
    DestinationOut = Kee[int](2)

  class FillRule(CuteNum, scoped=True):
    """
    The enum 'QCanvasPainter::FillRule' of Qt, with the 2 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    NonZero = Kee[int](0)
    EvenOdd = Kee[int](1)

  class ImageFlag(CuteFlags, scoped=True):
    """
    The flags enum 'QCanvasPainter::ImageFlag' of Qt, with the 7 names Qt
    gives in it. Qt names the type of its combinations
    'QCanvasPainter::ImageFlags'. C++ keeps these names inside the enum, so
    the class that holds the enum does not have them.
    """

    GenerateMipmaps = 0x1
    RepeatX = 0x2
    RepeatY = 0x4
    Repeat = 0x6
    FlipY = 0x8
    Premultiplied = 0x10
    Nearest = 0x20

  ImageFlags = ImageFlag

  class LineCap(CuteNum, scoped=True):
    """
    The enum 'QCanvasPainter::LineCap' of Qt, with the 3 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Butt = Kee[int](0)
    Round = Kee[int](1)
    Square = Kee[int](2)

  class LineJoin(CuteNum, scoped=True):
    """
    The enum 'QCanvasPainter::LineJoin' of Qt, with the 3 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Round = Kee[int](0)
    Bevel = Kee[int](1)
    Miter = Kee[int](2)

  class PathConnection(CuteNum, scoped=True):
    """
    The enum 'QCanvasPainter::PathConnection' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    NotConnected = Kee[int](0)
    Connected = Kee[int](1)

  class PathWinding(CuteNum, scoped=True):
    """
    The enum 'QCanvasPainter::PathWinding' of Qt, with the 2 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    CounterClockWise = Kee[int](0)
    ClockWise = Kee[int](1)

  class TextAlign(CuteNum, scoped=True):
    """
    The enum 'QCanvasPainter::TextAlign' of Qt, with the 5 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Left = Kee[int](0)
    Right = Kee[int](1)
    Center = Kee[int](2)
    Start = Kee[int](3)
    End = Kee[int](4)

  class TextBaseline(CuteNum, scoped=True):
    """
    The enum 'QCanvasPainter::TextBaseline' of Qt, with the 5 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Top = Kee[int](0)
    Hanging = Kee[int](1)
    Middle = Kee[int](2)
    Alphabetic = Kee[int](3)
    Bottom = Kee[int](4)

  class TextDirection(CuteNum, scoped=True):
    """
    The enum 'QCanvasPainter::TextDirection' of Qt, with the 4 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    LeftToRight = Kee[int](0)
    RightToLeft = Kee[int](1)
    Inherit = Kee[int](2)
    Auto = Kee[int](3)

  class WrapMode(CuteNum, scoped=True):
    """
    The enum 'QCanvasPainter::WrapMode' of Qt, with the 4 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    NoWrap = Kee[int](0)
    Wrap = Kee[int](1)
    WordWrap = Kee[int](2)
    WrapAnywhere = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanvasPainter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getTransform(self) -> QTransform:
    """
    Calls Qt's 'QTransform QCanvasPainter::getTransform() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#getTransform

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QCanvasPainter::getTransform() const
    address = self.uglySide.call(
        'ritual_ZNK14QCanvasPainter12getTransformEv',
    )
    from ..QtGui import QTransform
    return QTransform._cuteOwning(address)

  @overload(str, float, float)
  @overload(str, float, float, float)
  def textBoundingBox(
      self,
      text: str,
      x: float,
      y: float,
      maxWidth: float = 0.0,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF QCanvasPainter::textBoundingBox(const QString &text,
    qreal x, qreal y, qreal maxWidth) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainter.html#textBoundingBox

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    maxWidth : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QCanvasPainter::textBoundingBox(const QString &text, qreal x,
    #      qreal y, qreal maxWidth) const
    address = self.uglySide.call(
        'ritual_ZNK14QCanvasPainter15textBoundingBoxERK7QStringddd',
        text, x, y, maxWidth,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(str, QPointF)
  @overload(str, QPointF, float)
  def textBoundingBox(
      self,
      text: str,
      point: QPointF,
      maxWidth: float = 0.0,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF QCanvasPainter::textBoundingBox(const QString &text,
    QPointF point, qreal maxWidth) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainter.html#textBoundingBox

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    maxWidth : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QCanvasPainter::textBoundingBox(const QString &text, QPointF
    #      point, qreal maxWidth) const
    address = self.uglySide.call(
        'ritual_ZNK14QCanvasPainter15textBoundingBoxERK7QString7QPointFd',
        text, self._valueOf(point, 'QPointF'), maxWidth,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(str, QRectF)
  def textBoundingBox(self, text: str, rect: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF QCanvasPainter::textBoundingBox(const QString &text,
    const QRectF &rect) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainter.html#textBoundingBox

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
    #  QRectF QCanvasPainter::textBoundingBox(const QString &text, const
    #      QRectF &rect) const
    address = self.uglySide.call(
        'ritual_ZNK14QCanvasPainter15textBoundingBoxERK7QStringRK6QRectF',
        text, self._valueOf(rect),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def activeImageMemoryUsage(self) -> int:
    """
    Calls Qt's 'qsizetype QCanvasPainter::activeImageMemoryUsage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainter.html#activeImageMemoryUsage
    """
    #  qsizetype QCanvasPainter::activeImageMemoryUsage() const
    return self.uglySide.call(
        'ritual_ZNK14QCanvasPainter22activeImageMemoryUsageEv',
    )

  def activeImageCount(self) -> int:
    """
    Calls Qt's 'qsizetype QCanvasPainter::activeImageCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainter.html#activeImageCount
    """
    #  qsizetype QCanvasPainter::activeImageCount() const
    return self.uglySide.call(
        'ritual_ZNK14QCanvasPainter16activeImageCountEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setStrokeStyle(self, color: QColor) -> None:
    """
    Calls Qt's 'void QCanvasPainter::setStrokeStyle(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#setStrokeStyle

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QCanvasPainter::setStrokeStyle(QColor color)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter14setStrokeStyleE6QColor',
        self._valueOf(color),
    )

  @overload(QCanvasBrush)
  def setStrokeStyle(self, brush: QCanvasBrush) -> None:
    """
    Calls Qt's 'void QCanvasPainter::setStrokeStyle(const QCanvasBrush
    &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#setStrokeStyle

    Parameters
    ----------

    brush : QCanvasBrush
      Passed on as a value: Qt reads the C++ QCanvasBrush, which stays
      Python's own.
    """
    #  void QCanvasPainter::setStrokeStyle(const QCanvasBrush &brush)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter14setStrokeStyleERK12QCanvasBrush',
        self._valueOf(brush),
    )

  @overload(QColor)
  def setFillStyle(self, color: QColor) -> None:
    """
    Calls Qt's 'void QCanvasPainter::setFillStyle(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#setFillStyle

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QCanvasPainter::setFillStyle(QColor color)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter12setFillStyleE6QColor',
        self._valueOf(color),
    )

  @overload(QCanvasBrush)
  def setFillStyle(self, brush: QCanvasBrush) -> None:
    """
    Calls Qt's 'void QCanvasPainter::setFillStyle(const QCanvasBrush
    &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#setFillStyle

    Parameters
    ----------

    brush : QCanvasBrush
      Passed on as a value: Qt reads the C++ QCanvasBrush, which stays
      Python's own.
    """
    #  void QCanvasPainter::setFillStyle(const QCanvasBrush &brush)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter12setFillStyleERK12QCanvasBrush',
        self._valueOf(brush),
    )

  @overload(float)
  def setMiterLimit(self, limit: float) -> None:
    """
    Calls Qt's 'void QCanvasPainter::setMiterLimit(qreal limit)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#setMiterLimit

    Parameters
    ----------

    limit : float
      Passed on as it is.
    """
    #  void QCanvasPainter::setMiterLimit(qreal limit)
    self.uglySide.call('ritual_ZN14QCanvasPainter13setMiterLimitEd', limit)

  @overload(float)
  def setLineWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QCanvasPainter::setLineWidth(qreal width)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#setLineWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QCanvasPainter::setLineWidth(qreal width)
    self.uglySide.call('ritual_ZN14QCanvasPainter12setLineWidthEd', width)

  @overload(LineCap)
  def setLineCap(self, cap: LineCap) -> None:
    """
    Calls Qt's 'void QCanvasPainter::setLineCap(LineCap cap)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#setLineCap

    Parameters
    ----------

    cap : LineCap
      Passed on as its number.
    """
    #  void QCanvasPainter::setLineCap(LineCap cap)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter10setLineCapENS_7LineCapE', cap.value,
    )

  @overload(LineJoin)
  def setLineJoin(self, join: LineJoin) -> None:
    """
    Calls Qt's 'void QCanvasPainter::setLineJoin(LineJoin join)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#setLineJoin

    Parameters
    ----------

    join : LineJoin
      Passed on as its number.
    """
    #  void QCanvasPainter::setLineJoin(LineJoin join)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter11setLineJoinENS_8LineJoinE', join.value,
    )

  @overload(float)
  def setGlobalAlpha(self, alpha: float) -> None:
    """
    Calls Qt's 'void QCanvasPainter::setGlobalAlpha(qreal alpha)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#setGlobalAlpha

    Parameters
    ----------

    alpha : float
      Passed on as it is.
    """
    #  void QCanvasPainter::setGlobalAlpha(qreal alpha)
    self.uglySide.call('ritual_ZN14QCanvasPainter14setGlobalAlphaEd', alpha)

  @overload(CompositeOperation)
  def setGlobalCompositeOperation(
      self,
      operation: CompositeOperation,
  ) -> None:
    """
    Calls Qt's 'void
    QCanvasPainter::setGlobalCompositeOperation(CompositeOperation
    operation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainter.html#setGlobalCompositeOperation

    Parameters
    ----------

    operation : CompositeOperation
      Passed on as its number.
    """
    #  void QCanvasPainter::setGlobalCompositeOperation(CompositeOperation
    #      operation)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter27setGlobalCompositeOperationENS_18Compos'
        'iteOperationE',
        operation.value,
    )

  @overload(float)
  def setGlobalBrightness(self, value: float) -> None:
    """
    Calls Qt's 'void QCanvasPainter::setGlobalBrightness(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainter.html#setGlobalBrightness

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QCanvasPainter::setGlobalBrightness(qreal value)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter19setGlobalBrightnessEd', value,
    )

  @overload(float)
  def setGlobalContrast(self, value: float) -> None:
    """
    Calls Qt's 'void QCanvasPainter::setGlobalContrast(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainter.html#setGlobalContrast

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QCanvasPainter::setGlobalContrast(qreal value)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter17setGlobalContrastEd', value,
    )

  @overload(float)
  def setGlobalSaturation(self, value: float) -> None:
    """
    Calls Qt's 'void QCanvasPainter::setGlobalSaturation(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainter.html#setGlobalSaturation

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QCanvasPainter::setGlobalSaturation(qreal value)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter19setGlobalSaturationEd', value,
    )

  @overload(FillRule)
  def setFillRule(self, fillRule: FillRule) -> None:
    """
    Calls Qt's 'void QCanvasPainter::setFillRule(FillRule fillRule)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#setFillRule

    Parameters
    ----------

    fillRule : FillRule
      Passed on as its number.
    """
    #  void QCanvasPainter::setFillRule(FillRule fillRule)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter11setFillRuleENS_8FillRuleE',
        fillRule.value,
    )

  @overload(QTransform)
  def setTransform(self, transform: QTransform) -> None:
    """
    Calls Qt's 'void QCanvasPainter::setTransform(const QTransform
    &transform)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#setTransform

    Parameters
    ----------

    transform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  void QCanvasPainter::setTransform(const QTransform &transform)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter12setTransformERK10QTransform',
        self._valueOf(transform),
    )

  @overload(float, float, float, float)
  def setClipRect(
      self,
      x: float,
      y: float,
      width: float,
      height: float,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPainter::setClipRect(qreal x, qreal y, qreal
    width, qreal height)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#setClipRect

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
    #  void QCanvasPainter::setClipRect(qreal x, qreal y, qreal width, qreal
    #      height)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter11setClipRectEdddd', x, y, width, height,
    )

  @overload(QRectF)
  def setClipRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QCanvasPainter::setClipRect(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#setClipRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QCanvasPainter::setClipRect(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter11setClipRectERK6QRectF',
        self._valueOf(rect),
    )

  @overload(PathWinding)
  def setPathWinding(self, winding: PathWinding) -> None:
    """
    Calls Qt's 'void QCanvasPainter::setPathWinding(PathWinding winding)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#setPathWinding

    Parameters
    ----------

    winding : PathWinding
      Passed on as its number.
    """
    #  void QCanvasPainter::setPathWinding(PathWinding winding)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter14setPathWindingENS_11PathWindingE',
        winding.value,
    )

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QCanvasPainter::setFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QCanvasPainter::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter7setFontERK5QFont', self._valueOf(font),
    )

  @overload(TextAlign)
  def setTextAlign(self, align: TextAlign) -> None:
    """
    Calls Qt's 'void QCanvasPainter::setTextAlign(QCanvasPainter::TextAlign
    align)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#setTextAlign

    Parameters
    ----------

    align : TextAlign
      Passed on as its number.
    """
    #  void QCanvasPainter::setTextAlign(QCanvasPainter::TextAlign align)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter12setTextAlignENS_9TextAlignE',
        align.value,
    )

  @overload(TextBaseline)
  def setTextBaseline(self, baseline: TextBaseline) -> None:
    """
    Calls Qt's 'void
    QCanvasPainter::setTextBaseline(QCanvasPainter::TextBaseline baseline)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainter.html#setTextBaseline

    Parameters
    ----------

    baseline : TextBaseline
      Passed on as its number.
    """
    #  void QCanvasPainter::setTextBaseline(QCanvasPainter::TextBaseline
    #      baseline)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter15setTextBaselineENS_12TextBaselineE',
        baseline.value,
    )

  @overload(TextDirection)
  def setTextDirection(self, direction: TextDirection) -> None:
    """
    Calls Qt's 'void
    QCanvasPainter::setTextDirection(QCanvasPainter::TextDirection
    direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainter.html#setTextDirection

    Parameters
    ----------

    direction : TextDirection
      Passed on as its number.
    """
    #  void QCanvasPainter::setTextDirection(QCanvasPainter::TextDirection
    #      direction)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter16setTextDirectionENS_13TextDirectionE',
        direction.value,
    )

  @overload(WrapMode)
  def setTextWrapMode(self, wrapMode: WrapMode) -> None:
    """
    Calls Qt's 'void QCanvasPainter::setTextWrapMode(QCanvasPainter::WrapMode
    wrapMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainter.html#setTextWrapMode

    Parameters
    ----------

    wrapMode : WrapMode
      Passed on as its number.
    """
    #  void QCanvasPainter::setTextWrapMode(QCanvasPainter::WrapMode
    #      wrapMode)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter15setTextWrapModeENS_8WrapModeE',
        wrapMode.value,
    )

  @overload(float)
  def setTextLineHeight(self, height: float) -> None:
    """
    Calls Qt's 'void QCanvasPainter::setTextLineHeight(qreal height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainter.html#setTextLineHeight

    Parameters
    ----------

    height : float
      Passed on as it is.
    """
    #  void QCanvasPainter::setTextLineHeight(qreal height)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter17setTextLineHeightEd', height,
    )

  @overload(float)
  def setTextAntialias(self, antialias: float) -> None:
    """
    Calls Qt's 'void QCanvasPainter::setTextAntialias(qreal antialias)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainter.html#setTextAntialias

    Parameters
    ----------

    antialias : float
      Passed on as it is.
    """
    #  void QCanvasPainter::setTextAntialias(qreal antialias)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter16setTextAntialiasEd', antialias,
    )

  @overload(float)
  def setAntialias(self, antialias: float) -> None:
    """
    Calls Qt's 'void QCanvasPainter::setAntialias(qreal antialias)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#setAntialias

    Parameters
    ----------

    antialias : float
      Passed on as it is.
    """
    #  void QCanvasPainter::setAntialias(qreal antialias)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter12setAntialiasEd', antialias,
    )

  @overload(bool)
  def setWindingEnforce(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QCanvasPainter::setWindingEnforce(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainter.html#setWindingEnforce

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QCanvasPainter::setWindingEnforce(bool enabled)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter17setWindingEnforceEb', enabled,
    )

  @overload(bool)
  def setHighQualityStroking(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QCanvasPainter::setHighQualityStroking(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainter.html#setHighQualityStroking

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QCanvasPainter::setHighQualityStroking(bool enabled)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter22setHighQualityStrokingEb', enabled,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QCanvasPainter::QCanvasPainter()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#QCanvasPainter
    """
    #  QCanvasPainter::QCanvasPainter()
    self._noteCreation(QCanvasPainter, lambda: Rituals.call(
        'ritual_ZN14QCanvasPainterC1Ev',
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

  def save(self) -> None:
    """
    Calls Qt's 'void QCanvasPainter::save()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#save
    """
    #  void QCanvasPainter::save()
    self.uglySide.call('ritual_ZN14QCanvasPainter4saveEv')

  def restore(self) -> None:
    """
    Calls Qt's 'void QCanvasPainter::restore()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#restore
    """
    #  void QCanvasPainter::restore()
    self.uglySide.call('ritual_ZN14QCanvasPainter7restoreEv')

  def reset(self) -> None:
    """
    Calls Qt's 'void QCanvasPainter::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#reset
    """
    #  void QCanvasPainter::reset()
    self.uglySide.call('ritual_ZN14QCanvasPainter5resetEv')

  def resetTransform(self) -> None:
    """
    Calls Qt's 'void QCanvasPainter::resetTransform()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#resetTransform
    """
    #  void QCanvasPainter::resetTransform()
    self.uglySide.call('ritual_ZN14QCanvasPainter14resetTransformEv')

  @overload(QTransform)
  def transform(self, transform: QTransform) -> None:
    """
    Calls Qt's 'void QCanvasPainter::transform(const QTransform &transform)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#transform

    Parameters
    ----------

    transform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  void QCanvasPainter::transform(const QTransform &transform)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter9transformERK10QTransform',
        self._valueOf(transform),
    )

  @overload(float, float)
  def translate(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QCanvasPainter::translate(qreal x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#translate

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QCanvasPainter::translate(qreal x, qreal y)
    self.uglySide.call('ritual_ZN14QCanvasPainter9translateEdd', x, y)

  @overload(QPointF)
  def translate(self, point: QPointF) -> None:
    """
    Calls Qt's 'void QCanvasPainter::translate(QPointF point)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#translate

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QCanvasPainter::translate(QPointF point)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter9translateE7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(float)
  def rotate(self, angle: float) -> None:
    """
    Calls Qt's 'void QCanvasPainter::rotate(qreal angle)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#rotate

    Parameters
    ----------

    angle : float
      Passed on as it is.
    """
    #  void QCanvasPainter::rotate(qreal angle)
    self.uglySide.call('ritual_ZN14QCanvasPainter6rotateEd', angle)

  @overload(float)
  @overload(float, float)
  def skew(self, angleX: float, angleY: float = 0.0) -> None:
    """
    Calls Qt's 'void QCanvasPainter::skew(qreal angleX, qreal angleY)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#skew

    Parameters
    ----------

    angleX : float
      Passed on as it is.

    angleY : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  void QCanvasPainter::skew(qreal angleX, qreal angleY)
    self.uglySide.call('ritual_ZN14QCanvasPainter4skewEdd', angleX, angleY)

  @overload(float)
  def scale(self, scale: float) -> None:
    """
    Calls Qt's 'void QCanvasPainter::scale(qreal scale)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#scale

    Parameters
    ----------

    scale : float
      Passed on as it is.
    """
    #  void QCanvasPainter::scale(qreal scale)
    self.uglySide.call('ritual_ZN14QCanvasPainter5scaleEd', scale)

  @overload(float, float)
  def scale(self, scaleX: float, scaleY: float) -> None:
    """
    Calls Qt's 'void QCanvasPainter::scale(qreal scaleX, qreal scaleY)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#scale

    Parameters
    ----------

    scaleX : float
      Passed on as it is.

    scaleY : float
      Passed on as it is.
    """
    #  void QCanvasPainter::scale(qreal scaleX, qreal scaleY)
    self.uglySide.call('ritual_ZN14QCanvasPainter5scaleEdd', scaleX, scaleY)

  def resetClipping(self) -> None:
    """
    Calls Qt's 'void QCanvasPainter::resetClipping()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#resetClipping
    """
    #  void QCanvasPainter::resetClipping()
    self.uglySide.call('ritual_ZN14QCanvasPainter13resetClippingEv')

  def beginPath(self) -> None:
    """
    Calls Qt's 'void QCanvasPainter::beginPath()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#beginPath
    """
    #  void QCanvasPainter::beginPath()
    self.uglySide.call('ritual_ZN14QCanvasPainter9beginPathEv')

  def closePath(self) -> None:
    """
    Calls Qt's 'void QCanvasPainter::closePath()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#closePath
    """
    #  void QCanvasPainter::closePath()
    self.uglySide.call('ritual_ZN14QCanvasPainter9closePathEv')

  @overload(float, float)
  def moveTo(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QCanvasPainter::moveTo(qreal x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#moveTo

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QCanvasPainter::moveTo(qreal x, qreal y)
    self.uglySide.call('ritual_ZN14QCanvasPainter6moveToEdd', x, y)

  @overload(QPointF)
  def moveTo(self, point: QPointF) -> None:
    """
    Calls Qt's 'void QCanvasPainter::moveTo(QPointF point)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#moveTo

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QCanvasPainter::moveTo(QPointF point)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter6moveToE7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(float, float)
  def lineTo(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QCanvasPainter::lineTo(qreal x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#lineTo

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QCanvasPainter::lineTo(qreal x, qreal y)
    self.uglySide.call('ritual_ZN14QCanvasPainter6lineToEdd', x, y)

  @overload(QPointF)
  def lineTo(self, point: QPointF) -> None:
    """
    Calls Qt's 'void QCanvasPainter::lineTo(QPointF point)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#lineTo

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QCanvasPainter::lineTo(QPointF point)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter6lineToE7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(float, float, float, float, float, float)
  def bezierCurveTo(
      self,
      cp1X: float,
      cp1Y: float,
      cp2X: float,
      cp2Y: float,
      x: float,
      y: float,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPainter::bezierCurveTo(qreal cp1X, qreal cp1Y,
    qreal cp2X, qreal cp2Y, qreal x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#bezierCurveTo

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
    #  void QCanvasPainter::bezierCurveTo(qreal cp1X, qreal cp1Y, qreal cp2X,
    #      qreal cp2Y, qreal x, qreal y)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter13bezierCurveToEdddddd',
        cp1X, cp1Y, cp2X, cp2Y, x, y,
    )

  @overload(QPointF, QPointF, QPointF)
  def bezierCurveTo(
      self,
      controlPoint1: QPointF,
      controlPoint2: QPointF,
      endPoint: QPointF,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPainter::bezierCurveTo(QPointF controlPoint1,
    QPointF controlPoint2, QPointF endPoint)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#bezierCurveTo

    Parameters
    ----------

    controlPoint1 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    controlPoint2 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    endPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QCanvasPainter::bezierCurveTo(QPointF controlPoint1, QPointF
    #      controlPoint2, QPointF endPoint)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter13bezierCurveToE7QPointFS0_S0_',
        self._valueOf(controlPoint1, 'QPointF'), self._valueOf(controlPoint2,
        'QPointF'), self._valueOf(endPoint, 'QPointF'),
    )

  @overload(float, float, float, float)
  def quadraticCurveTo(
      self,
      cpX: float,
      cpY: float,
      x: float,
      y: float,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPainter::quadraticCurveTo(qreal cpX, qreal cpY,
    qreal x, qreal y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainter.html#quadraticCurveTo

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
    #  void QCanvasPainter::quadraticCurveTo(qreal cpX, qreal cpY, qreal x,
    #      qreal y)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter16quadraticCurveToEdddd', cpX, cpY, x, y,
    )

  @overload(QPointF, QPointF)
  def quadraticCurveTo(
      self,
      controlPoint: QPointF,
      endPoint: QPointF,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPainter::quadraticCurveTo(QPointF controlPoint,
    QPointF endPoint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainter.html#quadraticCurveTo

    Parameters
    ----------

    controlPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    endPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QCanvasPainter::quadraticCurveTo(QPointF controlPoint, QPointF
    #      endPoint)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter16quadraticCurveToE7QPointFS0_',
        self._valueOf(controlPoint, 'QPointF'), self._valueOf(endPoint,
        'QPointF'),
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
    Calls Qt's 'void QCanvasPainter::arcTo(qreal x1, qreal y1, qreal x2,
    qreal y2, qreal radius)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#arcTo

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
    #  void QCanvasPainter::arcTo(qreal x1, qreal y1, qreal x2, qreal y2,
    #      qreal radius)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter5arcToEddddd', x1, y1, x2, y2, radius,
    )

  @overload(QPointF, QPointF, float)
  def arcTo(
      self,
      controlPoint1: QPointF,
      controlPoint2: QPointF,
      radius: float,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPainter::arcTo(QPointF controlPoint1, QPointF
    controlPoint2, qreal radius)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#arcTo

    Parameters
    ----------

    controlPoint1 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    controlPoint2 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    radius : float
      Passed on as it is.
    """
    #  void QCanvasPainter::arcTo(QPointF controlPoint1, QPointF
    #      controlPoint2, qreal radius)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter5arcToE7QPointFS0_d',
        self._valueOf(controlPoint1, 'QPointF'), self._valueOf(controlPoint2,
        'QPointF'), radius,
    )

  @overload(float, float, float, float, float)
  @overload(float, float, float, float, float, PathWinding)
  @overload(float, float, float, float, float, PathWinding, PathConnection)
  def arc(
      self,
      centerX: float,
      centerY: float,
      radius: float,
      a0: float,
      a1: float,
      direction: PathWinding = PathWinding.ClockWise,
      connection: PathConnection = PathConnection.Connected,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPainter::arc(qreal centerX, qreal centerY, qreal
    radius, qreal a0, qreal a1, PathWinding direction, PathConnection
    connection)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#arc

    Parameters
    ----------

    centerX : float
      Passed on as it is.

    centerY : float
      Passed on as it is.

    radius : float
      Passed on as it is.

    a0 : float
      Passed on as it is.

    a1 : float
      Passed on as it is.

    direction : PathWinding
      Passed on as its number. May be left out, as in Qt: it is then
      PathWinding.ClockWise.

    connection : PathConnection
      Passed on as its number. May be left out, as in Qt: it is then
      PathConnection.Connected.
    """
    #  void QCanvasPainter::arc(qreal centerX, qreal centerY, qreal radius,
    #      qreal a0, qreal a1, PathWinding direction, PathConnection
    #      connection)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter3arcEdddddNS_11PathWindingENS_14PathConne'
        'ctionE',
        centerX, centerY, radius, a0, a1, direction.value, connection.value,
    )

  @overload(QPointF, float, float, float)
  @overload(QPointF, float, float, float, PathWinding)
  @overload(QPointF, float, float, float, PathWinding, PathConnection)
  def arc(
      self,
      centerPoint: QPointF,
      radius: float,
      a0: float,
      a1: float,
      direction: PathWinding = PathWinding.ClockWise,
      connection: PathConnection = PathConnection.Connected,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPainter::arc(QPointF centerPoint, qreal radius,
    qreal a0, qreal a1, PathWinding direction, PathConnection connection)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#arc

    Parameters
    ----------

    centerPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    radius : float
      Passed on as it is.

    a0 : float
      Passed on as it is.

    a1 : float
      Passed on as it is.

    direction : PathWinding
      Passed on as its number. May be left out, as in Qt: it is then
      PathWinding.ClockWise.

    connection : PathConnection
      Passed on as its number. May be left out, as in Qt: it is then
      PathConnection.Connected.
    """
    #  void QCanvasPainter::arc(QPointF centerPoint, qreal radius, qreal a0,
    #      qreal a1, PathWinding direction, PathConnection connection)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter3arcE7QPointFdddNS_11PathWindingENS_14Pat'
        'hConnectionE',
        self._valueOf(centerPoint, 'QPointF'), radius, a0, a1,
        direction.value, connection.value,
    )

  @overload(float, float, float, float)
  def rect(self, x: float, y: float, width: float, height: float) -> None:
    """
    Calls Qt's 'void QCanvasPainter::rect(qreal x, qreal y, qreal width,
    qreal height)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#rect

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
    #  void QCanvasPainter::rect(qreal x, qreal y, qreal width, qreal height)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter4rectEdddd', x, y, width, height,
    )

  @overload(QRectF)
  def rect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QCanvasPainter::rect(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#rect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QCanvasPainter::rect(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter4rectERK6QRectF', self._valueOf(rect),
    )

  @overload(float, float, float, float, float)
  def roundRect(
      self,
      x: float,
      y: float,
      width: float,
      height: float,
      radius: float,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPainter::roundRect(qreal x, qreal y, qreal width,
    qreal height, qreal radius)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#roundRect

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
    #  void QCanvasPainter::roundRect(qreal x, qreal y, qreal width, qreal
    #      height, qreal radius)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter9roundRectEddddd',
        x, y, width, height, radius,
    )

  @overload(QRectF, float)
  def roundRect(self, rect: QRectF, radius: float) -> None:
    """
    Calls Qt's 'void QCanvasPainter::roundRect(const QRectF &rect, qreal
    radius)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#roundRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    radius : float
      Passed on as it is.
    """
    #  void QCanvasPainter::roundRect(const QRectF &rect, qreal radius)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter9roundRectERK6QRectFd',
        self._valueOf(rect), radius,
    )

  @overload(float, float, float, float, float, float, float, float)
  def roundRect(
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
    Calls Qt's 'void QCanvasPainter::roundRect(qreal x, qreal y, qreal width,
    qreal height, qreal radiusTopLeft, qreal radiusTopRight, qreal
    radiusBottomRight, qreal radiusBottomLeft)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#roundRect

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
    #  void QCanvasPainter::roundRect(qreal x, qreal y, qreal width, qreal
    #      height, qreal radiusTopLeft, qreal radiusTopRight, qreal
    #      radiusBottomRight, qreal radiusBottomLeft)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter9roundRectEdddddddd',
        x, y, width, height, radiusTopLeft, radiusTopRight,
        radiusBottomRight, radiusBottomLeft,
    )

  @overload(QRectF, float, float, float, float)
  def roundRect(
      self,
      rect: QRectF,
      radiusTopLeft: float,
      radiusTopRight: float,
      radiusBottomRight: float,
      radiusBottomLeft: float,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPainter::roundRect(const QRectF &rect, qreal
    radiusTopLeft, qreal radiusTopRight, qreal radiusBottomRight, qreal
    radiusBottomLeft)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#roundRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    radiusTopLeft : float
      Passed on as it is.

    radiusTopRight : float
      Passed on as it is.

    radiusBottomRight : float
      Passed on as it is.

    radiusBottomLeft : float
      Passed on as it is.
    """
    #  void QCanvasPainter::roundRect(const QRectF &rect, qreal
    #      radiusTopLeft, qreal radiusTopRight, qreal radiusBottomRight,
    #      qreal radiusBottomLeft)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter9roundRectERK6QRectFdddd',
        self._valueOf(rect), radiusTopLeft, radiusTopRight,
        radiusBottomRight, radiusBottomLeft,
    )

  @overload(float, float, float, float)
  def ellipse(
      self,
      centerX: float,
      centerY: float,
      radiusX: float,
      radiusY: float,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPainter::ellipse(qreal centerX, qreal centerY,
    qreal radiusX, qreal radiusY)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#ellipse

    Parameters
    ----------

    centerX : float
      Passed on as it is.

    centerY : float
      Passed on as it is.

    radiusX : float
      Passed on as it is.

    radiusY : float
      Passed on as it is.
    """
    #  void QCanvasPainter::ellipse(qreal centerX, qreal centerY, qreal
    #      radiusX, qreal radiusY)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter7ellipseEdddd',
        centerX, centerY, radiusX, radiusY,
    )

  @overload(QPointF, float, float)
  def ellipse(
      self,
      centerPoint: QPointF,
      radiusX: float,
      radiusY: float,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPainter::ellipse(QPointF centerPoint, qreal
    radiusX, qreal radiusY)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#ellipse

    Parameters
    ----------

    centerPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    radiusX : float
      Passed on as it is.

    radiusY : float
      Passed on as it is.
    """
    #  void QCanvasPainter::ellipse(QPointF centerPoint, qreal radiusX, qreal
    #      radiusY)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter7ellipseE7QPointFdd',
        self._valueOf(centerPoint, 'QPointF'), radiusX, radiusY,
    )

  @overload(QRectF)
  def ellipse(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QCanvasPainter::ellipse(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#ellipse

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QCanvasPainter::ellipse(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter7ellipseERK6QRectF', self._valueOf(rect),
    )

  @overload(float, float, float)
  def circle(self, centerX: float, centerY: float, radius: float) -> None:
    """
    Calls Qt's 'void QCanvasPainter::circle(qreal centerX, qreal centerY,
    qreal radius)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#circle

    Parameters
    ----------

    centerX : float
      Passed on as it is.

    centerY : float
      Passed on as it is.

    radius : float
      Passed on as it is.
    """
    #  void QCanvasPainter::circle(qreal centerX, qreal centerY, qreal
    #      radius)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter6circleEddd', centerX, centerY, radius,
    )

  @overload(QPointF, float)
  def circle(self, centerPoint: QPointF, radius: float) -> None:
    """
    Calls Qt's 'void QCanvasPainter::circle(QPointF centerPoint, qreal
    radius)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#circle

    Parameters
    ----------

    centerPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    radius : float
      Passed on as it is.
    """
    #  void QCanvasPainter::circle(QPointF centerPoint, qreal radius)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter6circleE7QPointFd',
        self._valueOf(centerPoint, 'QPointF'), radius,
    )

  @overload(QPainterPath)
  def addPath(self, path: QPainterPath) -> None:
    """
    Calls Qt's 'void QCanvasPainter::addPath(const QPainterPath &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#addPath

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.
    """
    #  void QCanvasPainter::addPath(const QPainterPath &path)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter7addPathERK12QPainterPath',
        self._valueOf(path),
    )

  @overload(QCanvasPath)
  @overload(QCanvasPath, QTransform)
  def addPath(
      self,
      path: QCanvasPath,
      transform: Optional[QTransform] = None,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPainter::addPath(const QCanvasPath &path, const
    QTransform &transform)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#addPath

    Parameters
    ----------

    path : QCanvasPath
      Passed on as a value: Qt reads the C++ QCanvasPath, which stays
      Python's own.

    transform : Optional[QTransform]
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own. May be left out, as in Qt: a new 'QTransform()' is then passed on.
    """
    #  void QCanvasPainter::addPath(const QCanvasPath &path, const QTransform
    #      &transform)
    if transform is None:
      from ..QtGui import QTransform
      transform = QTransform()
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter7addPathERK11QCanvasPathRK10QTransform',
        self._valueOf(path), self._valueOf(transform),
    )

  @overload(QCanvasPath, int, int)
  @overload(QCanvasPath, int, int, QTransform)
  def addPath(
      self,
      path: QCanvasPath,
      start: int,
      count: int,
      transform: Optional[QTransform] = None,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPainter::addPath(const QCanvasPath &path,
    qsizetype start, qsizetype count, const QTransform &transform)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#addPath

    Parameters
    ----------

    path : QCanvasPath
      Passed on as a value: Qt reads the C++ QCanvasPath, which stays
      Python's own.

    start : int
      Passed on as it is.

    count : int
      Passed on as it is.

    transform : Optional[QTransform]
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own. May be left out, as in Qt: a new 'QTransform()' is then passed on.
    """
    #  void QCanvasPainter::addPath(const QCanvasPath &path, qsizetype start,
    #      qsizetype count, const QTransform &transform)
    if transform is None:
      from ..QtGui import QTransform
      transform = QTransform()
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter7addPathERK11QCanvasPathxxRK10QTransform',
        self._valueOf(path), start, count, self._valueOf(transform),
    )

  def beginSolidSubPath(self) -> None:
    """
    Calls Qt's 'void QCanvasPainter::beginSolidSubPath()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainter.html#beginSolidSubPath
    """
    #  void QCanvasPainter::beginSolidSubPath()
    self.uglySide.call('ritual_ZN14QCanvasPainter17beginSolidSubPathEv')

  def beginHoleSubPath(self) -> None:
    """
    Calls Qt's 'void QCanvasPainter::beginHoleSubPath()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainter.html#beginHoleSubPath
    """
    #  void QCanvasPainter::beginHoleSubPath()
    self.uglySide.call('ritual_ZN14QCanvasPainter16beginHoleSubPathEv')

  @overload()
  def fill(self) -> None:
    """
    Calls Qt's 'void QCanvasPainter::fill()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#fill
    """
    #  void QCanvasPainter::fill()
    self.uglySide.call('ritual_ZN14QCanvasPainter4fillEv')

  @overload(FillRule)
  def fill(self, fillRule: FillRule) -> None:
    """
    Calls Qt's 'void QCanvasPainter::fill(FillRule fillRule)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#fill

    Parameters
    ----------

    fillRule : FillRule
      Passed on as its number.
    """
    #  void QCanvasPainter::fill(FillRule fillRule)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter4fillENS_8FillRuleE', fillRule.value,
    )

  @overload(QCanvasPath)
  @overload(QCanvasPath, int)
  def fill(self, path: QCanvasPath, pathGroup: int = -1) -> None:
    """
    Calls Qt's 'void QCanvasPainter::fill(const QCanvasPath &path, int
    pathGroup)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#fill

    Parameters
    ----------

    path : QCanvasPath
      Passed on as a value: Qt reads the C++ QCanvasPath, which stays
      Python's own.

    pathGroup : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void QCanvasPainter::fill(const QCanvasPath &path, int pathGroup)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter4fillERK11QCanvasPathi',
        self._valueOf(path), pathGroup,
    )

  @overload(QCanvasPath, FillRule)
  @overload(QCanvasPath, FillRule, int)
  def fill(
      self,
      path: QCanvasPath,
      fillRule: FillRule,
      pathGroup: int = -1,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPainter::fill(const QCanvasPath &path, FillRule
    fillRule, int pathGroup)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#fill

    Parameters
    ----------

    path : QCanvasPath
      Passed on as a value: Qt reads the C++ QCanvasPath, which stays
      Python's own.

    fillRule : FillRule
      Passed on as its number.

    pathGroup : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void QCanvasPainter::fill(const QCanvasPath &path, FillRule fillRule,
    #      int pathGroup)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter4fillERK11QCanvasPathNS_8FillRuleEi',
        self._valueOf(path), fillRule.value, pathGroup,
    )

  @overload()
  def stroke(self) -> None:
    """
    Calls Qt's 'void QCanvasPainter::stroke()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#stroke
    """
    #  void QCanvasPainter::stroke()
    self.uglySide.call('ritual_ZN14QCanvasPainter6strokeEv')

  @overload(QCanvasPath)
  @overload(QCanvasPath, int)
  def stroke(self, path: QCanvasPath, pathGroup: int = -1) -> None:
    """
    Calls Qt's 'void QCanvasPainter::stroke(const QCanvasPath &path, int
    pathGroup)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#stroke

    Parameters
    ----------

    path : QCanvasPath
      Passed on as a value: Qt reads the C++ QCanvasPath, which stays
      Python's own.

    pathGroup : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void QCanvasPainter::stroke(const QCanvasPath &path, int pathGroup)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter6strokeERK11QCanvasPathi',
        self._valueOf(path), pathGroup,
    )

  @overload(float, float, float, float)
  def fillRect(
      self,
      x: float,
      y: float,
      width: float,
      height: float,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPainter::fillRect(qreal x, qreal y, qreal width,
    qreal height)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#fillRect

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
    #  void QCanvasPainter::fillRect(qreal x, qreal y, qreal width, qreal
    #      height)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter8fillRectEdddd', x, y, width, height,
    )

  @overload(QRectF)
  def fillRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QCanvasPainter::fillRect(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#fillRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QCanvasPainter::fillRect(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter8fillRectERK6QRectF', self._valueOf(rect),
    )

  @overload(float, float, float, float)
  def clearRect(
      self,
      x: float,
      y: float,
      width: float,
      height: float,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPainter::clearRect(qreal x, qreal y, qreal width,
    qreal height)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#clearRect

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
    #  void QCanvasPainter::clearRect(qreal x, qreal y, qreal width, qreal
    #      height)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter9clearRectEdddd', x, y, width, height,
    )

  @overload(QRectF)
  def clearRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QCanvasPainter::clearRect(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#clearRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QCanvasPainter::clearRect(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter9clearRectERK6QRectF', self._valueOf(rect),
    )

  @overload(float, float, float, float)
  def strokeRect(
      self,
      x: float,
      y: float,
      width: float,
      height: float,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPainter::strokeRect(qreal x, qreal y, qreal
    width, qreal height)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#strokeRect

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
    #  void QCanvasPainter::strokeRect(qreal x, qreal y, qreal width, qreal
    #      height)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter10strokeRectEdddd', x, y, width, height,
    )

  @overload(QRectF)
  def strokeRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QCanvasPainter::strokeRect(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#strokeRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QCanvasPainter::strokeRect(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter10strokeRectERK6QRectF',
        self._valueOf(rect),
    )

  @overload(QCanvasBoxShadow)
  def drawBoxShadow(self, shadow: QCanvasBoxShadow) -> None:
    """
    Calls Qt's 'void QCanvasPainter::drawBoxShadow(const QCanvasBoxShadow
    &shadow)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#drawBoxShadow

    Parameters
    ----------

    shadow : QCanvasBoxShadow
      Passed on as a value: Qt reads the C++ QCanvasBoxShadow, which stays
      Python's own.
    """
    #  void QCanvasPainter::drawBoxShadow(const QCanvasBoxShadow &shadow)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter13drawBoxShadowERK16QCanvasBoxShadow',
        self._valueOf(shadow),
    )

  @overload(QCanvasImage, float, float)
  def drawImage(self, image: QCanvasImage, x: float, y: float) -> None:
    """
    Calls Qt's 'void QCanvasPainter::drawImage(const QCanvasImage &image,
    qreal x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#drawImage

    Parameters
    ----------

    image : QCanvasImage
      Passed on as a value: Qt reads the C++ QCanvasImage, which stays
      Python's own.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QCanvasPainter::drawImage(const QCanvasImage &image, qreal x,
    #      qreal y)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter9drawImageERK12QCanvasImagedd',
        self._valueOf(image), x, y,
    )

  @overload(QCanvasImage, float, float, float, float)
  def drawImage(
      self,
      image: QCanvasImage,
      x: float,
      y: float,
      width: float,
      height: float,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPainter::drawImage(const QCanvasImage &image,
    qreal x, qreal y, qreal width, qreal height)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#drawImage

    Parameters
    ----------

    image : QCanvasImage
      Passed on as a value: Qt reads the C++ QCanvasImage, which stays
      Python's own.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    width : float
      Passed on as it is.

    height : float
      Passed on as it is.
    """
    #  void QCanvasPainter::drawImage(const QCanvasImage &image, qreal x,
    #      qreal y, qreal width, qreal height)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter9drawImageERK12QCanvasImagedddd',
        self._valueOf(image), x, y, width, height,
    )

  @overload(QCanvasImage, QRectF)
  def drawImage(self, image: QCanvasImage, destinationRect: QRectF) -> None:
    """
    Calls Qt's 'void QCanvasPainter::drawImage(const QCanvasImage &image,
    const QRectF &destinationRect)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#drawImage

    Parameters
    ----------

    image : QCanvasImage
      Passed on as a value: Qt reads the C++ QCanvasImage, which stays
      Python's own.

    destinationRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QCanvasPainter::drawImage(const QCanvasImage &image, const QRectF
    #      &destinationRect)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter9drawImageERK12QCanvasImageRK6QRectF',
        self._valueOf(image), self._valueOf(destinationRect),
    )

  @overload(QCanvasImage, QRectF, QRectF)
  def drawImage(
      self,
      image: QCanvasImage,
      sourceRect: QRectF,
      destinationRect: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPainter::drawImage(const QCanvasImage &image,
    const QRectF &sourceRect, const QRectF &destinationRect)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#drawImage

    Parameters
    ----------

    image : QCanvasImage
      Passed on as a value: Qt reads the C++ QCanvasImage, which stays
      Python's own.

    sourceRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    destinationRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QCanvasPainter::drawImage(const QCanvasImage &image, const QRectF
    #      &sourceRect, const QRectF &destinationRect)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter9drawImageERK12QCanvasImageRK6QRectFS5_',
        self._valueOf(image), self._valueOf(sourceRect),
        self._valueOf(destinationRect),
    )

  @overload(str, float, float)
  @overload(str, float, float, float)
  def fillText(
      self,
      text: str,
      x: float,
      y: float,
      maxWidth: float = 0.0,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPainter::fillText(const QString &text, qreal x,
    qreal y, qreal maxWidth)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#fillText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    maxWidth : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  void QCanvasPainter::fillText(const QString &text, qreal x, qreal y,
    #      qreal maxWidth)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter8fillTextERK7QStringddd',
        text, x, y, maxWidth,
    )

  @overload(str, QPointF)
  @overload(str, QPointF, float)
  def fillText(
      self,
      text: str,
      point: QPointF,
      maxWidth: float = 0.0,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPainter::fillText(const QString &text, QPointF
    point, qreal maxWidth)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#fillText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    maxWidth : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  void QCanvasPainter::fillText(const QString &text, QPointF point,
    #      qreal maxWidth)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter8fillTextERK7QString7QPointFd',
        text, self._valueOf(point, 'QPointF'), maxWidth,
    )

  @overload(str, QRectF)
  def fillText(self, text: str, rect: QRectF) -> None:
    """
    Calls Qt's 'void QCanvasPainter::fillText(const QString &text, const
    QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#fillText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QCanvasPainter::fillText(const QString &text, const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter8fillTextERK7QStringRK6QRectF',
        text, self._valueOf(rect),
    )

  @overload(QImage)
  @overload(QImage, ImageFlags)
  def addImage(
      self,
      image: QImage,
      flags: ImageFlags = ImageFlags(),
  ) -> QCanvasImage:
    """
    Calls Qt's 'QCanvasImage QCanvasPainter::addImage(const QImage &image,
    QCanvasPainter::ImageFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#addImage

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    flags : ImageFlags
      Passed on as its number. May be left out, as in Qt: it is then
      ImageFlags().

    Returns
    -------

    QCanvasImage
      A new cute QCanvasImage around the copy Qt gave back. Python owns it.
    """
    #  QCanvasImage QCanvasPainter::addImage(const QImage &image,
    #      QCanvasPainter::ImageFlags flags)
    address = self.uglySide.call(
        'ritual_ZN14QCanvasPainter8addImageERK6QImage6QFlagsINS_9ImageFlagE'
        'E',
        self._valueOf(image), flags.value,
    )
    from . import QCanvasImage
    return QCanvasImage._cuteOwning(address)

  @overload(QRhiTexture)
  @overload(NoneType)
  @overload(QRhiTexture, ImageFlags)
  @overload(NoneType, ImageFlags)
  def addImage(
      self,
      texture: Optional[QRhiTexture],
      flags: ImageFlags = ImageFlags(),
  ) -> QCanvasImage:
    """
    Calls Qt's 'QCanvasImage QCanvasPainter::addImage(QRhiTexture *texture,
    QCanvasPainter::ImageFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#addImage

    Parameters
    ----------

    texture : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : ImageFlags
      Passed on as its number. May be left out, as in Qt: it is then
      ImageFlags().

    Returns
    -------

    QCanvasImage
      A new cute QCanvasImage around the copy Qt gave back. Python owns it.
    """
    #  QCanvasImage QCanvasPainter::addImage(QRhiTexture *texture,
    #      QCanvasPainter::ImageFlags flags)
    address = self.uglySide.call(
        'ritual_ZN14QCanvasPainter8addImageEP11QRhiTexture6QFlagsINS_9Image'
        'FlagEE',
        self._addressOf(texture), flags.value,
    )
    from . import QCanvasImage
    return QCanvasImage._cuteOwning(address)

  @overload(QCanvasOffscreenCanvas)
  @overload(QCanvasOffscreenCanvas, ImageFlags)
  def addImage(
      self,
      canvas: QCanvasOffscreenCanvas,
      flags: ImageFlags = ImageFlags(),
  ) -> QCanvasImage:
    """
    Calls Qt's 'QCanvasImage QCanvasPainter::addImage(const
    QCanvasOffscreenCanvas &canvas, QCanvasPainter::ImageFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#addImage

    Parameters
    ----------

    canvas : QCanvasOffscreenCanvas
      Passed on as a value: Qt reads the C++ QCanvasOffscreenCanvas, which
      stays Python's own.

    flags : ImageFlags
      Passed on as its number. May be left out, as in Qt: it is then
      ImageFlags().

    Returns
    -------

    QCanvasImage
      A new cute QCanvasImage around the copy Qt gave back. Python owns it.
    """
    #  QCanvasImage QCanvasPainter::addImage(const QCanvasOffscreenCanvas
    #      &canvas, QCanvasPainter::ImageFlags flags)
    address = self.uglySide.call(
        'ritual_ZN14QCanvasPainter8addImageERK22QCanvasOffscreenCanvas6QFla'
        'gsINS_9ImageFlagEE',
        self._valueOf(canvas), flags.value,
    )
    from . import QCanvasImage
    return QCanvasImage._cuteOwning(address)

  @overload(QCanvasImage)
  def removeImage(self, image: QCanvasImage) -> None:
    """
    Calls Qt's 'void QCanvasPainter::removeImage(const QCanvasImage &image)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#removeImage

    Parameters
    ----------

    image : QCanvasImage
      Passed on as a value: Qt reads the C++ QCanvasImage, which stays
      Python's own.
    """
    #  void QCanvasPainter::removeImage(const QCanvasImage &image)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter11removeImageERK12QCanvasImage',
        self._valueOf(image),
    )

  def cleanupResources(self) -> None:
    """
    Calls Qt's 'void QCanvasPainter::cleanupResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainter.html#cleanupResources
    """
    #  void QCanvasPainter::cleanupResources()
    self.uglySide.call('ritual_ZN14QCanvasPainter16cleanupResourcesEv')

  @overload(int)
  def removePathGroup(self, pathGroup: int) -> None:
    """
    Calls Qt's 'void QCanvasPainter::removePathGroup(int pathGroup)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainter.html#removePathGroup

    Parameters
    ----------

    pathGroup : int
      Passed on as it is.
    """
    #  void QCanvasPainter::removePathGroup(int pathGroup)
    self.uglySide.call(
        'ritual_ZN14QCanvasPainter15removePathGroupEi', pathGroup,
    )

  @overload(QSize)
  @overload(QSize, int)
  @overload(QSize, int, QCanvasOffscreenCanvas.Flags)
  def createCanvas(
      self,
      pixelSize: QSize,
      sampleCount: int = 1,
      flags: QCanvasOffscreenCanvas.Flags = QCanvasOffscreenCanvas.Flags(),
  ) -> QCanvasOffscreenCanvas:
    """
    Calls Qt's 'QCanvasOffscreenCanvas QCanvasPainter::createCanvas(QSize
    pixelSize, int sampleCount, QCanvasOffscreenCanvas::Flags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#createCanvas

    Parameters
    ----------

    pixelSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    sampleCount : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    flags : QCanvasOffscreenCanvas.Flags
      Passed on as its number. May be left out, as in Qt: it is then
      QCanvasOffscreenCanvas.Flags().

    Returns
    -------

    QCanvasOffscreenCanvas
      A new cute QCanvasOffscreenCanvas around the copy Qt gave back. Python
      owns it.
    """
    #  QCanvasOffscreenCanvas QCanvasPainter::createCanvas(QSize pixelSize,
    #      int sampleCount, QCanvasOffscreenCanvas::Flags flags)
    address = self.uglySide.call(
        'ritual_ZN14QCanvasPainter12createCanvasE5QSizei6QFlagsIN22QCanvasO'
        'ffscreenCanvas4FlagEE',
        self._valueOf(pixelSize), sampleCount, flags.value,
    )
    return QCanvasOffscreenCanvas._cuteOwning(address)

  def d_func(self) -> Optional[QCanvasPainterPrivate]:
    """
    Calls Qt's 'QCanvasPainterPrivate *QCanvasPainter::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainter.html#d_func

    Returns
    -------

    Optional[QCanvasPainterPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCanvasPainterPrivate *QCanvasPainter::d_func()
    address = self.uglySide.call('ritual_ZN14QCanvasPainter6d_funcEv')
    from . import QCanvasPainterPrivate
    return QCanvasPainterPrivate._cuteAt(address)

  @staticmethod
  def destroyCanvas(*__, **_) -> Never:
    """
    Qt's 'void QCanvasPainter::destroyCanvas(QCanvasOffscreenCanvas
    &canvas)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCanvasPainter.destroyCanvas' has no cute function yet. Qt's "
        "'void QCanvasPainter::destroyCanvas(QCanvasOffscreenCanvas "
        "&canvas)': takes a type Python has no way to hand over yet.")
