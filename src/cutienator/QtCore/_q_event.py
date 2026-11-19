"""
QEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qcoreevent.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ._q_event_type import Type

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QEvent(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QEvent: a plain Python object standing in front of
  one C++ QEvent.

  What exists
  -----------

  Every function of Qt's QEvent that has a ritual and that Python can call so
  far, 11 names in all: 'type', 'spontaneous', 'setAccepted', 'isAccepted',
  'accept', 'ignore', 'isInputEvent', 'isPointerEvent', 'isSinglePointEvent',
  'registerEventType', 'clone'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QEvent::~QEvent()': the destructor: Python never removes a C++
    QEvent.

  What has no ritual
  ------------------

  11 of the 24 functions Qt declares: 5 protected; 2 private; 2 forbidden; 1
  declared and nowhere to be found; 1 a template.

  What to expect
  --------------

  - The C++ QEvent is created at the first use, not by 'QEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QEvent.
  """

  #  The enums Qt writes inside QEvent, and the names Qt has for the
  #  combinations of its flags enums.
  Type = Type

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload()
  @overload(int)
  def registerEventType(hint: int = -1) -> int:
    """
    Calls Qt's 'int QEvent::registerEventType(int hint)'.

    Qt's own words: https://doc.qt.io/qt-6/qevent.html#registerEventType

    Parameters
    ----------

    hint : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  int QEvent::registerEventType(int hint)
    return Rituals.call('ritual_ZN6QEvent17registerEventTypeEi', hint)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> Type:
    """
    Calls Qt's 'Type QEvent::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qevent.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QEvent::type() const
    return Type(self.uglySide.call('ritual_ZNK6QEvent4typeEv'))

  def spontaneous(self) -> bool:
    """
    Calls Qt's 'bool QEvent::spontaneous() const'.

    Qt's own words: https://doc.qt.io/qt-6/qevent.html#spontaneous
    """
    #  bool QEvent::spontaneous() const
    return self.uglySide.call('ritual_ZNK6QEvent11spontaneousEv')

  def isAccepted(self) -> bool:
    """
    Calls Qt's 'bool QEvent::isAccepted() const'.

    Qt's own words: https://doc.qt.io/qt-6/qevent.html#isAccepted
    """
    #  bool QEvent::isAccepted() const
    return self.uglySide.call('ritual_ZNK6QEvent10isAcceptedEv')

  def isInputEvent(self) -> bool:
    """
    Calls Qt's 'bool QEvent::isInputEvent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qevent.html#isInputEvent
    """
    #  bool QEvent::isInputEvent() const
    return self.uglySide.call('ritual_ZNK6QEvent12isInputEventEv')

  def isPointerEvent(self) -> bool:
    """
    Calls Qt's 'bool QEvent::isPointerEvent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qevent.html#isPointerEvent
    """
    #  bool QEvent::isPointerEvent() const
    return self.uglySide.call('ritual_ZNK6QEvent14isPointerEventEv')

  def isSinglePointEvent(self) -> bool:
    """
    Calls Qt's 'bool QEvent::isSinglePointEvent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qevent.html#isSinglePointEvent
    """
    #  bool QEvent::isSinglePointEvent() const
    return self.uglySide.call('ritual_ZNK6QEvent18isSinglePointEventEv')

  def clone(self) -> Optional[QEvent]:
    """
    Calls Qt's 'QEvent *QEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qevent.html#clone

    Returns
    -------

    Optional[QEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QEvent *QEvent::clone() const
    address = self.uglySide.call('ritual_ZNK6QEvent5cloneEv')
    return QEvent._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAccepted(self, accepted: bool) -> None:
    """
    Calls Qt's 'void QEvent::setAccepted(bool accepted)'.

    Qt's own words: https://doc.qt.io/qt-6/qevent.html#setAccepted

    Parameters
    ----------

    accepted : bool
      Passed on as it is.
    """
    #  void QEvent::setAccepted(bool accepted)
    self.uglySide.call('ritual_ZN6QEvent11setAcceptedEb', accepted)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Type)
  def __init__(self, type: Type) -> None:
    """
    Notes what was given, for Qt's 'QEvent::QEvent(Type type)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qevent.html#QEvent

    Parameters
    ----------

    type : Type
      Passed on as its number.
    """
    #  QEvent::QEvent(Type type)
    self._noteCreation(QEvent, lambda: Rituals.call(
        'ritual_ZN6QEventC1ENS_4TypeE', type.value,
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

  def accept(self) -> None:
    """
    Calls Qt's 'void QEvent::accept()'.

    Qt's own words: https://doc.qt.io/qt-6/qevent.html#accept
    """
    #  void QEvent::accept()
    self.uglySide.call('ritual_ZN6QEvent6acceptEv')

  def ignore(self) -> None:
    """
    Calls Qt's 'void QEvent::ignore()'.

    Qt's own words: https://doc.qt.io/qt-6/qevent.html#ignore
    """
    #  void QEvent::ignore()
    self.uglySide.call('ritual_ZN6QEvent6ignoreEv')
