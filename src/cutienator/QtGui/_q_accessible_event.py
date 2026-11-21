"""
QAccessibleEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QAccessible

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


class QAccessibleEvent(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAccessibleEvent: a plain Python object standing in
  front of one C++ QAccessibleEvent.

  What exists
  -----------

  Every function of Qt's QAccessibleEvent that has a ritual and that Python
  can call so far, 6 names in all: 'type', 'object', 'uniqueId', 'setChild',
  'child', 'accessibleInterface'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAccessibleEvent::~QAccessibleEvent()': the destructor: Python
    never removes a C++ QAccessibleEvent.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QAccessibleEvent is created at the first use, not by
    'QAccessibleEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QAccessible.Event:
    """
    Calls Qt's 'QAccessible::Event QAccessibleEvent::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibleevent.html#type

    Returns
    -------

    QAccessible.Event
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAccessible.Event(number)' gives.
    """
    #  QAccessible::Event QAccessibleEvent::type() const
    return QAccessible.Event(self.uglySide.call(
        'ritual_ZNK16QAccessibleEvent4typeEv',
    ))

  def object(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QAccessibleEvent::object() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibleevent.html#object

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QAccessibleEvent::object() const
    address = self.uglySide.call('ritual_ZNK16QAccessibleEvent6objectEv')
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def uniqueId(self) -> int:
    """
    Calls Qt's 'QAccessible::Id QAccessibleEvent::uniqueId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibleevent.html#uniqueId
    """
    #  QAccessible::Id QAccessibleEvent::uniqueId() const
    return self.uglySide.call('ritual_ZNK16QAccessibleEvent8uniqueIdEv')

  def child(self) -> int:
    """
    Calls Qt's 'int QAccessibleEvent::child() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibleevent.html#child
    """
    #  int QAccessibleEvent::child() const
    return self.uglySide.call('ritual_ZNK16QAccessibleEvent5childEv')

  def accessibleInterface(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleEvent::accessibleInterface()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleevent.html#accessibleInterface

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleEvent::accessibleInterface() const
    address = self.uglySide.call(
        'ritual_ZNK16QAccessibleEvent19accessibleInterfaceEv',
    )
    from . import QAccessibleInterface
    return QAccessibleInterface._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setChild(self, chld: int) -> None:
    """
    Calls Qt's 'void QAccessibleEvent::setChild(int chld)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibleevent.html#setChild

    Parameters
    ----------

    chld : int
      Passed on as it is.
    """
    #  void QAccessibleEvent::setChild(int chld)
    self.uglySide.call('ritual_ZN16QAccessibleEvent8setChildEi', chld)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject, QAccessible.Event)
  @overload(NoneType, QAccessible.Event)
  def __init__(self, obj: Optional[QObject], typ: QAccessible.Event) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleEvent::QAccessibleEvent(QObject *obj, QAccessible::Event
    typ)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleevent.html#QAccessibleEvent

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    typ : QAccessible.Event
      Passed on as its number.
    """
    #  QAccessibleEvent::QAccessibleEvent(QObject *obj, QAccessible::Event
    #      typ)
    self._noteCreation(QAccessibleEvent, lambda: Rituals.call(
        'ritual_ZN16QAccessibleEventC1EP7QObjectN11QAccessible5EventE',
        self._addressOf(obj), typ.value,
    ))

  @overload(QAccessibleInterface, QAccessible.Event)
  def __init__(
      self,
      iface: Optional[QAccessibleInterface],
      typ: QAccessible.Event,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleEvent::QAccessibleEvent(QAccessibleInterface *iface,
    QAccessible::Event typ)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleevent.html#QAccessibleEvent

    Parameters
    ----------

    iface : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    typ : QAccessible.Event
      Passed on as its number.
    """
    #  QAccessibleEvent::QAccessibleEvent(QAccessibleInterface *iface,
    #      QAccessible::Event typ)
    self._noteCreation(QAccessibleEvent, lambda: Rituals.call(
        'ritual_ZN16QAccessibleEventC1EP20QAccessibleInterfaceN11QAccessibl'
        'e5EventE',
        self._addressOf(iface), typ.value,
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
