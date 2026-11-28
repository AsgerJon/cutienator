"""
QMediaFormat binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/qmediaformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QMimeType


class QMediaFormat(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMediaFormat: a plain Python object standing in front
  of one C++ QMediaFormat.

  C++ hands a QMediaFormat around as a copy, so every C++ QMediaFormat behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMediaFormat that has a ritual and that Python can
  call so far, 17 names in all: 'fileFormat', 'setFileFormat',
  'setVideoCodec', 'videoCodec', 'setAudioCodec', 'audioCodec',
  'isSupported', 'mimeType', 'fileFormatName', 'audioCodecName',
  'videoCodecName', 'fileFormatDescription', 'audioCodecDescription',
  'videoCodecDescription', '__eq__', '__ne__', 'resolveForEncoding'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMediaFormat::~QMediaFormat()': the destructor: Python removes its
    C++ QMediaFormat by it, and has no other use for it.
  - Qt's 'QMediaFormat &QMediaFormat::operator=(const QMediaFormat &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QMediaFormat::QMediaFormat(QMediaFormat &&other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QMediaFormat &QMediaFormat::operator=(QMediaFormat &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QMediaFormat::swap(QMediaFormat &other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QList<FileFormat> QMediaFormat::supportedFileFormats(ConversionMode
    m)': gives a type Python has no way to take yet.
  - Qt's 'QList<VideoCodec> QMediaFormat::supportedVideoCodecs(ConversionMode
    m)': gives a type Python has no way to take yet.
  - Qt's 'QList<AudioCodec> QMediaFormat::supportedAudioCodecs(ConversionMode
    m)': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  3 of the 30 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QMediaFormat is created at the first use, not by
    'QMediaFormat(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMediaFormat back gives a copy the ritual made for
    Python, in a new cute QMediaFormat.
  - Each name of Qt's QMediaFormat that has no cute function yet,
    'supportedAudioCodecs', 'supportedFileFormats', 'supportedVideoCodecs',
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QMediaFormat, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class AudioCodec(CuteNum, scoped=True):
    """
    The enum 'QMediaFormat::AudioCodec' of Qt, with the 13 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Unspecified = Kee[int](-1)
    MP3 = Kee[int](0)
    AAC = Kee[int](1)
    AC3 = Kee[int](2)
    EAC3 = Kee[int](3)
    FLAC = Kee[int](4)
    DolbyTrueHD = Kee[int](5)
    Opus = Kee[int](6)
    Vorbis = Kee[int](7)
    Wave = Kee[int](8)
    WMA = Kee[int](9)
    ALAC = Kee[int](10)
    LastAudioCodec = Kee[int](10)

  class ConversionMode(CuteNum):
    """
    The enum 'QMediaFormat::ConversionMode' of Qt, with the 2 names Qt gives
    in it.
    """

    Encode = Kee[int](0)
    Decode = Kee[int](1)

  class FileFormat(CuteNum):
    """
    The enum 'QMediaFormat::FileFormat' of Qt, with the 15 names Qt gives in
    it.
    """

    UnspecifiedFormat = Kee[int](-1)
    WMV = Kee[int](0)
    AVI = Kee[int](1)
    Matroska = Kee[int](2)
    MPEG4 = Kee[int](3)
    Ogg = Kee[int](4)
    QuickTime = Kee[int](5)
    WebM = Kee[int](6)
    Mpeg4Audio = Kee[int](7)
    AAC = Kee[int](8)
    WMA = Kee[int](9)
    MP3 = Kee[int](10)
    FLAC = Kee[int](11)
    Wave = Kee[int](12)
    LastFileFormat = Kee[int](12)

  class ResolveFlags(CuteNum):
    """
    The enum 'QMediaFormat::ResolveFlags' of Qt, with the 2 names Qt gives in
    it.
    """

    NoFlags = Kee[int](0)
    RequiresVideo = Kee[int](1)

  class VideoCodec(CuteNum, scoped=True):
    """
    The enum 'QMediaFormat::VideoCodec' of Qt, with the 13 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Unspecified = Kee[int](-1)
    MPEG1 = Kee[int](0)
    MPEG2 = Kee[int](1)
    MPEG4 = Kee[int](2)
    H264 = Kee[int](3)
    H265 = Kee[int](4)
    VP8 = Kee[int](5)
    VP9 = Kee[int](6)
    AV1 = Kee[int](7)
    Theora = Kee[int](8)
    WMV = Kee[int](9)
    MotionJPEG = Kee[int](10)
    LastVideoCodec = Kee[int](10)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(FileFormat)
  def fileFormatName(fileFormat: FileFormat) -> str:
    """
    Calls Qt's 'QString QMediaFormat::fileFormatName(FileFormat fileFormat)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaformat.html#fileFormatName

    Parameters
    ----------

    fileFormat : FileFormat
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMediaFormat::fileFormatName(FileFormat fileFormat)
    return Rituals.call(
        'ritual_ZN12QMediaFormat14fileFormatNameENS_10FileFormatE',
        fileFormat.value,
    )

  @staticmethod
  @overload(AudioCodec)
  def audioCodecName(codec: AudioCodec) -> str:
    """
    Calls Qt's 'QString QMediaFormat::audioCodecName(AudioCodec codec)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaformat.html#audioCodecName

    Parameters
    ----------

    codec : AudioCodec
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMediaFormat::audioCodecName(AudioCodec codec)
    return Rituals.call(
        'ritual_ZN12QMediaFormat14audioCodecNameENS_10AudioCodecE',
        codec.value,
    )

  @staticmethod
  @overload(VideoCodec)
  def videoCodecName(codec: VideoCodec) -> str:
    """
    Calls Qt's 'QString QMediaFormat::videoCodecName(VideoCodec codec)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaformat.html#videoCodecName

    Parameters
    ----------

    codec : VideoCodec
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMediaFormat::videoCodecName(VideoCodec codec)
    return Rituals.call(
        'ritual_ZN12QMediaFormat14videoCodecNameENS_10VideoCodecE',
        codec.value,
    )

  @staticmethod
  @overload(FileFormat)
  def fileFormatDescription(fileFormat: FileFormat) -> str:
    """
    Calls Qt's 'QString
    QMediaFormat::fileFormatDescription(QMediaFormat::FileFormat
    fileFormat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaformat.html#fileFormatDescription

    Parameters
    ----------

    fileFormat : FileFormat
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMediaFormat::fileFormatDescription(QMediaFormat::FileFormat
    #      fileFormat)
    return Rituals.call(
        'ritual_ZN12QMediaFormat21fileFormatDescriptionENS_10FileFormatE',
        fileFormat.value,
    )

  @staticmethod
  @overload(AudioCodec)
  def audioCodecDescription(codec: AudioCodec) -> str:
    """
    Calls Qt's 'QString
    QMediaFormat::audioCodecDescription(QMediaFormat::AudioCodec codec)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaformat.html#audioCodecDescription

    Parameters
    ----------

    codec : AudioCodec
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMediaFormat::audioCodecDescription(QMediaFormat::AudioCodec
    #      codec)
    return Rituals.call(
        'ritual_ZN12QMediaFormat21audioCodecDescriptionENS_10AudioCodecE',
        codec.value,
    )

  @staticmethod
  @overload(VideoCodec)
  def videoCodecDescription(codec: VideoCodec) -> str:
    """
    Calls Qt's 'QString
    QMediaFormat::videoCodecDescription(QMediaFormat::VideoCodec codec)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaformat.html#videoCodecDescription

    Parameters
    ----------

    codec : VideoCodec
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMediaFormat::videoCodecDescription(QMediaFormat::VideoCodec
    #      codec)
    return Rituals.call(
        'ritual_ZN12QMediaFormat21videoCodecDescriptionENS_10VideoCodecE',
        codec.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMediaFormat'

  #  Qt's '~QMediaFormat()'. Naming it makes this a value class: Python owns
  #  every C++ QMediaFormat behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QMediaFormatD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def fileFormat(self) -> FileFormat:
    """
    Calls Qt's 'FileFormat QMediaFormat::fileFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaformat.html#fileFormat

    Returns
    -------

    FileFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FileFormat(number)'
      gives.
    """
    #  FileFormat QMediaFormat::fileFormat() const
    return QMediaFormat.FileFormat(self.uglySide.call(
        'ritual_ZNK12QMediaFormat10fileFormatEv',
    ))

  def videoCodec(self) -> VideoCodec:
    """
    Calls Qt's 'VideoCodec QMediaFormat::videoCodec() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaformat.html#videoCodec

    Returns
    -------

    VideoCodec
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'VideoCodec(number)'
      gives.
    """
    #  VideoCodec QMediaFormat::videoCodec() const
    return QMediaFormat.VideoCodec(self.uglySide.call(
        'ritual_ZNK12QMediaFormat10videoCodecEv',
    ))

  def audioCodec(self) -> AudioCodec:
    """
    Calls Qt's 'AudioCodec QMediaFormat::audioCodec() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaformat.html#audioCodec

    Returns
    -------

    AudioCodec
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'AudioCodec(number)'
      gives.
    """
    #  AudioCodec QMediaFormat::audioCodec() const
    return QMediaFormat.AudioCodec(self.uglySide.call(
        'ritual_ZNK12QMediaFormat10audioCodecEv',
    ))

  @overload(ConversionMode)
  def isSupported(self, mode: ConversionMode) -> bool:
    """
    Calls Qt's 'bool QMediaFormat::isSupported(ConversionMode mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaformat.html#isSupported

    Parameters
    ----------

    mode : ConversionMode
      Passed on as its number.
    """
    #  bool QMediaFormat::isSupported(ConversionMode mode) const
    return self.uglySide.call(
        'ritual_ZNK12QMediaFormat11isSupportedENS_14ConversionModeE',
        mode.value,
    )

  def mimeType(self) -> QMimeType:
    """
    Calls Qt's 'QMimeType QMediaFormat::mimeType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaformat.html#mimeType

    Returns
    -------

    QMimeType
      A new cute QMimeType around the copy Qt gave back. Python owns it.
    """
    #  QMimeType QMediaFormat::mimeType() const
    address = self.uglySide.call('ritual_ZNK12QMediaFormat8mimeTypeEv')
    from ..QtCore import QMimeType
    return QMimeType._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(FileFormat)
  def setFileFormat(self, f: FileFormat) -> None:
    """
    Calls Qt's 'void QMediaFormat::setFileFormat(FileFormat f)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaformat.html#setFileFormat

    Parameters
    ----------

    f : FileFormat
      Passed on as its number.
    """
    #  void QMediaFormat::setFileFormat(FileFormat f)
    self.uglySide.call(
        'ritual_ZN12QMediaFormat13setFileFormatENS_10FileFormatE', f.value,
    )

  @overload(VideoCodec)
  def setVideoCodec(self, codec: VideoCodec) -> None:
    """
    Calls Qt's 'void QMediaFormat::setVideoCodec(VideoCodec codec)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaformat.html#setVideoCodec

    Parameters
    ----------

    codec : VideoCodec
      Passed on as its number.
    """
    #  void QMediaFormat::setVideoCodec(VideoCodec codec)
    self.uglySide.call(
        'ritual_ZN12QMediaFormat13setVideoCodecENS_10VideoCodecE',
        codec.value,
    )

  @overload(AudioCodec)
  def setAudioCodec(self, codec: AudioCodec) -> None:
    """
    Calls Qt's 'void QMediaFormat::setAudioCodec(AudioCodec codec)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaformat.html#setAudioCodec

    Parameters
    ----------

    codec : AudioCodec
      Passed on as its number.
    """
    #  void QMediaFormat::setAudioCodec(AudioCodec codec)
    self.uglySide.call(
        'ritual_ZN12QMediaFormat13setAudioCodecENS_10AudioCodecE',
        codec.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QMediaFormat) -> bool:
    """
    Calls Qt's 'bool QMediaFormat::operator==(const QMediaFormat &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaformat.html#operator==

    Parameters
    ----------

    other : QMediaFormat
      Passed on as a value: Qt reads the C++ QMediaFormat, which stays
      Python's own.
    """
    #  bool QMediaFormat::operator==(const QMediaFormat &other) const
    return self.uglySide.call(
        'ritual_ZNK12QMediaFormateqERKS_', self._valueOf(other),
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
  def __ne__(self, other: QMediaFormat) -> bool:
    """
    Calls Qt's 'bool QMediaFormat::operator!=(const QMediaFormat &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaformat.html#operator!=

    Parameters
    ----------

    other : QMediaFormat
      Passed on as a value: Qt reads the C++ QMediaFormat, which stays
      Python's own.
    """
    #  bool QMediaFormat::operator!=(const QMediaFormat &other) const
    return self.uglySide.call(
        'ritual_ZNK12QMediaFormatneERKS_', self._valueOf(other),
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

  @overload()
  @overload(FileFormat)
  def __init__(
      self,
      format: FileFormat = FileFormat.UnspecifiedFormat,
  ) -> None:
    """
    Notes what was given, for Qt's 'QMediaFormat::QMediaFormat(FileFormat
    format)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmediaformat.html#QMediaFormat

    Parameters
    ----------

    format : FileFormat
      Passed on as its number. May be left out, as in Qt: it is then
      FileFormat.UnspecifiedFormat.
    """
    #  QMediaFormat::QMediaFormat(FileFormat format)
    self._noteCreation(QMediaFormat, lambda: Rituals.call(
        'ritual_ZN12QMediaFormatC1ENS_10FileFormatE', format.value,
    ))

  @overload(THIS)
  def __init__(self, other: QMediaFormat) -> None:
    """
    Notes what was given, for Qt's 'QMediaFormat::QMediaFormat(const
    QMediaFormat &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmediaformat.html#QMediaFormat

    Parameters
    ----------

    other : QMediaFormat
      Passed on as a value: Qt reads the C++ QMediaFormat, which stays
      Python's own.
    """
    #  QMediaFormat::QMediaFormat(const QMediaFormat &other)
    self._noteCreation(QMediaFormat, lambda: Rituals.call(
        'ritual_ZN12QMediaFormatC1ERKS_', self._valueOf(other),
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

  @overload(ResolveFlags)
  def resolveForEncoding(self, flags: ResolveFlags) -> None:
    """
    Calls Qt's 'void QMediaFormat::resolveForEncoding(ResolveFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaformat.html#resolveForEncoding

    Parameters
    ----------

    flags : ResolveFlags
      Passed on as its number.
    """
    #  void QMediaFormat::resolveForEncoding(ResolveFlags flags)
    self.uglySide.call(
        'ritual_ZN12QMediaFormat18resolveForEncodingENS_12ResolveFlagsE',
        flags.value,
    )

  @staticmethod
  def supportedAudioCodecs(*__, **_) -> Never:
    """
    Qt's 'QList<AudioCodec> QMediaFormat::supportedAudioCodecs(ConversionMode
    m)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QMediaFormat.supportedAudioCodecs' has no cute function yet. Qt's "
        "'QList<AudioCodec> "
        "QMediaFormat::supportedAudioCodecs(ConversionMode m)': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def supportedFileFormats(*__, **_) -> Never:
    """
    Qt's 'QList<FileFormat> QMediaFormat::supportedFileFormats(ConversionMode
    m)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QMediaFormat.supportedFileFormats' has no cute function yet. Qt's "
        "'QList<FileFormat> "
        "QMediaFormat::supportedFileFormats(ConversionMode m)': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def supportedVideoCodecs(*__, **_) -> Never:
    """
    Qt's 'QList<VideoCodec> QMediaFormat::supportedVideoCodecs(ConversionMode
    m)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QMediaFormat.supportedVideoCodecs' has no cute function yet. Qt's "
        "'QList<VideoCodec> "
        "QMediaFormat::supportedVideoCodecs(ConversionMode m)': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QMediaFormat::swap(QMediaFormat &other)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMediaFormat.swap' has no cute function yet. Qt's 'void "
        "QMediaFormat::swap(QMediaFormat &other)': takes a type Python has "
        "no way to hand over yet.")
