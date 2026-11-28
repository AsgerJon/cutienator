"""
QChildWindowEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qevent.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QChildWindowEvent(QEvent):
  """
  The cute side of Qt's QChildWindowEvent: a plain Python object standing in
  front of one C++ QChildWindowEvent.

  It is built on the cute 'QEvent', as Qt's QChildWindowEvent is built on
  Qt's QEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QChildWindowEvent that has a ritual and that Python
  can call so far, 2 names in all: 'clone', 'child'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QChildWindowEvent::QChildWindowEvent(const QChildWindowEvent &a0)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QChildWindowEvent &QChildWindowEvent::operator=(const
    QChildWindowEvent &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QChildWindowEvent::~QChildWindowEvent()': the destructor: Python
    never removes a C++ QChildWindowEvent.

  What has no ritual
  ------------------

  2 of the 8 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QChildWindowEvent is created at the first use, not by
    'QChildWindowEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QChildWindowEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QChildWindowEvent'

  #  A C++ QChildWindowEvent Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QChildWindowEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QChildWindowEvent]:
    """
    Calls Qt's 'QChildWindowEvent *QChildWindowEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchildwindowevent.html#clone

    Returns
    -------

    Optional[QChildWindowEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QChildWindowEvent *QChildWindowEvent::clone() const
    ritual = 'ritual_ZNK17QChildWindowEvent5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QChildWindowEvent5cloneEv'
    address = self.uglySide.call(ritual)
    return QChildWindowEvent._cuteAt(address)

  def child(self) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QChildWindowEvent::child() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchildwindowevent.html#child

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QChildWindowEvent::child() const
    address = self.uglySide.call('ritual_ZNK17QChildWindowEvent5childEv')
    from . import QWindow
    return QWindow._cuteAt(address)

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

  @overload(QEvent.Type, QWindow)
  @overload(QEvent.Type, NoneType)
  def __init__(
      self,
      type: QEvent.Type,
      childWindow: Optional[QWindow],
  ) -> None:
    """
    Notes what was given, for Qt's 'QChildWindowEvent::QChildWindowEvent(Type
    type, QWindow *childWindow)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qchildwindowevent.html#QChildWindowEvent

    Parameters
    ----------

    type : QEvent.Type
      Passed on as its number.

    childWindow : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QChildWindowEvent::QChildWindowEvent(Type type, QWindow *childWindow)
    self._noteCreation(QChildWindowEvent, lambda: Rituals.call(
        'ritual_ZN17QChildWindowEventC1EN6QEvent4TypeEP7QWindow',
        type.value, self._addressOf(childWindow),
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
