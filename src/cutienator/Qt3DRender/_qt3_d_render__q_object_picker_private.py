"""
Qt3DRender::QObjectPickerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qobjectpicker_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::QObjectPickerPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QObjectPickerPrivate(Qt3DCore.QComponentPrivate):
  """
  The cute side of Qt's Qt3DRender::QObjectPickerPrivate: a plain Python
  object standing in front of one C++ Qt3DRender::QObjectPickerPrivate.

  It is built on the cute 'Qt3DCore::QComponentPrivate', as Qt's
  Qt3DRender::QObjectPickerPrivate is built on Qt's
  Qt3DCore::QComponentPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QObjectPickerPrivate that has a ritual
  and that Python can call so far, 8 names in all: 'q_func',
  'propagateEvent', 'pressedEvent', 'clickedEvent', 'movedEvent',
  'releasedEvent', 'setPressed', 'setContainsMouse'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QObjectPicker *Qt3DRender::QObjectPickerPrivate::q_func()
    const': takes in Python what 'QObjectPicker
    *Qt3DRender::QObjectPickerPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DRender::QObjectPickerPrivate is created at the first use, not
    by 'Qt3DRender::QObjectPickerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QObjectPickerPrivate.
  """

  #  The enums Qt writes inside Qt3DRender::QObjectPickerPrivate, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class EventType(CuteNum):
    """
    The enum 'Qt3DRender::QObjectPickerPrivate::EventType' of Qt, with the 4
    names Qt gives in it.
    """

    Pressed = Kee[int](0)
    Released = Kee[int](1)
    Clicked = Kee[int](2)
    Moved = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QObjectPickerPrivate'

  #  A C++ Qt3DRender::QObjectPickerPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QObjectPickerPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setPressed(self, pressed: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::QObjectPickerPrivate::setPressed(bool
    pressed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qobjectpickerprivate.html#setPressed

    Parameters
    ----------

    pressed : bool
      Passed on as it is.
    """
    #  void Qt3DRender::QObjectPickerPrivate::setPressed(bool pressed)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender20QObjectPickerPrivate10setPressedEb', pressed,
    )

  @overload(bool)
  def setContainsMouse(self, containsMouse: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::QObjectPickerPrivate::setContainsMouse(bool
    containsMouse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qobjectpickerprivate.html

    Parameters
    ----------

    containsMouse : bool
      Passed on as it is.
    """
    #  void Qt3DRender::QObjectPickerPrivate::setContainsMouse(bool
    #      containsMouse)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender20QObjectPickerPrivate16setContainsMouseEb',
        containsMouse,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QObjectPickerPrivate::QObjectPickerPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qobjectpickerprivate.html
    """
    #  Qt3DRender::QObjectPickerPrivate::QObjectPickerPrivate()
    self._noteCreation(QObjectPickerPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender20QObjectPickerPrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DRender.QObjectPicker]:
    """
    Calls Qt's 'QObjectPicker *Qt3DRender::QObjectPickerPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qobjectpickerprivate.html#q_func

    Returns
    -------

    Optional[Qt3DRender.QObjectPicker]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObjectPicker *Qt3DRender::QObjectPickerPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender20QObjectPickerPrivate6q_funcEv',
    )
    return Qt3DRender.QObjectPicker._cuteAt(address)

  @overload(WAIT['Qt3DRender.QPickEvent'], EventType)
  @overload(NoneType, EventType)
  def propagateEvent(
      self,
      event: Optional[Qt3DRender.QPickEvent],
      type: EventType,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QObjectPickerPrivate::propagateEvent(QPickEvent *event,
    EventType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qobjectpickerprivate.html

    Parameters
    ----------

    event : Optional[Qt3DRender.QPickEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type : EventType
      Passed on as its number.
    """
    #  void Qt3DRender::QObjectPickerPrivate::propagateEvent(QPickEvent
    #      *event, EventType type)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender20QObjectPickerPrivate14propagateEventEPNS_10'
        'QPickEventENS0_9EventTypeE',
        self._addressOf(event), type.value,
    )

  @overload(WAIT['Qt3DRender.QPickEvent'])
  @overload(NoneType)
  def pressedEvent(self, event: Optional[Qt3DRender.QPickEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QObjectPickerPrivate::pressedEvent(QPickEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qobjectpickerprivate.html#pressedEvent

    Parameters
    ----------

    event : Optional[Qt3DRender.QPickEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QObjectPickerPrivate::pressedEvent(QPickEvent *event)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender20QObjectPickerPrivate12pressedEventEPNS_10QP'
        'ickEventE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DRender.QPickEvent'])
  @overload(NoneType)
  def clickedEvent(self, event: Optional[Qt3DRender.QPickEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QObjectPickerPrivate::clickedEvent(QPickEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qobjectpickerprivate.html#clickedEvent

    Parameters
    ----------

    event : Optional[Qt3DRender.QPickEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QObjectPickerPrivate::clickedEvent(QPickEvent *event)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender20QObjectPickerPrivate12clickedEventEPNS_10QP'
        'ickEventE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DRender.QPickEvent'])
  @overload(NoneType)
  def movedEvent(self, event: Optional[Qt3DRender.QPickEvent]) -> None:
    """
    Calls Qt's 'void Qt3DRender::QObjectPickerPrivate::movedEvent(QPickEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qobjectpickerprivate.html#movedEvent

    Parameters
    ----------

    event : Optional[Qt3DRender.QPickEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QObjectPickerPrivate::movedEvent(QPickEvent *event)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender20QObjectPickerPrivate10movedEventEPNS_10QPic'
        'kEventE',
        self._addressOf(event),
    )

  @overload(WAIT['Qt3DRender.QPickEvent'])
  @overload(NoneType)
  def releasedEvent(self, event: Optional[Qt3DRender.QPickEvent]) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QObjectPickerPrivate::releasedEvent(QPickEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qobjectpickerprivate.html#releasedEvent

    Parameters
    ----------

    event : Optional[Qt3DRender.QPickEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QObjectPickerPrivate::releasedEvent(QPickEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender20QObjectPickerPrivate13releasedEventEPNS_10Q'
        'PickEventE',
        self._addressOf(event),
    )
