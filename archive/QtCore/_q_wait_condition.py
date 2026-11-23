"""
QWaitCondition binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qwaitcondition.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QDeadlineTimer, QMutex, QReadWriteLock
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeadlineTimer = WAIT['QDeadlineTimer']
  QMutex = WAIT['QMutex']
  QReadWriteLock = WAIT['QReadWriteLock']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaitCondition(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWaitCondition: a plain Python object standing in
  front of one C++ QWaitCondition.

  What exists
  -----------

  Every function of Qt's QWaitCondition that has a ritual and that Python can
  call so far, 5 names in all: 'wait', 'wakeOne', 'wakeAll', 'notify_one',
  'notify_all'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWaitCondition::~QWaitCondition()': the destructor: Python never
    removes a C++ QWaitCondition.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QWaitCondition is created at the first use, not by
    'QWaitCondition(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaitCondition.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaitCondition'

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
    Notes what was given, for Qt's 'QWaitCondition::QWaitCondition()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwaitcondition.html#QWaitCondition
    """
    #  QWaitCondition::QWaitCondition()
    self._noteCreation(QWaitCondition, lambda: Rituals.call(
        'ritual_ZN14QWaitConditionC1Ev',
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

  @overload(QMutex, QDeadlineTimer)
  @overload(NoneType, QDeadlineTimer)
  def wait(
      self,
      lockedMutex: Optional[QMutex],
      deadline: QDeadlineTimer,
  ) -> bool:
    """
    Calls Qt's 'bool QWaitCondition::wait(QMutex *lockedMutex, QDeadlineTimer
    deadline)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaitcondition.html#wait

    Parameters
    ----------

    lockedMutex : Optional[QMutex]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    deadline : QDeadlineTimer
      Passed on as a value: Qt reads the C++ QDeadlineTimer, which stays
      Python's own.
    """
    #  bool QWaitCondition::wait(QMutex *lockedMutex, QDeadlineTimer
    #      deadline)
    return self.uglySide.call(
        'ritual_ZN14QWaitCondition4waitEP6QMutex14QDeadlineTimer',
        self._addressOf(lockedMutex), self._valueOf(deadline),
    )

  @overload(QMutex, int)
  @overload(NoneType, int)
  def wait(self, lockedMutex: Optional[QMutex], time: int) -> bool:
    """
    Calls Qt's 'bool QWaitCondition::wait(QMutex *lockedMutex, unsigned long
    time)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaitcondition.html#wait

    Parameters
    ----------

    lockedMutex : Optional[QMutex]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    time : int
      Passed on as it is.
    """
    #  bool QWaitCondition::wait(QMutex *lockedMutex, unsigned long time)
    return self.uglySide.call(
        'ritual_ZN14QWaitCondition4waitEP6QMutexm',
        self._addressOf(lockedMutex), time,
    )

  @overload(QReadWriteLock, QDeadlineTimer)
  def wait(
      self,
      lockedReadWriteLock: Optional[QReadWriteLock],
      deadline: QDeadlineTimer,
  ) -> bool:
    """
    Calls Qt's 'bool QWaitCondition::wait(QReadWriteLock
    *lockedReadWriteLock, QDeadlineTimer deadline)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaitcondition.html#wait

    Parameters
    ----------

    lockedReadWriteLock : Optional[QReadWriteLock]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    deadline : QDeadlineTimer
      Passed on as a value: Qt reads the C++ QDeadlineTimer, which stays
      Python's own.
    """
    #  bool QWaitCondition::wait(QReadWriteLock *lockedReadWriteLock,
    #      QDeadlineTimer deadline)
    return self.uglySide.call(
        'ritual_ZN14QWaitCondition4waitEP14QReadWriteLock14QDeadlineTimer',
        self._addressOf(lockedReadWriteLock), self._valueOf(deadline),
    )

  @overload(QReadWriteLock, int)
  def wait(
      self,
      lockedReadWriteLock: Optional[QReadWriteLock],
      time: int,
  ) -> bool:
    """
    Calls Qt's 'bool QWaitCondition::wait(QReadWriteLock
    *lockedReadWriteLock, unsigned long time)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaitcondition.html#wait

    Parameters
    ----------

    lockedReadWriteLock : Optional[QReadWriteLock]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    time : int
      Passed on as it is.
    """
    #  bool QWaitCondition::wait(QReadWriteLock *lockedReadWriteLock,
    #      unsigned long time)
    return self.uglySide.call(
        'ritual_ZN14QWaitCondition4waitEP14QReadWriteLockm',
        self._addressOf(lockedReadWriteLock), time,
    )

  def wakeOne(self) -> None:
    """
    Calls Qt's 'void QWaitCondition::wakeOne()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaitcondition.html#wakeOne
    """
    #  void QWaitCondition::wakeOne()
    self.uglySide.call('ritual_ZN14QWaitCondition7wakeOneEv')

  def wakeAll(self) -> None:
    """
    Calls Qt's 'void QWaitCondition::wakeAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaitcondition.html#wakeAll
    """
    #  void QWaitCondition::wakeAll()
    self.uglySide.call('ritual_ZN14QWaitCondition7wakeAllEv')

  def notify_one(self) -> None:
    """
    Calls Qt's 'void QWaitCondition::notify_one()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaitcondition.html#notify_one
    """
    #  void QWaitCondition::notify_one()
    self.uglySide.call('ritual_ZN14QWaitCondition10notify_oneEv')

  def notify_all(self) -> None:
    """
    Calls Qt's 'void QWaitCondition::notify_all()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaitcondition.html#notify_all
    """
    #  void QWaitCondition::notify_all()
    self.uglySide.call('ritual_ZN14QWaitCondition10notify_allEv')
