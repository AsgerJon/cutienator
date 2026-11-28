"""
QWaylandMouseTracker binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandmousetracker_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QWaylandMouseTracker to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject
  from ..QtGui import QHoverEvent, QMouseEvent
  from ..QtQuick import QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QHoverEvent = WAIT['QHoverEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandMouseTracker(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWaylandMouseTracker: a plain Python object standing
  in front of one C++ QWaylandMouseTracker.

  What exists
  -----------

  Every function of Qt's QWaylandMouseTracker that has a ritual and that
  Python can call so far, 16 names in all: 'metaObject', 'tr', 'mouseX',
  'mouseY', 'setWindowSystemCursorEnabled', 'windowSystemCursorEnabled',
  'hovered', 'mouseXChanged', 'mouseYChanged',
  'windowSystemCursorEnabledChanged', 'hoveredChanged',
  'childMouseEventFilter', 'mouseMoveEvent', 'hoverMoveEvent',
  'hoverEnterEvent', 'hoverLeaveEvent'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandMouseTracker::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QWaylandMouseTracker::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QWaylandMouseTrackerPrivate *QWaylandMouseTracker::d_func()': gives
    'QWaylandMouseTrackerPrivate', which has no cute class yet.
  - Qt's 'const QWaylandMouseTrackerPrivate *QWaylandMouseTracker::d_func()
    const': gives 'QWaylandMouseTrackerPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandMouseTracker is created at the first use, not by
    'QWaylandMouseTracker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandMouseTracker.
  - Qt tells when it has removed the C++ QWaylandMouseTracker. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

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
    Calls Qt's 'QString QWaylandMouseTracker::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandmousetracker.html#tr

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
    #  QString QWaylandMouseTracker::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QWaylandMouseTracker2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandMouseTracker'

  #  A C++ QWaylandMouseTracker Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaylandMouseTracker'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWaylandMouseTracker::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandmousetracker.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandMouseTracker::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QWaylandMouseTracker10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def mouseX(self) -> float:
    """
    Calls Qt's 'qreal QWaylandMouseTracker::mouseX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandmousetracker.html#mouseX
    """
    #  qreal QWaylandMouseTracker::mouseX() const
    return self.uglySide.call('ritual_ZNK20QWaylandMouseTracker6mouseXEv')

  def mouseY(self) -> float:
    """
    Calls Qt's 'qreal QWaylandMouseTracker::mouseY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandmousetracker.html#mouseY
    """
    #  qreal QWaylandMouseTracker::mouseY() const
    return self.uglySide.call('ritual_ZNK20QWaylandMouseTracker6mouseYEv')

  def windowSystemCursorEnabled(self) -> bool:
    """
    Calls Qt's 'bool QWaylandMouseTracker::windowSystemCursorEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandmousetracker.html
    """
    #  bool QWaylandMouseTracker::windowSystemCursorEnabled() const
    return self.uglySide.call(
        'ritual_ZNK20QWaylandMouseTracker25windowSystemCursorEnabledEv',
    )

  def hovered(self) -> bool:
    """
    Calls Qt's 'bool QWaylandMouseTracker::hovered() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandmousetracker.html#hovered
    """
    #  bool QWaylandMouseTracker::hovered() const
    return self.uglySide.call('ritual_ZNK20QWaylandMouseTracker7hoveredEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setWindowSystemCursorEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QWaylandMouseTracker::setWindowSystemCursorEnabled(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandmousetracker.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QWaylandMouseTracker::setWindowSystemCursorEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN20QWaylandMouseTracker28setWindowSystemCursorEnabledEb',
        enable,
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
    'QWaylandMouseTracker::QWaylandMouseTracker(QQuickItem *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandmousetracker.html#QWaylandMouseTracker

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWaylandMouseTracker::QWaylandMouseTracker(QQuickItem *parent)
    self._noteCreation(QWaylandMouseTracker, lambda: Rituals.call(
        'ritual_ZN20QWaylandMouseTrackerC1EP10QQuickItem',
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

  def mouseXChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandMouseTracker::mouseXChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandmousetracker.html#mouseXChanged
    """
    #  void QWaylandMouseTracker::mouseXChanged()
    self.uglySide.call('ritual_ZN20QWaylandMouseTracker13mouseXChangedEv')

  def mouseYChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandMouseTracker::mouseYChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandmousetracker.html#mouseYChanged
    """
    #  void QWaylandMouseTracker::mouseYChanged()
    self.uglySide.call('ritual_ZN20QWaylandMouseTracker13mouseYChangedEv')

  def windowSystemCursorEnabledChanged(self) -> None:
    """
    Calls Qt's 'void
    QWaylandMouseTracker::windowSystemCursorEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandmousetracker.html
    """
    #  void QWaylandMouseTracker::windowSystemCursorEnabledChanged()
    self.uglySide.call(
        'ritual_ZN20QWaylandMouseTracker32windowSystemCursorEnabledChangedE'
        'v',
    )

  def hoveredChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandMouseTracker::hoveredChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandmousetracker.html#hoveredChanged
    """
    #  void QWaylandMouseTracker::hoveredChanged()
    self.uglySide.call('ritual_ZN20QWaylandMouseTracker14hoveredChangedEv')

  @overload(QQuickItem, QEvent)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def childMouseEventFilter(
      self,
      item: Optional[QQuickItem],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QWaylandMouseTracker::childMouseEventFilter(QQuickItem
    *item, QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandmousetracker.html#childMouseEventFilter

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWaylandMouseTracker::childMouseEventFilter(QQuickItem *item,
    #      QEvent *event)
    ritual = (
        'ritual_ZN20QWaylandMouseTracker21childMouseEventFilterEP10QQuickIt'
        'emP6QEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QWaylandMouseTracker21childMouseEventFilterEP10QQ'
          'uickItemP6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(item), self._addressOf(event),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QWaylandMouseTracker::mouseMoveEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandmousetracker.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandMouseTracker::mouseMoveEvent(QMouseEvent *event)
    ritual = 'ritual_ZN20QWaylandMouseTracker14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QWaylandMouseTracker14mouseMoveEventEP11QMouseEve'
          'nt')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverMoveEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QWaylandMouseTracker::hoverMoveEvent(QHoverEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandmousetracker.html#hoverMoveEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandMouseTracker::hoverMoveEvent(QHoverEvent *event)
    ritual = 'ritual_ZN20QWaylandMouseTracker14hoverMoveEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QWaylandMouseTracker14hoverMoveEventEP11QHoverEve'
          'nt')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverEnterEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QWaylandMouseTracker::hoverEnterEvent(QHoverEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandmousetracker.html#hoverEnterEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandMouseTracker::hoverEnterEvent(QHoverEvent *event)
    ritual = (
        'ritual_ZN20QWaylandMouseTracker15hoverEnterEventEP11QHoverEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QWaylandMouseTracker15hoverEnterEventEP11QHoverEv'
          'ent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverLeaveEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QWaylandMouseTracker::hoverLeaveEvent(QHoverEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandmousetracker.html#hoverLeaveEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandMouseTracker::hoverLeaveEvent(QHoverEvent *event)
    ritual = (
        'ritual_ZN20QWaylandMouseTracker15hoverLeaveEventEP11QHoverEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QWaylandMouseTracker15hoverLeaveEventEP11QHoverEv'
          'ent')
    self.uglySide.call(ritual, self._addressOf(event))
