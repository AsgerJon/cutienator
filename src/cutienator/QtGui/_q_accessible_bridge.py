"""
QAccessibleBridge binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qaccessiblebridge.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QAccessibleEvent, QAccessibleInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAccessibleEvent = WAIT['QAccessibleEvent']
  QAccessibleInterface = WAIT['QAccessibleInterface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleBridge(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAccessibleBridge: a plain Python object standing in
  front of one C++ QAccessibleBridge.

  What exists
  -----------

  Every function of Qt's QAccessibleBridge that has a ritual and that Python
  can call so far, 2 names in all: 'setRootObject',
  'notifyAccessibilityUpdate'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAccessibleBridge::~QAccessibleBridge()': the destructor: Python
    never removes a C++ QAccessibleBridge.

  What to expect
  --------------

  - The C++ QAccessibleBridge is created at the first use, not by
    'QAccessibleBridge(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleBridge.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleBridge'

  #  A C++ QAccessibleBridge Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleBridge'

  #  The functions Qt calls itself that QAccessibleBridge is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setRootObject': (
          ('_ZN17QAccessibleBridge13setRootObjectEP20QAccessibleInterface',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QAccessibleInterface'),
           )),
      ),
      'notifyAccessibilityUpdate': (
          ('_ZN17QAccessibleBridge25notifyAccessibilityUpdateEP16QAccessibl'
           'eEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QAccessibleEvent'),
           )),
      ),
  }

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

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def setRootObject(self, a0: Optional[QAccessibleInterface]) -> None:
    """
    Calls Qt's 'void QAccessibleBridge::setRootObject(QAccessibleInterface
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblebridge.html#setRootObject

    Parameters
    ----------

    a0 : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAccessibleBridge::setRootObject(QAccessibleInterface *a0)
    self.uglySide.call(
        'ritual_ZN17QAccessibleBridge13setRootObjectEP20QAccessibleInterfac'
        'e',
        self._addressOf(a0, 'QAccessibleInterface'),
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

  @overload(QAccessibleEvent)
  @overload(NoneType)
  def notifyAccessibilityUpdate(
      self,
      event: Optional[QAccessibleEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QAccessibleBridge::notifyAccessibilityUpdate(QAccessibleEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblebridge.html#notifyAccessibilityUpdate

    Parameters
    ----------

    event : Optional[QAccessibleEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAccessibleBridge::notifyAccessibilityUpdate(QAccessibleEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN17QAccessibleBridge25notifyAccessibilityUpdateEP16QAccess'
        'ibleEvent',
        self._addressOf(event),
    )
