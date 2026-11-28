"""
QContextMenuEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qevent.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QInputEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPoint
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']


class QContextMenuEvent(QInputEvent):
  """
  The cute side of Qt's QContextMenuEvent: a plain Python object standing in
  front of one C++ QContextMenuEvent.

  It is built on the cute 'QInputEvent', as Qt's QContextMenuEvent is built
  on Qt's QInputEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QContextMenuEvent that has a ritual and that Python
  can call so far, 8 names in all: 'clone', 'x', 'y', 'globalX', 'globalY',
  'pos', 'globalPos', 'reason'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QContextMenuEvent::QContextMenuEvent(const QContextMenuEvent &a0)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QContextMenuEvent &QContextMenuEvent::operator=(const
    QContextMenuEvent &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QContextMenuEvent::~QContextMenuEvent()': the destructor: Python
    never removes a C++ QContextMenuEvent.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QContextMenuEvent is created at the first use, not by
    'QContextMenuEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QContextMenuEvent.
  """

  #  The enums Qt writes inside QContextMenuEvent, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Reason(CuteNum):
    """
    The enum 'QContextMenuEvent::Reason' of Qt, with the 3 names Qt gives in
    it.
    """

    Mouse = Kee[int](0)
    Keyboard = Kee[int](1)
    Other = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QContextMenuEvent'

  #  A C++ QContextMenuEvent Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QContextMenuEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QContextMenuEvent]:
    """
    Calls Qt's 'QContextMenuEvent *QContextMenuEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcontextmenuevent.html#clone

    Returns
    -------

    Optional[QContextMenuEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QContextMenuEvent *QContextMenuEvent::clone() const
    ritual = 'ritual_ZNK17QContextMenuEvent5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QContextMenuEvent5cloneEv'
    address = self.uglySide.call(ritual)
    return QContextMenuEvent._cuteAt(address)

  def x(self) -> int:
    """
    Calls Qt's 'int QContextMenuEvent::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcontextmenuevent.html#x
    """
    #  int QContextMenuEvent::x() const
    return self.uglySide.call('ritual_ZNK17QContextMenuEvent1xEv')

  def y(self) -> int:
    """
    Calls Qt's 'int QContextMenuEvent::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcontextmenuevent.html#y
    """
    #  int QContextMenuEvent::y() const
    return self.uglySide.call('ritual_ZNK17QContextMenuEvent1yEv')

  def globalX(self) -> int:
    """
    Calls Qt's 'int QContextMenuEvent::globalX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcontextmenuevent.html#globalX
    """
    #  int QContextMenuEvent::globalX() const
    return self.uglySide.call('ritual_ZNK17QContextMenuEvent7globalXEv')

  def globalY(self) -> int:
    """
    Calls Qt's 'int QContextMenuEvent::globalY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcontextmenuevent.html#globalY
    """
    #  int QContextMenuEvent::globalY() const
    return self.uglySide.call('ritual_ZNK17QContextMenuEvent7globalYEv')

  def pos(self) -> QPoint:
    """
    Calls Qt's 'const QPoint &QContextMenuEvent::pos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcontextmenuevent.html#pos

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  const QPoint &QContextMenuEvent::pos() const
    address = self.uglySide.call('ritual_ZNK17QContextMenuEvent3posEv')
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def globalPos(self) -> QPoint:
    """
    Calls Qt's 'const QPoint &QContextMenuEvent::globalPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcontextmenuevent.html#globalPos

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  const QPoint &QContextMenuEvent::globalPos() const
    address = self.uglySide.call('ritual_ZNK17QContextMenuEvent9globalPosEv')
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def reason(self) -> Reason:
    """
    Calls Qt's 'Reason QContextMenuEvent::reason() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcontextmenuevent.html#reason

    Returns
    -------

    Reason
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Reason(number)' gives.
    """
    #  Reason QContextMenuEvent::reason() const
    return QContextMenuEvent.Reason(self.uglySide.call(
        'ritual_ZNK17QContextMenuEvent6reasonEv',
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

  @overload(Reason, QPoint, QPoint)
  @overload(Reason, QPoint, QPoint, Qt.KeyboardModifiers)
  def __init__(
      self,
      reason: Reason,
      pos: QPoint,
      globalPos: QPoint,
      modifiers: Qt.KeyboardModifiers = Qt.KeyboardModifiers.NoModifier,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QContextMenuEvent::QContextMenuEvent(Reason reason, const QPoint &pos,
    const QPoint &globalPos, Qt::KeyboardModifiers modifiers)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcontextmenuevent.html#QContextMenuEvent

    Parameters
    ----------

    reason : Reason
      Passed on as its number.

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    globalPos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.KeyboardModifiers.NoModifier.
    """
    #  QContextMenuEvent::QContextMenuEvent(Reason reason, const QPoint &pos,
    #      const QPoint &globalPos, Qt::KeyboardModifiers modifiers)
    self._noteCreation(QContextMenuEvent, lambda: Rituals.call(
        'ritual_ZN17QContextMenuEventC1ENS_6ReasonERK6QPointS3_6QFlagsIN2Qt'
        '16KeyboardModifierEE',
        reason.value, self._valueOf(pos), self._valueOf(globalPos),
        modifiers.value,
    ))

  @overload(Reason, QPoint)
  def __init__(self, reason: Reason, pos: QPoint) -> None:
    """
    Notes what was given, for Qt's
    'QContextMenuEvent::QContextMenuEvent(Reason reason, const QPoint &pos)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcontextmenuevent.html#QContextMenuEvent

    Parameters
    ----------

    reason : Reason
      Passed on as its number.

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  QContextMenuEvent::QContextMenuEvent(Reason reason, const QPoint &pos)
    self._noteCreation(QContextMenuEvent, lambda: Rituals.call(
        'ritual_ZN17QContextMenuEventC1ENS_6ReasonERK6QPoint',
        reason.value, self._valueOf(pos),
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
