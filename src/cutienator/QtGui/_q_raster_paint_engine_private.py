"""
QRasterPaintEnginePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qpaintengine_raster_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QRasterPaintEnginePrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QPaintEngineExPrivate, QPainter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF, QRect, QRectF
  from . import QClipData, QImage, QRasterPaintEngine, QTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']
  QPointF = WAIT['QPointF']
  QRect = WAIT['QRect']
  QRectF = WAIT['QRectF']


class QRasterPaintEnginePrivate(QPaintEngineExPrivate):
  """
  The cute side of Qt's QRasterPaintEnginePrivate: a plain Python object
  standing in front of one C++ QRasterPaintEnginePrivate.

  It is built on the cute 'QPaintEngineExPrivate', as Qt's
  QRasterPaintEnginePrivate is built on Qt's QPaintEngineExPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QRasterPaintEnginePrivate that has a ritual and that
  Python can call so far, 10 names in all: 'q_func', 'updateClipping',
  'systemStateChanged', 'blitImage', 'brushMatrix', 'isUnclipped_normalized',
  'isUnclipped', 'clip', 'recalculateFastImages', 'canUseFastImageBlending'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QRasterPaintEngine *QRasterPaintEnginePrivate::q_func()
    const': takes in Python what 'QRasterPaintEngine
    *QRasterPaintEnginePrivate::q_func()' takes.
  - Qt's 'void QRasterPaintEnginePrivate::drawImage(const QPointF &pt, const
    QImage &img, SrcOverBlendFunc func, const QRect &clip, int alpha, const
    QRect &sr)': takes a type Python has no way to hand over yet.
  - Qt's 'ProcessSpans QRasterPaintEnginePrivate::getPenFunc(const QRectF
    &rect, const QSpanData *data) const': gives a type Python has no way to
    take yet.
  - Qt's 'ProcessSpans QRasterPaintEnginePrivate::getBrushFunc(const QRect
    &rect, const QSpanData *data) const': gives a type Python has no way to
    take yet.
  - Qt's 'ProcessSpans QRasterPaintEnginePrivate::getBrushFunc(const QRectF
    &rect, const QSpanData *data) const': gives a type Python has no way to
    take yet.

  What has no ritual
  ------------------

  6 of the 23 functions Qt declares: 3 leans on 'QRasterizer; 2 Qt's library
  has no name for it, and its code in Qt's source does not compile apart from
  its file; 1 leans on 'QSpanData.

  What to expect
  --------------

  - The C++ QRasterPaintEnginePrivate is created at the first use, not by
    'QRasterPaintEnginePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRasterPaintEnginePrivate.
  - Each name of Qt's QRasterPaintEnginePrivate that has no cute function
    yet, 'canUseImageBlitting', 'drawImage', 'getBrushFunc', 'getPenFunc',
    'initializeRasterizer', 'rasterize', 'rasterizeLine_dashed',
    'updateMatrixData', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRasterPaintEnginePrivate'

  #  A C++ QRasterPaintEnginePrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRasterPaintEnginePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def brushMatrix(self) -> QTransform:
    """
    Calls Qt's 'QTransform QRasterPaintEnginePrivate::brushMatrix() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengineprivate.html#brushMatrix

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QRasterPaintEnginePrivate::brushMatrix() const
    address = self.uglySide.call(
        'ritual_ZNK25QRasterPaintEnginePrivate11brushMatrixEv',
    )
    from . import QTransform
    return QTransform._cuteOwning(address)

  @overload(QRect)
  def isUnclipped_normalized(self, rect: QRect) -> bool:
    """
    Calls Qt's 'bool QRasterPaintEnginePrivate::isUnclipped_normalized(const
    QRect &rect) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengineprivate.html

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  bool QRasterPaintEnginePrivate::isUnclipped_normalized(const QRect
    #      &rect) const
    return self.uglySide.call(
        'ritual_ZNK25QRasterPaintEnginePrivate22isUnclipped_normalizedERK5Q'
        'Rect',
        self._valueOf(rect),
    )

  @overload(QRect, int)
  def isUnclipped(self, rect: QRect, penWidth: int) -> bool:
    """
    Calls Qt's 'bool QRasterPaintEnginePrivate::isUnclipped(const QRect
    &rect, int penWidth) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengineprivate.html#isUnclipped

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    penWidth : int
      Passed on as it is.
    """
    #  bool QRasterPaintEnginePrivate::isUnclipped(const QRect &rect, int
    #      penWidth) const
    return self.uglySide.call(
        'ritual_ZNK25QRasterPaintEnginePrivate11isUnclippedERK5QRecti',
        self._valueOf(rect), penWidth,
    )

  @overload(QRectF, int)
  def isUnclipped(self, rect: QRectF, penWidth: int) -> bool:
    """
    Calls Qt's 'bool QRasterPaintEnginePrivate::isUnclipped(const QRectF
    &rect, int penWidth) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengineprivate.html#isUnclipped

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    penWidth : int
      Passed on as it is.
    """
    #  bool QRasterPaintEnginePrivate::isUnclipped(const QRectF &rect, int
    #      penWidth) const
    return self.uglySide.call(
        'ritual_ZNK25QRasterPaintEnginePrivate11isUnclippedERK6QRectFi',
        self._valueOf(rect), penWidth,
    )

  def clip(self) -> Optional[QClipData]:
    """
    Calls Qt's 'const QClipData *QRasterPaintEnginePrivate::clip() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengineprivate.html#clip

    Returns
    -------

    Optional[QClipData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QClipData *QRasterPaintEnginePrivate::clip() const
    address = self.uglySide.call(
        'ritual_ZNK25QRasterPaintEnginePrivate4clipEv',
    )
    from . import QClipData
    return QClipData._cuteAt(address)

  @overload(QPainter.CompositionMode, QImage)
  def canUseFastImageBlending(
      self,
      mode: QPainter.CompositionMode,
      image: QImage,
  ) -> bool:
    """
    Calls Qt's 'bool
    QRasterPaintEnginePrivate::canUseFastImageBlending(QPainter::
    CompositionMode mode, const QImage &image) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengineprivate.html

    Parameters
    ----------

    mode : QPainter.CompositionMode
      Passed on as its number.

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  bool QRasterPaintEnginePrivate::canUseFastImageBlending(QPainter::
    #      CompositionMode mode, const QImage &image) const
    return self.uglySide.call(
        'ritual_ZNK25QRasterPaintEnginePrivate23canUseFastImageBlendingEN8Q'
        'Painter15CompositionModeERK6QImage',
        mode.value, self._valueOf(image),
    )

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
    'QRasterPaintEnginePrivate::QRasterPaintEnginePrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengineprivate.html
    """
    #  QRasterPaintEnginePrivate::QRasterPaintEnginePrivate()
    self._noteCreation(QRasterPaintEnginePrivate, lambda: Rituals.call(
        'ritual_ZN25QRasterPaintEnginePrivateC1Ev',
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

  def q_func(self) -> Optional[QRasterPaintEngine]:
    """
    Calls Qt's 'QRasterPaintEngine *QRasterPaintEnginePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengineprivate.html#q_func

    Returns
    -------

    Optional[QRasterPaintEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRasterPaintEngine *QRasterPaintEnginePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN25QRasterPaintEnginePrivate6q_funcEv',
    )
    from . import QRasterPaintEngine
    return QRasterPaintEngine._cuteAt(address)

  def updateClipping(self) -> None:
    """
    Calls Qt's 'void QRasterPaintEnginePrivate::updateClipping()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengineprivate.html#updateClipping
    """
    #  void QRasterPaintEnginePrivate::updateClipping()
    self.uglySide.call(
        'ritual_ZN25QRasterPaintEnginePrivate14updateClippingEv',
    )

  def systemStateChanged(self) -> None:
    """
    Calls Qt's 'void QRasterPaintEnginePrivate::systemStateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengineprivate.html#systemStateChanged
    """
    #  void QRasterPaintEnginePrivate::systemStateChanged()
    ritual = 'ritual_ZN25QRasterPaintEnginePrivate18systemStateChangedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QRasterPaintEnginePrivate18systemStateChangedEv')
    self.uglySide.call(ritual)

  @overload(QPointF, QImage, QRect)
  @overload(QPointF, QImage, QRect, QRect)
  def blitImage(
      self,
      pt: QPointF,
      img: QImage,
      clip: QRect,
      sr: Optional[QRect] = None,
  ) -> None:
    """
    Calls Qt's 'void QRasterPaintEnginePrivate::blitImage(const QPointF &pt,
    const QImage &img, const QRect &clip, const QRect &sr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengineprivate.html#blitImage

    Parameters
    ----------

    pt : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    img : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    clip : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    sr : Optional[QRect]
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
      May be left out, as in Qt: a new 'QRect()' is then passed on.
    """
    #  void QRasterPaintEnginePrivate::blitImage(const QPointF &pt, const
    #      QImage &img, const QRect &clip, const QRect &sr)
    if sr is None:
      from ..QtCore import QRect
      sr = QRect()
    self.uglySide.call(
        'ritual_ZN25QRasterPaintEnginePrivate9blitImageERK7QPointFRK6QImage'
        'RK5QRectS8_',
        self._valueOf(pt, 'QPointF'), self._valueOf(img),
        self._valueOf(clip), self._valueOf(sr),
    )

  def recalculateFastImages(self) -> None:
    """
    Calls Qt's 'void QRasterPaintEnginePrivate::recalculateFastImages()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengineprivate.html
    """
    #  void QRasterPaintEnginePrivate::recalculateFastImages()
    self.uglySide.call(
        'ritual_ZN25QRasterPaintEnginePrivate21recalculateFastImagesEv',
    )

  @staticmethod
  def canUseImageBlitting(*__, **_) -> Never:
    """
    Qt's 'bool
    QRasterPaintEnginePrivate::canUseImageBlitting(QPainter::CompositionMode
    mode, const QImage &image, const QPointF &pt, const QRectF &sr) const':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: no matching function for call to
    'isPixelAligned'.
    """
    raise NotImplementedError(
        "'QRasterPaintEnginePrivate.canUseImageBlitting' has no cute "
        "function yet. Qt's 'bool "
        "QRasterPaintEnginePrivate::canUseImageBlitting(QPainter::Compositio"
        "nMode mode, const QImage &image, const QPointF &pt, const QRectF "
        "&sr) const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: no matching function "
        "for call to 'isPixelAligned'.")

  @staticmethod
  def drawImage(*__, **_) -> Never:
    """
    Qt's 'void QRasterPaintEnginePrivate::drawImage(const QPointF &pt, const
    QImage &img, SrcOverBlendFunc func, const QRect &clip, int alpha, const
    QRect &sr)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QRasterPaintEnginePrivate.drawImage' has no cute function yet. "
        "Qt's 'void QRasterPaintEnginePrivate::drawImage(const QPointF &pt, "
        "const QImage &img, SrcOverBlendFunc func, const QRect &clip, int "
        "alpha, const QRect &sr)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def getBrushFunc(*__, **_) -> Never:
    """
    - Qt's 'ProcessSpans QRasterPaintEnginePrivate::getBrushFunc(const QRect
      &rect, const QSpanData *data) const': gives a type Python has no way to
      take yet.
    - Qt's 'ProcessSpans QRasterPaintEnginePrivate::getBrushFunc(const QRectF
      &rect, const QSpanData *data) const': gives a type Python has no way to
      take yet.
    """
    raise NotImplementedError(
        "'QRasterPaintEnginePrivate.getBrushFunc' has no cute function yet. "
        "Qt's 'ProcessSpans QRasterPaintEnginePrivate::getBrushFunc(const "
        "QRect &rect, const QSpanData *data) const': gives a type Python "
        "has no way to take yet. Qt's 'ProcessSpans "
        "QRasterPaintEnginePrivate::getBrushFunc(const QRectF &rect, const "
        "QSpanData *data) const': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def getPenFunc(*__, **_) -> Never:
    """
    Qt's 'ProcessSpans QRasterPaintEnginePrivate::getPenFunc(const QRectF
    &rect, const QSpanData *data) const': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QRasterPaintEnginePrivate.getPenFunc' has no cute function yet. "
        "Qt's 'ProcessSpans QRasterPaintEnginePrivate::getPenFunc(const "
        "QRectF &rect, const QSpanData *data) const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def initializeRasterizer(*__, **_) -> Never:
    """
    Qt's 'void QRasterPaintEnginePrivate::initializeRasterizer(QSpanData
    *data)': leans on 'QRasterizer::initialize(void (*)(int, QT_FT_Span_
    const*, void*), void*)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QRasterPaintEnginePrivate.initializeRasterizer' has no cute "
        "function yet. Qt's 'void "
        "QRasterPaintEnginePrivate::initializeRasterizer(QSpanData *data)': "
        "leans on 'QRasterizer::initialize(void (*)(int, QT_FT_Span_ "
        "const*, void*), void*)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def rasterize(*__, **_) -> Never:
    """
    - Qt's 'void QRasterPaintEnginePrivate::rasterize(QT_FT_Outline *outline,
      ProcessSpans callback, void *userData, QRasterBuffer *rasterBuffer)':
      Qt's library has no name for it, and its code in Qt's source does not
      compile apart from its file: use of undeclared identifier
      'q_gray_rendered_spans'.
    - Qt's 'void QRasterPaintEnginePrivate::rasterize(QT_FT_Outline *outline,
      ProcessSpans callback, QSpanData *spanData, QRasterBuffer
      *rasterBuffer)': leans on 'QRasterizer::rasterize(QT_FT_Outline_
      const*, Qt::FillRule)', which Qt's source does not mark for use from
      outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QRasterPaintEnginePrivate.rasterize' has no cute function yet. "
        "Qt's 'void QRasterPaintEnginePrivate::rasterize(QT_FT_Outline "
        "*outline, ProcessSpans callback, void *userData, QRasterBuffer "
        "*rasterBuffer)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'q_gray_rendered_spans'. Qt's 'void "
        "QRasterPaintEnginePrivate::rasterize(QT_FT_Outline *outline, "
        "ProcessSpans callback, QSpanData *spanData, QRasterBuffer "
        "*rasterBuffer)': leans on 'QRasterizer::rasterize(QT_FT_Outline_ "
        "const*, Qt::FillRule)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def rasterizeLine_dashed(*__, **_) -> Never:
    """
    Qt's 'void QRasterPaintEnginePrivate::rasterizeLine_dashed(QLineF line,
    qreal width, int *dashIndex, qreal *dashOffset, bool *inDash)': leans on
    'QRasterizer::rasterizeLine(QPointF const&, QPointF const&, double,
    bool)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QRasterPaintEnginePrivate.rasterizeLine_dashed' has no cute "
        "function yet. Qt's 'void "
        "QRasterPaintEnginePrivate::rasterizeLine_dashed(QLineF line, qreal "
        "width, int *dashIndex, qreal *dashOffset, bool *inDash)': leans on "
        "'QRasterizer::rasterizeLine(QPointF const&, QPointF const&, "
        "double, bool)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def updateMatrixData(*__, **_) -> Never:
    """
    Qt's 'void QRasterPaintEnginePrivate::updateMatrixData(QSpanData
    *spanData, const QBrush &brush, const QTransform &brushMatrix)': leans on
    'QSpanData::adjustSpanMethods()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QRasterPaintEnginePrivate.updateMatrixData' has no cute function "
        "yet. Qt's 'void "
        "QRasterPaintEnginePrivate::updateMatrixData(QSpanData *spanData, "
        "const QBrush &brush, const QTransform &brushMatrix)': leans on "
        "'QSpanData::adjustSpanMethods()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")
