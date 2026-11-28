"""
QFocusEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qevent.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import Qt, QEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QFocusEvent(QEvent):
  """
  The cute side of Qt's QFocusEvent: a plain Python object standing in front
  of one C++ QFocusEvent.

  It is built on the cute 'QEvent', as Qt's QFocusEvent is built on Qt's
  QEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFocusEvent that has a ritual and that Python can
  call so far, 4 names in all: 'clone', 'gotFocus', 'lostFocus', 'reason'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFocusEvent::QFocusEvent(const QFocusEvent &a0)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QFocusEvent &QFocusEvent::operator=(const QFocusEvent &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QFocusEvent::~QFocusEvent()': the destructor: Python never removes
    a C++ QFocusEvent.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QFocusEvent is created at the first use, not by
    'QFocusEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFocusEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFocusEvent'

  #  A C++ QFocusEvent Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFocusEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QFocusEvent]:
    """
    Calls Qt's 'QFocusEvent *QFocusEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfocusevent.html#clone

    Returns
    -------

    Optional[QFocusEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFocusEvent *QFocusEvent::clone() const
    ritual = 'ritual_ZNK11QFocusEvent5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFocusEvent5cloneEv'
    address = self.uglySide.call(ritual)
    return QFocusEvent._cuteAt(address)

  def gotFocus(self) -> bool:
    """
    Calls Qt's 'bool QFocusEvent::gotFocus() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfocusevent.html#gotFocus
    """
    #  bool QFocusEvent::gotFocus() const
    return self.uglySide.call('ritual_ZNK11QFocusEvent8gotFocusEv')

  def lostFocus(self) -> bool:
    """
    Calls Qt's 'bool QFocusEvent::lostFocus() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfocusevent.html#lostFocus
    """
    #  bool QFocusEvent::lostFocus() const
    return self.uglySide.call('ritual_ZNK11QFocusEvent9lostFocusEv')

  def reason(self) -> Qt.FocusReason:
    """
    Calls Qt's 'Qt::FocusReason QFocusEvent::reason() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfocusevent.html#reason

    Returns
    -------

    Qt.FocusReason
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.FocusReason(number)'
      gives.
    """
    #  Qt::FocusReason QFocusEvent::reason() const
    return Qt.FocusReason(self.uglySide.call(
        'ritual_ZNK11QFocusEvent6reasonEv',
    ))

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

  @overload(QEvent.Type)
  @overload(QEvent.Type, Qt.FocusReason)
  def __init__(
      self,
      type: QEvent.Type,
      reason: Qt.FocusReason = Qt.FocusReason.OtherFocusReason,
  ) -> None:
    """
    Notes what was given, for Qt's 'QFocusEvent::QFocusEvent(Type type,
    Qt::FocusReason reason)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfocusevent.html#QFocusEvent

    Parameters
    ----------

    type : QEvent.Type
      Passed on as its number.

    reason : Qt.FocusReason
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.FocusReason.OtherFocusReason.
    """
    #  QFocusEvent::QFocusEvent(Type type, Qt::FocusReason reason)
    self._noteCreation(QFocusEvent, lambda: Rituals.call(
        'ritual_ZN11QFocusEventC1EN6QEvent4TypeEN2Qt11FocusReasonE',
        type.value, reason.value,
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
