"""
QGraphicsViewPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qgraphicsview_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QGraphicsViewPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QAbstractScrollAreaPrivate, QGraphicsView

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPoint, QPointF, QRect, QRectF
  from ..QtGui import QCursor, QDropEvent, QMouseEvent, QRegion, QTouchEvent
  from ..QtGui import QTransform
  from . import QGraphicsItem, QGraphicsSceneDragDropEvent
  from . import QStyleOptionGraphicsItem, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCursor = WAIT['QCursor']
  QDropEvent = WAIT['QDropEvent']
  QGraphicsItem = WAIT['QGraphicsItem']
  QGraphicsSceneDragDropEvent = WAIT['QGraphicsSceneDragDropEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QRect = WAIT['QRect']
  QRectF = WAIT['QRectF']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
  QTouchEvent = WAIT['QTouchEvent']
  QTransform = WAIT['QTransform']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsViewPrivate(QAbstractScrollAreaPrivate):
  """
  The cute side of Qt's QGraphicsViewPrivate: a plain Python object standing
  in front of one C++ QGraphicsViewPrivate.

  It is built on the cute 'QAbstractScrollAreaPrivate', as Qt's
  QGraphicsViewPrivate is built on Qt's QAbstractScrollAreaPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsViewPrivate that has a ritual and that
  Python can call so far, 35 names in all: 'q_func',
  'recalculateContentSize', 'centerView', 'updateLastCenterPoint',
  'horizontalScroll', 'verticalScroll', 'mapRectToScene', 'mapRectFromScene',
  'updateScroll', 'canStartScrollingAt', 'replayLastMouseEvent',
  'storeMouseEvent', 'mouseMoveEventHandler', 'rubberBandRegion',
  'updateRubberBand', 'clearRubberBand', 'allocStyleOptionsArray',
  'freeStyleOptionsArray', '_q_setViewportCursor', '_q_unsetViewportCursor',
  'storeDragDropEvent', 'populateSceneDragDropEvent', 'mapToViewTransform',
  'mapToViewRect', 'mapToViewRegion', 'processPendingUpdates', 'updateAll',
  'dispatchPendingUpdateRequests', 'setUpdateClip', 'updateRectF',
  'updateRect', 'updateRegion', 'mapToScene', 'translateTouchEvent',
  'updateInputMethodSensitivity'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QGraphicsView *QGraphicsViewPrivate::q_func() const': takes
    in Python what 'QGraphicsView *QGraphicsViewPrivate::q_func()' takes.
  - Qt's 'QGraphicsViewPrivate::~QGraphicsViewPrivate()': the destructor:
    Python never removes a C++ QGraphicsViewPrivate.
  - Qt's 'QList<QGraphicsItem *> QGraphicsViewPrivate::findItems(const
    QRegion &exposedRegion, bool *allItems, const QTransform &viewTransform)
    const': takes a number to change where it is.

  What to expect
  --------------

  - The C++ QGraphicsViewPrivate is created at the first use, not by
    'QGraphicsViewPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsViewPrivate.
  - Each name of Qt's QGraphicsViewPrivate that has no cute function yet,
    'findItems', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, QTouchEvent)
  @overload(THIS, NoneType)
  @overload(NoneType, QTouchEvent)
  @overload(NoneType, NoneType)
  def translateTouchEvent(
      d: Optional[QGraphicsViewPrivate],
      touchEvent: Optional[QTouchEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsViewPrivate::translateTouchEvent(QGraphicsViewPrivate *d,
    QTouchEvent *touchEvent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#translateTouchEvent

    Parameters
    ----------

    d : Optional[QGraphicsViewPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    touchEvent : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsViewPrivate::translateTouchEvent(QGraphicsViewPrivate
    #      *d, QTouchEvent *touchEvent)
    Rituals.call(
        'ritual_ZN20QGraphicsViewPrivate19translateTouchEventEPS_P11QTouchE'
        'vent',
        CuteMixin._addressOf(d), CuteMixin._addressOf(touchEvent),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsViewPrivate'

  #  A C++ QGraphicsViewPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsViewPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def horizontalScroll(self) -> int:
    """
    Calls Qt's 'qint64 QGraphicsViewPrivate::horizontalScroll() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#horizontalScroll
    """
    #  qint64 QGraphicsViewPrivate::horizontalScroll() const
    return self.uglySide.call(
        'ritual_ZNK20QGraphicsViewPrivate16horizontalScrollEv',
    )

  def verticalScroll(self) -> int:
    """
    Calls Qt's 'qint64 QGraphicsViewPrivate::verticalScroll() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#verticalScroll
    """
    #  qint64 QGraphicsViewPrivate::verticalScroll() const
    return self.uglySide.call(
        'ritual_ZNK20QGraphicsViewPrivate14verticalScrollEv',
    )

  @overload(QRect)
  def mapRectToScene(self, rect: QRect) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsViewPrivate::mapRectToScene(const QRect
    &rect) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#mapRectToScene

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsViewPrivate::mapRectToScene(const QRect &rect) const
    address = self.uglySide.call(
        'ritual_ZNK20QGraphicsViewPrivate14mapRectToSceneERK5QRect',
        self._valueOf(rect),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QRectF)
  def mapRectFromScene(self, rect: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsViewPrivate::mapRectFromScene(const QRectF
    &rect) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#mapRectFromScene

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsViewPrivate::mapRectFromScene(const QRectF &rect)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK20QGraphicsViewPrivate16mapRectFromSceneERK6QRectF',
        self._valueOf(rect),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QPoint)
  def canStartScrollingAt(self, startPos: QPoint) -> bool:
    """
    Calls Qt's 'bool QGraphicsViewPrivate::canStartScrollingAt(const QPoint
    &startPos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#canStartScrollingAt

    Parameters
    ----------

    startPos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  bool QGraphicsViewPrivate::canStartScrollingAt(const QPoint &startPos)
    #      const
    ritual = (
        'ritual_ZNK20QGraphicsViewPrivate19canStartScrollingAtERK6QPoint')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QGraphicsViewPrivate19canStartScrollingAtERK6QPo'
          'int')
    return self.uglySide.call(ritual, self._valueOf(startPos))

  @overload(QWidget, QRect)
  @overload(NoneType, QRect)
  def rubberBandRegion(
      self,
      widget: Optional[QWidget],
      rect: QRect,
  ) -> QRegion:
    """
    Calls Qt's 'QRegion QGraphicsViewPrivate::rubberBandRegion(const QWidget
    *widget, const QRect &rect) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#rubberBandRegion

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QGraphicsViewPrivate::rubberBandRegion(const QWidget *widget,
    #      const QRect &rect) const
    address = self.uglySide.call(
        'ritual_ZNK20QGraphicsViewPrivate16rubberBandRegionEPK7QWidgetRK5QR'
        'ect',
        self._addressOf(widget), self._valueOf(rect),
    )
    from ..QtGui import QRegion
    return QRegion._cuteOwning(address)

  @overload(QGraphicsItem)
  @overload(NoneType)
  def mapToViewTransform(self, item: Optional[QGraphicsItem]) -> QTransform:
    """
    Calls Qt's 'QTransform QGraphicsViewPrivate::mapToViewTransform(const
    QGraphicsItem *item) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#mapToViewTransform

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QGraphicsViewPrivate::mapToViewTransform(const
    #      QGraphicsItem *item) const
    address = self.uglySide.call(
        'ritual_ZNK20QGraphicsViewPrivate18mapToViewTransformEPK13QGraphics'
        'Item',
        self._addressOf(item, 'QGraphicsItem'),
    )
    from ..QtGui import QTransform
    return QTransform._cuteOwning(address)

  @overload(QGraphicsItem, QRectF)
  @overload(NoneType, QRectF)
  def mapToViewRect(
      self,
      item: Optional[QGraphicsItem],
      rect: QRectF,
  ) -> QRect:
    """
    Calls Qt's 'QRect QGraphicsViewPrivate::mapToViewRect(const QGraphicsItem
    *item, const QRectF &rect) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#mapToViewRect

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QGraphicsViewPrivate::mapToViewRect(const QGraphicsItem *item,
    #      const QRectF &rect) const
    address = self.uglySide.call(
        'ritual_ZNK20QGraphicsViewPrivate13mapToViewRectEPK13QGraphicsItemR'
        'K6QRectF',
        self._addressOf(item, 'QGraphicsItem'), self._valueOf(rect),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QGraphicsItem, QRectF)
  @overload(NoneType, QRectF)
  def mapToViewRegion(
      self,
      item: Optional[QGraphicsItem],
      rect: QRectF,
  ) -> QRegion:
    """
    Calls Qt's 'QRegion QGraphicsViewPrivate::mapToViewRegion(const
    QGraphicsItem *item, const QRectF &rect) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#mapToViewRegion

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QGraphicsViewPrivate::mapToViewRegion(const QGraphicsItem
    #      *item, const QRectF &rect) const
    address = self.uglySide.call(
        'ritual_ZNK20QGraphicsViewPrivate15mapToViewRegionEPK13QGraphicsIte'
        'mRK6QRectF',
        self._addressOf(item, 'QGraphicsItem'), self._valueOf(rect),
    )
    from ..QtGui import QRegion
    return QRegion._cuteOwning(address)

  @overload(QPointF)
  def mapToScene(self, point: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsViewPrivate::mapToScene(const QPointF
    &point) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#mapToScene

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsViewPrivate::mapToScene(const QPointF &point) const
    address = self.uglySide.call(
        'ritual_ZNK20QGraphicsViewPrivate10mapToSceneERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QRectF)
  def mapToScene(self, rect: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsViewPrivate::mapToScene(const QRectF &rect)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#mapToScene

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsViewPrivate::mapToScene(const QRectF &rect) const
    address = self.uglySide.call(
        'ritual_ZNK20QGraphicsViewPrivate10mapToSceneERK6QRectF',
        self._valueOf(rect),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGraphicsItem)
  @overload(NoneType)
  def setUpdateClip(self, a0: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void QGraphicsViewPrivate::setUpdateClip(QGraphicsItem *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#setUpdateClip

    Parameters
    ----------

    a0 : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsViewPrivate::setUpdateClip(QGraphicsItem *a0)
    self.uglySide.call(
        'ritual_ZN20QGraphicsViewPrivate13setUpdateClipEP13QGraphicsItem',
        self._addressOf(a0, 'QGraphicsItem'),
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
    'QGraphicsViewPrivate::QGraphicsViewPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#QGraphicsViewPrivate
    """
    #  QGraphicsViewPrivate::QGraphicsViewPrivate()
    self._noteCreation(QGraphicsViewPrivate, lambda: Rituals.call(
        'ritual_ZN20QGraphicsViewPrivateC1Ev',
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

  def q_func(self) -> Optional[QGraphicsView]:
    """
    Calls Qt's 'QGraphicsView *QGraphicsViewPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsviewprivate.html#q_func

    Returns
    -------

    Optional[QGraphicsView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsView *QGraphicsViewPrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QGraphicsViewPrivate6q_funcEv')
    return QGraphicsView._cuteAt(address)

  def recalculateContentSize(self) -> None:
    """
    Calls Qt's 'void QGraphicsViewPrivate::recalculateContentSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#recalculateContentSize
    """
    #  void QGraphicsViewPrivate::recalculateContentSize()
    self.uglySide.call(
        'ritual_ZN20QGraphicsViewPrivate22recalculateContentSizeEv',
    )

  @overload(QGraphicsView.ViewportAnchor)
  def centerView(self, anchor: QGraphicsView.ViewportAnchor) -> None:
    """
    Calls Qt's 'void
    QGraphicsViewPrivate::centerView(QGraphicsView::ViewportAnchor anchor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#centerView

    Parameters
    ----------

    anchor : QGraphicsView.ViewportAnchor
      Passed on as its number.
    """
    #  void QGraphicsViewPrivate::centerView(QGraphicsView::ViewportAnchor
    #      anchor)
    self.uglySide.call(
        'ritual_ZN20QGraphicsViewPrivate10centerViewEN13QGraphicsView14View'
        'portAnchorE',
        anchor.value,
    )

  def updateLastCenterPoint(self) -> None:
    """
    Calls Qt's 'void QGraphicsViewPrivate::updateLastCenterPoint()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#updateLastCenterPoint
    """
    #  void QGraphicsViewPrivate::updateLastCenterPoint()
    self.uglySide.call(
        'ritual_ZN20QGraphicsViewPrivate21updateLastCenterPointEv',
    )

  def updateScroll(self) -> None:
    """
    Calls Qt's 'void QGraphicsViewPrivate::updateScroll()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#updateScroll
    """
    #  void QGraphicsViewPrivate::updateScroll()
    self.uglySide.call('ritual_ZN20QGraphicsViewPrivate12updateScrollEv')

  def replayLastMouseEvent(self) -> None:
    """
    Calls Qt's 'void QGraphicsViewPrivate::replayLastMouseEvent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#replayLastMouseEvent
    """
    #  void QGraphicsViewPrivate::replayLastMouseEvent()
    self.uglySide.call(
        'ritual_ZN20QGraphicsViewPrivate20replayLastMouseEventEv',
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def storeMouseEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsViewPrivate::storeMouseEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#storeMouseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsViewPrivate::storeMouseEvent(QMouseEvent *event)
    self.uglySide.call(
        'ritual_ZN20QGraphicsViewPrivate15storeMouseEventEP11QMouseEvent',
        self._addressOf(event),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEventHandler(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsViewPrivate::mouseMoveEventHandler(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#mouseMoveEventHandler

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsViewPrivate::mouseMoveEventHandler(QMouseEvent *event)
    self.uglySide.call(
        'ritual_ZN20QGraphicsViewPrivate21mouseMoveEventHandlerEP11QMouseEv'
        'ent',
        self._addressOf(event),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def updateRubberBand(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsViewPrivate::updateRubberBand(const QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#updateRubberBand

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsViewPrivate::updateRubberBand(const QMouseEvent *event)
    self.uglySide.call(
        'ritual_ZN20QGraphicsViewPrivate16updateRubberBandEPK11QMouseEvent',
        self._addressOf(event),
    )

  def clearRubberBand(self) -> None:
    """
    Calls Qt's 'void QGraphicsViewPrivate::clearRubberBand()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#clearRubberBand
    """
    #  void QGraphicsViewPrivate::clearRubberBand()
    self.uglySide.call('ritual_ZN20QGraphicsViewPrivate15clearRubberBandEv')

  @overload(int)
  def allocStyleOptionsArray(
      self,
      numItems: int,
  ) -> Optional[QStyleOptionGraphicsItem]:
    """
    Calls Qt's 'QStyleOptionGraphicsItem
    *QGraphicsViewPrivate::allocStyleOptionsArray(int numItems)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#allocStyleOptionsArray

    Parameters
    ----------

    numItems : int
      Passed on as it is.

    Returns
    -------

    Optional[QStyleOptionGraphicsItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStyleOptionGraphicsItem
    #      *QGraphicsViewPrivate::allocStyleOptionsArray(int numItems)
    address = self.uglySide.call(
        'ritual_ZN20QGraphicsViewPrivate22allocStyleOptionsArrayEi',
        numItems,
    )
    from . import QStyleOptionGraphicsItem
    return QStyleOptionGraphicsItem._cuteAt(address)

  @overload(QStyleOptionGraphicsItem)
  @overload(NoneType)
  def freeStyleOptionsArray(
      self,
      array: Optional[QStyleOptionGraphicsItem],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsViewPrivate::freeStyleOptionsArray(QStyleOptionGraphicsItem
    *array)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#freeStyleOptionsArray

    Parameters
    ----------

    array : Optional[QStyleOptionGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsViewPrivate::freeStyleOptionsArray(
    #      QStyleOptionGraphicsItem *array)
    self.uglySide.call(
        'ritual_ZN20QGraphicsViewPrivate21freeStyleOptionsArrayEP24QStyleOp'
        'tionGraphicsItem',
        self._addressOf(array),
    )

  @overload(QCursor)
  def _q_setViewportCursor(self, cursor: QCursor) -> None:
    """
    Calls Qt's 'void QGraphicsViewPrivate::_q_setViewportCursor(const QCursor
    &cursor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#_q_setViewportCursor

    Parameters
    ----------

    cursor : QCursor
      Passed on as a value: Qt reads the C++ QCursor, which stays Python's
      own.
    """
    #  void QGraphicsViewPrivate::_q_setViewportCursor(const QCursor &cursor)
    self.uglySide.call(
        'ritual_ZN20QGraphicsViewPrivate20_q_setViewportCursorERK7QCursor',
        self._valueOf(cursor),
    )

  def _q_unsetViewportCursor(self) -> None:
    """
    Calls Qt's 'void QGraphicsViewPrivate::_q_unsetViewportCursor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#_q_unsetViewportCursor
    """
    #  void QGraphicsViewPrivate::_q_unsetViewportCursor()
    self.uglySide.call(
        'ritual_ZN20QGraphicsViewPrivate22_q_unsetViewportCursorEv',
    )

  @overload(QGraphicsSceneDragDropEvent)
  @overload(NoneType)
  def storeDragDropEvent(
      self,
      event: Optional[QGraphicsSceneDragDropEvent],
  ) -> None:
    """
    Calls Qt's 'void QGraphicsViewPrivate::storeDragDropEvent(const
    QGraphicsSceneDragDropEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#storeDragDropEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneDragDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsViewPrivate::storeDragDropEvent(const
    #      QGraphicsSceneDragDropEvent *event)
    self.uglySide.call(
        'ritual_ZN20QGraphicsViewPrivate18storeDragDropEventEPK27QGraphicsS'
        'ceneDragDropEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneDragDropEvent, QDropEvent)
  @overload(QGraphicsSceneDragDropEvent, NoneType)
  @overload(NoneType, QDropEvent)
  @overload(NoneType, NoneType)
  def populateSceneDragDropEvent(
      self,
      dest: Optional[QGraphicsSceneDragDropEvent],
      source: Optional[QDropEvent],
  ) -> None:
    """
    Calls Qt's 'void QGraphicsViewPrivate::populateSceneDragDropEvent(
    QGraphicsSceneDragDropEvent *dest, QDropEvent *source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html

    Parameters
    ----------

    dest : Optional[QGraphicsSceneDragDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    source : Optional[QDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsViewPrivate::populateSceneDragDropEvent(
    #      QGraphicsSceneDragDropEvent *dest, QDropEvent *source)
    self.uglySide.call(
        'ritual_ZN20QGraphicsViewPrivate26populateSceneDragDropEventEP27QGr'
        'aphicsSceneDragDropEventP10QDropEvent',
        self._addressOf(dest), self._addressOf(source),
    )

  def processPendingUpdates(self) -> None:
    """
    Calls Qt's 'void QGraphicsViewPrivate::processPendingUpdates()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#processPendingUpdates
    """
    #  void QGraphicsViewPrivate::processPendingUpdates()
    self.uglySide.call(
        'ritual_ZN20QGraphicsViewPrivate21processPendingUpdatesEv',
    )

  def updateAll(self) -> None:
    """
    Calls Qt's 'void QGraphicsViewPrivate::updateAll()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#updateAll
    """
    #  void QGraphicsViewPrivate::updateAll()
    self.uglySide.call('ritual_ZN20QGraphicsViewPrivate9updateAllEv')

  def dispatchPendingUpdateRequests(self) -> None:
    """
    Calls Qt's 'void QGraphicsViewPrivate::dispatchPendingUpdateRequests()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html
    """
    #  void QGraphicsViewPrivate::dispatchPendingUpdateRequests()
    self.uglySide.call(
        'ritual_ZN20QGraphicsViewPrivate29dispatchPendingUpdateRequestsEv',
    )

  @overload(QRectF)
  def updateRectF(self, rect: QRectF) -> bool:
    """
    Calls Qt's 'bool QGraphicsViewPrivate::updateRectF(const QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#updateRectF

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  bool QGraphicsViewPrivate::updateRectF(const QRectF &rect)
    return self.uglySide.call(
        'ritual_ZN20QGraphicsViewPrivate11updateRectFERK6QRectF',
        self._valueOf(rect),
    )

  @overload(QRect)
  def updateRect(self, rect: QRect) -> bool:
    """
    Calls Qt's 'bool QGraphicsViewPrivate::updateRect(const QRect &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#updateRect

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  bool QGraphicsViewPrivate::updateRect(const QRect &rect)
    return self.uglySide.call(
        'ritual_ZN20QGraphicsViewPrivate10updateRectERK5QRect',
        self._valueOf(rect),
    )

  @overload(QRectF, QTransform)
  def updateRegion(self, rect: QRectF, xform: QTransform) -> bool:
    """
    Calls Qt's 'bool QGraphicsViewPrivate::updateRegion(const QRectF &rect,
    const QTransform &xform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html#updateRegion

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    xform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  bool QGraphicsViewPrivate::updateRegion(const QRectF &rect, const
    #      QTransform &xform)
    return self.uglySide.call(
        'ritual_ZN20QGraphicsViewPrivate12updateRegionERK6QRectFRK10QTransf'
        'orm',
        self._valueOf(rect), self._valueOf(xform),
    )

  def updateInputMethodSensitivity(self) -> None:
    """
    Calls Qt's 'void QGraphicsViewPrivate::updateInputMethodSensitivity()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsviewprivate.html
    """
    #  void QGraphicsViewPrivate::updateInputMethodSensitivity()
    self.uglySide.call(
        'ritual_ZN20QGraphicsViewPrivate28updateInputMethodSensitivityEv',
    )

  @staticmethod
  def findItems(*__, **_) -> Never:
    """
    Qt's 'QList<QGraphicsItem *> QGraphicsViewPrivate::findItems(const
    QRegion &exposedRegion, bool *allItems, const QTransform &viewTransform)
    const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QGraphicsViewPrivate.findItems' has no cute function yet. Qt's "
        "'QList<QGraphicsItem *> QGraphicsViewPrivate::findItems(const "
        "QRegion &exposedRegion, bool *allItems, const QTransform "
        "&viewTransform) const': takes a number to change where it is.")
