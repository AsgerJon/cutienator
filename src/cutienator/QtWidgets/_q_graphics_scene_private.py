"""
QGraphicsScenePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qgraphicsscene_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QGraphicsScenePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QPoint, QPointF, QRectF
  from ..QtGui import QFont, QPalette, QTouchEvent
  from . import QGraphicsItem, QGraphicsScene, QGraphicsSceneDragDropEvent
  from . import QGraphicsSceneMouseEvent, QGraphicsView, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QFont = WAIT['QFont']
  QGraphicsItem = WAIT['QGraphicsItem']
  QGraphicsScene = WAIT['QGraphicsScene']
  QGraphicsSceneDragDropEvent = WAIT['QGraphicsSceneDragDropEvent']
  QGraphicsSceneMouseEvent = WAIT['QGraphicsSceneMouseEvent']
  QGraphicsView = WAIT['QGraphicsView']
  QPalette = WAIT['QPalette']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']
  QTouchEvent = WAIT['QTouchEvent']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsScenePrivate(QObjectPrivate):
  """
  The cute side of Qt's QGraphicsScenePrivate: a plain Python object standing
  in front of one C++ QGraphicsScenePrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QGraphicsScenePrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsScenePrivate that has a ritual and that
  Python can call so far, 38 names in all: 'q_func', 'get', '_q_emitUpdated',
  'registerTopLevelItem', 'unregisterTopLevelItem', '_q_polishItems',
  '_q_processDirtyItems', 'setScenePosItemEnabled', 'registerScenePosItem',
  'unregisterScenePosItem', '_q_updateScenePosDescendants',
  'clearMouseGrabber', 'enableMouseTrackingOnViews', 'itemsAtPosition',
  'storeMouseButtonsForMouseGrabber', 'addView', 'removeView',
  'installSceneEventFilter', 'removeSceneEventFilter',
  'filterDescendantEvent', 'filterEvent', 'itemAcceptsHoverEvents_helper',
  'cloneDragDropEvent', 'markDirty', 'processDirtyItemsRecursive',
  'resetDirtyItem', 'ensureSortedTopLevelItems',
  'ensureSequentialTopLevelSiblingIndexes', 'setFont_helper', 'resolveFont',
  'updateFont', 'setPalette_helper', 'resolvePalette', 'updatePalette',
  'updateTouchPointsForItem', 'findClosestTouchPointId',
  'enableTouchEventsOnViews', 'updateInputMethodSensitivityInViews'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QGraphicsScene *QGraphicsScenePrivate::q_func() const': takes
    in Python what 'QGraphicsScene *QGraphicsScenePrivate::q_func()' takes.
  - Qt's 'void QGraphicsScenePrivate::drawItems(QPainter *painter, const
    QTransform *const viewTransform, QRegion *exposedRegion, QWidget
    *widget)': takes a type Python has no way to hand over yet.
  - Qt's 'void QGraphicsScenePrivate::drawSubtreeRecursive(QGraphicsItem
    *item, QPainter *painter, const QTransform *const a2, QRegion
    *exposedRegion, QWidget *widget, qreal parentOpacity, const QTransform
    *const effectTransform)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QGraphicsScenePrivate::gestureTargetsAtHotSpots(const
    QSet<QGesture *> &gestures, Qt::GestureFlag flag, QHash<QGraphicsObject
    *, QSet<QGesture *>> *targets, QSet<QGraphicsObject *> *itemsSet,
    QSet<QGesture *> *normal, QSet<QGesture *> *conflicts)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  30 of the 73 functions Qt declares: 20 leans on 'QGraphicsScenePrivate; 5
  Qt's library has no name for it, and its code in Qt's source does not
  compile apart from its file; 2 cannot be called and cannot be called
  through the meta-object and cannot be copied; 2 leans on 'QGestureManager;
  1 leans on 'vtable for QGraphicsSceneBspTreeIndex', which Qt's source does
  not mark for use from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QGraphicsScenePrivate is created at the first use, not by
    'QGraphicsScenePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsScenePrivate.
  - Each name of Qt's QGraphicsScenePrivate that has no cute function yet,
    '_q_updateLater', 'addPopup', 'cancelGesturesForChildren',
    'clearKeyboardGrabber', 'dispatchHoverEvent', 'draw', 'drawItemHelper',
    'drawItems', 'drawSubtreeRecursive', 'enterModal', 'gestureEventHandler',
    'gestureTargetsAtHotSpots', 'grabGesture', 'grabKeyboard', 'grabMouse',
    'init', 'leaveModal', 'leaveScene', 'mousePressEventHandler',
    'removeItemHelper', 'removePopup', 'sendDragDropEvent', 'sendEvent',
    'sendHoverEvent', 'sendMouseEvent', 'sendTouchBeginEvent',
    'setActivePanelHelper', 'setFocusItemHelper', 'touchEventHandler',
    'ungrabGesture', 'ungrabKeyboard', 'ungrabMouse', 'windowForItem', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QGraphicsScenePrivate, each a class in here
  #  as in C++.

  class UpdatedRectsCmp(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QGraphicsScenePrivate::UpdatedRectsCmp: a plain
    Python object standing in front of one C++
    QGraphicsScenePrivate::UpdatedRectsCmp.

    C++ hands a QGraphicsScenePrivate::UpdatedRectsCmp around as a copy, so
    every C++ QGraphicsScenePrivate::UpdatedRectsCmp behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QGraphicsScenePrivate::UpdatedRectsCmp that has a
    ritual and that Python can call so far, 1 name in all: '__call__'. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QGraphicsScenePrivate::UpdatedRectsCmp::~UpdatedRectsCmp()': the
      destructor: Python removes its C++
      QGraphicsScenePrivate::UpdatedRectsCmp by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QGraphicsScenePrivate::UpdatedRectsCmp is created at the first
      use, not by 'QGraphicsScenePrivate::UpdatedRectsCmp(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QGraphicsScenePrivate::UpdatedRectsCmp back gives a
      copy the ritual made for Python, in a new cute
      QGraphicsScenePrivate::UpdatedRectsCmp.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QRectF = WAIT['QRectF']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QGraphicsScenePrivate::UpdatedRectsCmp'

    #  Qt's '~QGraphicsScenePrivate::UpdatedRectsCmp()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QGraphicsScenePrivate::UpdatedRectsCmp behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN21QGraphicsScenePrivate15UpdatedRectsCmpD1Ev')

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

    @overload(QRectF, QRectF)
    def __call__(self, a: QRectF, b: QRectF) -> bool:
      """
      Calls Qt's 'bool
      QGraphicsScenePrivate::UpdatedRectsCmp::operator()(const QRectF &a,
      const QRectF &b) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qgraphicssceneprivate-updatedrectscmp.html

      Parameters
      ----------

      a : QRectF
        Passed on as a value: Qt reads the C++ QRectF, which stays Python's
        own.

      b : QRectF
        Passed on as a value: Qt reads the C++ QRectF, which stays Python's
        own.
      """
      #  bool QGraphicsScenePrivate::UpdatedRectsCmp::operator()(const QRectF
      #      &a, const QRectF &b) const
      return self.uglySide.call(
          'ritual_ZNK21QGraphicsScenePrivate15UpdatedRectsCmpclERK6QRectFS3'
          '_',
          self._valueOf(a), self._valueOf(b),
      )

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
  @overload(QGraphicsScene)
  @overload(NoneType)
  def get(q: Optional[QGraphicsScene]) -> Optional[QGraphicsScenePrivate]:
    """
    Calls Qt's 'QGraphicsScenePrivate
    *QGraphicsScenePrivate::get(QGraphicsScene *q)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicssceneprivate.html#get

    Parameters
    ----------

    q : Optional[QGraphicsScene]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QGraphicsScenePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsScenePrivate *QGraphicsScenePrivate::get(QGraphicsScene *q)
    address = Rituals.call(
        'ritual_ZN21QGraphicsScenePrivate3getEP14QGraphicsScene',
        CuteMixin._addressOf(q),
    )
    return QGraphicsScenePrivate._cuteAt(address)

  @staticmethod
  @overload(QGraphicsItem, QTouchEvent)
  @overload(QGraphicsItem, NoneType)
  @overload(NoneType, QTouchEvent)
  @overload(NoneType, NoneType)
  def updateTouchPointsForItem(
      item: Optional[QGraphicsItem],
      touchEvent: Optional[QTouchEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsScenePrivate::updateTouchPointsForItem(QGraphicsItem *item,
    QTouchEvent *touchEvent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    touchEvent : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsScenePrivate::updateTouchPointsForItem(QGraphicsItem
    #      *item, QTouchEvent *touchEvent)
    Rituals.call(
        'ritual_ZN21QGraphicsScenePrivate24updateTouchPointsForItemEP13QGra'
        'phicsItemP11QTouchEvent',
        CuteMixin._addressOf(item, 'QGraphicsItem'),
        CuteMixin._addressOf(touchEvent),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsScenePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPoint, QPointF, QWidget)
  @overload(QPoint, QPointF, NoneType)
  def itemsAtPosition(
      self,
      screenPos: QPoint,
      scenePos: QPointF,
      widget: Optional[QWidget],
  ) -> QList[QGraphicsItem]:
    """
    Calls Qt's 'QList<QGraphicsItem *>
    QGraphicsScenePrivate::itemsAtPosition(const QPoint &screenPos, const
    QPointF &scenePos, QWidget *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html#itemsAtPosition

    Parameters
    ----------

    screenPos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    scenePos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QList[QGraphicsItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGraphicsItem *> QGraphicsScenePrivate::itemsAtPosition(const
    #      QPoint &screenPos, const QPointF &scenePos, QWidget *widget) const
    address = self.uglySide.call(
        'ritual_ZNK21QGraphicsScenePrivate15itemsAtPositionERK6QPointRK7QPo'
        'intFP7QWidget',
        self._valueOf(screenPos), self._valueOf(scenePos, 'QPointF'),
        self._addressOf(widget),
    )
    from . import QGraphicsItem
    return QList[QGraphicsItem]._cuteOwning(address)

  @overload(QGraphicsItem)
  @overload(NoneType)
  def itemAcceptsHoverEvents_helper(
      self,
      item: Optional[QGraphicsItem],
  ) -> bool:
    """
    Calls Qt's 'bool
    QGraphicsScenePrivate::itemAcceptsHoverEvents_helper(const QGraphicsItem
    *item) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGraphicsScenePrivate::itemAcceptsHoverEvents_helper(const
    #      QGraphicsItem *item) const
    return self.uglySide.call(
        'ritual_ZNK21QGraphicsScenePrivate29itemAcceptsHoverEvents_helperEP'
        'K13QGraphicsItem',
        self._addressOf(item, 'QGraphicsItem'),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGraphicsItem, bool)
  @overload(NoneType, bool)
  def setScenePosItemEnabled(
      self,
      item: Optional[QGraphicsItem],
      enabled: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsScenePrivate::setScenePosItemEnabled(QGraphicsItem *item, bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html#setScenePosItemEnabled

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    enabled : bool
      Passed on as it is.
    """
    #  void QGraphicsScenePrivate::setScenePosItemEnabled(QGraphicsItem
    #      *item, bool enabled)
    self.uglySide.call(
        'ritual_ZN21QGraphicsScenePrivate22setScenePosItemEnabledEP13QGraph'
        'icsItemb',
        self._addressOf(item, 'QGraphicsItem'), enabled,
    )

  @overload(QFont)
  def setFont_helper(self, font: QFont) -> None:
    """
    Calls Qt's 'void QGraphicsScenePrivate::setFont_helper(const QFont
    &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html#setFont_helper

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QGraphicsScenePrivate::setFont_helper(const QFont &font)
    self.uglySide.call(
        'ritual_ZN21QGraphicsScenePrivate14setFont_helperERK5QFont',
        self._valueOf(font),
    )

  @overload(QPalette)
  def setPalette_helper(self, palette: QPalette) -> None:
    """
    Calls Qt's 'void QGraphicsScenePrivate::setPalette_helper(const QPalette
    &palette)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html#setPalette_helper

    Parameters
    ----------

    palette : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.
    """
    #  void QGraphicsScenePrivate::setPalette_helper(const QPalette &palette)
    self.uglySide.call(
        'ritual_ZN21QGraphicsScenePrivate17setPalette_helperERK8QPalette',
        self._valueOf(palette),
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
    'QGraphicsScenePrivate::QGraphicsScenePrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html#QGraphicsScenePrivate
    """
    #  QGraphicsScenePrivate::QGraphicsScenePrivate()
    self._noteCreation(QGraphicsScenePrivate, lambda: Rituals.call(
        'ritual_ZN21QGraphicsScenePrivateC1Ev',
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

  def q_func(self) -> Optional[QGraphicsScene]:
    """
    Calls Qt's 'QGraphicsScene *QGraphicsScenePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicssceneprivate.html#q_func

    Returns
    -------

    Optional[QGraphicsScene]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsScene *QGraphicsScenePrivate::q_func()
    address = self.uglySide.call('ritual_ZN21QGraphicsScenePrivate6q_funcEv')
    from . import QGraphicsScene
    return QGraphicsScene._cuteAt(address)

  def _q_emitUpdated(self) -> None:
    """
    Calls Qt's 'void QGraphicsScenePrivate::_q_emitUpdated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html#_q_emitUpdated
    """
    #  void QGraphicsScenePrivate::_q_emitUpdated()
    self.uglySide.call('ritual_ZN21QGraphicsScenePrivate14_q_emitUpdatedEv')

  @overload(QGraphicsItem)
  @overload(NoneType)
  def registerTopLevelItem(self, item: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void
    QGraphicsScenePrivate::registerTopLevelItem(QGraphicsItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html#registerTopLevelItem

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsScenePrivate::registerTopLevelItem(QGraphicsItem *item)
    self.uglySide.call(
        'ritual_ZN21QGraphicsScenePrivate20registerTopLevelItemEP13QGraphic'
        'sItem',
        self._addressOf(item, 'QGraphicsItem'),
    )

  @overload(QGraphicsItem)
  @overload(NoneType)
  def unregisterTopLevelItem(self, item: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void
    QGraphicsScenePrivate::unregisterTopLevelItem(QGraphicsItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html#unregisterTopLevelItem

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsScenePrivate::unregisterTopLevelItem(QGraphicsItem
    #      *item)
    self.uglySide.call(
        'ritual_ZN21QGraphicsScenePrivate22unregisterTopLevelItemEP13QGraph'
        'icsItem',
        self._addressOf(item, 'QGraphicsItem'),
    )

  def _q_polishItems(self) -> None:
    """
    Calls Qt's 'void QGraphicsScenePrivate::_q_polishItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html#_q_polishItems
    """
    #  void QGraphicsScenePrivate::_q_polishItems()
    self.uglySide.call('ritual_ZN21QGraphicsScenePrivate14_q_polishItemsEv')

  def _q_processDirtyItems(self) -> None:
    """
    Calls Qt's 'void QGraphicsScenePrivate::_q_processDirtyItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html#_q_processDirtyItems
    """
    #  void QGraphicsScenePrivate::_q_processDirtyItems()
    self.uglySide.call(
        'ritual_ZN21QGraphicsScenePrivate20_q_processDirtyItemsEv',
    )

  @overload(QGraphicsItem)
  @overload(NoneType)
  def registerScenePosItem(self, item: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void
    QGraphicsScenePrivate::registerScenePosItem(QGraphicsItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html#registerScenePosItem

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsScenePrivate::registerScenePosItem(QGraphicsItem *item)
    self.uglySide.call(
        'ritual_ZN21QGraphicsScenePrivate20registerScenePosItemEP13QGraphic'
        'sItem',
        self._addressOf(item, 'QGraphicsItem'),
    )

  @overload(QGraphicsItem)
  @overload(NoneType)
  def unregisterScenePosItem(self, item: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void
    QGraphicsScenePrivate::unregisterScenePosItem(QGraphicsItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html#unregisterScenePosItem

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsScenePrivate::unregisterScenePosItem(QGraphicsItem
    #      *item)
    self.uglySide.call(
        'ritual_ZN21QGraphicsScenePrivate22unregisterScenePosItemEP13QGraph'
        'icsItem',
        self._addressOf(item, 'QGraphicsItem'),
    )

  def _q_updateScenePosDescendants(self) -> None:
    """
    Calls Qt's 'void QGraphicsScenePrivate::_q_updateScenePosDescendants()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html
    """
    #  void QGraphicsScenePrivate::_q_updateScenePosDescendants()
    self.uglySide.call(
        'ritual_ZN21QGraphicsScenePrivate28_q_updateScenePosDescendantsEv',
    )

  def clearMouseGrabber(self) -> None:
    """
    Calls Qt's 'void QGraphicsScenePrivate::clearMouseGrabber()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html#clearMouseGrabber
    """
    #  void QGraphicsScenePrivate::clearMouseGrabber()
    self.uglySide.call(
        'ritual_ZN21QGraphicsScenePrivate17clearMouseGrabberEv',
    )

  def enableMouseTrackingOnViews(self) -> None:
    """
    Calls Qt's 'void QGraphicsScenePrivate::enableMouseTrackingOnViews()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html
    """
    #  void QGraphicsScenePrivate::enableMouseTrackingOnViews()
    self.uglySide.call(
        'ritual_ZN21QGraphicsScenePrivate26enableMouseTrackingOnViewsEv',
    )

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def storeMouseButtonsForMouseGrabber(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void QGraphicsScenePrivate::storeMouseButtonsForMouseGrabber(
    QGraphicsSceneMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsScenePrivate::storeMouseButtonsForMouseGrabber(
    #      QGraphicsSceneMouseEvent *event)
    self.uglySide.call(
        'ritual_ZN21QGraphicsScenePrivate32storeMouseButtonsForMouseGrabber'
        'EP24QGraphicsSceneMouseEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsView)
  @overload(NoneType)
  def addView(self, view: Optional[QGraphicsView]) -> None:
    """
    Calls Qt's 'void QGraphicsScenePrivate::addView(QGraphicsView *view)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicssceneprivate.html#addView

    Parameters
    ----------

    view : Optional[QGraphicsView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsScenePrivate::addView(QGraphicsView *view)
    self.uglySide.call(
        'ritual_ZN21QGraphicsScenePrivate7addViewEP13QGraphicsView',
        self._addressOf(view),
    )

  @overload(QGraphicsView)
  @overload(NoneType)
  def removeView(self, view: Optional[QGraphicsView]) -> None:
    """
    Calls Qt's 'void QGraphicsScenePrivate::removeView(QGraphicsView *view)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html#removeView

    Parameters
    ----------

    view : Optional[QGraphicsView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsScenePrivate::removeView(QGraphicsView *view)
    self.uglySide.call(
        'ritual_ZN21QGraphicsScenePrivate10removeViewEP13QGraphicsView',
        self._addressOf(view),
    )

  @overload(QGraphicsItem, QGraphicsItem)
  @overload(QGraphicsItem, NoneType)
  @overload(NoneType, QGraphicsItem)
  @overload(NoneType, NoneType)
  def installSceneEventFilter(
      self,
      watched: Optional[QGraphicsItem],
      filter: Optional[QGraphicsItem],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsScenePrivate::installSceneEventFilter(QGraphicsItem *watched,
    QGraphicsItem *filter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html#installSceneEventFilter

    Parameters
    ----------

    watched : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    filter : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsScenePrivate::installSceneEventFilter(QGraphicsItem
    #      *watched, QGraphicsItem *filter)
    self.uglySide.call(
        'ritual_ZN21QGraphicsScenePrivate23installSceneEventFilterEP13QGrap'
        'hicsItemS1_',
        self._addressOf(watched, 'QGraphicsItem'), self._addressOf(filter,
        'QGraphicsItem'),
    )

  @overload(QGraphicsItem, QGraphicsItem)
  @overload(QGraphicsItem, NoneType)
  @overload(NoneType, QGraphicsItem)
  @overload(NoneType, NoneType)
  def removeSceneEventFilter(
      self,
      watched: Optional[QGraphicsItem],
      filter: Optional[QGraphicsItem],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsScenePrivate::removeSceneEventFilter(QGraphicsItem *watched,
    QGraphicsItem *filter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html#removeSceneEventFilter

    Parameters
    ----------

    watched : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    filter : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsScenePrivate::removeSceneEventFilter(QGraphicsItem
    #      *watched, QGraphicsItem *filter)
    self.uglySide.call(
        'ritual_ZN21QGraphicsScenePrivate22removeSceneEventFilterEP13QGraph'
        'icsItemS1_',
        self._addressOf(watched, 'QGraphicsItem'), self._addressOf(filter,
        'QGraphicsItem'),
    )

  @overload(QGraphicsItem, QEvent)
  @overload(QGraphicsItem, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def filterDescendantEvent(
      self,
      item: Optional[QGraphicsItem],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool
    QGraphicsScenePrivate::filterDescendantEvent(QGraphicsItem *item, QEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html#filterDescendantEvent

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGraphicsScenePrivate::filterDescendantEvent(QGraphicsItem *item,
    #      QEvent *event)
    return self.uglySide.call(
        'ritual_ZN21QGraphicsScenePrivate21filterDescendantEventEP13QGraphi'
        'csItemP6QEvent',
        self._addressOf(item, 'QGraphicsItem'), self._addressOf(event),
    )

  @overload(QGraphicsItem, QEvent)
  @overload(QGraphicsItem, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def filterEvent(
      self,
      item: Optional[QGraphicsItem],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QGraphicsScenePrivate::filterEvent(QGraphicsItem *item,
    QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html#filterEvent

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGraphicsScenePrivate::filterEvent(QGraphicsItem *item, QEvent
    #      *event)
    return self.uglySide.call(
        'ritual_ZN21QGraphicsScenePrivate11filterEventEP13QGraphicsItemP6QE'
        'vent',
        self._addressOf(item, 'QGraphicsItem'), self._addressOf(event),
    )

  @overload(QGraphicsSceneDragDropEvent, QGraphicsSceneDragDropEvent)
  @overload(QGraphicsSceneDragDropEvent, NoneType)
  @overload(NoneType, QGraphicsSceneDragDropEvent)
  @overload(NoneType, NoneType)
  def cloneDragDropEvent(
      self,
      dest: Optional[QGraphicsSceneDragDropEvent],
      source: Optional[QGraphicsSceneDragDropEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsScenePrivate::cloneDragDropEvent(QGraphicsSceneDragDropEvent
    *dest, QGraphicsSceneDragDropEvent *source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html#cloneDragDropEvent

    Parameters
    ----------

    dest : Optional[QGraphicsSceneDragDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    source : Optional[QGraphicsSceneDragDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsScenePrivate::cloneDragDropEvent(
    #      QGraphicsSceneDragDropEvent *dest, QGraphicsSceneDragDropEvent
    #      *source)
    self.uglySide.call(
        'ritual_ZN21QGraphicsScenePrivate18cloneDragDropEventEP27QGraphicsS'
        'ceneDragDropEventS1_',
        self._addressOf(dest), self._addressOf(source),
    )

  @overload(QGraphicsItem)
  @overload(NoneType)
  @overload(QGraphicsItem, QRectF)
  @overload(NoneType, QRectF)
  @overload(QGraphicsItem, QRectF, bool)
  @overload(NoneType, QRectF, bool)
  @overload(QGraphicsItem, QRectF, bool, bool)
  @overload(NoneType, QRectF, bool, bool)
  @overload(QGraphicsItem, QRectF, bool, bool, bool)
  @overload(NoneType, QRectF, bool, bool, bool)
  @overload(QGraphicsItem, QRectF, bool, bool, bool, bool)
  @overload(NoneType, QRectF, bool, bool, bool, bool)
  @overload(QGraphicsItem, QRectF, bool, bool, bool, bool, bool)
  @overload(NoneType, QRectF, bool, bool, bool, bool, bool)
  def markDirty(
      self,
      item: Optional[QGraphicsItem],
      rect: Optional[QRectF] = None,
      invalidateChildren: bool = False,
      force: bool = False,
      ignoreOpacity: bool = False,
      removingItemFromScene: bool = False,
      updateBoundingRect: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsScenePrivate::markDirty(QGraphicsItem *item,
    const QRectF &rect, bool invalidateChildren, bool force, bool
    ignoreOpacity, bool removingItemFromScene, bool updateBoundingRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html#markDirty

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.

    invalidateChildren : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    force : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    ignoreOpacity : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    removingItemFromScene : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    updateBoundingRect : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QGraphicsScenePrivate::markDirty(QGraphicsItem *item, const
    #      QRectF &rect, bool invalidateChildren, bool force, bool
    #      ignoreOpacity, bool removingItemFromScene, bool
    #      updateBoundingRect)
    if rect is None:
      from ..QtCore import QRectF
      rect = QRectF()
    self.uglySide.call(
        'ritual_ZN21QGraphicsScenePrivate9markDirtyEP13QGraphicsItemRK6QRec'
        'tFbbbbb',
        self._addressOf(item, 'QGraphicsItem'), self._valueOf(rect),
        invalidateChildren, force, ignoreOpacity, removingItemFromScene,
        updateBoundingRect,
    )

  @overload(QGraphicsItem)
  @overload(NoneType)
  @overload(QGraphicsItem, bool)
  @overload(NoneType, bool)
  @overload(QGraphicsItem, bool, float)
  @overload(NoneType, bool, float)
  def processDirtyItemsRecursive(
      self,
      item: Optional[QGraphicsItem],
      dirtyAncestorContainsChildren: bool = False,
      parentOpacity: float = 1.0,
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsScenePrivate::processDirtyItemsRecursive(QGraphicsItem *item,
    bool dirtyAncestorContainsChildren, qreal parentOpacity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dirtyAncestorContainsChildren : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    parentOpacity : float
      Passed on as it is. May be left out, as in Qt: it is then 1.0.
    """
    #  void QGraphicsScenePrivate::processDirtyItemsRecursive(QGraphicsItem
    #      *item, bool dirtyAncestorContainsChildren, qreal parentOpacity)
    self.uglySide.call(
        'ritual_ZN21QGraphicsScenePrivate26processDirtyItemsRecursiveEP13QG'
        'raphicsItembd',
        self._addressOf(item, 'QGraphicsItem'),
        dirtyAncestorContainsChildren, parentOpacity,
    )

  @overload(QGraphicsItem)
  @overload(NoneType)
  @overload(QGraphicsItem, bool)
  @overload(NoneType, bool)
  def resetDirtyItem(
      self,
      item: Optional[QGraphicsItem],
      recursive: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsScenePrivate::resetDirtyItem(QGraphicsItem
    *item, bool recursive)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html#resetDirtyItem

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    recursive : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QGraphicsScenePrivate::resetDirtyItem(QGraphicsItem *item, bool
    #      recursive)
    self.uglySide.call(
        'ritual_ZN21QGraphicsScenePrivate14resetDirtyItemEP13QGraphicsItemb',
        self._addressOf(item, 'QGraphicsItem'), recursive,
    )

  def ensureSortedTopLevelItems(self) -> None:
    """
    Calls Qt's 'void QGraphicsScenePrivate::ensureSortedTopLevelItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html
    """
    #  void QGraphicsScenePrivate::ensureSortedTopLevelItems()
    self.uglySide.call(
        'ritual_ZN21QGraphicsScenePrivate25ensureSortedTopLevelItemsEv',
    )

  def ensureSequentialTopLevelSiblingIndexes(self) -> None:
    """
    Calls Qt's 'void
    QGraphicsScenePrivate::ensureSequentialTopLevelSiblingIndexes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html
    """
    #  void QGraphicsScenePrivate::ensureSequentialTopLevelSiblingIndexes()
    self.uglySide.call(
        'ritual_ZN21QGraphicsScenePrivate38ensureSequentialTopLevelSiblingI'
        'ndexesEv',
    )

  def resolveFont(self) -> None:
    """
    Calls Qt's 'void QGraphicsScenePrivate::resolveFont()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html#resolveFont
    """
    #  void QGraphicsScenePrivate::resolveFont()
    self.uglySide.call('ritual_ZN21QGraphicsScenePrivate11resolveFontEv')

  @overload(QFont)
  def updateFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QGraphicsScenePrivate::updateFont(const QFont &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html#updateFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QGraphicsScenePrivate::updateFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN21QGraphicsScenePrivate10updateFontERK5QFont',
        self._valueOf(font),
    )

  def resolvePalette(self) -> None:
    """
    Calls Qt's 'void QGraphicsScenePrivate::resolvePalette()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html#resolvePalette
    """
    #  void QGraphicsScenePrivate::resolvePalette()
    self.uglySide.call('ritual_ZN21QGraphicsScenePrivate14resolvePaletteEv')

  @overload(QPalette)
  def updatePalette(self, palette: QPalette) -> None:
    """
    Calls Qt's 'void QGraphicsScenePrivate::updatePalette(const QPalette
    &palette)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html#updatePalette

    Parameters
    ----------

    palette : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.
    """
    #  void QGraphicsScenePrivate::updatePalette(const QPalette &palette)
    self.uglySide.call(
        'ritual_ZN21QGraphicsScenePrivate13updatePaletteERK8QPalette',
        self._valueOf(palette),
    )

  @overload(QPointF)
  def findClosestTouchPointId(self, scenePos: QPointF) -> int:
    """
    Calls Qt's 'int QGraphicsScenePrivate::findClosestTouchPointId(const
    QPointF &scenePos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html#findClosestTouchPointId

    Parameters
    ----------

    scenePos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  int QGraphicsScenePrivate::findClosestTouchPointId(const QPointF
    #      &scenePos)
    return self.uglySide.call(
        'ritual_ZN21QGraphicsScenePrivate23findClosestTouchPointIdERK7QPoin'
        'tF',
        self._valueOf(scenePos, 'QPointF'),
    )

  def enableTouchEventsOnViews(self) -> None:
    """
    Calls Qt's 'void QGraphicsScenePrivate::enableTouchEventsOnViews()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html
    """
    #  void QGraphicsScenePrivate::enableTouchEventsOnViews()
    self.uglySide.call(
        'ritual_ZN21QGraphicsScenePrivate24enableTouchEventsOnViewsEv',
    )

  def updateInputMethodSensitivityInViews(self) -> None:
    """
    Calls Qt's 'void
    QGraphicsScenePrivate::updateInputMethodSensitivityInViews()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneprivate.html
    """
    #  void QGraphicsScenePrivate::updateInputMethodSensitivityInViews()
    self.uglySide.call(
        'ritual_ZN21QGraphicsScenePrivate35updateInputMethodSensitivityInVi'
        'ewsEv',
    )

  @staticmethod
  def _q_updateLater(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsScenePrivate::_q_updateLater()': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate._q_updateLater' has no cute function yet. "
        "Qt's 'void QGraphicsScenePrivate::_q_updateLater()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def addPopup(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsScenePrivate::addPopup(QGraphicsWidget *widget)':
    leans on 'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, QEvent*)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate.addPopup' has no cute function yet. Qt's "
        "'void QGraphicsScenePrivate::addPopup(QGraphicsWidget *widget)': "
        "leans on 'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, "
        "QEvent*)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def cancelGesturesForChildren(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsScenePrivate::cancelGesturesForChildren(QGesture
    *original)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'DEBUG'.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate.cancelGesturesForChildren' has no cute "
        "function yet. Qt's 'void "
        "QGraphicsScenePrivate::cancelGesturesForChildren(QGesture "
        "*original)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'DEBUG'.")

  @staticmethod
  def clearKeyboardGrabber(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsScenePrivate::clearKeyboardGrabber()': leans on
    'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, QEvent*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate.clearKeyboardGrabber' has no cute function "
        "yet. Qt's 'void QGraphicsScenePrivate::clearKeyboardGrabber()': "
        "leans on 'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, "
        "QEvent*)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def dispatchHoverEvent(*__, **_) -> Never:
    """
    Qt's 'bool
    QGraphicsScenePrivate::dispatchHoverEvent(QGraphicsSceneHoverEvent
    *hoverEvent)': leans on 'QGraphicsScenePrivate::sendEvent(QGraphicsItem*,
    QEvent*)', which Qt's source does not mark for use from outside Qt and
    has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate.dispatchHoverEvent' has no cute function "
        "yet. Qt's 'bool "
        "QGraphicsScenePrivate::dispatchHoverEvent(QGraphicsSceneHoverEvent "
        "*hoverEvent)': leans on "
        "'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, QEvent*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def draw(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsScenePrivate::draw(QGraphicsItem *a0, QPainter *a1,
    const QTransform *const a2, const QTransform *const a3, QRegion *a4,
    QWidget *a5, qreal a6, const QTransform *const a7, bool a8, bool a9)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'setWorldTransform'.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate.draw' has no cute function yet. Qt's 'void "
        "QGraphicsScenePrivate::draw(QGraphicsItem *a0, QPainter *a1, const "
        "QTransform *const a2, const QTransform *const a3, QRegion *a4, "
        "QWidget *a5, qreal a6, const QTransform *const a7, bool a8, bool "
        "a9)': Qt's library has no name for it, and its code in Qt's source "
        "does not compile apart from its file: use of undeclared identifier "
        "'setWorldTransform'.")

  @staticmethod
  def drawItemHelper(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsScenePrivate::drawItemHelper(QGraphicsItem *item,
    QPainter *painter, const QStyleOptionGraphicsItem *option, QWidget
    *widget, bool painterStateProtection)': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier '_q_paintItem'.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate.drawItemHelper' has no cute function yet. "
        "Qt's 'void QGraphicsScenePrivate::drawItemHelper(QGraphicsItem "
        "*item, QPainter *painter, const QStyleOptionGraphicsItem *option, "
        "QWidget *widget, bool painterStateProtection)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier '_q_paintItem'.")

  @staticmethod
  def drawItems(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsScenePrivate::drawItems(QPainter *painter, const
    QTransform *const viewTransform, QRegion *exposedRegion, QWidget
    *widget)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate.drawItems' has no cute function yet. Qt's "
        "'void QGraphicsScenePrivate::drawItems(QPainter *painter, const "
        "QTransform *const viewTransform, QRegion *exposedRegion, QWidget "
        "*widget)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def drawSubtreeRecursive(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsScenePrivate::drawSubtreeRecursive(QGraphicsItem
    *item, QPainter *painter, const QTransform *const a2, QRegion
    *exposedRegion, QWidget *widget, qreal parentOpacity, const QTransform
    *const effectTransform)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate.drawSubtreeRecursive' has no cute function "
        "yet. Qt's 'void "
        "QGraphicsScenePrivate::drawSubtreeRecursive(QGraphicsItem *item, "
        "QPainter *painter, const QTransform *const a2, QRegion "
        "*exposedRegion, QWidget *widget, qreal parentOpacity, const "
        "QTransform *const effectTransform)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def enterModal(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsScenePrivate::enterModal(QGraphicsItem *item,
    QGraphicsItem::PanelModality panelModality)': leans on
    'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, QEvent*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate.enterModal' has no cute function yet. Qt's "
        "'void QGraphicsScenePrivate::enterModal(QGraphicsItem *item, "
        "QGraphicsItem::PanelModality panelModality)': leans on "
        "'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, QEvent*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def gestureEventHandler(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsScenePrivate::gestureEventHandler(QGestureEvent
    *event)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'DEBUG'.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate.gestureEventHandler' has no cute function "
        "yet. Qt's 'void "
        "QGraphicsScenePrivate::gestureEventHandler(QGestureEvent *event)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'DEBUG'.")

  @staticmethod
  def gestureTargetsAtHotSpots(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsScenePrivate::gestureTargetsAtHotSpots(const
    QSet<QGesture *> &gestures, Qt::GestureFlag flag, QHash<QGraphicsObject
    *, QSet<QGesture *>> *targets, QSet<QGraphicsObject *> *itemsSet,
    QSet<QGesture *> *normal, QSet<QGesture *> *conflicts)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate.gestureTargetsAtHotSpots' has no cute "
        "function yet. Qt's 'void "
        "QGraphicsScenePrivate::gestureTargetsAtHotSpots(const "
        "QSet<QGesture *> &gestures, Qt::GestureFlag flag, "
        "QHash<QGraphicsObject *, QSet<QGesture *>> *targets, "
        "QSet<QGraphicsObject *> *itemsSet, QSet<QGesture *> *normal, "
        "QSet<QGesture *> *conflicts)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def grabGesture(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsScenePrivate::grabGesture(QGraphicsItem *a0,
    Qt::GestureType gesture)': leans on
    'QGestureManager::QGestureManager(QObject*)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate.grabGesture' has no cute function yet. Qt's "
        "'void QGraphicsScenePrivate::grabGesture(QGraphicsItem *a0, "
        "Qt::GestureType gesture)': leans on "
        "'QGestureManager::QGestureManager(QObject*)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def grabKeyboard(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsScenePrivate::grabKeyboard(QGraphicsItem *item)':
    leans on 'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, QEvent*)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate.grabKeyboard' has no cute function yet. "
        "Qt's 'void QGraphicsScenePrivate::grabKeyboard(QGraphicsItem "
        "*item)': leans on "
        "'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, QEvent*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def grabMouse(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsScenePrivate::grabMouse(QGraphicsItem *item, bool
    implicit)': leans on 'QGraphicsScenePrivate::sendEvent(QGraphicsItem*,
    QEvent*)', which Qt's source does not mark for use from outside Qt and
    has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate.grabMouse' has no cute function yet. Qt's "
        "'void QGraphicsScenePrivate::grabMouse(QGraphicsItem *item, bool "
        "implicit)': leans on "
        "'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, QEvent*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def init(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsScenePrivate::init()': leans on 'vtable for
    QGraphicsSceneBspTreeIndex', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate.init' has no cute function yet. Qt's 'void "
        "QGraphicsScenePrivate::init()': leans on 'vtable for "
        "QGraphicsSceneBspTreeIndex', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def leaveModal(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsScenePrivate::leaveModal(QGraphicsItem *item)': leans
    on 'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, QEvent*)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate.leaveModal' has no cute function yet. Qt's "
        "'void QGraphicsScenePrivate::leaveModal(QGraphicsItem *item)': "
        "leans on 'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, "
        "QEvent*)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def leaveScene(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsScenePrivate::leaveScene(QWidget *viewport)': leans
    on 'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, QEvent*)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate.leaveScene' has no cute function yet. Qt's "
        "'void QGraphicsScenePrivate::leaveScene(QWidget *viewport)': leans "
        "on 'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, QEvent*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def mousePressEventHandler(*__, **_) -> Never:
    """
    Qt's 'void
    QGraphicsScenePrivate::mousePressEventHandler(QGraphicsSceneMouseEvent
    *mouseEvent)': leans on 'QGraphicsScenePrivate::sendEvent(QGraphicsItem*,
    QEvent*)', which Qt's source does not mark for use from outside Qt and
    has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate.mousePressEventHandler' has no cute "
        "function yet. Qt's 'void "
        "QGraphicsScenePrivate::mousePressEventHandler(QGraphicsSceneMouseEv"
        "ent *mouseEvent)': leans on "
        "'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, QEvent*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def removeItemHelper(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsScenePrivate::removeItemHelper(QGraphicsItem *item)':
    leans on 'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, QEvent*)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate.removeItemHelper' has no cute function yet. "
        "Qt's 'void QGraphicsScenePrivate::removeItemHelper(QGraphicsItem "
        "*item)': leans on "
        "'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, QEvent*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def removePopup(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsScenePrivate::removePopup(QGraphicsWidget *widget,
    bool itemIsDying)': leans on
    'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, QEvent*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate.removePopup' has no cute function yet. Qt's "
        "'void QGraphicsScenePrivate::removePopup(QGraphicsWidget *widget, "
        "bool itemIsDying)': leans on "
        "'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, QEvent*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def sendDragDropEvent(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsScenePrivate::sendDragDropEvent(QGraphicsItem *item,
    QGraphicsSceneDragDropEvent *dragDropEvent)': leans on
    'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, QEvent*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate.sendDragDropEvent' has no cute function "
        "yet. Qt's 'void "
        "QGraphicsScenePrivate::sendDragDropEvent(QGraphicsItem *item, "
        "QGraphicsSceneDragDropEvent *dragDropEvent)': leans on "
        "'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, QEvent*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def sendEvent(*__, **_) -> Never:
    """
    Qt's 'bool QGraphicsScenePrivate::sendEvent(QGraphicsItem *item, QEvent
    *event)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'qt_sendSpontaneousEvent'.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate.sendEvent' has no cute function yet. Qt's "
        "'bool QGraphicsScenePrivate::sendEvent(QGraphicsItem *item, QEvent "
        "*event)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'qt_sendSpontaneousEvent'.")

  @staticmethod
  def sendHoverEvent(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsScenePrivate::sendHoverEvent(QEvent::Type type,
    QGraphicsItem *item, QGraphicsSceneHoverEvent *hoverEvent)': leans on
    'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, QEvent*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate.sendHoverEvent' has no cute function yet. "
        "Qt's 'void QGraphicsScenePrivate::sendHoverEvent(QEvent::Type "
        "type, QGraphicsItem *item, QGraphicsSceneHoverEvent *hoverEvent)': "
        "leans on 'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, "
        "QEvent*)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def sendMouseEvent(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsScenePrivate::sendMouseEvent(QGraphicsSceneMouseEvent
    *mouseEvent)': leans on 'QGraphicsScenePrivate::sendEvent(QGraphicsItem*,
    QEvent*)', which Qt's source does not mark for use from outside Qt and
    has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate.sendMouseEvent' has no cute function yet. "
        "Qt's 'void "
        "QGraphicsScenePrivate::sendMouseEvent(QGraphicsSceneMouseEvent "
        "*mouseEvent)': leans on "
        "'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, QEvent*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def sendTouchBeginEvent(*__, **_) -> Never:
    """
    Qt's 'bool QGraphicsScenePrivate::sendTouchBeginEvent(QGraphicsItem
    *item, QTouchEvent *touchEvent)': leans on
    'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, QEvent*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate.sendTouchBeginEvent' has no cute function "
        "yet. Qt's 'bool "
        "QGraphicsScenePrivate::sendTouchBeginEvent(QGraphicsItem *item, "
        "QTouchEvent *touchEvent)': leans on "
        "'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, QEvent*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setActivePanelHelper(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsScenePrivate::setActivePanelHelper(QGraphicsItem
    *item, bool duringActivationEvent)': leans on
    'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, QEvent*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate.setActivePanelHelper' has no cute function "
        "yet. Qt's 'void "
        "QGraphicsScenePrivate::setActivePanelHelper(QGraphicsItem *item, "
        "bool duringActivationEvent)': leans on "
        "'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, QEvent*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setFocusItemHelper(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsScenePrivate::setFocusItemHelper(QGraphicsItem *item,
    Qt::FocusReason focusReason, bool emitFocusChanged)': leans on
    'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, QEvent*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate.setFocusItemHelper' has no cute function "
        "yet. Qt's 'void "
        "QGraphicsScenePrivate::setFocusItemHelper(QGraphicsItem *item, "
        "Qt::FocusReason focusReason, bool emitFocusChanged)': leans on "
        "'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, QEvent*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def touchEventHandler(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsScenePrivate::touchEventHandler(QTouchEvent
    *touchEvent)': leans on 'QGraphicsScenePrivate::sendEvent(QGraphicsItem*,
    QEvent*)', which Qt's source does not mark for use from outside Qt and
    has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate.touchEventHandler' has no cute function "
        "yet. Qt's 'void "
        "QGraphicsScenePrivate::touchEventHandler(QTouchEvent "
        "*touchEvent)': leans on "
        "'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, QEvent*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def ungrabGesture(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsScenePrivate::ungrabGesture(QGraphicsItem *a0,
    Qt::GestureType gesture)': leans on
    'QGestureManager::QGestureManager(QObject*)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate.ungrabGesture' has no cute function yet. "
        "Qt's 'void QGraphicsScenePrivate::ungrabGesture(QGraphicsItem *a0, "
        "Qt::GestureType gesture)': leans on "
        "'QGestureManager::QGestureManager(QObject*)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def ungrabKeyboard(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsScenePrivate::ungrabKeyboard(QGraphicsItem *item,
    bool itemIsDying)': leans on
    'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, QEvent*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate.ungrabKeyboard' has no cute function yet. "
        "Qt's 'void QGraphicsScenePrivate::ungrabKeyboard(QGraphicsItem "
        "*item, bool itemIsDying)': leans on "
        "'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, QEvent*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def ungrabMouse(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsScenePrivate::ungrabMouse(QGraphicsItem *item, bool
    itemIsDying)': leans on 'QGraphicsScenePrivate::sendEvent(QGraphicsItem*,
    QEvent*)', which Qt's source does not mark for use from outside Qt and
    has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate.ungrabMouse' has no cute function yet. Qt's "
        "'void QGraphicsScenePrivate::ungrabMouse(QGraphicsItem *item, bool "
        "itemIsDying)': leans on "
        "'QGraphicsScenePrivate::sendEvent(QGraphicsItem*, QEvent*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def windowForItem(*__, **_) -> Never:
    """
    Qt's 'QGraphicsWidget *QGraphicsScenePrivate::windowForItem(const
    QGraphicsItem *item) const': cannot be called and cannot be called
    through the meta-object and cannot be copied: no header file has its
    code, Qt's source does not mark it or its class for use from outside Qt
    or writes it 'inline' or nowhere, and it is no signal, slot or invokable
    function giving back nothing, of a class built on QObject, and Qt's
    source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QGraphicsScenePrivate.windowForItem' has no cute function yet. "
        "Qt's 'QGraphicsWidget *QGraphicsScenePrivate::windowForItem(const "
        "QGraphicsItem *item) const': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")
