"""
QPixmap binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qpixmap.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QPaintDevice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QIODevice, QRect, QSize, QSizeF
  from . import QBitmap, QColor, QImage, QImageReader, QPaintEngine, QRegion
  from . import QTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBitmap = WAIT['QBitmap']
  QByteArray = WAIT['QByteArray']
  QColor = WAIT['QColor']
  QIODevice = WAIT['QIODevice']
  QImage = WAIT['QImage']
  QImageReader = WAIT['QImageReader']
  QRect = WAIT['QRect']
  QRegion = WAIT['QRegion']
  QSize = WAIT['QSize']
  QTransform = WAIT['QTransform']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPixmap(QPaintDevice):
  """
  The cute side of Qt's QPixmap: a plain Python object standing in front of
  one C++ QPixmap.

  It is built on the cute 'QPaintDevice', as Qt's QPixmap is built on Qt's
  QPaintDevice, and has everything that class has.

  C++ hands a QPixmap around as a copy, so every C++ QPixmap behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPixmap that has a ritual and that Python can call
  so far, 37 names in all: 'isNull', 'devType', 'width', 'height', 'size',
  'rect', 'depth', 'defaultDepth', 'fill', 'mask', 'setMask',
  'devicePixelRatio', 'setDevicePixelRatio', 'deviceIndependentSize',
  'hasAlpha', 'hasAlphaChannel', 'createHeuristicMask',
  'createMaskFromColor', 'scaled', 'scaledToWidth', 'scaledToHeight',
  'transformed', 'trueMatrix', 'toImage', 'fromImage', 'fromImageReader',
  'load', 'loadFromData', 'save', 'convertFromImage', 'copy', 'scroll',
  'cacheKey', 'isDetached', 'detach', 'isQBitmap', 'paintEngine'. It can be
  made from Python, in 5 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPixmap::~QPixmap()': the destructor: Python removes its C++
    QPixmap by it, and has no other use for it.
  - Qt's 'QVariant QPixmap::operator QVariant() const': an operator Python
    has no name for.
  - Qt's 'bool QPixmap::operator!() const': an operator Python has no name
    for.

  What has no ritual
  ------------------

  18 of the 67 functions Qt declares: 11 takes or gives a type that cannot be
  passed yet; 3 private; 2 forbidden; 2 protected.

  What to expect
  --------------

  - The C++ QPixmap is created at the first use, not by 'QPixmap(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPixmap back gives a copy the ritual made for Python,
    in a new cute QPixmap.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def defaultDepth() -> int:
    """
    Calls Qt's 'int QPixmap::defaultDepth()'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#defaultDepth
    """
    #  int QPixmap::defaultDepth()
    return Rituals.call('ritual_ZN7QPixmap12defaultDepthEv')

  @staticmethod
  @overload(QTransform, int, int)
  def trueMatrix(m: QTransform, w: int, h: int) -> QTransform:
    """
    Calls Qt's 'QTransform QPixmap::trueMatrix(const QTransform &m, int w,
    int h)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#trueMatrix

    Parameters
    ----------

    m : QTransform
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
    #  QTransform QPixmap::trueMatrix(const QTransform &m, int w, int h)
    address = Rituals.call(
        'ritual_ZN7QPixmap10trueMatrixERK10QTransformii',
        CuteMixin._valueOf(m), w, h,
    )
    from . import QTransform
    return QTransform._cuteOwning(address)

  @staticmethod
  @overload(QImage)
  @overload(QImage, Qt.ImageConversionFlags)
  def fromImage(
      image: QImage,
      flags: Qt.ImageConversionFlags = Qt.ImageConversionFlags.AutoColor,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QPixmap::fromImage(const QImage &image,
    Qt::ImageConversionFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#fromImage

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    flags : Qt.ImageConversionFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ImageConversionFlags.AutoColor.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QPixmap::fromImage(const QImage &image,
    #      Qt::ImageConversionFlags flags)
    address = Rituals.call(
        'ritual_ZN7QPixmap9fromImageERK6QImage6QFlagsIN2Qt19ImageConversion'
        'FlagEE',
        CuteMixin._valueOf(image), flags.value,
    )
    return QPixmap._cuteOwning(address)

  @staticmethod
  @overload(QImageReader)
  @overload(NoneType)
  @overload(QImageReader, Qt.ImageConversionFlags)
  @overload(NoneType, Qt.ImageConversionFlags)
  def fromImageReader(
      imageReader: Optional[QImageReader],
      flags: Qt.ImageConversionFlags = Qt.ImageConversionFlags.AutoColor,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QPixmap::fromImageReader(QImageReader *imageReader,
    Qt::ImageConversionFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#fromImageReader

    Parameters
    ----------

    imageReader : Optional[QImageReader]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : Qt.ImageConversionFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ImageConversionFlags.AutoColor.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QPixmap::fromImageReader(QImageReader *imageReader,
    #      Qt::ImageConversionFlags flags)
    address = Rituals.call(
        'ritual_ZN7QPixmap15fromImageReaderEP12QImageReader6QFlagsIN2Qt19Im'
        'ageConversionFlagEE',
        CuteMixin._addressOf(imageReader), flags.value,
    )
    return QPixmap._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPixmap'

  #  Qt's '~QPixmap()'. Naming it makes this a value class: Python owns every
  #  C++ QPixmap behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN7QPixmapD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QPixmap::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#isNull
    """
    #  bool QPixmap::isNull() const
    return self.uglySide.call('ritual_ZNK7QPixmap6isNullEv')

  def devType(self) -> int:
    """
    Calls Qt's 'int QPixmap::devType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#devType
    """
    #  int QPixmap::devType() const
    return self.uglySide.call('ritual_ZNK7QPixmap7devTypeEv')

  def width(self) -> int:
    """
    Calls Qt's 'int QPixmap::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#width
    """
    #  int QPixmap::width() const
    return self.uglySide.call('ritual_ZNK7QPixmap5widthEv')

  def height(self) -> int:
    """
    Calls Qt's 'int QPixmap::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#height
    """
    #  int QPixmap::height() const
    return self.uglySide.call('ritual_ZNK7QPixmap6heightEv')

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QPixmap::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QPixmap::size() const
    address = self.uglySide.call('ritual_ZNK7QPixmap4sizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def rect(self) -> QRect:
    """
    Calls Qt's 'QRect QPixmap::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#rect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QPixmap::rect() const
    address = self.uglySide.call('ritual_ZNK7QPixmap4rectEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def depth(self) -> int:
    """
    Calls Qt's 'int QPixmap::depth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#depth
    """
    #  int QPixmap::depth() const
    return self.uglySide.call('ritual_ZNK7QPixmap5depthEv')

  def mask(self) -> QBitmap:
    """
    Calls Qt's 'QBitmap QPixmap::mask() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#mask

    Returns
    -------

    QBitmap
      A new cute QBitmap around the copy Qt gave back. Python owns it.
    """
    #  QBitmap QPixmap::mask() const
    address = self.uglySide.call('ritual_ZNK7QPixmap4maskEv')
    from . import QBitmap
    return QBitmap._cuteOwning(address)

  def devicePixelRatio(self) -> float:
    """
    Calls Qt's 'qreal QPixmap::devicePixelRatio() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#devicePixelRatio
    """
    #  qreal QPixmap::devicePixelRatio() const
    return self.uglySide.call('ritual_ZNK7QPixmap16devicePixelRatioEv')

  def deviceIndependentSize(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QPixmap::deviceIndependentSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#deviceIndependentSize

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QPixmap::deviceIndependentSize() const
    address = self.uglySide.call(
        'ritual_ZNK7QPixmap21deviceIndependentSizeEv',
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def hasAlpha(self) -> bool:
    """
    Calls Qt's 'bool QPixmap::hasAlpha() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#hasAlpha
    """
    #  bool QPixmap::hasAlpha() const
    return self.uglySide.call('ritual_ZNK7QPixmap8hasAlphaEv')

  def hasAlphaChannel(self) -> bool:
    """
    Calls Qt's 'bool QPixmap::hasAlphaChannel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#hasAlphaChannel
    """
    #  bool QPixmap::hasAlphaChannel() const
    return self.uglySide.call('ritual_ZNK7QPixmap15hasAlphaChannelEv')

  @overload()
  @overload(bool)
  def createHeuristicMask(self, clipTight: bool = True) -> QBitmap:
    """
    Calls Qt's 'QBitmap QPixmap::createHeuristicMask(bool clipTight) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#createHeuristicMask

    Parameters
    ----------

    clipTight : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    QBitmap
      A new cute QBitmap around the copy Qt gave back. Python owns it.
    """
    #  QBitmap QPixmap::createHeuristicMask(bool clipTight) const
    address = self.uglySide.call(
        'ritual_ZNK7QPixmap19createHeuristicMaskEb', clipTight,
    )
    from . import QBitmap
    return QBitmap._cuteOwning(address)

  @overload(QColor)
  @overload(QColor, Qt.MaskMode)
  def createMaskFromColor(
      self,
      maskColor: QColor,
      mode: Qt.MaskMode = Qt.MaskMode.MaskInColor,
  ) -> QBitmap:
    """
    Calls Qt's 'QBitmap QPixmap::createMaskFromColor(const QColor &maskColor,
    Qt::MaskMode mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#createMaskFromColor

    Parameters
    ----------

    maskColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    mode : Qt.MaskMode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.MaskMode.MaskInColor.

    Returns
    -------

    QBitmap
      A new cute QBitmap around the copy Qt gave back. Python owns it.
    """
    #  QBitmap QPixmap::createMaskFromColor(const QColor &maskColor,
    #      Qt::MaskMode mode) const
    address = self.uglySide.call(
        'ritual_ZNK7QPixmap19createMaskFromColorERK6QColorN2Qt8MaskModeE',
        self._valueOf(maskColor), mode.value,
    )
    from . import QBitmap
    return QBitmap._cuteOwning(address)

  @overload(int, int)
  @overload(int, int, Qt.AspectRatioMode)
  @overload(int, int, Qt.AspectRatioMode, Qt.TransformationMode)
  def scaled(
      self,
      w: int,
      h: int,
      aspectMode: Qt.AspectRatioMode = Qt.AspectRatioMode.IgnoreAspectRatio,
      mode: Qt.TransformationMode = Qt.TransformationMode.FastTransformation,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QPixmap::scaled(int w, int h, Qt::AspectRatioMode
    aspectMode, Qt::TransformationMode mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#scaled

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

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QPixmap::scaled(int w, int h, Qt::AspectRatioMode aspectMode,
    #      Qt::TransformationMode mode) const
    address = self.uglySide.call(
        'ritual_ZNK7QPixmap6scaledEiiN2Qt15AspectRatioModeENS0_18Transforma'
        'tionModeE',
        w, h, aspectMode.value, mode.value,
    )
    return QPixmap._cuteOwning(address)

  @overload(QSize)
  @overload(QSize, Qt.AspectRatioMode)
  @overload(QSize, Qt.AspectRatioMode, Qt.TransformationMode)
  def scaled(
      self,
      s: QSize,
      aspectMode: Qt.AspectRatioMode = Qt.AspectRatioMode.IgnoreAspectRatio,
      mode: Qt.TransformationMode = Qt.TransformationMode.FastTransformation,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QPixmap::scaled(const QSize &s, Qt::AspectRatioMode
    aspectMode, Qt::TransformationMode mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#scaled

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

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QPixmap::scaled(const QSize &s, Qt::AspectRatioMode
    #      aspectMode, Qt::TransformationMode mode) const
    address = self.uglySide.call(
        'ritual_ZNK7QPixmap6scaledERK5QSizeN2Qt15AspectRatioModeENS3_18Tran'
        'sformationModeE',
        self._valueOf(s), aspectMode.value, mode.value,
    )
    return QPixmap._cuteOwning(address)

  @overload(int)
  @overload(int, Qt.TransformationMode)
  def scaledToWidth(
      self,
      w: int,
      mode: Qt.TransformationMode = Qt.TransformationMode.FastTransformation,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QPixmap::scaledToWidth(int w, Qt::TransformationMode
    mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#scaledToWidth

    Parameters
    ----------

    w : int
      Passed on as it is.

    mode : Qt.TransformationMode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.TransformationMode.FastTransformation.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QPixmap::scaledToWidth(int w, Qt::TransformationMode mode)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK7QPixmap13scaledToWidthEiN2Qt18TransformationModeE',
        w, mode.value,
    )
    return QPixmap._cuteOwning(address)

  @overload(int)
  @overload(int, Qt.TransformationMode)
  def scaledToHeight(
      self,
      h: int,
      mode: Qt.TransformationMode = Qt.TransformationMode.FastTransformation,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QPixmap::scaledToHeight(int h, Qt::TransformationMode
    mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#scaledToHeight

    Parameters
    ----------

    h : int
      Passed on as it is.

    mode : Qt.TransformationMode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.TransformationMode.FastTransformation.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QPixmap::scaledToHeight(int h, Qt::TransformationMode mode)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK7QPixmap14scaledToHeightEiN2Qt18TransformationModeE',
        h, mode.value,
    )
    return QPixmap._cuteOwning(address)

  @overload(QTransform)
  @overload(QTransform, Qt.TransformationMode)
  def transformed(
      self,
      a0: QTransform,
      mode: Qt.TransformationMode = Qt.TransformationMode.FastTransformation,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QPixmap::transformed(const QTransform &a0,
    Qt::TransformationMode mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#transformed

    Parameters
    ----------

    a0 : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.

    mode : Qt.TransformationMode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.TransformationMode.FastTransformation.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QPixmap::transformed(const QTransform &a0,
    #      Qt::TransformationMode mode) const
    address = self.uglySide.call(
        'ritual_ZNK7QPixmap11transformedERK10QTransformN2Qt18Transformation'
        'ModeE',
        self._valueOf(a0), mode.value,
    )
    return QPixmap._cuteOwning(address)

  def toImage(self) -> QImage:
    """
    Calls Qt's 'QImage QPixmap::toImage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#toImage

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QPixmap::toImage() const
    address = self.uglySide.call('ritual_ZNK7QPixmap7toImageEv')
    from . import QImage
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
    Calls Qt's 'bool QPixmap::save(const QString &fileName, const char
    *format, int quality) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#save

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
    #  bool QPixmap::save(const QString &fileName, const char *format, int
    #      quality) const
    return self.uglySide.call(
        'ritual_ZNK7QPixmap4saveERK7QStringPKci',
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
    Calls Qt's 'bool QPixmap::save(QIODevice *device, const char *format, int
    quality) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#save

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
    #  bool QPixmap::save(QIODevice *device, const char *format, int quality)
    #      const
    return self.uglySide.call(
        'ritual_ZNK7QPixmap4saveEP9QIODevicePKci',
        self._addressOf(device), self._bytesOf(format), quality,
    )

  @overload(int, int, int, int)
  def copy(self, x: int, y: int, width: int, height: int) -> QPixmap:
    """
    Calls Qt's 'QPixmap QPixmap::copy(int x, int y, int width, int height)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#copy

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QPixmap::copy(int x, int y, int width, int height) const
    address = self.uglySide.call(
        'ritual_ZNK7QPixmap4copyEiiii', x, y, width, height,
    )
    return QPixmap._cuteOwning(address)

  @overload()
  @overload(QRect)
  def copy(self, rect: Optional[QRect] = None) -> QPixmap:
    """
    Calls Qt's 'QPixmap QPixmap::copy(const QRect &rect) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#copy

    Parameters
    ----------

    rect : Optional[QRect]
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
      May be left out, as in Qt: a new 'QRect()' is then passed on.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QPixmap::copy(const QRect &rect) const
    if rect is None:
      from ..QtCore import QRect
      rect = QRect()
    address = self.uglySide.call(
        'ritual_ZNK7QPixmap4copyERK5QRect', self._valueOf(rect),
    )
    return QPixmap._cuteOwning(address)

  def cacheKey(self) -> int:
    """
    Calls Qt's 'qint64 QPixmap::cacheKey() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#cacheKey
    """
    #  qint64 QPixmap::cacheKey() const
    return self.uglySide.call('ritual_ZNK7QPixmap8cacheKeyEv')

  def isDetached(self) -> bool:
    """
    Calls Qt's 'bool QPixmap::isDetached() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#isDetached
    """
    #  bool QPixmap::isDetached() const
    return self.uglySide.call('ritual_ZNK7QPixmap10isDetachedEv')

  def isQBitmap(self) -> bool:
    """
    Calls Qt's 'bool QPixmap::isQBitmap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#isQBitmap
    """
    #  bool QPixmap::isQBitmap() const
    return self.uglySide.call('ritual_ZNK7QPixmap9isQBitmapEv')

  def paintEngine(self) -> Optional[QPaintEngine]:
    """
    Calls Qt's 'QPaintEngine *QPixmap::paintEngine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#paintEngine

    Returns
    -------

    Optional[QPaintEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintEngine *QPixmap::paintEngine() const
    address = self.uglySide.call('ritual_ZNK7QPixmap11paintEngineEv')
    from . import QPaintEngine
    return QPaintEngine._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QBitmap)
  def setMask(self, a0: QBitmap) -> None:
    """
    Calls Qt's 'void QPixmap::setMask(const QBitmap &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#setMask

    Parameters
    ----------

    a0 : QBitmap
      Passed on as a value: Qt reads the C++ QBitmap, which stays Python's
      own.
    """
    #  void QPixmap::setMask(const QBitmap &a0)
    self.uglySide.call(
        'ritual_ZN7QPixmap7setMaskERK7QBitmap', self._valueOf(a0),
    )

  @overload(float)
  def setDevicePixelRatio(self, scaleFactor: float) -> None:
    """
    Calls Qt's 'void QPixmap::setDevicePixelRatio(qreal scaleFactor)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#setDevicePixelRatio

    Parameters
    ----------

    scaleFactor : float
      Passed on as it is.
    """
    #  void QPixmap::setDevicePixelRatio(qreal scaleFactor)
    self.uglySide.call(
        'ritual_ZN7QPixmap19setDevicePixelRatioEd', scaleFactor,
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
    Notes what was given, for Qt's 'QPixmap::QPixmap()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#QPixmap
    """
    #  QPixmap::QPixmap()
    self._noteCreation(QPixmap, lambda: Rituals.call(
        'ritual_ZN7QPixmapC1Ev',
    ))

  @overload(int, int)
  def __init__(self, w: int, h: int) -> None:
    """
    Notes what was given, for Qt's 'QPixmap::QPixmap(int w, int h)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#QPixmap

    Parameters
    ----------

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.
    """
    #  QPixmap::QPixmap(int w, int h)
    self._noteCreation(QPixmap, lambda: Rituals.call(
        'ritual_ZN7QPixmapC1Eii', w, h,
    ))

  @overload(QSize)
  def __init__(self, a0: QSize) -> None:
    """
    Notes what was given, for Qt's 'QPixmap::QPixmap(const QSize &a0)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#QPixmap

    Parameters
    ----------

    a0 : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  QPixmap::QPixmap(const QSize &a0)
    self._noteCreation(QPixmap, lambda: Rituals.call(
        'ritual_ZN7QPixmapC1ERK5QSize', self._valueOf(a0),
    ))

  @overload(str)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(str, str, Qt.ImageConversionFlags)
  @overload(str, NoneType, Qt.ImageConversionFlags)
  def __init__(
      self,
      fileName: str,
      format: Optional[str] = None,
      flags: Qt.ImageConversionFlags = Qt.ImageConversionFlags.AutoColor,
  ) -> None:
    """
    Notes what was given, for Qt's 'QPixmap::QPixmap(const QString &fileName,
    const char *format, Qt::ImageConversionFlags flags)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#QPixmap

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    format : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    flags : Qt.ImageConversionFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ImageConversionFlags.AutoColor.
    """
    #  QPixmap::QPixmap(const QString &fileName, const char *format,
    #      Qt::ImageConversionFlags flags)
    self._noteCreation(QPixmap, lambda: Rituals.call(
        'ritual_ZN7QPixmapC1ERK7QStringPKc6QFlagsIN2Qt19ImageConversionFlag'
        'EE',
        fileName, self._bytesOf(format), flags.value,
    ))

  @overload(THIS)
  def __init__(self, a0: QPixmap) -> None:
    """
    Notes what was given, for Qt's 'QPixmap::QPixmap(const QPixmap &a0)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#QPixmap

    Parameters
    ----------

    a0 : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  QPixmap::QPixmap(const QPixmap &a0)
    self._noteCreation(QPixmap, lambda: Rituals.call(
        'ritual_ZN7QPixmapC1ERKS_', self._valueOf(a0),
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

  @overload()
  @overload(QColor)
  def fill(self, fillColor: Optional[QColor] = None) -> None:
    """
    Calls Qt's 'void QPixmap::fill(const QColor &fillColor)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#fill

    Parameters
    ----------

    fillColor : Optional[QColor]
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own. May be left out, as in Qt: a new 'QColor(Qt.GlobalColor.white)' is
      then passed on.
    """
    #  void QPixmap::fill(const QColor &fillColor)
    if fillColor is None:
      from . import QColor
      fillColor = QColor(Qt.GlobalColor.white)
    self.uglySide.call(
        'ritual_ZN7QPixmap4fillERK6QColor', self._valueOf(fillColor),
    )

  @overload(str)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(str, str, Qt.ImageConversionFlags)
  @overload(str, NoneType, Qt.ImageConversionFlags)
  def load(
      self,
      fileName: str,
      format: Optional[str] = None,
      flags: Qt.ImageConversionFlags = Qt.ImageConversionFlags.AutoColor,
  ) -> bool:
    """
    Calls Qt's 'bool QPixmap::load(const QString &fileName, const char
    *format, Qt::ImageConversionFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#load

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    format : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    flags : Qt.ImageConversionFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ImageConversionFlags.AutoColor.
    """
    #  bool QPixmap::load(const QString &fileName, const char *format,
    #      Qt::ImageConversionFlags flags)
    return self.uglySide.call(
        'ritual_ZN7QPixmap4loadERK7QStringPKc6QFlagsIN2Qt19ImageConversionF'
        'lagEE',
        fileName, self._bytesOf(format), flags.value,
    )

  @overload(QByteArray)
  @overload(QByteArray, str)
  @overload(QByteArray, NoneType)
  @overload(QByteArray, str, Qt.ImageConversionFlags)
  @overload(QByteArray, NoneType, Qt.ImageConversionFlags)
  def loadFromData(
      self,
      data: QByteArray,
      format: Optional[str] = None,
      flags: Qt.ImageConversionFlags = Qt.ImageConversionFlags.AutoColor,
  ) -> bool:
    """
    Calls Qt's 'bool QPixmap::loadFromData(const QByteArray &data, const char
    *format, Qt::ImageConversionFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#loadFromData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    format : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    flags : Qt.ImageConversionFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ImageConversionFlags.AutoColor.
    """
    #  bool QPixmap::loadFromData(const QByteArray &data, const char *format,
    #      Qt::ImageConversionFlags flags)
    return self.uglySide.call(
        'ritual_ZN7QPixmap12loadFromDataERK10QByteArrayPKc6QFlagsIN2Qt19Ima'
        'geConversionFlagEE',
        self._valueOf(data), self._bytesOf(format), flags.value,
    )

  @overload(QImage)
  @overload(QImage, Qt.ImageConversionFlags)
  def convertFromImage(
      self,
      img: QImage,
      flags: Qt.ImageConversionFlags = Qt.ImageConversionFlags.AutoColor,
  ) -> bool:
    """
    Calls Qt's 'bool QPixmap::convertFromImage(const QImage &img,
    Qt::ImageConversionFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#convertFromImage

    Parameters
    ----------

    img : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    flags : Qt.ImageConversionFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ImageConversionFlags.AutoColor.
    """
    #  bool QPixmap::convertFromImage(const QImage &img,
    #      Qt::ImageConversionFlags flags)
    return self.uglySide.call(
        'ritual_ZN7QPixmap16convertFromImageERK6QImage6QFlagsIN2Qt19ImageCo'
        'nversionFlagEE',
        self._valueOf(img), flags.value,
    )

  @overload(int, int, int, int, int, int)
  @overload(int, int, int, int, int, int, QRegion)
  @overload(int, int, int, int, int, int, NoneType)
  def scroll(
      self,
      dx: int,
      dy: int,
      x: int,
      y: int,
      width: int,
      height: int,
      exposed: Optional[QRegion] = None,
  ) -> None:
    """
    Calls Qt's 'void QPixmap::scroll(int dx, int dy, int x, int y, int width,
    int height, QRegion *exposed)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#scroll

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.

    exposed : Optional[QRegion]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QPixmap::scroll(int dx, int dy, int x, int y, int width, int
    #      height, QRegion *exposed)
    self.uglySide.call(
        'ritual_ZN7QPixmap6scrollEiiiiiiP7QRegion',
        dx, dy, x, y, width, height, self._addressOf(exposed),
    )

  @overload(int, int, QRect)
  @overload(int, int, QRect, QRegion)
  @overload(int, int, QRect, NoneType)
  def scroll(
      self,
      dx: int,
      dy: int,
      rect: QRect,
      exposed: Optional[QRegion] = None,
  ) -> None:
    """
    Calls Qt's 'void QPixmap::scroll(int dx, int dy, const QRect &rect,
    QRegion *exposed)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#scroll

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    exposed : Optional[QRegion]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QPixmap::scroll(int dx, int dy, const QRect &rect, QRegion
    #      *exposed)
    self.uglySide.call(
        'ritual_ZN7QPixmap6scrollEiiRK5QRectP7QRegion',
        dx, dy, self._valueOf(rect), self._addressOf(exposed),
    )

  def detach(self) -> None:
    """
    Calls Qt's 'void QPixmap::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmap.html#detach
    """
    #  void QPixmap::detach()
    self.uglySide.call('ritual_ZN7QPixmap6detachEv')
