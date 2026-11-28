"""
QAccessibleObjectDestroyedEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qaccessiblecache_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QAccessibleObjectDestroyedEvent to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QAccessibleEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
  from . import QAccessibleInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAccessibleInterface = WAIT['QAccessibleInterface']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleObjectDestroyedEvent(QAccessibleEvent):
  """
  The cute side of Qt's QAccessibleObjectDestroyedEvent: a plain Python
  object standing in front of one C++ QAccessibleObjectDestroyedEvent.

  It is built on the cute 'QAccessibleEvent', as Qt's
  QAccessibleObjectDestroyedEvent is built on Qt's QAccessibleEvent, and has
  everything that class has.

  What exists
  -----------

  No function of Qt's QAccessibleObjectDestroyedEvent yet. It can be made
  from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QAccessibleObjectDestroyedEvent::~QAccessibleObjectDestroyedEvent()':
    the destructor: Python never removes a C++
    QAccessibleObjectDestroyedEvent.

  What to expect
  --------------

  - The C++ QAccessibleObjectDestroyedEvent is created at the first use, not
    by 'QAccessibleObjectDestroyedEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleObjectDestroyedEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleObjectDestroyedEvent'

  #  A C++ QAccessibleObjectDestroyedEvent Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleObjectDestroyedEvent'

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

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, obj: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleObjectDestroyedEvent::QAccessibleObjectDestroyedEvent(QObject
    *obj)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleobjectdestroyedevent.html

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAccessibleObjectDestroyedEvent::QAccessibleObjectDestroyedEvent(
    #      QObject *obj)
    self._noteCreation(QAccessibleObjectDestroyedEvent, lambda: Rituals.call(
        'ritual_ZN31QAccessibleObjectDestroyedEventC1EP7QObject',
        self._addressOf(obj, 'QObject'),
    ))

  @overload(QAccessibleInterface)
  def __init__(self, iface: Optional[QAccessibleInterface]) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleObjectDestroyedEvent::QAccessibleObjectDestroyedEvent(
    QAccessibleInterface *iface)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleobjectdestroyedevent.html

    Parameters
    ----------

    iface : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAccessibleObjectDestroyedEvent::QAccessibleObjectDestroyedEvent(
    #      QAccessibleInterface *iface)
    self._noteCreation(QAccessibleObjectDestroyedEvent, lambda: Rituals.call(
        'ritual_ZN31QAccessibleObjectDestroyedEventC1EP20QAccessibleInterfa'
        'ce',
        self._addressOf(iface, 'QAccessibleInterface'),
    ))

  @overload(int)
  def __init__(self, uniqueId: int) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleObjectDestroyedEvent::QAccessibleObjectDestroyedEvent(
    QAccessible::Id uniqueId)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleobjectdestroyedevent.html

    Parameters
    ----------

    uniqueId : int
      Passed on as it is.
    """
    #  QAccessibleObjectDestroyedEvent::QAccessibleObjectDestroyedEvent(
    #      QAccessible::Id uniqueId)
    self._noteCreation(QAccessibleObjectDestroyedEvent, lambda: Rituals.call(
        'ritual_ZN31QAccessibleObjectDestroyedEventC1Ej', uniqueId,
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
