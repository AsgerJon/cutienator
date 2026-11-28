"""
QQuickTapHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktaphandler_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickTapHandler to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QPointingDevice
from . import QQuickSinglePointHandler

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QTimerEvent
  from ..QtGui import QEventPoint, QPointerEvent
  from . import QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEventPoint = WAIT['QEventPoint']
  QPointerEvent = WAIT['QPointerEvent']
  QQuickItem = WAIT['QQuickItem']
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTapHandler(QQuickSinglePointHandler):
  """
  The cute side of Qt's QQuickTapHandler: a plain Python object standing in
  front of one C++ QQuickTapHandler.

  It is built on the cute 'QQuickSinglePointHandler', as Qt's
  QQuickTapHandler is built on Qt's QQuickSinglePointHandler, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTapHandler that has a ritual and that Python
  can call so far, 26 names in all: 'metaObject', 'tr', 'isPressed',
  'tapCount', 'timeHeld', 'longPressThreshold', 'setLongPressThreshold',
  'resetLongPressThreshold', 'gesturePolicy', 'setGesturePolicy',
  'exclusiveSignals', 'setExclusiveSignals', 'pressedChanged',
  'tapCountChanged', 'timeHeldChanged', 'longPressThresholdChanged',
  'gesturePolicyChanged', 'exclusiveSignalsChanged', 'tapped',
  'singleTapped', 'doubleTapped', 'longPressed', 'timerEvent',
  'wantsEventPoint', 'connectPreRenderSignal', 'updateTimeHeld'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTapHandler::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickTapHandler::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickTapHandler::onGrabChanged(QQuickPointerHandler *grabber,
    QPointingDevice::GrabTransition transition, QPointerEvent *ev,
    QEventPoint &point)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQuickTapHandler::handleEventPoint(QPointerEvent *event,
    QEventPoint &point)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQuickTapHandler::setPressed(bool press, bool cancel,
    QPointerEvent *event, QEventPoint &point)': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  2 of the 34 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickTapHandler is created at the first use, not by
    'QQuickTapHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTapHandler.
  - Qt tells when it has removed the C++ QQuickTapHandler. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickTapHandler that has no cute function yet,
    'setPressed', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QQuickTapHandler, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ExclusiveSignal(CuteFlags):
    """
    The flags enum 'QQuickTapHandler::ExclusiveSignal' of Qt, with the 3
    names Qt gives in it. Qt names the type of its combinations
    'QQuickTapHandler::ExclusiveSignals'.
    """

    NotExclusive = 0x0
    SingleTap = 0x1
    DoubleTap = 0x2

  ExclusiveSignals = ExclusiveSignal

  class GesturePolicy(CuteNum):
    """
    The enum 'QQuickTapHandler::GesturePolicy' of Qt, with the 4 names Qt
    gives in it.
    """

    DragThreshold = Kee[int](0)
    WithinBounds = Kee[int](1)
    ReleaseWithinBounds = Kee[int](2)
    DragWithinBounds = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QQuickTapHandler::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktaphandler.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTapHandler::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQuickTapHandler2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTapHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickTapHandler::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktaphandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTapHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickTapHandler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isPressed(self) -> bool:
    """
    Calls Qt's 'bool QQuickTapHandler::isPressed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktaphandler.html#isPressed
    """
    #  bool QQuickTapHandler::isPressed() const
    return self.uglySide.call('ritual_ZNK16QQuickTapHandler9isPressedEv')

  def tapCount(self) -> int:
    """
    Calls Qt's 'int QQuickTapHandler::tapCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktaphandler.html#tapCount
    """
    #  int QQuickTapHandler::tapCount() const
    return self.uglySide.call('ritual_ZNK16QQuickTapHandler8tapCountEv')

  def timeHeld(self) -> float:
    """
    Calls Qt's 'qreal QQuickTapHandler::timeHeld() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktaphandler.html#timeHeld
    """
    #  qreal QQuickTapHandler::timeHeld() const
    return self.uglySide.call('ritual_ZNK16QQuickTapHandler8timeHeldEv')

  def longPressThreshold(self) -> float:
    """
    Calls Qt's 'qreal QQuickTapHandler::longPressThreshold() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktaphandler.html#longPressThreshold
    """
    #  qreal QQuickTapHandler::longPressThreshold() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickTapHandler18longPressThresholdEv',
    )

  def gesturePolicy(self) -> GesturePolicy:
    """
    Calls Qt's 'GesturePolicy QQuickTapHandler::gesturePolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktaphandler.html#gesturePolicy

    Returns
    -------

    GesturePolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'GesturePolicy(number)'
      gives.
    """
    #  GesturePolicy QQuickTapHandler::gesturePolicy() const
    return QQuickTapHandler.GesturePolicy(self.uglySide.call(
        'ritual_ZNK16QQuickTapHandler13gesturePolicyEv',
    ))

  def exclusiveSignals(self) -> ExclusiveSignals:
    """
    Calls Qt's 'QQuickTapHandler::ExclusiveSignals
    QQuickTapHandler::exclusiveSignals() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktaphandler.html#exclusiveSignals

    Returns
    -------

    ExclusiveSignals
      The value standing for the combination Qt gave back.
    """
    #  QQuickTapHandler::ExclusiveSignals
    #      QQuickTapHandler::exclusiveSignals() const
    return QQuickTapHandler.ExclusiveSignals(self.uglySide.call(
        'ritual_ZNK16QQuickTapHandler16exclusiveSignalsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setLongPressThreshold(self, longPressThreshold: float) -> None:
    """
    Calls Qt's 'void QQuickTapHandler::setLongPressThreshold(qreal
    longPressThreshold)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktaphandler.html#setLongPressThreshold

    Parameters
    ----------

    longPressThreshold : float
      Passed on as it is.
    """
    #  void QQuickTapHandler::setLongPressThreshold(qreal longPressThreshold)
    self.uglySide.call(
        'ritual_ZN16QQuickTapHandler21setLongPressThresholdEd',
        longPressThreshold,
    )

  @overload(GesturePolicy)
  def setGesturePolicy(self, gesturePolicy: GesturePolicy) -> None:
    """
    Calls Qt's 'void QQuickTapHandler::setGesturePolicy(GesturePolicy
    gesturePolicy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktaphandler.html#setGesturePolicy

    Parameters
    ----------

    gesturePolicy : GesturePolicy
      Passed on as its number.
    """
    #  void QQuickTapHandler::setGesturePolicy(GesturePolicy gesturePolicy)
    self.uglySide.call(
        'ritual_ZN16QQuickTapHandler16setGesturePolicyENS_13GesturePolicyE',
        gesturePolicy.value,
    )

  @overload(ExclusiveSignals)
  def setExclusiveSignals(
      self,
      newexclusiveSignals: ExclusiveSignals,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickTapHandler::setExclusiveSignals(QQuickTapHandler::ExclusiveSignals
    newexclusiveSignals)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktaphandler.html#setExclusiveSignals

    Parameters
    ----------

    newexclusiveSignals : ExclusiveSignals
      Passed on as its number.
    """
    #  void QQuickTapHandler::setExclusiveSignals(QQuickTapHandler::
    #      ExclusiveSignals newexclusiveSignals)
    self.uglySide.call(
        'ritual_ZN16QQuickTapHandler19setExclusiveSignalsE6QFlagsINS_15Excl'
        'usiveSignalEE',
        newexclusiveSignals.value,
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickTapHandler::QQuickTapHandler(QQuickItem *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktaphandler.html#QQuickTapHandler

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickTapHandler::QQuickTapHandler(QQuickItem *parent)
    self._noteCreation(QQuickTapHandler, lambda: Rituals.call(
        'ritual_ZN16QQuickTapHandlerC1EP10QQuickItem',
        self._addressOf(parent),
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

  def resetLongPressThreshold(self) -> None:
    """
    Calls Qt's 'void QQuickTapHandler::resetLongPressThreshold()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktaphandler.html#resetLongPressThreshold
    """
    #  void QQuickTapHandler::resetLongPressThreshold()
    self.uglySide.call(
        'ritual_ZN16QQuickTapHandler23resetLongPressThresholdEv',
    )

  def pressedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTapHandler::pressedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktaphandler.html#pressedChanged
    """
    #  void QQuickTapHandler::pressedChanged()
    self.uglySide.call('ritual_ZN16QQuickTapHandler14pressedChangedEv')

  def tapCountChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTapHandler::tapCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktaphandler.html#tapCountChanged
    """
    #  void QQuickTapHandler::tapCountChanged()
    self.uglySide.call('ritual_ZN16QQuickTapHandler15tapCountChangedEv')

  def timeHeldChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTapHandler::timeHeldChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktaphandler.html#timeHeldChanged
    """
    #  void QQuickTapHandler::timeHeldChanged()
    self.uglySide.call('ritual_ZN16QQuickTapHandler15timeHeldChangedEv')

  def longPressThresholdChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTapHandler::longPressThresholdChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktaphandler.html#longPressThresholdChanged
    """
    #  void QQuickTapHandler::longPressThresholdChanged()
    self.uglySide.call(
        'ritual_ZN16QQuickTapHandler25longPressThresholdChangedEv',
    )

  def gesturePolicyChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTapHandler::gesturePolicyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktaphandler.html#gesturePolicyChanged
    """
    #  void QQuickTapHandler::gesturePolicyChanged()
    self.uglySide.call('ritual_ZN16QQuickTapHandler20gesturePolicyChangedEv')

  def exclusiveSignalsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTapHandler::exclusiveSignalsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktaphandler.html#exclusiveSignalsChanged
    """
    #  void QQuickTapHandler::exclusiveSignalsChanged()
    self.uglySide.call(
        'ritual_ZN16QQuickTapHandler23exclusiveSignalsChangedEv',
    )

  @overload(QEventPoint, Qt.MouseButton)
  def tapped(self, eventPoint: QEventPoint, a1: Qt.MouseButton) -> None:
    """
    Calls Qt's 'void QQuickTapHandler::tapped(QEventPoint eventPoint,
    Qt::MouseButton a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktaphandler.html#tapped

    Parameters
    ----------

    eventPoint : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.

    a1 : Qt.MouseButton
      Passed on as its number.
    """
    #  void QQuickTapHandler::tapped(QEventPoint eventPoint, Qt::MouseButton
    #      a1)
    self.uglySide.call(
        'ritual_ZN16QQuickTapHandler6tappedE11QEventPointN2Qt11MouseButtonE',
        self._valueOf(eventPoint), a1.value,
    )

  @overload(QEventPoint, Qt.MouseButton)
  def singleTapped(
      self,
      eventPoint: QEventPoint,
      a1: Qt.MouseButton,
  ) -> None:
    """
    Calls Qt's 'void QQuickTapHandler::singleTapped(QEventPoint eventPoint,
    Qt::MouseButton a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktaphandler.html#singleTapped

    Parameters
    ----------

    eventPoint : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.

    a1 : Qt.MouseButton
      Passed on as its number.
    """
    #  void QQuickTapHandler::singleTapped(QEventPoint eventPoint,
    #      Qt::MouseButton a1)
    self.uglySide.call(
        'ritual_ZN16QQuickTapHandler12singleTappedE11QEventPointN2Qt11Mouse'
        'ButtonE',
        self._valueOf(eventPoint), a1.value,
    )

  @overload(QEventPoint, Qt.MouseButton)
  def doubleTapped(
      self,
      eventPoint: QEventPoint,
      a1: Qt.MouseButton,
  ) -> None:
    """
    Calls Qt's 'void QQuickTapHandler::doubleTapped(QEventPoint eventPoint,
    Qt::MouseButton a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktaphandler.html#doubleTapped

    Parameters
    ----------

    eventPoint : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.

    a1 : Qt.MouseButton
      Passed on as its number.
    """
    #  void QQuickTapHandler::doubleTapped(QEventPoint eventPoint,
    #      Qt::MouseButton a1)
    self.uglySide.call(
        'ritual_ZN16QQuickTapHandler12doubleTappedE11QEventPointN2Qt11Mouse'
        'ButtonE',
        self._valueOf(eventPoint), a1.value,
    )

  def longPressed(self) -> None:
    """
    Calls Qt's 'void QQuickTapHandler::longPressed()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktaphandler.html#longPressed
    """
    #  void QQuickTapHandler::longPressed()
    self.uglySide.call('ritual_ZN16QQuickTapHandler11longPressedEv')

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QQuickTapHandler::timerEvent(QTimerEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktaphandler.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTapHandler::timerEvent(QTimerEvent *event)
    ritual = 'ritual_ZN16QQuickTapHandler10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickTapHandler10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QPointerEvent, QEventPoint)
  @overload(NoneType, QEventPoint)
  def wantsEventPoint(
      self,
      event: Optional[QPointerEvent],
      point: QEventPoint,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickTapHandler::wantsEventPoint(const QPointerEvent
    *event, const QEventPoint &point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktaphandler.html#wantsEventPoint

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.
    """
    #  bool QQuickTapHandler::wantsEventPoint(const QPointerEvent *event,
    #      const QEventPoint &point)
    ritual = (
        'ritual_ZN16QQuickTapHandler15wantsEventPointEPK13QPointerEventRK11'
        'QEventPoint')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickTapHandler15wantsEventPointEPK13QPointerEve'
          'ntRK11QEventPoint')
    return self.uglySide.call(
        ritual, self._addressOf(event), self._valueOf(point),
    )

  @overload()
  @overload(bool)
  def connectPreRenderSignal(self, conn: bool = True) -> None:
    """
    Calls Qt's 'void QQuickTapHandler::connectPreRenderSignal(bool conn)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktaphandler.html#connectPreRenderSignal

    Parameters
    ----------

    conn : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QQuickTapHandler::connectPreRenderSignal(bool conn)
    self.uglySide.call(
        'ritual_ZN16QQuickTapHandler22connectPreRenderSignalEb', conn,
    )

  def updateTimeHeld(self) -> None:
    """
    Calls Qt's 'void QQuickTapHandler::updateTimeHeld()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktaphandler.html#updateTimeHeld
    """
    #  void QQuickTapHandler::updateTimeHeld()
    self.uglySide.call('ritual_ZN16QQuickTapHandler14updateTimeHeldEv')

  @staticmethod
  def setPressed(*__, **_) -> Never:
    """
    Qt's 'void QQuickTapHandler::setPressed(bool press, bool cancel,
    QPointerEvent *event, QEventPoint &point)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickTapHandler.setPressed' has no cute function yet. Qt's 'void "
        "QQuickTapHandler::setPressed(bool press, bool cancel, "
        "QPointerEvent *event, QEventPoint &point)': takes a type Python "
        "has no way to hand over yet.")
