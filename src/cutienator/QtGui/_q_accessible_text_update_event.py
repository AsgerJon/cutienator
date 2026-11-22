"""
QAccessibleTextUpdateEvent binding of the Qt C++
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


class QAccessibleTextUpdateEvent(QAccessibleTextCursorEvent):
  """
  The cute side of Qt's QAccessibleTextUpdateEvent: a plain Python object
  standing in front of one C++ QAccessibleTextUpdateEvent.

  It is built on the cute 'QAccessibleTextCursorEvent', as Qt's
  QAccessibleTextUpdateEvent is built on Qt's QAccessibleTextCursorEvent, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleTextUpdateEvent that has a ritual and
  that Python can call so far, 3 names in all: 'textRemoved', 'textInserted',
  'changePosition'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAccessibleTextUpdateEvent::~QAccessibleTextUpdateEvent()': the
    destructor: Python never removes a C++ QAccessibleTextUpdateEvent.

  What to expect
  --------------

  - The C++ QAccessibleTextUpdateEvent is created at the first use, not by
    'QAccessibleTextUpdateEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleTextUpdateEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleTextUpdateEvent'

  #  A C++ QAccessibleTextUpdateEvent Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleTextUpdateEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def textRemoved(self) -> str:
    """
    Calls Qt's 'QString QAccessibleTextUpdateEvent::textRemoved() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextupdateevent.html#textRemoved

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleTextUpdateEvent::textRemoved() const
    return self.uglySide.call(
        'ritual_ZNK26QAccessibleTextUpdateEvent11textRemovedEv',
    )

  def textInserted(self) -> str:
    """
    Calls Qt's 'QString QAccessibleTextUpdateEvent::textInserted() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextupdateevent.html#textInserted

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleTextUpdateEvent::textInserted() const
    return self.uglySide.call(
        'ritual_ZNK26QAccessibleTextUpdateEvent12textInsertedEv',
    )

  def changePosition(self) -> int:
    """
    Calls Qt's 'int QAccessibleTextUpdateEvent::changePosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextupdateevent.html#changePosition
    """
    #  int QAccessibleTextUpdateEvent::changePosition() const
    return self.uglySide.call(
        'ritual_ZNK26QAccessibleTextUpdateEvent14changePositionEv',
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

  @overload(QObject, int, str, str)
  @overload(NoneType, int, str, str)
  def __init__(
      self,
      obj: Optional[QObject],
      position: int,
      oldText: str,
      text: str,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleTextUpdateEvent::QAccessibleTextUpdateEvent(QObject *obj, int
    position, const QString &oldText, const QString &text)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextupdateevent.html

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    position : int
      Passed on as it is.

    oldText : str
      Passed on as it is: a QString is made of it for the call.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QAccessibleTextUpdateEvent::QAccessibleTextUpdateEvent(QObject *obj,
    #      int position, const QString &oldText, const QString &text)
    self._noteCreation(QAccessibleTextUpdateEvent, lambda: Rituals.call(
        'ritual_ZN26QAccessibleTextUpdateEventC1EP7QObjectiRK7QStringS4_',
        self._addressOf(obj), position, oldText, text,
    ))

  @overload(QAccessibleInterface, int, str, str)
  def __init__(
      self,
      iface: Optional[QAccessibleInterface],
      position: int,
      oldText: str,
      text: str,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleTextUpdateEvent::QAccessibleTextUpdateEvent(
    QAccessibleInterface *iface, int position, const QString &oldText, const
    QString &text)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextupdateevent.html

    Parameters
    ----------

    iface : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    position : int
      Passed on as it is.

    oldText : str
      Passed on as it is: a QString is made of it for the call.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QAccessibleTextUpdateEvent::QAccessibleTextUpdateEvent(
    #      QAccessibleInterface *iface, int position, const QString &oldText,
    #      const QString &text)
    self._noteCreation(QAccessibleTextUpdateEvent, lambda: Rituals.call(
        'ritual_ZN26QAccessibleTextUpdateEventC1EP20QAccessibleInterfaceiRK'
        '7QStringS4_',
        self._addressOf(iface), position, oldText, text,
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
