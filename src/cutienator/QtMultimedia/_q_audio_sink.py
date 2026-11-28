"""
QAudioSink binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/qaudiosink.h, Qt 6.12.0. Changes made here are lost.
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


class QAudioSink(QObject):
  """
  The cute side of Qt's QAudioSink: a plain Python object standing in front
  of one C++ QAudioSink.

  It is built on the cute 'QObject', as Qt's QAudioSink is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAudioSink that has a ritual and that Python can
  call so far, 24 names in all: 'metaObject', 'tr', 'isNull', 'format',
  'start', 'stop', 'reset', 'suspend', 'resume', 'setBufferSize',
  'bufferSize', 'setBufferFrameCount', 'bufferFrameCount',
  'setNativePeriodFrameCount', 'nativePeriodFrameCount', 'bytesFree',
  'framesFree', 'processedUSecs', 'elapsedUSecs', 'error', 'state',
  'setVolume', 'volume', 'stateChanged'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAudioSink::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QAudioSink::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QAudioSink::~QAudioSink()': the destructor: Python never removes a
    C++ QAudioSink.
  - Qt's 'void QAudioSink::startABIImpl(QtAudioPrivate::AudioSinkCallback
    &&a0)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  6 of the 37 functions Qt declares: 2 not a gap; 2 a template; 2 forbidden.

  What to expect
  --------------

  - The C++ QAudioSink is created at the first use, not by 'QAudioSink(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAudioSink.
  - Qt tells when it has removed the C++ QAudioSink. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QAudioSink that has no cute function yet,
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
    Calls Qt's 'QString QAudioSink::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosink.html#tr

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
    #  QString QAudioSink::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QAudioSink2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAudioSink'

  #  A C++ QAudioSink Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAudioSink'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAudioSink::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosink.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAudioSink::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QAudioSink10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QAudioSink::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosink.html#isNull
    """
    #  bool QAudioSink::isNull() const
    return self.uglySide.call('ritual_ZNK10QAudioSink6isNullEv')

  def format(self) -> QAudioFormat:
    """
    Calls Qt's 'QAudioFormat QAudioSink::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosink.html#format

    Returns
    -------

    QAudioFormat
      A new cute QAudioFormat around the copy Qt gave back. Python owns it.
    """
    #  QAudioFormat QAudioSink::format() const
    address = self.uglySide.call('ritual_ZNK10QAudioSink6formatEv')
    from . import QAudioFormat
    return QAudioFormat._cuteOwning(address)

  def bufferSize(self) -> int:
    """
    Calls Qt's 'qsizetype QAudioSink::bufferSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosink.html#bufferSize
    """
    #  qsizetype QAudioSink::bufferSize() const
    return self.uglySide.call('ritual_ZNK10QAudioSink10bufferSizeEv')

  def bufferFrameCount(self) -> int:
    """
    Calls Qt's 'qsizetype QAudioSink::bufferFrameCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosink.html#bufferFrameCount
    """
    #  qsizetype QAudioSink::bufferFrameCount() const
    return self.uglySide.call('ritual_ZNK10QAudioSink16bufferFrameCountEv')

  def nativePeriodFrameCount(self) -> int:
    """
    Calls Qt's 'qsizetype QAudioSink::nativePeriodFrameCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudiosink.html#nativePeriodFrameCount
    """
    #  qsizetype QAudioSink::nativePeriodFrameCount() const
    return self.uglySide.call(
        'ritual_ZNK10QAudioSink22nativePeriodFrameCountEv',
    )

  def bytesFree(self) -> int:
    """
    Calls Qt's 'qsizetype QAudioSink::bytesFree() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosink.html#bytesFree
    """
    #  qsizetype QAudioSink::bytesFree() const
    return self.uglySide.call('ritual_ZNK10QAudioSink9bytesFreeEv')

  def framesFree(self) -> int:
    """
    Calls Qt's 'qsizetype QAudioSink::framesFree() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosink.html#framesFree
    """
    #  qsizetype QAudioSink::framesFree() const
    return self.uglySide.call('ritual_ZNK10QAudioSink10framesFreeEv')

  def processedUSecs(self) -> int:
    """
    Calls Qt's 'qint64 QAudioSink::processedUSecs() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosink.html#processedUSecs
    """
    #  qint64 QAudioSink::processedUSecs() const
    return self.uglySide.call('ritual_ZNK10QAudioSink14processedUSecsEv')

  def elapsedUSecs(self) -> int:
    """
    Calls Qt's 'qint64 QAudioSink::elapsedUSecs() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosink.html#elapsedUSecs
    """
    #  qint64 QAudioSink::elapsedUSecs() const
    return self.uglySide.call('ritual_ZNK10QAudioSink12elapsedUSecsEv')

  def error(self) -> QAudio.Error:
    """
    Calls Qt's 'QtAudio::Error QAudioSink::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosink.html#error

    Returns
    -------

    QAudio.Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAudio.Error(number)'
      gives.
    """
    #  QtAudio::Error QAudioSink::error() const
    return QAudio.Error(self.uglySide.call('ritual_ZNK10QAudioSink5errorEv'))

  def state(self) -> QAudio.State:
    """
    Calls Qt's 'QtAudio::State QAudioSink::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosink.html#state

    Returns
    -------

    QAudio.State
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAudio.State(number)'
      gives.
    """
    #  QtAudio::State QAudioSink::state() const
    return QAudio.State(self.uglySide.call('ritual_ZNK10QAudioSink5stateEv'))

  def volume(self) -> float:
    """
    Calls Qt's 'qreal QAudioSink::volume() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosink.html#volume
    """
    #  qreal QAudioSink::volume() const
    return self.uglySide.call('ritual_ZNK10QAudioSink6volumeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setBufferSize(self, bytes: int) -> None:
    """
    Calls Qt's 'void QAudioSink::setBufferSize(qsizetype bytes)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosink.html#setBufferSize

    Parameters
    ----------

    bytes : int
      Passed on as it is.
    """
    #  void QAudioSink::setBufferSize(qsizetype bytes)
    self.uglySide.call('ritual_ZN10QAudioSink13setBufferSizeEx', bytes)

  @overload(int)
  def setBufferFrameCount(self, framesCount: int) -> None:
    """
    Calls Qt's 'void QAudioSink::setBufferFrameCount(qsizetype framesCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudiosink.html#setBufferFrameCount

    Parameters
    ----------

    framesCount : int
      Passed on as it is.
    """
    #  void QAudioSink::setBufferFrameCount(qsizetype framesCount)
    self.uglySide.call(
        'ritual_ZN10QAudioSink19setBufferFrameCountEx', framesCount,
    )

  @overload(int)
  def setNativePeriodFrameCount(self, frameCount: int) -> None:
    """
    Calls Qt's 'void QAudioSink::setNativePeriodFrameCount(qsizetype
    frameCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudiosink.html#setNativePeriodFrameCount

    Parameters
    ----------

    frameCount : int
      Passed on as it is.
    """
    #  void QAudioSink::setNativePeriodFrameCount(qsizetype frameCount)
    self.uglySide.call(
        'ritual_ZN10QAudioSink25setNativePeriodFrameCountEx', frameCount,
    )

  @overload(float)
  def setVolume(self, a0: float) -> None:
    """
    Calls Qt's 'void QAudioSink::setVolume(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosink.html#setVolume

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QAudioSink::setVolume(qreal a0)
    self.uglySide.call('ritual_ZN10QAudioSink9setVolumeEd', a0)

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
    Notes what was given, for Qt's 'QAudioSink::QAudioSink(const QAudioFormat
    &format, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosink.html#QAudioSink

    Parameters
    ----------

    format : QAudioFormat
      Passed on as a value: Qt reads the C++ QAudioFormat, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAudioSink::QAudioSink(const QAudioFormat &format, QObject *parent)
    self._noteCreation(QAudioSink, lambda: Rituals.call(
        'ritual_ZN10QAudioSinkC1ERK12QAudioFormatP7QObject',
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
    Notes what was given, for Qt's 'QAudioSink::QAudioSink(const QAudioDevice
    &audioDeviceInfo, const QAudioFormat &format, QObject *parent)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosink.html#QAudioSink

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
    #  QAudioSink::QAudioSink(const QAudioDevice &audioDeviceInfo, const
    #      QAudioFormat &format, QObject *parent)
    self._noteCreation(QAudioSink, lambda: Rituals.call(
        'ritual_ZN10QAudioSinkC1ERK12QAudioDeviceRK12QAudioFormatP7QObject',
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
    Calls Qt's 'void QAudioSink::start(QIODevice *device)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosink.html#start

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAudioSink::start(QIODevice *device)
    self.uglySide.call(
        'ritual_ZN10QAudioSink5startEP9QIODevice', self._addressOf(device),
    )

  @overload()
  def start(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QAudioSink::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosink.html#start

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QAudioSink::start()
    address = self.uglySide.call('ritual_ZN10QAudioSink5startEv')
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  def stop(self) -> None:
    """
    Calls Qt's 'void QAudioSink::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosink.html#stop
    """
    #  void QAudioSink::stop()
    self.uglySide.call('ritual_ZN10QAudioSink4stopEv')

  def reset(self) -> None:
    """
    Calls Qt's 'void QAudioSink::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosink.html#reset
    """
    #  void QAudioSink::reset()
    self.uglySide.call('ritual_ZN10QAudioSink5resetEv')

  def suspend(self) -> None:
    """
    Calls Qt's 'void QAudioSink::suspend()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosink.html#suspend
    """
    #  void QAudioSink::suspend()
    self.uglySide.call('ritual_ZN10QAudioSink7suspendEv')

  def resume(self) -> None:
    """
    Calls Qt's 'void QAudioSink::resume()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosink.html#resume
    """
    #  void QAudioSink::resume()
    self.uglySide.call('ritual_ZN10QAudioSink6resumeEv')

  @overload(QAudio.State)
  def stateChanged(self, state: QAudio.State) -> None:
    """
    Calls Qt's 'void QAudioSink::stateChanged(QAudio::State state)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiosink.html#stateChanged

    Parameters
    ----------

    state : QAudio.State
      Passed on as its number.
    """
    #  void QAudioSink::stateChanged(QAudio::State state)
    self.uglySide.call(
        'ritual_ZN10QAudioSink12stateChangedEN6QAudio5StateE', state.value,
    )

  @staticmethod
  def startABIImpl(*__, **_) -> Never:
    """
    Qt's 'void QAudioSink::startABIImpl(QtAudioPrivate::AudioSinkCallback
    &&a0)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAudioSink.startABIImpl' has no cute function yet. Qt's 'void "
        "QAudioSink::startABIImpl(QtAudioPrivate::AudioSinkCallback &&a0)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def startImpl(*__, **_) -> Never:
    """
    Qt's 'QAudioSink::startImpl': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QAudioSink.startImpl' has no cute function yet. Qt's "
        "'QAudioSink::startImpl': a template: a pattern and no single "
        "function.")
