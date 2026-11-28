"""
QMediaPlayer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/qmediaplayer.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QIODevice, QMetaObject, QUrl
  from . import QAudioBufferOutput, QAudioOutput, QMediaMetaData
  from . import QMediaPlayerPrivate, QMediaTimeRange, QPlaybackOptions
  from . import QVideoSink
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioBufferOutput = WAIT['QAudioBufferOutput']
  QAudioOutput = WAIT['QAudioOutput']
  QIODevice = WAIT['QIODevice']
  QPlaybackOptions = WAIT['QPlaybackOptions']
  QUrl = WAIT['QUrl']
  QVideoSink = WAIT['QVideoSink']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMediaPlayer(QObject):
  """
  The cute side of Qt's QMediaPlayer: a plain Python object standing in front
  of one C++ QMediaPlayer.

  It is built on the cute 'QObject', as Qt's QMediaPlayer is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMediaPlayer that has a ritual and that Python can
  call so far, 74 names in all: 'metaObject', 'tr', 'audioTracks',
  'videoTracks', 'subtitleTracks', 'activeAudioTrack', 'activeVideoTrack',
  'activeSubtitleTrack', 'setActiveAudioTrack', 'setActiveVideoTrack',
  'setActiveSubtitleTrack', 'setAudioBufferOutput', 'audioBufferOutput',
  'setAudioOutput', 'audioOutput', 'setVideoOutput', 'videoOutput',
  'setVideoSink', 'videoSink', 'source', 'sourceDevice', 'playbackState',
  'mediaStatus', 'duration', 'position', 'hasAudio', 'hasVideo',
  'bufferProgress', 'bufferedTimeRange', 'isSeekable', 'playbackRate',
  'isPlaying', 'loops', 'setLoops', 'error', 'errorString', 'isAvailable',
  'metaData', 'pitchCompensationAvailability', 'pitchCompensation',
  'playbackOptions', 'play', 'pause', 'stop', 'setPosition',
  'setPlaybackRate', 'setSource', 'setSourceDevice', 'setPitchCompensation',
  'setPlaybackOptions', 'resetPlaybackOptions', 'sourceChanged',
  'playbackStateChanged', 'mediaStatusChanged', 'durationChanged',
  'positionChanged', 'hasAudioChanged', 'hasVideoChanged',
  'bufferProgressChanged', 'seekableChanged', 'playingChanged',
  'playbackRateChanged', 'loopsChanged', 'metaDataChanged',
  'videoOutputChanged', 'audioOutputChanged', 'audioBufferOutputChanged',
  'tracksChanged', 'activeTracksChanged', 'errorChanged', 'errorOccurred',
  'pitchCompensationChanged', 'playbackOptionsChanged', 'd_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QMediaPlayer::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QMediaPlayer::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QMediaPlayer::~QMediaPlayer()': the destructor: Python never
    removes a C++ QMediaPlayer.
  - Qt's 'const QMediaPlayerPrivate *QMediaPlayer::d_func() const': takes in
    Python what 'QMediaPlayerPrivate *QMediaPlayer::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 83 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QMediaPlayer is created at the first use, not by
    'QMediaPlayer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMediaPlayer.
  - Qt tells when it has removed the C++ QMediaPlayer. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QMediaPlayer, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Error(CuteNum):
    """
    The enum 'QMediaPlayer::Error' of Qt, with the 5 names Qt gives in it.
    """

    NoError = Kee[int](0)
    ResourceError = Kee[int](1)
    FormatError = Kee[int](2)
    NetworkError = Kee[int](3)
    AccessDeniedError = Kee[int](4)

  class Loops(CuteNum):
    """
    The enum 'QMediaPlayer::Loops' of Qt, with the 2 names Qt gives in it.
    """

    Infinite = Kee[int](-1)
    Once = Kee[int](1)

  class MediaStatus(CuteNum):
    """
    The enum 'QMediaPlayer::MediaStatus' of Qt, with the 8 names Qt gives in
    it.
    """

    NoMedia = Kee[int](0)
    LoadingMedia = Kee[int](1)
    LoadedMedia = Kee[int](2)
    StalledMedia = Kee[int](3)
    BufferingMedia = Kee[int](4)
    BufferedMedia = Kee[int](5)
    EndOfMedia = Kee[int](6)
    InvalidMedia = Kee[int](7)

  class PitchCompensationAvailability(CuteNum, scoped=True):
    """
    The enum 'QMediaPlayer::PitchCompensationAvailability' of Qt, with the 3
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    AlwaysOn = Kee[int](0)
    Available = Kee[int](1)
    Unavailable = Kee[int](2)

  class PlaybackState(CuteNum):
    """
    The enum 'QMediaPlayer::PlaybackState' of Qt, with the 3 names Qt gives
    in it.
    """

    StoppedState = Kee[int](0)
    PlayingState = Kee[int](1)
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
    Calls Qt's 'QString QMediaPlayer::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#tr

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
    #  QString QMediaPlayer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QMediaPlayer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMediaPlayer'

  #  A C++ QMediaPlayer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMediaPlayer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QMediaPlayer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QMediaPlayer::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QMediaPlayer10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def audioTracks(self) -> QList[QMediaMetaData]:
    """
    Calls Qt's 'QList<QMediaMetaData> QMediaPlayer::audioTracks() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#audioTracks

    Returns
    -------

    QList[QMediaMetaData]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QMediaMetaData> QMediaPlayer::audioTracks() const
    address = self.uglySide.call('ritual_ZNK12QMediaPlayer11audioTracksEv')
    from . import QMediaMetaData
    return QList[QMediaMetaData]._cuteOwning(address)

  def videoTracks(self) -> QList[QMediaMetaData]:
    """
    Calls Qt's 'QList<QMediaMetaData> QMediaPlayer::videoTracks() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#videoTracks

    Returns
    -------

    QList[QMediaMetaData]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QMediaMetaData> QMediaPlayer::videoTracks() const
    address = self.uglySide.call('ritual_ZNK12QMediaPlayer11videoTracksEv')
    from . import QMediaMetaData
    return QList[QMediaMetaData]._cuteOwning(address)

  def subtitleTracks(self) -> QList[QMediaMetaData]:
    """
    Calls Qt's 'QList<QMediaMetaData> QMediaPlayer::subtitleTracks() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#subtitleTracks

    Returns
    -------

    QList[QMediaMetaData]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QMediaMetaData> QMediaPlayer::subtitleTracks() const
    address = self.uglySide.call(
        'ritual_ZNK12QMediaPlayer14subtitleTracksEv',
    )
    from . import QMediaMetaData
    return QList[QMediaMetaData]._cuteOwning(address)

  def activeAudioTrack(self) -> int:
    """
    Calls Qt's 'int QMediaPlayer::activeAudioTrack() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#activeAudioTrack
    """
    #  int QMediaPlayer::activeAudioTrack() const
    return self.uglySide.call('ritual_ZNK12QMediaPlayer16activeAudioTrackEv')

  def activeVideoTrack(self) -> int:
    """
    Calls Qt's 'int QMediaPlayer::activeVideoTrack() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#activeVideoTrack
    """
    #  int QMediaPlayer::activeVideoTrack() const
    return self.uglySide.call('ritual_ZNK12QMediaPlayer16activeVideoTrackEv')

  def activeSubtitleTrack(self) -> int:
    """
    Calls Qt's 'int QMediaPlayer::activeSubtitleTrack() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaplayer.html#activeSubtitleTrack
    """
    #  int QMediaPlayer::activeSubtitleTrack() const
    return self.uglySide.call(
        'ritual_ZNK12QMediaPlayer19activeSubtitleTrackEv',
    )

  def audioBufferOutput(self) -> Optional[QAudioBufferOutput]:
    """
    Calls Qt's 'QAudioBufferOutput *QMediaPlayer::audioBufferOutput() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaplayer.html#audioBufferOutput

    Returns
    -------

    Optional[QAudioBufferOutput]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAudioBufferOutput *QMediaPlayer::audioBufferOutput() const
    address = self.uglySide.call(
        'ritual_ZNK12QMediaPlayer17audioBufferOutputEv',
    )
    from . import QAudioBufferOutput
    return QAudioBufferOutput._cuteAt(address)

  def audioOutput(self) -> Optional[QAudioOutput]:
    """
    Calls Qt's 'QAudioOutput *QMediaPlayer::audioOutput() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#audioOutput

    Returns
    -------

    Optional[QAudioOutput]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAudioOutput *QMediaPlayer::audioOutput() const
    address = self.uglySide.call('ritual_ZNK12QMediaPlayer11audioOutputEv')
    from . import QAudioOutput
    return QAudioOutput._cuteAt(address)

  def videoOutput(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QMediaPlayer::videoOutput() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#videoOutput

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QMediaPlayer::videoOutput() const
    address = self.uglySide.call('ritual_ZNK12QMediaPlayer11videoOutputEv')
    return QObject._cuteAt(address)

  def videoSink(self) -> Optional[QVideoSink]:
    """
    Calls Qt's 'QVideoSink *QMediaPlayer::videoSink() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#videoSink

    Returns
    -------

    Optional[QVideoSink]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVideoSink *QMediaPlayer::videoSink() const
    address = self.uglySide.call('ritual_ZNK12QMediaPlayer9videoSinkEv')
    from . import QVideoSink
    return QVideoSink._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QMediaPlayer::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QMediaPlayer::source() const
    address = self.uglySide.call('ritual_ZNK12QMediaPlayer6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def sourceDevice(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'const QIODevice *QMediaPlayer::sourceDevice() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#sourceDevice

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QIODevice *QMediaPlayer::sourceDevice() const
    address = self.uglySide.call('ritual_ZNK12QMediaPlayer12sourceDeviceEv')
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  def playbackState(self) -> PlaybackState:
    """
    Calls Qt's 'PlaybackState QMediaPlayer::playbackState() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#playbackState

    Returns
    -------

    PlaybackState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PlaybackState(number)'
      gives.
    """
    #  PlaybackState QMediaPlayer::playbackState() const
    return QMediaPlayer.PlaybackState(self.uglySide.call(
        'ritual_ZNK12QMediaPlayer13playbackStateEv',
    ))

  def mediaStatus(self) -> MediaStatus:
    """
    Calls Qt's 'MediaStatus QMediaPlayer::mediaStatus() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#mediaStatus

    Returns
    -------

    MediaStatus
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'MediaStatus(number)'
      gives.
    """
    #  MediaStatus QMediaPlayer::mediaStatus() const
    return QMediaPlayer.MediaStatus(self.uglySide.call(
        'ritual_ZNK12QMediaPlayer11mediaStatusEv',
    ))

  def duration(self) -> int:
    """
    Calls Qt's 'qint64 QMediaPlayer::duration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#duration
    """
    #  qint64 QMediaPlayer::duration() const
    return self.uglySide.call('ritual_ZNK12QMediaPlayer8durationEv')

  def position(self) -> int:
    """
    Calls Qt's 'qint64 QMediaPlayer::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#position
    """
    #  qint64 QMediaPlayer::position() const
    return self.uglySide.call('ritual_ZNK12QMediaPlayer8positionEv')

  def hasAudio(self) -> bool:
    """
    Calls Qt's 'bool QMediaPlayer::hasAudio() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#hasAudio
    """
    #  bool QMediaPlayer::hasAudio() const
    return self.uglySide.call('ritual_ZNK12QMediaPlayer8hasAudioEv')

  def hasVideo(self) -> bool:
    """
    Calls Qt's 'bool QMediaPlayer::hasVideo() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#hasVideo
    """
    #  bool QMediaPlayer::hasVideo() const
    return self.uglySide.call('ritual_ZNK12QMediaPlayer8hasVideoEv')

  def bufferProgress(self) -> float:
    """
    Calls Qt's 'float QMediaPlayer::bufferProgress() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#bufferProgress
    """
    #  float QMediaPlayer::bufferProgress() const
    return self.uglySide.call('ritual_ZNK12QMediaPlayer14bufferProgressEv')

  def bufferedTimeRange(self) -> QMediaTimeRange:
    """
    Calls Qt's 'QMediaTimeRange QMediaPlayer::bufferedTimeRange() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaplayer.html#bufferedTimeRange

    Returns
    -------

    QMediaTimeRange
      A new cute QMediaTimeRange around the copy Qt gave back. Python owns
      it.
    """
    #  QMediaTimeRange QMediaPlayer::bufferedTimeRange() const
    address = self.uglySide.call(
        'ritual_ZNK12QMediaPlayer17bufferedTimeRangeEv',
    )
    from . import QMediaTimeRange
    return QMediaTimeRange._cuteOwning(address)

  def isSeekable(self) -> bool:
    """
    Calls Qt's 'bool QMediaPlayer::isSeekable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#isSeekable
    """
    #  bool QMediaPlayer::isSeekable() const
    return self.uglySide.call('ritual_ZNK12QMediaPlayer10isSeekableEv')

  def playbackRate(self) -> float:
    """
    Calls Qt's 'qreal QMediaPlayer::playbackRate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#playbackRate
    """
    #  qreal QMediaPlayer::playbackRate() const
    return self.uglySide.call('ritual_ZNK12QMediaPlayer12playbackRateEv')

  def isPlaying(self) -> bool:
    """
    Calls Qt's 'bool QMediaPlayer::isPlaying() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#isPlaying
    """
    #  bool QMediaPlayer::isPlaying() const
    return self.uglySide.call('ritual_ZNK12QMediaPlayer9isPlayingEv')

  def loops(self) -> int:
    """
    Calls Qt's 'int QMediaPlayer::loops() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#loops
    """
    #  int QMediaPlayer::loops() const
    return self.uglySide.call('ritual_ZNK12QMediaPlayer5loopsEv')

  def error(self) -> Error:
    """
    Calls Qt's 'Error QMediaPlayer::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QMediaPlayer::error() const
    return QMediaPlayer.Error(self.uglySide.call(
        'ritual_ZNK12QMediaPlayer5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QMediaPlayer::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMediaPlayer::errorString() const
    return self.uglySide.call('ritual_ZNK12QMediaPlayer11errorStringEv')

  def isAvailable(self) -> bool:
    """
    Calls Qt's 'bool QMediaPlayer::isAvailable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#isAvailable
    """
    #  bool QMediaPlayer::isAvailable() const
    return self.uglySide.call('ritual_ZNK12QMediaPlayer11isAvailableEv')

  def metaData(self) -> QMediaMetaData:
    """
    Calls Qt's 'QMediaMetaData QMediaPlayer::metaData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#metaData

    Returns
    -------

    QMediaMetaData
      A new cute QMediaMetaData around the copy Qt gave back. Python owns it.
    """
    #  QMediaMetaData QMediaPlayer::metaData() const
    address = self.uglySide.call('ritual_ZNK12QMediaPlayer8metaDataEv')
    from . import QMediaMetaData
    return QMediaMetaData._cuteOwning(address)

  def pitchCompensationAvailability(self) -> PitchCompensationAvailability:
    """
    Calls Qt's 'PitchCompensationAvailability
    QMediaPlayer::pitchCompensationAvailability() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaplayer.html#pitchCompensationAvailability

    Returns
    -------

    PitchCompensationAvailability
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'PitchCompensationAvailability(number)' gives.
    """
    #  PitchCompensationAvailability
    #      QMediaPlayer::pitchCompensationAvailability() const
    return QMediaPlayer.PitchCompensationAvailability(self.uglySide.call(
        'ritual_ZNK12QMediaPlayer29pitchCompensationAvailabilityEv',
    ))

  def pitchCompensation(self) -> bool:
    """
    Calls Qt's 'bool QMediaPlayer::pitchCompensation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaplayer.html#pitchCompensation
    """
    #  bool QMediaPlayer::pitchCompensation() const
    return self.uglySide.call(
        'ritual_ZNK12QMediaPlayer17pitchCompensationEv',
    )

  def playbackOptions(self) -> QPlaybackOptions:
    """
    Calls Qt's 'QPlaybackOptions QMediaPlayer::playbackOptions() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#playbackOptions

    Returns
    -------

    QPlaybackOptions
      A new cute QPlaybackOptions around the copy Qt gave back. Python owns
      it.
    """
    #  QPlaybackOptions QMediaPlayer::playbackOptions() const
    address = self.uglySide.call(
        'ritual_ZNK12QMediaPlayer15playbackOptionsEv',
    )
    from . import QPlaybackOptions
    return QPlaybackOptions._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setActiveAudioTrack(self, index: int) -> None:
    """
    Calls Qt's 'void QMediaPlayer::setActiveAudioTrack(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaplayer.html#setActiveAudioTrack

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QMediaPlayer::setActiveAudioTrack(int index)
    self.uglySide.call(
        'ritual_ZN12QMediaPlayer19setActiveAudioTrackEi', index,
    )

  @overload(int)
  def setActiveVideoTrack(self, index: int) -> None:
    """
    Calls Qt's 'void QMediaPlayer::setActiveVideoTrack(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaplayer.html#setActiveVideoTrack

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QMediaPlayer::setActiveVideoTrack(int index)
    self.uglySide.call(
        'ritual_ZN12QMediaPlayer19setActiveVideoTrackEi', index,
    )

  @overload(int)
  def setActiveSubtitleTrack(self, index: int) -> None:
    """
    Calls Qt's 'void QMediaPlayer::setActiveSubtitleTrack(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaplayer.html#setActiveSubtitleTrack

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QMediaPlayer::setActiveSubtitleTrack(int index)
    self.uglySide.call(
        'ritual_ZN12QMediaPlayer22setActiveSubtitleTrackEi', index,
    )

  @overload(QAudioBufferOutput)
  @overload(NoneType)
  def setAudioBufferOutput(
      self,
      output: Optional[QAudioBufferOutput],
  ) -> None:
    """
    Calls Qt's 'void QMediaPlayer::setAudioBufferOutput(QAudioBufferOutput
    *output)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaplayer.html#setAudioBufferOutput

    Parameters
    ----------

    output : Optional[QAudioBufferOutput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMediaPlayer::setAudioBufferOutput(QAudioBufferOutput *output)
    self.uglySide.call(
        'ritual_ZN12QMediaPlayer20setAudioBufferOutputEP18QAudioBufferOutpu'
        't',
        self._addressOf(output),
    )

  @overload(QAudioOutput)
  @overload(NoneType)
  def setAudioOutput(self, output: Optional[QAudioOutput]) -> None:
    """
    Calls Qt's 'void QMediaPlayer::setAudioOutput(QAudioOutput *output)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#setAudioOutput

    Parameters
    ----------

    output : Optional[QAudioOutput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMediaPlayer::setAudioOutput(QAudioOutput *output)
    self.uglySide.call(
        'ritual_ZN12QMediaPlayer14setAudioOutputEP12QAudioOutput',
        self._addressOf(output),
    )

  @overload(QObject)
  @overload(NoneType)
  def setVideoOutput(self, a0: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QMediaPlayer::setVideoOutput(QObject *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#setVideoOutput

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMediaPlayer::setVideoOutput(QObject *a0)
    self.uglySide.call(
        'ritual_ZN12QMediaPlayer14setVideoOutputEP7QObject',
        self._addressOf(a0, 'QObject'),
    )

  @overload(QVideoSink)
  @overload(NoneType)
  def setVideoSink(self, sink: Optional[QVideoSink]) -> None:
    """
    Calls Qt's 'void QMediaPlayer::setVideoSink(QVideoSink *sink)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#setVideoSink

    Parameters
    ----------

    sink : Optional[QVideoSink]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMediaPlayer::setVideoSink(QVideoSink *sink)
    self.uglySide.call(
        'ritual_ZN12QMediaPlayer12setVideoSinkEP10QVideoSink',
        self._addressOf(sink),
    )

  @overload(int)
  def setLoops(self, loops: int) -> None:
    """
    Calls Qt's 'void QMediaPlayer::setLoops(int loops)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#setLoops

    Parameters
    ----------

    loops : int
      Passed on as it is.
    """
    #  void QMediaPlayer::setLoops(int loops)
    self.uglySide.call('ritual_ZN12QMediaPlayer8setLoopsEi', loops)

  @overload(int)
  def setPosition(self, position: int) -> None:
    """
    Calls Qt's 'void QMediaPlayer::setPosition(qint64 position)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#setPosition

    Parameters
    ----------

    position : int
      Passed on as it is.
    """
    #  void QMediaPlayer::setPosition(qint64 position)
    self.uglySide.call('ritual_ZN12QMediaPlayer11setPositionEx', position)

  @overload(float)
  def setPlaybackRate(self, rate: float) -> None:
    """
    Calls Qt's 'void QMediaPlayer::setPlaybackRate(qreal rate)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#setPlaybackRate

    Parameters
    ----------

    rate : float
      Passed on as it is.
    """
    #  void QMediaPlayer::setPlaybackRate(qreal rate)
    self.uglySide.call('ritual_ZN12QMediaPlayer15setPlaybackRateEd', rate)

  @overload(QUrl)
  def setSource(self, source: QUrl) -> None:
    """
    Calls Qt's 'void QMediaPlayer::setSource(const QUrl &source)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#setSource

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QMediaPlayer::setSource(const QUrl &source)
    self.uglySide.call(
        'ritual_ZN12QMediaPlayer9setSourceERK4QUrl', self._valueOf(source),
    )

  @overload(QIODevice)
  @overload(NoneType)
  @overload(QIODevice, QUrl)
  @overload(NoneType, QUrl)
  def setSourceDevice(
      self,
      device: Optional[QIODevice],
      sourceUrl: Optional[QUrl] = None,
  ) -> None:
    """
    Calls Qt's 'void QMediaPlayer::setSourceDevice(QIODevice *device, const
    QUrl &sourceUrl)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#setSourceDevice

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    sourceUrl : Optional[QUrl]
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
      May be left out, as in Qt: a new 'QUrl()' is then passed on.
    """
    #  void QMediaPlayer::setSourceDevice(QIODevice *device, const QUrl
    #      &sourceUrl)
    if sourceUrl is None:
      from ..QtCore import QUrl
      sourceUrl = QUrl()
    self.uglySide.call(
        'ritual_ZN12QMediaPlayer15setSourceDeviceEP9QIODeviceRK4QUrl',
        self._addressOf(device), self._valueOf(sourceUrl),
    )

  @overload(bool)
  def setPitchCompensation(self, a0: bool) -> None:
    """
    Calls Qt's 'void QMediaPlayer::setPitchCompensation(bool a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaplayer.html#setPitchCompensation

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QMediaPlayer::setPitchCompensation(bool a0) const
    self.uglySide.call(
        'ritual_ZNK12QMediaPlayer20setPitchCompensationEb', a0,
    )

  @overload(QPlaybackOptions)
  def setPlaybackOptions(self, options: QPlaybackOptions) -> None:
    """
    Calls Qt's 'void QMediaPlayer::setPlaybackOptions(const QPlaybackOptions
    &options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaplayer.html#setPlaybackOptions

    Parameters
    ----------

    options : QPlaybackOptions
      Passed on as a value: Qt reads the C++ QPlaybackOptions, which stays
      Python's own.
    """
    #  void QMediaPlayer::setPlaybackOptions(const QPlaybackOptions &options)
    self.uglySide.call(
        'ritual_ZN12QMediaPlayer18setPlaybackOptionsERK16QPlaybackOptions',
        self._valueOf(options),
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
    Notes what was given, for Qt's 'QMediaPlayer::QMediaPlayer(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#QMediaPlayer

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QMediaPlayer::QMediaPlayer(QObject *parent)
    self._noteCreation(QMediaPlayer, lambda: Rituals.call(
        'ritual_ZN12QMediaPlayerC1EP7QObject',
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

  def play(self) -> None:
    """
    Calls Qt's 'void QMediaPlayer::play()'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#play
    """
    #  void QMediaPlayer::play()
    self.uglySide.call('ritual_ZN12QMediaPlayer4playEv')

  def pause(self) -> None:
    """
    Calls Qt's 'void QMediaPlayer::pause()'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#pause
    """
    #  void QMediaPlayer::pause()
    self.uglySide.call('ritual_ZN12QMediaPlayer5pauseEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QMediaPlayer::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#stop
    """
    #  void QMediaPlayer::stop()
    self.uglySide.call('ritual_ZN12QMediaPlayer4stopEv')

  def resetPlaybackOptions(self) -> None:
    """
    Calls Qt's 'void QMediaPlayer::resetPlaybackOptions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaplayer.html#resetPlaybackOptions
    """
    #  void QMediaPlayer::resetPlaybackOptions()
    self.uglySide.call('ritual_ZN12QMediaPlayer20resetPlaybackOptionsEv')

  @overload(QUrl)
  def sourceChanged(self, media: QUrl) -> None:
    """
    Calls Qt's 'void QMediaPlayer::sourceChanged(const QUrl &media)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#sourceChanged

    Parameters
    ----------

    media : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QMediaPlayer::sourceChanged(const QUrl &media)
    self.uglySide.call(
        'ritual_ZN12QMediaPlayer13sourceChangedERK4QUrl',
        self._valueOf(media),
    )

  @overload(PlaybackState)
  def playbackStateChanged(self, newState: PlaybackState) -> None:
    """
    Calls Qt's 'void
    QMediaPlayer::playbackStateChanged(QMediaPlayer::PlaybackState
    newState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaplayer.html#playbackStateChanged

    Parameters
    ----------

    newState : PlaybackState
      Passed on as its number.
    """
    #  void QMediaPlayer::playbackStateChanged(QMediaPlayer::PlaybackState
    #      newState)
    self.uglySide.call(
        'ritual_ZN12QMediaPlayer20playbackStateChangedENS_13PlaybackStateE',
        newState.value,
    )

  @overload(MediaStatus)
  def mediaStatusChanged(self, status: MediaStatus) -> None:
    """
    Calls Qt's 'void
    QMediaPlayer::mediaStatusChanged(QMediaPlayer::MediaStatus status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaplayer.html#mediaStatusChanged

    Parameters
    ----------

    status : MediaStatus
      Passed on as its number.
    """
    #  void QMediaPlayer::mediaStatusChanged(QMediaPlayer::MediaStatus
    #      status)
    self.uglySide.call(
        'ritual_ZN12QMediaPlayer18mediaStatusChangedENS_11MediaStatusE',
        status.value,
    )

  @overload(int)
  def durationChanged(self, duration: int) -> None:
    """
    Calls Qt's 'void QMediaPlayer::durationChanged(qint64 duration)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#durationChanged

    Parameters
    ----------

    duration : int
      Passed on as it is.
    """
    #  void QMediaPlayer::durationChanged(qint64 duration)
    self.uglySide.call(
        'ritual_ZN12QMediaPlayer15durationChangedEx', duration,
    )

  @overload(int)
  def positionChanged(self, position: int) -> None:
    """
    Calls Qt's 'void QMediaPlayer::positionChanged(qint64 position)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#positionChanged

    Parameters
    ----------

    position : int
      Passed on as it is.
    """
    #  void QMediaPlayer::positionChanged(qint64 position)
    self.uglySide.call(
        'ritual_ZN12QMediaPlayer15positionChangedEx', position,
    )

  @overload(bool)
  def hasAudioChanged(self, available: bool) -> None:
    """
    Calls Qt's 'void QMediaPlayer::hasAudioChanged(bool available)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#hasAudioChanged

    Parameters
    ----------

    available : bool
      Passed on as it is.
    """
    #  void QMediaPlayer::hasAudioChanged(bool available)
    self.uglySide.call(
        'ritual_ZN12QMediaPlayer15hasAudioChangedEb', available,
    )

  @overload(bool)
  def hasVideoChanged(self, videoAvailable: bool) -> None:
    """
    Calls Qt's 'void QMediaPlayer::hasVideoChanged(bool videoAvailable)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#hasVideoChanged

    Parameters
    ----------

    videoAvailable : bool
      Passed on as it is.
    """
    #  void QMediaPlayer::hasVideoChanged(bool videoAvailable)
    self.uglySide.call(
        'ritual_ZN12QMediaPlayer15hasVideoChangedEb', videoAvailable,
    )

  @overload(float)
  def bufferProgressChanged(self, progress: float) -> None:
    """
    Calls Qt's 'void QMediaPlayer::bufferProgressChanged(float progress)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaplayer.html#bufferProgressChanged

    Parameters
    ----------

    progress : float
      Passed on as it is.
    """
    #  void QMediaPlayer::bufferProgressChanged(float progress)
    self.uglySide.call(
        'ritual_ZN12QMediaPlayer21bufferProgressChangedEf', progress,
    )

  @overload(bool)
  def seekableChanged(self, seekable: bool) -> None:
    """
    Calls Qt's 'void QMediaPlayer::seekableChanged(bool seekable)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#seekableChanged

    Parameters
    ----------

    seekable : bool
      Passed on as it is.
    """
    #  void QMediaPlayer::seekableChanged(bool seekable)
    self.uglySide.call(
        'ritual_ZN12QMediaPlayer15seekableChangedEb', seekable,
    )

  @overload(bool)
  def playingChanged(self, playing: bool) -> None:
    """
    Calls Qt's 'void QMediaPlayer::playingChanged(bool playing)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#playingChanged

    Parameters
    ----------

    playing : bool
      Passed on as it is.
    """
    #  void QMediaPlayer::playingChanged(bool playing)
    self.uglySide.call('ritual_ZN12QMediaPlayer14playingChangedEb', playing)

  @overload(float)
  def playbackRateChanged(self, rate: float) -> None:
    """
    Calls Qt's 'void QMediaPlayer::playbackRateChanged(qreal rate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaplayer.html#playbackRateChanged

    Parameters
    ----------

    rate : float
      Passed on as it is.
    """
    #  void QMediaPlayer::playbackRateChanged(qreal rate)
    self.uglySide.call(
        'ritual_ZN12QMediaPlayer19playbackRateChangedEd', rate,
    )

  def loopsChanged(self) -> None:
    """
    Calls Qt's 'void QMediaPlayer::loopsChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#loopsChanged
    """
    #  void QMediaPlayer::loopsChanged()
    self.uglySide.call('ritual_ZN12QMediaPlayer12loopsChangedEv')

  def metaDataChanged(self) -> None:
    """
    Calls Qt's 'void QMediaPlayer::metaDataChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#metaDataChanged
    """
    #  void QMediaPlayer::metaDataChanged()
    self.uglySide.call('ritual_ZN12QMediaPlayer15metaDataChangedEv')

  def videoOutputChanged(self) -> None:
    """
    Calls Qt's 'void QMediaPlayer::videoOutputChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaplayer.html#videoOutputChanged
    """
    #  void QMediaPlayer::videoOutputChanged()
    self.uglySide.call('ritual_ZN12QMediaPlayer18videoOutputChangedEv')

  def audioOutputChanged(self) -> None:
    """
    Calls Qt's 'void QMediaPlayer::audioOutputChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaplayer.html#audioOutputChanged
    """
    #  void QMediaPlayer::audioOutputChanged()
    self.uglySide.call('ritual_ZN12QMediaPlayer18audioOutputChangedEv')

  def audioBufferOutputChanged(self) -> None:
    """
    Calls Qt's 'void QMediaPlayer::audioBufferOutputChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaplayer.html#audioBufferOutputChanged
    """
    #  void QMediaPlayer::audioBufferOutputChanged()
    self.uglySide.call('ritual_ZN12QMediaPlayer24audioBufferOutputChangedEv')

  def tracksChanged(self) -> None:
    """
    Calls Qt's 'void QMediaPlayer::tracksChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#tracksChanged
    """
    #  void QMediaPlayer::tracksChanged()
    self.uglySide.call('ritual_ZN12QMediaPlayer13tracksChangedEv')

  def activeTracksChanged(self) -> None:
    """
    Calls Qt's 'void QMediaPlayer::activeTracksChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaplayer.html#activeTracksChanged
    """
    #  void QMediaPlayer::activeTracksChanged()
    self.uglySide.call('ritual_ZN12QMediaPlayer19activeTracksChangedEv')

  def errorChanged(self) -> None:
    """
    Calls Qt's 'void QMediaPlayer::errorChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#errorChanged
    """
    #  void QMediaPlayer::errorChanged()
    self.uglySide.call('ritual_ZN12QMediaPlayer12errorChangedEv')

  @overload(Error, str)
  def errorOccurred(self, error: Error, errorString: str) -> None:
    """
    Calls Qt's 'void QMediaPlayer::errorOccurred(QMediaPlayer::Error error,
    const QString &errorString)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#errorOccurred

    Parameters
    ----------

    error : Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMediaPlayer::errorOccurred(QMediaPlayer::Error error, const
    #      QString &errorString)
    self.uglySide.call(
        'ritual_ZN12QMediaPlayer13errorOccurredENS_5ErrorERK7QString',
        error.value, errorString,
    )

  @overload(bool)
  def pitchCompensationChanged(self, a0: bool) -> None:
    """
    Calls Qt's 'void QMediaPlayer::pitchCompensationChanged(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaplayer.html#pitchCompensationChanged

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QMediaPlayer::pitchCompensationChanged(bool a0)
    self.uglySide.call(
        'ritual_ZN12QMediaPlayer24pitchCompensationChangedEb', a0,
    )

  def playbackOptionsChanged(self) -> None:
    """
    Calls Qt's 'void QMediaPlayer::playbackOptionsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaplayer.html#playbackOptionsChanged
    """
    #  void QMediaPlayer::playbackOptionsChanged()
    self.uglySide.call('ritual_ZN12QMediaPlayer22playbackOptionsChangedEv')

  def d_func(self) -> Optional[QMediaPlayerPrivate]:
    """
    Calls Qt's 'QMediaPlayerPrivate *QMediaPlayer::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayer.html#d_func

    Returns
    -------

    Optional[QMediaPlayerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMediaPlayerPrivate *QMediaPlayer::d_func()
    address = self.uglySide.call('ritual_ZN12QMediaPlayer6d_funcEv')
    from . import QMediaPlayerPrivate
    return QMediaPlayerPrivate._cuteAt(address)
