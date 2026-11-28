"""
QSoundEffectPrivateSynchronous binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qsoundeffectsynchronous_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QSoundEffectPrivateSynchronous to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QIODevice
from . import QAudio, QSoundEffect, QSoundEffectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QAudioDevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioDevice = WAIT['QAudioDevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSoundEffectPrivateSynchronous(QIODevice, QSoundEffectPrivate):
  """
  The cute side of Qt's QSoundEffectPrivateSynchronous: a plain Python object
  standing in front of one C++ QSoundEffectPrivateSynchronous.

  It is built on the cute 'QIODevice', as Qt's QSoundEffectPrivateSynchronous
  is built on Qt's QIODevice, and has everything that class has. It is built
  on the cute 'QSoundEffectPrivate' as well, as Qt's
  QSoundEffectPrivateSynchronous is built on Qt's QSoundEffectPrivate too,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSoundEffectPrivateSynchronous that has a ritual and
  that Python can call so far, 24 names in all: 'writeData', 'size',
  'bytesAvailable', 'isSequential', 'atEnd', 'setLoopsRemaining',
  'setStatus', 'setPlaying', 'updateAudioOutput', 'decoderError',
  'loopCount', 'setLoopCount', 'loopsRemaining', 'volume', 'setVolume',
  'muted', 'setMuted', 'play', 'stop', 'playing', 'setAudioDevice', 'status',
  'audioDevice', 'stateChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSoundEffectPrivateSynchronous::~QSoundEffectPrivateSynchronous()':
    the destructor: Python never removes a C++
    QSoundEffectPrivateSynchronous.
  - Qt's 'qint64 QSoundEffectPrivateSynchronous::readData(char *data, qint64
    len)': names 'char', which has no cute class yet.
  - Qt's 'void QSoundEffectPrivateSynchronous::sampleReady(SharedSamplePtr
    a0)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSoundEffectPrivateSynchronous::setSource(QUrl a0,
    QSampleCache &a1)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSoundEffectPrivateSynchronous is created at the first use, not
    by 'QSoundEffectPrivateSynchronous(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSoundEffectPrivateSynchronous.
  - Qt tells when it has removed the C++ QSoundEffectPrivateSynchronous.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSoundEffectPrivateSynchronous that has no cute
    function yet, 'sampleReady', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSoundEffectPrivateSynchronous'

  #  Qt's QSoundEffectPrivateSynchronous is built on more than one class. The
  #  part of a C++ QSoundEffectPrivateSynchronous that belongs to a class
  #  after the first begins somewhere inside the object, and the ritual named
  #  for that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QSoundEffectPrivate':
          'ritual_cast_QSoundEffectPrivateSynchronous_QSoundEffectPrivate',
  }

  #  A C++ QSoundEffectPrivateSynchronous Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSoundEffectPrivateSynchronous'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def size(self) -> int:
    """
    Calls Qt's 'qint64 QSoundEffectPrivateSynchronous::size() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsoundeffectprivatesynchronous.html#size
    """
    #  qint64 QSoundEffectPrivateSynchronous::size() const
    ritual = 'ritual_ZNK30QSoundEffectPrivateSynchronous4sizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK30QSoundEffectPrivateSynchronous4sizeEv'
    return self.uglySide.call(ritual)

  def bytesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QSoundEffectPrivateSynchronous::bytesAvailable()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsoundeffectprivatesynchronous.html#bytesAvailable
    """
    #  qint64 QSoundEffectPrivateSynchronous::bytesAvailable() const
    ritual = 'ritual_ZNK30QSoundEffectPrivateSynchronous14bytesAvailableEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK30QSoundEffectPrivateSynchronous14bytesAvailableEv')
    return self.uglySide.call(ritual)

  def isSequential(self) -> bool:
    """
    Calls Qt's 'bool QSoundEffectPrivateSynchronous::isSequential() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsoundeffectprivatesynchronous.html#isSequential
    """
    #  bool QSoundEffectPrivateSynchronous::isSequential() const
    ritual = 'ritual_ZNK30QSoundEffectPrivateSynchronous12isSequentialEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK30QSoundEffectPrivateSynchronous12isSequentialEv')
    return self.uglySide.call(ritual)

  def atEnd(self) -> bool:
    """
    Calls Qt's 'bool QSoundEffectPrivateSynchronous::atEnd() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsoundeffectprivatesynchronous.html#atEnd
    """
    #  bool QSoundEffectPrivateSynchronous::atEnd() const
    ritual = 'ritual_ZNK30QSoundEffectPrivateSynchronous5atEndEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK30QSoundEffectPrivateSynchronous5atEndEv'
    return self.uglySide.call(ritual)

  def loopCount(self) -> int:
    """
    Calls Qt's 'int QSoundEffectPrivateSynchronous::loopCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsoundeffectprivatesynchronous.html#loopCount
    """
    #  int QSoundEffectPrivateSynchronous::loopCount() const
    ritual = 'ritual_ZNK30QSoundEffectPrivateSynchronous9loopCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK30QSoundEffectPrivateSynchronous9loopCountEv'
    return self.uglySide.call(ritual)

  def loopsRemaining(self) -> int:
    """
    Calls Qt's 'int QSoundEffectPrivateSynchronous::loopsRemaining() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsoundeffectprivatesynchronous.html#loopsRemaining
    """
    #  int QSoundEffectPrivateSynchronous::loopsRemaining() const
    ritual = 'ritual_ZNK30QSoundEffectPrivateSynchronous14loopsRemainingEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK30QSoundEffectPrivateSynchronous14loopsRemainingEv')
    return self.uglySide.call(ritual)

  def volume(self) -> float:
    """
    Calls Qt's 'float QSoundEffectPrivateSynchronous::volume() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsoundeffectprivatesynchronous.html#volume
    """
    #  float QSoundEffectPrivateSynchronous::volume() const
    ritual = 'ritual_ZNK30QSoundEffectPrivateSynchronous6volumeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK30QSoundEffectPrivateSynchronous6volumeEv'
    return self.uglySide.call(ritual)

  def muted(self) -> bool:
    """
    Calls Qt's 'bool QSoundEffectPrivateSynchronous::muted() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsoundeffectprivatesynchronous.html#muted
    """
    #  bool QSoundEffectPrivateSynchronous::muted() const
    ritual = 'ritual_ZNK30QSoundEffectPrivateSynchronous5mutedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK30QSoundEffectPrivateSynchronous5mutedEv'
    return self.uglySide.call(ritual)

  def playing(self) -> bool:
    """
    Calls Qt's 'bool QSoundEffectPrivateSynchronous::playing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsoundeffectprivatesynchronous.html#playing
    """
    #  bool QSoundEffectPrivateSynchronous::playing() const
    ritual = 'ritual_ZNK30QSoundEffectPrivateSynchronous7playingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK30QSoundEffectPrivateSynchronous7playingEv'
    return self.uglySide.call(ritual)

  def status(self) -> QSoundEffect.Status:
    """
    Calls Qt's 'QSoundEffect::Status QSoundEffectPrivateSynchronous::status()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsoundeffectprivatesynchronous.html#status

    Returns
    -------

    QSoundEffect.Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSoundEffect.Status(number)' gives.
    """
    #  QSoundEffect::Status QSoundEffectPrivateSynchronous::status() const
    ritual = 'ritual_ZNK30QSoundEffectPrivateSynchronous6statusEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK30QSoundEffectPrivateSynchronous6statusEv'
    return QSoundEffect.Status(self.uglySide.call(ritual))

  def audioDevice(self) -> QAudioDevice:
    """
    Calls Qt's 'QAudioDevice QSoundEffectPrivateSynchronous::audioDevice()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsoundeffectprivatesynchronous.html#audioDevice

    Returns
    -------

    QAudioDevice
      A new cute QAudioDevice around the copy Qt gave back. Python owns it.
    """
    #  QAudioDevice QSoundEffectPrivateSynchronous::audioDevice() const
    ritual = 'ritual_ZNK30QSoundEffectPrivateSynchronous11audioDeviceEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK30QSoundEffectPrivateSynchronous11audioDeviceEv')
    address = self.uglySide.call(ritual)
    from . import QAudioDevice
    return QAudioDevice._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setLoopsRemaining(self, loopsRemaining: int) -> None:
    """
    Calls Qt's 'void QSoundEffectPrivateSynchronous::setLoopsRemaining(int
    loopsRemaining)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsoundeffectprivatesynchronous.html

    Parameters
    ----------

    loopsRemaining : int
      Passed on as it is.
    """
    #  void QSoundEffectPrivateSynchronous::setLoopsRemaining(int
    #      loopsRemaining)
    self.uglySide.call(
        'ritual_ZN30QSoundEffectPrivateSynchronous17setLoopsRemainingEi',
        loopsRemaining,
    )

  @overload(QSoundEffect.Status)
  def setStatus(self, status: QSoundEffect.Status) -> None:
    """
    Calls Qt's 'void
    QSoundEffectPrivateSynchronous::setStatus(QSoundEffect::Status status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsoundeffectprivatesynchronous.html#setStatus

    Parameters
    ----------

    status : QSoundEffect.Status
      Passed on as its number.
    """
    #  void QSoundEffectPrivateSynchronous::setStatus(QSoundEffect::Status
    #      status)
    self.uglySide.call(
        'ritual_ZN30QSoundEffectPrivateSynchronous9setStatusEN12QSoundEffec'
        't6StatusE',
        status.value,
    )

  @overload(bool)
  def setPlaying(self, playing: bool) -> None:
    """
    Calls Qt's 'void QSoundEffectPrivateSynchronous::setPlaying(bool
    playing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsoundeffectprivatesynchronous.html#setPlaying

    Parameters
    ----------

    playing : bool
      Passed on as it is.
    """
    #  void QSoundEffectPrivateSynchronous::setPlaying(bool playing)
    self.uglySide.call(
        'ritual_ZN30QSoundEffectPrivateSynchronous10setPlayingEb', playing,
    )

  @overload(int)
  def setLoopCount(self, loopCount: int) -> bool:
    """
    Calls Qt's 'bool QSoundEffectPrivateSynchronous::setLoopCount(int
    loopCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsoundeffectprivatesynchronous.html#setLoopCount

    Parameters
    ----------

    loopCount : int
      Passed on as it is.
    """
    #  bool QSoundEffectPrivateSynchronous::setLoopCount(int loopCount)
    ritual = 'ritual_ZN30QSoundEffectPrivateSynchronous12setLoopCountEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QSoundEffectPrivateSynchronous12setLoopCountEi')
    return self.uglySide.call(ritual, loopCount)

  @overload(float)
  def setVolume(self, volume: float) -> bool:
    """
    Calls Qt's 'bool QSoundEffectPrivateSynchronous::setVolume(float
    volume)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsoundeffectprivatesynchronous.html#setVolume

    Parameters
    ----------

    volume : float
      Passed on as it is.
    """
    #  bool QSoundEffectPrivateSynchronous::setVolume(float volume)
    ritual = 'ritual_ZN30QSoundEffectPrivateSynchronous9setVolumeEf'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN30QSoundEffectPrivateSynchronous9setVolumeEf'
    return self.uglySide.call(ritual, volume)

  @overload(bool)
  def setMuted(self, muted: bool) -> bool:
    """
    Calls Qt's 'bool QSoundEffectPrivateSynchronous::setMuted(bool muted)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsoundeffectprivatesynchronous.html#setMuted

    Parameters
    ----------

    muted : bool
      Passed on as it is.
    """
    #  bool QSoundEffectPrivateSynchronous::setMuted(bool muted)
    ritual = 'ritual_ZN30QSoundEffectPrivateSynchronous8setMutedEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN30QSoundEffectPrivateSynchronous8setMutedEb'
    return self.uglySide.call(ritual, muted)

  @overload(QAudioDevice)
  def setAudioDevice(self, device: QAudioDevice) -> bool:
    """
    Calls Qt's 'bool
    QSoundEffectPrivateSynchronous::setAudioDevice(QAudioDevice device)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsoundeffectprivatesynchronous.html#setAudioDevice

    Parameters
    ----------

    device : QAudioDevice
      Passed on as a value: Qt reads the C++ QAudioDevice, which stays
      Python's own.
    """
    #  bool QSoundEffectPrivateSynchronous::setAudioDevice(QAudioDevice
    #      device)
    ritual = (
        'ritual_ZN30QSoundEffectPrivateSynchronous14setAudioDeviceE12QAudio'
        'Device')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QSoundEffectPrivateSynchronous14setAudioDeviceE12'
          'QAudioDevice')
    return self.uglySide.call(ritual, self._valueOf(device))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSoundEffect, QAudioDevice)
  @overload(NoneType, QAudioDevice)
  def __init__(
      self,
      q: Optional[QSoundEffect],
      audioDevice: QAudioDevice,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QSoundEffectPrivateSynchronous::QSoundEffectPrivateSynchronous(
    QSoundEffect *q, const QAudioDevice &audioDevice)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsoundeffectprivatesynchronous.html

    Parameters
    ----------

    q : Optional[QSoundEffect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    audioDevice : QAudioDevice
      Passed on as a value: Qt reads the C++ QAudioDevice, which stays
      Python's own.
    """
    #  QSoundEffectPrivateSynchronous::QSoundEffectPrivateSynchronous(
    #      QSoundEffect *q, const QAudioDevice &audioDevice)
    self._noteCreation(QSoundEffectPrivateSynchronous, lambda: Rituals.call(
        'ritual_ZN30QSoundEffectPrivateSynchronousC1EP12QSoundEffectRK12QAu'
        'dioDevice',
        self._addressOf(q), self._valueOf(audioDevice),
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

  @overload(str, int)
  @overload(NoneType, int)
  def writeData(self, data: Optional[str], len: int) -> int:
    """
    Calls Qt's 'qint64 QSoundEffectPrivateSynchronous::writeData(const char
    *data, qint64 len)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsoundeffectprivatesynchronous.html#writeData

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.
    """
    #  qint64 QSoundEffectPrivateSynchronous::writeData(const char *data,
    #      qint64 len)
    return self.uglySide.call(
        'ritual_ZN30QSoundEffectPrivateSynchronous9writeDataEPKcx',
        self._bytesOf(data), len,
    )

  def updateAudioOutput(self) -> bool:
    """
    Calls Qt's 'bool QSoundEffectPrivateSynchronous::updateAudioOutput()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsoundeffectprivatesynchronous.html
    """
    #  bool QSoundEffectPrivateSynchronous::updateAudioOutput()
    return self.uglySide.call(
        'ritual_ZN30QSoundEffectPrivateSynchronous17updateAudioOutputEv',
    )

  def decoderError(self) -> None:
    """
    Calls Qt's 'void QSoundEffectPrivateSynchronous::decoderError()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsoundeffectprivatesynchronous.html#decoderError
    """
    #  void QSoundEffectPrivateSynchronous::decoderError()
    self.uglySide.call(
        'ritual_ZN30QSoundEffectPrivateSynchronous12decoderErrorEv',
    )

  def play(self) -> None:
    """
    Calls Qt's 'void QSoundEffectPrivateSynchronous::play()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsoundeffectprivatesynchronous.html#play
    """
    #  void QSoundEffectPrivateSynchronous::play()
    ritual = 'ritual_ZN30QSoundEffectPrivateSynchronous4playEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN30QSoundEffectPrivateSynchronous4playEv'
    self.uglySide.call(ritual)

  def stop(self) -> None:
    """
    Calls Qt's 'void QSoundEffectPrivateSynchronous::stop()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsoundeffectprivatesynchronous.html#stop
    """
    #  void QSoundEffectPrivateSynchronous::stop()
    ritual = 'ritual_ZN30QSoundEffectPrivateSynchronous4stopEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN30QSoundEffectPrivateSynchronous4stopEv'
    self.uglySide.call(ritual)

  @overload(QAudio.State)
  def stateChanged(self, a0: QAudio.State) -> None:
    """
    Calls Qt's 'void
    QSoundEffectPrivateSynchronous::stateChanged(QAudio::State a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsoundeffectprivatesynchronous.html#stateChanged

    Parameters
    ----------

    a0 : QAudio.State
      Passed on as its number.
    """
    #  void QSoundEffectPrivateSynchronous::stateChanged(QAudio::State a0)
    self.uglySide.call(
        'ritual_ZN30QSoundEffectPrivateSynchronous12stateChangedEN6QAudio5S'
        'tateE',
        a0.value,
    )

  @staticmethod
  def sampleReady(*__, **_) -> Never:
    """
    Qt's 'void QSoundEffectPrivateSynchronous::sampleReady(SharedSamplePtr
    a0)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSoundEffectPrivateSynchronous.sampleReady' has no cute function "
        "yet. Qt's 'void "
        "QSoundEffectPrivateSynchronous::sampleReady(SharedSamplePtr a0)': "
        "takes a type Python has no way to hand over yet.")
