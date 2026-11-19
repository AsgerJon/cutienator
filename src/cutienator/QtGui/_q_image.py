"""
QImage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qimage.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import Qt
from ..QtCore import QByteArray
from ..QtCore import QByteArrayView
from ._q_color import QColor
from ._q_color_space import QColorSpace
from ..QtCore import QIODevice
from ._q_paint_device import QPaintDevice
from ..QtCore import QPoint
from ..QtCore import QRect
from ..QtCore import QSize
from ..QtCore import QSizeF
from ._q_transform import QTransform
from ._q_image_format import Format
from ._q_image_invert_mode import InvertMode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QImage(QPaintDevice):
  """
  The cute side of Qt's QImage: a plain Python object standing in front of
  one C++ QImage.

  It is built on the cute 'QPaintDevice', as Qt's QImage is built on Qt's
  QPaintDevice, and has everything that class has.

  C++ hands a QImage around as a copy, so every C++ QImage behind a cute one
  is Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QImage that has a ritual and that Python can call so
  far, 68 names in all: 'isNull', 'devType', 'detach', 'isDetached', 'copy',
  'format', 'convertToFormat', 'reinterpretAsFormat', 'convertedTo',
  'convertTo', 'width', 'height', 'size', 'rect', 'depth', 'colorCount',
  'bitPlaneCount', 'color', 'setColor', 'setColorCount', 'allGray',
  'isGrayscale', 'sizeInBytes', 'bytesPerLine', 'valid', 'pixelIndex',
  'pixel', 'setPixel', 'pixelColor', 'setPixelColor', 'devicePixelRatio',
  'setDevicePixelRatio', 'deviceIndependentSize', 'fill', 'hasAlphaChannel',
  'setAlphaChannel', 'createAlphaMask', 'createHeuristicMask',
  'createMaskFromColor', 'scaled', 'scaledToWidth', 'scaledToHeight',
  'transformed', 'trueMatrix', 'mirrored', 'mirror', 'rgbSwapped', 'flipped',
  'flip', 'rgbSwap', 'invertPixels', 'colorSpace', 'convertedToColorSpace',
  'convertToColorSpace', 'setColorSpace', 'load', 'loadFromData', 'save',
  'fromData', 'cacheKey', 'dotsPerMeterX', 'dotsPerMeterY',
  'setDotsPerMeterX', 'setDotsPerMeterY', 'offset', 'setOffset', 'text',
  'setText'. It can be made from Python, in 5 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QImage::~QImage()': the destructor: Python removes its C++ QImage
    by it, and has no other use for it.
  - Qt's 'bool QImage::operator==(const QImage &a0) const': an operator,
    which is not reflected yet.
  - Qt's 'bool QImage::operator!=(const QImage &a0) const': an operator,
    which is not reflected yet.
  - Qt's 'QVariant QImage::operator QVariant() const': an operator, which is
    not reflected yet.
  - Qt's 'QImage QImage::colorTransformed(const QColorTransform &transform)
    const': names 'QColorTransform', which has no cute class yet.
  - Qt's 'QImage QImage::colorTransformed(const QColorTransform &transform,
    QImage::Format format, Qt::ImageConversionFlags flags) const': names
    'QColorTransform', which has no cute class yet.
  - Qt's 'void QImage::applyColorTransform(const QColorTransform
    &transform)': names 'QColorTransform', which has no cute class yet.
  - Qt's 'void QImage::applyColorTransform(const QColorTransform &transform,
    QImage::Format format, Qt::ImageConversionFlags flags)': names
    'QColorTransform', which has no cute class yet.
  - Qt's 'QPaintEngine *QImage::paintEngine() const': gives 'QPaintEngine',
    which has no cute class yet.
  - Qt's 'QPixelFormat QImage::pixelFormat() const': gives 'QPixelFormat',
    which has no cute class yet.
  - Qt's 'QPixelFormat QImage::toPixelFormat(QImage::Format format)': gives
    'QPixelFormat', which has no cute class yet.
  - Qt's 'QImage::Format QImage::toImageFormat(QPixelFormat format)': names
    'QPixelFormat', which has no cute class yet.

  What has no ritual
  ------------------

  42 of the 143 functions Qt declares: 22 takes or gives a type that cannot
  be passed yet; 9 protected; 8 can only be called on a value about to be
  thrown away; 1 declared and nowhere to be found; 1 a template; 1 private.

  What to expect
  --------------

  - The C++ QImage is created at the first use, not by 'QImage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QImage back gives a copy the ritual made for Python,
    in a new cute QImage.
  """

  #  The enums Qt writes inside QImage, and the names Qt has for the
  #  combinations of its flags enums.
  Format = Format
  InvertMode = InvertMode

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QTransform, int, int)
  def trueMatrix(a0: QTransform, w: int, h: int) -> QTransform:
    """
    Calls Qt's 'QTransform QImage::trueMatrix(const QTransform &a0, int w,
    int h)'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#trueMatrix

    Parameters
    ----------

    a0 : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QImage::trueMatrix(const QTransform &a0, int w, int h)
    address = Rituals.call(
        'ritual_ZN6QImage10trueMatrixERK10QTransformii',
        CuteMixin._valueOf(a0), w, h,
    )
    return QTransform._cuteOwning(address)

  @staticmethod
  @overload(QByteArrayView)
  @overload(QByteArrayView, str)
  @overload(QByteArrayView, NoneType)
  def fromData(data: QByteArrayView, format: Optional[str] = None) -> QImage:
    """
    Calls Qt's 'QImage QImage::fromData(QByteArrayView data, const char
    *format)'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#fromData

    Parameters
    ----------

    data : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    format : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QImage::fromData(QByteArrayView data, const char *format)
    address = Rituals.call(
        'ritual_ZN6QImage8fromDataE14QByteArrayViewPKc',
        CuteMixin._valueOf(data), CuteMixin._bytesOf(format),
    )
    return QImage._cuteOwning(address)

  @staticmethod
  @overload(QByteArray)
  @overload(QByteArray, str)
  @overload(QByteArray, NoneType)
  def fromData(data: QByteArray, format: Optional[str] = None) -> QImage:
    """
    Calls Qt's 'QImage QImage::fromData(const QByteArray &data, const char
    *format)'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#fromData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    format : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QImage::fromData(const QByteArray &data, const char *format)
    address = Rituals.call(
        'ritual_ZN6QImage8fromDataERK10QByteArrayPKc',
        CuteMixin._valueOf(data), CuteMixin._bytesOf(format),
    )
    return QImage._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QImage'

  #  Qt's '~QImage()'. Naming it makes this a value class: Python owns every
  #  C++ QImage behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QImageD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QImage::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#isNull
    """
    #  bool QImage::isNull() const
    return self.uglySide.call('ritual_ZNK6QImage6isNullEv')

  def devType(self) -> int:
    """
    Calls Qt's 'int QImage::devType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#devType
    """
    #  int QImage::devType() const
    return self.uglySide.call('ritual_ZNK6QImage7devTypeEv')

  def isDetached(self) -> bool:
    """
    Calls Qt's 'bool QImage::isDetached() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#isDetached
    """
    #  bool QImage::isDetached() const
    return self.uglySide.call('ritual_ZNK6QImage10isDetachedEv')

  @overload()
  @overload(QRect)
  def copy(self, rect: Optional[QRect] = None) -> QImage:
    """
    Calls Qt's 'QImage QImage::copy(const QRect &rect) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#copy

    Parameters
    ----------

    rect : Optional[QRect]
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
      May be left out, as in Qt: a new 'QRect()' is then passed on.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QImage::copy(const QRect &rect) const
    if rect is None:
      rect = QRect()
    address = self.uglySide.call(
        'ritual_ZNK6QImage4copyERK5QRect', self._valueOf(rect),
    )
    return QImage._cuteOwning(address)

  @overload(int, int, int, int)
  def copy(self, x: int, y: int, w: int, h: int) -> QImage:
    """
    Calls Qt's 'QImage QImage::copy(int x, int y, int w, int h) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#copy

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

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QImage::copy(int x, int y, int w, int h) const
    address = self.uglySide.call('ritual_ZNK6QImage4copyEiiii', x, y, w, h)
    return QImage._cuteOwning(address)

  def format(self) -> Format:
    """
    Calls Qt's 'Format QImage::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#format

    Returns
    -------

    Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Format(number)' gives.
    """
    #  Format QImage::format() const
    return Format(self.uglySide.call('ritual_ZNK6QImage6formatEv'))

  @overload(Format)
  @overload(Format, Qt.ImageConversionFlags)
  def convertToFormat(
      self,
      f: Format,
      flags: Qt.ImageConversionFlags = Qt.ImageConversionFlags.AutoColor,
  ) -> QImage:
    """
    Calls Qt's 'QImage QImage::convertToFormat(Format f,
    Qt::ImageConversionFlags flags) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#convertToFormat

    Parameters
    ----------

    f : Format
      Passed on as its number.

    flags : Qt.ImageConversionFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ImageConversionFlags.AutoColor.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QImage::convertToFormat(Format f, Qt::ImageConversionFlags
    #      flags) const
    address = self.uglySide.call(
        'ritual_ZNKR6QImage15convertToFormatENS_6FormatE6QFlagsIN2Qt19Image'
        'ConversionFlagEE',
        f.value, flags.value,
    )
    return QImage._cuteOwning(address)

  @overload(Format)
  @overload(Format, Qt.ImageConversionFlags)
  def convertedTo(
      self,
      f: Format,
      flags: Qt.ImageConversionFlags = Qt.ImageConversionFlags.AutoColor,
  ) -> QImage:
    """
    Calls Qt's 'QImage QImage::convertedTo(Format f, Qt::ImageConversionFlags
    flags) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#convertedTo

    Parameters
    ----------

    f : Format
      Passed on as its number.

    flags : Qt.ImageConversionFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ImageConversionFlags.AutoColor.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QImage::convertedTo(Format f, Qt::ImageConversionFlags flags)
    #      const
    address = self.uglySide.call(
        'ritual_ZNKR6QImage11convertedToENS_6FormatE6QFlagsIN2Qt19ImageConv'
        'ersionFlagEE',
        f.value, flags.value,
    )
    return QImage._cuteOwning(address)

  def width(self) -> int:
    """
    Calls Qt's 'int QImage::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#width
    """
    #  int QImage::width() const
    return self.uglySide.call('ritual_ZNK6QImage5widthEv')

  def height(self) -> int:
    """
    Calls Qt's 'int QImage::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#height
    """
    #  int QImage::height() const
    return self.uglySide.call('ritual_ZNK6QImage6heightEv')

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QImage::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QImage::size() const
    address = self.uglySide.call('ritual_ZNK6QImage4sizeEv')
    return QSize._cuteOwning(address)

  def rect(self) -> QRect:
    """
    Calls Qt's 'QRect QImage::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#rect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QImage::rect() const
    address = self.uglySide.call('ritual_ZNK6QImage4rectEv')
    return QRect._cuteOwning(address)

  def depth(self) -> int:
    """
    Calls Qt's 'int QImage::depth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#depth
    """
    #  int QImage::depth() const
    return self.uglySide.call('ritual_ZNK6QImage5depthEv')

  def colorCount(self) -> int:
    """
    Calls Qt's 'int QImage::colorCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#colorCount
    """
    #  int QImage::colorCount() const
    return self.uglySide.call('ritual_ZNK6QImage10colorCountEv')

  def bitPlaneCount(self) -> int:
    """
    Calls Qt's 'int QImage::bitPlaneCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#bitPlaneCount
    """
    #  int QImage::bitPlaneCount() const
    return self.uglySide.call('ritual_ZNK6QImage13bitPlaneCountEv')

  @overload(int)
  def color(self, i: int) -> int:
    """
    Calls Qt's 'QRgb QImage::color(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#color

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  QRgb QImage::color(int i) const
    return self.uglySide.call('ritual_ZNK6QImage5colorEi', i)

  def allGray(self) -> bool:
    """
    Calls Qt's 'bool QImage::allGray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#allGray
    """
    #  bool QImage::allGray() const
    return self.uglySide.call('ritual_ZNK6QImage7allGrayEv')

  def isGrayscale(self) -> bool:
    """
    Calls Qt's 'bool QImage::isGrayscale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#isGrayscale
    """
    #  bool QImage::isGrayscale() const
    return self.uglySide.call('ritual_ZNK6QImage11isGrayscaleEv')

  def sizeInBytes(self) -> int:
    """
    Calls Qt's 'qsizetype QImage::sizeInBytes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#sizeInBytes
    """
    #  qsizetype QImage::sizeInBytes() const
    return self.uglySide.call('ritual_ZNK6QImage11sizeInBytesEv')

  def bytesPerLine(self) -> int:
    """
    Calls Qt's 'qsizetype QImage::bytesPerLine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#bytesPerLine
    """
    #  qsizetype QImage::bytesPerLine() const
    return self.uglySide.call('ritual_ZNK6QImage12bytesPerLineEv')

  @overload(int, int)
  def valid(self, x: int, y: int) -> bool:
    """
    Calls Qt's 'bool QImage::valid(int x, int y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#valid

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  bool QImage::valid(int x, int y) const
    return self.uglySide.call('ritual_ZNK6QImage5validEii', x, y)

  @overload(QPoint)
  def valid(self, pt: QPoint) -> bool:
    """
    Calls Qt's 'bool QImage::valid(const QPoint &pt) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#valid

    Parameters
    ----------

    pt : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  bool QImage::valid(const QPoint &pt) const
    return self.uglySide.call(
        'ritual_ZNK6QImage5validERK6QPoint', self._valueOf(pt),
    )

  @overload(int, int)
  def pixelIndex(self, x: int, y: int) -> int:
    """
    Calls Qt's 'int QImage::pixelIndex(int x, int y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#pixelIndex

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  int QImage::pixelIndex(int x, int y) const
    return self.uglySide.call('ritual_ZNK6QImage10pixelIndexEii', x, y)

  @overload(QPoint)
  def pixelIndex(self, pt: QPoint) -> int:
    """
    Calls Qt's 'int QImage::pixelIndex(const QPoint &pt) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#pixelIndex

    Parameters
    ----------

    pt : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  int QImage::pixelIndex(const QPoint &pt) const
    return self.uglySide.call(
        'ritual_ZNK6QImage10pixelIndexERK6QPoint', self._valueOf(pt),
    )

  @overload(int, int)
  def pixel(self, x: int, y: int) -> int:
    """
    Calls Qt's 'QRgb QImage::pixel(int x, int y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#pixel

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  QRgb QImage::pixel(int x, int y) const
    return self.uglySide.call('ritual_ZNK6QImage5pixelEii', x, y)

  @overload(QPoint)
  def pixel(self, pt: QPoint) -> int:
    """
    Calls Qt's 'QRgb QImage::pixel(const QPoint &pt) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#pixel

    Parameters
    ----------

    pt : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  QRgb QImage::pixel(const QPoint &pt) const
    return self.uglySide.call(
        'ritual_ZNK6QImage5pixelERK6QPoint', self._valueOf(pt),
    )

  @overload(int, int)
  def pixelColor(self, x: int, y: int) -> QColor:
    """
    Calls Qt's 'QColor QImage::pixelColor(int x, int y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#pixelColor

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QImage::pixelColor(int x, int y) const
    address = self.uglySide.call('ritual_ZNK6QImage10pixelColorEii', x, y)
    return QColor._cuteOwning(address)

  @overload(QPoint)
  def pixelColor(self, pt: QPoint) -> QColor:
    """
    Calls Qt's 'QColor QImage::pixelColor(const QPoint &pt) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#pixelColor

    Parameters
    ----------

    pt : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QImage::pixelColor(const QPoint &pt) const
    address = self.uglySide.call(
        'ritual_ZNK6QImage10pixelColorERK6QPoint', self._valueOf(pt),
    )
    return QColor._cuteOwning(address)

  def devicePixelRatio(self) -> float:
    """
    Calls Qt's 'qreal QImage::devicePixelRatio() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#devicePixelRatio
    """
    #  qreal QImage::devicePixelRatio() const
    return self.uglySide.call('ritual_ZNK6QImage16devicePixelRatioEv')

  def deviceIndependentSize(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QImage::deviceIndependentSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#deviceIndependentSize

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QImage::deviceIndependentSize() const
    address = self.uglySide.call(
        'ritual_ZNK6QImage21deviceIndependentSizeEv',
    )
    return QSizeF._cuteOwning(address)

  def hasAlphaChannel(self) -> bool:
    """
    Calls Qt's 'bool QImage::hasAlphaChannel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#hasAlphaChannel
    """
    #  bool QImage::hasAlphaChannel() const
    return self.uglySide.call('ritual_ZNK6QImage15hasAlphaChannelEv')

  @overload()
  @overload(Qt.ImageConversionFlags)
  def createAlphaMask(
      self,
      flags: Qt.ImageConversionFlags = Qt.ImageConversionFlags.AutoColor,
  ) -> QImage:
    """
    Calls Qt's 'QImage QImage::createAlphaMask(Qt::ImageConversionFlags
    flags) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#createAlphaMask

    Parameters
    ----------

    flags : Qt.ImageConversionFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ImageConversionFlags.AutoColor.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QImage::createAlphaMask(Qt::ImageConversionFlags flags) const
    address = self.uglySide.call(
        'ritual_ZNK6QImage15createAlphaMaskE6QFlagsIN2Qt19ImageConversionFl'
        'agEE',
        flags.value,
    )
    return QImage._cuteOwning(address)

  @overload()
  @overload(bool)
  def createHeuristicMask(self, clipTight: bool = True) -> QImage:
    """
    Calls Qt's 'QImage QImage::createHeuristicMask(bool clipTight) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#createHeuristicMask

    Parameters
    ----------

    clipTight : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QImage::createHeuristicMask(bool clipTight) const
    address = self.uglySide.call(
        'ritual_ZNK6QImage19createHeuristicMaskEb', clipTight,
    )
    return QImage._cuteOwning(address)

  @overload(int)
  @overload(int, Qt.MaskMode)
  def createMaskFromColor(
      self,
      color: int,
      mode: Qt.MaskMode = Qt.MaskMode.MaskInColor,
  ) -> QImage:
    """
    Calls Qt's 'QImage QImage::createMaskFromColor(QRgb color, Qt::MaskMode
    mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#createMaskFromColor

    Parameters
    ----------

    color : int
      Passed on as it is.

    mode : Qt.MaskMode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.MaskMode.MaskInColor.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QImage::createMaskFromColor(QRgb color, Qt::MaskMode mode)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK6QImage19createMaskFromColorEjN2Qt8MaskModeE',
        color, mode.value,
    )
    return QImage._cuteOwning(address)

  @overload(int, int)
  @overload(int, int, Qt.AspectRatioMode)
  @overload(int, int, Qt.AspectRatioMode, Qt.TransformationMode)
  def scaled(
      self,
      w: int,
      h: int,
      aspectMode: Qt.AspectRatioMode = Qt.AspectRatioMode.IgnoreAspectRatio,
      mode: Qt.TransformationMode = Qt.TransformationMode.FastTransformation,
  ) -> QImage:
    """
    Calls Qt's 'QImage QImage::scaled(int w, int h, Qt::AspectRatioMode
    aspectMode, Qt::TransformationMode mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#scaled

    Parameters
    ----------

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.

    aspectMode : Qt.AspectRatioMode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.AspectRatioMode.IgnoreAspectRatio.

    mode : Qt.TransformationMode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.TransformationMode.FastTransformation.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QImage::scaled(int w, int h, Qt::AspectRatioMode aspectMode,
    #      Qt::TransformationMode mode) const
    address = self.uglySide.call(
        'ritual_ZNK6QImage6scaledEiiN2Qt15AspectRatioModeENS0_18Transformat'
        'ionModeE',
        w, h, aspectMode.value, mode.value,
    )
    return QImage._cuteOwning(address)

  @overload(QSize)
  @overload(QSize, Qt.AspectRatioMode)
  @overload(QSize, Qt.AspectRatioMode, Qt.TransformationMode)
  def scaled(
      self,
      s: QSize,
      aspectMode: Qt.AspectRatioMode = Qt.AspectRatioMode.IgnoreAspectRatio,
      mode: Qt.TransformationMode = Qt.TransformationMode.FastTransformation,
  ) -> QImage:
    """
    Calls Qt's 'QImage QImage::scaled(const QSize &s, Qt::AspectRatioMode
    aspectMode, Qt::TransformationMode mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#scaled

    Parameters
    ----------

    s : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    aspectMode : Qt.AspectRatioMode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.AspectRatioMode.IgnoreAspectRatio.

    mode : Qt.TransformationMode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.TransformationMode.FastTransformation.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QImage::scaled(const QSize &s, Qt::AspectRatioMode aspectMode,
    #      Qt::TransformationMode mode) const
    address = self.uglySide.call(
        'ritual_ZNK6QImage6scaledERK5QSizeN2Qt15AspectRatioModeENS3_18Trans'
        'formationModeE',
        self._valueOf(s), aspectMode.value, mode.value,
    )
    return QImage._cuteOwning(address)

  @overload(int)
  @overload(int, Qt.TransformationMode)
  def scaledToWidth(
      self,
      w: int,
      mode: Qt.TransformationMode = Qt.TransformationMode.FastTransformation,
  ) -> QImage:
    """
    Calls Qt's 'QImage QImage::scaledToWidth(int w, Qt::TransformationMode
    mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#scaledToWidth

    Parameters
    ----------

    w : int
      Passed on as it is.

    mode : Qt.TransformationMode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.TransformationMode.FastTransformation.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QImage::scaledToWidth(int w, Qt::TransformationMode mode) const
    address = self.uglySide.call(
        'ritual_ZNK6QImage13scaledToWidthEiN2Qt18TransformationModeE',
        w, mode.value,
    )
    return QImage._cuteOwning(address)

  @overload(int)
  @overload(int, Qt.TransformationMode)
  def scaledToHeight(
      self,
      h: int,
      mode: Qt.TransformationMode = Qt.TransformationMode.FastTransformation,
  ) -> QImage:
    """
    Calls Qt's 'QImage QImage::scaledToHeight(int h, Qt::TransformationMode
    mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#scaledToHeight

    Parameters
    ----------

    h : int
      Passed on as it is.

    mode : Qt.TransformationMode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.TransformationMode.FastTransformation.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QImage::scaledToHeight(int h, Qt::TransformationMode mode)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK6QImage14scaledToHeightEiN2Qt18TransformationModeE',
        h, mode.value,
    )
    return QImage._cuteOwning(address)

  @overload(QTransform)
  @overload(QTransform, Qt.TransformationMode)
  def transformed(
      self,
      matrix: QTransform,
      mode: Qt.TransformationMode = Qt.TransformationMode.FastTransformation,
  ) -> QImage:
    """
    Calls Qt's 'QImage QImage::transformed(const QTransform &matrix,
    Qt::TransformationMode mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#transformed

    Parameters
    ----------

    matrix : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.

    mode : Qt.TransformationMode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.TransformationMode.FastTransformation.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QImage::transformed(const QTransform &matrix,
    #      Qt::TransformationMode mode) const
    address = self.uglySide.call(
        'ritual_ZNK6QImage11transformedERK10QTransformN2Qt18TransformationM'
        'odeE',
        self._valueOf(matrix), mode.value,
    )
    return QImage._cuteOwning(address)

  @overload()
  @overload(bool)
  @overload(bool, bool)
  def mirrored(
      self,
      horizontally: bool = False,
      vertically: bool = True,
  ) -> QImage:
    """
    Calls Qt's 'QImage QImage::mirrored(bool horizontally, bool vertically)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#mirrored

    Parameters
    ----------

    horizontally : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    vertically : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QImage::mirrored(bool horizontally, bool vertically) const
    address = self.uglySide.call(
        'ritual_ZNKR6QImage8mirroredEbb', horizontally, vertically,
    )
    return QImage._cuteOwning(address)

  def rgbSwapped(self) -> QImage:
    """
    Calls Qt's 'QImage QImage::rgbSwapped() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#rgbSwapped

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QImage::rgbSwapped() const
    address = self.uglySide.call('ritual_ZNKR6QImage10rgbSwappedEv')
    return QImage._cuteOwning(address)

  @overload()
  @overload(Qt.Orientations)
  def flipped(
      self,
      orient: Qt.Orientations = Qt.Orientations.Vertical,
  ) -> QImage:
    """
    Calls Qt's 'QImage QImage::flipped(Qt::Orientations orient) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#flipped

    Parameters
    ----------

    orient : Qt.Orientations
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Orientations.Vertical.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QImage::flipped(Qt::Orientations orient) const
    address = self.uglySide.call(
        'ritual_ZNKR6QImage7flippedE6QFlagsIN2Qt11OrientationEE',
        orient.value,
    )
    return QImage._cuteOwning(address)

  def colorSpace(self) -> QColorSpace:
    """
    Calls Qt's 'QColorSpace QImage::colorSpace() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#colorSpace

    Returns
    -------

    QColorSpace
      A new cute QColorSpace around the copy Qt gave back. Python owns it.
    """
    #  QColorSpace QImage::colorSpace() const
    address = self.uglySide.call('ritual_ZNK6QImage10colorSpaceEv')
    return QColorSpace._cuteOwning(address)

  @overload(QColorSpace)
  def convertedToColorSpace(self, colorSpace: QColorSpace) -> QImage:
    """
    Calls Qt's 'QImage QImage::convertedToColorSpace(const QColorSpace
    &colorSpace) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#convertedToColorSpace

    Parameters
    ----------

    colorSpace : QColorSpace
      Passed on as a value: Qt reads the C++ QColorSpace, which stays
      Python's own.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QImage::convertedToColorSpace(const QColorSpace &colorSpace)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK6QImage21convertedToColorSpaceERK11QColorSpace',
        self._valueOf(colorSpace),
    )
    return QImage._cuteOwning(address)

  @overload(QColorSpace, Format)
  @overload(QColorSpace, Format, Qt.ImageConversionFlags)
  def convertedToColorSpace(
      self,
      colorSpace: QColorSpace,
      format: Format,
      flags: Qt.ImageConversionFlags = Qt.ImageConversionFlags.AutoColor,
  ) -> QImage:
    """
    Calls Qt's 'QImage QImage::convertedToColorSpace(const QColorSpace
    &colorSpace, QImage::Format format, Qt::ImageConversionFlags flags)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#convertedToColorSpace

    Parameters
    ----------

    colorSpace : QColorSpace
      Passed on as a value: Qt reads the C++ QColorSpace, which stays
      Python's own.

    format : Format
      Passed on as its number.

    flags : Qt.ImageConversionFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ImageConversionFlags.AutoColor.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QImage::convertedToColorSpace(const QColorSpace &colorSpace,
    #      QImage::Format format, Qt::ImageConversionFlags flags) const
    address = self.uglySide.call(
        'ritual_ZNKR6QImage21convertedToColorSpaceERK11QColorSpaceNS_6Forma'
        'tE6QFlagsIN2Qt19ImageConversionFlagEE',
        self._valueOf(colorSpace), format.value, flags.value,
    )
    return QImage._cuteOwning(address)

  @overload(str)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  def save(
      self,
      fileName: str,
      format: Optional[str] = None,
      quality: int = -1,
  ) -> bool:
    """
    Calls Qt's 'bool QImage::save(const QString &fileName, const char
    *format, int quality) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#save

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    format : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    quality : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  bool QImage::save(const QString &fileName, const char *format, int
    #      quality) const
    return self.uglySide.call(
        'ritual_ZNK6QImage4saveERK7QStringPKci',
        fileName, self._bytesOf(format), quality,
    )

  @overload(QIODevice)
  @overload(NoneType)
  @overload(QIODevice, str)
  @overload(QIODevice, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(QIODevice, str, int)
  @overload(QIODevice, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def save(
      self,
      device: Optional[QIODevice],
      format: Optional[str] = None,
      quality: int = -1,
  ) -> bool:
    """
    Calls Qt's 'bool QImage::save(QIODevice *device, const char *format, int
    quality) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#save

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    format : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    quality : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  bool QImage::save(QIODevice *device, const char *format, int quality)
    #      const
    return self.uglySide.call(
        'ritual_ZNK6QImage4saveEP9QIODevicePKci',
        self._addressOf(device), self._bytesOf(format), quality,
    )

  def cacheKey(self) -> int:
    """
    Calls Qt's 'qint64 QImage::cacheKey() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#cacheKey
    """
    #  qint64 QImage::cacheKey() const
    return self.uglySide.call('ritual_ZNK6QImage8cacheKeyEv')

  def dotsPerMeterX(self) -> int:
    """
    Calls Qt's 'int QImage::dotsPerMeterX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#dotsPerMeterX
    """
    #  int QImage::dotsPerMeterX() const
    return self.uglySide.call('ritual_ZNK6QImage13dotsPerMeterXEv')

  def dotsPerMeterY(self) -> int:
    """
    Calls Qt's 'int QImage::dotsPerMeterY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#dotsPerMeterY
    """
    #  int QImage::dotsPerMeterY() const
    return self.uglySide.call('ritual_ZNK6QImage13dotsPerMeterYEv')

  def offset(self) -> QPoint:
    """
    Calls Qt's 'QPoint QImage::offset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#offset

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QImage::offset() const
    address = self.uglySide.call('ritual_ZNK6QImage6offsetEv')
    return QPoint._cuteOwning(address)

  @overload()
  @overload(str)
  def text(self, key: str = '') -> str:
    """
    Calls Qt's 'QString QImage::text(const QString &key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#text

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QImage::text(const QString &key) const
    return self.uglySide.call('ritual_ZNK6QImage4textERK7QString', key)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int)
  def setColor(self, i: int, c: int) -> None:
    """
    Calls Qt's 'void QImage::setColor(int i, QRgb c)'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#setColor

    Parameters
    ----------

    i : int
      Passed on as it is.

    c : int
      Passed on as it is.
    """
    #  void QImage::setColor(int i, QRgb c)
    self.uglySide.call('ritual_ZN6QImage8setColorEij', i, c)

  @overload(int)
  def setColorCount(self, a0: int) -> None:
    """
    Calls Qt's 'void QImage::setColorCount(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#setColorCount

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QImage::setColorCount(int a0)
    self.uglySide.call('ritual_ZN6QImage13setColorCountEi', a0)

  @overload(int, int, int)
  def setPixel(self, x: int, y: int, index_or_rgb: int) -> None:
    """
    Calls Qt's 'void QImage::setPixel(int x, int y, uint index_or_rgb)'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#setPixel

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    index_or_rgb : int
      Passed on as it is.
    """
    #  void QImage::setPixel(int x, int y, uint index_or_rgb)
    self.uglySide.call('ritual_ZN6QImage8setPixelEiij', x, y, index_or_rgb)

  @overload(QPoint, int)
  def setPixel(self, pt: QPoint, index_or_rgb: int) -> None:
    """
    Calls Qt's 'void QImage::setPixel(const QPoint &pt, uint index_or_rgb)'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#setPixel

    Parameters
    ----------

    pt : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    index_or_rgb : int
      Passed on as it is.
    """
    #  void QImage::setPixel(const QPoint &pt, uint index_or_rgb)
    self.uglySide.call(
        'ritual_ZN6QImage8setPixelERK6QPointj',
        self._valueOf(pt), index_or_rgb,
    )

  @overload(int, int, QColor)
  def setPixelColor(self, x: int, y: int, c: QColor) -> None:
    """
    Calls Qt's 'void QImage::setPixelColor(int x, int y, const QColor &c)'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#setPixelColor

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    c : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QImage::setPixelColor(int x, int y, const QColor &c)
    self.uglySide.call(
        'ritual_ZN6QImage13setPixelColorEiiRK6QColor',
        x, y, self._valueOf(c),
    )

  @overload(QPoint, QColor)
  def setPixelColor(self, pt: QPoint, c: QColor) -> None:
    """
    Calls Qt's 'void QImage::setPixelColor(const QPoint &pt, const QColor
    &c)'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#setPixelColor

    Parameters
    ----------

    pt : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    c : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QImage::setPixelColor(const QPoint &pt, const QColor &c)
    self.uglySide.call(
        'ritual_ZN6QImage13setPixelColorERK6QPointRK6QColor',
        self._valueOf(pt), self._valueOf(c),
    )

  @overload(float)
  def setDevicePixelRatio(self, scaleFactor: float) -> None:
    """
    Calls Qt's 'void QImage::setDevicePixelRatio(qreal scaleFactor)'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#setDevicePixelRatio

    Parameters
    ----------

    scaleFactor : float
      Passed on as it is.
    """
    #  void QImage::setDevicePixelRatio(qreal scaleFactor)
    self.uglySide.call(
        'ritual_ZN6QImage19setDevicePixelRatioEd', scaleFactor,
    )

  @overload(THIS)
  def setAlphaChannel(self, alphaChannel: QImage) -> None:
    """
    Calls Qt's 'void QImage::setAlphaChannel(const QImage &alphaChannel)'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#setAlphaChannel

    Parameters
    ----------

    alphaChannel : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QImage::setAlphaChannel(const QImage &alphaChannel)
    self.uglySide.call(
        'ritual_ZN6QImage15setAlphaChannelERKS_',
        self._valueOf(alphaChannel),
    )

  @overload(QColorSpace)
  def setColorSpace(self, colorSpace: QColorSpace) -> None:
    """
    Calls Qt's 'void QImage::setColorSpace(const QColorSpace &colorSpace)'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#setColorSpace

    Parameters
    ----------

    colorSpace : QColorSpace
      Passed on as a value: Qt reads the C++ QColorSpace, which stays
      Python's own.
    """
    #  void QImage::setColorSpace(const QColorSpace &colorSpace)
    self.uglySide.call(
        'ritual_ZN6QImage13setColorSpaceERK11QColorSpace',
        self._valueOf(colorSpace),
    )

  @overload(int)
  def setDotsPerMeterX(self, a0: int) -> None:
    """
    Calls Qt's 'void QImage::setDotsPerMeterX(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#setDotsPerMeterX

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QImage::setDotsPerMeterX(int a0)
    self.uglySide.call('ritual_ZN6QImage16setDotsPerMeterXEi', a0)

  @overload(int)
  def setDotsPerMeterY(self, a0: int) -> None:
    """
    Calls Qt's 'void QImage::setDotsPerMeterY(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#setDotsPerMeterY

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QImage::setDotsPerMeterY(int a0)
    self.uglySide.call('ritual_ZN6QImage16setDotsPerMeterYEi', a0)

  @overload(QPoint)
  def setOffset(self, a0: QPoint) -> None:
    """
    Calls Qt's 'void QImage::setOffset(const QPoint &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#setOffset

    Parameters
    ----------

    a0 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QImage::setOffset(const QPoint &a0)
    self.uglySide.call(
        'ritual_ZN6QImage9setOffsetERK6QPoint', self._valueOf(a0),
    )

  @overload(str, str)
  def setText(self, key: str, value: str) -> None:
    """
    Calls Qt's 'void QImage::setText(const QString &key, const QString
    &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#setText

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QImage::setText(const QString &key, const QString &value)
    self.uglySide.call('ritual_ZN6QImage7setTextERK7QStringS2_', key, value)

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
    Notes what was given, for Qt's 'QImage::QImage()', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#QImage
    """
    #  QImage::QImage()
    self._noteCreation(QImage, lambda: Rituals.call('ritual_ZN6QImageC1Ev'))

  @overload(QSize, Format)
  def __init__(self, size: QSize, format: Format) -> None:
    """
    Notes what was given, for Qt's 'QImage::QImage(const QSize &size, Format
    format)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#QImage

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    format : Format
      Passed on as its number.
    """
    #  QImage::QImage(const QSize &size, Format format)
    self._noteCreation(QImage, lambda: Rituals.call(
        'ritual_ZN6QImageC1ERK5QSizeNS_6FormatE',
        self._valueOf(size), format.value,
    ))

  @overload(int, int, Format)
  def __init__(self, width: int, height: int, format: Format) -> None:
    """
    Notes what was given, for Qt's 'QImage::QImage(int width, int height,
    Format format)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#QImage

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.

    format : Format
      Passed on as its number.
    """
    #  QImage::QImage(int width, int height, Format format)
    self._noteCreation(QImage, lambda: Rituals.call(
        'ritual_ZN6QImageC1EiiNS_6FormatE', width, height, format.value,
    ))

  @overload(str)
  @overload(str, str)
  @overload(str, NoneType)
  def __init__(self, fileName: str, format: Optional[str] = None) -> None:
    """
    Notes what was given, for Qt's 'QImage::QImage(const QString &fileName,
    const char *format)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#QImage

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    format : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.
    """
    #  QImage::QImage(const QString &fileName, const char *format)
    self._noteCreation(QImage, lambda: Rituals.call(
        'ritual_ZN6QImageC1ERK7QStringPKc', fileName, self._bytesOf(format),
    ))

  @overload(THIS)
  def __init__(self, a0: QImage) -> None:
    """
    Notes what was given, for Qt's 'QImage::QImage(const QImage &a0)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#QImage

    Parameters
    ----------

    a0 : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  QImage::QImage(const QImage &a0)
    self._noteCreation(QImage, lambda: Rituals.call(
        'ritual_ZN6QImageC1ERKS_', self._valueOf(a0),
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

  def detach(self) -> None:
    """
    Calls Qt's 'void QImage::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#detach
    """
    #  void QImage::detach()
    self.uglySide.call('ritual_ZN6QImage6detachEv')

  @overload(Format)
  def reinterpretAsFormat(self, f: Format) -> bool:
    """
    Calls Qt's 'bool QImage::reinterpretAsFormat(Format f)'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#reinterpretAsFormat

    Parameters
    ----------

    f : Format
      Passed on as its number.
    """
    #  bool QImage::reinterpretAsFormat(Format f)
    return self.uglySide.call(
        'ritual_ZN6QImage19reinterpretAsFormatENS_6FormatE', f.value,
    )

  @overload(Format)
  @overload(Format, Qt.ImageConversionFlags)
  def convertTo(
      self,
      f: Format,
      flags: Qt.ImageConversionFlags = Qt.ImageConversionFlags.AutoColor,
  ) -> None:
    """
    Calls Qt's 'void QImage::convertTo(Format f, Qt::ImageConversionFlags
    flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#convertTo

    Parameters
    ----------

    f : Format
      Passed on as its number.

    flags : Qt.ImageConversionFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ImageConversionFlags.AutoColor.
    """
    #  void QImage::convertTo(Format f, Qt::ImageConversionFlags flags)
    self.uglySide.call(
        'ritual_ZN6QImage9convertToENS_6FormatE6QFlagsIN2Qt19ImageConversio'
        'nFlagEE',
        f.value, flags.value,
    )

  @overload(int)
  def fill(self, pixel: int) -> None:
    """
    Calls Qt's 'void QImage::fill(uint pixel)'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#fill

    Parameters
    ----------

    pixel : int
      Passed on as it is.
    """
    #  void QImage::fill(uint pixel)
    self.uglySide.call('ritual_ZN6QImage4fillEj', pixel)

  @overload(QColor)
  def fill(self, color: QColor) -> None:
    """
    Calls Qt's 'void QImage::fill(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#fill

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QImage::fill(const QColor &color)
    self.uglySide.call(
        'ritual_ZN6QImage4fillERK6QColor', self._valueOf(color),
    )

  @overload(Qt.GlobalColor)
  def fill(self, color: Qt.GlobalColor) -> None:
    """
    Calls Qt's 'void QImage::fill(Qt::GlobalColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#fill

    Parameters
    ----------

    color : Qt.GlobalColor
      Passed on as its number.
    """
    #  void QImage::fill(Qt::GlobalColor color)
    self.uglySide.call(
        'ritual_ZN6QImage4fillEN2Qt11GlobalColorE', color.value,
    )

  @overload()
  @overload(bool)
  @overload(bool, bool)
  def mirror(
      self,
      horizontally: bool = False,
      vertically: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QImage::mirror(bool horizontally, bool vertically)'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#mirror

    Parameters
    ----------

    horizontally : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    vertically : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QImage::mirror(bool horizontally, bool vertically)
    self.uglySide.call(
        'ritual_ZN6QImage6mirrorEbb', horizontally, vertically,
    )

  @overload()
  @overload(Qt.Orientations)
  def flip(self, orient: Qt.Orientations = Qt.Orientations.Vertical) -> None:
    """
    Calls Qt's 'void QImage::flip(Qt::Orientations orient)'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#flip

    Parameters
    ----------

    orient : Qt.Orientations
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Orientations.Vertical.
    """
    #  void QImage::flip(Qt::Orientations orient)
    self.uglySide.call(
        'ritual_ZN6QImage4flipE6QFlagsIN2Qt11OrientationEE', orient.value,
    )

  def rgbSwap(self) -> None:
    """
    Calls Qt's 'void QImage::rgbSwap()'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#rgbSwap
    """
    #  void QImage::rgbSwap()
    self.uglySide.call('ritual_ZN6QImage7rgbSwapEv')

  @overload()
  @overload(InvertMode)
  def invertPixels(self, a0: InvertMode = InvertMode.InvertRgb) -> None:
    """
    Calls Qt's 'void QImage::invertPixels(InvertMode a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#invertPixels

    Parameters
    ----------

    a0 : InvertMode
      Passed on as its number. May be left out, as in Qt: it is then
      InvertMode.InvertRgb.
    """
    #  void QImage::invertPixels(InvertMode a0)
    self.uglySide.call(
        'ritual_ZN6QImage12invertPixelsENS_10InvertModeE', a0.value,
    )

  @overload(QColorSpace)
  def convertToColorSpace(self, colorSpace: QColorSpace) -> None:
    """
    Calls Qt's 'void QImage::convertToColorSpace(const QColorSpace
    &colorSpace)'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#convertToColorSpace

    Parameters
    ----------

    colorSpace : QColorSpace
      Passed on as a value: Qt reads the C++ QColorSpace, which stays
      Python's own.
    """
    #  void QImage::convertToColorSpace(const QColorSpace &colorSpace)
    self.uglySide.call(
        'ritual_ZN6QImage19convertToColorSpaceERK11QColorSpace',
        self._valueOf(colorSpace),
    )

  @overload(QColorSpace, Format)
  @overload(QColorSpace, Format, Qt.ImageConversionFlags)
  def convertToColorSpace(
      self,
      colorSpace: QColorSpace,
      format: Format,
      flags: Qt.ImageConversionFlags = Qt.ImageConversionFlags.AutoColor,
  ) -> None:
    """
    Calls Qt's 'void QImage::convertToColorSpace(const QColorSpace
    &colorSpace, QImage::Format format, Qt::ImageConversionFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#convertToColorSpace

    Parameters
    ----------

    colorSpace : QColorSpace
      Passed on as a value: Qt reads the C++ QColorSpace, which stays
      Python's own.

    format : Format
      Passed on as its number.

    flags : Qt.ImageConversionFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ImageConversionFlags.AutoColor.
    """
    #  void QImage::convertToColorSpace(const QColorSpace &colorSpace,
    #      QImage::Format format, Qt::ImageConversionFlags flags)
    self.uglySide.call(
        'ritual_ZN6QImage19convertToColorSpaceERK11QColorSpaceNS_6FormatE6Q'
        'FlagsIN2Qt19ImageConversionFlagEE',
        self._valueOf(colorSpace), format.value, flags.value,
    )

  @overload(QIODevice, str)
  @overload(QIODevice, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  def load(self, device: Optional[QIODevice], format: Optional[str]) -> bool:
    """
    Calls Qt's 'bool QImage::load(QIODevice *device, const char *format)'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#load

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    format : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QImage::load(QIODevice *device, const char *format)
    return self.uglySide.call(
        'ritual_ZN6QImage4loadEP9QIODevicePKc',
        self._addressOf(device), self._bytesOf(format),
    )

  @overload(str)
  @overload(str, str)
  @overload(str, NoneType)
  def load(self, fileName: str, format: Optional[str] = None) -> bool:
    """
    Calls Qt's 'bool QImage::load(const QString &fileName, const char
    *format)'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#load

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    format : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.
    """
    #  bool QImage::load(const QString &fileName, const char *format)
    return self.uglySide.call(
        'ritual_ZN6QImage4loadERK7QStringPKc',
        fileName, self._bytesOf(format),
    )

  @overload(QByteArrayView)
  @overload(QByteArrayView, str)
  @overload(QByteArrayView, NoneType)
  def loadFromData(
      self,
      data: QByteArrayView,
      format: Optional[str] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QImage::loadFromData(QByteArrayView data, const char
    *format)'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#loadFromData

    Parameters
    ----------

    data : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    format : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.
    """
    #  bool QImage::loadFromData(QByteArrayView data, const char *format)
    return self.uglySide.call(
        'ritual_ZN6QImage12loadFromDataE14QByteArrayViewPKc',
        self._valueOf(data), self._bytesOf(format),
    )

  @overload(QByteArray)
  @overload(QByteArray, str)
  @overload(QByteArray, NoneType)
  def loadFromData(
      self,
      data: QByteArray,
      format: Optional[str] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QImage::loadFromData(const QByteArray &data, const char
    *format)'.

    Qt's own words: https://doc.qt.io/qt-6/qimage.html#loadFromData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    format : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.
    """
    #  bool QImage::loadFromData(const QByteArray &data, const char *format)
    return self.uglySide.call(
        'ritual_ZN6QImage12loadFromDataERK10QByteArrayPKc',
        self._valueOf(data), self._bytesOf(format),
    )
