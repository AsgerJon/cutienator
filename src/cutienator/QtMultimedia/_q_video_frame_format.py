"""
QVideoFrameFormat binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/qvideoframeformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtGui import QImage
from . import QtVideo

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QRect, QSize
  from ..QtGui import QMatrix4x4
  from . import QVideoFrame
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QMatrix4x4 = WAIT['QMatrix4x4']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']
  QVideoFrame = WAIT['QVideoFrame']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QVideoFrameFormat(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QVideoFrameFormat: a plain Python object standing in
  front of one C++ QVideoFrameFormat.

  C++ hands a QVideoFrameFormat around as a copy, so every C++
  QVideoFrameFormat behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QVideoFrameFormat that has a ritual and that Python
  can call so far, 38 names in all: 'detach', '__eq__', '__ne__', 'isValid',
  'pixelFormat', 'frameSize', 'setFrameSize', 'frameWidth', 'frameHeight',
  'planeCount', 'viewport', 'setViewport', 'scanLineDirection',
  'setScanLineDirection', 'frameRate', 'setFrameRate', 'streamFrameRate',
  'setStreamFrameRate', 'yCbCrColorSpace', 'setYCbCrColorSpace',
  'colorSpace', 'setColorSpace', 'colorTransfer', 'setColorTransfer',
  'colorRange', 'setColorRange', 'isMirrored', 'setMirrored', 'rotation',
  'setRotation', 'vertexShaderFileName', 'fragmentShaderFileName',
  'updateUniformData', 'maxLuminance', 'setMaxLuminance',
  'pixelFormatFromImageFormat', 'imageFormatFromPixelFormat',
  'pixelFormatToString'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVideoFrameFormat::~QVideoFrameFormat()': the destructor: Python
    removes its C++ QVideoFrameFormat by it, and has no other use for it.
  - Qt's 'QVideoFrameFormat::QVideoFrameFormat(QVideoFrameFormat &&other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QVideoFrameFormat &QVideoFrameFormat::operator=(QVideoFrameFormat
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'void QVideoFrameFormat::swap(QVideoFrameFormat &other)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QVideoFrameFormat &QVideoFrameFormat::operator=(const
    QVideoFrameFormat &format)': assignment: Python binds a name and has no
    operator for it.

  What has no ritual
  ------------------

  3 of the 50 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QVideoFrameFormat is created at the first use, not by
    'QVideoFrameFormat(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QVideoFrameFormat back gives a copy the ritual made
    for Python, in a new cute QVideoFrameFormat.
  - Each name of Qt's QVideoFrameFormat that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QVideoFrameFormat, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ColorRange(CuteNum):
    """
    The enum 'QVideoFrameFormat::ColorRange' of Qt, with the 3 names Qt gives
    in it.
    """

    ColorRange_Unknown = Kee[int](0)
    ColorRange_Video = Kee[int](1)
    ColorRange_Full = Kee[int](2)

  class ColorSpace(CuteNum):
    """
    The enum 'QVideoFrameFormat::ColorSpace' of Qt, with the 5 names Qt gives
    in it.
    """

    ColorSpace_Undefined = Kee[int](0)
    ColorSpace_BT601 = Kee[int](1)
    ColorSpace_BT709 = Kee[int](2)
    ColorSpace_AdobeRgb = Kee[int](5)
    ColorSpace_BT2020 = Kee[int](6)

  class ColorTransfer(CuteNum):
    """
    The enum 'QVideoFrameFormat::ColorTransfer' of Qt, with the 8 names Qt
    gives in it.
    """

    ColorTransfer_Unknown = Kee[int](0)
    ColorTransfer_BT709 = Kee[int](1)
    ColorTransfer_BT601 = Kee[int](2)
    ColorTransfer_Linear = Kee[int](3)
    ColorTransfer_Gamma22 = Kee[int](4)
    ColorTransfer_Gamma28 = Kee[int](5)
    ColorTransfer_ST2084 = Kee[int](6)
    ColorTransfer_STD_B67 = Kee[int](7)

  class Direction(CuteNum):
    """
    The enum 'QVideoFrameFormat::Direction' of Qt, with the 2 names Qt gives
    in it.
    """

    TopToBottom = Kee[int](0)
    BottomToTop = Kee[int](1)

  class PixelFormat(CuteNum):
    """
    The enum 'QVideoFrameFormat::PixelFormat' of Qt, with the 32 names Qt
    gives in it.
    """

    Format_Invalid = Kee[int](0)
    Format_ARGB8888 = Kee[int](1)
    Format_ARGB8888_Premultiplied = Kee[int](2)
    Format_XRGB8888 = Kee[int](3)
    Format_BGRA8888 = Kee[int](4)
    Format_BGRA8888_Premultiplied = Kee[int](5)
    Format_BGRX8888 = Kee[int](6)
    Format_ABGR8888 = Kee[int](7)
    Format_XBGR8888 = Kee[int](8)
    Format_RGBA8888 = Kee[int](9)
    Format_RGBX8888 = Kee[int](10)
    Format_AYUV = Kee[int](11)
    Format_AYUV_Premultiplied = Kee[int](12)
    Format_YUV420P = Kee[int](13)
    Format_YUV422P = Kee[int](14)
    Format_YV12 = Kee[int](15)
    Format_UYVY = Kee[int](16)
    Format_YUYV = Kee[int](17)
    Format_NV12 = Kee[int](18)
    Format_NV21 = Kee[int](19)
    Format_IMC1 = Kee[int](20)
    Format_IMC2 = Kee[int](21)
    Format_IMC3 = Kee[int](22)
    Format_IMC4 = Kee[int](23)
    Format_Y8 = Kee[int](24)
    Format_Y16 = Kee[int](25)
    Format_P010 = Kee[int](26)
    Format_P016 = Kee[int](27)
    Format_SamplerExternalOES = Kee[int](28)
    Format_Jpeg = Kee[int](29)
    Format_SamplerRect = Kee[int](30)
    Format_YUV420P10 = Kee[int](31)

  class YCbCrColorSpace(CuteNum):
    """
    The enum 'QVideoFrameFormat::YCbCrColorSpace' of Qt, with the 7 names Qt
    gives in it.
    """

    YCbCr_Undefined = Kee[int](0)
    YCbCr_BT601 = Kee[int](1)
    YCbCr_BT709 = Kee[int](2)
    YCbCr_xvYCC601 = Kee[int](3)
    YCbCr_xvYCC709 = Kee[int](4)
    YCbCr_JPEG = Kee[int](5)
    YCbCr_BT2020 = Kee[int](6)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QImage.Format)
  def pixelFormatFromImageFormat(format: QImage.Format) -> PixelFormat:
    """
    Calls Qt's 'PixelFormat
    QVideoFrameFormat::pixelFormatFromImageFormat(QImage::Format format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeformat.html#pixelFormatFromImageFormat

    Parameters
    ----------

    format : QImage.Format
      Passed on as its number.

    Returns
    -------

    PixelFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PixelFormat(number)'
      gives.
    """
    #  PixelFormat
    #      QVideoFrameFormat::pixelFormatFromImageFormat(QImage::Format
    #      format)
    return QVideoFrameFormat.PixelFormat(Rituals.call(
        'ritual_ZN17QVideoFrameFormat26pixelFormatFromImageFormatEN6QImage6'
        'FormatE',
        format.value,
    ))

  @staticmethod
  @overload(PixelFormat)
  def imageFormatFromPixelFormat(format: PixelFormat) -> QImage.Format:
    """
    Calls Qt's 'QImage::Format
    QVideoFrameFormat::imageFormatFromPixelFormat(PixelFormat format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeformat.html#imageFormatFromPixelFormat

    Parameters
    ----------

    format : PixelFormat
      Passed on as its number.

    Returns
    -------

    QImage.Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QImage.Format(number)'
      gives.
    """
    #  QImage::Format
    #      QVideoFrameFormat::imageFormatFromPixelFormat(PixelFormat format)
    return QImage.Format(Rituals.call(
        'ritual_ZN17QVideoFrameFormat26imageFormatFromPixelFormatENS_11Pixe'
        'lFormatE',
        format.value,
    ))

  @staticmethod
  @overload(PixelFormat)
  def pixelFormatToString(pixelFormat: PixelFormat) -> str:
    """
    Calls Qt's 'QString
    QVideoFrameFormat::pixelFormatToString(QVideoFrameFormat::PixelFormat
    pixelFormat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeformat.html#pixelFormatToString

    Parameters
    ----------

    pixelFormat : PixelFormat
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QVideoFrameFormat::pixelFormatToString(QVideoFrameFormat::
    #      PixelFormat pixelFormat)
    return Rituals.call(
        'ritual_ZN17QVideoFrameFormat19pixelFormatToStringENS_11PixelFormat'
        'E',
        pixelFormat.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVideoFrameFormat'

  #  Qt's '~QVideoFrameFormat()'. Naming it makes this a value class: Python
  #  owns every C++ QVideoFrameFormat behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QVideoFrameFormatD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QVideoFrameFormat::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframeformat.html#isValid
    """
    #  bool QVideoFrameFormat::isValid() const
    return self.uglySide.call('ritual_ZNK17QVideoFrameFormat7isValidEv')

  def pixelFormat(self) -> PixelFormat:
    """
    Calls Qt's 'QVideoFrameFormat::PixelFormat
    QVideoFrameFormat::pixelFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframeformat.html#pixelFormat

    Returns
    -------

    PixelFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PixelFormat(number)'
      gives.
    """
    #  QVideoFrameFormat::PixelFormat QVideoFrameFormat::pixelFormat() const
    return QVideoFrameFormat.PixelFormat(self.uglySide.call(
        'ritual_ZNK17QVideoFrameFormat11pixelFormatEv',
    ))

  def frameSize(self) -> QSize:
    """
    Calls Qt's 'QSize QVideoFrameFormat::frameSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframeformat.html#frameSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QVideoFrameFormat::frameSize() const
    address = self.uglySide.call('ritual_ZNK17QVideoFrameFormat9frameSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def frameWidth(self) -> int:
    """
    Calls Qt's 'int QVideoFrameFormat::frameWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframeformat.html#frameWidth
    """
    #  int QVideoFrameFormat::frameWidth() const
    return self.uglySide.call('ritual_ZNK17QVideoFrameFormat10frameWidthEv')

  def frameHeight(self) -> int:
    """
    Calls Qt's 'int QVideoFrameFormat::frameHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframeformat.html#frameHeight
    """
    #  int QVideoFrameFormat::frameHeight() const
    return self.uglySide.call('ritual_ZNK17QVideoFrameFormat11frameHeightEv')

  def planeCount(self) -> int:
    """
    Calls Qt's 'int QVideoFrameFormat::planeCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframeformat.html#planeCount
    """
    #  int QVideoFrameFormat::planeCount() const
    return self.uglySide.call('ritual_ZNK17QVideoFrameFormat10planeCountEv')

  def viewport(self) -> QRect:
    """
    Calls Qt's 'QRect QVideoFrameFormat::viewport() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframeformat.html#viewport

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QVideoFrameFormat::viewport() const
    address = self.uglySide.call('ritual_ZNK17QVideoFrameFormat8viewportEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def scanLineDirection(self) -> Direction:
    """
    Calls Qt's 'Direction QVideoFrameFormat::scanLineDirection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeformat.html#scanLineDirection

    Returns
    -------

    Direction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Direction(number)' gives.
    """
    #  Direction QVideoFrameFormat::scanLineDirection() const
    return QVideoFrameFormat.Direction(self.uglySide.call(
        'ritual_ZNK17QVideoFrameFormat17scanLineDirectionEv',
    ))

  def frameRate(self) -> float:
    """
    Calls Qt's 'qreal QVideoFrameFormat::frameRate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframeformat.html#frameRate
    """
    #  qreal QVideoFrameFormat::frameRate() const
    return self.uglySide.call('ritual_ZNK17QVideoFrameFormat9frameRateEv')

  def streamFrameRate(self) -> float:
    """
    Calls Qt's 'qreal QVideoFrameFormat::streamFrameRate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeformat.html#streamFrameRate
    """
    #  qreal QVideoFrameFormat::streamFrameRate() const
    return self.uglySide.call(
        'ritual_ZNK17QVideoFrameFormat15streamFrameRateEv',
    )

  def yCbCrColorSpace(self) -> YCbCrColorSpace:
    """
    Calls Qt's 'YCbCrColorSpace QVideoFrameFormat::yCbCrColorSpace() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeformat.html#yCbCrColorSpace

    Returns
    -------

    YCbCrColorSpace
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'YCbCrColorSpace(number)'
      gives.
    """
    #  YCbCrColorSpace QVideoFrameFormat::yCbCrColorSpace() const
    return QVideoFrameFormat.YCbCrColorSpace(self.uglySide.call(
        'ritual_ZNK17QVideoFrameFormat15yCbCrColorSpaceEv',
    ))

  def colorSpace(self) -> ColorSpace:
    """
    Calls Qt's 'ColorSpace QVideoFrameFormat::colorSpace() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframeformat.html#colorSpace

    Returns
    -------

    ColorSpace
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ColorSpace(number)'
      gives.
    """
    #  ColorSpace QVideoFrameFormat::colorSpace() const
    return QVideoFrameFormat.ColorSpace(self.uglySide.call(
        'ritual_ZNK17QVideoFrameFormat10colorSpaceEv',
    ))

  def colorTransfer(self) -> ColorTransfer:
    """
    Calls Qt's 'ColorTransfer QVideoFrameFormat::colorTransfer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeformat.html#colorTransfer

    Returns
    -------

    ColorTransfer
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ColorTransfer(number)'
      gives.
    """
    #  ColorTransfer QVideoFrameFormat::colorTransfer() const
    return QVideoFrameFormat.ColorTransfer(self.uglySide.call(
        'ritual_ZNK17QVideoFrameFormat13colorTransferEv',
    ))

  def colorRange(self) -> ColorRange:
    """
    Calls Qt's 'ColorRange QVideoFrameFormat::colorRange() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframeformat.html#colorRange

    Returns
    -------

    ColorRange
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ColorRange(number)'
      gives.
    """
    #  ColorRange QVideoFrameFormat::colorRange() const
    return QVideoFrameFormat.ColorRange(self.uglySide.call(
        'ritual_ZNK17QVideoFrameFormat10colorRangeEv',
    ))

  def isMirrored(self) -> bool:
    """
    Calls Qt's 'bool QVideoFrameFormat::isMirrored() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframeformat.html#isMirrored
    """
    #  bool QVideoFrameFormat::isMirrored() const
    return self.uglySide.call('ritual_ZNK17QVideoFrameFormat10isMirroredEv')

  def rotation(self) -> QtVideo.Rotation:
    """
    Calls Qt's 'QtVideo::Rotation QVideoFrameFormat::rotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframeformat.html#rotation

    Returns
    -------

    QtVideo.Rotation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QtVideo.Rotation(number)'
      gives.
    """
    #  QtVideo::Rotation QVideoFrameFormat::rotation() const
    return QtVideo.Rotation(self.uglySide.call(
        'ritual_ZNK17QVideoFrameFormat8rotationEv',
    ))

  def vertexShaderFileName(self) -> str:
    """
    Calls Qt's 'QString QVideoFrameFormat::vertexShaderFileName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeformat.html#vertexShaderFileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QVideoFrameFormat::vertexShaderFileName() const
    return self.uglySide.call(
        'ritual_ZNK17QVideoFrameFormat20vertexShaderFileNameEv',
    )

  def fragmentShaderFileName(self) -> str:
    """
    Calls Qt's 'QString QVideoFrameFormat::fragmentShaderFileName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeformat.html#fragmentShaderFileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QVideoFrameFormat::fragmentShaderFileName() const
    return self.uglySide.call(
        'ritual_ZNK17QVideoFrameFormat22fragmentShaderFileNameEv',
    )

  def maxLuminance(self) -> float:
    """
    Calls Qt's 'float QVideoFrameFormat::maxLuminance() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeformat.html#maxLuminance
    """
    #  float QVideoFrameFormat::maxLuminance() const
    return self.uglySide.call(
        'ritual_ZNK17QVideoFrameFormat12maxLuminanceEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSize)
  def setFrameSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QVideoFrameFormat::setFrameSize(const QSize &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeformat.html#setFrameSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QVideoFrameFormat::setFrameSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN17QVideoFrameFormat12setFrameSizeERK5QSize',
        self._valueOf(size),
    )

  @overload(int, int)
  def setFrameSize(self, width: int, height: int) -> None:
    """
    Calls Qt's 'void QVideoFrameFormat::setFrameSize(int width, int height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeformat.html#setFrameSize

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void QVideoFrameFormat::setFrameSize(int width, int height)
    self.uglySide.call(
        'ritual_ZN17QVideoFrameFormat12setFrameSizeEii', width, height,
    )

  @overload(QRect)
  def setViewport(self, viewport: QRect) -> None:
    """
    Calls Qt's 'void QVideoFrameFormat::setViewport(const QRect &viewport)'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframeformat.html#setViewport

    Parameters
    ----------

    viewport : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QVideoFrameFormat::setViewport(const QRect &viewport)
    self.uglySide.call(
        'ritual_ZN17QVideoFrameFormat11setViewportERK5QRect',
        self._valueOf(viewport),
    )

  @overload(Direction)
  def setScanLineDirection(self, direction: Direction) -> None:
    """
    Calls Qt's 'void QVideoFrameFormat::setScanLineDirection(Direction
    direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeformat.html#setScanLineDirection

    Parameters
    ----------

    direction : Direction
      Passed on as its number.
    """
    #  void QVideoFrameFormat::setScanLineDirection(Direction direction)
    self.uglySide.call(
        'ritual_ZN17QVideoFrameFormat20setScanLineDirectionENS_9DirectionE',
        direction.value,
    )

  @overload(float)
  def setFrameRate(self, rate: float) -> None:
    """
    Calls Qt's 'void QVideoFrameFormat::setFrameRate(qreal rate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeformat.html#setFrameRate

    Parameters
    ----------

    rate : float
      Passed on as it is.
    """
    #  void QVideoFrameFormat::setFrameRate(qreal rate)
    self.uglySide.call('ritual_ZN17QVideoFrameFormat12setFrameRateEd', rate)

  @overload(float)
  def setStreamFrameRate(self, rate: float) -> None:
    """
    Calls Qt's 'void QVideoFrameFormat::setStreamFrameRate(qreal rate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeformat.html#setStreamFrameRate

    Parameters
    ----------

    rate : float
      Passed on as it is.
    """
    #  void QVideoFrameFormat::setStreamFrameRate(qreal rate)
    self.uglySide.call(
        'ritual_ZN17QVideoFrameFormat18setStreamFrameRateEd', rate,
    )

  @overload(YCbCrColorSpace)
  def setYCbCrColorSpace(self, colorSpace: YCbCrColorSpace) -> None:
    """
    Calls Qt's 'void QVideoFrameFormat::setYCbCrColorSpace(YCbCrColorSpace
    colorSpace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeformat.html#setYCbCrColorSpace

    Parameters
    ----------

    colorSpace : YCbCrColorSpace
      Passed on as its number.
    """
    #  void QVideoFrameFormat::setYCbCrColorSpace(YCbCrColorSpace colorSpace)
    self.uglySide.call(
        'ritual_ZN17QVideoFrameFormat18setYCbCrColorSpaceENS_15YCbCrColorSp'
        'aceE',
        colorSpace.value,
    )

  @overload(ColorSpace)
  def setColorSpace(self, colorSpace: ColorSpace) -> None:
    """
    Calls Qt's 'void QVideoFrameFormat::setColorSpace(ColorSpace
    colorSpace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeformat.html#setColorSpace

    Parameters
    ----------

    colorSpace : ColorSpace
      Passed on as its number.
    """
    #  void QVideoFrameFormat::setColorSpace(ColorSpace colorSpace)
    self.uglySide.call(
        'ritual_ZN17QVideoFrameFormat13setColorSpaceENS_10ColorSpaceE',
        colorSpace.value,
    )

  @overload(ColorTransfer)
  def setColorTransfer(self, colorTransfer: ColorTransfer) -> None:
    """
    Calls Qt's 'void QVideoFrameFormat::setColorTransfer(ColorTransfer
    colorTransfer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeformat.html#setColorTransfer

    Parameters
    ----------

    colorTransfer : ColorTransfer
      Passed on as its number.
    """
    #  void QVideoFrameFormat::setColorTransfer(ColorTransfer colorTransfer)
    self.uglySide.call(
        'ritual_ZN17QVideoFrameFormat16setColorTransferENS_13ColorTransferE',
        colorTransfer.value,
    )

  @overload(ColorRange)
  def setColorRange(self, range: ColorRange) -> None:
    """
    Calls Qt's 'void QVideoFrameFormat::setColorRange(ColorRange range)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeformat.html#setColorRange

    Parameters
    ----------

    range : ColorRange
      Passed on as its number.
    """
    #  void QVideoFrameFormat::setColorRange(ColorRange range)
    self.uglySide.call(
        'ritual_ZN17QVideoFrameFormat13setColorRangeENS_10ColorRangeE',
        range.value,
    )

  @overload(bool)
  def setMirrored(self, mirrored: bool) -> None:
    """
    Calls Qt's 'void QVideoFrameFormat::setMirrored(bool mirrored)'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframeformat.html#setMirrored

    Parameters
    ----------

    mirrored : bool
      Passed on as it is.
    """
    #  void QVideoFrameFormat::setMirrored(bool mirrored)
    self.uglySide.call(
        'ritual_ZN17QVideoFrameFormat11setMirroredEb', mirrored,
    )

  @overload(QtVideo.Rotation)
  def setRotation(self, rotation: QtVideo.Rotation) -> None:
    """
    Calls Qt's 'void QVideoFrameFormat::setRotation(QtVideo::Rotation
    rotation)'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframeformat.html#setRotation

    Parameters
    ----------

    rotation : QtVideo.Rotation
      Passed on as its number.
    """
    #  void QVideoFrameFormat::setRotation(QtVideo::Rotation rotation)
    self.uglySide.call(
        'ritual_ZN17QVideoFrameFormat11setRotationEN7QtVideo8RotationE',
        rotation.value,
    )

  @overload(float)
  def setMaxLuminance(self, lum: float) -> None:
    """
    Calls Qt's 'void QVideoFrameFormat::setMaxLuminance(float lum)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeformat.html#setMaxLuminance

    Parameters
    ----------

    lum : float
      Passed on as it is.
    """
    #  void QVideoFrameFormat::setMaxLuminance(float lum)
    self.uglySide.call(
        'ritual_ZN17QVideoFrameFormat15setMaxLuminanceEf', lum,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, format: QVideoFrameFormat) -> bool:
    """
    Calls Qt's 'bool QVideoFrameFormat::operator==(const QVideoFrameFormat
    &format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframeformat.html#operator==

    Parameters
    ----------

    format : QVideoFrameFormat
      Passed on as a value: Qt reads the C++ QVideoFrameFormat, which stays
      Python's own.
    """
    #  bool QVideoFrameFormat::operator==(const QVideoFrameFormat &format)
    #      const
    return self.uglySide.call(
        'ritual_ZNK17QVideoFrameFormateqERKS_', self._valueOf(format),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, format: QVideoFrameFormat) -> bool:
    """
    Calls Qt's 'bool QVideoFrameFormat::operator!=(const QVideoFrameFormat
    &format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframeformat.html#operator!=

    Parameters
    ----------

    format : QVideoFrameFormat
      Passed on as a value: Qt reads the C++ QVideoFrameFormat, which stays
      Python's own.
    """
    #  bool QVideoFrameFormat::operator!=(const QVideoFrameFormat &format)
    #      const
    return self.uglySide.call(
        'ritual_ZNK17QVideoFrameFormatneERKS_', self._valueOf(format),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QVideoFrameFormat::QVideoFrameFormat()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeformat.html#QVideoFrameFormat
    """
    #  QVideoFrameFormat::QVideoFrameFormat()
    self._noteCreation(QVideoFrameFormat, lambda: Rituals.call(
        'ritual_ZN17QVideoFrameFormatC1Ev',
    ))

  @overload(QSize, PixelFormat)
  def __init__(self, size: QSize, pixelFormat: PixelFormat) -> None:
    """
    Notes what was given, for Qt's
    'QVideoFrameFormat::QVideoFrameFormat(const QSize &size, PixelFormat
    pixelFormat)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeformat.html#QVideoFrameFormat

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    pixelFormat : PixelFormat
      Passed on as its number.
    """
    #  QVideoFrameFormat::QVideoFrameFormat(const QSize &size, PixelFormat
    #      pixelFormat)
    self._noteCreation(QVideoFrameFormat, lambda: Rituals.call(
        'ritual_ZN17QVideoFrameFormatC1ERK5QSizeNS_11PixelFormatE',
        self._valueOf(size), pixelFormat.value,
    ))

  @overload(THIS)
  def __init__(self, format: QVideoFrameFormat) -> None:
    """
    Notes what was given, for Qt's
    'QVideoFrameFormat::QVideoFrameFormat(const QVideoFrameFormat &format)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeformat.html#QVideoFrameFormat

    Parameters
    ----------

    format : QVideoFrameFormat
      Passed on as a value: Qt reads the C++ QVideoFrameFormat, which stays
      Python's own.
    """
    #  QVideoFrameFormat::QVideoFrameFormat(const QVideoFrameFormat &format)
    self._noteCreation(QVideoFrameFormat, lambda: Rituals.call(
        'ritual_ZN17QVideoFrameFormatC1ERKS_', self._valueOf(format),
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
    Calls Qt's 'void QVideoFrameFormat::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframeformat.html#detach
    """
    #  void QVideoFrameFormat::detach()
    self.uglySide.call('ritual_ZN17QVideoFrameFormat6detachEv')

  @overload(QByteArray, QVideoFrame, QMatrix4x4, float)
  @overload(NoneType, QVideoFrame, QMatrix4x4, float)
  def updateUniformData(
      self,
      dst: Optional[QByteArray],
      frame: QVideoFrame,
      transform: QMatrix4x4,
      opacity: float,
  ) -> None:
    """
    Calls Qt's 'void QVideoFrameFormat::updateUniformData(QByteArray *dst,
    const QVideoFrame &frame, const QMatrix4x4 &transform, float opacity)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeformat.html#updateUniformData

    Parameters
    ----------

    dst : Optional[QByteArray]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    frame : QVideoFrame
      Passed on as a value: Qt reads the C++ QVideoFrame, which stays
      Python's own.

    transform : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    opacity : float
      Passed on as it is.
    """
    #  void QVideoFrameFormat::updateUniformData(QByteArray *dst, const
    #      QVideoFrame &frame, const QMatrix4x4 &transform, float opacity)
    #      const
    self.uglySide.call(
        'ritual_ZNK17QVideoFrameFormat17updateUniformDataEP10QByteArrayRK11'
        'QVideoFrameRK10QMatrix4x4f',
        self._addressOf(dst), self._valueOf(frame), self._valueOf(transform),
        opacity,
    )

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QVideoFrameFormat::swap(QVideoFrameFormat &other)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QVideoFrameFormat.swap' has no cute function yet. Qt's 'void "
        "QVideoFrameFormat::swap(QVideoFrameFormat &other)': takes a type "
        "Python has no way to hand over yet.")
