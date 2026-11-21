"""
QTimerEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qcoreevent.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import Qt, QEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QTimerEvent(QEvent):
  """
  The cute side of Qt's QTimerEvent: a plain Python object standing in front
  of one C++ QTimerEvent.

  It is built on the cute 'QEvent', as Qt's QTimerEvent is built on Qt's
  QEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTimerEvent that has a ritual and that Python can
  call so far, 3 names in all: 'clone', 'timerId', 'id'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTimerEvent::~QTimerEvent()': the destructor: Python never removes
    a C++ QTimerEvent.

  What has no ritual
  ------------------

  5 of the 11 functions Qt declares: 2 protected; 2 forbidden; 1 takes or
  gives a type that cannot be passed yet.

  What to expect
  --------------

  - The C++ QTimerEvent is created at the first use, not by
    'QTimerEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTimerEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTimerEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QTimerEvent]:
    """
    Calls Qt's 'QTimerEvent *QTimerEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimerevent.html#clone

    Returns
    -------

    Optional[QTimerEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTimerEvent *QTimerEvent::clone() const
    address = self.uglySide.call('ritual_ZNK11QTimerEvent5cloneEv')
    return QTimerEvent._cuteAt(address)

  def timerId(self) -> int:
    """
    Calls Qt's 'int QTimerEvent::timerId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimerevent.html#timerId
    """
    #  int QTimerEvent::timerId() const
    return self.uglySide.call('ritual_ZNK11QTimerEvent7timerIdEv')

  def id(self) -> Qt.TimerId:
    """
    Calls Qt's 'Qt::TimerId QTimerEvent::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimerevent.html#id

    Returns
    -------

    Qt.TimerId
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.TimerId(number)'
      gives.
    """
    #  Qt::TimerId QTimerEvent::id() const
    return Qt.TimerId(self.uglySide.call('ritual_ZNK11QTimerEvent2idEv'))

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

  @overload(int)
  def __init__(self, timerId: int) -> None:
    """
    Notes what was given, for Qt's 'QTimerEvent::QTimerEvent(int timerId)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtimerevent.html#QTimerEvent

    Parameters
    ----------

    timerId : int
      Passed on as it is.
    """
    #  QTimerEvent::QTimerEvent(int timerId)
    self._noteCreation(QTimerEvent, lambda: Rituals.call(
        'ritual_ZN11QTimerEventC1Ei', timerId,
    ))

  @overload(Qt.TimerId)
  def __init__(self, timerId: Qt.TimerId) -> None:
    """
    Notes what was given, for Qt's 'QTimerEvent::QTimerEvent(Qt::TimerId
    timerId)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtimerevent.html#QTimerEvent

    Parameters
    ----------

    timerId : Qt.TimerId
      Passed on as its number.
    """
    #  QTimerEvent::QTimerEvent(Qt::TimerId timerId)
    self._noteCreation(QTimerEvent, lambda: Rituals.call(
        'ritual_ZN11QTimerEventC1EN2Qt7TimerIdE', timerId.value,
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
