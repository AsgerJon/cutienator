"""
QSpatialAudioSoundPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSpatialAudio/6.12.0/QtSpatialAudio/private/qspatialaudiosound_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QSpatialAudioSoundPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']


class QSpatialAudioSoundPrivate(QObjectPrivate):
  """
  The cute side of Qt's QSpatialAudioSoundPrivate: a plain Python object
  standing in front of one C++ QSpatialAudioSoundPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QSpatialAudioSoundPrivate
  is built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSpatialAudioSoundPrivate that has a ritual and that
  Python can call so far, 14 names in all: 'url', 'loadUrl', 'setVolume',
  'volume', 'loops', 'setLoops', 'autoPlay', 'setAutoPlay',
  'updateRoomEffects', 'play', 'pause', 'stop', 'state', 'applyVolume'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QSpatialAudioSoundPrivate::setState(SharedPlaybackState a0)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 19 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 a template;
  1 leans on 'QSpatialAudioSoundPrivate.

  What to expect
  --------------

  - The C++ QSpatialAudioSoundPrivate is created at the first use, not by
    'QSpatialAudioSoundPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSpatialAudioSoundPrivate.
  - Each name of Qt's QSpatialAudioSoundPrivate that has no cute function
    yet, '__init__', 'getAPI', 'setState', 'withResonanceApi', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSpatialAudioSoundPrivate, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class State(CuteNum, scoped=True):
    """
    The enum 'QSpatialAudioSoundPrivate::State' of Qt, with the 3 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Stopped = Kee[int](0)
    Playing = Kee[int](1)
    Paused = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSpatialAudioSoundPrivate'

  #  A C++ QSpatialAudioSoundPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSpatialAudioSoundPrivate'

  #  The functions Qt calls itself that QSpatialAudioSoundPrivate is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'updateRoomEffects': (
          ('_ZN25QSpatialAudioSoundPrivate17updateRoomEffectsEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'applyVolume': (
          ('_ZN25QSpatialAudioSoundPrivate11applyVolumeEv',
           ('nothing', 'nothing', ''),
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

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QSpatialAudioSoundPrivate::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialaudiosoundprivate.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QSpatialAudioSoundPrivate::url() const
    address = self.uglySide.call(
        'ritual_ZNK25QSpatialAudioSoundPrivate3urlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def volume(self) -> float:
    """
    Calls Qt's 'float QSpatialAudioSoundPrivate::volume() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialaudiosoundprivate.html#volume
    """
    #  float QSpatialAudioSoundPrivate::volume() const
    return self.uglySide.call(
        'ritual_ZNK25QSpatialAudioSoundPrivate6volumeEv',
    )

  def loops(self) -> int:
    """
    Calls Qt's 'int QSpatialAudioSoundPrivate::loops() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialaudiosoundprivate.html#loops
    """
    #  int QSpatialAudioSoundPrivate::loops() const
    return self.uglySide.call(
        'ritual_ZNK25QSpatialAudioSoundPrivate5loopsEv',
    )

  def autoPlay(self) -> bool:
    """
    Calls Qt's 'bool QSpatialAudioSoundPrivate::autoPlay() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialaudiosoundprivate.html#autoPlay
    """
    #  bool QSpatialAudioSoundPrivate::autoPlay() const
    return self.uglySide.call(
        'ritual_ZNK25QSpatialAudioSoundPrivate8autoPlayEv',
    )

  def state(self) -> State:
    """
    Calls Qt's 'State QSpatialAudioSoundPrivate::state() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialaudiosoundprivate.html#state

    Returns
    -------

    State
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'State(number)' gives.
    """
    #  State QSpatialAudioSoundPrivate::state() const
    return QSpatialAudioSoundPrivate.State(self.uglySide.call(
        'ritual_ZNK25QSpatialAudioSoundPrivate5stateEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setVolume(self, volume: float) -> None:
    """
    Calls Qt's 'void QSpatialAudioSoundPrivate::setVolume(float volume)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialaudiosoundprivate.html#setVolume

    Parameters
    ----------

    volume : float
      Passed on as it is.
    """
    #  void QSpatialAudioSoundPrivate::setVolume(float volume)
    self.uglySide.call(
        'ritual_ZN25QSpatialAudioSoundPrivate9setVolumeEf', volume,
    )

  @overload(int)
  def setLoops(self, a0: int) -> None:
    """
    Calls Qt's 'void QSpatialAudioSoundPrivate::setLoops(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialaudiosoundprivate.html#setLoops

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QSpatialAudioSoundPrivate::setLoops(int a0)
    self.uglySide.call('ritual_ZN25QSpatialAudioSoundPrivate8setLoopsEi', a0)

  @overload(bool)
  def setAutoPlay(self, a0: bool) -> None:
    """
    Calls Qt's 'void QSpatialAudioSoundPrivate::setAutoPlay(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialaudiosoundprivate.html#setAutoPlay

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QSpatialAudioSoundPrivate::setAutoPlay(bool a0)
    self.uglySide.call(
        'ritual_ZN25QSpatialAudioSoundPrivate11setAutoPlayEb', a0,
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
    Qt's 'QSpatialAudioSoundPrivate::QSpatialAudioSoundPrivate(QAudioEngine
    *engine, int nchannels, int sourceId)': leans on
    'QSpatialAudioSoundPrivate::applyVolume()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSpatialAudioSoundPrivate.__init__' has no cute function yet. "
        "Qt's "
        "'QSpatialAudioSoundPrivate::QSpatialAudioSoundPrivate(QAudioEngine "
        "*engine, int nchannels, int sourceId)': leans on "
        "'QSpatialAudioSoundPrivate::applyVolume()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  @overload(QUrl)
  def loadUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QSpatialAudioSoundPrivate::loadUrl(const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialaudiosoundprivate.html#loadUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QSpatialAudioSoundPrivate::loadUrl(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN25QSpatialAudioSoundPrivate7loadUrlERK4QUrl',
        self._valueOf(url),
    )

  def updateRoomEffects(self) -> None:
    """
    Calls Qt's 'void QSpatialAudioSoundPrivate::updateRoomEffects()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialaudiosoundprivate.html#updateRoomEffects
    """
    #  void QSpatialAudioSoundPrivate::updateRoomEffects()
    ritual = 'ritual_ZN25QSpatialAudioSoundPrivate17updateRoomEffectsEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QSpatialAudioSoundPrivate17updateRoomEffectsEv')
    self.uglySide.call(ritual)

  def play(self) -> None:
    """
    Calls Qt's 'void QSpatialAudioSoundPrivate::play()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialaudiosoundprivate.html#play
    """
    #  void QSpatialAudioSoundPrivate::play()
    self.uglySide.call('ritual_ZN25QSpatialAudioSoundPrivate4playEv')

  def pause(self) -> None:
    """
    Calls Qt's 'void QSpatialAudioSoundPrivate::pause()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialaudiosoundprivate.html#pause
    """
    #  void QSpatialAudioSoundPrivate::pause()
    self.uglySide.call('ritual_ZN25QSpatialAudioSoundPrivate5pauseEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QSpatialAudioSoundPrivate::stop()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialaudiosoundprivate.html#stop
    """
    #  void QSpatialAudioSoundPrivate::stop()
    self.uglySide.call('ritual_ZN25QSpatialAudioSoundPrivate4stopEv')

  def applyVolume(self) -> None:
    """
    Calls Qt's 'void QSpatialAudioSoundPrivate::applyVolume()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialaudiosoundprivate.html#applyVolume
    """
    #  void QSpatialAudioSoundPrivate::applyVolume()
    self.uglySide.call('ritual_ZN25QSpatialAudioSoundPrivate11applyVolumeEv')

  @staticmethod
  def getAPI(*__, **_) -> Never:
    """
    Qt's 'vraudio::ResonanceAudioApi *QSpatialAudioSoundPrivate::getAPI()':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'element_type' (aka 'vraudio::ResonanceAudio').
    """
    raise NotImplementedError(
        "'QSpatialAudioSoundPrivate.getAPI' has no cute function yet. Qt's "
        "'vraudio::ResonanceAudioApi *QSpatialAudioSoundPrivate::getAPI()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'element_type' (aka 'vraudio::ResonanceAudio').")

  @staticmethod
  def setState(*__, **_) -> Never:
    """
    Qt's 'void QSpatialAudioSoundPrivate::setState(SharedPlaybackState a0)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSpatialAudioSoundPrivate.setState' has no cute function yet. "
        "Qt's 'void QSpatialAudioSoundPrivate::setState(SharedPlaybackState "
        "a0)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def withResonanceApi(*__, **_) -> Never:
    """
    Qt's 'QSpatialAudioSoundPrivate::withResonanceApi': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QSpatialAudioSoundPrivate.withResonanceApi' has no cute function "
        "yet. Qt's 'QSpatialAudioSoundPrivate::withResonanceApi': a "
        "template: a pattern and no single function.")
