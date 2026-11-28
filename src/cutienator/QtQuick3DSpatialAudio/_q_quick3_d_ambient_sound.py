"""
QQuick3DAmbientSound binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DSpatialAudio/6.12.0/QtQuick3DSpatialAudio/private/qquick3dambientsound_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DAmbientSound to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']


class QQuick3DAmbientSound(QObject):
  """
  The cute side of Qt's QQuick3DAmbientSound: a plain Python object standing
  in front of one C++ QQuick3DAmbientSound.

  It is built on the cute 'QObject', as Qt's QQuick3DAmbientSound is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DAmbientSound that has a ritual and that
  Python can call so far, 16 names in all: 'metaObject', 'setSource',
  'source', 'setVolume', 'volume', 'loops', 'setLoops', 'autoPlay',
  'setAutoPlay', 'play', 'pause', 'stop', 'sourceChanged', 'volumeChanged',
  'loopsChanged', 'autoPlayChanged'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DAmbientSound::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DAmbientSound::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DAmbientSound::~QQuick3DAmbientSound()': the destructor:
    Python never removes a C++ QQuick3DAmbientSound.

  What has no ritual
  ------------------

  4 of the 23 functions Qt declares: 2 not a gap; 2 leans on
  'QQuick3DAmbientSound.

  What to expect
  --------------

  - The C++ QQuick3DAmbientSound is created at the first use, not by
    'QQuick3DAmbientSound(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DAmbientSound.
  - Qt tells when it has removed the C++ QQuick3DAmbientSound. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DAmbientSound that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QQuick3DAmbientSound, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Loops(CuteNum):
    """
    The enum 'QQuick3DAmbientSound::Loops' of Qt, with the 2 names Qt gives
    in it.
    """

    Infinite = Kee[int](-1)
    Once = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DAmbientSound'

  #  A C++ QQuick3DAmbientSound Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DAmbientSound'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DAmbientSound::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dambientsound.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DAmbientSound::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuick3DAmbientSound10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuick3DAmbientSound::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dambientsound.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuick3DAmbientSound::source() const
    address = self.uglySide.call('ritual_ZNK20QQuick3DAmbientSound6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def volume(self) -> float:
    """
    Calls Qt's 'float QQuick3DAmbientSound::volume() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dambientsound.html#volume
    """
    #  float QQuick3DAmbientSound::volume() const
    return self.uglySide.call('ritual_ZNK20QQuick3DAmbientSound6volumeEv')

  def loops(self) -> int:
    """
    Calls Qt's 'int QQuick3DAmbientSound::loops() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dambientsound.html#loops
    """
    #  int QQuick3DAmbientSound::loops() const
    return self.uglySide.call('ritual_ZNK20QQuick3DAmbientSound5loopsEv')

  def autoPlay(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DAmbientSound::autoPlay() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dambientsound.html#autoPlay
    """
    #  bool QQuick3DAmbientSound::autoPlay() const
    return self.uglySide.call('ritual_ZNK20QQuick3DAmbientSound8autoPlayEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, source: QUrl) -> None:
    """
    Calls Qt's 'void QQuick3DAmbientSound::setSource(const QUrl &source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dambientsound.html#setSource

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuick3DAmbientSound::setSource(const QUrl &source)
    self.uglySide.call(
        'ritual_ZN20QQuick3DAmbientSound9setSourceERK4QUrl',
        self._valueOf(source),
    )

  @overload(float)
  def setVolume(self, volume: float) -> None:
    """
    Calls Qt's 'void QQuick3DAmbientSound::setVolume(float volume)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dambientsound.html#setVolume

    Parameters
    ----------

    volume : float
      Passed on as it is.
    """
    #  void QQuick3DAmbientSound::setVolume(float volume)
    self.uglySide.call('ritual_ZN20QQuick3DAmbientSound9setVolumeEf', volume)

  @overload(int)
  def setLoops(self, loops: int) -> None:
    """
    Calls Qt's 'void QQuick3DAmbientSound::setLoops(int loops)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dambientsound.html#setLoops

    Parameters
    ----------

    loops : int
      Passed on as it is.
    """
    #  void QQuick3DAmbientSound::setLoops(int loops)
    self.uglySide.call('ritual_ZN20QQuick3DAmbientSound8setLoopsEi', loops)

  @overload(bool)
  def setAutoPlay(self, autoPlay: bool) -> None:
    """
    Calls Qt's 'void QQuick3DAmbientSound::setAutoPlay(bool autoPlay)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dambientsound.html#setAutoPlay

    Parameters
    ----------

    autoPlay : bool
      Passed on as it is.
    """
    #  void QQuick3DAmbientSound::setAutoPlay(bool autoPlay)
    self.uglySide.call(
        'ritual_ZN20QQuick3DAmbientSound11setAutoPlayEb', autoPlay,
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
    Qt's 'QQuick3DAmbientSound::QQuick3DAmbientSound()': leans on
    'QQuick3DAmbientSound::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DAmbientSound.__init__' has no cute function yet. Qt's "
        "'QQuick3DAmbientSound::QQuick3DAmbientSound()': leans on "
        "'QQuick3DAmbientSound::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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
    Calls Qt's 'void QQuick3DAmbientSound::play()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dambientsound.html#play
    """
    #  void QQuick3DAmbientSound::play()
    self.uglySide.call('ritual_ZN20QQuick3DAmbientSound4playEv')

  def pause(self) -> None:
    """
    Calls Qt's 'void QQuick3DAmbientSound::pause()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dambientsound.html#pause
    """
    #  void QQuick3DAmbientSound::pause()
    self.uglySide.call('ritual_ZN20QQuick3DAmbientSound5pauseEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QQuick3DAmbientSound::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dambientsound.html#stop
    """
    #  void QQuick3DAmbientSound::stop()
    self.uglySide.call('ritual_ZN20QQuick3DAmbientSound4stopEv')

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DAmbientSound::sourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dambientsound.html#sourceChanged
    """
    #  void QQuick3DAmbientSound::sourceChanged()
    self.uglySide.call('ritual_ZN20QQuick3DAmbientSound13sourceChangedEv')

  def volumeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DAmbientSound::volumeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dambientsound.html#volumeChanged
    """
    #  void QQuick3DAmbientSound::volumeChanged()
    self.uglySide.call('ritual_ZN20QQuick3DAmbientSound13volumeChangedEv')

  def loopsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DAmbientSound::loopsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dambientsound.html#loopsChanged
    """
    #  void QQuick3DAmbientSound::loopsChanged()
    self.uglySide.call('ritual_ZN20QQuick3DAmbientSound12loopsChangedEv')

  def autoPlayChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DAmbientSound::autoPlayChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dambientsound.html#autoPlayChanged
    """
    #  void QQuick3DAmbientSound::autoPlayChanged()
    self.uglySide.call('ritual_ZN20QQuick3DAmbientSound15autoPlayChangedEv')
