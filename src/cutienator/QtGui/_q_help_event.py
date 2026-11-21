"""
QHelpEvent binding of the Qt C++
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


class QHelpEvent(QEvent):
  """
  The cute side of Qt's QHelpEvent: a plain Python object standing in front
  of one C++ QHelpEvent.

  It is built on the cute 'QEvent', as Qt's QHelpEvent is built on Qt's
  QEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHelpEvent that has a ritual and that Python can
  call so far, 7 names in all: 'clone', 'x', 'y', 'globalX', 'globalY',
  'pos', 'globalPos'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHelpEvent::~QHelpEvent()': the destructor: Python never removes a
    C++ QHelpEvent.

  What has no ritual
  ------------------

  4 of the 13 functions Qt declares: 2 protected; 2 forbidden.

  What to expect
  --------------

  - The C++ QHelpEvent is created at the first use, not by 'QHelpEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHelpEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHelpEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QHelpEvent]:
    """
    Calls Qt's 'QHelpEvent *QHelpEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpevent.html#clone

    Returns
    -------

    Optional[QHelpEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHelpEvent *QHelpEvent::clone() const
    address = self.uglySide.call('ritual_ZNK10QHelpEvent5cloneEv')
    return QHelpEvent._cuteAt(address)

  def x(self) -> int:
    """
    Calls Qt's 'int QHelpEvent::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpevent.html#x
    """
    #  int QHelpEvent::x() const
    return self.uglySide.call('ritual_ZNK10QHelpEvent1xEv')

  def y(self) -> int:
    """
    Calls Qt's 'int QHelpEvent::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpevent.html#y
    """
    #  int QHelpEvent::y() const
    return self.uglySide.call('ritual_ZNK10QHelpEvent1yEv')

  def globalX(self) -> int:
    """
    Calls Qt's 'int QHelpEvent::globalX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpevent.html#globalX
    """
    #  int QHelpEvent::globalX() const
    return self.uglySide.call('ritual_ZNK10QHelpEvent7globalXEv')

  def globalY(self) -> int:
    """
    Calls Qt's 'int QHelpEvent::globalY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpevent.html#globalY
    """
    #  int QHelpEvent::globalY() const
    return self.uglySide.call('ritual_ZNK10QHelpEvent7globalYEv')

  def pos(self) -> QPoint:
    """
    Calls Qt's 'const QPoint &QHelpEvent::pos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpevent.html#pos

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  const QPoint &QHelpEvent::pos() const
    address = self.uglySide.call('ritual_ZNK10QHelpEvent3posEv')
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def globalPos(self) -> QPoint:
    """
    Calls Qt's 'const QPoint &QHelpEvent::globalPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpevent.html#globalPos

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  const QPoint &QHelpEvent::globalPos() const
    address = self.uglySide.call('ritual_ZNK10QHelpEvent9globalPosEv')
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

  @overload(QEvent.Type, QPoint, QPoint)
  def __init__(
      self,
      type: QEvent.Type,
      pos: QPoint,
      globalPos: QPoint,
  ) -> None:
    """
    Notes what was given, for Qt's 'QHelpEvent::QHelpEvent(Type type, const
    QPoint &pos, const QPoint &globalPos)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qhelpevent.html#QHelpEvent

    Parameters
    ----------

    type : QEvent.Type
      Passed on as its number.

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    globalPos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  QHelpEvent::QHelpEvent(Type type, const QPoint &pos, const QPoint
    #      &globalPos)
    self._noteCreation(QHelpEvent, lambda: Rituals.call(
        'ritual_ZN10QHelpEventC1EN6QEvent4TypeERK6QPointS4_',
        type.value, self._valueOf(pos), self._valueOf(globalPos),
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
