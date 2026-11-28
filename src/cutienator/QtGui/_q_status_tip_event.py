"""
QStatusTipEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qevent.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QStatusTipEvent(QEvent):
  """
  The cute side of Qt's QStatusTipEvent: a plain Python object standing in
  front of one C++ QStatusTipEvent.

  It is built on the cute 'QEvent', as Qt's QStatusTipEvent is built on Qt's
  QEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QStatusTipEvent that has a ritual and that Python
  can call so far, 2 names in all: 'clone', 'tip'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStatusTipEvent::QStatusTipEvent(const QStatusTipEvent &a0)': takes
    a type Python has no way to hand over yet.
  - Qt's 'QStatusTipEvent &QStatusTipEvent::operator=(const QStatusTipEvent
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QStatusTipEvent::~QStatusTipEvent()': the destructor: Python never
    removes a C++ QStatusTipEvent.

  What has no ritual
  ------------------

  2 of the 8 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QStatusTipEvent is created at the first use, not by
    'QStatusTipEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStatusTipEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStatusTipEvent'

  #  A C++ QStatusTipEvent Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QStatusTipEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QStatusTipEvent]:
    """
    Calls Qt's 'QStatusTipEvent *QStatusTipEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstatustipevent.html#clone

    Returns
    -------

    Optional[QStatusTipEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStatusTipEvent *QStatusTipEvent::clone() const
    ritual = 'ritual_ZNK15QStatusTipEvent5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QStatusTipEvent5cloneEv'
    address = self.uglySide.call(ritual)
    return QStatusTipEvent._cuteAt(address)

  def tip(self) -> str:
    """
    Calls Qt's 'QString QStatusTipEvent::tip() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstatustipevent.html#tip

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStatusTipEvent::tip() const
    return self.uglySide.call('ritual_ZNK15QStatusTipEvent3tipEv')

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

  @overload(str)
  def __init__(self, tip: str) -> None:
    """
    Notes what was given, for Qt's 'QStatusTipEvent::QStatusTipEvent(const
    QString &tip)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatustipevent.html#QStatusTipEvent

    Parameters
    ----------

    tip : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QStatusTipEvent::QStatusTipEvent(const QString &tip)
    self._noteCreation(QStatusTipEvent, lambda: Rituals.call(
        'ritual_ZN15QStatusTipEventC1ERK7QString', tip,
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
