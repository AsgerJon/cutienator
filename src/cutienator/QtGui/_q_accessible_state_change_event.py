"""
QAccessibleStateChangeEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QAccessible, QAccessibleEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
  from . import QAccessibleInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAccessibleInterface = WAIT['QAccessibleInterface']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleStateChangeEvent(QAccessibleEvent):
  """
  The cute side of Qt's QAccessibleStateChangeEvent: a plain Python object
  standing in front of one C++ QAccessibleStateChangeEvent.

  It is built on the cute 'QAccessibleEvent', as Qt's
  QAccessibleStateChangeEvent is built on Qt's QAccessibleEvent, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleStateChangeEvent that has a ritual and
  that Python can call so far, 1 name in all: 'changedStates'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAccessibleStateChangeEvent::~QAccessibleStateChangeEvent()': the
    destructor: Python never removes a C++ QAccessibleStateChangeEvent.

  What to expect
  --------------

  - The C++ QAccessibleStateChangeEvent is created at the first use, not by
    'QAccessibleStateChangeEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleStateChangeEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleStateChangeEvent'

  #  A C++ QAccessibleStateChangeEvent Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleStateChangeEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def changedStates(self) -> QAccessible.State:
    """
    Calls Qt's 'QAccessible::State
    QAccessibleStateChangeEvent::changedStates() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblestatechangeevent.html#changedStates

    Returns
    -------

    QAccessible.State
      A new cute QAccessible::State around the copy Qt gave back. Python owns
      it.
    """
    #  QAccessible::State QAccessibleStateChangeEvent::changedStates() const
    address = self.uglySide.call(
        'ritual_ZNK27QAccessibleStateChangeEvent13changedStatesEv',
    )
    return QAccessible.State._cuteOwning(address)

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

  @overload(QObject, QAccessible.State)
  @overload(NoneType, QAccessible.State)
  def __init__(
      self,
      obj: Optional[QObject],
      state: QAccessible.State,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleStateChangeEvent::QAccessibleStateChangeEvent(QObject *obj,
    QAccessible::State state)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblestatechangeevent.html

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    state : QAccessible.State
      Passed on as a value: Qt reads the C++ QAccessible::State, which stays
      Python's own.
    """
    #  QAccessibleStateChangeEvent::QAccessibleStateChangeEvent(QObject *obj,
    #      QAccessible::State state)
    self._noteCreation(QAccessibleStateChangeEvent, lambda: Rituals.call(
        'ritual_ZN27QAccessibleStateChangeEventC1EP7QObjectN11QAccessible5S'
        'tateE',
        self._addressOf(obj), self._valueOf(state),
    ))

  @overload(QAccessibleInterface, QAccessible.State)
  def __init__(
      self,
      iface: Optional[QAccessibleInterface],
      state: QAccessible.State,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleStateChangeEvent::QAccessibleStateChangeEvent(
    QAccessibleInterface *iface, QAccessible::State state)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblestatechangeevent.html

    Parameters
    ----------

    iface : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    state : QAccessible.State
      Passed on as a value: Qt reads the C++ QAccessible::State, which stays
      Python's own.
    """
    #  QAccessibleStateChangeEvent::QAccessibleStateChangeEvent(
    #      QAccessibleInterface *iface, QAccessible::State state)
    self._noteCreation(QAccessibleStateChangeEvent, lambda: Rituals.call(
        'ritual_ZN27QAccessibleStateChangeEventC1EP20QAccessibleInterfaceN1'
        '1QAccessible5StateE',
        self._addressOf(iface), self._valueOf(state),
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
