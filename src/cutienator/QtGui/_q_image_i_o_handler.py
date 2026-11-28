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
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QImage

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QIODevice, QRect, QSize, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QIODevice = WAIT['QIODevice']
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
  'allocateImage'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QImageIOHandlerPrivate *QImageIOHandler::d_func()': gives
    'QImageIOHandlerPrivate', which has no cute class yet.
  - Qt's 'const QImageIOHandlerPrivate *QImageIOHandler::d_func() const':
    gives 'QImageIOHandlerPrivate', which has no cute class yet.
  - Qt's 'QImageIOHandler::~QImageIOHandler()': the destructor: Python never
    removes a C++ QImageIOHandler.
  - Qt's 'void QImageIOHandler::setFormat(const QByteArray &format) const':
    takes in Python what 'void QImageIOHandler::setFormat(const QByteArray
    &format)' takes.
  - Qt's 'QImageIOHandler::QImageIOHandler(QImageIOHandlerPrivate &dd)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 26 functions Qt declares: 2 forbidden.

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
  - Each name of Qt's QImageIOHandler that has no cute function yet,
    'd_func', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QImageIOHandler, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ImageOption(CuteNum):
    """
    The enum 'QImageIOHandler::ImageOption' of Qt, with the 19 names Qt gives
    in it.
    """

    Size = Kee[int](0)
    ClipRect = Kee[int](1)
    Description = Kee[int](2)
    ScaledClipRect = Kee[int](3)
    ScaledSize = Kee[int](4)
    CompressionRatio = Kee[int](5)
    Gamma = Kee[int](6)
    Quality = Kee[int](7)
    Name = Kee[int](8)
    SubType = Kee[int](9)
    IncrementalReading = Kee[int](10)
    Endianness = Kee[int](11)
    Animation = Kee[int](12)
    BackgroundColor = Kee[int](13)
    ImageFormat = Kee[int](14)
    SupportedSubTypes = Kee[int](15)
    OptimizedWrite = Kee[int](16)
    ProgressiveScanWrite = Kee[int](17)
    ImageTransformation = Kee[int](18)

  class Transformation(CuteFlags):
    """
    The flags enum 'QImageIOHandler::Transformation' of Qt, with the 8 names
    Qt gives in it. Qt names the type of its combinations
    'QImageIOHandler::Transformations'.
    """

    TransformationNone = 0x0
    TransformationMirror = 0x1
    TransformationFlip = 0x2
    TransformationRotate180 = 0x3
    TransformationRotate90 = 0x4
    TransformationMirrorAndRotate90 = 0x5
    TransformationFlipAndRotate90 = 0x6
    TransformationRotate270 = 0x7

  Transformations = Transformation

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QSize, QImage.Format, QImage)
  @overload(QSize, QImage.Format, NoneType)
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

  #  A C++ QImageIOHandler Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QImageIOHandler'

  #  The functions Qt calls itself that QImageIOHandler is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'canRead': (
          ('_ZNK15QImageIOHandler7canReadEv',
           ('bool', 'number', ''),
           ()),
      ),
      'read': (
          ('_ZN15QImageIOHandler4readEP6QImage',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtGui:QImage'),
           )),
      ),
      'write': (
          ('_ZN15QImageIOHandler5writeERK6QImage',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtGui:QImage'),
           )),
      ),
      'option': (
          ('_ZNK15QImageIOHandler6optionENS_11ImageOptionE',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('int', 'enum', 'QtGui:QImageIOHandler.ImageOption'),
           )),
      ),
      'setOption': (
          ('_ZN15QImageIOHandler9setOptionENS_11ImageOptionERK8QVariant',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtGui:QImageIOHandler.ImageOption'),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'supportsOption': (
          ('_ZNK15QImageIOHandler14supportsOptionENS_11ImageOptionE',
           ('bool', 'number', ''),
           (
               ('int', 'enum', 'QtGui:QImageIOHandler.ImageOption'),
           )),
      ),
      'jumpToNextImage': (
          ('_ZN15QImageIOHandler15jumpToNextImageEv',
           ('bool', 'number', ''),
           ()),
      ),
      'jumpToImage': (
          ('_ZN15QImageIOHandler11jumpToImageEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'loopCount': (
          ('_ZNK15QImageIOHandler9loopCountEv',
           ('int', 'number', ''),
           ()),
      ),
      'imageCount': (
          ('_ZNK15QImageIOHandler10imageCountEv',
           ('int', 'number', ''),
           ()),
      ),
      'nextImageDelay': (
          ('_ZNK15QImageIOHandler14nextImageDelayEv',
           ('int', 'number', ''),
           ()),
      ),
      'currentImageNumber': (
          ('_ZNK15QImageIOHandler18currentImageNumberEv',
           ('int', 'number', ''),
           ()),
      ),
      'currentImageRect': (
          ('_ZNK15QImageIOHandler16currentImageRectEv',
           ('address', 'value', 'QtCore:QRect'),
           ()),
      ),
  }

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
    ritual = 'ritual_ZNK15QImageIOHandler6optionENS_11ImageOptionE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QImageIOHandler6optionENS_11ImageOptionE'
    address = self.uglySide.call(ritual, option.value)
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
    ritual = 'ritual_ZNK15QImageIOHandler14supportsOptionENS_11ImageOptionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK15QImageIOHandler14supportsOptionENS_11ImageOption'
          'E')
    return self.uglySide.call(ritual, option.value)

  def loopCount(self) -> int:
    """
    Calls Qt's 'int QImageIOHandler::loopCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimageiohandler.html#loopCount
    """
    #  int QImageIOHandler::loopCount() const
    ritual = 'ritual_ZNK15QImageIOHandler9loopCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QImageIOHandler9loopCountEv'
    return self.uglySide.call(ritual)

  def imageCount(self) -> int:
    """
    Calls Qt's 'int QImageIOHandler::imageCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimageiohandler.html#imageCount
    """
    #  int QImageIOHandler::imageCount() const
    ritual = 'ritual_ZNK15QImageIOHandler10imageCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QImageIOHandler10imageCountEv'
    return self.uglySide.call(ritual)

  def nextImageDelay(self) -> int:
    """
    Calls Qt's 'int QImageIOHandler::nextImageDelay() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimageiohandler.html#nextImageDelay
    """
    #  int QImageIOHandler::nextImageDelay() const
    ritual = 'ritual_ZNK15QImageIOHandler14nextImageDelayEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QImageIOHandler14nextImageDelayEv'
    return self.uglySide.call(ritual)

  def currentImageNumber(self) -> int:
    """
    Calls Qt's 'int QImageIOHandler::currentImageNumber() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimageiohandler.html#currentImageNumber
    """
    #  int QImageIOHandler::currentImageNumber() const
    ritual = 'ritual_ZNK15QImageIOHandler18currentImageNumberEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QImageIOHandler18currentImageNumberEv'
    return self.uglySide.call(ritual)

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
    ritual = 'ritual_ZNK15QImageIOHandler16currentImageRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QImageIOHandler16currentImageRectEv'
    address = self.uglySide.call(ritual)
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
    ritual = (
        'ritual_ZN15QImageIOHandler9setOptionENS_11ImageOptionERK8QVariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QImageIOHandler9setOptionENS_11ImageOptionERK8QVa'
          'riant')
    self.uglySide.call(ritual, option.value, self._valueOf(value))

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
    Notes what was given, for Qt's 'QImageIOHandler::QImageIOHandler()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qimageiohandler.html#QImageIOHandler
    """
    #  QImageIOHandler::QImageIOHandler()
    self._noteCreation(QImageIOHandler, lambda: Rituals.call(
        'ritual_ZN15QImageIOHandlerC1Ev',
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
    ritual = 'ritual_ZN15QImageIOHandler5writeERK6QImage'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QImageIOHandler5writeERK6QImage'
    return self.uglySide.call(ritual, self._valueOf(image))

  def jumpToNextImage(self) -> bool:
    """
    Calls Qt's 'bool QImageIOHandler::jumpToNextImage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimageiohandler.html#jumpToNextImage
    """
    #  bool QImageIOHandler::jumpToNextImage()
    ritual = 'ritual_ZN15QImageIOHandler15jumpToNextImageEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QImageIOHandler15jumpToNextImageEv'
    return self.uglySide.call(ritual)

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
    ritual = 'ritual_ZN15QImageIOHandler11jumpToImageEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QImageIOHandler11jumpToImageEi'
    return self.uglySide.call(ritual, imageNumber)

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QImageIOHandlerPrivate *QImageIOHandler::d_func()': gives
      'QImageIOHandlerPrivate', which has no cute class yet.
    - Qt's 'const QImageIOHandlerPrivate *QImageIOHandler::d_func() const':
      gives 'QImageIOHandlerPrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QImageIOHandler.d_func' has no cute function yet. Qt's "
        "'QImageIOHandlerPrivate *QImageIOHandler::d_func()': gives "
        "'QImageIOHandlerPrivate', which has no cute class yet. Qt's 'const "
        "QImageIOHandlerPrivate *QImageIOHandler::d_func() const': gives "
        "'QImageIOHandlerPrivate', which has no cute class yet.")
