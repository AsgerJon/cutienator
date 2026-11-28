"""
QWindowSystemInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QEvent, QEventLoop

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMimeData, QPoint, QPointF, QRect, QUrl
  from . import QInputDevice, QPlatformDragQtResponse
  from . import QPlatformDropQtResponse, QPlatformScreen, QPointingDevice
  from . import QScreen, QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QInputDevice = WAIT['QInputDevice']
  QMimeData = WAIT['QMimeData']
  QPlatformScreen = WAIT['QPlatformScreen']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QPointingDevice = WAIT['QPointingDevice']
  QRect = WAIT['QRect']
  QScreen = WAIT['QScreen']
  QUrl = WAIT['QUrl']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWindowSystemInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWindowSystemInterface: a plain Python object
  standing in front of one C++ QWindowSystemInterface.

  C++ hands a QWindowSystemInterface around as a copy, so every C++
  QWindowSystemInterface behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QWindowSystemInterface that has a ritual and that
  Python can call so far, 30 names in all: 'handleShortcutEvent',
  'handleExtendedKeyEvent', 'handleWheelEvent', 'registerInputDevice',
  'handleEnterLeaveEvent', 'handleDrag', 'handleDrop', 'handleScreenAdded',
  'handleScreenRemoved', 'handlePrimaryScreenChanged',
  'handleScreenOrientationChange', 'handleScreenGeometryChange',
  'handleScreenLogicalDotsPerInchChange', 'handleScreenRefreshRateChange',
  'handleFileOpenEvent', 'handleTabletEvent',
  'handleTabletEnterLeaveProximityEvent', 'handleTabletEnterProximityEvent',
  'handleTabletLeaveProximityEvent', 'handleGestureEvent',
  'handleGestureEventWithRealValue', 'handleGestureEventWithValueAndDelta',
  'handlePlatformPanelEvent', 'handleEnterWhatsThisEvent',
  'sendWindowSystemEvents', 'setSynchronousWindowSystemEvents',
  'flushWindowSystemEvents', 'deferredFlushWindowSystemEvents',
  'windowSystemEventsQueued', 'nonUserInputEventsQueued'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QWindowSystemInterface::handleNativeEvent(QWindow *window,
    const QByteArray &eventType, void *message, qintptr *result)': names
    'void', which has no cute class yet.
  - Qt's 'QWindowSystemInterface::~QWindowSystemInterface()': the destructor:
    Python removes its C++ QWindowSystemInterface by it, and has no other use
    for it.

  What has no ritual
  ------------------

  25 of the 68 functions Qt declares: 25 a template.

  What to expect
  --------------

  - The C++ QWindowSystemInterface is created at the first use, not by
    'QWindowSystemInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWindowSystemInterface back gives a copy the ritual
    made for Python, in a new cute QWindowSystemInterface.
  - Each name of Qt's QWindowSystemInterface that has no cute function yet,
    'handleApplicationStateChanged', 'handleApplicationTermination',
    'handleCloseEvent', 'handleContextMenuEvent', 'handleEnterEvent',
    'handleExposeEvent', 'handleFocusWindowChanged', 'handleGeometryChange',
    'handleKeyEvent', 'handleLeaveEvent', 'handleMouseEvent',
    'handleNativeEvent', 'handlePaintEvent', 'handleSafeAreaMarginsChanged',
    'handleThemeChange', 'handleTouchCancelEvent', 'handleTouchEvent',
    'handleWindowDevicePixelRatioChanged', 'handleWindowScreenChanged',
    'handleWindowStateChanged', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QWindowSystemInterface, each a class in
  #  here as in C++.

  class AsynchronousDelivery(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWindowSystemInterface::AsynchronousDelivery: a
    plain Python object standing in front of one C++
    QWindowSystemInterface::AsynchronousDelivery.

    C++ hands a QWindowSystemInterface::AsynchronousDelivery around as a
    copy, so every C++ QWindowSystemInterface::AsynchronousDelivery behind a
    cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QWindowSystemInterface::AsynchronousDelivery yet.
    None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QWindowSystemInterface::AsynchronousDelivery::~AsynchronousDelivery(
      )': the destructor: Python removes its C++
      QWindowSystemInterface::AsynchronousDelivery by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterface::AsynchronousDelivery is created at the
      first use, not by 'QWindowSystemInterface::AsynchronousDelivery(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWindowSystemInterface::AsynchronousDelivery back
      gives a copy the ritual made for Python, in a new cute
      QWindowSystemInterface::AsynchronousDelivery.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterface::AsynchronousDelivery'

    #  Qt's '~QWindowSystemInterface::AsynchronousDelivery()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QWindowSystemInterface::AsynchronousDelivery behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN22QWindowSystemInterface20AsynchronousDeliveryD1Ev')

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

  class DefaultDelivery(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWindowSystemInterface::DefaultDelivery: a plain
    Python object standing in front of one C++
    QWindowSystemInterface::DefaultDelivery.

    C++ hands a QWindowSystemInterface::DefaultDelivery around as a copy, so
    every C++ QWindowSystemInterface::DefaultDelivery behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QWindowSystemInterface::DefaultDelivery yet. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWindowSystemInterface::DefaultDelivery::~DefaultDelivery()': the
      destructor: Python removes its C++
      QWindowSystemInterface::DefaultDelivery by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QWindowSystemInterface::DefaultDelivery is created at the first
      use, not by 'QWindowSystemInterface::DefaultDelivery(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWindowSystemInterface::DefaultDelivery back gives
      a copy the ritual made for Python, in a new cute
      QWindowSystemInterface::DefaultDelivery.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterface::DefaultDelivery'

    #  Qt's '~QWindowSystemInterface::DefaultDelivery()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QWindowSystemInterface::DefaultDelivery behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN22QWindowSystemInterface15DefaultDeliveryD1Ev')

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

  class SynchronousDelivery(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWindowSystemInterface::SynchronousDelivery: a
    plain Python object standing in front of one C++
    QWindowSystemInterface::SynchronousDelivery.

    C++ hands a QWindowSystemInterface::SynchronousDelivery around as a copy,
    so every C++ QWindowSystemInterface::SynchronousDelivery behind a cute
    one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QWindowSystemInterface::SynchronousDelivery yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QWindowSystemInterface::SynchronousDelivery::~SynchronousDelivery()':
      the destructor: Python removes its C++
      QWindowSystemInterface::SynchronousDelivery by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterface::SynchronousDelivery is created at the
      first use, not by 'QWindowSystemInterface::SynchronousDelivery(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWindowSystemInterface::SynchronousDelivery back
      gives a copy the ritual made for Python, in a new cute
      QWindowSystemInterface::SynchronousDelivery.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterface::SynchronousDelivery'

    #  Qt's '~QWindowSystemInterface::SynchronousDelivery()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QWindowSystemInterface::SynchronousDelivery behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN22QWindowSystemInterface19SynchronousDeliveryD1Ev')

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

  class TouchPoint(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWindowSystemInterface::TouchPoint: a plain Python
    object standing in front of one C++ QWindowSystemInterface::TouchPoint.

    C++ hands a QWindowSystemInterface::TouchPoint around as a copy, so every
    C++ QWindowSystemInterface::TouchPoint behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QWindowSystemInterface::TouchPoint yet. It can be
    made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWindowSystemInterface::TouchPoint::~TouchPoint()': the
      destructor: Python removes its C++ QWindowSystemInterface::TouchPoint
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QWindowSystemInterface::TouchPoint is created at the first use,
      not by 'QWindowSystemInterface::TouchPoint(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWindowSystemInterface::TouchPoint back gives a
      copy the ritual made for Python, in a new cute
      QWindowSystemInterface::TouchPoint.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowSystemInterface::TouchPoint'

    #  Qt's '~QWindowSystemInterface::TouchPoint()'. Naming it makes this a
    #  value class: Python owns every C++ QWindowSystemInterface::TouchPoint
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN22QWindowSystemInterface10TouchPointD1Ev'

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
      'QWindowSystemInterface::TouchPoint::TouchPoint()', which is called at
      the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsysteminterface-touchpoint.html
      """
      #  QWindowSystemInterface::TouchPoint::TouchPoint()
      self._noteCreation(
          QWindowSystemInterface.TouchPoint, lambda: Rituals.call(
              'ritual_ZN22QWindowSystemInterface10TouchPointC1Ev',
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QWindow, int, int, Qt.KeyboardModifiers, int, int, int)
  @overload(NoneType, int, int, Qt.KeyboardModifiers, int, int, int)
  @overload(QWindow, int, int, Qt.KeyboardModifiers, int, int, int, str)
  @overload(NoneType, int, int, Qt.KeyboardModifiers, int, int, int, str)
  @overload(
      QWindow, int, int, Qt.KeyboardModifiers, int, int, int, str, bool,
  )
  @overload(
      NoneType, int, int, Qt.KeyboardModifiers, int, int, int, str, bool,
  )
  @overload(
      QWindow, int, int, Qt.KeyboardModifiers, int, int, int, str, bool, int,
  )
  @overload(
      NoneType, int, int, Qt.KeyboardModifiers, int, int, int, str, bool,
      int,
  )
  def handleShortcutEvent(
      window: Optional[QWindow],
      timestamp: int,
      k: int,
      mods: Qt.KeyboardModifiers,
      nativeScanCode: int,
      nativeVirtualKey: int,
      nativeModifiers: int,
      text: str = '',
      autorep: bool = False,
      count: int = 1,
  ) -> bool:
    """
    Calls Qt's 'bool QWindowSystemInterface::handleShortcutEvent(QWindow
    *window, ulong timestamp, int k, Qt::KeyboardModifiers mods, quint32
    nativeScanCode, quint32 nativeVirtualKey, quint32 nativeModifiers, const
    QString &text, bool autorep, ushort count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html#handleShortcutEvent

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    timestamp : int
      Passed on as it is.

    k : int
      Passed on as it is.

    mods : Qt.KeyboardModifiers
      Passed on as its number.

    nativeScanCode : int
      Passed on as it is.

    nativeVirtualKey : int
      Passed on as it is.

    nativeModifiers : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    autorep : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    count : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  bool QWindowSystemInterface::handleShortcutEvent(QWindow *window,
    #      ulong timestamp, int k, Qt::KeyboardModifiers mods, quint32
    #      nativeScanCode, quint32 nativeVirtualKey, quint32 nativeModifiers,
    #      const QString &text, bool autorep, ushort count)
    return Rituals.call(
        'ritual_ZN22QWindowSystemInterface19handleShortcutEventEP7QWindowmi'
        '6QFlagsIN2Qt16KeyboardModifierEEjjjRK7QStringbt',
        CuteMixin._addressOf(window), timestamp, k, mods.value,
        nativeScanCode, nativeVirtualKey, nativeModifiers, text, autorep,
        count,
    )

  @staticmethod
  @overload(QWindow, QEvent.Type, int, Qt.KeyboardModifiers, int, int, int)
  @overload(NoneType, QEvent.Type, int, Qt.KeyboardModifiers, int, int, int)
  @overload(
      QWindow, QEvent.Type, int, Qt.KeyboardModifiers, int, int, int, str,
  )
  @overload(
      NoneType, QEvent.Type, int, Qt.KeyboardModifiers, int, int, int, str,
  )
  @overload(
      QWindow, QEvent.Type, int, Qt.KeyboardModifiers, int, int, int, str,
      bool,
  )
  @overload(
      NoneType, QEvent.Type, int, Qt.KeyboardModifiers, int, int, int, str,
      bool,
  )
  @overload(
      QWindow, QEvent.Type, int, Qt.KeyboardModifiers, int, int, int, str,
      bool, int,
  )
  @overload(
      NoneType, QEvent.Type, int, Qt.KeyboardModifiers, int, int, int, str,
      bool, int,
  )
  def handleExtendedKeyEvent(
      window: Optional[QWindow],
      type: QEvent.Type,
      key: int,
      modifiers: Qt.KeyboardModifiers,
      nativeScanCode: int,
      nativeVirtualKey: int,
      nativeModifiers: int,
      text: str = '',
      autorep: bool = False,
      count: int = 1,
  ) -> bool:
    """
    Calls Qt's 'bool QWindowSystemInterface::handleExtendedKeyEvent(QWindow
    *window, QEvent::Type type, int key, Qt::KeyboardModifiers modifiers,
    quint32 nativeScanCode, quint32 nativeVirtualKey, quint32
    nativeModifiers, const QString &text, bool autorep, ushort count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html#handleExtendedKeyEvent

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type : QEvent.Type
      Passed on as its number.

    key : int
      Passed on as it is.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.

    nativeScanCode : int
      Passed on as it is.

    nativeVirtualKey : int
      Passed on as it is.

    nativeModifiers : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    autorep : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    count : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  bool QWindowSystemInterface::handleExtendedKeyEvent(QWindow *window,
    #      QEvent::Type type, int key, Qt::KeyboardModifiers modifiers,
    #      quint32 nativeScanCode, quint32 nativeVirtualKey, quint32
    #      nativeModifiers, const QString &text, bool autorep, ushort count)
    return Rituals.call(
        'ritual_ZN22QWindowSystemInterface22handleExtendedKeyEventEP7QWindo'
        'wN6QEvent4TypeEi6QFlagsIN2Qt16KeyboardModifierEEjjjRK7QStringbt',
        CuteMixin._addressOf(window), type.value, key, modifiers.value,
        nativeScanCode, nativeVirtualKey, nativeModifiers, text, autorep,
        count,
    )

  @staticmethod
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
  def handleExtendedKeyEvent(
      window: Optional[QWindow],
      timestamp: int,
      type: QEvent.Type,
      key: int,
      modifiers: Qt.KeyboardModifiers,
      nativeScanCode: int,
      nativeVirtualKey: int,
      nativeModifiers: int,
      text: str = '',
      autorep: bool = False,
      count: int = 1,
  ) -> bool:
    """
    Calls Qt's 'bool QWindowSystemInterface::handleExtendedKeyEvent(QWindow
    *window, ulong timestamp, QEvent::Type type, int key,
    Qt::KeyboardModifiers modifiers, quint32 nativeScanCode, quint32
    nativeVirtualKey, quint32 nativeModifiers, const QString &text, bool
    autorep, ushort count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html#handleExtendedKeyEvent

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    timestamp : int
      Passed on as it is.

    type : QEvent.Type
      Passed on as its number.

    key : int
      Passed on as it is.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.

    nativeScanCode : int
      Passed on as it is.

    nativeVirtualKey : int
      Passed on as it is.

    nativeModifiers : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    autorep : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    count : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  bool QWindowSystemInterface::handleExtendedKeyEvent(QWindow *window,
    #      ulong timestamp, QEvent::Type type, int key, Qt::KeyboardModifiers
    #      modifiers, quint32 nativeScanCode, quint32 nativeVirtualKey,
    #      quint32 nativeModifiers, const QString &text, bool autorep, ushort
    #      count)
    return Rituals.call(
        'ritual_ZN22QWindowSystemInterface22handleExtendedKeyEventEP7QWindo'
        'wmN6QEvent4TypeEi6QFlagsIN2Qt16KeyboardModifierEEjjjRK7QStringbt',
        CuteMixin._addressOf(window), timestamp, type.value, key,
        modifiers.value, nativeScanCode, nativeVirtualKey, nativeModifiers,
        text, autorep, count,
    )

  @staticmethod
  @overload(
      QWindow, int, QInputDevice, QEvent.Type, int, Qt.KeyboardModifiers,
      int, int, int,
  )
  @overload(
      QWindow, int, NoneType, QEvent.Type, int, Qt.KeyboardModifiers, int,
      int, int,
  )
  @overload(
      NoneType, int, QInputDevice, QEvent.Type, int, Qt.KeyboardModifiers,
      int, int, int,
  )
  @overload(
      NoneType, int, NoneType, QEvent.Type, int, Qt.KeyboardModifiers, int,
      int, int,
  )
  @overload(
      QWindow, int, QInputDevice, QEvent.Type, int, Qt.KeyboardModifiers,
      int, int, int, str,
  )
  @overload(
      QWindow, int, NoneType, QEvent.Type, int, Qt.KeyboardModifiers, int,
      int, int, str,
  )
  @overload(
      NoneType, int, QInputDevice, QEvent.Type, int, Qt.KeyboardModifiers,
      int, int, int, str,
  )
  @overload(
      NoneType, int, NoneType, QEvent.Type, int, Qt.KeyboardModifiers, int,
      int, int, str,
  )
  @overload(
      QWindow, int, QInputDevice, QEvent.Type, int, Qt.KeyboardModifiers,
      int, int, int, str, bool,
  )
  @overload(
      QWindow, int, NoneType, QEvent.Type, int, Qt.KeyboardModifiers, int,
      int, int, str, bool,
  )
  @overload(
      NoneType, int, QInputDevice, QEvent.Type, int, Qt.KeyboardModifiers,
      int, int, int, str, bool,
  )
  @overload(
      NoneType, int, NoneType, QEvent.Type, int, Qt.KeyboardModifiers, int,
      int, int, str, bool,
  )
  @overload(
      QWindow, int, QInputDevice, QEvent.Type, int, Qt.KeyboardModifiers,
      int, int, int, str, bool, int,
  )
  @overload(
      QWindow, int, NoneType, QEvent.Type, int, Qt.KeyboardModifiers, int,
      int, int, str, bool, int,
  )
  @overload(
      NoneType, int, QInputDevice, QEvent.Type, int, Qt.KeyboardModifiers,
      int, int, int, str, bool, int,
  )
  @overload(
      NoneType, int, NoneType, QEvent.Type, int, Qt.KeyboardModifiers, int,
      int, int, str, bool, int,
  )
  def handleExtendedKeyEvent(
      window: Optional[QWindow],
      timestamp: int,
      device: Optional[QInputDevice],
      type: QEvent.Type,
      key: int,
      modifiers: Qt.KeyboardModifiers,
      nativeScanCode: int,
      nativeVirtualKey: int,
      nativeModifiers: int,
      text: str = '',
      autorep: bool = False,
      count: int = 1,
  ) -> bool:
    """
    Calls Qt's 'bool QWindowSystemInterface::handleExtendedKeyEvent(QWindow
    *window, ulong timestamp, const QInputDevice *device, QEvent::Type type,
    int key, Qt::KeyboardModifiers modifiers, quint32 nativeScanCode, quint32
    nativeVirtualKey, quint32 nativeModifiers, const QString &text, bool
    autorep, ushort count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html#handleExtendedKeyEvent

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    timestamp : int
      Passed on as it is.

    device : Optional[QInputDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type : QEvent.Type
      Passed on as its number.

    key : int
      Passed on as it is.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.

    nativeScanCode : int
      Passed on as it is.

    nativeVirtualKey : int
      Passed on as it is.

    nativeModifiers : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    autorep : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    count : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  bool QWindowSystemInterface::handleExtendedKeyEvent(QWindow *window,
    #      ulong timestamp, const QInputDevice *device, QEvent::Type type,
    #      int key, Qt::KeyboardModifiers modifiers, quint32 nativeScanCode,
    #      quint32 nativeVirtualKey, quint32 nativeModifiers, const QString
    #      &text, bool autorep, ushort count)
    return Rituals.call(
        'ritual_ZN22QWindowSystemInterface22handleExtendedKeyEventEP7QWindo'
        'wmPK12QInputDeviceN6QEvent4TypeEi6QFlagsIN2Qt16KeyboardModifierEEj'
        'jjRK7QStringbt',
        CuteMixin._addressOf(window), timestamp,
        CuteMixin._addressOf(device), type.value, key, modifiers.value,
        nativeScanCode, nativeVirtualKey, nativeModifiers, text, autorep,
        count,
    )

  @staticmethod
  @overload(QWindow, QPointF, QPointF, QPoint, QPoint)
  @overload(NoneType, QPointF, QPointF, QPoint, QPoint)
  @overload(QWindow, QPointF, QPointF, QPoint, QPoint, Qt.KeyboardModifiers)
  @overload(NoneType, QPointF, QPointF, QPoint, QPoint, Qt.KeyboardModifiers)
  @overload(
      QWindow, QPointF, QPointF, QPoint, QPoint, Qt.KeyboardModifiers,
      Qt.ScrollPhase,
  )
  @overload(
      NoneType, QPointF, QPointF, QPoint, QPoint, Qt.KeyboardModifiers,
      Qt.ScrollPhase,
  )
  @overload(
      QWindow, QPointF, QPointF, QPoint, QPoint, Qt.KeyboardModifiers,
      Qt.ScrollPhase, Qt.MouseEventSource,
  )
  @overload(
      NoneType, QPointF, QPointF, QPoint, QPoint, Qt.KeyboardModifiers,
      Qt.ScrollPhase, Qt.MouseEventSource,
  )
  def handleWheelEvent(
      window: Optional[QWindow],
      local: QPointF,
      global_: QPointF,
      pixelDelta: QPoint,
      angleDelta: QPoint,
      mods: Qt.KeyboardModifiers = Qt.KeyboardModifiers.NoModifier,
      phase: Qt.ScrollPhase = Qt.ScrollPhase.NoScrollPhase,
      source: Qt.MouseEventSource = (
          Qt.MouseEventSource.MouseEventNotSynthesized),
  ) -> bool:
    """
    Calls Qt's 'bool QWindowSystemInterface::handleWheelEvent(QWindow
    *window, const QPointF &local, const QPointF &global, QPoint pixelDelta,
    QPoint angleDelta, Qt::KeyboardModifiers mods, Qt::ScrollPhase phase,
    Qt::MouseEventSource source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html#handleWheelEvent

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    local : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    global_ : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    pixelDelta : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    angleDelta : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    mods : Qt.KeyboardModifiers
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.KeyboardModifiers.NoModifier.

    phase : Qt.ScrollPhase
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ScrollPhase.NoScrollPhase.

    source : Qt.MouseEventSource
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.MouseEventSource.MouseEventNotSynthesized.
    """
    #  bool QWindowSystemInterface::handleWheelEvent(QWindow *window, const
    #      QPointF &local, const QPointF &global, QPoint pixelDelta, QPoint
    #      angleDelta, Qt::KeyboardModifiers mods, Qt::ScrollPhase phase,
    #      Qt::MouseEventSource source)
    return Rituals.call(
        'ritual_ZN22QWindowSystemInterface16handleWheelEventEP7QWindowRK7QP'
        'ointFS4_6QPointS5_6QFlagsIN2Qt16KeyboardModifierEENS7_11ScrollPhas'
        'eENS7_16MouseEventSourceE',
        CuteMixin._addressOf(window), CuteMixin._valueOf(local, 'QPointF'),
        CuteMixin._valueOf(global_, 'QPointF'),
        CuteMixin._valueOf(pixelDelta), CuteMixin._valueOf(angleDelta),
        mods.value, phase.value, source.value,
    )

  @staticmethod
  @overload(QWindow, int, QPointF, QPointF, QPoint, QPoint)
  @overload(NoneType, int, QPointF, QPointF, QPoint, QPoint)
  @overload(
      QWindow, int, QPointF, QPointF, QPoint, QPoint, Qt.KeyboardModifiers,
  )
  @overload(
      NoneType, int, QPointF, QPointF, QPoint, QPoint, Qt.KeyboardModifiers,
  )
  @overload(
      QWindow, int, QPointF, QPointF, QPoint, QPoint, Qt.KeyboardModifiers,
      Qt.ScrollPhase,
  )
  @overload(
      NoneType, int, QPointF, QPointF, QPoint, QPoint, Qt.KeyboardModifiers,
      Qt.ScrollPhase,
  )
  @overload(
      QWindow, int, QPointF, QPointF, QPoint, QPoint, Qt.KeyboardModifiers,
      Qt.ScrollPhase, Qt.MouseEventSource,
  )
  @overload(
      NoneType, int, QPointF, QPointF, QPoint, QPoint, Qt.KeyboardModifiers,
      Qt.ScrollPhase, Qt.MouseEventSource,
  )
  @overload(
      QWindow, int, QPointF, QPointF, QPoint, QPoint, Qt.KeyboardModifiers,
      Qt.ScrollPhase, Qt.MouseEventSource, bool,
  )
  @overload(
      NoneType, int, QPointF, QPointF, QPoint, QPoint, Qt.KeyboardModifiers,
      Qt.ScrollPhase, Qt.MouseEventSource, bool,
  )
  def handleWheelEvent(
      window: Optional[QWindow],
      timestamp: int,
      local: QPointF,
      global_: QPointF,
      pixelDelta: QPoint,
      angleDelta: QPoint,
      mods: Qt.KeyboardModifiers = Qt.KeyboardModifiers.NoModifier,
      phase: Qt.ScrollPhase = Qt.ScrollPhase.NoScrollPhase,
      source: Qt.MouseEventSource = (
          Qt.MouseEventSource.MouseEventNotSynthesized),
      inverted: bool = False,
  ) -> bool:
    """
    Calls Qt's 'bool QWindowSystemInterface::handleWheelEvent(QWindow
    *window, ulong timestamp, const QPointF &local, const QPointF &global,
    QPoint pixelDelta, QPoint angleDelta, Qt::KeyboardModifiers mods,
    Qt::ScrollPhase phase, Qt::MouseEventSource source, bool inverted)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html#handleWheelEvent

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    timestamp : int
      Passed on as it is.

    local : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    global_ : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    pixelDelta : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    angleDelta : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    mods : Qt.KeyboardModifiers
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.KeyboardModifiers.NoModifier.

    phase : Qt.ScrollPhase
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ScrollPhase.NoScrollPhase.

    source : Qt.MouseEventSource
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.MouseEventSource.MouseEventNotSynthesized.

    inverted : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  bool QWindowSystemInterface::handleWheelEvent(QWindow *window, ulong
    #      timestamp, const QPointF &local, const QPointF &global, QPoint
    #      pixelDelta, QPoint angleDelta, Qt::KeyboardModifiers mods,
    #      Qt::ScrollPhase phase, Qt::MouseEventSource source, bool inverted)
    return Rituals.call(
        'ritual_ZN22QWindowSystemInterface16handleWheelEventEP7QWindowmRK7Q'
        'PointFS4_6QPointS5_6QFlagsIN2Qt16KeyboardModifierEENS7_11ScrollPha'
        'seENS7_16MouseEventSourceEb',
        CuteMixin._addressOf(window), timestamp, CuteMixin._valueOf(local,
        'QPointF'), CuteMixin._valueOf(global_, 'QPointF'),
        CuteMixin._valueOf(pixelDelta), CuteMixin._valueOf(angleDelta),
        mods.value, phase.value, source.value, inverted,
    )

  @staticmethod
  @overload(QWindow, int, QPointingDevice, QPointF, QPointF, QPoint, QPoint)
  @overload(QWindow, int, NoneType, QPointF, QPointF, QPoint, QPoint)
  @overload(NoneType, int, QPointingDevice, QPointF, QPointF, QPoint, QPoint)
  @overload(NoneType, int, NoneType, QPointF, QPointF, QPoint, QPoint)
  @overload(
      QWindow, int, QPointingDevice, QPointF, QPointF, QPoint, QPoint,
      Qt.KeyboardModifiers,
  )
  @overload(
      QWindow, int, NoneType, QPointF, QPointF, QPoint, QPoint,
      Qt.KeyboardModifiers,
  )
  @overload(
      NoneType, int, QPointingDevice, QPointF, QPointF, QPoint, QPoint,
      Qt.KeyboardModifiers,
  )
  @overload(
      NoneType, int, NoneType, QPointF, QPointF, QPoint, QPoint,
      Qt.KeyboardModifiers,
  )
  @overload(
      QWindow, int, QPointingDevice, QPointF, QPointF, QPoint, QPoint,
      Qt.KeyboardModifiers, Qt.ScrollPhase,
  )
  @overload(
      QWindow, int, NoneType, QPointF, QPointF, QPoint, QPoint,
      Qt.KeyboardModifiers, Qt.ScrollPhase,
  )
  @overload(
      NoneType, int, QPointingDevice, QPointF, QPointF, QPoint, QPoint,
      Qt.KeyboardModifiers, Qt.ScrollPhase,
  )
  @overload(
      NoneType, int, NoneType, QPointF, QPointF, QPoint, QPoint,
      Qt.KeyboardModifiers, Qt.ScrollPhase,
  )
  @overload(
      QWindow, int, QPointingDevice, QPointF, QPointF, QPoint, QPoint,
      Qt.KeyboardModifiers, Qt.ScrollPhase, Qt.MouseEventSource,
  )
  @overload(
      QWindow, int, NoneType, QPointF, QPointF, QPoint, QPoint,
      Qt.KeyboardModifiers, Qt.ScrollPhase, Qt.MouseEventSource,
  )
  @overload(
      NoneType, int, QPointingDevice, QPointF, QPointF, QPoint, QPoint,
      Qt.KeyboardModifiers, Qt.ScrollPhase, Qt.MouseEventSource,
  )
  @overload(
      NoneType, int, NoneType, QPointF, QPointF, QPoint, QPoint,
      Qt.KeyboardModifiers, Qt.ScrollPhase, Qt.MouseEventSource,
  )
  @overload(
      QWindow, int, QPointingDevice, QPointF, QPointF, QPoint, QPoint,
      Qt.KeyboardModifiers, Qt.ScrollPhase, Qt.MouseEventSource, bool,
  )
  @overload(
      QWindow, int, NoneType, QPointF, QPointF, QPoint, QPoint,
      Qt.KeyboardModifiers, Qt.ScrollPhase, Qt.MouseEventSource, bool,
  )
  @overload(
      NoneType, int, QPointingDevice, QPointF, QPointF, QPoint, QPoint,
      Qt.KeyboardModifiers, Qt.ScrollPhase, Qt.MouseEventSource, bool,
  )
  @overload(
      NoneType, int, NoneType, QPointF, QPointF, QPoint, QPoint,
      Qt.KeyboardModifiers, Qt.ScrollPhase, Qt.MouseEventSource, bool,
  )
  def handleWheelEvent(
      window: Optional[QWindow],
      timestamp: int,
      device: Optional[QPointingDevice],
      local: QPointF,
      global_: QPointF,
      pixelDelta: QPoint,
      angleDelta: QPoint,
      mods: Qt.KeyboardModifiers = Qt.KeyboardModifiers.NoModifier,
      phase: Qt.ScrollPhase = Qt.ScrollPhase.NoScrollPhase,
      source: Qt.MouseEventSource = (
          Qt.MouseEventSource.MouseEventNotSynthesized),
      inverted: bool = False,
  ) -> bool:
    """
    Calls Qt's 'bool QWindowSystemInterface::handleWheelEvent(QWindow
    *window, ulong timestamp, const QPointingDevice *device, const QPointF
    &local, const QPointF &global, QPoint pixelDelta, QPoint angleDelta,
    Qt::KeyboardModifiers mods, Qt::ScrollPhase phase, Qt::MouseEventSource
    source, bool inverted)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html#handleWheelEvent

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    timestamp : int
      Passed on as it is.

    device : Optional[QPointingDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    local : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    global_ : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    pixelDelta : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    angleDelta : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    mods : Qt.KeyboardModifiers
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.KeyboardModifiers.NoModifier.

    phase : Qt.ScrollPhase
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ScrollPhase.NoScrollPhase.

    source : Qt.MouseEventSource
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.MouseEventSource.MouseEventNotSynthesized.

    inverted : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  bool QWindowSystemInterface::handleWheelEvent(QWindow *window, ulong
    #      timestamp, const QPointingDevice *device, const QPointF &local,
    #      const QPointF &global, QPoint pixelDelta, QPoint angleDelta,
    #      Qt::KeyboardModifiers mods, Qt::ScrollPhase phase,
    #      Qt::MouseEventSource source, bool inverted)
    return Rituals.call(
        'ritual_ZN22QWindowSystemInterface16handleWheelEventEP7QWindowmPK15'
        'QPointingDeviceRK7QPointFS7_6QPointS8_6QFlagsIN2Qt16KeyboardModifi'
        'erEENSA_11ScrollPhaseENSA_16MouseEventSourceEb',
        CuteMixin._addressOf(window), timestamp,
        CuteMixin._addressOf(device), CuteMixin._valueOf(local, 'QPointF'),
        CuteMixin._valueOf(global_, 'QPointF'),
        CuteMixin._valueOf(pixelDelta), CuteMixin._valueOf(angleDelta),
        mods.value, phase.value, source.value, inverted,
    )

  @staticmethod
  @overload(QInputDevice)
  @overload(NoneType)
  def registerInputDevice(device: Optional[QInputDevice]) -> None:
    """
    Calls Qt's 'void QWindowSystemInterface::registerInputDevice(const
    QInputDevice *device)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html#registerInputDevice

    Parameters
    ----------

    device : Optional[QInputDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindowSystemInterface::registerInputDevice(const QInputDevice
    #      *device)
    Rituals.call(
        'ritual_ZN22QWindowSystemInterface19registerInputDeviceEPK12QInputD'
        'evice',
        CuteMixin._addressOf(device),
    )

  @staticmethod
  @overload(QWindow, QWindow)
  @overload(QWindow, NoneType)
  @overload(NoneType, QWindow)
  @overload(NoneType, NoneType)
  @overload(QWindow, QWindow, QPointF)
  @overload(QWindow, NoneType, QPointF)
  @overload(NoneType, QWindow, QPointF)
  @overload(NoneType, NoneType, QPointF)
  @overload(QWindow, QWindow, QPointF, QPointF)
  @overload(QWindow, NoneType, QPointF, QPointF)
  @overload(NoneType, QWindow, QPointF, QPointF)
  @overload(NoneType, NoneType, QPointF, QPointF)
  def handleEnterLeaveEvent(
      enter: Optional[QWindow],
      leave: Optional[QWindow],
      local: Optional[QPointF] = None,
      global_: Optional[QPointF] = None,
  ) -> None:
    """
    Calls Qt's 'void QWindowSystemInterface::handleEnterLeaveEvent(QWindow
    *enter, QWindow *leave, const QPointF &local, const QPointF &global)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html#handleEnterLeaveEvent

    Parameters
    ----------

    enter : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    leave : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    local : Optional[QPointF]
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own. May be left out, as in Qt: a new 'QPointF()' is then passed on.

    global_ : Optional[QPointF]
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own. May be left out, as in Qt: a new 'QPointF()' is then passed on.
    """
    #  void QWindowSystemInterface::handleEnterLeaveEvent(QWindow *enter,
    #      QWindow *leave, const QPointF &local, const QPointF &global)
    if local is None:
      from ..QtCore import QPointF
      local = QPointF()
    if global_ is None:
      from ..QtCore import QPointF
      global_ = QPointF()
    Rituals.call(
        'ritual_ZN22QWindowSystemInterface21handleEnterLeaveEventEP7QWindow'
        'S1_RK7QPointFS4_',
        CuteMixin._addressOf(enter), CuteMixin._addressOf(leave),
        CuteMixin._valueOf(local, 'QPointF'), CuteMixin._valueOf(global_,
        'QPointF'),
    )

  @staticmethod
  @overload(
      QWindow, QMimeData, QPoint, Qt.DropActions, Qt.MouseButtons,
      Qt.KeyboardModifiers,
  )
  @overload(
      QWindow, NoneType, QPoint, Qt.DropActions, Qt.MouseButtons,
      Qt.KeyboardModifiers,
  )
  @overload(
      NoneType, QMimeData, QPoint, Qt.DropActions, Qt.MouseButtons,
      Qt.KeyboardModifiers,
  )
  @overload(
      NoneType, NoneType, QPoint, Qt.DropActions, Qt.MouseButtons,
      Qt.KeyboardModifiers,
  )
  def handleDrag(
      window: Optional[QWindow],
      dropData: Optional[QMimeData],
      p: QPoint,
      supportedActions: Qt.DropActions,
      buttons: Qt.MouseButtons,
      modifiers: Qt.KeyboardModifiers,
  ) -> QPlatformDragQtResponse:
    """
    Calls Qt's 'QPlatformDragQtResponse
    QWindowSystemInterface::handleDrag(QWindow *window, const QMimeData
    *dropData, const QPoint &p, Qt::DropActions supportedActions,
    Qt::MouseButtons buttons, Qt::KeyboardModifiers modifiers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html#handleDrag

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dropData : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    supportedActions : Qt.DropActions
      Passed on as its number.

    buttons : Qt.MouseButtons
      Passed on as its number.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.

    Returns
    -------

    QPlatformDragQtResponse
      A new cute QPlatformDragQtResponse around the copy Qt gave back. Python
      owns it.
    """
    #  QPlatformDragQtResponse QWindowSystemInterface::handleDrag(QWindow
    #      *window, const QMimeData *dropData, const QPoint &p,
    #      Qt::DropActions supportedActions, Qt::MouseButtons buttons,
    #      Qt::KeyboardModifiers modifiers)
    address = Rituals.call(
        'ritual_ZN22QWindowSystemInterface10handleDragEP7QWindowPK9QMimeDat'
        'aRK6QPoint6QFlagsIN2Qt10DropActionEES8_INS9_11MouseButtonEES8_INS9'
        '_16KeyboardModifierEE',
        CuteMixin._addressOf(window), CuteMixin._addressOf(dropData),
        CuteMixin._valueOf(p), supportedActions.value, buttons.value,
        modifiers.value,
    )
    from . import QPlatformDragQtResponse
    return QPlatformDragQtResponse._cuteOwning(address)

  @staticmethod
  @overload(
      QWindow, QMimeData, QPoint, Qt.DropActions, Qt.MouseButtons,
      Qt.KeyboardModifiers,
  )
  @overload(
      QWindow, NoneType, QPoint, Qt.DropActions, Qt.MouseButtons,
      Qt.KeyboardModifiers,
  )
  @overload(
      NoneType, QMimeData, QPoint, Qt.DropActions, Qt.MouseButtons,
      Qt.KeyboardModifiers,
  )
  @overload(
      NoneType, NoneType, QPoint, Qt.DropActions, Qt.MouseButtons,
      Qt.KeyboardModifiers,
  )
  def handleDrop(
      window: Optional[QWindow],
      dropData: Optional[QMimeData],
      p: QPoint,
      supportedActions: Qt.DropActions,
      buttons: Qt.MouseButtons,
      modifiers: Qt.KeyboardModifiers,
  ) -> QPlatformDropQtResponse:
    """
    Calls Qt's 'QPlatformDropQtResponse
    QWindowSystemInterface::handleDrop(QWindow *window, const QMimeData
    *dropData, const QPoint &p, Qt::DropActions supportedActions,
    Qt::MouseButtons buttons, Qt::KeyboardModifiers modifiers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html#handleDrop

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dropData : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    supportedActions : Qt.DropActions
      Passed on as its number.

    buttons : Qt.MouseButtons
      Passed on as its number.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.

    Returns
    -------

    QPlatformDropQtResponse
      A new cute QPlatformDropQtResponse around the copy Qt gave back. Python
      owns it.
    """
    #  QPlatformDropQtResponse QWindowSystemInterface::handleDrop(QWindow
    #      *window, const QMimeData *dropData, const QPoint &p,
    #      Qt::DropActions supportedActions, Qt::MouseButtons buttons,
    #      Qt::KeyboardModifiers modifiers)
    address = Rituals.call(
        'ritual_ZN22QWindowSystemInterface10handleDropEP7QWindowPK9QMimeDat'
        'aRK6QPoint6QFlagsIN2Qt10DropActionEES8_INS9_11MouseButtonEES8_INS9'
        '_16KeyboardModifierEE',
        CuteMixin._addressOf(window), CuteMixin._addressOf(dropData),
        CuteMixin._valueOf(p), supportedActions.value, buttons.value,
        modifiers.value,
    )
    from . import QPlatformDropQtResponse
    return QPlatformDropQtResponse._cuteOwning(address)

  @staticmethod
  @overload(QPlatformScreen)
  @overload(NoneType)
  @overload(QPlatformScreen, bool)
  @overload(NoneType, bool)
  def handleScreenAdded(
      screen: Optional[QPlatformScreen],
      isPrimary: bool = False,
  ) -> None:
    """
    Calls Qt's 'void
    QWindowSystemInterface::handleScreenAdded(QPlatformScreen *screen, bool
    isPrimary)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html#handleScreenAdded

    Parameters
    ----------

    screen : Optional[QPlatformScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    isPrimary : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QWindowSystemInterface::handleScreenAdded(QPlatformScreen
    #      *screen, bool isPrimary)
    Rituals.call(
        'ritual_ZN22QWindowSystemInterface17handleScreenAddedEP15QPlatformS'
        'creenb',
        CuteMixin._addressOf(screen), isPrimary,
    )

  @staticmethod
  @overload(QPlatformScreen)
  @overload(NoneType)
  def handleScreenRemoved(screen: Optional[QPlatformScreen]) -> None:
    """
    Calls Qt's 'void
    QWindowSystemInterface::handleScreenRemoved(QPlatformScreen *screen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html#handleScreenRemoved

    Parameters
    ----------

    screen : Optional[QPlatformScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindowSystemInterface::handleScreenRemoved(QPlatformScreen
    #      *screen)
    Rituals.call(
        'ritual_ZN22QWindowSystemInterface19handleScreenRemovedEP15QPlatfor'
        'mScreen',
        CuteMixin._addressOf(screen),
    )

  @staticmethod
  @overload(QPlatformScreen)
  @overload(NoneType)
  def handlePrimaryScreenChanged(
      newPrimary: Optional[QPlatformScreen],
  ) -> None:
    """
    Calls Qt's 'void
    QWindowSystemInterface::handlePrimaryScreenChanged(QPlatformScreen
    *newPrimary)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html

    Parameters
    ----------

    newPrimary : Optional[QPlatformScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QWindowSystemInterface::handlePrimaryScreenChanged(QPlatformScreen
    #      *newPrimary)
    Rituals.call(
        'ritual_ZN22QWindowSystemInterface26handlePrimaryScreenChangedEP15Q'
        'PlatformScreen',
        CuteMixin._addressOf(newPrimary),
    )

  @staticmethod
  @overload(QScreen, Qt.ScreenOrientation)
  @overload(NoneType, Qt.ScreenOrientation)
  def handleScreenOrientationChange(
      screen: Optional[QScreen],
      newOrientation: Qt.ScreenOrientation,
  ) -> None:
    """
    Calls Qt's 'void
    QWindowSystemInterface::handleScreenOrientationChange(QScreen *screen,
    Qt::ScreenOrientation newOrientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html

    Parameters
    ----------

    screen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    newOrientation : Qt.ScreenOrientation
      Passed on as its number.
    """
    #  void QWindowSystemInterface::handleScreenOrientationChange(QScreen
    #      *screen, Qt::ScreenOrientation newOrientation)
    Rituals.call(
        'ritual_ZN22QWindowSystemInterface29handleScreenOrientationChangeEP'
        '7QScreenN2Qt17ScreenOrientationE',
        CuteMixin._addressOf(screen), newOrientation.value,
    )

  @staticmethod
  @overload(QScreen, QRect, QRect)
  @overload(NoneType, QRect, QRect)
  def handleScreenGeometryChange(
      screen: Optional[QScreen],
      newGeometry: QRect,
      newAvailableGeometry: QRect,
  ) -> None:
    """
    Calls Qt's 'void
    QWindowSystemInterface::handleScreenGeometryChange(QScreen *screen, const
    QRect &newGeometry, const QRect &newAvailableGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html

    Parameters
    ----------

    screen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    newGeometry : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    newAvailableGeometry : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QWindowSystemInterface::handleScreenGeometryChange(QScreen
    #      *screen, const QRect &newGeometry, const QRect
    #      &newAvailableGeometry)
    Rituals.call(
        'ritual_ZN22QWindowSystemInterface26handleScreenGeometryChangeEP7QS'
        'creenRK5QRectS4_',
        CuteMixin._addressOf(screen), CuteMixin._valueOf(newGeometry),
        CuteMixin._valueOf(newAvailableGeometry),
    )

  @staticmethod
  @overload(QScreen, float, float)
  @overload(NoneType, float, float)
  def handleScreenLogicalDotsPerInchChange(
      screen: Optional[QScreen],
      newDpiX: float,
      newDpiY: float,
  ) -> None:
    """
    Calls Qt's 'void
    QWindowSystemInterface::handleScreenLogicalDotsPerInchChange(QScreen
    *screen, qreal newDpiX, qreal newDpiY)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html

    Parameters
    ----------

    screen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    newDpiX : float
      Passed on as it is.

    newDpiY : float
      Passed on as it is.
    """
    #  void QWindowSystemInterface::handleScreenLogicalDotsPerInchChange(
    #      QScreen *screen, qreal newDpiX, qreal newDpiY)
    Rituals.call(
        'ritual_ZN22QWindowSystemInterface36handleScreenLogicalDotsPerInchC'
        'hangeEP7QScreendd',
        CuteMixin._addressOf(screen), newDpiX, newDpiY,
    )

  @staticmethod
  @overload(QScreen, float)
  @overload(NoneType, float)
  def handleScreenRefreshRateChange(
      screen: Optional[QScreen],
      newRefreshRate: float,
  ) -> None:
    """
    Calls Qt's 'void
    QWindowSystemInterface::handleScreenRefreshRateChange(QScreen *screen,
    qreal newRefreshRate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html

    Parameters
    ----------

    screen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    newRefreshRate : float
      Passed on as it is.
    """
    #  void QWindowSystemInterface::handleScreenRefreshRateChange(QScreen
    #      *screen, qreal newRefreshRate)
    Rituals.call(
        'ritual_ZN22QWindowSystemInterface29handleScreenRefreshRateChangeEP'
        '7QScreend',
        CuteMixin._addressOf(screen), newRefreshRate,
    )

  @staticmethod
  @overload(str)
  def handleFileOpenEvent(fileName: str) -> None:
    """
    Calls Qt's 'void QWindowSystemInterface::handleFileOpenEvent(const
    QString &fileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html#handleFileOpenEvent

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWindowSystemInterface::handleFileOpenEvent(const QString
    #      &fileName)
    Rituals.call(
        'ritual_ZN22QWindowSystemInterface19handleFileOpenEventERK7QString',
        fileName,
    )

  @staticmethod
  @overload(QUrl)
  def handleFileOpenEvent(url: QUrl) -> None:
    """
    Calls Qt's 'void QWindowSystemInterface::handleFileOpenEvent(const QUrl
    &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html#handleFileOpenEvent

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QWindowSystemInterface::handleFileOpenEvent(const QUrl &url)
    Rituals.call(
        'ritual_ZN22QWindowSystemInterface19handleFileOpenEventERK4QUrl',
        CuteMixin._valueOf(url),
    )

  @staticmethod
  @overload(
      QWindow, int, QPointingDevice, QPointF, QPointF, Qt.MouseButtons,
      float, float, float, float, float, float,
  )
  @overload(
      QWindow, int, NoneType, QPointF, QPointF, Qt.MouseButtons, float,
      float, float, float, float, float,
  )
  @overload(
      NoneType, int, QPointingDevice, QPointF, QPointF, Qt.MouseButtons,
      float, float, float, float, float, float,
  )
  @overload(
      NoneType, int, NoneType, QPointF, QPointF, Qt.MouseButtons, float,
      float, float, float, float, float,
  )
  @overload(
      QWindow, int, QPointingDevice, QPointF, QPointF, Qt.MouseButtons,
      float, float, float, float, float, float, Qt.KeyboardModifiers,
  )
  @overload(
      QWindow, int, NoneType, QPointF, QPointF, Qt.MouseButtons, float,
      float, float, float, float, float, Qt.KeyboardModifiers,
  )
  @overload(
      NoneType, int, QPointingDevice, QPointF, QPointF, Qt.MouseButtons,
      float, float, float, float, float, float, Qt.KeyboardModifiers,
  )
  @overload(
      NoneType, int, NoneType, QPointF, QPointF, Qt.MouseButtons, float,
      float, float, float, float, float, Qt.KeyboardModifiers,
  )
  def handleTabletEvent(
      window: Optional[QWindow],
      timestamp: int,
      device: Optional[QPointingDevice],
      local: QPointF,
      global_: QPointF,
      buttons: Qt.MouseButtons,
      pressure: float,
      xTilt: float,
      yTilt: float,
      tangentialPressure: float,
      rotation: float,
      z: float,
      modifiers: Qt.KeyboardModifiers = Qt.KeyboardModifiers.NoModifier,
  ) -> bool:
    """
    Calls Qt's 'bool QWindowSystemInterface::handleTabletEvent(QWindow
    *window, ulong timestamp, const QPointingDevice *device, const QPointF
    &local, const QPointF &global, Qt::MouseButtons buttons, qreal pressure,
    qreal xTilt, qreal yTilt, qreal tangentialPressure, qreal rotation, qreal
    z, Qt::KeyboardModifiers modifiers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html#handleTabletEvent

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    timestamp : int
      Passed on as it is.

    device : Optional[QPointingDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    local : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    global_ : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    buttons : Qt.MouseButtons
      Passed on as its number.

    pressure : float
      Passed on as it is.

    xTilt : float
      Passed on as it is.

    yTilt : float
      Passed on as it is.

    tangentialPressure : float
      Passed on as it is.

    rotation : float
      Passed on as it is.

    z : float
      Passed on as it is.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.KeyboardModifiers.NoModifier.
    """
    #  bool QWindowSystemInterface::handleTabletEvent(QWindow *window, ulong
    #      timestamp, const QPointingDevice *device, const QPointF &local,
    #      const QPointF &global, Qt::MouseButtons buttons, qreal pressure,
    #      qreal xTilt, qreal yTilt, qreal tangentialPressure, qreal
    #      rotation, qreal z, Qt::KeyboardModifiers modifiers)
    return Rituals.call(
        'ritual_ZN22QWindowSystemInterface17handleTabletEventEP7QWindowmPK1'
        '5QPointingDeviceRK7QPointFS7_6QFlagsIN2Qt11MouseButtonEEddddddS8_I'
        'NS9_16KeyboardModifierEE',
        CuteMixin._addressOf(window), timestamp,
        CuteMixin._addressOf(device), CuteMixin._valueOf(local, 'QPointF'),
        CuteMixin._valueOf(global_, 'QPointF'), buttons.value, pressure,
        xTilt, yTilt, tangentialPressure, rotation, z, modifiers.value,
    )

  @staticmethod
  @overload(
      QWindow, QPointingDevice, QPointF, QPointF, Qt.MouseButtons, float,
      float, float, float, float, float,
  )
  @overload(
      QWindow, NoneType, QPointF, QPointF, Qt.MouseButtons, float, float,
      float, float, float, float,
  )
  @overload(
      NoneType, QPointingDevice, QPointF, QPointF, Qt.MouseButtons, float,
      float, float, float, float, float,
  )
  @overload(
      NoneType, NoneType, QPointF, QPointF, Qt.MouseButtons, float, float,
      float, float, float, float,
  )
  @overload(
      QWindow, QPointingDevice, QPointF, QPointF, Qt.MouseButtons, float,
      float, float, float, float, float, Qt.KeyboardModifiers,
  )
  @overload(
      QWindow, NoneType, QPointF, QPointF, Qt.MouseButtons, float, float,
      float, float, float, float, Qt.KeyboardModifiers,
  )
  @overload(
      NoneType, QPointingDevice, QPointF, QPointF, Qt.MouseButtons, float,
      float, float, float, float, float, Qt.KeyboardModifiers,
  )
  @overload(
      NoneType, NoneType, QPointF, QPointF, Qt.MouseButtons, float, float,
      float, float, float, float, Qt.KeyboardModifiers,
  )
  def handleTabletEvent(
      window: Optional[QWindow],
      device: Optional[QPointingDevice],
      local: QPointF,
      global_: QPointF,
      buttons: Qt.MouseButtons,
      pressure: float,
      xTilt: float,
      yTilt: float,
      tangentialPressure: float,
      rotation: float,
      z: float,
      modifiers: Qt.KeyboardModifiers = Qt.KeyboardModifiers.NoModifier,
  ) -> bool:
    """
    Calls Qt's 'bool QWindowSystemInterface::handleTabletEvent(QWindow
    *window, const QPointingDevice *device, const QPointF &local, const
    QPointF &global, Qt::MouseButtons buttons, qreal pressure, qreal xTilt,
    qreal yTilt, qreal tangentialPressure, qreal rotation, qreal z,
    Qt::KeyboardModifiers modifiers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html#handleTabletEvent

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    device : Optional[QPointingDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    local : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    global_ : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    buttons : Qt.MouseButtons
      Passed on as its number.

    pressure : float
      Passed on as it is.

    xTilt : float
      Passed on as it is.

    yTilt : float
      Passed on as it is.

    tangentialPressure : float
      Passed on as it is.

    rotation : float
      Passed on as it is.

    z : float
      Passed on as it is.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.KeyboardModifiers.NoModifier.
    """
    #  bool QWindowSystemInterface::handleTabletEvent(QWindow *window, const
    #      QPointingDevice *device, const QPointF &local, const QPointF
    #      &global, Qt::MouseButtons buttons, qreal pressure, qreal xTilt,
    #      qreal yTilt, qreal tangentialPressure, qreal rotation, qreal z,
    #      Qt::KeyboardModifiers modifiers)
    return Rituals.call(
        'ritual_ZN22QWindowSystemInterface17handleTabletEventEP7QWindowPK15'
        'QPointingDeviceRK7QPointFS7_6QFlagsIN2Qt11MouseButtonEEddddddS8_IN'
        'S9_16KeyboardModifierEE',
        CuteMixin._addressOf(window), CuteMixin._addressOf(device),
        CuteMixin._valueOf(local, 'QPointF'), CuteMixin._valueOf(global_,
        'QPointF'), buttons.value, pressure, xTilt, yTilt,
        tangentialPressure, rotation, z, modifiers.value,
    )

  @staticmethod
  @overload(
      QWindow, int, QPointF, QPointF, int, int, Qt.MouseButtons, float,
      float, float, float, float, float, int,
  )
  @overload(
      NoneType, int, QPointF, QPointF, int, int, Qt.MouseButtons, float,
      float, float, float, float, float, int,
  )
  @overload(
      QWindow, int, QPointF, QPointF, int, int, Qt.MouseButtons, float,
      float, float, float, float, float, int, Qt.KeyboardModifiers,
  )
  @overload(
      NoneType, int, QPointF, QPointF, int, int, Qt.MouseButtons, float,
      float, float, float, float, float, int, Qt.KeyboardModifiers,
  )
  def handleTabletEvent(
      window: Optional[QWindow],
      timestamp: int,
      local: QPointF,
      global_: QPointF,
      device: int,
      pointerType: int,
      buttons: Qt.MouseButtons,
      pressure: float,
      xTilt: float,
      yTilt: float,
      tangentialPressure: float,
      rotation: float,
      z: float,
      uid: int,
      modifiers: Qt.KeyboardModifiers = Qt.KeyboardModifiers.NoModifier,
  ) -> bool:
    """
    Calls Qt's 'bool QWindowSystemInterface::handleTabletEvent(QWindow
    *window, ulong timestamp, const QPointF &local, const QPointF &global,
    int device, int pointerType, Qt::MouseButtons buttons, qreal pressure,
    qreal xTilt, qreal yTilt, qreal tangentialPressure, qreal rotation, qreal
    z, qint64 uid, Qt::KeyboardModifiers modifiers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html#handleTabletEvent

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    timestamp : int
      Passed on as it is.

    local : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    global_ : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    device : int
      Passed on as it is.

    pointerType : int
      Passed on as it is.

    buttons : Qt.MouseButtons
      Passed on as its number.

    pressure : float
      Passed on as it is.

    xTilt : float
      Passed on as it is.

    yTilt : float
      Passed on as it is.

    tangentialPressure : float
      Passed on as it is.

    rotation : float
      Passed on as it is.

    z : float
      Passed on as it is.

    uid : int
      Passed on as it is.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.KeyboardModifiers.NoModifier.
    """
    #  bool QWindowSystemInterface::handleTabletEvent(QWindow *window, ulong
    #      timestamp, const QPointF &local, const QPointF &global, int
    #      device, int pointerType, Qt::MouseButtons buttons, qreal pressure,
    #      qreal xTilt, qreal yTilt, qreal tangentialPressure, qreal
    #      rotation, qreal z, qint64 uid, Qt::KeyboardModifiers modifiers)
    return Rituals.call(
        'ritual_ZN22QWindowSystemInterface17handleTabletEventEP7QWindowmRK7'
        'QPointFS4_ii6QFlagsIN2Qt11MouseButtonEEddddddxS5_INS6_16KeyboardMo'
        'difierEE',
        CuteMixin._addressOf(window), timestamp, CuteMixin._valueOf(local,
        'QPointF'), CuteMixin._valueOf(global_, 'QPointF'), device,
        pointerType, buttons.value, pressure, xTilt, yTilt,
        tangentialPressure, rotation, z, uid, modifiers.value,
    )

  @staticmethod
  @overload(
      QWindow, QPointF, QPointF, int, int, Qt.MouseButtons, float, float,
      float, float, float, float, int,
  )
  @overload(
      NoneType, QPointF, QPointF, int, int, Qt.MouseButtons, float, float,
      float, float, float, float, int,
  )
  @overload(
      QWindow, QPointF, QPointF, int, int, Qt.MouseButtons, float, float,
      float, float, float, float, int, Qt.KeyboardModifiers,
  )
  @overload(
      NoneType, QPointF, QPointF, int, int, Qt.MouseButtons, float, float,
      float, float, float, float, int, Qt.KeyboardModifiers,
  )
  def handleTabletEvent(
      window: Optional[QWindow],
      local: QPointF,
      global_: QPointF,
      device: int,
      pointerType: int,
      buttons: Qt.MouseButtons,
      pressure: float,
      xTilt: float,
      yTilt: float,
      tangentialPressure: float,
      rotation: float,
      z: float,
      uid: int,
      modifiers: Qt.KeyboardModifiers = Qt.KeyboardModifiers.NoModifier,
  ) -> bool:
    """
    Calls Qt's 'bool QWindowSystemInterface::handleTabletEvent(QWindow
    *window, const QPointF &local, const QPointF &global, int device, int
    pointerType, Qt::MouseButtons buttons, qreal pressure, qreal xTilt, qreal
    yTilt, qreal tangentialPressure, qreal rotation, qreal z, qint64 uid,
    Qt::KeyboardModifiers modifiers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html#handleTabletEvent

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    local : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    global_ : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    device : int
      Passed on as it is.

    pointerType : int
      Passed on as it is.

    buttons : Qt.MouseButtons
      Passed on as its number.

    pressure : float
      Passed on as it is.

    xTilt : float
      Passed on as it is.

    yTilt : float
      Passed on as it is.

    tangentialPressure : float
      Passed on as it is.

    rotation : float
      Passed on as it is.

    z : float
      Passed on as it is.

    uid : int
      Passed on as it is.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.KeyboardModifiers.NoModifier.
    """
    #  bool QWindowSystemInterface::handleTabletEvent(QWindow *window, const
    #      QPointF &local, const QPointF &global, int device, int
    #      pointerType, Qt::MouseButtons buttons, qreal pressure, qreal
    #      xTilt, qreal yTilt, qreal tangentialPressure, qreal rotation,
    #      qreal z, qint64 uid, Qt::KeyboardModifiers modifiers)
    return Rituals.call(
        'ritual_ZN22QWindowSystemInterface17handleTabletEventEP7QWindowRK7Q'
        'PointFS4_ii6QFlagsIN2Qt11MouseButtonEEddddddxS5_INS6_16KeyboardMod'
        'ifierEE',
        CuteMixin._addressOf(window), CuteMixin._valueOf(local, 'QPointF'),
        CuteMixin._valueOf(global_, 'QPointF'), device, pointerType,
        buttons.value, pressure, xTilt, yTilt, tangentialPressure, rotation,
        z, uid, modifiers.value,
    )

  @staticmethod
  @overload(QWindow, int, QPointingDevice, bool)
  @overload(QWindow, int, NoneType, bool)
  @overload(NoneType, int, QPointingDevice, bool)
  @overload(NoneType, int, NoneType, bool)
  @overload(QWindow, int, QPointingDevice, bool, QPointF)
  @overload(QWindow, int, NoneType, bool, QPointF)
  @overload(NoneType, int, QPointingDevice, bool, QPointF)
  @overload(NoneType, int, NoneType, bool, QPointF)
  @overload(QWindow, int, QPointingDevice, bool, QPointF, QPointF)
  @overload(QWindow, int, NoneType, bool, QPointF, QPointF)
  @overload(NoneType, int, QPointingDevice, bool, QPointF, QPointF)
  @overload(NoneType, int, NoneType, bool, QPointF, QPointF)
  @overload(
      QWindow, int, QPointingDevice, bool, QPointF, QPointF, Qt.MouseButtons,
  )
  @overload(QWindow, int, NoneType, bool, QPointF, QPointF, Qt.MouseButtons)
  @overload(
      NoneType, int, QPointingDevice, bool, QPointF, QPointF,
      Qt.MouseButtons,
  )
  @overload(NoneType, int, NoneType, bool, QPointF, QPointF, Qt.MouseButtons)
  @overload(
      QWindow, int, QPointingDevice, bool, QPointF, QPointF, Qt.MouseButtons,
      float,
  )
  @overload(
      QWindow, int, NoneType, bool, QPointF, QPointF, Qt.MouseButtons, float,
  )
  @overload(
      NoneType, int, QPointingDevice, bool, QPointF, QPointF,
      Qt.MouseButtons, float,
  )
  @overload(
      NoneType, int, NoneType, bool, QPointF, QPointF, Qt.MouseButtons,
      float,
  )
  @overload(
      QWindow, int, QPointingDevice, bool, QPointF, QPointF, Qt.MouseButtons,
      float, float,
  )
  @overload(
      QWindow, int, NoneType, bool, QPointF, QPointF, Qt.MouseButtons, float,
      float,
  )
  @overload(
      NoneType, int, QPointingDevice, bool, QPointF, QPointF,
      Qt.MouseButtons, float, float,
  )
  @overload(
      NoneType, int, NoneType, bool, QPointF, QPointF, Qt.MouseButtons,
      float, float,
  )
  @overload(
      QWindow, int, QPointingDevice, bool, QPointF, QPointF, Qt.MouseButtons,
      float, float, float,
  )
  @overload(
      QWindow, int, NoneType, bool, QPointF, QPointF, Qt.MouseButtons, float,
      float, float,
  )
  @overload(
      NoneType, int, QPointingDevice, bool, QPointF, QPointF,
      Qt.MouseButtons, float, float, float,
  )
  @overload(
      NoneType, int, NoneType, bool, QPointF, QPointF, Qt.MouseButtons,
      float, float, float,
  )
  @overload(
      QWindow, int, QPointingDevice, bool, QPointF, QPointF, Qt.MouseButtons,
      float, float, float, float,
  )
  @overload(
      QWindow, int, NoneType, bool, QPointF, QPointF, Qt.MouseButtons, float,
      float, float, float,
  )
  @overload(
      NoneType, int, QPointingDevice, bool, QPointF, QPointF,
      Qt.MouseButtons, float, float, float, float,
  )
  @overload(
      NoneType, int, NoneType, bool, QPointF, QPointF, Qt.MouseButtons,
      float, float, float, float,
  )
  @overload(
      QWindow, int, QPointingDevice, bool, QPointF, QPointF, Qt.MouseButtons,
      float, float, float, float, float,
  )
  @overload(
      QWindow, int, NoneType, bool, QPointF, QPointF, Qt.MouseButtons, float,
      float, float, float, float,
  )
  @overload(
      NoneType, int, QPointingDevice, bool, QPointF, QPointF,
      Qt.MouseButtons, float, float, float, float, float,
  )
  @overload(
      NoneType, int, NoneType, bool, QPointF, QPointF, Qt.MouseButtons,
      float, float, float, float, float,
  )
  @overload(
      QWindow, int, QPointingDevice, bool, QPointF, QPointF, Qt.MouseButtons,
      float, float, float, float, float, Qt.KeyboardModifiers,
  )
  @overload(
      QWindow, int, NoneType, bool, QPointF, QPointF, Qt.MouseButtons, float,
      float, float, float, float, Qt.KeyboardModifiers,
  )
  @overload(
      NoneType, int, QPointingDevice, bool, QPointF, QPointF,
      Qt.MouseButtons, float, float, float, float, float,
      Qt.KeyboardModifiers,
  )
  @overload(
      NoneType, int, NoneType, bool, QPointF, QPointF, Qt.MouseButtons,
      float, float, float, float, float, Qt.KeyboardModifiers,
  )
  def handleTabletEnterLeaveProximityEvent(
      window: Optional[QWindow],
      timestamp: int,
      device: Optional[QPointingDevice],
      inProximity: bool,
      local: Optional[QPointF] = None,
      global_: Optional[QPointF] = None,
      buttons: Qt.MouseButtons = Qt.MouseButtons(),
      xTilt: float = 0.0,
      yTilt: float = 0.0,
      tangentialPressure: float = 0.0,
      rotation: float = 0.0,
      z: float = 0.0,
      modifiers: Qt.KeyboardModifiers = Qt.KeyboardModifiers.NoModifier,
  ) -> bool:
    """
    Calls Qt's 'bool
    QWindowSystemInterface::handleTabletEnterLeaveProximityEvent(QWindow
    *window, ulong timestamp, const QPointingDevice *device, bool
    inProximity, const QPointF &local, const QPointF &global,
    Qt::MouseButtons buttons, qreal xTilt, qreal yTilt, qreal
    tangentialPressure, qreal rotation, qreal z, Qt::KeyboardModifiers
    modifiers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    timestamp : int
      Passed on as it is.

    device : Optional[QPointingDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    inProximity : bool
      Passed on as it is.

    local : Optional[QPointF]
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own. May be left out, as in Qt: a new 'QPointF()' is then passed on.

    global_ : Optional[QPointF]
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own. May be left out, as in Qt: a new 'QPointF()' is then passed on.

    buttons : Qt.MouseButtons
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.MouseButtons().

    xTilt : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    yTilt : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    tangentialPressure : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    rotation : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    z : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.KeyboardModifiers.NoModifier.
    """
    #  bool QWindowSystemInterface::handleTabletEnterLeaveProximityEvent(
    #      QWindow *window, ulong timestamp, const QPointingDevice *device,
    #      bool inProximity, const QPointF &local, const QPointF &global,
    #      Qt::MouseButtons buttons, qreal xTilt, qreal yTilt, qreal
    #      tangentialPressure, qreal rotation, qreal z, Qt::KeyboardModifiers
    #      modifiers)
    if local is None:
      from ..QtCore import QPointF
      local = QPointF()
    if global_ is None:
      from ..QtCore import QPointF
      global_ = QPointF()
    return Rituals.call(
        'ritual_ZN22QWindowSystemInterface36handleTabletEnterLeaveProximity'
        'EventEP7QWindowmPK15QPointingDevicebRK7QPointFS7_6QFlagsIN2Qt11Mou'
        'seButtonEEdddddS8_INS9_16KeyboardModifierEE',
        CuteMixin._addressOf(window), timestamp,
        CuteMixin._addressOf(device), inProximity, CuteMixin._valueOf(local,
        'QPointF'), CuteMixin._valueOf(global_, 'QPointF'), buttons.value,
        xTilt, yTilt, tangentialPressure, rotation, z, modifiers.value,
    )

  @staticmethod
  @overload(QWindow, QPointingDevice, bool)
  @overload(QWindow, NoneType, bool)
  @overload(NoneType, QPointingDevice, bool)
  @overload(NoneType, NoneType, bool)
  @overload(QWindow, QPointingDevice, bool, QPointF)
  @overload(QWindow, NoneType, bool, QPointF)
  @overload(NoneType, QPointingDevice, bool, QPointF)
  @overload(NoneType, NoneType, bool, QPointF)
  @overload(QWindow, QPointingDevice, bool, QPointF, QPointF)
  @overload(QWindow, NoneType, bool, QPointF, QPointF)
  @overload(NoneType, QPointingDevice, bool, QPointF, QPointF)
  @overload(NoneType, NoneType, bool, QPointF, QPointF)
  @overload(
      QWindow, QPointingDevice, bool, QPointF, QPointF, Qt.MouseButtons,
  )
  @overload(QWindow, NoneType, bool, QPointF, QPointF, Qt.MouseButtons)
  @overload(
      NoneType, QPointingDevice, bool, QPointF, QPointF, Qt.MouseButtons,
  )
  @overload(NoneType, NoneType, bool, QPointF, QPointF, Qt.MouseButtons)
  @overload(
      QWindow, QPointingDevice, bool, QPointF, QPointF, Qt.MouseButtons,
      float,
  )
  @overload(
      QWindow, NoneType, bool, QPointF, QPointF, Qt.MouseButtons, float,
  )
  @overload(
      NoneType, QPointingDevice, bool, QPointF, QPointF, Qt.MouseButtons,
      float,
  )
  @overload(
      NoneType, NoneType, bool, QPointF, QPointF, Qt.MouseButtons, float,
  )
  @overload(
      QWindow, QPointingDevice, bool, QPointF, QPointF, Qt.MouseButtons,
      float, float,
  )
  @overload(
      QWindow, NoneType, bool, QPointF, QPointF, Qt.MouseButtons, float,
      float,
  )
  @overload(
      NoneType, QPointingDevice, bool, QPointF, QPointF, Qt.MouseButtons,
      float, float,
  )
  @overload(
      NoneType, NoneType, bool, QPointF, QPointF, Qt.MouseButtons, float,
      float,
  )
  @overload(
      QWindow, QPointingDevice, bool, QPointF, QPointF, Qt.MouseButtons,
      float, float, float,
  )
  @overload(
      QWindow, NoneType, bool, QPointF, QPointF, Qt.MouseButtons, float,
      float, float,
  )
  @overload(
      NoneType, QPointingDevice, bool, QPointF, QPointF, Qt.MouseButtons,
      float, float, float,
  )
  @overload(
      NoneType, NoneType, bool, QPointF, QPointF, Qt.MouseButtons, float,
      float, float,
  )
  @overload(
      QWindow, QPointingDevice, bool, QPointF, QPointF, Qt.MouseButtons,
      float, float, float, float,
  )
  @overload(
      QWindow, NoneType, bool, QPointF, QPointF, Qt.MouseButtons, float,
      float, float, float,
  )
  @overload(
      NoneType, QPointingDevice, bool, QPointF, QPointF, Qt.MouseButtons,
      float, float, float, float,
  )
  @overload(
      NoneType, NoneType, bool, QPointF, QPointF, Qt.MouseButtons, float,
      float, float, float,
  )
  @overload(
      QWindow, QPointingDevice, bool, QPointF, QPointF, Qt.MouseButtons,
      float, float, float, float, float,
  )
  @overload(
      QWindow, NoneType, bool, QPointF, QPointF, Qt.MouseButtons, float,
      float, float, float, float,
  )
  @overload(
      NoneType, QPointingDevice, bool, QPointF, QPointF, Qt.MouseButtons,
      float, float, float, float, float,
  )
  @overload(
      NoneType, NoneType, bool, QPointF, QPointF, Qt.MouseButtons, float,
      float, float, float, float,
  )
  @overload(
      QWindow, QPointingDevice, bool, QPointF, QPointF, Qt.MouseButtons,
      float, float, float, float, float, Qt.KeyboardModifiers,
  )
  @overload(
      QWindow, NoneType, bool, QPointF, QPointF, Qt.MouseButtons, float,
      float, float, float, float, Qt.KeyboardModifiers,
  )
  @overload(
      NoneType, QPointingDevice, bool, QPointF, QPointF, Qt.MouseButtons,
      float, float, float, float, float, Qt.KeyboardModifiers,
  )
  @overload(
      NoneType, NoneType, bool, QPointF, QPointF, Qt.MouseButtons, float,
      float, float, float, float, Qt.KeyboardModifiers,
  )
  def handleTabletEnterLeaveProximityEvent(
      window: Optional[QWindow],
      device: Optional[QPointingDevice],
      inProximity: bool,
      local: Optional[QPointF] = None,
      global_: Optional[QPointF] = None,
      buttons: Qt.MouseButtons = Qt.MouseButtons(),
      xTilt: float = 0.0,
      yTilt: float = 0.0,
      tangentialPressure: float = 0.0,
      rotation: float = 0.0,
      z: float = 0.0,
      modifiers: Qt.KeyboardModifiers = Qt.KeyboardModifiers.NoModifier,
  ) -> bool:
    """
    Calls Qt's 'bool
    QWindowSystemInterface::handleTabletEnterLeaveProximityEvent(QWindow
    *window, const QPointingDevice *device, bool inProximity, const QPointF
    &local, const QPointF &global, Qt::MouseButtons buttons, qreal xTilt,
    qreal yTilt, qreal tangentialPressure, qreal rotation, qreal z,
    Qt::KeyboardModifiers modifiers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    device : Optional[QPointingDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    inProximity : bool
      Passed on as it is.

    local : Optional[QPointF]
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own. May be left out, as in Qt: a new 'QPointF()' is then passed on.

    global_ : Optional[QPointF]
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own. May be left out, as in Qt: a new 'QPointF()' is then passed on.

    buttons : Qt.MouseButtons
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.MouseButtons().

    xTilt : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    yTilt : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    tangentialPressure : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    rotation : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    z : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.KeyboardModifiers.NoModifier.
    """
    #  bool QWindowSystemInterface::handleTabletEnterLeaveProximityEvent(
    #      QWindow *window, const QPointingDevice *device, bool inProximity,
    #      const QPointF &local, const QPointF &global, Qt::MouseButtons
    #      buttons, qreal xTilt, qreal yTilt, qreal tangentialPressure, qreal
    #      rotation, qreal z, Qt::KeyboardModifiers modifiers)
    if local is None:
      from ..QtCore import QPointF
      local = QPointF()
    if global_ is None:
      from ..QtCore import QPointF
      global_ = QPointF()
    return Rituals.call(
        'ritual_ZN22QWindowSystemInterface36handleTabletEnterLeaveProximity'
        'EventEP7QWindowPK15QPointingDevicebRK7QPointFS7_6QFlagsIN2Qt11Mous'
        'eButtonEEdddddS8_INS9_16KeyboardModifierEE',
        CuteMixin._addressOf(window), CuteMixin._addressOf(device),
        inProximity, CuteMixin._valueOf(local, 'QPointF'),
        CuteMixin._valueOf(global_, 'QPointF'), buttons.value, xTilt, yTilt,
        tangentialPressure, rotation, z, modifiers.value,
    )

  @staticmethod
  @overload(int, int, int, int)
  def handleTabletEnterProximityEvent(
      timestamp: int,
      deviceType: int,
      pointerType: int,
      uid: int,
  ) -> bool:
    """
    Calls Qt's 'bool
    QWindowSystemInterface::handleTabletEnterProximityEvent(ulong timestamp,
    int deviceType, int pointerType, qint64 uid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html

    Parameters
    ----------

    timestamp : int
      Passed on as it is.

    deviceType : int
      Passed on as it is.

    pointerType : int
      Passed on as it is.

    uid : int
      Passed on as it is.
    """
    #  bool QWindowSystemInterface::handleTabletEnterProximityEvent(ulong
    #      timestamp, int deviceType, int pointerType, qint64 uid)
    return Rituals.call(
        'ritual_ZN22QWindowSystemInterface31handleTabletEnterProximityEvent'
        'Emiix',
        timestamp, deviceType, pointerType, uid,
    )

  @staticmethod
  @overload(int, int, int)
  def handleTabletEnterProximityEvent(
      deviceType: int,
      pointerType: int,
      uid: int,
  ) -> None:
    """
    Calls Qt's 'void
    QWindowSystemInterface::handleTabletEnterProximityEvent(int deviceType,
    int pointerType, qint64 uid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html

    Parameters
    ----------

    deviceType : int
      Passed on as it is.

    pointerType : int
      Passed on as it is.

    uid : int
      Passed on as it is.
    """
    #  void QWindowSystemInterface::handleTabletEnterProximityEvent(int
    #      deviceType, int pointerType, qint64 uid)
    Rituals.call(
        'ritual_ZN22QWindowSystemInterface31handleTabletEnterProximityEvent'
        'Eiix',
        deviceType, pointerType, uid,
    )

  @staticmethod
  @overload(int, int, int, int)
  def handleTabletLeaveProximityEvent(
      timestamp: int,
      deviceType: int,
      pointerType: int,
      uid: int,
  ) -> bool:
    """
    Calls Qt's 'bool
    QWindowSystemInterface::handleTabletLeaveProximityEvent(ulong timestamp,
    int deviceType, int pointerType, qint64 uid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html

    Parameters
    ----------

    timestamp : int
      Passed on as it is.

    deviceType : int
      Passed on as it is.

    pointerType : int
      Passed on as it is.

    uid : int
      Passed on as it is.
    """
    #  bool QWindowSystemInterface::handleTabletLeaveProximityEvent(ulong
    #      timestamp, int deviceType, int pointerType, qint64 uid)
    return Rituals.call(
        'ritual_ZN22QWindowSystemInterface31handleTabletLeaveProximityEvent'
        'Emiix',
        timestamp, deviceType, pointerType, uid,
    )

  @staticmethod
  @overload(int, int, int)
  def handleTabletLeaveProximityEvent(
      deviceType: int,
      pointerType: int,
      uid: int,
  ) -> None:
    """
    Calls Qt's 'void
    QWindowSystemInterface::handleTabletLeaveProximityEvent(int deviceType,
    int pointerType, qint64 uid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html

    Parameters
    ----------

    deviceType : int
      Passed on as it is.

    pointerType : int
      Passed on as it is.

    uid : int
      Passed on as it is.
    """
    #  void QWindowSystemInterface::handleTabletLeaveProximityEvent(int
    #      deviceType, int pointerType, qint64 uid)
    Rituals.call(
        'ritual_ZN22QWindowSystemInterface31handleTabletLeaveProximityEvent'
        'Eiix',
        deviceType, pointerType, uid,
    )

  @staticmethod
  @overload(
      QWindow, int, QPointingDevice, Qt.NativeGestureType, QPointF, QPointF,
  )
  @overload(QWindow, int, NoneType, Qt.NativeGestureType, QPointF, QPointF)
  @overload(
      NoneType, int, QPointingDevice, Qt.NativeGestureType, QPointF, QPointF,
  )
  @overload(NoneType, int, NoneType, Qt.NativeGestureType, QPointF, QPointF)
  @overload(
      QWindow, int, QPointingDevice, Qt.NativeGestureType, QPointF, QPointF,
      int,
  )
  @overload(
      QWindow, int, NoneType, Qt.NativeGestureType, QPointF, QPointF, int,
  )
  @overload(
      NoneType, int, QPointingDevice, Qt.NativeGestureType, QPointF, QPointF,
      int,
  )
  @overload(
      NoneType, int, NoneType, Qt.NativeGestureType, QPointF, QPointF, int,
  )
  def handleGestureEvent(
      window: Optional[QWindow],
      timestamp: int,
      device: Optional[QPointingDevice],
      type: Qt.NativeGestureType,
      local: QPointF,
      global_: QPointF,
      fingerCount: int = 0,
  ) -> bool:
    """
    Calls Qt's 'bool QWindowSystemInterface::handleGestureEvent(QWindow
    *window, ulong timestamp, const QPointingDevice *device,
    Qt::NativeGestureType type, const QPointF &local, const QPointF &global,
    int fingerCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html#handleGestureEvent

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    timestamp : int
      Passed on as it is.

    device : Optional[QPointingDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type : Qt.NativeGestureType
      Passed on as its number.

    local : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    global_ : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    fingerCount : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  bool QWindowSystemInterface::handleGestureEvent(QWindow *window, ulong
    #      timestamp, const QPointingDevice *device, Qt::NativeGestureType
    #      type, const QPointF &local, const QPointF &global, int
    #      fingerCount)
    return Rituals.call(
        'ritual_ZN22QWindowSystemInterface18handleGestureEventEP7QWindowmPK'
        '15QPointingDeviceN2Qt17NativeGestureTypeERK7QPointFS9_i',
        CuteMixin._addressOf(window), timestamp,
        CuteMixin._addressOf(device), type.value, CuteMixin._valueOf(local,
        'QPointF'), CuteMixin._valueOf(global_, 'QPointF'), fingerCount,
    )

  @staticmethod
  @overload(
      QWindow, int, QPointingDevice, Qt.NativeGestureType, float, QPointF,
      QPointF,
  )
  @overload(
      QWindow, int, NoneType, Qt.NativeGestureType, float, QPointF, QPointF,
  )
  @overload(
      NoneType, int, QPointingDevice, Qt.NativeGestureType, float, QPointF,
      QPointF,
  )
  @overload(
      NoneType, int, NoneType, Qt.NativeGestureType, float, QPointF, QPointF,
  )
  @overload(
      QWindow, int, QPointingDevice, Qt.NativeGestureType, float, QPointF,
      QPointF, int,
  )
  @overload(
      QWindow, int, NoneType, Qt.NativeGestureType, float, QPointF, QPointF,
      int,
  )
  @overload(
      NoneType, int, QPointingDevice, Qt.NativeGestureType, float, QPointF,
      QPointF, int,
  )
  @overload(
      NoneType, int, NoneType, Qt.NativeGestureType, float, QPointF, QPointF,
      int,
  )
  def handleGestureEventWithRealValue(
      window: Optional[QWindow],
      timestamp: int,
      device: Optional[QPointingDevice],
      type: Qt.NativeGestureType,
      value: float,
      local: QPointF,
      global_: QPointF,
      fingerCount: int = 2,
  ) -> bool:
    """
    Calls Qt's 'bool
    QWindowSystemInterface::handleGestureEventWithRealValue(QWindow *window,
    ulong timestamp, const QPointingDevice *device, Qt::NativeGestureType
    type, qreal value, const QPointF &local, const QPointF &global, int
    fingerCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    timestamp : int
      Passed on as it is.

    device : Optional[QPointingDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type : Qt.NativeGestureType
      Passed on as its number.

    value : float
      Passed on as it is.

    local : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    global_ : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    fingerCount : int
      Passed on as it is. May be left out, as in Qt: it is then 2.
    """
    #  bool QWindowSystemInterface::handleGestureEventWithRealValue(QWindow
    #      *window, ulong timestamp, const QPointingDevice *device,
    #      Qt::NativeGestureType type, qreal value, const QPointF &local,
    #      const QPointF &global, int fingerCount)
    return Rituals.call(
        'ritual_ZN22QWindowSystemInterface31handleGestureEventWithRealValue'
        'EP7QWindowmPK15QPointingDeviceN2Qt17NativeGestureTypeEdRK7QPointFS'
        '9_i',
        CuteMixin._addressOf(window), timestamp,
        CuteMixin._addressOf(device), type.value, value,
        CuteMixin._valueOf(local, 'QPointF'), CuteMixin._valueOf(global_,
        'QPointF'), fingerCount,
    )

  @staticmethod
  @overload(
      QWindow, int, QPointingDevice, Qt.NativeGestureType, float, QPointF,
      QPointF, QPointF,
  )
  @overload(
      QWindow, int, NoneType, Qt.NativeGestureType, float, QPointF, QPointF,
      QPointF,
  )
  @overload(
      NoneType, int, QPointingDevice, Qt.NativeGestureType, float, QPointF,
      QPointF, QPointF,
  )
  @overload(
      NoneType, int, NoneType, Qt.NativeGestureType, float, QPointF, QPointF,
      QPointF,
  )
  @overload(
      QWindow, int, QPointingDevice, Qt.NativeGestureType, float, QPointF,
      QPointF, QPointF, int,
  )
  @overload(
      QWindow, int, NoneType, Qt.NativeGestureType, float, QPointF, QPointF,
      QPointF, int,
  )
  @overload(
      NoneType, int, QPointingDevice, Qt.NativeGestureType, float, QPointF,
      QPointF, QPointF, int,
  )
  @overload(
      NoneType, int, NoneType, Qt.NativeGestureType, float, QPointF, QPointF,
      QPointF, int,
  )
  def handleGestureEventWithValueAndDelta(
      window: Optional[QWindow],
      timestamp: int,
      device: Optional[QPointingDevice],
      type: Qt.NativeGestureType,
      value: float,
      delta: QPointF,
      local: QPointF,
      global_: QPointF,
      fingerCount: int = 2,
  ) -> bool:
    """
    Calls Qt's 'bool
    QWindowSystemInterface::handleGestureEventWithValueAndDelta(QWindow
    *window, ulong timestamp, const QPointingDevice *device,
    Qt::NativeGestureType type, qreal value, const QPointF &delta, const
    QPointF &local, const QPointF &global, int fingerCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    timestamp : int
      Passed on as it is.

    device : Optional[QPointingDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type : Qt.NativeGestureType
      Passed on as its number.

    value : float
      Passed on as it is.

    delta : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    local : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    global_ : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    fingerCount : int
      Passed on as it is. May be left out, as in Qt: it is then 2.
    """
    #  bool QWindowSystemInterface::handleGestureEventWithValueAndDelta(
    #      QWindow *window, ulong timestamp, const QPointingDevice *device,
    #      Qt::NativeGestureType type, qreal value, const QPointF &delta,
    #      const QPointF &local, const QPointF &global, int fingerCount)
    return Rituals.call(
        'ritual_ZN22QWindowSystemInterface35handleGestureEventWithValueAndD'
        'eltaEP7QWindowmPK15QPointingDeviceN2Qt17NativeGestureTypeEdRK7QPoi'
        'ntFS9_S9_i',
        CuteMixin._addressOf(window), timestamp,
        CuteMixin._addressOf(device), type.value, value,
        CuteMixin._valueOf(delta, 'QPointF'), CuteMixin._valueOf(local,
        'QPointF'), CuteMixin._valueOf(global_, 'QPointF'), fingerCount,
    )

  @staticmethod
  @overload(QWindow)
  @overload(NoneType)
  def handlePlatformPanelEvent(window: Optional[QWindow]) -> None:
    """
    Calls Qt's 'void QWindowSystemInterface::handlePlatformPanelEvent(QWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindowSystemInterface::handlePlatformPanelEvent(QWindow *window)
    Rituals.call(
        'ritual_ZN22QWindowSystemInterface24handlePlatformPanelEventEP7QWin'
        'dow',
        CuteMixin._addressOf(window),
    )

  @staticmethod
  def handleEnterWhatsThisEvent() -> None:
    """
    Calls Qt's 'void QWindowSystemInterface::handleEnterWhatsThisEvent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html
    """
    #  void QWindowSystemInterface::handleEnterWhatsThisEvent()
    Rituals.call(
        'ritual_ZN22QWindowSystemInterface25handleEnterWhatsThisEventEv',
    )

  @staticmethod
  @overload(QEventLoop.ProcessEventsFlags)
  def sendWindowSystemEvents(flags: QEventLoop.ProcessEventsFlags) -> bool:
    """
    Calls Qt's 'bool
    QWindowSystemInterface::sendWindowSystemEvents(QEventLoop::
    ProcessEventsFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html#sendWindowSystemEvents

    Parameters
    ----------

    flags : QEventLoop.ProcessEventsFlags
      Passed on as its number.
    """
    #  bool QWindowSystemInterface::sendWindowSystemEvents(QEventLoop::
    #      ProcessEventsFlags flags)
    return Rituals.call(
        'ritual_ZN22QWindowSystemInterface22sendWindowSystemEventsE6QFlagsI'
        'N10QEventLoop17ProcessEventsFlagEE',
        flags.value,
    )

  @staticmethod
  @overload(bool)
  def setSynchronousWindowSystemEvents(enable: bool) -> None:
    """
    Calls Qt's 'void
    QWindowSystemInterface::setSynchronousWindowSystemEvents(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QWindowSystemInterface::setSynchronousWindowSystemEvents(bool
    #      enable)
    Rituals.call(
        'ritual_ZN22QWindowSystemInterface32setSynchronousWindowSystemEvent'
        'sEb',
        enable,
    )

  @staticmethod
  @overload()
  @overload(QEventLoop.ProcessEventsFlags)
  def flushWindowSystemEvents(
      flags: QEventLoop.ProcessEventsFlags = (
          QEventLoop.ProcessEventsFlags.AllEvents),
  ) -> bool:
    """
    Calls Qt's 'bool
    QWindowSystemInterface::flushWindowSystemEvents(QEventLoop::
    ProcessEventsFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html

    Parameters
    ----------

    flags : QEventLoop.ProcessEventsFlags
      Passed on as its number. May be left out, as in Qt: it is then
      QEventLoop.ProcessEventsFlags.AllEvents.
    """
    #  bool QWindowSystemInterface::flushWindowSystemEvents(QEventLoop::
    #      ProcessEventsFlags flags)
    return Rituals.call(
        'ritual_ZN22QWindowSystemInterface23flushWindowSystemEventsE6QFlags'
        'IN10QEventLoop17ProcessEventsFlagEE',
        flags.value,
    )

  @staticmethod
  @overload(QEventLoop.ProcessEventsFlags)
  def deferredFlushWindowSystemEvents(
      flags: QEventLoop.ProcessEventsFlags,
  ) -> None:
    """
    Calls Qt's 'void
    QWindowSystemInterface::deferredFlushWindowSystemEvents(QEventLoop::
    ProcessEventsFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html

    Parameters
    ----------

    flags : QEventLoop.ProcessEventsFlags
      Passed on as its number.
    """
    #  void QWindowSystemInterface::deferredFlushWindowSystemEvents(
    #      QEventLoop::ProcessEventsFlags flags)
    Rituals.call(
        'ritual_ZN22QWindowSystemInterface31deferredFlushWindowSystemEvents'
        'E6QFlagsIN10QEventLoop17ProcessEventsFlagEE',
        flags.value,
    )

  @staticmethod
  def windowSystemEventsQueued() -> int:
    """
    Calls Qt's 'int QWindowSystemInterface::windowSystemEventsQueued()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html
    """
    #  int QWindowSystemInterface::windowSystemEventsQueued()
    return Rituals.call(
        'ritual_ZN22QWindowSystemInterface24windowSystemEventsQueuedEv',
    )

  @staticmethod
  def nonUserInputEventsQueued() -> bool:
    """
    Calls Qt's 'bool QWindowSystemInterface::nonUserInputEventsQueued()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsysteminterface.html
    """
    #  bool QWindowSystemInterface::nonUserInputEventsQueued()
    return Rituals.call(
        'ritual_ZN22QWindowSystemInterface24nonUserInputEventsQueuedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWindowSystemInterface'

  #  Qt's '~QWindowSystemInterface()'. Naming it makes this a value class:
  #  Python owns every C++ QWindowSystemInterface behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QWindowSystemInterfaceD1Ev'

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
  def handleApplicationStateChanged(*__, **_) -> Never:
    """
    Qt's 'QWindowSystemInterface::handleApplicationStateChanged': a template:
    a pattern and no single function.
    """
    raise NotImplementedError(
        "'QWindowSystemInterface.handleApplicationStateChanged' has no cute "
        "function yet. Qt's "
        "'QWindowSystemInterface::handleApplicationStateChanged': a "
        "template: a pattern and no single function.")

  @staticmethod
  def handleApplicationTermination(*__, **_) -> Never:
    """
    Qt's 'QWindowSystemInterface::handleApplicationTermination': a template:
    a pattern and no single function.
    """
    raise NotImplementedError(
        "'QWindowSystemInterface.handleApplicationTermination' has no cute "
        "function yet. Qt's "
        "'QWindowSystemInterface::handleApplicationTermination': a "
        "template: a pattern and no single function.")

  @staticmethod
  def handleCloseEvent(*__, **_) -> Never:
    """
    Qt's 'QWindowSystemInterface::handleCloseEvent': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QWindowSystemInterface.handleCloseEvent' has no cute function "
        "yet. Qt's 'QWindowSystemInterface::handleCloseEvent': a template: "
        "a pattern and no single function.")

  @staticmethod
  def handleContextMenuEvent(*__, **_) -> Never:
    """
    Qt's 'QWindowSystemInterface::handleContextMenuEvent': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QWindowSystemInterface.handleContextMenuEvent' has no cute "
        "function yet. Qt's "
        "'QWindowSystemInterface::handleContextMenuEvent': a template: a "
        "pattern and no single function.")

  @staticmethod
  def handleEnterEvent(*__, **_) -> Never:
    """
    Qt's 'QWindowSystemInterface::handleEnterEvent': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QWindowSystemInterface.handleEnterEvent' has no cute function "
        "yet. Qt's 'QWindowSystemInterface::handleEnterEvent': a template: "
        "a pattern and no single function.")

  @staticmethod
  def handleExposeEvent(*__, **_) -> Never:
    """
    Qt's 'QWindowSystemInterface::handleExposeEvent': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QWindowSystemInterface.handleExposeEvent' has no cute function "
        "yet. Qt's 'QWindowSystemInterface::handleExposeEvent': a template: "
        "a pattern and no single function.")

  @staticmethod
  def handleFocusWindowChanged(*__, **_) -> Never:
    """
    Qt's 'QWindowSystemInterface::handleFocusWindowChanged': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QWindowSystemInterface.handleFocusWindowChanged' has no cute "
        "function yet. Qt's "
        "'QWindowSystemInterface::handleFocusWindowChanged': a template: a "
        "pattern and no single function.")

  @staticmethod
  def handleGeometryChange(*__, **_) -> Never:
    """
    Qt's 'QWindowSystemInterface::handleGeometryChange': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QWindowSystemInterface.handleGeometryChange' has no cute function "
        "yet. Qt's 'QWindowSystemInterface::handleGeometryChange': a "
        "template: a pattern and no single function.")

  @staticmethod
  def handleKeyEvent(*__, **_) -> Never:
    """
    Qt's 'QWindowSystemInterface::handleKeyEvent': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QWindowSystemInterface.handleKeyEvent' has no cute function yet. "
        "Qt's 'QWindowSystemInterface::handleKeyEvent': a template: a "
        "pattern and no single function.")

  @staticmethod
  def handleLeaveEvent(*__, **_) -> Never:
    """
    Qt's 'QWindowSystemInterface::handleLeaveEvent': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QWindowSystemInterface.handleLeaveEvent' has no cute function "
        "yet. Qt's 'QWindowSystemInterface::handleLeaveEvent': a template: "
        "a pattern and no single function.")

  @staticmethod
  def handleMouseEvent(*__, **_) -> Never:
    """
    Qt's 'QWindowSystemInterface::handleMouseEvent': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QWindowSystemInterface.handleMouseEvent' has no cute function "
        "yet. Qt's 'QWindowSystemInterface::handleMouseEvent': a template: "
        "a pattern and no single function.")

  @staticmethod
  def handleNativeEvent(*__, **_) -> Never:
    """
    Qt's 'bool QWindowSystemInterface::handleNativeEvent(QWindow *window,
    const QByteArray &eventType, void *message, qintptr *result)': names
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWindowSystemInterface.handleNativeEvent' has no cute function "
        "yet. Qt's 'bool QWindowSystemInterface::handleNativeEvent(QWindow "
        "*window, const QByteArray &eventType, void *message, qintptr "
        "*result)': names 'void', which has no cute class yet.")

  @staticmethod
  def handlePaintEvent(*__, **_) -> Never:
    """
    Qt's 'QWindowSystemInterface::handlePaintEvent': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QWindowSystemInterface.handlePaintEvent' has no cute function "
        "yet. Qt's 'QWindowSystemInterface::handlePaintEvent': a template: "
        "a pattern and no single function.")

  @staticmethod
  def handleSafeAreaMarginsChanged(*__, **_) -> Never:
    """
    Qt's 'QWindowSystemInterface::handleSafeAreaMarginsChanged': a template:
    a pattern and no single function.
    """
    raise NotImplementedError(
        "'QWindowSystemInterface.handleSafeAreaMarginsChanged' has no cute "
        "function yet. Qt's "
        "'QWindowSystemInterface::handleSafeAreaMarginsChanged': a "
        "template: a pattern and no single function.")

  @staticmethod
  def handleThemeChange(*__, **_) -> Never:
    """
    Qt's 'QWindowSystemInterface::handleThemeChange': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QWindowSystemInterface.handleThemeChange' has no cute function "
        "yet. Qt's 'QWindowSystemInterface::handleThemeChange': a template: "
        "a pattern and no single function.")

  @staticmethod
  def handleTouchCancelEvent(*__, **_) -> Never:
    """
    Qt's 'QWindowSystemInterface::handleTouchCancelEvent': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QWindowSystemInterface.handleTouchCancelEvent' has no cute "
        "function yet. Qt's "
        "'QWindowSystemInterface::handleTouchCancelEvent': a template: a "
        "pattern and no single function.")

  @staticmethod
  def handleTouchEvent(*__, **_) -> Never:
    """
    Qt's 'QWindowSystemInterface::handleTouchEvent': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QWindowSystemInterface.handleTouchEvent' has no cute function "
        "yet. Qt's 'QWindowSystemInterface::handleTouchEvent': a template: "
        "a pattern and no single function.")

  @staticmethod
  def handleWindowDevicePixelRatioChanged(*__, **_) -> Never:
    """
    Qt's 'QWindowSystemInterface::handleWindowDevicePixelRatioChanged': a
    template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QWindowSystemInterface.handleWindowDevicePixelRatioChanged' has "
        "no cute function yet. Qt's "
        "'QWindowSystemInterface::handleWindowDevicePixelRatioChanged': a "
        "template: a pattern and no single function.")

  @staticmethod
  def handleWindowScreenChanged(*__, **_) -> Never:
    """
    Qt's 'QWindowSystemInterface::handleWindowScreenChanged': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QWindowSystemInterface.handleWindowScreenChanged' has no cute "
        "function yet. Qt's "
        "'QWindowSystemInterface::handleWindowScreenChanged': a template: a "
        "pattern and no single function.")

  @staticmethod
  def handleWindowStateChanged(*__, **_) -> Never:
    """
    Qt's 'QWindowSystemInterface::handleWindowStateChanged': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QWindowSystemInterface.handleWindowStateChanged' has no cute "
        "function yet. Qt's "
        "'QWindowSystemInterface::handleWindowStateChanged': a template: a "
        "pattern and no single function.")
