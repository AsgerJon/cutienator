"""
QMediaEncoderSettings binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qplatformmediarecorder_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QMediaEncoderSettings to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QMediaFormat, QMediaRecorder

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QMimeType, QSize
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSize = WAIT['QSize']


class QMediaEncoderSettings(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMediaEncoderSettings: a plain Python object standing
  in front of one C++ QMediaEncoderSettings.

  C++ hands a QMediaEncoderSettings around as a copy, so every C++
  QMediaEncoderSettings behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMediaEncoderSettings that has a ritual and that
  Python can call so far, 26 names in all: 'mediaFormat', 'setMediaFormat',
  'resolveFormat', 'fileFormat', 'videoCodec', 'audioCodec', 'mimeType',
  'preferredSuffix', 'encodingMode', 'setEncodingMode', 'quality',
  'setQuality', 'videoResolution', 'setVideoResolution', 'videoFrameRate',
  'setVideoFrameRate', 'videoBitRate', 'setVideoBitRate', 'audioBitRate',
  'setAudioBitRate', 'audioChannelCount', 'setAudioChannelCount',
  'audioSampleRate', 'setAudioSampleRate', '__eq__', '__ne__'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMediaEncoderSettings::~QMediaEncoderSettings()': the destructor:
    Python removes its C++ QMediaEncoderSettings by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QMediaEncoderSettings is created at the first use, not by
    'QMediaEncoderSettings(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMediaEncoderSettings back gives a copy the ritual
    made for Python, in a new cute QMediaEncoderSettings.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMediaEncoderSettings'

  #  Qt's '~QMediaEncoderSettings()'. Naming it makes this a value class:
  #  Python owns every C++ QMediaEncoderSettings behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QMediaEncoderSettingsD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def mediaFormat(self) -> QMediaFormat:
    """
    Calls Qt's 'QMediaFormat QMediaEncoderSettings::mediaFormat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaencodersettings.html#mediaFormat

    Returns
    -------

    QMediaFormat
      A new cute QMediaFormat around the copy Qt gave back. Python owns it.
    """
    #  QMediaFormat QMediaEncoderSettings::mediaFormat() const
    address = self.uglySide.call(
        'ritual_ZNK21QMediaEncoderSettings11mediaFormatEv',
    )
    return QMediaFormat._cuteOwning(address)

  def fileFormat(self) -> QMediaFormat.FileFormat:
    """
    Calls Qt's 'QMediaFormat::FileFormat QMediaEncoderSettings::fileFormat()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaencodersettings.html#fileFormat

    Returns
    -------

    QMediaFormat.FileFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QMediaFormat.FileFormat(number)' gives.
    """
    #  QMediaFormat::FileFormat QMediaEncoderSettings::fileFormat() const
    return QMediaFormat.FileFormat(self.uglySide.call(
        'ritual_ZNK21QMediaEncoderSettings10fileFormatEv',
    ))

  def videoCodec(self) -> QMediaFormat.VideoCodec:
    """
    Calls Qt's 'QMediaFormat::VideoCodec QMediaEncoderSettings::videoCodec()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaencodersettings.html#videoCodec

    Returns
    -------

    QMediaFormat.VideoCodec
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QMediaFormat.VideoCodec(number)' gives.
    """
    #  QMediaFormat::VideoCodec QMediaEncoderSettings::videoCodec() const
    return QMediaFormat.VideoCodec(self.uglySide.call(
        'ritual_ZNK21QMediaEncoderSettings10videoCodecEv',
    ))

  def audioCodec(self) -> QMediaFormat.AudioCodec:
    """
    Calls Qt's 'QMediaFormat::AudioCodec QMediaEncoderSettings::audioCodec()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaencodersettings.html#audioCodec

    Returns
    -------

    QMediaFormat.AudioCodec
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QMediaFormat.AudioCodec(number)' gives.
    """
    #  QMediaFormat::AudioCodec QMediaEncoderSettings::audioCodec() const
    return QMediaFormat.AudioCodec(self.uglySide.call(
        'ritual_ZNK21QMediaEncoderSettings10audioCodecEv',
    ))

  def mimeType(self) -> QMimeType:
    """
    Calls Qt's 'QMimeType QMediaEncoderSettings::mimeType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaencodersettings.html#mimeType

    Returns
    -------

    QMimeType
      A new cute QMimeType around the copy Qt gave back. Python owns it.
    """
    #  QMimeType QMediaEncoderSettings::mimeType() const
    address = self.uglySide.call(
        'ritual_ZNK21QMediaEncoderSettings8mimeTypeEv',
    )
    from ..QtCore import QMimeType
    return QMimeType._cuteOwning(address)

  def preferredSuffix(self) -> str:
    """
    Calls Qt's 'QString QMediaEncoderSettings::preferredSuffix() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaencodersettings.html#preferredSuffix

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMediaEncoderSettings::preferredSuffix() const
    return self.uglySide.call(
        'ritual_ZNK21QMediaEncoderSettings15preferredSuffixEv',
    )

  def encodingMode(self) -> QMediaRecorder.EncodingMode:
    """
    Calls Qt's 'QMediaRecorder::EncodingMode
    QMediaEncoderSettings::encodingMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaencodersettings.html#encodingMode

    Returns
    -------

    QMediaRecorder.EncodingMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QMediaRecorder.EncodingMode(number)' gives.
    """
    #  QMediaRecorder::EncodingMode QMediaEncoderSettings::encodingMode()
    #      const
    return QMediaRecorder.EncodingMode(self.uglySide.call(
        'ritual_ZNK21QMediaEncoderSettings12encodingModeEv',
    ))

  def quality(self) -> QMediaRecorder.Quality:
    """
    Calls Qt's 'QMediaRecorder::Quality QMediaEncoderSettings::quality()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaencodersettings.html#quality

    Returns
    -------

    QMediaRecorder.Quality
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QMediaRecorder.Quality(number)' gives.
    """
    #  QMediaRecorder::Quality QMediaEncoderSettings::quality() const
    return QMediaRecorder.Quality(self.uglySide.call(
        'ritual_ZNK21QMediaEncoderSettings7qualityEv',
    ))

  def videoResolution(self) -> QSize:
    """
    Calls Qt's 'QSize QMediaEncoderSettings::videoResolution() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaencodersettings.html#videoResolution

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QMediaEncoderSettings::videoResolution() const
    address = self.uglySide.call(
        'ritual_ZNK21QMediaEncoderSettings15videoResolutionEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def videoFrameRate(self) -> float:
    """
    Calls Qt's 'qreal QMediaEncoderSettings::videoFrameRate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaencodersettings.html#videoFrameRate
    """
    #  qreal QMediaEncoderSettings::videoFrameRate() const
    return self.uglySide.call(
        'ritual_ZNK21QMediaEncoderSettings14videoFrameRateEv',
    )

  def videoBitRate(self) -> int:
    """
    Calls Qt's 'int QMediaEncoderSettings::videoBitRate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaencodersettings.html#videoBitRate
    """
    #  int QMediaEncoderSettings::videoBitRate() const
    return self.uglySide.call(
        'ritual_ZNK21QMediaEncoderSettings12videoBitRateEv',
    )

  def audioBitRate(self) -> int:
    """
    Calls Qt's 'int QMediaEncoderSettings::audioBitRate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaencodersettings.html#audioBitRate
    """
    #  int QMediaEncoderSettings::audioBitRate() const
    return self.uglySide.call(
        'ritual_ZNK21QMediaEncoderSettings12audioBitRateEv',
    )

  def audioChannelCount(self) -> int:
    """
    Calls Qt's 'int QMediaEncoderSettings::audioChannelCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaencodersettings.html#audioChannelCount
    """
    #  int QMediaEncoderSettings::audioChannelCount() const
    return self.uglySide.call(
        'ritual_ZNK21QMediaEncoderSettings17audioChannelCountEv',
    )

  def audioSampleRate(self) -> int:
    """
    Calls Qt's 'int QMediaEncoderSettings::audioSampleRate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaencodersettings.html#audioSampleRate
    """
    #  int QMediaEncoderSettings::audioSampleRate() const
    return self.uglySide.call(
        'ritual_ZNK21QMediaEncoderSettings15audioSampleRateEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMediaFormat)
  def setMediaFormat(self, format: QMediaFormat) -> None:
    """
    Calls Qt's 'void QMediaEncoderSettings::setMediaFormat(const QMediaFormat
    &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaencodersettings.html#setMediaFormat

    Parameters
    ----------

    format : QMediaFormat
      Passed on as a value: Qt reads the C++ QMediaFormat, which stays
      Python's own.
    """
    #  void QMediaEncoderSettings::setMediaFormat(const QMediaFormat &format)
    self.uglySide.call(
        'ritual_ZN21QMediaEncoderSettings14setMediaFormatERK12QMediaFormat',
        self._valueOf(format),
    )

  @overload(QMediaRecorder.EncodingMode)
  def setEncodingMode(self, mode: QMediaRecorder.EncodingMode) -> None:
    """
    Calls Qt's 'void
    QMediaEncoderSettings::setEncodingMode(QMediaRecorder::EncodingMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaencodersettings.html#setEncodingMode

    Parameters
    ----------

    mode : QMediaRecorder.EncodingMode
      Passed on as its number.
    """
    #  void QMediaEncoderSettings::setEncodingMode(QMediaRecorder::
    #      EncodingMode mode)
    self.uglySide.call(
        'ritual_ZN21QMediaEncoderSettings15setEncodingModeEN14QMediaRecorde'
        'r12EncodingModeE',
        mode.value,
    )

  @overload(QMediaRecorder.Quality)
  def setQuality(self, quality: QMediaRecorder.Quality) -> None:
    """
    Calls Qt's 'void
    QMediaEncoderSettings::setQuality(QMediaRecorder::Quality quality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaencodersettings.html#setQuality

    Parameters
    ----------

    quality : QMediaRecorder.Quality
      Passed on as its number.
    """
    #  void QMediaEncoderSettings::setQuality(QMediaRecorder::Quality
    #      quality)
    self.uglySide.call(
        'ritual_ZN21QMediaEncoderSettings10setQualityEN14QMediaRecorder7Qua'
        'lityE',
        quality.value,
    )

  @overload(QSize)
  def setVideoResolution(self, size: QSize) -> None:
    """
    Calls Qt's 'void QMediaEncoderSettings::setVideoResolution(const QSize
    &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaencodersettings.html#setVideoResolution

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QMediaEncoderSettings::setVideoResolution(const QSize &size)
    self.uglySide.call(
        'ritual_ZN21QMediaEncoderSettings18setVideoResolutionERK5QSize',
        self._valueOf(size),
    )

  @overload(float)
  def setVideoFrameRate(self, rate: float) -> None:
    """
    Calls Qt's 'void QMediaEncoderSettings::setVideoFrameRate(qreal rate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaencodersettings.html#setVideoFrameRate

    Parameters
    ----------

    rate : float
      Passed on as it is.
    """
    #  void QMediaEncoderSettings::setVideoFrameRate(qreal rate)
    self.uglySide.call(
        'ritual_ZN21QMediaEncoderSettings17setVideoFrameRateEd', rate,
    )

  @overload(int)
  def setVideoBitRate(self, bitrate: int) -> None:
    """
    Calls Qt's 'void QMediaEncoderSettings::setVideoBitRate(int bitrate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaencodersettings.html#setVideoBitRate

    Parameters
    ----------

    bitrate : int
      Passed on as it is.
    """
    #  void QMediaEncoderSettings::setVideoBitRate(int bitrate)
    self.uglySide.call(
        'ritual_ZN21QMediaEncoderSettings15setVideoBitRateEi', bitrate,
    )

  @overload(int)
  def setAudioBitRate(self, bitrate: int) -> None:
    """
    Calls Qt's 'void QMediaEncoderSettings::setAudioBitRate(int bitrate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaencodersettings.html#setAudioBitRate

    Parameters
    ----------

    bitrate : int
      Passed on as it is.
    """
    #  void QMediaEncoderSettings::setAudioBitRate(int bitrate)
    self.uglySide.call(
        'ritual_ZN21QMediaEncoderSettings15setAudioBitRateEi', bitrate,
    )

  @overload(int)
  def setAudioChannelCount(self, channels: int) -> None:
    """
    Calls Qt's 'void QMediaEncoderSettings::setAudioChannelCount(int
    channels)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaencodersettings.html#setAudioChannelCount

    Parameters
    ----------

    channels : int
      Passed on as it is.
    """
    #  void QMediaEncoderSettings::setAudioChannelCount(int channels)
    self.uglySide.call(
        'ritual_ZN21QMediaEncoderSettings20setAudioChannelCountEi', channels,
    )

  @overload(int)
  def setAudioSampleRate(self, rate: int) -> None:
    """
    Calls Qt's 'void QMediaEncoderSettings::setAudioSampleRate(int rate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaencodersettings.html#setAudioSampleRate

    Parameters
    ----------

    rate : int
      Passed on as it is.
    """
    #  void QMediaEncoderSettings::setAudioSampleRate(int rate)
    self.uglySide.call(
        'ritual_ZN21QMediaEncoderSettings18setAudioSampleRateEi', rate,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QMediaEncoderSettings) -> bool:
    """
    Calls Qt's 'bool QMediaEncoderSettings::operator==(const
    QMediaEncoderSettings &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaencodersettings.html#operator==

    Parameters
    ----------

    other : QMediaEncoderSettings
      Passed on as a value: Qt reads the C++ QMediaEncoderSettings, which
      stays Python's own.
    """
    #  bool QMediaEncoderSettings::operator==(const QMediaEncoderSettings
    #      &other) const
    return self.uglySide.call(
        'ritual_ZNK21QMediaEncoderSettingseqERKS_', self._valueOf(other),
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
  def __ne__(self, other: QMediaEncoderSettings) -> bool:
    """
    Calls Qt's 'bool QMediaEncoderSettings::operator!=(const
    QMediaEncoderSettings &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaencodersettings.html#operator!=

    Parameters
    ----------

    other : QMediaEncoderSettings
      Passed on as a value: Qt reads the C++ QMediaEncoderSettings, which
      stays Python's own.
    """
    #  bool QMediaEncoderSettings::operator!=(const QMediaEncoderSettings
    #      &other) const
    return self.uglySide.call(
        'ritual_ZNK21QMediaEncoderSettingsneERKS_', self._valueOf(other),
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

  @overload()
  @overload(QMediaFormat.ResolveFlags)
  def resolveFormat(
      self,
      flags: QMediaFormat.ResolveFlags = QMediaFormat.ResolveFlags.NoFlags,
  ) -> None:
    """
    Calls Qt's 'void
    QMediaEncoderSettings::resolveFormat(QMediaFormat::ResolveFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaencodersettings.html#resolveFormat

    Parameters
    ----------

    flags : QMediaFormat.ResolveFlags
      Passed on as its number. May be left out, as in Qt: it is then
      QMediaFormat.ResolveFlags.NoFlags.
    """
    #  void QMediaEncoderSettings::resolveFormat(QMediaFormat::ResolveFlags
    #      flags)
    self.uglySide.call(
        'ritual_ZN21QMediaEncoderSettings13resolveFormatEN12QMediaFormat12R'
        'esolveFlagsE',
        flags.value,
    )
