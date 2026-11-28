"""
QBasicTimer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qbasictimer.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBasicTimer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QBasicTimer: a plain Python object standing in front
  of one C++ QBasicTimer.

  What exists
  -----------

  Every function of Qt's QBasicTimer that has a ritual and that Python can
  call so far, 5 names in all: 'isActive', 'timerId', 'id', 'start', 'stop'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QBasicTimer::~QBasicTimer()': the destructor: Python never removes
    a C++ QBasicTimer.
  - Qt's 'QBasicTimer::QBasicTimer(QBasicTimer &&other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QBasicTimer &QBasicTimer::operator=(QBasicTimer &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QBasicTimer::swap(QBasicTimer &other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void QBasicTimer::start(Duration duration, QObject *obj)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QBasicTimer::start(Duration duration, Qt::TimerType timerType,
    QObject *obj)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QBasicTimer is created at the first use, not by
    'QBasicTimer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBasicTimer.
  - Each name of Qt's QBasicTimer that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBasicTimer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QBasicTimer::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbasictimer.html#isActive
    """
    #  bool QBasicTimer::isActive() const
    return self.uglySide.call('ritual_ZNK11QBasicTimer8isActiveEv')

  def timerId(self) -> int:
    """
    Calls Qt's 'int QBasicTimer::timerId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbasictimer.html#timerId
    """
    #  int QBasicTimer::timerId() const
    return self.uglySide.call('ritual_ZNK11QBasicTimer7timerIdEv')

  def id(self) -> Qt.TimerId:
    """
    Calls Qt's 'Qt::TimerId QBasicTimer::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbasictimer.html#id

    Returns
    -------

    Qt.TimerId
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.TimerId(number)'
      gives.
    """
    #  Qt::TimerId QBasicTimer::id() const
    return Qt.TimerId(self.uglySide.call('ritual_ZNK11QBasicTimer2idEv'))

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
    Notes what was given, for Qt's 'QBasicTimer::QBasicTimer()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbasictimer.html#QBasicTimer
    """
    #  QBasicTimer::QBasicTimer()
    self._noteCreation(QBasicTimer, lambda: Rituals.call(
        'ritual_ZN11QBasicTimerC1Ev',
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

  @overload(int, QObject)
  @overload(int, NoneType)
  def start(self, msec: int, obj: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QBasicTimer::start(int msec, QObject *obj)'.

    Qt's own words: https://doc.qt.io/qt-6/qbasictimer.html#start

    Parameters
    ----------

    msec : int
      Passed on as it is.

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBasicTimer::start(int msec, QObject *obj)
    self.uglySide.call(
        'ritual_ZN11QBasicTimer5startEiP7QObject',
        msec, self._addressOf(obj, 'QObject'),
    )

  @overload(int, Qt.TimerType, QObject)
  @overload(int, Qt.TimerType, NoneType)
  def start(
      self,
      msec: int,
      timerType: Qt.TimerType,
      obj: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void QBasicTimer::start(int msec, Qt::TimerType timerType,
    QObject *obj)'.

    Qt's own words: https://doc.qt.io/qt-6/qbasictimer.html#start

    Parameters
    ----------

    msec : int
      Passed on as it is.

    timerType : Qt.TimerType
      Passed on as its number.

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBasicTimer::start(int msec, Qt::TimerType timerType, QObject
    #      *obj)
    self.uglySide.call(
        'ritual_ZN11QBasicTimer5startEiN2Qt9TimerTypeEP7QObject',
        msec, timerType.value, self._addressOf(obj, 'QObject'),
    )

  def stop(self) -> None:
    """
    Calls Qt's 'void QBasicTimer::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qbasictimer.html#stop
    """
    #  void QBasicTimer::stop()
    self.uglySide.call('ritual_ZN11QBasicTimer4stopEv')

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QBasicTimer::swap(QBasicTimer &other)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QBasicTimer.swap' has no cute function yet. Qt's 'void "
        "QBasicTimer::swap(QBasicTimer &other)': takes a type Python has no "
        "way to hand over yet.")
