"""
QQuickDeliveryAgentPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickdeliveryagent_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickDeliveryAgentPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QEvent, QList, QObjectPrivate
from ..QtGui import QPointingDevice, QPointingDevicePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject, QPoint, QPointF
  from ..QtGui import QContextMenuEvent, QEventPoint, QInputDevice, QKeyEvent
  from ..QtGui import QMouseEvent, QMutableSinglePointEvent, QPointerEvent
  from ..QtGui import QTouchEvent, QVector2D
  from . import QQuickDeliveryAgent, QQuickDragGrabber, QQuickItem
  from . import QQuickPointingDeviceExtra, QQuickWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QContextMenuEvent = WAIT['QContextMenuEvent']
  QEventPoint = WAIT['QEventPoint']
  QInputDevice = WAIT['QInputDevice']
  QKeyEvent = WAIT['QKeyEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QMutableSinglePointEvent = WAIT['QMutableSinglePointEvent']
  QObject = WAIT['QObject']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QPointerEvent = WAIT['QPointerEvent']
  QQuickDragGrabber = WAIT['QQuickDragGrabber']
  QQuickItem = WAIT['QQuickItem']
  QQuickWindow = WAIT['QQuickWindow']
  QTouchEvent = WAIT['QTouchEvent']
  QVector2D = WAIT['QVector2D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickDeliveryAgentPrivate(QObjectPrivate):
  """
  The cute side of Qt's QQuickDeliveryAgentPrivate: a plain Python object
  standing in front of one C++ QQuickDeliveryAgentPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QQuickDeliveryAgentPrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickDeliveryAgentPrivate that has a ritual and
  that Python can call so far, 64 names in all: 'q_func', 'deliverKeyEvent',
  'setFocusInScope', 'clearFocusInScope', 'clearFocusObject',
  'updateFocusItemTransform', 'focusTargetItem',
  'currentOrItemDeliveryAgent', 'isDeliveringTouchAsMouse',
  'cancelTouchMouseSynthesis', 'checkIfDoubleTapped',
  'resetIfDoubleTapPrevented', 'mousePointData', 'eventInDelivery',
  'deliverTouchAsMouse', 'translateTouchEvent', 'removeGrabber',
  'clearGrabbers', 'onGrabChanged', 'sendFilteredMouseEvent',
  'sendFilteredPointerEvent', 'sendFilteredPointerEventImpl',
  'deliverSinglePointEventUntilAccepted', 'handleTouchEvent',
  'handleMouseEvent', 'compressTouchEvent', 'flushFrameSynchronousEvents',
  'deliverDelayedTouchEvent', 'handleWindowDeactivate', 'handleWindowHidden',
  'allUpdatedPointsAccepted', 'localizePointerEvent', 'exclusiveGrabbers',
  'anyPointGrabbed', 'allPointsGrabbed', 'isMouseEvent',
  'isMouseOrWheelEvent', 'isHoverEvent', 'isTouchEvent', 'isTabletEvent',
  'isEventFromMouseOrTouchpad', 'isSynthMouse',
  'isWithinDoubleClickInterval', 'isWithinDoubleTapDistance',
  'isSinglePointDevice', 'deviceExtra', 'touchToMouseEvent',
  'ensureDeviceConnected', 'deliverPointerEvent', 'deliverTouchCancelEvent',
  'deliverPressOrReleaseEvent', 'deliverUpdatedPoints',
  'deliverMatchingPointsToItem', 'pointerTargets', 'mergePointerTargets',
  'deliverHoverEvent', 'deliverHoverEventRecursive',
  'deliverHoverEventToItem', 'sendHoverEvent', 'clearHover',
  'deliverDragEvent', 'dragOverThreshold', 'contextMenuTargets',
  'deliverContextMenuEvent'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickDeliveryAgent *QQuickDeliveryAgentPrivate::q_func()
    const': takes in Python what 'QQuickDeliveryAgent
    *QQuickDeliveryAgentPrivate::q_func()' takes.
  - Qt's 'QQuickDeliveryAgentPrivate::~QQuickDeliveryAgentPrivate()': the
    destructor: Python never removes a C++ QQuickDeliveryAgentPrivate.
  - Qt's 'void QQuickDeliveryAgentPrivate::notifyFocusChangesRecur(QQuickItem
    **item, int remaining, Qt::FocusReason reason)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QPointerEvent
    *QQuickDeliveryAgentPrivate::clonePointerEvent(QPointerEvent *event,
    std::optional<QPointF> transformedLocalPos)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QQuickDeliveryAgentPrivate::deliverToPassiveGrabbers(const
    QList<QPointer<QObject>> &passiveGrabbers, QPointerEvent *pointerEvent)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QList<QQuickItem *>
    QQuickDeliveryAgentPrivate::eventTargets(QQuickItem *a0, const QEvent
    *event, int pointId, QPointF localPos, QPointF scenePos,
    qxp::function_ref<std::optional<bool> (QQuickItem *, const QEvent *)>
    predicate) const': takes a type Python has no way to hand over yet.
  - Qt's 'void QQuickDeliveryAgentPrivate::eventTargetsAppend(QQuickItem *a0,
    const QEvent *event, int pointId, QPointF localPos, QPointF scenePos,
    qxp::function_ref<std::optional<bool> (QQuickItem *, const QEvent *)>
    predicate, QList<QQuickItem *> &targets) const': takes a type Python has
    no way to hand over yet.
  - Qt's 'bool QQuickDeliveryAgentPrivate::deliverDragEvent(QQuickDragGrabber
    *a0, QQuickItem *a1, QDragMoveEvent *a2, QVarLengthArray<QQuickItem *,
    64> *currentGrabItems, QObject *formerTarget)': names
    'QVarLengthArray<QQuickItem *, 64>', which has no cute class yet.

  What has no ritual
  ------------------

  1 of the 76 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QQuickDeliveryAgentPrivate is created at the first use, not by
    'QQuickDeliveryAgentPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickDeliveryAgentPrivate.
  - Each name of Qt's QQuickDeliveryAgentPrivate that has no cute function
    yet, 'clonePointerEvent', 'deliverToPassiveGrabbers', 'eventTargets',
    'eventTargetsAppend', 'isHoveringMoveEvent', 'notifyFocusChangesRecur',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QQuickDeliveryAgentPrivate, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class FocusOption(CuteFlags):
    """
    The flags enum 'QQuickDeliveryAgentPrivate::FocusOption' of Qt, with the
    2 names Qt gives in it. Qt names the type of its combinations
    'QQuickDeliveryAgentPrivate::FocusOptions'.
    """

    DontChangeFocusProperty = 0x1
    DontChangeSubFocusItem = 0x2

  FocusOptions = FocusOption

  class HoverChange(CuteNum, scoped=True):
    """
    The enum 'QQuickDeliveryAgentPrivate::HoverChange' of Qt, with the 2
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    Clear = Kee[int](0)
    Set = Kee[int](1)

  #  The classes Qt writes inside QQuickDeliveryAgentPrivate, each a class in
  #  here as in C++.

  class HoverItemState(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickDeliveryAgentPrivate::HoverItemState: a plain
    Python object standing in front of one C++
    QQuickDeliveryAgentPrivate::HoverItemState.

    C++ hands a QQuickDeliveryAgentPrivate::HoverItemState around as a copy,
    so every C++ QQuickDeliveryAgentPrivate::HoverItemState behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QQuickDeliveryAgentPrivate::HoverItemState yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickDeliveryAgentPrivate::HoverItemState::~HoverItemState()':
      the destructor: Python removes its C++
      QQuickDeliveryAgentPrivate::HoverItemState by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QQuickDeliveryAgentPrivate::HoverItemState is created at the
      first use, not by 'QQuickDeliveryAgentPrivate::HoverItemState(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickDeliveryAgentPrivate::HoverItemState back
      gives a copy the ritual made for Python, in a new cute
      QQuickDeliveryAgentPrivate::HoverItemState.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickDeliveryAgentPrivate::HoverItemState'

    #  Qt's '~QQuickDeliveryAgentPrivate::HoverItemState()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QQuickDeliveryAgentPrivate::HoverItemState behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN26QQuickDeliveryAgentPrivate14HoverItemStateD1Ev')

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickItem)
  @overload(NoneType)
  def currentOrItemDeliveryAgent(
      item: Optional[QQuickItem],
  ) -> Optional[QQuickDeliveryAgent]:
    """
    Calls Qt's 'QQuickDeliveryAgent
    *QQuickDeliveryAgentPrivate::currentOrItemDeliveryAgent(const QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickDeliveryAgent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDeliveryAgent
    #      *QQuickDeliveryAgentPrivate::currentOrItemDeliveryAgent(const
    #      QQuickItem *item)
    address = Rituals.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate26currentOrItemDeliveryAgentE'
        'PK10QQuickItem',
        CuteMixin._addressOf(item),
    )
    from . import QQuickDeliveryAgent
    return QQuickDeliveryAgent._cuteAt(address)

  @staticmethod
  @overload(QTouchEvent)
  @overload(NoneType)
  def translateTouchEvent(touchEvent: Optional[QTouchEvent]) -> None:
    """
    Calls Qt's 'void
    QQuickDeliveryAgentPrivate::translateTouchEvent(QTouchEvent
    *touchEvent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html

    Parameters
    ----------

    touchEvent : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDeliveryAgentPrivate::translateTouchEvent(QTouchEvent
    #      *touchEvent)
    Rituals.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate19translateTouchEventEP11QTou'
        'chEvent',
        CuteMixin._addressOf(touchEvent),
    )

  @staticmethod
  @overload(QPointerEvent, QQuickItem)
  @overload(QPointerEvent, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def localizePointerEvent(
      ev: Optional[QPointerEvent],
      dest: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickDeliveryAgentPrivate::localizePointerEvent(QPointerEvent *ev, const
    QQuickItem *dest)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html

    Parameters
    ----------

    ev : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dest : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDeliveryAgentPrivate::localizePointerEvent(QPointerEvent
    #      *ev, const QQuickItem *dest)
    Rituals.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate20localizePointerEventEP13QPo'
        'interEventPK10QQuickItem',
        CuteMixin._addressOf(ev), CuteMixin._addressOf(dest),
    )

  @staticmethod
  @overload(QPointerEvent)
  @overload(NoneType)
  def anyPointGrabbed(ev: Optional[QPointerEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickDeliveryAgentPrivate::anyPointGrabbed(const
    QPointerEvent *ev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#anyPointGrabbed

    Parameters
    ----------

    ev : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDeliveryAgentPrivate::anyPointGrabbed(const QPointerEvent
    #      *ev)
    return Rituals.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate15anyPointGrabbedEPK13QPointe'
        'rEvent',
        CuteMixin._addressOf(ev),
    )

  @staticmethod
  @overload(QPointerEvent)
  @overload(NoneType)
  def allPointsGrabbed(ev: Optional[QPointerEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickDeliveryAgentPrivate::allPointsGrabbed(const
    QPointerEvent *ev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#allPointsGrabbed

    Parameters
    ----------

    ev : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDeliveryAgentPrivate::allPointsGrabbed(const QPointerEvent
    #      *ev)
    return Rituals.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate16allPointsGrabbedEPK13QPoint'
        'erEvent',
        CuteMixin._addressOf(ev),
    )

  @staticmethod
  @overload(QPointerEvent)
  @overload(NoneType)
  def isMouseEvent(ev: Optional[QPointerEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickDeliveryAgentPrivate::isMouseEvent(const
    QPointerEvent *ev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#isMouseEvent

    Parameters
    ----------

    ev : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDeliveryAgentPrivate::isMouseEvent(const QPointerEvent *ev)
    return Rituals.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate12isMouseEventEPK13QPointerEv'
        'ent',
        CuteMixin._addressOf(ev),
    )

  @staticmethod
  @overload(QPointerEvent)
  @overload(NoneType)
  def isMouseOrWheelEvent(ev: Optional[QPointerEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickDeliveryAgentPrivate::isMouseOrWheelEvent(const
    QPointerEvent *ev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html

    Parameters
    ----------

    ev : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDeliveryAgentPrivate::isMouseOrWheelEvent(const
    #      QPointerEvent *ev)
    return Rituals.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate19isMouseOrWheelEventEPK13QPo'
        'interEvent',
        CuteMixin._addressOf(ev),
    )

  @staticmethod
  @overload(QPointerEvent)
  @overload(NoneType)
  def isHoverEvent(ev: Optional[QPointerEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickDeliveryAgentPrivate::isHoverEvent(const
    QPointerEvent *ev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#isHoverEvent

    Parameters
    ----------

    ev : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDeliveryAgentPrivate::isHoverEvent(const QPointerEvent *ev)
    return Rituals.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate12isHoverEventEPK13QPointerEv'
        'ent',
        CuteMixin._addressOf(ev),
    )

  @staticmethod
  @overload(QPointerEvent)
  @overload(NoneType)
  def isTouchEvent(ev: Optional[QPointerEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickDeliveryAgentPrivate::isTouchEvent(const
    QPointerEvent *ev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#isTouchEvent

    Parameters
    ----------

    ev : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDeliveryAgentPrivate::isTouchEvent(const QPointerEvent *ev)
    return Rituals.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate12isTouchEventEPK13QPointerEv'
        'ent',
        CuteMixin._addressOf(ev),
    )

  @staticmethod
  @overload(QPointerEvent)
  @overload(NoneType)
  def isTabletEvent(ev: Optional[QPointerEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickDeliveryAgentPrivate::isTabletEvent(const
    QPointerEvent *ev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#isTabletEvent

    Parameters
    ----------

    ev : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDeliveryAgentPrivate::isTabletEvent(const QPointerEvent
    #      *ev)
    return Rituals.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate13isTabletEventEPK13QPointerE'
        'vent',
        CuteMixin._addressOf(ev),
    )

  @staticmethod
  @overload(QPointerEvent)
  @overload(NoneType)
  def isEventFromMouseOrTouchpad(ev: Optional[QPointerEvent]) -> bool:
    """
    Calls Qt's 'bool
    QQuickDeliveryAgentPrivate::isEventFromMouseOrTouchpad(const
    QPointerEvent *ev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html

    Parameters
    ----------

    ev : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDeliveryAgentPrivate::isEventFromMouseOrTouchpad(const
    #      QPointerEvent *ev)
    return Rituals.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate26isEventFromMouseOrTouchpadE'
        'PK13QPointerEvent',
        CuteMixin._addressOf(ev),
    )

  @staticmethod
  @overload(QPointerEvent)
  @overload(NoneType)
  def isSynthMouse(ev: Optional[QPointerEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickDeliveryAgentPrivate::isSynthMouse(const
    QPointerEvent *ev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#isSynthMouse

    Parameters
    ----------

    ev : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDeliveryAgentPrivate::isSynthMouse(const QPointerEvent *ev)
    return Rituals.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate12isSynthMouseEPK13QPointerEv'
        'ent',
        CuteMixin._addressOf(ev),
    )

  @staticmethod
  @overload(int)
  def isWithinDoubleClickInterval(timeInterval: int) -> bool:
    """
    Calls Qt's 'bool
    QQuickDeliveryAgentPrivate::isWithinDoubleClickInterval(ulong
    timeInterval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html

    Parameters
    ----------

    timeInterval : int
      Passed on as it is.
    """
    #  bool QQuickDeliveryAgentPrivate::isWithinDoubleClickInterval(ulong
    #      timeInterval)
    return Rituals.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate27isWithinDoubleClickInterval'
        'Em',
        timeInterval,
    )

  @staticmethod
  @overload(QPoint)
  def isWithinDoubleTapDistance(distanceBetweenPresses: QPoint) -> bool:
    """
    Calls Qt's 'bool
    QQuickDeliveryAgentPrivate::isWithinDoubleTapDistance(const QPoint
    &distanceBetweenPresses)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html

    Parameters
    ----------

    distanceBetweenPresses : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  bool QQuickDeliveryAgentPrivate::isWithinDoubleTapDistance(const
    #      QPoint &distanceBetweenPresses)
    return Rituals.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate25isWithinDoubleTapDistanceER'
        'K6QPoint',
        CuteMixin._valueOf(distanceBetweenPresses),
    )

  @staticmethod
  @overload(QInputDevice)
  @overload(NoneType)
  def isSinglePointDevice(dev: Optional[QInputDevice]) -> bool:
    """
    Calls Qt's 'bool QQuickDeliveryAgentPrivate::isSinglePointDevice(const
    QInputDevice *dev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html

    Parameters
    ----------

    dev : Optional[QInputDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDeliveryAgentPrivate::isSinglePointDevice(const
    #      QInputDevice *dev)
    return Rituals.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate19isSinglePointDeviceEPK12QIn'
        'putDevice',
        CuteMixin._addressOf(dev),
    )

  @staticmethod
  @overload(QInputDevice)
  @overload(NoneType)
  def deviceExtra(
      device: Optional[QInputDevice],
  ) -> Optional[QQuickPointingDeviceExtra]:
    """
    Calls Qt's 'QQuickPointingDeviceExtra
    *QQuickDeliveryAgentPrivate::deviceExtra(const QInputDevice *device)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#deviceExtra

    Parameters
    ----------

    device : Optional[QInputDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickPointingDeviceExtra]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPointingDeviceExtra
    #      *QQuickDeliveryAgentPrivate::deviceExtra(const QInputDevice
    #      *device)
    address = Rituals.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate11deviceExtraEPK12QInputDevic'
        'e',
        CuteMixin._addressOf(device),
    )
    from . import QQuickPointingDeviceExtra
    return QQuickPointingDeviceExtra._cuteAt(address)

  @staticmethod
  @overload(float, Qt.Axis, QMouseEvent)
  @overload(float, Qt.Axis, NoneType)
  @overload(float, Qt.Axis, QMouseEvent, int)
  @overload(float, Qt.Axis, NoneType, int)
  def dragOverThreshold(
      d: float,
      axis: Qt.Axis,
      event: Optional[QMouseEvent],
      startDragThreshold: int = -1,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickDeliveryAgentPrivate::dragOverThreshold(qreal d,
    Qt::Axis axis, QMouseEvent *event, int startDragThreshold)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#dragOverThreshold

    Parameters
    ----------

    d : float
      Passed on as it is.

    axis : Qt.Axis
      Passed on as its number.

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    startDragThreshold : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  bool QQuickDeliveryAgentPrivate::dragOverThreshold(qreal d, Qt::Axis
    #      axis, QMouseEvent *event, int startDragThreshold)
    return Rituals.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate17dragOverThresholdEdN2Qt4Axi'
        'sEP11QMouseEventi',
        d, axis.value, CuteMixin._addressOf(event), startDragThreshold,
    )

  @staticmethod
  @overload(float, Qt.Axis, QEventPoint)
  @overload(float, Qt.Axis, QEventPoint, int)
  def dragOverThreshold(
      d: float,
      axis: Qt.Axis,
      tp: QEventPoint,
      startDragThreshold: int = -1,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickDeliveryAgentPrivate::dragOverThreshold(qreal d,
    Qt::Axis axis, const QEventPoint &tp, int startDragThreshold)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#dragOverThreshold

    Parameters
    ----------

    d : float
      Passed on as it is.

    axis : Qt.Axis
      Passed on as its number.

    tp : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.

    startDragThreshold : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  bool QQuickDeliveryAgentPrivate::dragOverThreshold(qreal d, Qt::Axis
    #      axis, const QEventPoint &tp, int startDragThreshold)
    return Rituals.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate17dragOverThresholdEdN2Qt4Axi'
        'sERK11QEventPointi',
        d, axis.value, CuteMixin._valueOf(tp), startDragThreshold,
    )

  @staticmethod
  @overload(QVector2D)
  def dragOverThreshold(delta: QVector2D) -> bool:
    """
    Calls Qt's 'bool QQuickDeliveryAgentPrivate::dragOverThreshold(QVector2D
    delta)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#dragOverThreshold

    Parameters
    ----------

    delta : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  bool QQuickDeliveryAgentPrivate::dragOverThreshold(QVector2D delta)
    return Rituals.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate17dragOverThresholdE9QVector2'
        'D',
        CuteMixin._valueOf(delta),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickDeliveryAgentPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def focusTargetItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickDeliveryAgentPrivate::focusTargetItem()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#focusTargetItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickDeliveryAgentPrivate::focusTargetItem() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickDeliveryAgentPrivate15focusTargetItemEv',
    )
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def isDeliveringTouchAsMouse(self) -> bool:
    """
    Calls Qt's 'bool QQuickDeliveryAgentPrivate::isDeliveringTouchAsMouse()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html
    """
    #  bool QQuickDeliveryAgentPrivate::isDeliveringTouchAsMouse() const
    return self.uglySide.call(
        'ritual_ZNK26QQuickDeliveryAgentPrivate24isDeliveringTouchAsMouseEv',
    )

  def eventInDelivery(self) -> Optional[QPointerEvent]:
    """
    Calls Qt's 'QPointerEvent *QQuickDeliveryAgentPrivate::eventInDelivery()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#eventInDelivery

    Returns
    -------

    Optional[QPointerEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPointerEvent *QQuickDeliveryAgentPrivate::eventInDelivery() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickDeliveryAgentPrivate15eventInDeliveryEv',
    )
    from ..QtGui import QPointerEvent
    return QPointerEvent._cuteAt(address)

  @overload(QQuickItem, QPointerEvent, QEventPoint, bool, bool)
  @overload(QQuickItem, NoneType, QEventPoint, bool, bool)
  @overload(NoneType, QPointerEvent, QEventPoint, bool, bool)
  @overload(NoneType, NoneType, QEventPoint, bool, bool)
  def pointerTargets(
      self,
      a0: Optional[QQuickItem],
      event: Optional[QPointerEvent],
      point: QEventPoint,
      checkMouseButtons: bool,
      checkAcceptsTouch: bool,
  ) -> QList[QQuickItem]:
    """
    Calls Qt's 'QList<QQuickItem *>
    QQuickDeliveryAgentPrivate::pointerTargets(QQuickItem *a0, const
    QPointerEvent *event, const QEventPoint &point, bool checkMouseButtons,
    bool checkAcceptsTouch) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#pointerTargets

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.

    checkMouseButtons : bool
      Passed on as it is.

    checkAcceptsTouch : bool
      Passed on as it is.

    Returns
    -------

    QList[QQuickItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQuickItem *>
    #      QQuickDeliveryAgentPrivate::pointerTargets(QQuickItem *a0, const
    #      QPointerEvent *event, const QEventPoint &point, bool
    #      checkMouseButtons, bool checkAcceptsTouch) const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickDeliveryAgentPrivate14pointerTargetsEP10QQuickIt'
        'emPK13QPointerEventRK11QEventPointbb',
        self._addressOf(a0), self._addressOf(event), self._valueOf(point),
        checkMouseButtons, checkAcceptsTouch,
    )
    from . import QQuickItem
    return QList[QQuickItem]._cuteOwning(address)

  @overload(QList[QQuickItem], QList[QQuickItem])
  def mergePointerTargets(
      self,
      list1: QList[QQuickItem],
      list2: QList[QQuickItem],
  ) -> QList[QQuickItem]:
    """
    Calls Qt's 'QList<QQuickItem *>
    QQuickDeliveryAgentPrivate::mergePointerTargets(const QList<QQuickItem *>
    &list1, const QList<QQuickItem *> &list2) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html

    Parameters
    ----------

    list1 : QList[QQuickItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    list2 : QList[QQuickItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QList[QQuickItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQuickItem *>
    #      QQuickDeliveryAgentPrivate::mergePointerTargets(const
    #      QList<QQuickItem *> &list1, const QList<QQuickItem *> &list2)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickDeliveryAgentPrivate19mergePointerTargetsERK5QLi'
        'stIP10QQuickItemES5_',
        self._valueOf(list1), self._valueOf(list2),
    )
    from . import QQuickItem
    return QList[QQuickItem]._cuteOwning(address)

  @overload(QQuickItem, QContextMenuEvent)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QContextMenuEvent)
  @overload(NoneType, NoneType)
  def contextMenuTargets(
      self,
      item: Optional[QQuickItem],
      event: Optional[QContextMenuEvent],
  ) -> QList[QQuickItem]:
    """
    Calls Qt's 'QList<QQuickItem *>
    QQuickDeliveryAgentPrivate::contextMenuTargets(QQuickItem *item, const
    QContextMenuEvent *event) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#contextMenuTargets

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QContextMenuEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QList[QQuickItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQuickItem *>
    #      QQuickDeliveryAgentPrivate::contextMenuTargets(QQuickItem *item,
    #      const QContextMenuEvent *event) const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickDeliveryAgentPrivate18contextMenuTargetsEP10QQui'
        'ckItemPK17QContextMenuEvent',
        self._addressOf(item), self._addressOf(event),
    )
    from . import QQuickItem
    return QList[QQuickItem]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickItem, QQuickItem, Qt.FocusReason)
  @overload(QQuickItem, NoneType, Qt.FocusReason)
  @overload(NoneType, QQuickItem, Qt.FocusReason)
  @overload(NoneType, NoneType, Qt.FocusReason)
  @overload(QQuickItem, QQuickItem, Qt.FocusReason, FocusOptions)
  @overload(QQuickItem, NoneType, Qt.FocusReason, FocusOptions)
  @overload(NoneType, QQuickItem, Qt.FocusReason, FocusOptions)
  @overload(NoneType, NoneType, Qt.FocusReason, FocusOptions)
  def setFocusInScope(
      self,
      scope: Optional[QQuickItem],
      item: Optional[QQuickItem],
      reason: Qt.FocusReason,
      a3: FocusOptions = FocusOptions(),
  ) -> None:
    """
    Calls Qt's 'void QQuickDeliveryAgentPrivate::setFocusInScope(QQuickItem
    *scope, QQuickItem *item, Qt::FocusReason reason, FocusOptions a3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#setFocusInScope

    Parameters
    ----------

    scope : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    reason : Qt.FocusReason
      Passed on as its number.

    a3 : FocusOptions
      Passed on as its number. May be left out, as in Qt: it is then
      FocusOptions().
    """
    #  void QQuickDeliveryAgentPrivate::setFocusInScope(QQuickItem *scope,
    #      QQuickItem *item, Qt::FocusReason reason, FocusOptions a3)
    self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate15setFocusInScopeEP10QQuickIt'
        'emS1_N2Qt11FocusReasonE6QFlagsINS_11FocusOptionEE',
        self._addressOf(scope), self._addressOf(item), reason.value,
        a3.value,
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

  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, root: Optional[QQuickItem]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickDeliveryAgentPrivate::QQuickDeliveryAgentPrivate(QQuickItem
    *root)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html

    Parameters
    ----------

    root : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickDeliveryAgentPrivate::QQuickDeliveryAgentPrivate(QQuickItem
    #      *root)
    self._noteCreation(QQuickDeliveryAgentPrivate, lambda: Rituals.call(
        'ritual_ZN26QQuickDeliveryAgentPrivateC1EP10QQuickItem',
        self._addressOf(root),
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

  def q_func(self) -> Optional[QQuickDeliveryAgent]:
    """
    Calls Qt's 'QQuickDeliveryAgent *QQuickDeliveryAgentPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#q_func

    Returns
    -------

    Optional[QQuickDeliveryAgent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDeliveryAgent *QQuickDeliveryAgentPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate6q_funcEv',
    )
    from . import QQuickDeliveryAgent
    return QQuickDeliveryAgent._cuteAt(address)

  @overload(QKeyEvent)
  @overload(NoneType)
  def deliverKeyEvent(self, e: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickDeliveryAgentPrivate::deliverKeyEvent(QKeyEvent
    *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#deliverKeyEvent

    Parameters
    ----------

    e : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDeliveryAgentPrivate::deliverKeyEvent(QKeyEvent *e)
    self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate15deliverKeyEventEP9QKeyEvent',
        self._addressOf(e),
    )

  @overload(QQuickItem, QQuickItem, Qt.FocusReason)
  @overload(QQuickItem, NoneType, Qt.FocusReason)
  @overload(NoneType, QQuickItem, Qt.FocusReason)
  @overload(NoneType, NoneType, Qt.FocusReason)
  @overload(QQuickItem, QQuickItem, Qt.FocusReason, FocusOptions)
  @overload(QQuickItem, NoneType, Qt.FocusReason, FocusOptions)
  @overload(NoneType, QQuickItem, Qt.FocusReason, FocusOptions)
  @overload(NoneType, NoneType, Qt.FocusReason, FocusOptions)
  def clearFocusInScope(
      self,
      scope: Optional[QQuickItem],
      item: Optional[QQuickItem],
      reason: Qt.FocusReason,
      a3: FocusOptions = FocusOptions(),
  ) -> None:
    """
    Calls Qt's 'void QQuickDeliveryAgentPrivate::clearFocusInScope(QQuickItem
    *scope, QQuickItem *item, Qt::FocusReason reason, FocusOptions a3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#clearFocusInScope

    Parameters
    ----------

    scope : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    reason : Qt.FocusReason
      Passed on as its number.

    a3 : FocusOptions
      Passed on as its number. May be left out, as in Qt: it is then
      FocusOptions().
    """
    #  void QQuickDeliveryAgentPrivate::clearFocusInScope(QQuickItem *scope,
    #      QQuickItem *item, Qt::FocusReason reason, FocusOptions a3)
    self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate17clearFocusInScopeEP10QQuick'
        'ItemS1_N2Qt11FocusReasonE6QFlagsINS_11FocusOptionEE',
        self._addressOf(scope), self._addressOf(item), reason.value,
        a3.value,
    )

  def clearFocusObject(self) -> None:
    """
    Calls Qt's 'void QQuickDeliveryAgentPrivate::clearFocusObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#clearFocusObject
    """
    #  void QQuickDeliveryAgentPrivate::clearFocusObject()
    self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate16clearFocusObjectEv',
    )

  def updateFocusItemTransform(self) -> None:
    """
    Calls Qt's 'void QQuickDeliveryAgentPrivate::updateFocusItemTransform()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html
    """
    #  void QQuickDeliveryAgentPrivate::updateFocusItemTransform()
    self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate24updateFocusItemTransformEv',
    )

  def cancelTouchMouseSynthesis(self) -> None:
    """
    Calls Qt's 'void
    QQuickDeliveryAgentPrivate::cancelTouchMouseSynthesis()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html
    """
    #  void QQuickDeliveryAgentPrivate::cancelTouchMouseSynthesis()
    self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate25cancelTouchMouseSynthesisEv',
    )

  @overload(int, QPoint)
  def checkIfDoubleTapped(
      self,
      newPressEventTimestamp: int,
      newPressPos: QPoint,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickDeliveryAgentPrivate::checkIfDoubleTapped(ulong
    newPressEventTimestamp, const QPoint &newPressPos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html

    Parameters
    ----------

    newPressEventTimestamp : int
      Passed on as it is.

    newPressPos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  bool QQuickDeliveryAgentPrivate::checkIfDoubleTapped(ulong
    #      newPressEventTimestamp, const QPoint &newPressPos)
    return self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate19checkIfDoubleTappedEmRK6QPo'
        'int',
        newPressEventTimestamp, self._valueOf(newPressPos),
    )

  @overload(QEventPoint)
  def resetIfDoubleTapPrevented(self, pressedPoint: QEventPoint) -> None:
    """
    Calls Qt's 'void
    QQuickDeliveryAgentPrivate::resetIfDoubleTapPrevented(const QEventPoint
    &pressedPoint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html

    Parameters
    ----------

    pressedPoint : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.
    """
    #  void QQuickDeliveryAgentPrivate::resetIfDoubleTapPrevented(const
    #      QEventPoint &pressedPoint)
    self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate25resetIfDoubleTapPreventedER'
        'K11QEventPoint',
        self._valueOf(pressedPoint),
    )

  def mousePointData(
      self,
  ) -> Optional[QPointingDevicePrivate.EventPointData]:
    """
    Calls Qt's 'QPointingDevicePrivate::EventPointData
    *QQuickDeliveryAgentPrivate::mousePointData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#mousePointData

    Returns
    -------

    Optional[QPointingDevicePrivate.EventPointData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPointingDevicePrivate::EventPointData
    #      *QQuickDeliveryAgentPrivate::mousePointData()
    address = self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate14mousePointDataEv',
    )
    return QPointingDevicePrivate.EventPointData._cuteAt(address)

  @overload(QQuickItem, QTouchEvent)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QTouchEvent)
  @overload(NoneType, NoneType)
  def deliverTouchAsMouse(
      self,
      item: Optional[QQuickItem],
      pointerEvent: Optional[QTouchEvent],
  ) -> bool:
    """
    Calls Qt's 'bool
    QQuickDeliveryAgentPrivate::deliverTouchAsMouse(QQuickItem *item,
    QTouchEvent *pointerEvent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pointerEvent : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDeliveryAgentPrivate::deliverTouchAsMouse(QQuickItem *item,
    #      QTouchEvent *pointerEvent)
    return self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate19deliverTouchAsMouseEP10QQui'
        'ckItemP11QTouchEvent',
        self._addressOf(item), self._addressOf(pointerEvent),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  @overload(QQuickItem, bool)
  @overload(NoneType, bool)
  @overload(QQuickItem, bool, bool)
  @overload(NoneType, bool, bool)
  @overload(QQuickItem, bool, bool, bool)
  @overload(NoneType, bool, bool, bool)
  def removeGrabber(
      self,
      grabber: Optional[QQuickItem],
      mouse: bool = True,
      touch: bool = True,
      cancel: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QQuickDeliveryAgentPrivate::removeGrabber(QQuickItem
    *grabber, bool mouse, bool touch, bool cancel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#removeGrabber

    Parameters
    ----------

    grabber : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mouse : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    touch : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    cancel : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickDeliveryAgentPrivate::removeGrabber(QQuickItem *grabber,
    #      bool mouse, bool touch, bool cancel)
    self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate13removeGrabberEP10QQuickItem'
        'bbb',
        self._addressOf(grabber), mouse, touch, cancel,
    )

  @overload(QPointerEvent)
  @overload(NoneType)
  def clearGrabbers(self, pointerEvent: Optional[QPointerEvent]) -> None:
    """
    Calls Qt's 'void QQuickDeliveryAgentPrivate::clearGrabbers(QPointerEvent
    *pointerEvent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#clearGrabbers

    Parameters
    ----------

    pointerEvent : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDeliveryAgentPrivate::clearGrabbers(QPointerEvent
    #      *pointerEvent)
    self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate13clearGrabbersEP13QPointerEv'
        'ent',
        self._addressOf(pointerEvent),
    )

  @overload(
      QObject, QPointingDevice.GrabTransition, QPointerEvent, QEventPoint,
  )
  @overload(QObject, QPointingDevice.GrabTransition, NoneType, QEventPoint)
  @overload(
      NoneType, QPointingDevice.GrabTransition, QPointerEvent, QEventPoint,
  )
  @overload(NoneType, QPointingDevice.GrabTransition, NoneType, QEventPoint)
  def onGrabChanged(
      self,
      grabber: Optional[QObject],
      transition: QPointingDevice.GrabTransition,
      event: Optional[QPointerEvent],
      point: QEventPoint,
  ) -> None:
    """
    Calls Qt's 'void QQuickDeliveryAgentPrivate::onGrabChanged(QObject
    *grabber, QPointingDevice::GrabTransition transition, const QPointerEvent
    *event, const QEventPoint &point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#onGrabChanged

    Parameters
    ----------

    grabber : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    transition : QPointingDevice.GrabTransition
      Passed on as its number.

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.
    """
    #  void QQuickDeliveryAgentPrivate::onGrabChanged(QObject *grabber,
    #      QPointingDevice::GrabTransition transition, const QPointerEvent
    #      *event, const QEventPoint &point)
    self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate13onGrabChangedEP7QObjectN15Q'
        'PointingDevice14GrabTransitionEPK13QPointerEventRK11QEventPoint',
        self._addressOf(grabber, 'QObject'), transition.value,
        self._addressOf(event), self._valueOf(point),
    )

  @overload(QEvent, QQuickItem, QQuickItem)
  @overload(QEvent, QQuickItem, NoneType)
  @overload(QEvent, NoneType, QQuickItem)
  @overload(QEvent, NoneType, NoneType)
  @overload(NoneType, QQuickItem, QQuickItem)
  @overload(NoneType, QQuickItem, NoneType)
  @overload(NoneType, NoneType, QQuickItem)
  @overload(NoneType, NoneType, NoneType)
  def sendFilteredMouseEvent(
      self,
      event: Optional[QEvent],
      receiver: Optional[QQuickItem],
      filteringParent: Optional[QQuickItem],
  ) -> bool:
    """
    Calls Qt's 'bool
    QQuickDeliveryAgentPrivate::sendFilteredMouseEvent(QEvent *event,
    QQuickItem *receiver, QQuickItem *filteringParent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    receiver : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    filteringParent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDeliveryAgentPrivate::sendFilteredMouseEvent(QEvent *event,
    #      QQuickItem *receiver, QQuickItem *filteringParent)
    return self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate22sendFilteredMouseEventEP6QE'
        'ventP10QQuickItemS3_',
        self._addressOf(event), self._addressOf(receiver),
        self._addressOf(filteringParent),
    )

  @overload(QPointerEvent, QQuickItem)
  @overload(QPointerEvent, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  @overload(QPointerEvent, QQuickItem, QQuickItem)
  @overload(QPointerEvent, QQuickItem, NoneType)
  @overload(QPointerEvent, NoneType, QQuickItem)
  @overload(QPointerEvent, NoneType, NoneType)
  @overload(NoneType, QQuickItem, QQuickItem)
  @overload(NoneType, QQuickItem, NoneType)
  @overload(NoneType, NoneType, QQuickItem)
  @overload(NoneType, NoneType, NoneType)
  def sendFilteredPointerEvent(
      self,
      event: Optional[QPointerEvent],
      receiver: Optional[QQuickItem],
      filteringParent: Optional[QQuickItem] = None,
  ) -> bool:
    """
    Calls Qt's 'bool
    QQuickDeliveryAgentPrivate::sendFilteredPointerEvent(QPointerEvent
    *event, QQuickItem *receiver, QQuickItem *filteringParent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    receiver : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    filteringParent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  bool
    #      QQuickDeliveryAgentPrivate::sendFilteredPointerEvent(QPointerEvent
    #      *event, QQuickItem *receiver, QQuickItem *filteringParent)
    return self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate24sendFilteredPointerEventEP1'
        '3QPointerEventP10QQuickItemS3_',
        self._addressOf(event), self._addressOf(receiver),
        self._addressOf(filteringParent),
    )

  @overload(QPointerEvent, QQuickItem, QQuickItem)
  @overload(QPointerEvent, QQuickItem, NoneType)
  @overload(QPointerEvent, NoneType, QQuickItem)
  @overload(QPointerEvent, NoneType, NoneType)
  @overload(NoneType, QQuickItem, QQuickItem)
  @overload(NoneType, QQuickItem, NoneType)
  @overload(NoneType, NoneType, QQuickItem)
  @overload(NoneType, NoneType, NoneType)
  def sendFilteredPointerEventImpl(
      self,
      event: Optional[QPointerEvent],
      receiver: Optional[QQuickItem],
      filteringParent: Optional[QQuickItem],
  ) -> bool:
    """
    Calls Qt's 'bool
    QQuickDeliveryAgentPrivate::sendFilteredPointerEventImpl(QPointerEvent
    *event, QQuickItem *receiver, QQuickItem *filteringParent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    receiver : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    filteringParent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDeliveryAgentPrivate::sendFilteredPointerEventImpl(
    #      QPointerEvent *event, QQuickItem *receiver, QQuickItem
    #      *filteringParent)
    return self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate28sendFilteredPointerEventImp'
        'lEP13QPointerEventP10QQuickItemS3_',
        self._addressOf(event), self._addressOf(receiver),
        self._addressOf(filteringParent),
    )

  @overload(QPointerEvent)
  @overload(NoneType)
  def deliverSinglePointEventUntilAccepted(
      self,
      a0: Optional[QPointerEvent],
  ) -> bool:
    """
    Calls Qt's 'bool
    QQuickDeliveryAgentPrivate::deliverSinglePointEventUntilAccepted(
    QPointerEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html

    Parameters
    ----------

    a0 : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDeliveryAgentPrivate::deliverSinglePointEventUntilAccepted(
    #      QPointerEvent *a0)
    return self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate36deliverSinglePointEventUnti'
        'lAcceptedEP13QPointerEvent',
        self._addressOf(a0),
    )

  @overload(QTouchEvent)
  @overload(NoneType)
  def handleTouchEvent(self, a0: Optional[QTouchEvent]) -> None:
    """
    Calls Qt's 'void QQuickDeliveryAgentPrivate::handleTouchEvent(QTouchEvent
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#handleTouchEvent

    Parameters
    ----------

    a0 : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDeliveryAgentPrivate::handleTouchEvent(QTouchEvent *a0)
    self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate16handleTouchEventEP11QTouchE'
        'vent',
        self._addressOf(a0),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def handleMouseEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickDeliveryAgentPrivate::handleMouseEvent(QMouseEvent
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#handleMouseEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDeliveryAgentPrivate::handleMouseEvent(QMouseEvent *a0)
    self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate16handleMouseEventEP11QMouseE'
        'vent',
        self._addressOf(a0),
    )

  @overload(QTouchEvent)
  @overload(NoneType)
  def compressTouchEvent(self, a0: Optional[QTouchEvent]) -> bool:
    """
    Calls Qt's 'bool
    QQuickDeliveryAgentPrivate::compressTouchEvent(QTouchEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#compressTouchEvent

    Parameters
    ----------

    a0 : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDeliveryAgentPrivate::compressTouchEvent(QTouchEvent *a0)
    return self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate18compressTouchEventEP11QTouc'
        'hEvent',
        self._addressOf(a0),
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def flushFrameSynchronousEvents(self, win: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void
    QQuickDeliveryAgentPrivate::flushFrameSynchronousEvents(QQuickWindow
    *win)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html

    Parameters
    ----------

    win : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDeliveryAgentPrivate::flushFrameSynchronousEvents(
    #      QQuickWindow *win)
    self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate27flushFrameSynchronousEvents'
        'EP12QQuickWindow',
        self._addressOf(win),
    )

  def deliverDelayedTouchEvent(self) -> None:
    """
    Calls Qt's 'void QQuickDeliveryAgentPrivate::deliverDelayedTouchEvent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html
    """
    #  void QQuickDeliveryAgentPrivate::deliverDelayedTouchEvent()
    self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate24deliverDelayedTouchEventEv',
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def handleWindowDeactivate(self, win: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void
    QQuickDeliveryAgentPrivate::handleWindowDeactivate(QQuickWindow *win)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html

    Parameters
    ----------

    win : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDeliveryAgentPrivate::handleWindowDeactivate(QQuickWindow
    #      *win)
    self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate22handleWindowDeactivateEP12Q'
        'QuickWindow',
        self._addressOf(win),
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def handleWindowHidden(self, win: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void
    QQuickDeliveryAgentPrivate::handleWindowHidden(QQuickWindow *win)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#handleWindowHidden

    Parameters
    ----------

    win : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDeliveryAgentPrivate::handleWindowHidden(QQuickWindow *win)
    self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate18handleWindowHiddenEP12QQuic'
        'kWindow',
        self._addressOf(win),
    )

  @overload(QPointerEvent)
  @overload(NoneType)
  def allUpdatedPointsAccepted(self, ev: Optional[QPointerEvent]) -> bool:
    """
    Calls Qt's 'bool
    QQuickDeliveryAgentPrivate::allUpdatedPointsAccepted(const QPointerEvent
    *ev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html

    Parameters
    ----------

    ev : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDeliveryAgentPrivate::allUpdatedPointsAccepted(const
    #      QPointerEvent *ev)
    return self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate24allUpdatedPointsAcceptedEPK'
        '13QPointerEvent',
        self._addressOf(ev),
    )

  @overload(QPointerEvent)
  @overload(NoneType)
  def exclusiveGrabbers(self, ev: Optional[QPointerEvent]) -> QList[QObject]:
    """
    Calls Qt's 'QList<QObject *>
    QQuickDeliveryAgentPrivate::exclusiveGrabbers(QPointerEvent *ev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#exclusiveGrabbers

    Parameters
    ----------

    ev : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QList[QObject]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QObject *>
    #      QQuickDeliveryAgentPrivate::exclusiveGrabbers(QPointerEvent *ev)
    address = self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate17exclusiveGrabbersEP13QPoint'
        'erEvent',
        self._addressOf(ev),
    )
    from ..QtCore import QObject
    return QList[QObject]._cuteOwning(address)

  @overload(QEvent.Type, QEventPoint, QTouchEvent, QMutableSinglePointEvent)
  @overload(QEvent.Type, QEventPoint, QTouchEvent, NoneType)
  @overload(QEvent.Type, QEventPoint, NoneType, QMutableSinglePointEvent)
  @overload(QEvent.Type, QEventPoint, NoneType, NoneType)
  def touchToMouseEvent(
      self,
      type: QEvent.Type,
      p: QEventPoint,
      touchEvent: Optional[QTouchEvent],
      mouseEvent: Optional[QMutableSinglePointEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickDeliveryAgentPrivate::touchToMouseEvent(QEvent::Type type, const
    QEventPoint &p, const QTouchEvent *touchEvent, QMutableSinglePointEvent
    *mouseEvent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#touchToMouseEvent

    Parameters
    ----------

    type : QEvent.Type
      Passed on as its number.

    p : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.

    touchEvent : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mouseEvent : Optional[QMutableSinglePointEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDeliveryAgentPrivate::touchToMouseEvent(QEvent::Type type,
    #      const QEventPoint &p, const QTouchEvent *touchEvent,
    #      QMutableSinglePointEvent *mouseEvent)
    self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate17touchToMouseEventEN6QEvent4'
        'TypeERK11QEventPointPK11QTouchEventP24QMutableSinglePointEvent',
        type.value, self._valueOf(p), self._addressOf(touchEvent),
        self._addressOf(mouseEvent),
    )

  @overload(QPointingDevice)
  @overload(NoneType)
  def ensureDeviceConnected(self, dev: Optional[QPointingDevice]) -> None:
    """
    Calls Qt's 'void QQuickDeliveryAgentPrivate::ensureDeviceConnected(const
    QPointingDevice *dev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html

    Parameters
    ----------

    dev : Optional[QPointingDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDeliveryAgentPrivate::ensureDeviceConnected(const
    #      QPointingDevice *dev)
    self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate21ensureDeviceConnectedEPK15Q'
        'PointingDevice',
        self._addressOf(dev),
    )

  @overload(QPointerEvent)
  @overload(NoneType)
  def deliverPointerEvent(self, a0: Optional[QPointerEvent]) -> None:
    """
    Calls Qt's 'void
    QQuickDeliveryAgentPrivate::deliverPointerEvent(QPointerEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html

    Parameters
    ----------

    a0 : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDeliveryAgentPrivate::deliverPointerEvent(QPointerEvent
    #      *a0)
    self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate19deliverPointerEventEP13QPoi'
        'nterEvent',
        self._addressOf(a0),
    )

  @overload(QTouchEvent)
  @overload(NoneType)
  def deliverTouchCancelEvent(self, a0: Optional[QTouchEvent]) -> bool:
    """
    Calls Qt's 'bool
    QQuickDeliveryAgentPrivate::deliverTouchCancelEvent(QTouchEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html

    Parameters
    ----------

    a0 : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDeliveryAgentPrivate::deliverTouchCancelEvent(QTouchEvent
    #      *a0)
    return self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate23deliverTouchCancelEventEP11'
        'QTouchEvent',
        self._addressOf(a0),
    )

  @overload(QPointerEvent)
  @overload(NoneType)
  @overload(QPointerEvent, bool)
  @overload(NoneType, bool)
  def deliverPressOrReleaseEvent(
      self,
      a0: Optional[QPointerEvent],
      handlersOnly: bool = False,
  ) -> bool:
    """
    Calls Qt's 'bool
    QQuickDeliveryAgentPrivate::deliverPressOrReleaseEvent(QPointerEvent *a0,
    bool handlersOnly)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html

    Parameters
    ----------

    a0 : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    handlersOnly : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  bool QQuickDeliveryAgentPrivate::deliverPressOrReleaseEvent(
    #      QPointerEvent *a0, bool handlersOnly)
    return self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate26deliverPressOrReleaseEventE'
        'P13QPointerEventb',
        self._addressOf(a0), handlersOnly,
    )

  @overload(QPointerEvent)
  @overload(NoneType)
  def deliverUpdatedPoints(self, event: Optional[QPointerEvent]) -> None:
    """
    Calls Qt's 'void
    QQuickDeliveryAgentPrivate::deliverUpdatedPoints(QPointerEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDeliveryAgentPrivate::deliverUpdatedPoints(QPointerEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate20deliverUpdatedPointsEP13QPo'
        'interEvent',
        self._addressOf(event),
    )

  @overload(QQuickItem, bool, QPointerEvent)
  @overload(QQuickItem, bool, NoneType)
  @overload(NoneType, bool, QPointerEvent)
  @overload(NoneType, bool, NoneType)
  @overload(QQuickItem, bool, QPointerEvent, bool)
  @overload(QQuickItem, bool, NoneType, bool)
  @overload(NoneType, bool, QPointerEvent, bool)
  @overload(NoneType, bool, NoneType, bool)
  def deliverMatchingPointsToItem(
      self,
      item: Optional[QQuickItem],
      isGrabber: bool,
      pointerEvent: Optional[QPointerEvent],
      handlersOnly: bool = False,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickDeliveryAgentPrivate::deliverMatchingPointsToItem(QQuickItem *item,
    bool isGrabber, QPointerEvent *pointerEvent, bool handlersOnly)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    isGrabber : bool
      Passed on as it is.

    pointerEvent : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    handlersOnly : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void
    #      QQuickDeliveryAgentPrivate::deliverMatchingPointsToItem(QQuickItem
    #      *item, bool isGrabber, QPointerEvent *pointerEvent, bool
    #      handlersOnly)
    self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate27deliverMatchingPointsToItem'
        'EP10QQuickItembP13QPointerEventb',
        self._addressOf(item), isGrabber, self._addressOf(pointerEvent),
        handlersOnly,
    )

  @overload(QPointF, QPointF, Qt.KeyboardModifiers, int)
  def deliverHoverEvent(
      self,
      scenePos: QPointF,
      lastScenePos: QPointF,
      modifiers: Qt.KeyboardModifiers,
      timestamp: int,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickDeliveryAgentPrivate::deliverHoverEvent(const
    QPointF &scenePos, const QPointF &lastScenePos, Qt::KeyboardModifiers
    modifiers, ulong timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#deliverHoverEvent

    Parameters
    ----------

    scenePos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    lastScenePos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.

    timestamp : int
      Passed on as it is.
    """
    #  bool QQuickDeliveryAgentPrivate::deliverHoverEvent(const QPointF
    #      &scenePos, const QPointF &lastScenePos, Qt::KeyboardModifiers
    #      modifiers, ulong timestamp)
    return self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate17deliverHoverEventERK7QPoint'
        'FS2_6QFlagsIN2Qt16KeyboardModifierEEm',
        self._valueOf(scenePos, 'QPointF'), self._valueOf(lastScenePos,
        'QPointF'), modifiers.value, timestamp,
    )

  @overload(
      QQuickItem, QPointF, QPointF, QPointF, QPointF, Qt.KeyboardModifiers,
      int,
  )
  @overload(
      NoneType, QPointF, QPointF, QPointF, QPointF, Qt.KeyboardModifiers,
      int,
  )
  def deliverHoverEventRecursive(
      self,
      a0: Optional[QQuickItem],
      localPos: QPointF,
      scenePos: QPointF,
      lastScenePos: QPointF,
      globalPos: QPointF,
      modifiers: Qt.KeyboardModifiers,
      timestamp: int,
  ) -> bool:
    """
    Calls Qt's 'bool
    QQuickDeliveryAgentPrivate::deliverHoverEventRecursive(QQuickItem *a0,
    const QPointF &localPos, const QPointF &scenePos, const QPointF
    &lastScenePos, const QPointF &globalPos, Qt::KeyboardModifiers modifiers,
    ulong timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    localPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    scenePos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    lastScenePos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    globalPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.

    timestamp : int
      Passed on as it is.
    """
    #  bool QQuickDeliveryAgentPrivate::deliverHoverEventRecursive(QQuickItem
    #      *a0, const QPointF &localPos, const QPointF &scenePos, const
    #      QPointF &lastScenePos, const QPointF &globalPos,
    #      Qt::KeyboardModifiers modifiers, ulong timestamp)
    return self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate26deliverHoverEventRecursiveE'
        'P10QQuickItemRK7QPointFS4_S4_S4_6QFlagsIN2Qt16KeyboardModifierEEm',
        self._addressOf(a0), self._valueOf(localPos, 'QPointF'),
        self._valueOf(scenePos, 'QPointF'), self._valueOf(lastScenePos,
        'QPointF'), self._valueOf(globalPos, 'QPointF'), modifiers.value,
        timestamp,
    )

  @overload(
      QQuickItem, QPointF, QPointF, QPointF, QPointF, Qt.KeyboardModifiers,
      int, HoverChange,
  )
  @overload(
      NoneType, QPointF, QPointF, QPointF, QPointF, Qt.KeyboardModifiers,
      int, HoverChange,
  )
  def deliverHoverEventToItem(
      self,
      item: Optional[QQuickItem],
      localPos: QPointF,
      scenePos: QPointF,
      lastScenePos: QPointF,
      globalPos: QPointF,
      modifiers: Qt.KeyboardModifiers,
      timestamp: int,
      hoverChange: HoverChange,
  ) -> bool:
    """
    Calls Qt's 'bool
    QQuickDeliveryAgentPrivate::deliverHoverEventToItem(QQuickItem *item,
    const QPointF &localPos, const QPointF &scenePos, const QPointF
    &lastScenePos, const QPointF &globalPos, Qt::KeyboardModifiers modifiers,
    ulong timestamp, HoverChange hoverChange)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    localPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    scenePos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    lastScenePos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    globalPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.

    timestamp : int
      Passed on as it is.

    hoverChange : HoverChange
      Passed on as its number.
    """
    #  bool QQuickDeliveryAgentPrivate::deliverHoverEventToItem(QQuickItem
    #      *item, const QPointF &localPos, const QPointF &scenePos, const
    #      QPointF &lastScenePos, const QPointF &globalPos,
    #      Qt::KeyboardModifiers modifiers, ulong timestamp, HoverChange
    #      hoverChange)
    return self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate23deliverHoverEventToItemEP10'
        'QQuickItemRK7QPointFS4_S4_S4_6QFlagsIN2Qt16KeyboardModifierEEmNS_1'
        '1HoverChangeE',
        self._addressOf(item), self._valueOf(localPos, 'QPointF'),
        self._valueOf(scenePos, 'QPointF'), self._valueOf(lastScenePos,
        'QPointF'), self._valueOf(globalPos, 'QPointF'), modifiers.value,
        timestamp, hoverChange.value,
    )

  @overload(
      QEvent.Type, QQuickItem, QPointF, QPointF, QPointF, QPointF,
      Qt.KeyboardModifiers, int,
  )
  @overload(
      QEvent.Type, NoneType, QPointF, QPointF, QPointF, QPointF,
      Qt.KeyboardModifiers, int,
  )
  def sendHoverEvent(
      self,
      a0: QEvent.Type,
      a1: Optional[QQuickItem],
      localPos: QPointF,
      scenePos: QPointF,
      lastScenePos: QPointF,
      globalPos: QPointF,
      modifiers: Qt.KeyboardModifiers,
      timestamp: int,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickDeliveryAgentPrivate::sendHoverEvent(QEvent::Type
    a0, QQuickItem *a1, const QPointF &localPos, const QPointF &scenePos,
    const QPointF &lastScenePos, const QPointF &globalPos,
    Qt::KeyboardModifiers modifiers, ulong timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#sendHoverEvent

    Parameters
    ----------

    a0 : QEvent.Type
      Passed on as its number.

    a1 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    localPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    scenePos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    lastScenePos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    globalPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.

    timestamp : int
      Passed on as it is.
    """
    #  bool QQuickDeliveryAgentPrivate::sendHoverEvent(QEvent::Type a0,
    #      QQuickItem *a1, const QPointF &localPos, const QPointF &scenePos,
    #      const QPointF &lastScenePos, const QPointF &globalPos,
    #      Qt::KeyboardModifiers modifiers, ulong timestamp)
    return self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate14sendHoverEventEN6QEvent4Typ'
        'eEP10QQuickItemRK7QPointFS6_S6_S6_6QFlagsIN2Qt16KeyboardModifierEE'
        'm',
        a0.value, self._addressOf(a1), self._valueOf(localPos, 'QPointF'),
        self._valueOf(scenePos, 'QPointF'), self._valueOf(lastScenePos,
        'QPointF'), self._valueOf(globalPos, 'QPointF'), modifiers.value,
        timestamp,
    )

  @overload()
  @overload(int)
  def clearHover(self, timestamp: int = 0) -> bool:
    """
    Calls Qt's 'bool QQuickDeliveryAgentPrivate::clearHover(ulong
    timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#clearHover

    Parameters
    ----------

    timestamp : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  bool QQuickDeliveryAgentPrivate::clearHover(ulong timestamp)
    return self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate10clearHoverEm', timestamp,
    )

  @overload(QQuickDragGrabber, QEvent)
  @overload(QQuickDragGrabber, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def deliverDragEvent(
      self,
      a0: Optional[QQuickDragGrabber],
      a1: Optional[QEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickDeliveryAgentPrivate::deliverDragEvent(QQuickDragGrabber *a0,
    QEvent *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html#deliverDragEvent

    Parameters
    ----------

    a0 : Optional[QQuickDragGrabber]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDeliveryAgentPrivate::deliverDragEvent(QQuickDragGrabber
    #      *a0, QEvent *a1)
    self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate16deliverDragEventEP17QQuickD'
        'ragGrabberP6QEvent',
        self._addressOf(a0), self._addressOf(a1),
    )

  @overload(QContextMenuEvent)
  @overload(NoneType)
  def deliverContextMenuEvent(
      self,
      event: Optional[QContextMenuEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickDeliveryAgentPrivate::deliverContextMenuEvent(QContextMenuEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagentprivate.html

    Parameters
    ----------

    event : Optional[QContextMenuEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDeliveryAgentPrivate::deliverContextMenuEvent(
    #      QContextMenuEvent *event)
    self.uglySide.call(
        'ritual_ZN26QQuickDeliveryAgentPrivate23deliverContextMenuEventEP17'
        'QContextMenuEvent',
        self._addressOf(event),
    )

  @staticmethod
  def clonePointerEvent(*__, **_) -> Never:
    """
    Qt's 'QPointerEvent
    *QQuickDeliveryAgentPrivate::clonePointerEvent(QPointerEvent *event,
    std::optional<QPointF> transformedLocalPos)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickDeliveryAgentPrivate.clonePointerEvent' has no cute "
        "function yet. Qt's 'QPointerEvent "
        "*QQuickDeliveryAgentPrivate::clonePointerEvent(QPointerEvent "
        "*event, std::optional<QPointF> transformedLocalPos)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def deliverToPassiveGrabbers(*__, **_) -> Never:
    """
    Qt's 'void QQuickDeliveryAgentPrivate::deliverToPassiveGrabbers(const
    QList<QPointer<QObject>> &passiveGrabbers, QPointerEvent *pointerEvent)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickDeliveryAgentPrivate.deliverToPassiveGrabbers' has no cute "
        "function yet. Qt's 'void "
        "QQuickDeliveryAgentPrivate::deliverToPassiveGrabbers(const "
        "QList<QPointer<QObject>> &passiveGrabbers, QPointerEvent "
        "*pointerEvent)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def eventTargets(*__, **_) -> Never:
    """
    Qt's 'QList<QQuickItem *>
    QQuickDeliveryAgentPrivate::eventTargets(QQuickItem *a0, const QEvent
    *event, int pointId, QPointF localPos, QPointF scenePos,
    qxp::function_ref<std::optional<bool> (QQuickItem *, const QEvent *)>
    predicate) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickDeliveryAgentPrivate.eventTargets' has no cute function "
        "yet. Qt's 'QList<QQuickItem *> "
        "QQuickDeliveryAgentPrivate::eventTargets(QQuickItem *a0, const "
        "QEvent *event, int pointId, QPointF localPos, QPointF scenePos, "
        "qxp::function_ref<std::optional<bool> (QQuickItem *, const QEvent "
        "*)> predicate) const': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def eventTargetsAppend(*__, **_) -> Never:
    """
    Qt's 'void QQuickDeliveryAgentPrivate::eventTargetsAppend(QQuickItem *a0,
    const QEvent *event, int pointId, QPointF localPos, QPointF scenePos,
    qxp::function_ref<std::optional<bool> (QQuickItem *, const QEvent *)>
    predicate, QList<QQuickItem *> &targets) const': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickDeliveryAgentPrivate.eventTargetsAppend' has no cute "
        "function yet. Qt's 'void "
        "QQuickDeliveryAgentPrivate::eventTargetsAppend(QQuickItem *a0, "
        "const QEvent *event, int pointId, QPointF localPos, QPointF "
        "scenePos, qxp::function_ref<std::optional<bool> (QQuickItem *, "
        "const QEvent *)> predicate, QList<QQuickItem *> &targets) const': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def isHoveringMoveEvent(*__, **_) -> Never:
    """
    Qt's 'bool QQuickDeliveryAgentPrivate::isHoveringMoveEvent(const
    QPointerEvent *ev)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QQuickDeliveryAgentPrivate.isHoveringMoveEvent' has no cute "
        "function yet. Qt's 'bool "
        "QQuickDeliveryAgentPrivate::isHoveringMoveEvent(const "
        "QPointerEvent *ev)': cannot be called and cannot be called through "
        "the meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def notifyFocusChangesRecur(*__, **_) -> Never:
    """
    Qt's 'void QQuickDeliveryAgentPrivate::notifyFocusChangesRecur(QQuickItem
    **item, int remaining, Qt::FocusReason reason)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickDeliveryAgentPrivate.notifyFocusChangesRecur' has no cute "
        "function yet. Qt's 'void "
        "QQuickDeliveryAgentPrivate::notifyFocusChangesRecur(QQuickItem "
        "**item, int remaining, Qt::FocusReason reason)': takes a type "
        "Python has no way to hand over yet.")
