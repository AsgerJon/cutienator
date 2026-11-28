"""
QColrPaintGraphRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qcolrpaintgraphrenderer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QColrPaintGraphRenderer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QGradient, QPainter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QRect, QRectF
  from . import QColor, QImage, QPainterPath, QTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QImage = WAIT['QImage']
  QPainterPath = WAIT['QPainterPath']
  QRect = WAIT['QRect']
  QRectF = WAIT['QRectF']
  QTransform = WAIT['QTransform']


class QColrPaintGraphRenderer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QColrPaintGraphRenderer: a plain Python object
  standing in front of one C++ QColrPaintGraphRenderer.

  C++ hands a QColrPaintGraphRenderer around as a copy, so every C++
  QColrPaintGraphRenderer behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QColrPaintGraphRenderer that has a ritual and that
  Python can call so far, 18 names in all: 'setBoundingRect', 'boundingRect',
  'currentTransform', 'currentPath', 'save', 'restore', 'appendPath',
  'setPath', 'prependTransform', 'setSolidColor', 'setCompositionMode',
  'drawCurrentPath', 'drawImage', 'setClip', 'beginCalculateBoundingBox',
  'beginRender', 'endRender', 'isRendering'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QColrPaintGraphRenderer::~QColrPaintGraphRenderer()': the
    destructor: Python removes its C++ QColrPaintGraphRenderer by it, and has
    no other use for it.
  - Qt's 'void QColrPaintGraphRenderer::setRadialGradient(QPointF c0, qreal
    r0, QPointF c1, qreal r1, QGradient::Spread spread, const QGradientStops
    &gradientStops)': takes a type Python has no way to hand over yet.
  - Qt's 'void QColrPaintGraphRenderer::setLinearGradient(QPointF p0, QPointF
    p1, QPointF p2, QGradient::Spread spread, const QGradientStops
    &gradientStops)': takes a type Python has no way to hand over yet.
  - Qt's 'void QColrPaintGraphRenderer::setConicalGradient(QPointF center,
    qreal startAngle, qreal endAngle, QGradient::Spread spread, const
    QGradientStops &gradientStops)': takes a type Python has no way to hand
    over yet.

  What to expect
  --------------

  - The C++ QColrPaintGraphRenderer is created at the first use, not by
    'QColrPaintGraphRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QColrPaintGraphRenderer back gives a copy the ritual
    made for Python, in a new cute QColrPaintGraphRenderer.
  - Each name of Qt's QColrPaintGraphRenderer that has no cute function yet,
    'setConicalGradient', 'setLinearGradient', 'setRadialGradient', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QColrPaintGraphRenderer'

  #  Qt's '~QColrPaintGraphRenderer()'. Naming it makes this a value class:
  #  Python owns every C++ QColrPaintGraphRenderer behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QColrPaintGraphRendererD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QColrPaintGraphRenderer::boundingRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolrpaintgraphrenderer.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QColrPaintGraphRenderer::boundingRect() const
    address = self.uglySide.call(
        'ritual_ZNK23QColrPaintGraphRenderer12boundingRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def currentTransform(self) -> QTransform:
    """
    Calls Qt's 'QTransform QColrPaintGraphRenderer::currentTransform()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolrpaintgraphrenderer.html#currentTransform

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QColrPaintGraphRenderer::currentTransform() const
    address = self.uglySide.call(
        'ritual_ZNK23QColrPaintGraphRenderer16currentTransformEv',
    )
    from . import QTransform
    return QTransform._cuteOwning(address)

  def currentPath(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QColrPaintGraphRenderer::currentPath() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolrpaintgraphrenderer.html#currentPath

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QColrPaintGraphRenderer::currentPath() const
    address = self.uglySide.call(
        'ritual_ZNK23QColrPaintGraphRenderer11currentPathEv',
    )
    from . import QPainterPath
    return QPainterPath._cuteOwning(address)

  def isRendering(self) -> bool:
    """
    Calls Qt's 'bool QColrPaintGraphRenderer::isRendering() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolrpaintgraphrenderer.html#isRendering
    """
    #  bool QColrPaintGraphRenderer::isRendering() const
    return self.uglySide.call(
        'ritual_ZNK23QColrPaintGraphRenderer11isRenderingEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF)
  def setBoundingRect(self, boundingRect: QRectF) -> None:
    """
    Calls Qt's 'void QColrPaintGraphRenderer::setBoundingRect(QRectF
    boundingRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolrpaintgraphrenderer.html#setBoundingRect

    Parameters
    ----------

    boundingRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QColrPaintGraphRenderer::setBoundingRect(QRectF boundingRect)
    self.uglySide.call(
        'ritual_ZN23QColrPaintGraphRenderer15setBoundingRectE6QRectF',
        self._valueOf(boundingRect),
    )

  @overload(QPainterPath)
  def setPath(self, path: QPainterPath) -> None:
    """
    Calls Qt's 'void QColrPaintGraphRenderer::setPath(const QPainterPath
    &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolrpaintgraphrenderer.html#setPath

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.
    """
    #  void QColrPaintGraphRenderer::setPath(const QPainterPath &path)
    self.uglySide.call(
        'ritual_ZN23QColrPaintGraphRenderer7setPathERK12QPainterPath',
        self._valueOf(path),
    )

  @overload(QColor)
  def setSolidColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QColrPaintGraphRenderer::setSolidColor(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolrpaintgraphrenderer.html#setSolidColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QColrPaintGraphRenderer::setSolidColor(QColor color)
    self.uglySide.call(
        'ritual_ZN23QColrPaintGraphRenderer13setSolidColorE6QColor',
        self._valueOf(color),
    )

  @overload(QPainter.CompositionMode)
  def setCompositionMode(self, mode: QPainter.CompositionMode) -> None:
    """
    Calls Qt's 'void
    QColrPaintGraphRenderer::setCompositionMode(QPainter::CompositionMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolrpaintgraphrenderer.html#setCompositionMode

    Parameters
    ----------

    mode : QPainter.CompositionMode
      Passed on as its number.
    """
    #  void QColrPaintGraphRenderer::setCompositionMode(QPainter::
    #      CompositionMode mode)
    self.uglySide.call(
        'ritual_ZN23QColrPaintGraphRenderer18setCompositionModeEN8QPainter1'
        '5CompositionModeE',
        mode.value,
    )

  @overload(QRect)
  def setClip(self, rect: QRect) -> None:
    """
    Calls Qt's 'void QColrPaintGraphRenderer::setClip(QRect rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolrpaintgraphrenderer.html#setClip

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QColrPaintGraphRenderer::setClip(QRect rect)
    self.uglySide.call(
        'ritual_ZN23QColrPaintGraphRenderer7setClipE5QRect',
        self._valueOf(rect),
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
    Calls Qt's 'void QColrPaintGraphRenderer::save()'.

    Qt's own words: https://doc.qt.io/qt-6/qcolrpaintgraphrenderer.html#save
    """
    #  void QColrPaintGraphRenderer::save()
    self.uglySide.call('ritual_ZN23QColrPaintGraphRenderer4saveEv')

  def restore(self) -> None:
    """
    Calls Qt's 'void QColrPaintGraphRenderer::restore()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolrpaintgraphrenderer.html#restore
    """
    #  void QColrPaintGraphRenderer::restore()
    self.uglySide.call('ritual_ZN23QColrPaintGraphRenderer7restoreEv')

  @overload(QPainterPath)
  def appendPath(self, path: QPainterPath) -> None:
    """
    Calls Qt's 'void QColrPaintGraphRenderer::appendPath(const QPainterPath
    &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolrpaintgraphrenderer.html#appendPath

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.
    """
    #  void QColrPaintGraphRenderer::appendPath(const QPainterPath &path)
    self.uglySide.call(
        'ritual_ZN23QColrPaintGraphRenderer10appendPathERK12QPainterPath',
        self._valueOf(path),
    )

  @overload(QTransform)
  def prependTransform(self, transform: QTransform) -> None:
    """
    Calls Qt's 'void QColrPaintGraphRenderer::prependTransform(const
    QTransform &transform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolrpaintgraphrenderer.html#prependTransform

    Parameters
    ----------

    transform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  void QColrPaintGraphRenderer::prependTransform(const QTransform
    #      &transform)
    self.uglySide.call(
        'ritual_ZN23QColrPaintGraphRenderer16prependTransformERK10QTransfor'
        'm',
        self._valueOf(transform),
    )

  def drawCurrentPath(self) -> None:
    """
    Calls Qt's 'void QColrPaintGraphRenderer::drawCurrentPath()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolrpaintgraphrenderer.html#drawCurrentPath
    """
    #  void QColrPaintGraphRenderer::drawCurrentPath()
    self.uglySide.call(
        'ritual_ZN23QColrPaintGraphRenderer15drawCurrentPathEv',
    )

  @overload(QImage)
  def drawImage(self, image: QImage) -> None:
    """
    Calls Qt's 'void QColrPaintGraphRenderer::drawImage(const QImage
    &image)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolrpaintgraphrenderer.html#drawImage

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QColrPaintGraphRenderer::drawImage(const QImage &image)
    self.uglySide.call(
        'ritual_ZN23QColrPaintGraphRenderer9drawImageERK6QImage',
        self._valueOf(image),
    )

  def beginCalculateBoundingBox(self) -> None:
    """
    Calls Qt's 'void QColrPaintGraphRenderer::beginCalculateBoundingBox()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolrpaintgraphrenderer.html
    """
    #  void QColrPaintGraphRenderer::beginCalculateBoundingBox()
    self.uglySide.call(
        'ritual_ZN23QColrPaintGraphRenderer25beginCalculateBoundingBoxEv',
    )

  @overload(float, QTransform)
  def beginRender(
      self,
      pixelSizeScale: float,
      transform: QTransform,
  ) -> None:
    """
    Calls Qt's 'void QColrPaintGraphRenderer::beginRender(qreal
    pixelSizeScale, const QTransform &transform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolrpaintgraphrenderer.html#beginRender

    Parameters
    ----------

    pixelSizeScale : float
      Passed on as it is.

    transform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  void QColrPaintGraphRenderer::beginRender(qreal pixelSizeScale, const
    #      QTransform &transform)
    self.uglySide.call(
        'ritual_ZN23QColrPaintGraphRenderer11beginRenderEdRK10QTransform',
        pixelSizeScale, self._valueOf(transform),
    )

  def endRender(self) -> QImage:
    """
    Calls Qt's 'QImage QColrPaintGraphRenderer::endRender()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolrpaintgraphrenderer.html#endRender

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QColrPaintGraphRenderer::endRender()
    address = self.uglySide.call(
        'ritual_ZN23QColrPaintGraphRenderer9endRenderEv',
    )
    from . import QImage
    return QImage._cuteOwning(address)

  @staticmethod
  def setConicalGradient(*__, **_) -> Never:
    """
    Qt's 'void QColrPaintGraphRenderer::setConicalGradient(QPointF center,
    qreal startAngle, qreal endAngle, QGradient::Spread spread, const
    QGradientStops &gradientStops)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QColrPaintGraphRenderer.setConicalGradient' has no cute function "
        "yet. Qt's 'void "
        "QColrPaintGraphRenderer::setConicalGradient(QPointF center, qreal "
        "startAngle, qreal endAngle, QGradient::Spread spread, const "
        "QGradientStops &gradientStops)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def setLinearGradient(*__, **_) -> Never:
    """
    Qt's 'void QColrPaintGraphRenderer::setLinearGradient(QPointF p0, QPointF
    p1, QPointF p2, QGradient::Spread spread, const QGradientStops
    &gradientStops)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QColrPaintGraphRenderer.setLinearGradient' has no cute function "
        "yet. Qt's 'void QColrPaintGraphRenderer::setLinearGradient(QPointF "
        "p0, QPointF p1, QPointF p2, QGradient::Spread spread, const "
        "QGradientStops &gradientStops)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def setRadialGradient(*__, **_) -> Never:
    """
    Qt's 'void QColrPaintGraphRenderer::setRadialGradient(QPointF c0, qreal
    r0, QPointF c1, qreal r1, QGradient::Spread spread, const QGradientStops
    &gradientStops)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QColrPaintGraphRenderer.setRadialGradient' has no cute function "
        "yet. Qt's 'void QColrPaintGraphRenderer::setRadialGradient(QPointF "
        "c0, qreal r0, QPointF c1, qreal r1, QGradient::Spread spread, "
        "const QGradientStops &gradientStops)': takes a type Python has no "
        "way to hand over yet.")
