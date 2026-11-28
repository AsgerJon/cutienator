"""
QBlittablePlatformPixmap binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qpixmap_blitter_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QBlittablePlatformPixmap to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QPaintDevice, QPlatformPixmap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPoint, QPointF, QRect, QRectF, QSize
  from . import QBlittable, QColor, QImage, QPaintEngine, QPainterPath
  from . import QTextItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBlittable = WAIT['QBlittable']
  QColor = WAIT['QColor']
  QImage = WAIT['QImage']
  QPainterPath = WAIT['QPainterPath']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QRect = WAIT['QRect']
  QRectF = WAIT['QRectF']
  QSize = WAIT['QSize']
  QTextItem = WAIT['QTextItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBlittablePlatformPixmap(QPlatformPixmap):
  """
  The cute side of Qt's QBlittablePlatformPixmap: a plain Python object
  standing in front of one C++ QBlittablePlatformPixmap.

  It is built on the cute 'QPlatformPixmap', as Qt's QBlittablePlatformPixmap
  is built on Qt's QPlatformPixmap, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBlittablePlatformPixmap that has a ritual and that
  Python can call so far, 15 names in all: 'createBlittable', 'blittable',
  'setBlittable', 'resize', 'metric', 'fill', 'buffer', 'toImage',
  'hasAlphaChannel', 'fromImage', 'devicePixelRatio', 'setDevicePixelRatio',
  'paintEngine', 'markRasterOverlay', 'unmarkRasterOverlay'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QBlittablePlatformPixmap::~QBlittablePlatformPixmap()': the
    destructor: Python never removes a C++ QBlittablePlatformPixmap.
  - Qt's 'void QBlittablePlatformPixmap::markRasterOverlay(const QVectorPath
    &a0)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QBlittablePlatformPixmap is created at the first use, not by
    'QBlittablePlatformPixmap(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBlittablePlatformPixmap.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBlittablePlatformPixmap'

  #  A C++ QBlittablePlatformPixmap Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBlittablePlatformPixmap'

  #  The functions Qt calls itself that QBlittablePlatformPixmap is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'createBlittable': (
          ('_ZNK24QBlittablePlatformPixmap15createBlittableERK5QSizeb',
           ('address', 'address', 'QtGui:QBlittable'),
           (
               ('address', 'value', 'QtCore:QSize'),
               ('bool', 'number', ''),
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

  @overload(QSize, bool)
  def createBlittable(
      self,
      size: QSize,
      alpha: bool,
  ) -> Optional[QBlittable]:
    """
    Calls Qt's 'QBlittable *QBlittablePlatformPixmap::createBlittable(const
    QSize &size, bool alpha) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblittableplatformpixmap.html#createBlittable

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    alpha : bool
      Passed on as it is.

    Returns
    -------

    Optional[QBlittable]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBlittable *QBlittablePlatformPixmap::createBlittable(const QSize
    #      &size, bool alpha) const
    address = self.uglySide.call(
        'ritual_ZNK24QBlittablePlatformPixmap15createBlittableERK5QSizeb',
        self._valueOf(size), alpha,
    )
    from . import QBlittable
    return QBlittable._cuteAt(address)

  def blittable(self) -> Optional[QBlittable]:
    """
    Calls Qt's 'QBlittable *QBlittablePlatformPixmap::blittable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblittableplatformpixmap.html#blittable

    Returns
    -------

    Optional[QBlittable]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBlittable *QBlittablePlatformPixmap::blittable() const
    address = self.uglySide.call(
        'ritual_ZNK24QBlittablePlatformPixmap9blittableEv',
    )
    from . import QBlittable
    return QBlittable._cuteAt(address)

  @overload(QPaintDevice.PaintDeviceMetric)
  def metric(self, metric: QPaintDevice.PaintDeviceMetric) -> int:
    """
    Calls Qt's 'int
    QBlittablePlatformPixmap::metric(QPaintDevice::PaintDeviceMetric metric)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblittableplatformpixmap.html#metric

    Parameters
    ----------

    metric : QPaintDevice.PaintDeviceMetric
      Passed on as its number.
    """
    #  int QBlittablePlatformPixmap::metric(QPaintDevice::PaintDeviceMetric
    #      metric) const
    ritual = (
        'ritual_ZNK24QBlittablePlatformPixmap6metricEN12QPaintDevice17Paint'
        'DeviceMetricE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QBlittablePlatformPixmap6metricEN12QPaintDevice1'
          '7PaintDeviceMetricE')
    return self.uglySide.call(ritual, metric.value)

  def toImage(self) -> QImage:
    """
    Calls Qt's 'QImage QBlittablePlatformPixmap::toImage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblittableplatformpixmap.html#toImage

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QBlittablePlatformPixmap::toImage() const
    ritual = 'ritual_ZNK24QBlittablePlatformPixmap7toImageEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QBlittablePlatformPixmap7toImageEv'
    address = self.uglySide.call(ritual)
    from . import QImage
    return QImage._cuteOwning(address)

  def hasAlphaChannel(self) -> bool:
    """
    Calls Qt's 'bool QBlittablePlatformPixmap::hasAlphaChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblittableplatformpixmap.html#hasAlphaChannel
    """
    #  bool QBlittablePlatformPixmap::hasAlphaChannel() const
    ritual = 'ritual_ZNK24QBlittablePlatformPixmap15hasAlphaChannelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QBlittablePlatformPixmap15hasAlphaChannelEv'
    return self.uglySide.call(ritual)

  def devicePixelRatio(self) -> float:
    """
    Calls Qt's 'qreal QBlittablePlatformPixmap::devicePixelRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblittableplatformpixmap.html#devicePixelRatio
    """
    #  qreal QBlittablePlatformPixmap::devicePixelRatio() const
    ritual = 'ritual_ZNK24QBlittablePlatformPixmap16devicePixelRatioEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QBlittablePlatformPixmap16devicePixelRatioEv'
    return self.uglySide.call(ritual)

  def paintEngine(self) -> Optional[QPaintEngine]:
    """
    Calls Qt's 'QPaintEngine *QBlittablePlatformPixmap::paintEngine() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblittableplatformpixmap.html#paintEngine

    Returns
    -------

    Optional[QPaintEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintEngine *QBlittablePlatformPixmap::paintEngine() const
    ritual = 'ritual_ZNK24QBlittablePlatformPixmap11paintEngineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QBlittablePlatformPixmap11paintEngineEv'
    address = self.uglySide.call(ritual)
    from . import QPaintEngine
    return QPaintEngine._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QBlittable)
  @overload(NoneType)
  def setBlittable(self, blittable: Optional[QBlittable]) -> None:
    """
    Calls Qt's 'void QBlittablePlatformPixmap::setBlittable(QBlittable
    *blittable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblittableplatformpixmap.html#setBlittable

    Parameters
    ----------

    blittable : Optional[QBlittable]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBlittablePlatformPixmap::setBlittable(QBlittable *blittable)
    self.uglySide.call(
        'ritual_ZN24QBlittablePlatformPixmap12setBlittableEP10QBlittable',
        self._addressOf(blittable),
    )

  @overload(float)
  def setDevicePixelRatio(self, scaleFactor: float) -> None:
    """
    Calls Qt's 'void QBlittablePlatformPixmap::setDevicePixelRatio(qreal
    scaleFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblittableplatformpixmap.html#setDevicePixelRatio

    Parameters
    ----------

    scaleFactor : float
      Passed on as it is.
    """
    #  void QBlittablePlatformPixmap::setDevicePixelRatio(qreal scaleFactor)
    ritual = 'ritual_ZN24QBlittablePlatformPixmap19setDevicePixelRatioEd'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QBlittablePlatformPixmap19setDevicePixelRatioEd')
    self.uglySide.call(ritual, scaleFactor)

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
    'QBlittablePlatformPixmap::QBlittablePlatformPixmap()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qblittableplatformpixmap.html
    """
    #  QBlittablePlatformPixmap::QBlittablePlatformPixmap()
    self._noteCreation(QBlittablePlatformPixmap, lambda: Rituals.call(
        'ritual_ZN24QBlittablePlatformPixmapC1Ev',
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

  @overload(int, int)
  def resize(self, width: int, height: int) -> None:
    """
    Calls Qt's 'void QBlittablePlatformPixmap::resize(int width, int
    height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblittableplatformpixmap.html#resize

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void QBlittablePlatformPixmap::resize(int width, int height)
    ritual = 'ritual_ZN24QBlittablePlatformPixmap6resizeEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QBlittablePlatformPixmap6resizeEii'
    self.uglySide.call(ritual, width, height)

  @overload(QColor)
  def fill(self, color: QColor) -> None:
    """
    Calls Qt's 'void QBlittablePlatformPixmap::fill(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qblittableplatformpixmap.html#fill

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QBlittablePlatformPixmap::fill(const QColor &color)
    ritual = 'ritual_ZN24QBlittablePlatformPixmap4fillERK6QColor'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QBlittablePlatformPixmap4fillERK6QColor'
    self.uglySide.call(ritual, self._valueOf(color))

  def buffer(self) -> Optional[QImage]:
    """
    Calls Qt's 'QImage *QBlittablePlatformPixmap::buffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblittableplatformpixmap.html#buffer

    Returns
    -------

    Optional[QImage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QImage *QBlittablePlatformPixmap::buffer()
    ritual = 'ritual_ZN24QBlittablePlatformPixmap6bufferEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QBlittablePlatformPixmap6bufferEv'
    address = self.uglySide.call(ritual)
    from . import QImage
    return QImage._cuteAt(address)

  @overload(QImage, Qt.ImageConversionFlags)
  def fromImage(self, image: QImage, flags: Qt.ImageConversionFlags) -> None:
    """
    Calls Qt's 'void QBlittablePlatformPixmap::fromImage(const QImage &image,
    Qt::ImageConversionFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblittableplatformpixmap.html#fromImage

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    flags : Qt.ImageConversionFlags
      Passed on as its number.
    """
    #  void QBlittablePlatformPixmap::fromImage(const QImage &image,
    #      Qt::ImageConversionFlags flags)
    ritual = (
        'ritual_ZN24QBlittablePlatformPixmap9fromImageERK6QImage6QFlagsIN2Q'
        't19ImageConversionFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QBlittablePlatformPixmap9fromImageERK6QImage6QFla'
          'gsIN2Qt19ImageConversionFlagEE')
    self.uglySide.call(ritual, self._valueOf(image), flags.value)

  @overload(QRectF)
  def markRasterOverlay(self, a0: QRectF) -> None:
    """
    Calls Qt's 'void QBlittablePlatformPixmap::markRasterOverlay(const QRectF
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblittableplatformpixmap.html#markRasterOverlay

    Parameters
    ----------

    a0 : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QBlittablePlatformPixmap::markRasterOverlay(const QRectF &a0)
    self.uglySide.call(
        'ritual_ZN24QBlittablePlatformPixmap17markRasterOverlayERK6QRectF',
        self._valueOf(a0),
    )

  @overload(QPointF, QTextItem)
  def markRasterOverlay(self, a0: QPointF, a1: QTextItem) -> None:
    """
    Calls Qt's 'void QBlittablePlatformPixmap::markRasterOverlay(const
    QPointF &a0, const QTextItem &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblittableplatformpixmap.html#markRasterOverlay

    Parameters
    ----------

    a0 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    a1 : QTextItem
      Passed on as a value: Qt reads the C++ QTextItem, which stays Python's
      own.
    """
    #  void QBlittablePlatformPixmap::markRasterOverlay(const QPointF &a0,
    #      const QTextItem &a1)
    self.uglySide.call(
        'ritual_ZN24QBlittablePlatformPixmap17markRasterOverlayERK7QPointFR'
        'K9QTextItem',
        self._valueOf(a0, 'QPointF'), self._valueOf(a1),
    )

  @overload(QPainterPath)
  def markRasterOverlay(self, a0: QPainterPath) -> None:
    """
    Calls Qt's 'void QBlittablePlatformPixmap::markRasterOverlay(const
    QPainterPath &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblittableplatformpixmap.html#markRasterOverlay

    Parameters
    ----------

    a0 : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.
    """
    #  void QBlittablePlatformPixmap::markRasterOverlay(const QPainterPath
    #      &a0)
    self.uglySide.call(
        'ritual_ZN24QBlittablePlatformPixmap17markRasterOverlayERK12QPainte'
        'rPath',
        self._valueOf(a0),
    )

  @overload(QRect, int)
  @overload(NoneType, int)
  def markRasterOverlay(
      self,
      rects: Optional[QRect],
      rectCount: int,
  ) -> None:
    """
    Calls Qt's 'void QBlittablePlatformPixmap::markRasterOverlay(const QRect
    *rects, int rectCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblittableplatformpixmap.html#markRasterOverlay

    Parameters
    ----------

    rects : Optional[QRect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rectCount : int
      Passed on as it is.
    """
    #  void QBlittablePlatformPixmap::markRasterOverlay(const QRect *rects,
    #      int rectCount)
    self.uglySide.call(
        'ritual_ZN24QBlittablePlatformPixmap17markRasterOverlayEPK5QRecti',
        self._addressOf(rects), rectCount,
    )

  @overload(QRectF, int)
  def markRasterOverlay(
      self,
      rects: Optional[QRectF],
      rectCount: int,
  ) -> None:
    """
    Calls Qt's 'void QBlittablePlatformPixmap::markRasterOverlay(const QRectF
    *rects, int rectCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblittableplatformpixmap.html#markRasterOverlay

    Parameters
    ----------

    rects : Optional[QRectF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rectCount : int
      Passed on as it is.
    """
    #  void QBlittablePlatformPixmap::markRasterOverlay(const QRectF *rects,
    #      int rectCount)
    self.uglySide.call(
        'ritual_ZN24QBlittablePlatformPixmap17markRasterOverlayEPK6QRectFi',
        self._addressOf(rects), rectCount,
    )

  @overload(QPointF, int)
  def markRasterOverlay(
      self,
      points: Optional[QPointF],
      pointCount: int,
  ) -> None:
    """
    Calls Qt's 'void QBlittablePlatformPixmap::markRasterOverlay(const
    QPointF *points, int pointCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblittableplatformpixmap.html#markRasterOverlay

    Parameters
    ----------

    points : Optional[QPointF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pointCount : int
      Passed on as it is.
    """
    #  void QBlittablePlatformPixmap::markRasterOverlay(const QPointF
    #      *points, int pointCount)
    self.uglySide.call(
        'ritual_ZN24QBlittablePlatformPixmap17markRasterOverlayEPK7QPointFi',
        self._addressOf(points, 'QPointF'), pointCount,
    )

  @overload(QPoint, int)
  def markRasterOverlay(
      self,
      points: Optional[QPoint],
      pointCount: int,
  ) -> None:
    """
    Calls Qt's 'void QBlittablePlatformPixmap::markRasterOverlay(const QPoint
    *points, int pointCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblittableplatformpixmap.html#markRasterOverlay

    Parameters
    ----------

    points : Optional[QPoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pointCount : int
      Passed on as it is.
    """
    #  void QBlittablePlatformPixmap::markRasterOverlay(const QPoint *points,
    #      int pointCount)
    self.uglySide.call(
        'ritual_ZN24QBlittablePlatformPixmap17markRasterOverlayEPK6QPointi',
        self._addressOf(points), pointCount,
    )

  @overload(QRectF)
  def unmarkRasterOverlay(self, a0: QRectF) -> None:
    """
    Calls Qt's 'void QBlittablePlatformPixmap::unmarkRasterOverlay(const
    QRectF &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblittableplatformpixmap.html#unmarkRasterOverlay

    Parameters
    ----------

    a0 : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QBlittablePlatformPixmap::unmarkRasterOverlay(const QRectF &a0)
    self.uglySide.call(
        'ritual_ZN24QBlittablePlatformPixmap19unmarkRasterOverlayERK6QRectF',
        self._valueOf(a0),
    )
