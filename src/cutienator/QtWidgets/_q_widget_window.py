"""
QWidgetWindow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qwidgetwindow_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QWidgetWindow to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtGui import QWindow

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QAccessibleInterface, QDragLeaveEvent, QDropEvent
  from ..QtGui import QExposeEvent, QMouseEvent, QMoveEvent
  from ..QtGui import QNativeGestureEvent, QResizeEvent, QTabletEvent
  from ..QtGui import QTouchEvent, QWindowStateChangeEvent
  from . import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDragLeaveEvent = WAIT['QDragLeaveEvent']
  QDropEvent = WAIT['QDropEvent']
  QExposeEvent = WAIT['QExposeEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QMoveEvent = WAIT['QMoveEvent']
  QNativeGestureEvent = WAIT['QNativeGestureEvent']
  QResizeEvent = WAIT['QResizeEvent']
  QTabletEvent = WAIT['QTabletEvent']
  QTouchEvent = WAIT['QTouchEvent']
  QWidget = WAIT['QWidget']
  QWindowStateChangeEvent = WAIT['QWindowStateChangeEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWidgetWindow(QWindow):
  """
  The cute side of Qt's QWidgetWindow: a plain Python object standing in
  front of one C++ QWidgetWindow.

  It is built on the cute 'QWindow', as Qt's QWidgetWindow is built on Qt's
  QWindow, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWidgetWindow that has a ritual and that Python can
  call so far, 18 names in all: 'metaObject', 'widget', 'accessibleRoot',
  'focusObject', 'focusNextPrevChild', 'handleNonClientAreaMouseEvent',
  'handleTouchEvent', 'handleMoveEvent', 'handleResizeEvent',
  'handleDragLeaveEvent', 'handleDropEvent', 'handleExposeEvent',
  'handleWindowStateChangedEvent', 'handleTabletEvent', 'handleGestureEvent',
  'updateSize', 'updateMargins', 'updateNormalGeometry'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWidgetWindow::~QWidgetWindow()': the destructor: Python never
    removes a C++ QWidgetWindow.

  What has no ritual
  ------------------

  27 of the 46 functions Qt declares: 15 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 5 takes or
  gives a type that cannot be passed yet; 4 leans on 'QWidgetWindow; 1 a
  template; 1 declared and nowhere to be found; 1 leans on 'void
  QWidgetRepaintManager.

  What to expect
  --------------

  - The C++ QWidgetWindow is created at the first use, not by
    'QWidgetWindow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWidgetWindow.
  - Qt tells when it has removed the C++ QWidgetWindow. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QWidget, bool)
  @overload(NoneType, bool)
  def focusNextPrevChild(widget: Optional[QWidget], next: bool) -> None:
    """
    Calls Qt's 'void QWidgetWindow::focusNextPrevChild(QWidget *widget, bool
    next)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetwindow.html#focusNextPrevChild

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    next : bool
      Passed on as it is.
    """
    #  void QWidgetWindow::focusNextPrevChild(QWidget *widget, bool next)
    Rituals.call(
        'ritual_ZN13QWidgetWindow18focusNextPrevChildEP7QWidgetb',
        CuteMixin._addressOf(widget), next,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWidgetWindow'

  #  A C++ QWidgetWindow Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWidgetWindow'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWidgetWindow::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetwindow.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWidgetWindow::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QWidgetWindow10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def widget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QWidgetWindow::widget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetwindow.html#widget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QWidgetWindow::widget() const
    address = self.uglySide.call('ritual_ZNK13QWidgetWindow6widgetEv')
    from . import QWidget
    return QWidget._cuteAt(address)

  def accessibleRoot(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QWidgetWindow::accessibleRoot() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetwindow.html#accessibleRoot

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QWidgetWindow::accessibleRoot() const
    ritual = 'ritual_ZNK13QWidgetWindow14accessibleRootEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QWidgetWindow14accessibleRootEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QAccessibleInterface
    return QAccessibleInterface._cuteAt(address)

  def focusObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QWidgetWindow::focusObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetwindow.html#focusObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QWidgetWindow::focusObject() const
    ritual = 'ritual_ZNK13QWidgetWindow11focusObjectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QWidgetWindow11focusObjectEv'
    address = self.uglySide.call(ritual)
    return QObject._cuteAt(address)

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

  @overload(QMouseEvent)
  @overload(NoneType)
  def handleNonClientAreaMouseEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QWidgetWindow::handleNonClientAreaMouseEvent(QMouseEvent
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetwindow.html#handleNonClientAreaMouseEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetWindow::handleNonClientAreaMouseEvent(QMouseEvent *a0)
    self.uglySide.call(
        'ritual_ZN13QWidgetWindow29handleNonClientAreaMouseEventEP11QMouseE'
        'vent',
        self._addressOf(a0),
    )

  @overload(QTouchEvent)
  @overload(NoneType)
  def handleTouchEvent(self, a0: Optional[QTouchEvent]) -> None:
    """
    Calls Qt's 'void QWidgetWindow::handleTouchEvent(QTouchEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetwindow.html#handleTouchEvent

    Parameters
    ----------

    a0 : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetWindow::handleTouchEvent(QTouchEvent *a0)
    self.uglySide.call(
        'ritual_ZN13QWidgetWindow16handleTouchEventEP11QTouchEvent',
        self._addressOf(a0),
    )

  @overload(QMoveEvent)
  @overload(NoneType)
  def handleMoveEvent(self, a0: Optional[QMoveEvent]) -> None:
    """
    Calls Qt's 'void QWidgetWindow::handleMoveEvent(QMoveEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetwindow.html#handleMoveEvent

    Parameters
    ----------

    a0 : Optional[QMoveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetWindow::handleMoveEvent(QMoveEvent *a0)
    self.uglySide.call(
        'ritual_ZN13QWidgetWindow15handleMoveEventEP10QMoveEvent',
        self._addressOf(a0),
    )

  @overload(QResizeEvent)
  @overload(NoneType)
  def handleResizeEvent(self, a0: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QWidgetWindow::handleResizeEvent(QResizeEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetwindow.html#handleResizeEvent

    Parameters
    ----------

    a0 : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetWindow::handleResizeEvent(QResizeEvent *a0)
    self.uglySide.call(
        'ritual_ZN13QWidgetWindow17handleResizeEventEP12QResizeEvent',
        self._addressOf(a0),
    )

  @overload(QDragLeaveEvent)
  @overload(NoneType)
  def handleDragLeaveEvent(self, a0: Optional[QDragLeaveEvent]) -> None:
    """
    Calls Qt's 'void QWidgetWindow::handleDragLeaveEvent(QDragLeaveEvent
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetwindow.html#handleDragLeaveEvent

    Parameters
    ----------

    a0 : Optional[QDragLeaveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetWindow::handleDragLeaveEvent(QDragLeaveEvent *a0)
    self.uglySide.call(
        'ritual_ZN13QWidgetWindow20handleDragLeaveEventEP15QDragLeaveEvent',
        self._addressOf(a0),
    )

  @overload(QDropEvent)
  @overload(NoneType)
  def handleDropEvent(self, a0: Optional[QDropEvent]) -> None:
    """
    Calls Qt's 'void QWidgetWindow::handleDropEvent(QDropEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetwindow.html#handleDropEvent

    Parameters
    ----------

    a0 : Optional[QDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetWindow::handleDropEvent(QDropEvent *a0)
    self.uglySide.call(
        'ritual_ZN13QWidgetWindow15handleDropEventEP10QDropEvent',
        self._addressOf(a0),
    )

  @overload(QExposeEvent)
  @overload(NoneType)
  def handleExposeEvent(self, a0: Optional[QExposeEvent]) -> None:
    """
    Calls Qt's 'void QWidgetWindow::handleExposeEvent(QExposeEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetwindow.html#handleExposeEvent

    Parameters
    ----------

    a0 : Optional[QExposeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetWindow::handleExposeEvent(QExposeEvent *a0)
    self.uglySide.call(
        'ritual_ZN13QWidgetWindow17handleExposeEventEP12QExposeEvent',
        self._addressOf(a0),
    )

  @overload(QWindowStateChangeEvent)
  @overload(NoneType)
  def handleWindowStateChangedEvent(
      self,
      event: Optional[QWindowStateChangeEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QWidgetWindow::handleWindowStateChangedEvent(QWindowStateChangeEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetwindow.html#handleWindowStateChangedEvent

    Parameters
    ----------

    event : Optional[QWindowStateChangeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetWindow::handleWindowStateChangedEvent(
    #      QWindowStateChangeEvent *event)
    self.uglySide.call(
        'ritual_ZN13QWidgetWindow29handleWindowStateChangedEventEP23QWindow'
        'StateChangeEvent',
        self._addressOf(event),
    )

  @overload(QTabletEvent)
  @overload(NoneType)
  def handleTabletEvent(self, a0: Optional[QTabletEvent]) -> None:
    """
    Calls Qt's 'void QWidgetWindow::handleTabletEvent(QTabletEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetwindow.html#handleTabletEvent

    Parameters
    ----------

    a0 : Optional[QTabletEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetWindow::handleTabletEvent(QTabletEvent *a0)
    self.uglySide.call(
        'ritual_ZN13QWidgetWindow17handleTabletEventEP12QTabletEvent',
        self._addressOf(a0),
    )

  @overload(QNativeGestureEvent)
  @overload(NoneType)
  def handleGestureEvent(self, a0: Optional[QNativeGestureEvent]) -> None:
    """
    Calls Qt's 'void QWidgetWindow::handleGestureEvent(QNativeGestureEvent
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetwindow.html#handleGestureEvent

    Parameters
    ----------

    a0 : Optional[QNativeGestureEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetWindow::handleGestureEvent(QNativeGestureEvent *a0)
    self.uglySide.call(
        'ritual_ZN13QWidgetWindow18handleGestureEventEP19QNativeGestureEven'
        't',
        self._addressOf(a0),
    )

  def updateSize(self) -> bool:
    """
    Calls Qt's 'bool QWidgetWindow::updateSize()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetwindow.html#updateSize
    """
    #  bool QWidgetWindow::updateSize()
    return self.uglySide.call('ritual_ZN13QWidgetWindow10updateSizeEv')

  def updateMargins(self) -> None:
    """
    Calls Qt's 'void QWidgetWindow::updateMargins()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetwindow.html#updateMargins
    """
    #  void QWidgetWindow::updateMargins()
    self.uglySide.call('ritual_ZN13QWidgetWindow13updateMarginsEv')

  def updateNormalGeometry(self) -> None:
    """
    Calls Qt's 'void QWidgetWindow::updateNormalGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetwindow.html#updateNormalGeometry
    """
    #  void QWidgetWindow::updateNormalGeometry()
    self.uglySide.call('ritual_ZN13QWidgetWindow20updateNormalGeometryEv')
