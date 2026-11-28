"""
QAudioEnginePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSpatialAudio/6.12.0/QtSpatialAudio/private/qaudioengine_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QAudioEnginePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import QAudioEngine

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtMultimedia import QAudioDevice
  from . import QAudioRoom, QSpatialAudioSoundPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioDevice = WAIT['QAudioDevice']
  QAudioRoom = WAIT['QAudioRoom']
  QSpatialAudioSoundPrivate = WAIT['QSpatialAudioSoundPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAudioEnginePrivate(QObjectPrivate):
  """
  The cute side of Qt's QAudioEnginePrivate: a plain Python object standing
  in front of one C++ QAudioEnginePrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QAudioEnginePrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAudioEnginePrivate that has a ritual and that
  Python can call so far, 20 names in all: 'q_func', 'get', 'sampleRate',
  'setDistanceScale', 'distanceScale', 'masterVolume', 'setOutputMode',
  'outputMode', 'addRoom', 'removeRoom', 'currentRoom', 'updateRoomEffects',
  'start', 'stop', 'setPaused', 'isPaused', 'setOutputDevice',
  'outputDevice', 'addSound', 'removeSound'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAudioEngine *QAudioEnginePrivate::q_func() const': takes in
    Python what 'QAudioEngine *QAudioEnginePrivate::q_func()' takes.
  - Qt's 'QAudioEnginePrivate::~QAudioEnginePrivate()': the destructor:
    Python never removes a C++ QAudioEnginePrivate.
  - Qt's 'std::optional<QVector3D> QAudioEnginePrivate::listenerPosition()
    const': gives a type Python has no way to take yet.
  - Qt's 'void
    QAudioEnginePrivate::setSoundPlaybackData(QSpatialAudioSoundPrivate *a0,
    SharedPlaybackState a1)': takes a type Python has no way to hand over
    yet.
  - Qt's 'SmallestRoomForListenerResult
    QAudioEnginePrivate::findSmallestRoomForListener(QSpan<QAudioRoom *>
    rooms) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  7 of the 32 functions Qt declares: 6 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 the class
  is abstract, so C++ cannot make one, and the C++ class of ours does not
  fill in every function it leaves open.

  What to expect
  --------------

  - The C++ QAudioEnginePrivate is created at the first use, not by
    'QAudioEnginePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAudioEnginePrivate.
  - Each name of Qt's QAudioEnginePrivate that has no cute function yet,
    '__init__', 'findSmallestRoomForListener', 'listenerPosition',
    'roomEffectsEnabled', 'setListenerPosition', 'setListenerRotation',
    'setMasterVolume', 'setRoomEffectsEnabled', 'setSoundPlaybackData',
    'updateRooms', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QAudioEngine)
  @overload(NoneType)
  def get(engine: Optional[QAudioEngine]) -> Optional[QAudioEnginePrivate]:
    """
    Calls Qt's 'QAudioEnginePrivate *QAudioEnginePrivate::get(QAudioEngine
    *engine)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioengineprivate.html#get

    Parameters
    ----------

    engine : Optional[QAudioEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAudioEnginePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAudioEnginePrivate *QAudioEnginePrivate::get(QAudioEngine *engine)
    address = Rituals.call(
        'ritual_ZN19QAudioEnginePrivate3getEP12QAudioEngine',
        CuteMixin._addressOf(engine),
    )
    return QAudioEnginePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAudioEnginePrivate'

  #  A C++ QAudioEnginePrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAudioEnginePrivate'

  #  The functions Qt calls itself that QAudioEnginePrivate is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'setSoundPlaybackData': (
          'void '
          'QAudioEnginePrivate::setSoundPlaybackData(QSpatialAudioSoundPriv'
          'ate *, SharedPlaybackState)',
      ),
  }

  #  The functions Qt calls itself that QAudioEnginePrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setOutputMode': (
          ('_ZN19QAudioEnginePrivate13setOutputModeEN12QAudioEngine10Output'
           'ModeE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtSpatialAudio:QAudioEngine.OutputMode'),
           )),
      ),
      'updateRoomEffects': (
          ('_ZN19QAudioEnginePrivate17updateRoomEffectsEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'start': (
          ('_ZN19QAudioEnginePrivate5startEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'stop': (
          ('_ZN19QAudioEnginePrivate4stopEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'setPaused': (
          ('_ZN19QAudioEnginePrivate9setPausedEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'isPaused': (
          ('_ZNK19QAudioEnginePrivate8isPausedEv',
           ('bool', 'number', ''),
           ()),
      ),
      'setOutputDevice': (
          ('_ZN19QAudioEnginePrivate15setOutputDeviceERK12QAudioDevice',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtMultimedia:QAudioDevice'),
           )),
      ),
      'outputDevice': (
          ('_ZNK19QAudioEnginePrivate12outputDeviceEv',
           ('address', 'value', 'QtMultimedia:QAudioDevice'),
           ()),
      ),
      'addSound': (
          ('_ZN19QAudioEnginePrivate8addSoundEP25QSpatialAudioSoundPrivate',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtSpatialAudio:QSpatialAudioSoundPrivate'),
           )),
      ),
      'removeSound': (
          ('_ZN19QAudioEnginePrivate11removeSoundEP25QSpatialAudioSoundPriv'
           'ate',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtSpatialAudio:QSpatialAudioSoundPrivate'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def sampleRate(self) -> int:
    """
    Calls Qt's 'int QAudioEnginePrivate::sampleRate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudioengineprivate.html#sampleRate
    """
    #  int QAudioEnginePrivate::sampleRate() const
    return self.uglySide.call(
        'ritual_ZNK19QAudioEnginePrivate10sampleRateEv',
    )

  def distanceScale(self) -> float:
    """
    Calls Qt's 'float QAudioEnginePrivate::distanceScale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudioengineprivate.html#distanceScale
    """
    #  float QAudioEnginePrivate::distanceScale() const
    return self.uglySide.call(
        'ritual_ZNK19QAudioEnginePrivate13distanceScaleEv',
    )

  def masterVolume(self) -> float:
    """
    Calls Qt's 'float QAudioEnginePrivate::masterVolume() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudioengineprivate.html#masterVolume
    """
    #  float QAudioEnginePrivate::masterVolume() const
    return self.uglySide.call(
        'ritual_ZNK19QAudioEnginePrivate12masterVolumeEv',
    )

  def outputMode(self) -> QAudioEngine.OutputMode:
    """
    Calls Qt's 'QAudioEngine::OutputMode QAudioEnginePrivate::outputMode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudioengineprivate.html#outputMode

    Returns
    -------

    QAudioEngine.OutputMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAudioEngine.OutputMode(number)' gives.
    """
    #  QAudioEngine::OutputMode QAudioEnginePrivate::outputMode() const
    return QAudioEngine.OutputMode(self.uglySide.call(
        'ritual_ZNK19QAudioEnginePrivate10outputModeEv',
    ))

  def currentRoom(self) -> Optional[QAudioRoom]:
    """
    Calls Qt's 'QAudioRoom *QAudioEnginePrivate::currentRoom() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudioengineprivate.html#currentRoom

    Returns
    -------

    Optional[QAudioRoom]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAudioRoom *QAudioEnginePrivate::currentRoom() const
    address = self.uglySide.call(
        'ritual_ZNK19QAudioEnginePrivate11currentRoomEv',
    )
    from . import QAudioRoom
    return QAudioRoom._cuteAt(address)

  def isPaused(self) -> bool:
    """
    Calls Qt's 'bool QAudioEnginePrivate::isPaused() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioengineprivate.html#isPaused
    """
    #  bool QAudioEnginePrivate::isPaused() const
    return self.uglySide.call('ritual_ZNK19QAudioEnginePrivate8isPausedEv')

  def outputDevice(self) -> QAudioDevice:
    """
    Calls Qt's 'QAudioDevice QAudioEnginePrivate::outputDevice() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudioengineprivate.html#outputDevice

    Returns
    -------

    QAudioDevice
      A new cute QAudioDevice around the copy Qt gave back. Python owns it.
    """
    #  QAudioDevice QAudioEnginePrivate::outputDevice() const
    address = self.uglySide.call(
        'ritual_ZNK19QAudioEnginePrivate12outputDeviceEv',
    )
    from ..QtMultimedia import QAudioDevice
    return QAudioDevice._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setDistanceScale(self, scale: float) -> None:
    """
    Calls Qt's 'void QAudioEnginePrivate::setDistanceScale(float scale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudioengineprivate.html#setDistanceScale

    Parameters
    ----------

    scale : float
      Passed on as it is.
    """
    #  void QAudioEnginePrivate::setDistanceScale(float scale)
    self.uglySide.call(
        'ritual_ZN19QAudioEnginePrivate16setDistanceScaleEf', scale,
    )

  @overload(QAudioEngine.OutputMode)
  def setOutputMode(self, a0: QAudioEngine.OutputMode) -> None:
    """
    Calls Qt's 'void
    QAudioEnginePrivate::setOutputMode(QAudioEngine::OutputMode a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudioengineprivate.html#setOutputMode

    Parameters
    ----------

    a0 : QAudioEngine.OutputMode
      Passed on as its number.
    """
    #  void QAudioEnginePrivate::setOutputMode(QAudioEngine::OutputMode a0)
    self.uglySide.call(
        'ritual_ZN19QAudioEnginePrivate13setOutputModeEN12QAudioEngine10Out'
        'putModeE',
        a0.value,
    )

  @overload(bool)
  def setPaused(self, a0: bool) -> None:
    """
    Calls Qt's 'void QAudioEnginePrivate::setPaused(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioengineprivate.html#setPaused

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QAudioEnginePrivate::setPaused(bool a0)
    self.uglySide.call('ritual_ZN19QAudioEnginePrivate9setPausedEb', a0)

  @overload(QAudioDevice)
  def setOutputDevice(self, a0: QAudioDevice) -> None:
    """
    Calls Qt's 'void QAudioEnginePrivate::setOutputDevice(const QAudioDevice
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudioengineprivate.html#setOutputDevice

    Parameters
    ----------

    a0 : QAudioDevice
      Passed on as a value: Qt reads the C++ QAudioDevice, which stays
      Python's own.
    """
    #  void QAudioEnginePrivate::setOutputDevice(const QAudioDevice &a0)
    self.uglySide.call(
        'ritual_ZN19QAudioEnginePrivate15setOutputDeviceERK12QAudioDevice',
        self._valueOf(a0),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QAudioEnginePrivate::QAudioEnginePrivate(int sampleRate)': the
    class is abstract, so C++ cannot make one, and the C++ class of ours does
    not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QAudioEnginePrivate.__init__' has no cute function yet. Qt's "
        "'QAudioEnginePrivate::QAudioEnginePrivate(int sampleRate)': the "
        "class is abstract, so C++ cannot make one, and the C++ class of "
        "ours does not fill in every function it leaves open.")

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

  def q_func(self) -> Optional[QAudioEngine]:
    """
    Calls Qt's 'QAudioEngine *QAudioEnginePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioengineprivate.html#q_func

    Returns
    -------

    Optional[QAudioEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAudioEngine *QAudioEnginePrivate::q_func()
    address = self.uglySide.call('ritual_ZN19QAudioEnginePrivate6q_funcEv')
    return QAudioEngine._cuteAt(address)

  @overload(QAudioRoom)
  @overload(NoneType)
  def addRoom(self, a0: Optional[QAudioRoom]) -> None:
    """
    Calls Qt's 'void QAudioEnginePrivate::addRoom(QAudioRoom *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioengineprivate.html#addRoom

    Parameters
    ----------

    a0 : Optional[QAudioRoom]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAudioEnginePrivate::addRoom(QAudioRoom *a0)
    self.uglySide.call(
        'ritual_ZN19QAudioEnginePrivate7addRoomEP10QAudioRoom',
        self._addressOf(a0),
    )

  @overload(QAudioRoom)
  @overload(NoneType)
  def removeRoom(self, a0: Optional[QAudioRoom]) -> None:
    """
    Calls Qt's 'void QAudioEnginePrivate::removeRoom(QAudioRoom *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudioengineprivate.html#removeRoom

    Parameters
    ----------

    a0 : Optional[QAudioRoom]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAudioEnginePrivate::removeRoom(QAudioRoom *a0)
    self.uglySide.call(
        'ritual_ZN19QAudioEnginePrivate10removeRoomEP10QAudioRoom',
        self._addressOf(a0),
    )

  def updateRoomEffects(self) -> None:
    """
    Calls Qt's 'void QAudioEnginePrivate::updateRoomEffects()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudioengineprivate.html#updateRoomEffects
    """
    #  void QAudioEnginePrivate::updateRoomEffects()
    self.uglySide.call('ritual_ZN19QAudioEnginePrivate17updateRoomEffectsEv')

  def start(self) -> None:
    """
    Calls Qt's 'void QAudioEnginePrivate::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioengineprivate.html#start
    """
    #  void QAudioEnginePrivate::start()
    self.uglySide.call('ritual_ZN19QAudioEnginePrivate5startEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QAudioEnginePrivate::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioengineprivate.html#stop
    """
    #  void QAudioEnginePrivate::stop()
    self.uglySide.call('ritual_ZN19QAudioEnginePrivate4stopEv')

  @overload(QSpatialAudioSoundPrivate)
  @overload(NoneType)
  def addSound(self, a0: Optional[QSpatialAudioSoundPrivate]) -> None:
    """
    Calls Qt's 'void QAudioEnginePrivate::addSound(QSpatialAudioSoundPrivate
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioengineprivate.html#addSound

    Parameters
    ----------

    a0 : Optional[QSpatialAudioSoundPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAudioEnginePrivate::addSound(QSpatialAudioSoundPrivate *a0)
    self.uglySide.call(
        'ritual_ZN19QAudioEnginePrivate8addSoundEP25QSpatialAudioSoundPriva'
        'te',
        self._addressOf(a0),
    )

  @overload(QSpatialAudioSoundPrivate)
  @overload(NoneType)
  def removeSound(self, a0: Optional[QSpatialAudioSoundPrivate]) -> None:
    """
    Calls Qt's 'void
    QAudioEnginePrivate::removeSound(QSpatialAudioSoundPrivate *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudioengineprivate.html#removeSound

    Parameters
    ----------

    a0 : Optional[QSpatialAudioSoundPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAudioEnginePrivate::removeSound(QSpatialAudioSoundPrivate *a0)
    self.uglySide.call(
        'ritual_ZN19QAudioEnginePrivate11removeSoundEP25QSpatialAudioSoundP'
        'rivate',
        self._addressOf(a0),
    )

  @staticmethod
  def findSmallestRoomForListener(*__, **_) -> Never:
    """
    Qt's 'SmallestRoomForListenerResult
    QAudioEnginePrivate::findSmallestRoomForListener(QSpan<QAudioRoom *>
    rooms) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAudioEnginePrivate.findSmallestRoomForListener' has no cute "
        "function yet. Qt's 'SmallestRoomForListenerResult "
        "QAudioEnginePrivate::findSmallestRoomForListener(QSpan<QAudioRoom "
        "*> rooms) const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def listenerPosition(*__, **_) -> Never:
    """
    Qt's 'std::optional<QVector3D> QAudioEnginePrivate::listenerPosition()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAudioEnginePrivate.listenerPosition' has no cute function yet. "
        "Qt's 'std::optional<QVector3D> "
        "QAudioEnginePrivate::listenerPosition() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def roomEffectsEnabled(*__, **_) -> Never:
    """
    Qt's 'bool QAudioEnginePrivate::roomEffectsEnabled() const': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type 'element_type' (aka
    'vraudio::ResonanceAudio').
    """
    raise NotImplementedError(
        "'QAudioEnginePrivate.roomEffectsEnabled' has no cute function yet. "
        "Qt's 'bool QAudioEnginePrivate::roomEffectsEnabled() const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'element_type' (aka 'vraudio::ResonanceAudio').")

  @staticmethod
  def setListenerPosition(*__, **_) -> Never:
    """
    Qt's 'void
    QAudioEnginePrivate::setListenerPosition(std::optional<QVector3D> a0)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'element_type' (aka 'vraudio::ResonanceAudio').
    """
    raise NotImplementedError(
        "'QAudioEnginePrivate.setListenerPosition' has no cute function "
        "yet. Qt's 'void "
        "QAudioEnginePrivate::setListenerPosition(std::optional<QVector3D> "
        "a0)': Qt's library has no name for it, and its code in Qt's source "
        "does not compile apart from its file: member access into "
        "incomplete type 'element_type' (aka 'vraudio::ResonanceAudio').")

  @staticmethod
  def setListenerRotation(*__, **_) -> Never:
    """
    Qt's 'void QAudioEnginePrivate::setListenerRotation(const QQuaternion
    &a0)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: member access into incomplete type
    'element_type' (aka 'vraudio::ResonanceAudio').
    """
    raise NotImplementedError(
        "'QAudioEnginePrivate.setListenerRotation' has no cute function "
        "yet. Qt's 'void QAudioEnginePrivate::setListenerRotation(const "
        "QQuaternion &a0)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: member access "
        "into incomplete type 'element_type' (aka "
        "'vraudio::ResonanceAudio').")

  @staticmethod
  def setMasterVolume(*__, **_) -> Never:
    """
    Qt's 'void QAudioEnginePrivate::setMasterVolume(float a0)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type 'element_type' (aka
    'vraudio::ResonanceAudio').
    """
    raise NotImplementedError(
        "'QAudioEnginePrivate.setMasterVolume' has no cute function yet. "
        "Qt's 'void QAudioEnginePrivate::setMasterVolume(float a0)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'element_type' (aka 'vraudio::ResonanceAudio').")

  @staticmethod
  def setRoomEffectsEnabled(*__, **_) -> Never:
    """
    Qt's 'void QAudioEnginePrivate::setRoomEffectsEnabled(bool a0)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type 'element_type'
    (aka 'vraudio::ResonanceAudio').
    """
    raise NotImplementedError(
        "'QAudioEnginePrivate.setRoomEffectsEnabled' has no cute function "
        "yet. Qt's 'void QAudioEnginePrivate::setRoomEffectsEnabled(bool "
        "a0)': Qt's library has no name for it, and its code in Qt's source "
        "does not compile apart from its file: member access into "
        "incomplete type 'element_type' (aka 'vraudio::ResonanceAudio').")

  @staticmethod
  def setSoundPlaybackData(*__, **_) -> Never:
    """
    Qt's 'void
    QAudioEnginePrivate::setSoundPlaybackData(QSpatialAudioSoundPrivate *a0,
    SharedPlaybackState a1)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QAudioEnginePrivate.setSoundPlaybackData' has no cute function "
        "yet. Qt's 'void "
        "QAudioEnginePrivate::setSoundPlaybackData(QSpatialAudioSoundPrivate"
        " *a0, SharedPlaybackState a1)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def updateRooms(*__, **_) -> Never:
    """
    Qt's 'void QAudioEnginePrivate::updateRooms()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    incomplete type 'QAudioRoomPrivate' named in nested name specifier.
    """
    raise NotImplementedError(
        "'QAudioEnginePrivate.updateRooms' has no cute function yet. Qt's "
        "'void QAudioEnginePrivate::updateRooms()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: incomplete type 'QAudioRoomPrivate' named in nested "
        "name specifier.")
