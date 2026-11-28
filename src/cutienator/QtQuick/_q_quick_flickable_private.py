"""
QQuickFlickablePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickflickable_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickFlickablePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QEvent
from . import QQuickItemPrivate, QQuickTimeLineValue

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF, QRectF
  from ..QtGui import QInputEvent, QPointerEvent, QSinglePointEvent
  from ..QtGui import QVector2D
  from . import QQuickFlickable, QQuickGeometryChange, QQuickItem
  from . import QQuickPointerHandler
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QInputEvent = WAIT['QInputEvent']
  QPointF = WAIT['QPointF']
  QPointerEvent = WAIT['QPointerEvent']
  QQuickFlickable = WAIT['QQuickFlickable']
  QQuickGeometryChange = WAIT['QQuickGeometryChange']
  QQuickItem = WAIT['QQuickItem']
  QQuickPointerHandler = WAIT['QQuickPointerHandler']
  QRectF = WAIT['QRectF']
  QSinglePointEvent = WAIT['QSinglePointEvent']
  QVector2D = WAIT['QVector2D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFlickablePrivate(QQuickItemPrivate):
  """
  The cute side of Qt's QQuickFlickablePrivate: a plain Python object
  standing in front of one C++ QQuickFlickablePrivate.

  It is built on the cute 'QQuickItemPrivate', as Qt's QQuickFlickablePrivate
  is built on Qt's QQuickItemPrivate, and has everything that class has. Qt's
  QQuickFlickablePrivate is built on Qt's
  QSafeQuickItemChangeListener<QQuickFlickablePrivate> as well, which is not
  reflected.

  What exists
  -----------

  Every function of Qt's QQuickFlickablePrivate that has a ritual and that
  Python can call so far, 33 names in all: 'q_func', 'get', 'init', 'flickX',
  'flickY', 'flickingStarted', 'fixupX', 'fixupY', 'clearTimeline',
  'updateBeginningEnd', 'isInnermostPressDelay', 'captureDelayedPress',
  'clearDelayedPress', 'replayDelayedPress', 'setViewportX', 'setViewportY',
  'overShootDistance', 'itemGeometryChanged', 'draggingStarting',
  'draggingEnding', 'isViewMoving', 'cancelInteraction', 'addPointerHandler',
  'wantsPointerEvent', 'updateVelocity', 'handlePressEvent',
  'handleMoveEvent', 'handleReleaseEvent', 'buttonsAccepted',
  'maybeBeginDrag', 'drag', 'firstPointLocalVelocity', 'computeCurrentTime'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickFlickable *QQuickFlickablePrivate::q_func() const':
    takes in Python what 'QQuickFlickable *QQuickFlickablePrivate::q_func()'
    takes.
  - Qt's 'bool QQuickFlickablePrivate::flick(AxisData &data, qreal minExtent,
    qreal maxExtent, qreal vSize, QQuickTimeLineCallback::Callback
    fixupCallback, QEvent::Type eventType, qreal velocity)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QQuickFlickablePrivate::fixup(AxisData &data, qreal minExtent,
    qreal maxExtent)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQuickFlickablePrivate::adjustContentPos(AxisData &data, qreal
    toPos)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQuickFlickablePrivate::resetTimeline(AxisData &data)': takes
    a type Python has no way to hand over yet.
  - Qt's 'void QQuickFlickablePrivate::fixupY_callback(void *a0)': names
    'void', which has no cute class yet.
  - Qt's 'void QQuickFlickablePrivate::fixupX_callback(void *a0)': names
    'void', which has no cute class yet.
  - Qt's 'void QQuickFlickablePrivate::viewportAxisMoved(AxisData &data,
    qreal minExtent, qreal maxExtent, QQuickTimeLineCallback::Callback
    fixupCallback)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQuickFlickablePrivate::data_append(QQmlListProperty<QObject>
    *a0, QObject *a1)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
  - Qt's 'qsizetype
    QQuickFlickablePrivate::data_count(QQmlListProperty<QObject> *a0)': names
    'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'QObject *QQuickFlickablePrivate::data_at(QQmlListProperty<QObject>
    *a0, qsizetype a1)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
  - Qt's 'void QQuickFlickablePrivate::data_clear(QQmlListProperty<QObject>
    *a0)': names 'QQmlListProperty<QObject>', which has no cute class yet.

  What to expect
  --------------

  - The C++ QQuickFlickablePrivate is created at the first use, not by
    'QQuickFlickablePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFlickablePrivate.
  - Each name of Qt's QQuickFlickablePrivate that has no cute function yet,
    'adjustContentPos', 'fixup', 'fixupX_callback', 'fixupY_callback',
    'flick', 'resetTimeline', 'viewportAxisMoved', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickFlickablePrivate, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class FixupMode(CuteNum):
    """
    The enum 'QQuickFlickablePrivate::FixupMode' of Qt, with the 3 names Qt
    gives in it.
    """

    Normal = Kee[int](0)
    Immediate = Kee[int](1)
    ExtentChanged = Kee[int](2)

  class MovementReason(CuteNum):
    """
    The enum 'QQuickFlickablePrivate::MovementReason' of Qt, with the 3 names
    Qt gives in it.
    """

    Other = Kee[int](0)
    SetIndex = Kee[int](1)
    Mouse = Kee[int](2)

  #  The classes Qt writes inside QQuickFlickablePrivate, each a class in
  #  here as in C++.

  class AxisData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickFlickablePrivate::AxisData: a plain Python
    object standing in front of one C++ QQuickFlickablePrivate::AxisData.

    What exists
    -----------

    Every function of Qt's QQuickFlickablePrivate::AxisData that has a ritual
    and that Python can call so far, 5 names in all: 'reset',
    'markExtentsDirty', 'resetTransitionTo', 'addVelocitySample',
    'updateVelocity'. None can be made from Python: one comes out of a
    function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickFlickablePrivate::AxisData::~AxisData()': the destructor:
      Python never removes a C++ QQuickFlickablePrivate::AxisData.

    What has no ritual
    ------------------

    1 of the 7 functions Qt declares: 1 takes or gives a type that cannot be
    passed yet.

    What to expect
    --------------

    - The C++ QQuickFlickablePrivate::AxisData is created at the first use,
      not by 'QQuickFlickablePrivate::AxisData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QQuickFlickablePrivate::AxisData.
    - Each name of Qt's QQuickFlickablePrivate::AxisData that has no cute
      function yet, '__init__', holds a function that raises
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
    __qt_class__ = 'QQuickFlickablePrivate::AxisData'

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
      Qt's 'QQuickFlickablePrivate::AxisData::AxisData(QQuickFlickablePrivate
      *fp, void (QQuickFlickablePrivate::*)(qreal) func)': takes or gives a
      type that cannot be passed yet: void
      (QQuickFlickablePrivate::*)(qreal).
      """
      raise NotImplementedError(
          "'QQuickFlickablePrivate.AxisData.__init__' has no cute function "
          "yet. Qt's "
          "'QQuickFlickablePrivate::AxisData::AxisData(QQuickFlickablePrivat"
          "e *fp, void (QQuickFlickablePrivate::*)(qreal) func)': takes or "
          "gives a type that cannot be passed yet: void "
          "(QQuickFlickablePrivate::*)(qreal).")

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

    def reset(self) -> None:
      """
      Calls Qt's 'void QQuickFlickablePrivate::AxisData::reset()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickflickableprivate-axisdata.html#reset
      """
      #  void QQuickFlickablePrivate::AxisData::reset()
      self.uglySide.call(
          'ritual_ZN22QQuickFlickablePrivate8AxisData5resetEv',
      )

    def markExtentsDirty(self) -> None:
      """
      Calls Qt's 'void QQuickFlickablePrivate::AxisData::markExtentsDirty()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickflickableprivate-axisdata.html
      """
      #  void QQuickFlickablePrivate::AxisData::markExtentsDirty()
      self.uglySide.call(
          'ritual_ZN22QQuickFlickablePrivate8AxisData16markExtentsDirtyEv',
      )

    def resetTransitionTo(self) -> None:
      """
      Calls Qt's 'void
      QQuickFlickablePrivate::AxisData::resetTransitionTo()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickflickableprivate-axisdata.html
      """
      #  void QQuickFlickablePrivate::AxisData::resetTransitionTo()
      self.uglySide.call(
          'ritual_ZN22QQuickFlickablePrivate8AxisData17resetTransitionToEv',
      )

    @overload(float, float)
    def addVelocitySample(self, v: float, maxVelocity: float) -> None:
      """
      Calls Qt's 'void
      QQuickFlickablePrivate::AxisData::addVelocitySample(qreal v, qreal
      maxVelocity)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickflickableprivate-axisdata.html

      Parameters
      ----------

      v : float
        Passed on as it is.

      maxVelocity : float
        Passed on as it is.
      """
      #  void QQuickFlickablePrivate::AxisData::addVelocitySample(qreal v,
      #      qreal maxVelocity)
      self.uglySide.call(
          'ritual_ZN22QQuickFlickablePrivate8AxisData17addVelocitySampleEdd',
          v, maxVelocity,
      )

    def updateVelocity(self) -> None:
      """
      Calls Qt's 'void QQuickFlickablePrivate::AxisData::updateVelocity()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickflickableprivate-axisdata.html
      """
      #  void QQuickFlickablePrivate::AxisData::updateVelocity()
      self.uglySide.call(
          'ritual_ZN22QQuickFlickablePrivate8AxisData14updateVelocityEv',
      )

  class Velocity(QQuickTimeLineValue):
    """
    The cute side of Qt's QQuickFlickablePrivate::Velocity: a plain Python
    object standing in front of one C++ QQuickFlickablePrivate::Velocity.

    It is built on the cute 'QQuickTimeLineValue', as Qt's
    QQuickFlickablePrivate::Velocity is built on Qt's QQuickTimeLineValue,
    and has everything that class has.

    C++ hands a QQuickFlickablePrivate::Velocity around as a copy, so every
    C++ QQuickFlickablePrivate::Velocity behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QQuickFlickablePrivate::Velocity that has a ritual
    and that Python can call so far, 1 name in all: 'setValue'. It can be
    made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickFlickablePrivate::Velocity::~Velocity()': the destructor:
      Python removes its C++ QQuickFlickablePrivate::Velocity by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QQuickFlickablePrivate::Velocity is created at the first use,
      not by 'QQuickFlickablePrivate::Velocity(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickFlickablePrivate::Velocity back gives a copy
      the ritual made for Python, in a new cute
      QQuickFlickablePrivate::Velocity.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QQuickFlickablePrivate = WAIT['QQuickFlickablePrivate']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickFlickablePrivate::Velocity'

    #  A C++ QQuickFlickablePrivate::Velocity Python makes is of a C++ class
    #  of ours, in which Python can take functions over. This ritual hands
    #  one over; see 'CuteMixin._takeOver'.
    __take_ritual__ = 'ritual_take_QQuickFlickablePrivate_Velocity'

    #  Qt's '~QQuickFlickablePrivate::Velocity()'. Naming it makes this a
    #  value class: Python owns every C++ QQuickFlickablePrivate::Velocity
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN22QQuickFlickablePrivate8VelocityD1Ev'

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

    @overload(float)
    def setValue(self, v: float) -> None:
      """
      Calls Qt's 'void QQuickFlickablePrivate::Velocity::setValue(qreal v)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickflickableprivate-velocity.html#setValue

      Parameters
      ----------

      v : float
        Passed on as it is.
      """
      #  void QQuickFlickablePrivate::Velocity::setValue(qreal v)
      ritual = 'ritual_ZN22QQuickFlickablePrivate8Velocity8setValueEd'
      if self.uglySide.isOurs():
        ritual = 'ritual_own_ZN22QQuickFlickablePrivate8Velocity8setValueEd'
      self.uglySide.call(ritual, v)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(QQuickFlickablePrivate)
    @overload(NoneType)
    def __init__(self, p: Optional[QQuickFlickablePrivate]) -> None:
      """
      Notes what was given, for Qt's
      'QQuickFlickablePrivate::Velocity::Velocity(QQuickFlickablePrivate
      *p)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickflickableprivate-velocity.html#Velocity

      Parameters
      ----------

      p : Optional[QQuickFlickablePrivate]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  QQuickFlickablePrivate::Velocity::Velocity(QQuickFlickablePrivate
      #      *p)
      self._noteCreation(
          QQuickFlickablePrivate.Velocity, lambda: Rituals.call(
              'ritual_ZN22QQuickFlickablePrivate8VelocityC1EPS_',
              self._addressOf(p),
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
  @overload(QQuickFlickable)
  @overload(NoneType)
  def get(o: Optional[QQuickFlickable]) -> Optional[QQuickFlickablePrivate]:
    """
    Calls Qt's 'QQuickFlickablePrivate
    *QQuickFlickablePrivate::get(QQuickFlickable *o)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickableprivate.html#get

    Parameters
    ----------

    o : Optional[QQuickFlickable]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickFlickablePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFlickablePrivate *QQuickFlickablePrivate::get(QQuickFlickable
    #      *o)
    address = Rituals.call(
        'ritual_ZN22QQuickFlickablePrivate3getEP15QQuickFlickable',
        CuteMixin._addressOf(o),
    )
    return QQuickFlickablePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFlickablePrivate'

  #  The functions Qt calls itself that QQuickFlickablePrivate is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'flick': (
          'bool QQuickFlickablePrivate::flick(AxisData &, qreal, qreal, '
          'qreal, QQuickTimeLineCallback::Callback, QEvent::Type, qreal)',
      ),
      'fixup': (
          'void QQuickFlickablePrivate::fixup(AxisData &, qreal, qreal)',
      ),
  }

  #  The functions Qt calls itself that QQuickFlickablePrivate is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'itemGeometryChanged': (
          ('_ZN22QQuickFlickablePrivate19itemGeometryChangedEP10QQuickItem2'
           '0QQuickGeometryChangeRK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'value', 'QtQuick:QQuickGeometryChange'),
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'wantsPointerEvent': (
          ('_ZN22QQuickFlickablePrivate17wantsPointerEventEPK13QPointerEven'
           't',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtGui:QPointerEvent'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickItem)
  @overload(NoneType)
  def isInnermostPressDelay(self, item: Optional[QQuickItem]) -> bool:
    """
    Calls Qt's 'bool QQuickFlickablePrivate::isInnermostPressDelay(QQuickItem
    *item) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickableprivate.html#isInnermostPressDelay

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickFlickablePrivate::isInnermostPressDelay(QQuickItem *item)
    #      const
    return self.uglySide.call(
        'ritual_ZNK22QQuickFlickablePrivate21isInnermostPressDelayEP10QQuic'
        'kItem',
        self._addressOf(item),
    )

  @overload(float)
  def overShootDistance(self, velocity: float) -> float:
    """
    Calls Qt's 'qreal QQuickFlickablePrivate::overShootDistance(qreal
    velocity) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickableprivate.html#overShootDistance

    Parameters
    ----------

    velocity : float
      Passed on as it is.
    """
    #  qreal QQuickFlickablePrivate::overShootDistance(qreal velocity) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickFlickablePrivate17overShootDistanceEd', velocity,
    )

  def isViewMoving(self) -> bool:
    """
    Calls Qt's 'bool QQuickFlickablePrivate::isViewMoving() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickableprivate.html#isViewMoving
    """
    #  bool QQuickFlickablePrivate::isViewMoving() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickFlickablePrivate12isViewMovingEv',
    )

  @overload(QInputEvent)
  @overload(NoneType)
  def computeCurrentTime(self, event: Optional[QInputEvent]) -> int:
    """
    Calls Qt's 'qint64 QQuickFlickablePrivate::computeCurrentTime(QInputEvent
    *event) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickableprivate.html#computeCurrentTime

    Parameters
    ----------

    event : Optional[QInputEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qint64 QQuickFlickablePrivate::computeCurrentTime(QInputEvent *event)
    #      const
    return self.uglySide.call(
        'ritual_ZNK22QQuickFlickablePrivate18computeCurrentTimeEP11QInputEv'
        'ent',
        self._addressOf(event),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setViewportX(self, x: float) -> None:
    """
    Calls Qt's 'void QQuickFlickablePrivate::setViewportX(qreal x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickableprivate.html#setViewportX

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QQuickFlickablePrivate::setViewportX(qreal x)
    self.uglySide.call(
        'ritual_ZN22QQuickFlickablePrivate12setViewportXEd', x,
    )

  @overload(float)
  def setViewportY(self, y: float) -> None:
    """
    Calls Qt's 'void QQuickFlickablePrivate::setViewportY(qreal y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickableprivate.html#setViewportY

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QQuickFlickablePrivate::setViewportY(qreal y)
    self.uglySide.call(
        'ritual_ZN22QQuickFlickablePrivate12setViewportYEd', y,
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
    Notes what was given, for Qt's
    'QQuickFlickablePrivate::QQuickFlickablePrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickableprivate.html#QQuickFlickablePrivate
    """
    #  QQuickFlickablePrivate::QQuickFlickablePrivate()
    self._noteCreation(QQuickFlickablePrivate, lambda: Rituals.call(
        'ritual_ZN22QQuickFlickablePrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickFlickable]:
    """
    Calls Qt's 'QQuickFlickable *QQuickFlickablePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickableprivate.html#q_func

    Returns
    -------

    Optional[QQuickFlickable]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFlickable *QQuickFlickablePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QQuickFlickablePrivate6q_funcEv',
    )
    from . import QQuickFlickable
    return QQuickFlickable._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QQuickFlickablePrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickableprivate.html#init
    """
    #  void QQuickFlickablePrivate::init()
    self.uglySide.call('ritual_ZN22QQuickFlickablePrivate4initEv')

  @overload(QEvent.Type, float)
  def flickX(self, eventType: QEvent.Type, velocity: float) -> bool:
    """
    Calls Qt's 'bool QQuickFlickablePrivate::flickX(QEvent::Type eventType,
    qreal velocity)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickableprivate.html#flickX

    Parameters
    ----------

    eventType : QEvent.Type
      Passed on as its number.

    velocity : float
      Passed on as it is.
    """
    #  bool QQuickFlickablePrivate::flickX(QEvent::Type eventType, qreal
    #      velocity)
    return self.uglySide.call(
        'ritual_ZN22QQuickFlickablePrivate6flickXEN6QEvent4TypeEd',
        eventType.value, velocity,
    )

  @overload(QEvent.Type, float)
  def flickY(self, eventType: QEvent.Type, velocity: float) -> bool:
    """
    Calls Qt's 'bool QQuickFlickablePrivate::flickY(QEvent::Type eventType,
    qreal velocity)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickableprivate.html#flickY

    Parameters
    ----------

    eventType : QEvent.Type
      Passed on as its number.

    velocity : float
      Passed on as it is.
    """
    #  bool QQuickFlickablePrivate::flickY(QEvent::Type eventType, qreal
    #      velocity)
    return self.uglySide.call(
        'ritual_ZN22QQuickFlickablePrivate6flickYEN6QEvent4TypeEd',
        eventType.value, velocity,
    )

  @overload(bool, bool)
  def flickingStarted(self, flickingH: bool, flickingV: bool) -> None:
    """
    Calls Qt's 'void QQuickFlickablePrivate::flickingStarted(bool flickingH,
    bool flickingV)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickableprivate.html#flickingStarted

    Parameters
    ----------

    flickingH : bool
      Passed on as it is.

    flickingV : bool
      Passed on as it is.
    """
    #  void QQuickFlickablePrivate::flickingStarted(bool flickingH, bool
    #      flickingV)
    self.uglySide.call(
        'ritual_ZN22QQuickFlickablePrivate15flickingStartedEbb',
        flickingH, flickingV,
    )

  def fixupX(self) -> None:
    """
    Calls Qt's 'void QQuickFlickablePrivate::fixupX()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickableprivate.html#fixupX
    """
    #  void QQuickFlickablePrivate::fixupX()
    self.uglySide.call('ritual_ZN22QQuickFlickablePrivate6fixupXEv')

  def fixupY(self) -> None:
    """
    Calls Qt's 'void QQuickFlickablePrivate::fixupY()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickableprivate.html#fixupY
    """
    #  void QQuickFlickablePrivate::fixupY()
    self.uglySide.call('ritual_ZN22QQuickFlickablePrivate6fixupYEv')

  def clearTimeline(self) -> None:
    """
    Calls Qt's 'void QQuickFlickablePrivate::clearTimeline()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickableprivate.html#clearTimeline
    """
    #  void QQuickFlickablePrivate::clearTimeline()
    self.uglySide.call('ritual_ZN22QQuickFlickablePrivate13clearTimelineEv')

  def updateBeginningEnd(self) -> None:
    """
    Calls Qt's 'void QQuickFlickablePrivate::updateBeginningEnd()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickableprivate.html#updateBeginningEnd
    """
    #  void QQuickFlickablePrivate::updateBeginningEnd()
    self.uglySide.call(
        'ritual_ZN22QQuickFlickablePrivate18updateBeginningEndEv',
    )

  @overload(QQuickItem, QPointerEvent)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QPointerEvent)
  @overload(NoneType, NoneType)
  def captureDelayedPress(
      self,
      item: Optional[QQuickItem],
      event: Optional[QPointerEvent],
  ) -> None:
    """
    Calls Qt's 'void QQuickFlickablePrivate::captureDelayedPress(QQuickItem
    *item, QPointerEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickableprivate.html#captureDelayedPress

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFlickablePrivate::captureDelayedPress(QQuickItem *item,
    #      QPointerEvent *event)
    self.uglySide.call(
        'ritual_ZN22QQuickFlickablePrivate19captureDelayedPressEP10QQuickIt'
        'emP13QPointerEvent',
        self._addressOf(item), self._addressOf(event),
    )

  def clearDelayedPress(self) -> None:
    """
    Calls Qt's 'void QQuickFlickablePrivate::clearDelayedPress()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickableprivate.html#clearDelayedPress
    """
    #  void QQuickFlickablePrivate::clearDelayedPress()
    self.uglySide.call(
        'ritual_ZN22QQuickFlickablePrivate17clearDelayedPressEv',
    )

  def replayDelayedPress(self) -> None:
    """
    Calls Qt's 'void QQuickFlickablePrivate::replayDelayedPress()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickableprivate.html#replayDelayedPress
    """
    #  void QQuickFlickablePrivate::replayDelayedPress()
    self.uglySide.call(
        'ritual_ZN22QQuickFlickablePrivate18replayDelayedPressEv',
    )

  @overload(QQuickItem, QQuickGeometryChange, QRectF)
  @overload(NoneType, QQuickGeometryChange, QRectF)
  def itemGeometryChanged(
      self,
      a0: Optional[QQuickItem],
      a1: QQuickGeometryChange,
      a2: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QQuickFlickablePrivate::itemGeometryChanged(QQuickItem
    *a0, QQuickGeometryChange a1, const QRectF &a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickableprivate.html#itemGeometryChanged

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QQuickGeometryChange
      Passed on as a value: Qt reads the C++ QQuickGeometryChange, which
      stays Python's own.

    a2 : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickFlickablePrivate::itemGeometryChanged(QQuickItem *a0,
    #      QQuickGeometryChange a1, const QRectF &a2)
    ritual = (
        'ritual_ZN22QQuickFlickablePrivate19itemGeometryChangedEP10QQuickIt'
        'em20QQuickGeometryChangeRK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickFlickablePrivate19itemGeometryChangedEP10QQ'
          'uickItem20QQuickGeometryChangeRK6QRectF')
    self.uglySide.call(
        ritual, self._addressOf(a0), self._valueOf(a1), self._valueOf(a2),
    )

  def draggingStarting(self) -> None:
    """
    Calls Qt's 'void QQuickFlickablePrivate::draggingStarting()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickableprivate.html#draggingStarting
    """
    #  void QQuickFlickablePrivate::draggingStarting()
    self.uglySide.call(
        'ritual_ZN22QQuickFlickablePrivate16draggingStartingEv',
    )

  def draggingEnding(self) -> None:
    """
    Calls Qt's 'void QQuickFlickablePrivate::draggingEnding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickableprivate.html#draggingEnding
    """
    #  void QQuickFlickablePrivate::draggingEnding()
    self.uglySide.call('ritual_ZN22QQuickFlickablePrivate14draggingEndingEv')

  def cancelInteraction(self) -> None:
    """
    Calls Qt's 'void QQuickFlickablePrivate::cancelInteraction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickableprivate.html#cancelInteraction
    """
    #  void QQuickFlickablePrivate::cancelInteraction()
    self.uglySide.call(
        'ritual_ZN22QQuickFlickablePrivate17cancelInteractionEv',
    )

  @overload(QQuickPointerHandler)
  @overload(NoneType)
  def addPointerHandler(self, h: Optional[QQuickPointerHandler]) -> None:
    """
    Calls Qt's 'void
    QQuickFlickablePrivate::addPointerHandler(QQuickPointerHandler *h)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickableprivate.html#addPointerHandler

    Parameters
    ----------

    h : Optional[QQuickPointerHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFlickablePrivate::addPointerHandler(QQuickPointerHandler
    #      *h)
    ritual = (
        'ritual_ZN22QQuickFlickablePrivate17addPointerHandlerEP20QQuickPoin'
        'terHandler')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickFlickablePrivate17addPointerHandlerEP20QQui'
          'ckPointerHandler')
    self.uglySide.call(ritual, self._addressOf(h))

  @overload(QPointerEvent)
  @overload(NoneType)
  def wantsPointerEvent(self, a0: Optional[QPointerEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickFlickablePrivate::wantsPointerEvent(const
    QPointerEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickableprivate.html#wantsPointerEvent

    Parameters
    ----------

    a0 : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickFlickablePrivate::wantsPointerEvent(const QPointerEvent
    #      *a0)
    ritual = (
        'ritual_ZN22QQuickFlickablePrivate17wantsPointerEventEPK13QPointerE'
        'vent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickFlickablePrivate17wantsPointerEventEPK13QPo'
          'interEvent')
    return self.uglySide.call(ritual, self._addressOf(a0))

  def updateVelocity(self) -> None:
    """
    Calls Qt's 'void QQuickFlickablePrivate::updateVelocity()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickableprivate.html#updateVelocity
    """
    #  void QQuickFlickablePrivate::updateVelocity()
    self.uglySide.call('ritual_ZN22QQuickFlickablePrivate14updateVelocityEv')

  @overload(QPointerEvent)
  @overload(NoneType)
  def handlePressEvent(self, a0: Optional[QPointerEvent]) -> None:
    """
    Calls Qt's 'void QQuickFlickablePrivate::handlePressEvent(QPointerEvent
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickableprivate.html#handlePressEvent

    Parameters
    ----------

    a0 : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFlickablePrivate::handlePressEvent(QPointerEvent *a0)
    self.uglySide.call(
        'ritual_ZN22QQuickFlickablePrivate16handlePressEventEP13QPointerEve'
        'nt',
        self._addressOf(a0),
    )

  @overload(QPointerEvent)
  @overload(NoneType)
  def handleMoveEvent(self, a0: Optional[QPointerEvent]) -> None:
    """
    Calls Qt's 'void QQuickFlickablePrivate::handleMoveEvent(QPointerEvent
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickableprivate.html#handleMoveEvent

    Parameters
    ----------

    a0 : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFlickablePrivate::handleMoveEvent(QPointerEvent *a0)
    self.uglySide.call(
        'ritual_ZN22QQuickFlickablePrivate15handleMoveEventEP13QPointerEven'
        't',
        self._addressOf(a0),
    )

  @overload(QPointerEvent)
  @overload(NoneType)
  def handleReleaseEvent(self, a0: Optional[QPointerEvent]) -> None:
    """
    Calls Qt's 'void QQuickFlickablePrivate::handleReleaseEvent(QPointerEvent
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickableprivate.html#handleReleaseEvent

    Parameters
    ----------

    a0 : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFlickablePrivate::handleReleaseEvent(QPointerEvent *a0)
    self.uglySide.call(
        'ritual_ZN22QQuickFlickablePrivate18handleReleaseEventEP13QPointerE'
        'vent',
        self._addressOf(a0),
    )

  @overload(QSinglePointEvent)
  @overload(NoneType)
  def buttonsAccepted(self, event: Optional[QSinglePointEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickFlickablePrivate::buttonsAccepted(const
    QSinglePointEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickableprivate.html#buttonsAccepted

    Parameters
    ----------

    event : Optional[QSinglePointEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickFlickablePrivate::buttonsAccepted(const QSinglePointEvent
    #      *event)
    return self.uglySide.call(
        'ritual_ZN22QQuickFlickablePrivate15buttonsAcceptedEPK17QSinglePoin'
        'tEvent',
        self._addressOf(event),
    )

  @overload(int, QPointF)
  @overload(int, QPointF, Qt.MouseButtons)
  def maybeBeginDrag(
      self,
      currentTimestamp: int,
      pressPosn: QPointF,
      buttons: Qt.MouseButtons = Qt.MouseButtons.NoButton,
  ) -> None:
    """
    Calls Qt's 'void QQuickFlickablePrivate::maybeBeginDrag(qint64
    currentTimestamp, const QPointF &pressPosn, Qt::MouseButtons buttons)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickableprivate.html#maybeBeginDrag

    Parameters
    ----------

    currentTimestamp : int
      Passed on as it is.

    pressPosn : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    buttons : Qt.MouseButtons
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.MouseButtons.NoButton.
    """
    #  void QQuickFlickablePrivate::maybeBeginDrag(qint64 currentTimestamp,
    #      const QPointF &pressPosn, Qt::MouseButtons buttons)
    self.uglySide.call(
        'ritual_ZN22QQuickFlickablePrivate14maybeBeginDragExRK7QPointF6QFla'
        'gsIN2Qt11MouseButtonEE',
        currentTimestamp, self._valueOf(pressPosn, 'QPointF'), buttons.value,
    )

  @overload(
      int, QEvent.Type, QPointF, QVector2D, bool, bool, bool, QVector2D,
  )
  def drag(
      self,
      currentTimestamp: int,
      eventType: QEvent.Type,
      localPos: QPointF,
      deltas: QVector2D,
      overThreshold: bool,
      momentum: bool,
      velocitySensitiveOverBounds: bool,
      velocity: QVector2D,
  ) -> None:
    """
    Calls Qt's 'void QQuickFlickablePrivate::drag(qint64 currentTimestamp,
    QEvent::Type eventType, const QPointF &localPos, const QVector2D &deltas,
    bool overThreshold, bool momentum, bool velocitySensitiveOverBounds,
    const QVector2D &velocity)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickableprivate.html#drag

    Parameters
    ----------

    currentTimestamp : int
      Passed on as it is.

    eventType : QEvent.Type
      Passed on as its number.

    localPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    deltas : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    overThreshold : bool
      Passed on as it is.

    momentum : bool
      Passed on as it is.

    velocitySensitiveOverBounds : bool
      Passed on as it is.

    velocity : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void QQuickFlickablePrivate::drag(qint64 currentTimestamp,
    #      QEvent::Type eventType, const QPointF &localPos, const QVector2D
    #      &deltas, bool overThreshold, bool momentum, bool
    #      velocitySensitiveOverBounds, const QVector2D &velocity)
    self.uglySide.call(
        'ritual_ZN22QQuickFlickablePrivate4dragExN6QEvent4TypeERK7QPointFRK'
        '9QVector2DbbbS7_',
        currentTimestamp, eventType.value, self._valueOf(localPos,
        'QPointF'), self._valueOf(deltas), overThreshold, momentum,
        velocitySensitiveOverBounds, self._valueOf(velocity),
    )

  @overload(QPointerEvent)
  @overload(NoneType)
  def firstPointLocalVelocity(
      self,
      event: Optional[QPointerEvent],
  ) -> QVector2D:
    """
    Calls Qt's 'QVector2D
    QQuickFlickablePrivate::firstPointLocalVelocity(QPointerEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickableprivate.html

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D
    #      QQuickFlickablePrivate::firstPointLocalVelocity(QPointerEvent
    #      *event)
    address = self.uglySide.call(
        'ritual_ZN22QQuickFlickablePrivate23firstPointLocalVelocityEP13QPoi'
        'nterEvent',
        self._addressOf(event),
    )
    from ..QtGui import QVector2D
    return QVector2D._cuteOwning(address)

  @staticmethod
  def adjustContentPos(*__, **_) -> Never:
    """
    Qt's 'void QQuickFlickablePrivate::adjustContentPos(AxisData &data, qreal
    toPos)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickFlickablePrivate.adjustContentPos' has no cute function "
        "yet. Qt's 'void QQuickFlickablePrivate::adjustContentPos(AxisData "
        "&data, qreal toPos)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def fixup(*__, **_) -> Never:
    """
    Qt's 'void QQuickFlickablePrivate::fixup(AxisData &data, qreal minExtent,
    qreal maxExtent)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickFlickablePrivate.fixup' has no cute function yet. Qt's "
        "'void QQuickFlickablePrivate::fixup(AxisData &data, qreal "
        "minExtent, qreal maxExtent)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def fixupX_callback(*__, **_) -> Never:
    """
    Qt's 'void QQuickFlickablePrivate::fixupX_callback(void *a0)': names
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickFlickablePrivate.fixupX_callback' has no cute function yet. "
        "Qt's 'void QQuickFlickablePrivate::fixupX_callback(void *a0)': "
        "names 'void', which has no cute class yet.")

  @staticmethod
  def fixupY_callback(*__, **_) -> Never:
    """
    Qt's 'void QQuickFlickablePrivate::fixupY_callback(void *a0)': names
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickFlickablePrivate.fixupY_callback' has no cute function yet. "
        "Qt's 'void QQuickFlickablePrivate::fixupY_callback(void *a0)': "
        "names 'void', which has no cute class yet.")

  @staticmethod
  def flick(*__, **_) -> Never:
    """
    Qt's 'bool QQuickFlickablePrivate::flick(AxisData &data, qreal minExtent,
    qreal maxExtent, qreal vSize, QQuickTimeLineCallback::Callback
    fixupCallback, QEvent::Type eventType, qreal velocity)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickFlickablePrivate.flick' has no cute function yet. Qt's "
        "'bool QQuickFlickablePrivate::flick(AxisData &data, qreal "
        "minExtent, qreal maxExtent, qreal vSize, "
        "QQuickTimeLineCallback::Callback fixupCallback, QEvent::Type "
        "eventType, qreal velocity)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def resetTimeline(*__, **_) -> Never:
    """
    Qt's 'void QQuickFlickablePrivate::resetTimeline(AxisData &data)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickFlickablePrivate.resetTimeline' has no cute function yet. "
        "Qt's 'void QQuickFlickablePrivate::resetTimeline(AxisData &data)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def viewportAxisMoved(*__, **_) -> Never:
    """
    Qt's 'void QQuickFlickablePrivate::viewportAxisMoved(AxisData &data,
    qreal minExtent, qreal maxExtent, QQuickTimeLineCallback::Callback
    fixupCallback)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickFlickablePrivate.viewportAxisMoved' has no cute function "
        "yet. Qt's 'void QQuickFlickablePrivate::viewportAxisMoved(AxisData "
        "&data, qreal minExtent, qreal maxExtent, "
        "QQuickTimeLineCallback::Callback fixupCallback)': takes a type "
        "Python has no way to hand over yet.")
