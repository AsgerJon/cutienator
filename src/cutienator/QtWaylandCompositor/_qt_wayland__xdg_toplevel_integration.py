"""
QtWayland::XdgToplevelIntegration binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandxdgshellintegration_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtWayland::XdgToplevelIntegration to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import Qt, QObject
from . import QWaylandQuickShellIntegration

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject, QPointF
  from ..QtGui import QMouseEvent, QTouchEvent
  from . import QWaylandSeat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QPointF = WAIT['QPointF']
  QTouchEvent = WAIT['QTouchEvent']
  QWaylandSeat = WAIT['QWaylandSeat']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class XdgToplevelIntegration(QWaylandQuickShellIntegration):
  """
  The cute side of Qt's QtWayland::XdgToplevelIntegration: a plain Python
  object standing in front of one C++ QtWayland::XdgToplevelIntegration.

  It is built on the cute 'QWaylandQuickShellIntegration', as Qt's
  QtWayland::XdgToplevelIntegration is built on Qt's
  QWaylandQuickShellIntegration, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtWayland::XdgToplevelIntegration that has a ritual
  and that Python can call so far, 19 names in all: 'metaObject',
  'eventFilter', 'handleStartMove', 'handleStartResize',
  'handleSetMaximized', 'handleUnsetMaximized', 'handleMaximizedChanged',
  'handleSetFullscreen', 'handleUnsetFullscreen', 'handleFullscreenChanged',
  'handleActivatedChanged', 'handleSurfaceSizeChanged',
  'handleToplevelDestroyed', 'handleMaximizedSizeChanged',
  'handleFullscreenSizeChanged', 'filterPointerMoveEvent',
  'filterMouseMoveEvent', 'filterPointerReleaseEvent',
  'filterTouchUpdateEvent'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtWayland::XdgToplevelIntegration::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QtWayland::XdgToplevelIntegration::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  4 of the 25 functions Qt declares: 2 not a gap; 2 leans on 'QtWayland.

  What to expect
  --------------

  - The C++ QtWayland::XdgToplevelIntegration is created at the first use,
    not by 'QtWayland::XdgToplevelIntegration(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtWayland::XdgToplevelIntegration.
  - Qt tells when it has removed the C++ QtWayland::XdgToplevelIntegration.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QtWayland::XdgToplevelIntegration that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtWayland::XdgToplevelIntegration'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QtWayland::XdgToplevelIntegration::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-xdgtoplevelintegration.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtWayland::XdgToplevelIntegration::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK9QtWayland22XdgToplevelIntegration10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QtWayland::XdgToplevelIntegration::XdgToplevelIntegration(
    QWaylandQuickShellSurfaceItem *item)': leans on
    'QtWayland::XdgToplevelIntegration::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QtWayland.XdgToplevelIntegration.__init__' has no cute function "
        "yet. Qt's "
        "'QtWayland::XdgToplevelIntegration::XdgToplevelIntegration(QWayland"
        "QuickShellSurfaceItem *item)': leans on "
        "'QtWayland::XdgToplevelIntegration::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(
      self,
      object: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QtWayland::XdgToplevelIntegration::eventFilter(QObject
    *object, QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-xdgtoplevelintegration.html#eventFilter

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QtWayland::XdgToplevelIntegration::eventFilter(QObject *object,
    #      QEvent *event)
    ritual = (
        'ritual_ZN9QtWayland22XdgToplevelIntegration11eventFilterEP7QObject'
        'P6QEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QtWayland22XdgToplevelIntegration11eventFilterEP7Q'
          'ObjectP6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(object, 'QObject'), self._addressOf(event),
    )

  @overload(QWaylandSeat)
  @overload(NoneType)
  def handleStartMove(self, seat: Optional[QWaylandSeat]) -> None:
    """
    Calls Qt's 'void
    QtWayland::XdgToplevelIntegration::handleStartMove(QWaylandSeat *seat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-xdgtoplevelintegration.html

    Parameters
    ----------

    seat : Optional[QWaylandSeat]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtWayland::XdgToplevelIntegration::handleStartMove(QWaylandSeat
    #      *seat)
    self.uglySide.call(
        'ritual_ZN9QtWayland22XdgToplevelIntegration15handleStartMoveEP12QW'
        'aylandSeat',
        self._addressOf(seat),
    )

  @overload(QWaylandSeat, Qt.Edges)
  @overload(NoneType, Qt.Edges)
  def handleStartResize(
      self,
      seat: Optional[QWaylandSeat],
      edges: Qt.Edges,
  ) -> None:
    """
    Calls Qt's 'void
    QtWayland::XdgToplevelIntegration::handleStartResize(QWaylandSeat *seat,
    Qt::Edges edges)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-xdgtoplevelintegration.html

    Parameters
    ----------

    seat : Optional[QWaylandSeat]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    edges : Qt.Edges
      Passed on as its number.
    """
    #  void QtWayland::XdgToplevelIntegration::handleStartResize(QWaylandSeat
    #      *seat, Qt::Edges edges)
    self.uglySide.call(
        'ritual_ZN9QtWayland22XdgToplevelIntegration17handleStartResizeEP12'
        'QWaylandSeat6QFlagsIN2Qt4EdgeEE',
        self._addressOf(seat), edges.value,
    )

  def handleSetMaximized(self) -> None:
    """
    Calls Qt's 'void
    QtWayland::XdgToplevelIntegration::handleSetMaximized()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-xdgtoplevelintegration.html
    """
    #  void QtWayland::XdgToplevelIntegration::handleSetMaximized()
    self.uglySide.call(
        'ritual_ZN9QtWayland22XdgToplevelIntegration18handleSetMaximizedEv',
    )

  def handleUnsetMaximized(self) -> None:
    """
    Calls Qt's 'void
    QtWayland::XdgToplevelIntegration::handleUnsetMaximized()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-xdgtoplevelintegration.html
    """
    #  void QtWayland::XdgToplevelIntegration::handleUnsetMaximized()
    self.uglySide.call(
        'ritual_ZN9QtWayland22XdgToplevelIntegration20handleUnsetMaximizedE'
        'v',
    )

  def handleMaximizedChanged(self) -> None:
    """
    Calls Qt's 'void
    QtWayland::XdgToplevelIntegration::handleMaximizedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-xdgtoplevelintegration.html
    """
    #  void QtWayland::XdgToplevelIntegration::handleMaximizedChanged()
    self.uglySide.call(
        'ritual_ZN9QtWayland22XdgToplevelIntegration22handleMaximizedChange'
        'dEv',
    )

  def handleSetFullscreen(self) -> None:
    """
    Calls Qt's 'void
    QtWayland::XdgToplevelIntegration::handleSetFullscreen()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-xdgtoplevelintegration.html
    """
    #  void QtWayland::XdgToplevelIntegration::handleSetFullscreen()
    self.uglySide.call(
        'ritual_ZN9QtWayland22XdgToplevelIntegration19handleSetFullscreenEv',
    )

  def handleUnsetFullscreen(self) -> None:
    """
    Calls Qt's 'void
    QtWayland::XdgToplevelIntegration::handleUnsetFullscreen()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-xdgtoplevelintegration.html
    """
    #  void QtWayland::XdgToplevelIntegration::handleUnsetFullscreen()
    self.uglySide.call(
        'ritual_ZN9QtWayland22XdgToplevelIntegration21handleUnsetFullscreen'
        'Ev',
    )

  def handleFullscreenChanged(self) -> None:
    """
    Calls Qt's 'void
    QtWayland::XdgToplevelIntegration::handleFullscreenChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-xdgtoplevelintegration.html
    """
    #  void QtWayland::XdgToplevelIntegration::handleFullscreenChanged()
    self.uglySide.call(
        'ritual_ZN9QtWayland22XdgToplevelIntegration23handleFullscreenChang'
        'edEv',
    )

  def handleActivatedChanged(self) -> None:
    """
    Calls Qt's 'void
    QtWayland::XdgToplevelIntegration::handleActivatedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-xdgtoplevelintegration.html
    """
    #  void QtWayland::XdgToplevelIntegration::handleActivatedChanged()
    self.uglySide.call(
        'ritual_ZN9QtWayland22XdgToplevelIntegration22handleActivatedChange'
        'dEv',
    )

  def handleSurfaceSizeChanged(self) -> None:
    """
    Calls Qt's 'void
    QtWayland::XdgToplevelIntegration::handleSurfaceSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-xdgtoplevelintegration.html
    """
    #  void QtWayland::XdgToplevelIntegration::handleSurfaceSizeChanged()
    self.uglySide.call(
        'ritual_ZN9QtWayland22XdgToplevelIntegration24handleSurfaceSizeChan'
        'gedEv',
    )

  def handleToplevelDestroyed(self) -> None:
    """
    Calls Qt's 'void
    QtWayland::XdgToplevelIntegration::handleToplevelDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-xdgtoplevelintegration.html
    """
    #  void QtWayland::XdgToplevelIntegration::handleToplevelDestroyed()
    self.uglySide.call(
        'ritual_ZN9QtWayland22XdgToplevelIntegration23handleToplevelDestroy'
        'edEv',
    )

  def handleMaximizedSizeChanged(self) -> None:
    """
    Calls Qt's 'void
    QtWayland::XdgToplevelIntegration::handleMaximizedSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-xdgtoplevelintegration.html
    """
    #  void QtWayland::XdgToplevelIntegration::handleMaximizedSizeChanged()
    self.uglySide.call(
        'ritual_ZN9QtWayland22XdgToplevelIntegration26handleMaximizedSizeCh'
        'angedEv',
    )

  def handleFullscreenSizeChanged(self) -> None:
    """
    Calls Qt's 'void
    QtWayland::XdgToplevelIntegration::handleFullscreenSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-xdgtoplevelintegration.html
    """
    #  void QtWayland::XdgToplevelIntegration::handleFullscreenSizeChanged()
    self.uglySide.call(
        'ritual_ZN9QtWayland22XdgToplevelIntegration27handleFullscreenSizeC'
        'hangedEv',
    )

  @overload(QPointF)
  def filterPointerMoveEvent(self, scenePosition: QPointF) -> bool:
    """
    Calls Qt's 'bool
    QtWayland::XdgToplevelIntegration::filterPointerMoveEvent(const QPointF
    &scenePosition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-xdgtoplevelintegration.html

    Parameters
    ----------

    scenePosition : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QtWayland::XdgToplevelIntegration::filterPointerMoveEvent(const
    #      QPointF &scenePosition)
    return self.uglySide.call(
        'ritual_ZN9QtWayland22XdgToplevelIntegration22filterPointerMoveEven'
        'tERK7QPointF',
        self._valueOf(scenePosition, 'QPointF'),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def filterMouseMoveEvent(self, event: Optional[QMouseEvent]) -> bool:
    """
    Calls Qt's 'bool
    QtWayland::XdgToplevelIntegration::filterMouseMoveEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-xdgtoplevelintegration.html

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QtWayland::XdgToplevelIntegration::filterMouseMoveEvent(
    #      QMouseEvent *event)
    return self.uglySide.call(
        'ritual_ZN9QtWayland22XdgToplevelIntegration20filterMouseMoveEventE'
        'P11QMouseEvent',
        self._addressOf(event),
    )

  def filterPointerReleaseEvent(self) -> bool:
    """
    Calls Qt's 'bool
    QtWayland::XdgToplevelIntegration::filterPointerReleaseEvent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-xdgtoplevelintegration.html
    """
    #  bool QtWayland::XdgToplevelIntegration::filterPointerReleaseEvent()
    return self.uglySide.call(
        'ritual_ZN9QtWayland22XdgToplevelIntegration25filterPointerReleaseE'
        'ventEv',
    )

  @overload(QTouchEvent)
  @overload(NoneType)
  def filterTouchUpdateEvent(self, event: Optional[QTouchEvent]) -> bool:
    """
    Calls Qt's 'bool
    QtWayland::XdgToplevelIntegration::filterTouchUpdateEvent(QTouchEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-xdgtoplevelintegration.html

    Parameters
    ----------

    event : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QtWayland::XdgToplevelIntegration::filterTouchUpdateEvent(
    #      QTouchEvent *event)
    return self.uglySide.call(
        'ritual_ZN9QtWayland22XdgToplevelIntegration22filterTouchUpdateEven'
        'tEP11QTouchEvent',
        self._addressOf(event),
    )
