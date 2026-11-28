"""
QImageCapture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/qimagecapture.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QSize
  from ..QtGui import QImage
  from . import QMediaCaptureSession, QMediaMetaData, QVideoFrame
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']
  QMediaCaptureSession = WAIT['QMediaCaptureSession']
  QMediaMetaData = WAIT['QMediaMetaData']
  QSize = WAIT['QSize']
  QVideoFrame = WAIT['QVideoFrame']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QImageCapture(QObject):
  """
  The cute side of Qt's QImageCapture: a plain Python object standing in
  front of one C++ QImageCapture.

  It is built on the cute 'QObject', as Qt's QImageCapture is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QImageCapture that has a ritual and that Python can
  call so far, 33 names in all: 'metaObject', 'tr', 'isAvailable',
  'captureSession', 'error', 'errorString', 'isReadyForCapture',
  'fileFormat', 'setFileFormat', 'fileFormatName', 'fileFormatDescription',
  'resolution', 'setResolution', 'quality', 'setQuality', 'metaData',
  'setMetaData', 'addMetaData', 'captureToFile', 'capture', 'errorChanged',
  'errorOccurred', 'readyForCaptureChanged', 'metaDataChanged',
  'fileFormatChanged', 'qualityChanged', 'resolutionChanged', 'imageExposed',
  'imageCaptured', 'imageMetadataAvailable', 'imageAvailable', 'imageSaved',
  'setCaptureSession'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QImageCapture::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QImageCapture::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QImageCapture::~QImageCapture()': the destructor: Python never
    removes a C++ QImageCapture.
  - Qt's 'QList<FileFormat> QImageCapture::supportedFormats()': gives a type
    Python has no way to take yet.
  - Qt's 'class QPlatformImageCapture
    *QImageCapture::platformImageCapture()': gives 'class
    QPlatformImageCapture', which has no cute class yet.
  - Qt's 'QImageCapturePrivate *QImageCapture::d_func()': gives
    'QImageCapturePrivate', which has no cute class yet.
  - Qt's 'const QImageCapturePrivate *QImageCapture::d_func() const': gives
    'QImageCapturePrivate', which has no cute class yet.

  What has no ritual
  ------------------

  5 of the 47 functions Qt declares: 3 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QImageCapture is created at the first use, not by
    'QImageCapture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QImageCapture.
  - Qt tells when it has removed the C++ QImageCapture. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QImageCapture that has no cute function yet,
    'platformImageCapture', 'supportedFormats', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QImageCapture, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Error(CuteNum):
    """
    The enum 'QImageCapture::Error' of Qt, with the 6 names Qt gives in it.
    """

    NoError = Kee[int](0)
    NotReadyError = Kee[int](1)
    ResourceError = Kee[int](2)
    OutOfSpaceError = Kee[int](3)
    NotSupportedFeatureError = Kee[int](4)
    FormatError = Kee[int](5)

  class FileFormat(CuteNum):
    """
    The enum 'QImageCapture::FileFormat' of Qt, with the 6 names Qt gives in
    it.
    """

    UnspecifiedFormat = Kee[int](0)
    JPEG = Kee[int](1)
    PNG = Kee[int](2)
    WebP = Kee[int](3)
    Tiff = Kee[int](4)
    LastFileFormat = Kee[int](4)

  class Quality(CuteNum):
    """
    The enum 'QImageCapture::Quality' of Qt, with the 5 names Qt gives in it.
    """

    VeryLowQuality = Kee[int](0)
    LowQuality = Kee[int](1)
    NormalQuality = Kee[int](2)
    HighQuality = Kee[int](3)
    VeryHighQuality = Kee[int](4)

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
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QImageCapture::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagecapture.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QImageCapture::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QImageCapture2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(FileFormat)
  def fileFormatName(c: FileFormat) -> str:
    """
    Calls Qt's 'QString QImageCapture::fileFormatName(FileFormat c)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagecapture.html#fileFormatName

    Parameters
    ----------

    c : FileFormat
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QImageCapture::fileFormatName(FileFormat c)
    return Rituals.call(
        'ritual_ZN13QImageCapture14fileFormatNameENS_10FileFormatE', c.value,
    )

  @staticmethod
  @overload(FileFormat)
  def fileFormatDescription(c: FileFormat) -> str:
    """
    Calls Qt's 'QString QImageCapture::fileFormatDescription(FileFormat c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagecapture.html#fileFormatDescription

    Parameters
    ----------

    c : FileFormat
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QImageCapture::fileFormatDescription(FileFormat c)
    return Rituals.call(
        'ritual_ZN13QImageCapture21fileFormatDescriptionENS_10FileFormatE',
        c.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QImageCapture'

  #  A C++ QImageCapture Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QImageCapture'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QImageCapture::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagecapture.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QImageCapture::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QImageCapture10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isAvailable(self) -> bool:
    """
    Calls Qt's 'bool QImageCapture::isAvailable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagecapture.html#isAvailable
    """
    #  bool QImageCapture::isAvailable() const
    return self.uglySide.call('ritual_ZNK13QImageCapture11isAvailableEv')

  def captureSession(self) -> Optional[QMediaCaptureSession]:
    """
    Calls Qt's 'QMediaCaptureSession *QImageCapture::captureSession() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagecapture.html#captureSession

    Returns
    -------

    Optional[QMediaCaptureSession]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMediaCaptureSession *QImageCapture::captureSession() const
    address = self.uglySide.call(
        'ritual_ZNK13QImageCapture14captureSessionEv',
    )
    from . import QMediaCaptureSession
    return QMediaCaptureSession._cuteAt(address)

  def error(self) -> Error:
    """
    Calls Qt's 'Error QImageCapture::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagecapture.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QImageCapture::error() const
    return QImageCapture.Error(self.uglySide.call(
        'ritual_ZNK13QImageCapture5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QImageCapture::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagecapture.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QImageCapture::errorString() const
    return self.uglySide.call('ritual_ZNK13QImageCapture11errorStringEv')

  def isReadyForCapture(self) -> bool:
    """
    Calls Qt's 'bool QImageCapture::isReadyForCapture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagecapture.html#isReadyForCapture
    """
    #  bool QImageCapture::isReadyForCapture() const
    return self.uglySide.call(
        'ritual_ZNK13QImageCapture17isReadyForCaptureEv',
    )

  def fileFormat(self) -> FileFormat:
    """
    Calls Qt's 'FileFormat QImageCapture::fileFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagecapture.html#fileFormat

    Returns
    -------

    FileFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FileFormat(number)'
      gives.
    """
    #  FileFormat QImageCapture::fileFormat() const
    return QImageCapture.FileFormat(self.uglySide.call(
        'ritual_ZNK13QImageCapture10fileFormatEv',
    ))

  def resolution(self) -> QSize:
    """
    Calls Qt's 'QSize QImageCapture::resolution() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagecapture.html#resolution

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QImageCapture::resolution() const
    address = self.uglySide.call('ritual_ZNK13QImageCapture10resolutionEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def quality(self) -> Quality:
    """
    Calls Qt's 'Quality QImageCapture::quality() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagecapture.html#quality

    Returns
    -------

    Quality
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Quality(number)' gives.
    """
    #  Quality QImageCapture::quality() const
    return QImageCapture.Quality(self.uglySide.call(
        'ritual_ZNK13QImageCapture7qualityEv',
    ))

  def metaData(self) -> QMediaMetaData:
    """
    Calls Qt's 'QMediaMetaData QImageCapture::metaData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimagecapture.html#metaData

    Returns
    -------

    QMediaMetaData
      A new cute QMediaMetaData around the copy Qt gave back. Python owns it.
    """
    #  QMediaMetaData QImageCapture::metaData() const
    address = self.uglySide.call('ritual_ZNK13QImageCapture8metaDataEv')
    from . import QMediaMetaData
    return QMediaMetaData._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(FileFormat)
  def setFileFormat(self, format: FileFormat) -> None:
    """
    Calls Qt's 'void QImageCapture::setFileFormat(FileFormat format)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagecapture.html#setFileFormat

    Parameters
    ----------

    format : FileFormat
      Passed on as its number.
    """
    #  void QImageCapture::setFileFormat(FileFormat format)
    self.uglySide.call(
        'ritual_ZN13QImageCapture13setFileFormatENS_10FileFormatE',
        format.value,
    )

  @overload(QSize)
  def setResolution(self, a0: QSize) -> None:
    """
    Calls Qt's 'void QImageCapture::setResolution(const QSize &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagecapture.html#setResolution

    Parameters
    ----------

    a0 : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QImageCapture::setResolution(const QSize &a0)
    self.uglySide.call(
        'ritual_ZN13QImageCapture13setResolutionERK5QSize',
        self._valueOf(a0),
    )

  @overload(int, int)
  def setResolution(self, width: int, height: int) -> None:
    """
    Calls Qt's 'void QImageCapture::setResolution(int width, int height)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagecapture.html#setResolution

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void QImageCapture::setResolution(int width, int height)
    self.uglySide.call(
        'ritual_ZN13QImageCapture13setResolutionEii', width, height,
    )

  @overload(Quality)
  def setQuality(self, quality: Quality) -> None:
    """
    Calls Qt's 'void QImageCapture::setQuality(Quality quality)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagecapture.html#setQuality

    Parameters
    ----------

    quality : Quality
      Passed on as its number.
    """
    #  void QImageCapture::setQuality(Quality quality)
    self.uglySide.call(
        'ritual_ZN13QImageCapture10setQualityENS_7QualityE', quality.value,
    )

  @overload(QMediaMetaData)
  def setMetaData(self, metaData: QMediaMetaData) -> None:
    """
    Calls Qt's 'void QImageCapture::setMetaData(const QMediaMetaData
    &metaData)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagecapture.html#setMetaData

    Parameters
    ----------

    metaData : QMediaMetaData
      Passed on as a value: Qt reads the C++ QMediaMetaData, which stays
      Python's own.
    """
    #  void QImageCapture::setMetaData(const QMediaMetaData &metaData)
    self.uglySide.call(
        'ritual_ZN13QImageCapture11setMetaDataERK14QMediaMetaData',
        self._valueOf(metaData),
    )

  @overload(QMediaCaptureSession)
  @overload(NoneType)
  def setCaptureSession(
      self,
      session: Optional[QMediaCaptureSession],
  ) -> None:
    """
    Calls Qt's 'void QImageCapture::setCaptureSession(QMediaCaptureSession
    *session)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagecapture.html#setCaptureSession

    Parameters
    ----------

    session : Optional[QMediaCaptureSession]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QImageCapture::setCaptureSession(QMediaCaptureSession *session)
    self.uglySide.call(
        'ritual_ZN13QImageCapture17setCaptureSessionEP20QMediaCaptureSessio'
        'n',
        self._addressOf(session),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QImageCapture::QImageCapture(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qimagecapture.html#QImageCapture

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QImageCapture::QImageCapture(QObject *parent)
    self._noteCreation(QImageCapture, lambda: Rituals.call(
        'ritual_ZN13QImageCaptureC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(QMediaMetaData)
  def addMetaData(self, metaData: QMediaMetaData) -> None:
    """
    Calls Qt's 'void QImageCapture::addMetaData(const QMediaMetaData
    &metaData)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagecapture.html#addMetaData

    Parameters
    ----------

    metaData : QMediaMetaData
      Passed on as a value: Qt reads the C++ QMediaMetaData, which stays
      Python's own.
    """
    #  void QImageCapture::addMetaData(const QMediaMetaData &metaData)
    self.uglySide.call(
        'ritual_ZN13QImageCapture11addMetaDataERK14QMediaMetaData',
        self._valueOf(metaData),
    )

  @overload()
  @overload(str)
  def captureToFile(self, location: str = '') -> int:
    """
    Calls Qt's 'int QImageCapture::captureToFile(const QString &location)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagecapture.html#captureToFile

    Parameters
    ----------

    location : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  int QImageCapture::captureToFile(const QString &location)
    return self.uglySide.call(
        'ritual_ZN13QImageCapture13captureToFileERK7QString', location,
    )

  def capture(self) -> int:
    """
    Calls Qt's 'int QImageCapture::capture()'.

    Qt's own words: https://doc.qt.io/qt-6/qimagecapture.html#capture
    """
    #  int QImageCapture::capture()
    return self.uglySide.call('ritual_ZN13QImageCapture7captureEv')

  def errorChanged(self) -> None:
    """
    Calls Qt's 'void QImageCapture::errorChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qimagecapture.html#errorChanged
    """
    #  void QImageCapture::errorChanged()
    self.uglySide.call('ritual_ZN13QImageCapture12errorChangedEv')

  @overload(int, Error, str)
  def errorOccurred(self, id: int, error: Error, errorString: str) -> None:
    """
    Calls Qt's 'void QImageCapture::errorOccurred(int id,
    QImageCapture::Error error, const QString &errorString)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagecapture.html#errorOccurred

    Parameters
    ----------

    id : int
      Passed on as it is.

    error : Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QImageCapture::errorOccurred(int id, QImageCapture::Error error,
    #      const QString &errorString)
    self.uglySide.call(
        'ritual_ZN13QImageCapture13errorOccurredEiNS_5ErrorERK7QString',
        id, error.value, errorString,
    )

  @overload(bool)
  def readyForCaptureChanged(self, ready: bool) -> None:
    """
    Calls Qt's 'void QImageCapture::readyForCaptureChanged(bool ready)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagecapture.html#readyForCaptureChanged

    Parameters
    ----------

    ready : bool
      Passed on as it is.
    """
    #  void QImageCapture::readyForCaptureChanged(bool ready)
    self.uglySide.call(
        'ritual_ZN13QImageCapture22readyForCaptureChangedEb', ready,
    )

  def metaDataChanged(self) -> None:
    """
    Calls Qt's 'void QImageCapture::metaDataChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qimagecapture.html#metaDataChanged
    """
    #  void QImageCapture::metaDataChanged()
    self.uglySide.call('ritual_ZN13QImageCapture15metaDataChangedEv')

  def fileFormatChanged(self) -> None:
    """
    Calls Qt's 'void QImageCapture::fileFormatChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagecapture.html#fileFormatChanged
    """
    #  void QImageCapture::fileFormatChanged()
    self.uglySide.call('ritual_ZN13QImageCapture17fileFormatChangedEv')

  def qualityChanged(self) -> None:
    """
    Calls Qt's 'void QImageCapture::qualityChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qimagecapture.html#qualityChanged
    """
    #  void QImageCapture::qualityChanged()
    self.uglySide.call('ritual_ZN13QImageCapture14qualityChangedEv')

  def resolutionChanged(self) -> None:
    """
    Calls Qt's 'void QImageCapture::resolutionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagecapture.html#resolutionChanged
    """
    #  void QImageCapture::resolutionChanged()
    self.uglySide.call('ritual_ZN13QImageCapture17resolutionChangedEv')

  @overload(int)
  def imageExposed(self, id: int) -> None:
    """
    Calls Qt's 'void QImageCapture::imageExposed(int id)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagecapture.html#imageExposed

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void QImageCapture::imageExposed(int id)
    self.uglySide.call('ritual_ZN13QImageCapture12imageExposedEi', id)

  @overload(int, QImage)
  def imageCaptured(self, id: int, preview: QImage) -> None:
    """
    Calls Qt's 'void QImageCapture::imageCaptured(int id, const QImage
    &preview)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagecapture.html#imageCaptured

    Parameters
    ----------

    id : int
      Passed on as it is.

    preview : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QImageCapture::imageCaptured(int id, const QImage &preview)
    self.uglySide.call(
        'ritual_ZN13QImageCapture13imageCapturedEiRK6QImage',
        id, self._valueOf(preview),
    )

  @overload(int, QMediaMetaData)
  def imageMetadataAvailable(
      self,
      id: int,
      metaData: QMediaMetaData,
  ) -> None:
    """
    Calls Qt's 'void QImageCapture::imageMetadataAvailable(int id, const
    QMediaMetaData &metaData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimagecapture.html#imageMetadataAvailable

    Parameters
    ----------

    id : int
      Passed on as it is.

    metaData : QMediaMetaData
      Passed on as a value: Qt reads the C++ QMediaMetaData, which stays
      Python's own.
    """
    #  void QImageCapture::imageMetadataAvailable(int id, const
    #      QMediaMetaData &metaData)
    self.uglySide.call(
        'ritual_ZN13QImageCapture22imageMetadataAvailableEiRK14QMediaMetaDa'
        'ta',
        id, self._valueOf(metaData),
    )

  @overload(int, QVideoFrame)
  def imageAvailable(self, id: int, frame: QVideoFrame) -> None:
    """
    Calls Qt's 'void QImageCapture::imageAvailable(int id, const QVideoFrame
    &frame)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagecapture.html#imageAvailable

    Parameters
    ----------

    id : int
      Passed on as it is.

    frame : QVideoFrame
      Passed on as a value: Qt reads the C++ QVideoFrame, which stays
      Python's own.
    """
    #  void QImageCapture::imageAvailable(int id, const QVideoFrame &frame)
    self.uglySide.call(
        'ritual_ZN13QImageCapture14imageAvailableEiRK11QVideoFrame',
        id, self._valueOf(frame),
    )

  @overload(int, str)
  def imageSaved(self, id: int, fileName: str) -> None:
    """
    Calls Qt's 'void QImageCapture::imageSaved(int id, const QString
    &fileName)'.

    Qt's own words: https://doc.qt.io/qt-6/qimagecapture.html#imageSaved

    Parameters
    ----------

    id : int
      Passed on as it is.

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QImageCapture::imageSaved(int id, const QString &fileName)
    self.uglySide.call(
        'ritual_ZN13QImageCapture10imageSavedEiRK7QString', id, fileName,
    )

  @staticmethod
  def platformImageCapture(*__, **_) -> Never:
    """
    Qt's 'class QPlatformImageCapture
    *QImageCapture::platformImageCapture()': gives 'class
    QPlatformImageCapture', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QImageCapture.platformImageCapture' has no cute function yet. "
        "Qt's 'class QPlatformImageCapture "
        "*QImageCapture::platformImageCapture()': gives 'class "
        "QPlatformImageCapture', which has no cute class yet.")

  @staticmethod
  def supportedFormats(*__, **_) -> Never:
    """
    Qt's 'QList<FileFormat> QImageCapture::supportedFormats()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QImageCapture.supportedFormats' has no cute function yet. Qt's "
        "'QList<FileFormat> QImageCapture::supportedFormats()': gives a "
        "type Python has no way to take yet.")
