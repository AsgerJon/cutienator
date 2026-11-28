"""
QWindowSystemEventHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from . import QWindowSystemInterfacePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWindowSystemEventHandler(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWindowSystemEventHandler: a plain Python object
  standing in front of one C++ QWindowSystemEventHandler.

  C++ hands a QWindowSystemEventHandler around as a copy, so every C++
  QWindowSystemEventHandler behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QWindowSystemEventHandler that has a ritual and that
  Python can call so far, 1 name in all: 'sendEvent'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWindowSystemEventHandler::~QWindowSystemEventHandler()': the
    destructor: Python removes its C++ QWindowSystemEventHandler by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QWindowSystemEventHandler is created at the first use, not by
    'QWindowSystemEventHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWindowSystemEventHandler back gives a copy the
    ritual made for Python, in a new cute QWindowSystemEventHandler.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWindowSystemEventHandler'

  #  A C++ QWindowSystemEventHandler Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWindowSystemEventHandler'

  #  The functions Qt calls itself that QWindowSystemEventHandler is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'sendEvent': (
          ('_ZN25QWindowSystemEventHandler9sendEventEPN29QWindowSystemInter'
           'facePrivate17WindowSystemEventE',
           ('bool', 'number', ''),
           (
               ('address', 'address',
                'QtGui:QWindowSystemInterfacePrivate.WindowSystemEvent'),
           )),
      ),
  }

  #  Qt's '~QWindowSystemEventHandler()'. Naming it makes this a value class:
  #  Python owns every C++ QWindowSystemEventHandler behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QWindowSystemEventHandlerD1Ev'

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload(QWindowSystemInterfacePrivate.WindowSystemEvent)
  @overload(NoneType)
  def sendEvent(
      self,
      event: Optional[QWindowSystemInterfacePrivate.WindowSystemEvent],
  ) -> bool:
    """
    Calls Qt's 'bool
    QWindowSystemEventHandler::sendEvent(QWindowSystemInterfacePrivate::
    WindowSystemEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsystemeventhandler.html#sendEvent

    Parameters
    ----------

    event : Optional[QWindowSystemInterfacePrivate.WindowSystemEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWindowSystemEventHandler::sendEvent(
    #      QWindowSystemInterfacePrivate::WindowSystemEvent *event)
    ritual = (
        'ritual_ZN25QWindowSystemEventHandler9sendEventEPN29QWindowSystemIn'
        'terfacePrivate17WindowSystemEventE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QWindowSystemEventHandler9sendEventEPN29QWindowSy'
          'stemInterfacePrivate17WindowSystemEventE')
    return self.uglySide.call(ritual, self._addressOf(event))
