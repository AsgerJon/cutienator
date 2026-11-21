"""
QPainter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qpainter.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QGradientPreset, QPainterCompositionMode
from . import QPainterPixmapFragmentHint, QPainterRenderHint

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QLine, QLineF, QPoint, QPointF, QRect, QRectF
  from . import QBrush, QColor, QFont, QFontInfo, QFontMetrics, QGradient
  from . import QImage, QPaintDevice, QPaintEngine, QPainterPath, QPen
  from . import QPicture, QPixmap, QPolygon, QPolygonF, QRegion, QStaticText
  from . import QTextItem, QTextOption, QTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QColor = WAIT['QColor']
  QFont = WAIT['QFont']
  QImage = WAIT['QImage']
  QLine = WAIT['QLine']
  QLineF = WAIT['QLineF']
  QPaintDevice = WAIT['QPaintDevice']
  QPainterPath = WAIT['QPainterPath']
  QPen = WAIT['QPen']
  QPicture = WAIT['QPicture']
  QPixmap = WAIT['QPixmap']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QPolygon = WAIT['QPolygon']
  QPolygonF = WAIT['QPolygonF']
  QRect = WAIT['QRect']
  QRectF = WAIT['QRectF']
  QRegion = WAIT['QRegion']
  QStaticText = WAIT['QStaticText']
  QTextItem = WAIT['QTextItem']
  QTextOption = WAIT['QTextOption']
  QTransform = WAIT['QTransform']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPainter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPainter: a plain Python object standing in front of
  one C++ QPainter.

  What exists
  -----------

  Every function of Qt's QPainter that has a ritual and that Python can call
  so far, 88 names in all: 'device', 'begin', 'end', 'isActive',
  'setCompositionMode', 'compositionMode', 'font', 'setFont', 'fontMetrics',
  'fontInfo', 'setPen', 'pen', 'setBrush', 'brush', 'setBackgroundMode',
  'backgroundMode', 'brushOrigin', 'brushOriginF', 'setBrushOrigin',
  'setBackground', 'background', 'opacity', 'setOpacity', 'clipRegion',
  'clipPath', 'setClipRect', 'setClipRegion', 'setClipPath', 'setClipping',
  'hasClipping', 'clipBoundingRect', 'save', 'restore', 'setTransform',
  'transform', 'deviceTransform', 'resetTransform', 'setWorldTransform',
  'worldTransform', 'combinedTransform', 'setWorldMatrixEnabled',
  'worldMatrixEnabled', 'scale', 'shear', 'rotate', 'translate', 'window',
  'setWindow', 'viewport', 'setViewport', 'setViewTransformEnabled',
  'viewTransformEnabled', 'strokePath', 'fillPath', 'drawPath', 'drawPoint',
  'drawPoints', 'drawLine', 'drawLines', 'drawRect', 'drawRects',
  'drawEllipse', 'drawPolyline', 'drawPolygon', 'drawConvexPolygon',
  'drawArc', 'drawPie', 'drawChord', 'drawRoundedRect', 'drawTiledPixmap',
  'drawPicture', 'drawPixmap', 'drawImage', 'setLayoutDirection',
  'layoutDirection', 'drawStaticText', 'drawText', 'boundingRect',
  'drawTextItem', 'fillRect', 'eraseRect', 'setRenderHint', 'setRenderHints',
  'renderHints', 'testRenderHint', 'paintEngine', 'beginNativePainting',
  'endNativePainting'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPainter::~QPainter()': the destructor: Python never removes a C++
    QPainter.
  - Qt's 'void QPainter::drawPixmapFragments(const PixmapFragment *fragments,
    int fragmentCount, const QPixmap &pixmap, PixmapFragmentHints hints)':
    names 'QPainter::PixmapFragment', which has no cute class yet.
  - Qt's 'void QPainter::drawGlyphRun(const QPointF &position, const
    QGlyphRun &glyphRun)': names 'QGlyphRun', which has no cute class yet.

  What has no ritual
  ------------------

  17 of the 211 functions Qt declares: 8 takes or gives a type that cannot be
  passed yet; 5 private; 2 forbidden; 1 declared and nowhere to be found; 1 a
  template.

  What to expect
  --------------

  - The C++ QPainter is created at the first use, not by 'QPainter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPainter.
  """

  #  The enums Qt writes inside QPainter, and the names Qt has for the
  #  combinations of its flags enums.
  CompositionMode = QPainterCompositionMode
  PixmapFragmentHint = QPainterPixmapFragmentHint
  PixmapFragmentHints = QPainterPixmapFragmentHint
  RenderHint = QPainterRenderHint
  RenderHints = QPainterRenderHint

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPainter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def device(self) -> Optional[QPaintDevice]:
    """
    Calls Qt's 'QPaintDevice *QPainter::device() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#device

    Returns
    -------

    Optional[QPaintDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintDevice *QPainter::device() const
    address = self.uglySide.call('ritual_ZNK8QPainter6deviceEv')
    from . import QPaintDevice
    return QPaintDevice._cuteAt(address)

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QPainter::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#isActive
    """
    #  bool QPainter::isActive() const
    return self.uglySide.call('ritual_ZNK8QPainter8isActiveEv')

  def compositionMode(self) -> CompositionMode:
    """
    Calls Qt's 'CompositionMode QPainter::compositionMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#compositionMode

    Returns
    -------

    CompositionMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'CompositionMode(number)'
      gives.
    """
    #  CompositionMode QPainter::compositionMode() const
    return QPainter.CompositionMode(self.uglySide.call(
        'ritual_ZNK8QPainter15compositionModeEv',
    ))

  def font(self) -> QFont:
    """
    Calls Qt's 'const QFont &QPainter::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  const QFont &QPainter::font() const
    address = self.uglySide.call('ritual_ZNK8QPainter4fontEv')
    from . import QFont
    return QFont._cuteOwning(address)

  def fontMetrics(self) -> QFontMetrics:
    """
    Calls Qt's 'QFontMetrics QPainter::fontMetrics() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#fontMetrics

    Returns
    -------

    QFontMetrics
      A new cute QFontMetrics around the copy Qt gave back. Python owns it.
    """
    #  QFontMetrics QPainter::fontMetrics() const
    address = self.uglySide.call('ritual_ZNK8QPainter11fontMetricsEv')
    from . import QFontMetrics
    return QFontMetrics._cuteOwning(address)

  def fontInfo(self) -> QFontInfo:
    """
    Calls Qt's 'QFontInfo QPainter::fontInfo() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#fontInfo

    Returns
    -------

    QFontInfo
      A new cute QFontInfo around the copy Qt gave back. Python owns it.
    """
    #  QFontInfo QPainter::fontInfo() const
    address = self.uglySide.call('ritual_ZNK8QPainter8fontInfoEv')
    from . import QFontInfo
    return QFontInfo._cuteOwning(address)

  def pen(self) -> QPen:
    """
    Calls Qt's 'const QPen &QPainter::pen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#pen

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  const QPen &QPainter::pen() const
    address = self.uglySide.call('ritual_ZNK8QPainter3penEv')
    from . import QPen
    return QPen._cuteOwning(address)

  def brush(self) -> QBrush:
    """
    Calls Qt's 'const QBrush &QPainter::brush() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#brush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  const QBrush &QPainter::brush() const
    address = self.uglySide.call('ritual_ZNK8QPainter5brushEv')
    from . import QBrush
    return QBrush._cuteOwning(address)

  def backgroundMode(self) -> Qt.BGMode:
    """
    Calls Qt's 'Qt::BGMode QPainter::backgroundMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#backgroundMode

    Returns
    -------

    Qt.BGMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.BGMode(number)' gives.
    """
    #  Qt::BGMode QPainter::backgroundMode() const
    return Qt.BGMode(self.uglySide.call(
        'ritual_ZNK8QPainter14backgroundModeEv',
    ))

  def brushOrigin(self) -> QPoint:
    """
    Calls Qt's 'QPoint QPainter::brushOrigin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#brushOrigin

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QPainter::brushOrigin() const
    address = self.uglySide.call('ritual_ZNK8QPainter11brushOriginEv')
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def brushOriginF(self) -> QPointF:
    """
    Calls Qt's 'QPointF QPainter::brushOriginF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#brushOriginF

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QPainter::brushOriginF() const
    address = self.uglySide.call('ritual_ZNK8QPainter12brushOriginFEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def background(self) -> QBrush:
    """
    Calls Qt's 'const QBrush &QPainter::background() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#background

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  const QBrush &QPainter::background() const
    address = self.uglySide.call('ritual_ZNK8QPainter10backgroundEv')
    from . import QBrush
    return QBrush._cuteOwning(address)

  def opacity(self) -> float:
    """
    Calls Qt's 'qreal QPainter::opacity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#opacity
    """
    #  qreal QPainter::opacity() const
    return self.uglySide.call('ritual_ZNK8QPainter7opacityEv')

  def clipRegion(self) -> QRegion:
    """
    Calls Qt's 'QRegion QPainter::clipRegion() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#clipRegion

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QPainter::clipRegion() const
    address = self.uglySide.call('ritual_ZNK8QPainter10clipRegionEv')
    from . import QRegion
    return QRegion._cuteOwning(address)

  def clipPath(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QPainter::clipPath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#clipPath

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QPainter::clipPath() const
    address = self.uglySide.call('ritual_ZNK8QPainter8clipPathEv')
    from . import QPainterPath
    return QPainterPath._cuteOwning(address)

  def hasClipping(self) -> bool:
    """
    Calls Qt's 'bool QPainter::hasClipping() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#hasClipping
    """
    #  bool QPainter::hasClipping() const
    return self.uglySide.call('ritual_ZNK8QPainter11hasClippingEv')

  def clipBoundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QPainter::clipBoundingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#clipBoundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QPainter::clipBoundingRect() const
    address = self.uglySide.call('ritual_ZNK8QPainter16clipBoundingRectEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def transform(self) -> QTransform:
    """
    Calls Qt's 'const QTransform &QPainter::transform() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#transform

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  const QTransform &QPainter::transform() const
    address = self.uglySide.call('ritual_ZNK8QPainter9transformEv')
    from . import QTransform
    return QTransform._cuteOwning(address)

  def deviceTransform(self) -> QTransform:
    """
    Calls Qt's 'const QTransform &QPainter::deviceTransform() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#deviceTransform

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  const QTransform &QPainter::deviceTransform() const
    address = self.uglySide.call('ritual_ZNK8QPainter15deviceTransformEv')
    from . import QTransform
    return QTransform._cuteOwning(address)

  def worldTransform(self) -> QTransform:
    """
    Calls Qt's 'const QTransform &QPainter::worldTransform() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#worldTransform

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  const QTransform &QPainter::worldTransform() const
    address = self.uglySide.call('ritual_ZNK8QPainter14worldTransformEv')
    from . import QTransform
    return QTransform._cuteOwning(address)

  def combinedTransform(self) -> QTransform:
    """
    Calls Qt's 'QTransform QPainter::combinedTransform() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#combinedTransform

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QPainter::combinedTransform() const
    address = self.uglySide.call('ritual_ZNK8QPainter17combinedTransformEv')
    from . import QTransform
    return QTransform._cuteOwning(address)

  def worldMatrixEnabled(self) -> bool:
    """
    Calls Qt's 'bool QPainter::worldMatrixEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#worldMatrixEnabled
    """
    #  bool QPainter::worldMatrixEnabled() const
    return self.uglySide.call('ritual_ZNK8QPainter18worldMatrixEnabledEv')

  def window(self) -> QRect:
    """
    Calls Qt's 'QRect QPainter::window() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#window

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QPainter::window() const
    address = self.uglySide.call('ritual_ZNK8QPainter6windowEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def viewport(self) -> QRect:
    """
    Calls Qt's 'QRect QPainter::viewport() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#viewport

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QPainter::viewport() const
    address = self.uglySide.call('ritual_ZNK8QPainter8viewportEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def viewTransformEnabled(self) -> bool:
    """
    Calls Qt's 'bool QPainter::viewTransformEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#viewTransformEnabled
    """
    #  bool QPainter::viewTransformEnabled() const
    return self.uglySide.call('ritual_ZNK8QPainter20viewTransformEnabledEv')

  def layoutDirection(self) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection QPainter::layoutDirection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#layoutDirection

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection QPainter::layoutDirection() const
    return Qt.LayoutDirection(self.uglySide.call(
        'ritual_ZNK8QPainter15layoutDirectionEv',
    ))

  def renderHints(self) -> RenderHints:
    """
    Calls Qt's 'RenderHints QPainter::renderHints() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#renderHints

    Returns
    -------

    RenderHints
      The value standing for the combination Qt gave back.
    """
    #  RenderHints QPainter::renderHints() const
    return QPainter.RenderHints(self.uglySide.call(
        'ritual_ZNK8QPainter11renderHintsEv',
    ))

  @overload(RenderHint)
  def testRenderHint(self, hint: RenderHint) -> bool:
    """
    Calls Qt's 'bool QPainter::testRenderHint(RenderHint hint) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#testRenderHint

    Parameters
    ----------

    hint : RenderHint
      Passed on as its number.
    """
    #  bool QPainter::testRenderHint(RenderHint hint) const
    return self.uglySide.call(
        'ritual_ZNK8QPainter14testRenderHintENS_10RenderHintE', hint.value,
    )

  def paintEngine(self) -> Optional[QPaintEngine]:
    """
    Calls Qt's 'QPaintEngine *QPainter::paintEngine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#paintEngine

    Returns
    -------

    Optional[QPaintEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintEngine *QPainter::paintEngine() const
    address = self.uglySide.call('ritual_ZNK8QPainter11paintEngineEv')
    from . import QPaintEngine
    return QPaintEngine._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(CompositionMode)
  def setCompositionMode(self, mode: CompositionMode) -> None:
    """
    Calls Qt's 'void QPainter::setCompositionMode(CompositionMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#setCompositionMode

    Parameters
    ----------

    mode : CompositionMode
      Passed on as its number.
    """
    #  void QPainter::setCompositionMode(CompositionMode mode)
    self.uglySide.call(
        'ritual_ZN8QPainter18setCompositionModeENS_15CompositionModeE',
        mode.value,
    )

  @overload(QFont)
  def setFont(self, f: QFont) -> None:
    """
    Calls Qt's 'void QPainter::setFont(const QFont &f)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#setFont

    Parameters
    ----------

    f : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QPainter::setFont(const QFont &f)
    self.uglySide.call(
        'ritual_ZN8QPainter7setFontERK5QFont', self._valueOf(f),
    )

  @overload(QColor)
  def setPen(self, color: QColor) -> None:
    """
    Calls Qt's 'void QPainter::setPen(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#setPen

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QPainter::setPen(const QColor &color)
    self.uglySide.call(
        'ritual_ZN8QPainter6setPenERK6QColor', self._valueOf(color),
    )

  @overload(QPen)
  def setPen(self, pen: QPen) -> None:
    """
    Calls Qt's 'void QPainter::setPen(const QPen &pen)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#setPen

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void QPainter::setPen(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN8QPainter6setPenERK4QPen', self._valueOf(pen),
    )

  @overload(Qt.PenStyle)
  def setPen(self, style: Qt.PenStyle) -> None:
    """
    Calls Qt's 'void QPainter::setPen(Qt::PenStyle style)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#setPen

    Parameters
    ----------

    style : Qt.PenStyle
      Passed on as its number.
    """
    #  void QPainter::setPen(Qt::PenStyle style)
    self.uglySide.call(
        'ritual_ZN8QPainter6setPenEN2Qt8PenStyleE', style.value,
    )

  @overload(QBrush)
  def setBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QPainter::setBrush(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#setBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QPainter::setBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN8QPainter8setBrushERK6QBrush', self._valueOf(brush),
    )

  @overload(Qt.BrushStyle)
  def setBrush(self, style: Qt.BrushStyle) -> None:
    """
    Calls Qt's 'void QPainter::setBrush(Qt::BrushStyle style)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#setBrush

    Parameters
    ----------

    style : Qt.BrushStyle
      Passed on as its number.
    """
    #  void QPainter::setBrush(Qt::BrushStyle style)
    self.uglySide.call(
        'ritual_ZN8QPainter8setBrushEN2Qt10BrushStyleE', style.value,
    )

  @overload(QColor)
  def setBrush(self, color: QColor) -> None:
    """
    Calls Qt's 'void QPainter::setBrush(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#setBrush

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QPainter::setBrush(QColor color)
    self.uglySide.call(
        'ritual_ZN8QPainter8setBrushE6QColor', self._valueOf(color),
    )

  @overload(Qt.GlobalColor)
  def setBrush(self, color: Qt.GlobalColor) -> None:
    """
    Calls Qt's 'void QPainter::setBrush(Qt::GlobalColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#setBrush

    Parameters
    ----------

    color : Qt.GlobalColor
      Passed on as its number.
    """
    #  void QPainter::setBrush(Qt::GlobalColor color)
    self.uglySide.call(
        'ritual_ZN8QPainter8setBrushEN2Qt11GlobalColorE', color.value,
    )

  @overload(Qt.BGMode)
  def setBackgroundMode(self, mode: Qt.BGMode) -> None:
    """
    Calls Qt's 'void QPainter::setBackgroundMode(Qt::BGMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#setBackgroundMode

    Parameters
    ----------

    mode : Qt.BGMode
      Passed on as its number.
    """
    #  void QPainter::setBackgroundMode(Qt::BGMode mode)
    self.uglySide.call(
        'ritual_ZN8QPainter17setBackgroundModeEN2Qt6BGModeE', mode.value,
    )

  @overload(int, int)
  def setBrushOrigin(self, x: int, y: int) -> None:
    """
    Calls Qt's 'void QPainter::setBrushOrigin(int x, int y)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#setBrushOrigin

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QPainter::setBrushOrigin(int x, int y)
    self.uglySide.call('ritual_ZN8QPainter14setBrushOriginEii', x, y)

  @overload(QPoint)
  def setBrushOrigin(self, a0: QPoint) -> None:
    """
    Calls Qt's 'void QPainter::setBrushOrigin(const QPoint &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#setBrushOrigin

    Parameters
    ----------

    a0 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QPainter::setBrushOrigin(const QPoint &a0)
    self.uglySide.call(
        'ritual_ZN8QPainter14setBrushOriginERK6QPoint', self._valueOf(a0),
    )

  @overload(QPointF)
  def setBrushOrigin(self, a0: QPointF) -> None:
    """
    Calls Qt's 'void QPainter::setBrushOrigin(const QPointF &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#setBrushOrigin

    Parameters
    ----------

    a0 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QPainter::setBrushOrigin(const QPointF &a0)
    self.uglySide.call(
        'ritual_ZN8QPainter14setBrushOriginERK7QPointF', self._valueOf(a0),
    )

  @overload(QBrush)
  def setBackground(self, bg: QBrush) -> None:
    """
    Calls Qt's 'void QPainter::setBackground(const QBrush &bg)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#setBackground

    Parameters
    ----------

    bg : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QPainter::setBackground(const QBrush &bg)
    self.uglySide.call(
        'ritual_ZN8QPainter13setBackgroundERK6QBrush', self._valueOf(bg),
    )

  @overload(float)
  def setOpacity(self, opacity: float) -> None:
    """
    Calls Qt's 'void QPainter::setOpacity(qreal opacity)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#setOpacity

    Parameters
    ----------

    opacity : float
      Passed on as it is.
    """
    #  void QPainter::setOpacity(qreal opacity)
    self.uglySide.call('ritual_ZN8QPainter10setOpacityEd', opacity)

  @overload(QRectF)
  @overload(QRectF, Qt.ClipOperation)
  def setClipRect(
      self,
      a0: QRectF,
      op: Qt.ClipOperation = Qt.ClipOperation.ReplaceClip,
  ) -> None:
    """
    Calls Qt's 'void QPainter::setClipRect(const QRectF &a0,
    Qt::ClipOperation op)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#setClipRect

    Parameters
    ----------

    a0 : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    op : Qt.ClipOperation
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ClipOperation.ReplaceClip.
    """
    #  void QPainter::setClipRect(const QRectF &a0, Qt::ClipOperation op)
    self.uglySide.call(
        'ritual_ZN8QPainter11setClipRectERK6QRectFN2Qt13ClipOperationE',
        self._valueOf(a0), op.value,
    )

  @overload(QRect)
  @overload(QRect, Qt.ClipOperation)
  def setClipRect(
      self,
      a0: QRect,
      op: Qt.ClipOperation = Qt.ClipOperation.ReplaceClip,
  ) -> None:
    """
    Calls Qt's 'void QPainter::setClipRect(const QRect &a0, Qt::ClipOperation
    op)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#setClipRect

    Parameters
    ----------

    a0 : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    op : Qt.ClipOperation
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ClipOperation.ReplaceClip.
    """
    #  void QPainter::setClipRect(const QRect &a0, Qt::ClipOperation op)
    self.uglySide.call(
        'ritual_ZN8QPainter11setClipRectERK5QRectN2Qt13ClipOperationE',
        self._valueOf(a0), op.value,
    )

  @overload(int, int, int, int)
  @overload(int, int, int, int, Qt.ClipOperation)
  def setClipRect(
      self,
      x: int,
      y: int,
      w: int,
      h: int,
      op: Qt.ClipOperation = Qt.ClipOperation.ReplaceClip,
  ) -> None:
    """
    Calls Qt's 'void QPainter::setClipRect(int x, int y, int w, int h,
    Qt::ClipOperation op)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#setClipRect

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.

    op : Qt.ClipOperation
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ClipOperation.ReplaceClip.
    """
    #  void QPainter::setClipRect(int x, int y, int w, int h,
    #      Qt::ClipOperation op)
    self.uglySide.call(
        'ritual_ZN8QPainter11setClipRectEiiiiN2Qt13ClipOperationE',
        x, y, w, h, op.value,
    )

  @overload(QRegion)
  @overload(QRegion, Qt.ClipOperation)
  def setClipRegion(
      self,
      a0: QRegion,
      op: Qt.ClipOperation = Qt.ClipOperation.ReplaceClip,
  ) -> None:
    """
    Calls Qt's 'void QPainter::setClipRegion(const QRegion &a0,
    Qt::ClipOperation op)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#setClipRegion

    Parameters
    ----------

    a0 : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.

    op : Qt.ClipOperation
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ClipOperation.ReplaceClip.
    """
    #  void QPainter::setClipRegion(const QRegion &a0, Qt::ClipOperation op)
    self.uglySide.call(
        'ritual_ZN8QPainter13setClipRegionERK7QRegionN2Qt13ClipOperationE',
        self._valueOf(a0), op.value,
    )

  @overload(QPainterPath)
  @overload(QPainterPath, Qt.ClipOperation)
  def setClipPath(
      self,
      path: QPainterPath,
      op: Qt.ClipOperation = Qt.ClipOperation.ReplaceClip,
  ) -> None:
    """
    Calls Qt's 'void QPainter::setClipPath(const QPainterPath &path,
    Qt::ClipOperation op)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#setClipPath

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    op : Qt.ClipOperation
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ClipOperation.ReplaceClip.
    """
    #  void QPainter::setClipPath(const QPainterPath &path, Qt::ClipOperation
    #      op)
    self.uglySide.call(
        'ritual_ZN8QPainter11setClipPathERK12QPainterPathN2Qt13ClipOperatio'
        'nE',
        self._valueOf(path), op.value,
    )

  @overload(bool)
  def setClipping(self, enable: bool) -> None:
    """
    Calls Qt's 'void QPainter::setClipping(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#setClipping

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QPainter::setClipping(bool enable)
    self.uglySide.call('ritual_ZN8QPainter11setClippingEb', enable)

  @overload(QTransform)
  @overload(QTransform, bool)
  def setTransform(
      self,
      transform: QTransform,
      combine: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QPainter::setTransform(const QTransform &transform, bool
    combine)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#setTransform

    Parameters
    ----------

    transform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.

    combine : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QPainter::setTransform(const QTransform &transform, bool combine)
    self.uglySide.call(
        'ritual_ZN8QPainter12setTransformERK10QTransformb',
        self._valueOf(transform), combine,
    )

  @overload(QTransform)
  @overload(QTransform, bool)
  def setWorldTransform(
      self,
      matrix: QTransform,
      combine: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QPainter::setWorldTransform(const QTransform &matrix,
    bool combine)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#setWorldTransform

    Parameters
    ----------

    matrix : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.

    combine : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QPainter::setWorldTransform(const QTransform &matrix, bool
    #      combine)
    self.uglySide.call(
        'ritual_ZN8QPainter17setWorldTransformERK10QTransformb',
        self._valueOf(matrix), combine,
    )

  @overload(bool)
  def setWorldMatrixEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QPainter::setWorldMatrixEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainter.html#setWorldMatrixEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QPainter::setWorldMatrixEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN8QPainter21setWorldMatrixEnabledEb', enabled,
    )

  @overload(QRect)
  def setWindow(self, window: QRect) -> None:
    """
    Calls Qt's 'void QPainter::setWindow(const QRect &window)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#setWindow

    Parameters
    ----------

    window : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QPainter::setWindow(const QRect &window)
    self.uglySide.call(
        'ritual_ZN8QPainter9setWindowERK5QRect', self._valueOf(window),
    )

  @overload(int, int, int, int)
  def setWindow(self, x: int, y: int, w: int, h: int) -> None:
    """
    Calls Qt's 'void QPainter::setWindow(int x, int y, int w, int h)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#setWindow

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.
    """
    #  void QPainter::setWindow(int x, int y, int w, int h)
    self.uglySide.call('ritual_ZN8QPainter9setWindowEiiii', x, y, w, h)

  @overload(QRect)
  def setViewport(self, viewport: QRect) -> None:
    """
    Calls Qt's 'void QPainter::setViewport(const QRect &viewport)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#setViewport

    Parameters
    ----------

    viewport : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QPainter::setViewport(const QRect &viewport)
    self.uglySide.call(
        'ritual_ZN8QPainter11setViewportERK5QRect', self._valueOf(viewport),
    )

  @overload(int, int, int, int)
  def setViewport(self, x: int, y: int, w: int, h: int) -> None:
    """
    Calls Qt's 'void QPainter::setViewport(int x, int y, int w, int h)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#setViewport

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.
    """
    #  void QPainter::setViewport(int x, int y, int w, int h)
    self.uglySide.call('ritual_ZN8QPainter11setViewportEiiii', x, y, w, h)

  @overload(bool)
  def setViewTransformEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QPainter::setViewTransformEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainter.html#setViewTransformEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QPainter::setViewTransformEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN8QPainter23setViewTransformEnabledEb', enable,
    )

  @overload(Qt.LayoutDirection)
  def setLayoutDirection(self, direction: Qt.LayoutDirection) -> None:
    """
    Calls Qt's 'void QPainter::setLayoutDirection(Qt::LayoutDirection
    direction)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#setLayoutDirection

    Parameters
    ----------

    direction : Qt.LayoutDirection
      Passed on as its number.
    """
    #  void QPainter::setLayoutDirection(Qt::LayoutDirection direction)
    self.uglySide.call(
        'ritual_ZN8QPainter18setLayoutDirectionEN2Qt15LayoutDirectionE',
        direction.value,
    )

  @overload(RenderHint)
  @overload(RenderHint, bool)
  def setRenderHint(self, hint: RenderHint, on: bool = True) -> None:
    """
    Calls Qt's 'void QPainter::setRenderHint(RenderHint hint, bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#setRenderHint

    Parameters
    ----------

    hint : RenderHint
      Passed on as its number.

    on : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QPainter::setRenderHint(RenderHint hint, bool on)
    self.uglySide.call(
        'ritual_ZN8QPainter13setRenderHintENS_10RenderHintEb',
        hint.value, on,
    )

  @overload(RenderHints)
  @overload(RenderHints, bool)
  def setRenderHints(self, hints: RenderHints, on: bool = True) -> None:
    """
    Calls Qt's 'void QPainter::setRenderHints(RenderHints hints, bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#setRenderHints

    Parameters
    ----------

    hints : RenderHints
      Passed on as its number.

    on : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QPainter::setRenderHints(RenderHints hints, bool on)
    self.uglySide.call(
        'ritual_ZN8QPainter14setRenderHintsE6QFlagsINS_10RenderHintEEb',
        hints.value, on,
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
    Notes what was given, for Qt's 'QPainter::QPainter()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#QPainter
    """
    #  QPainter::QPainter()
    self._noteCreation(QPainter, lambda: Rituals.call(
        'ritual_ZN8QPainterC1Ev',
    ))

  @overload(QPaintDevice)
  @overload(NoneType)
  def __init__(self, a0: Optional[QPaintDevice]) -> None:
    """
    Notes what was given, for Qt's 'QPainter::QPainter(QPaintDevice *a0)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#QPainter

    Parameters
    ----------

    a0 : Optional[QPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPainter::QPainter(QPaintDevice *a0)
    self._noteCreation(QPainter, lambda: Rituals.call(
        'ritual_ZN8QPainterC1EP12QPaintDevice', self._addressOf(a0),
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
  def begin(self, a0: Optional[QPaintDevice]) -> bool:
    """
    Calls Qt's 'bool QPainter::begin(QPaintDevice *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#begin

    Parameters
    ----------

    a0 : Optional[QPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPainter::begin(QPaintDevice *a0)
    return self.uglySide.call(
        'ritual_ZN8QPainter5beginEP12QPaintDevice', self._addressOf(a0),
    )

  def end(self) -> bool:
    """
    Calls Qt's 'bool QPainter::end()'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#end
    """
    #  bool QPainter::end()
    return self.uglySide.call('ritual_ZN8QPainter3endEv')

  def save(self) -> None:
    """
    Calls Qt's 'void QPainter::save()'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#save
    """
    #  void QPainter::save()
    self.uglySide.call('ritual_ZN8QPainter4saveEv')

  def restore(self) -> None:
    """
    Calls Qt's 'void QPainter::restore()'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#restore
    """
    #  void QPainter::restore()
    self.uglySide.call('ritual_ZN8QPainter7restoreEv')

  def resetTransform(self) -> None:
    """
    Calls Qt's 'void QPainter::resetTransform()'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#resetTransform
    """
    #  void QPainter::resetTransform()
    self.uglySide.call('ritual_ZN8QPainter14resetTransformEv')

  @overload(float, float)
  def scale(self, sx: float, sy: float) -> None:
    """
    Calls Qt's 'void QPainter::scale(qreal sx, qreal sy)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#scale

    Parameters
    ----------

    sx : float
      Passed on as it is.

    sy : float
      Passed on as it is.
    """
    #  void QPainter::scale(qreal sx, qreal sy)
    self.uglySide.call('ritual_ZN8QPainter5scaleEdd', sx, sy)

  @overload(float, float)
  def shear(self, sh: float, sv: float) -> None:
    """
    Calls Qt's 'void QPainter::shear(qreal sh, qreal sv)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#shear

    Parameters
    ----------

    sh : float
      Passed on as it is.

    sv : float
      Passed on as it is.
    """
    #  void QPainter::shear(qreal sh, qreal sv)
    self.uglySide.call('ritual_ZN8QPainter5shearEdd', sh, sv)

  @overload(float)
  def rotate(self, a: float) -> None:
    """
    Calls Qt's 'void QPainter::rotate(qreal a)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#rotate

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QPainter::rotate(qreal a)
    self.uglySide.call('ritual_ZN8QPainter6rotateEd', a)

  @overload(QPointF)
  def translate(self, offset: QPointF) -> None:
    """
    Calls Qt's 'void QPainter::translate(const QPointF &offset)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#translate

    Parameters
    ----------

    offset : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QPainter::translate(const QPointF &offset)
    self.uglySide.call(
        'ritual_ZN8QPainter9translateERK7QPointF', self._valueOf(offset),
    )

  @overload(QPoint)
  def translate(self, offset: QPoint) -> None:
    """
    Calls Qt's 'void QPainter::translate(const QPoint &offset)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#translate

    Parameters
    ----------

    offset : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QPainter::translate(const QPoint &offset)
    self.uglySide.call(
        'ritual_ZN8QPainter9translateERK6QPoint', self._valueOf(offset),
    )

  @overload(float, float)
  def translate(self, dx: float, dy: float) -> None:
    """
    Calls Qt's 'void QPainter::translate(qreal dx, qreal dy)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#translate

    Parameters
    ----------

    dx : float
      Passed on as it is.

    dy : float
      Passed on as it is.
    """
    #  void QPainter::translate(qreal dx, qreal dy)
    self.uglySide.call('ritual_ZN8QPainter9translateEdd', dx, dy)

  @overload(QPainterPath, QPen)
  def strokePath(self, path: QPainterPath, pen: QPen) -> None:
    """
    Calls Qt's 'void QPainter::strokePath(const QPainterPath &path, const
    QPen &pen)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#strokePath

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void QPainter::strokePath(const QPainterPath &path, const QPen &pen)
    self.uglySide.call(
        'ritual_ZN8QPainter10strokePathERK12QPainterPathRK4QPen',
        self._valueOf(path), self._valueOf(pen),
    )

  @overload(QPainterPath, QBrush)
  def fillPath(self, path: QPainterPath, brush: QBrush) -> None:
    """
    Calls Qt's 'void QPainter::fillPath(const QPainterPath &path, const
    QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#fillPath

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QPainter::fillPath(const QPainterPath &path, const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN8QPainter8fillPathERK12QPainterPathRK6QBrush',
        self._valueOf(path), self._valueOf(brush),
    )

  @overload(QPainterPath)
  def drawPath(self, path: QPainterPath) -> None:
    """
    Calls Qt's 'void QPainter::drawPath(const QPainterPath &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPath

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.
    """
    #  void QPainter::drawPath(const QPainterPath &path)
    self.uglySide.call(
        'ritual_ZN8QPainter8drawPathERK12QPainterPath', self._valueOf(path),
    )

  @overload(QPointF)
  def drawPoint(self, pt: QPointF) -> None:
    """
    Calls Qt's 'void QPainter::drawPoint(const QPointF &pt)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPoint

    Parameters
    ----------

    pt : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QPainter::drawPoint(const QPointF &pt)
    self.uglySide.call(
        'ritual_ZN8QPainter9drawPointERK7QPointF', self._valueOf(pt),
    )

  @overload(QPoint)
  def drawPoint(self, p: QPoint) -> None:
    """
    Calls Qt's 'void QPainter::drawPoint(const QPoint &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPoint

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QPainter::drawPoint(const QPoint &p)
    self.uglySide.call(
        'ritual_ZN8QPainter9drawPointERK6QPoint', self._valueOf(p),
    )

  @overload(int, int)
  def drawPoint(self, x: int, y: int) -> None:
    """
    Calls Qt's 'void QPainter::drawPoint(int x, int y)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPoint

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QPainter::drawPoint(int x, int y)
    self.uglySide.call('ritual_ZN8QPainter9drawPointEii', x, y)

  @overload(QPointF, int)
  @overload(NoneType, int)
  def drawPoints(self, points: Optional[QPointF], pointCount: int) -> None:
    """
    Calls Qt's 'void QPainter::drawPoints(const QPointF *points, int
    pointCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPoints

    Parameters
    ----------

    points : Optional[QPointF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pointCount : int
      Passed on as it is.
    """
    #  void QPainter::drawPoints(const QPointF *points, int pointCount)
    self.uglySide.call(
        'ritual_ZN8QPainter10drawPointsEPK7QPointFi',
        self._addressOf(points), pointCount,
    )

  @overload(QPolygonF)
  def drawPoints(self, points: QPolygonF) -> None:
    """
    Calls Qt's 'void QPainter::drawPoints(const QPolygonF &points)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPoints

    Parameters
    ----------

    points : QPolygonF
      Passed on as a value: Qt reads the C++ QPolygonF, which stays Python's
      own.
    """
    #  void QPainter::drawPoints(const QPolygonF &points)
    self.uglySide.call(
        'ritual_ZN8QPainter10drawPointsERK9QPolygonF', self._valueOf(points),
    )

  @overload(QPoint, int)
  def drawPoints(self, points: Optional[QPoint], pointCount: int) -> None:
    """
    Calls Qt's 'void QPainter::drawPoints(const QPoint *points, int
    pointCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPoints

    Parameters
    ----------

    points : Optional[QPoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pointCount : int
      Passed on as it is.
    """
    #  void QPainter::drawPoints(const QPoint *points, int pointCount)
    self.uglySide.call(
        'ritual_ZN8QPainter10drawPointsEPK6QPointi',
        self._addressOf(points), pointCount,
    )

  @overload(QPolygon)
  def drawPoints(self, points: QPolygon) -> None:
    """
    Calls Qt's 'void QPainter::drawPoints(const QPolygon &points)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPoints

    Parameters
    ----------

    points : QPolygon
      Passed on as a value: Qt reads the C++ QPolygon, which stays Python's
      own.
    """
    #  void QPainter::drawPoints(const QPolygon &points)
    self.uglySide.call(
        'ritual_ZN8QPainter10drawPointsERK8QPolygon', self._valueOf(points),
    )

  @overload(QLineF)
  def drawLine(self, line: QLineF) -> None:
    """
    Calls Qt's 'void QPainter::drawLine(const QLineF &line)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawLine

    Parameters
    ----------

    line : QLineF
      Passed on as a value: Qt reads the C++ QLineF, which stays Python's
      own.
    """
    #  void QPainter::drawLine(const QLineF &line)
    self.uglySide.call(
        'ritual_ZN8QPainter8drawLineERK6QLineF', self._valueOf(line),
    )

  @overload(QLine)
  def drawLine(self, line: QLine) -> None:
    """
    Calls Qt's 'void QPainter::drawLine(const QLine &line)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawLine

    Parameters
    ----------

    line : QLine
      Passed on as a value: Qt reads the C++ QLine, which stays Python's own.
    """
    #  void QPainter::drawLine(const QLine &line)
    self.uglySide.call(
        'ritual_ZN8QPainter8drawLineERK5QLine', self._valueOf(line),
    )

  @overload(int, int, int, int)
  def drawLine(self, x1: int, y1: int, x2: int, y2: int) -> None:
    """
    Calls Qt's 'void QPainter::drawLine(int x1, int y1, int x2, int y2)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawLine

    Parameters
    ----------

    x1 : int
      Passed on as it is.

    y1 : int
      Passed on as it is.

    x2 : int
      Passed on as it is.

    y2 : int
      Passed on as it is.
    """
    #  void QPainter::drawLine(int x1, int y1, int x2, int y2)
    self.uglySide.call('ritual_ZN8QPainter8drawLineEiiii', x1, y1, x2, y2)

  @overload(QPoint, QPoint)
  def drawLine(self, p1: QPoint, p2: QPoint) -> None:
    """
    Calls Qt's 'void QPainter::drawLine(const QPoint &p1, const QPoint &p2)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawLine

    Parameters
    ----------

    p1 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    p2 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QPainter::drawLine(const QPoint &p1, const QPoint &p2)
    self.uglySide.call(
        'ritual_ZN8QPainter8drawLineERK6QPointS2_',
        self._valueOf(p1), self._valueOf(p2),
    )

  @overload(QPointF, QPointF)
  def drawLine(self, p1: QPointF, p2: QPointF) -> None:
    """
    Calls Qt's 'void QPainter::drawLine(const QPointF &p1, const QPointF
    &p2)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawLine

    Parameters
    ----------

    p1 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    p2 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QPainter::drawLine(const QPointF &p1, const QPointF &p2)
    self.uglySide.call(
        'ritual_ZN8QPainter8drawLineERK7QPointFS2_',
        self._valueOf(p1), self._valueOf(p2),
    )

  @overload(QLineF, int)
  @overload(NoneType, int)
  def drawLines(self, lines: Optional[QLineF], lineCount: int) -> None:
    """
    Calls Qt's 'void QPainter::drawLines(const QLineF *lines, int
    lineCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawLines

    Parameters
    ----------

    lines : Optional[QLineF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    lineCount : int
      Passed on as it is.
    """
    #  void QPainter::drawLines(const QLineF *lines, int lineCount)
    self.uglySide.call(
        'ritual_ZN8QPainter9drawLinesEPK6QLineFi',
        self._addressOf(lines), lineCount,
    )

  @overload(QPointF, int)
  def drawLines(self, pointPairs: Optional[QPointF], lineCount: int) -> None:
    """
    Calls Qt's 'void QPainter::drawLines(const QPointF *pointPairs, int
    lineCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawLines

    Parameters
    ----------

    pointPairs : Optional[QPointF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    lineCount : int
      Passed on as it is.
    """
    #  void QPainter::drawLines(const QPointF *pointPairs, int lineCount)
    self.uglySide.call(
        'ritual_ZN8QPainter9drawLinesEPK7QPointFi',
        self._addressOf(pointPairs), lineCount,
    )

  @overload(QLine, int)
  def drawLines(self, lines: Optional[QLine], lineCount: int) -> None:
    """
    Calls Qt's 'void QPainter::drawLines(const QLine *lines, int lineCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawLines

    Parameters
    ----------

    lines : Optional[QLine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    lineCount : int
      Passed on as it is.
    """
    #  void QPainter::drawLines(const QLine *lines, int lineCount)
    self.uglySide.call(
        'ritual_ZN8QPainter9drawLinesEPK5QLinei',
        self._addressOf(lines), lineCount,
    )

  @overload(QPoint, int)
  def drawLines(self, pointPairs: Optional[QPoint], lineCount: int) -> None:
    """
    Calls Qt's 'void QPainter::drawLines(const QPoint *pointPairs, int
    lineCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawLines

    Parameters
    ----------

    pointPairs : Optional[QPoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    lineCount : int
      Passed on as it is.
    """
    #  void QPainter::drawLines(const QPoint *pointPairs, int lineCount)
    self.uglySide.call(
        'ritual_ZN8QPainter9drawLinesEPK6QPointi',
        self._addressOf(pointPairs), lineCount,
    )

  @overload(QRectF)
  def drawRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QPainter::drawRect(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QPainter::drawRect(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN8QPainter8drawRectERK6QRectF', self._valueOf(rect),
    )

  @overload(int, int, int, int)
  def drawRect(self, x1: int, y1: int, w: int, h: int) -> None:
    """
    Calls Qt's 'void QPainter::drawRect(int x1, int y1, int w, int h)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawRect

    Parameters
    ----------

    x1 : int
      Passed on as it is.

    y1 : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.
    """
    #  void QPainter::drawRect(int x1, int y1, int w, int h)
    self.uglySide.call('ritual_ZN8QPainter8drawRectEiiii', x1, y1, w, h)

  @overload(QRect)
  def drawRect(self, rect: QRect) -> None:
    """
    Calls Qt's 'void QPainter::drawRect(const QRect &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawRect

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QPainter::drawRect(const QRect &rect)
    self.uglySide.call(
        'ritual_ZN8QPainter8drawRectERK5QRect', self._valueOf(rect),
    )

  @overload(QRectF, int)
  @overload(NoneType, int)
  def drawRects(self, rects: Optional[QRectF], rectCount: int) -> None:
    """
    Calls Qt's 'void QPainter::drawRects(const QRectF *rects, int
    rectCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawRects

    Parameters
    ----------

    rects : Optional[QRectF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rectCount : int
      Passed on as it is.
    """
    #  void QPainter::drawRects(const QRectF *rects, int rectCount)
    self.uglySide.call(
        'ritual_ZN8QPainter9drawRectsEPK6QRectFi',
        self._addressOf(rects), rectCount,
    )

  @overload(QRect, int)
  def drawRects(self, rects: Optional[QRect], rectCount: int) -> None:
    """
    Calls Qt's 'void QPainter::drawRects(const QRect *rects, int rectCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawRects

    Parameters
    ----------

    rects : Optional[QRect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rectCount : int
      Passed on as it is.
    """
    #  void QPainter::drawRects(const QRect *rects, int rectCount)
    self.uglySide.call(
        'ritual_ZN8QPainter9drawRectsEPK5QRecti',
        self._addressOf(rects), rectCount,
    )

  @overload(QRectF)
  def drawEllipse(self, r: QRectF) -> None:
    """
    Calls Qt's 'void QPainter::drawEllipse(const QRectF &r)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawEllipse

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QPainter::drawEllipse(const QRectF &r)
    self.uglySide.call(
        'ritual_ZN8QPainter11drawEllipseERK6QRectF', self._valueOf(r),
    )

  @overload(QRect)
  def drawEllipse(self, r: QRect) -> None:
    """
    Calls Qt's 'void QPainter::drawEllipse(const QRect &r)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawEllipse

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QPainter::drawEllipse(const QRect &r)
    self.uglySide.call(
        'ritual_ZN8QPainter11drawEllipseERK5QRect', self._valueOf(r),
    )

  @overload(int, int, int, int)
  def drawEllipse(self, x: int, y: int, w: int, h: int) -> None:
    """
    Calls Qt's 'void QPainter::drawEllipse(int x, int y, int w, int h)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawEllipse

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.
    """
    #  void QPainter::drawEllipse(int x, int y, int w, int h)
    self.uglySide.call('ritual_ZN8QPainter11drawEllipseEiiii', x, y, w, h)

  @overload(QPointF, float, float)
  def drawEllipse(self, center: QPointF, rx: float, ry: float) -> None:
    """
    Calls Qt's 'void QPainter::drawEllipse(const QPointF &center, qreal rx,
    qreal ry)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawEllipse

    Parameters
    ----------

    center : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    rx : float
      Passed on as it is.

    ry : float
      Passed on as it is.
    """
    #  void QPainter::drawEllipse(const QPointF &center, qreal rx, qreal ry)
    self.uglySide.call(
        'ritual_ZN8QPainter11drawEllipseERK7QPointFdd',
        self._valueOf(center), rx, ry,
    )

  @overload(QPoint, int, int)
  def drawEllipse(self, center: QPoint, rx: int, ry: int) -> None:
    """
    Calls Qt's 'void QPainter::drawEllipse(const QPoint &center, int rx, int
    ry)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawEllipse

    Parameters
    ----------

    center : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    rx : int
      Passed on as it is.

    ry : int
      Passed on as it is.
    """
    #  void QPainter::drawEllipse(const QPoint &center, int rx, int ry)
    self.uglySide.call(
        'ritual_ZN8QPainter11drawEllipseERK6QPointii',
        self._valueOf(center), rx, ry,
    )

  @overload(QPointF, int)
  @overload(NoneType, int)
  def drawPolyline(self, points: Optional[QPointF], pointCount: int) -> None:
    """
    Calls Qt's 'void QPainter::drawPolyline(const QPointF *points, int
    pointCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPolyline

    Parameters
    ----------

    points : Optional[QPointF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pointCount : int
      Passed on as it is.
    """
    #  void QPainter::drawPolyline(const QPointF *points, int pointCount)
    self.uglySide.call(
        'ritual_ZN8QPainter12drawPolylineEPK7QPointFi',
        self._addressOf(points), pointCount,
    )

  @overload(QPolygonF)
  def drawPolyline(self, polyline: QPolygonF) -> None:
    """
    Calls Qt's 'void QPainter::drawPolyline(const QPolygonF &polyline)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPolyline

    Parameters
    ----------

    polyline : QPolygonF
      Passed on as a value: Qt reads the C++ QPolygonF, which stays Python's
      own.
    """
    #  void QPainter::drawPolyline(const QPolygonF &polyline)
    self.uglySide.call(
        'ritual_ZN8QPainter12drawPolylineERK9QPolygonF',
        self._valueOf(polyline),
    )

  @overload(QPoint, int)
  def drawPolyline(self, points: Optional[QPoint], pointCount: int) -> None:
    """
    Calls Qt's 'void QPainter::drawPolyline(const QPoint *points, int
    pointCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPolyline

    Parameters
    ----------

    points : Optional[QPoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pointCount : int
      Passed on as it is.
    """
    #  void QPainter::drawPolyline(const QPoint *points, int pointCount)
    self.uglySide.call(
        'ritual_ZN8QPainter12drawPolylineEPK6QPointi',
        self._addressOf(points), pointCount,
    )

  @overload(QPolygon)
  def drawPolyline(self, polygon: QPolygon) -> None:
    """
    Calls Qt's 'void QPainter::drawPolyline(const QPolygon &polygon)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPolyline

    Parameters
    ----------

    polygon : QPolygon
      Passed on as a value: Qt reads the C++ QPolygon, which stays Python's
      own.
    """
    #  void QPainter::drawPolyline(const QPolygon &polygon)
    self.uglySide.call(
        'ritual_ZN8QPainter12drawPolylineERK8QPolygon',
        self._valueOf(polygon),
    )

  @overload(QPointF, int)
  @overload(NoneType, int)
  @overload(QPointF, int, Qt.FillRule)
  @overload(NoneType, int, Qt.FillRule)
  def drawPolygon(
      self,
      points: Optional[QPointF],
      pointCount: int,
      fillRule: Qt.FillRule = Qt.FillRule.OddEvenFill,
  ) -> None:
    """
    Calls Qt's 'void QPainter::drawPolygon(const QPointF *points, int
    pointCount, Qt::FillRule fillRule)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPolygon

    Parameters
    ----------

    points : Optional[QPointF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pointCount : int
      Passed on as it is.

    fillRule : Qt.FillRule
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.FillRule.OddEvenFill.
    """
    #  void QPainter::drawPolygon(const QPointF *points, int pointCount,
    #      Qt::FillRule fillRule)
    self.uglySide.call(
        'ritual_ZN8QPainter11drawPolygonEPK7QPointFiN2Qt8FillRuleE',
        self._addressOf(points), pointCount, fillRule.value,
    )

  @overload(QPolygonF)
  @overload(QPolygonF, Qt.FillRule)
  def drawPolygon(
      self,
      polygon: QPolygonF,
      fillRule: Qt.FillRule = Qt.FillRule.OddEvenFill,
  ) -> None:
    """
    Calls Qt's 'void QPainter::drawPolygon(const QPolygonF &polygon,
    Qt::FillRule fillRule)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPolygon

    Parameters
    ----------

    polygon : QPolygonF
      Passed on as a value: Qt reads the C++ QPolygonF, which stays Python's
      own.

    fillRule : Qt.FillRule
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.FillRule.OddEvenFill.
    """
    #  void QPainter::drawPolygon(const QPolygonF &polygon, Qt::FillRule
    #      fillRule)
    self.uglySide.call(
        'ritual_ZN8QPainter11drawPolygonERK9QPolygonFN2Qt8FillRuleE',
        self._valueOf(polygon), fillRule.value,
    )

  @overload(QPoint, int)
  @overload(QPoint, int, Qt.FillRule)
  def drawPolygon(
      self,
      points: Optional[QPoint],
      pointCount: int,
      fillRule: Qt.FillRule = Qt.FillRule.OddEvenFill,
  ) -> None:
    """
    Calls Qt's 'void QPainter::drawPolygon(const QPoint *points, int
    pointCount, Qt::FillRule fillRule)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPolygon

    Parameters
    ----------

    points : Optional[QPoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pointCount : int
      Passed on as it is.

    fillRule : Qt.FillRule
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.FillRule.OddEvenFill.
    """
    #  void QPainter::drawPolygon(const QPoint *points, int pointCount,
    #      Qt::FillRule fillRule)
    self.uglySide.call(
        'ritual_ZN8QPainter11drawPolygonEPK6QPointiN2Qt8FillRuleE',
        self._addressOf(points), pointCount, fillRule.value,
    )

  @overload(QPolygon)
  @overload(QPolygon, Qt.FillRule)
  def drawPolygon(
      self,
      polygon: QPolygon,
      fillRule: Qt.FillRule = Qt.FillRule.OddEvenFill,
  ) -> None:
    """
    Calls Qt's 'void QPainter::drawPolygon(const QPolygon &polygon,
    Qt::FillRule fillRule)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPolygon

    Parameters
    ----------

    polygon : QPolygon
      Passed on as a value: Qt reads the C++ QPolygon, which stays Python's
      own.

    fillRule : Qt.FillRule
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.FillRule.OddEvenFill.
    """
    #  void QPainter::drawPolygon(const QPolygon &polygon, Qt::FillRule
    #      fillRule)
    self.uglySide.call(
        'ritual_ZN8QPainter11drawPolygonERK8QPolygonN2Qt8FillRuleE',
        self._valueOf(polygon), fillRule.value,
    )

  @overload(QPointF, int)
  @overload(NoneType, int)
  def drawConvexPolygon(
      self,
      points: Optional[QPointF],
      pointCount: int,
  ) -> None:
    """
    Calls Qt's 'void QPainter::drawConvexPolygon(const QPointF *points, int
    pointCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawConvexPolygon

    Parameters
    ----------

    points : Optional[QPointF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pointCount : int
      Passed on as it is.
    """
    #  void QPainter::drawConvexPolygon(const QPointF *points, int
    #      pointCount)
    self.uglySide.call(
        'ritual_ZN8QPainter17drawConvexPolygonEPK7QPointFi',
        self._addressOf(points), pointCount,
    )

  @overload(QPolygonF)
  def drawConvexPolygon(self, polygon: QPolygonF) -> None:
    """
    Calls Qt's 'void QPainter::drawConvexPolygon(const QPolygonF &polygon)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawConvexPolygon

    Parameters
    ----------

    polygon : QPolygonF
      Passed on as a value: Qt reads the C++ QPolygonF, which stays Python's
      own.
    """
    #  void QPainter::drawConvexPolygon(const QPolygonF &polygon)
    self.uglySide.call(
        'ritual_ZN8QPainter17drawConvexPolygonERK9QPolygonF',
        self._valueOf(polygon),
    )

  @overload(QPoint, int)
  def drawConvexPolygon(
      self,
      points: Optional[QPoint],
      pointCount: int,
  ) -> None:
    """
    Calls Qt's 'void QPainter::drawConvexPolygon(const QPoint *points, int
    pointCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawConvexPolygon

    Parameters
    ----------

    points : Optional[QPoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pointCount : int
      Passed on as it is.
    """
    #  void QPainter::drawConvexPolygon(const QPoint *points, int pointCount)
    self.uglySide.call(
        'ritual_ZN8QPainter17drawConvexPolygonEPK6QPointi',
        self._addressOf(points), pointCount,
    )

  @overload(QPolygon)
  def drawConvexPolygon(self, polygon: QPolygon) -> None:
    """
    Calls Qt's 'void QPainter::drawConvexPolygon(const QPolygon &polygon)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawConvexPolygon

    Parameters
    ----------

    polygon : QPolygon
      Passed on as a value: Qt reads the C++ QPolygon, which stays Python's
      own.
    """
    #  void QPainter::drawConvexPolygon(const QPolygon &polygon)
    self.uglySide.call(
        'ritual_ZN8QPainter17drawConvexPolygonERK8QPolygon',
        self._valueOf(polygon),
    )

  @overload(QRectF, int, int)
  def drawArc(self, rect: QRectF, a: int, alen: int) -> None:
    """
    Calls Qt's 'void QPainter::drawArc(const QRectF &rect, int a, int alen)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawArc

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    a : int
      Passed on as it is.

    alen : int
      Passed on as it is.
    """
    #  void QPainter::drawArc(const QRectF &rect, int a, int alen)
    self.uglySide.call(
        'ritual_ZN8QPainter7drawArcERK6QRectFii',
        self._valueOf(rect), a, alen,
    )

  @overload(QRect, int, int)
  def drawArc(self, a0: QRect, a: int, alen: int) -> None:
    """
    Calls Qt's 'void QPainter::drawArc(const QRect &a0, int a, int alen)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawArc

    Parameters
    ----------

    a0 : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    a : int
      Passed on as it is.

    alen : int
      Passed on as it is.
    """
    #  void QPainter::drawArc(const QRect &a0, int a, int alen)
    self.uglySide.call(
        'ritual_ZN8QPainter7drawArcERK5QRectii', self._valueOf(a0), a, alen,
    )

  @overload(int, int, int, int, int, int)
  def drawArc(
      self,
      x: int,
      y: int,
      w: int,
      h: int,
      a: int,
      alen: int,
  ) -> None:
    """
    Calls Qt's 'void QPainter::drawArc(int x, int y, int w, int h, int a, int
    alen)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawArc

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.

    a : int
      Passed on as it is.

    alen : int
      Passed on as it is.
    """
    #  void QPainter::drawArc(int x, int y, int w, int h, int a, int alen)
    self.uglySide.call(
        'ritual_ZN8QPainter7drawArcEiiiiii', x, y, w, h, a, alen,
    )

  @overload(QRectF, int, int)
  def drawPie(self, rect: QRectF, a: int, alen: int) -> None:
    """
    Calls Qt's 'void QPainter::drawPie(const QRectF &rect, int a, int alen)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPie

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    a : int
      Passed on as it is.

    alen : int
      Passed on as it is.
    """
    #  void QPainter::drawPie(const QRectF &rect, int a, int alen)
    self.uglySide.call(
        'ritual_ZN8QPainter7drawPieERK6QRectFii',
        self._valueOf(rect), a, alen,
    )

  @overload(int, int, int, int, int, int)
  def drawPie(
      self,
      x: int,
      y: int,
      w: int,
      h: int,
      a: int,
      alen: int,
  ) -> None:
    """
    Calls Qt's 'void QPainter::drawPie(int x, int y, int w, int h, int a, int
    alen)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPie

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.

    a : int
      Passed on as it is.

    alen : int
      Passed on as it is.
    """
    #  void QPainter::drawPie(int x, int y, int w, int h, int a, int alen)
    self.uglySide.call(
        'ritual_ZN8QPainter7drawPieEiiiiii', x, y, w, h, a, alen,
    )

  @overload(QRect, int, int)
  def drawPie(self, a0: QRect, a: int, alen: int) -> None:
    """
    Calls Qt's 'void QPainter::drawPie(const QRect &a0, int a, int alen)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPie

    Parameters
    ----------

    a0 : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    a : int
      Passed on as it is.

    alen : int
      Passed on as it is.
    """
    #  void QPainter::drawPie(const QRect &a0, int a, int alen)
    self.uglySide.call(
        'ritual_ZN8QPainter7drawPieERK5QRectii', self._valueOf(a0), a, alen,
    )

  @overload(QRectF, int, int)
  def drawChord(self, rect: QRectF, a: int, alen: int) -> None:
    """
    Calls Qt's 'void QPainter::drawChord(const QRectF &rect, int a, int
    alen)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawChord

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    a : int
      Passed on as it is.

    alen : int
      Passed on as it is.
    """
    #  void QPainter::drawChord(const QRectF &rect, int a, int alen)
    self.uglySide.call(
        'ritual_ZN8QPainter9drawChordERK6QRectFii',
        self._valueOf(rect), a, alen,
    )

  @overload(int, int, int, int, int, int)
  def drawChord(
      self,
      x: int,
      y: int,
      w: int,
      h: int,
      a: int,
      alen: int,
  ) -> None:
    """
    Calls Qt's 'void QPainter::drawChord(int x, int y, int w, int h, int a,
    int alen)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawChord

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.

    a : int
      Passed on as it is.

    alen : int
      Passed on as it is.
    """
    #  void QPainter::drawChord(int x, int y, int w, int h, int a, int alen)
    self.uglySide.call(
        'ritual_ZN8QPainter9drawChordEiiiiii', x, y, w, h, a, alen,
    )

  @overload(QRect, int, int)
  def drawChord(self, a0: QRect, a: int, alen: int) -> None:
    """
    Calls Qt's 'void QPainter::drawChord(const QRect &a0, int a, int alen)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawChord

    Parameters
    ----------

    a0 : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    a : int
      Passed on as it is.

    alen : int
      Passed on as it is.
    """
    #  void QPainter::drawChord(const QRect &a0, int a, int alen)
    self.uglySide.call(
        'ritual_ZN8QPainter9drawChordERK5QRectii',
        self._valueOf(a0), a, alen,
    )

  @overload(QRectF, float, float)
  @overload(QRectF, float, float, Qt.SizeMode)
  def drawRoundedRect(
      self,
      rect: QRectF,
      xRadius: float,
      yRadius: float,
      mode: Qt.SizeMode = Qt.SizeMode.AbsoluteSize,
  ) -> None:
    """
    Calls Qt's 'void QPainter::drawRoundedRect(const QRectF &rect, qreal
    xRadius, qreal yRadius, Qt::SizeMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawRoundedRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    xRadius : float
      Passed on as it is.

    yRadius : float
      Passed on as it is.

    mode : Qt.SizeMode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.SizeMode.AbsoluteSize.
    """
    #  void QPainter::drawRoundedRect(const QRectF &rect, qreal xRadius,
    #      qreal yRadius, Qt::SizeMode mode)
    self.uglySide.call(
        'ritual_ZN8QPainter15drawRoundedRectERK6QRectFddN2Qt8SizeModeE',
        self._valueOf(rect), xRadius, yRadius, mode.value,
    )

  @overload(int, int, int, int, float, float)
  @overload(int, int, int, int, float, float, Qt.SizeMode)
  def drawRoundedRect(
      self,
      x: int,
      y: int,
      w: int,
      h: int,
      xRadius: float,
      yRadius: float,
      mode: Qt.SizeMode = Qt.SizeMode.AbsoluteSize,
  ) -> None:
    """
    Calls Qt's 'void QPainter::drawRoundedRect(int x, int y, int w, int h,
    qreal xRadius, qreal yRadius, Qt::SizeMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawRoundedRect

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.

    xRadius : float
      Passed on as it is.

    yRadius : float
      Passed on as it is.

    mode : Qt.SizeMode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.SizeMode.AbsoluteSize.
    """
    #  void QPainter::drawRoundedRect(int x, int y, int w, int h, qreal
    #      xRadius, qreal yRadius, Qt::SizeMode mode)
    self.uglySide.call(
        'ritual_ZN8QPainter15drawRoundedRectEiiiiddN2Qt8SizeModeE',
        x, y, w, h, xRadius, yRadius, mode.value,
    )

  @overload(QRect, float, float)
  @overload(QRect, float, float, Qt.SizeMode)
  def drawRoundedRect(
      self,
      rect: QRect,
      xRadius: float,
      yRadius: float,
      mode: Qt.SizeMode = Qt.SizeMode.AbsoluteSize,
  ) -> None:
    """
    Calls Qt's 'void QPainter::drawRoundedRect(const QRect &rect, qreal
    xRadius, qreal yRadius, Qt::SizeMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawRoundedRect

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    xRadius : float
      Passed on as it is.

    yRadius : float
      Passed on as it is.

    mode : Qt.SizeMode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.SizeMode.AbsoluteSize.
    """
    #  void QPainter::drawRoundedRect(const QRect &rect, qreal xRadius, qreal
    #      yRadius, Qt::SizeMode mode)
    self.uglySide.call(
        'ritual_ZN8QPainter15drawRoundedRectERK5QRectddN2Qt8SizeModeE',
        self._valueOf(rect), xRadius, yRadius, mode.value,
    )

  @overload(QRectF, QPixmap)
  @overload(QRectF, QPixmap, QPointF)
  def drawTiledPixmap(
      self,
      rect: QRectF,
      pm: QPixmap,
      offset: Optional[QPointF] = None,
  ) -> None:
    """
    Calls Qt's 'void QPainter::drawTiledPixmap(const QRectF &rect, const
    QPixmap &pm, const QPointF &offset)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawTiledPixmap

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    pm : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    offset : Optional[QPointF]
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own. May be left out, as in Qt: a new 'QPointF()' is then passed on.
    """
    #  void QPainter::drawTiledPixmap(const QRectF &rect, const QPixmap &pm,
    #      const QPointF &offset)
    if offset is None:
      from ..QtCore import QPointF
      offset = QPointF()
    self.uglySide.call(
        'ritual_ZN8QPainter15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF',
        self._valueOf(rect), self._valueOf(pm), self._valueOf(offset),
    )

  @overload(int, int, int, int, QPixmap)
  @overload(int, int, int, int, QPixmap, int)
  @overload(int, int, int, int, QPixmap, int, int)
  def drawTiledPixmap(
      self,
      x: int,
      y: int,
      w: int,
      h: int,
      a4: QPixmap,
      sx: int = 0,
      sy: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QPainter::drawTiledPixmap(int x, int y, int w, int h,
    const QPixmap &a4, int sx, int sy)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawTiledPixmap

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.

    a4 : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    sx : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    sy : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QPainter::drawTiledPixmap(int x, int y, int w, int h, const
    #      QPixmap &a4, int sx, int sy)
    self.uglySide.call(
        'ritual_ZN8QPainter15drawTiledPixmapEiiiiRK7QPixmapii',
        x, y, w, h, self._valueOf(a4), sx, sy,
    )

  @overload(QRect, QPixmap)
  @overload(QRect, QPixmap, QPoint)
  def drawTiledPixmap(
      self,
      a0: QRect,
      a1: QPixmap,
      a2: Optional[QPoint] = None,
  ) -> None:
    """
    Calls Qt's 'void QPainter::drawTiledPixmap(const QRect &a0, const QPixmap
    &a1, const QPoint &a2)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawTiledPixmap

    Parameters
    ----------

    a0 : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    a1 : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    a2 : Optional[QPoint]
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own. May be left out, as in Qt: a new 'QPoint()' is then passed on.
    """
    #  void QPainter::drawTiledPixmap(const QRect &a0, const QPixmap &a1,
    #      const QPoint &a2)
    if a2 is None:
      from ..QtCore import QPoint
      a2 = QPoint()
    self.uglySide.call(
        'ritual_ZN8QPainter15drawTiledPixmapERK5QRectRK7QPixmapRK6QPoint',
        self._valueOf(a0), self._valueOf(a1), self._valueOf(a2),
    )

  @overload(QPointF, QPicture)
  def drawPicture(self, p: QPointF, picture: QPicture) -> None:
    """
    Calls Qt's 'void QPainter::drawPicture(const QPointF &p, const QPicture
    &picture)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPicture

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    picture : QPicture
      Passed on as a value: Qt reads the C++ QPicture, which stays Python's
      own.
    """
    #  void QPainter::drawPicture(const QPointF &p, const QPicture &picture)
    self.uglySide.call(
        'ritual_ZN8QPainter11drawPictureERK7QPointFRK8QPicture',
        self._valueOf(p), self._valueOf(picture),
    )

  @overload(int, int, QPicture)
  def drawPicture(self, x: int, y: int, picture: QPicture) -> None:
    """
    Calls Qt's 'void QPainter::drawPicture(int x, int y, const QPicture
    &picture)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPicture

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    picture : QPicture
      Passed on as a value: Qt reads the C++ QPicture, which stays Python's
      own.
    """
    #  void QPainter::drawPicture(int x, int y, const QPicture &picture)
    self.uglySide.call(
        'ritual_ZN8QPainter11drawPictureEiiRK8QPicture',
        x, y, self._valueOf(picture),
    )

  @overload(QPoint, QPicture)
  def drawPicture(self, p: QPoint, picture: QPicture) -> None:
    """
    Calls Qt's 'void QPainter::drawPicture(const QPoint &p, const QPicture
    &picture)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPicture

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    picture : QPicture
      Passed on as a value: Qt reads the C++ QPicture, which stays Python's
      own.
    """
    #  void QPainter::drawPicture(const QPoint &p, const QPicture &picture)
    self.uglySide.call(
        'ritual_ZN8QPainter11drawPictureERK6QPointRK8QPicture',
        self._valueOf(p), self._valueOf(picture),
    )

  @overload(QRectF, QPixmap, QRectF)
  def drawPixmap(
      self,
      targetRect: QRectF,
      pixmap: QPixmap,
      sourceRect: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QPainter::drawPixmap(const QRectF &targetRect, const
    QPixmap &pixmap, const QRectF &sourceRect)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPixmap

    Parameters
    ----------

    targetRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    sourceRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QPainter::drawPixmap(const QRectF &targetRect, const QPixmap
    #      &pixmap, const QRectF &sourceRect)
    self.uglySide.call(
        'ritual_ZN8QPainter10drawPixmapERK6QRectFRK7QPixmapS2_',
        self._valueOf(targetRect), self._valueOf(pixmap),
        self._valueOf(sourceRect),
    )

  @overload(QRect, QPixmap, QRect)
  def drawPixmap(
      self,
      targetRect: QRect,
      pixmap: QPixmap,
      sourceRect: QRect,
  ) -> None:
    """
    Calls Qt's 'void QPainter::drawPixmap(const QRect &targetRect, const
    QPixmap &pixmap, const QRect &sourceRect)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPixmap

    Parameters
    ----------

    targetRect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    sourceRect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QPainter::drawPixmap(const QRect &targetRect, const QPixmap
    #      &pixmap, const QRect &sourceRect)
    self.uglySide.call(
        'ritual_ZN8QPainter10drawPixmapERK5QRectRK7QPixmapS2_',
        self._valueOf(targetRect), self._valueOf(pixmap),
        self._valueOf(sourceRect),
    )

  @overload(int, int, int, int, QPixmap, int, int, int, int)
  def drawPixmap(
      self,
      x: int,
      y: int,
      w: int,
      h: int,
      pm: QPixmap,
      sx: int,
      sy: int,
      sw: int,
      sh: int,
  ) -> None:
    """
    Calls Qt's 'void QPainter::drawPixmap(int x, int y, int w, int h, const
    QPixmap &pm, int sx, int sy, int sw, int sh)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPixmap

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.

    pm : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    sx : int
      Passed on as it is.

    sy : int
      Passed on as it is.

    sw : int
      Passed on as it is.

    sh : int
      Passed on as it is.
    """
    #  void QPainter::drawPixmap(int x, int y, int w, int h, const QPixmap
    #      &pm, int sx, int sy, int sw, int sh)
    self.uglySide.call(
        'ritual_ZN8QPainter10drawPixmapEiiiiRK7QPixmapiiii',
        x, y, w, h, self._valueOf(pm), sx, sy, sw, sh,
    )

  @overload(int, int, QPixmap, int, int, int, int)
  def drawPixmap(
      self,
      x: int,
      y: int,
      pm: QPixmap,
      sx: int,
      sy: int,
      sw: int,
      sh: int,
  ) -> None:
    """
    Calls Qt's 'void QPainter::drawPixmap(int x, int y, const QPixmap &pm,
    int sx, int sy, int sw, int sh)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPixmap

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    pm : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    sx : int
      Passed on as it is.

    sy : int
      Passed on as it is.

    sw : int
      Passed on as it is.

    sh : int
      Passed on as it is.
    """
    #  void QPainter::drawPixmap(int x, int y, const QPixmap &pm, int sx, int
    #      sy, int sw, int sh)
    self.uglySide.call(
        'ritual_ZN8QPainter10drawPixmapEiiRK7QPixmapiiii',
        x, y, self._valueOf(pm), sx, sy, sw, sh,
    )

  @overload(QPointF, QPixmap, QRectF)
  def drawPixmap(self, p: QPointF, pm: QPixmap, sr: QRectF) -> None:
    """
    Calls Qt's 'void QPainter::drawPixmap(const QPointF &p, const QPixmap
    &pm, const QRectF &sr)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPixmap

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    pm : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    sr : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QPainter::drawPixmap(const QPointF &p, const QPixmap &pm, const
    #      QRectF &sr)
    self.uglySide.call(
        'ritual_ZN8QPainter10drawPixmapERK7QPointFRK7QPixmapRK6QRectF',
        self._valueOf(p), self._valueOf(pm), self._valueOf(sr),
    )

  @overload(QPoint, QPixmap, QRect)
  def drawPixmap(self, p: QPoint, pm: QPixmap, sr: QRect) -> None:
    """
    Calls Qt's 'void QPainter::drawPixmap(const QPoint &p, const QPixmap &pm,
    const QRect &sr)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPixmap

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    pm : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    sr : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QPainter::drawPixmap(const QPoint &p, const QPixmap &pm, const
    #      QRect &sr)
    self.uglySide.call(
        'ritual_ZN8QPainter10drawPixmapERK6QPointRK7QPixmapRK5QRect',
        self._valueOf(p), self._valueOf(pm), self._valueOf(sr),
    )

  @overload(QPointF, QPixmap)
  def drawPixmap(self, p: QPointF, pm: QPixmap) -> None:
    """
    Calls Qt's 'void QPainter::drawPixmap(const QPointF &p, const QPixmap
    &pm)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPixmap

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    pm : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  void QPainter::drawPixmap(const QPointF &p, const QPixmap &pm)
    self.uglySide.call(
        'ritual_ZN8QPainter10drawPixmapERK7QPointFRK7QPixmap',
        self._valueOf(p), self._valueOf(pm),
    )

  @overload(QPoint, QPixmap)
  def drawPixmap(self, p: QPoint, pm: QPixmap) -> None:
    """
    Calls Qt's 'void QPainter::drawPixmap(const QPoint &p, const QPixmap
    &pm)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPixmap

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    pm : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  void QPainter::drawPixmap(const QPoint &p, const QPixmap &pm)
    self.uglySide.call(
        'ritual_ZN8QPainter10drawPixmapERK6QPointRK7QPixmap',
        self._valueOf(p), self._valueOf(pm),
    )

  @overload(int, int, QPixmap)
  def drawPixmap(self, x: int, y: int, pm: QPixmap) -> None:
    """
    Calls Qt's 'void QPainter::drawPixmap(int x, int y, const QPixmap &pm)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPixmap

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    pm : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  void QPainter::drawPixmap(int x, int y, const QPixmap &pm)
    self.uglySide.call(
        'ritual_ZN8QPainter10drawPixmapEiiRK7QPixmap',
        x, y, self._valueOf(pm),
    )

  @overload(QRect, QPixmap)
  def drawPixmap(self, r: QRect, pm: QPixmap) -> None:
    """
    Calls Qt's 'void QPainter::drawPixmap(const QRect &r, const QPixmap
    &pm)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPixmap

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    pm : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  void QPainter::drawPixmap(const QRect &r, const QPixmap &pm)
    self.uglySide.call(
        'ritual_ZN8QPainter10drawPixmapERK5QRectRK7QPixmap',
        self._valueOf(r), self._valueOf(pm),
    )

  @overload(int, int, int, int, QPixmap)
  def drawPixmap(self, x: int, y: int, w: int, h: int, pm: QPixmap) -> None:
    """
    Calls Qt's 'void QPainter::drawPixmap(int x, int y, int w, int h, const
    QPixmap &pm)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawPixmap

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.

    pm : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  void QPainter::drawPixmap(int x, int y, int w, int h, const QPixmap
    #      &pm)
    self.uglySide.call(
        'ritual_ZN8QPainter10drawPixmapEiiiiRK7QPixmap',
        x, y, w, h, self._valueOf(pm),
    )

  @overload(QRectF, QImage, QRectF)
  @overload(QRectF, QImage, QRectF, Qt.ImageConversionFlags)
  def drawImage(
      self,
      targetRect: QRectF,
      image: QImage,
      sourceRect: QRectF,
      flags: Qt.ImageConversionFlags = Qt.ImageConversionFlags.AutoColor,
  ) -> None:
    """
    Calls Qt's 'void QPainter::drawImage(const QRectF &targetRect, const
    QImage &image, const QRectF &sourceRect, Qt::ImageConversionFlags
    flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawImage

    Parameters
    ----------

    targetRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    sourceRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    flags : Qt.ImageConversionFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ImageConversionFlags.AutoColor.
    """
    #  void QPainter::drawImage(const QRectF &targetRect, const QImage
    #      &image, const QRectF &sourceRect, Qt::ImageConversionFlags flags)
    self.uglySide.call(
        'ritual_ZN8QPainter9drawImageERK6QRectFRK6QImageS2_6QFlagsIN2Qt19Im'
        'ageConversionFlagEE',
        self._valueOf(targetRect), self._valueOf(image),
        self._valueOf(sourceRect), flags.value,
    )

  @overload(QRect, QImage, QRect)
  @overload(QRect, QImage, QRect, Qt.ImageConversionFlags)
  def drawImage(
      self,
      targetRect: QRect,
      image: QImage,
      sourceRect: QRect,
      flags: Qt.ImageConversionFlags = Qt.ImageConversionFlags.AutoColor,
  ) -> None:
    """
    Calls Qt's 'void QPainter::drawImage(const QRect &targetRect, const
    QImage &image, const QRect &sourceRect, Qt::ImageConversionFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawImage

    Parameters
    ----------

    targetRect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    sourceRect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    flags : Qt.ImageConversionFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ImageConversionFlags.AutoColor.
    """
    #  void QPainter::drawImage(const QRect &targetRect, const QImage &image,
    #      const QRect &sourceRect, Qt::ImageConversionFlags flags)
    self.uglySide.call(
        'ritual_ZN8QPainter9drawImageERK5QRectRK6QImageS2_6QFlagsIN2Qt19Ima'
        'geConversionFlagEE',
        self._valueOf(targetRect), self._valueOf(image),
        self._valueOf(sourceRect), flags.value,
    )

  @overload(QPointF, QImage, QRectF)
  @overload(QPointF, QImage, QRectF, Qt.ImageConversionFlags)
  def drawImage(
      self,
      p: QPointF,
      image: QImage,
      sr: QRectF,
      flags: Qt.ImageConversionFlags = Qt.ImageConversionFlags.AutoColor,
  ) -> None:
    """
    Calls Qt's 'void QPainter::drawImage(const QPointF &p, const QImage
    &image, const QRectF &sr, Qt::ImageConversionFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawImage

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    sr : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    flags : Qt.ImageConversionFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ImageConversionFlags.AutoColor.
    """
    #  void QPainter::drawImage(const QPointF &p, const QImage &image, const
    #      QRectF &sr, Qt::ImageConversionFlags flags)
    self.uglySide.call(
        'ritual_ZN8QPainter9drawImageERK7QPointFRK6QImageRK6QRectF6QFlagsIN'
        '2Qt19ImageConversionFlagEE',
        self._valueOf(p), self._valueOf(image), self._valueOf(sr),
        flags.value,
    )

  @overload(QPoint, QImage, QRect)
  @overload(QPoint, QImage, QRect, Qt.ImageConversionFlags)
  def drawImage(
      self,
      p: QPoint,
      image: QImage,
      sr: QRect,
      flags: Qt.ImageConversionFlags = Qt.ImageConversionFlags.AutoColor,
  ) -> None:
    """
    Calls Qt's 'void QPainter::drawImage(const QPoint &p, const QImage
    &image, const QRect &sr, Qt::ImageConversionFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawImage

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    sr : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    flags : Qt.ImageConversionFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ImageConversionFlags.AutoColor.
    """
    #  void QPainter::drawImage(const QPoint &p, const QImage &image, const
    #      QRect &sr, Qt::ImageConversionFlags flags)
    self.uglySide.call(
        'ritual_ZN8QPainter9drawImageERK6QPointRK6QImageRK5QRect6QFlagsIN2Q'
        't19ImageConversionFlagEE',
        self._valueOf(p), self._valueOf(image), self._valueOf(sr),
        flags.value,
    )

  @overload(QRectF, QImage)
  def drawImage(self, r: QRectF, image: QImage) -> None:
    """
    Calls Qt's 'void QPainter::drawImage(const QRectF &r, const QImage
    &image)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawImage

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QPainter::drawImage(const QRectF &r, const QImage &image)
    self.uglySide.call(
        'ritual_ZN8QPainter9drawImageERK6QRectFRK6QImage',
        self._valueOf(r), self._valueOf(image),
    )

  @overload(QRect, QImage)
  def drawImage(self, r: QRect, image: QImage) -> None:
    """
    Calls Qt's 'void QPainter::drawImage(const QRect &r, const QImage
    &image)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawImage

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QPainter::drawImage(const QRect &r, const QImage &image)
    self.uglySide.call(
        'ritual_ZN8QPainter9drawImageERK5QRectRK6QImage',
        self._valueOf(r), self._valueOf(image),
    )

  @overload(QPointF, QImage)
  def drawImage(self, p: QPointF, image: QImage) -> None:
    """
    Calls Qt's 'void QPainter::drawImage(const QPointF &p, const QImage
    &image)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawImage

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QPainter::drawImage(const QPointF &p, const QImage &image)
    self.uglySide.call(
        'ritual_ZN8QPainter9drawImageERK7QPointFRK6QImage',
        self._valueOf(p), self._valueOf(image),
    )

  @overload(QPoint, QImage)
  def drawImage(self, p: QPoint, image: QImage) -> None:
    """
    Calls Qt's 'void QPainter::drawImage(const QPoint &p, const QImage
    &image)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawImage

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QPainter::drawImage(const QPoint &p, const QImage &image)
    self.uglySide.call(
        'ritual_ZN8QPainter9drawImageERK6QPointRK6QImage',
        self._valueOf(p), self._valueOf(image),
    )

  @overload(int, int, QImage)
  @overload(int, int, QImage, int)
  @overload(int, int, QImage, int, int)
  @overload(int, int, QImage, int, int, int)
  @overload(int, int, QImage, int, int, int, int)
  @overload(int, int, QImage, int, int, int, int, Qt.ImageConversionFlags)
  def drawImage(
      self,
      x: int,
      y: int,
      image: QImage,
      sx: int = 0,
      sy: int = 0,
      sw: int = -1,
      sh: int = -1,
      flags: Qt.ImageConversionFlags = Qt.ImageConversionFlags.AutoColor,
  ) -> None:
    """
    Calls Qt's 'void QPainter::drawImage(int x, int y, const QImage &image,
    int sx, int sy, int sw, int sh, Qt::ImageConversionFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawImage

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    sx : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    sy : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    sw : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    sh : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    flags : Qt.ImageConversionFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ImageConversionFlags.AutoColor.
    """
    #  void QPainter::drawImage(int x, int y, const QImage &image, int sx,
    #      int sy, int sw, int sh, Qt::ImageConversionFlags flags)
    self.uglySide.call(
        'ritual_ZN8QPainter9drawImageEiiRK6QImageiiii6QFlagsIN2Qt19ImageCon'
        'versionFlagEE',
        x, y, self._valueOf(image), sx, sy, sw, sh, flags.value,
    )

  @overload(QPointF, QStaticText)
  def drawStaticText(
      self,
      topLeftPosition: QPointF,
      staticText: QStaticText,
  ) -> None:
    """
    Calls Qt's 'void QPainter::drawStaticText(const QPointF &topLeftPosition,
    const QStaticText &staticText)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawStaticText

    Parameters
    ----------

    topLeftPosition : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    staticText : QStaticText
      Passed on as a value: Qt reads the C++ QStaticText, which stays
      Python's own.
    """
    #  void QPainter::drawStaticText(const QPointF &topLeftPosition, const
    #      QStaticText &staticText)
    self.uglySide.call(
        'ritual_ZN8QPainter14drawStaticTextERK7QPointFRK11QStaticText',
        self._valueOf(topLeftPosition), self._valueOf(staticText),
    )

  @overload(QPoint, QStaticText)
  def drawStaticText(
      self,
      topLeftPosition: QPoint,
      staticText: QStaticText,
  ) -> None:
    """
    Calls Qt's 'void QPainter::drawStaticText(const QPoint &topLeftPosition,
    const QStaticText &staticText)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawStaticText

    Parameters
    ----------

    topLeftPosition : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    staticText : QStaticText
      Passed on as a value: Qt reads the C++ QStaticText, which stays
      Python's own.
    """
    #  void QPainter::drawStaticText(const QPoint &topLeftPosition, const
    #      QStaticText &staticText)
    self.uglySide.call(
        'ritual_ZN8QPainter14drawStaticTextERK6QPointRK11QStaticText',
        self._valueOf(topLeftPosition), self._valueOf(staticText),
    )

  @overload(int, int, QStaticText)
  def drawStaticText(
      self,
      left: int,
      top: int,
      staticText: QStaticText,
  ) -> None:
    """
    Calls Qt's 'void QPainter::drawStaticText(int left, int top, const
    QStaticText &staticText)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawStaticText

    Parameters
    ----------

    left : int
      Passed on as it is.

    top : int
      Passed on as it is.

    staticText : QStaticText
      Passed on as a value: Qt reads the C++ QStaticText, which stays
      Python's own.
    """
    #  void QPainter::drawStaticText(int left, int top, const QStaticText
    #      &staticText)
    self.uglySide.call(
        'ritual_ZN8QPainter14drawStaticTextEiiRK11QStaticText',
        left, top, self._valueOf(staticText),
    )

  @overload(QPointF, str)
  def drawText(self, p: QPointF, s: str) -> None:
    """
    Calls Qt's 'void QPainter::drawText(const QPointF &p, const QString &s)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawText

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPainter::drawText(const QPointF &p, const QString &s)
    self.uglySide.call(
        'ritual_ZN8QPainter8drawTextERK7QPointFRK7QString',
        self._valueOf(p), s,
    )

  @overload(QPoint, str)
  def drawText(self, p: QPoint, s: str) -> None:
    """
    Calls Qt's 'void QPainter::drawText(const QPoint &p, const QString &s)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawText

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPainter::drawText(const QPoint &p, const QString &s)
    self.uglySide.call(
        'ritual_ZN8QPainter8drawTextERK6QPointRK7QString',
        self._valueOf(p), s,
    )

  @overload(int, int, str)
  def drawText(self, x: int, y: int, s: str) -> None:
    """
    Calls Qt's 'void QPainter::drawText(int x, int y, const QString &s)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawText

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPainter::drawText(int x, int y, const QString &s)
    self.uglySide.call('ritual_ZN8QPainter8drawTextEiiRK7QString', x, y, s)

  @overload(QPointF, str, int, int)
  def drawText(
      self,
      p: QPointF,
      str: str,
      tf: int,
      justificationPadding: int,
  ) -> None:
    """
    Calls Qt's 'void QPainter::drawText(const QPointF &p, const QString &str,
    int tf, int justificationPadding)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawText

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    str : str
      Passed on as it is: a QString is made of it for the call.

    tf : int
      Passed on as it is.

    justificationPadding : int
      Passed on as it is.
    """
    #  void QPainter::drawText(const QPointF &p, const QString &str, int tf,
    #      int justificationPadding)
    self.uglySide.call(
        'ritual_ZN8QPainter8drawTextERK7QPointFRK7QStringii',
        self._valueOf(p), str, tf, justificationPadding,
    )

  @overload(QRectF, int, str)
  @overload(QRectF, int, str, QRectF)
  @overload(QRectF, int, str, NoneType)
  def drawText(
      self,
      r: QRectF,
      flags: int,
      text: str,
      br: Optional[QRectF] = None,
  ) -> None:
    """
    Calls Qt's 'void QPainter::drawText(const QRectF &r, int flags, const
    QString &text, QRectF *br)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawText

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    flags : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.

    br : Optional[QRectF]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QPainter::drawText(const QRectF &r, int flags, const QString
    #      &text, QRectF *br)
    self.uglySide.call(
        'ritual_ZN8QPainter8drawTextERK6QRectFiRK7QStringPS0_',
        self._valueOf(r), flags, text, self._addressOf(br),
    )

  @overload(QRect, int, str)
  @overload(QRect, int, str, QRect)
  @overload(QRect, int, str, NoneType)
  def drawText(
      self,
      r: QRect,
      flags: int,
      text: str,
      br: Optional[QRect] = None,
  ) -> None:
    """
    Calls Qt's 'void QPainter::drawText(const QRect &r, int flags, const
    QString &text, QRect *br)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawText

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    flags : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.

    br : Optional[QRect]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QPainter::drawText(const QRect &r, int flags, const QString
    #      &text, QRect *br)
    self.uglySide.call(
        'ritual_ZN8QPainter8drawTextERK5QRectiRK7QStringPS0_',
        self._valueOf(r), flags, text, self._addressOf(br),
    )

  @overload(int, int, int, int, int, str)
  @overload(int, int, int, int, int, str, QRect)
  @overload(int, int, int, int, int, str, NoneType)
  def drawText(
      self,
      x: int,
      y: int,
      w: int,
      h: int,
      flags: int,
      text: str,
      br: Optional[QRect] = None,
  ) -> None:
    """
    Calls Qt's 'void QPainter::drawText(int x, int y, int w, int h, int
    flags, const QString &text, QRect *br)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawText

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.

    flags : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.

    br : Optional[QRect]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QPainter::drawText(int x, int y, int w, int h, int flags, const
    #      QString &text, QRect *br)
    self.uglySide.call(
        'ritual_ZN8QPainter8drawTextEiiiiiRK7QStringP5QRect',
        x, y, w, h, flags, text, self._addressOf(br),
    )

  @overload(QRectF, str)
  @overload(QRectF, str, QTextOption)
  def drawText(
      self,
      r: QRectF,
      text: str,
      o: Optional[QTextOption] = None,
  ) -> None:
    """
    Calls Qt's 'void QPainter::drawText(const QRectF &r, const QString &text,
    const QTextOption &o)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawText

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    text : str
      Passed on as it is: a QString is made of it for the call.

    o : Optional[QTextOption]
      Passed on as a value: Qt reads the C++ QTextOption, which stays
      Python's own. May be left out, as in Qt: a new 'QTextOption()' is then
      passed on.
    """
    #  void QPainter::drawText(const QRectF &r, const QString &text, const
    #      QTextOption &o)
    if o is None:
      from . import QTextOption
      o = QTextOption()
    self.uglySide.call(
        'ritual_ZN8QPainter8drawTextERK6QRectFRK7QStringRK11QTextOption',
        self._valueOf(r), text, self._valueOf(o),
    )

  @overload(QRectF, int, str)
  def boundingRect(self, rect: QRectF, flags: int, text: str) -> QRectF:
    """
    Calls Qt's 'QRectF QPainter::boundingRect(const QRectF &rect, int flags,
    const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#boundingRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    flags : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QPainter::boundingRect(const QRectF &rect, int flags, const
    #      QString &text)
    address = self.uglySide.call(
        'ritual_ZN8QPainter12boundingRectERK6QRectFiRK7QString',
        self._valueOf(rect), flags, text,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QRect, int, str)
  def boundingRect(self, rect: QRect, flags: int, text: str) -> QRect:
    """
    Calls Qt's 'QRect QPainter::boundingRect(const QRect &rect, int flags,
    const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#boundingRect

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    flags : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QPainter::boundingRect(const QRect &rect, int flags, const
    #      QString &text)
    address = self.uglySide.call(
        'ritual_ZN8QPainter12boundingRectERK5QRectiRK7QString',
        self._valueOf(rect), flags, text,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(int, int, int, int, int, str)
  def boundingRect(
      self,
      x: int,
      y: int,
      w: int,
      h: int,
      flags: int,
      text: str,
  ) -> QRect:
    """
    Calls Qt's 'QRect QPainter::boundingRect(int x, int y, int w, int h, int
    flags, const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#boundingRect

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.

    flags : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QPainter::boundingRect(int x, int y, int w, int h, int flags,
    #      const QString &text)
    address = self.uglySide.call(
        'ritual_ZN8QPainter12boundingRectEiiiiiRK7QString',
        x, y, w, h, flags, text,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QRectF, str)
  @overload(QRectF, str, QTextOption)
  def boundingRect(
      self,
      rect: QRectF,
      text: str,
      o: Optional[QTextOption] = None,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF QPainter::boundingRect(const QRectF &rect, const
    QString &text, const QTextOption &o)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#boundingRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    text : str
      Passed on as it is: a QString is made of it for the call.

    o : Optional[QTextOption]
      Passed on as a value: Qt reads the C++ QTextOption, which stays
      Python's own. May be left out, as in Qt: a new 'QTextOption()' is then
      passed on.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QPainter::boundingRect(const QRectF &rect, const QString &text,
    #      const QTextOption &o)
    if o is None:
      from . import QTextOption
      o = QTextOption()
    address = self.uglySide.call(
        'ritual_ZN8QPainter12boundingRectERK6QRectFRK7QStringRK11QTextOptio'
        'n',
        self._valueOf(rect), text, self._valueOf(o),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QPointF, QTextItem)
  def drawTextItem(self, p: QPointF, ti: QTextItem) -> None:
    """
    Calls Qt's 'void QPainter::drawTextItem(const QPointF &p, const QTextItem
    &ti)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawTextItem

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    ti : QTextItem
      Passed on as a value: Qt reads the C++ QTextItem, which stays Python's
      own.
    """
    #  void QPainter::drawTextItem(const QPointF &p, const QTextItem &ti)
    self.uglySide.call(
        'ritual_ZN8QPainter12drawTextItemERK7QPointFRK9QTextItem',
        self._valueOf(p), self._valueOf(ti),
    )

  @overload(int, int, QTextItem)
  def drawTextItem(self, x: int, y: int, ti: QTextItem) -> None:
    """
    Calls Qt's 'void QPainter::drawTextItem(int x, int y, const QTextItem
    &ti)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawTextItem

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    ti : QTextItem
      Passed on as a value: Qt reads the C++ QTextItem, which stays Python's
      own.
    """
    #  void QPainter::drawTextItem(int x, int y, const QTextItem &ti)
    self.uglySide.call(
        'ritual_ZN8QPainter12drawTextItemEiiRK9QTextItem',
        x, y, self._valueOf(ti),
    )

  @overload(QPoint, QTextItem)
  def drawTextItem(self, p: QPoint, ti: QTextItem) -> None:
    """
    Calls Qt's 'void QPainter::drawTextItem(const QPoint &p, const QTextItem
    &ti)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#drawTextItem

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    ti : QTextItem
      Passed on as a value: Qt reads the C++ QTextItem, which stays Python's
      own.
    """
    #  void QPainter::drawTextItem(const QPoint &p, const QTextItem &ti)
    self.uglySide.call(
        'ritual_ZN8QPainter12drawTextItemERK6QPointRK9QTextItem',
        self._valueOf(p), self._valueOf(ti),
    )

  @overload(QRectF, QBrush)
  def fillRect(self, a0: QRectF, a1: QBrush) -> None:
    """
    Calls Qt's 'void QPainter::fillRect(const QRectF &a0, const QBrush &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#fillRect

    Parameters
    ----------

    a0 : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    a1 : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QPainter::fillRect(const QRectF &a0, const QBrush &a1)
    self.uglySide.call(
        'ritual_ZN8QPainter8fillRectERK6QRectFRK6QBrush',
        self._valueOf(a0), self._valueOf(a1),
    )

  @overload(int, int, int, int, QBrush)
  def fillRect(self, x: int, y: int, w: int, h: int, a4: QBrush) -> None:
    """
    Calls Qt's 'void QPainter::fillRect(int x, int y, int w, int h, const
    QBrush &a4)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#fillRect

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.

    a4 : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QPainter::fillRect(int x, int y, int w, int h, const QBrush &a4)
    self.uglySide.call(
        'ritual_ZN8QPainter8fillRectEiiiiRK6QBrush',
        x, y, w, h, self._valueOf(a4),
    )

  @overload(QRect, QBrush)
  def fillRect(self, a0: QRect, a1: QBrush) -> None:
    """
    Calls Qt's 'void QPainter::fillRect(const QRect &a0, const QBrush &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#fillRect

    Parameters
    ----------

    a0 : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    a1 : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QPainter::fillRect(const QRect &a0, const QBrush &a1)
    self.uglySide.call(
        'ritual_ZN8QPainter8fillRectERK5QRectRK6QBrush',
        self._valueOf(a0), self._valueOf(a1),
    )

  @overload(QRectF, QColor)
  def fillRect(self, a0: QRectF, color: QColor) -> None:
    """
    Calls Qt's 'void QPainter::fillRect(const QRectF &a0, const QColor
    &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#fillRect

    Parameters
    ----------

    a0 : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QPainter::fillRect(const QRectF &a0, const QColor &color)
    self.uglySide.call(
        'ritual_ZN8QPainter8fillRectERK6QRectFRK6QColor',
        self._valueOf(a0), self._valueOf(color),
    )

  @overload(int, int, int, int, QColor)
  def fillRect(self, x: int, y: int, w: int, h: int, color: QColor) -> None:
    """
    Calls Qt's 'void QPainter::fillRect(int x, int y, int w, int h, const
    QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#fillRect

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QPainter::fillRect(int x, int y, int w, int h, const QColor
    #      &color)
    self.uglySide.call(
        'ritual_ZN8QPainter8fillRectEiiiiRK6QColor',
        x, y, w, h, self._valueOf(color),
    )

  @overload(QRect, QColor)
  def fillRect(self, a0: QRect, color: QColor) -> None:
    """
    Calls Qt's 'void QPainter::fillRect(const QRect &a0, const QColor
    &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#fillRect

    Parameters
    ----------

    a0 : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QPainter::fillRect(const QRect &a0, const QColor &color)
    self.uglySide.call(
        'ritual_ZN8QPainter8fillRectERK5QRectRK6QColor',
        self._valueOf(a0), self._valueOf(color),
    )

  @overload(int, int, int, int, Qt.GlobalColor)
  def fillRect(
      self,
      x: int,
      y: int,
      w: int,
      h: int,
      c: Qt.GlobalColor,
  ) -> None:
    """
    Calls Qt's 'void QPainter::fillRect(int x, int y, int w, int h,
    Qt::GlobalColor c)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#fillRect

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.

    c : Qt.GlobalColor
      Passed on as its number.
    """
    #  void QPainter::fillRect(int x, int y, int w, int h, Qt::GlobalColor c)
    self.uglySide.call(
        'ritual_ZN8QPainter8fillRectEiiiiN2Qt11GlobalColorE',
        x, y, w, h, c.value,
    )

  @overload(QRect, Qt.GlobalColor)
  def fillRect(self, r: QRect, c: Qt.GlobalColor) -> None:
    """
    Calls Qt's 'void QPainter::fillRect(const QRect &r, Qt::GlobalColor c)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#fillRect

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    c : Qt.GlobalColor
      Passed on as its number.
    """
    #  void QPainter::fillRect(const QRect &r, Qt::GlobalColor c)
    self.uglySide.call(
        'ritual_ZN8QPainter8fillRectERK5QRectN2Qt11GlobalColorE',
        self._valueOf(r), c.value,
    )

  @overload(QRectF, Qt.GlobalColor)
  def fillRect(self, r: QRectF, c: Qt.GlobalColor) -> None:
    """
    Calls Qt's 'void QPainter::fillRect(const QRectF &r, Qt::GlobalColor c)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#fillRect

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    c : Qt.GlobalColor
      Passed on as its number.
    """
    #  void QPainter::fillRect(const QRectF &r, Qt::GlobalColor c)
    self.uglySide.call(
        'ritual_ZN8QPainter8fillRectERK6QRectFN2Qt11GlobalColorE',
        self._valueOf(r), c.value,
    )

  @overload(int, int, int, int, Qt.BrushStyle)
  def fillRect(
      self,
      x: int,
      y: int,
      w: int,
      h: int,
      style: Qt.BrushStyle,
  ) -> None:
    """
    Calls Qt's 'void QPainter::fillRect(int x, int y, int w, int h,
    Qt::BrushStyle style)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#fillRect

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.

    style : Qt.BrushStyle
      Passed on as its number.
    """
    #  void QPainter::fillRect(int x, int y, int w, int h, Qt::BrushStyle
    #      style)
    self.uglySide.call(
        'ritual_ZN8QPainter8fillRectEiiiiN2Qt10BrushStyleE',
        x, y, w, h, style.value,
    )

  @overload(QRect, Qt.BrushStyle)
  def fillRect(self, r: QRect, style: Qt.BrushStyle) -> None:
    """
    Calls Qt's 'void QPainter::fillRect(const QRect &r, Qt::BrushStyle
    style)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#fillRect

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    style : Qt.BrushStyle
      Passed on as its number.
    """
    #  void QPainter::fillRect(const QRect &r, Qt::BrushStyle style)
    self.uglySide.call(
        'ritual_ZN8QPainter8fillRectERK5QRectN2Qt10BrushStyleE',
        self._valueOf(r), style.value,
    )

  @overload(QRectF, Qt.BrushStyle)
  def fillRect(self, r: QRectF, style: Qt.BrushStyle) -> None:
    """
    Calls Qt's 'void QPainter::fillRect(const QRectF &r, Qt::BrushStyle
    style)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#fillRect

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    style : Qt.BrushStyle
      Passed on as its number.
    """
    #  void QPainter::fillRect(const QRectF &r, Qt::BrushStyle style)
    self.uglySide.call(
        'ritual_ZN8QPainter8fillRectERK6QRectFN2Qt10BrushStyleE',
        self._valueOf(r), style.value,
    )

  @overload(int, int, int, int, QGradientPreset)
  def fillRect(
      self,
      x: int,
      y: int,
      w: int,
      h: int,
      preset: QGradient.Preset,
  ) -> None:
    """
    Calls Qt's 'void QPainter::fillRect(int x, int y, int w, int h,
    QGradient::Preset preset)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#fillRect

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.

    preset : QGradient.Preset
      Passed on as its number.
    """
    #  void QPainter::fillRect(int x, int y, int w, int h, QGradient::Preset
    #      preset)
    self.uglySide.call(
        'ritual_ZN8QPainter8fillRectEiiiiN9QGradient6PresetE',
        x, y, w, h, preset.value,
    )

  @overload(QRect, QGradientPreset)
  def fillRect(self, r: QRect, preset: QGradient.Preset) -> None:
    """
    Calls Qt's 'void QPainter::fillRect(const QRect &r, QGradient::Preset
    preset)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#fillRect

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    preset : QGradient.Preset
      Passed on as its number.
    """
    #  void QPainter::fillRect(const QRect &r, QGradient::Preset preset)
    self.uglySide.call(
        'ritual_ZN8QPainter8fillRectERK5QRectN9QGradient6PresetE',
        self._valueOf(r), preset.value,
    )

  @overload(QRectF, QGradientPreset)
  def fillRect(self, r: QRectF, preset: QGradient.Preset) -> None:
    """
    Calls Qt's 'void QPainter::fillRect(const QRectF &r, QGradient::Preset
    preset)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#fillRect

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    preset : QGradient.Preset
      Passed on as its number.
    """
    #  void QPainter::fillRect(const QRectF &r, QGradient::Preset preset)
    self.uglySide.call(
        'ritual_ZN8QPainter8fillRectERK6QRectFN9QGradient6PresetE',
        self._valueOf(r), preset.value,
    )

  @overload(QRectF)
  def eraseRect(self, a0: QRectF) -> None:
    """
    Calls Qt's 'void QPainter::eraseRect(const QRectF &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#eraseRect

    Parameters
    ----------

    a0 : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QPainter::eraseRect(const QRectF &a0)
    self.uglySide.call(
        'ritual_ZN8QPainter9eraseRectERK6QRectF', self._valueOf(a0),
    )

  @overload(int, int, int, int)
  def eraseRect(self, x: int, y: int, w: int, h: int) -> None:
    """
    Calls Qt's 'void QPainter::eraseRect(int x, int y, int w, int h)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#eraseRect

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.
    """
    #  void QPainter::eraseRect(int x, int y, int w, int h)
    self.uglySide.call('ritual_ZN8QPainter9eraseRectEiiii', x, y, w, h)

  @overload(QRect)
  def eraseRect(self, a0: QRect) -> None:
    """
    Calls Qt's 'void QPainter::eraseRect(const QRect &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#eraseRect

    Parameters
    ----------

    a0 : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QPainter::eraseRect(const QRect &a0)
    self.uglySide.call(
        'ritual_ZN8QPainter9eraseRectERK5QRect', self._valueOf(a0),
    )

  def beginNativePainting(self) -> None:
    """
    Calls Qt's 'void QPainter::beginNativePainting()'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#beginNativePainting
    """
    #  void QPainter::beginNativePainting()
    self.uglySide.call('ritual_ZN8QPainter19beginNativePaintingEv')

  def endNativePainting(self) -> None:
    """
    Calls Qt's 'void QPainter::endNativePainting()'.

    Qt's own words: https://doc.qt.io/qt-6/qpainter.html#endNativePainting
    """
    #  void QPainter::endNativePainting()
    self.uglySide.call('ritual_ZN8QPainter17endNativePaintingEv')
