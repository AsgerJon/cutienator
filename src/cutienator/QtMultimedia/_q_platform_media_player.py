"""
QPlatformMediaPlayer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qplatformmediaplayer_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QPlatformMediaPlayer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QMediaPlayer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QIODevice, QUrl
  from . import QAudioBufferOutput, QMediaMetaData, QMediaTimeRange
  from . import QPlatformAudioOutput, QPlaybackOptions, QVideoSink
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioBufferOutput = WAIT['QAudioBufferOutput']
  QIODevice = WAIT['QIODevice']
  QPlatformAudioOutput = WAIT['QPlatformAudioOutput']
  QUrl = WAIT['QUrl']
  QVideoSink = WAIT['QVideoSink']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformMediaPlayer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlatformMediaPlayer: a plain Python object standing
  in front of one C++ QPlatformMediaPlayer.

  What exists
  -----------

  Every function of Qt's QPlatformMediaPlayer that has a ritual and that
  Python can call so far, 51 names in all: 'state', 'mediaStatus',
  'duration', 'position', 'setPosition', 'bufferProgress',
  'isAudioAvailable', 'isVideoAvailable', 'isSeekable',
  'availablePlaybackRanges', 'playbackRate', 'setPlaybackRate', 'media',
  'mediaStream', 'setMedia', 'play', 'pause', 'stop',
  'streamPlaybackSupported', 'setAudioOutput', 'setAudioBufferOutput',
  'metaData', 'setVideoSink', 'canPlayQrc', 'trackCount', 'trackMetaData',
  'activeTrack', 'setActiveTrack', 'durationChanged', 'positionChanged',
  'audioAvailableChanged', 'videoAvailableChanged', 'seekableChanged',
  'playbackRateChanged', 'bufferProgressChanged', 'metaDataChanged',
  'tracksChanged', 'activeTracksChanged', 'stateChanged',
  'mediaStatusChanged', 'error', 'setInvalidMediaWithError',
  'resetCurrentLoop', 'doLoop', 'loops', 'setLoops',
  'pitchCompensationAvailability', 'setPitchCompensation',
  'pitchCompensation', 'pitchCompensationChanged', 'playbackOptions'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlatformMediaPlayer::~QPlatformMediaPlayer()': the destructor:
    Python never removes a C++ QPlatformMediaPlayer.
  - Qt's 'void
    QPlatformMediaPlayer::durationChanged(std::chrono::milliseconds ms)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void
    QPlatformMediaPlayer::positionChanged(std::chrono::milliseconds ms)':
    takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QPlatformMediaPlayer is created at the first use, not by
    'QPlatformMediaPlayer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformMediaPlayer.
  """

  #  The enums Qt writes inside QPlatformMediaPlayer, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class TrackType(CuteNum):
    """
    The enum 'QPlatformMediaPlayer::TrackType' of Qt, with the 4 names Qt
    gives in it.
    """

    VideoStream = Kee[int](0)
    AudioStream = Kee[int](1)
    SubtitleStream = Kee[int](2)
    NTrackTypes = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformMediaPlayer'

  #  A C++ QPlatformMediaPlayer Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformMediaPlayer'

  #  The functions Qt calls itself that QPlatformMediaPlayer is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'duration': (
          ('_ZNK20QPlatformMediaPlayer8durationEv',
           ('long long', 'number', ''),
           ()),
      ),
      'position': (
          ('_ZNK20QPlatformMediaPlayer8positionEv',
           ('long long', 'number', ''),
           ()),
      ),
      'setPosition': (
          ('_ZN20QPlatformMediaPlayer11setPositionEx',
           ('nothing', 'nothing', ''),
           (
               ('long long', 'number', ''),
           )),
      ),
      'bufferProgress': (
          ('_ZNK20QPlatformMediaPlayer14bufferProgressEv',
           ('float', 'number', ''),
           ()),
      ),
      'isAudioAvailable': (
          ('_ZNK20QPlatformMediaPlayer16isAudioAvailableEv',
           ('bool', 'number', ''),
           ()),
      ),
      'isVideoAvailable': (
          ('_ZNK20QPlatformMediaPlayer16isVideoAvailableEv',
           ('bool', 'number', ''),
           ()),
      ),
      'isSeekable': (
          ('_ZNK20QPlatformMediaPlayer10isSeekableEv',
           ('bool', 'number', ''),
           ()),
      ),
      'availablePlaybackRanges': (
          ('_ZNK20QPlatformMediaPlayer23availablePlaybackRangesEv',
           ('address', 'value', 'QtMultimedia:QMediaTimeRange'),
           ()),
      ),
      'playbackRate': (
          ('_ZNK20QPlatformMediaPlayer12playbackRateEv',
           ('double', 'number', ''),
           ()),
      ),
      'setPlaybackRate': (
          ('_ZN20QPlatformMediaPlayer15setPlaybackRateEd',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
           )),
      ),
      'media': (
          ('_ZNK20QPlatformMediaPlayer5mediaEv',
           ('address', 'value', 'QtCore:QUrl'),
           ()),
      ),
      'mediaStream': (
          ('_ZNK20QPlatformMediaPlayer11mediaStreamEv',
           ('address', 'address', 'QtCore:QIODevice'),
           ()),
      ),
      'setMedia': (
          ('_ZN20QPlatformMediaPlayer8setMediaERK4QUrlP9QIODevice',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QUrl'),
               ('address', 'address', 'QtCore:QIODevice'),
           )),
      ),
      'play': (
          ('_ZN20QPlatformMediaPlayer4playEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'pause': (
          ('_ZN20QPlatformMediaPlayer5pauseEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'stop': (
          ('_ZN20QPlatformMediaPlayer4stopEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'streamPlaybackSupported': (
          ('_ZNK20QPlatformMediaPlayer23streamPlaybackSupportedEv',
           ('bool', 'number', ''),
           ()),
      ),
      'setAudioOutput': (
          ('_ZN20QPlatformMediaPlayer14setAudioOutputEP20QPlatformAudioOutp'
           'ut',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtMultimedia:QPlatformAudioOutput'),
           )),
      ),
      'setAudioBufferOutput': (
          ('_ZN20QPlatformMediaPlayer20setAudioBufferOutputEP18QAudioBuffer'
           'Output',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtMultimedia:QAudioBufferOutput'),
           )),
      ),
      'metaData': (
          ('_ZNK20QPlatformMediaPlayer8metaDataEv',
           ('address', 'value', 'QtMultimedia:QMediaMetaData'),
           ()),
      ),
      'setVideoSink': (
          ('_ZN20QPlatformMediaPlayer12setVideoSinkEP10QVideoSink',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtMultimedia:QVideoSink'),
           )),
      ),
      'canPlayQrc': (
          ('_ZNK20QPlatformMediaPlayer10canPlayQrcEv',
           ('bool', 'number', ''),
           ()),
      ),
      'trackCount': (
          ('_ZN20QPlatformMediaPlayer10trackCountENS_9TrackTypeE',
           ('int', 'number', ''),
           (
               ('int', 'enum',
                'QtMultimedia:QPlatformMediaPlayer.TrackType'),
           )),
      ),
      'trackMetaData': (
          ('_ZN20QPlatformMediaPlayer13trackMetaDataENS_9TrackTypeEi',
           ('address', 'value', 'QtMultimedia:QMediaMetaData'),
           (
               ('int', 'enum',
                'QtMultimedia:QPlatformMediaPlayer.TrackType'),
               ('int', 'number', ''),
           )),
      ),
      'activeTrack': (
          ('_ZN20QPlatformMediaPlayer11activeTrackENS_9TrackTypeE',
           ('int', 'number', ''),
           (
               ('int', 'enum',
                'QtMultimedia:QPlatformMediaPlayer.TrackType'),
           )),
      ),
      'setActiveTrack': (
          ('_ZN20QPlatformMediaPlayer14setActiveTrackENS_9TrackTypeEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtMultimedia:QPlatformMediaPlayer.TrackType'),
               ('int', 'number', ''),
           )),
      ),
      'setLoops': (
          ('_ZN20QPlatformMediaPlayer8setLoopsEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'pitchCompensationAvailability': (
          ('_ZNK20QPlatformMediaPlayer29pitchCompensationAvailabilityEv',
           ('int', 'enum',
            'QtMultimedia:QPlatformMediaPlayer.PitchCompensationAvailability'),
           ()),
      ),
      'setPitchCompensation': (
          ('_ZN20QPlatformMediaPlayer20setPitchCompensationEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'pitchCompensation': (
          ('_ZNK20QPlatformMediaPlayer17pitchCompensationEv',
           ('bool', 'number', ''),
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

  def state(self) -> QMediaPlayer.PlaybackState:
    """
    Calls Qt's 'QMediaPlayer::PlaybackState QPlatformMediaPlayer::state()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmediaplayer.html#state

    Returns
    -------

    QMediaPlayer.PlaybackState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QMediaPlayer.PlaybackState(number)' gives.
    """
    #  QMediaPlayer::PlaybackState QPlatformMediaPlayer::state() const
    return QMediaPlayer.PlaybackState(self.uglySide.call(
        'ritual_ZNK20QPlatformMediaPlayer5stateEv',
    ))

  def mediaStatus(self) -> QMediaPlayer.MediaStatus:
    """
    Calls Qt's 'QMediaPlayer::MediaStatus QPlatformMediaPlayer::mediaStatus()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#mediaStatus

    Returns
    -------

    QMediaPlayer.MediaStatus
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QMediaPlayer.MediaStatus(number)' gives.
    """
    #  QMediaPlayer::MediaStatus QPlatformMediaPlayer::mediaStatus() const
    return QMediaPlayer.MediaStatus(self.uglySide.call(
        'ritual_ZNK20QPlatformMediaPlayer11mediaStatusEv',
    ))

  def duration(self) -> int:
    """
    Calls Qt's 'qint64 QPlatformMediaPlayer::duration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmediaplayer.html#duration
    """
    #  qint64 QPlatformMediaPlayer::duration() const
    return self.uglySide.call('ritual_ZNK20QPlatformMediaPlayer8durationEv')

  def position(self) -> int:
    """
    Calls Qt's 'qint64 QPlatformMediaPlayer::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmediaplayer.html#position
    """
    #  qint64 QPlatformMediaPlayer::position() const
    ritual = 'ritual_ZNK20QPlatformMediaPlayer8positionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QPlatformMediaPlayer8positionEv'
    return self.uglySide.call(ritual)

  def bufferProgress(self) -> float:
    """
    Calls Qt's 'float QPlatformMediaPlayer::bufferProgress() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#bufferProgress
    """
    #  float QPlatformMediaPlayer::bufferProgress() const
    return self.uglySide.call(
        'ritual_ZNK20QPlatformMediaPlayer14bufferProgressEv',
    )

  def isAudioAvailable(self) -> bool:
    """
    Calls Qt's 'bool QPlatformMediaPlayer::isAudioAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#isAudioAvailable
    """
    #  bool QPlatformMediaPlayer::isAudioAvailable() const
    ritual = 'ritual_ZNK20QPlatformMediaPlayer16isAudioAvailableEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QPlatformMediaPlayer16isAudioAvailableEv'
    return self.uglySide.call(ritual)

  def isVideoAvailable(self) -> bool:
    """
    Calls Qt's 'bool QPlatformMediaPlayer::isVideoAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#isVideoAvailable
    """
    #  bool QPlatformMediaPlayer::isVideoAvailable() const
    ritual = 'ritual_ZNK20QPlatformMediaPlayer16isVideoAvailableEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QPlatformMediaPlayer16isVideoAvailableEv'
    return self.uglySide.call(ritual)

  def isSeekable(self) -> bool:
    """
    Calls Qt's 'bool QPlatformMediaPlayer::isSeekable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#isSeekable
    """
    #  bool QPlatformMediaPlayer::isSeekable() const
    ritual = 'ritual_ZNK20QPlatformMediaPlayer10isSeekableEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QPlatformMediaPlayer10isSeekableEv'
    return self.uglySide.call(ritual)

  def availablePlaybackRanges(self) -> QMediaTimeRange:
    """
    Calls Qt's 'QMediaTimeRange
    QPlatformMediaPlayer::availablePlaybackRanges() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#availablePlaybackRanges

    Returns
    -------

    QMediaTimeRange
      A new cute QMediaTimeRange around the copy Qt gave back. Python owns
      it.
    """
    #  QMediaTimeRange QPlatformMediaPlayer::availablePlaybackRanges() const
    address = self.uglySide.call(
        'ritual_ZNK20QPlatformMediaPlayer23availablePlaybackRangesEv',
    )
    from . import QMediaTimeRange
    return QMediaTimeRange._cuteOwning(address)

  def playbackRate(self) -> float:
    """
    Calls Qt's 'qreal QPlatformMediaPlayer::playbackRate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#playbackRate
    """
    #  qreal QPlatformMediaPlayer::playbackRate() const
    return self.uglySide.call(
        'ritual_ZNK20QPlatformMediaPlayer12playbackRateEv',
    )

  def media(self) -> QUrl:
    """
    Calls Qt's 'QUrl QPlatformMediaPlayer::media() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmediaplayer.html#media

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QPlatformMediaPlayer::media() const
    address = self.uglySide.call('ritual_ZNK20QPlatformMediaPlayer5mediaEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def mediaStream(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'const QIODevice *QPlatformMediaPlayer::mediaStream() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#mediaStream

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QIODevice *QPlatformMediaPlayer::mediaStream() const
    address = self.uglySide.call(
        'ritual_ZNK20QPlatformMediaPlayer11mediaStreamEv',
    )
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  def streamPlaybackSupported(self) -> bool:
    """
    Calls Qt's 'bool QPlatformMediaPlayer::streamPlaybackSupported() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#streamPlaybackSupported
    """
    #  bool QPlatformMediaPlayer::streamPlaybackSupported() const
    ritual = 'ritual_ZNK20QPlatformMediaPlayer23streamPlaybackSupportedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QPlatformMediaPlayer23streamPlaybackSupportedEv')
    return self.uglySide.call(ritual)

  def metaData(self) -> QMediaMetaData:
    """
    Calls Qt's 'QMediaMetaData QPlatformMediaPlayer::metaData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmediaplayer.html#metaData

    Returns
    -------

    QMediaMetaData
      A new cute QMediaMetaData around the copy Qt gave back. Python owns it.
    """
    #  QMediaMetaData QPlatformMediaPlayer::metaData() const
    ritual = 'ritual_ZNK20QPlatformMediaPlayer8metaDataEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QPlatformMediaPlayer8metaDataEv'
    address = self.uglySide.call(ritual)
    from . import QMediaMetaData
    return QMediaMetaData._cuteOwning(address)

  def canPlayQrc(self) -> bool:
    """
    Calls Qt's 'bool QPlatformMediaPlayer::canPlayQrc() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#canPlayQrc
    """
    #  bool QPlatformMediaPlayer::canPlayQrc() const
    ritual = 'ritual_ZNK20QPlatformMediaPlayer10canPlayQrcEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QPlatformMediaPlayer10canPlayQrcEv'
    return self.uglySide.call(ritual)

  def loops(self) -> int:
    """
    Calls Qt's 'int QPlatformMediaPlayer::loops() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmediaplayer.html#loops
    """
    #  int QPlatformMediaPlayer::loops() const
    return self.uglySide.call('ritual_ZNK20QPlatformMediaPlayer5loopsEv')

  def pitchCompensationAvailability(
      self,
  ) -> QMediaPlayer.PitchCompensationAvailability:
    """
    Calls Qt's 'PitchCompensationAvailability
    QPlatformMediaPlayer::pitchCompensationAvailability() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html

    Returns
    -------

    QMediaPlayer.PitchCompensationAvailability
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QMediaPlayer.PitchCompensationAvailability(number)' gives.
    """
    #  PitchCompensationAvailability
    #      QPlatformMediaPlayer::pitchCompensationAvailability() const
    ritual = (
        'ritual_ZNK20QPlatformMediaPlayer29pitchCompensationAvailabilityEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QPlatformMediaPlayer29pitchCompensationAvailabil'
          'ityEv')
    return QMediaPlayer.PitchCompensationAvailability(self.uglySide.call(
        ritual,
    ))

  def pitchCompensation(self) -> bool:
    """
    Calls Qt's 'bool QPlatformMediaPlayer::pitchCompensation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#pitchCompensation
    """
    #  bool QPlatformMediaPlayer::pitchCompensation() const
    ritual = 'ritual_ZNK20QPlatformMediaPlayer17pitchCompensationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QPlatformMediaPlayer17pitchCompensationEv'
    return self.uglySide.call(ritual)

  def playbackOptions(self) -> QPlaybackOptions:
    """
    Calls Qt's 'QPlaybackOptions QPlatformMediaPlayer::playbackOptions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#playbackOptions

    Returns
    -------

    QPlaybackOptions
      A new cute QPlaybackOptions around the copy Qt gave back. Python owns
      it.
    """
    #  QPlaybackOptions QPlatformMediaPlayer::playbackOptions() const
    address = self.uglySide.call(
        'ritual_ZNK20QPlatformMediaPlayer15playbackOptionsEv',
    )
    from . import QPlaybackOptions
    return QPlaybackOptions._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setPosition(self, position: int) -> None:
    """
    Calls Qt's 'void QPlatformMediaPlayer::setPosition(qint64 position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#setPosition

    Parameters
    ----------

    position : int
      Passed on as it is.
    """
    #  void QPlatformMediaPlayer::setPosition(qint64 position)
    self.uglySide.call(
        'ritual_ZN20QPlatformMediaPlayer11setPositionEx', position,
    )

  @overload(float)
  def setPlaybackRate(self, rate: float) -> None:
    """
    Calls Qt's 'void QPlatformMediaPlayer::setPlaybackRate(qreal rate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#setPlaybackRate

    Parameters
    ----------

    rate : float
      Passed on as it is.
    """
    #  void QPlatformMediaPlayer::setPlaybackRate(qreal rate)
    self.uglySide.call(
        'ritual_ZN20QPlatformMediaPlayer15setPlaybackRateEd', rate,
    )

  @overload(QUrl, QIODevice)
  @overload(QUrl, NoneType)
  def setMedia(self, media: QUrl, stream: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void QPlatformMediaPlayer::setMedia(const QUrl &media,
    QIODevice *stream)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmediaplayer.html#setMedia

    Parameters
    ----------

    media : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    stream : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformMediaPlayer::setMedia(const QUrl &media, QIODevice
    #      *stream)
    self.uglySide.call(
        'ritual_ZN20QPlatformMediaPlayer8setMediaERK4QUrlP9QIODevice',
        self._valueOf(media), self._addressOf(stream),
    )

  @overload(QPlatformAudioOutput)
  @overload(NoneType)
  def setAudioOutput(self, a0: Optional[QPlatformAudioOutput]) -> None:
    """
    Calls Qt's 'void
    QPlatformMediaPlayer::setAudioOutput(QPlatformAudioOutput *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#setAudioOutput

    Parameters
    ----------

    a0 : Optional[QPlatformAudioOutput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformMediaPlayer::setAudioOutput(QPlatformAudioOutput *a0)
    ritual = (
        'ritual_ZN20QPlatformMediaPlayer14setAudioOutputEP20QPlatformAudioO'
        'utput')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QPlatformMediaPlayer14setAudioOutputEP20QPlatform'
          'AudioOutput')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QAudioBufferOutput)
  @overload(NoneType)
  def setAudioBufferOutput(self, a0: Optional[QAudioBufferOutput]) -> None:
    """
    Calls Qt's 'void
    QPlatformMediaPlayer::setAudioBufferOutput(QAudioBufferOutput *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#setAudioBufferOutput

    Parameters
    ----------

    a0 : Optional[QAudioBufferOutput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformMediaPlayer::setAudioBufferOutput(QAudioBufferOutput
    #      *a0)
    ritual = (
        'ritual_ZN20QPlatformMediaPlayer20setAudioBufferOutputEP18QAudioBuf'
        'ferOutput')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QPlatformMediaPlayer20setAudioBufferOutputEP18QAu'
          'dioBufferOutput')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QVideoSink)
  @overload(NoneType)
  def setVideoSink(self, a0: Optional[QVideoSink]) -> None:
    """
    Calls Qt's 'void QPlatformMediaPlayer::setVideoSink(QVideoSink *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#setVideoSink

    Parameters
    ----------

    a0 : Optional[QVideoSink]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformMediaPlayer::setVideoSink(QVideoSink *a0)
    self.uglySide.call(
        'ritual_ZN20QPlatformMediaPlayer12setVideoSinkEP10QVideoSink',
        self._addressOf(a0),
    )

  @overload(TrackType, int)
  def setActiveTrack(self, a0: TrackType, a1: int) -> None:
    """
    Calls Qt's 'void QPlatformMediaPlayer::setActiveTrack(TrackType a0, int
    a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#setActiveTrack

    Parameters
    ----------

    a0 : TrackType
      Passed on as its number.

    a1 : int
      Passed on as it is.
    """
    #  void QPlatformMediaPlayer::setActiveTrack(TrackType a0, int a1)
    ritual = (
        'ritual_ZN20QPlatformMediaPlayer14setActiveTrackENS_9TrackTypeEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QPlatformMediaPlayer14setActiveTrackENS_9TrackTyp'
          'eEi')
    self.uglySide.call(ritual, a0.value, a1)

  @overload(QMediaPlayer.Error, str)
  def setInvalidMediaWithError(
      self,
      a0: QMediaPlayer.Error,
      errString: str,
  ) -> None:
    """
    Calls Qt's 'void
    QPlatformMediaPlayer::setInvalidMediaWithError(QMediaPlayer::Error a0,
    const QString &errString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#setInvalidMediaWithError

    Parameters
    ----------

    a0 : QMediaPlayer.Error
      Passed on as its number.

    errString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void
    #      QPlatformMediaPlayer::setInvalidMediaWithError(QMediaPlayer::Error
    #      a0, const QString &errString)
    self.uglySide.call(
        'ritual_ZN20QPlatformMediaPlayer24setInvalidMediaWithErrorEN12QMedi'
        'aPlayer5ErrorERK7QString',
        a0.value, errString,
    )

  @overload(int)
  def setLoops(self, loops: int) -> None:
    """
    Calls Qt's 'void QPlatformMediaPlayer::setLoops(int loops)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmediaplayer.html#setLoops

    Parameters
    ----------

    loops : int
      Passed on as it is.
    """
    #  void QPlatformMediaPlayer::setLoops(int loops)
    ritual = 'ritual_ZN20QPlatformMediaPlayer8setLoopsEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QPlatformMediaPlayer8setLoopsEi'
    self.uglySide.call(ritual, loops)

  @overload(bool)
  def setPitchCompensation(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QPlatformMediaPlayer::setPitchCompensation(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#setPitchCompensation

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QPlatformMediaPlayer::setPitchCompensation(bool enabled)
    ritual = 'ritual_ZN20QPlatformMediaPlayer20setPitchCompensationEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QPlatformMediaPlayer20setPitchCompensationEb'
    self.uglySide.call(ritual, enabled)

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
  @overload(QMediaPlayer)
  @overload(NoneType)
  def __init__(self, parent: Optional[QMediaPlayer] = None) -> None:
    """
    Notes what was given, for Qt's
    'QPlatformMediaPlayer::QPlatformMediaPlayer(QMediaPlayer *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#QPlatformMediaPlayer

    Parameters
    ----------

    parent : Optional[QMediaPlayer]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPlatformMediaPlayer::QPlatformMediaPlayer(QMediaPlayer *parent)
    self._noteCreation(QPlatformMediaPlayer, lambda: Rituals.call(
        'ritual_ZN20QPlatformMediaPlayerC1EP12QMediaPlayer',
        self._addressOf(parent),
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
    Calls Qt's 'void QPlatformMediaPlayer::play()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmediaplayer.html#play
    """
    #  void QPlatformMediaPlayer::play()
    self.uglySide.call('ritual_ZN20QPlatformMediaPlayer4playEv')

  def pause(self) -> None:
    """
    Calls Qt's 'void QPlatformMediaPlayer::pause()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmediaplayer.html#pause
    """
    #  void QPlatformMediaPlayer::pause()
    self.uglySide.call('ritual_ZN20QPlatformMediaPlayer5pauseEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QPlatformMediaPlayer::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmediaplayer.html#stop
    """
    #  void QPlatformMediaPlayer::stop()
    self.uglySide.call('ritual_ZN20QPlatformMediaPlayer4stopEv')

  @overload(TrackType)
  def trackCount(self, a0: TrackType) -> int:
    """
    Calls Qt's 'int QPlatformMediaPlayer::trackCount(TrackType a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#trackCount

    Parameters
    ----------

    a0 : TrackType
      Passed on as its number.
    """
    #  int QPlatformMediaPlayer::trackCount(TrackType a0)
    ritual = 'ritual_ZN20QPlatformMediaPlayer10trackCountENS_9TrackTypeE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QPlatformMediaPlayer10trackCountENS_9TrackTypeE')
    return self.uglySide.call(ritual, a0.value)

  @overload(TrackType, int)
  def trackMetaData(self, a0: TrackType, a1: int) -> QMediaMetaData:
    """
    Calls Qt's 'QMediaMetaData QPlatformMediaPlayer::trackMetaData(TrackType
    a0, int a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#trackMetaData

    Parameters
    ----------

    a0 : TrackType
      Passed on as its number.

    a1 : int
      Passed on as it is.

    Returns
    -------

    QMediaMetaData
      A new cute QMediaMetaData around the copy Qt gave back. Python owns it.
    """
    #  QMediaMetaData QPlatformMediaPlayer::trackMetaData(TrackType a0, int
    #      a1)
    ritual = 'ritual_ZN20QPlatformMediaPlayer13trackMetaDataENS_9TrackTypeEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QPlatformMediaPlayer13trackMetaDataENS_9TrackType'
          'Ei')
    address = self.uglySide.call(ritual, a0.value, a1)
    from . import QMediaMetaData
    return QMediaMetaData._cuteOwning(address)

  @overload(TrackType)
  def activeTrack(self, a0: TrackType) -> int:
    """
    Calls Qt's 'int QPlatformMediaPlayer::activeTrack(TrackType a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#activeTrack

    Parameters
    ----------

    a0 : TrackType
      Passed on as its number.
    """
    #  int QPlatformMediaPlayer::activeTrack(TrackType a0)
    ritual = 'ritual_ZN20QPlatformMediaPlayer11activeTrackENS_9TrackTypeE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QPlatformMediaPlayer11activeTrackENS_9TrackTypeE')
    return self.uglySide.call(ritual, a0.value)

  @overload(int)
  def durationChanged(self, duration: int) -> None:
    """
    Calls Qt's 'void QPlatformMediaPlayer::durationChanged(qint64 duration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#durationChanged

    Parameters
    ----------

    duration : int
      Passed on as it is.
    """
    #  void QPlatformMediaPlayer::durationChanged(qint64 duration)
    self.uglySide.call(
        'ritual_ZN20QPlatformMediaPlayer15durationChangedEx', duration,
    )

  @overload(int)
  def positionChanged(self, position: int) -> None:
    """
    Calls Qt's 'void QPlatformMediaPlayer::positionChanged(qint64 position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#positionChanged

    Parameters
    ----------

    position : int
      Passed on as it is.
    """
    #  void QPlatformMediaPlayer::positionChanged(qint64 position)
    self.uglySide.call(
        'ritual_ZN20QPlatformMediaPlayer15positionChangedEx', position,
    )

  @overload(bool)
  def audioAvailableChanged(self, audioAvailable: bool) -> None:
    """
    Calls Qt's 'void QPlatformMediaPlayer::audioAvailableChanged(bool
    audioAvailable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#audioAvailableChanged

    Parameters
    ----------

    audioAvailable : bool
      Passed on as it is.
    """
    #  void QPlatformMediaPlayer::audioAvailableChanged(bool audioAvailable)
    self.uglySide.call(
        'ritual_ZN20QPlatformMediaPlayer21audioAvailableChangedEb',
        audioAvailable,
    )

  @overload(bool)
  def videoAvailableChanged(self, videoAvailable: bool) -> None:
    """
    Calls Qt's 'void QPlatformMediaPlayer::videoAvailableChanged(bool
    videoAvailable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#videoAvailableChanged

    Parameters
    ----------

    videoAvailable : bool
      Passed on as it is.
    """
    #  void QPlatformMediaPlayer::videoAvailableChanged(bool videoAvailable)
    self.uglySide.call(
        'ritual_ZN20QPlatformMediaPlayer21videoAvailableChangedEb',
        videoAvailable,
    )

  @overload(bool)
  def seekableChanged(self, seekable: bool) -> None:
    """
    Calls Qt's 'void QPlatformMediaPlayer::seekableChanged(bool seekable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#seekableChanged

    Parameters
    ----------

    seekable : bool
      Passed on as it is.
    """
    #  void QPlatformMediaPlayer::seekableChanged(bool seekable)
    self.uglySide.call(
        'ritual_ZN20QPlatformMediaPlayer15seekableChangedEb', seekable,
    )

  @overload(float)
  def playbackRateChanged(self, rate: float) -> None:
    """
    Calls Qt's 'void QPlatformMediaPlayer::playbackRateChanged(qreal rate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#playbackRateChanged

    Parameters
    ----------

    rate : float
      Passed on as it is.
    """
    #  void QPlatformMediaPlayer::playbackRateChanged(qreal rate)
    self.uglySide.call(
        'ritual_ZN20QPlatformMediaPlayer19playbackRateChangedEd', rate,
    )

  @overload(float)
  def bufferProgressChanged(self, progress: float) -> None:
    """
    Calls Qt's 'void QPlatformMediaPlayer::bufferProgressChanged(float
    progress)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#bufferProgressChanged

    Parameters
    ----------

    progress : float
      Passed on as it is.
    """
    #  void QPlatformMediaPlayer::bufferProgressChanged(float progress)
    self.uglySide.call(
        'ritual_ZN20QPlatformMediaPlayer21bufferProgressChangedEf', progress,
    )

  def metaDataChanged(self) -> None:
    """
    Calls Qt's 'void QPlatformMediaPlayer::metaDataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#metaDataChanged
    """
    #  void QPlatformMediaPlayer::metaDataChanged()
    self.uglySide.call('ritual_ZN20QPlatformMediaPlayer15metaDataChangedEv')

  def tracksChanged(self) -> None:
    """
    Calls Qt's 'void QPlatformMediaPlayer::tracksChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#tracksChanged
    """
    #  void QPlatformMediaPlayer::tracksChanged()
    self.uglySide.call('ritual_ZN20QPlatformMediaPlayer13tracksChangedEv')

  def activeTracksChanged(self) -> None:
    """
    Calls Qt's 'void QPlatformMediaPlayer::activeTracksChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#activeTracksChanged
    """
    #  void QPlatformMediaPlayer::activeTracksChanged()
    self.uglySide.call(
        'ritual_ZN20QPlatformMediaPlayer19activeTracksChangedEv',
    )

  @overload(QMediaPlayer.PlaybackState)
  def stateChanged(self, newState: QMediaPlayer.PlaybackState) -> None:
    """
    Calls Qt's 'void
    QPlatformMediaPlayer::stateChanged(QMediaPlayer::PlaybackState
    newState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#stateChanged

    Parameters
    ----------

    newState : QMediaPlayer.PlaybackState
      Passed on as its number.
    """
    #  void QPlatformMediaPlayer::stateChanged(QMediaPlayer::PlaybackState
    #      newState)
    self.uglySide.call(
        'ritual_ZN20QPlatformMediaPlayer12stateChangedEN12QMediaPlayer13Pla'
        'ybackStateE',
        newState.value,
    )

  @overload(QMediaPlayer.MediaStatus)
  def mediaStatusChanged(self, status: QMediaPlayer.MediaStatus) -> None:
    """
    Calls Qt's 'void
    QPlatformMediaPlayer::mediaStatusChanged(QMediaPlayer::MediaStatus
    status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#mediaStatusChanged

    Parameters
    ----------

    status : QMediaPlayer.MediaStatus
      Passed on as its number.
    """
    #  void
    #      QPlatformMediaPlayer::mediaStatusChanged(QMediaPlayer::MediaStatus
    #      status)
    self.uglySide.call(
        'ritual_ZN20QPlatformMediaPlayer18mediaStatusChangedEN12QMediaPlaye'
        'r11MediaStatusE',
        status.value,
    )

  @overload(QMediaPlayer.Error, str)
  def error(self, a0: QMediaPlayer.Error, errorString: str) -> None:
    """
    Calls Qt's 'void QPlatformMediaPlayer::error(QMediaPlayer::Error a0,
    const QString &errorString)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmediaplayer.html#error

    Parameters
    ----------

    a0 : QMediaPlayer.Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlatformMediaPlayer::error(QMediaPlayer::Error a0, const QString
    #      &errorString)
    self.uglySide.call(
        'ritual_ZN20QPlatformMediaPlayer5errorEN12QMediaPlayer5ErrorERK7QSt'
        'ring',
        a0.value, errorString,
    )

  def resetCurrentLoop(self) -> None:
    """
    Calls Qt's 'void QPlatformMediaPlayer::resetCurrentLoop()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#resetCurrentLoop
    """
    #  void QPlatformMediaPlayer::resetCurrentLoop()
    self.uglySide.call('ritual_ZN20QPlatformMediaPlayer16resetCurrentLoopEv')

  def doLoop(self) -> bool:
    """
    Calls Qt's 'bool QPlatformMediaPlayer::doLoop()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmediaplayer.html#doLoop
    """
    #  bool QPlatformMediaPlayer::doLoop()
    return self.uglySide.call('ritual_ZN20QPlatformMediaPlayer6doLoopEv')

  @overload(bool)
  def pitchCompensationChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QPlatformMediaPlayer::pitchCompensationChanged(bool
    enabled) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaplayer.html#pitchCompensationChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QPlatformMediaPlayer::pitchCompensationChanged(bool enabled)
    #      const
    self.uglySide.call(
        'ritual_ZNK20QPlatformMediaPlayer24pitchCompensationChangedEb',
        enabled,
    )
