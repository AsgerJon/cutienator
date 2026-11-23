"""
QChildEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qcoreevent.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QChildEvent(QEvent):
  """
  The cute side of Qt's QChildEvent: a plain Python object standing in front
  of one C++ QChildEvent.

  It is built on the cute 'QEvent', as Qt's QChildEvent is built on Qt's
  QEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QChildEvent that has a ritual and that Python can
  call so far, 5 names in all: 'clone', 'child', 'added', 'polished',
  'removed'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QChildEvent::~QChildEvent()': the destructor: Python never removes
    a C++ QChildEvent.

  What has no ritual
  ------------------

  4 of the 11 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 2 forbidden.

  What to expect
  --------------

  - The C++ QChildEvent is created at the first use, not by
    'QChildEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QChildEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QChildEvent'

  #  A C++ QChildEvent Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QChildEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QChildEvent]:
    """
    Calls Qt's 'QChildEvent *QChildEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchildevent.html#clone

    Returns
    -------

    Optional[QChildEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QChildEvent *QChildEvent::clone() const
    ritual = 'ritual_ZNK11QChildEvent5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QChildEvent5cloneEv'
    address = self.uglySide.call(ritual)
    return QChildEvent._cuteAt(address)

  def child(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QChildEvent::child() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchildevent.html#child

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QChildEvent::child() const
    address = self.uglySide.call('ritual_ZNK11QChildEvent5childEv')
    from . import QObject
    return QObject._cuteAt(address)

  def added(self) -> bool:
    """
    Calls Qt's 'bool QChildEvent::added() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchildevent.html#added
    """
    #  bool QChildEvent::added() const
    return self.uglySide.call('ritual_ZNK11QChildEvent5addedEv')

  def polished(self) -> bool:
    """
    Calls Qt's 'bool QChildEvent::polished() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchildevent.html#polished
    """
    #  bool QChildEvent::polished() const
    return self.uglySide.call('ritual_ZNK11QChildEvent8polishedEv')

  def removed(self) -> bool:
    """
    Calls Qt's 'bool QChildEvent::removed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchildevent.html#removed
    """
    #  bool QChildEvent::removed() const
    return self.uglySide.call('ritual_ZNK11QChildEvent7removedEv')

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

  @overload(QEvent.Type, QObject)
  @overload(QEvent.Type, NoneType)
  def __init__(self, type: QEvent.Type, child: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's 'QChildEvent::QChildEvent(Type type,
    QObject *child)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qchildevent.html#QChildEvent

    Parameters
    ----------

    type : QEvent.Type
      Passed on as its number.

    child : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QChildEvent::QChildEvent(Type type, QObject *child)
    self._noteCreation(QChildEvent, lambda: Rituals.call(
        'ritual_ZN11QChildEventC1EN6QEvent4TypeEP7QObject',
        type.value, self._addressOf(child),
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
