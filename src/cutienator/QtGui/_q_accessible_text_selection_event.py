"""
QAccessibleTextSelectionEvent binding of the Qt C++
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


class QAccessibleTextSelectionEvent(QAccessibleTextCursorEvent):
  """
  The cute side of Qt's QAccessibleTextSelectionEvent: a plain Python object
  standing in front of one C++ QAccessibleTextSelectionEvent.

  It is built on the cute 'QAccessibleTextCursorEvent', as Qt's
  QAccessibleTextSelectionEvent is built on Qt's QAccessibleTextCursorEvent,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleTextSelectionEvent that has a ritual and
  that Python can call so far, 3 names in all: 'setSelection',
  'selectionStart', 'selectionEnd'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAccessibleTextSelectionEvent::~QAccessibleTextSelectionEvent()':
    the destructor: Python never removes a C++ QAccessibleTextSelectionEvent.

  What to expect
  --------------

  - The C++ QAccessibleTextSelectionEvent is created at the first use, not by
    'QAccessibleTextSelectionEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleTextSelectionEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleTextSelectionEvent'

  #  A C++ QAccessibleTextSelectionEvent Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleTextSelectionEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def selectionStart(self) -> int:
    """
    Calls Qt's 'int QAccessibleTextSelectionEvent::selectionStart() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextselectionevent.html#selectionStart
    """
    #  int QAccessibleTextSelectionEvent::selectionStart() const
    return self.uglySide.call(
        'ritual_ZNK29QAccessibleTextSelectionEvent14selectionStartEv',
    )

  def selectionEnd(self) -> int:
    """
    Calls Qt's 'int QAccessibleTextSelectionEvent::selectionEnd() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextselectionevent.html#selectionEnd
    """
    #  int QAccessibleTextSelectionEvent::selectionEnd() const
    return self.uglySide.call(
        'ritual_ZNK29QAccessibleTextSelectionEvent12selectionEndEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int)
  def setSelection(self, start: int, end: int) -> None:
    """
    Calls Qt's 'void QAccessibleTextSelectionEvent::setSelection(int start,
    int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextselectionevent.html#setSelection

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QAccessibleTextSelectionEvent::setSelection(int start, int end)
    self.uglySide.call(
        'ritual_ZN29QAccessibleTextSelectionEvent12setSelectionEii',
        start, end,
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

  @overload(QObject, int, int)
  @overload(NoneType, int, int)
  def __init__(self, obj: Optional[QObject], start: int, end: int) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleTextSelectionEvent::QAccessibleTextSelectionEvent(QObject
    *obj, int start, int end)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextselectionevent.html

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  QAccessibleTextSelectionEvent::QAccessibleTextSelectionEvent(QObject
    #      *obj, int start, int end)
    self._noteCreation(QAccessibleTextSelectionEvent, lambda: Rituals.call(
        'ritual_ZN29QAccessibleTextSelectionEventC1EP7QObjectii',
        self._addressOf(obj), start, end,
    ))

  @overload(QAccessibleInterface, int, int)
  def __init__(
      self,
      iface: Optional[QAccessibleInterface],
      start: int,
      end: int,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleTextSelectionEvent::QAccessibleTextSelectionEvent(
    QAccessibleInterface *iface, int start, int end)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletextselectionevent.html

    Parameters
    ----------

    iface : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  QAccessibleTextSelectionEvent::QAccessibleTextSelectionEvent(
    #      QAccessibleInterface *iface, int start, int end)
    self._noteCreation(QAccessibleTextSelectionEvent, lambda: Rituals.call(
        'ritual_ZN29QAccessibleTextSelectionEventC1EP20QAccessibleInterface'
        'ii',
        self._addressOf(iface), start, end,
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
