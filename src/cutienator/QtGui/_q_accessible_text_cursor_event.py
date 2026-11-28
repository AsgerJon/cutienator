"""
QAccessibleTextCursorEvent binding of the Qt C++
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
from . import QAccessibleEvent

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


class QAccessibleTextCursorEvent(QAccessibleEvent):
  """
  The cute side of Qt's QAccessibleTextCursorEvent: a plain Python object
  standing in front of one C++ QAccessibleTextCursorEvent.

  It is built on the cute 'QAccessibleEvent', as Qt's
  QAccessibleTextCursorEvent is built on Qt's QAccessibleEvent, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleTextCursorEvent that has a ritual and
  that Python can call so far, 2 names in all: 'setCursorPosition',
  'cursorPosition'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAccessibleTextCursorEvent::~QAccessibleTextCursorEvent()': the
    destructor: Python never removes a C++ QAccessibleTextCursorEvent.

  What to expect
  --------------

  - The C++ QAccessibleTextCursorEvent is created at the first use, not by
    'QAccessibleTextCursorEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleTextCursorEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleTextCursorEvent'

  #  A C++ QAccessibleTextCursorEvent Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleTextCursorEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def cursorPosition(self) -> int:
    """
    Calls Qt's 'int QAccessibleTextCursorEvent::cursorPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextcursorevent.html#cursorPosition
    """
    #  int QAccessibleTextCursorEvent::cursorPosition() const
    return self.uglySide.call(
        'ritual_ZNK26QAccessibleTextCursorEvent14cursorPositionEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setCursorPosition(self, position: int) -> None:
    """
    Calls Qt's 'void QAccessibleTextCursorEvent::setCursorPosition(int
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextcursorevent.html#setCursorPosition

    Parameters
    ----------

    position : int
      Passed on as it is.
    """
    #  void QAccessibleTextCursorEvent::setCursorPosition(int position)
    self.uglySide.call(
        'ritual_ZN26QAccessibleTextCursorEvent17setCursorPositionEi',
        position,
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

  @overload(QObject, int)
  @overload(NoneType, int)
  def __init__(self, obj: Optional[QObject], cursorPos: int) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleTextCursorEvent::QAccessibleTextCursorEvent(QObject *obj, int
    cursorPos)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextcursorevent.html

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    cursorPos : int
      Passed on as it is.
    """
    #  QAccessibleTextCursorEvent::QAccessibleTextCursorEvent(QObject *obj,
    #      int cursorPos)
    self._noteCreation(QAccessibleTextCursorEvent, lambda: Rituals.call(
        'ritual_ZN26QAccessibleTextCursorEventC1EP7QObjecti',
        self._addressOf(obj, 'QObject'), cursorPos,
    ))

  @overload(QAccessibleInterface, int)
  def __init__(
      self,
      iface: Optional[QAccessibleInterface],
      cursorPos: int,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleTextCursorEvent::QAccessibleTextCursorEvent(
    QAccessibleInterface *iface, int cursorPos)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextcursorevent.html

    Parameters
    ----------

    iface : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    cursorPos : int
      Passed on as it is.
    """
    #  QAccessibleTextCursorEvent::QAccessibleTextCursorEvent(
    #      QAccessibleInterface *iface, int cursorPos)
    self._noteCreation(QAccessibleTextCursorEvent, lambda: Rituals.call(
        'ritual_ZN26QAccessibleTextCursorEventC1EP20QAccessibleInterfacei',
        self._addressOf(iface, 'QAccessibleInterface'), cursorPos,
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
