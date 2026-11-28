"""
QMenuSloppyState binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qmenu_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QMenuSloppyState to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF, QRect
  from ..QtGui import QAction
  from . import QMenu
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAction = WAIT['QAction']
  QMenu = WAIT['QMenu']
  QPointF = WAIT['QPointF']
  QRect = WAIT['QRect']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMenuSloppyState(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMenuSloppyState: a plain Python object standing in
  front of one C++ QMenuSloppyState.

  What exists
  -----------

  Every function of Qt's QMenuSloppyState that has a ritual and that Python
  can call so far, 18 names in all: 'initialize', 'reset', 'enabled',
  'startTimer', 'startTimerIfNotRunning', 'stopTimer', 'enter', 'childEnter',
  'leave', 'childLeave', 'slope', 'checkSlope', 'processMouseEvent',
  'setSubMenuPopup', 'hasParentActiveDelayTimer', 'timeForTimeout',
  'isTimerId', 'subMenu'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMenuSloppyState::~QMenuSloppyState()': the destructor: Python
    never removes a C++ QMenuSloppyState.

  What has no ritual
  ------------------

  5 of the 25 functions Qt declares: 4 forbidden; 1 leans on
  'QMenuBarPrivate.

  What to expect
  --------------

  - The C++ QMenuSloppyState is created at the first use, not by
    'QMenuSloppyState(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMenuSloppyState.
  - Each name of Qt's QMenuSloppyState that has no cute function yet,
    'timeout', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QMenuSloppyState, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class MouseEventResult(CuteNum):
    """
    The enum 'QMenuSloppyState::MouseEventResult' of Qt, with the 3 names Qt
    gives in it.
    """

    EventIsProcessed = Kee[int](0)
    EventShouldBePropagated = Kee[int](1)
    EventDiscardsSloppyState = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QPointF, QPointF)
  def slope(p1: QPointF, p2: QPointF) -> float:
    """
    Calls Qt's 'qreal QMenuSloppyState::slope(const QPointF &p1, const
    QPointF &p2)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenusloppystate.html#slope

    Parameters
    ----------

    p1 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    p2 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  qreal QMenuSloppyState::slope(const QPointF &p1, const QPointF &p2)
    return Rituals.call(
        'ritual_ZN16QMenuSloppyState5slopeERK7QPointFS2_',
        CuteMixin._valueOf(p1, 'QPointF'), CuteMixin._valueOf(p2, 'QPointF'),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMenuSloppyState'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def enabled(self) -> bool:
    """
    Calls Qt's 'bool QMenuSloppyState::enabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenusloppystate.html#enabled
    """
    #  bool QMenuSloppyState::enabled() const
    return self.uglySide.call('ritual_ZNK16QMenuSloppyState7enabledEv')

  def hasParentActiveDelayTimer(self) -> bool:
    """
    Calls Qt's 'bool QMenuSloppyState::hasParentActiveDelayTimer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenusloppystate.html#hasParentActiveDelayTimer
    """
    #  bool QMenuSloppyState::hasParentActiveDelayTimer() const
    return self.uglySide.call(
        'ritual_ZNK16QMenuSloppyState25hasParentActiveDelayTimerEv',
    )

  def timeForTimeout(self) -> int:
    """
    Calls Qt's 'int QMenuSloppyState::timeForTimeout() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenusloppystate.html#timeForTimeout
    """
    #  int QMenuSloppyState::timeForTimeout() const
    return self.uglySide.call(
        'ritual_ZNK16QMenuSloppyState14timeForTimeoutEv',
    )

  @overload(int)
  def isTimerId(self, timerId: int) -> bool:
    """
    Calls Qt's 'bool QMenuSloppyState::isTimerId(int timerId) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenusloppystate.html#isTimerId

    Parameters
    ----------

    timerId : int
      Passed on as it is.
    """
    #  bool QMenuSloppyState::isTimerId(int timerId) const
    return self.uglySide.call(
        'ritual_ZNK16QMenuSloppyState9isTimerIdEi', timerId,
    )

  def subMenu(self) -> Optional[QMenu]:
    """
    Calls Qt's 'QMenu *QMenuSloppyState::subMenu() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenusloppystate.html#subMenu

    Returns
    -------

    Optional[QMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenu *QMenuSloppyState::subMenu() const
    address = self.uglySide.call('ritual_ZNK16QMenuSloppyState7subMenuEv')
    from . import QMenu
    return QMenu._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRect, QAction, QMenu)
  @overload(QRect, QAction, NoneType)
  @overload(QRect, NoneType, QMenu)
  @overload(QRect, NoneType, NoneType)
  def setSubMenuPopup(
      self,
      actionRect: QRect,
      resetAction: Optional[QAction],
      subMenu: Optional[QMenu],
  ) -> None:
    """
    Calls Qt's 'void QMenuSloppyState::setSubMenuPopup(const QRect
    &actionRect, QAction *resetAction, QMenu *subMenu)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenusloppystate.html#setSubMenuPopup

    Parameters
    ----------

    actionRect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    resetAction : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    subMenu : Optional[QMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenuSloppyState::setSubMenuPopup(const QRect &actionRect,
    #      QAction *resetAction, QMenu *subMenu)
    self.uglySide.call(
        'ritual_ZN16QMenuSloppyState15setSubMenuPopupERK5QRectP7QActionP5QM'
        'enu',
        self._valueOf(actionRect), self._addressOf(resetAction),
        self._addressOf(subMenu),
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
    Notes what was given, for Qt's 'QMenuSloppyState::QMenuSloppyState()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenusloppystate.html#QMenuSloppyState
    """
    #  QMenuSloppyState::QMenuSloppyState()
    self._noteCreation(QMenuSloppyState, lambda: Rituals.call(
        'ritual_ZN16QMenuSloppyStateC1Ev',
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

  @overload(QMenu)
  @overload(NoneType)
  def initialize(self, menu: Optional[QMenu]) -> None:
    """
    Calls Qt's 'void QMenuSloppyState::initialize(QMenu *menu)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenusloppystate.html#initialize

    Parameters
    ----------

    menu : Optional[QMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenuSloppyState::initialize(QMenu *menu)
    self.uglySide.call(
        'ritual_ZN16QMenuSloppyState10initializeEP5QMenu',
        self._addressOf(menu),
    )

  def reset(self) -> None:
    """
    Calls Qt's 'void QMenuSloppyState::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qmenusloppystate.html#reset
    """
    #  void QMenuSloppyState::reset()
    self.uglySide.call('ritual_ZN16QMenuSloppyState5resetEv')

  def startTimer(self) -> None:
    """
    Calls Qt's 'void QMenuSloppyState::startTimer()'.

    Qt's own words: https://doc.qt.io/qt-6/qmenusloppystate.html#startTimer
    """
    #  void QMenuSloppyState::startTimer()
    self.uglySide.call('ritual_ZN16QMenuSloppyState10startTimerEv')

  def startTimerIfNotRunning(self) -> None:
    """
    Calls Qt's 'void QMenuSloppyState::startTimerIfNotRunning()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenusloppystate.html#startTimerIfNotRunning
    """
    #  void QMenuSloppyState::startTimerIfNotRunning()
    self.uglySide.call(
        'ritual_ZN16QMenuSloppyState22startTimerIfNotRunningEv',
    )

  def stopTimer(self) -> None:
    """
    Calls Qt's 'void QMenuSloppyState::stopTimer()'.

    Qt's own words: https://doc.qt.io/qt-6/qmenusloppystate.html#stopTimer
    """
    #  void QMenuSloppyState::stopTimer()
    self.uglySide.call('ritual_ZN16QMenuSloppyState9stopTimerEv')

  def enter(self) -> None:
    """
    Calls Qt's 'void QMenuSloppyState::enter()'.

    Qt's own words: https://doc.qt.io/qt-6/qmenusloppystate.html#enter
    """
    #  void QMenuSloppyState::enter()
    self.uglySide.call('ritual_ZN16QMenuSloppyState5enterEv')

  def childEnter(self) -> None:
    """
    Calls Qt's 'void QMenuSloppyState::childEnter()'.

    Qt's own words: https://doc.qt.io/qt-6/qmenusloppystate.html#childEnter
    """
    #  void QMenuSloppyState::childEnter()
    self.uglySide.call('ritual_ZN16QMenuSloppyState10childEnterEv')

  def leave(self) -> None:
    """
    Calls Qt's 'void QMenuSloppyState::leave()'.

    Qt's own words: https://doc.qt.io/qt-6/qmenusloppystate.html#leave
    """
    #  void QMenuSloppyState::leave()
    self.uglySide.call('ritual_ZN16QMenuSloppyState5leaveEv')

  def childLeave(self) -> None:
    """
    Calls Qt's 'void QMenuSloppyState::childLeave()'.

    Qt's own words: https://doc.qt.io/qt-6/qmenusloppystate.html#childLeave
    """
    #  void QMenuSloppyState::childLeave()
    self.uglySide.call('ritual_ZN16QMenuSloppyState10childLeaveEv')

  @overload(float, float, bool)
  def checkSlope(self, oldS: float, newS: float, wantSteeper: bool) -> bool:
    """
    Calls Qt's 'bool QMenuSloppyState::checkSlope(qreal oldS, qreal newS,
    bool wantSteeper)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenusloppystate.html#checkSlope

    Parameters
    ----------

    oldS : float
      Passed on as it is.

    newS : float
      Passed on as it is.

    wantSteeper : bool
      Passed on as it is.
    """
    #  bool QMenuSloppyState::checkSlope(qreal oldS, qreal newS, bool
    #      wantSteeper)
    return self.uglySide.call(
        'ritual_ZN16QMenuSloppyState10checkSlopeEddb',
        oldS, newS, wantSteeper,
    )

  @overload(QPointF, QAction, QAction)
  @overload(QPointF, QAction, NoneType)
  @overload(QPointF, NoneType, QAction)
  @overload(QPointF, NoneType, NoneType)
  def processMouseEvent(
      self,
      mousePos: QPointF,
      resetAction: Optional[QAction],
      currentAction: Optional[QAction],
  ) -> MouseEventResult:
    """
    Calls Qt's 'MouseEventResult QMenuSloppyState::processMouseEvent(const
    QPointF &mousePos, QAction *resetAction, QAction *currentAction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenusloppystate.html#processMouseEvent

    Parameters
    ----------

    mousePos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    resetAction : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    currentAction : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    MouseEventResult
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'MouseEventResult(number)'
      gives.
    """
    #  MouseEventResult QMenuSloppyState::processMouseEvent(const QPointF
    #      &mousePos, QAction *resetAction, QAction *currentAction)
    return QMenuSloppyState.MouseEventResult(self.uglySide.call(
        'ritual_ZN16QMenuSloppyState17processMouseEventERK7QPointFP7QAction'
        'S4_',
        self._valueOf(mousePos, 'QPointF'), self._addressOf(resetAction),
        self._addressOf(currentAction),
    ))

  @staticmethod
  def timeout(*__, **_) -> Never:
    """
    Qt's 'void QMenuSloppyState::timeout()': leans on
    'QMenuBarPrivate::updateGeometries()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMenuSloppyState.timeout' has no cute function yet. Qt's 'void "
        "QMenuSloppyState::timeout()': leans on "
        "'QMenuBarPrivate::updateGeometries()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
