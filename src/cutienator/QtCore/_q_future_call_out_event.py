"""
QFutureCallOutEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qfutureinterface_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QFutureCallOutEvent to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum
from ..occult import Rituals
from . import QEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QFutureCallOutEvent(QEvent):
  """
  The cute side of Qt's QFutureCallOutEvent: a plain Python object standing
  in front of one C++ QFutureCallOutEvent.

  It is built on the cute 'QEvent', as Qt's QFutureCallOutEvent is built on
  Qt's QEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFutureCallOutEvent that has a ritual and that
  Python can call so far, 1 name in all: 'clone'. It can be made from Python,
  in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFutureCallOutEvent::QFutureCallOutEvent(const QFutureCallOutEvent
    &a0)': takes a type Python has no way to hand over yet.
  - Qt's 'QFutureCallOutEvent &QFutureCallOutEvent::operator=(const
    QFutureCallOutEvent &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QFutureCallOutEvent::~QFutureCallOutEvent()': the destructor:
    Python never removes a C++ QFutureCallOutEvent.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QFutureCallOutEvent is created at the first use, not by
    'QFutureCallOutEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFutureCallOutEvent.
  """

  #  The enums Qt writes inside QFutureCallOutEvent, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class CallOutType(CuteNum):
    """
    The enum 'QFutureCallOutEvent::CallOutType' of Qt, with the 9 names Qt
    gives in it.
    """

    Started = Kee[int](0)
    Finished = Kee[int](1)
    Canceled = Kee[int](2)
    Suspending = Kee[int](3)
    Suspended = Kee[int](4)
    Resumed = Kee[int](5)
    Progress = Kee[int](6)
    ProgressRange = Kee[int](7)
    ResultsReady = Kee[int](8)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFutureCallOutEvent'

  #  A C++ QFutureCallOutEvent Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFutureCallOutEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QFutureCallOutEvent]:
    """
    Calls Qt's 'QFutureCallOutEvent *QFutureCallOutEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfuturecalloutevent.html#clone

    Returns
    -------

    Optional[QFutureCallOutEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFutureCallOutEvent *QFutureCallOutEvent::clone() const
    ritual = 'ritual_ZNK19QFutureCallOutEvent5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QFutureCallOutEvent5cloneEv'
    address = self.uglySide.call(ritual)
    return QFutureCallOutEvent._cuteAt(address)

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
    Notes what was given, for Qt's
    'QFutureCallOutEvent::QFutureCallOutEvent()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfuturecalloutevent.html#QFutureCallOutEvent
    """
    #  QFutureCallOutEvent::QFutureCallOutEvent()
    self._noteCreation(QFutureCallOutEvent, lambda: Rituals.call(
        'ritual_ZN19QFutureCallOutEventC1Ev',
    ))

  @overload(CallOutType)
  @overload(CallOutType, int)
  def __init__(self, callOutType: CallOutType, index1: int = -1) -> None:
    """
    Notes what was given, for Qt's
    'QFutureCallOutEvent::QFutureCallOutEvent(CallOutType callOutType, int
    index1)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfuturecalloutevent.html#QFutureCallOutEvent

    Parameters
    ----------

    callOutType : CallOutType
      Passed on as its number.

    index1 : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  QFutureCallOutEvent::QFutureCallOutEvent(CallOutType callOutType, int
    #      index1)
    self._noteCreation(QFutureCallOutEvent, lambda: Rituals.call(
        'ritual_ZN19QFutureCallOutEventC1ENS_11CallOutTypeEi',
        callOutType.value, index1,
    ))

  @overload(CallOutType, int, int)
  def __init__(
      self,
      callOutType: CallOutType,
      index1: int,
      index2: int,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QFutureCallOutEvent::QFutureCallOutEvent(CallOutType callOutType, int
    index1, int index2)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfuturecalloutevent.html#QFutureCallOutEvent

    Parameters
    ----------

    callOutType : CallOutType
      Passed on as its number.

    index1 : int
      Passed on as it is.

    index2 : int
      Passed on as it is.
    """
    #  QFutureCallOutEvent::QFutureCallOutEvent(CallOutType callOutType, int
    #      index1, int index2)
    self._noteCreation(QFutureCallOutEvent, lambda: Rituals.call(
        'ritual_ZN19QFutureCallOutEventC1ENS_11CallOutTypeEii',
        callOutType.value, index1, index2,
    ))

  @overload(CallOutType, int, str)
  def __init__(
      self,
      callOutType: CallOutType,
      index1: int,
      text: str,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QFutureCallOutEvent::QFutureCallOutEvent(CallOutType callOutType, int
    index1, const QString &text)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfuturecalloutevent.html#QFutureCallOutEvent

    Parameters
    ----------

    callOutType : CallOutType
      Passed on as its number.

    index1 : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QFutureCallOutEvent::QFutureCallOutEvent(CallOutType callOutType, int
    #      index1, const QString &text)
    self._noteCreation(QFutureCallOutEvent, lambda: Rituals.call(
        'ritual_ZN19QFutureCallOutEventC1ENS_11CallOutTypeEiRK7QString',
        callOutType.value, index1, text,
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
