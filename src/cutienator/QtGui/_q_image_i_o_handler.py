"""
QImageIOHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qimageiohandler.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QImageFormat, QImageIOHandlerImageOption
from . import QImageIOHandlerTransformation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QIODevice, QRect, QSize, QVariant
  from . import QImage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QIODevice = WAIT['QIODevice']
  QImage = WAIT['QImage']
  QSize = WAIT['QSize']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QImageIOHandler(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QImageIOHandler: a plain Python object standing in
  front of one C++ QImageIOHandler.

  What exists
  -----------

  Every function of Qt's QImageIOHandler that has a ritual and that Python
  can call so far, 18 names in all: 'setDevice', 'device', 'setFormat',
  'format', 'canRead', 'read', 'write', 'option', 'setOption',
  'supportsOption', 'jumpToNextImage', 'jumpToImage', 'loopCount',
  'imageCount', 'nextImageDelay', 'currentImageNumber', 'currentImageRect',
  'allocateImage'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QImageIOHandler::~QImageIOHandler()': the destructor: Python never
    removes a C++ QImageIOHandler.
  - Qt's 'void QImageIOHandler::setFormat(const QByteArray &format) const':
    takes in Python what 'void QImageIOHandler::setFormat(const QByteArray
    &format)' takes.

  What has no ritual
  ------------------

  6 of the 26 functions Qt declares: 2 private; 2 forbidden; 1 the class is
  abstract, so C++ cannot make one; 1 protected.

  What to expect
  --------------

  - The C++ QImageIOHandler is created at the first use, not by
    'QImageIOHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QImageIOHandler.
  """

  #  The enums Qt writes inside QImageIOHandler, and the names Qt has for the
  #  combinations of its flags enums.
  ImageOption = QImageIOHandlerImageOption
  Transformation = QImageIOHandlerTransformation
  Transformations = QImageIOHandlerTransformation

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QSize, QImageFormat, QImage)
  @overload(QSize, QImageFormat, NoneType)
  def allocateImage(
      size: QSize,
      format: QImage.Format,
      image: Optional[QImage],
  ) -> bool:
    """
    Calls Qt's 'bool QImageIOHandler::allocateImage(QSize size,
    QImage::Format format, QImage *image)'.

    Qt's own words: https://doc.qt.io/qt-6/qimageiohandler.html#allocateImage

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    format : QImage.Format
      Passed on as its number.

    image : Optional[QImage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QImageIOHandler::allocateImage(QSize size, QImage::Format format,
    #      QImage *image)
    return Rituals.call(
        'ritual_ZN15QImageIOHandler13allocateImageE5QSizeN6QImage6FormatEPS'
        '1_',
        CuteMixin._valueOf(size), format.value, CuteMixin._addressOf(image),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QImageIOHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def device(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QImageIOHandler::device() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimageiohandler.html#device

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QImageIOHandler::device() const
    address = self.uglySide.call('ritual_ZNK15QImageIOHandler6deviceEv')
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  def format(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QImageIOHandler::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimageiohandler.html#format

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QImageIOHandler::format() const
    address = self.uglySide.call('ritual_ZNK15QImageIOHandler6formatEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def canRead(self) -> bool:
    """
    Calls Qt's 'bool QImageIOHandler::canRead() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimageiohandler.html#canRead
    """
    #  bool QImageIOHandler::canRead() const
    return self.uglySide.call('ritual_ZNK15QImageIOHandler7canReadEv')

  @overload(ImageOption)
  def option(self, option: ImageOption) -> QVariant:
    """
    Calls Qt's 'QVariant QImageIOHandler::option(ImageOption option) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimageiohandler.html#option

    Parameters
    ----------

    option : ImageOption
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QImageIOHandler::option(ImageOption option) const
    address = self.uglySide.call(
        'ritual_ZNK15QImageIOHandler6optionENS_11ImageOptionE', option.value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(ImageOption)
  def supportsOption(self, option: ImageOption) -> bool:
    """
    Calls Qt's 'bool QImageIOHandler::supportsOption(ImageOption option)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimageiohandler.html#supportsOption

    Parameters
    ----------

    option : ImageOption
      Passed on as its number.
    """
    #  bool QImageIOHandler::supportsOption(ImageOption option) const
    return self.uglySide.call(
        'ritual_ZNK15QImageIOHandler14supportsOptionENS_11ImageOptionE',
        option.value,
    )

  def loopCount(self) -> int:
    """
    Calls Qt's 'int QImageIOHandler::loopCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimageiohandler.html#loopCount
    """
    #  int QImageIOHandler::loopCount() const
    return self.uglySide.call('ritual_ZNK15QImageIOHandler9loopCountEv')

  def imageCount(self) -> int:
    """
    Calls Qt's 'int QImageIOHandler::imageCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimageiohandler.html#imageCount
    """
    #  int QImageIOHandler::imageCount() const
    return self.uglySide.call('ritual_ZNK15QImageIOHandler10imageCountEv')

  def nextImageDelay(self) -> int:
    """
    Calls Qt's 'int QImageIOHandler::nextImageDelay() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimageiohandler.html#nextImageDelay
    """
    #  int QImageIOHandler::nextImageDelay() const
    return self.uglySide.call(
        'ritual_ZNK15QImageIOHandler14nextImageDelayEv',
    )

  def currentImageNumber(self) -> int:
    """
    Calls Qt's 'int QImageIOHandler::currentImageNumber() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimageiohandler.html#currentImageNumber
    """
    #  int QImageIOHandler::currentImageNumber() const
    return self.uglySide.call(
        'ritual_ZNK15QImageIOHandler18currentImageNumberEv',
    )

  def currentImageRect(self) -> QRect:
    """
    Calls Qt's 'QRect QImageIOHandler::currentImageRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimageiohandler.html#currentImageRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QImageIOHandler::currentImageRect() const
    address = self.uglySide.call(
        'ritual_ZNK15QImageIOHandler16currentImageRectEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QIODevice)
  @overload(NoneType)
  def setDevice(self, device: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void QImageIOHandler::setDevice(QIODevice *device)'.

    Qt's own words: https://doc.qt.io/qt-6/qimageiohandler.html#setDevice

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QImageIOHandler::setDevice(QIODevice *device)
    self.uglySide.call(
        'ritual_ZN15QImageIOHandler9setDeviceEP9QIODevice',
        self._addressOf(device),
    )

  @overload(QByteArray)
  def setFormat(self, format: QByteArray) -> None:
    """
    Calls Qt's 'void QImageIOHandler::setFormat(const QByteArray &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qimageiohandler.html#setFormat

    Parameters
    ----------

    format : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QImageIOHandler::setFormat(const QByteArray &format)
    self.uglySide.call(
        'ritual_ZN15QImageIOHandler9setFormatERK10QByteArray',
        self._valueOf(format),
    )

  @overload(ImageOption, QVariant)
  def setOption(self, option: ImageOption, value: QVariant) -> None:
    """
    Calls Qt's 'void QImageIOHandler::setOption(ImageOption option, const
    QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qimageiohandler.html#setOption

    Parameters
    ----------

    option : ImageOption
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QImageIOHandler::setOption(ImageOption option, const QVariant
    #      &value)
    self.uglySide.call(
        'ritual_ZN15QImageIOHandler9setOptionENS_11ImageOptionERK8QVariant',
        option.value, self._valueOf(value),
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

  @overload(QImage)
  @overload(NoneType)
  def read(self, image: Optional[QImage]) -> bool:
    """
    Calls Qt's 'bool QImageIOHandler::read(QImage *image)'.

    Qt's own words: https://doc.qt.io/qt-6/qimageiohandler.html#read

    Parameters
    ----------

    image : Optional[QImage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QImageIOHandler::read(QImage *image)
    return self.uglySide.call(
        'ritual_ZN15QImageIOHandler4readEP6QImage', self._addressOf(image),
    )

  @overload(QImage)
  def write(self, image: QImage) -> bool:
    """
    Calls Qt's 'bool QImageIOHandler::write(const QImage &image)'.

    Qt's own words: https://doc.qt.io/qt-6/qimageiohandler.html#write

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  bool QImageIOHandler::write(const QImage &image)
    return self.uglySide.call(
        'ritual_ZN15QImageIOHandler5writeERK6QImage', self._valueOf(image),
    )

  def jumpToNextImage(self) -> bool:
    """
    Calls Qt's 'bool QImageIOHandler::jumpToNextImage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimageiohandler.html#jumpToNextImage
    """
    #  bool QImageIOHandler::jumpToNextImage()
    return self.uglySide.call(
        'ritual_ZN15QImageIOHandler15jumpToNextImageEv',
    )

  @overload(int)
  def jumpToImage(self, imageNumber: int) -> bool:
    """
    Calls Qt's 'bool QImageIOHandler::jumpToImage(int imageNumber)'.

    Qt's own words: https://doc.qt.io/qt-6/qimageiohandler.html#jumpToImage

    Parameters
    ----------

    imageNumber : int
      Passed on as it is.
    """
    #  bool QImageIOHandler::jumpToImage(int imageNumber)
    return self.uglySide.call(
        'ritual_ZN15QImageIOHandler11jumpToImageEi', imageNumber,
    )
