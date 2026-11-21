"""
QScrollEvent binding of the Qt C++
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
from ..QtCore import QEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']


class QScrollEvent(QEvent):
  """
  The cute side of Qt's QScrollEvent: a plain Python object standing in front
  of one C++ QScrollEvent.

  It is built on the cute 'QEvent', as Qt's QScrollEvent is built on Qt's
  QEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QScrollEvent that has a ritual and that Python can
  call so far, 4 names in all: 'clone', 'contentPos', 'overshootDistance',
  'scrollState'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QScrollEvent::~QScrollEvent()': the destructor: Python never
    removes a C++ QScrollEvent.

  What has no ritual
  ------------------

  4 of the 10 functions Qt declares: 2 protected; 2 forbidden.

  What to expect
  --------------

  - The C++ QScrollEvent is created at the first use, not by
    'QScrollEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScrollEvent.
  """

  #  The enums Qt writes inside QScrollEvent, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ScrollState(CuteNum):
    """
    The enum 'QScrollEvent::ScrollState' of Qt, with the 3 names Qt gives in
    it.
    """

    ScrollStarted = Kee[int](0)
    ScrollUpdated = Kee[int](1)
    ScrollFinished = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScrollEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QScrollEvent]:
    """
    Calls Qt's 'QScrollEvent *QScrollEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollevent.html#clone

    Returns
    -------

    Optional[QScrollEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScrollEvent *QScrollEvent::clone() const
    address = self.uglySide.call('ritual_ZNK12QScrollEvent5cloneEv')
    return QScrollEvent._cuteAt(address)

  def contentPos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QScrollEvent::contentPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollevent.html#contentPos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QScrollEvent::contentPos() const
    address = self.uglySide.call('ritual_ZNK12QScrollEvent10contentPosEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def overshootDistance(self) -> QPointF:
    """
    Calls Qt's 'QPointF QScrollEvent::overshootDistance() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollevent.html#overshootDistance

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QScrollEvent::overshootDistance() const
    address = self.uglySide.call(
        'ritual_ZNK12QScrollEvent17overshootDistanceEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def scrollState(self) -> ScrollState:
    """
    Calls Qt's 'ScrollState QScrollEvent::scrollState() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollevent.html#scrollState

    Returns
    -------

    ScrollState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ScrollState(number)'
      gives.
    """
    #  ScrollState QScrollEvent::scrollState() const
    return QScrollEvent.ScrollState(self.uglySide.call(
        'ritual_ZNK12QScrollEvent11scrollStateEv',
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

  @overload(QPointF, QPointF, ScrollState)
  def __init__(
      self,
      contentPos: QPointF,
      overshoot: QPointF,
      scrollState: ScrollState,
  ) -> None:
    """
    Notes what was given, for Qt's 'QScrollEvent::QScrollEvent(const QPointF
    &contentPos, const QPointF &overshoot, ScrollState scrollState)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qscrollevent.html#QScrollEvent

    Parameters
    ----------

    contentPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    overshoot : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    scrollState : ScrollState
      Passed on as its number.
    """
    #  QScrollEvent::QScrollEvent(const QPointF &contentPos, const QPointF
    #      &overshoot, ScrollState scrollState)
    self._noteCreation(QScrollEvent, lambda: Rituals.call(
        'ritual_ZN12QScrollEventC1ERK7QPointFS2_NS_11ScrollStateE',
        self._valueOf(contentPos), self._valueOf(overshoot),
        scrollState.value,
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
