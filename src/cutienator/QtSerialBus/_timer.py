"""
Timer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/6.12.0/QtSerialBus/private/qmodbusrtuserialclient_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Timer to be private: it declares the class in a header it calls
#  private. cutienator does not care. Qt hands objects of the class out all
#  the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QTimerEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Timer(QObject):
  """
  The cute side of Qt's Timer: a plain Python object standing in front of one
  C++ Timer.

  It is built on the cute 'QObject', as Qt's Timer is built on Qt's QObject,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Timer that has a ritual and that Python can call so
  far, 6 names in all: 'metaObject', 'start', 'stop', 'isActive', 'timeout',
  'timerEvent'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Timer::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int Timer::qt_metacall(QMetaObject::Call a0, int a1, void **a2)':
    one of Qt's own inner workings.

  What has no ritual
  ------------------

  4 of the 12 functions Qt declares: 2 not a gap; 1 leans on 'Timer; 1 leans
  on 'vtable for Timer', which Qt's source does not mark for use from outside
  Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ Timer is created at the first use, not by 'Timer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Timer.
  - Qt tells when it has removed the C++ Timer. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's Timer that has no cute function yet, '__init__', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Timer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Timer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/timer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Timer::metaObject() const
    address = self.uglySide.call('ritual_ZNK5Timer10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool Timer::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/timer.html#isActive
    """
    #  bool Timer::isActive() const
    return self.uglySide.call('ritual_ZNK5Timer8isActiveEv')

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'Timer::Timer()': leans on 'vtable for Timer', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'Timer.__init__' has no cute function yet. Qt's 'Timer::Timer()': "
        "leans on 'vtable for Timer', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

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

  @overload(int)
  def start(self, msec: int) -> int:
    """
    Calls Qt's 'int Timer::start(int msec)'.

    Qt's own words: https://doc.qt.io/qt-6/timer.html#start

    Parameters
    ----------

    msec : int
      Passed on as it is.
    """
    #  int Timer::start(int msec)
    return self.uglySide.call('ritual_ZN5Timer5startEi', msec)

  def stop(self) -> None:
    """
    Calls Qt's 'void Timer::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/timer.html#stop
    """
    #  void Timer::stop()
    self.uglySide.call('ritual_ZN5Timer4stopEv')

  @overload(int)
  def timeout(self, timerId: int) -> None:
    """
    Calls Qt's 'void Timer::timeout(int timerId)'.

    Qt's own words: https://doc.qt.io/qt-6/timer.html#timeout

    Parameters
    ----------

    timerId : int
      Passed on as it is.
    """
    #  void Timer::timeout(int timerId)
    self.uglySide.call('ritual_ZN5Timer7timeoutEi', timerId)

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void Timer::timerEvent(QTimerEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/timer.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Timer::timerEvent(QTimerEvent *event)
    self.uglySide.call(
        'ritual_ZN5Timer10timerEventEP11QTimerEvent', self._addressOf(event),
    )
