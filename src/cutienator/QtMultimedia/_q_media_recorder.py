"""
QMediaRecorder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/qmediarecorder.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QIODevice, QMetaObject, QSize, QUrl
  from . import QMediaCaptureSession, QMediaFormat, QMediaMetaData
  from . import QMediaRecorderPrivate, QPlatformMediaRecorder
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIODevice = WAIT['QIODevice']
  QMediaCaptureSession = WAIT['QMediaCaptureSession']
  QMediaFormat = WAIT['QMediaFormat']
  QMediaMetaData = WAIT['QMediaMetaData']
  QSize = WAIT['QSize']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMediaRecorder(QObject):
  """
  The cute side of Qt's QMediaRecorder: a plain Python object standing in
  front of one C++ QMediaRecorder.

  It is built on the cute 'QObject', as Qt's QMediaRecorder is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMediaRecorder that has a ritual and that Python can
  call so far, 59 names in all: 'metaObject', 'tr', 'isAvailable',
  'outputLocation', 'setOutputLocation', 'setOutputDevice', 'outputDevice',
  'actualLocation', 'recorderState', 'error', 'errorString', 'duration',
  'mediaFormat', 'setMediaFormat', 'encodingMode', 'setEncodingMode',
  'quality', 'setQuality', 'videoResolution', 'setVideoResolution',
  'videoFrameRate', 'setVideoFrameRate', 'videoBitRate', 'setVideoBitRate',
  'audioBitRate', 'setAudioBitRate', 'audioChannelCount',
  'setAudioChannelCount', 'audioSampleRate', 'setAudioSampleRate',
  'metaData', 'setMetaData', 'addMetaData', 'autoStop', 'setAutoStop',
  'captureSession', 'platformRecoder', 'record', 'pause', 'stop',
  'recorderStateChanged', 'durationChanged', 'actualLocationChanged',
  'encoderSettingsChanged', 'errorOccurred', 'errorChanged',
  'metaDataChanged', 'mediaFormatChanged', 'encodingModeChanged',
  'qualityChanged', 'videoResolutionChanged', 'videoFrameRateChanged',
  'videoBitRateChanged', 'audioBitRateChanged', 'audioChannelCountChanged',
  'audioSampleRateChanged', 'autoStopChanged', 'setCaptureSession', 'd_func'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QMediaRecorder::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QMediaRecorder::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QMediaRecorder::~QMediaRecorder()': the destructor: Python never
    removes a C++ QMediaRecorder.
  - Qt's 'const QMediaRecorderPrivate *QMediaRecorder::d_func() const': takes
    in Python what 'QMediaRecorderPrivate *QMediaRecorder::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 69 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QMediaRecorder is created at the first use, not by
    'QMediaRecorder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMediaRecorder.
  - Qt tells when it has removed the C++ QMediaRecorder. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QMediaRecorder, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class EncodingMode(CuteNum):
    """
    The enum 'QMediaRecorder::EncodingMode' of Qt, with the 4 names Qt gives
    in it.
    """

    ConstantQualityEncoding = Kee[int](0)
    ConstantBitRateEncoding = Kee[int](1)
    AverageBitRateEncoding = Kee[int](2)
    TwoPassEncoding = Kee[int](3)

  class Error(CuteNum):
    """
    The enum 'QMediaRecorder::Error' of Qt, with the 5 names Qt gives in it.
    """

    NoError = Kee[int](0)
    ResourceError = Kee[int](1)
    FormatError = Kee[int](2)
    OutOfSpaceError = Kee[int](3)
    LocationNotWritable = Kee[int](4)

  class Quality(CuteNum):
    """
    The enum 'QMediaRecorder::Quality' of Qt, with the 5 names Qt gives in
    it.
    """

    VeryLowQuality = Kee[int](0)
    LowQuality = Kee[int](1)
    NormalQuality = Kee[int](2)
    HighQuality = Kee[int](3)
    VeryHighQuality = Kee[int](4)

  class RecorderState(CuteNum):
    """
    The enum 'QMediaRecorder::RecorderState' of Qt, with the 3 names Qt gives
    in it.
    """

    StoppedState = Kee[int](0)
    RecordingState = Kee[int](1)
    PausedState = Kee[int](2)

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
    Calls Qt's 'QString QMediaRecorder::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorder.html#tr

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
    #  QString QMediaRecorder::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QMediaRecorder2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMediaRecorder'

  #  A C++ QMediaRecorder Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMediaRecorder'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QMediaRecorder::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorder.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QMediaRecorder::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QMediaRecorder10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isAvailable(self) -> bool:
    """
    Calls Qt's 'bool QMediaRecorder::isAvailable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorder.html#isAvailable
    """
    #  bool QMediaRecorder::isAvailable() const
    return self.uglySide.call('ritual_ZNK14QMediaRecorder11isAvailableEv')

  def outputLocation(self) -> QUrl:
    """
    Calls Qt's 'QUrl QMediaRecorder::outputLocation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorder.html#outputLocation

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QMediaRecorder::outputLocation() const
    address = self.uglySide.call(
        'ritual_ZNK14QMediaRecorder14outputLocationEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def outputDevice(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QMediaRecorder::outputDevice() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorder.html#outputDevice

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QMediaRecorder::outputDevice() const
    address = self.uglySide.call(
        'ritual_ZNK14QMediaRecorder12outputDeviceEv',
    )
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  def actualLocation(self) -> QUrl:
    """
    Calls Qt's 'QUrl QMediaRecorder::actualLocation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorder.html#actualLocation

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QMediaRecorder::actualLocation() const
    address = self.uglySide.call(
        'ritual_ZNK14QMediaRecorder14actualLocationEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def recorderState(self) -> RecorderState:
    """
    Calls Qt's 'RecorderState QMediaRecorder::recorderState() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorder.html#recorderState

    Returns
    -------

    RecorderState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RecorderState(number)'
      gives.
    """
    #  RecorderState QMediaRecorder::recorderState() const
    return QMediaRecorder.RecorderState(self.uglySide.call(
        'ritual_ZNK14QMediaRecorder13recorderStateEv',
    ))

  def error(self) -> Error:
    """
    Calls Qt's 'Error QMediaRecorder::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorder.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QMediaRecorder::error() const
    return QMediaRecorder.Error(self.uglySide.call(
        'ritual_ZNK14QMediaRecorder5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QMediaRecorder::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorder.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMediaRecorder::errorString() const
    return self.uglySide.call('ritual_ZNK14QMediaRecorder11errorStringEv')

  def duration(self) -> int:
    """
    Calls Qt's 'qint64 QMediaRecorder::duration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorder.html#duration
    """
    #  qint64 QMediaRecorder::duration() const
    return self.uglySide.call('ritual_ZNK14QMediaRecorder8durationEv')

  def mediaFormat(self) -> QMediaFormat:
    """
    Calls Qt's 'QMediaFormat QMediaRecorder::mediaFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorder.html#mediaFormat

    Returns
    -------

    QMediaFormat
      A new cute QMediaFormat around the copy Qt gave back. Python owns it.
    """
    #  QMediaFormat QMediaRecorder::mediaFormat() const
    address = self.uglySide.call('ritual_ZNK14QMediaRecorder11mediaFormatEv')
    from . import QMediaFormat
    return QMediaFormat._cuteOwning(address)

  def encodingMode(self) -> EncodingMode:
    """
    Calls Qt's 'EncodingMode QMediaRecorder::encodingMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorder.html#encodingMode

    Returns
    -------

    EncodingMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'EncodingMode(number)'
      gives.
    """
    #  EncodingMode QMediaRecorder::encodingMode() const
    return QMediaRecorder.EncodingMode(self.uglySide.call(
        'ritual_ZNK14QMediaRecorder12encodingModeEv',
    ))

  def quality(self) -> Quality:
    """
    Calls Qt's 'Quality QMediaRecorder::quality() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorder.html#quality

    Returns
    -------

    Quality
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Quality(number)' gives.
    """
    #  Quality QMediaRecorder::quality() const
    return QMediaRecorder.Quality(self.uglySide.call(
        'ritual_ZNK14QMediaRecorder7qualityEv',
    ))

  def videoResolution(self) -> QSize:
    """
    Calls Qt's 'QSize QMediaRecorder::videoResolution() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediarecorder.html#videoResolution

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QMediaRecorder::videoResolution() const
    address = self.uglySide.call(
        'ritual_ZNK14QMediaRecorder15videoResolutionEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def videoFrameRate(self) -> float:
    """
    Calls Qt's 'qreal QMediaRecorder::videoFrameRate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorder.html#videoFrameRate
    """
    #  qreal QMediaRecorder::videoFrameRate() const
    return self.uglySide.call('ritual_ZNK14QMediaRecorder14videoFrameRateEv')

  def videoBitRate(self) -> int:
    """
    Calls Qt's 'int QMediaRecorder::videoBitRate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorder.html#videoBitRate
    """
    #  int QMediaRecorder::videoBitRate() const
    return self.uglySide.call('ritual_ZNK14QMediaRecorder12videoBitRateEv')

  def audioBitRate(self) -> int:
    """
    Calls Qt's 'int QMediaRecorder::audioBitRate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorder.html#audioBitRate
    """
    #  int QMediaRecorder::audioBitRate() const
    return self.uglySide.call('ritual_ZNK14QMediaRecorder12audioBitRateEv')

  def audioChannelCount(self) -> int:
    """
    Calls Qt's 'int QMediaRecorder::audioChannelCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediarecorder.html#audioChannelCount
    """
    #  int QMediaRecorder::audioChannelCount() const
    return self.uglySide.call(
        'ritual_ZNK14QMediaRecorder17audioChannelCountEv',
    )

  def audioSampleRate(self) -> int:
    """
    Calls Qt's 'int QMediaRecorder::audioSampleRate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediarecorder.html#audioSampleRate
    """
    #  int QMediaRecorder::audioSampleRate() const
    return self.uglySide.call(
        'ritual_ZNK14QMediaRecorder15audioSampleRateEv',
    )

  def metaData(self) -> QMediaMetaData:
    """
    Calls Qt's 'QMediaMetaData QMediaRecorder::metaData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorder.html#metaData

    Returns
    -------

    QMediaMetaData
      A new cute QMediaMetaData around the copy Qt gave back. Python owns it.
    """
    #  QMediaMetaData QMediaRecorder::metaData() const
    address = self.uglySide.call('ritual_ZNK14QMediaRecorder8metaDataEv')
    from . import QMediaMetaData
    return QMediaMetaData._cuteOwning(address)

  def autoStop(self) -> bool:
    """
    Calls Qt's 'bool QMediaRecorder::autoStop() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorder.html#autoStop
    """
    #  bool QMediaRecorder::autoStop() const
    return self.uglySide.call('ritual_ZNK14QMediaRecorder8autoStopEv')

  def captureSession(self) -> Optional[QMediaCaptureSession]:
    """
    Calls Qt's 'QMediaCaptureSession *QMediaRecorder::captureSession()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorder.html#captureSession

    Returns
    -------

    Optional[QMediaCaptureSession]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMediaCaptureSession *QMediaRecorder::captureSession() const
    address = self.uglySide.call(
        'ritual_ZNK14QMediaRecorder14captureSessionEv',
    )
    from . import QMediaCaptureSession
    return QMediaCaptureSession._cuteAt(address)

  def platformRecoder(self) -> Optional[QPlatformMediaRecorder]:
    """
    Calls Qt's 'QPlatformMediaRecorder *QMediaRecorder::platformRecoder()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediarecorder.html#platformRecoder

    Returns
    -------

    Optional[QPlatformMediaRecorder]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMediaRecorder *QMediaRecorder::platformRecoder() const
    address = self.uglySide.call(
        'ritual_ZNK14QMediaRecorder15platformRecoderEv',
    )
    from . import QPlatformMediaRecorder
    return QPlatformMediaRecorder._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setOutputLocation(self, location: QUrl) -> None:
    """
    Calls Qt's 'void QMediaRecorder::setOutputLocation(const QUrl
    &location)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediarecorder.html#setOutputLocation

    Parameters
    ----------

    location : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QMediaRecorder::setOutputLocation(const QUrl &location)
    self.uglySide.call(
        'ritual_ZN14QMediaRecorder17setOutputLocationERK4QUrl',
        self._valueOf(location),
    )

  @overload(QIODevice)
  @overload(NoneType)
  def setOutputDevice(self, device: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void QMediaRecorder::setOutputDevice(QIODevice *device)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediarecorder.html#setOutputDevice

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMediaRecorder::setOutputDevice(QIODevice *device)
    self.uglySide.call(
        'ritual_ZN14QMediaRecorder15setOutputDeviceEP9QIODevice',
        self._addressOf(device),
    )

  @overload(QMediaFormat)
  def setMediaFormat(self, format: QMediaFormat) -> None:
    """
    Calls Qt's 'void QMediaRecorder::setMediaFormat(const QMediaFormat
    &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorder.html#setMediaFormat

    Parameters
    ----------

    format : QMediaFormat
      Passed on as a value: Qt reads the C++ QMediaFormat, which stays
      Python's own.
    """
    #  void QMediaRecorder::setMediaFormat(const QMediaFormat &format)
    self.uglySide.call(
        'ritual_ZN14QMediaRecorder14setMediaFormatERK12QMediaFormat',
        self._valueOf(format),
    )

  @overload(EncodingMode)
  def setEncodingMode(self, a0: EncodingMode) -> None:
    """
    Calls Qt's 'void QMediaRecorder::setEncodingMode(EncodingMode a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediarecorder.html#setEncodingMode

    Parameters
    ----------

    a0 : EncodingMode
      Passed on as its number.
    """
    #  void QMediaRecorder::setEncodingMode(EncodingMode a0)
    self.uglySide.call(
        'ritual_ZN14QMediaRecorder15setEncodingModeENS_12EncodingModeE',
        a0.value,
    )

  @overload(Quality)
  def setQuality(self, quality: Quality) -> None:
    """
    Calls Qt's 'void QMediaRecorder::setQuality(Quality quality)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorder.html#setQuality

    Parameters
    ----------

    quality : Quality
      Passed on as its number.
    """
    #  void QMediaRecorder::setQuality(Quality quality)
    self.uglySide.call(
        'ritual_ZN14QMediaRecorder10setQualityENS_7QualityE', quality.value,
    )

  @overload(QSize)
  def setVideoResolution(self, a0: QSize) -> None:
    """
    Calls Qt's 'void QMediaRecorder::setVideoResolution(const QSize &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediarecorder.html#setVideoResolution

    Parameters
    ----------

    a0 : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QMediaRecorder::setVideoResolution(const QSize &a0)
    self.uglySide.call(
        'ritual_ZN14QMediaRecorder18setVideoResolutionERK5QSize',
        self._valueOf(a0),
    )

  @overload(int, int)
  def setVideoResolution(self, width: int, height: int) -> None:
    """
    Calls Qt's 'void QMediaRecorder::setVideoResolution(int width, int
    height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediarecorder.html#setVideoResolution

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void QMediaRecorder::setVideoResolution(int width, int height)
    self.uglySide.call(
        'ritual_ZN14QMediaRecorder18setVideoResolutionEii', width, height,
    )

  @overload(float)
  def setVideoFrameRate(self, frameRate: float) -> None:
    """
    Calls Qt's 'void QMediaRecorder::setVideoFrameRate(qreal frameRate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediarecorder.html#setVideoFrameRate

    Parameters
    ----------

    frameRate : float
      Passed on as it is.
    """
    #  void QMediaRecorder::setVideoFrameRate(qreal frameRate)
    self.uglySide.call(
        'ritual_ZN14QMediaRecorder17setVideoFrameRateEd', frameRate,
    )

  @overload(int)
  def setVideoBitRate(self, bitRate: int) -> None:
    """
    Calls Qt's 'void QMediaRecorder::setVideoBitRate(int bitRate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediarecorder.html#setVideoBitRate

    Parameters
    ----------

    bitRate : int
      Passed on as it is.
    """
    #  void QMediaRecorder::setVideoBitRate(int bitRate)
    self.uglySide.call(
        'ritual_ZN14QMediaRecorder15setVideoBitRateEi', bitRate,
    )

  @overload(int)
  def setAudioBitRate(self, bitRate: int) -> None:
    """
    Calls Qt's 'void QMediaRecorder::setAudioBitRate(int bitRate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediarecorder.html#setAudioBitRate

    Parameters
    ----------

    bitRate : int
      Passed on as it is.
    """
    #  void QMediaRecorder::setAudioBitRate(int bitRate)
    self.uglySide.call(
        'ritual_ZN14QMediaRecorder15setAudioBitRateEi', bitRate,
    )

  @overload(int)
  def setAudioChannelCount(self, channels: int) -> None:
    """
    Calls Qt's 'void QMediaRecorder::setAudioChannelCount(int channels)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediarecorder.html#setAudioChannelCount

    Parameters
    ----------

    channels : int
      Passed on as it is.
    """
    #  void QMediaRecorder::setAudioChannelCount(int channels)
    self.uglySide.call(
        'ritual_ZN14QMediaRecorder20setAudioChannelCountEi', channels,
    )

  @overload(int)
  def setAudioSampleRate(self, sampleRate: int) -> None:
    """
    Calls Qt's 'void QMediaRecorder::setAudioSampleRate(int sampleRate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediarecorder.html#setAudioSampleRate

    Parameters
    ----------

    sampleRate : int
      Passed on as it is.
    """
    #  void QMediaRecorder::setAudioSampleRate(int sampleRate)
    self.uglySide.call(
        'ritual_ZN14QMediaRecorder18setAudioSampleRateEi', sampleRate,
    )

  @overload(QMediaMetaData)
  def setMetaData(self, metaData: QMediaMetaData) -> None:
    """
    Calls Qt's 'void QMediaRecorder::setMetaData(const QMediaMetaData
    &metaData)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorder.html#setMetaData

    Parameters
    ----------

    metaData : QMediaMetaData
      Passed on as a value: Qt reads the C++ QMediaMetaData, which stays
      Python's own.
    """
    #  void QMediaRecorder::setMetaData(const QMediaMetaData &metaData)
    self.uglySide.call(
        'ritual_ZN14QMediaRecorder11setMetaDataERK14QMediaMetaData',
        self._valueOf(metaData),
    )

  @overload(bool)
  def setAutoStop(self, autoStop: bool) -> None:
    """
    Calls Qt's 'void QMediaRecorder::setAutoStop(bool autoStop)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorder.html#setAutoStop

    Parameters
    ----------

    autoStop : bool
      Passed on as it is.
    """
    #  void QMediaRecorder::setAutoStop(bool autoStop)
    self.uglySide.call('ritual_ZN14QMediaRecorder11setAutoStopEb', autoStop)

  @overload(QMediaCaptureSession)
  @overload(NoneType)
  def setCaptureSession(
      self,
      session: Optional[QMediaCaptureSession],
  ) -> None:
    """
    Calls Qt's 'void QMediaRecorder::setCaptureSession(QMediaCaptureSession
    *session)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediarecorder.html#setCaptureSession

    Parameters
    ----------

    session : Optional[QMediaCaptureSession]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMediaRecorder::setCaptureSession(QMediaCaptureSession *session)
    self.uglySide.call(
        'ritual_ZN14QMediaRecorder17setCaptureSessionEP20QMediaCaptureSessi'
        'on',
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
    Notes what was given, for Qt's 'QMediaRecorder::QMediaRecorder(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorder.html#QMediaRecorder

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QMediaRecorder::QMediaRecorder(QObject *parent)
    self._noteCreation(QMediaRecorder, lambda: Rituals.call(
        'ritual_ZN14QMediaRecorderC1EP7QObject',
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
    Calls Qt's 'void QMediaRecorder::addMetaData(const QMediaMetaData
    &metaData)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorder.html#addMetaData

    Parameters
    ----------

    metaData : QMediaMetaData
      Passed on as a value: Qt reads the C++ QMediaMetaData, which stays
      Python's own.
    """
    #  void QMediaRecorder::addMetaData(const QMediaMetaData &metaData)
    self.uglySide.call(
        'ritual_ZN14QMediaRecorder11addMetaDataERK14QMediaMetaData',
        self._valueOf(metaData),
    )

  def record(self) -> None:
    """
    Calls Qt's 'void QMediaRecorder::record()'.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorder.html#record
    """
    #  void QMediaRecorder::record()
    self.uglySide.call('ritual_ZN14QMediaRecorder6recordEv')

  def pause(self) -> None:
    """
    Calls Qt's 'void QMediaRecorder::pause()'.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorder.html#pause
    """
    #  void QMediaRecorder::pause()
    self.uglySide.call('ritual_ZN14QMediaRecorder5pauseEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QMediaRecorder::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorder.html#stop
    """
    #  void QMediaRecorder::stop()
    self.uglySide.call('ritual_ZN14QMediaRecorder4stopEv')

  @overload(RecorderState)
  def recorderStateChanged(self, state: RecorderState) -> None:
    """
    Calls Qt's 'void
    QMediaRecorder::recorderStateChanged(QMediaRecorder::RecorderState
    state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediarecorder.html#recorderStateChanged

    Parameters
    ----------

    state : RecorderState
      Passed on as its number.
    """
    #  void
    #      QMediaRecorder::recorderStateChanged(QMediaRecorder::RecorderState
    #      state)
    self.uglySide.call(
        'ritual_ZN14QMediaRecorder20recorderStateChangedENS_13RecorderState'
        'E',
        state.value,
    )

  @overload(int)
  def durationChanged(self, duration: int) -> None:
    """
    Calls Qt's 'void QMediaRecorder::durationChanged(qint64 duration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediarecorder.html#durationChanged

    Parameters
    ----------

    duration : int
      Passed on as it is.
    """
    #  void QMediaRecorder::durationChanged(qint64 duration)
    self.uglySide.call(
        'ritual_ZN14QMediaRecorder15durationChangedEx', duration,
    )

  @overload(QUrl)
  def actualLocationChanged(self, location: QUrl) -> None:
    """
    Calls Qt's 'void QMediaRecorder::actualLocationChanged(const QUrl
    &location)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediarecorder.html#actualLocationChanged

    Parameters
    ----------

    location : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QMediaRecorder::actualLocationChanged(const QUrl &location)
    self.uglySide.call(
        'ritual_ZN14QMediaRecorder21actualLocationChangedERK4QUrl',
        self._valueOf(location),
    )

  def encoderSettingsChanged(self) -> None:
    """
    Calls Qt's 'void QMediaRecorder::encoderSettingsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediarecorder.html#encoderSettingsChanged
    """
    #  void QMediaRecorder::encoderSettingsChanged()
    self.uglySide.call('ritual_ZN14QMediaRecorder22encoderSettingsChangedEv')

  @overload(Error, str)
  def errorOccurred(self, error: Error, errorString: str) -> None:
    """
    Calls Qt's 'void QMediaRecorder::errorOccurred(QMediaRecorder::Error
    error, const QString &errorString)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorder.html#errorOccurred

    Parameters
    ----------

    error : Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMediaRecorder::errorOccurred(QMediaRecorder::Error error, const
    #      QString &errorString)
    self.uglySide.call(
        'ritual_ZN14QMediaRecorder13errorOccurredENS_5ErrorERK7QString',
        error.value, errorString,
    )

  def errorChanged(self) -> None:
    """
    Calls Qt's 'void QMediaRecorder::errorChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorder.html#errorChanged
    """
    #  void QMediaRecorder::errorChanged()
    self.uglySide.call('ritual_ZN14QMediaRecorder12errorChangedEv')

  def metaDataChanged(self) -> None:
    """
    Calls Qt's 'void QMediaRecorder::metaDataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediarecorder.html#metaDataChanged
    """
    #  void QMediaRecorder::metaDataChanged()
    self.uglySide.call('ritual_ZN14QMediaRecorder15metaDataChangedEv')

  def mediaFormatChanged(self) -> None:
    """
    Calls Qt's 'void QMediaRecorder::mediaFormatChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediarecorder.html#mediaFormatChanged
    """
    #  void QMediaRecorder::mediaFormatChanged()
    self.uglySide.call('ritual_ZN14QMediaRecorder18mediaFormatChangedEv')

  def encodingModeChanged(self) -> None:
    """
    Calls Qt's 'void QMediaRecorder::encodingModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediarecorder.html#encodingModeChanged
    """
    #  void QMediaRecorder::encodingModeChanged()
    self.uglySide.call('ritual_ZN14QMediaRecorder19encodingModeChangedEv')

  def qualityChanged(self) -> None:
    """
    Calls Qt's 'void QMediaRecorder::qualityChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorder.html#qualityChanged
    """
    #  void QMediaRecorder::qualityChanged()
    self.uglySide.call('ritual_ZN14QMediaRecorder14qualityChangedEv')

  def videoResolutionChanged(self) -> None:
    """
    Calls Qt's 'void QMediaRecorder::videoResolutionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediarecorder.html#videoResolutionChanged
    """
    #  void QMediaRecorder::videoResolutionChanged()
    self.uglySide.call('ritual_ZN14QMediaRecorder22videoResolutionChangedEv')

  def videoFrameRateChanged(self) -> None:
    """
    Calls Qt's 'void QMediaRecorder::videoFrameRateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediarecorder.html#videoFrameRateChanged
    """
    #  void QMediaRecorder::videoFrameRateChanged()
    self.uglySide.call('ritual_ZN14QMediaRecorder21videoFrameRateChangedEv')

  def videoBitRateChanged(self) -> None:
    """
    Calls Qt's 'void QMediaRecorder::videoBitRateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediarecorder.html#videoBitRateChanged
    """
    #  void QMediaRecorder::videoBitRateChanged()
    self.uglySide.call('ritual_ZN14QMediaRecorder19videoBitRateChangedEv')

  def audioBitRateChanged(self) -> None:
    """
    Calls Qt's 'void QMediaRecorder::audioBitRateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediarecorder.html#audioBitRateChanged
    """
    #  void QMediaRecorder::audioBitRateChanged()
    self.uglySide.call('ritual_ZN14QMediaRecorder19audioBitRateChangedEv')

  def audioChannelCountChanged(self) -> None:
    """
    Calls Qt's 'void QMediaRecorder::audioChannelCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediarecorder.html#audioChannelCountChanged
    """
    #  void QMediaRecorder::audioChannelCountChanged()
    self.uglySide.call(
        'ritual_ZN14QMediaRecorder24audioChannelCountChangedEv',
    )

  def audioSampleRateChanged(self) -> None:
    """
    Calls Qt's 'void QMediaRecorder::audioSampleRateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediarecorder.html#audioSampleRateChanged
    """
    #  void QMediaRecorder::audioSampleRateChanged()
    self.uglySide.call('ritual_ZN14QMediaRecorder22audioSampleRateChangedEv')

  def autoStopChanged(self) -> None:
    """
    Calls Qt's 'void QMediaRecorder::autoStopChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediarecorder.html#autoStopChanged
    """
    #  void QMediaRecorder::autoStopChanged()
    self.uglySide.call('ritual_ZN14QMediaRecorder15autoStopChangedEv')

  def d_func(self) -> Optional[QMediaRecorderPrivate]:
    """
    Calls Qt's 'QMediaRecorderPrivate *QMediaRecorder::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qmediarecorder.html#d_func

    Returns
    -------

    Optional[QMediaRecorderPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMediaRecorderPrivate *QMediaRecorder::d_func()
    address = self.uglySide.call('ritual_ZN14QMediaRecorder6d_funcEv')
    from . import QMediaRecorderPrivate
    return QMediaRecorderPrivate._cuteAt(address)
