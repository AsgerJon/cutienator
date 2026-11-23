"""
QAccessibleAnnouncementEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QAccessible, QAccessibleEvent

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


class QAccessibleAnnouncementEvent(QAccessibleEvent):
  """
  The cute side of Qt's QAccessibleAnnouncementEvent: a plain Python object
  standing in front of one C++ QAccessibleAnnouncementEvent.

  It is built on the cute 'QAccessibleEvent', as Qt's
  QAccessibleAnnouncementEvent is built on Qt's QAccessibleEvent, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleAnnouncementEvent that has a ritual and
  that Python can call so far, 3 names in all: 'message', 'politeness',
  'setPoliteness'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAccessibleAnnouncementEvent::~QAccessibleAnnouncementEvent()': the
    destructor: Python never removes a C++ QAccessibleAnnouncementEvent.

  What to expect
  --------------

  - The C++ QAccessibleAnnouncementEvent is created at the first use, not by
    'QAccessibleAnnouncementEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleAnnouncementEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleAnnouncementEvent'

  #  A C++ QAccessibleAnnouncementEvent Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleAnnouncementEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def message(self) -> str:
    """
    Calls Qt's 'QString QAccessibleAnnouncementEvent::message() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleannouncementevent.html#message

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleAnnouncementEvent::message() const
    return self.uglySide.call(
        'ritual_ZNK28QAccessibleAnnouncementEvent7messageEv',
    )

  def politeness(self) -> QAccessible.AnnouncementPoliteness:
    """
    Calls Qt's 'QAccessible::AnnouncementPoliteness
    QAccessibleAnnouncementEvent::politeness() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleannouncementevent.html#politeness

    Returns
    -------

    QAccessible.AnnouncementPoliteness
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAccessible.AnnouncementPoliteness(number)' gives.
    """
    #  QAccessible::AnnouncementPoliteness
    #      QAccessibleAnnouncementEvent::politeness() const
    return QAccessible.AnnouncementPoliteness(self.uglySide.call(
        'ritual_ZNK28QAccessibleAnnouncementEvent10politenessEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAccessible.AnnouncementPoliteness)
  def setPoliteness(
      self,
      politeness: QAccessible.AnnouncementPoliteness,
  ) -> None:
    """
    Calls Qt's 'void
    QAccessibleAnnouncementEvent::setPoliteness(QAccessible::
    AnnouncementPoliteness politeness)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleannouncementevent.html#setPoliteness

    Parameters
    ----------

    politeness : QAccessible.AnnouncementPoliteness
      Passed on as its number.
    """
    #  void QAccessibleAnnouncementEvent::setPoliteness(QAccessible::
    #      AnnouncementPoliteness politeness)
    self.uglySide.call(
        'ritual_ZN28QAccessibleAnnouncementEvent13setPolitenessEN11QAccessi'
        'ble22AnnouncementPolitenessE',
        politeness.value,
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

  @overload(QObject, str)
  @overload(NoneType, str)
  def __init__(self, object: Optional[QObject], message: str) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleAnnouncementEvent::QAccessibleAnnouncementEvent(QObject
    *object, const QString &message)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleannouncementevent.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QAccessibleAnnouncementEvent::QAccessibleAnnouncementEvent(QObject
    #      *object, const QString &message)
    self._noteCreation(QAccessibleAnnouncementEvent, lambda: Rituals.call(
        'ritual_ZN28QAccessibleAnnouncementEventC1EP7QObjectRK7QString',
        self._addressOf(object, 'QObject'), message,
    ))

  @overload(QAccessibleInterface, str)
  def __init__(
      self,
      iface: Optional[QAccessibleInterface],
      message: str,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleAnnouncementEvent::QAccessibleAnnouncementEvent(
    QAccessibleInterface *iface, const QString &message)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleannouncementevent.html

    Parameters
    ----------

    iface : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QAccessibleAnnouncementEvent::QAccessibleAnnouncementEvent(
    #      QAccessibleInterface *iface, const QString &message)
    self._noteCreation(QAccessibleAnnouncementEvent, lambda: Rituals.call(
        'ritual_ZN28QAccessibleAnnouncementEventC1EP20QAccessibleInterfaceR'
        'K7QString',
        self._addressOf(iface), message,
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
