"""
QImageWriter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qimagewriter.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QImageIOHandlerImageOption, QImageIOHandlerTransformation
from . import QImageWriterImageWriterError

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QIODevice
  from . import QImage, QImageIOHandler
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QIODevice = WAIT['QIODevice']
  QImage = WAIT['QImage']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QImageWriter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QImageWriter: a plain Python object standing in front
  of one C++ QImageWriter.

  What exists
  -----------

  Every function of Qt's QImageWriter that has a ritual and that Python can
  call so far, 25 names in all: 'tr', 'setFormat', 'format', 'setDevice',
  'device', 'setFileName', 'fileName', 'setQuality', 'quality',
  'setCompression', 'compression', 'setSubType', 'subType',
  'setOptimizedWrite', 'optimizedWrite', 'setProgressiveScanWrite',
  'progressiveScanWrite', 'transformation', 'setTransformation', 'setText',
  'canWrite', 'write', 'error', 'errorString', 'supportsOption'. It can be
  made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QImageWriter::~QImageWriter()': the destructor: Python never
    removes a C++ QImageWriter.

  What has no ritual
  ------------------

  6 of the 35 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 2 forbidden.

  What to expect
  --------------

  - The C++ QImageWriter is created at the first use, not by
    'QImageWriter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QImageWriter.
  """

  #  The enums Qt writes inside QImageWriter, and the names Qt has for the
  #  combinations of its flags enums.
  ImageWriterError = QImageWriterImageWriterError

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
    Calls Qt's 'QString QImageWriter::tr(const char *sourceText, const char
    *disambiguation, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagewriter.html#tr

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
    #  QString QImageWriter::tr(const char *sourceText, const char
    #      *disambiguation, int n)
    return Rituals.call(
        'ritual_ZN12QImageWriter2trEPKcS1_i',
        CuteMixin._bytesOf(sourceText), CuteMixin._bytesOf(disambiguation),
        n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QImageWriter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def format(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QImageWriter::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagewriter.html#format

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QImageWriter::format() const
    address = self.uglySide.call('ritual_ZNK12QImageWriter6formatEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def device(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QImageWriter::device() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagewriter.html#device

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QImageWriter::device() const
    address = self.uglySide.call('ritual_ZNK12QImageWriter6deviceEv')
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  def fileName(self) -> str:
    """
    Calls Qt's 'QString QImageWriter::fileName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagewriter.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QImageWriter::fileName() const
    return self.uglySide.call('ritual_ZNK12QImageWriter8fileNameEv')

  def quality(self) -> int:
    """
    Calls Qt's 'int QImageWriter::quality() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagewriter.html#quality
    """
    #  int QImageWriter::quality() const
    return self.uglySide.call('ritual_ZNK12QImageWriter7qualityEv')

  def compression(self) -> int:
    """
    Calls Qt's 'int QImageWriter::compression() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagewriter.html#compression
    """
    #  int QImageWriter::compression() const
    return self.uglySide.call('ritual_ZNK12QImageWriter11compressionEv')

  def subType(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QImageWriter::subType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagewriter.html#subType

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QImageWriter::subType() const
    address = self.uglySide.call('ritual_ZNK12QImageWriter7subTypeEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def optimizedWrite(self) -> bool:
    """
    Calls Qt's 'bool QImageWriter::optimizedWrite() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagewriter.html#optimizedWrite
    """
    #  bool QImageWriter::optimizedWrite() const
    return self.uglySide.call('ritual_ZNK12QImageWriter14optimizedWriteEv')

  def progressiveScanWrite(self) -> bool:
    """
    Calls Qt's 'bool QImageWriter::progressiveScanWrite() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagewriter.html#progressiveScanWrite
    """
    #  bool QImageWriter::progressiveScanWrite() const
    return self.uglySide.call(
        'ritual_ZNK12QImageWriter20progressiveScanWriteEv',
    )

  def transformation(self) -> QImageIOHandler.Transformations:
    """
    Calls Qt's 'QImageIOHandler::Transformations
    QImageWriter::transformation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagewriter.html#transformation

    Returns
    -------

    QImageIOHandler.Transformations
      The value standing for the combination Qt gave back.
    """
    #  QImageIOHandler::Transformations QImageWriter::transformation() const
    return QImageIOHandlerTransformation(self.uglySide.call(
        'ritual_ZNK12QImageWriter14transformationEv',
    ))

  def canWrite(self) -> bool:
    """
    Calls Qt's 'bool QImageWriter::canWrite() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagewriter.html#canWrite
    """
    #  bool QImageWriter::canWrite() const
    return self.uglySide.call('ritual_ZNK12QImageWriter8canWriteEv')

  def error(self) -> ImageWriterError:
    """
    Calls Qt's 'ImageWriterError QImageWriter::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagewriter.html#error

    Returns
    -------

    ImageWriterError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ImageWriterError(number)'
      gives.
    """
    #  ImageWriterError QImageWriter::error() const
    return QImageWriter.ImageWriterError(self.uglySide.call(
        'ritual_ZNK12QImageWriter5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QImageWriter::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagewriter.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QImageWriter::errorString() const
    return self.uglySide.call('ritual_ZNK12QImageWriter11errorStringEv')

  @overload(QImageIOHandlerImageOption)
  def supportsOption(self, option: QImageIOHandler.ImageOption) -> bool:
    """
    Calls Qt's 'bool
    QImageWriter::supportsOption(QImageIOHandler::ImageOption option) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagewriter.html#supportsOption

    Parameters
    ----------

    option : QImageIOHandler.ImageOption
      Passed on as its number.
    """
    #  bool QImageWriter::supportsOption(QImageIOHandler::ImageOption option)
    #      const
    return self.uglySide.call(
        'ritual_ZNK12QImageWriter14supportsOptionEN15QImageIOHandler11Image'
        'OptionE',
        option.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  def setFormat(self, format: QByteArray) -> None:
    """
    Calls Qt's 'void QImageWriter::setFormat(const QByteArray &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagewriter.html#setFormat

    Parameters
    ----------

    format : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QImageWriter::setFormat(const QByteArray &format)
    self.uglySide.call(
        'ritual_ZN12QImageWriter9setFormatERK10QByteArray',
        self._valueOf(format),
    )

  @overload(QIODevice)
  @overload(NoneType)
  def setDevice(self, device: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void QImageWriter::setDevice(QIODevice *device)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagewriter.html#setDevice

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QImageWriter::setDevice(QIODevice *device)
    self.uglySide.call(
        'ritual_ZN12QImageWriter9setDeviceEP9QIODevice',
        self._addressOf(device),
    )

  @overload(str)
  def setFileName(self, fileName: str) -> None:
    """
    Calls Qt's 'void QImageWriter::setFileName(const QString &fileName)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagewriter.html#setFileName

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QImageWriter::setFileName(const QString &fileName)
    self.uglySide.call(
        'ritual_ZN12QImageWriter11setFileNameERK7QString', fileName,
    )

  @overload(int)
  def setQuality(self, quality: int) -> None:
    """
    Calls Qt's 'void QImageWriter::setQuality(int quality)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagewriter.html#setQuality

    Parameters
    ----------

    quality : int
      Passed on as it is.
    """
    #  void QImageWriter::setQuality(int quality)
    self.uglySide.call('ritual_ZN12QImageWriter10setQualityEi', quality)

  @overload(int)
  def setCompression(self, compression: int) -> None:
    """
    Calls Qt's 'void QImageWriter::setCompression(int compression)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagewriter.html#setCompression

    Parameters
    ----------

    compression : int
      Passed on as it is.
    """
    #  void QImageWriter::setCompression(int compression)
    self.uglySide.call(
        'ritual_ZN12QImageWriter14setCompressionEi', compression,
    )

  @overload(QByteArray)
  def setSubType(self, type: QByteArray) -> None:
    """
    Calls Qt's 'void QImageWriter::setSubType(const QByteArray &type)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagewriter.html#setSubType

    Parameters
    ----------

    type : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QImageWriter::setSubType(const QByteArray &type)
    self.uglySide.call(
        'ritual_ZN12QImageWriter10setSubTypeERK10QByteArray',
        self._valueOf(type),
    )

  @overload(bool)
  def setOptimizedWrite(self, optimize: bool) -> None:
    """
    Calls Qt's 'void QImageWriter::setOptimizedWrite(bool optimize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagewriter.html#setOptimizedWrite

    Parameters
    ----------

    optimize : bool
      Passed on as it is.
    """
    #  void QImageWriter::setOptimizedWrite(bool optimize)
    self.uglySide.call(
        'ritual_ZN12QImageWriter17setOptimizedWriteEb', optimize,
    )

  @overload(bool)
  def setProgressiveScanWrite(self, progressive: bool) -> None:
    """
    Calls Qt's 'void QImageWriter::setProgressiveScanWrite(bool
    progressive)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagewriter.html#setProgressiveScanWrite

    Parameters
    ----------

    progressive : bool
      Passed on as it is.
    """
    #  void QImageWriter::setProgressiveScanWrite(bool progressive)
    self.uglySide.call(
        'ritual_ZN12QImageWriter23setProgressiveScanWriteEb', progressive,
    )

  @overload(QImageIOHandlerTransformation)
  def setTransformation(
      self,
      orientation: QImageIOHandler.Transformations,
  ) -> None:
    """
    Calls Qt's 'void
    QImageWriter::setTransformation(QImageIOHandler::Transformations
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagewriter.html#setTransformation

    Parameters
    ----------

    orientation : QImageIOHandler.Transformations
      Passed on as its number.
    """
    #  void QImageWriter::setTransformation(QImageIOHandler::Transformations
    #      orientation)
    self.uglySide.call(
        'ritual_ZN12QImageWriter17setTransformationE6QFlagsIN15QImageIOHand'
        'ler14TransformationEE',
        orientation.value,
    )

  @overload(str, str)
  def setText(self, key: str, text: str) -> None:
    """
    Calls Qt's 'void QImageWriter::setText(const QString &key, const QString
    &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagewriter.html#setText

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QImageWriter::setText(const QString &key, const QString &text)
    self.uglySide.call(
        'ritual_ZN12QImageWriter7setTextERK7QStringS2_', key, text,
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
    Notes what was given, for Qt's 'QImageWriter::QImageWriter()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qimagewriter.html#QImageWriter
    """
    #  QImageWriter::QImageWriter()
    self._noteCreation(QImageWriter, lambda: Rituals.call(
        'ritual_ZN12QImageWriterC1Ev',
    ))

  @overload(QIODevice, QByteArray)
  @overload(NoneType, QByteArray)
  def __init__(
      self,
      device: Optional[QIODevice],
      format: QByteArray,
  ) -> None:
    """
    Notes what was given, for Qt's 'QImageWriter::QImageWriter(QIODevice
    *device, const QByteArray &format)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qimagewriter.html#QImageWriter

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    format : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QImageWriter::QImageWriter(QIODevice *device, const QByteArray
    #      &format)
    self._noteCreation(QImageWriter, lambda: Rituals.call(
        'ritual_ZN12QImageWriterC1EP9QIODeviceRK10QByteArray',
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
    Notes what was given, for Qt's 'QImageWriter::QImageWriter(const QString
    &fileName, const QByteArray &format)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qimagewriter.html#QImageWriter

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    format : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.
    """
    #  QImageWriter::QImageWriter(const QString &fileName, const QByteArray
    #      &format)
    if format is None:
      from ..QtCore import QByteArray
      format = QByteArray()
    self._noteCreation(QImageWriter, lambda: Rituals.call(
        'ritual_ZN12QImageWriterC1ERK7QStringRK10QByteArray',
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

  @overload(QImage)
  def write(self, image: QImage) -> bool:
    """
    Calls Qt's 'bool QImageWriter::write(const QImage &image)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagewriter.html#write

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  bool QImageWriter::write(const QImage &image)
    return self.uglySide.call(
        'ritual_ZN12QImageWriter5writeERK6QImage', self._valueOf(image),
    )
