"""
QToolBarChangeEvent binding of the Qt C++
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


class QToolBarChangeEvent(QEvent):
  """
  The cute side of Qt's QToolBarChangeEvent: a plain Python object standing
  in front of one C++ QToolBarChangeEvent.

  It is built on the cute 'QEvent', as Qt's QToolBarChangeEvent is built on
  Qt's QEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QToolBarChangeEvent that has a ritual and that
  Python can call so far, 2 names in all: 'clone', 'toggle'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QToolBarChangeEvent::QToolBarChangeEvent(const QToolBarChangeEvent
    &a0)': takes a type Python has no way to hand over yet.
  - Qt's 'QToolBarChangeEvent &QToolBarChangeEvent::operator=(const
    QToolBarChangeEvent &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QToolBarChangeEvent::~QToolBarChangeEvent()': the destructor:
    Python never removes a C++ QToolBarChangeEvent.

  What has no ritual
  ------------------

  2 of the 8 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QToolBarChangeEvent is created at the first use, not by
    'QToolBarChangeEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QToolBarChangeEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QToolBarChangeEvent'

  #  A C++ QToolBarChangeEvent Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QToolBarChangeEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QToolBarChangeEvent]:
    """
    Calls Qt's 'QToolBarChangeEvent *QToolBarChangeEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbarchangeevent.html#clone

    Returns
    -------

    Optional[QToolBarChangeEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QToolBarChangeEvent *QToolBarChangeEvent::clone() const
    ritual = 'ritual_ZNK19QToolBarChangeEvent5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QToolBarChangeEvent5cloneEv'
    address = self.uglySide.call(ritual)
    return QToolBarChangeEvent._cuteAt(address)

  def toggle(self) -> bool:
    """
    Calls Qt's 'bool QToolBarChangeEvent::toggle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbarchangeevent.html#toggle
    """
    #  bool QToolBarChangeEvent::toggle() const
    return self.uglySide.call('ritual_ZNK19QToolBarChangeEvent6toggleEv')

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

  @overload(bool)
  def __init__(self, t: bool) -> None:
    """
    Notes what was given, for Qt's
    'QToolBarChangeEvent::QToolBarChangeEvent(bool t)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbarchangeevent.html#QToolBarChangeEvent

    Parameters
    ----------

    t : bool
      Passed on as it is.
    """
    #  QToolBarChangeEvent::QToolBarChangeEvent(bool t)
    self._noteCreation(QToolBarChangeEvent, lambda: Rituals.call(
        'ritual_ZN19QToolBarChangeEventC1Eb', t,
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
