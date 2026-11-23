"""
QDynamicPropertyChangeEvent binding of the Qt C++
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

  from . import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QDynamicPropertyChangeEvent(QEvent):
  """
  The cute side of Qt's QDynamicPropertyChangeEvent: a plain Python object
  standing in front of one C++ QDynamicPropertyChangeEvent.

  It is built on the cute 'QEvent', as Qt's QDynamicPropertyChangeEvent is
  built on Qt's QEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDynamicPropertyChangeEvent that has a ritual and
  that Python can call so far, 2 names in all: 'clone', 'propertyName'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDynamicPropertyChangeEvent::~QDynamicPropertyChangeEvent()': the
    destructor: Python never removes a C++ QDynamicPropertyChangeEvent.

  What has no ritual
  ------------------

  4 of the 8 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 2 forbidden.

  What to expect
  --------------

  - The C++ QDynamicPropertyChangeEvent is created at the first use, not by
    'QDynamicPropertyChangeEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDynamicPropertyChangeEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDynamicPropertyChangeEvent'

  #  A C++ QDynamicPropertyChangeEvent Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDynamicPropertyChangeEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QDynamicPropertyChangeEvent]:
    """
    Calls Qt's 'QDynamicPropertyChangeEvent
    *QDynamicPropertyChangeEvent::clone() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicpropertychangeevent.html#clone

    Returns
    -------

    Optional[QDynamicPropertyChangeEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDynamicPropertyChangeEvent *QDynamicPropertyChangeEvent::clone()
    #      const
    ritual = 'ritual_ZNK27QDynamicPropertyChangeEvent5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK27QDynamicPropertyChangeEvent5cloneEv'
    address = self.uglySide.call(ritual)
    return QDynamicPropertyChangeEvent._cuteAt(address)

  def propertyName(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QDynamicPropertyChangeEvent::propertyName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicpropertychangeevent.html#propertyName

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QDynamicPropertyChangeEvent::propertyName() const
    address = self.uglySide.call(
        'ritual_ZNK27QDynamicPropertyChangeEvent12propertyNameEv',
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

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

  @overload(QByteArray)
  def __init__(self, name: QByteArray) -> None:
    """
    Notes what was given, for Qt's
    'QDynamicPropertyChangeEvent::QDynamicPropertyChangeEvent(const
    QByteArray &name)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicpropertychangeevent.html

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QDynamicPropertyChangeEvent::QDynamicPropertyChangeEvent(const
    #      QByteArray &name)
    self._noteCreation(QDynamicPropertyChangeEvent, lambda: Rituals.call(
        'ritual_ZN27QDynamicPropertyChangeEventC1ERK10QByteArray',
        self._valueOf(name),
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
