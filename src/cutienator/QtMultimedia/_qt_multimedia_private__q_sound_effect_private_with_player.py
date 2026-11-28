"""
QtMultimediaPrivate::QSoundEffectPrivateWithPlayer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qsoundeffectwithplayer_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QtMultimediaPrivate::QSoundEffectPrivateWithPlayer to be private:
#  it declares the class in a header it calls private. cutienator does not
#  care. Qt hands objects of the class out all the same, and a class we are
#  handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QSoundEffect, QSoundEffectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QAudioDevice, QAudioFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioDevice = WAIT['QAudioDevice']
  QAudioFormat = WAIT['QAudioFormat']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSoundEffectPrivateWithPlayer(QObject, QSoundEffectPrivate):
  """
  The cute side of Qt's QtMultimediaPrivate::QSoundEffectPrivateWithPlayer: a
  plain Python object standing in front of one C++
  QtMultimediaPrivate::QSoundEffectPrivateWithPlayer.

  It is built on the cute 'QObject', as Qt's
  QtMultimediaPrivate::QSoundEffectPrivateWithPlayer is built on Qt's
  QObject, and has everything that class has. It is built on the cute
  'QSoundEffectPrivate' as well, as Qt's
  QtMultimediaPrivate::QSoundEffectPrivateWithPlayer is built on Qt's
  QSoundEffectPrivate too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtMultimediaPrivate::QSoundEffectPrivateWithPlayer
  that has a ritual and that Python can call so far, 18 names in all:
  'setAudioDevice', 'audioDevice', 'status', 'loopCount', 'setLoopCount',
  'loopsRemaining', 'volume', 'setVolume', 'muted', 'setMuted', 'play',
  'stop', 'playing', 'setStatus', 'formatIsSupported',
  'setResolvedAudioDevice', 'resolveAudioDevice', 'setLoopsRemaining'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'std::shared_ptr<QRtAudioEngine>
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::getEngineFor(const
    QAudioDevice &a0, const QAudioFormat &a1)': gives a type Python has no
    way to take yet.
  - Qt's 'QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::
    ~QSoundEffectPrivateWithPlayer()': the destructor: Python never removes a
    C++ QtMultimediaPrivate::QSoundEffectPrivateWithPlayer.
  - Qt's 'void
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::setSource(QUrl a0,
    QSampleCache &a1)': takes a type Python has no way to hand over yet.
  - Qt's 'const std::shared_ptr<QRtAudioEngine>
    &QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::player() const':
    gives a type Python has no way to take yet.
  - Qt's 'const std::set<std::shared_ptr<QSoundEffectVoice>,
    QRtAudioEngineVoiceCompare>
    &QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::voices() const':
    gives a type Python has no way to take yet.
  - Qt's 'void QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::play(std::
    shared_ptr<QSoundEffectVoice> a0)': takes a type Python has no way to
    hand over yet.
  - Qt's 'bool
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::updatePlayer(const
    SharedSamplePtr &sample)': takes a type Python has no way to hand over
    yet.
  - Qt's 'std::optional<VoiceId>
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::activeVoice() const':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 31 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QtMultimediaPrivate::QSoundEffectPrivateWithPlayer is created at
    the first use, not by
    'QtMultimediaPrivate::QSoundEffectPrivateWithPlayer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer.
  - Qt tells when it has removed the C++
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QtMultimediaPrivate::QSoundEffectPrivateWithPlayer that
    has no cute function yet, 'activeVoice', 'getEngineFor', 'player',
    'updatePlayer', 'voices', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QAudioFormat)
  def formatIsSupported(a0: QAudioFormat) -> bool:
    """
    Calls Qt's 'bool
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::formatIsSupported(
    const QAudioFormat &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qsoundeffectprivatewithplayer.html

    Parameters
    ----------

    a0 : QAudioFormat
      Passed on as a value: Qt reads the C++ QAudioFormat, which stays
      Python's own.
    """
    #  bool QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::
    #      formatIsSupported(const QAudioFormat &a0)
    return Rituals.call(
        'ritual_ZN19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer17for'
        'matIsSupportedERK12QAudioFormat',
        CuteMixin._valueOf(a0),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtMultimediaPrivate::QSoundEffectPrivateWithPlayer'

  #  Qt's QtMultimediaPrivate::QSoundEffectPrivateWithPlayer is built on more
  #  than one class. The part of a C++
  #  QtMultimediaPrivate::QSoundEffectPrivateWithPlayer that belongs to a
  #  class after the first begins somewhere inside the object, and the ritual
  #  named for that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QSoundEffectPrivate':
          'ritual_cast_QtMultimediaPrivate_QSoundEffectPrivateWithPlayer_QSoundEffectPrivate',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def audioDevice(self) -> QAudioDevice:
    """
    Calls Qt's 'QAudioDevice
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::audioDevice() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qsoundeffectprivatewithplayer.html

    Returns
    -------

    QAudioDevice
      A new cute QAudioDevice around the copy Qt gave back. Python owns it.
    """
    #  QAudioDevice
    #      QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::audioDevice()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer11au'
        'dioDeviceEv',
    )
    from . import QAudioDevice
    return QAudioDevice._cuteOwning(address)

  def status(self) -> QSoundEffect.Status:
    """
    Calls Qt's 'QSoundEffect::Status
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::status() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qsoundeffectprivatewithplayer.html

    Returns
    -------

    QSoundEffect.Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSoundEffect.Status(number)' gives.
    """
    #  QSoundEffect::Status
    #      QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::status() const
    return QSoundEffect.Status(self.uglySide.call(
        'ritual_ZNK19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer6sta'
        'tusEv',
    ))

  def loopCount(self) -> int:
    """
    Calls Qt's 'int
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::loopCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qsoundeffectprivatewithplayer.html
    """
    #  int QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::loopCount()
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer9loo'
        'pCountEv',
    )

  def loopsRemaining(self) -> int:
    """
    Calls Qt's 'int
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::loopsRemaining()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qsoundeffectprivatewithplayer.html
    """
    #  int QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::
    #      loopsRemaining() const
    return self.uglySide.call(
        'ritual_ZNK19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer14lo'
        'opsRemainingEv',
    )

  def volume(self) -> float:
    """
    Calls Qt's 'float
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::volume() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qsoundeffectprivatewithplayer.html
    """
    #  float QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::volume()
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer6vol'
        'umeEv',
    )

  def muted(self) -> bool:
    """
    Calls Qt's 'bool
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::muted() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qsoundeffectprivatewithplayer.html
    """
    #  bool QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::muted() const
    return self.uglySide.call(
        'ritual_ZNK19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer5mut'
        'edEv',
    )

  def playing(self) -> bool:
    """
    Calls Qt's 'bool
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::playing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qsoundeffectprivatewithplayer.html
    """
    #  bool QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::playing()
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer7pla'
        'yingEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAudioDevice)
  def setAudioDevice(self, device: QAudioDevice) -> bool:
    """
    Calls Qt's 'bool
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::setAudioDevice(
    QAudioDevice device)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qsoundeffectprivatewithplayer.html

    Parameters
    ----------

    device : QAudioDevice
      Passed on as a value: Qt reads the C++ QAudioDevice, which stays
      Python's own.
    """
    #  bool QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::
    #      setAudioDevice(QAudioDevice device)
    return self.uglySide.call(
        'ritual_ZN19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer14set'
        'AudioDeviceE12QAudioDevice',
        self._valueOf(device),
    )

  @overload(int)
  def setLoopCount(self, a0: int) -> bool:
    """
    Calls Qt's 'bool
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::setLoopCount(int
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qsoundeffectprivatewithplayer.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  bool QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::setLoopCount(
    #      int a0)
    return self.uglySide.call(
        'ritual_ZN19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer12set'
        'LoopCountEi',
        a0,
    )

  @overload(float)
  def setVolume(self, a0: float) -> bool:
    """
    Calls Qt's 'bool
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::setVolume(float a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qsoundeffectprivatewithplayer.html

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  bool QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::setVolume(
    #      float a0)
    return self.uglySide.call(
        'ritual_ZN19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer9setV'
        'olumeEf',
        a0,
    )

  @overload(bool)
  def setMuted(self, a0: bool) -> bool:
    """
    Calls Qt's 'bool
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::setMuted(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qsoundeffectprivatewithplayer.html

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  bool QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::setMuted(bool
    #      a0)
    return self.uglySide.call(
        'ritual_ZN19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer8setM'
        'utedEb',
        a0,
    )

  @overload(QSoundEffect.Status)
  def setStatus(self, status: QSoundEffect.Status) -> None:
    """
    Calls Qt's 'void
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::setStatus(
    QSoundEffect::Status status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qsoundeffectprivatewithplayer.html

    Parameters
    ----------

    status : QSoundEffect.Status
      Passed on as its number.
    """
    #  void QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::setStatus(
    #      QSoundEffect::Status status)
    self.uglySide.call(
        'ritual_ZN19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer9setS'
        'tatusEN12QSoundEffect6StatusE',
        status.value,
    )

  @overload(QAudioDevice)
  def setResolvedAudioDevice(self, device: QAudioDevice) -> None:
    """
    Calls Qt's 'void QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::
    setResolvedAudioDevice(QAudioDevice device)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qsoundeffectprivatewithplayer.html

    Parameters
    ----------

    device : QAudioDevice
      Passed on as a value: Qt reads the C++ QAudioDevice, which stays
      Python's own.
    """
    #  void QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::
    #      setResolvedAudioDevice(QAudioDevice device)
    self.uglySide.call(
        'ritual_ZN19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer22set'
        'ResolvedAudioDeviceE12QAudioDevice',
        self._valueOf(device),
    )

  @overload(int)
  def setLoopsRemaining(self, a0: int) -> None:
    """
    Calls Qt's 'void
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::setLoopsRemaining(int
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qsoundeffectprivatewithplayer.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::
    #      setLoopsRemaining(int a0)
    self.uglySide.call(
        'ritual_ZN19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer17set'
        'LoopsRemainingEi',
        a0,
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

  @overload(QSoundEffect, QAudioDevice)
  @overload(NoneType, QAudioDevice)
  def __init__(
      self,
      q: Optional[QSoundEffect],
      audioDevice: QAudioDevice,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::
    QSoundEffectPrivateWithPlayer(QSoundEffect *q, QAudioDevice
    audioDevice)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qsoundeffectprivatewithplayer.html

    Parameters
    ----------

    q : Optional[QSoundEffect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    audioDevice : QAudioDevice
      Passed on as a value: Qt reads the C++ QAudioDevice, which stays
      Python's own.
    """
    #  QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::
    #      QSoundEffectPrivateWithPlayer(QSoundEffect *q, QAudioDevice
    #      audioDevice)
    self._noteCreation(QSoundEffectPrivateWithPlayer, lambda: Rituals.call(
        'ritual_ZN19QtMultimediaPrivate29QSoundEffectPrivateWithPlayerC1EP1'
        '2QSoundEffect12QAudioDevice',
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

  def play(self) -> None:
    """
    Calls Qt's 'void
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::play()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qsoundeffectprivatewithplayer.html
    """
    #  void QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::play()
    self.uglySide.call(
        'ritual_ZN19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer4play'
        'Ev',
    )

  def stop(self) -> None:
    """
    Calls Qt's 'void
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::stop()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qsoundeffectprivatewithplayer.html
    """
    #  void QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::stop()
    self.uglySide.call(
        'ritual_ZN19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer4stop'
        'Ev',
    )

  def resolveAudioDevice(self) -> None:
    """
    Calls Qt's 'void
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::resolveAudioDevice(
    )'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qsoundeffectprivatewithplayer.html
    """
    #  void QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::
    #      resolveAudioDevice()
    self.uglySide.call(
        'ritual_ZN19QtMultimediaPrivate29QSoundEffectPrivateWithPlayer18res'
        'olveAudioDeviceEv',
    )

  @staticmethod
  def activeVoice(*__, **_) -> Never:
    """
    Qt's 'std::optional<VoiceId>
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::activeVoice() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtMultimediaPrivate.QSoundEffectPrivateWithPlayer.activeVoice' "
        "has no cute function yet. Qt's 'std::optional<VoiceId> "
        "QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::activeVoice() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def getEngineFor(*__, **_) -> Never:
    """
    Qt's 'std::shared_ptr<QRtAudioEngine>
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::getEngineFor(const
    QAudioDevice &a0, const QAudioFormat &a1)': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QtMultimediaPrivate.QSoundEffectPrivateWithPlayer.getEngineFor' "
        "has no cute function yet. Qt's 'std::shared_ptr<QRtAudioEngine> "
        "QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::getEngineFor(co"
        "nst QAudioDevice &a0, const QAudioFormat &a1)': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def player(*__, **_) -> Never:
    """
    Qt's 'const std::shared_ptr<QRtAudioEngine>
    &QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::player() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtMultimediaPrivate.QSoundEffectPrivateWithPlayer.player' has no "
        "cute function yet. Qt's 'const std::shared_ptr<QRtAudioEngine> "
        "&QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::player() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def updatePlayer(*__, **_) -> Never:
    """
    Qt's 'bool
    QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::updatePlayer(const
    SharedSamplePtr &sample)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QtMultimediaPrivate.QSoundEffectPrivateWithPlayer.updatePlayer' "
        "has no cute function yet. Qt's 'bool "
        "QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::updatePlayer(co"
        "nst SharedSamplePtr &sample)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def voices(*__, **_) -> Never:
    """
    Qt's 'const std::set<std::shared_ptr<QSoundEffectVoice>,
    QRtAudioEngineVoiceCompare>
    &QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::voices() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtMultimediaPrivate.QSoundEffectPrivateWithPlayer.voices' has no "
        "cute function yet. Qt's 'const "
        "std::set<std::shared_ptr<QSoundEffectVoice>, "
        "QRtAudioEngineVoiceCompare> "
        "&QtMultimediaPrivate::QSoundEffectPrivateWithPlayer::voices() "
        "const': gives a type Python has no way to take yet.")
