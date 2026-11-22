"""
QScroller binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qscroller.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF, QRectF
  from . import QScrollerProperties
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']
  QScrollerProperties = WAIT['QScrollerProperties']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScroller(QObject):
  """
  The cute side of Qt's QScroller: a plain Python object standing in front of
  one C++ QScroller.

  It is built on the cute 'QObject', as Qt's QScroller is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QScroller that has a ritual and that Python can call
  so far, 22 names in all: 'metaObject', 'tr', 'hasScroller', 'scroller',
  'grabGesture', 'grabbedGesture', 'ungrabGesture', 'activeScrollers',
  'target', 'state', 'handleInput', 'stop', 'velocity', 'finalPosition',
  'pixelPerMeter', 'scrollerProperties', 'setSnapPositionsX',
  'setSnapPositionsY', 'setScrollerProperties', 'scrollTo', 'ensureVisible',
  'resendPrepareEvent'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QScroller *QScroller::scroller(const QObject *target)': takes
    in Python what 'QScroller *QScroller::scroller(QObject *target)' takes.

  What has no ritual
  ------------------

  14 of the 39 functions Qt declares: 5 private; 4 takes or gives a type that
  cannot be passed yet; 2 a signal; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QScroller is created at the first use, not by 'QScroller(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScroller.
  - Qt tells when it has removed the C++ QScroller. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QScroller, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Input(CuteNum):
    """The enum 'QScroller::Input' of Qt, with the 3 names Qt gives in it."""

    InputPress = Kee[int](1)
    InputMove = Kee[int](2)
    InputRelease = Kee[int](3)

  class ScrollerGestureType(CuteNum):
    """
    The enum 'QScroller::ScrollerGestureType' of Qt, with the 4 names Qt
    gives in it.
    """

    TouchGesture = Kee[int](0)
    LeftMouseButtonGesture = Kee[int](1)
    RightMouseButtonGesture = Kee[int](2)
    MiddleMouseButtonGesture = Kee[int](3)

  class State(CuteNum):
    """The enum 'QScroller::State' of Qt, with the 4 names Qt gives in it."""

    Inactive = Kee[int](0)
    Pressed = Kee[int](1)
    Dragging = Kee[int](2)
    Scrolling = Kee[int](3)

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
    Calls Qt's 'QString QScroller::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qscroller.html#tr

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
    #  QString QScroller::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9QScroller2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def hasScroller(target: Optional[QObject]) -> bool:
    """
    Calls Qt's 'bool QScroller::hasScroller(QObject *target)'.

    Qt's own words: https://doc.qt.io/qt-6/qscroller.html#hasScroller

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QScroller::hasScroller(QObject *target)
    return Rituals.call(
        'ritual_ZN9QScroller11hasScrollerEP7QObject',
        CuteMixin._addressOf(target),
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def scroller(target: Optional[QObject]) -> Optional[QScroller]:
    """
    Calls Qt's 'QScroller *QScroller::scroller(QObject *target)'.

    Qt's own words: https://doc.qt.io/qt-6/qscroller.html#scroller

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QScroller]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScroller *QScroller::scroller(QObject *target)
    address = Rituals.call(
        'ritual_ZN9QScroller8scrollerEP7QObject',
        CuteMixin._addressOf(target),
    )
    return QScroller._cuteAt(address)

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  @overload(QObject, ScrollerGestureType)
  @overload(NoneType, ScrollerGestureType)
  def grabGesture(
      target: Optional[QObject],
      gestureType: ScrollerGestureType = ScrollerGestureType.TouchGesture,
  ) -> Qt.GestureType:
    """
    Calls Qt's 'Qt::GestureType QScroller::grabGesture(QObject *target,
    ScrollerGestureType gestureType)'.

    Qt's own words: https://doc.qt.io/qt-6/qscroller.html#grabGesture

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    gestureType : ScrollerGestureType
      Passed on as its number. May be left out, as in Qt: it is then
      ScrollerGestureType.TouchGesture.

    Returns
    -------

    Qt.GestureType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.GestureType(number)'
      gives.
    """
    #  Qt::GestureType QScroller::grabGesture(QObject *target,
    #      ScrollerGestureType gestureType)
    return Qt.GestureType(Rituals.call(
        'ritual_ZN9QScroller11grabGestureEP7QObjectNS_19ScrollerGestureType'
        'E',
        CuteMixin._addressOf(target), gestureType.value,
    ))

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def grabbedGesture(target: Optional[QObject]) -> Qt.GestureType:
    """
    Calls Qt's 'Qt::GestureType QScroller::grabbedGesture(QObject *target)'.

    Qt's own words: https://doc.qt.io/qt-6/qscroller.html#grabbedGesture

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Qt.GestureType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.GestureType(number)'
      gives.
    """
    #  Qt::GestureType QScroller::grabbedGesture(QObject *target)
    return Qt.GestureType(Rituals.call(
        'ritual_ZN9QScroller14grabbedGestureEP7QObject',
        CuteMixin._addressOf(target),
    ))

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def ungrabGesture(target: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QScroller::ungrabGesture(QObject *target)'.

    Qt's own words: https://doc.qt.io/qt-6/qscroller.html#ungrabGesture

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScroller::ungrabGesture(QObject *target)
    Rituals.call(
        'ritual_ZN9QScroller13ungrabGestureEP7QObject',
        CuteMixin._addressOf(target),
    )

  @staticmethod
  def activeScrollers() -> QList[QScroller]:
    """
    Calls Qt's 'QList<QScroller *> QScroller::activeScrollers()'.

    Qt's own words: https://doc.qt.io/qt-6/qscroller.html#activeScrollers

    Returns
    -------

    QList[QScroller]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QScroller *> QScroller::activeScrollers()
    address = Rituals.call('ritual_ZN9QScroller15activeScrollersEv')
    return QList[QScroller]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScroller'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QScroller::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscroller.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QScroller::metaObject() const
    address = self.uglySide.call('ritual_ZNK9QScroller10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def target(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QScroller::target() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscroller.html#target

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QScroller::target() const
    address = self.uglySide.call('ritual_ZNK9QScroller6targetEv')
    return QObject._cuteAt(address)

  def state(self) -> State:
    """
    Calls Qt's 'State QScroller::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscroller.html#state

    Returns
    -------

    State
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'State(number)' gives.
    """
    #  State QScroller::state() const
    return QScroller.State(self.uglySide.call(
        'ritual_ZNK9QScroller5stateEv',
    ))

  def velocity(self) -> QPointF:
    """
    Calls Qt's 'QPointF QScroller::velocity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscroller.html#velocity

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QScroller::velocity() const
    address = self.uglySide.call('ritual_ZNK9QScroller8velocityEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def finalPosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QScroller::finalPosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscroller.html#finalPosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QScroller::finalPosition() const
    address = self.uglySide.call('ritual_ZNK9QScroller13finalPositionEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def pixelPerMeter(self) -> QPointF:
    """
    Calls Qt's 'QPointF QScroller::pixelPerMeter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscroller.html#pixelPerMeter

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QScroller::pixelPerMeter() const
    address = self.uglySide.call('ritual_ZNK9QScroller13pixelPerMeterEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def scrollerProperties(self) -> QScrollerProperties:
    """
    Calls Qt's 'QScrollerProperties QScroller::scrollerProperties() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscroller.html#scrollerProperties

    Returns
    -------

    QScrollerProperties
      A new cute QScrollerProperties around the copy Qt gave back. Python
      owns it.
    """
    #  QScrollerProperties QScroller::scrollerProperties() const
    address = self.uglySide.call(
        'ritual_ZNK9QScroller18scrollerPropertiesEv',
    )
    from . import QScrollerProperties
    return QScrollerProperties._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float, float)
  def setSnapPositionsX(self, first: float, interval: float) -> None:
    """
    Calls Qt's 'void QScroller::setSnapPositionsX(qreal first, qreal
    interval)'.

    Qt's own words: https://doc.qt.io/qt-6/qscroller.html#setSnapPositionsX

    Parameters
    ----------

    first : float
      Passed on as it is.

    interval : float
      Passed on as it is.
    """
    #  void QScroller::setSnapPositionsX(qreal first, qreal interval)
    self.uglySide.call(
        'ritual_ZN9QScroller17setSnapPositionsXEdd', first, interval,
    )

  @overload(float, float)
  def setSnapPositionsY(self, first: float, interval: float) -> None:
    """
    Calls Qt's 'void QScroller::setSnapPositionsY(qreal first, qreal
    interval)'.

    Qt's own words: https://doc.qt.io/qt-6/qscroller.html#setSnapPositionsY

    Parameters
    ----------

    first : float
      Passed on as it is.

    interval : float
      Passed on as it is.
    """
    #  void QScroller::setSnapPositionsY(qreal first, qreal interval)
    self.uglySide.call(
        'ritual_ZN9QScroller17setSnapPositionsYEdd', first, interval,
    )

  @overload(QScrollerProperties)
  def setScrollerProperties(self, prop: QScrollerProperties) -> None:
    """
    Calls Qt's 'void QScroller::setScrollerProperties(const
    QScrollerProperties &prop)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscroller.html#setScrollerProperties

    Parameters
    ----------

    prop : QScrollerProperties
      Passed on as a value: Qt reads the C++ QScrollerProperties, which stays
      Python's own.
    """
    #  void QScroller::setScrollerProperties(const QScrollerProperties &prop)
    self.uglySide.call(
        'ritual_ZN9QScroller21setScrollerPropertiesERK19QScrollerProperties',
        self._valueOf(prop),
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

  @overload(Input, QPointF)
  @overload(Input, QPointF, int)
  def handleInput(
      self,
      input: Input,
      position: QPointF,
      timestamp: int = 0,
  ) -> bool:
    """
    Calls Qt's 'bool QScroller::handleInput(Input input, const QPointF
    &position, qint64 timestamp)'.

    Qt's own words: https://doc.qt.io/qt-6/qscroller.html#handleInput

    Parameters
    ----------

    input : Input
      Passed on as its number.

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    timestamp : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  bool QScroller::handleInput(Input input, const QPointF &position,
    #      qint64 timestamp)
    return self.uglySide.call(
        'ritual_ZN9QScroller11handleInputENS_5InputERK7QPointFx',
        input.value, self._valueOf(position), timestamp,
    )

  def stop(self) -> None:
    """
    Calls Qt's 'void QScroller::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qscroller.html#stop
    """
    #  void QScroller::stop()
    self.uglySide.call('ritual_ZN9QScroller4stopEv')

  @overload(QPointF)
  def scrollTo(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QScroller::scrollTo(const QPointF &pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qscroller.html#scrollTo

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QScroller::scrollTo(const QPointF &pos)
    self.uglySide.call(
        'ritual_ZN9QScroller8scrollToERK7QPointF', self._valueOf(pos),
    )

  @overload(QPointF, int)
  def scrollTo(self, pos: QPointF, scrollTime: int) -> None:
    """
    Calls Qt's 'void QScroller::scrollTo(const QPointF &pos, int
    scrollTime)'.

    Qt's own words: https://doc.qt.io/qt-6/qscroller.html#scrollTo

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    scrollTime : int
      Passed on as it is.
    """
    #  void QScroller::scrollTo(const QPointF &pos, int scrollTime)
    self.uglySide.call(
        'ritual_ZN9QScroller8scrollToERK7QPointFi',
        self._valueOf(pos), scrollTime,
    )

  @overload(QRectF, float, float)
  def ensureVisible(
      self,
      rect: QRectF,
      xmargin: float,
      ymargin: float,
  ) -> None:
    """
    Calls Qt's 'void QScroller::ensureVisible(const QRectF &rect, qreal
    xmargin, qreal ymargin)'.

    Qt's own words: https://doc.qt.io/qt-6/qscroller.html#ensureVisible

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    xmargin : float
      Passed on as it is.

    ymargin : float
      Passed on as it is.
    """
    #  void QScroller::ensureVisible(const QRectF &rect, qreal xmargin, qreal
    #      ymargin)
    self.uglySide.call(
        'ritual_ZN9QScroller13ensureVisibleERK6QRectFdd',
        self._valueOf(rect), xmargin, ymargin,
    )

  @overload(QRectF, float, float, int)
  def ensureVisible(
      self,
      rect: QRectF,
      xmargin: float,
      ymargin: float,
      scrollTime: int,
  ) -> None:
    """
    Calls Qt's 'void QScroller::ensureVisible(const QRectF &rect, qreal
    xmargin, qreal ymargin, int scrollTime)'.

    Qt's own words: https://doc.qt.io/qt-6/qscroller.html#ensureVisible

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    xmargin : float
      Passed on as it is.

    ymargin : float
      Passed on as it is.

    scrollTime : int
      Passed on as it is.
    """
    #  void QScroller::ensureVisible(const QRectF &rect, qreal xmargin, qreal
    #      ymargin, int scrollTime)
    self.uglySide.call(
        'ritual_ZN9QScroller13ensureVisibleERK6QRectFddi',
        self._valueOf(rect), xmargin, ymargin, scrollTime,
    )

  def resendPrepareEvent(self) -> None:
    """
    Calls Qt's 'void QScroller::resendPrepareEvent()'.

    Qt's own words: https://doc.qt.io/qt-6/qscroller.html#resendPrepareEvent
    """
    #  void QScroller::resendPrepareEvent()
    self.uglySide.call('ritual_ZN9QScroller18resendPrepareEventEv')


#  Qt's 'QList<QScroller *>': the list of QScroller, which 'QList[QScroller]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QScroller.
QList.createKind(
    QScroller, 'address',
    make='ritual_list_make_QScroller_ptr',
    add='ritual_list_add_QScroller_ptr',
    size='ritual_list_size_QScroller_ptr',
    at='ritual_list_at_QScroller_ptr',
    drop='ritual_list_drop_QScroller_ptr',
)
