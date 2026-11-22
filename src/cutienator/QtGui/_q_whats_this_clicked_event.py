"""
QWhatsThisClickedEvent binding of the Qt C++
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


class QWhatsThisClickedEvent(QEvent):
  """
  The cute side of Qt's QWhatsThisClickedEvent: a plain Python object
  standing in front of one C++ QWhatsThisClickedEvent.

  It is built on the cute 'QEvent', as Qt's QWhatsThisClickedEvent is built
  on Qt's QEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWhatsThisClickedEvent that has a ritual and that
  Python can call so far, 2 names in all: 'clone', 'href'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWhatsThisClickedEvent::~QWhatsThisClickedEvent()': the destructor:
    Python never removes a C++ QWhatsThisClickedEvent.

  What has no ritual
  ------------------

  4 of the 8 functions Qt declares: 2 protected; 2 forbidden.

  What to expect
  --------------

  - The C++ QWhatsThisClickedEvent is created at the first use, not by
    'QWhatsThisClickedEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWhatsThisClickedEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWhatsThisClickedEvent'

  #  A C++ QWhatsThisClickedEvent Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWhatsThisClickedEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QWhatsThisClickedEvent]:
    """
    Calls Qt's 'QWhatsThisClickedEvent *QWhatsThisClickedEvent::clone()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwhatsthisclickedevent.html#clone

    Returns
    -------

    Optional[QWhatsThisClickedEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWhatsThisClickedEvent *QWhatsThisClickedEvent::clone() const
    ritual = 'ritual_ZNK22QWhatsThisClickedEvent5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QWhatsThisClickedEvent5cloneEv'
    address = self.uglySide.call(ritual)
    return QWhatsThisClickedEvent._cuteAt(address)

  def href(self) -> str:
    """
    Calls Qt's 'QString QWhatsThisClickedEvent::href() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwhatsthisclickedevent.html#href

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWhatsThisClickedEvent::href() const
    return self.uglySide.call('ritual_ZNK22QWhatsThisClickedEvent4hrefEv')

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
  def __init__(self, href: str) -> None:
    """
    Notes what was given, for Qt's
    'QWhatsThisClickedEvent::QWhatsThisClickedEvent(const QString &href)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwhatsthisclickedevent.html#QWhatsThisClickedEvent

    Parameters
    ----------

    href : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QWhatsThisClickedEvent::QWhatsThisClickedEvent(const QString &href)
    self._noteCreation(QWhatsThisClickedEvent, lambda: Rituals.call(
        'ritual_ZN22QWhatsThisClickedEventC1ERK7QString', href,
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
