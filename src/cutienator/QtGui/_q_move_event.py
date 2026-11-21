"""
QMoveEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qevent.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPoint
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']


class QMoveEvent(QEvent):
  """
  The cute side of Qt's QMoveEvent: a plain Python object standing in front
  of one C++ QMoveEvent.

  It is built on the cute 'QEvent', as Qt's QMoveEvent is built on Qt's
  QEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMoveEvent that has a ritual and that Python can
  call so far, 3 names in all: 'clone', 'pos', 'oldPos'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMoveEvent::~QMoveEvent()': the destructor: Python never removes a
    C++ QMoveEvent.

  What has no ritual
  ------------------

  4 of the 9 functions Qt declares: 2 protected; 2 forbidden.

  What to expect
  --------------

  - The C++ QMoveEvent is created at the first use, not by 'QMoveEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMoveEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMoveEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QMoveEvent]:
    """
    Calls Qt's 'QMoveEvent *QMoveEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmoveevent.html#clone

    Returns
    -------

    Optional[QMoveEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMoveEvent *QMoveEvent::clone() const
    address = self.uglySide.call('ritual_ZNK10QMoveEvent5cloneEv')
    return QMoveEvent._cuteAt(address)

  def pos(self) -> QPoint:
    """
    Calls Qt's 'const QPoint &QMoveEvent::pos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmoveevent.html#pos

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  const QPoint &QMoveEvent::pos() const
    address = self.uglySide.call('ritual_ZNK10QMoveEvent3posEv')
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def oldPos(self) -> QPoint:
    """
    Calls Qt's 'const QPoint &QMoveEvent::oldPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmoveevent.html#oldPos

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  const QPoint &QMoveEvent::oldPos() const
    address = self.uglySide.call('ritual_ZNK10QMoveEvent6oldPosEv')
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

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

  @overload(QPoint, QPoint)
  def __init__(self, pos: QPoint, oldPos: QPoint) -> None:
    """
    Notes what was given, for Qt's 'QMoveEvent::QMoveEvent(const QPoint &pos,
    const QPoint &oldPos)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmoveevent.html#QMoveEvent

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    oldPos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  QMoveEvent::QMoveEvent(const QPoint &pos, const QPoint &oldPos)
    self._noteCreation(QMoveEvent, lambda: Rituals.call(
        'ritual_ZN10QMoveEventC1ERK6QPointS2_',
        self._valueOf(pos), self._valueOf(oldPos),
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
