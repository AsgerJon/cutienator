"""
QQuickContext2DCommandBuffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickcontext2dcommandbuffer_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickContext2DCommandBuffer to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QPainter
from . import QQuickContext2D

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRectF
  from ..QtGui import QBrush, QColor, QImage, QPainterPath, QPen, QTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QColor = WAIT['QColor']
  QImage = WAIT['QImage']
  QPainterPath = WAIT['QPainterPath']
  QPen = WAIT['QPen']
  QRectF = WAIT['QRectF']
  QTransform = WAIT['QTransform']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickContext2DCommandBuffer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickContext2DCommandBuffer: a plain Python object
  standing in front of one C++ QQuickContext2DCommandBuffer.

  What exists
  -----------

  Every function of Qt's QQuickContext2DCommandBuffer that has a ritual and
  that Python can call so far, 50 names in all: 'reset', 'clear', 'size',
  'isEmpty', 'hasNext', 'takeNextCommand', 'takeGlobalAlpha',
  'takeGlobalCompositeOperation', 'takeStrokeStyle', 'takeFillStyle',
  'takeLineWidth', 'takeLineCap', 'takeLineJoin', 'takeMiterLimit',
  'setGlobalAlpha', 'setGlobalCompositeOperation', 'setStrokeStyle',
  'drawImage', 'takeShadowOffsetX', 'takeShadowOffsetY', 'takeShadowBlur',
  'takeShadowColor', 'updateMatrix', 'clearRect', 'fillRect', 'strokeRect',
  'fill', 'stroke', 'clip', 'setFillStyle', 'setLineWidth', 'setLineCap',
  'setLineJoin', 'setLineDashOffset', 'setMiterLimit', 'setShadowOffsetX',
  'setShadowOffsetY', 'setShadowBlur', 'setShadowColor', 'takeMatrix',
  'takeRect', 'takePath', 'takeImage', 'takeInt', 'takeBool', 'takeReal',
  'takeColor', 'takeBrush', 'makePen', 'setPainterState'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickContext2DCommandBuffer::~QQuickContext2DCommandBuffer()': the
    destructor: Python never removes a C++ QQuickContext2DCommandBuffer.
  - Qt's 'void QQuickContext2DCommandBuffer::drawPixmap(
    QQmlRefPointer<QQuickCanvasPixmap> pixmap, const QRectF &sr, const QRectF
    &dr)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQuickContext2DCommandBuffer::setLineDash(const QList<qreal>
    &pattern)': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlRefPointer<QQuickCanvasPixmap>
    QQuickContext2DCommandBuffer::takePixmap()': gives a type Python has no
    way to take yet.

  What has no ritual
  ------------------

  1 of the 56 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQuickContext2DCommandBuffer is created at the first use, not by
    'QQuickContext2DCommandBuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickContext2DCommandBuffer.
  - Each name of Qt's QQuickContext2DCommandBuffer that has no cute function
    yet, 'drawPixmap', 'replay', 'setLineDash', 'takePixmap', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickContext2D.State)
  def makePen(state: QQuickContext2D.State) -> QPen:
    """
    Calls Qt's 'QPen QQuickContext2DCommandBuffer::makePen(const
    QQuickContext2D::State &state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#makePen

    Parameters
    ----------

    state : QQuickContext2D.State
      Passed on as a value: Qt reads the C++ QQuickContext2D::State, which
      stays Python's own.

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen QQuickContext2DCommandBuffer::makePen(const
    #      QQuickContext2D::State &state)
    address = Rituals.call(
        'ritual_ZN28QQuickContext2DCommandBuffer7makePenERKN15QQuickContext'
        '2D5StateE',
        CuteMixin._valueOf(state),
    )
    from ..QtGui import QPen
    return QPen._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickContext2DCommandBuffer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def size(self) -> int:
    """
    Calls Qt's 'int QQuickContext2DCommandBuffer::size() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#size
    """
    #  int QQuickContext2DCommandBuffer::size() const
    return self.uglySide.call(
        'ritual_ZNK28QQuickContext2DCommandBuffer4sizeEv',
    )

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QQuickContext2DCommandBuffer::isEmpty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#isEmpty
    """
    #  bool QQuickContext2DCommandBuffer::isEmpty() const
    return self.uglySide.call(
        'ritual_ZNK28QQuickContext2DCommandBuffer7isEmptyEv',
    )

  def hasNext(self) -> bool:
    """
    Calls Qt's 'bool QQuickContext2DCommandBuffer::hasNext() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#hasNext
    """
    #  bool QQuickContext2DCommandBuffer::hasNext() const
    return self.uglySide.call(
        'ritual_ZNK28QQuickContext2DCommandBuffer7hasNextEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setGlobalAlpha(self, alpha: float) -> None:
    """
    Calls Qt's 'void QQuickContext2DCommandBuffer::setGlobalAlpha(qreal
    alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#setGlobalAlpha

    Parameters
    ----------

    alpha : float
      Passed on as it is.
    """
    #  void QQuickContext2DCommandBuffer::setGlobalAlpha(qreal alpha)
    self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer14setGlobalAlphaEd', alpha,
    )

  @overload(QPainter.CompositionMode)
  def setGlobalCompositeOperation(
      self,
      cm: QPainter.CompositionMode,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickContext2DCommandBuffer::setGlobalCompositeOperation(QPainter::
    CompositionMode cm)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html

    Parameters
    ----------

    cm : QPainter.CompositionMode
      Passed on as its number.
    """
    #  void QQuickContext2DCommandBuffer::setGlobalCompositeOperation(
    #      QPainter::CompositionMode cm)
    self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer27setGlobalCompositeOperati'
        'onEN8QPainter15CompositionModeE',
        cm.value,
    )

  @overload(QBrush)
  @overload(QBrush, bool)
  @overload(QBrush, bool, bool)
  def setStrokeStyle(
      self,
      style: QBrush,
      repeatX: bool = False,
      repeatY: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QQuickContext2DCommandBuffer::setStrokeStyle(const
    QBrush &style, bool repeatX, bool repeatY)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#setStrokeStyle

    Parameters
    ----------

    style : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.

    repeatX : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    repeatY : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickContext2DCommandBuffer::setStrokeStyle(const QBrush &style,
    #      bool repeatX, bool repeatY)
    self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer14setStrokeStyleERK6QBrushb'
        'b',
        self._valueOf(style), repeatX, repeatY,
    )

  @overload(QBrush)
  @overload(QBrush, bool)
  @overload(QBrush, bool, bool)
  def setFillStyle(
      self,
      style: QBrush,
      repeatX: bool = False,
      repeatY: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QQuickContext2DCommandBuffer::setFillStyle(const QBrush
    &style, bool repeatX, bool repeatY)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#setFillStyle

    Parameters
    ----------

    style : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.

    repeatX : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    repeatY : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickContext2DCommandBuffer::setFillStyle(const QBrush &style,
    #      bool repeatX, bool repeatY)
    self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer12setFillStyleERK6QBrushbb',
        self._valueOf(style), repeatX, repeatY,
    )

  @overload(float)
  def setLineWidth(self, w: float) -> None:
    """
    Calls Qt's 'void QQuickContext2DCommandBuffer::setLineWidth(qreal w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#setLineWidth

    Parameters
    ----------

    w : float
      Passed on as it is.
    """
    #  void QQuickContext2DCommandBuffer::setLineWidth(qreal w)
    self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer12setLineWidthEd', w,
    )

  @overload(Qt.PenCapStyle)
  def setLineCap(self, cap: Qt.PenCapStyle) -> None:
    """
    Calls Qt's 'void QQuickContext2DCommandBuffer::setLineCap(Qt::PenCapStyle
    cap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#setLineCap

    Parameters
    ----------

    cap : Qt.PenCapStyle
      Passed on as its number.
    """
    #  void QQuickContext2DCommandBuffer::setLineCap(Qt::PenCapStyle cap)
    self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer10setLineCapEN2Qt11PenCapSt'
        'yleE',
        cap.value,
    )

  @overload(Qt.PenJoinStyle)
  def setLineJoin(self, join: Qt.PenJoinStyle) -> None:
    """
    Calls Qt's 'void
    QQuickContext2DCommandBuffer::setLineJoin(Qt::PenJoinStyle join)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#setLineJoin

    Parameters
    ----------

    join : Qt.PenJoinStyle
      Passed on as its number.
    """
    #  void QQuickContext2DCommandBuffer::setLineJoin(Qt::PenJoinStyle join)
    self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer11setLineJoinEN2Qt12PenJoin'
        'StyleE',
        join.value,
    )

  @overload(float)
  def setLineDashOffset(self, offset: float) -> None:
    """
    Calls Qt's 'void QQuickContext2DCommandBuffer::setLineDashOffset(qreal
    offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html

    Parameters
    ----------

    offset : float
      Passed on as it is.
    """
    #  void QQuickContext2DCommandBuffer::setLineDashOffset(qreal offset)
    self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer17setLineDashOffsetEd',
        offset,
    )

  @overload(float)
  def setMiterLimit(self, limit: float) -> None:
    """
    Calls Qt's 'void QQuickContext2DCommandBuffer::setMiterLimit(qreal
    limit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#setMiterLimit

    Parameters
    ----------

    limit : float
      Passed on as it is.
    """
    #  void QQuickContext2DCommandBuffer::setMiterLimit(qreal limit)
    self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer13setMiterLimitEd', limit,
    )

  @overload(float)
  def setShadowOffsetX(self, x: float) -> None:
    """
    Calls Qt's 'void QQuickContext2DCommandBuffer::setShadowOffsetX(qreal
    x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#setShadowOffsetX

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QQuickContext2DCommandBuffer::setShadowOffsetX(qreal x)
    self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer16setShadowOffsetXEd', x,
    )

  @overload(float)
  def setShadowOffsetY(self, y: float) -> None:
    """
    Calls Qt's 'void QQuickContext2DCommandBuffer::setShadowOffsetY(qreal
    y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#setShadowOffsetY

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QQuickContext2DCommandBuffer::setShadowOffsetY(qreal y)
    self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer16setShadowOffsetYEd', y,
    )

  @overload(float)
  def setShadowBlur(self, b: float) -> None:
    """
    Calls Qt's 'void QQuickContext2DCommandBuffer::setShadowBlur(qreal b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#setShadowBlur

    Parameters
    ----------

    b : float
      Passed on as it is.
    """
    #  void QQuickContext2DCommandBuffer::setShadowBlur(qreal b)
    self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer13setShadowBlurEd', b,
    )

  @overload(QColor)
  def setShadowColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickContext2DCommandBuffer::setShadowColor(const
    QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#setShadowColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickContext2DCommandBuffer::setShadowColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer14setShadowColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QPainter, QQuickContext2D.State, QPen)
  @overload(NoneType, QQuickContext2D.State, QPen)
  def setPainterState(
      self,
      painter: Optional[QPainter],
      state: QQuickContext2D.State,
      pen: QPen,
  ) -> None:
    """
    Calls Qt's 'void QQuickContext2DCommandBuffer::setPainterState(QPainter
    *painter, const QQuickContext2D::State &state, const QPen &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#setPainterState

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    state : QQuickContext2D.State
      Passed on as a value: Qt reads the C++ QQuickContext2D::State, which
      stays Python's own.

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void QQuickContext2DCommandBuffer::setPainterState(QPainter *painter,
    #      const QQuickContext2D::State &state, const QPen &pen)
    self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer15setPainterStateEP8QPainte'
        'rRKN15QQuickContext2D5StateERK4QPen',
        self._addressOf(painter), self._valueOf(state), self._valueOf(pen),
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
    Notes what was given, for Qt's
    'QQuickContext2DCommandBuffer::QQuickContext2DCommandBuffer()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html
    """
    #  QQuickContext2DCommandBuffer::QQuickContext2DCommandBuffer()
    self._noteCreation(QQuickContext2DCommandBuffer, lambda: Rituals.call(
        'ritual_ZN28QQuickContext2DCommandBufferC1Ev',
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

  def reset(self) -> None:
    """
    Calls Qt's 'void QQuickContext2DCommandBuffer::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#reset
    """
    #  void QQuickContext2DCommandBuffer::reset()
    self.uglySide.call('ritual_ZN28QQuickContext2DCommandBuffer5resetEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QQuickContext2DCommandBuffer::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#clear
    """
    #  void QQuickContext2DCommandBuffer::clear()
    self.uglySide.call('ritual_ZN28QQuickContext2DCommandBuffer5clearEv')

  def takeNextCommand(self) -> QQuickContext2D.PaintCommand:
    """
    Calls Qt's 'QQuickContext2D::PaintCommand
    QQuickContext2DCommandBuffer::takeNextCommand()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#takeNextCommand

    Returns
    -------

    QQuickContext2D.PaintCommand
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickContext2D.PaintCommand(number)' gives.
    """
    #  QQuickContext2D::PaintCommand
    #      QQuickContext2DCommandBuffer::takeNextCommand()
    return QQuickContext2D.PaintCommand(self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer15takeNextCommandEv',
    ))

  def takeGlobalAlpha(self) -> float:
    """
    Calls Qt's 'qreal QQuickContext2DCommandBuffer::takeGlobalAlpha()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#takeGlobalAlpha
    """
    #  qreal QQuickContext2DCommandBuffer::takeGlobalAlpha()
    return self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer15takeGlobalAlphaEv',
    )

  def takeGlobalCompositeOperation(self) -> QPainter.CompositionMode:
    """
    Calls Qt's 'QPainter::CompositionMode
    QQuickContext2DCommandBuffer::takeGlobalCompositeOperation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html

    Returns
    -------

    QPainter.CompositionMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPainter.CompositionMode(number)' gives.
    """
    #  QPainter::CompositionMode
    #      QQuickContext2DCommandBuffer::takeGlobalCompositeOperation()
    return QPainter.CompositionMode(self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer28takeGlobalCompositeOperat'
        'ionEv',
    ))

  def takeStrokeStyle(self) -> QBrush:
    """
    Calls Qt's 'QBrush QQuickContext2DCommandBuffer::takeStrokeStyle()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#takeStrokeStyle

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QQuickContext2DCommandBuffer::takeStrokeStyle()
    address = self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer15takeStrokeStyleEv',
    )
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def takeFillStyle(self) -> QBrush:
    """
    Calls Qt's 'QBrush QQuickContext2DCommandBuffer::takeFillStyle()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#takeFillStyle

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QQuickContext2DCommandBuffer::takeFillStyle()
    address = self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer13takeFillStyleEv',
    )
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def takeLineWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickContext2DCommandBuffer::takeLineWidth()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#takeLineWidth
    """
    #  qreal QQuickContext2DCommandBuffer::takeLineWidth()
    return self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer13takeLineWidthEv',
    )

  def takeLineCap(self) -> Qt.PenCapStyle:
    """
    Calls Qt's 'Qt::PenCapStyle QQuickContext2DCommandBuffer::takeLineCap()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#takeLineCap

    Returns
    -------

    Qt.PenCapStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.PenCapStyle(number)'
      gives.
    """
    #  Qt::PenCapStyle QQuickContext2DCommandBuffer::takeLineCap()
    return Qt.PenCapStyle(self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer11takeLineCapEv',
    ))

  def takeLineJoin(self) -> Qt.PenJoinStyle:
    """
    Calls Qt's 'Qt::PenJoinStyle
    QQuickContext2DCommandBuffer::takeLineJoin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#takeLineJoin

    Returns
    -------

    Qt.PenJoinStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.PenJoinStyle(number)'
      gives.
    """
    #  Qt::PenJoinStyle QQuickContext2DCommandBuffer::takeLineJoin()
    return Qt.PenJoinStyle(self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer12takeLineJoinEv',
    ))

  def takeMiterLimit(self) -> float:
    """
    Calls Qt's 'qreal QQuickContext2DCommandBuffer::takeMiterLimit()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#takeMiterLimit
    """
    #  qreal QQuickContext2DCommandBuffer::takeMiterLimit()
    return self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer14takeMiterLimitEv',
    )

  @overload(QImage, QRectF, QRectF)
  def drawImage(self, image: QImage, sr: QRectF, dr: QRectF) -> None:
    """
    Calls Qt's 'void QQuickContext2DCommandBuffer::drawImage(const QImage
    &image, const QRectF &sr, const QRectF &dr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#drawImage

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    sr : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    dr : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickContext2DCommandBuffer::drawImage(const QImage &image,
    #      const QRectF &sr, const QRectF &dr)
    self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer9drawImageERK6QImageRK6QRec'
        'tFS5_',
        self._valueOf(image), self._valueOf(sr), self._valueOf(dr),
    )

  def takeShadowOffsetX(self) -> float:
    """
    Calls Qt's 'qreal QQuickContext2DCommandBuffer::takeShadowOffsetX()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html
    """
    #  qreal QQuickContext2DCommandBuffer::takeShadowOffsetX()
    return self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer17takeShadowOffsetXEv',
    )

  def takeShadowOffsetY(self) -> float:
    """
    Calls Qt's 'qreal QQuickContext2DCommandBuffer::takeShadowOffsetY()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html
    """
    #  qreal QQuickContext2DCommandBuffer::takeShadowOffsetY()
    return self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer17takeShadowOffsetYEv',
    )

  def takeShadowBlur(self) -> float:
    """
    Calls Qt's 'qreal QQuickContext2DCommandBuffer::takeShadowBlur()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#takeShadowBlur
    """
    #  qreal QQuickContext2DCommandBuffer::takeShadowBlur()
    return self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer14takeShadowBlurEv',
    )

  def takeShadowColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickContext2DCommandBuffer::takeShadowColor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#takeShadowColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickContext2DCommandBuffer::takeShadowColor()
    address = self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer15takeShadowColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload(QTransform)
  def updateMatrix(self, matrix: QTransform) -> None:
    """
    Calls Qt's 'void QQuickContext2DCommandBuffer::updateMatrix(const
    QTransform &matrix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#updateMatrix

    Parameters
    ----------

    matrix : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  void QQuickContext2DCommandBuffer::updateMatrix(const QTransform
    #      &matrix)
    self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer12updateMatrixERK10QTransfo'
        'rm',
        self._valueOf(matrix),
    )

  @overload(QRectF)
  def clearRect(self, r: QRectF) -> None:
    """
    Calls Qt's 'void QQuickContext2DCommandBuffer::clearRect(const QRectF
    &r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#clearRect

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickContext2DCommandBuffer::clearRect(const QRectF &r)
    self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer9clearRectERK6QRectF',
        self._valueOf(r),
    )

  @overload(QRectF)
  def fillRect(self, r: QRectF) -> None:
    """
    Calls Qt's 'void QQuickContext2DCommandBuffer::fillRect(const QRectF
    &r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#fillRect

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickContext2DCommandBuffer::fillRect(const QRectF &r)
    self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer8fillRectERK6QRectF',
        self._valueOf(r),
    )

  @overload(QRectF)
  def strokeRect(self, r: QRectF) -> None:
    """
    Calls Qt's 'void QQuickContext2DCommandBuffer::strokeRect(const QRectF
    &r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#strokeRect

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickContext2DCommandBuffer::strokeRect(const QRectF &r)
    self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer10strokeRectERK6QRectF',
        self._valueOf(r),
    )

  @overload(QPainterPath)
  def fill(self, path: QPainterPath) -> None:
    """
    Calls Qt's 'void QQuickContext2DCommandBuffer::fill(const QPainterPath
    &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#fill

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.
    """
    #  void QQuickContext2DCommandBuffer::fill(const QPainterPath &path)
    self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer4fillERK12QPainterPath',
        self._valueOf(path),
    )

  @overload(QPainterPath)
  def stroke(self, path: QPainterPath) -> None:
    """
    Calls Qt's 'void QQuickContext2DCommandBuffer::stroke(const QPainterPath
    &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#stroke

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.
    """
    #  void QQuickContext2DCommandBuffer::stroke(const QPainterPath &path)
    self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer6strokeERK12QPainterPath',
        self._valueOf(path),
    )

  @overload(bool, QPainterPath)
  def clip(self, enabled: bool, path: QPainterPath) -> None:
    """
    Calls Qt's 'void QQuickContext2DCommandBuffer::clip(bool enabled, const
    QPainterPath &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#clip

    Parameters
    ----------

    enabled : bool
      Passed on as it is.

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.
    """
    #  void QQuickContext2DCommandBuffer::clip(bool enabled, const
    #      QPainterPath &path)
    self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer4clipEbRK12QPainterPath',
        enabled, self._valueOf(path),
    )

  def takeMatrix(self) -> QTransform:
    """
    Calls Qt's 'QTransform QQuickContext2DCommandBuffer::takeMatrix()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#takeMatrix

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QQuickContext2DCommandBuffer::takeMatrix()
    address = self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer10takeMatrixEv',
    )
    from ..QtGui import QTransform
    return QTransform._cuteOwning(address)

  def takeRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickContext2DCommandBuffer::takeRect()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#takeRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickContext2DCommandBuffer::takeRect()
    address = self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer8takeRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def takePath(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QQuickContext2DCommandBuffer::takePath()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#takePath

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QQuickContext2DCommandBuffer::takePath()
    address = self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer8takePathEv',
    )
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  def takeImage(self) -> QImage:
    """
    Calls Qt's 'const QImage &QQuickContext2DCommandBuffer::takeImage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#takeImage

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  const QImage &QQuickContext2DCommandBuffer::takeImage()
    address = self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer9takeImageEv',
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def takeInt(self) -> int:
    """
    Calls Qt's 'int QQuickContext2DCommandBuffer::takeInt()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#takeInt
    """
    #  int QQuickContext2DCommandBuffer::takeInt()
    return self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer7takeIntEv',
    )

  def takeBool(self) -> bool:
    """
    Calls Qt's 'bool QQuickContext2DCommandBuffer::takeBool()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#takeBool
    """
    #  bool QQuickContext2DCommandBuffer::takeBool()
    return self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer8takeBoolEv',
    )

  def takeReal(self) -> float:
    """
    Calls Qt's 'qreal QQuickContext2DCommandBuffer::takeReal()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#takeReal
    """
    #  qreal QQuickContext2DCommandBuffer::takeReal()
    return self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer8takeRealEv',
    )

  def takeColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickContext2DCommandBuffer::takeColor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#takeColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickContext2DCommandBuffer::takeColor()
    address = self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer9takeColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def takeBrush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QQuickContext2DCommandBuffer::takeBrush()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dcommandbuffer.html#takeBrush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QQuickContext2DCommandBuffer::takeBrush()
    address = self.uglySide.call(
        'ritual_ZN28QQuickContext2DCommandBuffer9takeBrushEv',
    )
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  @staticmethod
  def drawPixmap(*__, **_) -> Never:
    """
    Qt's 'void QQuickContext2DCommandBuffer::drawPixmap(
    QQmlRefPointer<QQuickCanvasPixmap> pixmap, const QRectF &sr, const QRectF
    &dr)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickContext2DCommandBuffer.drawPixmap' has no cute function "
        "yet. Qt's 'void "
        "QQuickContext2DCommandBuffer::drawPixmap(QQmlRefPointer<QQuickCanva"
        "sPixmap> pixmap, const QRectF &sr, const QRectF &dr)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def replay(*__, **_) -> Never:
    """
    Qt's 'void QQuickContext2DCommandBuffer::replay(QPainter *painter,
    QQuickContext2D::State &state, const QVector2D &scaleFactor)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'HAS_SHADOW'.
    """
    raise NotImplementedError(
        "'QQuickContext2DCommandBuffer.replay' has no cute function yet. "
        "Qt's 'void QQuickContext2DCommandBuffer::replay(QPainter *painter, "
        "QQuickContext2D::State &state, const QVector2D &scaleFactor)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'HAS_SHADOW'.")

  @staticmethod
  def setLineDash(*__, **_) -> Never:
    """
    Qt's 'void QQuickContext2DCommandBuffer::setLineDash(const QList<qreal>
    &pattern)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickContext2DCommandBuffer.setLineDash' has no cute function "
        "yet. Qt's 'void QQuickContext2DCommandBuffer::setLineDash(const "
        "QList<qreal> &pattern)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def takePixmap(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QQuickCanvasPixmap>
    QQuickContext2DCommandBuffer::takePixmap()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QQuickContext2DCommandBuffer.takePixmap' has no cute function "
        "yet. Qt's 'QQmlRefPointer<QQuickCanvasPixmap> "
        "QQuickContext2DCommandBuffer::takePixmap()': gives a type Python "
        "has no way to take yet.")
