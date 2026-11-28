"""
QtWayland::WlShellIntegration binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandwlshellintegration_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtWayland::WlShellIntegration to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject
from . import QWaylandQuickShellIntegration, QWaylandWlShellSurface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject, QPoint, QPointF
  from ..QtGui import QMouseEvent
  from . import QWaylandOutput, QWaylandSeat, QWaylandSurface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QWaylandOutput = WAIT['QWaylandOutput']
  QWaylandSeat = WAIT['QWaylandSeat']
  QWaylandSurface = WAIT['QWaylandSurface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class WlShellIntegration(QWaylandQuickShellIntegration):
  """
  The cute side of Qt's QtWayland::WlShellIntegration: a plain Python object
  standing in front of one C++ QtWayland::WlShellIntegration.

  It is built on the cute 'QWaylandQuickShellIntegration', as Qt's
  QtWayland::WlShellIntegration is built on Qt's
  QWaylandQuickShellIntegration, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtWayland::WlShellIntegration that has a ritual and
  that Python can call so far, 20 names in all: 'metaObject', 'eventFilter',
  'handleStartMove', 'handleStartResize', 'handleSetDefaultTopLevel',
  'handleSetTransient', 'handleSetMaximized', 'handleSetFullScreen',
  'handleSetPopup', 'handleShellSurfaceDestroyed',
  'handleSurfaceHasContentChanged', 'handleRedraw',
  'adjustOffsetForNextFrame', 'handleFullScreenSizeChanged',
  'handleMaximizedSizeChanged', 'handlePopupClosed', 'handlePopupRemoved',
  'devicePixelRatio', 'filterMouseMoveEvent', 'filterMouseReleaseEvent'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtWayland::WlShellIntegration::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QtWayland::WlShellIntegration::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QtWayland::WlShellIntegration::~WlShellIntegration()': the
    destructor: Python never removes a C++ QtWayland::WlShellIntegration.

  What has no ritual
  ------------------

  4 of the 27 functions Qt declares: 2 not a gap; 2 leans on 'QtWayland.

  What to expect
  --------------

  - The C++ QtWayland::WlShellIntegration is created at the first use, not by
    'QtWayland::WlShellIntegration(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtWayland::WlShellIntegration.
  - Qt tells when it has removed the C++ QtWayland::WlShellIntegration. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QtWayland::WlShellIntegration that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtWayland::WlShellIntegration'

  #  A C++ QtWayland::WlShellIntegration Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtWayland_WlShellIntegration'

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
    *QtWayland::WlShellIntegration::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-wlshellintegration.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtWayland::WlShellIntegration::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK9QtWayland18WlShellIntegration10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def devicePixelRatio(self) -> float:
    """
    Calls Qt's 'qreal QtWayland::WlShellIntegration::devicePixelRatio()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-wlshellintegration.html#devicePixelRatio
    """
    #  qreal QtWayland::WlShellIntegration::devicePixelRatio() const
    return self.uglySide.call(
        'ritual_ZNK9QtWayland18WlShellIntegration16devicePixelRatioEv',
    )

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
    Qt's 'QtWayland::WlShellIntegration::WlShellIntegration(
    QWaylandQuickShellSurfaceItem *item)': leans on
    'QtWayland::WlShellIntegration::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QtWayland.WlShellIntegration.__init__' has no cute function yet. "
        "Qt's "
        "'QtWayland::WlShellIntegration::WlShellIntegration(QWaylandQuickShe"
        "llSurfaceItem *item)': leans on "
        "'QtWayland::WlShellIntegration::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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
    Calls Qt's 'bool QtWayland::WlShellIntegration::eventFilter(QObject
    *object, QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-wlshellintegration.html#eventFilter

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QtWayland::WlShellIntegration::eventFilter(QObject *object,
    #      QEvent *event)
    ritual = (
        'ritual_ZN9QtWayland18WlShellIntegration11eventFilterEP7QObjectP6QE'
        'vent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QtWayland18WlShellIntegration11eventFilterEP7QObje'
          'ctP6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(object, 'QObject'), self._addressOf(event),
    )

  @overload(QWaylandSeat)
  @overload(NoneType)
  def handleStartMove(self, seat: Optional[QWaylandSeat]) -> None:
    """
    Calls Qt's 'void
    QtWayland::WlShellIntegration::handleStartMove(QWaylandSeat *seat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-wlshellintegration.html#handleStartMove

    Parameters
    ----------

    seat : Optional[QWaylandSeat]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtWayland::WlShellIntegration::handleStartMove(QWaylandSeat
    #      *seat)
    self.uglySide.call(
        'ritual_ZN9QtWayland18WlShellIntegration15handleStartMoveEP12QWayla'
        'ndSeat',
        self._addressOf(seat),
    )

  @overload(QWaylandSeat, QWaylandWlShellSurface.ResizeEdge)
  @overload(NoneType, QWaylandWlShellSurface.ResizeEdge)
  def handleStartResize(
      self,
      seat: Optional[QWaylandSeat],
      edges: QWaylandWlShellSurface.ResizeEdge,
  ) -> None:
    """
    Calls Qt's 'void
    QtWayland::WlShellIntegration::handleStartResize(QWaylandSeat *seat,
    QWaylandWlShellSurface::ResizeEdge edges)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-wlshellintegration.html

    Parameters
    ----------

    seat : Optional[QWaylandSeat]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    edges : QWaylandWlShellSurface.ResizeEdge
      Passed on as its number.
    """
    #  void QtWayland::WlShellIntegration::handleStartResize(QWaylandSeat
    #      *seat, QWaylandWlShellSurface::ResizeEdge edges)
    self.uglySide.call(
        'ritual_ZN9QtWayland18WlShellIntegration17handleStartResizeEP12QWay'
        'landSeatN22QWaylandWlShellSurface10ResizeEdgeE',
        self._addressOf(seat), edges.value,
    )

  def handleSetDefaultTopLevel(self) -> None:
    """
    Calls Qt's 'void
    QtWayland::WlShellIntegration::handleSetDefaultTopLevel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-wlshellintegration.html
    """
    #  void QtWayland::WlShellIntegration::handleSetDefaultTopLevel()
    self.uglySide.call(
        'ritual_ZN9QtWayland18WlShellIntegration24handleSetDefaultTopLevelE'
        'v',
    )

  @overload(QWaylandSurface, QPoint, bool)
  @overload(NoneType, QPoint, bool)
  def handleSetTransient(
      self,
      parentSurface: Optional[QWaylandSurface],
      relativeToParent: QPoint,
      inactive: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QtWayland::WlShellIntegration::handleSetTransient(QWaylandSurface
    *parentSurface, const QPoint &relativeToParent, bool inactive)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-wlshellintegration.html

    Parameters
    ----------

    parentSurface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    relativeToParent : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    inactive : bool
      Passed on as it is.
    """
    #  void QtWayland::WlShellIntegration::handleSetTransient(QWaylandSurface
    #      *parentSurface, const QPoint &relativeToParent, bool inactive)
    self.uglySide.call(
        'ritual_ZN9QtWayland18WlShellIntegration18handleSetTransientEP15QWa'
        'ylandSurfaceRK6QPointb',
        self._addressOf(parentSurface), self._valueOf(relativeToParent),
        inactive,
    )

  @overload(QWaylandOutput)
  @overload(NoneType)
  def handleSetMaximized(self, output: Optional[QWaylandOutput]) -> None:
    """
    Calls Qt's 'void
    QtWayland::WlShellIntegration::handleSetMaximized(QWaylandOutput
    *output)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-wlshellintegration.html

    Parameters
    ----------

    output : Optional[QWaylandOutput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtWayland::WlShellIntegration::handleSetMaximized(QWaylandOutput
    #      *output)
    self.uglySide.call(
        'ritual_ZN9QtWayland18WlShellIntegration18handleSetMaximizedEP14QWa'
        'ylandOutput',
        self._addressOf(output),
    )

  @overload(QWaylandWlShellSurface.FullScreenMethod, int, QWaylandOutput)
  @overload(QWaylandWlShellSurface.FullScreenMethod, int, NoneType)
  def handleSetFullScreen(
      self,
      method: QWaylandWlShellSurface.FullScreenMethod,
      framerate: int,
      output: Optional[QWaylandOutput],
  ) -> None:
    """
    Calls Qt's 'void QtWayland::WlShellIntegration::handleSetFullScreen(
    QWaylandWlShellSurface::FullScreenMethod method, uint framerate,
    QWaylandOutput *output)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-wlshellintegration.html

    Parameters
    ----------

    method : QWaylandWlShellSurface.FullScreenMethod
      Passed on as its number.

    framerate : int
      Passed on as it is.

    output : Optional[QWaylandOutput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtWayland::WlShellIntegration::handleSetFullScreen(
    #      QWaylandWlShellSurface::FullScreenMethod method, uint framerate,
    #      QWaylandOutput *output)
    self.uglySide.call(
        'ritual_ZN9QtWayland18WlShellIntegration19handleSetFullScreenEN22QW'
        'aylandWlShellSurface16FullScreenMethodEjP14QWaylandOutput',
        method.value, framerate, self._addressOf(output),
    )

  @overload(QWaylandSeat, QWaylandSurface, QPoint)
  @overload(QWaylandSeat, NoneType, QPoint)
  @overload(NoneType, QWaylandSurface, QPoint)
  @overload(NoneType, NoneType, QPoint)
  def handleSetPopup(
      self,
      seat: Optional[QWaylandSeat],
      parent: Optional[QWaylandSurface],
      relativeToParent: QPoint,
  ) -> None:
    """
    Calls Qt's 'void
    QtWayland::WlShellIntegration::handleSetPopup(QWaylandSeat *seat,
    QWaylandSurface *parent, const QPoint &relativeToParent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-wlshellintegration.html#handleSetPopup

    Parameters
    ----------

    seat : Optional[QWaylandSeat]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    relativeToParent : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QtWayland::WlShellIntegration::handleSetPopup(QWaylandSeat *seat,
    #      QWaylandSurface *parent, const QPoint &relativeToParent)
    self.uglySide.call(
        'ritual_ZN9QtWayland18WlShellIntegration14handleSetPopupEP12QWaylan'
        'dSeatP15QWaylandSurfaceRK6QPoint',
        self._addressOf(seat), self._addressOf(parent),
        self._valueOf(relativeToParent),
    )

  def handleShellSurfaceDestroyed(self) -> None:
    """
    Calls Qt's 'void
    QtWayland::WlShellIntegration::handleShellSurfaceDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-wlshellintegration.html
    """
    #  void QtWayland::WlShellIntegration::handleShellSurfaceDestroyed()
    self.uglySide.call(
        'ritual_ZN9QtWayland18WlShellIntegration27handleShellSurfaceDestroy'
        'edEv',
    )

  def handleSurfaceHasContentChanged(self) -> None:
    """
    Calls Qt's 'void
    QtWayland::WlShellIntegration::handleSurfaceHasContentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-wlshellintegration.html
    """
    #  void QtWayland::WlShellIntegration::handleSurfaceHasContentChanged()
    self.uglySide.call(
        'ritual_ZN9QtWayland18WlShellIntegration30handleSurfaceHasContentCh'
        'angedEv',
    )

  def handleRedraw(self) -> None:
    """
    Calls Qt's 'void QtWayland::WlShellIntegration::handleRedraw()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-wlshellintegration.html#handleRedraw
    """
    #  void QtWayland::WlShellIntegration::handleRedraw()
    self.uglySide.call(
        'ritual_ZN9QtWayland18WlShellIntegration12handleRedrawEv',
    )

  @overload(QPointF)
  def adjustOffsetForNextFrame(self, offset: QPointF) -> None:
    """
    Calls Qt's 'void
    QtWayland::WlShellIntegration::adjustOffsetForNextFrame(const QPointF
    &offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-wlshellintegration.html

    Parameters
    ----------

    offset : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QtWayland::WlShellIntegration::adjustOffsetForNextFrame(const
    #      QPointF &offset)
    self.uglySide.call(
        'ritual_ZN9QtWayland18WlShellIntegration24adjustOffsetForNextFrameE'
        'RK7QPointF',
        self._valueOf(offset, 'QPointF'),
    )

  def handleFullScreenSizeChanged(self) -> None:
    """
    Calls Qt's 'void
    QtWayland::WlShellIntegration::handleFullScreenSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-wlshellintegration.html
    """
    #  void QtWayland::WlShellIntegration::handleFullScreenSizeChanged()
    self.uglySide.call(
        'ritual_ZN9QtWayland18WlShellIntegration27handleFullScreenSizeChang'
        'edEv',
    )

  def handleMaximizedSizeChanged(self) -> None:
    """
    Calls Qt's 'void
    QtWayland::WlShellIntegration::handleMaximizedSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-wlshellintegration.html
    """
    #  void QtWayland::WlShellIntegration::handleMaximizedSizeChanged()
    self.uglySide.call(
        'ritual_ZN9QtWayland18WlShellIntegration26handleMaximizedSizeChange'
        'dEv',
    )

  def handlePopupClosed(self) -> None:
    """
    Calls Qt's 'void QtWayland::WlShellIntegration::handlePopupClosed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-wlshellintegration.html
    """
    #  void QtWayland::WlShellIntegration::handlePopupClosed()
    self.uglySide.call(
        'ritual_ZN9QtWayland18WlShellIntegration17handlePopupClosedEv',
    )

  def handlePopupRemoved(self) -> None:
    """
    Calls Qt's 'void QtWayland::WlShellIntegration::handlePopupRemoved()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-wlshellintegration.html
    """
    #  void QtWayland::WlShellIntegration::handlePopupRemoved()
    self.uglySide.call(
        'ritual_ZN9QtWayland18WlShellIntegration18handlePopupRemovedEv',
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def filterMouseMoveEvent(self, event: Optional[QMouseEvent]) -> bool:
    """
    Calls Qt's 'bool
    QtWayland::WlShellIntegration::filterMouseMoveEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-wlshellintegration.html

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QtWayland::WlShellIntegration::filterMouseMoveEvent(QMouseEvent
    #      *event)
    return self.uglySide.call(
        'ritual_ZN9QtWayland18WlShellIntegration20filterMouseMoveEventEP11Q'
        'MouseEvent',
        self._addressOf(event),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def filterMouseReleaseEvent(self, event: Optional[QMouseEvent]) -> bool:
    """
    Calls Qt's 'bool
    QtWayland::WlShellIntegration::filterMouseReleaseEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-wlshellintegration.html

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool
    #      QtWayland::WlShellIntegration::filterMouseReleaseEvent(QMouseEvent
    #      *event)
    return self.uglySide.call(
        'ritual_ZN9QtWayland18WlShellIntegration23filterMouseReleaseEventEP'
        '11QMouseEvent',
        self._addressOf(event),
    )
