"""
QAudioEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSpatialAudio/qaudioengine.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtMultimedia import QAudioDevice
  from . import QAudioEnginePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioDevice = WAIT['QAudioDevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAudioEngine(QObject):
  """
  The cute side of Qt's QAudioEngine: a plain Python object standing in front
  of one C++ QAudioEngine.

  It is built on the cute 'QObject', as Qt's QAudioEngine is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAudioEngine that has a ritual and that Python can
  call so far, 25 names in all: 'metaObject', 'tr', 'setOutputMode',
  'outputMode', 'sampleRate', 'setOutputDevice', 'outputDevice',
  'setMasterVolume', 'masterVolume', 'setPaused', 'paused',
  'setRoomEffectsEnabled', 'roomEffectsEnabled', 'setDistanceScale',
  'distanceScale', 'outputModeChanged', 'outputDeviceChanged',
  'masterVolumeChanged', 'pausedChanged', 'distanceScaleChanged', 'start',
  'stop', 'pause', 'resume', 'd_func'. It can be made from Python, in 3 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAudioEngine::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QAudioEngine::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QAudioEngine::~QAudioEngine()': the destructor: Python never
    removes a C++ QAudioEngine.
  - Qt's 'const QAudioEnginePrivate *QAudioEngine::d_func() const': takes in
    Python what 'QAudioEnginePrivate *QAudioEngine::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 34 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QAudioEngine is created at the first use, not by
    'QAudioEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAudioEngine.
  - Qt tells when it has removed the C++ QAudioEngine. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QAudioEngine, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class OutputMode(CuteNum):
    """
    The enum 'QAudioEngine::OutputMode' of Qt, with the 3 names Qt gives in
    it.
    """

    Surround = Kee[int](0)
    Stereo = Kee[int](1)
    Headphone = Kee[int](2)

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
    Calls Qt's 'QString QAudioEngine::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioengine.html#tr

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
    #  QString QAudioEngine::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QAudioEngine2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAudioEngine'

  #  A C++ QAudioEngine Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAudioEngine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAudioEngine::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioengine.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAudioEngine::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QAudioEngine10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def outputMode(self) -> OutputMode:
    """
    Calls Qt's 'OutputMode QAudioEngine::outputMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioengine.html#outputMode

    Returns
    -------

    OutputMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'OutputMode(number)'
      gives.
    """
    #  OutputMode QAudioEngine::outputMode() const
    return QAudioEngine.OutputMode(self.uglySide.call(
        'ritual_ZNK12QAudioEngine10outputModeEv',
    ))

  def sampleRate(self) -> int:
    """
    Calls Qt's 'int QAudioEngine::sampleRate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioengine.html#sampleRate
    """
    #  int QAudioEngine::sampleRate() const
    return self.uglySide.call('ritual_ZNK12QAudioEngine10sampleRateEv')

  def outputDevice(self) -> QAudioDevice:
    """
    Calls Qt's 'QAudioDevice QAudioEngine::outputDevice() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioengine.html#outputDevice

    Returns
    -------

    QAudioDevice
      A new cute QAudioDevice around the copy Qt gave back. Python owns it.
    """
    #  QAudioDevice QAudioEngine::outputDevice() const
    address = self.uglySide.call('ritual_ZNK12QAudioEngine12outputDeviceEv')
    from ..QtMultimedia import QAudioDevice
    return QAudioDevice._cuteOwning(address)

  def masterVolume(self) -> float:
    """
    Calls Qt's 'float QAudioEngine::masterVolume() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioengine.html#masterVolume
    """
    #  float QAudioEngine::masterVolume() const
    return self.uglySide.call('ritual_ZNK12QAudioEngine12masterVolumeEv')

  def paused(self) -> bool:
    """
    Calls Qt's 'bool QAudioEngine::paused() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioengine.html#paused
    """
    #  bool QAudioEngine::paused() const
    return self.uglySide.call('ritual_ZNK12QAudioEngine6pausedEv')

  def roomEffectsEnabled(self) -> bool:
    """
    Calls Qt's 'bool QAudioEngine::roomEffectsEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudioengine.html#roomEffectsEnabled
    """
    #  bool QAudioEngine::roomEffectsEnabled() const
    return self.uglySide.call(
        'ritual_ZNK12QAudioEngine18roomEffectsEnabledEv',
    )

  def distanceScale(self) -> float:
    """
    Calls Qt's 'float QAudioEngine::distanceScale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioengine.html#distanceScale
    """
    #  float QAudioEngine::distanceScale() const
    return self.uglySide.call('ritual_ZNK12QAudioEngine13distanceScaleEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(OutputMode)
  def setOutputMode(self, mode: OutputMode) -> None:
    """
    Calls Qt's 'void QAudioEngine::setOutputMode(OutputMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioengine.html#setOutputMode

    Parameters
    ----------

    mode : OutputMode
      Passed on as its number.
    """
    #  void QAudioEngine::setOutputMode(OutputMode mode)
    self.uglySide.call(
        'ritual_ZN12QAudioEngine13setOutputModeENS_10OutputModeE',
        mode.value,
    )

  @overload(QAudioDevice)
  def setOutputDevice(self, device: QAudioDevice) -> None:
    """
    Calls Qt's 'void QAudioEngine::setOutputDevice(const QAudioDevice
    &device)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioengine.html#setOutputDevice

    Parameters
    ----------

    device : QAudioDevice
      Passed on as a value: Qt reads the C++ QAudioDevice, which stays
      Python's own.
    """
    #  void QAudioEngine::setOutputDevice(const QAudioDevice &device)
    self.uglySide.call(
        'ritual_ZN12QAudioEngine15setOutputDeviceERK12QAudioDevice',
        self._valueOf(device),
    )

  @overload(float)
  def setMasterVolume(self, volume: float) -> None:
    """
    Calls Qt's 'void QAudioEngine::setMasterVolume(float volume)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioengine.html#setMasterVolume

    Parameters
    ----------

    volume : float
      Passed on as it is.
    """
    #  void QAudioEngine::setMasterVolume(float volume)
    self.uglySide.call('ritual_ZN12QAudioEngine15setMasterVolumeEf', volume)

  @overload(bool)
  def setPaused(self, paused: bool) -> None:
    """
    Calls Qt's 'void QAudioEngine::setPaused(bool paused)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioengine.html#setPaused

    Parameters
    ----------

    paused : bool
      Passed on as it is.
    """
    #  void QAudioEngine::setPaused(bool paused)
    self.uglySide.call('ritual_ZN12QAudioEngine9setPausedEb', paused)

  @overload(bool)
  def setRoomEffectsEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QAudioEngine::setRoomEffectsEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudioengine.html#setRoomEffectsEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QAudioEngine::setRoomEffectsEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN12QAudioEngine21setRoomEffectsEnabledEb', enabled,
    )

  @overload(float)
  def setDistanceScale(self, scale: float) -> None:
    """
    Calls Qt's 'void QAudioEngine::setDistanceScale(float scale)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioengine.html#setDistanceScale

    Parameters
    ----------

    scale : float
      Passed on as it is.
    """
    #  void QAudioEngine::setDistanceScale(float scale)
    self.uglySide.call('ritual_ZN12QAudioEngine16setDistanceScaleEf', scale)

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QAudioEngine::QAudioEngine()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qaudioengine.html#QAudioEngine
    """
    #  QAudioEngine::QAudioEngine()
    self._noteCreation(QAudioEngine, lambda: Rituals.call(
        'ritual_ZN12QAudioEngineC1Ev',
    ))

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's 'QAudioEngine::QAudioEngine(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qaudioengine.html#QAudioEngine

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAudioEngine::QAudioEngine(QObject *parent)
    self._noteCreation(QAudioEngine, lambda: Rituals.call(
        'ritual_ZN12QAudioEngineC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(int)
  @overload(int, QObject)
  @overload(int, NoneType)
  def __init__(
      self,
      sampleRate: int,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QAudioEngine::QAudioEngine(int
    sampleRate, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qaudioengine.html#QAudioEngine

    Parameters
    ----------

    sampleRate : int
      Passed on as it is.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAudioEngine::QAudioEngine(int sampleRate, QObject *parent)
    self._noteCreation(QAudioEngine, lambda: Rituals.call(
        'ritual_ZN12QAudioEngineC1EiP7QObject',
        sampleRate, self._addressOf(parent, 'QObject'),
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

  def outputModeChanged(self) -> None:
    """
    Calls Qt's 'void QAudioEngine::outputModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudioengine.html#outputModeChanged
    """
    #  void QAudioEngine::outputModeChanged()
    self.uglySide.call('ritual_ZN12QAudioEngine17outputModeChangedEv')

  def outputDeviceChanged(self) -> None:
    """
    Calls Qt's 'void QAudioEngine::outputDeviceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudioengine.html#outputDeviceChanged
    """
    #  void QAudioEngine::outputDeviceChanged()
    self.uglySide.call('ritual_ZN12QAudioEngine19outputDeviceChangedEv')

  def masterVolumeChanged(self) -> None:
    """
    Calls Qt's 'void QAudioEngine::masterVolumeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudioengine.html#masterVolumeChanged
    """
    #  void QAudioEngine::masterVolumeChanged()
    self.uglySide.call('ritual_ZN12QAudioEngine19masterVolumeChangedEv')

  def pausedChanged(self) -> None:
    """
    Calls Qt's 'void QAudioEngine::pausedChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioengine.html#pausedChanged
    """
    #  void QAudioEngine::pausedChanged()
    self.uglySide.call('ritual_ZN12QAudioEngine13pausedChangedEv')

  def distanceScaleChanged(self) -> None:
    """
    Calls Qt's 'void QAudioEngine::distanceScaleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudioengine.html#distanceScaleChanged
    """
    #  void QAudioEngine::distanceScaleChanged()
    self.uglySide.call('ritual_ZN12QAudioEngine20distanceScaleChangedEv')

  def start(self) -> None:
    """
    Calls Qt's 'void QAudioEngine::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioengine.html#start
    """
    #  void QAudioEngine::start()
    self.uglySide.call('ritual_ZN12QAudioEngine5startEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QAudioEngine::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioengine.html#stop
    """
    #  void QAudioEngine::stop()
    self.uglySide.call('ritual_ZN12QAudioEngine4stopEv')

  def pause(self) -> None:
    """
    Calls Qt's 'void QAudioEngine::pause()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioengine.html#pause
    """
    #  void QAudioEngine::pause()
    self.uglySide.call('ritual_ZN12QAudioEngine5pauseEv')

  def resume(self) -> None:
    """
    Calls Qt's 'void QAudioEngine::resume()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioengine.html#resume
    """
    #  void QAudioEngine::resume()
    self.uglySide.call('ritual_ZN12QAudioEngine6resumeEv')

  def d_func(self) -> Optional[QAudioEnginePrivate]:
    """
    Calls Qt's 'QAudioEnginePrivate *QAudioEngine::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioengine.html#d_func

    Returns
    -------

    Optional[QAudioEnginePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAudioEnginePrivate *QAudioEngine::d_func()
    address = self.uglySide.call('ritual_ZN12QAudioEngine6d_funcEv')
    from . import QAudioEnginePrivate
    return QAudioEnginePrivate._cuteAt(address)
