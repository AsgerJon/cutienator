"""
QApplicationStateChangeEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qevent.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import Qt, QEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QApplicationStateChangeEvent(QEvent):
  """
  The cute side of Qt's QApplicationStateChangeEvent: a plain Python object
  standing in front of one C++ QApplicationStateChangeEvent.

  It is built on the cute 'QEvent', as Qt's QApplicationStateChangeEvent is
  built on Qt's QEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QApplicationStateChangeEvent that has a ritual and
  that Python can call so far, 2 names in all: 'clone', 'applicationState'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QApplicationStateChangeEvent::~QApplicationStateChangeEvent()': the
    destructor: Python never removes a C++ QApplicationStateChangeEvent.

  What has no ritual
  ------------------

  4 of the 8 functions Qt declares: 2 protected; 2 forbidden.

  What to expect
  --------------

  - The C++ QApplicationStateChangeEvent is created at the first use, not by
    'QApplicationStateChangeEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QApplicationStateChangeEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QApplicationStateChangeEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QApplicationStateChangeEvent]:
    """
    Calls Qt's 'QApplicationStateChangeEvent
    *QApplicationStateChangeEvent::clone() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationstatechangeevent.html#clone

    Returns
    -------

    Optional[QApplicationStateChangeEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QApplicationStateChangeEvent *QApplicationStateChangeEvent::clone()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK28QApplicationStateChangeEvent5cloneEv',
    )
    return QApplicationStateChangeEvent._cuteAt(address)

  def applicationState(self) -> Qt.ApplicationState:
    """
    Calls Qt's 'Qt::ApplicationState
    QApplicationStateChangeEvent::applicationState() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationstatechangeevent.html#applicationState

    Returns
    -------

    Qt.ApplicationState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.ApplicationState(number)' gives.
    """
    #  Qt::ApplicationState QApplicationStateChangeEvent::applicationState()
    #      const
    return Qt.ApplicationState(self.uglySide.call(
        'ritual_ZNK28QApplicationStateChangeEvent16applicationStateEv',
    ))

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

  @overload(Qt.ApplicationState)
  def __init__(self, state: Qt.ApplicationState) -> None:
    """
    Notes what was given, for Qt's
    'QApplicationStateChangeEvent::QApplicationStateChangeEvent(Qt::
    ApplicationState state)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationstatechangeevent.html

    Parameters
    ----------

    state : Qt.ApplicationState
      Passed on as its number.
    """
    #  QApplicationStateChangeEvent::QApplicationStateChangeEvent(Qt::
    #      ApplicationState state)
    self._noteCreation(QApplicationStateChangeEvent, lambda: Rituals.call(
        'ritual_ZN28QApplicationStateChangeEventC1EN2Qt16ApplicationStateE',
        state.value,
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
