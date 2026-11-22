"""
QAccessibleTextInsertEvent binding of the Qt C++
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
from . import QAccessibleTextCursorEvent

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


class QAccessibleTextInsertEvent(QAccessibleTextCursorEvent):
  """
  The cute side of Qt's QAccessibleTextInsertEvent: a plain Python object
  standing in front of one C++ QAccessibleTextInsertEvent.

  It is built on the cute 'QAccessibleTextCursorEvent', as Qt's
  QAccessibleTextInsertEvent is built on Qt's QAccessibleTextCursorEvent, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleTextInsertEvent that has a ritual and
  that Python can call so far, 2 names in all: 'textInserted',
  'changePosition'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAccessibleTextInsertEvent::~QAccessibleTextInsertEvent()': the
    destructor: Python never removes a C++ QAccessibleTextInsertEvent.

  What to expect
  --------------

  - The C++ QAccessibleTextInsertEvent is created at the first use, not by
    'QAccessibleTextInsertEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleTextInsertEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleTextInsertEvent'

  #  A C++ QAccessibleTextInsertEvent Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleTextInsertEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def textInserted(self) -> str:
    """
    Calls Qt's 'QString QAccessibleTextInsertEvent::textInserted() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextinsertevent.html#textInserted

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleTextInsertEvent::textInserted() const
    return self.uglySide.call(
        'ritual_ZNK26QAccessibleTextInsertEvent12textInsertedEv',
    )

  def changePosition(self) -> int:
    """
    Calls Qt's 'int QAccessibleTextInsertEvent::changePosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextinsertevent.html#changePosition
    """
    #  int QAccessibleTextInsertEvent::changePosition() const
    return self.uglySide.call(
        'ritual_ZNK26QAccessibleTextInsertEvent14changePositionEv',
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

  @overload(QObject, int, str)
  @overload(NoneType, int, str)
  def __init__(
      self,
      obj: Optional[QObject],
      position: int,
      text: str,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleTextInsertEvent::QAccessibleTextInsertEvent(QObject *obj, int
    position, const QString &text)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextinsertevent.html

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    position : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QAccessibleTextInsertEvent::QAccessibleTextInsertEvent(QObject *obj,
    #      int position, const QString &text)
    self._noteCreation(QAccessibleTextInsertEvent, lambda: Rituals.call(
        'ritual_ZN26QAccessibleTextInsertEventC1EP7QObjectiRK7QString',
        self._addressOf(obj), position, text,
    ))

  @overload(QAccessibleInterface, int, str)
  def __init__(
      self,
      iface: Optional[QAccessibleInterface],
      position: int,
      text: str,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleTextInsertEvent::QAccessibleTextInsertEvent(
    QAccessibleInterface *iface, int position, const QString &text)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextinsertevent.html

    Parameters
    ----------

    iface : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    position : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QAccessibleTextInsertEvent::QAccessibleTextInsertEvent(
    #      QAccessibleInterface *iface, int position, const QString &text)
    self._noteCreation(QAccessibleTextInsertEvent, lambda: Rituals.call(
        'ritual_ZN26QAccessibleTextInsertEventC1EP20QAccessibleInterfaceiRK'
        '7QString',
        self._addressOf(iface), position, text,
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
