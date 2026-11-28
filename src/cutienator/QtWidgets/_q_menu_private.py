"""
QMenuPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qmenu_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QMenuPrivate to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QWidget, QWidgetPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPoint, QPointF, QRect
  from ..QtGui import QAction, QPaintEvent, QPainter, QPlatformMenu
  from ..QtGui import QPlatformMenuItem, QScreen, QWindow
  from . import QMenu
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAction = WAIT['QAction']
  QMenu = WAIT['QMenu']
  QPainter = WAIT['QPainter']
  QPlatformMenu = WAIT['QPlatformMenu']
  QPlatformMenuItem = WAIT['QPlatformMenuItem']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QRect = WAIT['QRect']
  QScreen = WAIT['QScreen']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMenuPrivate(QWidgetPrivate):
  """
  The cute side of Qt's QMenuPrivate: a plain Python object standing in front
  of one C++ QMenuPrivate.

  It is built on the cute 'QWidgetPrivate', as Qt's QMenuPrivate is built on
  Qt's QWidgetPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMenuPrivate that has a ritual and that Python can
  call so far, 30 names in all: 'q_func', 'init', 'createPlatformMenu',
  'setPlatformMenu', 'syncPlatformMenu', 'copyActionToPlatformItem',
  'insertActionInPlatformMenu', 'get', 'scrollerHeight', 'isContextMenu',
  'actionRect', 'updateActionRects', 'popupGeometry',
  'useFullScreenForPopup', 'getLastVisibleAction', 'topCausedWidget',
  'actionAt', 'setSyncAction', 'hideMenu', 'transientParentWindow',
  'indexOf', 'setOverrideMenuAction', '_q_overrideMenuActionDestroyed',
  '_q_actionHovered', '_q_platformMenuAboutToShow', 'hasMouseMoved',
  'updateLayoutDirection', 'drawTearOff', 'rect', 'considerAction'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QMenu *QMenuPrivate::q_func() const': takes in Python what
    'QMenu *QMenuPrivate::q_func()' takes.
  - Qt's 'QMenuPrivate::~QMenuPrivate()': the destructor: Python never
    removes a C++ QMenuPrivate.
  - Qt's 'void QMenuPrivate::popup(const QPoint &p, QAction *atAction,
    PositionFunction positionFunction)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QAction *QMenuPrivate::exec(const QPoint &p, QAction *action,
    PositionFunction positionFunction)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QList<QPointer<QWidget>> QMenuPrivate::calcCausedStack() const':
    gives a type Python has no way to take yet.
  - Qt's 'void QMenuPrivate::activateCausedStack(const
    QList<QPointer<QWidget>> &a0, QAction *a1, QAction::ActionEvent a2, bool
    a3)': takes a type Python has no way to hand over yet.
  - Qt's 'void QMenuPrivate::drawScroller(QPainter *painter,
    ScrollerTearOffItem::Type type, const QRect &rect)': names the enum
    'QMenuPrivate::ScrollerTearOffItem::Type', whose class cannot be named
    here.

  What has no ritual
  ------------------

  11 of the 50 functions Qt declares: 9 leans on 'QMenuBarPrivate; 1 Qt's
  library has no name for it, and its code in Qt's source does not compile
  apart from its file; 1 leans on 'QTornOffMenu.

  What to expect
  --------------

  - The C++ QMenuPrivate is created at the first use, not by
    'QMenuPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMenuPrivate.
  - Each name of Qt's QMenuPrivate that has no cute function yet, '__init__',
    '_q_actionTriggered', 'activateAction', 'activateCausedStack',
    'calcCausedStack', 'drawScroller', 'exec', 'hideUpToMenuBar',
    'mouseEventTaken', 'popup', 'popupAction', 'scrollMenu',
    'setCurrentAction', 'setFirstActionActive', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QMenuPrivate, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class SelectionDirection(CuteNum, scoped=True):
    """
    The enum 'QMenuPrivate::SelectionDirection' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Up = Kee[int](0)
    Down = Kee[int](1)

  class SelectionReason(CuteNum):
    """
    The enum 'QMenuPrivate::SelectionReason' of Qt, with the 3 names Qt gives
    in it.
    """

    SelectedFromKeyboard = Kee[int](0)
    SelectedFromAPI = Kee[int](1)
    SelectedFromElsewhere = Kee[int](2)

  #  The classes Qt writes inside QMenuPrivate, each a class in here as in
  #  C++.

  class DelayState(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QMenuPrivate::DelayState: a plain Python object
    standing in front of one C++ QMenuPrivate::DelayState.

    What exists
    -----------

    Every function of Qt's QMenuPrivate::DelayState that has a ritual and
    that Python can call so far, 3 names in all: 'initialize', 'start',
    'stop'. It can be made from Python, in 1 way; see '__init__'.

    What to expect
    --------------

    - The C++ QMenuPrivate::DelayState is created at the first use, not by
      'QMenuPrivate::DelayState(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QMenuPrivate::DelayState.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QAction = WAIT['QAction']
      QMenu = WAIT['QMenu']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QMenuPrivate::DelayState'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QMenuPrivate::DelayState::DelayState()', which is called at the first
      use.

      Qt's own words:
      https://doc.qt.io/qt-6/qmenuprivate-delaystate.html#DelayState
      """
      #  QMenuPrivate::DelayState::DelayState()
      self._noteCreation(QMenuPrivate.DelayState, lambda: Rituals.call(
          'ritual_ZN12QMenuPrivate10DelayStateC1Ev',
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(QMenu)
    @overload(NoneType)
    def initialize(self, parent: Optional[QMenu]) -> None:
      """
      Calls Qt's 'void QMenuPrivate::DelayState::initialize(QMenu *parent)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qmenuprivate-delaystate.html#initialize

      Parameters
      ----------

      parent : Optional[QMenu]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  void QMenuPrivate::DelayState::initialize(QMenu *parent)
      self.uglySide.call(
          'ritual_ZN12QMenuPrivate10DelayState10initializeEP5QMenu',
          self._addressOf(parent),
      )

    @overload(int, QAction)
    @overload(int, NoneType)
    def start(self, timeout: int, toStartAction: Optional[QAction]) -> None:
      """
      Calls Qt's 'void QMenuPrivate::DelayState::start(int timeout, QAction
      *toStartAction)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qmenuprivate-delaystate.html#start

      Parameters
      ----------

      timeout : int
        Passed on as it is.

      toStartAction : Optional[QAction]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  void QMenuPrivate::DelayState::start(int timeout, QAction
      #      *toStartAction)
      self.uglySide.call(
          'ritual_ZN12QMenuPrivate10DelayState5startEiP7QAction',
          timeout, self._addressOf(toStartAction),
      )

    def stop(self) -> None:
      """
      Calls Qt's 'void QMenuPrivate::DelayState::stop()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qmenuprivate-delaystate.html#stop
      """
      #  void QMenuPrivate::DelayState::stop()
      self.uglySide.call('ritual_ZN12QMenuPrivate10DelayState4stopEv')

  class QMenuCaused(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QMenuPrivate::QMenuCaused: a plain Python object
    standing in front of one C++ QMenuPrivate::QMenuCaused.

    C++ hands a QMenuPrivate::QMenuCaused around as a copy, so every C++
    QMenuPrivate::QMenuCaused behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QMenuPrivate::QMenuCaused yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QMenuPrivate::QMenuCaused::~QMenuCaused()': the destructor:
      Python removes its C++ QMenuPrivate::QMenuCaused by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QMenuPrivate::QMenuCaused is created at the first use, not by
      'QMenuPrivate::QMenuCaused(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QMenuPrivate::QMenuCaused back gives a copy the
      ritual made for Python, in a new cute QMenuPrivate::QMenuCaused.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QMenuPrivate::QMenuCaused'

    #  Qt's '~QMenuPrivate::QMenuCaused()'. Naming it makes this a value
    #  class: Python owns every C++ QMenuPrivate::QMenuCaused behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN12QMenuPrivate11QMenuCausedD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class QMenuScroller(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QMenuPrivate::QMenuScroller: a plain Python object
    standing in front of one C++ QMenuPrivate::QMenuScroller.

    What exists
    -----------

    No function of Qt's QMenuPrivate::QMenuScroller yet. It can be made from
    Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QMenuPrivate::QMenuScroller::~QMenuScroller()': the destructor:
      Python never removes a C++ QMenuPrivate::QMenuScroller.

    What to expect
    --------------

    - The C++ QMenuPrivate::QMenuScroller is created at the first use, not by
      'QMenuPrivate::QMenuScroller(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QMenuPrivate::QMenuScroller.
    """

    #  The enums Qt writes inside QMenuPrivate::QMenuScroller, each a class
    #  in here as in C++, and the names Qt has for the combinations of its
    #  flags enums.

    class ScrollDirection(CuteNum):
      """
      The enum 'QMenuPrivate::QMenuScroller::ScrollDirection' of Qt, with the
      3 names Qt gives in it.
      """

      ScrollNone = Kee[int](0)
      ScrollUp = Kee[int](1)
      ScrollDown = Kee[int](2)

    class ScrollLocation(CuteNum):
      """
      The enum 'QMenuPrivate::QMenuScroller::ScrollLocation' of Qt, with the
      4 names Qt gives in it.
      """

      ScrollStay = Kee[int](0)
      ScrollBottom = Kee[int](1)
      ScrollTop = Kee[int](2)
      ScrollCenter = Kee[int](3)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QMenuPrivate::QMenuScroller'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QMenuPrivate::QMenuScroller::QMenuScroller()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qmenuprivate-qmenuscroller.html#QMenuScroller
      """
      #  QMenuPrivate::QMenuScroller::QMenuScroller()
      self._noteCreation(QMenuPrivate.QMenuScroller, lambda: Rituals.call(
          'ritual_ZN12QMenuPrivate13QMenuScrollerC1Ev',
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class ScrollerTearOffItem(QWidget):
    """
    The cute side of Qt's QMenuPrivate::ScrollerTearOffItem: a plain Python
    object standing in front of one C++ QMenuPrivate::ScrollerTearOffItem.

    It is built on the cute 'QWidget', as Qt's
    QMenuPrivate::ScrollerTearOffItem is built on Qt's QWidget, and has
    everything that class has.

    What exists
    -----------

    Every function of Qt's QMenuPrivate::ScrollerTearOffItem that has a
    ritual and that Python can call so far, 2 names in all: 'paintEvent',
    'updateScrollerRects'. It can be made from Python, in 1 way; see
    '__init__'.

    What to expect
    --------------

    - The C++ QMenuPrivate::ScrollerTearOffItem is created at the first use,
      not by 'QMenuPrivate::ScrollerTearOffItem(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QMenuPrivate::ScrollerTearOffItem.
    - Qt tells when it has removed the C++ QMenuPrivate::ScrollerTearOffItem.
      Every call on the cute object, and every use of it as an argument, then
      raises 'RuntimeError', and nothing reaches C++.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QMenuPrivate = WAIT['QMenuPrivate']
      QPaintEvent = WAIT['QPaintEvent']
      QRect = WAIT['QRect']

    #  The enums Qt writes inside QMenuPrivate::ScrollerTearOffItem, each a
    #  class in here as in C++, and the names Qt has for the combinations of
    #  its flags enums.

    class Type(CuteNum):
      """
      The enum 'QMenuPrivate::ScrollerTearOffItem::Type' of Qt, with the 2
      names Qt gives in it.
      """

      ScrollUp = Kee[int](0)
      ScrollDown = Kee[int](1)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QMenuPrivate::ScrollerTearOffItem'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(Type, QMenuPrivate)
    @overload(Type, NoneType)
    @overload(Type, QMenuPrivate, QWidget)
    @overload(Type, QMenuPrivate, NoneType)
    @overload(Type, NoneType, QWidget)
    @overload(Type, NoneType, NoneType)
    @overload(Type, QMenuPrivate, QWidget, Qt.WindowFlags)
    @overload(Type, QMenuPrivate, NoneType, Qt.WindowFlags)
    @overload(Type, NoneType, QWidget, Qt.WindowFlags)
    @overload(Type, NoneType, NoneType, Qt.WindowFlags)
    def __init__(
        self,
        type: Type,
        mPrivate: Optional[QMenuPrivate],
        parent: Optional[QWidget] = None,
        f: Qt.WindowFlags = Qt.WindowFlags(),
    ) -> None:
      """
      Notes what was given, for Qt's
      'QMenuPrivate::ScrollerTearOffItem::ScrollerTearOffItem(Type type,
      QMenuPrivate *mPrivate, QWidget *parent, Qt::WindowFlags f)', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qmenuprivate-scrollertearoffitem.html

      Parameters
      ----------

      type : Type
        Passed on as its number.

      mPrivate : Optional[QMenuPrivate]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      parent : Optional[QWidget]
        Passed on as the address of its C++ object. None is passed on as no
        object. May be left out, as in Qt: it is then None.

      f : Qt.WindowFlags
        Passed on as its number. May be left out, as in Qt: it is then
        Qt.WindowFlags().
      """
      #  QMenuPrivate::ScrollerTearOffItem::ScrollerTearOffItem(Type type,
      #      QMenuPrivate *mPrivate, QWidget *parent, Qt::WindowFlags f)
      self._noteCreation(
          QMenuPrivate.ScrollerTearOffItem, lambda: Rituals.call(
              'ritual_ZN12QMenuPrivate19ScrollerTearOffItemC1ENS0_4TypeEPS_'
              'P7QWidget6QFlagsIN2Qt10WindowTypeEE',
              type.value, self._addressOf(mPrivate), self._addressOf(parent),
              f.value,
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(QPaintEvent)
    @overload(NoneType)
    def paintEvent(self, e: Optional[QPaintEvent]) -> None:
      """
      Calls Qt's 'void
      QMenuPrivate::ScrollerTearOffItem::paintEvent(QPaintEvent *e)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qmenuprivate-scrollertearoffitem.html#paintEvent

      Parameters
      ----------

      e : Optional[QPaintEvent]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  void QMenuPrivate::ScrollerTearOffItem::paintEvent(QPaintEvent *e)
      ritual = (
          'ritual_ZN12QMenuPrivate19ScrollerTearOffItem10paintEventEP11QPai'
          'ntEvent')
      if self.uglySide.isOurs():
        ritual = (
            'ritual_own_ZN12QMenuPrivate19ScrollerTearOffItem10paintEventEP'
            '11QPaintEvent')
      self.uglySide.call(ritual, self._addressOf(e))

    @overload(QRect)
    def updateScrollerRects(self, rect: QRect) -> None:
      """
      Calls Qt's 'void
      QMenuPrivate::ScrollerTearOffItem::updateScrollerRects(const QRect
      &rect)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qmenuprivate-scrollertearoffitem.html

      Parameters
      ----------

      rect : QRect
        Passed on as a value: Qt reads the C++ QRect, which stays Python's
        own.
      """
      #  void QMenuPrivate::ScrollerTearOffItem::updateScrollerRects(const
      #      QRect &rect)
      self.uglySide.call(
          'ritual_ZN12QMenuPrivate19ScrollerTearOffItem19updateScrollerRect'
          'sERK5QRect',
          self._valueOf(rect),
      )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QMenu)
  @overload(NoneType)
  def get(m: Optional[QMenu]) -> Optional[QMenuPrivate]:
    """
    Calls Qt's 'QMenuPrivate *QMenuPrivate::get(QMenu *m)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenuprivate.html#get

    Parameters
    ----------

    m : Optional[QMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QMenuPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenuPrivate *QMenuPrivate::get(QMenu *m)
    address = Rituals.call(
        'ritual_ZN12QMenuPrivate3getEP5QMenu', CuteMixin._addressOf(m),
    )
    return QMenuPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMenuPrivate'

  #  A C++ QMenuPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMenuPrivate'

  #  The functions Qt calls itself that QMenuPrivate is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'calcCausedStack': (
          'QList<QPointer<QWidget>> QMenuPrivate::calcCausedStack() const',
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def scrollerHeight(self) -> int:
    """
    Calls Qt's 'int QMenuPrivate::scrollerHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenuprivate.html#scrollerHeight
    """
    #  int QMenuPrivate::scrollerHeight() const
    return self.uglySide.call('ritual_ZNK12QMenuPrivate14scrollerHeightEv')

  def isContextMenu(self) -> bool:
    """
    Calls Qt's 'bool QMenuPrivate::isContextMenu() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenuprivate.html#isContextMenu
    """
    #  bool QMenuPrivate::isContextMenu() const
    return self.uglySide.call('ritual_ZNK12QMenuPrivate13isContextMenuEv')

  @overload(QAction)
  @overload(NoneType)
  def actionRect(self, a0: Optional[QAction]) -> QRect:
    """
    Calls Qt's 'QRect QMenuPrivate::actionRect(QAction *a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenuprivate.html#actionRect

    Parameters
    ----------

    a0 : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QMenuPrivate::actionRect(QAction *a0) const
    address = self.uglySide.call(
        'ritual_ZNK12QMenuPrivate10actionRectEP7QAction',
        self._addressOf(a0),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload()
  @overload(QScreen)
  @overload(NoneType)
  def popupGeometry(self, screen: Optional[QScreen] = None) -> QRect:
    """
    Calls Qt's 'QRect QMenuPrivate::popupGeometry(QScreen *screen) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenuprivate.html#popupGeometry

    Parameters
    ----------

    screen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QMenuPrivate::popupGeometry(QScreen *screen) const
    address = self.uglySide.call(
        'ritual_ZNK12QMenuPrivate13popupGeometryEP7QScreen',
        self._addressOf(screen),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def useFullScreenForPopup(self) -> bool:
    """
    Calls Qt's 'bool QMenuPrivate::useFullScreenForPopup() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenuprivate.html#useFullScreenForPopup
    """
    #  bool QMenuPrivate::useFullScreenForPopup() const
    return self.uglySide.call(
        'ritual_ZNK12QMenuPrivate21useFullScreenForPopupEv',
    )

  def getLastVisibleAction(self) -> int:
    """
    Calls Qt's 'int QMenuPrivate::getLastVisibleAction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenuprivate.html#getLastVisibleAction
    """
    #  int QMenuPrivate::getLastVisibleAction() const
    return self.uglySide.call(
        'ritual_ZNK12QMenuPrivate20getLastVisibleActionEv',
    )

  def topCausedWidget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QMenuPrivate::topCausedWidget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenuprivate.html#topCausedWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QMenuPrivate::topCausedWidget() const
    address = self.uglySide.call(
        'ritual_ZNK12QMenuPrivate15topCausedWidgetEv',
    )
    from . import QWidget
    return QWidget._cuteAt(address)

  @overload(QPoint)
  def actionAt(self, p: QPoint) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QMenuPrivate::actionAt(QPoint p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenuprivate.html#actionAt

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QMenuPrivate::actionAt(QPoint p) const
    address = self.uglySide.call(
        'ritual_ZNK12QMenuPrivate8actionAtE6QPoint', self._valueOf(p),
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(int)
  def actionAt(self, i: int) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QMenuPrivate::actionAt(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenuprivate.html#actionAt

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QMenuPrivate::actionAt(int i) const
    address = self.uglySide.call('ritual_ZNK12QMenuPrivate8actionAtEi', i)
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def transientParentWindow(self) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QMenuPrivate::transientParentWindow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenuprivate.html#transientParentWindow

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QMenuPrivate::transientParentWindow() const
    address = self.uglySide.call(
        'ritual_ZNK12QMenuPrivate21transientParentWindowEv',
    )
    from ..QtGui import QWindow
    return QWindow._cuteAt(address)

  @overload(QAction)
  @overload(NoneType)
  def indexOf(self, act: Optional[QAction]) -> int:
    """
    Calls Qt's 'int QMenuPrivate::indexOf(QAction *act) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenuprivate.html#indexOf

    Parameters
    ----------

    act : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QMenuPrivate::indexOf(QAction *act) const
    return self.uglySide.call(
        'ritual_ZNK12QMenuPrivate7indexOfEP7QAction', self._addressOf(act),
    )

  @overload(QPointF)
  def hasMouseMoved(self, globalPos: QPointF) -> bool:
    """
    Calls Qt's 'bool QMenuPrivate::hasMouseMoved(const QPointF &globalPos)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenuprivate.html#hasMouseMoved

    Parameters
    ----------

    globalPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QMenuPrivate::hasMouseMoved(const QPointF &globalPos) const
    return self.uglySide.call(
        'ritual_ZNK12QMenuPrivate13hasMouseMovedERK7QPointF',
        self._valueOf(globalPos, 'QPointF'),
    )

  def rect(self) -> QRect:
    """
    Calls Qt's 'QRect QMenuPrivate::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenuprivate.html#rect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QMenuPrivate::rect() const
    address = self.uglySide.call('ritual_ZNK12QMenuPrivate4rectEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QAction)
  @overload(NoneType)
  def considerAction(self, action: Optional[QAction]) -> bool:
    """
    Calls Qt's 'bool QMenuPrivate::considerAction(const QAction *action)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenuprivate.html#considerAction

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QMenuPrivate::considerAction(const QAction *action) const
    return self.uglySide.call(
        'ritual_ZNK12QMenuPrivate14considerActionEPK7QAction',
        self._addressOf(action),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPlatformMenu)
  @overload(NoneType)
  def setPlatformMenu(self, menu: Optional[QPlatformMenu]) -> None:
    """
    Calls Qt's 'void QMenuPrivate::setPlatformMenu(QPlatformMenu *menu)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenuprivate.html#setPlatformMenu

    Parameters
    ----------

    menu : Optional[QPlatformMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenuPrivate::setPlatformMenu(QPlatformMenu *menu)
    self.uglySide.call(
        'ritual_ZN12QMenuPrivate15setPlatformMenuEP13QPlatformMenu',
        self._addressOf(menu),
    )

  def setSyncAction(self) -> None:
    """
    Calls Qt's 'void QMenuPrivate::setSyncAction()'.

    Qt's own words: https://doc.qt.io/qt-6/qmenuprivate.html#setSyncAction
    """
    #  void QMenuPrivate::setSyncAction()
    self.uglySide.call('ritual_ZN12QMenuPrivate13setSyncActionEv')

  @overload(QAction)
  @overload(NoneType)
  def setOverrideMenuAction(self, a0: Optional[QAction]) -> None:
    """
    Calls Qt's 'void QMenuPrivate::setOverrideMenuAction(QAction *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenuprivate.html#setOverrideMenuAction

    Parameters
    ----------

    a0 : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenuPrivate::setOverrideMenuAction(QAction *a0)
    self.uglySide.call(
        'ritual_ZN12QMenuPrivate21setOverrideMenuActionEP7QAction',
        self._addressOf(a0),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QMenuPrivate::QMenuPrivate()': leans on
    'QTornOffMenu::staticMetaObject', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMenuPrivate.__init__' has no cute function yet. Qt's "
        "'QMenuPrivate::QMenuPrivate()': leans on "
        "'QTornOffMenu::staticMetaObject', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

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

  def q_func(self) -> Optional[QMenu]:
    """
    Calls Qt's 'QMenu *QMenuPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qmenuprivate.html#q_func

    Returns
    -------

    Optional[QMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenu *QMenuPrivate::q_func()
    address = self.uglySide.call('ritual_ZN12QMenuPrivate6q_funcEv')
    from . import QMenu
    return QMenu._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QMenuPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qmenuprivate.html#init
    """
    #  void QMenuPrivate::init()
    self.uglySide.call('ritual_ZN12QMenuPrivate4initEv')

  def createPlatformMenu(self) -> Optional[QPlatformMenu]:
    """
    Calls Qt's 'QPlatformMenu *QMenuPrivate::createPlatformMenu()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenuprivate.html#createPlatformMenu

    Returns
    -------

    Optional[QPlatformMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMenu *QMenuPrivate::createPlatformMenu()
    address = self.uglySide.call(
        'ritual_ZN12QMenuPrivate18createPlatformMenuEv',
    )
    from ..QtGui import QPlatformMenu
    return QPlatformMenu._cuteAt(address)

  def syncPlatformMenu(self) -> None:
    """
    Calls Qt's 'void QMenuPrivate::syncPlatformMenu()'.

    Qt's own words: https://doc.qt.io/qt-6/qmenuprivate.html#syncPlatformMenu
    """
    #  void QMenuPrivate::syncPlatformMenu()
    self.uglySide.call('ritual_ZN12QMenuPrivate16syncPlatformMenuEv')

  @overload(QAction, QPlatformMenuItem)
  @overload(QAction, NoneType)
  @overload(NoneType, QPlatformMenuItem)
  @overload(NoneType, NoneType)
  def copyActionToPlatformItem(
      self,
      action: Optional[QAction],
      item: Optional[QPlatformMenuItem],
  ) -> None:
    """
    Calls Qt's 'void QMenuPrivate::copyActionToPlatformItem(const QAction
    *action, QPlatformMenuItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenuprivate.html#copyActionToPlatformItem

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QPlatformMenuItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenuPrivate::copyActionToPlatformItem(const QAction *action,
    #      QPlatformMenuItem *item)
    self.uglySide.call(
        'ritual_ZN12QMenuPrivate24copyActionToPlatformItemEPK7QActionP17QPl'
        'atformMenuItem',
        self._addressOf(action), self._addressOf(item),
    )

  @overload(QAction, QPlatformMenuItem)
  @overload(QAction, NoneType)
  @overload(NoneType, QPlatformMenuItem)
  @overload(NoneType, NoneType)
  def insertActionInPlatformMenu(
      self,
      action: Optional[QAction],
      beforeItem: Optional[QPlatformMenuItem],
  ) -> Optional[QPlatformMenuItem]:
    """
    Calls Qt's 'QPlatformMenuItem
    *QMenuPrivate::insertActionInPlatformMenu(const QAction *action,
    QPlatformMenuItem *beforeItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenuprivate.html#insertActionInPlatformMenu

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    beforeItem : Optional[QPlatformMenuItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPlatformMenuItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMenuItem *QMenuPrivate::insertActionInPlatformMenu(const
    #      QAction *action, QPlatformMenuItem *beforeItem)
    address = self.uglySide.call(
        'ritual_ZN12QMenuPrivate26insertActionInPlatformMenuEPK7QActionP17Q'
        'PlatformMenuItem',
        self._addressOf(action), self._addressOf(beforeItem),
    )
    from ..QtGui import QPlatformMenuItem
    return QPlatformMenuItem._cuteAt(address)

  @overload()
  def updateActionRects(self) -> None:
    """
    Calls Qt's 'void QMenuPrivate::updateActionRects() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenuprivate.html#updateActionRects
    """
    #  void QMenuPrivate::updateActionRects() const
    self.uglySide.call('ritual_ZNK12QMenuPrivate17updateActionRectsEv')

  @overload(QRect)
  def updateActionRects(self, screen: QRect) -> None:
    """
    Calls Qt's 'void QMenuPrivate::updateActionRects(const QRect &screen)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenuprivate.html#updateActionRects

    Parameters
    ----------

    screen : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QMenuPrivate::updateActionRects(const QRect &screen) const
    self.uglySide.call(
        'ritual_ZNK12QMenuPrivate17updateActionRectsERK5QRect',
        self._valueOf(screen),
    )

  @overload(QMenu)
  @overload(NoneType)
  def hideMenu(self, menu: Optional[QMenu]) -> None:
    """
    Calls Qt's 'void QMenuPrivate::hideMenu(QMenu *menu)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenuprivate.html#hideMenu

    Parameters
    ----------

    menu : Optional[QMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenuPrivate::hideMenu(QMenu *menu)
    self.uglySide.call(
        'ritual_ZN12QMenuPrivate8hideMenuEP5QMenu', self._addressOf(menu),
    )

  def _q_overrideMenuActionDestroyed(self) -> None:
    """
    Calls Qt's 'void QMenuPrivate::_q_overrideMenuActionDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenuprivate.html#_q_overrideMenuActionDestroyed
    """
    #  void QMenuPrivate::_q_overrideMenuActionDestroyed()
    self.uglySide.call(
        'ritual_ZN12QMenuPrivate30_q_overrideMenuActionDestroyedEv',
    )

  def _q_actionHovered(self) -> None:
    """
    Calls Qt's 'void QMenuPrivate::_q_actionHovered()'.

    Qt's own words: https://doc.qt.io/qt-6/qmenuprivate.html#_q_actionHovered
    """
    #  void QMenuPrivate::_q_actionHovered()
    self.uglySide.call('ritual_ZN12QMenuPrivate16_q_actionHoveredEv')

  def _q_platformMenuAboutToShow(self) -> None:
    """
    Calls Qt's 'void QMenuPrivate::_q_platformMenuAboutToShow()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenuprivate.html#_q_platformMenuAboutToShow
    """
    #  void QMenuPrivate::_q_platformMenuAboutToShow()
    self.uglySide.call(
        'ritual_ZN12QMenuPrivate26_q_platformMenuAboutToShowEv',
    )

  def updateLayoutDirection(self) -> None:
    """
    Calls Qt's 'void QMenuPrivate::updateLayoutDirection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenuprivate.html#updateLayoutDirection
    """
    #  void QMenuPrivate::updateLayoutDirection()
    self.uglySide.call('ritual_ZN12QMenuPrivate21updateLayoutDirectionEv')

  @overload(QPainter, QRect)
  @overload(NoneType, QRect)
  def drawTearOff(self, painter: Optional[QPainter], rect: QRect) -> None:
    """
    Calls Qt's 'void QMenuPrivate::drawTearOff(QPainter *painter, const QRect
    &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenuprivate.html#drawTearOff

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QMenuPrivate::drawTearOff(QPainter *painter, const QRect &rect)
    self.uglySide.call(
        'ritual_ZN12QMenuPrivate11drawTearOffEP8QPainterRK5QRect',
        self._addressOf(painter), self._valueOf(rect),
    )

  @staticmethod
  def _q_actionTriggered(*__, **_) -> Never:
    """
    Qt's 'void QMenuPrivate::_q_actionTriggered()': leans on
    'QMenuBarPrivate::updateGeometries()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMenuPrivate._q_actionTriggered' has no cute function yet. Qt's "
        "'void QMenuPrivate::_q_actionTriggered()': leans on "
        "'QMenuBarPrivate::updateGeometries()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def activateAction(*__, **_) -> Never:
    """
    Qt's 'void QMenuPrivate::activateAction(QAction *a0, QAction::ActionEvent
    a1, bool self_)': leans on 'QMenuBarPrivate::updateGeometries()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QMenuPrivate.activateAction' has no cute function yet. Qt's 'void "
        "QMenuPrivate::activateAction(QAction *a0, QAction::ActionEvent a1, "
        "bool self_)': leans on 'QMenuBarPrivate::updateGeometries()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def activateCausedStack(*__, **_) -> Never:
    """
    Qt's 'void QMenuPrivate::activateCausedStack(const
    QList<QPointer<QWidget>> &a0, QAction *a1, QAction::ActionEvent a2, bool
    a3)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMenuPrivate.activateCausedStack' has no cute function yet. Qt's "
        "'void QMenuPrivate::activateCausedStack(const "
        "QList<QPointer<QWidget>> &a0, QAction *a1, QAction::ActionEvent "
        "a2, bool a3)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def calcCausedStack(*__, **_) -> Never:
    """
    Qt's 'QList<QPointer<QWidget>> QMenuPrivate::calcCausedStack() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QMenuPrivate.calcCausedStack' has no cute function yet. Qt's "
        "'QList<QPointer<QWidget>> QMenuPrivate::calcCausedStack() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def drawScroller(*__, **_) -> Never:
    """
    Qt's 'void QMenuPrivate::drawScroller(QPainter *painter,
    ScrollerTearOffItem::Type type, const QRect &rect)': names the enum
    'QMenuPrivate::ScrollerTearOffItem::Type', whose class cannot be named
    here.
    """
    raise NotImplementedError(
        "'QMenuPrivate.drawScroller' has no cute function yet. Qt's 'void "
        "QMenuPrivate::drawScroller(QPainter *painter, "
        "ScrollerTearOffItem::Type type, const QRect &rect)': names the "
        "enum 'QMenuPrivate::ScrollerTearOffItem::Type', whose class cannot "
        "be named here.")

  @staticmethod
  def exec(*__, **_) -> Never:
    """
    Qt's 'QAction *QMenuPrivate::exec(const QPoint &p, QAction *action,
    PositionFunction positionFunction)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QMenuPrivate.exec' has no cute function yet. Qt's 'QAction "
        "*QMenuPrivate::exec(const QPoint &p, QAction *action, "
        "PositionFunction positionFunction)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def hideUpToMenuBar(*__, **_) -> Never:
    """
    Qt's 'void QMenuPrivate::hideUpToMenuBar()': leans on
    'QMenuBarPrivate::updateGeometries()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMenuPrivate.hideUpToMenuBar' has no cute function yet. Qt's "
        "'void QMenuPrivate::hideUpToMenuBar()': leans on "
        "'QMenuBarPrivate::updateGeometries()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def mouseEventTaken(*__, **_) -> Never:
    """
    Qt's 'bool QMenuPrivate::mouseEventTaken(QMouseEvent *a0)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: allocation of incomplete type 'QTornOffMenu'.
    """
    raise NotImplementedError(
        "'QMenuPrivate.mouseEventTaken' has no cute function yet. Qt's "
        "'bool QMenuPrivate::mouseEventTaken(QMouseEvent *a0)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: allocation of incomplete type "
        "'QTornOffMenu'.")

  @staticmethod
  def popup(*__, **_) -> Never:
    """
    Qt's 'void QMenuPrivate::popup(const QPoint &p, QAction *atAction,
    PositionFunction positionFunction)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QMenuPrivate.popup' has no cute function yet. Qt's 'void "
        "QMenuPrivate::popup(const QPoint &p, QAction *atAction, "
        "PositionFunction positionFunction)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def popupAction(*__, **_) -> Never:
    """
    Qt's 'void QMenuPrivate::popupAction(QAction *a0, int a1, bool a2)':
    leans on 'QMenuBarPrivate::updateGeometries()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMenuPrivate.popupAction' has no cute function yet. Qt's 'void "
        "QMenuPrivate::popupAction(QAction *a0, int a1, bool a2)': leans on "
        "'QMenuBarPrivate::updateGeometries()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def scrollMenu(*__, **_) -> Never:
    """
    - Qt's 'void QMenuPrivate::scrollMenu(QMenuScroller::ScrollLocation
      location, bool active)': leans on
      'QMenuBarPrivate::updateGeometries()', which Qt's source does not mark
      for use from outside Qt and has no code for that could be taken.
    - Qt's 'void QMenuPrivate::scrollMenu(QMenuScroller::ScrollDirection
      direction, bool page, bool active)': leans on
      'QMenuBarPrivate::updateGeometries()', which Qt's source does not mark
      for use from outside Qt and has no code for that could be taken.
    - Qt's 'void QMenuPrivate::scrollMenu(QAction *action,
      QMenuScroller::ScrollLocation location, bool active)': leans on
      'QMenuBarPrivate::updateGeometries()', which Qt's source does not mark
      for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMenuPrivate.scrollMenu' has no cute function yet. Qt's 'void "
        "QMenuPrivate::scrollMenu(QMenuScroller::ScrollLocation location, "
        "bool active)': leans on 'QMenuBarPrivate::updateGeometries()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken. Qt's 'void "
        "QMenuPrivate::scrollMenu(QMenuScroller::ScrollDirection direction, "
        "bool page, bool active)': leans on "
        "'QMenuBarPrivate::updateGeometries()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken. Qt's 'void QMenuPrivate::scrollMenu(QAction *action, "
        "QMenuScroller::ScrollLocation location, bool active)': leans on "
        "'QMenuBarPrivate::updateGeometries()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setCurrentAction(*__, **_) -> Never:
    """
    Qt's 'void QMenuPrivate::setCurrentAction(QAction *a0, int popup,
    SelectionReason reason, SelectionDirection direction, bool
    activateFirst)': leans on 'QMenuBarPrivate::updateGeometries()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QMenuPrivate.setCurrentAction' has no cute function yet. Qt's "
        "'void QMenuPrivate::setCurrentAction(QAction *a0, int popup, "
        "SelectionReason reason, SelectionDirection direction, bool "
        "activateFirst)': leans on 'QMenuBarPrivate::updateGeometries()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setFirstActionActive(*__, **_) -> Never:
    """
    Qt's 'void QMenuPrivate::setFirstActionActive()': leans on
    'QMenuBarPrivate::updateGeometries()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMenuPrivate.setFirstActionActive' has no cute function yet. Qt's "
        "'void QMenuPrivate::setFirstActionActive()': leans on "
        "'QMenuBarPrivate::updateGeometries()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
