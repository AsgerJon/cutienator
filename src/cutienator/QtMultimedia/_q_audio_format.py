"""
QAudioFormat binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/qaudioformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QAudioFormat(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAudioFormat: a plain Python object standing in front
  of one C++ QAudioFormat.

  C++ hands a QAudioFormat around as a copy, so every C++ QAudioFormat behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QAudioFormat that has a ritual and that Python can
  call so far, 21 names in all: 'isValid', 'setSampleRate', 'sampleRate',
  'setChannelConfig', 'channelConfig', 'setChannelCount', 'channelCount',
  'channelOffset', 'setSampleFormat', 'sampleFormat', 'bytesForDuration',
  'durationForBytes', 'bytesForFrames', 'framesForBytes',
  'framesForDuration', 'durationForFrames', 'bytesPerFrame',
  'bytesPerSample', '__eq__', '__ne__',
  'defaultChannelConfigForChannelCount'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'float QAudioFormat::normalizedSampleValue(const void *sample)
    const': names 'void', which has no cute class yet.
  - Qt's 'QAudioFormat::~QAudioFormat()': the destructor: Python removes its
    C++ QAudioFormat by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 24 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QAudioFormat is created at the first use, not by
    'QAudioFormat(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QAudioFormat back gives a copy the ritual made for
    Python, in a new cute QAudioFormat.
  - Each name of Qt's QAudioFormat that has no cute function yet,
    'normalizedSampleValue', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QAudioFormat, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class AudioChannelPosition(CuteNum):
    """
    The enum 'QAudioFormat::AudioChannelPosition' of Qt, with the 25 names Qt
    gives in it.
    """

    UnknownPosition = Kee[int](0)
    FrontLeft = Kee[int](1)
    FrontRight = Kee[int](2)
    FrontCenter = Kee[int](3)
    LFE = Kee[int](4)
    BackLeft = Kee[int](5)
    BackRight = Kee[int](6)
    FrontLeftOfCenter = Kee[int](7)
    FrontRightOfCenter = Kee[int](8)
    BackCenter = Kee[int](9)
    SideLeft = Kee[int](10)
    SideRight = Kee[int](11)
    TopCenter = Kee[int](12)
    TopFrontLeft = Kee[int](13)
    TopFrontCenter = Kee[int](14)
    TopFrontRight = Kee[int](15)
    TopBackLeft = Kee[int](16)
    TopBackCenter = Kee[int](17)
    TopBackRight = Kee[int](18)
    LFE2 = Kee[int](19)
    TopSideLeft = Kee[int](20)
    TopSideRight = Kee[int](21)
    BottomFrontCenter = Kee[int](22)
    BottomFrontLeft = Kee[int](23)
    BottomFrontRight = Kee[int](24)

  class ChannelConfig(CuteNum):
    """
    The enum 'QAudioFormat::ChannelConfig' of Qt, with the 10 names Qt gives
    in it.
    """

    ChannelConfigUnknown = Kee[int](0)
    ChannelConfigMono = Kee[int](8)
    ChannelConfigStereo = Kee[int](6)
    ChannelConfig2Dot1 = Kee[int](22)
    ChannelConfig3Dot0 = Kee[int](14)
    ChannelConfig3Dot1 = Kee[int](30)
    ChannelConfigSurround5Dot0 = Kee[int](110)
    ChannelConfigSurround5Dot1 = Kee[int](126)
    ChannelConfigSurround7Dot0 = Kee[int](3182)
    ChannelConfigSurround7Dot1 = Kee[int](3198)

  class SampleFormat(CuteNum):
    """
    The enum 'QAudioFormat::SampleFormat' of Qt, with the 6 names Qt gives in
    it.
    """

    Unknown = Kee[int](0)
    UInt8 = Kee[int](1)
    Int16 = Kee[int](2)
    Int32 = Kee[int](3)
    Float = Kee[int](4)
    NSampleFormats = Kee[int](5)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int)
  def defaultChannelConfigForChannelCount(
      channelCount: int,
  ) -> ChannelConfig:
    """
    Calls Qt's 'ChannelConfig
    QAudioFormat::defaultChannelConfigForChannelCount(int channelCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudioformat.html

    Parameters
    ----------

    channelCount : int
      Passed on as it is.

    Returns
    -------

    ChannelConfig
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ChannelConfig(number)'
      gives.
    """
    #  ChannelConfig QAudioFormat::defaultChannelConfigForChannelCount(int
    #      channelCount)
    return QAudioFormat.ChannelConfig(Rituals.call(
        'ritual_ZN12QAudioFormat35defaultChannelConfigForChannelCountEi',
        channelCount,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAudioFormat'

  #  Qt's '~QAudioFormat()'. Naming it makes this a value class: Python owns
  #  every C++ QAudioFormat behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QAudioFormatD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QAudioFormat::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioformat.html#isValid
    """
    #  bool QAudioFormat::isValid() const
    return self.uglySide.call('ritual_ZNK12QAudioFormat7isValidEv')

  def sampleRate(self) -> int:
    """
    Calls Qt's 'int QAudioFormat::sampleRate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioformat.html#sampleRate
    """
    #  int QAudioFormat::sampleRate() const
    return self.uglySide.call('ritual_ZNK12QAudioFormat10sampleRateEv')

  def channelConfig(self) -> ChannelConfig:
    """
    Calls Qt's 'ChannelConfig QAudioFormat::channelConfig() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioformat.html#channelConfig

    Returns
    -------

    ChannelConfig
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ChannelConfig(number)'
      gives.
    """
    #  ChannelConfig QAudioFormat::channelConfig() const
    return QAudioFormat.ChannelConfig(self.uglySide.call(
        'ritual_ZNK12QAudioFormat13channelConfigEv',
    ))

  def channelCount(self) -> int:
    """
    Calls Qt's 'int QAudioFormat::channelCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioformat.html#channelCount
    """
    #  int QAudioFormat::channelCount() const
    return self.uglySide.call('ritual_ZNK12QAudioFormat12channelCountEv')

  @overload(AudioChannelPosition)
  def channelOffset(self, channel: AudioChannelPosition) -> int:
    """
    Calls Qt's 'int QAudioFormat::channelOffset(AudioChannelPosition channel)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioformat.html#channelOffset

    Parameters
    ----------

    channel : AudioChannelPosition
      Passed on as its number.
    """
    #  int QAudioFormat::channelOffset(AudioChannelPosition channel) const
    return self.uglySide.call(
        'ritual_ZNK12QAudioFormat13channelOffsetENS_20AudioChannelPositionE',
        channel.value,
    )

  def sampleFormat(self) -> SampleFormat:
    """
    Calls Qt's 'SampleFormat QAudioFormat::sampleFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioformat.html#sampleFormat

    Returns
    -------

    SampleFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SampleFormat(number)'
      gives.
    """
    #  SampleFormat QAudioFormat::sampleFormat() const
    return QAudioFormat.SampleFormat(self.uglySide.call(
        'ritual_ZNK12QAudioFormat12sampleFormatEv',
    ))

  @overload(int)
  def bytesForDuration(self, microseconds: int) -> int:
    """
    Calls Qt's 'qint32 QAudioFormat::bytesForDuration(qint64 microseconds)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioformat.html#bytesForDuration

    Parameters
    ----------

    microseconds : int
      Passed on as it is.
    """
    #  qint32 QAudioFormat::bytesForDuration(qint64 microseconds) const
    return self.uglySide.call(
        'ritual_ZNK12QAudioFormat16bytesForDurationEx', microseconds,
    )

  @overload(int)
  def durationForBytes(self, byteCount: int) -> int:
    """
    Calls Qt's 'qint64 QAudioFormat::durationForBytes(qint32 byteCount)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioformat.html#durationForBytes

    Parameters
    ----------

    byteCount : int
      Passed on as it is.
    """
    #  qint64 QAudioFormat::durationForBytes(qint32 byteCount) const
    return self.uglySide.call(
        'ritual_ZNK12QAudioFormat16durationForBytesEi', byteCount,
    )

  @overload(int)
  def bytesForFrames(self, frameCount: int) -> int:
    """
    Calls Qt's 'qint32 QAudioFormat::bytesForFrames(qint32 frameCount)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioformat.html#bytesForFrames

    Parameters
    ----------

    frameCount : int
      Passed on as it is.
    """
    #  qint32 QAudioFormat::bytesForFrames(qint32 frameCount) const
    return self.uglySide.call(
        'ritual_ZNK12QAudioFormat14bytesForFramesEi', frameCount,
    )

  @overload(int)
  def framesForBytes(self, byteCount: int) -> int:
    """
    Calls Qt's 'qint32 QAudioFormat::framesForBytes(qint32 byteCount) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioformat.html#framesForBytes

    Parameters
    ----------

    byteCount : int
      Passed on as it is.
    """
    #  qint32 QAudioFormat::framesForBytes(qint32 byteCount) const
    return self.uglySide.call(
        'ritual_ZNK12QAudioFormat14framesForBytesEi', byteCount,
    )

  @overload(int)
  def framesForDuration(self, microseconds: int) -> int:
    """
    Calls Qt's 'qint32 QAudioFormat::framesForDuration(qint64 microseconds)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudioformat.html#framesForDuration

    Parameters
    ----------

    microseconds : int
      Passed on as it is.
    """
    #  qint32 QAudioFormat::framesForDuration(qint64 microseconds) const
    return self.uglySide.call(
        'ritual_ZNK12QAudioFormat17framesForDurationEx', microseconds,
    )

  @overload(int)
  def durationForFrames(self, frameCount: int) -> int:
    """
    Calls Qt's 'qint64 QAudioFormat::durationForFrames(qint32 frameCount)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudioformat.html#durationForFrames

    Parameters
    ----------

    frameCount : int
      Passed on as it is.
    """
    #  qint64 QAudioFormat::durationForFrames(qint32 frameCount) const
    return self.uglySide.call(
        'ritual_ZNK12QAudioFormat17durationForFramesEi', frameCount,
    )

  def bytesPerFrame(self) -> int:
    """
    Calls Qt's 'int QAudioFormat::bytesPerFrame() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioformat.html#bytesPerFrame
    """
    #  int QAudioFormat::bytesPerFrame() const
    return self.uglySide.call('ritual_ZNK12QAudioFormat13bytesPerFrameEv')

  def bytesPerSample(self) -> int:
    """
    Calls Qt's 'int QAudioFormat::bytesPerSample() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioformat.html#bytesPerSample
    """
    #  int QAudioFormat::bytesPerSample() const
    return self.uglySide.call('ritual_ZNK12QAudioFormat14bytesPerSampleEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setSampleRate(self, sampleRate: int) -> None:
    """
    Calls Qt's 'void QAudioFormat::setSampleRate(int sampleRate)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioformat.html#setSampleRate

    Parameters
    ----------

    sampleRate : int
      Passed on as it is.
    """
    #  void QAudioFormat::setSampleRate(int sampleRate)
    self.uglySide.call(
        'ritual_ZN12QAudioFormat13setSampleRateEi', sampleRate,
    )

  @overload(ChannelConfig)
  def setChannelConfig(self, config: ChannelConfig) -> None:
    """
    Calls Qt's 'void QAudioFormat::setChannelConfig(ChannelConfig config)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioformat.html#setChannelConfig

    Parameters
    ----------

    config : ChannelConfig
      Passed on as its number.
    """
    #  void QAudioFormat::setChannelConfig(ChannelConfig config)
    self.uglySide.call(
        'ritual_ZN12QAudioFormat16setChannelConfigENS_13ChannelConfigE',
        config.value,
    )

  @overload(int)
  def setChannelCount(self, channelCount: int) -> None:
    """
    Calls Qt's 'void QAudioFormat::setChannelCount(int channelCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioformat.html#setChannelCount

    Parameters
    ----------

    channelCount : int
      Passed on as it is.
    """
    #  void QAudioFormat::setChannelCount(int channelCount)
    self.uglySide.call(
        'ritual_ZN12QAudioFormat15setChannelCountEi', channelCount,
    )

  @overload(SampleFormat)
  def setSampleFormat(self, f: SampleFormat) -> None:
    """
    Calls Qt's 'void QAudioFormat::setSampleFormat(SampleFormat f)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioformat.html#setSampleFormat

    Parameters
    ----------

    f : SampleFormat
      Passed on as its number.
    """
    #  void QAudioFormat::setSampleFormat(SampleFormat f)
    self.uglySide.call(
        'ritual_ZN12QAudioFormat15setSampleFormatENS_12SampleFormatE',
        f.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, b: QAudioFormat) -> bool:
    """
    Calls Qt's 'bool operator==(const QAudioFormat &a, const QAudioFormat
    &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioformat.html#operator==

    Parameters
    ----------

    b : QAudioFormat
      Passed on as a value: Qt reads the C++ QAudioFormat, which stays
      Python's own.
    """
    #  bool operator==(const QAudioFormat &a, const QAudioFormat &b)
    return Rituals.call(
        'ritual_ZeqRK12QAudioFormatS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
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
  def __ne__(self, b: QAudioFormat) -> bool:
    """
    Calls Qt's 'bool operator!=(const QAudioFormat &a, const QAudioFormat
    &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioformat.html#operator!=

    Parameters
    ----------

    b : QAudioFormat
      Passed on as a value: Qt reads the C++ QAudioFormat, which stays
      Python's own.
    """
    #  bool operator!=(const QAudioFormat &a, const QAudioFormat &b)
    return Rituals.call(
        'ritual_ZneRK12QAudioFormatS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
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

  @staticmethod
  def normalizedSampleValue(*__, **_) -> Never:
    """
    Qt's 'float QAudioFormat::normalizedSampleValue(const void *sample)
    const': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QAudioFormat.normalizedSampleValue' has no cute function yet. "
        "Qt's 'float QAudioFormat::normalizedSampleValue(const void "
        "*sample) const': names 'void', which has no cute class yet.")
