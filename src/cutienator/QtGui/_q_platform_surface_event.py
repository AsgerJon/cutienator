"""
QPlatformSurfaceEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qevent.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum
from ..occult import Rituals
from ..QtCore import QEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QPlatformSurfaceEvent(QEvent):
  """
  The cute side of Qt's QPlatformSurfaceEvent: a plain Python object standing
  in front of one C++ QPlatformSurfaceEvent.

  It is built on the cute 'QEvent', as Qt's QPlatformSurfaceEvent is built on
  Qt's QEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformSurfaceEvent that has a ritual and that
  Python can call so far, 2 names in all: 'clone', 'surfaceEventType'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlatformSurfaceEvent::~QPlatformSurfaceEvent()': the destructor:
    Python never removes a C++ QPlatformSurfaceEvent.

  What has no ritual
  ------------------

  4 of the 8 functions Qt declares: 2 protected; 2 forbidden.

  What to expect
  --------------

  - The C++ QPlatformSurfaceEvent is created at the first use, not by
    'QPlatformSurfaceEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformSurfaceEvent.
  """

  #  The enums Qt writes inside QPlatformSurfaceEvent, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class SurfaceEventType(CuteNum):
    """
    The enum 'QPlatformSurfaceEvent::SurfaceEventType' of Qt, with the 2
    names Qt gives in it.
    """

    SurfaceCreated = Kee[int](0)
    SurfaceAboutToBeDestroyed = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformSurfaceEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QPlatformSurfaceEvent]:
    """
    Calls Qt's 'QPlatformSurfaceEvent *QPlatformSurfaceEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformsurfaceevent.html#clone

    Returns
    -------

    Optional[QPlatformSurfaceEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformSurfaceEvent *QPlatformSurfaceEvent::clone() const
    address = self.uglySide.call('ritual_ZNK21QPlatformSurfaceEvent5cloneEv')
    return QPlatformSurfaceEvent._cuteAt(address)

  def surfaceEventType(self) -> SurfaceEventType:
    """
    Calls Qt's 'SurfaceEventType QPlatformSurfaceEvent::surfaceEventType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsurfaceevent.html#surfaceEventType

    Returns
    -------

    SurfaceEventType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SurfaceEventType(number)'
      gives.
    """
    #  SurfaceEventType QPlatformSurfaceEvent::surfaceEventType() const
    return QPlatformSurfaceEvent.SurfaceEventType(self.uglySide.call(
        'ritual_ZNK21QPlatformSurfaceEvent16surfaceEventTypeEv',
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

  @overload(SurfaceEventType)
  def __init__(self, surfaceEventType: SurfaceEventType) -> None:
    """
    Notes what was given, for Qt's
    'QPlatformSurfaceEvent::QPlatformSurfaceEvent(SurfaceEventType
    surfaceEventType)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsurfaceevent.html#QPlatformSurfaceEvent

    Parameters
    ----------

    surfaceEventType : SurfaceEventType
      Passed on as its number.
    """
    #  QPlatformSurfaceEvent::QPlatformSurfaceEvent(SurfaceEventType
    #      surfaceEventType)
    self._noteCreation(QPlatformSurfaceEvent, lambda: Rituals.call(
        'ritual_ZN21QPlatformSurfaceEventC1ENS_16SurfaceEventTypeE',
        surfaceEventType.value,
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
