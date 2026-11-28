"""
Qt3DCore::QTickClock binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qtickclock_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DCore::QTickClock to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QTickClock(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DCore::QTickClock: a plain Python object standing
  in front of one C++ Qt3DCore::QTickClock.

  C++ hands a Qt3DCore::QTickClock around as a copy, so every C++
  Qt3DCore::QTickClock behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QTickClock that has a ritual and that
  Python can call so far, 2 names in all: 'setTickFrequency', 'reset'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DCore::QTickClock::~QTickClock()': the destructor: Python
    removes its C++ Qt3DCore::QTickClock by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 6 functions Qt declares: 2 leans on 'Qt3DCore.

  What to expect
  --------------

  - The C++ Qt3DCore::QTickClock is created at the first use, not by
    'Qt3DCore::QTickClock(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DCore::QTickClock back gives a copy the ritual
    made for Python, in a new cute Qt3DCore::QTickClock.
  - Each name of Qt's Qt3DCore::QTickClock that has no cute function yet,
    'start', 'waitForNextTick', holds a function that raises
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
  __qt_class__ = 'Qt3DCore::QTickClock'

  #  Qt's '~Qt3DCore::QTickClock()'. Naming it makes this a value class:
  #  Python owns every C++ Qt3DCore::QTickClock behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8Qt3DCore10QTickClockD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setTickFrequency(self, frequency: float) -> None:
    """
    Calls Qt's 'void Qt3DCore::QTickClock::setTickFrequency(float
    frequency)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qtickclock.html#setTickFrequency

    Parameters
    ----------

    frequency : float
      Passed on as it is.
    """
    #  void Qt3DCore::QTickClock::setTickFrequency(float frequency)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QTickClock16setTickFrequencyEf', frequency,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'Qt3DCore::QTickClock::QTickClock()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qtickclock.html#QTickClock
    """
    #  Qt3DCore::QTickClock::QTickClock()
    self._noteCreation(QTickClock, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore10QTickClockC1Ev',
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

  def reset(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QTickClock::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qtickclock.html#reset
    """
    #  void Qt3DCore::QTickClock::reset()
    self.uglySide.call('ritual_ZN8Qt3DCore10QTickClock5resetEv')

  @staticmethod
  def start(*__, **_) -> Never:
    """
    Qt's 'void Qt3DCore::QTickClock::start()': leans on
    'Qt3DCore::ChangeArbiter()', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DCore.QTickClock.start' has no cute function yet. Qt's 'void "
        "Qt3DCore::QTickClock::start()': leans on "
        "'Qt3DCore::ChangeArbiter()', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def waitForNextTick(*__, **_) -> Never:
    """
    Qt's 'qint64 Qt3DCore::QTickClock::waitForNextTick()': leans on
    'Qt3DCore::ChangeArbiter()', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DCore.QTickClock.waitForNextTick' has no cute function yet. "
        "Qt's 'qint64 Qt3DCore::QTickClock::waitForNextTick()': leans on "
        "'Qt3DCore::ChangeArbiter()', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")
