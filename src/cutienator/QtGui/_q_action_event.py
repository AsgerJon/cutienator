"""
QActionEvent binding of the Qt C++
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

  from . import QAction
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAction = WAIT['QAction']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QActionEvent(QEvent):
  """
  The cute side of Qt's QActionEvent: a plain Python object standing in front
  of one C++ QActionEvent.

  It is built on the cute 'QEvent', as Qt's QActionEvent is built on Qt's
  QEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QActionEvent that has a ritual and that Python can
  call so far, 3 names in all: 'clone', 'action', 'before'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QActionEvent::~QActionEvent()': the destructor: Python never
    removes a C++ QActionEvent.

  What has no ritual
  ------------------

  4 of the 9 functions Qt declares: 2 protected; 2 forbidden.

  What to expect
  --------------

  - The C++ QActionEvent is created at the first use, not by
    'QActionEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QActionEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QActionEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QActionEvent]:
    """
    Calls Qt's 'QActionEvent *QActionEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qactionevent.html#clone

    Returns
    -------

    Optional[QActionEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QActionEvent *QActionEvent::clone() const
    address = self.uglySide.call('ritual_ZNK12QActionEvent5cloneEv')
    return QActionEvent._cuteAt(address)

  def action(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QActionEvent::action() const'.

    Qt's own words: https://doc.qt.io/qt-6/qactionevent.html#action

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QActionEvent::action() const
    address = self.uglySide.call('ritual_ZNK12QActionEvent6actionEv')
    from . import QAction
    return QAction._cuteAt(address)

  def before(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QActionEvent::before() const'.

    Qt's own words: https://doc.qt.io/qt-6/qactionevent.html#before

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QActionEvent::before() const
    address = self.uglySide.call('ritual_ZNK12QActionEvent6beforeEv')
    from . import QAction
    return QAction._cuteAt(address)

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

  @overload(int, QAction)
  @overload(int, NoneType)
  @overload(int, QAction, QAction)
  @overload(int, QAction, NoneType)
  @overload(int, NoneType, QAction)
  @overload(int, NoneType, NoneType)
  def __init__(
      self,
      type: int,
      action: Optional[QAction],
      before: Optional[QAction] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QActionEvent::QActionEvent(int type,
    QAction *action, QAction *before)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qactionevent.html#QActionEvent

    Parameters
    ----------

    type : int
      Passed on as it is.

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    before : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QActionEvent::QActionEvent(int type, QAction *action, QAction *before)
    self._noteCreation(QActionEvent, lambda: Rituals.call(
        'ritual_ZN12QActionEventC1EiP7QActionS1_',
        type, self._addressOf(action), self._addressOf(before),
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
