"""
QEvent binding of the Qt C++, so far with what QObject needs of it.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from cutienator.cute._cute_mixin import CuteMixin
from cutienator.cute._meta_cute import MetaCute
from cutienator.occult._ugly import Ugly
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QEvent(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QEvent, so far with what 'QObject' needs of it.
  'QObject.event' and 'QObject.eventFilter' take one, and a signature can
  only name a cute class.

    event = QEvent(0)          # 0 is Qt's 'QEvent::None'
    QObject().event(event)     # False: nothing took it
    event.isAccepted()         # True, as Qt makes every event

  What exists so far
  ------------------

  - Creation from the number of an event type. Qt's 'QEvent::Type' is an
    enum, and no enum is reflected yet, so the number is passed as it
    is.
  - 'type', 'isAccepted', 'accept' and 'ignore', each reflecting the Qt
    function of the same name through a ritual.

  What to expect
  --------------

  - The C++ QEvent is created at the first use, not by 'QEvent(0)'.
  - Python never removes the C++ QEvent. C++ cannot copy one, so it is
    no value, and Qt may keep one it is handed.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables

  #  Fallback Variables

  #  Private Variables
  #  The number of the event type given to the constructor.
  __given_type__: Optional[int] = None

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _createUglySide(self, ) -> None:
    """
    Creates the C++ QEvent and the Ugly standing for it.

    'CuteMixin' calls this at the first read of 'uglySide'. The C++
    QEvent is created with the type number given to 'QEvent(...)'.
    """
    #  QEvent::QEvent(Type type)
    ritualName = 'ritual_ZN6QEventC1ENS_4TypeE'
    ugly = Ugly()
    address = Rituals.call(ritualName, self.__given_type__)
    ugly.setAddress(address)
    ugly.setCuteSide(self)
    self.__ugly_side__ = ugly

  def type(self) -> int:
    """
    Calls Qt's 'Type QEvent::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qevent.html#type

    Returns
    -------

    int
      The number of the event type. Qt's 'QEvent::Type' is an enum, and
      no enum is reflected yet.
    """
    #  Type QEvent::type() const
    return self.uglySide.call('ritual_ZNK6QEvent4typeEv')

  def isAccepted(self) -> bool:
    """
    Calls Qt's 'bool QEvent::isAccepted() const'.

    Qt's own words: https://doc.qt.io/qt-6/qevent.html#accepted-prop
    """
    #  bool QEvent::isAccepted() const
    return self.uglySide.call('ritual_ZNK6QEvent10isAcceptedEv')

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

  @overload(int)
  def __init__(self, eventType: int) -> None:
    """
    Notes the event type for Qt's 'QEvent::QEvent(Type type)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qevent.html#QEvent

    Parameters
    ----------

    eventType : int
      The number of the event type, as 0 for Qt's 'QEvent::None'.

    Raises
    ------

    DispatchException
      Called with anything but one 'int'.
    """
    self.__given_type__ = eventType

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
