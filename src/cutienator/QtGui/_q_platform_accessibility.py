"""
QPlatformAccessibility binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformaccessibility.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
  from . import QAccessibleEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAccessibleEvent = WAIT['QAccessibleEvent']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformAccessibility(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlatformAccessibility: a plain Python object
  standing in front of one C++ QPlatformAccessibility.

  C++ hands a QPlatformAccessibility around as a copy, so every C++
  QPlatformAccessibility behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPlatformAccessibility that has a ritual and that
  Python can call so far, 7 names in all: 'notifyAccessibilityUpdate',
  'setRootObject', 'initialize', 'cleanup', 'isActive', 'setActive',
  'clearActiveNotificationState'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlatformAccessibility::~QPlatformAccessibility()': the destructor:
    Python removes its C++ QPlatformAccessibility by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QPlatformAccessibility is created at the first use, not by
    'QPlatformAccessibility(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlatformAccessibility back gives a copy the ritual
    made for Python, in a new cute QPlatformAccessibility.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformAccessibility'

  #  A C++ QPlatformAccessibility Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformAccessibility'

  #  The functions Qt calls itself that QPlatformAccessibility is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'notifyAccessibilityUpdate': (
          ('_ZN22QPlatformAccessibility25notifyAccessibilityUpdateEP16QAcce'
           'ssibleEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QAccessibleEvent'),
           )),
      ),
      'setRootObject': (
          ('_ZN22QPlatformAccessibility13setRootObjectEP7QObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'initialize': (
          ('_ZN22QPlatformAccessibility10initializeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'cleanup': (
          ('_ZN22QPlatformAccessibility7cleanupEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Qt's '~QPlatformAccessibility()'. Naming it makes this a value class:
  #  Python owns every C++ QPlatformAccessibility behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QPlatformAccessibilityD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QPlatformAccessibility::isActive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaccessibility.html#isActive
    """
    #  bool QPlatformAccessibility::isActive() const
    return self._callAs(
        'QPlatformAccessibility',
        'ritual_ZNK22QPlatformAccessibility8isActiveEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def setRootObject(self, o: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QPlatformAccessibility::setRootObject(QObject *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaccessibility.html#setRootObject

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformAccessibility::setRootObject(QObject *o)
    ritual = 'ritual_ZN22QPlatformAccessibility13setRootObjectEP7QObject'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QPlatformAccessibility13setRootObjectEP7QObject')
    self._callAs(
        'QPlatformAccessibility', ritual, self._addressOf(o, 'QObject'),
    )

  @overload(bool)
  def setActive(self, active: bool) -> None:
    """
    Calls Qt's 'void QPlatformAccessibility::setActive(bool active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaccessibility.html#setActive

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QPlatformAccessibility::setActive(bool active)
    self._callAs(
        'QPlatformAccessibility',
        'ritual_ZN22QPlatformAccessibility9setActiveEb',
        active,
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
    'QPlatformAccessibility::QPlatformAccessibility()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaccessibility.html#QPlatformAccessibility
    """
    #  QPlatformAccessibility::QPlatformAccessibility()
    self._noteCreation(QPlatformAccessibility, lambda: Rituals.call(
        'ritual_ZN22QPlatformAccessibilityC1Ev',
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

  @overload(QAccessibleEvent)
  @overload(NoneType)
  def notifyAccessibilityUpdate(
      self,
      event: Optional[QAccessibleEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QPlatformAccessibility::notifyAccessibilityUpdate(QAccessibleEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaccessibility.html

    Parameters
    ----------

    event : Optional[QAccessibleEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QPlatformAccessibility::notifyAccessibilityUpdate(QAccessibleEvent
    #      *event)
    ritual = (
        'ritual_ZN22QPlatformAccessibility25notifyAccessibilityUpdateEP16QA'
        'ccessibleEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QPlatformAccessibility25notifyAccessibilityUpdate'
          'EP16QAccessibleEvent')
    self._callAs('QPlatformAccessibility', ritual, self._addressOf(event))

  def initialize(self) -> None:
    """
    Calls Qt's 'void QPlatformAccessibility::initialize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaccessibility.html#initialize
    """
    #  void QPlatformAccessibility::initialize()
    ritual = 'ritual_ZN22QPlatformAccessibility10initializeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QPlatformAccessibility10initializeEv'
    self._callAs('QPlatformAccessibility', ritual)

  def cleanup(self) -> None:
    """
    Calls Qt's 'void QPlatformAccessibility::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaccessibility.html#cleanup
    """
    #  void QPlatformAccessibility::cleanup()
    ritual = 'ritual_ZN22QPlatformAccessibility7cleanupEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QPlatformAccessibility7cleanupEv'
    self._callAs('QPlatformAccessibility', ritual)

  def clearActiveNotificationState(self) -> None:
    """
    Calls Qt's 'void QPlatformAccessibility::clearActiveNotificationState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaccessibility.html
    """
    #  void QPlatformAccessibility::clearActiveNotificationState()
    self._callAs(
        'QPlatformAccessibility',
        'ritual_ZN22QPlatformAccessibility28clearActiveNotificationStateEv',
    )
