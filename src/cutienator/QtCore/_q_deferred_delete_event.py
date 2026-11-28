"""
QDeferredDeleteEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qcoreevent_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QDeferredDeleteEvent to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class QDeferredDeleteEvent(QEvent):
  """
  The cute side of Qt's QDeferredDeleteEvent: a plain Python object standing
  in front of one C++ QDeferredDeleteEvent.

  It is built on the cute 'QEvent', as Qt's QDeferredDeleteEvent is built on
  Qt's QEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeferredDeleteEvent that has a ritual and that
  Python can call so far, 3 names in all: 'clone', 'loopLevel', 'scopeLevel'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDeferredDeleteEvent &QDeferredDeleteEvent::operator=(const
    QDeferredDeleteEvent &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QDeferredDeleteEvent::~QDeferredDeleteEvent()': the destructor:
    Python never removes a C++ QDeferredDeleteEvent.

  What has no ritual
  ------------------

  4 of the 9 functions Qt declares: 2 forbidden; 2 leans on
  'QDeferredDeleteEvent.

  What to expect
  --------------

  - The C++ QDeferredDeleteEvent is created at the first use, not by
    'QDeferredDeleteEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeferredDeleteEvent.
  - Each name of Qt's QDeferredDeleteEvent that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeferredDeleteEvent'

  #  A C++ QDeferredDeleteEvent Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeferredDeleteEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QDeferredDeleteEvent]:
    """
    Calls Qt's 'QDeferredDeleteEvent *QDeferredDeleteEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeferreddeleteevent.html#clone

    Returns
    -------

    Optional[QDeferredDeleteEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDeferredDeleteEvent *QDeferredDeleteEvent::clone() const
    address = self.uglySide.call('ritual_ZNK20QDeferredDeleteEvent5cloneEv')
    return QDeferredDeleteEvent._cuteAt(address)

  def loopLevel(self) -> int:
    """
    Calls Qt's 'int QDeferredDeleteEvent::loopLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeferreddeleteevent.html#loopLevel
    """
    #  int QDeferredDeleteEvent::loopLevel() const
    return self.uglySide.call('ritual_ZNK20QDeferredDeleteEvent9loopLevelEv')

  def scopeLevel(self) -> int:
    """
    Calls Qt's 'int QDeferredDeleteEvent::scopeLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeferreddeleteevent.html#scopeLevel
    """
    #  int QDeferredDeleteEvent::scopeLevel() const
    return self.uglySide.call(
        'ritual_ZNK20QDeferredDeleteEvent10scopeLevelEv',
    )

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QDeferredDeleteEvent::QDeferredDeleteEvent(const
      QDeferredDeleteEvent &a0)': leans on 'QDeferredDeleteEvent::clone()
      const', which Qt's source does not mark for use from outside Qt and has
      no code for that could be taken.
    - Qt's 'QDeferredDeleteEvent::QDeferredDeleteEvent(int loopLevel, int
      scopeLevel)': leans on 'QDeferredDeleteEvent::clone() const', which
      Qt's source does not mark for use from outside Qt and has no code for
      that could be taken.
    """
    raise NotImplementedError(
        "'QDeferredDeleteEvent.__init__' has no cute function yet. Qt's "
        "'QDeferredDeleteEvent::QDeferredDeleteEvent(const "
        "QDeferredDeleteEvent &a0)': leans on "
        "'QDeferredDeleteEvent::clone() const', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken. Qt's 'QDeferredDeleteEvent::QDeferredDeleteEvent(int "
        "loopLevel, int scopeLevel)': leans on "
        "'QDeferredDeleteEvent::clone() const', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

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
