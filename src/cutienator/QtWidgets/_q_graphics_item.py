"""
QGraphicsItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgraphicsitem.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QPointF, QRectF, QSize, QVariant
  from ..QtGui import QCursor, QFocusEvent, QInputMethodEvent, QKeyEvent
  from ..QtGui import QPainter, QPainterPath, QPolygonF, QRegion, QTransform
  from . import QGraphicsEffect, QGraphicsItemGroup, QGraphicsObject
  from . import QGraphicsScene, QGraphicsSceneContextMenuEvent
  from . import QGraphicsSceneDragDropEvent, QGraphicsSceneHoverEvent
  from . import QGraphicsSceneMouseEvent, QGraphicsSceneWheelEvent
  from . import QGraphicsWidget, QStyleOptionGraphicsItem, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCursor = WAIT['QCursor']
  QEvent = WAIT['QEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QGraphicsEffect = WAIT['QGraphicsEffect']
  QGraphicsItemGroup = WAIT['QGraphicsItemGroup']
  QGraphicsSceneContextMenuEvent = WAIT['QGraphicsSceneContextMenuEvent']
  QGraphicsSceneDragDropEvent = WAIT['QGraphicsSceneDragDropEvent']
  QGraphicsSceneHoverEvent = WAIT['QGraphicsSceneHoverEvent']
  QGraphicsSceneMouseEvent = WAIT['QGraphicsSceneMouseEvent']
  QGraphicsSceneWheelEvent = WAIT['QGraphicsSceneWheelEvent']
  QInputMethodEvent = WAIT['QInputMethodEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QPainter = WAIT['QPainter']
  QPainterPath = WAIT['QPainterPath']
  QPointF = WAIT['QPointF']
  QPolygonF = WAIT['QPolygonF']
  QRectF = WAIT['QRectF']
  QSize = WAIT['QSize']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
  QTransform = WAIT['QTransform']
  QVariant = WAIT['QVariant']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGraphicsItem: a plain Python object standing in
  front of one C++ QGraphicsItem.

  What exists
  -----------

  Every function of Qt's QGraphicsItem that has a ritual and that Python can
  call so far, 154 names in all: 'scene', 'parentItem', 'topLevelItem',
  'parentObject', 'parentWidget', 'topLevelWidget', 'window', 'panel',
  'setParentItem', 'isWidget', 'isWindow', 'isPanel', 'toGraphicsObject',
  'group', 'setGroup', 'flags', 'setFlag', 'setFlags', 'cacheMode',
  'setCacheMode', 'panelModality', 'setPanelModality', 'toolTip',
  'setToolTip', 'cursor', 'setCursor', 'hasCursor', 'unsetCursor',
  'isVisible', 'isVisibleTo', 'setVisible', 'hide', 'show', 'isEnabled',
  'setEnabled', 'isSelected', 'setSelected', 'acceptDrops', 'setAcceptDrops',
  'opacity', 'effectiveOpacity', 'setOpacity', 'graphicsEffect',
  'setGraphicsEffect', 'acceptedMouseButtons', 'setAcceptedMouseButtons',
  'acceptHoverEvents', 'setAcceptHoverEvents', 'acceptTouchEvents',
  'setAcceptTouchEvents', 'filtersChildEvents', 'setFiltersChildEvents',
  'handlesChildEvents', 'setHandlesChildEvents', 'isActive', 'setActive',
  'hasFocus', 'setFocus', 'clearFocus', 'focusProxy', 'setFocusProxy',
  'focusItem', 'focusScopeItem', 'grabMouse', 'ungrabMouse', 'grabKeyboard',
  'ungrabKeyboard', 'pos', 'x', 'setX', 'y', 'setY', 'scenePos', 'setPos',
  'moveBy', 'ensureVisible', 'transform', 'sceneTransform',
  'deviceTransform', 'setTransform', 'resetTransform', 'setRotation',
  'rotation', 'setScale', 'scale', 'transformOriginPoint',
  'setTransformOriginPoint', 'advance', 'zValue', 'setZValue', 'stackBefore',
  'boundingRect', 'childrenBoundingRect', 'sceneBoundingRect', 'shape',
  'isClipped', 'clipPath', 'contains', 'collidesWithItem',
  'collidesWithPath', 'isObscured', 'isObscuredBy', 'opaqueArea',
  'boundingRegion', 'boundingRegionGranularity',
  'setBoundingRegionGranularity', 'paint', 'update', 'scroll', 'mapToItem',
  'mapToParent', 'mapToScene', 'mapRectToItem', 'mapRectToParent',
  'mapRectToScene', 'mapFromItem', 'mapFromParent', 'mapFromScene',
  'mapRectFromItem', 'mapRectFromParent', 'mapRectFromScene', 'isAncestorOf',
  'commonAncestorItem', 'isUnderMouse', 'data', 'setData',
  'inputMethodHints', 'setInputMethodHints', 'type',
  'installSceneEventFilter', 'removeSceneEventFilter', 'sceneEventFilter',
  'sceneEvent', 'contextMenuEvent', 'dragEnterEvent', 'dragLeaveEvent',
  'dragMoveEvent', 'dropEvent', 'focusInEvent', 'focusOutEvent',
  'hoverEnterEvent', 'hoverMoveEvent', 'hoverLeaveEvent', 'keyPressEvent',
  'keyReleaseEvent', 'mousePressEvent', 'mouseMoveEvent',
  'mouseReleaseEvent', 'mouseDoubleClickEvent', 'wheelEvent',
  'inputMethodEvent', 'inputMethodQuery', 'itemChange', 'extension'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsItem::~QGraphicsItem()': the destructor: Python never
    removes a C++ QGraphicsItem.
  - Qt's 'const QGraphicsObject *QGraphicsItem::toGraphicsObject() const':
    takes in Python what 'QGraphicsObject *QGraphicsItem::toGraphicsObject()'
    takes.
  - Qt's 'QTransform QGraphicsItem::itemTransform(const QGraphicsItem *other,
    bool *ok) const': takes a number to change where it is.

  What has no ritual
  ------------------

  17 of the 215 functions Qt declares: 7 protected; 5 takes or gives a type
  that cannot be passed yet; 2 forbidden; 2 private; 1 the class is abstract,
  so C++ cannot make one.

  What to expect
  --------------

  - The C++ QGraphicsItem is created at the first use, not by
    'QGraphicsItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsItem.
  """

  #  The enums Qt writes inside QGraphicsItem, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class CacheMode(CuteNum):
    """
    The enum 'QGraphicsItem::CacheMode' of Qt, with the 3 names Qt gives in
    it.
    """

    NoCache = Kee[int](0)
    ItemCoordinateCache = Kee[int](1)
    DeviceCoordinateCache = Kee[int](2)

  class GraphicsItemChange(CuteNum):
    """
    The enum 'QGraphicsItem::GraphicsItemChange' of Qt, with the 33 names Qt
    gives in it.
    """

    ItemPositionChange = Kee[int](0)
    ItemVisibleChange = Kee[int](2)
    ItemEnabledChange = Kee[int](3)
    ItemSelectedChange = Kee[int](4)
    ItemParentChange = Kee[int](5)
    ItemChildAddedChange = Kee[int](6)
    ItemChildRemovedChange = Kee[int](7)
    ItemTransformChange = Kee[int](8)
    ItemPositionHasChanged = Kee[int](9)
    ItemTransformHasChanged = Kee[int](10)
    ItemSceneChange = Kee[int](11)
    ItemVisibleHasChanged = Kee[int](12)
    ItemEnabledHasChanged = Kee[int](13)
    ItemSelectedHasChanged = Kee[int](14)
    ItemParentHasChanged = Kee[int](15)
    ItemSceneHasChanged = Kee[int](16)
    ItemCursorChange = Kee[int](17)
    ItemCursorHasChanged = Kee[int](18)
    ItemToolTipChange = Kee[int](19)
    ItemToolTipHasChanged = Kee[int](20)
    ItemFlagsChange = Kee[int](21)
    ItemFlagsHaveChanged = Kee[int](22)
    ItemZValueChange = Kee[int](23)
    ItemZValueHasChanged = Kee[int](24)
    ItemOpacityChange = Kee[int](25)
    ItemOpacityHasChanged = Kee[int](26)
    ItemScenePositionHasChanged = Kee[int](27)
    ItemRotationChange = Kee[int](28)
    ItemRotationHasChanged = Kee[int](29)
    ItemScaleChange = Kee[int](30)
    ItemScaleHasChanged = Kee[int](31)
    ItemTransformOriginPointChange = Kee[int](32)
    ItemTransformOriginPointHasChanged = Kee[int](33)

  class GraphicsItemFlag(CuteFlags):
    """
    The flags enum 'QGraphicsItem::GraphicsItemFlag' of Qt, with the 20 names
    Qt gives in it. Qt names the type of its combinations
    'QGraphicsItem::GraphicsItemFlags'.
    """

    ItemIsMovable = 0x1
    ItemIsSelectable = 0x2
    ItemIsFocusable = 0x4
    ItemClipsToShape = 0x8
    ItemClipsChildrenToShape = 0x10
    ItemIgnoresTransformations = 0x20
    ItemIgnoresParentOpacity = 0x40
    ItemDoesntPropagateOpacityToChildren = 0x80
    ItemStacksBehindParent = 0x100
    ItemUsesExtendedStyleOption = 0x200
    ItemHasNoContents = 0x400
    ItemSendsGeometryChanges = 0x800
    ItemAcceptsInputMethod = 0x1000
    ItemNegativeZStacksBehindParent = 0x2000
    ItemIsPanel = 0x4000
    ItemIsFocusScope = 0x8000
    ItemSendsScenePositionChanges = 0x10000
    ItemStopsClickFocusPropagation = 0x20000
    ItemStopsFocusHandling = 0x40000
    ItemContainsChildrenInShape = 0x80000

  GraphicsItemFlags = GraphicsItemFlag

  class PanelModality(CuteNum):
    """
    The enum 'QGraphicsItem::PanelModality' of Qt, with the 3 names Qt gives
    in it.
    """

    NonModal = Kee[int](0)
    PanelModal = Kee[int](1)
    SceneModal = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsItem'

  #  A C++ QGraphicsItem Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsItem'

  #  The functions Qt calls itself that QGraphicsItem is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'supportsExtension': (
          'bool QGraphicsItem::supportsExtension(Extension) const',
      ),
      'setExtension': (
          'void QGraphicsItem::setExtension(Extension, const QVariant &)',
      ),
  }

  #  The functions Qt calls itself that QGraphicsItem is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'advance': (
          ('_ZN13QGraphicsItem7advanceEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'boundingRect': (
          ('_ZNK13QGraphicsItem12boundingRectEv',
           ('address', 'value', 'QtCore:QRectF'),
           ()),
      ),
      'shape': (
          ('_ZNK13QGraphicsItem5shapeEv',
           ('address', 'value', 'QtGui:QPainterPath'),
           ()),
      ),
      'contains': (
          ('_ZNK13QGraphicsItem8containsERK7QPointF',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QPointF'),
           )),
      ),
      'collidesWithItem': (
          ('_ZNK13QGraphicsItem16collidesWithItemEPKS_N2Qt17ItemSelectionMo'
           'deE',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtWidgets:QGraphicsItem'),
               ('int', 'enum', 'QtCore:Qt.ItemSelectionMode'),
           )),
      ),
      'collidesWithPath': (
          ('_ZNK13QGraphicsItem16collidesWithPathERK12QPainterPathN2Qt17Ite'
           'mSelectionModeE',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtGui:QPainterPath'),
               ('int', 'enum', 'QtCore:Qt.ItemSelectionMode'),
           )),
      ),
      'isObscuredBy': (
          ('_ZNK13QGraphicsItem12isObscuredByEPKS_',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtWidgets:QGraphicsItem'),
           )),
      ),
      'opaqueArea': (
          ('_ZNK13QGraphicsItem10opaqueAreaEv',
           ('address', 'value', 'QtGui:QPainterPath'),
           ()),
      ),
      'paint': (
          ('_ZN13QGraphicsItem5paintEP8QPainterPK24QStyleOptionGraphicsItem'
           'P7QWidget',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPainter'),
               ('address', 'address', 'QtWidgets:QStyleOptionGraphicsItem'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'type': (
          ('_ZNK13QGraphicsItem4typeEv',
           ('int', 'number', ''),
           ()),
      ),
      'sceneEventFilter': (
          ('_ZN13QGraphicsItem16sceneEventFilterEPS_P6QEvent',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtWidgets:QGraphicsItem'),
               ('address', 'address', 'QtCore:QEvent'),
           )),
      ),
      'sceneEvent': (
          ('_ZN13QGraphicsItem10sceneEventEP6QEvent',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCore:QEvent'),
           )),
      ),
      'contextMenuEvent': (
          ('_ZN13QGraphicsItem16contextMenuEventEP30QGraphicsSceneContextMe'
           'nuEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtWidgets:QGraphicsSceneContextMenuEvent'),
           )),
      ),
      'dragEnterEvent': (
          ('_ZN13QGraphicsItem14dragEnterEventEP27QGraphicsSceneDragDropEve'
           'nt',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtWidgets:QGraphicsSceneDragDropEvent'),
           )),
      ),
      'dragLeaveEvent': (
          ('_ZN13QGraphicsItem14dragLeaveEventEP27QGraphicsSceneDragDropEve'
           'nt',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtWidgets:QGraphicsSceneDragDropEvent'),
           )),
      ),
      'dragMoveEvent': (
          ('_ZN13QGraphicsItem13dragMoveEventEP27QGraphicsSceneDragDropEven'
           't',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtWidgets:QGraphicsSceneDragDropEvent'),
           )),
      ),
      'dropEvent': (
          ('_ZN13QGraphicsItem9dropEventEP27QGraphicsSceneDragDropEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtWidgets:QGraphicsSceneDragDropEvent'),
           )),
      ),
      'focusInEvent': (
          ('_ZN13QGraphicsItem12focusInEventEP11QFocusEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QFocusEvent'),
           )),
      ),
      'focusOutEvent': (
          ('_ZN13QGraphicsItem13focusOutEventEP11QFocusEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QFocusEvent'),
           )),
      ),
      'hoverEnterEvent': (
          ('_ZN13QGraphicsItem15hoverEnterEventEP24QGraphicsSceneHoverEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QGraphicsSceneHoverEvent'),
           )),
      ),
      'hoverMoveEvent': (
          ('_ZN13QGraphicsItem14hoverMoveEventEP24QGraphicsSceneHoverEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QGraphicsSceneHoverEvent'),
           )),
      ),
      'hoverLeaveEvent': (
          ('_ZN13QGraphicsItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QGraphicsSceneHoverEvent'),
           )),
      ),
      'keyPressEvent': (
          ('_ZN13QGraphicsItem13keyPressEventEP9QKeyEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QKeyEvent'),
           )),
      ),
      'keyReleaseEvent': (
          ('_ZN13QGraphicsItem15keyReleaseEventEP9QKeyEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QKeyEvent'),
           )),
      ),
      'mousePressEvent': (
          ('_ZN13QGraphicsItem15mousePressEventEP24QGraphicsSceneMouseEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QGraphicsSceneMouseEvent'),
           )),
      ),
      'mouseMoveEvent': (
          ('_ZN13QGraphicsItem14mouseMoveEventEP24QGraphicsSceneMouseEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QGraphicsSceneMouseEvent'),
           )),
      ),
      'mouseReleaseEvent': (
          ('_ZN13QGraphicsItem17mouseReleaseEventEP24QGraphicsSceneMouseEve'
           'nt',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QGraphicsSceneMouseEvent'),
           )),
      ),
      'mouseDoubleClickEvent': (
          ('_ZN13QGraphicsItem21mouseDoubleClickEventEP24QGraphicsSceneMous'
           'eEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QGraphicsSceneMouseEvent'),
           )),
      ),
      'wheelEvent': (
          ('_ZN13QGraphicsItem10wheelEventEP24QGraphicsSceneWheelEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QGraphicsSceneWheelEvent'),
           )),
      ),
      'inputMethodEvent': (
          ('_ZN13QGraphicsItem16inputMethodEventEP17QInputMethodEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QInputMethodEvent'),
           )),
      ),
      'inputMethodQuery': (
          ('_ZNK13QGraphicsItem16inputMethodQueryEN2Qt16InputMethodQueryE',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('int', 'enum', 'QtCore:Qt.InputMethodQuery'),
           )),
      ),
      'itemChange': (
          ('_ZN13QGraphicsItem10itemChangeENS_18GraphicsItemChangeERK8QVari'
           'ant',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('int', 'enum', 'QtWidgets:QGraphicsItem.GraphicsItemChange'),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'extension': (
          ('_ZNK13QGraphicsItem9extensionERK8QVariant',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('address', 'value', 'QtCore:QVariant'),
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

  def scene(self) -> Optional[QGraphicsScene]:
    """
    Calls Qt's 'QGraphicsScene *QGraphicsItem::scene() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#scene

    Returns
    -------

    Optional[QGraphicsScene]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsScene *QGraphicsItem::scene() const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem5sceneEv',
    )
    from . import QGraphicsScene
    return QGraphicsScene._cuteAt(address)

  def parentItem(self) -> Optional[QGraphicsItem]:
    """
    Calls Qt's 'QGraphicsItem *QGraphicsItem::parentItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#parentItem

    Returns
    -------

    Optional[QGraphicsItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsItem *QGraphicsItem::parentItem() const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem10parentItemEv',
    )
    return QGraphicsItem._cuteAt(address)

  def topLevelItem(self) -> Optional[QGraphicsItem]:
    """
    Calls Qt's 'QGraphicsItem *QGraphicsItem::topLevelItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#topLevelItem

    Returns
    -------

    Optional[QGraphicsItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsItem *QGraphicsItem::topLevelItem() const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem12topLevelItemEv',
    )
    return QGraphicsItem._cuteAt(address)

  def parentObject(self) -> Optional[QGraphicsObject]:
    """
    Calls Qt's 'QGraphicsObject *QGraphicsItem::parentObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#parentObject

    Returns
    -------

    Optional[QGraphicsObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsObject *QGraphicsItem::parentObject() const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem12parentObjectEv',
    )
    from . import QGraphicsObject
    return QGraphicsObject._cuteAt(address)

  def parentWidget(self) -> Optional[QGraphicsWidget]:
    """
    Calls Qt's 'QGraphicsWidget *QGraphicsItem::parentWidget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#parentWidget

    Returns
    -------

    Optional[QGraphicsWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsWidget *QGraphicsItem::parentWidget() const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem12parentWidgetEv',
    )
    from . import QGraphicsWidget
    return QGraphicsWidget._cuteAt(address)

  def topLevelWidget(self) -> Optional[QGraphicsWidget]:
    """
    Calls Qt's 'QGraphicsWidget *QGraphicsItem::topLevelWidget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#topLevelWidget

    Returns
    -------

    Optional[QGraphicsWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsWidget *QGraphicsItem::topLevelWidget() const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem14topLevelWidgetEv',
    )
    from . import QGraphicsWidget
    return QGraphicsWidget._cuteAt(address)

  def window(self) -> Optional[QGraphicsWidget]:
    """
    Calls Qt's 'QGraphicsWidget *QGraphicsItem::window() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#window

    Returns
    -------

    Optional[QGraphicsWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsWidget *QGraphicsItem::window() const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem6windowEv',
    )
    from . import QGraphicsWidget
    return QGraphicsWidget._cuteAt(address)

  def panel(self) -> Optional[QGraphicsItem]:
    """
    Calls Qt's 'QGraphicsItem *QGraphicsItem::panel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#panel

    Returns
    -------

    Optional[QGraphicsItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsItem *QGraphicsItem::panel() const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem5panelEv',
    )
    return QGraphicsItem._cuteAt(address)

  def isWidget(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsItem::isWidget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#isWidget
    """
    #  bool QGraphicsItem::isWidget() const
    return self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem8isWidgetEv',
    )

  def isWindow(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsItem::isWindow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#isWindow
    """
    #  bool QGraphicsItem::isWindow() const
    return self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem8isWindowEv',
    )

  def isPanel(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsItem::isPanel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#isPanel
    """
    #  bool QGraphicsItem::isPanel() const
    return self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem7isPanelEv',
    )

  def group(self) -> Optional[QGraphicsItemGroup]:
    """
    Calls Qt's 'QGraphicsItemGroup *QGraphicsItem::group() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#group

    Returns
    -------

    Optional[QGraphicsItemGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsItemGroup *QGraphicsItem::group() const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem5groupEv',
    )
    from . import QGraphicsItemGroup
    return QGraphicsItemGroup._cuteAt(address)

  def flags(self) -> GraphicsItemFlags:
    """
    Calls Qt's 'GraphicsItemFlags QGraphicsItem::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#flags

    Returns
    -------

    GraphicsItemFlags
      The value standing for the combination Qt gave back.
    """
    #  GraphicsItemFlags QGraphicsItem::flags() const
    return QGraphicsItem.GraphicsItemFlags(self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem5flagsEv',
    ))

  def cacheMode(self) -> CacheMode:
    """
    Calls Qt's 'CacheMode QGraphicsItem::cacheMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#cacheMode

    Returns
    -------

    CacheMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'CacheMode(number)' gives.
    """
    #  CacheMode QGraphicsItem::cacheMode() const
    return QGraphicsItem.CacheMode(self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem9cacheModeEv',
    ))

  def panelModality(self) -> PanelModality:
    """
    Calls Qt's 'PanelModality QGraphicsItem::panelModality() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#panelModality

    Returns
    -------

    PanelModality
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PanelModality(number)'
      gives.
    """
    #  PanelModality QGraphicsItem::panelModality() const
    return QGraphicsItem.PanelModality(self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem13panelModalityEv',
    ))

  def toolTip(self) -> str:
    """
    Calls Qt's 'QString QGraphicsItem::toolTip() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#toolTip

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGraphicsItem::toolTip() const
    return self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem7toolTipEv',
    )

  def cursor(self) -> QCursor:
    """
    Calls Qt's 'QCursor QGraphicsItem::cursor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#cursor

    Returns
    -------

    QCursor
      A new cute QCursor around the copy Qt gave back. Python owns it.
    """
    #  QCursor QGraphicsItem::cursor() const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem6cursorEv',
    )
    from ..QtGui import QCursor
    return QCursor._cuteOwning(address)

  def hasCursor(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsItem::hasCursor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#hasCursor
    """
    #  bool QGraphicsItem::hasCursor() const
    return self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem9hasCursorEv',
    )

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsItem::isVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#isVisible
    """
    #  bool QGraphicsItem::isVisible() const
    return self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem9isVisibleEv',
    )

  @overload(THIS)
  @overload(NoneType)
  def isVisibleTo(self, parent: Optional[QGraphicsItem]) -> bool:
    """
    Calls Qt's 'bool QGraphicsItem::isVisibleTo(const QGraphicsItem *parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#isVisibleTo

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGraphicsItem::isVisibleTo(const QGraphicsItem *parent) const
    return self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem11isVisibleToEPKS_',
        self._addressOf(parent, 'QGraphicsItem'),
    )

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsItem::isEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#isEnabled
    """
    #  bool QGraphicsItem::isEnabled() const
    return self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem9isEnabledEv',
    )

  def isSelected(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsItem::isSelected() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#isSelected
    """
    #  bool QGraphicsItem::isSelected() const
    return self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem10isSelectedEv',
    )

  def acceptDrops(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsItem::acceptDrops() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#acceptDrops
    """
    #  bool QGraphicsItem::acceptDrops() const
    return self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem11acceptDropsEv',
    )

  def opacity(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsItem::opacity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#opacity
    """
    #  qreal QGraphicsItem::opacity() const
    return self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem7opacityEv',
    )

  def effectiveOpacity(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsItem::effectiveOpacity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#effectiveOpacity
    """
    #  qreal QGraphicsItem::effectiveOpacity() const
    return self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem16effectiveOpacityEv',
    )

  def graphicsEffect(self) -> Optional[QGraphicsEffect]:
    """
    Calls Qt's 'QGraphicsEffect *QGraphicsItem::graphicsEffect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#graphicsEffect

    Returns
    -------

    Optional[QGraphicsEffect]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsEffect *QGraphicsItem::graphicsEffect() const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem14graphicsEffectEv',
    )
    from . import QGraphicsEffect
    return QGraphicsEffect._cuteAt(address)

  def acceptedMouseButtons(self) -> Qt.MouseButtons:
    """
    Calls Qt's 'Qt::MouseButtons QGraphicsItem::acceptedMouseButtons()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#acceptedMouseButtons

    Returns
    -------

    Qt.MouseButtons
      The value standing for the combination Qt gave back.
    """
    #  Qt::MouseButtons QGraphicsItem::acceptedMouseButtons() const
    return Qt.MouseButtons(self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem20acceptedMouseButtonsEv',
    ))

  def acceptHoverEvents(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsItem::acceptHoverEvents() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#acceptHoverEvents
    """
    #  bool QGraphicsItem::acceptHoverEvents() const
    return self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem17acceptHoverEventsEv',
    )

  def acceptTouchEvents(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsItem::acceptTouchEvents() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#acceptTouchEvents
    """
    #  bool QGraphicsItem::acceptTouchEvents() const
    return self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem17acceptTouchEventsEv',
    )

  def filtersChildEvents(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsItem::filtersChildEvents() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#filtersChildEvents
    """
    #  bool QGraphicsItem::filtersChildEvents() const
    return self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem18filtersChildEventsEv',
    )

  def handlesChildEvents(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsItem::handlesChildEvents() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#handlesChildEvents
    """
    #  bool QGraphicsItem::handlesChildEvents() const
    return self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem18handlesChildEventsEv',
    )

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsItem::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#isActive
    """
    #  bool QGraphicsItem::isActive() const
    return self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem8isActiveEv',
    )

  def hasFocus(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsItem::hasFocus() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#hasFocus
    """
    #  bool QGraphicsItem::hasFocus() const
    return self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem8hasFocusEv',
    )

  def focusProxy(self) -> Optional[QGraphicsItem]:
    """
    Calls Qt's 'QGraphicsItem *QGraphicsItem::focusProxy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#focusProxy

    Returns
    -------

    Optional[QGraphicsItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsItem *QGraphicsItem::focusProxy() const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem10focusProxyEv',
    )
    return QGraphicsItem._cuteAt(address)

  def focusItem(self) -> Optional[QGraphicsItem]:
    """
    Calls Qt's 'QGraphicsItem *QGraphicsItem::focusItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#focusItem

    Returns
    -------

    Optional[QGraphicsItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsItem *QGraphicsItem::focusItem() const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem9focusItemEv',
    )
    return QGraphicsItem._cuteAt(address)

  def focusScopeItem(self) -> Optional[QGraphicsItem]:
    """
    Calls Qt's 'QGraphicsItem *QGraphicsItem::focusScopeItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#focusScopeItem

    Returns
    -------

    Optional[QGraphicsItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsItem *QGraphicsItem::focusScopeItem() const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem14focusScopeItemEv',
    )
    return QGraphicsItem._cuteAt(address)

  def pos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsItem::pos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#pos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsItem::pos() const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem3posEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def x(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsItem::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#x
    """
    #  qreal QGraphicsItem::x() const
    return self._callAs('QGraphicsItem', 'ritual_ZNK13QGraphicsItem1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsItem::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#y
    """
    #  qreal QGraphicsItem::y() const
    return self._callAs('QGraphicsItem', 'ritual_ZNK13QGraphicsItem1yEv')

  def scenePos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsItem::scenePos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#scenePos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsItem::scenePos() const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem8scenePosEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def transform(self) -> QTransform:
    """
    Calls Qt's 'QTransform QGraphicsItem::transform() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#transform

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QGraphicsItem::transform() const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem9transformEv',
    )
    from ..QtGui import QTransform
    return QTransform._cuteOwning(address)

  def sceneTransform(self) -> QTransform:
    """
    Calls Qt's 'QTransform QGraphicsItem::sceneTransform() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#sceneTransform

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QGraphicsItem::sceneTransform() const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem14sceneTransformEv',
    )
    from ..QtGui import QTransform
    return QTransform._cuteOwning(address)

  @overload(QTransform)
  def deviceTransform(self, viewportTransform: QTransform) -> QTransform:
    """
    Calls Qt's 'QTransform QGraphicsItem::deviceTransform(const QTransform
    &viewportTransform) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#deviceTransform

    Parameters
    ----------

    viewportTransform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QGraphicsItem::deviceTransform(const QTransform
    #      &viewportTransform) const
    address = self._callAs(
        'QGraphicsItem',
        'ritual_ZNK13QGraphicsItem15deviceTransformERK10QTransform',
        self._valueOf(viewportTransform),
    )
    from ..QtGui import QTransform
    return QTransform._cuteOwning(address)

  def rotation(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsItem::rotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#rotation
    """
    #  qreal QGraphicsItem::rotation() const
    return self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem8rotationEv',
    )

  def scale(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsItem::scale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#scale
    """
    #  qreal QGraphicsItem::scale() const
    return self._callAs('QGraphicsItem', 'ritual_ZNK13QGraphicsItem5scaleEv')

  def transformOriginPoint(self) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsItem::transformOriginPoint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#transformOriginPoint

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsItem::transformOriginPoint() const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem20transformOriginPointEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def zValue(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsItem::zValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#zValue
    """
    #  qreal QGraphicsItem::zValue() const
    return self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem6zValueEv',
    )

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsItem::boundingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsItem::boundingRect() const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem12boundingRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def childrenBoundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsItem::childrenBoundingRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#childrenBoundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsItem::childrenBoundingRect() const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem20childrenBoundingRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def sceneBoundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsItem::sceneBoundingRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#sceneBoundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsItem::sceneBoundingRect() const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem17sceneBoundingRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def shape(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGraphicsItem::shape() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#shape

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGraphicsItem::shape() const
    ritual = 'ritual_ZNK13QGraphicsItem5shapeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QGraphicsItem5shapeEv'
    address = self._callAs('QGraphicsItem', ritual)
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  def isClipped(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsItem::isClipped() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#isClipped
    """
    #  bool QGraphicsItem::isClipped() const
    return self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem9isClippedEv',
    )

  def clipPath(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGraphicsItem::clipPath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#clipPath

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGraphicsItem::clipPath() const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem8clipPathEv',
    )
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  @overload(QPointF)
  def contains(self, point: QPointF) -> bool:
    """
    Calls Qt's 'bool QGraphicsItem::contains(const QPointF &point) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#contains

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QGraphicsItem::contains(const QPointF &point) const
    ritual = 'ritual_ZNK13QGraphicsItem8containsERK7QPointF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QGraphicsItem8containsERK7QPointF'
    return self._callAs('QGraphicsItem', ritual, self._valueOf(point))

  @overload(THIS)
  @overload(NoneType)
  @overload(THIS, Qt.ItemSelectionMode)
  @overload(NoneType, Qt.ItemSelectionMode)
  def collidesWithItem(
      self,
      other: Optional[QGraphicsItem],
      mode: Qt.ItemSelectionMode = Qt.ItemSelectionMode.IntersectsItemShape,
  ) -> bool:
    """
    Calls Qt's 'bool QGraphicsItem::collidesWithItem(const QGraphicsItem
    *other, Qt::ItemSelectionMode mode) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#collidesWithItem

    Parameters
    ----------

    other : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mode : Qt.ItemSelectionMode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ItemSelectionMode.IntersectsItemShape.
    """
    #  bool QGraphicsItem::collidesWithItem(const QGraphicsItem *other,
    #      Qt::ItemSelectionMode mode) const
    ritual = (
        'ritual_ZNK13QGraphicsItem16collidesWithItemEPKS_N2Qt17ItemSelectio'
        'nModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13QGraphicsItem16collidesWithItemEPKS_N2Qt17ItemSe'
          'lectionModeE')
    return self._callAs(
        'QGraphicsItem', ritual,
        self._addressOf(other, 'QGraphicsItem'), mode.value,
    )

  @overload(QPainterPath)
  @overload(QPainterPath, Qt.ItemSelectionMode)
  def collidesWithPath(
      self,
      path: QPainterPath,
      mode: Qt.ItemSelectionMode = Qt.ItemSelectionMode.IntersectsItemShape,
  ) -> bool:
    """
    Calls Qt's 'bool QGraphicsItem::collidesWithPath(const QPainterPath
    &path, Qt::ItemSelectionMode mode) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#collidesWithPath

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    mode : Qt.ItemSelectionMode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ItemSelectionMode.IntersectsItemShape.
    """
    #  bool QGraphicsItem::collidesWithPath(const QPainterPath &path,
    #      Qt::ItemSelectionMode mode) const
    ritual = (
        'ritual_ZNK13QGraphicsItem16collidesWithPathERK12QPainterPathN2Qt17'
        'ItemSelectionModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13QGraphicsItem16collidesWithPathERK12QPainterPath'
          'N2Qt17ItemSelectionModeE')
    return self._callAs(
        'QGraphicsItem', ritual, self._valueOf(path), mode.value,
    )

  @overload()
  @overload(QRectF)
  def isObscured(self, rect: Optional[QRectF] = None) -> bool:
    """
    Calls Qt's 'bool QGraphicsItem::isObscured(const QRectF &rect) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#isObscured

    Parameters
    ----------

    rect : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.
    """
    #  bool QGraphicsItem::isObscured(const QRectF &rect) const
    if rect is None:
      from ..QtCore import QRectF
      rect = QRectF()
    return self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem10isObscuredERK6QRectF',
        self._valueOf(rect),
    )

  @overload(float, float, float, float)
  def isObscured(self, x: float, y: float, w: float, h: float) -> bool:
    """
    Calls Qt's 'bool QGraphicsItem::isObscured(qreal x, qreal y, qreal w,
    qreal h) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#isObscured

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.
    """
    #  bool QGraphicsItem::isObscured(qreal x, qreal y, qreal w, qreal h)
    #      const
    return self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem10isObscuredEdddd',
        x, y, w, h,
    )

  @overload(THIS)
  @overload(NoneType)
  def isObscuredBy(self, item: Optional[QGraphicsItem]) -> bool:
    """
    Calls Qt's 'bool QGraphicsItem::isObscuredBy(const QGraphicsItem *item)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#isObscuredBy

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGraphicsItem::isObscuredBy(const QGraphicsItem *item) const
    ritual = 'ritual_ZNK13QGraphicsItem12isObscuredByEPKS_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QGraphicsItem12isObscuredByEPKS_'
    return self._callAs(
        'QGraphicsItem', ritual, self._addressOf(item, 'QGraphicsItem'),
    )

  def opaqueArea(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGraphicsItem::opaqueArea() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#opaqueArea

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGraphicsItem::opaqueArea() const
    ritual = 'ritual_ZNK13QGraphicsItem10opaqueAreaEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QGraphicsItem10opaqueAreaEv'
    address = self._callAs('QGraphicsItem', ritual)
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  @overload(QTransform)
  def boundingRegion(self, itemToDeviceTransform: QTransform) -> QRegion:
    """
    Calls Qt's 'QRegion QGraphicsItem::boundingRegion(const QTransform
    &itemToDeviceTransform) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#boundingRegion

    Parameters
    ----------

    itemToDeviceTransform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QGraphicsItem::boundingRegion(const QTransform
    #      &itemToDeviceTransform) const
    address = self._callAs(
        'QGraphicsItem',
        'ritual_ZNK13QGraphicsItem14boundingRegionERK10QTransform',
        self._valueOf(itemToDeviceTransform),
    )
    from ..QtGui import QRegion
    return QRegion._cuteOwning(address)

  def boundingRegionGranularity(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsItem::boundingRegionGranularity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#boundingRegionGranularity
    """
    #  qreal QGraphicsItem::boundingRegionGranularity() const
    return self._callAs(
        'QGraphicsItem',
        'ritual_ZNK13QGraphicsItem25boundingRegionGranularityEv',
    )

  @overload(THIS, QPointF)
  @overload(NoneType, QPointF)
  def mapToItem(
      self,
      item: Optional[QGraphicsItem],
      point: QPointF,
  ) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsItem::mapToItem(const QGraphicsItem *item,
    const QPointF &point) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapToItem

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsItem::mapToItem(const QGraphicsItem *item, const
    #      QPointF &point) const
    address = self._callAs(
        'QGraphicsItem',
        'ritual_ZNK13QGraphicsItem9mapToItemEPKS_RK7QPointF',
        self._addressOf(item, 'QGraphicsItem'), self._valueOf(point),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(THIS, QRectF)
  @overload(NoneType, QRectF)
  def mapToItem(
      self,
      item: Optional[QGraphicsItem],
      rect: QRectF,
  ) -> QPolygonF:
    """
    Calls Qt's 'QPolygonF QGraphicsItem::mapToItem(const QGraphicsItem *item,
    const QRectF &rect) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapToItem

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

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  QPolygonF QGraphicsItem::mapToItem(const QGraphicsItem *item, const
    #      QRectF &rect) const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem9mapToItemEPKS_RK6QRectF',
        self._addressOf(item, 'QGraphicsItem'), self._valueOf(rect),
    )
    from ..QtGui import QPolygonF
    return QPolygonF._cuteOwning(address)

  @overload(THIS, QPolygonF)
  @overload(NoneType, QPolygonF)
  def mapToItem(
      self,
      item: Optional[QGraphicsItem],
      polygon: QPolygonF,
  ) -> QPolygonF:
    """
    Calls Qt's 'QPolygonF QGraphicsItem::mapToItem(const QGraphicsItem *item,
    const QPolygonF &polygon) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapToItem

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    polygon : QPolygonF
      Passed on as a value: Qt reads the C++ QPolygonF, which stays Python's
      own.

    Returns
    -------

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  QPolygonF QGraphicsItem::mapToItem(const QGraphicsItem *item, const
    #      QPolygonF &polygon) const
    address = self._callAs(
        'QGraphicsItem',
        'ritual_ZNK13QGraphicsItem9mapToItemEPKS_RK9QPolygonF',
        self._addressOf(item, 'QGraphicsItem'), self._valueOf(polygon),
    )
    from ..QtGui import QPolygonF
    return QPolygonF._cuteOwning(address)

  @overload(THIS, QPainterPath)
  @overload(NoneType, QPainterPath)
  def mapToItem(
      self,
      item: Optional[QGraphicsItem],
      path: QPainterPath,
  ) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGraphicsItem::mapToItem(const QGraphicsItem
    *item, const QPainterPath &path) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapToItem

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGraphicsItem::mapToItem(const QGraphicsItem *item, const
    #      QPainterPath &path) const
    address = self._callAs(
        'QGraphicsItem',
        'ritual_ZNK13QGraphicsItem9mapToItemEPKS_RK12QPainterPath',
        self._addressOf(item, 'QGraphicsItem'), self._valueOf(path),
    )
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  @overload(THIS, float, float)
  @overload(NoneType, float, float)
  def mapToItem(
      self,
      item: Optional[QGraphicsItem],
      x: float,
      y: float,
  ) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsItem::mapToItem(const QGraphicsItem *item,
    qreal x, qreal y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapToItem

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsItem::mapToItem(const QGraphicsItem *item, qreal x,
    #      qreal y) const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem9mapToItemEPKS_dd',
        self._addressOf(item, 'QGraphicsItem'), x, y,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(THIS, float, float, float, float)
  @overload(NoneType, float, float, float, float)
  def mapToItem(
      self,
      item: Optional[QGraphicsItem],
      x: float,
      y: float,
      w: float,
      h: float,
  ) -> QPolygonF:
    """
    Calls Qt's 'QPolygonF QGraphicsItem::mapToItem(const QGraphicsItem *item,
    qreal x, qreal y, qreal w, qreal h) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapToItem

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.

    Returns
    -------

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  QPolygonF QGraphicsItem::mapToItem(const QGraphicsItem *item, qreal x,
    #      qreal y, qreal w, qreal h) const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem9mapToItemEPKS_dddd',
        self._addressOf(item, 'QGraphicsItem'), x, y, w, h,
    )
    from ..QtGui import QPolygonF
    return QPolygonF._cuteOwning(address)

  @overload(QPointF)
  def mapToParent(self, point: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsItem::mapToParent(const QPointF &point)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapToParent

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
    #  QPointF QGraphicsItem::mapToParent(const QPointF &point) const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem11mapToParentERK7QPointF',
        self._valueOf(point),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QRectF)
  def mapToParent(self, rect: QRectF) -> QPolygonF:
    """
    Calls Qt's 'QPolygonF QGraphicsItem::mapToParent(const QRectF &rect)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapToParent

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  QPolygonF QGraphicsItem::mapToParent(const QRectF &rect) const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem11mapToParentERK6QRectF',
        self._valueOf(rect),
    )
    from ..QtGui import QPolygonF
    return QPolygonF._cuteOwning(address)

  @overload(QPolygonF)
  def mapToParent(self, polygon: QPolygonF) -> QPolygonF:
    """
    Calls Qt's 'QPolygonF QGraphicsItem::mapToParent(const QPolygonF
    &polygon) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapToParent

    Parameters
    ----------

    polygon : QPolygonF
      Passed on as a value: Qt reads the C++ QPolygonF, which stays Python's
      own.

    Returns
    -------

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  QPolygonF QGraphicsItem::mapToParent(const QPolygonF &polygon) const
    address = self._callAs(
        'QGraphicsItem',
        'ritual_ZNK13QGraphicsItem11mapToParentERK9QPolygonF',
        self._valueOf(polygon),
    )
    from ..QtGui import QPolygonF
    return QPolygonF._cuteOwning(address)

  @overload(QPainterPath)
  def mapToParent(self, path: QPainterPath) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGraphicsItem::mapToParent(const QPainterPath
    &path) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapToParent

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGraphicsItem::mapToParent(const QPainterPath &path)
    #      const
    address = self._callAs(
        'QGraphicsItem',
        'ritual_ZNK13QGraphicsItem11mapToParentERK12QPainterPath',
        self._valueOf(path),
    )
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  @overload(float, float)
  def mapToParent(self, x: float, y: float) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsItem::mapToParent(qreal x, qreal y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapToParent

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsItem::mapToParent(qreal x, qreal y) const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem11mapToParentEdd', x, y,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(float, float, float, float)
  def mapToParent(self, x: float, y: float, w: float, h: float) -> QPolygonF:
    """
    Calls Qt's 'QPolygonF QGraphicsItem::mapToParent(qreal x, qreal y, qreal
    w, qreal h) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapToParent

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.

    Returns
    -------

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  QPolygonF QGraphicsItem::mapToParent(qreal x, qreal y, qreal w, qreal
    #      h) const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem11mapToParentEdddd',
        x, y, w, h,
    )
    from ..QtGui import QPolygonF
    return QPolygonF._cuteOwning(address)

  @overload(QPointF)
  def mapToScene(self, point: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsItem::mapToScene(const QPointF &point)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapToScene

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
    #  QPointF QGraphicsItem::mapToScene(const QPointF &point) const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem10mapToSceneERK7QPointF',
        self._valueOf(point),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QRectF)
  def mapToScene(self, rect: QRectF) -> QPolygonF:
    """
    Calls Qt's 'QPolygonF QGraphicsItem::mapToScene(const QRectF &rect)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapToScene

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  QPolygonF QGraphicsItem::mapToScene(const QRectF &rect) const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem10mapToSceneERK6QRectF',
        self._valueOf(rect),
    )
    from ..QtGui import QPolygonF
    return QPolygonF._cuteOwning(address)

  @overload(QPolygonF)
  def mapToScene(self, polygon: QPolygonF) -> QPolygonF:
    """
    Calls Qt's 'QPolygonF QGraphicsItem::mapToScene(const QPolygonF &polygon)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapToScene

    Parameters
    ----------

    polygon : QPolygonF
      Passed on as a value: Qt reads the C++ QPolygonF, which stays Python's
      own.

    Returns
    -------

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  QPolygonF QGraphicsItem::mapToScene(const QPolygonF &polygon) const
    address = self._callAs(
        'QGraphicsItem',
        'ritual_ZNK13QGraphicsItem10mapToSceneERK9QPolygonF',
        self._valueOf(polygon),
    )
    from ..QtGui import QPolygonF
    return QPolygonF._cuteOwning(address)

  @overload(QPainterPath)
  def mapToScene(self, path: QPainterPath) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGraphicsItem::mapToScene(const QPainterPath
    &path) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapToScene

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGraphicsItem::mapToScene(const QPainterPath &path) const
    address = self._callAs(
        'QGraphicsItem',
        'ritual_ZNK13QGraphicsItem10mapToSceneERK12QPainterPath',
        self._valueOf(path),
    )
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  @overload(float, float)
  def mapToScene(self, x: float, y: float) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsItem::mapToScene(qreal x, qreal y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapToScene

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsItem::mapToScene(qreal x, qreal y) const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem10mapToSceneEdd', x, y,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(float, float, float, float)
  def mapToScene(self, x: float, y: float, w: float, h: float) -> QPolygonF:
    """
    Calls Qt's 'QPolygonF QGraphicsItem::mapToScene(qreal x, qreal y, qreal
    w, qreal h) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapToScene

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.

    Returns
    -------

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  QPolygonF QGraphicsItem::mapToScene(qreal x, qreal y, qreal w, qreal
    #      h) const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem10mapToSceneEdddd',
        x, y, w, h,
    )
    from ..QtGui import QPolygonF
    return QPolygonF._cuteOwning(address)

  @overload(THIS, QRectF)
  @overload(NoneType, QRectF)
  def mapRectToItem(
      self,
      item: Optional[QGraphicsItem],
      rect: QRectF,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsItem::mapRectToItem(const QGraphicsItem
    *item, const QRectF &rect) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapRectToItem

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

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsItem::mapRectToItem(const QGraphicsItem *item, const
    #      QRectF &rect) const
    address = self._callAs(
        'QGraphicsItem',
        'ritual_ZNK13QGraphicsItem13mapRectToItemEPKS_RK6QRectF',
        self._addressOf(item, 'QGraphicsItem'), self._valueOf(rect),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(THIS, float, float, float, float)
  @overload(NoneType, float, float, float, float)
  def mapRectToItem(
      self,
      item: Optional[QGraphicsItem],
      x: float,
      y: float,
      w: float,
      h: float,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsItem::mapRectToItem(const QGraphicsItem
    *item, qreal x, qreal y, qreal w, qreal h) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapRectToItem

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsItem::mapRectToItem(const QGraphicsItem *item, qreal
    #      x, qreal y, qreal w, qreal h) const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem13mapRectToItemEPKS_dddd',
        self._addressOf(item, 'QGraphicsItem'), x, y, w, h,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QRectF)
  def mapRectToParent(self, rect: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsItem::mapRectToParent(const QRectF &rect)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapRectToParent

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
    #  QRectF QGraphicsItem::mapRectToParent(const QRectF &rect) const
    address = self._callAs(
        'QGraphicsItem',
        'ritual_ZNK13QGraphicsItem15mapRectToParentERK6QRectF',
        self._valueOf(rect),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(float, float, float, float)
  def mapRectToParent(
      self,
      x: float,
      y: float,
      w: float,
      h: float,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsItem::mapRectToParent(qreal x, qreal y, qreal
    w, qreal h) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapRectToParent

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsItem::mapRectToParent(qreal x, qreal y, qreal w, qreal
    #      h) const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem15mapRectToParentEdddd',
        x, y, w, h,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QRectF)
  def mapRectToScene(self, rect: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsItem::mapRectToScene(const QRectF &rect)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapRectToScene

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
    #  QRectF QGraphicsItem::mapRectToScene(const QRectF &rect) const
    address = self._callAs(
        'QGraphicsItem',
        'ritual_ZNK13QGraphicsItem14mapRectToSceneERK6QRectF',
        self._valueOf(rect),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(float, float, float, float)
  def mapRectToScene(self, x: float, y: float, w: float, h: float) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsItem::mapRectToScene(qreal x, qreal y, qreal
    w, qreal h) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapRectToScene

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsItem::mapRectToScene(qreal x, qreal y, qreal w, qreal
    #      h) const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem14mapRectToSceneEdddd',
        x, y, w, h,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(THIS, QPointF)
  @overload(NoneType, QPointF)
  def mapFromItem(
      self,
      item: Optional[QGraphicsItem],
      point: QPointF,
  ) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsItem::mapFromItem(const QGraphicsItem *item,
    const QPointF &point) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapFromItem

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsItem::mapFromItem(const QGraphicsItem *item, const
    #      QPointF &point) const
    address = self._callAs(
        'QGraphicsItem',
        'ritual_ZNK13QGraphicsItem11mapFromItemEPKS_RK7QPointF',
        self._addressOf(item, 'QGraphicsItem'), self._valueOf(point),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(THIS, QRectF)
  @overload(NoneType, QRectF)
  def mapFromItem(
      self,
      item: Optional[QGraphicsItem],
      rect: QRectF,
  ) -> QPolygonF:
    """
    Calls Qt's 'QPolygonF QGraphicsItem::mapFromItem(const QGraphicsItem
    *item, const QRectF &rect) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapFromItem

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

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  QPolygonF QGraphicsItem::mapFromItem(const QGraphicsItem *item, const
    #      QRectF &rect) const
    address = self._callAs(
        'QGraphicsItem',
        'ritual_ZNK13QGraphicsItem11mapFromItemEPKS_RK6QRectF',
        self._addressOf(item, 'QGraphicsItem'), self._valueOf(rect),
    )
    from ..QtGui import QPolygonF
    return QPolygonF._cuteOwning(address)

  @overload(THIS, QPolygonF)
  @overload(NoneType, QPolygonF)
  def mapFromItem(
      self,
      item: Optional[QGraphicsItem],
      polygon: QPolygonF,
  ) -> QPolygonF:
    """
    Calls Qt's 'QPolygonF QGraphicsItem::mapFromItem(const QGraphicsItem
    *item, const QPolygonF &polygon) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapFromItem

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    polygon : QPolygonF
      Passed on as a value: Qt reads the C++ QPolygonF, which stays Python's
      own.

    Returns
    -------

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  QPolygonF QGraphicsItem::mapFromItem(const QGraphicsItem *item, const
    #      QPolygonF &polygon) const
    address = self._callAs(
        'QGraphicsItem',
        'ritual_ZNK13QGraphicsItem11mapFromItemEPKS_RK9QPolygonF',
        self._addressOf(item, 'QGraphicsItem'), self._valueOf(polygon),
    )
    from ..QtGui import QPolygonF
    return QPolygonF._cuteOwning(address)

  @overload(THIS, QPainterPath)
  @overload(NoneType, QPainterPath)
  def mapFromItem(
      self,
      item: Optional[QGraphicsItem],
      path: QPainterPath,
  ) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGraphicsItem::mapFromItem(const QGraphicsItem
    *item, const QPainterPath &path) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapFromItem

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGraphicsItem::mapFromItem(const QGraphicsItem *item,
    #      const QPainterPath &path) const
    address = self._callAs(
        'QGraphicsItem',
        'ritual_ZNK13QGraphicsItem11mapFromItemEPKS_RK12QPainterPath',
        self._addressOf(item, 'QGraphicsItem'), self._valueOf(path),
    )
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  @overload(THIS, float, float)
  @overload(NoneType, float, float)
  def mapFromItem(
      self,
      item: Optional[QGraphicsItem],
      x: float,
      y: float,
  ) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsItem::mapFromItem(const QGraphicsItem *item,
    qreal x, qreal y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapFromItem

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsItem::mapFromItem(const QGraphicsItem *item, qreal x,
    #      qreal y) const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem11mapFromItemEPKS_dd',
        self._addressOf(item, 'QGraphicsItem'), x, y,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(THIS, float, float, float, float)
  @overload(NoneType, float, float, float, float)
  def mapFromItem(
      self,
      item: Optional[QGraphicsItem],
      x: float,
      y: float,
      w: float,
      h: float,
  ) -> QPolygonF:
    """
    Calls Qt's 'QPolygonF QGraphicsItem::mapFromItem(const QGraphicsItem
    *item, qreal x, qreal y, qreal w, qreal h) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapFromItem

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.

    Returns
    -------

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  QPolygonF QGraphicsItem::mapFromItem(const QGraphicsItem *item, qreal
    #      x, qreal y, qreal w, qreal h) const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem11mapFromItemEPKS_dddd',
        self._addressOf(item, 'QGraphicsItem'), x, y, w, h,
    )
    from ..QtGui import QPolygonF
    return QPolygonF._cuteOwning(address)

  @overload(QPointF)
  def mapFromParent(self, point: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsItem::mapFromParent(const QPointF &point)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapFromParent

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
    #  QPointF QGraphicsItem::mapFromParent(const QPointF &point) const
    address = self._callAs(
        'QGraphicsItem',
        'ritual_ZNK13QGraphicsItem13mapFromParentERK7QPointF',
        self._valueOf(point),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QRectF)
  def mapFromParent(self, rect: QRectF) -> QPolygonF:
    """
    Calls Qt's 'QPolygonF QGraphicsItem::mapFromParent(const QRectF &rect)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapFromParent

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  QPolygonF QGraphicsItem::mapFromParent(const QRectF &rect) const
    address = self._callAs(
        'QGraphicsItem',
        'ritual_ZNK13QGraphicsItem13mapFromParentERK6QRectF',
        self._valueOf(rect),
    )
    from ..QtGui import QPolygonF
    return QPolygonF._cuteOwning(address)

  @overload(QPolygonF)
  def mapFromParent(self, polygon: QPolygonF) -> QPolygonF:
    """
    Calls Qt's 'QPolygonF QGraphicsItem::mapFromParent(const QPolygonF
    &polygon) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapFromParent

    Parameters
    ----------

    polygon : QPolygonF
      Passed on as a value: Qt reads the C++ QPolygonF, which stays Python's
      own.

    Returns
    -------

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  QPolygonF QGraphicsItem::mapFromParent(const QPolygonF &polygon) const
    address = self._callAs(
        'QGraphicsItem',
        'ritual_ZNK13QGraphicsItem13mapFromParentERK9QPolygonF',
        self._valueOf(polygon),
    )
    from ..QtGui import QPolygonF
    return QPolygonF._cuteOwning(address)

  @overload(QPainterPath)
  def mapFromParent(self, path: QPainterPath) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGraphicsItem::mapFromParent(const QPainterPath
    &path) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapFromParent

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGraphicsItem::mapFromParent(const QPainterPath &path)
    #      const
    address = self._callAs(
        'QGraphicsItem',
        'ritual_ZNK13QGraphicsItem13mapFromParentERK12QPainterPath',
        self._valueOf(path),
    )
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  @overload(float, float)
  def mapFromParent(self, x: float, y: float) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsItem::mapFromParent(qreal x, qreal y)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapFromParent

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsItem::mapFromParent(qreal x, qreal y) const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem13mapFromParentEdd', x, y,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(float, float, float, float)
  def mapFromParent(
      self,
      x: float,
      y: float,
      w: float,
      h: float,
  ) -> QPolygonF:
    """
    Calls Qt's 'QPolygonF QGraphicsItem::mapFromParent(qreal x, qreal y,
    qreal w, qreal h) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapFromParent

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.

    Returns
    -------

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  QPolygonF QGraphicsItem::mapFromParent(qreal x, qreal y, qreal w,
    #      qreal h) const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem13mapFromParentEdddd',
        x, y, w, h,
    )
    from ..QtGui import QPolygonF
    return QPolygonF._cuteOwning(address)

  @overload(QPointF)
  def mapFromScene(self, point: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsItem::mapFromScene(const QPointF &point)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapFromScene

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
    #  QPointF QGraphicsItem::mapFromScene(const QPointF &point) const
    address = self._callAs(
        'QGraphicsItem',
        'ritual_ZNK13QGraphicsItem12mapFromSceneERK7QPointF',
        self._valueOf(point),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QRectF)
  def mapFromScene(self, rect: QRectF) -> QPolygonF:
    """
    Calls Qt's 'QPolygonF QGraphicsItem::mapFromScene(const QRectF &rect)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapFromScene

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  QPolygonF QGraphicsItem::mapFromScene(const QRectF &rect) const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem12mapFromSceneERK6QRectF',
        self._valueOf(rect),
    )
    from ..QtGui import QPolygonF
    return QPolygonF._cuteOwning(address)

  @overload(QPolygonF)
  def mapFromScene(self, polygon: QPolygonF) -> QPolygonF:
    """
    Calls Qt's 'QPolygonF QGraphicsItem::mapFromScene(const QPolygonF
    &polygon) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapFromScene

    Parameters
    ----------

    polygon : QPolygonF
      Passed on as a value: Qt reads the C++ QPolygonF, which stays Python's
      own.

    Returns
    -------

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  QPolygonF QGraphicsItem::mapFromScene(const QPolygonF &polygon) const
    address = self._callAs(
        'QGraphicsItem',
        'ritual_ZNK13QGraphicsItem12mapFromSceneERK9QPolygonF',
        self._valueOf(polygon),
    )
    from ..QtGui import QPolygonF
    return QPolygonF._cuteOwning(address)

  @overload(QPainterPath)
  def mapFromScene(self, path: QPainterPath) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGraphicsItem::mapFromScene(const QPainterPath
    &path) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapFromScene

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGraphicsItem::mapFromScene(const QPainterPath &path)
    #      const
    address = self._callAs(
        'QGraphicsItem',
        'ritual_ZNK13QGraphicsItem12mapFromSceneERK12QPainterPath',
        self._valueOf(path),
    )
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  @overload(float, float)
  def mapFromScene(self, x: float, y: float) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsItem::mapFromScene(qreal x, qreal y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapFromScene

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsItem::mapFromScene(qreal x, qreal y) const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem12mapFromSceneEdd', x, y,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(float, float, float, float)
  def mapFromScene(
      self,
      x: float,
      y: float,
      w: float,
      h: float,
  ) -> QPolygonF:
    """
    Calls Qt's 'QPolygonF QGraphicsItem::mapFromScene(qreal x, qreal y, qreal
    w, qreal h) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapFromScene

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.

    Returns
    -------

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  QPolygonF QGraphicsItem::mapFromScene(qreal x, qreal y, qreal w, qreal
    #      h) const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem12mapFromSceneEdddd',
        x, y, w, h,
    )
    from ..QtGui import QPolygonF
    return QPolygonF._cuteOwning(address)

  @overload(THIS, QRectF)
  @overload(NoneType, QRectF)
  def mapRectFromItem(
      self,
      item: Optional[QGraphicsItem],
      rect: QRectF,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsItem::mapRectFromItem(const QGraphicsItem
    *item, const QRectF &rect) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapRectFromItem

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

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsItem::mapRectFromItem(const QGraphicsItem *item, const
    #      QRectF &rect) const
    address = self._callAs(
        'QGraphicsItem',
        'ritual_ZNK13QGraphicsItem15mapRectFromItemEPKS_RK6QRectF',
        self._addressOf(item, 'QGraphicsItem'), self._valueOf(rect),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(THIS, float, float, float, float)
  @overload(NoneType, float, float, float, float)
  def mapRectFromItem(
      self,
      item: Optional[QGraphicsItem],
      x: float,
      y: float,
      w: float,
      h: float,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsItem::mapRectFromItem(const QGraphicsItem
    *item, qreal x, qreal y, qreal w, qreal h) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mapRectFromItem

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsItem::mapRectFromItem(const QGraphicsItem *item, qreal
    #      x, qreal y, qreal w, qreal h) const
    address = self._callAs(
        'QGraphicsItem',
        'ritual_ZNK13QGraphicsItem15mapRectFromItemEPKS_dddd',
        self._addressOf(item, 'QGraphicsItem'), x, y, w, h,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QRectF)
  def mapRectFromParent(self, rect: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsItem::mapRectFromParent(const QRectF &rect)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#mapRectFromParent

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
    #  QRectF QGraphicsItem::mapRectFromParent(const QRectF &rect) const
    address = self._callAs(
        'QGraphicsItem',
        'ritual_ZNK13QGraphicsItem17mapRectFromParentERK6QRectF',
        self._valueOf(rect),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(float, float, float, float)
  def mapRectFromParent(
      self,
      x: float,
      y: float,
      w: float,
      h: float,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsItem::mapRectFromParent(qreal x, qreal y,
    qreal w, qreal h) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#mapRectFromParent

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsItem::mapRectFromParent(qreal x, qreal y, qreal w,
    #      qreal h) const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem17mapRectFromParentEdddd',
        x, y, w, h,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QRectF)
  def mapRectFromScene(self, rect: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsItem::mapRectFromScene(const QRectF &rect)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#mapRectFromScene

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
    #  QRectF QGraphicsItem::mapRectFromScene(const QRectF &rect) const
    address = self._callAs(
        'QGraphicsItem',
        'ritual_ZNK13QGraphicsItem16mapRectFromSceneERK6QRectF',
        self._valueOf(rect),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(float, float, float, float)
  def mapRectFromScene(
      self,
      x: float,
      y: float,
      w: float,
      h: float,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsItem::mapRectFromScene(qreal x, qreal y,
    qreal w, qreal h) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#mapRectFromScene

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsItem::mapRectFromScene(qreal x, qreal y, qreal w,
    #      qreal h) const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem16mapRectFromSceneEdddd',
        x, y, w, h,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(THIS)
  @overload(NoneType)
  def isAncestorOf(self, child: Optional[QGraphicsItem]) -> bool:
    """
    Calls Qt's 'bool QGraphicsItem::isAncestorOf(const QGraphicsItem *child)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#isAncestorOf

    Parameters
    ----------

    child : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGraphicsItem::isAncestorOf(const QGraphicsItem *child) const
    return self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem12isAncestorOfEPKS_',
        self._addressOf(child, 'QGraphicsItem'),
    )

  @overload(THIS)
  @overload(NoneType)
  def commonAncestorItem(
      self,
      other: Optional[QGraphicsItem],
  ) -> Optional[QGraphicsItem]:
    """
    Calls Qt's 'QGraphicsItem *QGraphicsItem::commonAncestorItem(const
    QGraphicsItem *other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#commonAncestorItem

    Parameters
    ----------

    other : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QGraphicsItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsItem *QGraphicsItem::commonAncestorItem(const QGraphicsItem
    #      *other) const
    address = self._callAs(
        'QGraphicsItem',
        'ritual_ZNK13QGraphicsItem18commonAncestorItemEPKS_',
        self._addressOf(other, 'QGraphicsItem'),
    )
    return QGraphicsItem._cuteAt(address)

  def isUnderMouse(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsItem::isUnderMouse() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#isUnderMouse
    """
    #  bool QGraphicsItem::isUnderMouse() const
    return self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem12isUnderMouseEv',
    )

  @overload(int)
  def data(self, key: int) -> QVariant:
    """
    Calls Qt's 'QVariant QGraphicsItem::data(int key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#data

    Parameters
    ----------

    key : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QGraphicsItem::data(int key) const
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem4dataEi', key,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def inputMethodHints(self) -> Qt.InputMethodHints:
    """
    Calls Qt's 'Qt::InputMethodHints QGraphicsItem::inputMethodHints()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#inputMethodHints

    Returns
    -------

    Qt.InputMethodHints
      The value standing for the combination Qt gave back.
    """
    #  Qt::InputMethodHints QGraphicsItem::inputMethodHints() const
    return Qt.InputMethodHints(self._callAs(
        'QGraphicsItem', 'ritual_ZNK13QGraphicsItem16inputMethodHintsEv',
    ))

  def type(self) -> int:
    """
    Calls Qt's 'int QGraphicsItem::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#type
    """
    #  int QGraphicsItem::type() const
    ritual = 'ritual_ZNK13QGraphicsItem4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QGraphicsItem4typeEv'
    return self._callAs('QGraphicsItem', ritual)

  @overload(Qt.InputMethodQuery)
  def inputMethodQuery(self, query: Qt.InputMethodQuery) -> QVariant:
    """
    Calls Qt's 'QVariant QGraphicsItem::inputMethodQuery(Qt::InputMethodQuery
    query) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#inputMethodQuery

    Parameters
    ----------

    query : Qt.InputMethodQuery
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QGraphicsItem::inputMethodQuery(Qt::InputMethodQuery query)
    #      const
    address = self._callAs(
        'QGraphicsItem',
        'ritual_own_ZNK13QGraphicsItem16inputMethodQueryEN2Qt16InputMethodQ'
        'ueryE',
        query.value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QVariant)
  def extension(self, variant: QVariant) -> QVariant:
    """
    Calls Qt's 'QVariant QGraphicsItem::extension(const QVariant &variant)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#extension

    Parameters
    ----------

    variant : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QGraphicsItem::extension(const QVariant &variant) const
    address = self._callAs(
        'QGraphicsItem',
        'ritual_own_ZNK13QGraphicsItem9extensionERK8QVariant',
        self._valueOf(variant),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  @overload(NoneType)
  def setParentItem(self, parent: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setParentItem(QGraphicsItem *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#setParentItem

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItem::setParentItem(QGraphicsItem *parent)
    self._callAs(
        'QGraphicsItem', 'ritual_ZN13QGraphicsItem13setParentItemEPS_',
        self._addressOf(parent, 'QGraphicsItem'),
    )

  @overload(QGraphicsItemGroup)
  @overload(NoneType)
  def setGroup(self, group: Optional[QGraphicsItemGroup]) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setGroup(QGraphicsItemGroup *group)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#setGroup

    Parameters
    ----------

    group : Optional[QGraphicsItemGroup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItem::setGroup(QGraphicsItemGroup *group)
    self._callAs(
        'QGraphicsItem',
        'ritual_ZN13QGraphicsItem8setGroupEP18QGraphicsItemGroup',
        self._addressOf(group),
    )

  @overload(GraphicsItemFlag)
  @overload(GraphicsItemFlag, bool)
  def setFlag(self, flag: GraphicsItemFlag, enabled: bool = True) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setFlag(GraphicsItemFlag flag, bool
    enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#setFlag

    Parameters
    ----------

    flag : GraphicsItemFlag
      Passed on as its number.

    enabled : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QGraphicsItem::setFlag(GraphicsItemFlag flag, bool enabled)
    self._callAs(
        'QGraphicsItem',
        'ritual_ZN13QGraphicsItem7setFlagENS_16GraphicsItemFlagEb',
        flag.value, enabled,
    )

  @overload(GraphicsItemFlags)
  def setFlags(self, flags: GraphicsItemFlags) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setFlags(GraphicsItemFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#setFlags

    Parameters
    ----------

    flags : GraphicsItemFlags
      Passed on as its number.
    """
    #  void QGraphicsItem::setFlags(GraphicsItemFlags flags)
    self._callAs(
        'QGraphicsItem',
        'ritual_ZN13QGraphicsItem8setFlagsE6QFlagsINS_16GraphicsItemFlagEE',
        flags.value,
    )

  @overload(CacheMode)
  @overload(CacheMode, QSize)
  def setCacheMode(
      self,
      mode: CacheMode,
      cacheSize: Optional[QSize] = None,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setCacheMode(CacheMode mode, const QSize
    &cacheSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#setCacheMode

    Parameters
    ----------

    mode : CacheMode
      Passed on as its number.

    cacheSize : Optional[QSize]
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
      May be left out, as in Qt: a new 'QSize()' is then passed on.
    """
    #  void QGraphicsItem::setCacheMode(CacheMode mode, const QSize
    #      &cacheSize)
    if cacheSize is None:
      from ..QtCore import QSize
      cacheSize = QSize()
    self._callAs(
        'QGraphicsItem',
        'ritual_ZN13QGraphicsItem12setCacheModeENS_9CacheModeERK5QSize',
        mode.value, self._valueOf(cacheSize),
    )

  @overload(PanelModality)
  def setPanelModality(self, panelModality: PanelModality) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setPanelModality(PanelModality
    panelModality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#setPanelModality

    Parameters
    ----------

    panelModality : PanelModality
      Passed on as its number.
    """
    #  void QGraphicsItem::setPanelModality(PanelModality panelModality)
    self._callAs(
        'QGraphicsItem',
        'ritual_ZN13QGraphicsItem16setPanelModalityENS_13PanelModalityE',
        panelModality.value,
    )

  @overload(str)
  def setToolTip(self, toolTip: str) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setToolTip(const QString &toolTip)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#setToolTip

    Parameters
    ----------

    toolTip : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGraphicsItem::setToolTip(const QString &toolTip)
    self._callAs(
        'QGraphicsItem', 'ritual_ZN13QGraphicsItem10setToolTipERK7QString',
        toolTip,
    )

  @overload(QCursor)
  def setCursor(self, cursor: QCursor) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setCursor(const QCursor &cursor)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#setCursor

    Parameters
    ----------

    cursor : QCursor
      Passed on as a value: Qt reads the C++ QCursor, which stays Python's
      own.
    """
    #  void QGraphicsItem::setCursor(const QCursor &cursor)
    self._callAs(
        'QGraphicsItem', 'ritual_ZN13QGraphicsItem9setCursorERK7QCursor',
        self._valueOf(cursor),
    )

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QGraphicsItem::setVisible(bool visible)
    self._callAs(
        'QGraphicsItem', 'ritual_ZN13QGraphicsItem10setVisibleEb', visible,
    )

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setEnabled(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QGraphicsItem::setEnabled(bool enabled)
    self._callAs(
        'QGraphicsItem', 'ritual_ZN13QGraphicsItem10setEnabledEb', enabled,
    )

  @overload(bool)
  def setSelected(self, selected: bool) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setSelected(bool selected)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#setSelected

    Parameters
    ----------

    selected : bool
      Passed on as it is.
    """
    #  void QGraphicsItem::setSelected(bool selected)
    self._callAs(
        'QGraphicsItem', 'ritual_ZN13QGraphicsItem11setSelectedEb', selected,
    )

  @overload(bool)
  def setAcceptDrops(self, on: bool) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setAcceptDrops(bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#setAcceptDrops

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QGraphicsItem::setAcceptDrops(bool on)
    self._callAs(
        'QGraphicsItem', 'ritual_ZN13QGraphicsItem14setAcceptDropsEb', on,
    )

  @overload(float)
  def setOpacity(self, opacity: float) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setOpacity(qreal opacity)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#setOpacity

    Parameters
    ----------

    opacity : float
      Passed on as it is.
    """
    #  void QGraphicsItem::setOpacity(qreal opacity)
    self._callAs(
        'QGraphicsItem', 'ritual_ZN13QGraphicsItem10setOpacityEd', opacity,
    )

  @overload(QGraphicsEffect)
  @overload(NoneType)
  def setGraphicsEffect(self, effect: Optional[QGraphicsEffect]) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setGraphicsEffect(QGraphicsEffect
    *effect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#setGraphicsEffect

    Parameters
    ----------

    effect : Optional[QGraphicsEffect]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItem::setGraphicsEffect(QGraphicsEffect *effect)
    self._callAs(
        'QGraphicsItem',
        'ritual_ZN13QGraphicsItem17setGraphicsEffectEP15QGraphicsEffect',
        self._addressOf(effect),
    )

  @overload(Qt.MouseButtons)
  def setAcceptedMouseButtons(self, buttons: Qt.MouseButtons) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setAcceptedMouseButtons(Qt::MouseButtons
    buttons)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#setAcceptedMouseButtons

    Parameters
    ----------

    buttons : Qt.MouseButtons
      Passed on as its number.
    """
    #  void QGraphicsItem::setAcceptedMouseButtons(Qt::MouseButtons buttons)
    self._callAs(
        'QGraphicsItem',
        'ritual_ZN13QGraphicsItem23setAcceptedMouseButtonsE6QFlagsIN2Qt11Mo'
        'useButtonEE',
        buttons.value,
    )

  @overload(bool)
  def setAcceptHoverEvents(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setAcceptHoverEvents(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#setAcceptHoverEvents

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QGraphicsItem::setAcceptHoverEvents(bool enabled)
    self._callAs(
        'QGraphicsItem', 'ritual_ZN13QGraphicsItem20setAcceptHoverEventsEb',
        enabled,
    )

  @overload(bool)
  def setAcceptTouchEvents(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setAcceptTouchEvents(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#setAcceptTouchEvents

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QGraphicsItem::setAcceptTouchEvents(bool enabled)
    self._callAs(
        'QGraphicsItem', 'ritual_ZN13QGraphicsItem20setAcceptTouchEventsEb',
        enabled,
    )

  @overload(bool)
  def setFiltersChildEvents(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setFiltersChildEvents(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#setFiltersChildEvents

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QGraphicsItem::setFiltersChildEvents(bool enabled)
    self._callAs(
        'QGraphicsItem', 'ritual_ZN13QGraphicsItem21setFiltersChildEventsEb',
        enabled,
    )

  @overload(bool)
  def setHandlesChildEvents(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setHandlesChildEvents(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#setHandlesChildEvents

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QGraphicsItem::setHandlesChildEvents(bool enabled)
    self._callAs(
        'QGraphicsItem', 'ritual_ZN13QGraphicsItem21setHandlesChildEventsEb',
        enabled,
    )

  @overload(bool)
  def setActive(self, active: bool) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setActive(bool active)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#setActive

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QGraphicsItem::setActive(bool active)
    self._callAs(
        'QGraphicsItem', 'ritual_ZN13QGraphicsItem9setActiveEb', active,
    )

  @overload()
  @overload(Qt.FocusReason)
  def setFocus(
      self,
      focusReason: Qt.FocusReason = Qt.FocusReason.OtherFocusReason,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setFocus(Qt::FocusReason focusReason)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#setFocus

    Parameters
    ----------

    focusReason : Qt.FocusReason
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.FocusReason.OtherFocusReason.
    """
    #  void QGraphicsItem::setFocus(Qt::FocusReason focusReason)
    self._callAs(
        'QGraphicsItem',
        'ritual_ZN13QGraphicsItem8setFocusEN2Qt11FocusReasonE',
        focusReason.value,
    )

  @overload(THIS)
  @overload(NoneType)
  def setFocusProxy(self, item: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setFocusProxy(QGraphicsItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#setFocusProxy

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItem::setFocusProxy(QGraphicsItem *item)
    self._callAs(
        'QGraphicsItem', 'ritual_ZN13QGraphicsItem13setFocusProxyEPS_',
        self._addressOf(item, 'QGraphicsItem'),
    )

  @overload(float)
  def setX(self, x: float) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setX(qreal x)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#setX

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QGraphicsItem::setX(qreal x)
    self._callAs('QGraphicsItem', 'ritual_ZN13QGraphicsItem4setXEd', x)

  @overload(float)
  def setY(self, y: float) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setY(qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#setY

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QGraphicsItem::setY(qreal y)
    self._callAs('QGraphicsItem', 'ritual_ZN13QGraphicsItem4setYEd', y)

  @overload(QPointF)
  def setPos(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setPos(const QPointF &pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#setPos

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphicsItem::setPos(const QPointF &pos)
    self._callAs(
        'QGraphicsItem', 'ritual_ZN13QGraphicsItem6setPosERK7QPointF',
        self._valueOf(pos),
    )

  @overload(float, float)
  def setPos(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setPos(qreal x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#setPos

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QGraphicsItem::setPos(qreal x, qreal y)
    self._callAs('QGraphicsItem', 'ritual_ZN13QGraphicsItem6setPosEdd', x, y)

  @overload(QTransform)
  @overload(QTransform, bool)
  def setTransform(self, matrix: QTransform, combine: bool = False) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setTransform(const QTransform &matrix,
    bool combine)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#setTransform

    Parameters
    ----------

    matrix : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.

    combine : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QGraphicsItem::setTransform(const QTransform &matrix, bool
    #      combine)
    self._callAs(
        'QGraphicsItem',
        'ritual_ZN13QGraphicsItem12setTransformERK10QTransformb',
        self._valueOf(matrix), combine,
    )

  @overload(float)
  def setRotation(self, angle: float) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setRotation(qreal angle)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#setRotation

    Parameters
    ----------

    angle : float
      Passed on as it is.
    """
    #  void QGraphicsItem::setRotation(qreal angle)
    self._callAs(
        'QGraphicsItem', 'ritual_ZN13QGraphicsItem11setRotationEd', angle,
    )

  @overload(float)
  def setScale(self, scale: float) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setScale(qreal scale)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#setScale

    Parameters
    ----------

    scale : float
      Passed on as it is.
    """
    #  void QGraphicsItem::setScale(qreal scale)
    self._callAs(
        'QGraphicsItem', 'ritual_ZN13QGraphicsItem8setScaleEd', scale,
    )

  @overload(QPointF)
  def setTransformOriginPoint(self, origin: QPointF) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setTransformOriginPoint(const QPointF
    &origin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#setTransformOriginPoint

    Parameters
    ----------

    origin : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphicsItem::setTransformOriginPoint(const QPointF &origin)
    self._callAs(
        'QGraphicsItem',
        'ritual_ZN13QGraphicsItem23setTransformOriginPointERK7QPointF',
        self._valueOf(origin),
    )

  @overload(float, float)
  def setTransformOriginPoint(self, ax: float, ay: float) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setTransformOriginPoint(qreal ax, qreal
    ay)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#setTransformOriginPoint

    Parameters
    ----------

    ax : float
      Passed on as it is.

    ay : float
      Passed on as it is.
    """
    #  void QGraphicsItem::setTransformOriginPoint(qreal ax, qreal ay)
    self._callAs(
        'QGraphicsItem',
        'ritual_ZN13QGraphicsItem23setTransformOriginPointEdd',
        ax, ay,
    )

  @overload(float)
  def setZValue(self, z: float) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setZValue(qreal z)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#setZValue

    Parameters
    ----------

    z : float
      Passed on as it is.
    """
    #  void QGraphicsItem::setZValue(qreal z)
    self._callAs('QGraphicsItem', 'ritual_ZN13QGraphicsItem9setZValueEd', z)

  @overload(float)
  def setBoundingRegionGranularity(self, granularity: float) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setBoundingRegionGranularity(qreal
    granularity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#setBoundingRegionGranularity

    Parameters
    ----------

    granularity : float
      Passed on as it is.
    """
    #  void QGraphicsItem::setBoundingRegionGranularity(qreal granularity)
    self._callAs(
        'QGraphicsItem',
        'ritual_ZN13QGraphicsItem28setBoundingRegionGranularityEd',
        granularity,
    )

  @overload(int, QVariant)
  def setData(self, key: int, value: QVariant) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setData(int key, const QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#setData

    Parameters
    ----------

    key : int
      Passed on as it is.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QGraphicsItem::setData(int key, const QVariant &value)
    self._callAs(
        'QGraphicsItem', 'ritual_ZN13QGraphicsItem7setDataEiRK8QVariant',
        key, self._valueOf(value),
    )

  @overload(Qt.InputMethodHints)
  def setInputMethodHints(self, hints: Qt.InputMethodHints) -> None:
    """
    Calls Qt's 'void QGraphicsItem::setInputMethodHints(Qt::InputMethodHints
    hints)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#setInputMethodHints

    Parameters
    ----------

    hints : Qt.InputMethodHints
      Passed on as its number.
    """
    #  void QGraphicsItem::setInputMethodHints(Qt::InputMethodHints hints)
    self._callAs(
        'QGraphicsItem',
        'ritual_ZN13QGraphicsItem19setInputMethodHintsE6QFlagsIN2Qt15InputM'
        'ethodHintEE',
        hints.value,
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

  def toGraphicsObject(self) -> Optional[QGraphicsObject]:
    """
    Calls Qt's 'QGraphicsObject *QGraphicsItem::toGraphicsObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#toGraphicsObject

    Returns
    -------

    Optional[QGraphicsObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsObject *QGraphicsItem::toGraphicsObject()
    address = self._callAs(
        'QGraphicsItem', 'ritual_ZN13QGraphicsItem16toGraphicsObjectEv',
    )
    from . import QGraphicsObject
    return QGraphicsObject._cuteAt(address)

  def unsetCursor(self) -> None:
    """
    Calls Qt's 'void QGraphicsItem::unsetCursor()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#unsetCursor
    """
    #  void QGraphicsItem::unsetCursor()
    self._callAs('QGraphicsItem', 'ritual_ZN13QGraphicsItem11unsetCursorEv')

  def hide(self) -> None:
    """
    Calls Qt's 'void QGraphicsItem::hide()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#hide
    """
    #  void QGraphicsItem::hide()
    self._callAs('QGraphicsItem', 'ritual_ZN13QGraphicsItem4hideEv')

  def show(self) -> None:
    """
    Calls Qt's 'void QGraphicsItem::show()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#show
    """
    #  void QGraphicsItem::show()
    self._callAs('QGraphicsItem', 'ritual_ZN13QGraphicsItem4showEv')

  def clearFocus(self) -> None:
    """
    Calls Qt's 'void QGraphicsItem::clearFocus()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#clearFocus
    """
    #  void QGraphicsItem::clearFocus()
    self._callAs('QGraphicsItem', 'ritual_ZN13QGraphicsItem10clearFocusEv')

  def grabMouse(self) -> None:
    """
    Calls Qt's 'void QGraphicsItem::grabMouse()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#grabMouse
    """
    #  void QGraphicsItem::grabMouse()
    self._callAs('QGraphicsItem', 'ritual_ZN13QGraphicsItem9grabMouseEv')

  def ungrabMouse(self) -> None:
    """
    Calls Qt's 'void QGraphicsItem::ungrabMouse()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#ungrabMouse
    """
    #  void QGraphicsItem::ungrabMouse()
    self._callAs('QGraphicsItem', 'ritual_ZN13QGraphicsItem11ungrabMouseEv')

  def grabKeyboard(self) -> None:
    """
    Calls Qt's 'void QGraphicsItem::grabKeyboard()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#grabKeyboard
    """
    #  void QGraphicsItem::grabKeyboard()
    self._callAs('QGraphicsItem', 'ritual_ZN13QGraphicsItem12grabKeyboardEv')

  def ungrabKeyboard(self) -> None:
    """
    Calls Qt's 'void QGraphicsItem::ungrabKeyboard()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#ungrabKeyboard
    """
    #  void QGraphicsItem::ungrabKeyboard()
    self._callAs(
        'QGraphicsItem', 'ritual_ZN13QGraphicsItem14ungrabKeyboardEv',
    )

  @overload(float, float)
  def moveBy(self, dx: float, dy: float) -> None:
    """
    Calls Qt's 'void QGraphicsItem::moveBy(qreal dx, qreal dy)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#moveBy

    Parameters
    ----------

    dx : float
      Passed on as it is.

    dy : float
      Passed on as it is.
    """
    #  void QGraphicsItem::moveBy(qreal dx, qreal dy)
    self._callAs(
        'QGraphicsItem', 'ritual_ZN13QGraphicsItem6moveByEdd', dx, dy,
    )

  @overload()
  @overload(QRectF)
  @overload(QRectF, int)
  @overload(QRectF, int, int)
  def ensureVisible(
      self,
      rect: Optional[QRectF] = None,
      xmargin: int = 50,
      ymargin: int = 50,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsItem::ensureVisible(const QRectF &rect, int
    xmargin, int ymargin)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#ensureVisible

    Parameters
    ----------

    rect : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.

    xmargin : int
      Passed on as it is. May be left out, as in Qt: it is then 50.

    ymargin : int
      Passed on as it is. May be left out, as in Qt: it is then 50.
    """
    #  void QGraphicsItem::ensureVisible(const QRectF &rect, int xmargin, int
    #      ymargin)
    if rect is None:
      from ..QtCore import QRectF
      rect = QRectF()
    self._callAs(
        'QGraphicsItem',
        'ritual_ZN13QGraphicsItem13ensureVisibleERK6QRectFii',
        self._valueOf(rect), xmargin, ymargin,
    )

  @overload(float, float, float, float)
  @overload(float, float, float, float, int)
  @overload(float, float, float, float, int, int)
  def ensureVisible(
      self,
      x: float,
      y: float,
      w: float,
      h: float,
      xmargin: int = 50,
      ymargin: int = 50,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsItem::ensureVisible(qreal x, qreal y, qreal w,
    qreal h, int xmargin, int ymargin)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#ensureVisible

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.

    xmargin : int
      Passed on as it is. May be left out, as in Qt: it is then 50.

    ymargin : int
      Passed on as it is. May be left out, as in Qt: it is then 50.
    """
    #  void QGraphicsItem::ensureVisible(qreal x, qreal y, qreal w, qreal h,
    #      int xmargin, int ymargin)
    self._callAs(
        'QGraphicsItem', 'ritual_ZN13QGraphicsItem13ensureVisibleEddddii',
        x, y, w, h, xmargin, ymargin,
    )

  def resetTransform(self) -> None:
    """
    Calls Qt's 'void QGraphicsItem::resetTransform()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#resetTransform
    """
    #  void QGraphicsItem::resetTransform()
    self._callAs(
        'QGraphicsItem', 'ritual_ZN13QGraphicsItem14resetTransformEv',
    )

  @overload(int)
  def advance(self, phase: int) -> None:
    """
    Calls Qt's 'void QGraphicsItem::advance(int phase)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#advance

    Parameters
    ----------

    phase : int
      Passed on as it is.
    """
    #  void QGraphicsItem::advance(int phase)
    ritual = 'ritual_ZN13QGraphicsItem7advanceEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QGraphicsItem7advanceEi'
    self._callAs('QGraphicsItem', ritual, phase)

  @overload(THIS)
  @overload(NoneType)
  def stackBefore(self, sibling: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void QGraphicsItem::stackBefore(const QGraphicsItem
    *sibling)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#stackBefore

    Parameters
    ----------

    sibling : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItem::stackBefore(const QGraphicsItem *sibling)
    self._callAs(
        'QGraphicsItem', 'ritual_ZN13QGraphicsItem11stackBeforeEPKS_',
        self._addressOf(sibling, 'QGraphicsItem'),
    )

  @overload(QPainter, QStyleOptionGraphicsItem)
  @overload(QPainter, NoneType)
  @overload(NoneType, QStyleOptionGraphicsItem)
  @overload(NoneType, NoneType)
  @overload(QPainter, QStyleOptionGraphicsItem, QWidget)
  @overload(QPainter, QStyleOptionGraphicsItem, NoneType)
  @overload(QPainter, NoneType, QWidget)
  @overload(QPainter, NoneType, NoneType)
  @overload(NoneType, QStyleOptionGraphicsItem, QWidget)
  @overload(NoneType, QStyleOptionGraphicsItem, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  def paint(
      self,
      painter: Optional[QPainter],
      option: Optional[QStyleOptionGraphicsItem],
      widget: Optional[QWidget] = None,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsItem::paint(QPainter *painter, const
    QStyleOptionGraphicsItem *option, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#paint

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    option : Optional[QStyleOptionGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QGraphicsItem::paint(QPainter *painter, const
    #      QStyleOptionGraphicsItem *option, QWidget *widget)
    self._callAs(
        'QGraphicsItem',
        'ritual_ZN13QGraphicsItem5paintEP8QPainterPK24QStyleOptionGraphicsI'
        'temP7QWidget',
        self._addressOf(painter), self._addressOf(option),
        self._addressOf(widget),
    )

  @overload()
  @overload(QRectF)
  def update(self, rect: Optional[QRectF] = None) -> None:
    """
    Calls Qt's 'void QGraphicsItem::update(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#update

    Parameters
    ----------

    rect : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.
    """
    #  void QGraphicsItem::update(const QRectF &rect)
    if rect is None:
      from ..QtCore import QRectF
      rect = QRectF()
    self._callAs(
        'QGraphicsItem', 'ritual_ZN13QGraphicsItem6updateERK6QRectF',
        self._valueOf(rect),
    )

  @overload(float, float, float, float)
  def update(self, x: float, y: float, width: float, height: float) -> None:
    """
    Calls Qt's 'void QGraphicsItem::update(qreal x, qreal y, qreal width,
    qreal height)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#update

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    width : float
      Passed on as it is.

    height : float
      Passed on as it is.
    """
    #  void QGraphicsItem::update(qreal x, qreal y, qreal width, qreal
    #      height)
    self._callAs(
        'QGraphicsItem', 'ritual_ZN13QGraphicsItem6updateEdddd',
        x, y, width, height,
    )

  @overload(float, float)
  @overload(float, float, QRectF)
  def scroll(
      self,
      dx: float,
      dy: float,
      rect: Optional[QRectF] = None,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsItem::scroll(qreal dx, qreal dy, const QRectF
    &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#scroll

    Parameters
    ----------

    dx : float
      Passed on as it is.

    dy : float
      Passed on as it is.

    rect : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.
    """
    #  void QGraphicsItem::scroll(qreal dx, qreal dy, const QRectF &rect)
    if rect is None:
      from ..QtCore import QRectF
      rect = QRectF()
    self._callAs(
        'QGraphicsItem', 'ritual_ZN13QGraphicsItem6scrollEddRK6QRectF',
        dx, dy, self._valueOf(rect),
    )

  @overload(THIS)
  @overload(NoneType)
  def installSceneEventFilter(
      self,
      filterItem: Optional[QGraphicsItem],
  ) -> None:
    """
    Calls Qt's 'void QGraphicsItem::installSceneEventFilter(QGraphicsItem
    *filterItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#installSceneEventFilter

    Parameters
    ----------

    filterItem : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItem::installSceneEventFilter(QGraphicsItem *filterItem)
    self._callAs(
        'QGraphicsItem',
        'ritual_ZN13QGraphicsItem23installSceneEventFilterEPS_',
        self._addressOf(filterItem, 'QGraphicsItem'),
    )

  @overload(THIS)
  @overload(NoneType)
  def removeSceneEventFilter(
      self,
      filterItem: Optional[QGraphicsItem],
  ) -> None:
    """
    Calls Qt's 'void QGraphicsItem::removeSceneEventFilter(QGraphicsItem
    *filterItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#removeSceneEventFilter

    Parameters
    ----------

    filterItem : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItem::removeSceneEventFilter(QGraphicsItem *filterItem)
    self._callAs(
        'QGraphicsItem',
        'ritual_ZN13QGraphicsItem22removeSceneEventFilterEPS_',
        self._addressOf(filterItem, 'QGraphicsItem'),
    )

  @overload(THIS, QEvent)
  @overload(THIS, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def sceneEventFilter(
      self,
      watched: Optional[QGraphicsItem],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QGraphicsItem::sceneEventFilter(QGraphicsItem *watched,
    QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#sceneEventFilter

    Parameters
    ----------

    watched : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGraphicsItem::sceneEventFilter(QGraphicsItem *watched, QEvent
    #      *event)
    return self._callAs(
        'QGraphicsItem',
        'ritual_own_ZN13QGraphicsItem16sceneEventFilterEPS_P6QEvent',
        self._addressOf(watched, 'QGraphicsItem'), self._addressOf(event),
    )

  @overload(QEvent)
  @overload(NoneType)
  def sceneEvent(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QGraphicsItem::sceneEvent(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#sceneEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGraphicsItem::sceneEvent(QEvent *event)
    return self._callAs(
        'QGraphicsItem', 'ritual_own_ZN13QGraphicsItem10sceneEventEP6QEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneContextMenuEvent)
  @overload(NoneType)
  def contextMenuEvent(
      self,
      event: Optional[QGraphicsSceneContextMenuEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsItem::contextMenuEvent(QGraphicsSceneContextMenuEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#contextMenuEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneContextMenuEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItem::contextMenuEvent(QGraphicsSceneContextMenuEvent
    #      *event)
    self._callAs(
        'QGraphicsItem',
        'ritual_own_ZN13QGraphicsItem16contextMenuEventEP30QGraphicsSceneCo'
        'ntextMenuEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneDragDropEvent)
  @overload(NoneType)
  def dragEnterEvent(
      self,
      event: Optional[QGraphicsSceneDragDropEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsItem::dragEnterEvent(QGraphicsSceneDragDropEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#dragEnterEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneDragDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItem::dragEnterEvent(QGraphicsSceneDragDropEvent *event)
    self._callAs(
        'QGraphicsItem',
        'ritual_own_ZN13QGraphicsItem14dragEnterEventEP27QGraphicsSceneDrag'
        'DropEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneDragDropEvent)
  @overload(NoneType)
  def dragLeaveEvent(
      self,
      event: Optional[QGraphicsSceneDragDropEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsItem::dragLeaveEvent(QGraphicsSceneDragDropEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#dragLeaveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneDragDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItem::dragLeaveEvent(QGraphicsSceneDragDropEvent *event)
    self._callAs(
        'QGraphicsItem',
        'ritual_own_ZN13QGraphicsItem14dragLeaveEventEP27QGraphicsSceneDrag'
        'DropEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneDragDropEvent)
  @overload(NoneType)
  def dragMoveEvent(
      self,
      event: Optional[QGraphicsSceneDragDropEvent],
  ) -> None:
    """
    Calls Qt's 'void QGraphicsItem::dragMoveEvent(QGraphicsSceneDragDropEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#dragMoveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneDragDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItem::dragMoveEvent(QGraphicsSceneDragDropEvent *event)
    self._callAs(
        'QGraphicsItem',
        'ritual_own_ZN13QGraphicsItem13dragMoveEventEP27QGraphicsSceneDragD'
        'ropEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneDragDropEvent)
  @overload(NoneType)
  def dropEvent(self, event: Optional[QGraphicsSceneDragDropEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsItem::dropEvent(QGraphicsSceneDragDropEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#dropEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneDragDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItem::dropEvent(QGraphicsSceneDragDropEvent *event)
    self._callAs(
        'QGraphicsItem',
        'ritual_own_ZN13QGraphicsItem9dropEventEP27QGraphicsSceneDragDropEv'
        'ent',
        self._addressOf(event),
    )

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsItem::focusInEvent(QFocusEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#focusInEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItem::focusInEvent(QFocusEvent *event)
    self._callAs(
        'QGraphicsItem',
        'ritual_own_ZN13QGraphicsItem12focusInEventEP11QFocusEvent',
        self._addressOf(event),
    )

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsItem::focusOutEvent(QFocusEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#focusOutEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItem::focusOutEvent(QFocusEvent *event)
    self._callAs(
        'QGraphicsItem',
        'ritual_own_ZN13QGraphicsItem13focusOutEventEP11QFocusEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverEnterEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void QGraphicsItem::hoverEnterEvent(QGraphicsSceneHoverEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#hoverEnterEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
    self._callAs(
        'QGraphicsItem',
        'ritual_own_ZN13QGraphicsItem15hoverEnterEventEP24QGraphicsSceneHov'
        'erEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverMoveEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void QGraphicsItem::hoverMoveEvent(QGraphicsSceneHoverEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#hoverMoveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItem::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
    self._callAs(
        'QGraphicsItem',
        'ritual_own_ZN13QGraphicsItem14hoverMoveEventEP24QGraphicsSceneHove'
        'rEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverLeaveEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void QGraphicsItem::hoverLeaveEvent(QGraphicsSceneHoverEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#hoverLeaveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
    self._callAs(
        'QGraphicsItem',
        'ritual_own_ZN13QGraphicsItem15hoverLeaveEventEP24QGraphicsSceneHov'
        'erEvent',
        self._addressOf(event),
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsItem::keyPressEvent(QKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#keyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItem::keyPressEvent(QKeyEvent *event)
    self._callAs(
        'QGraphicsItem',
        'ritual_own_ZN13QGraphicsItem13keyPressEventEP9QKeyEvent',
        self._addressOf(event),
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsItem::keyReleaseEvent(QKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#keyReleaseEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItem::keyReleaseEvent(QKeyEvent *event)
    self._callAs(
        'QGraphicsItem',
        'ritual_own_ZN13QGraphicsItem15keyReleaseEventEP9QKeyEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mousePressEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void QGraphicsItem::mousePressEvent(QGraphicsSceneMouseEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
    self._callAs(
        'QGraphicsItem',
        'ritual_own_ZN13QGraphicsItem15mousePressEventEP24QGraphicsSceneMou'
        'seEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void QGraphicsItem::mouseMoveEvent(QGraphicsSceneMouseEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItem::mouseMoveEvent(QGraphicsSceneMouseEvent *event)
    self._callAs(
        'QGraphicsItem',
        'ritual_own_ZN13QGraphicsItem14mouseMoveEventEP24QGraphicsSceneMous'
        'eEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsItem::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItem::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)
    self._callAs(
        'QGraphicsItem',
        'ritual_own_ZN13QGraphicsItem17mouseReleaseEventEP24QGraphicsSceneM'
        'ouseEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#mouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
    #      *event)
    self._callAs(
        'QGraphicsItem',
        'ritual_own_ZN13QGraphicsItem21mouseDoubleClickEventEP24QGraphicsSc'
        'eneMouseEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, event: Optional[QGraphicsSceneWheelEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsItem::wheelEvent(QGraphicsSceneWheelEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#wheelEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItem::wheelEvent(QGraphicsSceneWheelEvent *event)
    self._callAs(
        'QGraphicsItem',
        'ritual_own_ZN13QGraphicsItem10wheelEventEP24QGraphicsSceneWheelEve'
        'nt',
        self._addressOf(event),
    )

  @overload(QInputMethodEvent)
  @overload(NoneType)
  def inputMethodEvent(self, event: Optional[QInputMethodEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsItem::inputMethodEvent(QInputMethodEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitem.html#inputMethodEvent

    Parameters
    ----------

    event : Optional[QInputMethodEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItem::inputMethodEvent(QInputMethodEvent *event)
    self._callAs(
        'QGraphicsItem',
        'ritual_own_ZN13QGraphicsItem16inputMethodEventEP17QInputMethodEven'
        't',
        self._addressOf(event),
    )

  @overload(GraphicsItemChange, QVariant)
  def itemChange(
      self,
      change: GraphicsItemChange,
      value: QVariant,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QGraphicsItem::itemChange(GraphicsItemChange change,
    const QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitem.html#itemChange

    Parameters
    ----------

    change : GraphicsItemChange
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QGraphicsItem::itemChange(GraphicsItemChange change, const
    #      QVariant &value)
    address = self._callAs(
        'QGraphicsItem',
        'ritual_own_ZN13QGraphicsItem10itemChangeENS_18GraphicsItemChangeER'
        'K8QVariant',
        change.value, self._valueOf(value),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)
