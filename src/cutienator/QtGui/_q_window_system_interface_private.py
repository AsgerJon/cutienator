"""
QWindowSystemInterfacePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QEvent, QEventLoop, QList
from . import QWindowSystemInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPoint, QPointF, QRect, QUrl
  from . import QEventPoint, QInputDevice, QPointingDevice, QRegion, QScreen
  from . import QWindow, QWindowSystemEventHandler
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEventPoint = WAIT['QEventPoint']
  QWindow = WAIT['QWindow']
  QWindowSystemEventHandler = WAIT['QWindowSystemEventHandler']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWindowSystemInterfacePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWindowSystemInterfacePrivate: a plain Python object
  standing in front of one C++ QWindowSystemInterfacePrivate.

  C++ hands a QWindowSystemInterfacePrivate around as a copy, so every C++
  QWindowSystemInterfacePrivate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QWindowSystemInterfacePrivate that has a ritual and
  that Python can call so far, 9 names in all: 'windowSystemEventsQueued',
  'nonUserInputEventsQueued', 'getWindowSystemEvent',
  'getNonUserInputWindowSystemEvent', 'peekWindowSystemEvent',
  'removeWindowSystemEvent', 'toNativeTouchPoint',
  'installWindowSystemEventHandler', 'removeWindowSystemEventhandler'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<QEventPoint>
    QWindowSystemInterfacePrivate::fromNativeTouchPoints(const
    QList<QWindowSystemInterface::TouchPoint> &points, const QWindow *window,
    QEvent::Type *type)': takes a type Python has no way to hand over yet.
  - Qt's 'QWindowSystemInterfacePrivate::~QWindowSystemInterfacePrivate()':
    the destructor: Python removes its C++ QWindowSystemInterfacePrivate by
    it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 12 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QWindowSystemInterfacePrivate is created at the first use, not by
    'QWindowSystemInterfacePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWindowSystemInterfacePrivate back gives a copy the
    ritual made for Python, in a new cute QWindowSystemInterfacePrivate.
  - Each name of Qt's QWindowSystemInterfacePrivate that has no cute function
    yet, 'fromNativeTouchPoints', 'toNativeTouchPoints', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QWindowSystemInterfacePrivate, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class EventType(CuteNum):
    """
    The enum 'QWindowSystemInterfacePrivate::EventType' of Qt, with the 33
    names Qt gives in it.
    """

    UserInputEvent = Kee[int](256)
    Close = Kee[int](257)
    GeometryChange = Kee[int](2)
    Enter = Kee[int](259)
    Leave = Kee[int](260)
    FocusWindow = Kee[int](5)
    WindowStateChanged = Kee[int](6)
    Mouse = Kee[int](263)
    Wheel = Kee[int](265)
    Key = Kee[int](266)
    Touch = Kee[int](267)
    ScreenOrientation = Kee[int](12)
    ScreenGeometry = Kee[int](13)
    ScreenAvailableGeometry = Kee[int](14)
    ScreenLogicalDotsPerInch = Kee[int](15)
    ScreenRefreshRate = Kee[int](16)
    ThemeChange = Kee[int](17)
    Expose = Kee[int](18)
    FileOpen = Kee[int](275)
    Tablet = Kee[int](276)
    TabletEnterProximity = Kee[int](277)
    TabletLeaveProximity = Kee[int](278)
    PlatformPanel = Kee[int](279)
    ContextMenu = Kee[int](280)
    EnterWhatsThisMode = Kee[int](281)
    Gesture = Kee[int](282)
    ApplicationStateChanged = Kee[int](25)
    FlushEvents = Kee[int](32)
    WindowScreenChanged = Kee[int](33)
    SafeAreaMarginsChanged = Kee[int](34)
    ApplicationTermination = Kee[int](35)
    Paint = Kee[int](36)
    WindowDevicePixelRatioChanged = Kee[int](37)

  #  The classes Qt writes inside QWindowSystemInterfacePrivate, each a class
  #  in here as in C++.

  class ApplicationStateChangedEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's
    QWindowSystemInterfacePrivate::ApplicationStateChangedEvent: a plain
    Python object standing in front of one C++
    QWindowSystemInterfacePrivate::ApplicationStateChangedEvent.

    C++ hands a QWindowSystemInterfacePrivate::ApplicationStateChangedEvent
    around as a copy, so every C++
    QWindowSystemInterfacePrivate::ApplicationStateChangedEvent behind a cute
    one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's
    QWindowSystemInterfacePrivate::ApplicationStateChangedEvent yet. It can
    be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWindowSystemInterfacePrivate::ApplicationStateChangedEvent::
      ~ApplicationStateChangedEvent()': the destructor: Python removes its
      C++ QWindowSystemInterfacePrivate::ApplicationStateChangedEvent by it,
      and has no other use for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::ApplicationStateChangedEvent is
      created at the first use, not by
      'QWindowSystemInterfacePrivate::ApplicationStateChangedEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a
      QWindowSystemInterfacePrivate::ApplicationStateChangedEvent back gives
      a copy the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::ApplicationStateChangedEvent.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::ApplicationStateChangedEvent'

    #  Qt's '~QWindowSystemInterfacePrivate::ApplicationStateChangedEvent()'.
    #  Naming it makes this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::ApplicationStateChangedEvent behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate28ApplicationStateChangedEventD1Ev')

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

    @overload(Qt.ApplicationState)
    @overload(Qt.ApplicationState, bool)
    def __init__(
        self,
        newState: Qt.ApplicationState,
        forcePropagate: bool = False,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QWindowSystemInterfacePrivate::ApplicationStateChangedEvent::
      ApplicationStateChangedEvent(Qt::ApplicationState newState, bool
      forcePropagate)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-applicationstatechangedevent.html

      Parameters
      ----------

      newState : Qt.ApplicationState
        Passed on as its number.

      forcePropagate : bool
        Passed on as it is. May be left out, as in Qt: it is then False.
      """
      #  QWindowSystemInterfacePrivate::ApplicationStateChangedEvent::
      #      ApplicationStateChangedEvent(Qt::ApplicationState newState, bool
      #      forcePropagate)
      self._noteCreation(
          QWindowSystemInterfacePrivate.ApplicationStateChangedEvent, lambda: Rituals.call(
              'ritual_ZN29QWindowSystemInterfacePrivate28ApplicationStateCh'
              'angedEventC1EN2Qt16ApplicationStateEb',
              newState.value, forcePropagate,
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

  class CloseEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWindowSystemInterfacePrivate::CloseEvent: a plain
    Python object standing in front of one C++
    QWindowSystemInterfacePrivate::CloseEvent.

    C++ hands a QWindowSystemInterfacePrivate::CloseEvent around as a copy,
    so every C++ QWindowSystemInterfacePrivate::CloseEvent behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QWindowSystemInterfacePrivate::CloseEvent yet. It can
    be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWindowSystemInterfacePrivate::CloseEvent::~CloseEvent()': the
      destructor: Python removes its C++
      QWindowSystemInterfacePrivate::CloseEvent by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::CloseEvent is created at the
      first use, not by 'QWindowSystemInterfacePrivate::CloseEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWindowSystemInterfacePrivate::CloseEvent back
      gives a copy the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::CloseEvent.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QWindow = WAIT['QWindow']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::CloseEvent'

    #  Qt's '~QWindowSystemInterfacePrivate::CloseEvent()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::CloseEvent behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate10CloseEventD1Ev')

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

    @overload(QWindow)
    @overload(NoneType)
    def __init__(self, w: Optional[QWindow]) -> None:
      """
      Notes what was given, for Qt's
      'QWindowSystemInterfacePrivate::CloseEvent::CloseEvent(QWindow *w)',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-closeevent.html

      Parameters
      ----------

      w : Optional[QWindow]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  QWindowSystemInterfacePrivate::CloseEvent::CloseEvent(QWindow *w)
      self._noteCreation(
          QWindowSystemInterfacePrivate.CloseEvent, lambda: Rituals.call(
              'ritual_ZN29QWindowSystemInterfacePrivate10CloseEventC1EP7QWi'
              'ndow',
              self._addressOf(w),
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

  class ContextMenuEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWindowSystemInterfacePrivate::ContextMenuEvent: a
    plain Python object standing in front of one C++
    QWindowSystemInterfacePrivate::ContextMenuEvent.

    C++ hands a QWindowSystemInterfacePrivate::ContextMenuEvent around as a
    copy, so every C++ QWindowSystemInterfacePrivate::ContextMenuEvent behind
    a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QWindowSystemInterfacePrivate::ContextMenuEvent yet.
    It can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QWindowSystemInterfacePrivate::ContextMenuEvent::~ContextMenuEvent()':
      the destructor: Python removes its C++
      QWindowSystemInterfacePrivate::ContextMenuEvent by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::ContextMenuEvent is created at
      the first use, not by
      'QWindowSystemInterfacePrivate::ContextMenuEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWindowSystemInterfacePrivate::ContextMenuEvent
      back gives a copy the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::ContextMenuEvent.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QPoint = WAIT['QPoint']
      QWindow = WAIT['QWindow']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::ContextMenuEvent'

    #  Qt's '~QWindowSystemInterfacePrivate::ContextMenuEvent()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::ContextMenuEvent behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate16ContextMenuEventD1Ev')

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

    @overload(QWindow, bool, QPoint, QPoint, Qt.KeyboardModifiers)
    @overload(NoneType, bool, QPoint, QPoint, Qt.KeyboardModifiers)
    def __init__(
        self,
        w: Optional[QWindow],
        mouseTriggered: bool,
        pos: QPoint,
        globalPos: QPoint,
        modifiers: Qt.KeyboardModifiers,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QWindowSystemInterfacePrivate::ContextMenuEvent::ContextMenuEvent(
      QWindow *w, bool mouseTriggered, const QPoint &pos, const QPoint
      &globalPos, Qt::KeyboardModifiers modifiers)', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-contextmenuevent.html

      Parameters
      ----------

      w : Optional[QWindow]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      mouseTriggered : bool
        Passed on as it is.

      pos : QPoint
        Passed on as a value: Qt reads the C++ QPoint, which stays Python's
        own.

      globalPos : QPoint
        Passed on as a value: Qt reads the C++ QPoint, which stays Python's
        own.

      modifiers : Qt.KeyboardModifiers
        Passed on as its number.
      """
      #  QWindowSystemInterfacePrivate::ContextMenuEvent::
      #      ContextMenuEvent(QWindow *w, bool mouseTriggered, const QPoint
      #      &pos, const QPoint &globalPos, Qt::KeyboardModifiers modifiers)
      self._noteCreation(
          QWindowSystemInterfacePrivate.ContextMenuEvent, lambda: Rituals.call(
              'ritual_ZN29QWindowSystemInterfacePrivate16ContextMenuEventC1'
              'EP7QWindowbRK6QPointS5_6QFlagsIN2Qt16KeyboardModifierEE',
              self._addressOf(w), mouseTriggered, self._valueOf(pos),
              self._valueOf(globalPos), modifiers.value,
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

  class EnterEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWindowSystemInterfacePrivate::EnterEvent: a plain
    Python object standing in front of one C++
    QWindowSystemInterfacePrivate::EnterEvent.

    C++ hands a QWindowSystemInterfacePrivate::EnterEvent around as a copy,
    so every C++ QWindowSystemInterfacePrivate::EnterEvent behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QWindowSystemInterfacePrivate::EnterEvent yet. It can
    be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWindowSystemInterfacePrivate::EnterEvent::~EnterEvent()': the
      destructor: Python removes its C++
      QWindowSystemInterfacePrivate::EnterEvent by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::EnterEvent is created at the
      first use, not by 'QWindowSystemInterfacePrivate::EnterEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWindowSystemInterfacePrivate::EnterEvent back
      gives a copy the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::EnterEvent.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QPointF = WAIT['QPointF']
      QWindow = WAIT['QWindow']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::EnterEvent'

    #  Qt's '~QWindowSystemInterfacePrivate::EnterEvent()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::EnterEvent behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate10EnterEventD1Ev')

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

    @overload(QWindow, QPointF, QPointF)
    @overload(NoneType, QPointF, QPointF)
    def __init__(
        self,
        enter: Optional[QWindow],
        local: QPointF,
        global_: QPointF,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QWindowSystemInterfacePrivate::EnterEvent::EnterEvent(QWindow *enter,
      const QPointF &local, const QPointF &global)', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-enterevent.html

      Parameters
      ----------

      enter : Optional[QWindow]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      local : QPointF
        Passed on as a value: Qt reads the C++ QPointF, which stays Python's
        own.

      global_ : QPointF
        Passed on as a value: Qt reads the C++ QPointF, which stays Python's
        own.
      """
      #  QWindowSystemInterfacePrivate::EnterEvent::EnterEvent(QWindow
      #      *enter, const QPointF &local, const QPointF &global)
      self._noteCreation(
          QWindowSystemInterfacePrivate.EnterEvent, lambda: Rituals.call(
              'ritual_ZN29QWindowSystemInterfacePrivate10EnterEventC1EP7QWi'
              'ndowRK7QPointFS5_',
              self._addressOf(enter), self._valueOf(local, 'QPointF'),
              self._valueOf(global_, 'QPointF'),
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

  class ExposeEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWindowSystemInterfacePrivate::ExposeEvent: a plain
    Python object standing in front of one C++
    QWindowSystemInterfacePrivate::ExposeEvent.

    C++ hands a QWindowSystemInterfacePrivate::ExposeEvent around as a copy,
    so every C++ QWindowSystemInterfacePrivate::ExposeEvent behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QWindowSystemInterfacePrivate::ExposeEvent yet. It
    can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWindowSystemInterfacePrivate::ExposeEvent::~ExposeEvent()': the
      destructor: Python removes its C++
      QWindowSystemInterfacePrivate::ExposeEvent by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::ExposeEvent is created at the
      first use, not by 'QWindowSystemInterfacePrivate::ExposeEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWindowSystemInterfacePrivate::ExposeEvent back
      gives a copy the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::ExposeEvent.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QRegion = WAIT['QRegion']
      QWindow = WAIT['QWindow']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::ExposeEvent'

    #  Qt's '~QWindowSystemInterfacePrivate::ExposeEvent()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::ExposeEvent behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate11ExposeEventD1Ev')

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

    @overload(QWindow, QRegion)
    @overload(NoneType, QRegion)
    def __init__(self, window: Optional[QWindow], region: QRegion) -> None:
      """
      Notes what was given, for Qt's
      'QWindowSystemInterfacePrivate::ExposeEvent::ExposeEvent(QWindow
      *window, const QRegion &region)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-exposeevent.html

      Parameters
      ----------

      window : Optional[QWindow]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      region : QRegion
        Passed on as a value: Qt reads the C++ QRegion, which stays Python's
        own.
      """
      #  QWindowSystemInterfacePrivate::ExposeEvent::ExposeEvent(QWindow
      #      *window, const QRegion &region)
      self._noteCreation(
          QWindowSystemInterfacePrivate.ExposeEvent, lambda: Rituals.call(
              'ritual_ZN29QWindowSystemInterfacePrivate11ExposeEventC1EP7QW'
              'indowRK7QRegion',
              self._addressOf(window), self._valueOf(region),
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

  class FileOpenEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWindowSystemInterfacePrivate::FileOpenEvent: a
    plain Python object standing in front of one C++
    QWindowSystemInterfacePrivate::FileOpenEvent.

    C++ hands a QWindowSystemInterfacePrivate::FileOpenEvent around as a
    copy, so every C++ QWindowSystemInterfacePrivate::FileOpenEvent behind a
    cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QWindowSystemInterfacePrivate::FileOpenEvent yet. It
    can be made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWindowSystemInterfacePrivate::FileOpenEvent::~FileOpenEvent()':
      the destructor: Python removes its C++
      QWindowSystemInterfacePrivate::FileOpenEvent by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::FileOpenEvent is created at the
      first use, not by 'QWindowSystemInterfacePrivate::FileOpenEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWindowSystemInterfacePrivate::FileOpenEvent back
      gives a copy the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::FileOpenEvent.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QUrl = WAIT['QUrl']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::FileOpenEvent'

    #  Qt's '~QWindowSystemInterfacePrivate::FileOpenEvent()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::FileOpenEvent behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate13FileOpenEventD1Ev')

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

    @overload(str)
    def __init__(self, fileName: str) -> None:
      """
      Notes what was given, for Qt's
      'QWindowSystemInterfacePrivate::FileOpenEvent::FileOpenEvent(const
      QString &fileName)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-fileopenevent.html

      Parameters
      ----------

      fileName : str
        Passed on as it is: a QString is made of it for the call.
      """
      #  QWindowSystemInterfacePrivate::FileOpenEvent::FileOpenEvent(const
      #      QString &fileName)
      self._noteCreation(
          QWindowSystemInterfacePrivate.FileOpenEvent, lambda: Rituals.call(
              'ritual_ZN29QWindowSystemInterfacePrivate13FileOpenEventC1ERK'
              '7QString',
              fileName,
          ))

    @overload(QUrl)
    def __init__(self, url: QUrl) -> None:
      """
      Notes what was given, for Qt's
      'QWindowSystemInterfacePrivate::FileOpenEvent::FileOpenEvent(const QUrl
      &url)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-fileopenevent.html

      Parameters
      ----------

      url : QUrl
        Passed on as a value: Qt reads the C++ QUrl, which stays Python's
        own.
      """
      #  QWindowSystemInterfacePrivate::FileOpenEvent::FileOpenEvent(const
      #      QUrl &url)
      self._noteCreation(
          QWindowSystemInterfacePrivate.FileOpenEvent, lambda: Rituals.call(
              'ritual_ZN29QWindowSystemInterfacePrivate13FileOpenEventC1ERK'
              '4QUrl',
              self._valueOf(url),
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

  class FlushEventsEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWindowSystemInterfacePrivate::FlushEventsEvent: a
    plain Python object standing in front of one C++
    QWindowSystemInterfacePrivate::FlushEventsEvent.

    C++ hands a QWindowSystemInterfacePrivate::FlushEventsEvent around as a
    copy, so every C++ QWindowSystemInterfacePrivate::FlushEventsEvent behind
    a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QWindowSystemInterfacePrivate::FlushEventsEvent yet.
    It can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QWindowSystemInterfacePrivate::FlushEventsEvent::~FlushEventsEvent()':
      the destructor: Python removes its C++
      QWindowSystemInterfacePrivate::FlushEventsEvent by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::FlushEventsEvent is created at
      the first use, not by
      'QWindowSystemInterfacePrivate::FlushEventsEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWindowSystemInterfacePrivate::FlushEventsEvent
      back gives a copy the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::FlushEventsEvent.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::FlushEventsEvent'

    #  Qt's '~QWindowSystemInterfacePrivate::FlushEventsEvent()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::FlushEventsEvent behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate16FlushEventsEventD1Ev')

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
    @overload(QEventLoop.ProcessEventsFlags)
    def __init__(
        self,
        f: QEventLoop.ProcessEventsFlags = (
            QEventLoop.ProcessEventsFlags.AllEvents),
    ) -> None:
      """
      Notes what was given, for Qt's
      'QWindowSystemInterfacePrivate::FlushEventsEvent::FlushEventsEvent(
      QEventLoop::ProcessEventsFlags f)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-flusheventsevent.html

      Parameters
      ----------

      f : QEventLoop.ProcessEventsFlags
        Passed on as its number. May be left out, as in Qt: it is then
        QEventLoop.ProcessEventsFlags.AllEvents.
      """
      #  QWindowSystemInterfacePrivate::FlushEventsEvent::
      #      FlushEventsEvent(QEventLoop::ProcessEventsFlags f)
      self._noteCreation(
          QWindowSystemInterfacePrivate.FlushEventsEvent, lambda: Rituals.call(
              'ritual_ZN29QWindowSystemInterfacePrivate16FlushEventsEventC1'
              'E6QFlagsIN10QEventLoop17ProcessEventsFlagEE',
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

  class FocusWindowEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWindowSystemInterfacePrivate::FocusWindowEvent: a
    plain Python object standing in front of one C++
    QWindowSystemInterfacePrivate::FocusWindowEvent.

    C++ hands a QWindowSystemInterfacePrivate::FocusWindowEvent around as a
    copy, so every C++ QWindowSystemInterfacePrivate::FocusWindowEvent behind
    a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QWindowSystemInterfacePrivate::FocusWindowEvent yet.
    It can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QWindowSystemInterfacePrivate::FocusWindowEvent::~FocusWindowEvent()':
      the destructor: Python removes its C++
      QWindowSystemInterfacePrivate::FocusWindowEvent by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::FocusWindowEvent is created at
      the first use, not by
      'QWindowSystemInterfacePrivate::FocusWindowEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWindowSystemInterfacePrivate::FocusWindowEvent
      back gives a copy the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::FocusWindowEvent.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QWindow = WAIT['QWindow']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::FocusWindowEvent'

    #  Qt's '~QWindowSystemInterfacePrivate::FocusWindowEvent()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::FocusWindowEvent behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate16FocusWindowEventD1Ev')

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

    @overload(QWindow, Qt.FocusReason)
    @overload(NoneType, Qt.FocusReason)
    def __init__(
        self,
        focusedWindow: Optional[QWindow],
        r: Qt.FocusReason,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QWindowSystemInterfacePrivate::FocusWindowEvent::FocusWindowEvent(
      QWindow *focusedWindow, Qt::FocusReason r)', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-focuswindowevent.html

      Parameters
      ----------

      focusedWindow : Optional[QWindow]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      r : Qt.FocusReason
        Passed on as its number.
      """
      #  QWindowSystemInterfacePrivate::FocusWindowEvent::
      #      FocusWindowEvent(QWindow *focusedWindow, Qt::FocusReason r)
      self._noteCreation(
          QWindowSystemInterfacePrivate.FocusWindowEvent, lambda: Rituals.call(
              'ritual_ZN29QWindowSystemInterfacePrivate16FocusWindowEventC1'
              'EP7QWindowN2Qt11FocusReasonE',
              self._addressOf(focusedWindow), r.value,
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

  class GeometryChangeEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWindowSystemInterfacePrivate::GeometryChangeEvent:
    a plain Python object standing in front of one C++
    QWindowSystemInterfacePrivate::GeometryChangeEvent.

    C++ hands a QWindowSystemInterfacePrivate::GeometryChangeEvent around as
    a copy, so every C++ QWindowSystemInterfacePrivate::GeometryChangeEvent
    behind a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QWindowSystemInterfacePrivate::GeometryChangeEvent
    yet. It can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWindowSystemInterfacePrivate::GeometryChangeEvent::
      ~GeometryChangeEvent()': the destructor: Python removes its C++
      QWindowSystemInterfacePrivate::GeometryChangeEvent by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::GeometryChangeEvent is created
      at the first use, not by
      'QWindowSystemInterfacePrivate::GeometryChangeEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWindowSystemInterfacePrivate::GeometryChangeEvent
      back gives a copy the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::GeometryChangeEvent.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QRect = WAIT['QRect']
      QWindow = WAIT['QWindow']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::GeometryChangeEvent'

    #  Qt's '~QWindowSystemInterfacePrivate::GeometryChangeEvent()'. Naming
    #  it makes this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::GeometryChangeEvent behind a cute one,
    #  and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate19GeometryChangeEventD1Ev')

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

    @overload(QWindow, QRect, QRect)
    @overload(NoneType, QRect, QRect)
    def __init__(
        self,
        window: Optional[QWindow],
        requestedGeometry: QRect,
        newGeometry: QRect,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QWindowSystemInterfacePrivate::GeometryChangeEvent::
      GeometryChangeEvent(QWindow *window, QRect requestedGeometry, QRect
      newGeometry)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-geometrychangeevent.html

      Parameters
      ----------

      window : Optional[QWindow]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      requestedGeometry : QRect
        Passed on as a value: Qt reads the C++ QRect, which stays Python's
        own.

      newGeometry : QRect
        Passed on as a value: Qt reads the C++ QRect, which stays Python's
        own.
      """
      #  QWindowSystemInterfacePrivate::GeometryChangeEvent::
      #      GeometryChangeEvent(QWindow *window, QRect requestedGeometry,
      #      QRect newGeometry)
      self._noteCreation(
          QWindowSystemInterfacePrivate.GeometryChangeEvent, lambda: Rituals.call(
              'ritual_ZN29QWindowSystemInterfacePrivate19GeometryChangeEven'
              'tC1EP7QWindow5QRectS3_',
              self._addressOf(window), self._valueOf(requestedGeometry),
              self._valueOf(newGeometry),
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

  class GestureEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWindowSystemInterfacePrivate::GestureEvent: a
    plain Python object standing in front of one C++
    QWindowSystemInterfacePrivate::GestureEvent.

    C++ hands a QWindowSystemInterfacePrivate::GestureEvent around as a copy,
    so every C++ QWindowSystemInterfacePrivate::GestureEvent behind a cute
    one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QWindowSystemInterfacePrivate::GestureEvent yet. It
    can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWindowSystemInterfacePrivate::GestureEvent::~GestureEvent()':
      the destructor: Python removes its C++
      QWindowSystemInterfacePrivate::GestureEvent by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::GestureEvent is created at the
      first use, not by 'QWindowSystemInterfacePrivate::GestureEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWindowSystemInterfacePrivate::GestureEvent back
      gives a copy the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::GestureEvent.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QPointF = WAIT['QPointF']
      QPointingDevice = WAIT['QPointingDevice']
      QWindow = WAIT['QWindow']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::GestureEvent'

    #  Qt's '~QWindowSystemInterfacePrivate::GestureEvent()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::GestureEvent behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate12GestureEventD1Ev')

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

    @overload(
        QWindow, int, Qt.NativeGestureType, QPointingDevice, int, QPointF,
        QPointF, float, QPointF,
    )
    @overload(
        QWindow, int, Qt.NativeGestureType, NoneType, int, QPointF, QPointF,
        float, QPointF,
    )
    @overload(
        NoneType, int, Qt.NativeGestureType, QPointingDevice, int, QPointF,
        QPointF, float, QPointF,
    )
    @overload(
        NoneType, int, Qt.NativeGestureType, NoneType, int, QPointF, QPointF,
        float, QPointF,
    )
    def __init__(
        self,
        window: Optional[QWindow],
        time: int,
        type: Qt.NativeGestureType,
        dev: Optional[QPointingDevice],
        fingerCount: int,
        pos: QPointF,
        globalPos: QPointF,
        realValue: float,
        delta: QPointF,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QWindowSystemInterfacePrivate::GestureEvent::GestureEvent(QWindow
      *window, ulong time, Qt::NativeGestureType type, const QPointingDevice
      *dev, int fingerCount, QPointF pos, QPointF globalPos, qreal realValue,
      QPointF delta)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-gestureevent.html

      Parameters
      ----------

      window : Optional[QWindow]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      time : int
        Passed on as it is.

      type : Qt.NativeGestureType
        Passed on as its number.

      dev : Optional[QPointingDevice]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      fingerCount : int
        Passed on as it is.

      pos : QPointF
        Passed on as a value: Qt reads the C++ QPointF, which stays Python's
        own.

      globalPos : QPointF
        Passed on as a value: Qt reads the C++ QPointF, which stays Python's
        own.

      realValue : float
        Passed on as it is.

      delta : QPointF
        Passed on as a value: Qt reads the C++ QPointF, which stays Python's
        own.
      """
      #  QWindowSystemInterfacePrivate::GestureEvent::GestureEvent(QWindow
      #      *window, ulong time, Qt::NativeGestureType type, const
      #      QPointingDevice *dev, int fingerCount, QPointF pos, QPointF
      #      globalPos, qreal realValue, QPointF delta)
      self._noteCreation(
          QWindowSystemInterfacePrivate.GestureEvent, lambda: Rituals.call(
              'ritual_ZN29QWindowSystemInterfacePrivate12GestureEventC1EP7Q'
              'WindowmN2Qt17NativeGestureTypeEPK15QPointingDevicei7QPointFS'
              '8_dS8_',
              self._addressOf(window), time, type.value,
              self._addressOf(dev), fingerCount, self._valueOf(pos,
              'QPointF'), self._valueOf(globalPos, 'QPointF'), realValue,
              self._valueOf(delta, 'QPointF'),
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

  class InputEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWindowSystemInterfacePrivate::InputEvent: a plain
    Python object standing in front of one C++
    QWindowSystemInterfacePrivate::InputEvent.

    C++ hands a QWindowSystemInterfacePrivate::InputEvent around as a copy,
    so every C++ QWindowSystemInterfacePrivate::InputEvent behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QWindowSystemInterfacePrivate::InputEvent yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWindowSystemInterfacePrivate::InputEvent::InputEvent(QWindow *w,
      ulong time, EventType t, Qt::KeyboardModifiers mods, const QInputDevice
      *dev)': names the enum 'QWindowSystemInterfacePrivate::EventType',
      whose class cannot be named here.
    - Qt's 'QWindowSystemInterfacePrivate::InputEvent::~InputEvent()': the
      destructor: Python removes its C++
      QWindowSystemInterfacePrivate::InputEvent by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::InputEvent is created at the
      first use, not by 'QWindowSystemInterfacePrivate::InputEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWindowSystemInterfacePrivate::InputEvent back
      gives a copy the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::InputEvent.
    - Each name of Qt's QWindowSystemInterfacePrivate::InputEvent that has no
      cute function yet, '__init__', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::InputEvent'

    #  Qt's '~QWindowSystemInterfacePrivate::InputEvent()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::InputEvent behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate10InputEventD1Ev')

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

    @staticmethod
    def __init__(*__, **_) -> Never:
      """
      Qt's 'QWindowSystemInterfacePrivate::InputEvent::InputEvent(QWindow *w,
      ulong time, EventType t, Qt::KeyboardModifiers mods, const QInputDevice
      *dev)': names the enum 'QWindowSystemInterfacePrivate::EventType',
      whose class cannot be named here.
      """
      raise NotImplementedError(
          "'QWindowSystemInterfacePrivate.InputEvent.__init__' has no cute "
          "function yet. Qt's "
          "'QWindowSystemInterfacePrivate::InputEvent::InputEvent(QWindow "
          "*w, ulong time, EventType t, Qt::KeyboardModifiers mods, const "
          "QInputDevice *dev)': names the enum "
          "'QWindowSystemInterfacePrivate::EventType', whose class cannot "
          "be named here.")

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

  class KeyEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWindowSystemInterfacePrivate::KeyEvent: a plain
    Python object standing in front of one C++
    QWindowSystemInterfacePrivate::KeyEvent.

    C++ hands a QWindowSystemInterfacePrivate::KeyEvent around as a copy, so
    every C++ QWindowSystemInterfacePrivate::KeyEvent behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QWindowSystemInterfacePrivate::KeyEvent yet. It can
    be made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWindowSystemInterfacePrivate::KeyEvent::~KeyEvent()': the
      destructor: Python removes its C++
      QWindowSystemInterfacePrivate::KeyEvent by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::KeyEvent is created at the first
      use, not by 'QWindowSystemInterfacePrivate::KeyEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWindowSystemInterfacePrivate::KeyEvent back gives
      a copy the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::KeyEvent.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QInputDevice = WAIT['QInputDevice']
      QWindow = WAIT['QWindow']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::KeyEvent'

    #  Qt's '~QWindowSystemInterfacePrivate::KeyEvent()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::KeyEvent behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate8KeyEventD1Ev')

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

    @overload(QWindow, int, QEvent.Type, int, Qt.KeyboardModifiers)
    @overload(NoneType, int, QEvent.Type, int, Qt.KeyboardModifiers)
    @overload(QWindow, int, QEvent.Type, int, Qt.KeyboardModifiers, str)
    @overload(NoneType, int, QEvent.Type, int, Qt.KeyboardModifiers, str)
    @overload(
        QWindow, int, QEvent.Type, int, Qt.KeyboardModifiers, str, bool,
    )
    @overload(
        NoneType, int, QEvent.Type, int, Qt.KeyboardModifiers, str, bool,
    )
    @overload(
        QWindow, int, QEvent.Type, int, Qt.KeyboardModifiers, str, bool, int,
    )
    @overload(
        NoneType, int, QEvent.Type, int, Qt.KeyboardModifiers, str, bool,
        int,
    )
    @overload(
        QWindow, int, QEvent.Type, int, Qt.KeyboardModifiers, str, bool, int,
        QInputDevice,
    )
    @overload(
        QWindow, int, QEvent.Type, int, Qt.KeyboardModifiers, str, bool, int,
        NoneType,
    )
    @overload(
        NoneType, int, QEvent.Type, int, Qt.KeyboardModifiers, str, bool,
        int, QInputDevice,
    )
    @overload(
        NoneType, int, QEvent.Type, int, Qt.KeyboardModifiers, str, bool,
        int, NoneType,
    )
    def __init__(
        self,
        w: Optional[QWindow],
        time: int,
        t: QEvent.Type,
        k: int,
        mods: Qt.KeyboardModifiers,
        text: str = '',
        autorep: bool = False,
        count: int = 1,
        device: Optional[QInputDevice] = ...,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QWindowSystemInterfacePrivate::KeyEvent::KeyEvent(QWindow *w, ulong
      time, QEvent::Type t, int k, Qt::KeyboardModifiers mods, const QString
      &text, bool autorep, ushort count, const QInputDevice *device)', which
      is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-keyevent.html

      Parameters
      ----------

      w : Optional[QWindow]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      time : int
        Passed on as it is.

      t : QEvent.Type
        Passed on as its number.

      k : int
        Passed on as it is.

      mods : Qt.KeyboardModifiers
        Passed on as its number.

      text : str
        Passed on as it is: a QString is made of it for the call. May be left
        out, as in Qt: it is then ''.

      autorep : bool
        Passed on as it is. May be left out, as in Qt: it is then False.

      count : int
        Passed on as it is. May be left out, as in Qt: it is then 1.

      device : Optional[QInputDevice]
        Passed on as the address of its C++ object. None is passed on as no
        object. May be left out, as in Qt: what
        'QInputDevice.primaryKeyboard()' gives is then passed on.
      """
      #  QWindowSystemInterfacePrivate::KeyEvent::KeyEvent(QWindow *w, ulong
      #      time, QEvent::Type t, int k, Qt::KeyboardModifiers mods, const
      #      QString &text, bool autorep, ushort count, const QInputDevice
      #      *device)
      if device is ...:
        from . import QInputDevice
        device = QInputDevice.primaryKeyboard()
      self._noteCreation(
          QWindowSystemInterfacePrivate.KeyEvent, lambda: Rituals.call(
              'ritual_ZN29QWindowSystemInterfacePrivate8KeyEventC1EP7QWindo'
              'wmN6QEvent4TypeEi6QFlagsIN2Qt16KeyboardModifierEERK7QStringb'
              'tPK12QInputDevice',
              self._addressOf(w), time, t.value, k, mods.value, text,
              autorep, count, self._addressOf(device),
          ))

    @overload(
        QWindow, int, QEvent.Type, int, Qt.KeyboardModifiers, int, int, int,
    )
    @overload(
        NoneType, int, QEvent.Type, int, Qt.KeyboardModifiers, int, int, int,
    )
    @overload(
        QWindow, int, QEvent.Type, int, Qt.KeyboardModifiers, int, int, int,
        str,
    )
    @overload(
        NoneType, int, QEvent.Type, int, Qt.KeyboardModifiers, int, int, int,
        str,
    )
    @overload(
        QWindow, int, QEvent.Type, int, Qt.KeyboardModifiers, int, int, int,
        str, bool,
    )
    @overload(
        NoneType, int, QEvent.Type, int, Qt.KeyboardModifiers, int, int, int,
        str, bool,
    )
    @overload(
        QWindow, int, QEvent.Type, int, Qt.KeyboardModifiers, int, int, int,
        str, bool, int,
    )
    @overload(
        NoneType, int, QEvent.Type, int, Qt.KeyboardModifiers, int, int, int,
        str, bool, int,
    )
    @overload(
        QWindow, int, QEvent.Type, int, Qt.KeyboardModifiers, int, int, int,
        str, bool, int, QInputDevice,
    )
    @overload(
        QWindow, int, QEvent.Type, int, Qt.KeyboardModifiers, int, int, int,
        str, bool, int, NoneType,
    )
    @overload(
        NoneType, int, QEvent.Type, int, Qt.KeyboardModifiers, int, int, int,
        str, bool, int, QInputDevice,
    )
    @overload(
        NoneType, int, QEvent.Type, int, Qt.KeyboardModifiers, int, int, int,
        str, bool, int, NoneType,
    )
    def __init__(
        self,
        w: Optional[QWindow],
        time: int,
        t: QEvent.Type,
        k: int,
        mods: Qt.KeyboardModifiers,
        nativeSC: int,
        nativeVK: int,
        nativeMods: int,
        text: str = '',
        autorep: bool = False,
        count: int = 1,
        device: Optional[QInputDevice] = ...,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QWindowSystemInterfacePrivate::KeyEvent::KeyEvent(QWindow *w, ulong
      time, QEvent::Type t, int k, Qt::KeyboardModifiers mods, quint32
      nativeSC, quint32 nativeVK, quint32 nativeMods, const QString &text,
      bool autorep, ushort count, const QInputDevice *device)', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-keyevent.html

      Parameters
      ----------

      w : Optional[QWindow]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      time : int
        Passed on as it is.

      t : QEvent.Type
        Passed on as its number.

      k : int
        Passed on as it is.

      mods : Qt.KeyboardModifiers
        Passed on as its number.

      nativeSC : int
        Passed on as it is.

      nativeVK : int
        Passed on as it is.

      nativeMods : int
        Passed on as it is.

      text : str
        Passed on as it is: a QString is made of it for the call. May be left
        out, as in Qt: it is then ''.

      autorep : bool
        Passed on as it is. May be left out, as in Qt: it is then False.

      count : int
        Passed on as it is. May be left out, as in Qt: it is then 1.

      device : Optional[QInputDevice]
        Passed on as the address of its C++ object. None is passed on as no
        object. May be left out, as in Qt: what
        'QInputDevice.primaryKeyboard()' gives is then passed on.
      """
      #  QWindowSystemInterfacePrivate::KeyEvent::KeyEvent(QWindow *w, ulong
      #      time, QEvent::Type t, int k, Qt::KeyboardModifiers mods, quint32
      #      nativeSC, quint32 nativeVK, quint32 nativeMods, const QString
      #      &text, bool autorep, ushort count, const QInputDevice *device)
      if device is ...:
        from . import QInputDevice
        device = QInputDevice.primaryKeyboard()
      self._noteCreation(
          QWindowSystemInterfacePrivate.KeyEvent, lambda: Rituals.call(
              'ritual_ZN29QWindowSystemInterfacePrivate8KeyEventC1EP7QWindo'
              'wmN6QEvent4TypeEi6QFlagsIN2Qt16KeyboardModifierEEjjjRK7QStri'
              'ngbtPK12QInputDevice',
              self._addressOf(w), time, t.value, k, mods.value, nativeSC,
              nativeVK, nativeMods, text, autorep, count,
              self._addressOf(device),
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

  class LeaveEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWindowSystemInterfacePrivate::LeaveEvent: a plain
    Python object standing in front of one C++
    QWindowSystemInterfacePrivate::LeaveEvent.

    C++ hands a QWindowSystemInterfacePrivate::LeaveEvent around as a copy,
    so every C++ QWindowSystemInterfacePrivate::LeaveEvent behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QWindowSystemInterfacePrivate::LeaveEvent yet. It can
    be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWindowSystemInterfacePrivate::LeaveEvent::~LeaveEvent()': the
      destructor: Python removes its C++
      QWindowSystemInterfacePrivate::LeaveEvent by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::LeaveEvent is created at the
      first use, not by 'QWindowSystemInterfacePrivate::LeaveEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWindowSystemInterfacePrivate::LeaveEvent back
      gives a copy the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::LeaveEvent.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QWindow = WAIT['QWindow']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::LeaveEvent'

    #  Qt's '~QWindowSystemInterfacePrivate::LeaveEvent()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::LeaveEvent behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate10LeaveEventD1Ev')

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

    @overload(QWindow)
    @overload(NoneType)
    def __init__(self, leave: Optional[QWindow]) -> None:
      """
      Notes what was given, for Qt's
      'QWindowSystemInterfacePrivate::LeaveEvent::LeaveEvent(QWindow
      *leave)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-leaveevent.html

      Parameters
      ----------

      leave : Optional[QWindow]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  QWindowSystemInterfacePrivate::LeaveEvent::LeaveEvent(QWindow
      #      *leave)
      self._noteCreation(
          QWindowSystemInterfacePrivate.LeaveEvent, lambda: Rituals.call(
              'ritual_ZN29QWindowSystemInterfacePrivate10LeaveEventC1EP7QWi'
              'ndow',
              self._addressOf(leave),
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

  class MouseEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWindowSystemInterfacePrivate::MouseEvent: a plain
    Python object standing in front of one C++
    QWindowSystemInterfacePrivate::MouseEvent.

    C++ hands a QWindowSystemInterfacePrivate::MouseEvent around as a copy,
    so every C++ QWindowSystemInterfacePrivate::MouseEvent behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QWindowSystemInterfacePrivate::MouseEvent yet. It can
    be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWindowSystemInterfacePrivate::MouseEvent::~MouseEvent()': the
      destructor: Python removes its C++
      QWindowSystemInterfacePrivate::MouseEvent by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::MouseEvent is created at the
      first use, not by 'QWindowSystemInterfacePrivate::MouseEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWindowSystemInterfacePrivate::MouseEvent back
      gives a copy the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::MouseEvent.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QPointF = WAIT['QPointF']
      QPointingDevice = WAIT['QPointingDevice']
      QWindow = WAIT['QWindow']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::MouseEvent'

    #  Qt's '~QWindowSystemInterfacePrivate::MouseEvent()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::MouseEvent behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate10MouseEventD1Ev')

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

    @overload(
        QWindow, int, QPointF, QPointF, Qt.MouseButtons,
        Qt.KeyboardModifiers, Qt.MouseButton, QEvent.Type,
    )
    @overload(
        NoneType, int, QPointF, QPointF, Qt.MouseButtons,
        Qt.KeyboardModifiers, Qt.MouseButton, QEvent.Type,
    )
    @overload(
        QWindow, int, QPointF, QPointF, Qt.MouseButtons,
        Qt.KeyboardModifiers, Qt.MouseButton, QEvent.Type,
        Qt.MouseEventSource,
    )
    @overload(
        NoneType, int, QPointF, QPointF, Qt.MouseButtons,
        Qt.KeyboardModifiers, Qt.MouseButton, QEvent.Type,
        Qt.MouseEventSource,
    )
    @overload(
        QWindow, int, QPointF, QPointF, Qt.MouseButtons,
        Qt.KeyboardModifiers, Qt.MouseButton, QEvent.Type,
        Qt.MouseEventSource, bool,
    )
    @overload(
        NoneType, int, QPointF, QPointF, Qt.MouseButtons,
        Qt.KeyboardModifiers, Qt.MouseButton, QEvent.Type,
        Qt.MouseEventSource, bool,
    )
    @overload(
        QWindow, int, QPointF, QPointF, Qt.MouseButtons,
        Qt.KeyboardModifiers, Qt.MouseButton, QEvent.Type,
        Qt.MouseEventSource, bool, QPointingDevice,
    )
    @overload(
        QWindow, int, QPointF, QPointF, Qt.MouseButtons,
        Qt.KeyboardModifiers, Qt.MouseButton, QEvent.Type,
        Qt.MouseEventSource, bool, NoneType,
    )
    @overload(
        NoneType, int, QPointF, QPointF, Qt.MouseButtons,
        Qt.KeyboardModifiers, Qt.MouseButton, QEvent.Type,
        Qt.MouseEventSource, bool, QPointingDevice,
    )
    @overload(
        NoneType, int, QPointF, QPointF, Qt.MouseButtons,
        Qt.KeyboardModifiers, Qt.MouseButton, QEvent.Type,
        Qt.MouseEventSource, bool, NoneType,
    )
    @overload(
        QWindow, int, QPointF, QPointF, Qt.MouseButtons,
        Qt.KeyboardModifiers, Qt.MouseButton, QEvent.Type,
        Qt.MouseEventSource, bool, QPointingDevice, int,
    )
    @overload(
        QWindow, int, QPointF, QPointF, Qt.MouseButtons,
        Qt.KeyboardModifiers, Qt.MouseButton, QEvent.Type,
        Qt.MouseEventSource, bool, NoneType, int,
    )
    @overload(
        NoneType, int, QPointF, QPointF, Qt.MouseButtons,
        Qt.KeyboardModifiers, Qt.MouseButton, QEvent.Type,
        Qt.MouseEventSource, bool, QPointingDevice, int,
    )
    @overload(
        NoneType, int, QPointF, QPointF, Qt.MouseButtons,
        Qt.KeyboardModifiers, Qt.MouseButton, QEvent.Type,
        Qt.MouseEventSource, bool, NoneType, int,
    )
    def __init__(
        self,
        w: Optional[QWindow],
        time: int,
        local: QPointF,
        global_: QPointF,
        state: Qt.MouseButtons,
        mods: Qt.KeyboardModifiers,
        b: Qt.MouseButton,
        type: QEvent.Type,
        src: Qt.MouseEventSource = (
            Qt.MouseEventSource.MouseEventNotSynthesized),
        frame: bool = False,
        device: Optional[QPointingDevice] = ...,
        evPtId: int = -1,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QWindowSystemInterfacePrivate::MouseEvent::MouseEvent(QWindow *w,
      ulong time, const QPointF &local, const QPointF &global,
      Qt::MouseButtons state, Qt::KeyboardModifiers mods, Qt::MouseButton b,
      QEvent::Type type, Qt::MouseEventSource src, bool frame, const
      QPointingDevice *device, int evPtId)', which is called at the first
      use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-mouseevent.html

      Parameters
      ----------

      w : Optional[QWindow]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      time : int
        Passed on as it is.

      local : QPointF
        Passed on as a value: Qt reads the C++ QPointF, which stays Python's
        own.

      global_ : QPointF
        Passed on as a value: Qt reads the C++ QPointF, which stays Python's
        own.

      state : Qt.MouseButtons
        Passed on as its number.

      mods : Qt.KeyboardModifiers
        Passed on as its number.

      b : Qt.MouseButton
        Passed on as its number.

      type : QEvent.Type
        Passed on as its number.

      src : Qt.MouseEventSource
        Passed on as its number. May be left out, as in Qt: it is then
        Qt.MouseEventSource.MouseEventNotSynthesized.

      frame : bool
        Passed on as it is. May be left out, as in Qt: it is then False.

      device : Optional[QPointingDevice]
        Passed on as the address of its C++ object. None is passed on as no
        object. May be left out, as in Qt: what
        'QPointingDevice.primaryPointingDevice()' gives is then passed on.

      evPtId : int
        Passed on as it is. May be left out, as in Qt: it is then -1.
      """
      #  QWindowSystemInterfacePrivate::MouseEvent::MouseEvent(QWindow *w,
      #      ulong time, const QPointF &local, const QPointF &global,
      #      Qt::MouseButtons state, Qt::KeyboardModifiers mods,
      #      Qt::MouseButton b, QEvent::Type type, Qt::MouseEventSource src,
      #      bool frame, const QPointingDevice *device, int evPtId)
      if device is ...:
        from . import QPointingDevice
        device = QPointingDevice.primaryPointingDevice()
      self._noteCreation(
          QWindowSystemInterfacePrivate.MouseEvent, lambda: Rituals.call(
              'ritual_ZN29QWindowSystemInterfacePrivate10MouseEventC1EP7QWi'
              'ndowmRK7QPointFS5_6QFlagsIN2Qt11MouseButtonEES6_INS7_16Keybo'
              'ardModifierEES8_N6QEvent4TypeENS7_16MouseEventSourceEbPK15QP'
              'ointingDevicei',
              self._addressOf(w), time, self._valueOf(local, 'QPointF'),
              self._valueOf(global_, 'QPointF'), state.value, mods.value,
              b.value, type.value, src.value, frame, self._addressOf(device),
              evPtId,
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

  class PaintEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWindowSystemInterfacePrivate::PaintEvent: a plain
    Python object standing in front of one C++
    QWindowSystemInterfacePrivate::PaintEvent.

    C++ hands a QWindowSystemInterfacePrivate::PaintEvent around as a copy,
    so every C++ QWindowSystemInterfacePrivate::PaintEvent behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QWindowSystemInterfacePrivate::PaintEvent yet. It can
    be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWindowSystemInterfacePrivate::PaintEvent::~PaintEvent()': the
      destructor: Python removes its C++
      QWindowSystemInterfacePrivate::PaintEvent by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::PaintEvent is created at the
      first use, not by 'QWindowSystemInterfacePrivate::PaintEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWindowSystemInterfacePrivate::PaintEvent back
      gives a copy the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::PaintEvent.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QRegion = WAIT['QRegion']
      QWindow = WAIT['QWindow']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::PaintEvent'

    #  Qt's '~QWindowSystemInterfacePrivate::PaintEvent()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::PaintEvent behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate10PaintEventD1Ev')

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

    @overload(QWindow, QRegion)
    @overload(NoneType, QRegion)
    def __init__(self, window: Optional[QWindow], region: QRegion) -> None:
      """
      Notes what was given, for Qt's
      'QWindowSystemInterfacePrivate::PaintEvent::PaintEvent(QWindow *window,
      const QRegion &region)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-paintevent.html

      Parameters
      ----------

      window : Optional[QWindow]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      region : QRegion
        Passed on as a value: Qt reads the C++ QRegion, which stays Python's
        own.
      """
      #  QWindowSystemInterfacePrivate::PaintEvent::PaintEvent(QWindow
      #      *window, const QRegion &region)
      self._noteCreation(
          QWindowSystemInterfacePrivate.PaintEvent, lambda: Rituals.call(
              'ritual_ZN29QWindowSystemInterfacePrivate10PaintEventC1EP7QWi'
              'ndowRK7QRegion',
              self._addressOf(window), self._valueOf(region),
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

  class PlatformPanelEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWindowSystemInterfacePrivate::PlatformPanelEvent:
    a plain Python object standing in front of one C++
    QWindowSystemInterfacePrivate::PlatformPanelEvent.

    C++ hands a QWindowSystemInterfacePrivate::PlatformPanelEvent around as a
    copy, so every C++ QWindowSystemInterfacePrivate::PlatformPanelEvent
    behind a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QWindowSystemInterfacePrivate::PlatformPanelEvent
    yet. It can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWindowSystemInterfacePrivate::PlatformPanelEvent::
      ~PlatformPanelEvent()': the destructor: Python removes its C++
      QWindowSystemInterfacePrivate::PlatformPanelEvent by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::PlatformPanelEvent is created at
      the first use, not by
      'QWindowSystemInterfacePrivate::PlatformPanelEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWindowSystemInterfacePrivate::PlatformPanelEvent
      back gives a copy the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::PlatformPanelEvent.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QWindow = WAIT['QWindow']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::PlatformPanelEvent'

    #  Qt's '~QWindowSystemInterfacePrivate::PlatformPanelEvent()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::PlatformPanelEvent behind a cute one,
    #  and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate18PlatformPanelEventD1Ev')

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

    @overload(QWindow)
    @overload(NoneType)
    def __init__(self, w: Optional[QWindow]) -> None:
      """
      Notes what was given, for Qt's
      'QWindowSystemInterfacePrivate::PlatformPanelEvent::PlatformPanelEvent(
      QWindow *w)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-platformpanelevent.html

      Parameters
      ----------

      w : Optional[QWindow]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  QWindowSystemInterfacePrivate::PlatformPanelEvent::
      #      PlatformPanelEvent(QWindow *w)
      self._noteCreation(
          QWindowSystemInterfacePrivate.PlatformPanelEvent, lambda: Rituals.call(
              'ritual_ZN29QWindowSystemInterfacePrivate18PlatformPanelEvent'
              'C1EP7QWindow',
              self._addressOf(w),
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

  class PointerEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWindowSystemInterfacePrivate::PointerEvent: a
    plain Python object standing in front of one C++
    QWindowSystemInterfacePrivate::PointerEvent.

    C++ hands a QWindowSystemInterfacePrivate::PointerEvent around as a copy,
    so every C++ QWindowSystemInterfacePrivate::PointerEvent behind a cute
    one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QWindowSystemInterfacePrivate::PointerEvent yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWindowSystemInterfacePrivate::PointerEvent::PointerEvent(QWindow
      *w, ulong time, EventType t, Qt::KeyboardModifiers mods, const
      QPointingDevice *device)': names the enum
      'QWindowSystemInterfacePrivate::EventType', whose class cannot be named
      here.
    - Qt's 'QWindowSystemInterfacePrivate::PointerEvent::~PointerEvent()':
      the destructor: Python removes its C++
      QWindowSystemInterfacePrivate::PointerEvent by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::PointerEvent is created at the
      first use, not by 'QWindowSystemInterfacePrivate::PointerEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWindowSystemInterfacePrivate::PointerEvent back
      gives a copy the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::PointerEvent.
    - Each name of Qt's QWindowSystemInterfacePrivate::PointerEvent that has
      no cute function yet, '__init__', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::PointerEvent'

    #  Qt's '~QWindowSystemInterfacePrivate::PointerEvent()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::PointerEvent behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate12PointerEventD1Ev')

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

    @staticmethod
    def __init__(*__, **_) -> Never:
      """
      Qt's 'QWindowSystemInterfacePrivate::PointerEvent::PointerEvent(QWindow
      *w, ulong time, EventType t, Qt::KeyboardModifiers mods, const
      QPointingDevice *device)': names the enum
      'QWindowSystemInterfacePrivate::EventType', whose class cannot be named
      here.
      """
      raise NotImplementedError(
          "'QWindowSystemInterfacePrivate.PointerEvent.__init__' has no "
          "cute function yet. Qt's "
          "'QWindowSystemInterfacePrivate::PointerEvent::PointerEvent(QWindo"
          "w *w, ulong time, EventType t, Qt::KeyboardModifiers mods, const "
          "QPointingDevice *device)': names the enum "
          "'QWindowSystemInterfacePrivate::EventType', whose class cannot "
          "be named here.")

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

  class SafeAreaMarginsChangedEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's
    QWindowSystemInterfacePrivate::SafeAreaMarginsChangedEvent: a plain
    Python object standing in front of one C++
    QWindowSystemInterfacePrivate::SafeAreaMarginsChangedEvent.

    C++ hands a QWindowSystemInterfacePrivate::SafeAreaMarginsChangedEvent
    around as a copy, so every C++
    QWindowSystemInterfacePrivate::SafeAreaMarginsChangedEvent behind a cute
    one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's
    QWindowSystemInterfacePrivate::SafeAreaMarginsChangedEvent yet. It can be
    made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWindowSystemInterfacePrivate::SafeAreaMarginsChangedEvent::
      ~SafeAreaMarginsChangedEvent()': the destructor: Python removes its C++
      QWindowSystemInterfacePrivate::SafeAreaMarginsChangedEvent by it, and
      has no other use for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::SafeAreaMarginsChangedEvent is
      created at the first use, not by
      'QWindowSystemInterfacePrivate::SafeAreaMarginsChangedEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a
      QWindowSystemInterfacePrivate::SafeAreaMarginsChangedEvent back gives a
      copy the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::SafeAreaMarginsChangedEvent.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QWindow = WAIT['QWindow']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::SafeAreaMarginsChangedEvent'

    #  Qt's '~QWindowSystemInterfacePrivate::SafeAreaMarginsChangedEvent()'.
    #  Naming it makes this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::SafeAreaMarginsChangedEvent behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate27SafeAreaMarginsChangedEventD1Ev')

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

    @overload(QWindow)
    @overload(NoneType)
    def __init__(self, w: Optional[QWindow]) -> None:
      """
      Notes what was given, for Qt's
      'QWindowSystemInterfacePrivate::SafeAreaMarginsChangedEvent::
      SafeAreaMarginsChangedEvent(QWindow *w)', which is called at the first
      use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-safeareamarginschangedevent.html

      Parameters
      ----------

      w : Optional[QWindow]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  QWindowSystemInterfacePrivate::SafeAreaMarginsChangedEvent::
      #      SafeAreaMarginsChangedEvent(QWindow *w)
      self._noteCreation(
          QWindowSystemInterfacePrivate.SafeAreaMarginsChangedEvent, lambda: Rituals.call(
              'ritual_ZN29QWindowSystemInterfacePrivate27SafeAreaMarginsCha'
              'ngedEventC1EP7QWindow',
              self._addressOf(w),
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

  class ScreenGeometryEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWindowSystemInterfacePrivate::ScreenGeometryEvent:
    a plain Python object standing in front of one C++
    QWindowSystemInterfacePrivate::ScreenGeometryEvent.

    C++ hands a QWindowSystemInterfacePrivate::ScreenGeometryEvent around as
    a copy, so every C++ QWindowSystemInterfacePrivate::ScreenGeometryEvent
    behind a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QWindowSystemInterfacePrivate::ScreenGeometryEvent
    yet. It can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWindowSystemInterfacePrivate::ScreenGeometryEvent::
      ~ScreenGeometryEvent()': the destructor: Python removes its C++
      QWindowSystemInterfacePrivate::ScreenGeometryEvent by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::ScreenGeometryEvent is created
      at the first use, not by
      'QWindowSystemInterfacePrivate::ScreenGeometryEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWindowSystemInterfacePrivate::ScreenGeometryEvent
      back gives a copy the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::ScreenGeometryEvent.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QRect = WAIT['QRect']
      QScreen = WAIT['QScreen']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::ScreenGeometryEvent'

    #  Qt's '~QWindowSystemInterfacePrivate::ScreenGeometryEvent()'. Naming
    #  it makes this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::ScreenGeometryEvent behind a cute one,
    #  and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate19ScreenGeometryEventD1Ev')

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

    @overload(QScreen, QRect, QRect)
    @overload(NoneType, QRect, QRect)
    def __init__(self, s: Optional[QScreen], g: QRect, ag: QRect) -> None:
      """
      Notes what was given, for Qt's
      'QWindowSystemInterfacePrivate::ScreenGeometryEvent::
      ScreenGeometryEvent(QScreen *s, const QRect &g, const QRect &ag)',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-screengeometryevent.html

      Parameters
      ----------

      s : Optional[QScreen]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      g : QRect
        Passed on as a value: Qt reads the C++ QRect, which stays Python's
        own.

      ag : QRect
        Passed on as a value: Qt reads the C++ QRect, which stays Python's
        own.
      """
      #  QWindowSystemInterfacePrivate::ScreenGeometryEvent::
      #      ScreenGeometryEvent(QScreen *s, const QRect &g, const QRect &ag)
      self._noteCreation(
          QWindowSystemInterfacePrivate.ScreenGeometryEvent, lambda: Rituals.call(
              'ritual_ZN29QWindowSystemInterfacePrivate19ScreenGeometryEven'
              'tC1EP7QScreenRK5QRectS5_',
              self._addressOf(s), self._valueOf(g), self._valueOf(ag),
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

  class ScreenLogicalDotsPerInchEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's
    QWindowSystemInterfacePrivate::ScreenLogicalDotsPerInchEvent: a plain
    Python object standing in front of one C++
    QWindowSystemInterfacePrivate::ScreenLogicalDotsPerInchEvent.

    C++ hands a QWindowSystemInterfacePrivate::ScreenLogicalDotsPerInchEvent
    around as a copy, so every C++
    QWindowSystemInterfacePrivate::ScreenLogicalDotsPerInchEvent behind a
    cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's
    QWindowSystemInterfacePrivate::ScreenLogicalDotsPerInchEvent yet. It can
    be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWindowSystemInterfacePrivate::ScreenLogicalDotsPerInchEvent::
      ~ScreenLogicalDotsPerInchEvent()': the destructor: Python removes its
      C++ QWindowSystemInterfacePrivate::ScreenLogicalDotsPerInchEvent by it,
      and has no other use for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::ScreenLogicalDotsPerInchEvent is
      created at the first use, not by
      'QWindowSystemInterfacePrivate::ScreenLogicalDotsPerInchEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a
      QWindowSystemInterfacePrivate::ScreenLogicalDotsPerInchEvent back gives
      a copy the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::ScreenLogicalDotsPerInchEvent.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QScreen = WAIT['QScreen']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::ScreenLogicalDotsPerInchEvent'

    #  Qt's
    #  '~QWindowSystemInterfacePrivate::ScreenLogicalDotsPerInchEvent()'.
    #  Naming it makes this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::ScreenLogicalDotsPerInchEvent behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate29ScreenLogicalDotsPerInchEventD1Ev')

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

    @overload(QScreen, float, float)
    @overload(NoneType, float, float)
    def __init__(self, s: Optional[QScreen], dx: float, dy: float) -> None:
      """
      Notes what was given, for Qt's
      'QWindowSystemInterfacePrivate::ScreenLogicalDotsPerInchEvent::
      ScreenLogicalDotsPerInchEvent(QScreen *s, qreal dx, qreal dy)', which
      is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-screenlogicaldotsperinchevent.html

      Parameters
      ----------

      s : Optional[QScreen]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      dx : float
        Passed on as it is.

      dy : float
        Passed on as it is.
      """
      #  QWindowSystemInterfacePrivate::ScreenLogicalDotsPerInchEvent::
      #      ScreenLogicalDotsPerInchEvent(QScreen *s, qreal dx, qreal dy)
      self._noteCreation(
          QWindowSystemInterfacePrivate.ScreenLogicalDotsPerInchEvent, lambda: Rituals.call(
              'ritual_ZN29QWindowSystemInterfacePrivate29ScreenLogicalDotsP'
              'erInchEventC1EP7QScreendd',
              self._addressOf(s), dx, dy,
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

  class ScreenOrientationEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's
    QWindowSystemInterfacePrivate::ScreenOrientationEvent: a plain Python
    object standing in front of one C++
    QWindowSystemInterfacePrivate::ScreenOrientationEvent.

    C++ hands a QWindowSystemInterfacePrivate::ScreenOrientationEvent around
    as a copy, so every C++
    QWindowSystemInterfacePrivate::ScreenOrientationEvent behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QWindowSystemInterfacePrivate::ScreenOrientationEvent
    yet. It can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWindowSystemInterfacePrivate::ScreenOrientationEvent::
      ~ScreenOrientationEvent()': the destructor: Python removes its C++
      QWindowSystemInterfacePrivate::ScreenOrientationEvent by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::ScreenOrientationEvent is
      created at the first use, not by
      'QWindowSystemInterfacePrivate::ScreenOrientationEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a
      QWindowSystemInterfacePrivate::ScreenOrientationEvent back gives a copy
      the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::ScreenOrientationEvent.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QScreen = WAIT['QScreen']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::ScreenOrientationEvent'

    #  Qt's '~QWindowSystemInterfacePrivate::ScreenOrientationEvent()'.
    #  Naming it makes this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::ScreenOrientationEvent behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate22ScreenOrientationEventD1Ev')

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

    @overload(QScreen, Qt.ScreenOrientation)
    @overload(NoneType, Qt.ScreenOrientation)
    def __init__(
        self,
        s: Optional[QScreen],
        o: Qt.ScreenOrientation,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QWindowSystemInterfacePrivate::ScreenOrientationEvent::
      ScreenOrientationEvent(QScreen *s, Qt::ScreenOrientation o)', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-screenorientationevent.html

      Parameters
      ----------

      s : Optional[QScreen]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      o : Qt.ScreenOrientation
        Passed on as its number.
      """
      #  QWindowSystemInterfacePrivate::ScreenOrientationEvent::
      #      ScreenOrientationEvent(QScreen *s, Qt::ScreenOrientation o)
      self._noteCreation(
          QWindowSystemInterfacePrivate.ScreenOrientationEvent, lambda: Rituals.call(
              'ritual_ZN29QWindowSystemInterfacePrivate22ScreenOrientationE'
              'ventC1EP7QScreenN2Qt17ScreenOrientationE',
              self._addressOf(s), o.value,
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

  class ScreenRefreshRateEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's
    QWindowSystemInterfacePrivate::ScreenRefreshRateEvent: a plain Python
    object standing in front of one C++
    QWindowSystemInterfacePrivate::ScreenRefreshRateEvent.

    C++ hands a QWindowSystemInterfacePrivate::ScreenRefreshRateEvent around
    as a copy, so every C++
    QWindowSystemInterfacePrivate::ScreenRefreshRateEvent behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QWindowSystemInterfacePrivate::ScreenRefreshRateEvent
    yet. It can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWindowSystemInterfacePrivate::ScreenRefreshRateEvent::
      ~ScreenRefreshRateEvent()': the destructor: Python removes its C++
      QWindowSystemInterfacePrivate::ScreenRefreshRateEvent by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::ScreenRefreshRateEvent is
      created at the first use, not by
      'QWindowSystemInterfacePrivate::ScreenRefreshRateEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a
      QWindowSystemInterfacePrivate::ScreenRefreshRateEvent back gives a copy
      the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::ScreenRefreshRateEvent.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QScreen = WAIT['QScreen']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::ScreenRefreshRateEvent'

    #  Qt's '~QWindowSystemInterfacePrivate::ScreenRefreshRateEvent()'.
    #  Naming it makes this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::ScreenRefreshRateEvent behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate22ScreenRefreshRateEventD1Ev')

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

    @overload(QScreen, float)
    @overload(NoneType, float)
    def __init__(self, s: Optional[QScreen], r: float) -> None:
      """
      Notes what was given, for Qt's
      'QWindowSystemInterfacePrivate::ScreenRefreshRateEvent::
      ScreenRefreshRateEvent(QScreen *s, qreal r)', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-screenrefreshrateevent.html

      Parameters
      ----------

      s : Optional[QScreen]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      r : float
        Passed on as it is.
      """
      #  QWindowSystemInterfacePrivate::ScreenRefreshRateEvent::
      #      ScreenRefreshRateEvent(QScreen *s, qreal r)
      self._noteCreation(
          QWindowSystemInterfacePrivate.ScreenRefreshRateEvent, lambda: Rituals.call(
              'ritual_ZN29QWindowSystemInterfacePrivate22ScreenRefreshRateE'
              'ventC1EP7QScreend',
              self._addressOf(s), r,
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

  class TabletEnterProximityEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's
    QWindowSystemInterfacePrivate::TabletEnterProximityEvent: a plain Python
    object standing in front of one C++
    QWindowSystemInterfacePrivate::TabletEnterProximityEvent.

    C++ hands a QWindowSystemInterfacePrivate::TabletEnterProximityEvent
    around as a copy, so every C++
    QWindowSystemInterfacePrivate::TabletEnterProximityEvent behind a cute
    one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's
    QWindowSystemInterfacePrivate::TabletEnterProximityEvent yet. It can be
    made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWindowSystemInterfacePrivate::TabletEnterProximityEvent::
      ~TabletEnterProximityEvent()': the destructor: Python removes its C++
      QWindowSystemInterfacePrivate::TabletEnterProximityEvent by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::TabletEnterProximityEvent is
      created at the first use, not by
      'QWindowSystemInterfacePrivate::TabletEnterProximityEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a
      QWindowSystemInterfacePrivate::TabletEnterProximityEvent back gives a
      copy the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::TabletEnterProximityEvent.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QPointF = WAIT['QPointF']
      QPointingDevice = WAIT['QPointingDevice']
      QWindow = WAIT['QWindow']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::TabletEnterProximityEvent'

    #  Qt's '~QWindowSystemInterfacePrivate::TabletEnterProximityEvent()'.
    #  Naming it makes this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::TabletEnterProximityEvent behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate25TabletEnterProximityEventD1Ev')

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

    @overload(
        QWindow, int, QPointF, QPointF, QPointingDevice, Qt.MouseButtons,
        float, float, float, float, float, Qt.KeyboardModifiers,
    )
    @overload(
        QWindow, int, QPointF, QPointF, NoneType, Qt.MouseButtons, float,
        float, float, float, float, Qt.KeyboardModifiers,
    )
    @overload(
        NoneType, int, QPointF, QPointF, QPointingDevice, Qt.MouseButtons,
        float, float, float, float, float, Qt.KeyboardModifiers,
    )
    @overload(
        NoneType, int, QPointF, QPointF, NoneType, Qt.MouseButtons, float,
        float, float, float, float, Qt.KeyboardModifiers,
    )
    def __init__(
        self,
        w: Optional[QWindow],
        time: int,
        local: QPointF,
        global_: QPointF,
        device: Optional[QPointingDevice],
        b: Qt.MouseButtons,
        xTilt: float,
        yTilt: float,
        tpressure: float,
        rotation: float,
        z: float,
        mods: Qt.KeyboardModifiers,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QWindowSystemInterfacePrivate::TabletEnterProximityEvent::
      TabletEnterProximityEvent(QWindow *w, ulong time, const QPointF &local,
      const QPointF &global, const QPointingDevice *device, Qt::MouseButtons
      b, qreal xTilt, qreal yTilt, qreal tpressure, qreal rotation, qreal z,
      Qt::KeyboardModifiers mods)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-tabletenterproximityevent.html

      Parameters
      ----------

      w : Optional[QWindow]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      time : int
        Passed on as it is.

      local : QPointF
        Passed on as a value: Qt reads the C++ QPointF, which stays Python's
        own.

      global_ : QPointF
        Passed on as a value: Qt reads the C++ QPointF, which stays Python's
        own.

      device : Optional[QPointingDevice]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      b : Qt.MouseButtons
        Passed on as its number.

      xTilt : float
        Passed on as it is.

      yTilt : float
        Passed on as it is.

      tpressure : float
        Passed on as it is.

      rotation : float
        Passed on as it is.

      z : float
        Passed on as it is.

      mods : Qt.KeyboardModifiers
        Passed on as its number.
      """
      #  QWindowSystemInterfacePrivate::TabletEnterProximityEvent::
      #      TabletEnterProximityEvent(QWindow *w, ulong time, const QPointF
      #      &local, const QPointF &global, const QPointingDevice *device,
      #      Qt::MouseButtons b, qreal xTilt, qreal yTilt, qreal tpressure,
      #      qreal rotation, qreal z, Qt::KeyboardModifiers mods)
      self._noteCreation(
          QWindowSystemInterfacePrivate.TabletEnterProximityEvent, lambda: Rituals.call(
              'ritual_ZN29QWindowSystemInterfacePrivate25TabletEnterProximi'
              'tyEventC1EP7QWindowmRK7QPointFS5_PK15QPointingDevice6QFlagsI'
              'N2Qt11MouseButtonEEdddddS9_INSA_16KeyboardModifierEE',
              self._addressOf(w), time, self._valueOf(local, 'QPointF'),
              self._valueOf(global_, 'QPointF'), self._addressOf(device),
              b.value, xTilt, yTilt, tpressure, rotation, z, mods.value,
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

  class TabletEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWindowSystemInterfacePrivate::TabletEvent: a plain
    Python object standing in front of one C++
    QWindowSystemInterfacePrivate::TabletEvent.

    C++ hands a QWindowSystemInterfacePrivate::TabletEvent around as a copy,
    so every C++ QWindowSystemInterfacePrivate::TabletEvent behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QWindowSystemInterfacePrivate::TabletEvent that
    has a ritual and that Python can call so far, 1 name in all:
    'setPlatformSynthesizesMouse'. It can be made from Python, in 1 way; see
    '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWindowSystemInterfacePrivate::TabletEvent::~TabletEvent()': the
      destructor: Python removes its C++
      QWindowSystemInterfacePrivate::TabletEvent by it, and has no other use
      for it.

    What has no ritual
    ------------------

    1 of the 4 functions Qt declares: 1 cannot be called and cannot be called
    through the meta-object and cannot be copied.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::TabletEvent is created at the
      first use, not by 'QWindowSystemInterfacePrivate::TabletEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWindowSystemInterfacePrivate::TabletEvent back
      gives a copy the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::TabletEvent.
    - Each name of Qt's QWindowSystemInterfacePrivate::TabletEvent that has
      no cute function yet, 'handleTabletEvent', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QPointF = WAIT['QPointF']
      QPointingDevice = WAIT['QPointingDevice']
      QWindow = WAIT['QWindow']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(bool)
    def setPlatformSynthesizesMouse(v: bool) -> None:
      """
      Calls Qt's 'void QWindowSystemInterfacePrivate::TabletEvent::
      setPlatformSynthesizesMouse(bool v)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-tabletevent.html

      Parameters
      ----------

      v : bool
        Passed on as it is.
      """
      #  void QWindowSystemInterfacePrivate::TabletEvent::
      #      setPlatformSynthesizesMouse(bool v)
      Rituals.call(
          'ritual_ZN29QWindowSystemInterfacePrivate11TabletEvent27setPlatfo'
          'rmSynthesizesMouseEb',
          v,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::TabletEvent'

    #  Qt's '~QWindowSystemInterfacePrivate::TabletEvent()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::TabletEvent behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate11TabletEventD1Ev')

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

    @overload(
        QWindow, int, QPointF, QPointF, QPointingDevice, Qt.MouseButtons,
        float, float, float, float, float, float, Qt.KeyboardModifiers,
    )
    @overload(
        QWindow, int, QPointF, QPointF, NoneType, Qt.MouseButtons, float,
        float, float, float, float, float, Qt.KeyboardModifiers,
    )
    @overload(
        NoneType, int, QPointF, QPointF, QPointingDevice, Qt.MouseButtons,
        float, float, float, float, float, float, Qt.KeyboardModifiers,
    )
    @overload(
        NoneType, int, QPointF, QPointF, NoneType, Qt.MouseButtons, float,
        float, float, float, float, float, Qt.KeyboardModifiers,
    )
    def __init__(
        self,
        w: Optional[QWindow],
        time: int,
        local: QPointF,
        global_: QPointF,
        device: Optional[QPointingDevice],
        b: Qt.MouseButtons,
        pressure: float,
        xTilt: float,
        yTilt: float,
        tpressure: float,
        rotation: float,
        z: float,
        mods: Qt.KeyboardModifiers,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QWindowSystemInterfacePrivate::TabletEvent::TabletEvent(QWindow *w,
      ulong time, const QPointF &local, const QPointF &global, const
      QPointingDevice *device, Qt::MouseButtons b, qreal pressure, qreal
      xTilt, qreal yTilt, qreal tpressure, qreal rotation, qreal z,
      Qt::KeyboardModifiers mods)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-tabletevent.html

      Parameters
      ----------

      w : Optional[QWindow]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      time : int
        Passed on as it is.

      local : QPointF
        Passed on as a value: Qt reads the C++ QPointF, which stays Python's
        own.

      global_ : QPointF
        Passed on as a value: Qt reads the C++ QPointF, which stays Python's
        own.

      device : Optional[QPointingDevice]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      b : Qt.MouseButtons
        Passed on as its number.

      pressure : float
        Passed on as it is.

      xTilt : float
        Passed on as it is.

      yTilt : float
        Passed on as it is.

      tpressure : float
        Passed on as it is.

      rotation : float
        Passed on as it is.

      z : float
        Passed on as it is.

      mods : Qt.KeyboardModifiers
        Passed on as its number.
      """
      #  QWindowSystemInterfacePrivate::TabletEvent::TabletEvent(QWindow *w,
      #      ulong time, const QPointF &local, const QPointF &global, const
      #      QPointingDevice *device, Qt::MouseButtons b, qreal pressure,
      #      qreal xTilt, qreal yTilt, qreal tpressure, qreal rotation, qreal
      #      z, Qt::KeyboardModifiers mods)
      self._noteCreation(
          QWindowSystemInterfacePrivate.TabletEvent, lambda: Rituals.call(
              'ritual_ZN29QWindowSystemInterfacePrivate11TabletEventC1EP7QW'
              'indowmRK7QPointFS5_PK15QPointingDevice6QFlagsIN2Qt11MouseBut'
              'tonEEddddddS9_INSA_16KeyboardModifierEE',
              self._addressOf(w), time, self._valueOf(local, 'QPointF'),
              self._valueOf(global_, 'QPointF'), self._addressOf(device),
              b.value, pressure, xTilt, yTilt, tpressure, rotation, z,
              mods.value,
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

    @staticmethod
    def handleTabletEvent(*__, **_) -> Never:
      """
      Qt's 'void
      QWindowSystemInterfacePrivate::TabletEvent::handleTabletEvent(QWindow
      *w, const QPointF &local, const QPointF &global, int device, int
      pointerType, Qt::MouseButtons buttons, qreal pressure, qreal xTilt,
      qreal yTilt, qreal tangentialPressure, qreal rotation, qreal z, qint64
      uid, Qt::KeyboardModifiers modifiers)': cannot be called and cannot be
      called through the meta-object and cannot be copied: no header file has
      its code, Qt's source does not mark it or its class for use from
      outside Qt or writes it 'inline' or nowhere, and it is no signal, slot
      or invokable function giving back nothing, of a class built on QObject,
      and Qt's source has no code for it that could be told from the rest.
      """
      raise NotImplementedError(
          "'QWindowSystemInterfacePrivate.TabletEvent.handleTabletEvent' "
          "has no cute function yet. Qt's 'void "
          "QWindowSystemInterfacePrivate::TabletEvent::handleTabletEvent(QWi"
          "ndow *w, const QPointF &local, const QPointF &global, int "
          "device, int pointerType, Qt::MouseButtons buttons, qreal "
          "pressure, qreal xTilt, qreal yTilt, qreal tangentialPressure, "
          "qreal rotation, qreal z, qint64 uid, Qt::KeyboardModifiers "
          "modifiers)': cannot be called and cannot be called through the "
          "meta-object and cannot be copied: no header file has its code, "
          "Qt's source does not mark it or its class for use from outside "
          "Qt or writes it 'inline' or nowhere, and it is no signal, slot "
          "or invokable function giving back nothing, of a class built on "
          "QObject, and Qt's source has no code for it that could be told "
          "from the rest.")

  class TabletLeaveProximityEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's
    QWindowSystemInterfacePrivate::TabletLeaveProximityEvent: a plain Python
    object standing in front of one C++
    QWindowSystemInterfacePrivate::TabletLeaveProximityEvent.

    C++ hands a QWindowSystemInterfacePrivate::TabletLeaveProximityEvent
    around as a copy, so every C++
    QWindowSystemInterfacePrivate::TabletLeaveProximityEvent behind a cute
    one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's
    QWindowSystemInterfacePrivate::TabletLeaveProximityEvent yet. It can be
    made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWindowSystemInterfacePrivate::TabletLeaveProximityEvent::
      ~TabletLeaveProximityEvent()': the destructor: Python removes its C++
      QWindowSystemInterfacePrivate::TabletLeaveProximityEvent by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::TabletLeaveProximityEvent is
      created at the first use, not by
      'QWindowSystemInterfacePrivate::TabletLeaveProximityEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a
      QWindowSystemInterfacePrivate::TabletLeaveProximityEvent back gives a
      copy the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::TabletLeaveProximityEvent.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QPointF = WAIT['QPointF']
      QPointingDevice = WAIT['QPointingDevice']
      QWindow = WAIT['QWindow']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::TabletLeaveProximityEvent'

    #  Qt's '~QWindowSystemInterfacePrivate::TabletLeaveProximityEvent()'.
    #  Naming it makes this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::TabletLeaveProximityEvent behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate25TabletLeaveProximityEventD1Ev')

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

    @overload(
        QWindow, int, QPointF, QPointF, QPointingDevice, Qt.MouseButtons,
        float, float, float, float, float, Qt.KeyboardModifiers,
    )
    @overload(
        QWindow, int, QPointF, QPointF, NoneType, Qt.MouseButtons, float,
        float, float, float, float, Qt.KeyboardModifiers,
    )
    @overload(
        NoneType, int, QPointF, QPointF, QPointingDevice, Qt.MouseButtons,
        float, float, float, float, float, Qt.KeyboardModifiers,
    )
    @overload(
        NoneType, int, QPointF, QPointF, NoneType, Qt.MouseButtons, float,
        float, float, float, float, Qt.KeyboardModifiers,
    )
    def __init__(
        self,
        w: Optional[QWindow],
        time: int,
        local: QPointF,
        global_: QPointF,
        device: Optional[QPointingDevice],
        b: Qt.MouseButtons,
        xTilt: float,
        yTilt: float,
        tpressure: float,
        rotation: float,
        z: float,
        mods: Qt.KeyboardModifiers,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QWindowSystemInterfacePrivate::TabletLeaveProximityEvent::
      TabletLeaveProximityEvent(QWindow *w, ulong time, const QPointF &local,
      const QPointF &global, const QPointingDevice *device, Qt::MouseButtons
      b, qreal xTilt, qreal yTilt, qreal tpressure, qreal rotation, qreal z,
      Qt::KeyboardModifiers mods)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-tabletleaveproximityevent.html

      Parameters
      ----------

      w : Optional[QWindow]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      time : int
        Passed on as it is.

      local : QPointF
        Passed on as a value: Qt reads the C++ QPointF, which stays Python's
        own.

      global_ : QPointF
        Passed on as a value: Qt reads the C++ QPointF, which stays Python's
        own.

      device : Optional[QPointingDevice]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      b : Qt.MouseButtons
        Passed on as its number.

      xTilt : float
        Passed on as it is.

      yTilt : float
        Passed on as it is.

      tpressure : float
        Passed on as it is.

      rotation : float
        Passed on as it is.

      z : float
        Passed on as it is.

      mods : Qt.KeyboardModifiers
        Passed on as its number.
      """
      #  QWindowSystemInterfacePrivate::TabletLeaveProximityEvent::
      #      TabletLeaveProximityEvent(QWindow *w, ulong time, const QPointF
      #      &local, const QPointF &global, const QPointingDevice *device,
      #      Qt::MouseButtons b, qreal xTilt, qreal yTilt, qreal tpressure,
      #      qreal rotation, qreal z, Qt::KeyboardModifiers mods)
      self._noteCreation(
          QWindowSystemInterfacePrivate.TabletLeaveProximityEvent, lambda: Rituals.call(
              'ritual_ZN29QWindowSystemInterfacePrivate25TabletLeaveProximi'
              'tyEventC1EP7QWindowmRK7QPointFS5_PK15QPointingDevice6QFlagsI'
              'N2Qt11MouseButtonEEdddddS9_INSA_16KeyboardModifierEE',
              self._addressOf(w), time, self._valueOf(local, 'QPointF'),
              self._valueOf(global_, 'QPointF'), self._addressOf(device),
              b.value, xTilt, yTilt, tpressure, rotation, z, mods.value,
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

  class ThemeChangeEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWindowSystemInterfacePrivate::ThemeChangeEvent: a
    plain Python object standing in front of one C++
    QWindowSystemInterfacePrivate::ThemeChangeEvent.

    C++ hands a QWindowSystemInterfacePrivate::ThemeChangeEvent around as a
    copy, so every C++ QWindowSystemInterfacePrivate::ThemeChangeEvent behind
    a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QWindowSystemInterfacePrivate::ThemeChangeEvent yet.
    It can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QWindowSystemInterfacePrivate::ThemeChangeEvent::~ThemeChangeEvent()':
      the destructor: Python removes its C++
      QWindowSystemInterfacePrivate::ThemeChangeEvent by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::ThemeChangeEvent is created at
      the first use, not by
      'QWindowSystemInterfacePrivate::ThemeChangeEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWindowSystemInterfacePrivate::ThemeChangeEvent
      back gives a copy the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::ThemeChangeEvent.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::ThemeChangeEvent'

    #  Qt's '~QWindowSystemInterfacePrivate::ThemeChangeEvent()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::ThemeChangeEvent behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate16ThemeChangeEventD1Ev')

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
      'QWindowSystemInterfacePrivate::ThemeChangeEvent::ThemeChangeEvent()',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-themechangeevent.html
      """
      #  QWindowSystemInterfacePrivate::ThemeChangeEvent::ThemeChangeEvent()
      self._noteCreation(
          QWindowSystemInterfacePrivate.ThemeChangeEvent, lambda: Rituals.call(
              'ritual_ZN29QWindowSystemInterfacePrivate16ThemeChangeEventC1'
              'Ev',
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

  class TouchEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWindowSystemInterfacePrivate::TouchEvent: a plain
    Python object standing in front of one C++
    QWindowSystemInterfacePrivate::TouchEvent.

    C++ hands a QWindowSystemInterfacePrivate::TouchEvent around as a copy,
    so every C++ QWindowSystemInterfacePrivate::TouchEvent behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QWindowSystemInterfacePrivate::TouchEvent yet. It can
    be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWindowSystemInterfacePrivate::TouchEvent::~TouchEvent()': the
      destructor: Python removes its C++
      QWindowSystemInterfacePrivate::TouchEvent by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::TouchEvent is created at the
      first use, not by 'QWindowSystemInterfacePrivate::TouchEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWindowSystemInterfacePrivate::TouchEvent back
      gives a copy the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::TouchEvent.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QEventPoint = WAIT['QEventPoint']
      QPointingDevice = WAIT['QPointingDevice']
      QWindow = WAIT['QWindow']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::TouchEvent'

    #  Qt's '~QWindowSystemInterfacePrivate::TouchEvent()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::TouchEvent behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate10TouchEventD1Ev')

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

    @overload(
        QWindow, int, QEvent.Type, QPointingDevice, QList[QEventPoint],
        Qt.KeyboardModifiers,
    )
    @overload(
        QWindow, int, QEvent.Type, NoneType, QList[QEventPoint],
        Qt.KeyboardModifiers,
    )
    @overload(
        NoneType, int, QEvent.Type, QPointingDevice, QList[QEventPoint],
        Qt.KeyboardModifiers,
    )
    @overload(
        NoneType, int, QEvent.Type, NoneType, QList[QEventPoint],
        Qt.KeyboardModifiers,
    )
    def __init__(
        self,
        w: Optional[QWindow],
        time: int,
        t: QEvent.Type,
        device: Optional[QPointingDevice],
        p: QList[QEventPoint],
        mods: Qt.KeyboardModifiers,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QWindowSystemInterfacePrivate::TouchEvent::TouchEvent(QWindow *w,
      ulong time, QEvent::Type t, const QPointingDevice *device, const
      QList<QEventPoint> &p, Qt::KeyboardModifiers mods)', which is called at
      the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-touchevent.html

      Parameters
      ----------

      w : Optional[QWindow]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      time : int
        Passed on as it is.

      t : QEvent.Type
        Passed on as its number.

      device : Optional[QPointingDevice]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      p : QList[QEventPoint]
        Passed on as a list of Qt: Qt reads the C++ list, which stays
        Python's own. A list or tuple of Python is made into one first, and
        refused when an element does not fit.

      mods : Qt.KeyboardModifiers
        Passed on as its number.
      """
      #  QWindowSystemInterfacePrivate::TouchEvent::TouchEvent(QWindow *w,
      #      ulong time, QEvent::Type t, const QPointingDevice *device, const
      #      QList<QEventPoint> &p, Qt::KeyboardModifiers mods)
      self._noteCreation(
          QWindowSystemInterfacePrivate.TouchEvent, lambda: Rituals.call(
              'ritual_ZN29QWindowSystemInterfacePrivate10TouchEventC1EP7QWi'
              'ndowmN6QEvent4TypeEPK15QPointingDeviceRK5QListI11QEventPoint'
              'E6QFlagsIN2Qt16KeyboardModifierEE',
              self._addressOf(w), time, t.value, self._addressOf(device),
              self._valueOf(p), mods.value,
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

  class UserEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWindowSystemInterfacePrivate::UserEvent: a plain
    Python object standing in front of one C++
    QWindowSystemInterfacePrivate::UserEvent.

    C++ hands a QWindowSystemInterfacePrivate::UserEvent around as a copy, so
    every C++ QWindowSystemInterfacePrivate::UserEvent behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QWindowSystemInterfacePrivate::UserEvent yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWindowSystemInterfacePrivate::UserEvent::UserEvent(QWindow *w,
      ulong time, EventType t)': names the enum
      'QWindowSystemInterfacePrivate::EventType', whose class cannot be named
      here.
    - Qt's 'QWindowSystemInterfacePrivate::UserEvent::~UserEvent()': the
      destructor: Python removes its C++
      QWindowSystemInterfacePrivate::UserEvent by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::UserEvent is created at the
      first use, not by 'QWindowSystemInterfacePrivate::UserEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWindowSystemInterfacePrivate::UserEvent back gives
      a copy the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::UserEvent.
    - Each name of Qt's QWindowSystemInterfacePrivate::UserEvent that has no
      cute function yet, '__init__', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::UserEvent'

    #  Qt's '~QWindowSystemInterfacePrivate::UserEvent()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::UserEvent behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate9UserEventD1Ev')

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

    @staticmethod
    def __init__(*__, **_) -> Never:
      """
      Qt's 'QWindowSystemInterfacePrivate::UserEvent::UserEvent(QWindow *w,
      ulong time, EventType t)': names the enum
      'QWindowSystemInterfacePrivate::EventType', whose class cannot be named
      here.
      """
      raise NotImplementedError(
          "'QWindowSystemInterfacePrivate.UserEvent.__init__' has no cute "
          "function yet. Qt's "
          "'QWindowSystemInterfacePrivate::UserEvent::UserEvent(QWindow *w, "
          "ulong time, EventType t)': names the enum "
          "'QWindowSystemInterfacePrivate::EventType', whose class cannot "
          "be named here.")

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

  class WheelEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWindowSystemInterfacePrivate::WheelEvent: a plain
    Python object standing in front of one C++
    QWindowSystemInterfacePrivate::WheelEvent.

    C++ hands a QWindowSystemInterfacePrivate::WheelEvent around as a copy,
    so every C++ QWindowSystemInterfacePrivate::WheelEvent behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QWindowSystemInterfacePrivate::WheelEvent yet. It can
    be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWindowSystemInterfacePrivate::WheelEvent::~WheelEvent()': the
      destructor: Python removes its C++
      QWindowSystemInterfacePrivate::WheelEvent by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::WheelEvent is created at the
      first use, not by 'QWindowSystemInterfacePrivate::WheelEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWindowSystemInterfacePrivate::WheelEvent back
      gives a copy the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::WheelEvent.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QPoint = WAIT['QPoint']
      QPointF = WAIT['QPointF']
      QPointingDevice = WAIT['QPointingDevice']
      QWindow = WAIT['QWindow']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::WheelEvent'

    #  Qt's '~QWindowSystemInterfacePrivate::WheelEvent()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::WheelEvent behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate10WheelEventD1Ev')

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

    @overload(
        QWindow, int, QPointF, QPointF, QPoint, QPoint, int, Qt.Orientation,
        Qt.KeyboardModifiers,
    )
    @overload(
        NoneType, int, QPointF, QPointF, QPoint, QPoint, int, Qt.Orientation,
        Qt.KeyboardModifiers,
    )
    @overload(
        QWindow, int, QPointF, QPointF, QPoint, QPoint, int, Qt.Orientation,
        Qt.KeyboardModifiers, Qt.ScrollPhase,
    )
    @overload(
        NoneType, int, QPointF, QPointF, QPoint, QPoint, int, Qt.Orientation,
        Qt.KeyboardModifiers, Qt.ScrollPhase,
    )
    @overload(
        QWindow, int, QPointF, QPointF, QPoint, QPoint, int, Qt.Orientation,
        Qt.KeyboardModifiers, Qt.ScrollPhase, Qt.MouseEventSource,
    )
    @overload(
        NoneType, int, QPointF, QPointF, QPoint, QPoint, int, Qt.Orientation,
        Qt.KeyboardModifiers, Qt.ScrollPhase, Qt.MouseEventSource,
    )
    @overload(
        QWindow, int, QPointF, QPointF, QPoint, QPoint, int, Qt.Orientation,
        Qt.KeyboardModifiers, Qt.ScrollPhase, Qt.MouseEventSource, bool,
    )
    @overload(
        NoneType, int, QPointF, QPointF, QPoint, QPoint, int, Qt.Orientation,
        Qt.KeyboardModifiers, Qt.ScrollPhase, Qt.MouseEventSource, bool,
    )
    @overload(
        QWindow, int, QPointF, QPointF, QPoint, QPoint, int, Qt.Orientation,
        Qt.KeyboardModifiers, Qt.ScrollPhase, Qt.MouseEventSource, bool,
        QPointingDevice,
    )
    @overload(
        QWindow, int, QPointF, QPointF, QPoint, QPoint, int, Qt.Orientation,
        Qt.KeyboardModifiers, Qt.ScrollPhase, Qt.MouseEventSource, bool,
        NoneType,
    )
    @overload(
        NoneType, int, QPointF, QPointF, QPoint, QPoint, int, Qt.Orientation,
        Qt.KeyboardModifiers, Qt.ScrollPhase, Qt.MouseEventSource, bool,
        QPointingDevice,
    )
    @overload(
        NoneType, int, QPointF, QPointF, QPoint, QPoint, int, Qt.Orientation,
        Qt.KeyboardModifiers, Qt.ScrollPhase, Qt.MouseEventSource, bool,
        NoneType,
    )
    def __init__(
        self,
        w: Optional[QWindow],
        time: int,
        local: QPointF,
        global_: QPointF,
        pixelD: QPoint,
        angleD: QPoint,
        qt4D: int,
        qt4O: Qt.Orientation,
        mods: Qt.KeyboardModifiers,
        phase: Qt.ScrollPhase = Qt.ScrollPhase.NoScrollPhase,
        src: Qt.MouseEventSource = (
            Qt.MouseEventSource.MouseEventNotSynthesized),
        inverted: bool = False,
        device: Optional[QPointingDevice] = ...,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QWindowSystemInterfacePrivate::WheelEvent::WheelEvent(QWindow *w,
      ulong time, const QPointF &local, const QPointF &global, QPoint pixelD,
      QPoint angleD, int qt4D, Qt::Orientation qt4O, Qt::KeyboardModifiers
      mods, Qt::ScrollPhase phase, Qt::MouseEventSource src, bool inverted,
      const QPointingDevice *device)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-wheelevent.html

      Parameters
      ----------

      w : Optional[QWindow]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      time : int
        Passed on as it is.

      local : QPointF
        Passed on as a value: Qt reads the C++ QPointF, which stays Python's
        own.

      global_ : QPointF
        Passed on as a value: Qt reads the C++ QPointF, which stays Python's
        own.

      pixelD : QPoint
        Passed on as a value: Qt reads the C++ QPoint, which stays Python's
        own.

      angleD : QPoint
        Passed on as a value: Qt reads the C++ QPoint, which stays Python's
        own.

      qt4D : int
        Passed on as it is.

      qt4O : Qt.Orientation
        Passed on as its number.

      mods : Qt.KeyboardModifiers
        Passed on as its number.

      phase : Qt.ScrollPhase
        Passed on as its number. May be left out, as in Qt: it is then
        Qt.ScrollPhase.NoScrollPhase.

      src : Qt.MouseEventSource
        Passed on as its number. May be left out, as in Qt: it is then
        Qt.MouseEventSource.MouseEventNotSynthesized.

      inverted : bool
        Passed on as it is. May be left out, as in Qt: it is then False.

      device : Optional[QPointingDevice]
        Passed on as the address of its C++ object. None is passed on as no
        object. May be left out, as in Qt: what
        'QPointingDevice.primaryPointingDevice()' gives is then passed on.
      """
      #  QWindowSystemInterfacePrivate::WheelEvent::WheelEvent(QWindow *w,
      #      ulong time, const QPointF &local, const QPointF &global, QPoint
      #      pixelD, QPoint angleD, int qt4D, Qt::Orientation qt4O,
      #      Qt::KeyboardModifiers mods, Qt::ScrollPhase phase,
      #      Qt::MouseEventSource src, bool inverted, const QPointingDevice
      #      *device)
      if device is ...:
        from . import QPointingDevice
        device = QPointingDevice.primaryPointingDevice()
      self._noteCreation(
          QWindowSystemInterfacePrivate.WheelEvent, lambda: Rituals.call(
              'ritual_ZN29QWindowSystemInterfacePrivate10WheelEventC1EP7QWi'
              'ndowmRK7QPointFS5_6QPointS6_iN2Qt11OrientationE6QFlagsINS7_1'
              '6KeyboardModifierEENS7_11ScrollPhaseENS7_16MouseEventSourceE'
              'bPK15QPointingDevice',
              self._addressOf(w), time, self._valueOf(local, 'QPointF'),
              self._valueOf(global_, 'QPointF'), self._valueOf(pixelD),
              self._valueOf(angleD), qt4D, qt4O.value, mods.value,
              phase.value, src.value, inverted, self._addressOf(device),
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

  class WindowDevicePixelRatioChangedEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's
    QWindowSystemInterfacePrivate::WindowDevicePixelRatioChangedEvent: a
    plain Python object standing in front of one C++
    QWindowSystemInterfacePrivate::WindowDevicePixelRatioChangedEvent.

    C++ hands a
    QWindowSystemInterfacePrivate::WindowDevicePixelRatioChangedEvent around
    as a copy, so every C++
    QWindowSystemInterfacePrivate::WindowDevicePixelRatioChangedEvent behind
    a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's
    QWindowSystemInterfacePrivate::WindowDevicePixelRatioChangedEvent yet. It
    can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QWindowSystemInterfacePrivate::WindowDevicePixelRatioChangedEvent::
      ~WindowDevicePixelRatioChangedEvent()': the destructor: Python removes
      its C++
      QWindowSystemInterfacePrivate::WindowDevicePixelRatioChangedEvent by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++
      QWindowSystemInterfacePrivate::WindowDevicePixelRatioChangedEvent is
      created at the first use, not by
      'QWindowSystemInterfacePrivate::WindowDevicePixelRatioChangedEvent(
      ...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a
      QWindowSystemInterfacePrivate::WindowDevicePixelRatioChangedEvent back
      gives a copy the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::WindowDevicePixelRatioChangedEvent.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QWindow = WAIT['QWindow']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::WindowDevicePixelRatioChangedEvent'

    #  Qt's
    #  '~QWindowSystemInterfacePrivate::WindowDevicePixelRatioChangedEvent()'.
    #  Naming it makes this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::WindowDevicePixelRatioChangedEvent
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate34WindowDevicePixelRatioChangedEventD1Ev')

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

    @overload(QWindow)
    @overload(NoneType)
    def __init__(self, w: Optional[QWindow]) -> None:
      """
      Notes what was given, for Qt's
      'QWindowSystemInterfacePrivate::WindowDevicePixelRatioChangedEvent::
      WindowDevicePixelRatioChangedEvent(QWindow *w)', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-windowdevicepixelratiochangedevent.html

      Parameters
      ----------

      w : Optional[QWindow]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  QWindowSystemInterfacePrivate::WindowDevicePixelRatioChangedEvent::
      #      WindowDevicePixelRatioChangedEvent(QWindow *w)
      self._noteCreation(
          QWindowSystemInterfacePrivate.WindowDevicePixelRatioChangedEvent, lambda: Rituals.call(
              'ritual_ZN29QWindowSystemInterfacePrivate34WindowDevicePixelR'
              'atioChangedEventC1EP7QWindow',
              self._addressOf(w),
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

  class WindowScreenChangedEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's
    QWindowSystemInterfacePrivate::WindowScreenChangedEvent: a plain Python
    object standing in front of one C++
    QWindowSystemInterfacePrivate::WindowScreenChangedEvent.

    C++ hands a QWindowSystemInterfacePrivate::WindowScreenChangedEvent
    around as a copy, so every C++
    QWindowSystemInterfacePrivate::WindowScreenChangedEvent behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's
    QWindowSystemInterfacePrivate::WindowScreenChangedEvent yet. It can be
    made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWindowSystemInterfacePrivate::WindowScreenChangedEvent::
      ~WindowScreenChangedEvent()': the destructor: Python removes its C++
      QWindowSystemInterfacePrivate::WindowScreenChangedEvent by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::WindowScreenChangedEvent is
      created at the first use, not by
      'QWindowSystemInterfacePrivate::WindowScreenChangedEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a
      QWindowSystemInterfacePrivate::WindowScreenChangedEvent back gives a
      copy the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::WindowScreenChangedEvent.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QScreen = WAIT['QScreen']
      QWindow = WAIT['QWindow']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::WindowScreenChangedEvent'

    #  Qt's '~QWindowSystemInterfacePrivate::WindowScreenChangedEvent()'.
    #  Naming it makes this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::WindowScreenChangedEvent behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate24WindowScreenChangedEventD1Ev')

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

    @overload(QWindow, QScreen)
    @overload(QWindow, NoneType)
    @overload(NoneType, QScreen)
    @overload(NoneType, NoneType)
    def __init__(self, w: Optional[QWindow], s: Optional[QScreen]) -> None:
      """
      Notes what was given, for Qt's
      'QWindowSystemInterfacePrivate::WindowScreenChangedEvent::
      WindowScreenChangedEvent(QWindow *w, QScreen *s)', which is called at
      the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-windowscreenchangedevent.html

      Parameters
      ----------

      w : Optional[QWindow]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      s : Optional[QScreen]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  QWindowSystemInterfacePrivate::WindowScreenChangedEvent::
      #      WindowScreenChangedEvent(QWindow *w, QScreen *s)
      self._noteCreation(
          QWindowSystemInterfacePrivate.WindowScreenChangedEvent, lambda: Rituals.call(
              'ritual_ZN29QWindowSystemInterfacePrivate24WindowScreenChange'
              'dEventC1EP7QWindowP7QScreen',
              self._addressOf(w), self._addressOf(s),
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

  class WindowStateChangedEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's
    QWindowSystemInterfacePrivate::WindowStateChangedEvent: a plain Python
    object standing in front of one C++
    QWindowSystemInterfacePrivate::WindowStateChangedEvent.

    C++ hands a QWindowSystemInterfacePrivate::WindowStateChangedEvent around
    as a copy, so every C++
    QWindowSystemInterfacePrivate::WindowStateChangedEvent behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's
    QWindowSystemInterfacePrivate::WindowStateChangedEvent yet. It can be
    made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWindowSystemInterfacePrivate::WindowStateChangedEvent::
      ~WindowStateChangedEvent()': the destructor: Python removes its C++
      QWindowSystemInterfacePrivate::WindowStateChangedEvent by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::WindowStateChangedEvent is
      created at the first use, not by
      'QWindowSystemInterfacePrivate::WindowStateChangedEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a
      QWindowSystemInterfacePrivate::WindowStateChangedEvent back gives a
      copy the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::WindowStateChangedEvent.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QWindow = WAIT['QWindow']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::WindowStateChangedEvent'

    #  Qt's '~QWindowSystemInterfacePrivate::WindowStateChangedEvent()'.
    #  Naming it makes this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::WindowStateChangedEvent behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate23WindowStateChangedEventD1Ev')

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

    @overload(QWindow, Qt.WindowStates, Qt.WindowStates)
    @overload(NoneType, Qt.WindowStates, Qt.WindowStates)
    def __init__(
        self,
        _window: Optional[QWindow],
        _newState: Qt.WindowStates,
        _oldState: Qt.WindowStates,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QWindowSystemInterfacePrivate::WindowStateChangedEvent::
      WindowStateChangedEvent(QWindow *_window, Qt::WindowStates _newState,
      Qt::WindowStates _oldState)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-windowstatechangedevent.html

      Parameters
      ----------

      _window : Optional[QWindow]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      _newState : Qt.WindowStates
        Passed on as its number.

      _oldState : Qt.WindowStates
        Passed on as its number.
      """
      #  QWindowSystemInterfacePrivate::WindowStateChangedEvent::
      #      WindowStateChangedEvent(QWindow *_window, Qt::WindowStates
      #      _newState, Qt::WindowStates _oldState)
      self._noteCreation(
          QWindowSystemInterfacePrivate.WindowStateChangedEvent, lambda: Rituals.call(
              'ritual_ZN29QWindowSystemInterfacePrivate23WindowStateChanged'
              'EventC1EP7QWindow6QFlagsIN2Qt11WindowStateEES6_',
              self._addressOf(_window), _newState.value, _oldState.value,
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

  class WindowSystemEvent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWindowSystemInterfacePrivate::WindowSystemEvent: a
    plain Python object standing in front of one C++
    QWindowSystemInterfacePrivate::WindowSystemEvent.

    C++ hands a QWindowSystemInterfacePrivate::WindowSystemEvent around as a
    copy, so every C++ QWindowSystemInterfacePrivate::WindowSystemEvent
    behind a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QWindowSystemInterfacePrivate::WindowSystemEvent
    that has a ritual and that Python can call so far, 2 names in all:
    'synthetic', 'nullWindow'. None can be made from Python: one comes out of
    a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QWindowSystemInterfacePrivate::WindowSystemEvent::WindowSystemEvent(
      EventType t)': names the enum
      'QWindowSystemInterfacePrivate::EventType', whose class cannot be named
      here.
    - Qt's
      'QWindowSystemInterfacePrivate::WindowSystemEvent::~WindowSystemEvent(
      )': the destructor: Python removes its C++
      QWindowSystemInterfacePrivate::WindowSystemEvent by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::WindowSystemEvent is created at
      the first use, not by
      'QWindowSystemInterfacePrivate::WindowSystemEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWindowSystemInterfacePrivate::WindowSystemEvent
      back gives a copy the ritual made for Python, in a new cute
      QWindowSystemInterfacePrivate::WindowSystemEvent.
    - Each name of Qt's QWindowSystemInterfacePrivate::WindowSystemEvent that
      has no cute function yet, '__init__', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::WindowSystemEvent'

    #  Qt's '~QWindowSystemInterfacePrivate::WindowSystemEvent()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QWindowSystemInterfacePrivate::WindowSystemEvent behind a cute one,
    #  and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QWindowSystemInterfacePrivate17WindowSystemEventD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def synthetic(self) -> bool:
      """
      Calls Qt's 'bool
      QWindowSystemInterfacePrivate::WindowSystemEvent::synthetic() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-windowsystemevent.html
      """
      #  bool QWindowSystemInterfacePrivate::WindowSystemEvent::synthetic()
      #      const
      return self.uglySide.call(
          'ritual_ZNK29QWindowSystemInterfacePrivate17WindowSystemEvent9syn'
          'theticEv',
      )

    def nullWindow(self) -> bool:
      """
      Calls Qt's 'bool
      QWindowSystemInterfacePrivate::WindowSystemEvent::nullWindow() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-windowsystemevent.html
      """
      #  bool QWindowSystemInterfacePrivate::WindowSystemEvent::nullWindow()
      #      const
      return self.uglySide.call(
          'ritual_ZNK29QWindowSystemInterfacePrivate17WindowSystemEvent10nu'
          'llWindowEv',
      )

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

    @staticmethod
    def __init__(*__, **_) -> Never:
      """
      Qt's
      'QWindowSystemInterfacePrivate::WindowSystemEvent::WindowSystemEvent(
      EventType t)': names the enum
      'QWindowSystemInterfacePrivate::EventType', whose class cannot be named
      here.
      """
      raise NotImplementedError(
          "'QWindowSystemInterfacePrivate.WindowSystemEvent.__init__' has "
          "no cute function yet. Qt's "
          "'QWindowSystemInterfacePrivate::WindowSystemEvent::WindowSystemEv"
          "ent(EventType t)': names the enum "
          "'QWindowSystemInterfacePrivate::EventType', whose class cannot "
          "be named here.")

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

  class WindowSystemEventList(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's
    QWindowSystemInterfacePrivate::WindowSystemEventList: a plain Python
    object standing in front of one C++
    QWindowSystemInterfacePrivate::WindowSystemEventList.

    What exists
    -----------

    Every function of Qt's
    QWindowSystemInterfacePrivate::WindowSystemEventList that has a ritual
    and that Python can call so far, 3 names in all: 'clear',
    'nonUserInputEventsQueued', 'count'. It can be made from Python, in 1
    way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWindowSystemInterfacePrivate::WindowSystemEventList::
      ~WindowSystemEventList()': the destructor: Python never removes a C++
      QWindowSystemInterfacePrivate::WindowSystemEventList.
    - Qt's 'void
      QWindowSystemInterfacePrivate::WindowSystemEventList::prepend(
      WindowSystemEvent *e)': names
      'QWindowSystemInterfacePrivate::WindowSystemEvent', which stands beside
      this class inside 'QWindowSystemInterfacePrivate' and cannot be named
      from here.
    - Qt's 'WindowSystemEvent
      *QWindowSystemInterfacePrivate::WindowSystemEventList::
      takeFirstOrReturnNull()': gives
      'QWindowSystemInterfacePrivate::WindowSystemEvent', which stands beside
      this class inside 'QWindowSystemInterfacePrivate' and cannot be named
      from here.
    - Qt's 'WindowSystemEvent
      *QWindowSystemInterfacePrivate::WindowSystemEventList::
      takeFirstNonUserInputOrReturnNull()': gives
      'QWindowSystemInterfacePrivate::WindowSystemEvent', which stands beside
      this class inside 'QWindowSystemInterfacePrivate' and cannot be named
      from here.
    - Qt's 'void
      QWindowSystemInterfacePrivate::WindowSystemEventList::append(
      WindowSystemEvent *e)': names
      'QWindowSystemInterfacePrivate::WindowSystemEvent', which stands beside
      this class inside 'QWindowSystemInterfacePrivate' and cannot be named
      from here.
    - Qt's 'WindowSystemEvent
      *QWindowSystemInterfacePrivate::WindowSystemEventList::
      peekAtFirstOfType(EventType t) const': names the enum
      'QWindowSystemInterfacePrivate::EventType', whose class cannot be named
      here.
    - Qt's 'void
      QWindowSystemInterfacePrivate::WindowSystemEventList::remove(const
      WindowSystemEvent *e)': names
      'QWindowSystemInterfacePrivate::WindowSystemEvent', which stands beside
      this class inside 'QWindowSystemInterfacePrivate' and cannot be named
      from here.

    What has no ritual
    ------------------

    4 of the 15 functions Qt declares: 4 forbidden.

    What to expect
    --------------

    - The C++ QWindowSystemInterfacePrivate::WindowSystemEventList is created
      at the first use, not by
      'QWindowSystemInterfacePrivate::WindowSystemEventList(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++
      QWindowSystemInterfacePrivate::WindowSystemEventList.
    - Each name of Qt's QWindowSystemInterfacePrivate::WindowSystemEventList
      that has no cute function yet, 'append', 'peekAtFirstOfType',
      'prepend', 'remove', 'takeFirstNonUserInputOrReturnNull',
      'takeFirstOrReturnNull', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterfacePrivate::WindowSystemEventList'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def count(self) -> int:
      """
      Calls Qt's 'qsizetype
      QWindowSystemInterfacePrivate::WindowSystemEventList::count() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-windowsystemeventlist.html
      """
      #  qsizetype
      #      QWindowSystemInterfacePrivate::WindowSystemEventList::count()
      #      const
      return self.uglySide.call(
          'ritual_ZNK29QWindowSystemInterfacePrivate21WindowSystemEventList'
          '5countEv',
      )

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
      'QWindowSystemInterfacePrivate::WindowSystemEventList::
      WindowSystemEventList()', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-windowsystemeventlist.html
      """
      #  QWindowSystemInterfacePrivate::WindowSystemEventList::
      #      WindowSystemEventList()
      self._noteCreation(
          QWindowSystemInterfacePrivate.WindowSystemEventList, lambda: Rituals.call(
              'ritual_ZN29QWindowSystemInterfacePrivate21WindowSystemEventL'
              'istC1Ev',
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

    def clear(self) -> None:
      """
      Calls Qt's 'void
      QWindowSystemInterfacePrivate::WindowSystemEventList::clear()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-windowsystemeventlist.html
      """
      #  void QWindowSystemInterfacePrivate::WindowSystemEventList::clear()
      self.uglySide.call(
          'ritual_ZN29QWindowSystemInterfacePrivate21WindowSystemEventList5'
          'clearEv',
      )

    def nonUserInputEventsQueued(self) -> bool:
      """
      Calls Qt's 'bool QWindowSystemInterfacePrivate::WindowSystemEventList::
      nonUserInputEventsQueued()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate-windowsystemeventlist.html
      """
      #  bool QWindowSystemInterfacePrivate::WindowSystemEventList::
      #      nonUserInputEventsQueued()
      return self.uglySide.call(
          'ritual_ZN29QWindowSystemInterfacePrivate21WindowSystemEventList2'
          '4nonUserInputEventsQueuedEv',
      )

    @staticmethod
    def append(*__, **_) -> Never:
      """
      Qt's 'void
      QWindowSystemInterfacePrivate::WindowSystemEventList::append(
      WindowSystemEvent *e)': names
      'QWindowSystemInterfacePrivate::WindowSystemEvent', which stands beside
      this class inside 'QWindowSystemInterfacePrivate' and cannot be named
      from here.
      """
      raise NotImplementedError(
          "'QWindowSystemInterfacePrivate.WindowSystemEventList.append' has "
          "no cute function yet. Qt's 'void "
          "QWindowSystemInterfacePrivate::WindowSystemEventList::append(Wind"
          "owSystemEvent *e)': names "
          "'QWindowSystemInterfacePrivate::WindowSystemEvent', which stands "
          "beside this class inside 'QWindowSystemInterfacePrivate' and "
          "cannot be named from here.")

    @staticmethod
    def peekAtFirstOfType(*__, **_) -> Never:
      """
      Qt's 'WindowSystemEvent
      *QWindowSystemInterfacePrivate::WindowSystemEventList::
      peekAtFirstOfType(EventType t) const': names the enum
      'QWindowSystemInterfacePrivate::EventType', whose class cannot be named
      here.
      """
      raise NotImplementedError(
          "'QWindowSystemInterfacePrivate.WindowSystemEventList.peekAtFirstO"
          "fType' has no cute function yet. Qt's 'WindowSystemEvent "
          "*QWindowSystemInterfacePrivate::WindowSystemEventList::peekAtFirs"
          "tOfType(EventType t) const': names the enum "
          "'QWindowSystemInterfacePrivate::EventType', whose class cannot "
          "be named here.")

    @staticmethod
    def prepend(*__, **_) -> Never:
      """
      Qt's 'void
      QWindowSystemInterfacePrivate::WindowSystemEventList::prepend(
      WindowSystemEvent *e)': names
      'QWindowSystemInterfacePrivate::WindowSystemEvent', which stands beside
      this class inside 'QWindowSystemInterfacePrivate' and cannot be named
      from here.
      """
      raise NotImplementedError(
          "'QWindowSystemInterfacePrivate.WindowSystemEventList.prepend' "
          "has no cute function yet. Qt's 'void "
          "QWindowSystemInterfacePrivate::WindowSystemEventList::prepend(Win"
          "dowSystemEvent *e)': names "
          "'QWindowSystemInterfacePrivate::WindowSystemEvent', which stands "
          "beside this class inside 'QWindowSystemInterfacePrivate' and "
          "cannot be named from here.")

    @staticmethod
    def remove(*__, **_) -> Never:
      """
      Qt's 'void
      QWindowSystemInterfacePrivate::WindowSystemEventList::remove(const
      WindowSystemEvent *e)': names
      'QWindowSystemInterfacePrivate::WindowSystemEvent', which stands beside
      this class inside 'QWindowSystemInterfacePrivate' and cannot be named
      from here.
      """
      raise NotImplementedError(
          "'QWindowSystemInterfacePrivate.WindowSystemEventList.remove' has "
          "no cute function yet. Qt's 'void "
          "QWindowSystemInterfacePrivate::WindowSystemEventList::remove(cons"
          "t WindowSystemEvent *e)': names "
          "'QWindowSystemInterfacePrivate::WindowSystemEvent', which stands "
          "beside this class inside 'QWindowSystemInterfacePrivate' and "
          "cannot be named from here.")

    @staticmethod
    def takeFirstNonUserInputOrReturnNull(*__, **_) -> Never:
      """
      Qt's 'WindowSystemEvent
      *QWindowSystemInterfacePrivate::WindowSystemEventList::
      takeFirstNonUserInputOrReturnNull()': gives
      'QWindowSystemInterfacePrivate::WindowSystemEvent', which stands beside
      this class inside 'QWindowSystemInterfacePrivate' and cannot be named
      from here.
      """
      raise NotImplementedError(
          "'QWindowSystemInterfacePrivate.WindowSystemEventList.takeFirstNon"
          "UserInputOrReturnNull' has no cute function yet. Qt's "
          "'WindowSystemEvent "
          "*QWindowSystemInterfacePrivate::WindowSystemEventList::takeFirstN"
          "onUserInputOrReturnNull()': gives "
          "'QWindowSystemInterfacePrivate::WindowSystemEvent', which stands "
          "beside this class inside 'QWindowSystemInterfacePrivate' and "
          "cannot be named from here.")

    @staticmethod
    def takeFirstOrReturnNull(*__, **_) -> Never:
      """
      Qt's 'WindowSystemEvent
      *QWindowSystemInterfacePrivate::WindowSystemEventList::
      takeFirstOrReturnNull()': gives
      'QWindowSystemInterfacePrivate::WindowSystemEvent', which stands beside
      this class inside 'QWindowSystemInterfacePrivate' and cannot be named
      from here.
      """
      raise NotImplementedError(
          "'QWindowSystemInterfacePrivate.WindowSystemEventList.takeFirstOrR"
          "eturnNull' has no cute function yet. Qt's 'WindowSystemEvent "
          "*QWindowSystemInterfacePrivate::WindowSystemEventList::takeFirstO"
          "rReturnNull()': gives "
          "'QWindowSystemInterfacePrivate::WindowSystemEvent', which stands "
          "beside this class inside 'QWindowSystemInterfacePrivate' and "
          "cannot be named from here.")

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def windowSystemEventsQueued() -> int:
    """
    Calls Qt's 'qsizetype
    QWindowSystemInterfacePrivate::windowSystemEventsQueued()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate.html
    """
    #  qsizetype QWindowSystemInterfacePrivate::windowSystemEventsQueued()
    return Rituals.call(
        'ritual_ZN29QWindowSystemInterfacePrivate24windowSystemEventsQueued'
        'Ev',
    )

  @staticmethod
  def nonUserInputEventsQueued() -> bool:
    """
    Calls Qt's 'bool
    QWindowSystemInterfacePrivate::nonUserInputEventsQueued()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate.html
    """
    #  bool QWindowSystemInterfacePrivate::nonUserInputEventsQueued()
    return Rituals.call(
        'ritual_ZN29QWindowSystemInterfacePrivate24nonUserInputEventsQueued'
        'Ev',
    )

  @staticmethod
  def getWindowSystemEvent() -> Optional[WindowSystemEvent]:
    """
    Calls Qt's 'WindowSystemEvent
    *QWindowSystemInterfacePrivate::getWindowSystemEvent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate.html

    Returns
    -------

    Optional[WindowSystemEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  WindowSystemEvent
    #      *QWindowSystemInterfacePrivate::getWindowSystemEvent()
    address = Rituals.call(
        'ritual_ZN29QWindowSystemInterfacePrivate20getWindowSystemEventEv',
    )
    return QWindowSystemInterfacePrivate.WindowSystemEvent._cuteAt(address)

  @staticmethod
  def getNonUserInputWindowSystemEvent() -> Optional[WindowSystemEvent]:
    """
    Calls Qt's 'WindowSystemEvent
    *QWindowSystemInterfacePrivate::getNonUserInputWindowSystemEvent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate.html

    Returns
    -------

    Optional[WindowSystemEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  WindowSystemEvent
    #      *QWindowSystemInterfacePrivate::getNonUserInputWindowSystemEvent()
    address = Rituals.call(
        'ritual_ZN29QWindowSystemInterfacePrivate32getNonUserInputWindowSys'
        'temEventEv',
    )
    return QWindowSystemInterfacePrivate.WindowSystemEvent._cuteAt(address)

  @staticmethod
  @overload(EventType)
  def peekWindowSystemEvent(t: EventType) -> Optional[WindowSystemEvent]:
    """
    Calls Qt's 'WindowSystemEvent
    *QWindowSystemInterfacePrivate::peekWindowSystemEvent(EventType t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate.html

    Parameters
    ----------

    t : EventType
      Passed on as its number.

    Returns
    -------

    Optional[WindowSystemEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  WindowSystemEvent
    #      *QWindowSystemInterfacePrivate::peekWindowSystemEvent(EventType t)
    address = Rituals.call(
        'ritual_ZN29QWindowSystemInterfacePrivate21peekWindowSystemEventENS'
        '_9EventTypeE',
        t.value,
    )
    return QWindowSystemInterfacePrivate.WindowSystemEvent._cuteAt(address)

  @staticmethod
  @overload(WindowSystemEvent)
  @overload(NoneType)
  def removeWindowSystemEvent(event: Optional[WindowSystemEvent]) -> None:
    """
    Calls Qt's 'void
    QWindowSystemInterfacePrivate::removeWindowSystemEvent(WindowSystemEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate.html

    Parameters
    ----------

    event : Optional[WindowSystemEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindowSystemInterfacePrivate::removeWindowSystemEvent(
    #      WindowSystemEvent *event)
    Rituals.call(
        'ritual_ZN29QWindowSystemInterfacePrivate23removeWindowSystemEventE'
        'PNS_17WindowSystemEventE',
        CuteMixin._addressOf(event),
    )

  @staticmethod
  @overload(QEventPoint, QWindow)
  @overload(QEventPoint, NoneType)
  def toNativeTouchPoint(
      point: QEventPoint,
      window: Optional[QWindow],
  ) -> QWindowSystemInterface.TouchPoint:
    """
    Calls Qt's 'QWindowSystemInterface::TouchPoint
    QWindowSystemInterfacePrivate::toNativeTouchPoint(const QEventPoint
    &point, const QWindow *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate.html

    Parameters
    ----------

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QWindowSystemInterface.TouchPoint
      A new cute QWindowSystemInterface::TouchPoint around the copy Qt gave
      back. Python owns it.
    """
    #  QWindowSystemInterface::TouchPoint
    #      QWindowSystemInterfacePrivate::toNativeTouchPoint(const
    #      QEventPoint &point, const QWindow *window)
    address = Rituals.call(
        'ritual_ZN29QWindowSystemInterfacePrivate18toNativeTouchPointERK11Q'
        'EventPointPK7QWindow',
        CuteMixin._valueOf(point), CuteMixin._addressOf(window),
    )
    return QWindowSystemInterface.TouchPoint._cuteOwning(address)

  @staticmethod
  @overload(QWindowSystemEventHandler)
  @overload(NoneType)
  def installWindowSystemEventHandler(
      handler: Optional[QWindowSystemEventHandler],
  ) -> None:
    """
    Calls Qt's 'void
    QWindowSystemInterfacePrivate::installWindowSystemEventHandler(
    QWindowSystemEventHandler *handler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate.html

    Parameters
    ----------

    handler : Optional[QWindowSystemEventHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindowSystemInterfacePrivate::installWindowSystemEventHandler(
    #      QWindowSystemEventHandler *handler)
    Rituals.call(
        'ritual_ZN29QWindowSystemInterfacePrivate31installWindowSystemEvent'
        'HandlerEP25QWindowSystemEventHandler',
        CuteMixin._addressOf(handler),
    )

  @staticmethod
  @overload(QWindowSystemEventHandler)
  @overload(NoneType)
  def removeWindowSystemEventhandler(
      handler: Optional[QWindowSystemEventHandler],
  ) -> None:
    """
    Calls Qt's 'void
    QWindowSystemInterfacePrivate::removeWindowSystemEventhandler(
    QWindowSystemEventHandler *handler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterfaceprivate.html

    Parameters
    ----------

    handler : Optional[QWindowSystemEventHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindowSystemInterfacePrivate::removeWindowSystemEventhandler(
    #      QWindowSystemEventHandler *handler)
    Rituals.call(
        'ritual_ZN29QWindowSystemInterfacePrivate30removeWindowSystemEventh'
        'andlerEP25QWindowSystemEventHandler',
        CuteMixin._addressOf(handler),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWindowSystemInterfacePrivate'

  #  Qt's '~QWindowSystemInterfacePrivate()'. Naming it makes this a value
  #  class: Python owns every C++ QWindowSystemInterfacePrivate behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN29QWindowSystemInterfacePrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @staticmethod
  def fromNativeTouchPoints(*__, **_) -> Never:
    """
    Qt's 'QList<QEventPoint>
    QWindowSystemInterfacePrivate::fromNativeTouchPoints(const
    QList<QWindowSystemInterface::TouchPoint> &points, const QWindow *window,
    QEvent::Type *type)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWindowSystemInterfacePrivate.fromNativeTouchPoints' has no cute "
        "function yet. Qt's 'QList<QEventPoint> "
        "QWindowSystemInterfacePrivate::fromNativeTouchPoints(const "
        "QList<QWindowSystemInterface::TouchPoint> &points, const QWindow "
        "*window, QEvent::Type *type)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def toNativeTouchPoints(*__, **_) -> Never:
    """
    Qt's 'QWindowSystemInterfacePrivate::toNativeTouchPoints': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QWindowSystemInterfacePrivate.toNativeTouchPoints' has no cute "
        "function yet. Qt's "
        "'QWindowSystemInterfacePrivate::toNativeTouchPoints': a template: "
        "a pattern and no single function.")
