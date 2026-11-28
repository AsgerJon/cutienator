"""
QSoundEffect binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/qsoundeffect.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl
  from . import QAudioDevice, QSoundEffectPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioDevice = WAIT['QAudioDevice']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSoundEffect(QObject):
  """
  The cute side of Qt's QSoundEffect: a plain Python object standing in front
  of one C++ QSoundEffect.

  It is built on the cute 'QObject', as Qt's QSoundEffect is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSoundEffect that has a ritual and that Python can
  call so far, 29 names in all: 'metaObject', 'tr', 'supportedMimeTypes',
  'source', 'setSource', 'loopCount', 'loopsRemaining', 'setLoopCount',
  'audioDevice', 'setAudioDevice', 'volume', 'setVolume', 'isMuted',
  'setMuted', 'isLoaded', 'isPlaying', 'status', 'sourceChanged',
  'loopCountChanged', 'loopsRemainingChanged', 'volumeChanged',
  'mutedChanged', 'loadedChanged', 'playingChanged', 'statusChanged',
  'audioDeviceChanged', 'play', 'stop', 'd_func'. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSoundEffect::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QSoundEffect::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QSoundEffect::~QSoundEffect()': the destructor: Python never
    removes a C++ QSoundEffect.
  - Qt's 'const QSoundEffectPrivate *QSoundEffect::d_func() const': takes in
    Python what 'QSoundEffectPrivate *QSoundEffect::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 39 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QSoundEffect is created at the first use, not by
    'QSoundEffect(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSoundEffect.
  - Qt tells when it has removed the C++ QSoundEffect. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QSoundEffect, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Loop(CuteNum):
    """
    The enum 'QSoundEffect::Loop' of Qt, with the 1 names Qt gives in it.
    """

    Infinite = Kee[int](-2)

  class Status(CuteNum):
    """
    The enum 'QSoundEffect::Status' of Qt, with the 4 names Qt gives in it.
    """

    Null = Kee[int](0)
    Loading = Kee[int](1)
    Ready = Kee[int](2)
    Error = Kee[int](3)

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
    Calls Qt's 'QString QSoundEffect::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffect.html#tr

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
    #  QString QSoundEffect::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QSoundEffect2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def supportedMimeTypes() -> QStringList:
    """
    Calls Qt's 'QStringList QSoundEffect::supportedMimeTypes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsoundeffect.html#supportedMimeTypes

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QSoundEffect::supportedMimeTypes()
    address = Rituals.call('ritual_ZN12QSoundEffect18supportedMimeTypesEv')
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSoundEffect'

  #  A C++ QSoundEffect Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSoundEffect'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSoundEffect::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffect.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSoundEffect::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QSoundEffect10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QSoundEffect::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffect.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QSoundEffect::source() const
    address = self.uglySide.call('ritual_ZNK12QSoundEffect6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def loopCount(self) -> int:
    """
    Calls Qt's 'int QSoundEffect::loopCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffect.html#loopCount
    """
    #  int QSoundEffect::loopCount() const
    return self.uglySide.call('ritual_ZNK12QSoundEffect9loopCountEv')

  def loopsRemaining(self) -> int:
    """
    Calls Qt's 'int QSoundEffect::loopsRemaining() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffect.html#loopsRemaining
    """
    #  int QSoundEffect::loopsRemaining() const
    return self.uglySide.call('ritual_ZNK12QSoundEffect14loopsRemainingEv')

  def volume(self) -> float:
    """
    Calls Qt's 'float QSoundEffect::volume() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffect.html#volume
    """
    #  float QSoundEffect::volume() const
    return self.uglySide.call('ritual_ZNK12QSoundEffect6volumeEv')

  def isMuted(self) -> bool:
    """
    Calls Qt's 'bool QSoundEffect::isMuted() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffect.html#isMuted
    """
    #  bool QSoundEffect::isMuted() const
    return self.uglySide.call('ritual_ZNK12QSoundEffect7isMutedEv')

  def isLoaded(self) -> bool:
    """
    Calls Qt's 'bool QSoundEffect::isLoaded() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffect.html#isLoaded
    """
    #  bool QSoundEffect::isLoaded() const
    return self.uglySide.call('ritual_ZNK12QSoundEffect8isLoadedEv')

  def isPlaying(self) -> bool:
    """
    Calls Qt's 'bool QSoundEffect::isPlaying() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffect.html#isPlaying
    """
    #  bool QSoundEffect::isPlaying() const
    return self.uglySide.call('ritual_ZNK12QSoundEffect9isPlayingEv')

  def status(self) -> Status:
    """
    Calls Qt's 'Status QSoundEffect::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffect.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QSoundEffect::status() const
    return QSoundEffect.Status(self.uglySide.call(
        'ritual_ZNK12QSoundEffect6statusEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QSoundEffect::setSource(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffect.html#setSource

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QSoundEffect::setSource(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN12QSoundEffect9setSourceERK4QUrl', self._valueOf(url),
    )

  @overload(int)
  def setLoopCount(self, loopCount: int) -> None:
    """
    Calls Qt's 'void QSoundEffect::setLoopCount(int loopCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffect.html#setLoopCount

    Parameters
    ----------

    loopCount : int
      Passed on as it is.
    """
    #  void QSoundEffect::setLoopCount(int loopCount)
    self.uglySide.call('ritual_ZN12QSoundEffect12setLoopCountEi', loopCount)

  @overload(QAudioDevice)
  def setAudioDevice(self, device: QAudioDevice) -> None:
    """
    Calls Qt's 'void QSoundEffect::setAudioDevice(const QAudioDevice
    &device)'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffect.html#setAudioDevice

    Parameters
    ----------

    device : QAudioDevice
      Passed on as a value: Qt reads the C++ QAudioDevice, which stays
      Python's own.
    """
    #  void QSoundEffect::setAudioDevice(const QAudioDevice &device)
    self.uglySide.call(
        'ritual_ZN12QSoundEffect14setAudioDeviceERK12QAudioDevice',
        self._valueOf(device),
    )

  @overload(float)
  def setVolume(self, volume: float) -> None:
    """
    Calls Qt's 'void QSoundEffect::setVolume(float volume)'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffect.html#setVolume

    Parameters
    ----------

    volume : float
      Passed on as it is.
    """
    #  void QSoundEffect::setVolume(float volume)
    self.uglySide.call('ritual_ZN12QSoundEffect9setVolumeEf', volume)

  @overload(bool)
  def setMuted(self, muted: bool) -> None:
    """
    Calls Qt's 'void QSoundEffect::setMuted(bool muted)'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffect.html#setMuted

    Parameters
    ----------

    muted : bool
      Passed on as it is.
    """
    #  void QSoundEffect::setMuted(bool muted)
    self.uglySide.call('ritual_ZN12QSoundEffect8setMutedEb', muted)

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
    Notes what was given, for Qt's 'QSoundEffect::QSoundEffect(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffect.html#QSoundEffect

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSoundEffect::QSoundEffect(QObject *parent)
    self._noteCreation(QSoundEffect, lambda: Rituals.call(
        'ritual_ZN12QSoundEffectC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QAudioDevice)
  @overload(QAudioDevice, QObject)
  @overload(QAudioDevice, NoneType)
  def __init__(
      self,
      audioDevice: QAudioDevice,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSoundEffect::QSoundEffect(const
    QAudioDevice &audioDevice, QObject *parent)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffect.html#QSoundEffect

    Parameters
    ----------

    audioDevice : QAudioDevice
      Passed on as a value: Qt reads the C++ QAudioDevice, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSoundEffect::QSoundEffect(const QAudioDevice &audioDevice, QObject
    #      *parent)
    self._noteCreation(QSoundEffect, lambda: Rituals.call(
        'ritual_ZN12QSoundEffectC1ERK12QAudioDeviceP7QObject',
        self._valueOf(audioDevice), self._addressOf(parent, 'QObject'),
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

  def audioDevice(self) -> QAudioDevice:
    """
    Calls Qt's 'QAudioDevice QSoundEffect::audioDevice()'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffect.html#audioDevice

    Returns
    -------

    QAudioDevice
      A new cute QAudioDevice around the copy Qt gave back. Python owns it.
    """
    #  QAudioDevice QSoundEffect::audioDevice()
    address = self.uglySide.call('ritual_ZN12QSoundEffect11audioDeviceEv')
    from . import QAudioDevice
    return QAudioDevice._cuteOwning(address)

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QSoundEffect::sourceChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffect.html#sourceChanged
    """
    #  void QSoundEffect::sourceChanged()
    self.uglySide.call('ritual_ZN12QSoundEffect13sourceChangedEv')

  def loopCountChanged(self) -> None:
    """
    Calls Qt's 'void QSoundEffect::loopCountChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffect.html#loopCountChanged
    """
    #  void QSoundEffect::loopCountChanged()
    self.uglySide.call('ritual_ZN12QSoundEffect16loopCountChangedEv')

  def loopsRemainingChanged(self) -> None:
    """
    Calls Qt's 'void QSoundEffect::loopsRemainingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsoundeffect.html#loopsRemainingChanged
    """
    #  void QSoundEffect::loopsRemainingChanged()
    self.uglySide.call('ritual_ZN12QSoundEffect21loopsRemainingChangedEv')

  def volumeChanged(self) -> None:
    """
    Calls Qt's 'void QSoundEffect::volumeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffect.html#volumeChanged
    """
    #  void QSoundEffect::volumeChanged()
    self.uglySide.call('ritual_ZN12QSoundEffect13volumeChangedEv')

  def mutedChanged(self) -> None:
    """
    Calls Qt's 'void QSoundEffect::mutedChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffect.html#mutedChanged
    """
    #  void QSoundEffect::mutedChanged()
    self.uglySide.call('ritual_ZN12QSoundEffect12mutedChangedEv')

  def loadedChanged(self) -> None:
    """
    Calls Qt's 'void QSoundEffect::loadedChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffect.html#loadedChanged
    """
    #  void QSoundEffect::loadedChanged()
    self.uglySide.call('ritual_ZN12QSoundEffect13loadedChangedEv')

  def playingChanged(self) -> None:
    """
    Calls Qt's 'void QSoundEffect::playingChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffect.html#playingChanged
    """
    #  void QSoundEffect::playingChanged()
    self.uglySide.call('ritual_ZN12QSoundEffect14playingChangedEv')

  def statusChanged(self) -> None:
    """
    Calls Qt's 'void QSoundEffect::statusChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffect.html#statusChanged
    """
    #  void QSoundEffect::statusChanged()
    self.uglySide.call('ritual_ZN12QSoundEffect13statusChangedEv')

  def audioDeviceChanged(self) -> None:
    """
    Calls Qt's 'void QSoundEffect::audioDeviceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsoundeffect.html#audioDeviceChanged
    """
    #  void QSoundEffect::audioDeviceChanged()
    self.uglySide.call('ritual_ZN12QSoundEffect18audioDeviceChangedEv')

  def play(self) -> None:
    """
    Calls Qt's 'void QSoundEffect::play()'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffect.html#play
    """
    #  void QSoundEffect::play()
    self.uglySide.call('ritual_ZN12QSoundEffect4playEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QSoundEffect::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffect.html#stop
    """
    #  void QSoundEffect::stop()
    self.uglySide.call('ritual_ZN12QSoundEffect4stopEv')

  def d_func(self) -> Optional[QSoundEffectPrivate]:
    """
    Calls Qt's 'QSoundEffectPrivate *QSoundEffect::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffect.html#d_func

    Returns
    -------

    Optional[QSoundEffectPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSoundEffectPrivate *QSoundEffect::d_func()
    address = self.uglySide.call('ritual_ZN12QSoundEffect6d_funcEv')
    from . import QSoundEffectPrivate
    return QSoundEffectPrivate._cuteAt(address)
