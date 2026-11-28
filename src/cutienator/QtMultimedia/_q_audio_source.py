"""
QAudioSource binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/qaudiosource.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QAudio

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QIODevice, QMetaObject
  from . import QAudioDevice, QAudioFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioDevice = WAIT['QAudioDevice']
  QAudioFormat = WAIT['QAudioFormat']
  QIODevice = WAIT['QIODevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAudioSource(QObject):
  """
  The cute side of Qt's QAudioSource: a plain Python object standing in front
  of one C++ QAudioSource.

  It is built on the cute 'QObject', as Qt's QAudioSource is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAudioSource that has a ritual and that Python can
  call so far, 24 names in all: 'metaObject', 'tr', 'isNull', 'format',
  'start', 'stop', 'reset', 'suspend', 'resume', 'setBufferSize',
  'bufferSize', 'setBufferFrameCount', 'bufferFrameCount',
  'setNativePeriodFrameCount', 'nativePeriodFrameCount', 'bytesAvailable',
  'framesAvailable', 'setVolume', 'volume', 'processedUSecs', 'elapsedUSecs',
  'error', 'state', 'stateChanged'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAudioSource::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QAudioSource::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QAudioSource::~QAudioSource()': the destructor: Python never
    removes a C++ QAudioSource.
  - Qt's 'void QAudioSource::startABIImpl(QtAudioPrivate::AudioSourceCallback
    &&a0)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  6 of the 37 functions Qt declares: 2 not a gap; 2 a template; 2 forbidden.

  What to expect
  --------------

  - The C++ QAudioSource is created at the first use, not by
    'QAudioSource(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAudioSource.
  - Qt tells when it has removed the C++ QAudioSource. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QAudioSource that has no cute function yet,
    'startABIImpl', 'startImpl', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

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
    Calls Qt's 'QString QAudioSource::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosource.html#tr

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
    #  QString QAudioSource::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QAudioSource2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAudioSource'

  #  A C++ QAudioSource Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAudioSource'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAudioSource::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosource.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAudioSource::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QAudioSource10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QAudioSource::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosource.html#isNull
    """
    #  bool QAudioSource::isNull() const
    return self.uglySide.call('ritual_ZNK12QAudioSource6isNullEv')

  def format(self) -> QAudioFormat:
    """
    Calls Qt's 'QAudioFormat QAudioSource::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosource.html#format

    Returns
    -------

    QAudioFormat
      A new cute QAudioFormat around the copy Qt gave back. Python owns it.
    """
    #  QAudioFormat QAudioSource::format() const
    address = self.uglySide.call('ritual_ZNK12QAudioSource6formatEv')
    from . import QAudioFormat
    return QAudioFormat._cuteOwning(address)

  def bufferSize(self) -> int:
    """
    Calls Qt's 'qsizetype QAudioSource::bufferSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosource.html#bufferSize
    """
    #  qsizetype QAudioSource::bufferSize() const
    return self.uglySide.call('ritual_ZNK12QAudioSource10bufferSizeEv')

  def bufferFrameCount(self) -> int:
    """
    Calls Qt's 'qsizetype QAudioSource::bufferFrameCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosource.html#bufferFrameCount
    """
    #  qsizetype QAudioSource::bufferFrameCount() const
    return self.uglySide.call('ritual_ZNK12QAudioSource16bufferFrameCountEv')

  def nativePeriodFrameCount(self) -> int:
    """
    Calls Qt's 'qsizetype QAudioSource::nativePeriodFrameCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudiosource.html#nativePeriodFrameCount
    """
    #  qsizetype QAudioSource::nativePeriodFrameCount() const
    return self.uglySide.call(
        'ritual_ZNK12QAudioSource22nativePeriodFrameCountEv',
    )

  def bytesAvailable(self) -> int:
    """
    Calls Qt's 'qsizetype QAudioSource::bytesAvailable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosource.html#bytesAvailable
    """
    #  qsizetype QAudioSource::bytesAvailable() const
    return self.uglySide.call('ritual_ZNK12QAudioSource14bytesAvailableEv')

  def framesAvailable(self) -> int:
    """
    Calls Qt's 'qsizetype QAudioSource::framesAvailable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosource.html#framesAvailable
    """
    #  qsizetype QAudioSource::framesAvailable() const
    return self.uglySide.call('ritual_ZNK12QAudioSource15framesAvailableEv')

  def volume(self) -> float:
    """
    Calls Qt's 'qreal QAudioSource::volume() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosource.html#volume
    """
    #  qreal QAudioSource::volume() const
    return self.uglySide.call('ritual_ZNK12QAudioSource6volumeEv')

  def processedUSecs(self) -> int:
    """
    Calls Qt's 'qint64 QAudioSource::processedUSecs() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosource.html#processedUSecs
    """
    #  qint64 QAudioSource::processedUSecs() const
    return self.uglySide.call('ritual_ZNK12QAudioSource14processedUSecsEv')

  def elapsedUSecs(self) -> int:
    """
    Calls Qt's 'qint64 QAudioSource::elapsedUSecs() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosource.html#elapsedUSecs
    """
    #  qint64 QAudioSource::elapsedUSecs() const
    return self.uglySide.call('ritual_ZNK12QAudioSource12elapsedUSecsEv')

  def error(self) -> QAudio.Error:
    """
    Calls Qt's 'QtAudio::Error QAudioSource::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosource.html#error

    Returns
    -------

    QAudio.Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAudio.Error(number)'
      gives.
    """
    #  QtAudio::Error QAudioSource::error() const
    return QAudio.Error(self.uglySide.call(
        'ritual_ZNK12QAudioSource5errorEv',
    ))

  def state(self) -> QAudio.State:
    """
    Calls Qt's 'QtAudio::State QAudioSource::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosource.html#state

    Returns
    -------

    QAudio.State
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAudio.State(number)'
      gives.
    """
    #  QtAudio::State QAudioSource::state() const
    return QAudio.State(self.uglySide.call(
        'ritual_ZNK12QAudioSource5stateEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setBufferSize(self, bytes: int) -> None:
    """
    Calls Qt's 'void QAudioSource::setBufferSize(qsizetype bytes)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosource.html#setBufferSize

    Parameters
    ----------

    bytes : int
      Passed on as it is.
    """
    #  void QAudioSource::setBufferSize(qsizetype bytes)
    self.uglySide.call('ritual_ZN12QAudioSource13setBufferSizeEx', bytes)

  @overload(int)
  def setBufferFrameCount(self, frames: int) -> None:
    """
    Calls Qt's 'void QAudioSource::setBufferFrameCount(qsizetype frames)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudiosource.html#setBufferFrameCount

    Parameters
    ----------

    frames : int
      Passed on as it is.
    """
    #  void QAudioSource::setBufferFrameCount(qsizetype frames)
    self.uglySide.call(
        'ritual_ZN12QAudioSource19setBufferFrameCountEx', frames,
    )

  @overload(int)
  def setNativePeriodFrameCount(self, frameCount: int) -> None:
    """
    Calls Qt's 'void QAudioSource::setNativePeriodFrameCount(qsizetype
    frameCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudiosource.html#setNativePeriodFrameCount

    Parameters
    ----------

    frameCount : int
      Passed on as it is.
    """
    #  void QAudioSource::setNativePeriodFrameCount(qsizetype frameCount)
    self.uglySide.call(
        'ritual_ZN12QAudioSource25setNativePeriodFrameCountEx', frameCount,
    )

  @overload(float)
  def setVolume(self, volume: float) -> None:
    """
    Calls Qt's 'void QAudioSource::setVolume(qreal volume)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosource.html#setVolume

    Parameters
    ----------

    volume : float
      Passed on as it is.
    """
    #  void QAudioSource::setVolume(qreal volume)
    self.uglySide.call('ritual_ZN12QAudioSource9setVolumeEd', volume)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAudioFormat)
  @overload(QAudioFormat, QObject)
  @overload(QAudioFormat, NoneType)
  def __init__(
      self,
      format: QAudioFormat,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QAudioSource::QAudioSource(const
    QAudioFormat &format, QObject *parent)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosource.html#QAudioSource

    Parameters
    ----------

    format : QAudioFormat
      Passed on as a value: Qt reads the C++ QAudioFormat, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAudioSource::QAudioSource(const QAudioFormat &format, QObject
    #      *parent)
    self._noteCreation(QAudioSource, lambda: Rituals.call(
        'ritual_ZN12QAudioSourceC1ERK12QAudioFormatP7QObject',
        self._valueOf(format), self._addressOf(parent, 'QObject'),
    ))

  @overload(QAudioDevice, QAudioFormat)
  @overload(QAudioDevice, QAudioFormat, QObject)
  @overload(QAudioDevice, QAudioFormat, NoneType)
  def __init__(
      self,
      audioDeviceInfo: QAudioDevice,
      format: QAudioFormat,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QAudioSource::QAudioSource(const
    QAudioDevice &audioDeviceInfo, const QAudioFormat &format, QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosource.html#QAudioSource

    Parameters
    ----------

    audioDeviceInfo : QAudioDevice
      Passed on as a value: Qt reads the C++ QAudioDevice, which stays
      Python's own.

    format : QAudioFormat
      Passed on as a value: Qt reads the C++ QAudioFormat, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAudioSource::QAudioSource(const QAudioDevice &audioDeviceInfo, const
    #      QAudioFormat &format, QObject *parent)
    self._noteCreation(QAudioSource, lambda: Rituals.call(
        'ritual_ZN12QAudioSourceC1ERK12QAudioDeviceRK12QAudioFormatP7QObjec'
        't',
        self._valueOf(audioDeviceInfo), self._valueOf(format),
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

  @overload(QIODevice)
  @overload(NoneType)
  def start(self, device: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void QAudioSource::start(QIODevice *device)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosource.html#start

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAudioSource::start(QIODevice *device)
    self.uglySide.call(
        'ritual_ZN12QAudioSource5startEP9QIODevice', self._addressOf(device),
    )

  @overload()
  def start(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QAudioSource::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosource.html#start

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QAudioSource::start()
    address = self.uglySide.call('ritual_ZN12QAudioSource5startEv')
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  def stop(self) -> None:
    """
    Calls Qt's 'void QAudioSource::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosource.html#stop
    """
    #  void QAudioSource::stop()
    self.uglySide.call('ritual_ZN12QAudioSource4stopEv')

  def reset(self) -> None:
    """
    Calls Qt's 'void QAudioSource::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosource.html#reset
    """
    #  void QAudioSource::reset()
    self.uglySide.call('ritual_ZN12QAudioSource5resetEv')

  def suspend(self) -> None:
    """
    Calls Qt's 'void QAudioSource::suspend()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosource.html#suspend
    """
    #  void QAudioSource::suspend()
    self.uglySide.call('ritual_ZN12QAudioSource7suspendEv')

  def resume(self) -> None:
    """
    Calls Qt's 'void QAudioSource::resume()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosource.html#resume
    """
    #  void QAudioSource::resume()
    self.uglySide.call('ritual_ZN12QAudioSource6resumeEv')

  @overload(QAudio.State)
  def stateChanged(self, state: QAudio.State) -> None:
    """
    Calls Qt's 'void QAudioSource::stateChanged(QAudio::State state)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosource.html#stateChanged

    Parameters
    ----------

    state : QAudio.State
      Passed on as its number.
    """
    #  void QAudioSource::stateChanged(QAudio::State state)
    self.uglySide.call(
        'ritual_ZN12QAudioSource12stateChangedEN6QAudio5StateE', state.value,
    )

  @staticmethod
  def startABIImpl(*__, **_) -> Never:
    """
    Qt's 'void QAudioSource::startABIImpl(QtAudioPrivate::AudioSourceCallback
    &&a0)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAudioSource.startABIImpl' has no cute function yet. Qt's 'void "
        "QAudioSource::startABIImpl(QtAudioPrivate::AudioSourceCallback "
        "&&a0)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def startImpl(*__, **_) -> Never:
    """
    Qt's 'QAudioSource::startImpl': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QAudioSource.startImpl' has no cute function yet. Qt's "
        "'QAudioSource::startImpl': a template: a pattern and no single "
        "function.")
