"""
QSoundEffectPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qsoundeffect_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSoundEffectPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import QSoundEffect

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QUrl
  from . import QAudioDevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioDevice = WAIT['QAudioDevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSoundEffectPrivate(QObjectPrivate):
  """
  The cute side of Qt's QSoundEffectPrivate: a plain Python object standing
  in front of one C++ QSoundEffectPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QSoundEffectPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSoundEffectPrivate that has a ritual and that
  Python can call so far, 15 names in all: 'setAudioDevice', 'audioDevice',
  'url', 'status', 'loopCount', 'setLoopCount', 'loopsRemaining', 'volume',
  'setVolume', 'muted', 'setMuted', 'play', 'stop', 'playing', 'get'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QSoundEffectPrivate::resolveAndSetSource(const QUrl &a0,
    QSampleCache &a1)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSoundEffectPrivate::setSource(QUrl a0, QSampleCache &a1)':
    takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSoundEffectPrivate is created at the first use, not by
    'QSoundEffectPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSoundEffectPrivate.
  - Each name of Qt's QSoundEffectPrivate that has no cute function yet,
    'resolveAndSetSource', 'setSource', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QSoundEffect)
  @overload(NoneType)
  def get(a0: Optional[QSoundEffect]) -> Optional[QSoundEffectPrivate]:
    """
    Calls Qt's 'QSoundEffectPrivate *QSoundEffectPrivate::get(QSoundEffect
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffectprivate.html#get

    Parameters
    ----------

    a0 : Optional[QSoundEffect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSoundEffectPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSoundEffectPrivate *QSoundEffectPrivate::get(QSoundEffect *a0)
    address = Rituals.call(
        'ritual_ZN19QSoundEffectPrivate3getEP12QSoundEffect',
        CuteMixin._addressOf(a0),
    )
    return QSoundEffectPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSoundEffectPrivate'

  #  The functions Qt calls itself that QSoundEffectPrivate is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'setSource': (
          'void QSoundEffectPrivate::setSource(QUrl, QSampleCache &)',
      ),
  }

  #  The functions Qt calls itself that QSoundEffectPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setAudioDevice': (
          ('_ZN19QSoundEffectPrivate14setAudioDeviceE12QAudioDevice',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtMultimedia:QAudioDevice'),
           )),
      ),
      'audioDevice': (
          ('_ZNK19QSoundEffectPrivate11audioDeviceEv',
           ('address', 'value', 'QtMultimedia:QAudioDevice'),
           ()),
      ),
      'status': (
          ('_ZNK19QSoundEffectPrivate6statusEv',
           ('int', 'enum', 'QtMultimedia:QSoundEffect.Status'),
           ()),
      ),
      'loopCount': (
          ('_ZNK19QSoundEffectPrivate9loopCountEv',
           ('int', 'number', ''),
           ()),
      ),
      'setLoopCount': (
          ('_ZN19QSoundEffectPrivate12setLoopCountEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'loopsRemaining': (
          ('_ZNK19QSoundEffectPrivate14loopsRemainingEv',
           ('int', 'number', ''),
           ()),
      ),
      'volume': (
          ('_ZNK19QSoundEffectPrivate6volumeEv',
           ('float', 'number', ''),
           ()),
      ),
      'setVolume': (
          ('_ZN19QSoundEffectPrivate9setVolumeEf',
           ('bool', 'number', ''),
           (
               ('float', 'number', ''),
           )),
      ),
      'muted': (
          ('_ZNK19QSoundEffectPrivate5mutedEv',
           ('bool', 'number', ''),
           ()),
      ),
      'setMuted': (
          ('_ZN19QSoundEffectPrivate8setMutedEb',
           ('bool', 'number', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'play': (
          ('_ZN19QSoundEffectPrivate4playEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'stop': (
          ('_ZN19QSoundEffectPrivate4stopEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'playing': (
          ('_ZNK19QSoundEffectPrivate7playingEv',
           ('bool', 'number', ''),
           ()),
      ),
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
    Calls Qt's 'QAudioDevice QSoundEffectPrivate::audioDevice() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsoundeffectprivate.html#audioDevice

    Returns
    -------

    QAudioDevice
      A new cute QAudioDevice around the copy Qt gave back. Python owns it.
    """
    #  QAudioDevice QSoundEffectPrivate::audioDevice() const
    address = self._callAs(
        'QSoundEffectPrivate',
        'ritual_ZNK19QSoundEffectPrivate11audioDeviceEv',
    )
    from . import QAudioDevice
    return QAudioDevice._cuteOwning(address)

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QSoundEffectPrivate::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffectprivate.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QSoundEffectPrivate::url() const
    address = self._callAs(
        'QSoundEffectPrivate', 'ritual_ZNK19QSoundEffectPrivate3urlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def status(self) -> QSoundEffect.Status:
    """
    Calls Qt's 'QSoundEffect::Status QSoundEffectPrivate::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffectprivate.html#status

    Returns
    -------

    QSoundEffect.Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSoundEffect.Status(number)' gives.
    """
    #  QSoundEffect::Status QSoundEffectPrivate::status() const
    return QSoundEffect.Status(self._callAs(
        'QSoundEffectPrivate', 'ritual_ZNK19QSoundEffectPrivate6statusEv',
    ))

  def loopCount(self) -> int:
    """
    Calls Qt's 'int QSoundEffectPrivate::loopCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffectprivate.html#loopCount
    """
    #  int QSoundEffectPrivate::loopCount() const
    return self._callAs(
        'QSoundEffectPrivate', 'ritual_ZNK19QSoundEffectPrivate9loopCountEv',
    )

  def loopsRemaining(self) -> int:
    """
    Calls Qt's 'int QSoundEffectPrivate::loopsRemaining() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsoundeffectprivate.html#loopsRemaining
    """
    #  int QSoundEffectPrivate::loopsRemaining() const
    return self._callAs(
        'QSoundEffectPrivate',
        'ritual_ZNK19QSoundEffectPrivate14loopsRemainingEv',
    )

  def volume(self) -> float:
    """
    Calls Qt's 'float QSoundEffectPrivate::volume() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffectprivate.html#volume
    """
    #  float QSoundEffectPrivate::volume() const
    return self._callAs(
        'QSoundEffectPrivate', 'ritual_ZNK19QSoundEffectPrivate6volumeEv',
    )

  def muted(self) -> bool:
    """
    Calls Qt's 'bool QSoundEffectPrivate::muted() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffectprivate.html#muted
    """
    #  bool QSoundEffectPrivate::muted() const
    return self._callAs(
        'QSoundEffectPrivate', 'ritual_ZNK19QSoundEffectPrivate5mutedEv',
    )

  def playing(self) -> bool:
    """
    Calls Qt's 'bool QSoundEffectPrivate::playing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffectprivate.html#playing
    """
    #  bool QSoundEffectPrivate::playing() const
    return self._callAs(
        'QSoundEffectPrivate', 'ritual_ZNK19QSoundEffectPrivate7playingEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAudioDevice)
  def setAudioDevice(self, device: QAudioDevice) -> bool:
    """
    Calls Qt's 'bool QSoundEffectPrivate::setAudioDevice(QAudioDevice
    device)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsoundeffectprivate.html#setAudioDevice

    Parameters
    ----------

    device : QAudioDevice
      Passed on as a value: Qt reads the C++ QAudioDevice, which stays
      Python's own.
    """
    #  bool QSoundEffectPrivate::setAudioDevice(QAudioDevice device)
    return self._callAs(
        'QSoundEffectPrivate',
        'ritual_ZN19QSoundEffectPrivate14setAudioDeviceE12QAudioDevice',
        self._valueOf(device),
    )

  @overload(int)
  def setLoopCount(self, a0: int) -> bool:
    """
    Calls Qt's 'bool QSoundEffectPrivate::setLoopCount(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsoundeffectprivate.html#setLoopCount

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  bool QSoundEffectPrivate::setLoopCount(int a0)
    return self._callAs(
        'QSoundEffectPrivate',
        'ritual_ZN19QSoundEffectPrivate12setLoopCountEi',
        a0,
    )

  @overload(float)
  def setVolume(self, a0: float) -> bool:
    """
    Calls Qt's 'bool QSoundEffectPrivate::setVolume(float a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffectprivate.html#setVolume

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  bool QSoundEffectPrivate::setVolume(float a0)
    return self._callAs(
        'QSoundEffectPrivate', 'ritual_ZN19QSoundEffectPrivate9setVolumeEf',
        a0,
    )

  @overload(bool)
  def setMuted(self, a0: bool) -> bool:
    """
    Calls Qt's 'bool QSoundEffectPrivate::setMuted(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffectprivate.html#setMuted

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  bool QSoundEffectPrivate::setMuted(bool a0)
    return self._callAs(
        'QSoundEffectPrivate', 'ritual_ZN19QSoundEffectPrivate8setMutedEb',
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
    Calls Qt's 'void QSoundEffectPrivate::play()'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffectprivate.html#play
    """
    #  void QSoundEffectPrivate::play()
    self._callAs(
        'QSoundEffectPrivate', 'ritual_ZN19QSoundEffectPrivate4playEv',
    )

  def stop(self) -> None:
    """
    Calls Qt's 'void QSoundEffectPrivate::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qsoundeffectprivate.html#stop
    """
    #  void QSoundEffectPrivate::stop()
    self._callAs(
        'QSoundEffectPrivate', 'ritual_ZN19QSoundEffectPrivate4stopEv',
    )

  @staticmethod
  def resolveAndSetSource(*__, **_) -> Never:
    """
    Qt's 'void QSoundEffectPrivate::resolveAndSetSource(const QUrl &a0,
    QSampleCache &a1)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSoundEffectPrivate.resolveAndSetSource' has no cute function "
        "yet. Qt's 'void QSoundEffectPrivate::resolveAndSetSource(const "
        "QUrl &a0, QSampleCache &a1)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def setSource(*__, **_) -> Never:
    """
    Qt's 'void QSoundEffectPrivate::setSource(QUrl a0, QSampleCache &a1)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSoundEffectPrivate.setSource' has no cute function yet. Qt's "
        "'void QSoundEffectPrivate::setSource(QUrl a0, QSampleCache &a1)': "
        "takes a type Python has no way to hand over yet.")
