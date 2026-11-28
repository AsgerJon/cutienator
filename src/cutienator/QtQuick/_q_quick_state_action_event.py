"""
QQuickStateActionEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickstate_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickStateActionEvent to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickStateActionEvent(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickStateActionEvent: a plain Python object
  standing in front of one C++ QQuickStateActionEvent.

  What exists
  -----------

  Every function of Qt's QQuickStateActionEvent that has a ritual and that
  Python can call so far, 14 names in all: 'type', 'execute', 'isReversable',
  'reverse', 'saveOriginals', 'needsCopy', 'copyOriginals', 'isRewindable',
  'rewind', 'saveCurrentValues', 'saveTargetValues', 'changesBindings',
  'clearBindings', 'mayOverride'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickStateActionEvent::~QQuickStateActionEvent()': the destructor:
    Python never removes a C++ QQuickStateActionEvent.

  What to expect
  --------------

  - The C++ QQuickStateActionEvent is created at the first use, not by
    'QQuickStateActionEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickStateActionEvent.
  """

  #  The enums Qt writes inside QQuickStateActionEvent, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class EventType(CuteNum):
    """
    The enum 'QQuickStateActionEvent::EventType' of Qt, with the 4 names Qt
    gives in it.
    """

    Script = Kee[int](0)
    SignalHandler = Kee[int](1)
    ParentChange = Kee[int](2)
    AnchorChanges = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickStateActionEvent'

  #  A C++ QQuickStateActionEvent Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickStateActionEvent'

  #  The functions Qt calls itself that QQuickStateActionEvent is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'type': (
          ('_ZNK22QQuickStateActionEvent4typeEv',
           ('int', 'enum', 'QtQuick:QQuickStateActionEvent.EventType'),
           ()),
      ),
      'execute': (
          ('_ZN22QQuickStateActionEvent7executeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'isReversable': (
          ('_ZN22QQuickStateActionEvent12isReversableEv',
           ('bool', 'number', ''),
           ()),
      ),
      'reverse': (
          ('_ZN22QQuickStateActionEvent7reverseEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'saveOriginals': (
          ('_ZN22QQuickStateActionEvent13saveOriginalsEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'needsCopy': (
          ('_ZN22QQuickStateActionEvent9needsCopyEv',
           ('bool', 'number', ''),
           ()),
      ),
      'copyOriginals': (
          ('_ZN22QQuickStateActionEvent13copyOriginalsEPS_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickStateActionEvent'),
           )),
      ),
      'isRewindable': (
          ('_ZN22QQuickStateActionEvent12isRewindableEv',
           ('bool', 'number', ''),
           ()),
      ),
      'rewind': (
          ('_ZN22QQuickStateActionEvent6rewindEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'saveCurrentValues': (
          ('_ZN22QQuickStateActionEvent17saveCurrentValuesEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'saveTargetValues': (
          ('_ZN22QQuickStateActionEvent16saveTargetValuesEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'changesBindings': (
          ('_ZN22QQuickStateActionEvent15changesBindingsEv',
           ('bool', 'number', ''),
           ()),
      ),
      'clearBindings': (
          ('_ZN22QQuickStateActionEvent13clearBindingsEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'mayOverride': (
          ('_ZN22QQuickStateActionEvent11mayOverrideEPS_',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtQuick:QQuickStateActionEvent'),
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

  def type(self) -> EventType:
    """
    Calls Qt's 'EventType QQuickStateActionEvent::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstateactionevent.html#type

    Returns
    -------

    EventType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'EventType(number)' gives.
    """
    #  EventType QQuickStateActionEvent::type() const
    return QQuickStateActionEvent.EventType(self._callAs(
        'QQuickStateActionEvent',
        'ritual_ZNK22QQuickStateActionEvent4typeEv',
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

  def execute(self) -> None:
    """
    Calls Qt's 'void QQuickStateActionEvent::execute()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstateactionevent.html#execute
    """
    #  void QQuickStateActionEvent::execute()
    ritual = 'ritual_ZN22QQuickStateActionEvent7executeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickStateActionEvent7executeEv'
    self._callAs('QQuickStateActionEvent', ritual)

  def isReversable(self) -> bool:
    """
    Calls Qt's 'bool QQuickStateActionEvent::isReversable()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstateactionevent.html#isReversable
    """
    #  bool QQuickStateActionEvent::isReversable()
    ritual = 'ritual_ZN22QQuickStateActionEvent12isReversableEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickStateActionEvent12isReversableEv'
    return self._callAs('QQuickStateActionEvent', ritual)

  def reverse(self) -> None:
    """
    Calls Qt's 'void QQuickStateActionEvent::reverse()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstateactionevent.html#reverse
    """
    #  void QQuickStateActionEvent::reverse()
    ritual = 'ritual_ZN22QQuickStateActionEvent7reverseEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickStateActionEvent7reverseEv'
    self._callAs('QQuickStateActionEvent', ritual)

  def saveOriginals(self) -> None:
    """
    Calls Qt's 'void QQuickStateActionEvent::saveOriginals()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstateactionevent.html#saveOriginals
    """
    #  void QQuickStateActionEvent::saveOriginals()
    ritual = 'ritual_ZN22QQuickStateActionEvent13saveOriginalsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickStateActionEvent13saveOriginalsEv'
    self._callAs('QQuickStateActionEvent', ritual)

  def needsCopy(self) -> bool:
    """
    Calls Qt's 'bool QQuickStateActionEvent::needsCopy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstateactionevent.html#needsCopy
    """
    #  bool QQuickStateActionEvent::needsCopy()
    ritual = 'ritual_ZN22QQuickStateActionEvent9needsCopyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickStateActionEvent9needsCopyEv'
    return self._callAs('QQuickStateActionEvent', ritual)

  @overload(THIS)
  @overload(NoneType)
  def copyOriginals(self, a0: Optional[QQuickStateActionEvent]) -> None:
    """
    Calls Qt's 'void
    QQuickStateActionEvent::copyOriginals(QQuickStateActionEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstateactionevent.html#copyOriginals

    Parameters
    ----------

    a0 : Optional[QQuickStateActionEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickStateActionEvent::copyOriginals(QQuickStateActionEvent *a0)
    ritual = 'ritual_ZN22QQuickStateActionEvent13copyOriginalsEPS_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickStateActionEvent13copyOriginalsEPS_'
    self._callAs(
        'QQuickStateActionEvent', ritual,
        self._addressOf(a0, 'QQuickStateActionEvent'),
    )

  def isRewindable(self) -> bool:
    """
    Calls Qt's 'bool QQuickStateActionEvent::isRewindable()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstateactionevent.html#isRewindable
    """
    #  bool QQuickStateActionEvent::isRewindable()
    ritual = 'ritual_ZN22QQuickStateActionEvent12isRewindableEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickStateActionEvent12isRewindableEv'
    return self._callAs('QQuickStateActionEvent', ritual)

  def rewind(self) -> None:
    """
    Calls Qt's 'void QQuickStateActionEvent::rewind()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstateactionevent.html#rewind
    """
    #  void QQuickStateActionEvent::rewind()
    ritual = 'ritual_ZN22QQuickStateActionEvent6rewindEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickStateActionEvent6rewindEv'
    self._callAs('QQuickStateActionEvent', ritual)

  def saveCurrentValues(self) -> None:
    """
    Calls Qt's 'void QQuickStateActionEvent::saveCurrentValues()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstateactionevent.html#saveCurrentValues
    """
    #  void QQuickStateActionEvent::saveCurrentValues()
    ritual = 'ritual_ZN22QQuickStateActionEvent17saveCurrentValuesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickStateActionEvent17saveCurrentValuesEv'
    self._callAs('QQuickStateActionEvent', ritual)

  def saveTargetValues(self) -> None:
    """
    Calls Qt's 'void QQuickStateActionEvent::saveTargetValues()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstateactionevent.html#saveTargetValues
    """
    #  void QQuickStateActionEvent::saveTargetValues()
    ritual = 'ritual_ZN22QQuickStateActionEvent16saveTargetValuesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickStateActionEvent16saveTargetValuesEv'
    self._callAs('QQuickStateActionEvent', ritual)

  def changesBindings(self) -> bool:
    """
    Calls Qt's 'bool QQuickStateActionEvent::changesBindings()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstateactionevent.html#changesBindings
    """
    #  bool QQuickStateActionEvent::changesBindings()
    ritual = 'ritual_ZN22QQuickStateActionEvent15changesBindingsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickStateActionEvent15changesBindingsEv'
    return self._callAs('QQuickStateActionEvent', ritual)

  def clearBindings(self) -> None:
    """
    Calls Qt's 'void QQuickStateActionEvent::clearBindings()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstateactionevent.html#clearBindings
    """
    #  void QQuickStateActionEvent::clearBindings()
    ritual = 'ritual_ZN22QQuickStateActionEvent13clearBindingsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickStateActionEvent13clearBindingsEv'
    self._callAs('QQuickStateActionEvent', ritual)

  @overload(THIS)
  @overload(NoneType)
  def mayOverride(self, other: Optional[QQuickStateActionEvent]) -> bool:
    """
    Calls Qt's 'bool
    QQuickStateActionEvent::mayOverride(QQuickStateActionEvent *other)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstateactionevent.html#mayOverride

    Parameters
    ----------

    other : Optional[QQuickStateActionEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickStateActionEvent::mayOverride(QQuickStateActionEvent
    #      *other)
    ritual = 'ritual_ZN22QQuickStateActionEvent11mayOverrideEPS_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickStateActionEvent11mayOverrideEPS_'
    return self._callAs(
        'QQuickStateActionEvent', ritual,
        self._addressOf(other, 'QQuickStateActionEvent'),
    )
