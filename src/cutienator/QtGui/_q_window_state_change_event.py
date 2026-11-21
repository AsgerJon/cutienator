"""
QWindowStateChangeEvent binding of the Qt C++
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


class QWindowStateChangeEvent(QEvent):
  """
  The cute side of Qt's QWindowStateChangeEvent: a plain Python object
  standing in front of one C++ QWindowStateChangeEvent.

  It is built on the cute 'QEvent', as Qt's QWindowStateChangeEvent is built
  on Qt's QEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWindowStateChangeEvent that has a ritual and that
  Python can call so far, 3 names in all: 'clone', 'oldState', 'isOverride'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWindowStateChangeEvent::~QWindowStateChangeEvent()': the
    destructor: Python never removes a C++ QWindowStateChangeEvent.

  What has no ritual
  ------------------

  4 of the 9 functions Qt declares: 2 protected; 2 forbidden.

  What to expect
  --------------

  - The C++ QWindowStateChangeEvent is created at the first use, not by
    'QWindowStateChangeEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWindowStateChangeEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWindowStateChangeEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QWindowStateChangeEvent]:
    """
    Calls Qt's 'QWindowStateChangeEvent *QWindowStateChangeEvent::clone()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowstatechangeevent.html#clone

    Returns
    -------

    Optional[QWindowStateChangeEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindowStateChangeEvent *QWindowStateChangeEvent::clone() const
    address = self.uglySide.call(
        'ritual_ZNK23QWindowStateChangeEvent5cloneEv',
    )
    return QWindowStateChangeEvent._cuteAt(address)

  def oldState(self) -> Qt.WindowStates:
    """
    Calls Qt's 'Qt::WindowStates QWindowStateChangeEvent::oldState() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowstatechangeevent.html#oldState

    Returns
    -------

    Qt.WindowStates
      The value standing for the combination Qt gave back.
    """
    #  Qt::WindowStates QWindowStateChangeEvent::oldState() const
    return Qt.WindowStates(self.uglySide.call(
        'ritual_ZNK23QWindowStateChangeEvent8oldStateEv',
    ))

  def isOverride(self) -> bool:
    """
    Calls Qt's 'bool QWindowStateChangeEvent::isOverride() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowstatechangeevent.html#isOverride
    """
    #  bool QWindowStateChangeEvent::isOverride() const
    return self.uglySide.call(
        'ritual_ZNK23QWindowStateChangeEvent10isOverrideEv',
    )

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

  @overload(Qt.WindowStates)
  @overload(Qt.WindowStates, bool)
  def __init__(
      self,
      oldState: Qt.WindowStates,
      isOverride: bool = False,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QWindowStateChangeEvent::QWindowStateChangeEvent(Qt::WindowStates
    oldState, bool isOverride)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowstatechangeevent.html

    Parameters
    ----------

    oldState : Qt.WindowStates
      Passed on as its number.

    isOverride : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  QWindowStateChangeEvent::QWindowStateChangeEvent(Qt::WindowStates
    #      oldState, bool isOverride)
    self._noteCreation(QWindowStateChangeEvent, lambda: Rituals.call(
        'ritual_ZN23QWindowStateChangeEventC1E6QFlagsIN2Qt11WindowStateEEb',
        oldState.value, isOverride,
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
