"""
QRasterPlatformPixmap binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qpixmap_raster_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QRasterPlatformPixmap to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QImage, QPaintDevice, QPlatformPixmap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRect
  from . import QColor, QImageReader, QPaintEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QImageReader = WAIT['QImageReader']
  QRect = WAIT['QRect']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRasterPlatformPixmap(QPlatformPixmap):
  """
  The cute side of Qt's QRasterPlatformPixmap: a plain Python object standing
  in front of one C++ QRasterPlatformPixmap.

  It is built on the cute 'QPlatformPixmap', as Qt's QRasterPlatformPixmap is
  built on Qt's QPlatformPixmap, and has everything that class has.

  C++ hands a QRasterPlatformPixmap around as a copy, so every C++
  QRasterPlatformPixmap behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRasterPlatformPixmap that has a ritual and that
  Python can call so far, 16 names in all: 'createCompatiblePlatformPixmap',
  'resize', 'fromImage', 'fromImageReader', 'copy', 'scroll', 'fill',
  'hasAlphaChannel', 'toImage', 'paintEngine', 'buffer', 'devicePixelRatio',
  'setDevicePixelRatio', 'metric', 'createPixmapForImage',
  'systemNativeFormat'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRasterPlatformPixmap::~QRasterPlatformPixmap()': the destructor:
    Python removes its C++ QRasterPlatformPixmap by it, and has no other use
    for it.
  - Qt's 'bool QRasterPlatformPixmap::fromData(const uchar *buffer, uint len,
    const char *format, Qt::ImageConversionFlags flags)': names 'uchar',
    which has no cute class yet.
  - Qt's 'void QRasterPlatformPixmap::fromImageInPlace(QImage &image,
    Qt::ImageConversionFlags flags)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  1 of the 22 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QRasterPlatformPixmap is created at the first use, not by
    'QRasterPlatformPixmap(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRasterPlatformPixmap back gives a copy the ritual
    made for Python, in a new cute QRasterPlatformPixmap.
  - Each name of Qt's QRasterPlatformPixmap that has no cute function yet,
    'setImage', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def systemNativeFormat() -> QImage.Format:
    """
    Calls Qt's 'QImage::Format QRasterPlatformPixmap::systemNativeFormat()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterplatformpixmap.html#systemNativeFormat

    Returns
    -------

    QImage.Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QImage.Format(number)'
      gives.
    """
    #  QImage::Format QRasterPlatformPixmap::systemNativeFormat()
    return QImage.Format(Rituals.call(
        'ritual_ZN21QRasterPlatformPixmap18systemNativeFormatEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRasterPlatformPixmap'

  #  A C++ QRasterPlatformPixmap Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRasterPlatformPixmap'

  #  Qt's '~QRasterPlatformPixmap()'. Naming it makes this a value class:
  #  Python owns every C++ QRasterPlatformPixmap behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QRasterPlatformPixmapD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def createCompatiblePlatformPixmap(self) -> Optional[QPlatformPixmap]:
    """
    Calls Qt's 'QPlatformPixmap
    *QRasterPlatformPixmap::createCompatiblePlatformPixmap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterplatformpixmap.html

    Returns
    -------

    Optional[QPlatformPixmap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformPixmap
    #      *QRasterPlatformPixmap::createCompatiblePlatformPixmap() const
    ritual = (
        'ritual_ZNK21QRasterPlatformPixmap30createCompatiblePlatformPixmapE'
        'v')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QRasterPlatformPixmap30createCompatiblePlatformP'
          'ixmapEv')
    address = self.uglySide.call(ritual)
    return QPlatformPixmap._cuteAt(address)

  def hasAlphaChannel(self) -> bool:
    """
    Calls Qt's 'bool QRasterPlatformPixmap::hasAlphaChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterplatformpixmap.html#hasAlphaChannel
    """
    #  bool QRasterPlatformPixmap::hasAlphaChannel() const
    ritual = 'ritual_ZNK21QRasterPlatformPixmap15hasAlphaChannelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QRasterPlatformPixmap15hasAlphaChannelEv'
    return self.uglySide.call(ritual)

  @overload()
  def toImage(self) -> QImage:
    """
    Calls Qt's 'QImage QRasterPlatformPixmap::toImage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterplatformpixmap.html#toImage

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QRasterPlatformPixmap::toImage() const
    ritual = 'ritual_ZNK21QRasterPlatformPixmap7toImageEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QRasterPlatformPixmap7toImageEv'
    address = self.uglySide.call(ritual)
    return QImage._cuteOwning(address)

  @overload(QRect)
  def toImage(self, rect: QRect) -> QImage:
    """
    Calls Qt's 'QImage QRasterPlatformPixmap::toImage(const QRect &rect)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterplatformpixmap.html#toImage

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QRasterPlatformPixmap::toImage(const QRect &rect) const
    ritual = 'ritual_ZNK21QRasterPlatformPixmap7toImageERK5QRect'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QRasterPlatformPixmap7toImageERK5QRect'
    address = self.uglySide.call(ritual, self._valueOf(rect))
    return QImage._cuteOwning(address)

  def paintEngine(self) -> Optional[QPaintEngine]:
    """
    Calls Qt's 'QPaintEngine *QRasterPlatformPixmap::paintEngine() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterplatformpixmap.html#paintEngine

    Returns
    -------

    Optional[QPaintEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintEngine *QRasterPlatformPixmap::paintEngine() const
    ritual = 'ritual_ZNK21QRasterPlatformPixmap11paintEngineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QRasterPlatformPixmap11paintEngineEv'
    address = self.uglySide.call(ritual)
    from . import QPaintEngine
    return QPaintEngine._cuteAt(address)

  def devicePixelRatio(self) -> float:
    """
    Calls Qt's 'qreal QRasterPlatformPixmap::devicePixelRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterplatformpixmap.html#devicePixelRatio
    """
    #  qreal QRasterPlatformPixmap::devicePixelRatio() const
    ritual = 'ritual_ZNK21QRasterPlatformPixmap16devicePixelRatioEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QRasterPlatformPixmap16devicePixelRatioEv'
    return self.uglySide.call(ritual)

  @overload(QPaintDevice.PaintDeviceMetric)
  def metric(self, metric: QPaintDevice.PaintDeviceMetric) -> int:
    """
    Calls Qt's 'int
    QRasterPlatformPixmap::metric(QPaintDevice::PaintDeviceMetric metric)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterplatformpixmap.html#metric

    Parameters
    ----------

    metric : QPaintDevice.PaintDeviceMetric
      Passed on as its number.
    """
    #  int QRasterPlatformPixmap::metric(QPaintDevice::PaintDeviceMetric
    #      metric) const
    ritual = (
        'ritual_ZNK21QRasterPlatformPixmap6metricEN12QPaintDevice17PaintDev'
        'iceMetricE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QRasterPlatformPixmap6metricEN12QPaintDevice17Pa'
          'intDeviceMetricE')
    return self.uglySide.call(ritual, metric.value)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setDevicePixelRatio(self, scaleFactor: float) -> None:
    """
    Calls Qt's 'void QRasterPlatformPixmap::setDevicePixelRatio(qreal
    scaleFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterplatformpixmap.html#setDevicePixelRatio

    Parameters
    ----------

    scaleFactor : float
      Passed on as it is.
    """
    #  void QRasterPlatformPixmap::setDevicePixelRatio(qreal scaleFactor)
    ritual = 'ritual_ZN21QRasterPlatformPixmap19setDevicePixelRatioEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QRasterPlatformPixmap19setDevicePixelRatioEd'
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

  @overload(QPlatformPixmap.PixelType)
  def __init__(self, type: QPlatformPixmap.PixelType) -> None:
    """
    Notes what was given, for Qt's
    'QRasterPlatformPixmap::QRasterPlatformPixmap(PixelType type)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterplatformpixmap.html#QRasterPlatformPixmap

    Parameters
    ----------

    type : QPlatformPixmap.PixelType
      Passed on as its number.
    """
    #  QRasterPlatformPixmap::QRasterPlatformPixmap(PixelType type)
    self._noteCreation(QRasterPlatformPixmap, lambda: Rituals.call(
        'ritual_ZN21QRasterPlatformPixmapC1EN15QPlatformPixmap9PixelTypeE',
        type.value,
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
    Calls Qt's 'void QRasterPlatformPixmap::resize(int width, int height)'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterplatformpixmap.html#resize

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void QRasterPlatformPixmap::resize(int width, int height)
    ritual = 'ritual_ZN21QRasterPlatformPixmap6resizeEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QRasterPlatformPixmap6resizeEii'
    self.uglySide.call(ritual, width, height)

  @overload(QImage, Qt.ImageConversionFlags)
  def fromImage(self, image: QImage, flags: Qt.ImageConversionFlags) -> None:
    """
    Calls Qt's 'void QRasterPlatformPixmap::fromImage(const QImage &image,
    Qt::ImageConversionFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterplatformpixmap.html#fromImage

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    flags : Qt.ImageConversionFlags
      Passed on as its number.
    """
    #  void QRasterPlatformPixmap::fromImage(const QImage &image,
    #      Qt::ImageConversionFlags flags)
    ritual = (
        'ritual_ZN21QRasterPlatformPixmap9fromImageERK6QImage6QFlagsIN2Qt19'
        'ImageConversionFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QRasterPlatformPixmap9fromImageERK6QImage6QFlagsI'
          'N2Qt19ImageConversionFlagEE')
    self.uglySide.call(ritual, self._valueOf(image), flags.value)

  @overload(QImageReader, Qt.ImageConversionFlags)
  @overload(NoneType, Qt.ImageConversionFlags)
  def fromImageReader(
      self,
      imageReader: Optional[QImageReader],
      flags: Qt.ImageConversionFlags,
  ) -> None:
    """
    Calls Qt's 'void QRasterPlatformPixmap::fromImageReader(QImageReader
    *imageReader, Qt::ImageConversionFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterplatformpixmap.html#fromImageReader

    Parameters
    ----------

    imageReader : Optional[QImageReader]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : Qt.ImageConversionFlags
      Passed on as its number.
    """
    #  void QRasterPlatformPixmap::fromImageReader(QImageReader *imageReader,
    #      Qt::ImageConversionFlags flags)
    ritual = (
        'ritual_ZN21QRasterPlatformPixmap15fromImageReaderEP12QImageReader6'
        'QFlagsIN2Qt19ImageConversionFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QRasterPlatformPixmap15fromImageReaderEP12QImageR'
          'eader6QFlagsIN2Qt19ImageConversionFlagEE')
    self.uglySide.call(ritual, self._addressOf(imageReader), flags.value)

  @overload(QPlatformPixmap, QRect)
  @overload(NoneType, QRect)
  def copy(self, data: Optional[QPlatformPixmap], rect: QRect) -> None:
    """
    Calls Qt's 'void QRasterPlatformPixmap::copy(const QPlatformPixmap *data,
    const QRect &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterplatformpixmap.html#copy

    Parameters
    ----------

    data : Optional[QPlatformPixmap]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QRasterPlatformPixmap::copy(const QPlatformPixmap *data, const
    #      QRect &rect)
    ritual = (
        'ritual_ZN21QRasterPlatformPixmap4copyEPK15QPlatformPixmapRK5QRect')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QRasterPlatformPixmap4copyEPK15QPlatformPixmapRK5'
          'QRect')
    self.uglySide.call(ritual, self._addressOf(data), self._valueOf(rect))

  @overload(int, int, QRect)
  def scroll(self, dx: int, dy: int, rect: QRect) -> bool:
    """
    Calls Qt's 'bool QRasterPlatformPixmap::scroll(int dx, int dy, const
    QRect &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterplatformpixmap.html#scroll

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  bool QRasterPlatformPixmap::scroll(int dx, int dy, const QRect &rect)
    ritual = 'ritual_ZN21QRasterPlatformPixmap6scrollEiiRK5QRect'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QRasterPlatformPixmap6scrollEiiRK5QRect'
    return self.uglySide.call(ritual, dx, dy, self._valueOf(rect))

  @overload(QColor)
  def fill(self, color: QColor) -> None:
    """
    Calls Qt's 'void QRasterPlatformPixmap::fill(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterplatformpixmap.html#fill

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QRasterPlatformPixmap::fill(const QColor &color)
    ritual = 'ritual_ZN21QRasterPlatformPixmap4fillERK6QColor'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QRasterPlatformPixmap4fillERK6QColor'
    self.uglySide.call(ritual, self._valueOf(color))

  def buffer(self) -> Optional[QImage]:
    """
    Calls Qt's 'QImage *QRasterPlatformPixmap::buffer()'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterplatformpixmap.html#buffer

    Returns
    -------

    Optional[QImage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QImage *QRasterPlatformPixmap::buffer()
    ritual = 'ritual_ZN21QRasterPlatformPixmap6bufferEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QRasterPlatformPixmap6bufferEv'
    address = self.uglySide.call(ritual)
    return QImage._cuteAt(address)

  @overload(QImage, Qt.ImageConversionFlags)
  def createPixmapForImage(
      self,
      sourceImage: QImage,
      flags: Qt.ImageConversionFlags,
  ) -> None:
    """
    Calls Qt's 'void QRasterPlatformPixmap::createPixmapForImage(QImage
    sourceImage, Qt::ImageConversionFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterplatformpixmap.html#createPixmapForImage

    Parameters
    ----------

    sourceImage : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    flags : Qt.ImageConversionFlags
      Passed on as its number.
    """
    #  void QRasterPlatformPixmap::createPixmapForImage(QImage sourceImage,
    #      Qt::ImageConversionFlags flags)
    self.uglySide.call(
        'ritual_ZN21QRasterPlatformPixmap20createPixmapForImageE6QImage6QFl'
        'agsIN2Qt19ImageConversionFlagEE',
        self._valueOf(sourceImage), flags.value,
    )

  @staticmethod
  def setImage(*__, **_) -> Never:
    """
    Qt's 'void QRasterPlatformPixmap::setImage(const QImage &image)': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QRasterPlatformPixmap.setImage' has no cute function yet. Qt's "
        "'void QRasterPlatformPixmap::setImage(const QImage &image)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")
