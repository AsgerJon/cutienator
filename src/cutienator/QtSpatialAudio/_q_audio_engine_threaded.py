"""
QAudioEngineThreaded binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSpatialAudio/6.12.0/QtSpatialAudio/private/qaudioengine_threaded_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QAudioEngineThreaded to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QAudioEnginePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtMultimedia import QAudioDevice
  from . import QSpatialAudioSoundPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioDevice = WAIT['QAudioDevice']
  QSpatialAudioSoundPrivate = WAIT['QSpatialAudioSoundPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAudioEngineThreaded(QAudioEnginePrivate):
  """
  The cute side of Qt's QAudioEngineThreaded: a plain Python object standing
  in front of one C++ QAudioEngineThreaded.

  It is built on the cute 'QAudioEnginePrivate', as Qt's QAudioEngineThreaded
  is built on Qt's QAudioEnginePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAudioEngineThreaded that has a ritual and that
  Python can call so far, 6 names in all: 'isPaused', 'setOutputDevice',
  'outputDevice', 'addSound', 'removeSound', 'updateRoomEffects'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    QAudioEngineThreaded::setSoundPlaybackData(QSpatialAudioSoundPrivate *a0,
    SharedPlaybackState a1)': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  9 of the 16 functions Qt declares: 4 forbidden; 3 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file; 2
  leans on 'QAudioEnginePrivate.

  What to expect
  --------------

  - The C++ QAudioEngineThreaded is created at the first use, not by
    'QAudioEngineThreaded(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAudioEngineThreaded.
  - Each name of Qt's QAudioEngineThreaded that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAudioEngineThreaded'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isPaused(self) -> bool:
    """
    Calls Qt's 'bool QAudioEngineThreaded::isPaused() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioenginethreaded.html#isPaused
    """
    #  bool QAudioEngineThreaded::isPaused() const
    return self.uglySide.call('ritual_ZNK20QAudioEngineThreaded8isPausedEv')

  def outputDevice(self) -> QAudioDevice:
    """
    Calls Qt's 'QAudioDevice QAudioEngineThreaded::outputDevice() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudioenginethreaded.html#outputDevice

    Returns
    -------

    QAudioDevice
      A new cute QAudioDevice around the copy Qt gave back. Python owns it.
    """
    #  QAudioDevice QAudioEngineThreaded::outputDevice() const
    address = self.uglySide.call(
        'ritual_ZNK20QAudioEngineThreaded12outputDeviceEv',
    )
    from ..QtMultimedia import QAudioDevice
    return QAudioDevice._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAudioDevice)
  def setOutputDevice(self, device: QAudioDevice) -> None:
    """
    Calls Qt's 'void QAudioEngineThreaded::setOutputDevice(const QAudioDevice
    &device)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudioenginethreaded.html#setOutputDevice

    Parameters
    ----------

    device : QAudioDevice
      Passed on as a value: Qt reads the C++ QAudioDevice, which stays
      Python's own.
    """
    #  void QAudioEngineThreaded::setOutputDevice(const QAudioDevice &device)
    self.uglySide.call(
        'ritual_ZN20QAudioEngineThreaded15setOutputDeviceERK12QAudioDevice',
        self._valueOf(device),
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
    Qt's 'QAudioEngineThreaded::QAudioEngineThreaded(int sampleRate)': leans
    on 'QAudioEnginePrivate::setOutputMode(QAudioEngine::OutputMode)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QAudioEngineThreaded.__init__' has no cute function yet. Qt's "
        "'QAudioEngineThreaded::QAudioEngineThreaded(int sampleRate)': "
        "leans on "
        "'QAudioEnginePrivate::setOutputMode(QAudioEngine::OutputMode)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  @overload(QSpatialAudioSoundPrivate)
  @overload(NoneType)
  def addSound(self, a0: Optional[QSpatialAudioSoundPrivate]) -> None:
    """
    Calls Qt's 'void QAudioEngineThreaded::addSound(QSpatialAudioSoundPrivate
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioenginethreaded.html#addSound

    Parameters
    ----------

    a0 : Optional[QSpatialAudioSoundPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAudioEngineThreaded::addSound(QSpatialAudioSoundPrivate *a0)
    self.uglySide.call(
        'ritual_ZN20QAudioEngineThreaded8addSoundEP25QSpatialAudioSoundPriv'
        'ate',
        self._addressOf(a0),
    )

  @overload(QSpatialAudioSoundPrivate)
  @overload(NoneType)
  def removeSound(self, a0: Optional[QSpatialAudioSoundPrivate]) -> None:
    """
    Calls Qt's 'void
    QAudioEngineThreaded::removeSound(QSpatialAudioSoundPrivate *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudioenginethreaded.html#removeSound

    Parameters
    ----------

    a0 : Optional[QSpatialAudioSoundPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAudioEngineThreaded::removeSound(QSpatialAudioSoundPrivate *a0)
    self.uglySide.call(
        'ritual_ZN20QAudioEngineThreaded11removeSoundEP25QSpatialAudioSound'
        'Private',
        self._addressOf(a0),
    )

  def updateRoomEffects(self) -> None:
    """
    Calls Qt's 'void QAudioEngineThreaded::updateRoomEffects()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudioenginethreaded.html#updateRoomEffects
    """
    #  void QAudioEngineThreaded::updateRoomEffects()
    self.uglySide.call(
        'ritual_ZN20QAudioEngineThreaded17updateRoomEffectsEv',
    )
