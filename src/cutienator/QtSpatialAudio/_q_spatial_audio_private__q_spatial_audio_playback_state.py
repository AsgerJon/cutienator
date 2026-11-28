"""
QSpatialAudioPrivate::QSpatialAudioPlaybackState binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSpatialAudio/6.12.0/QtSpatialAudio/private/qspatialaudiosound_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QSpatialAudioPrivate::QSpatialAudioPlaybackState to be private:
#  it declares the class in a header it calls private. cutienator does not
#  care. Qt hands objects of the class out all the same, and a class we are
#  handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtMultimedia import QAudioBuffer, QAudioFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioBuffer = WAIT['QAudioBuffer']


class QSpatialAudioPlaybackState(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSpatialAudioPrivate::QSpatialAudioPlaybackState: a
  plain Python object standing in front of one C++
  QSpatialAudioPrivate::QSpatialAudioPlaybackState.

  What exists
  -----------

  Every function of Qt's QSpatialAudioPrivate::QSpatialAudioPlaybackState
  that has a ritual and that Python can call so far, 4 names in all: 'pause',
  'resume', 'setLoops', 'format'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    QSpatialAudioPrivate::QSpatialAudioPlaybackState::getBuffer(QSpan<float>
    output)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSpatialAudioPrivate::QSpatialAudioPlaybackState is created at
    the first use, not by
    'QSpatialAudioPrivate::QSpatialAudioPlaybackState(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    QSpatialAudioPrivate::QSpatialAudioPlaybackState.
  - Each name of Qt's QSpatialAudioPrivate::QSpatialAudioPlaybackState that
    has no cute function yet, 'getBuffer', holds a function that raises
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
  __qt_class__ = 'QSpatialAudioPrivate::QSpatialAudioPlaybackState'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def format(self) -> QAudioFormat:
    """
    Calls Qt's 'QAudioFormat
    QSpatialAudioPrivate::QSpatialAudioPlaybackState::format() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialaudioprivate-qspatialaudioplaybackstate.html

    Returns
    -------

    QAudioFormat
      A new cute QAudioFormat around the copy Qt gave back. Python owns it.
    """
    #  QAudioFormat
    #      QSpatialAudioPrivate::QSpatialAudioPlaybackState::format() const
    address = self.uglySide.call(
        'ritual_ZNK20QSpatialAudioPrivate26QSpatialAudioPlaybackState6forma'
        'tEv',
    )
    from ..QtMultimedia import QAudioFormat
    return QAudioFormat._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setLoops(self, a0: int) -> None:
    """
    Calls Qt's 'void
    QSpatialAudioPrivate::QSpatialAudioPlaybackState::setLoops(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialaudioprivate-qspatialaudioplaybackstate.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QSpatialAudioPrivate::QSpatialAudioPlaybackState::setLoops(int
    #      a0)
    self.uglySide.call(
        'ritual_ZN20QSpatialAudioPrivate26QSpatialAudioPlaybackState8setLoo'
        'psEi',
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

  @overload(QAudioBuffer, bool, int)
  def __init__(
      self,
      buffer: QAudioBuffer,
      playing: bool,
      loops: int,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QSpatialAudioPrivate::QSpatialAudioPlaybackState::
    QSpatialAudioPlaybackState(QAudioBuffer buffer, bool playing, int
    loops)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialaudioprivate-qspatialaudioplaybackstate.html

    Parameters
    ----------

    buffer : QAudioBuffer
      Passed on as a value: Qt reads the C++ QAudioBuffer, which stays
      Python's own.

    playing : bool
      Passed on as it is.

    loops : int
      Passed on as it is.
    """
    #  QSpatialAudioPrivate::QSpatialAudioPlaybackState::
    #      QSpatialAudioPlaybackState(QAudioBuffer buffer, bool playing, int
    #      loops)
    self._noteCreation(QSpatialAudioPlaybackState, lambda: Rituals.call(
        'ritual_ZN20QSpatialAudioPrivate26QSpatialAudioPlaybackStateC1E12QA'
        'udioBufferbi',
        self._valueOf(buffer), playing, loops,
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

  def pause(self) -> None:
    """
    Calls Qt's 'void
    QSpatialAudioPrivate::QSpatialAudioPlaybackState::pause()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialaudioprivate-qspatialaudioplaybackstate.html
    """
    #  void QSpatialAudioPrivate::QSpatialAudioPlaybackState::pause()
    self.uglySide.call(
        'ritual_ZN20QSpatialAudioPrivate26QSpatialAudioPlaybackState5pauseE'
        'v',
    )

  def resume(self) -> None:
    """
    Calls Qt's 'void
    QSpatialAudioPrivate::QSpatialAudioPlaybackState::resume()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialaudioprivate-qspatialaudioplaybackstate.html
    """
    #  void QSpatialAudioPrivate::QSpatialAudioPlaybackState::resume()
    self.uglySide.call(
        'ritual_ZN20QSpatialAudioPrivate26QSpatialAudioPlaybackState6resume'
        'Ev',
    )

  @staticmethod
  def getBuffer(*__, **_) -> Never:
    """
    Qt's 'void
    QSpatialAudioPrivate::QSpatialAudioPlaybackState::getBuffer(QSpan<float>
    output)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSpatialAudioPrivate.QSpatialAudioPlaybackState.getBuffer' has no "
        "cute function yet. Qt's 'void "
        "QSpatialAudioPrivate::QSpatialAudioPlaybackState::getBuffer(QSpan<f"
        "loat> output)': takes a type Python has no way to hand over yet.")
