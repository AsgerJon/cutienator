"""
QAmbientSound binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSpatialAudio/qambientsound.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl
  from . import QAudioEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioEngine = WAIT['QAudioEngine']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAmbientSound(QObject):
  """
  The cute side of Qt's QAmbientSound: a plain Python object standing in
  front of one C++ QAmbientSound.

  It is built on the cute 'QObject', as Qt's QAmbientSound is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAmbientSound that has a ritual and that Python can
  call so far, 18 names in all: 'metaObject', 'tr', 'setSource', 'source',
  'loops', 'setLoops', 'autoPlay', 'setAutoPlay', 'setVolume', 'volume',
  'engine', 'sourceChanged', 'loopsChanged', 'autoPlayChanged',
  'volumeChanged', 'play', 'pause', 'stop'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAmbientSound::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QAmbientSound::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QAmbientSound::~QAmbientSound()': the destructor: Python never
    removes a C++ QAmbientSound.
  - Qt's 'QAmbientSoundPrivate *QAmbientSound::d_func()': gives
    'QAmbientSoundPrivate', which has no cute class yet.
  - Qt's 'const QAmbientSoundPrivate *QAmbientSound::d_func() const': gives
    'QAmbientSoundPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 26 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QAmbientSound is created at the first use, not by
    'QAmbientSound(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAmbientSound.
  - Qt tells when it has removed the C++ QAmbientSound. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QAmbientSound, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Loops(CuteNum):
    """
    The enum 'QAmbientSound::Loops' of Qt, with the 2 names Qt gives in it.
    """

    Infinite = Kee[int](-1)
    Once = Kee[int](1)

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
    Calls Qt's 'QString QAmbientSound::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qambientsound.html#tr

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
    #  QString QAmbientSound::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QAmbientSound2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAmbientSound'

  #  A C++ QAmbientSound Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAmbientSound'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAmbientSound::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qambientsound.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAmbientSound::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QAmbientSound10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QAmbientSound::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qambientsound.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QAmbientSound::source() const
    address = self.uglySide.call('ritual_ZNK13QAmbientSound6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def loops(self) -> int:
    """
    Calls Qt's 'int QAmbientSound::loops() const'.

    Qt's own words: https://doc.qt.io/qt-6/qambientsound.html#loops
    """
    #  int QAmbientSound::loops() const
    return self.uglySide.call('ritual_ZNK13QAmbientSound5loopsEv')

  def autoPlay(self) -> bool:
    """
    Calls Qt's 'bool QAmbientSound::autoPlay() const'.

    Qt's own words: https://doc.qt.io/qt-6/qambientsound.html#autoPlay
    """
    #  bool QAmbientSound::autoPlay() const
    return self.uglySide.call('ritual_ZNK13QAmbientSound8autoPlayEv')

  def volume(self) -> float:
    """
    Calls Qt's 'float QAmbientSound::volume() const'.

    Qt's own words: https://doc.qt.io/qt-6/qambientsound.html#volume
    """
    #  float QAmbientSound::volume() const
    return self.uglySide.call('ritual_ZNK13QAmbientSound6volumeEv')

  def engine(self) -> Optional[QAudioEngine]:
    """
    Calls Qt's 'QAudioEngine *QAmbientSound::engine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qambientsound.html#engine

    Returns
    -------

    Optional[QAudioEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAudioEngine *QAmbientSound::engine() const
    address = self.uglySide.call('ritual_ZNK13QAmbientSound6engineEv')
    from . import QAudioEngine
    return QAudioEngine._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QAmbientSound::setSource(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qambientsound.html#setSource

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QAmbientSound::setSource(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN13QAmbientSound9setSourceERK4QUrl', self._valueOf(url),
    )

  @overload(int)
  def setLoops(self, loops: int) -> None:
    """
    Calls Qt's 'void QAmbientSound::setLoops(int loops)'.

    Qt's own words: https://doc.qt.io/qt-6/qambientsound.html#setLoops

    Parameters
    ----------

    loops : int
      Passed on as it is.
    """
    #  void QAmbientSound::setLoops(int loops)
    self.uglySide.call('ritual_ZN13QAmbientSound8setLoopsEi', loops)

  @overload(bool)
  def setAutoPlay(self, autoPlay: bool) -> None:
    """
    Calls Qt's 'void QAmbientSound::setAutoPlay(bool autoPlay)'.

    Qt's own words: https://doc.qt.io/qt-6/qambientsound.html#setAutoPlay

    Parameters
    ----------

    autoPlay : bool
      Passed on as it is.
    """
    #  void QAmbientSound::setAutoPlay(bool autoPlay)
    self.uglySide.call('ritual_ZN13QAmbientSound11setAutoPlayEb', autoPlay)

  @overload(float)
  def setVolume(self, volume: float) -> None:
    """
    Calls Qt's 'void QAmbientSound::setVolume(float volume)'.

    Qt's own words: https://doc.qt.io/qt-6/qambientsound.html#setVolume

    Parameters
    ----------

    volume : float
      Passed on as it is.
    """
    #  void QAmbientSound::setVolume(float volume)
    self.uglySide.call('ritual_ZN13QAmbientSound9setVolumeEf', volume)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAudioEngine)
  @overload(NoneType)
  def __init__(self, engine: Optional[QAudioEngine]) -> None:
    """
    Notes what was given, for Qt's 'QAmbientSound::QAmbientSound(QAudioEngine
    *engine)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qambientsound.html#QAmbientSound

    Parameters
    ----------

    engine : Optional[QAudioEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAmbientSound::QAmbientSound(QAudioEngine *engine)
    self._noteCreation(QAmbientSound, lambda: Rituals.call(
        'ritual_ZN13QAmbientSoundC1EP12QAudioEngine',
        self._addressOf(engine),
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

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QAmbientSound::sourceChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qambientsound.html#sourceChanged
    """
    #  void QAmbientSound::sourceChanged()
    self.uglySide.call('ritual_ZN13QAmbientSound13sourceChangedEv')

  def loopsChanged(self) -> None:
    """
    Calls Qt's 'void QAmbientSound::loopsChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qambientsound.html#loopsChanged
    """
    #  void QAmbientSound::loopsChanged()
    self.uglySide.call('ritual_ZN13QAmbientSound12loopsChangedEv')

  def autoPlayChanged(self) -> None:
    """
    Calls Qt's 'void QAmbientSound::autoPlayChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qambientsound.html#autoPlayChanged
    """
    #  void QAmbientSound::autoPlayChanged()
    self.uglySide.call('ritual_ZN13QAmbientSound15autoPlayChangedEv')

  def volumeChanged(self) -> None:
    """
    Calls Qt's 'void QAmbientSound::volumeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qambientsound.html#volumeChanged
    """
    #  void QAmbientSound::volumeChanged()
    self.uglySide.call('ritual_ZN13QAmbientSound13volumeChangedEv')

  def play(self) -> None:
    """
    Calls Qt's 'void QAmbientSound::play()'.

    Qt's own words: https://doc.qt.io/qt-6/qambientsound.html#play
    """
    #  void QAmbientSound::play()
    self.uglySide.call('ritual_ZN13QAmbientSound4playEv')

  def pause(self) -> None:
    """
    Calls Qt's 'void QAmbientSound::pause()'.

    Qt's own words: https://doc.qt.io/qt-6/qambientsound.html#pause
    """
    #  void QAmbientSound::pause()
    self.uglySide.call('ritual_ZN13QAmbientSound5pauseEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QAmbientSound::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qambientsound.html#stop
    """
    #  void QAmbientSound::stop()
    self.uglySide.call('ritual_ZN13QAmbientSound4stopEv')
