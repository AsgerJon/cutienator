"""
QImageReader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qimagereader.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QStringList
from . import QImage, QImageIOHandler

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QIODevice, QRect, QSize
  from . import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QColor = WAIT['QColor']
  QIODevice = WAIT['QIODevice']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QImageReader(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QImageReader: a plain Python object standing in front
  of one C++ QImageReader.

  What exists
  -----------

  Every function of Qt's QImageReader that has a ritual and that Python can
  call so far, 49 names in all: 'tr', 'setFormat', 'format',
  'setAutoDetectImageFormat', 'autoDetectImageFormat',
  'setDecideFormatFromContent', 'decideFormatFromContent', 'setDevice',
  'device', 'setFileName', 'fileName', 'size', 'effectiveSize',
  'imageFormat', 'textKeys', 'text', 'setClipRect', 'clipRect',
  'setScaledSize', 'scaledSize', 'setQuality', 'quality',
  'setScaledClipRect', 'scaledClipRect', 'setBackgroundColor',
  'backgroundColor', 'supportsAnimation', 'transformation',
  'setAutoTransform', 'autoTransform', 'subType', 'supportedSubTypes',
  'canRead', 'read', 'jumpToNextImage', 'jumpToImage', 'loopCount',
  'imageCount', 'nextImageDelay', 'currentImageNumber', 'currentImageRect',
  'error', 'errorString', 'supportsOption', 'supportedImageFormats',
  'supportedMimeTypes', 'imageFormatsForMimeType', 'allocationLimit',
  'setAllocationLimit'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QImageReader::~QImageReader()': the destructor: Python never
    removes a C++ QImageReader.

  What has no ritual
  ------------------

  2 of the 58 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QImageReader is created at the first use, not by
    'QImageReader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QImageReader.
  """

  #  The enums Qt writes inside QImageReader, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ImageReaderError(CuteNum):
    """
    The enum 'QImageReader::ImageReaderError' of Qt, with the 5 names Qt
    gives in it.
    """

    UnknownError = Kee[int](0)
    FileNotFoundError = Kee[int](1)
    DeviceError = Kee[int](2)
    UnsupportedFormatError = Kee[int](3)
    InvalidDataError = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(
      sourceText: Optional[str],
      disambiguation: Optional[str] = None,
      n: int = -1,
  ) -> str:
    """
    Calls Qt's 'QString QImageReader::tr(const char *sourceText, const char
    *disambiguation, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#tr

    Parameters
    ----------

    sourceText : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    disambiguation : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QImageReader::tr(const char *sourceText, const char
    #      *disambiguation, int n)
    return Rituals.call(
        'ritual_ZN12QImageReader2trEPKcS1_i',
        CuteMixin._bytesOf(sourceText), CuteMixin._bytesOf(disambiguation),
        n,
    )

  @staticmethod
  def supportedImageFormats() -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QImageReader::supportedImageFormats()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagereader.html#supportedImageFormats

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QImageReader::supportedImageFormats()
    address = Rituals.call(
        'ritual_ZN12QImageReader21supportedImageFormatsEv',
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  @staticmethod
  def supportedMimeTypes() -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QImageReader::supportedMimeTypes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagereader.html#supportedMimeTypes

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QImageReader::supportedMimeTypes()
    address = Rituals.call('ritual_ZN12QImageReader18supportedMimeTypesEv')
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  @staticmethod
  @overload(QByteArray)
  def imageFormatsForMimeType(mimeType: QByteArray) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QImageReader::imageFormatsForMimeType(const
    QByteArray &mimeType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagereader.html#imageFormatsForMimeType

    Parameters
    ----------

    mimeType : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QImageReader::imageFormatsForMimeType(const
    #      QByteArray &mimeType)
    address = Rituals.call(
        'ritual_ZN12QImageReader23imageFormatsForMimeTypeERK10QByteArray',
        CuteMixin._valueOf(mimeType),
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  @staticmethod
  def allocationLimit() -> int:
    """
    Calls Qt's 'int QImageReader::allocationLimit()'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#allocationLimit
    """
    #  int QImageReader::allocationLimit()
    return Rituals.call('ritual_ZN12QImageReader15allocationLimitEv')

  @staticmethod
  @overload(int)
  def setAllocationLimit(mbLimit: int) -> None:
    """
    Calls Qt's 'void QImageReader::setAllocationLimit(int mbLimit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagereader.html#setAllocationLimit

    Parameters
    ----------

    mbLimit : int
      Passed on as it is.
    """
    #  void QImageReader::setAllocationLimit(int mbLimit)
    Rituals.call('ritual_ZN12QImageReader18setAllocationLimitEi', mbLimit)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QImageReader'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def format(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QImageReader::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#format

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QImageReader::format() const
    address = self.uglySide.call('ritual_ZNK12QImageReader6formatEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def autoDetectImageFormat(self) -> bool:
    """
    Calls Qt's 'bool QImageReader::autoDetectImageFormat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagereader.html#autoDetectImageFormat
    """
    #  bool QImageReader::autoDetectImageFormat() const
    return self.uglySide.call(
        'ritual_ZNK12QImageReader21autoDetectImageFormatEv',
    )

  def decideFormatFromContent(self) -> bool:
    """
    Calls Qt's 'bool QImageReader::decideFormatFromContent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagereader.html#decideFormatFromContent
    """
    #  bool QImageReader::decideFormatFromContent() const
    return self.uglySide.call(
        'ritual_ZNK12QImageReader23decideFormatFromContentEv',
    )

  def device(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QImageReader::device() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#device

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QImageReader::device() const
    address = self.uglySide.call('ritual_ZNK12QImageReader6deviceEv')
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  def fileName(self) -> str:
    """
    Calls Qt's 'QString QImageReader::fileName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QImageReader::fileName() const
    return self.uglySide.call('ritual_ZNK12QImageReader8fileNameEv')

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QImageReader::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QImageReader::size() const
    address = self.uglySide.call('ritual_ZNK12QImageReader4sizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def effectiveSize(self) -> QSize:
    """
    Calls Qt's 'QSize QImageReader::effectiveSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#effectiveSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QImageReader::effectiveSize() const
    address = self.uglySide.call('ritual_ZNK12QImageReader13effectiveSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload()
  def imageFormat(self) -> QImage.Format:
    """
    Calls Qt's 'QImage::Format QImageReader::imageFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#imageFormat

    Returns
    -------

    QImage.Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QImage.Format(number)'
      gives.
    """
    #  QImage::Format QImageReader::imageFormat() const
    return QImage.Format(self.uglySide.call(
        'ritual_ZNK12QImageReader11imageFormatEv',
    ))

  @staticmethod
  @overload(str)
  def imageFormat(fileName: str) -> QByteArray:
    """
    Calls Qt's 'QByteArray QImageReader::imageFormat(const QString
    &fileName)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#imageFormat

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QImageReader::imageFormat(const QString &fileName)
    address = Rituals.call(
        'ritual_ZN12QImageReader11imageFormatERK7QString', fileName,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  @overload(QIODevice)
  @overload(NoneType)
  def imageFormat(device: Optional[QIODevice]) -> QByteArray:
    """
    Calls Qt's 'QByteArray QImageReader::imageFormat(QIODevice *device)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#imageFormat

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QImageReader::imageFormat(QIODevice *device)
    address = Rituals.call(
        'ritual_ZN12QImageReader11imageFormatEP9QIODevice',
        CuteMixin._addressOf(device),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def textKeys(self) -> QStringList:
    """
    Calls Qt's 'QStringList QImageReader::textKeys() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#textKeys

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QImageReader::textKeys() const
    address = self.uglySide.call('ritual_ZNK12QImageReader8textKeysEv')
    return QStringList._cuteOwning(address)

  @overload(str)
  def text(self, key: str) -> str:
    """
    Calls Qt's 'QString QImageReader::text(const QString &key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#text

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QImageReader::text(const QString &key) const
    return self.uglySide.call(
        'ritual_ZNK12QImageReader4textERK7QString', key,
    )

  def clipRect(self) -> QRect:
    """
    Calls Qt's 'QRect QImageReader::clipRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#clipRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QImageReader::clipRect() const
    address = self.uglySide.call('ritual_ZNK12QImageReader8clipRectEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def scaledSize(self) -> QSize:
    """
    Calls Qt's 'QSize QImageReader::scaledSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#scaledSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QImageReader::scaledSize() const
    address = self.uglySide.call('ritual_ZNK12QImageReader10scaledSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def quality(self) -> int:
    """
    Calls Qt's 'int QImageReader::quality() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#quality
    """
    #  int QImageReader::quality() const
    return self.uglySide.call('ritual_ZNK12QImageReader7qualityEv')

  def scaledClipRect(self) -> QRect:
    """
    Calls Qt's 'QRect QImageReader::scaledClipRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#scaledClipRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QImageReader::scaledClipRect() const
    address = self.uglySide.call(
        'ritual_ZNK12QImageReader14scaledClipRectEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def backgroundColor(self) -> QColor:
    """
    Calls Qt's 'QColor QImageReader::backgroundColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#backgroundColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QImageReader::backgroundColor() const
    address = self.uglySide.call(
        'ritual_ZNK12QImageReader15backgroundColorEv',
    )
    from . import QColor
    return QColor._cuteOwning(address)

  def supportsAnimation(self) -> bool:
    """
    Calls Qt's 'bool QImageReader::supportsAnimation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagereader.html#supportsAnimation
    """
    #  bool QImageReader::supportsAnimation() const
    return self.uglySide.call(
        'ritual_ZNK12QImageReader17supportsAnimationEv',
    )

  def transformation(self) -> QImageIOHandler.Transformations:
    """
    Calls Qt's 'QImageIOHandler::Transformations
    QImageReader::transformation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#transformation

    Returns
    -------

    QImageIOHandler.Transformations
      The value standing for the combination Qt gave back.
    """
    #  QImageIOHandler::Transformations QImageReader::transformation() const
    return QImageIOHandler.Transformations(self.uglySide.call(
        'ritual_ZNK12QImageReader14transformationEv',
    ))

  def autoTransform(self) -> bool:
    """
    Calls Qt's 'bool QImageReader::autoTransform() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#autoTransform
    """
    #  bool QImageReader::autoTransform() const
    return self.uglySide.call('ritual_ZNK12QImageReader13autoTransformEv')

  def subType(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QImageReader::subType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#subType

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QImageReader::subType() const
    address = self.uglySide.call('ritual_ZNK12QImageReader7subTypeEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def supportedSubTypes(self) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QImageReader::supportedSubTypes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagereader.html#supportedSubTypes

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QImageReader::supportedSubTypes() const
    address = self.uglySide.call(
        'ritual_ZNK12QImageReader17supportedSubTypesEv',
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  def canRead(self) -> bool:
    """
    Calls Qt's 'bool QImageReader::canRead() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#canRead
    """
    #  bool QImageReader::canRead() const
    return self.uglySide.call('ritual_ZNK12QImageReader7canReadEv')

  def loopCount(self) -> int:
    """
    Calls Qt's 'int QImageReader::loopCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#loopCount
    """
    #  int QImageReader::loopCount() const
    return self.uglySide.call('ritual_ZNK12QImageReader9loopCountEv')

  def imageCount(self) -> int:
    """
    Calls Qt's 'int QImageReader::imageCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#imageCount
    """
    #  int QImageReader::imageCount() const
    return self.uglySide.call('ritual_ZNK12QImageReader10imageCountEv')

  def nextImageDelay(self) -> int:
    """
    Calls Qt's 'int QImageReader::nextImageDelay() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#nextImageDelay
    """
    #  int QImageReader::nextImageDelay() const
    return self.uglySide.call('ritual_ZNK12QImageReader14nextImageDelayEv')

  def currentImageNumber(self) -> int:
    """
    Calls Qt's 'int QImageReader::currentImageNumber() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagereader.html#currentImageNumber
    """
    #  int QImageReader::currentImageNumber() const
    return self.uglySide.call(
        'ritual_ZNK12QImageReader18currentImageNumberEv',
    )

  def currentImageRect(self) -> QRect:
    """
    Calls Qt's 'QRect QImageReader::currentImageRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#currentImageRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QImageReader::currentImageRect() const
    address = self.uglySide.call(
        'ritual_ZNK12QImageReader16currentImageRectEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def error(self) -> ImageReaderError:
    """
    Calls Qt's 'ImageReaderError QImageReader::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#error

    Returns
    -------

    ImageReaderError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ImageReaderError(number)'
      gives.
    """
    #  ImageReaderError QImageReader::error() const
    return QImageReader.ImageReaderError(self.uglySide.call(
        'ritual_ZNK12QImageReader5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QImageReader::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QImageReader::errorString() const
    return self.uglySide.call('ritual_ZNK12QImageReader11errorStringEv')

  @overload(QImageIOHandler.ImageOption)
  def supportsOption(self, option: QImageIOHandler.ImageOption) -> bool:
    """
    Calls Qt's 'bool
    QImageReader::supportsOption(QImageIOHandler::ImageOption option) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#supportsOption

    Parameters
    ----------

    option : QImageIOHandler.ImageOption
      Passed on as its number.
    """
    #  bool QImageReader::supportsOption(QImageIOHandler::ImageOption option)
    #      const
    return self.uglySide.call(
        'ritual_ZNK12QImageReader14supportsOptionEN15QImageIOHandler11Image'
        'OptionE',
        option.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  def setFormat(self, format: QByteArray) -> None:
    """
    Calls Qt's 'void QImageReader::setFormat(const QByteArray &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#setFormat

    Parameters
    ----------

    format : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QImageReader::setFormat(const QByteArray &format)
    self.uglySide.call(
        'ritual_ZN12QImageReader9setFormatERK10QByteArray',
        self._valueOf(format),
    )

  @overload(bool)
  def setAutoDetectImageFormat(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QImageReader::setAutoDetectImageFormat(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagereader.html#setAutoDetectImageFormat

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QImageReader::setAutoDetectImageFormat(bool enabled)
    self.uglySide.call(
        'ritual_ZN12QImageReader24setAutoDetectImageFormatEb', enabled,
    )

  @overload(bool)
  def setDecideFormatFromContent(self, ignored: bool) -> None:
    """
    Calls Qt's 'void QImageReader::setDecideFormatFromContent(bool ignored)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagereader.html#setDecideFormatFromContent

    Parameters
    ----------

    ignored : bool
      Passed on as it is.
    """
    #  void QImageReader::setDecideFormatFromContent(bool ignored)
    self.uglySide.call(
        'ritual_ZN12QImageReader26setDecideFormatFromContentEb', ignored,
    )

  @overload(QIODevice)
  @overload(NoneType)
  def setDevice(self, device: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void QImageReader::setDevice(QIODevice *device)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#setDevice

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QImageReader::setDevice(QIODevice *device)
    self.uglySide.call(
        'ritual_ZN12QImageReader9setDeviceEP9QIODevice',
        self._addressOf(device),
    )

  @overload(str)
  def setFileName(self, fileName: str) -> None:
    """
    Calls Qt's 'void QImageReader::setFileName(const QString &fileName)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#setFileName

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QImageReader::setFileName(const QString &fileName)
    self.uglySide.call(
        'ritual_ZN12QImageReader11setFileNameERK7QString', fileName,
    )

  @overload(QRect)
  def setClipRect(self, rect: QRect) -> None:
    """
    Calls Qt's 'void QImageReader::setClipRect(const QRect &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#setClipRect

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QImageReader::setClipRect(const QRect &rect)
    self.uglySide.call(
        'ritual_ZN12QImageReader11setClipRectERK5QRect', self._valueOf(rect),
    )

  @overload(QSize)
  def setScaledSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QImageReader::setScaledSize(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#setScaledSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QImageReader::setScaledSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN12QImageReader13setScaledSizeERK5QSize',
        self._valueOf(size),
    )

  @overload(int)
  def setQuality(self, quality: int) -> None:
    """
    Calls Qt's 'void QImageReader::setQuality(int quality)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#setQuality

    Parameters
    ----------

    quality : int
      Passed on as it is.
    """
    #  void QImageReader::setQuality(int quality)
    self.uglySide.call('ritual_ZN12QImageReader10setQualityEi', quality)

  @overload(QRect)
  def setScaledClipRect(self, rect: QRect) -> None:
    """
    Calls Qt's 'void QImageReader::setScaledClipRect(const QRect &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagereader.html#setScaledClipRect

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QImageReader::setScaledClipRect(const QRect &rect)
    self.uglySide.call(
        'ritual_ZN12QImageReader17setScaledClipRectERK5QRect',
        self._valueOf(rect),
    )

  @overload(QColor)
  def setBackgroundColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QImageReader::setBackgroundColor(const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagereader.html#setBackgroundColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QImageReader::setBackgroundColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN12QImageReader18setBackgroundColorERK6QColor',
        self._valueOf(color),
    )

  @overload(bool)
  def setAutoTransform(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QImageReader::setAutoTransform(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#setAutoTransform

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QImageReader::setAutoTransform(bool enabled)
    self.uglySide.call(
        'ritual_ZN12QImageReader16setAutoTransformEb', enabled,
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
    Notes what was given, for Qt's 'QImageReader::QImageReader()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#QImageReader
    """
    #  QImageReader::QImageReader()
    self._noteCreation(QImageReader, lambda: Rituals.call(
        'ritual_ZN12QImageReaderC1Ev',
    ))

  @overload(QIODevice)
  @overload(NoneType)
  @overload(QIODevice, QByteArray)
  @overload(NoneType, QByteArray)
  def __init__(
      self,
      device: Optional[QIODevice],
      format: Optional[QByteArray] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QImageReader::QImageReader(QIODevice
    *device, const QByteArray &format)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#QImageReader

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    format : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.
    """
    #  QImageReader::QImageReader(QIODevice *device, const QByteArray
    #      &format)
    if format is None:
      from ..QtCore import QByteArray
      format = QByteArray()
    self._noteCreation(QImageReader, lambda: Rituals.call(
        'ritual_ZN12QImageReaderC1EP9QIODeviceRK10QByteArray',
        self._addressOf(device), self._valueOf(format),
    ))

  @overload(str)
  @overload(str, QByteArray)
  def __init__(
      self,
      fileName: str,
      format: Optional[QByteArray] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QImageReader::QImageReader(const QString
    &fileName, const QByteArray &format)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#QImageReader

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    format : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.
    """
    #  QImageReader::QImageReader(const QString &fileName, const QByteArray
    #      &format)
    if format is None:
      from ..QtCore import QByteArray
      format = QByteArray()
    self._noteCreation(QImageReader, lambda: Rituals.call(
        'ritual_ZN12QImageReaderC1ERK7QStringRK10QByteArray',
        fileName, self._valueOf(format),
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
  def read(self) -> QImage:
    """
    Calls Qt's 'QImage QImageReader::read()'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#read

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QImageReader::read()
    address = self.uglySide.call('ritual_ZN12QImageReader4readEv')
    return QImage._cuteOwning(address)

  @overload(QImage)
  @overload(NoneType)
  def read(self, image: Optional[QImage]) -> bool:
    """
    Calls Qt's 'bool QImageReader::read(QImage *image)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#read

    Parameters
    ----------

    image : Optional[QImage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QImageReader::read(QImage *image)
    return self.uglySide.call(
        'ritual_ZN12QImageReader4readEP6QImage', self._addressOf(image),
    )

  def jumpToNextImage(self) -> bool:
    """
    Calls Qt's 'bool QImageReader::jumpToNextImage()'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#jumpToNextImage
    """
    #  bool QImageReader::jumpToNextImage()
    return self.uglySide.call('ritual_ZN12QImageReader15jumpToNextImageEv')

  @overload(int)
  def jumpToImage(self, imageNumber: int) -> bool:
    """
    Calls Qt's 'bool QImageReader::jumpToImage(int imageNumber)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagereader.html#jumpToImage

    Parameters
    ----------

    imageNumber : int
      Passed on as it is.
    """
    #  bool QImageReader::jumpToImage(int imageNumber)
    return self.uglySide.call(
        'ritual_ZN12QImageReader11jumpToImageEi', imageNumber,
    )
