"""
QQuickItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qquickitem.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QObject
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject, QPointF, QRectF, QSize, QSizeF
  from ..QtCore import QVariant
  from ..QtGui import QCursor, QDragEnterEvent, QDragLeaveEvent
  from ..QtGui import QDragMoveEvent, QDropEvent, QFocusEvent, QHoverEvent
  from ..QtGui import QInputMethodEvent, QKeyEvent, QMouseEvent, QTouchEvent
  from ..QtGui import QWheelEvent
  from ..QtQml import QJSValue, QQmlV4Function
  from . import QQuickItemPrivate, QQuickWindow, QSGNode, QSGTextureProvider
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCursor = WAIT['QCursor']
  QDragEnterEvent = WAIT['QDragEnterEvent']
  QDragLeaveEvent = WAIT['QDragLeaveEvent']
  QDragMoveEvent = WAIT['QDragMoveEvent']
  QDropEvent = WAIT['QDropEvent']
  QEvent = WAIT['QEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QHoverEvent = WAIT['QHoverEvent']
  QInputMethodEvent = WAIT['QInputMethodEvent']
  QJSValue = WAIT['QJSValue']
  QKeyEvent = WAIT['QKeyEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QPointF = WAIT['QPointF']
  QQmlV4Function = WAIT['QQmlV4Function']
  QQuickWindow = WAIT['QQuickWindow']
  QRectF = WAIT['QRectF']
  QSGNode = WAIT['QSGNode']
  QSize = WAIT['QSize']
  QSizeF = WAIT['QSizeF']
  QTouchEvent = WAIT['QTouchEvent']
  QWheelEvent = WAIT['QWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickItem(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QQuickItem: a plain Python object standing in front
  of one C++ QQuickItem.

  It is built on the cute 'QObject', as Qt's QQuickItem is built on Qt's
  QObject, and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's QQuickItem is built on Qt's
  QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickItem that has a ritual and that Python can
  call so far, 181 names in all: 'metaObject', 'tr', 'window', 'parentItem',
  'setParentItem', 'stackBefore', 'stackAfter', 'childrenRect', 'childItems',
  'clip', 'setClip', 'state', 'setState', 'baselineOffset',
  'setBaselineOffset', 'x', 'y', 'position', 'setX', 'setY', 'setPosition',
  'width', 'setWidth', 'resetWidth', 'setImplicitWidth', 'implicitWidth',
  'height', 'setHeight', 'resetHeight', 'setImplicitHeight',
  'implicitHeight', 'size', 'setSize', 'transformOrigin',
  'setTransformOrigin', 'transformOriginPoint', 'setTransformOriginPoint',
  'z', 'setZ', 'rotation', 'setRotation', 'scale', 'setScale', 'opacity',
  'setOpacity', 'isVisible', 'setVisible', 'isEnabled', 'setEnabled',
  'smooth', 'setSmooth', 'activeFocusOnTab', 'setActiveFocusOnTab',
  'antialiasing', 'setAntialiasing', 'resetAntialiasing', 'flags', 'setFlag',
  'setFlags', 'boundingRect', 'clipRect', 'viewportItem', 'hasActiveFocus',
  'hasFocus', 'setFocus', 'isFocusScope', 'scopedFocusItem', 'focusPolicy',
  'setFocusPolicy', 'isAncestorOf', 'acceptedMouseButtons',
  'setAcceptedMouseButtons', 'acceptHoverEvents', 'setAcceptHoverEvents',
  'acceptTouchEvents', 'setAcceptTouchEvents', 'cursor', 'setCursor',
  'unsetCursor', 'isUnderMouse', 'grabMouse', 'ungrabMouse', 'keepMouseGrab',
  'setKeepMouseGrab', 'filtersChildMouseEvents',
  'setFiltersChildMouseEvents', 'ungrabTouchPoints', 'keepTouchGrab',
  'setKeepTouchGrab', 'grabToImage', 'contains', 'containmentMask',
  'setContainmentMask', 'mapToScene', 'mapRectToItem', 'mapRectToScene',
  'mapFromScene', 'mapRectFromItem', 'mapRectFromScene', 'polish',
  'mapFromItem', 'mapToItem', 'mapFromGlobal', 'mapToGlobal',
  'forceActiveFocus', 'nextItemInFocusChain', 'childAt', 'ensurePolished',
  'dumpItemTree', 'inputMethodQuery', 'isTextureProvider', 'textureProvider',
  'setMutabilityGroup', 'mutabilityGroup', 'update', 'childrenRectChanged',
  'baselineOffsetChanged', 'stateChanged', 'focusChanged',
  'activeFocusChanged', 'focusPolicyChanged', 'activeFocusOnTabChanged',
  'parentChanged', 'transformOriginChanged', 'smoothChanged',
  'antialiasingChanged', 'clipChanged', 'windowChanged', 'childrenChanged',
  'opacityChanged', 'enabledChanged', 'visibleChanged',
  'visibleChildrenChanged', 'rotationChanged', 'scaleChanged', 'xChanged',
  'yChanged', 'widthChanged', 'heightChanged', 'zChanged',
  'implicitWidthChanged', 'implicitHeightChanged', 'containmentMaskChanged',
  'paletteChanged', 'paletteCreated', 'mutabilityGroupChanged', 'event',
  'isComponentComplete', 'itemChange', 'geometryChange', 'updateInputMethod',
  'widthValid', 'heightValid', 'setImplicitSize', 'classBegin',
  'componentComplete', 'keyPressEvent', 'keyReleaseEvent',
  'inputMethodEvent', 'focusInEvent', 'focusOutEvent', 'mousePressEvent',
  'mouseMoveEvent', 'mouseReleaseEvent', 'mouseDoubleClickEvent',
  'mouseUngrabEvent', 'touchUngrabEvent', 'wheelEvent', 'touchEvent',
  'hoverEnterEvent', 'hoverMoveEvent', 'hoverLeaveEvent', 'dragEnterEvent',
  'dragMoveEvent', 'dragLeaveEvent', 'dropEvent', 'childMouseEventFilter',
  'updatePaintNode', 'releaseResources', 'updatePolish', 'd_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickItem::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickItem::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickItem::~QQuickItem()': the destructor: Python never removes a
    C++ QQuickItem.
  - Qt's 'QQmlListProperty<QQuickTransform> QQuickItem::transform()': gives a
    type Python has no way to take yet.
  - Qt's 'QBindable<qreal> QQuickItem::bindableX()': gives a type Python has
    no way to take yet.
  - Qt's 'QBindable<qreal> QQuickItem::bindableY()': gives a type Python has
    no way to take yet.
  - Qt's 'QBindable<qreal> QQuickItem::bindableWidth()': gives a type Python
    has no way to take yet.
  - Qt's 'QBindable<qreal> QQuickItem::bindableHeight()': gives a type Python
    has no way to take yet.
  - Qt's 'void QQuickItem::grabTouchPoints(const QList<int> &ids)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QSharedPointer<QQuickItemGrabResult> QQuickItem::grabToImage(const
    QSize &targetSize)': gives a type Python has no way to take yet.
  - Qt's 'QTransform QQuickItem::itemTransform(QQuickItem *a0, bool *a1)
    const': takes a number to change where it is.
  - Qt's 'QQuickItem::QQuickItem(QQuickItemPrivate &dd, QQuickItem *parent)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QDebug operator<<(QDebug debug, QQuickItem *item)': an operator
    between other classes, written inside this one.
  - Qt's 'const QQuickItemPrivate *QQuickItem::d_func() const': takes in
    Python what 'QQuickItemPrivate *QQuickItem::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 214 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickItem is created at the first use, not by 'QQuickItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickItem.
  - Qt tells when it has removed the C++ QQuickItem. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QQuickItem that has no cute function yet,
    'bindableHeight', 'bindableWidth', 'bindableX', 'bindableY',
    'grabTouchPoints', 'itemTransform', 'transform', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickItem, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Flag(CuteFlags):
    """
    The flags enum 'QQuickItem::Flag' of Qt, with the 7 names Qt gives in it.
    Qt names the type of its combinations 'QQuickItem::Flags'.
    """

    ItemClipsChildrenToShape = 0x1
    ItemAcceptsInputMethod = 0x2
    ItemIsFocusScope = 0x4
    ItemHasContents = 0x8
    ItemAcceptsDrops = 0x10
    ItemIsViewport = 0x20
    ItemObservesViewport = 0x40

  Flags = Flag

  class ItemChange(CuteNum):
    """
    The enum 'QQuickItem::ItemChange' of Qt, with the 13 names Qt gives in
    it.
    """

    ItemChildAddedChange = Kee[int](0)
    ItemChildRemovedChange = Kee[int](1)
    ItemSceneChange = Kee[int](2)
    ItemVisibleHasChanged = Kee[int](3)
    ItemParentHasChanged = Kee[int](4)
    ItemOpacityHasChanged = Kee[int](5)
    ItemActiveFocusHasChanged = Kee[int](6)
    ItemRotationHasChanged = Kee[int](7)
    ItemAntialiasingHasChanged = Kee[int](8)
    ItemDevicePixelRatioHasChanged = Kee[int](9)
    ItemEnabledHasChanged = Kee[int](10)
    ItemScaleHasChanged = Kee[int](11)
    ItemTransformHasChanged = Kee[int](12)

  class MutabilityGroup(CuteNum):
    """
    The enum 'QQuickItem::MutabilityGroup' of Qt, with the 4 names Qt gives
    in it.
    """

    AutoMutabilityGroup = Kee[int](0)
    StaticMutabilityGroup = Kee[int](1)
    ModerateMutabilityGroup = Kee[int](8)
    DynamicMutabilityGroup = Kee[int](15)

  class TransformOrigin(CuteNum):
    """
    The enum 'QQuickItem::TransformOrigin' of Qt, with the 9 names Qt gives
    in it.
    """

    TopLeft = Kee[int](0)
    Top = Kee[int](1)
    TopRight = Kee[int](2)
    Left = Kee[int](3)
    Center = Kee[int](4)
    Right = Kee[int](5)
    BottomLeft = Kee[int](6)
    Bottom = Kee[int](7)
    BottomRight = Kee[int](8)

  #  The classes Qt writes inside QQuickItem, each a class in here as in C++.

  class ItemChangeData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickItem::ItemChangeData: a plain Python object
    standing in front of one C++ QQuickItem::ItemChangeData.

    C++ hands a QQuickItem::ItemChangeData around as a copy, so every C++
    QQuickItem::ItemChangeData behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QQuickItem::ItemChangeData yet. It can be made from
    Python, in 4 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickItem::ItemChangeData::~ItemChangeData()': the destructor:
      Python removes its C++ QQuickItem::ItemChangeData by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QQuickItem::ItemChangeData is created at the first use, not by
      'QQuickItem::ItemChangeData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickItem::ItemChangeData back gives a copy the
      ritual made for Python, in a new cute QQuickItem::ItemChangeData.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QQuickItem = WAIT['QQuickItem']
      QQuickWindow = WAIT['QQuickWindow']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickItem::ItemChangeData'

    #  Qt's '~QQuickItem::ItemChangeData()'. Naming it makes this a value
    #  class: Python owns every C++ QQuickItem::ItemChangeData behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN10QQuickItem14ItemChangeDataD1Ev'

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

    @overload(QQuickItem)
    @overload(NoneType)
    def __init__(self, v: Optional[QQuickItem]) -> None:
      """
      Notes what was given, for Qt's
      'QQuickItem::ItemChangeData::ItemChangeData(QQuickItem *v)', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickitem-itemchangedata.html#ItemChangeData

      Parameters
      ----------

      v : Optional[QQuickItem]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  QQuickItem::ItemChangeData::ItemChangeData(QQuickItem *v)
      self._noteCreation(QQuickItem.ItemChangeData, lambda: Rituals.call(
          'ritual_ZN10QQuickItem14ItemChangeDataC1EPS_', self._addressOf(v),
      ))

    @overload(QQuickWindow)
    def __init__(self, v: Optional[QQuickWindow]) -> None:
      """
      Notes what was given, for Qt's
      'QQuickItem::ItemChangeData::ItemChangeData(QQuickWindow *v)', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickitem-itemchangedata.html#ItemChangeData

      Parameters
      ----------

      v : Optional[QQuickWindow]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  QQuickItem::ItemChangeData::ItemChangeData(QQuickWindow *v)
      self._noteCreation(QQuickItem.ItemChangeData, lambda: Rituals.call(
          'ritual_ZN10QQuickItem14ItemChangeDataC1EP12QQuickWindow',
          self._addressOf(v),
      ))

    @overload(float)
    def __init__(self, v: float) -> None:
      """
      Notes what was given, for Qt's
      'QQuickItem::ItemChangeData::ItemChangeData(qreal v)', which is called
      at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickitem-itemchangedata.html#ItemChangeData

      Parameters
      ----------

      v : float
        Passed on as it is.
      """
      #  QQuickItem::ItemChangeData::ItemChangeData(qreal v)
      self._noteCreation(QQuickItem.ItemChangeData, lambda: Rituals.call(
          'ritual_ZN10QQuickItem14ItemChangeDataC1Ed', v,
      ))

    @overload(bool)
    def __init__(self, v: bool) -> None:
      """
      Notes what was given, for Qt's
      'QQuickItem::ItemChangeData::ItemChangeData(bool v)', which is called
      at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickitem-itemchangedata.html#ItemChangeData

      Parameters
      ----------

      v : bool
        Passed on as it is.
      """
      #  QQuickItem::ItemChangeData::ItemChangeData(bool v)
      self._noteCreation(QQuickItem.ItemChangeData, lambda: Rituals.call(
          'ritual_ZN10QQuickItem14ItemChangeDataC1Eb', v,
      ))

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

  class UpdatePaintNodeData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickItem::UpdatePaintNodeData: a plain Python
    object standing in front of one C++ QQuickItem::UpdatePaintNodeData.

    C++ hands a QQuickItem::UpdatePaintNodeData around as a copy, so every
    C++ QQuickItem::UpdatePaintNodeData behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QQuickItem::UpdatePaintNodeData yet. It can be made
    from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickItem::UpdatePaintNodeData::~UpdatePaintNodeData()': the
      destructor: Python removes its C++ QQuickItem::UpdatePaintNodeData by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QQuickItem::UpdatePaintNodeData is created at the first use,
      not by 'QQuickItem::UpdatePaintNodeData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickItem::UpdatePaintNodeData back gives a copy
      the ritual made for Python, in a new cute
      QQuickItem::UpdatePaintNodeData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickItem::UpdatePaintNodeData'

    #  Qt's '~QQuickItem::UpdatePaintNodeData()'. Naming it makes this a
    #  value class: Python owns every C++ QQuickItem::UpdatePaintNodeData
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN10QQuickItem19UpdatePaintNodeDataD1Ev'

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QQuickItem::UpdatePaintNodeData::UpdatePaintNodeData()', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickitem-updatepaintnodedata.html
      """
      #  QQuickItem::UpdatePaintNodeData::UpdatePaintNodeData()
      self._noteCreation(
          QQuickItem.UpdatePaintNodeData, lambda: Rituals.call(
              'ritual_ZN10QQuickItem19UpdatePaintNodeDataC1Ev',
          ))

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
    Calls Qt's 'QString QQuickItem::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#tr

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
    #  QString QQuickItem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QQuickItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickItem'

  #  Qt's QQuickItem is built on more than one class. The part of a C++
  #  QQuickItem that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_QQuickItem_QQmlParserStatus',
  }

  #  A C++ QQuickItem Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickItem'

  #  The functions Qt calls itself that QQuickItem is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'boundingRect': (
          ('_ZNK10QQuickItem12boundingRectEv',
           ('address', 'value', 'QtCore:QRectF'),
           ()),
      ),
      'clipRect': (
          ('_ZNK10QQuickItem8clipRectEv',
           ('address', 'value', 'QtCore:QRectF'),
           ()),
      ),
      'contains': (
          ('_ZNK10QQuickItem8containsERK7QPointF',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QPointF'),
           )),
      ),
      'inputMethodQuery': (
          ('_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('int', 'enum', 'QtCore:Qt.InputMethodQuery'),
           )),
      ),
      'isTextureProvider': (
          ('_ZNK10QQuickItem17isTextureProviderEv',
           ('bool', 'number', ''),
           ()),
      ),
      'textureProvider': (
          ('_ZNK10QQuickItem15textureProviderEv',
           ('address', 'address', 'QtQuick:QSGTextureProvider'),
           ()),
      ),
      'itemChange': (
          ('_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDa'
           'taE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtQuick:QQuickItem.ItemChange'),
               ('address', 'value', 'QtQuick:QQuickItem.ItemChangeData'),
           )),
      ),
      'geometryChange': (
          ('_ZN10QQuickItem14geometryChangeERK6QRectFS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'keyPressEvent': (
          ('_ZN10QQuickItem13keyPressEventEP9QKeyEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QKeyEvent'),
           )),
      ),
      'keyReleaseEvent': (
          ('_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QKeyEvent'),
           )),
      ),
      'inputMethodEvent': (
          ('_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QInputMethodEvent'),
           )),
      ),
      'focusInEvent': (
          ('_ZN10QQuickItem12focusInEventEP11QFocusEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QFocusEvent'),
           )),
      ),
      'focusOutEvent': (
          ('_ZN10QQuickItem13focusOutEventEP11QFocusEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QFocusEvent'),
           )),
      ),
      'mousePressEvent': (
          ('_ZN10QQuickItem15mousePressEventEP11QMouseEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QMouseEvent'),
           )),
      ),
      'mouseMoveEvent': (
          ('_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QMouseEvent'),
           )),
      ),
      'mouseReleaseEvent': (
          ('_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QMouseEvent'),
           )),
      ),
      'mouseDoubleClickEvent': (
          ('_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QMouseEvent'),
           )),
      ),
      'mouseUngrabEvent': (
          ('_ZN10QQuickItem16mouseUngrabEventEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'touchUngrabEvent': (
          ('_ZN10QQuickItem16touchUngrabEventEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'wheelEvent': (
          ('_ZN10QQuickItem10wheelEventEP11QWheelEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QWheelEvent'),
           )),
      ),
      'touchEvent': (
          ('_ZN10QQuickItem10touchEventEP11QTouchEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QTouchEvent'),
           )),
      ),
      'hoverEnterEvent': (
          ('_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QHoverEvent'),
           )),
      ),
      'hoverMoveEvent': (
          ('_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QHoverEvent'),
           )),
      ),
      'hoverLeaveEvent': (
          ('_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QHoverEvent'),
           )),
      ),
      'dragEnterEvent': (
          ('_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QDragEnterEvent'),
           )),
      ),
      'dragMoveEvent': (
          ('_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QDragMoveEvent'),
           )),
      ),
      'dragLeaveEvent': (
          ('_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QDragLeaveEvent'),
           )),
      ),
      'dropEvent': (
          ('_ZN10QQuickItem9dropEventEP10QDropEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QDropEvent'),
           )),
      ),
      'childMouseEventFilter': (
          ('_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'address', 'QtCore:QEvent'),
           )),
      ),
      'updatePaintNode': (
          ('_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNode'
           'DataE',
           ('address', 'address', 'QtQuick:QSGNode'),
           (
               ('address', 'address', 'QtQuick:QSGNode'),
               ('address', 'address',
                'QtQuick:QQuickItem.UpdatePaintNodeData'),
           )),
      ),
      'releaseResources': (
          ('_ZN10QQuickItem16releaseResourcesEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'updatePolish': (
          ('_ZN10QQuickItem12updatePolishEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickItem::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickItem::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QQuickItem10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def window(self) -> Optional[QQuickWindow]:
    """
    Calls Qt's 'QQuickWindow *QQuickItem::window() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#window

    Returns
    -------

    Optional[QQuickWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWindow *QQuickItem::window() const
    address = self.uglySide.call('ritual_ZNK10QQuickItem6windowEv')
    from . import QQuickWindow
    return QQuickWindow._cuteAt(address)

  def parentItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickItem::parentItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#parentItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickItem::parentItem() const
    address = self.uglySide.call('ritual_ZNK10QQuickItem10parentItemEv')
    return QQuickItem._cuteAt(address)

  def childItems(self) -> QList[QQuickItem]:
    """
    Calls Qt's 'QList<QQuickItem *> QQuickItem::childItems() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#childItems

    Returns
    -------

    QList[QQuickItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQuickItem *> QQuickItem::childItems() const
    address = self.uglySide.call('ritual_ZNK10QQuickItem10childItemsEv')
    return QList[QQuickItem]._cuteOwning(address)

  def clip(self) -> bool:
    """
    Calls Qt's 'bool QQuickItem::clip() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#clip
    """
    #  bool QQuickItem::clip() const
    return self.uglySide.call('ritual_ZNK10QQuickItem4clipEv')

  def state(self) -> str:
    """
    Calls Qt's 'QString QQuickItem::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#state

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickItem::state() const
    return self.uglySide.call('ritual_ZNK10QQuickItem5stateEv')

  def baselineOffset(self) -> float:
    """
    Calls Qt's 'qreal QQuickItem::baselineOffset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#baselineOffset
    """
    #  qreal QQuickItem::baselineOffset() const
    return self.uglySide.call('ritual_ZNK10QQuickItem14baselineOffsetEv')

  def x(self) -> float:
    """
    Calls Qt's 'qreal QQuickItem::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#x
    """
    #  qreal QQuickItem::x() const
    return self.uglySide.call('ritual_ZNK10QQuickItem1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'qreal QQuickItem::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#y
    """
    #  qreal QQuickItem::y() const
    return self.uglySide.call('ritual_ZNK10QQuickItem1yEv')

  def position(self) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickItem::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#position

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickItem::position() const
    address = self.uglySide.call('ritual_ZNK10QQuickItem8positionEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def width(self) -> float:
    """
    Calls Qt's 'qreal QQuickItem::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#width
    """
    #  qreal QQuickItem::width() const
    return self.uglySide.call('ritual_ZNK10QQuickItem5widthEv')

  def implicitWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickItem::implicitWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#implicitWidth
    """
    #  qreal QQuickItem::implicitWidth() const
    return self.uglySide.call('ritual_ZNK10QQuickItem13implicitWidthEv')

  def height(self) -> float:
    """
    Calls Qt's 'qreal QQuickItem::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#height
    """
    #  qreal QQuickItem::height() const
    return self.uglySide.call('ritual_ZNK10QQuickItem6heightEv')

  def implicitHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickItem::implicitHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#implicitHeight
    """
    #  qreal QQuickItem::implicitHeight() const
    return self.uglySide.call('ritual_ZNK10QQuickItem14implicitHeightEv')

  def size(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QQuickItem::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#size

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QQuickItem::size() const
    address = self.uglySide.call('ritual_ZNK10QQuickItem4sizeEv')
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def transformOrigin(self) -> TransformOrigin:
    """
    Calls Qt's 'TransformOrigin QQuickItem::transformOrigin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#transformOrigin

    Returns
    -------

    TransformOrigin
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TransformOrigin(number)'
      gives.
    """
    #  TransformOrigin QQuickItem::transformOrigin() const
    return QQuickItem.TransformOrigin(self.uglySide.call(
        'ritual_ZNK10QQuickItem15transformOriginEv',
    ))

  def transformOriginPoint(self) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickItem::transformOriginPoint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitem.html#transformOriginPoint

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickItem::transformOriginPoint() const
    address = self.uglySide.call(
        'ritual_ZNK10QQuickItem20transformOriginPointEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def z(self) -> float:
    """
    Calls Qt's 'qreal QQuickItem::z() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#z
    """
    #  qreal QQuickItem::z() const
    return self.uglySide.call('ritual_ZNK10QQuickItem1zEv')

  def rotation(self) -> float:
    """
    Calls Qt's 'qreal QQuickItem::rotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#rotation
    """
    #  qreal QQuickItem::rotation() const
    return self.uglySide.call('ritual_ZNK10QQuickItem8rotationEv')

  def scale(self) -> float:
    """
    Calls Qt's 'qreal QQuickItem::scale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#scale
    """
    #  qreal QQuickItem::scale() const
    return self.uglySide.call('ritual_ZNK10QQuickItem5scaleEv')

  def opacity(self) -> float:
    """
    Calls Qt's 'qreal QQuickItem::opacity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#opacity
    """
    #  qreal QQuickItem::opacity() const
    return self.uglySide.call('ritual_ZNK10QQuickItem7opacityEv')

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QQuickItem::isVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#isVisible
    """
    #  bool QQuickItem::isVisible() const
    return self.uglySide.call('ritual_ZNK10QQuickItem9isVisibleEv')

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickItem::isEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#isEnabled
    """
    #  bool QQuickItem::isEnabled() const
    return self.uglySide.call('ritual_ZNK10QQuickItem9isEnabledEv')

  def smooth(self) -> bool:
    """
    Calls Qt's 'bool QQuickItem::smooth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#smooth
    """
    #  bool QQuickItem::smooth() const
    return self.uglySide.call('ritual_ZNK10QQuickItem6smoothEv')

  def activeFocusOnTab(self) -> bool:
    """
    Calls Qt's 'bool QQuickItem::activeFocusOnTab() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#activeFocusOnTab
    """
    #  bool QQuickItem::activeFocusOnTab() const
    return self.uglySide.call('ritual_ZNK10QQuickItem16activeFocusOnTabEv')

  def antialiasing(self) -> bool:
    """
    Calls Qt's 'bool QQuickItem::antialiasing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#antialiasing
    """
    #  bool QQuickItem::antialiasing() const
    return self.uglySide.call('ritual_ZNK10QQuickItem12antialiasingEv')

  def flags(self) -> Flags:
    """
    Calls Qt's 'Flags QQuickItem::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#flags

    Returns
    -------

    Flags
      The value standing for the combination Qt gave back.
    """
    #  Flags QQuickItem::flags() const
    return QQuickItem.Flags(self.uglySide.call(
        'ritual_ZNK10QQuickItem5flagsEv',
    ))

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickItem::boundingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickItem::boundingRect() const
    ritual = 'ritual_ZNK10QQuickItem12boundingRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QQuickItem12boundingRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def clipRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickItem::clipRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#clipRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickItem::clipRect() const
    ritual = 'ritual_ZNK10QQuickItem8clipRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QQuickItem8clipRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def viewportItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickItem::viewportItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#viewportItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickItem::viewportItem() const
    address = self.uglySide.call('ritual_ZNK10QQuickItem12viewportItemEv')
    return QQuickItem._cuteAt(address)

  def hasActiveFocus(self) -> bool:
    """
    Calls Qt's 'bool QQuickItem::hasActiveFocus() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#hasActiveFocus
    """
    #  bool QQuickItem::hasActiveFocus() const
    return self.uglySide.call('ritual_ZNK10QQuickItem14hasActiveFocusEv')

  def hasFocus(self) -> bool:
    """
    Calls Qt's 'bool QQuickItem::hasFocus() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#hasFocus
    """
    #  bool QQuickItem::hasFocus() const
    return self.uglySide.call('ritual_ZNK10QQuickItem8hasFocusEv')

  def isFocusScope(self) -> bool:
    """
    Calls Qt's 'bool QQuickItem::isFocusScope() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#isFocusScope
    """
    #  bool QQuickItem::isFocusScope() const
    return self.uglySide.call('ritual_ZNK10QQuickItem12isFocusScopeEv')

  def scopedFocusItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickItem::scopedFocusItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#scopedFocusItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickItem::scopedFocusItem() const
    address = self.uglySide.call('ritual_ZNK10QQuickItem15scopedFocusItemEv')
    return QQuickItem._cuteAt(address)

  def focusPolicy(self) -> Qt.FocusPolicy:
    """
    Calls Qt's 'Qt::FocusPolicy QQuickItem::focusPolicy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#focusPolicy

    Returns
    -------

    Qt.FocusPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.FocusPolicy(number)'
      gives.
    """
    #  Qt::FocusPolicy QQuickItem::focusPolicy() const
    return Qt.FocusPolicy(self.uglySide.call(
        'ritual_ZNK10QQuickItem11focusPolicyEv',
    ))

  @overload(THIS)
  @overload(NoneType)
  def isAncestorOf(self, child: Optional[QQuickItem]) -> bool:
    """
    Calls Qt's 'bool QQuickItem::isAncestorOf(const QQuickItem *child)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#isAncestorOf

    Parameters
    ----------

    child : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickItem::isAncestorOf(const QQuickItem *child) const
    return self.uglySide.call(
        'ritual_ZNK10QQuickItem12isAncestorOfEPKS_', self._addressOf(child),
    )

  def acceptedMouseButtons(self) -> Qt.MouseButtons:
    """
    Calls Qt's 'Qt::MouseButtons QQuickItem::acceptedMouseButtons() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitem.html#acceptedMouseButtons

    Returns
    -------

    Qt.MouseButtons
      The value standing for the combination Qt gave back.
    """
    #  Qt::MouseButtons QQuickItem::acceptedMouseButtons() const
    return Qt.MouseButtons(self.uglySide.call(
        'ritual_ZNK10QQuickItem20acceptedMouseButtonsEv',
    ))

  def acceptHoverEvents(self) -> bool:
    """
    Calls Qt's 'bool QQuickItem::acceptHoverEvents() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#acceptHoverEvents
    """
    #  bool QQuickItem::acceptHoverEvents() const
    return self.uglySide.call('ritual_ZNK10QQuickItem17acceptHoverEventsEv')

  def acceptTouchEvents(self) -> bool:
    """
    Calls Qt's 'bool QQuickItem::acceptTouchEvents() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#acceptTouchEvents
    """
    #  bool QQuickItem::acceptTouchEvents() const
    return self.uglySide.call('ritual_ZNK10QQuickItem17acceptTouchEventsEv')

  def cursor(self) -> QCursor:
    """
    Calls Qt's 'QCursor QQuickItem::cursor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#cursor

    Returns
    -------

    QCursor
      A new cute QCursor around the copy Qt gave back. Python owns it.
    """
    #  QCursor QQuickItem::cursor() const
    address = self.uglySide.call('ritual_ZNK10QQuickItem6cursorEv')
    from ..QtGui import QCursor
    return QCursor._cuteOwning(address)

  def isUnderMouse(self) -> bool:
    """
    Calls Qt's 'bool QQuickItem::isUnderMouse() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#isUnderMouse
    """
    #  bool QQuickItem::isUnderMouse() const
    return self.uglySide.call('ritual_ZNK10QQuickItem12isUnderMouseEv')

  def keepMouseGrab(self) -> bool:
    """
    Calls Qt's 'bool QQuickItem::keepMouseGrab() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#keepMouseGrab
    """
    #  bool QQuickItem::keepMouseGrab() const
    return self.uglySide.call('ritual_ZNK10QQuickItem13keepMouseGrabEv')

  def filtersChildMouseEvents(self) -> bool:
    """
    Calls Qt's 'bool QQuickItem::filtersChildMouseEvents() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitem.html#filtersChildMouseEvents
    """
    #  bool QQuickItem::filtersChildMouseEvents() const
    return self.uglySide.call(
        'ritual_ZNK10QQuickItem23filtersChildMouseEventsEv',
    )

  def keepTouchGrab(self) -> bool:
    """
    Calls Qt's 'bool QQuickItem::keepTouchGrab() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#keepTouchGrab
    """
    #  bool QQuickItem::keepTouchGrab() const
    return self.uglySide.call('ritual_ZNK10QQuickItem13keepTouchGrabEv')

  @overload(QPointF)
  def contains(self, point: QPointF) -> bool:
    """
    Calls Qt's 'bool QQuickItem::contains(const QPointF &point) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#contains

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QQuickItem::contains(const QPointF &point) const
    ritual = 'ritual_ZNK10QQuickItem8containsERK7QPointF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QQuickItem8containsERK7QPointF'
    return self.uglySide.call(ritual, self._valueOf(point, 'QPointF'))

  def containmentMask(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQuickItem::containmentMask() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#containmentMask

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQuickItem::containmentMask() const
    address = self.uglySide.call('ritual_ZNK10QQuickItem15containmentMaskEv')
    return QObject._cuteAt(address)

  @overload(QPointF)
  def mapToScene(self, point: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickItem::mapToScene(const QPointF &point) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#mapToScene

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
    #  QPointF QQuickItem::mapToScene(const QPointF &point) const
    address = self.uglySide.call(
        'ritual_ZNK10QQuickItem10mapToSceneERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(THIS, QRectF)
  @overload(NoneType, QRectF)
  def mapRectToItem(
      self,
      item: Optional[QQuickItem],
      rect: QRectF,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickItem::mapRectToItem(const QQuickItem *item,
    const QRectF &rect) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#mapRectToItem

    Parameters
    ----------

    item : Optional[QQuickItem]
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
    #  QRectF QQuickItem::mapRectToItem(const QQuickItem *item, const QRectF
    #      &rect) const
    address = self.uglySide.call(
        'ritual_ZNK10QQuickItem13mapRectToItemEPKS_RK6QRectF',
        self._addressOf(item), self._valueOf(rect),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QRectF)
  def mapRectToScene(self, rect: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickItem::mapRectToScene(const QRectF &rect) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#mapRectToScene

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
    #  QRectF QQuickItem::mapRectToScene(const QRectF &rect) const
    address = self.uglySide.call(
        'ritual_ZNK10QQuickItem14mapRectToSceneERK6QRectF',
        self._valueOf(rect),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QPointF)
  def mapFromScene(self, point: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickItem::mapFromScene(const QPointF &point)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#mapFromScene

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
    #  QPointF QQuickItem::mapFromScene(const QPointF &point) const
    address = self.uglySide.call(
        'ritual_ZNK10QQuickItem12mapFromSceneERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(THIS, QRectF)
  @overload(NoneType, QRectF)
  def mapRectFromItem(
      self,
      item: Optional[QQuickItem],
      rect: QRectF,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickItem::mapRectFromItem(const QQuickItem *item,
    const QRectF &rect) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#mapRectFromItem

    Parameters
    ----------

    item : Optional[QQuickItem]
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
    #  QRectF QQuickItem::mapRectFromItem(const QQuickItem *item, const
    #      QRectF &rect) const
    address = self.uglySide.call(
        'ritual_ZNK10QQuickItem15mapRectFromItemEPKS_RK6QRectF',
        self._addressOf(item), self._valueOf(rect),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QRectF)
  def mapRectFromScene(self, rect: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickItem::mapRectFromScene(const QRectF &rect)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#mapRectFromScene

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
    #  QRectF QQuickItem::mapRectFromScene(const QRectF &rect) const
    address = self.uglySide.call(
        'ritual_ZNK10QQuickItem16mapRectFromSceneERK6QRectF',
        self._valueOf(rect),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(float, float)
  def childAt(self, x: float, y: float) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickItem::childAt(qreal x, qreal y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#childAt

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickItem::childAt(qreal x, qreal y) const
    address = self.uglySide.call('ritual_ZNK10QQuickItem7childAtEdd', x, y)
    return QQuickItem._cuteAt(address)

  @overload(Qt.InputMethodQuery)
  def inputMethodQuery(self, query: Qt.InputMethodQuery) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery
    query) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#inputMethodQuery

    Parameters
    ----------

    query : Qt.InputMethodQuery
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
    #      const
    ritual = (
        'ritual_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQu'
          'eryE')
    address = self.uglySide.call(ritual, query.value)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def isTextureProvider(self) -> bool:
    """
    Calls Qt's 'bool QQuickItem::isTextureProvider() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#isTextureProvider
    """
    #  bool QQuickItem::isTextureProvider() const
    ritual = 'ritual_ZNK10QQuickItem17isTextureProviderEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QQuickItem17isTextureProviderEv'
    return self.uglySide.call(ritual)

  def textureProvider(self) -> Optional[QSGTextureProvider]:
    """
    Calls Qt's 'QSGTextureProvider *QQuickItem::textureProvider() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#textureProvider

    Returns
    -------

    Optional[QSGTextureProvider]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTextureProvider *QQuickItem::textureProvider() const
    ritual = 'ritual_ZNK10QQuickItem15textureProviderEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QQuickItem15textureProviderEv'
    address = self.uglySide.call(ritual)
    from . import QSGTextureProvider
    return QSGTextureProvider._cuteAt(address)

  def mutabilityGroup(self) -> int:
    """
    Calls Qt's 'int QQuickItem::mutabilityGroup() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#mutabilityGroup
    """
    #  int QQuickItem::mutabilityGroup() const
    return self.uglySide.call('ritual_ZNK10QQuickItem15mutabilityGroupEv')

  def isComponentComplete(self) -> bool:
    """
    Calls Qt's 'bool QQuickItem::isComponentComplete() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitem.html#isComponentComplete
    """
    #  bool QQuickItem::isComponentComplete() const
    return self.uglySide.call(
        'ritual_ZNK10QQuickItem19isComponentCompleteEv',
    )

  def widthValid(self) -> bool:
    """
    Calls Qt's 'bool QQuickItem::widthValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#widthValid
    """
    #  bool QQuickItem::widthValid() const
    return self.uglySide.call('ritual_ZNK10QQuickItem10widthValidEv')

  def heightValid(self) -> bool:
    """
    Calls Qt's 'bool QQuickItem::heightValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#heightValid
    """
    #  bool QQuickItem::heightValid() const
    return self.uglySide.call('ritual_ZNK10QQuickItem11heightValidEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  @overload(NoneType)
  def setParentItem(self, parent: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickItem::setParentItem(QQuickItem *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#setParentItem

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItem::setParentItem(QQuickItem *parent)
    self.uglySide.call(
        'ritual_ZN10QQuickItem13setParentItemEPS_', self._addressOf(parent),
    )

  @overload(bool)
  def setClip(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickItem::setClip(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#setClip

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickItem::setClip(bool a0)
    self.uglySide.call('ritual_ZN10QQuickItem7setClipEb', a0)

  @overload(str)
  def setState(self, a0: str) -> None:
    """
    Calls Qt's 'void QQuickItem::setState(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#setState

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickItem::setState(const QString &a0)
    self.uglySide.call('ritual_ZN10QQuickItem8setStateERK7QString', a0)

  @overload(float)
  def setBaselineOffset(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickItem::setBaselineOffset(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#setBaselineOffset

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickItem::setBaselineOffset(qreal a0)
    self.uglySide.call('ritual_ZN10QQuickItem17setBaselineOffsetEd', a0)

  @overload(float)
  def setX(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickItem::setX(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#setX

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickItem::setX(qreal a0)
    self.uglySide.call('ritual_ZN10QQuickItem4setXEd', a0)

  @overload(float)
  def setY(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickItem::setY(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#setY

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickItem::setY(qreal a0)
    self.uglySide.call('ritual_ZN10QQuickItem4setYEd', a0)

  @overload(QPointF)
  def setPosition(self, a0: QPointF) -> None:
    """
    Calls Qt's 'void QQuickItem::setPosition(const QPointF &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#setPosition

    Parameters
    ----------

    a0 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickItem::setPosition(const QPointF &a0)
    self.uglySide.call(
        'ritual_ZN10QQuickItem11setPositionERK7QPointF',
        self._valueOf(a0, 'QPointF'),
    )

  @overload(float)
  def setWidth(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickItem::setWidth(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#setWidth

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickItem::setWidth(qreal a0)
    self.uglySide.call('ritual_ZN10QQuickItem8setWidthEd', a0)

  @overload(float)
  def setImplicitWidth(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickItem::setImplicitWidth(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#setImplicitWidth

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickItem::setImplicitWidth(qreal a0)
    self.uglySide.call('ritual_ZN10QQuickItem16setImplicitWidthEd', a0)

  @overload(float)
  def setHeight(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickItem::setHeight(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#setHeight

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickItem::setHeight(qreal a0)
    self.uglySide.call('ritual_ZN10QQuickItem9setHeightEd', a0)

  @overload(float)
  def setImplicitHeight(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickItem::setImplicitHeight(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#setImplicitHeight

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickItem::setImplicitHeight(qreal a0)
    self.uglySide.call('ritual_ZN10QQuickItem17setImplicitHeightEd', a0)

  @overload(QSizeF)
  def setSize(self, size: QSizeF) -> None:
    """
    Calls Qt's 'void QQuickItem::setSize(const QSizeF &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#setSize

    Parameters
    ----------

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QQuickItem::setSize(const QSizeF &size)
    self.uglySide.call(
        'ritual_ZN10QQuickItem7setSizeERK6QSizeF', self._valueOf(size),
    )

  @overload(TransformOrigin)
  def setTransformOrigin(self, a0: TransformOrigin) -> None:
    """
    Calls Qt's 'void QQuickItem::setTransformOrigin(TransformOrigin a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#setTransformOrigin

    Parameters
    ----------

    a0 : TransformOrigin
      Passed on as its number.
    """
    #  void QQuickItem::setTransformOrigin(TransformOrigin a0)
    self.uglySide.call(
        'ritual_ZN10QQuickItem18setTransformOriginENS_15TransformOriginE',
        a0.value,
    )

  @overload(QPointF)
  def setTransformOriginPoint(self, a0: QPointF) -> None:
    """
    Calls Qt's 'void QQuickItem::setTransformOriginPoint(const QPointF &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitem.html#setTransformOriginPoint

    Parameters
    ----------

    a0 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickItem::setTransformOriginPoint(const QPointF &a0)
    self.uglySide.call(
        'ritual_ZN10QQuickItem23setTransformOriginPointERK7QPointF',
        self._valueOf(a0, 'QPointF'),
    )

  @overload(float)
  def setZ(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickItem::setZ(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#setZ

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickItem::setZ(qreal a0)
    self.uglySide.call('ritual_ZN10QQuickItem4setZEd', a0)

  @overload(float)
  def setRotation(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickItem::setRotation(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#setRotation

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickItem::setRotation(qreal a0)
    self.uglySide.call('ritual_ZN10QQuickItem11setRotationEd', a0)

  @overload(float)
  def setScale(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickItem::setScale(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#setScale

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickItem::setScale(qreal a0)
    self.uglySide.call('ritual_ZN10QQuickItem8setScaleEd', a0)

  @overload(float)
  def setOpacity(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickItem::setOpacity(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#setOpacity

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickItem::setOpacity(qreal a0)
    self.uglySide.call('ritual_ZN10QQuickItem10setOpacityEd', a0)

  @overload(bool)
  def setVisible(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickItem::setVisible(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#setVisible

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickItem::setVisible(bool a0)
    self.uglySide.call('ritual_ZN10QQuickItem10setVisibleEb', a0)

  @overload(bool)
  def setEnabled(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickItem::setEnabled(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#setEnabled

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickItem::setEnabled(bool a0)
    self.uglySide.call('ritual_ZN10QQuickItem10setEnabledEb', a0)

  @overload(bool)
  def setSmooth(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickItem::setSmooth(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#setSmooth

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickItem::setSmooth(bool a0)
    self.uglySide.call('ritual_ZN10QQuickItem9setSmoothEb', a0)

  @overload(bool)
  def setActiveFocusOnTab(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickItem::setActiveFocusOnTab(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitem.html#setActiveFocusOnTab

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickItem::setActiveFocusOnTab(bool a0)
    self.uglySide.call('ritual_ZN10QQuickItem19setActiveFocusOnTabEb', a0)

  @overload(bool)
  def setAntialiasing(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickItem::setAntialiasing(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#setAntialiasing

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickItem::setAntialiasing(bool a0)
    self.uglySide.call('ritual_ZN10QQuickItem15setAntialiasingEb', a0)

  @overload(Flag)
  @overload(Flag, bool)
  def setFlag(self, flag: Flag, enabled: bool = True) -> None:
    """
    Calls Qt's 'void QQuickItem::setFlag(Flag flag, bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#setFlag

    Parameters
    ----------

    flag : Flag
      Passed on as its number.

    enabled : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QQuickItem::setFlag(Flag flag, bool enabled)
    self.uglySide.call(
        'ritual_ZN10QQuickItem7setFlagENS_4FlagEb', flag.value, enabled,
    )

  @overload(Flags)
  def setFlags(self, flags: Flags) -> None:
    """
    Calls Qt's 'void QQuickItem::setFlags(Flags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#setFlags

    Parameters
    ----------

    flags : Flags
      Passed on as its number.
    """
    #  void QQuickItem::setFlags(Flags flags)
    self.uglySide.call(
        'ritual_ZN10QQuickItem8setFlagsE6QFlagsINS_4FlagEE', flags.value,
    )

  @overload(bool)
  def setFocus(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickItem::setFocus(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#setFocus

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickItem::setFocus(bool a0)
    self.uglySide.call('ritual_ZN10QQuickItem8setFocusEb', a0)

  @overload(bool, Qt.FocusReason)
  def setFocus(self, focus: bool, reason: Qt.FocusReason) -> None:
    """
    Calls Qt's 'void QQuickItem::setFocus(bool focus, Qt::FocusReason
    reason)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#setFocus

    Parameters
    ----------

    focus : bool
      Passed on as it is.

    reason : Qt.FocusReason
      Passed on as its number.
    """
    #  void QQuickItem::setFocus(bool focus, Qt::FocusReason reason)
    self.uglySide.call(
        'ritual_ZN10QQuickItem8setFocusEbN2Qt11FocusReasonE',
        focus, reason.value,
    )

  @overload(Qt.FocusPolicy)
  def setFocusPolicy(self, policy: Qt.FocusPolicy) -> None:
    """
    Calls Qt's 'void QQuickItem::setFocusPolicy(Qt::FocusPolicy policy)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#setFocusPolicy

    Parameters
    ----------

    policy : Qt.FocusPolicy
      Passed on as its number.
    """
    #  void QQuickItem::setFocusPolicy(Qt::FocusPolicy policy)
    self.uglySide.call(
        'ritual_ZN10QQuickItem14setFocusPolicyEN2Qt11FocusPolicyE',
        policy.value,
    )

  @overload(Qt.MouseButtons)
  def setAcceptedMouseButtons(self, buttons: Qt.MouseButtons) -> None:
    """
    Calls Qt's 'void QQuickItem::setAcceptedMouseButtons(Qt::MouseButtons
    buttons)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitem.html#setAcceptedMouseButtons

    Parameters
    ----------

    buttons : Qt.MouseButtons
      Passed on as its number.
    """
    #  void QQuickItem::setAcceptedMouseButtons(Qt::MouseButtons buttons)
    self.uglySide.call(
        'ritual_ZN10QQuickItem23setAcceptedMouseButtonsE6QFlagsIN2Qt11Mouse'
        'ButtonEE',
        buttons.value,
    )

  @overload(bool)
  def setAcceptHoverEvents(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickItem::setAcceptHoverEvents(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitem.html#setAcceptHoverEvents

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickItem::setAcceptHoverEvents(bool enabled)
    self.uglySide.call(
        'ritual_ZN10QQuickItem20setAcceptHoverEventsEb', enabled,
    )

  @overload(bool)
  def setAcceptTouchEvents(self, accept: bool) -> None:
    """
    Calls Qt's 'void QQuickItem::setAcceptTouchEvents(bool accept)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitem.html#setAcceptTouchEvents

    Parameters
    ----------

    accept : bool
      Passed on as it is.
    """
    #  void QQuickItem::setAcceptTouchEvents(bool accept)
    self.uglySide.call(
        'ritual_ZN10QQuickItem20setAcceptTouchEventsEb', accept,
    )

  @overload(QCursor)
  def setCursor(self, cursor: QCursor) -> None:
    """
    Calls Qt's 'void QQuickItem::setCursor(const QCursor &cursor)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#setCursor

    Parameters
    ----------

    cursor : QCursor
      Passed on as a value: Qt reads the C++ QCursor, which stays Python's
      own.
    """
    #  void QQuickItem::setCursor(const QCursor &cursor)
    self.uglySide.call(
        'ritual_ZN10QQuickItem9setCursorERK7QCursor', self._valueOf(cursor),
    )

  @overload(bool)
  def setKeepMouseGrab(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickItem::setKeepMouseGrab(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#setKeepMouseGrab

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickItem::setKeepMouseGrab(bool a0)
    self.uglySide.call('ritual_ZN10QQuickItem16setKeepMouseGrabEb', a0)

  @overload(bool)
  def setFiltersChildMouseEvents(self, filter: bool) -> None:
    """
    Calls Qt's 'void QQuickItem::setFiltersChildMouseEvents(bool filter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitem.html#setFiltersChildMouseEvents

    Parameters
    ----------

    filter : bool
      Passed on as it is.
    """
    #  void QQuickItem::setFiltersChildMouseEvents(bool filter)
    self.uglySide.call(
        'ritual_ZN10QQuickItem26setFiltersChildMouseEventsEb', filter,
    )

  @overload(bool)
  def setKeepTouchGrab(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickItem::setKeepTouchGrab(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#setKeepTouchGrab

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickItem::setKeepTouchGrab(bool a0)
    self.uglySide.call('ritual_ZN10QQuickItem16setKeepTouchGrabEb', a0)

  @overload(QObject)
  @overload(NoneType)
  def setContainmentMask(self, mask: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickItem::setContainmentMask(QObject *mask)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#setContainmentMask

    Parameters
    ----------

    mask : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItem::setContainmentMask(QObject *mask)
    self.uglySide.call(
        'ritual_ZN10QQuickItem18setContainmentMaskEP7QObject',
        self._addressOf(mask, 'QObject'),
    )

  @overload(int)
  def setMutabilityGroup(self, mutabilityGroup: int) -> None:
    """
    Calls Qt's 'void QQuickItem::setMutabilityGroup(int mutabilityGroup)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#setMutabilityGroup

    Parameters
    ----------

    mutabilityGroup : int
      Passed on as it is.
    """
    #  void QQuickItem::setMutabilityGroup(int mutabilityGroup)
    self.uglySide.call(
        'ritual_ZN10QQuickItem18setMutabilityGroupEi', mutabilityGroup,
    )

  @overload(float, float)
  def setImplicitSize(self, a0: float, a1: float) -> None:
    """
    Calls Qt's 'void QQuickItem::setImplicitSize(qreal a0, qreal a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#setImplicitSize

    Parameters
    ----------

    a0 : float
      Passed on as it is.

    a1 : float
      Passed on as it is.
    """
    #  void QQuickItem::setImplicitSize(qreal a0, qreal a1)
    self.uglySide.call('ritual_ZN10QQuickItem15setImplicitSizeEdd', a0, a1)

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
  @overload(THIS)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickItem::QQuickItem(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#QQuickItem

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickItem::QQuickItem(QQuickItem *parent)
    self._noteCreation(QQuickItem, lambda: Rituals.call(
        'ritual_ZN10QQuickItemC1EPS_', self._addressOf(parent),
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

  @overload(THIS)
  @overload(NoneType)
  def stackBefore(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickItem::stackBefore(const QQuickItem *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#stackBefore

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItem::stackBefore(const QQuickItem *a0)
    self.uglySide.call(
        'ritual_ZN10QQuickItem11stackBeforeEPKS_', self._addressOf(a0),
    )

  @overload(THIS)
  @overload(NoneType)
  def stackAfter(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickItem::stackAfter(const QQuickItem *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#stackAfter

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItem::stackAfter(const QQuickItem *a0)
    self.uglySide.call(
        'ritual_ZN10QQuickItem10stackAfterEPKS_', self._addressOf(a0),
    )

  def childrenRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickItem::childrenRect()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#childrenRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickItem::childrenRect()
    address = self.uglySide.call('ritual_ZN10QQuickItem12childrenRectEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def resetWidth(self) -> None:
    """
    Calls Qt's 'void QQuickItem::resetWidth()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#resetWidth
    """
    #  void QQuickItem::resetWidth()
    self.uglySide.call('ritual_ZN10QQuickItem10resetWidthEv')

  def resetHeight(self) -> None:
    """
    Calls Qt's 'void QQuickItem::resetHeight()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#resetHeight
    """
    #  void QQuickItem::resetHeight()
    self.uglySide.call('ritual_ZN10QQuickItem11resetHeightEv')

  def resetAntialiasing(self) -> None:
    """
    Calls Qt's 'void QQuickItem::resetAntialiasing()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#resetAntialiasing
    """
    #  void QQuickItem::resetAntialiasing()
    self.uglySide.call('ritual_ZN10QQuickItem17resetAntialiasingEv')

  def unsetCursor(self) -> None:
    """
    Calls Qt's 'void QQuickItem::unsetCursor()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#unsetCursor
    """
    #  void QQuickItem::unsetCursor()
    self.uglySide.call('ritual_ZN10QQuickItem11unsetCursorEv')

  def grabMouse(self) -> None:
    """
    Calls Qt's 'void QQuickItem::grabMouse()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#grabMouse
    """
    #  void QQuickItem::grabMouse()
    self.uglySide.call('ritual_ZN10QQuickItem9grabMouseEv')

  def ungrabMouse(self) -> None:
    """
    Calls Qt's 'void QQuickItem::ungrabMouse()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#ungrabMouse
    """
    #  void QQuickItem::ungrabMouse()
    self.uglySide.call('ritual_ZN10QQuickItem11ungrabMouseEv')

  def ungrabTouchPoints(self) -> None:
    """
    Calls Qt's 'void QQuickItem::ungrabTouchPoints()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#ungrabTouchPoints
    """
    #  void QQuickItem::ungrabTouchPoints()
    self.uglySide.call('ritual_ZN10QQuickItem17ungrabTouchPointsEv')

  @overload(QJSValue)
  @overload(QJSValue, QSize)
  def grabToImage(
      self,
      callback: QJSValue,
      targetSize: Optional[QSize] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickItem::grabToImage(const QJSValue &callback, const
    QSize &targetSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#grabToImage

    Parameters
    ----------

    callback : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.

    targetSize : Optional[QSize]
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
      May be left out, as in Qt: a new 'QSize()' is then passed on.
    """
    #  bool QQuickItem::grabToImage(const QJSValue &callback, const QSize
    #      &targetSize)
    if targetSize is None:
      from ..QtCore import QSize
      targetSize = QSize()
    return self.uglySide.call(
        'ritual_ZN10QQuickItem11grabToImageERK8QJSValueRK5QSize',
        self._valueOf(callback), self._valueOf(targetSize),
    )

  def polish(self) -> None:
    """
    Calls Qt's 'void QQuickItem::polish()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#polish
    """
    #  void QQuickItem::polish()
    self.uglySide.call('ritual_ZN10QQuickItem6polishEv')

  @overload(QQmlV4Function)
  @overload(NoneType)
  def mapFromItem(self, a0: Optional[QQmlV4Function]) -> None:
    """
    Calls Qt's 'void QQuickItem::mapFromItem(QQmlV4FunctionPtr a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#mapFromItem

    Parameters
    ----------

    a0 : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItem::mapFromItem(QQmlV4FunctionPtr a0) const
    self.uglySide.call(
        'ritual_ZNK10QQuickItem11mapFromItemEP14QQmlV4Function',
        self._addressOf(a0),
    )

  @overload(THIS, QPointF)
  @overload(NoneType, QPointF)
  def mapFromItem(
      self,
      item: Optional[QQuickItem],
      point: QPointF,
  ) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickItem::mapFromItem(const QQuickItem *item, const
    QPointF &point) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#mapFromItem

    Parameters
    ----------

    item : Optional[QQuickItem]
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
    #  QPointF QQuickItem::mapFromItem(const QQuickItem *item, const QPointF
    #      &point) const
    address = self.uglySide.call(
        'ritual_ZNK10QQuickItem11mapFromItemEPKS_RK7QPointF',
        self._addressOf(item), self._valueOf(point, 'QPointF'),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(THIS, float, float)
  @overload(NoneType, float, float)
  def mapFromItem(
      self,
      item: Optional[QQuickItem],
      x: float,
      y: float,
  ) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickItem::mapFromItem(const QQuickItem *item, qreal
    x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#mapFromItem

    Parameters
    ----------

    item : Optional[QQuickItem]
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
    #  QPointF QQuickItem::mapFromItem(const QQuickItem *item, qreal x, qreal
    #      y)
    address = self.uglySide.call(
        'ritual_ZN10QQuickItem11mapFromItemEPKS_dd',
        self._addressOf(item), x, y,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(THIS, QRectF)
  @overload(NoneType, QRectF)
  def mapFromItem(self, item: Optional[QQuickItem], rect: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickItem::mapFromItem(const QQuickItem *item, const
    QRectF &rect) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#mapFromItem

    Parameters
    ----------

    item : Optional[QQuickItem]
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
    #  QRectF QQuickItem::mapFromItem(const QQuickItem *item, const QRectF
    #      &rect) const
    address = self.uglySide.call(
        'ritual_ZNK10QQuickItem11mapFromItemEPKS_RK6QRectF',
        self._addressOf(item), self._valueOf(rect),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(THIS, float, float, float, float)
  @overload(NoneType, float, float, float, float)
  def mapFromItem(
      self,
      item: Optional[QQuickItem],
      x: float,
      y: float,
      width: float,
      height: float,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickItem::mapFromItem(const QQuickItem *item, qreal
    x, qreal y, qreal width, qreal height) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#mapFromItem

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    width : float
      Passed on as it is.

    height : float
      Passed on as it is.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickItem::mapFromItem(const QQuickItem *item, qreal x, qreal
    #      y, qreal width, qreal height) const
    address = self.uglySide.call(
        'ritual_ZNK10QQuickItem11mapFromItemEPKS_dddd',
        self._addressOf(item), x, y, width, height,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QQmlV4Function)
  @overload(NoneType)
  def mapToItem(self, a0: Optional[QQmlV4Function]) -> None:
    """
    Calls Qt's 'void QQuickItem::mapToItem(QQmlV4FunctionPtr a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#mapToItem

    Parameters
    ----------

    a0 : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItem::mapToItem(QQmlV4FunctionPtr a0) const
    self.uglySide.call(
        'ritual_ZNK10QQuickItem9mapToItemEP14QQmlV4Function',
        self._addressOf(a0),
    )

  @overload(THIS, QPointF)
  @overload(NoneType, QPointF)
  def mapToItem(self, item: Optional[QQuickItem], point: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickItem::mapToItem(const QQuickItem *item, const
    QPointF &point) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#mapToItem

    Parameters
    ----------

    item : Optional[QQuickItem]
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
    #  QPointF QQuickItem::mapToItem(const QQuickItem *item, const QPointF
    #      &point) const
    address = self.uglySide.call(
        'ritual_ZNK10QQuickItem9mapToItemEPKS_RK7QPointF',
        self._addressOf(item), self._valueOf(point, 'QPointF'),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(THIS, float, float)
  @overload(NoneType, float, float)
  def mapToItem(
      self,
      item: Optional[QQuickItem],
      x: float,
      y: float,
  ) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickItem::mapToItem(const QQuickItem *item, qreal
    x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#mapToItem

    Parameters
    ----------

    item : Optional[QQuickItem]
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
    #  QPointF QQuickItem::mapToItem(const QQuickItem *item, qreal x, qreal
    #      y)
    address = self.uglySide.call(
        'ritual_ZN10QQuickItem9mapToItemEPKS_dd',
        self._addressOf(item), x, y,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(THIS, QRectF)
  @overload(NoneType, QRectF)
  def mapToItem(self, item: Optional[QQuickItem], rect: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickItem::mapToItem(const QQuickItem *item, const
    QRectF &rect) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#mapToItem

    Parameters
    ----------

    item : Optional[QQuickItem]
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
    #  QRectF QQuickItem::mapToItem(const QQuickItem *item, const QRectF
    #      &rect) const
    address = self.uglySide.call(
        'ritual_ZNK10QQuickItem9mapToItemEPKS_RK6QRectF',
        self._addressOf(item), self._valueOf(rect),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(THIS, float, float, float, float)
  @overload(NoneType, float, float, float, float)
  def mapToItem(
      self,
      item: Optional[QQuickItem],
      x: float,
      y: float,
      width: float,
      height: float,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickItem::mapToItem(const QQuickItem *item, qreal x,
    qreal y, qreal width, qreal height) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#mapToItem

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    width : float
      Passed on as it is.

    height : float
      Passed on as it is.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickItem::mapToItem(const QQuickItem *item, qreal x, qreal y,
    #      qreal width, qreal height) const
    address = self.uglySide.call(
        'ritual_ZNK10QQuickItem9mapToItemEPKS_dddd',
        self._addressOf(item), x, y, width, height,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QQmlV4Function)
  @overload(NoneType)
  def mapFromGlobal(self, a0: Optional[QQmlV4Function]) -> None:
    """
    Calls Qt's 'void QQuickItem::mapFromGlobal(QQmlV4FunctionPtr a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#mapFromGlobal

    Parameters
    ----------

    a0 : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItem::mapFromGlobal(QQmlV4FunctionPtr a0) const
    self.uglySide.call(
        'ritual_ZNK10QQuickItem13mapFromGlobalEP14QQmlV4Function',
        self._addressOf(a0),
    )

  @overload(float, float)
  def mapFromGlobal(self, x: float, y: float) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickItem::mapFromGlobal(qreal x, qreal y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#mapFromGlobal

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
    #  QPointF QQuickItem::mapFromGlobal(qreal x, qreal y) const
    address = self.uglySide.call(
        'ritual_ZNK10QQuickItem13mapFromGlobalEdd', x, y,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QPointF)
  def mapFromGlobal(self, point: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickItem::mapFromGlobal(const QPointF &point)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#mapFromGlobal

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
    #  QPointF QQuickItem::mapFromGlobal(const QPointF &point) const
    address = self.uglySide.call(
        'ritual_ZNK10QQuickItem13mapFromGlobalERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QQmlV4Function)
  @overload(NoneType)
  def mapToGlobal(self, a0: Optional[QQmlV4Function]) -> None:
    """
    Calls Qt's 'void QQuickItem::mapToGlobal(QQmlV4FunctionPtr a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#mapToGlobal

    Parameters
    ----------

    a0 : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItem::mapToGlobal(QQmlV4FunctionPtr a0) const
    self.uglySide.call(
        'ritual_ZNK10QQuickItem11mapToGlobalEP14QQmlV4Function',
        self._addressOf(a0),
    )

  @overload(float, float)
  def mapToGlobal(self, x: float, y: float) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickItem::mapToGlobal(qreal x, qreal y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#mapToGlobal

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
    #  QPointF QQuickItem::mapToGlobal(qreal x, qreal y) const
    address = self.uglySide.call(
        'ritual_ZNK10QQuickItem11mapToGlobalEdd', x, y,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QPointF)
  def mapToGlobal(self, point: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickItem::mapToGlobal(const QPointF &point) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#mapToGlobal

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
    #  QPointF QQuickItem::mapToGlobal(const QPointF &point) const
    address = self.uglySide.call(
        'ritual_ZNK10QQuickItem11mapToGlobalERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload()
  def forceActiveFocus(self) -> None:
    """
    Calls Qt's 'void QQuickItem::forceActiveFocus()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#forceActiveFocus
    """
    #  void QQuickItem::forceActiveFocus()
    self.uglySide.call('ritual_ZN10QQuickItem16forceActiveFocusEv')

  @overload(Qt.FocusReason)
  def forceActiveFocus(self, reason: Qt.FocusReason) -> None:
    """
    Calls Qt's 'void QQuickItem::forceActiveFocus(Qt::FocusReason reason)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#forceActiveFocus

    Parameters
    ----------

    reason : Qt.FocusReason
      Passed on as its number.
    """
    #  void QQuickItem::forceActiveFocus(Qt::FocusReason reason)
    self.uglySide.call(
        'ritual_ZN10QQuickItem16forceActiveFocusEN2Qt11FocusReasonE',
        reason.value,
    )

  @overload()
  @overload(bool)
  def nextItemInFocusChain(
      self,
      forward: bool = True,
  ) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickItem::nextItemInFocusChain(bool forward)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitem.html#nextItemInFocusChain

    Parameters
    ----------

    forward : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickItem::nextItemInFocusChain(bool forward)
    address = self.uglySide.call(
        'ritual_ZN10QQuickItem20nextItemInFocusChainEb', forward,
    )
    return QQuickItem._cuteAt(address)

  def ensurePolished(self) -> None:
    """
    Calls Qt's 'void QQuickItem::ensurePolished()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#ensurePolished
    """
    #  void QQuickItem::ensurePolished()
    self.uglySide.call('ritual_ZN10QQuickItem14ensurePolishedEv')

  def dumpItemTree(self) -> None:
    """
    Calls Qt's 'void QQuickItem::dumpItemTree() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#dumpItemTree
    """
    #  void QQuickItem::dumpItemTree() const
    self.uglySide.call('ritual_ZNK10QQuickItem12dumpItemTreeEv')

  def update(self) -> None:
    """
    Calls Qt's 'void QQuickItem::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#update
    """
    #  void QQuickItem::update()
    self.uglySide.call('ritual_ZN10QQuickItem6updateEv')

  @overload(QRectF)
  def childrenRectChanged(self, a0: QRectF) -> None:
    """
    Calls Qt's 'void QQuickItem::childrenRectChanged(const QRectF &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitem.html#childrenRectChanged

    Parameters
    ----------

    a0 : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickItem::childrenRectChanged(const QRectF &a0)
    self.uglySide.call(
        'ritual_ZN10QQuickItem19childrenRectChangedERK6QRectF',
        self._valueOf(a0),
    )

  @overload(float)
  def baselineOffsetChanged(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickItem::baselineOffsetChanged(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitem.html#baselineOffsetChanged

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickItem::baselineOffsetChanged(qreal a0)
    self.uglySide.call('ritual_ZN10QQuickItem21baselineOffsetChangedEd', a0)

  @overload(str)
  def stateChanged(self, a0: str) -> None:
    """
    Calls Qt's 'void QQuickItem::stateChanged(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#stateChanged

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickItem::stateChanged(const QString &a0)
    self.uglySide.call('ritual_ZN10QQuickItem12stateChangedERK7QString', a0)

  @overload(bool)
  def focusChanged(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickItem::focusChanged(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#focusChanged

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickItem::focusChanged(bool a0)
    self.uglySide.call('ritual_ZN10QQuickItem12focusChangedEb', a0)

  @overload(bool)
  def activeFocusChanged(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickItem::activeFocusChanged(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#activeFocusChanged

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickItem::activeFocusChanged(bool a0)
    self.uglySide.call('ritual_ZN10QQuickItem18activeFocusChangedEb', a0)

  @overload(Qt.FocusPolicy)
  def focusPolicyChanged(self, a0: Qt.FocusPolicy) -> None:
    """
    Calls Qt's 'void QQuickItem::focusPolicyChanged(Qt::FocusPolicy a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#focusPolicyChanged

    Parameters
    ----------

    a0 : Qt.FocusPolicy
      Passed on as its number.
    """
    #  void QQuickItem::focusPolicyChanged(Qt::FocusPolicy a0)
    self.uglySide.call(
        'ritual_ZN10QQuickItem18focusPolicyChangedEN2Qt11FocusPolicyE',
        a0.value,
    )

  @overload(bool)
  def activeFocusOnTabChanged(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickItem::activeFocusOnTabChanged(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitem.html#activeFocusOnTabChanged

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickItem::activeFocusOnTabChanged(bool a0)
    self.uglySide.call(
        'ritual_ZN10QQuickItem23activeFocusOnTabChangedEb', a0,
    )

  @overload(THIS)
  @overload(NoneType)
  def parentChanged(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickItem::parentChanged(QQuickItem *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#parentChanged

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItem::parentChanged(QQuickItem *a0)
    self.uglySide.call(
        'ritual_ZN10QQuickItem13parentChangedEPS_', self._addressOf(a0),
    )

  @overload(TransformOrigin)
  def transformOriginChanged(self, a0: TransformOrigin) -> None:
    """
    Calls Qt's 'void QQuickItem::transformOriginChanged(TransformOrigin a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitem.html#transformOriginChanged

    Parameters
    ----------

    a0 : TransformOrigin
      Passed on as its number.
    """
    #  void QQuickItem::transformOriginChanged(TransformOrigin a0)
    self.uglySide.call(
        'ritual_ZN10QQuickItem22transformOriginChangedENS_15TransformOrigin'
        'E',
        a0.value,
    )

  @overload(bool)
  def smoothChanged(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickItem::smoothChanged(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#smoothChanged

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickItem::smoothChanged(bool a0)
    self.uglySide.call('ritual_ZN10QQuickItem13smoothChangedEb', a0)

  @overload(bool)
  def antialiasingChanged(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickItem::antialiasingChanged(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitem.html#antialiasingChanged

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickItem::antialiasingChanged(bool a0)
    self.uglySide.call('ritual_ZN10QQuickItem19antialiasingChangedEb', a0)

  @overload(bool)
  def clipChanged(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickItem::clipChanged(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#clipChanged

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickItem::clipChanged(bool a0)
    self.uglySide.call('ritual_ZN10QQuickItem11clipChangedEb', a0)

  @overload(QQuickWindow)
  @overload(NoneType)
  def windowChanged(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QQuickItem::windowChanged(QQuickWindow *window)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#windowChanged

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItem::windowChanged(QQuickWindow *window)
    self.uglySide.call(
        'ritual_ZN10QQuickItem13windowChangedEP12QQuickWindow',
        self._addressOf(window),
    )

  def childrenChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItem::childrenChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#childrenChanged
    """
    #  void QQuickItem::childrenChanged()
    self.uglySide.call('ritual_ZN10QQuickItem15childrenChangedEv')

  def opacityChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItem::opacityChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#opacityChanged
    """
    #  void QQuickItem::opacityChanged()
    self.uglySide.call('ritual_ZN10QQuickItem14opacityChangedEv')

  def enabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItem::enabledChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#enabledChanged
    """
    #  void QQuickItem::enabledChanged()
    self.uglySide.call('ritual_ZN10QQuickItem14enabledChangedEv')

  def visibleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItem::visibleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#visibleChanged
    """
    #  void QQuickItem::visibleChanged()
    self.uglySide.call('ritual_ZN10QQuickItem14visibleChangedEv')

  def visibleChildrenChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItem::visibleChildrenChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitem.html#visibleChildrenChanged
    """
    #  void QQuickItem::visibleChildrenChanged()
    self.uglySide.call('ritual_ZN10QQuickItem22visibleChildrenChangedEv')

  def rotationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItem::rotationChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#rotationChanged
    """
    #  void QQuickItem::rotationChanged()
    self.uglySide.call('ritual_ZN10QQuickItem15rotationChangedEv')

  def scaleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItem::scaleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#scaleChanged
    """
    #  void QQuickItem::scaleChanged()
    self.uglySide.call('ritual_ZN10QQuickItem12scaleChangedEv')

  def xChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItem::xChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#xChanged
    """
    #  void QQuickItem::xChanged()
    self.uglySide.call('ritual_ZN10QQuickItem8xChangedEv')

  def yChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItem::yChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#yChanged
    """
    #  void QQuickItem::yChanged()
    self.uglySide.call('ritual_ZN10QQuickItem8yChangedEv')

  def widthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItem::widthChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#widthChanged
    """
    #  void QQuickItem::widthChanged()
    self.uglySide.call('ritual_ZN10QQuickItem12widthChangedEv')

  def heightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItem::heightChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#heightChanged
    """
    #  void QQuickItem::heightChanged()
    self.uglySide.call('ritual_ZN10QQuickItem13heightChangedEv')

  def zChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItem::zChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#zChanged
    """
    #  void QQuickItem::zChanged()
    self.uglySide.call('ritual_ZN10QQuickItem8zChangedEv')

  def implicitWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItem::implicitWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitem.html#implicitWidthChanged
    """
    #  void QQuickItem::implicitWidthChanged()
    self.uglySide.call('ritual_ZN10QQuickItem20implicitWidthChangedEv')

  def implicitHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItem::implicitHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitem.html#implicitHeightChanged
    """
    #  void QQuickItem::implicitHeightChanged()
    self.uglySide.call('ritual_ZN10QQuickItem21implicitHeightChangedEv')

  def containmentMaskChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItem::containmentMaskChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitem.html#containmentMaskChanged
    """
    #  void QQuickItem::containmentMaskChanged()
    self.uglySide.call('ritual_ZN10QQuickItem22containmentMaskChangedEv')

  def paletteChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItem::paletteChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#paletteChanged
    """
    #  void QQuickItem::paletteChanged()
    self.uglySide.call('ritual_ZN10QQuickItem14paletteChangedEv')

  def paletteCreated(self) -> None:
    """
    Calls Qt's 'void QQuickItem::paletteCreated()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#paletteCreated
    """
    #  void QQuickItem::paletteCreated()
    self.uglySide.call('ritual_ZN10QQuickItem14paletteCreatedEv')

  @overload(int)
  def mutabilityGroupChanged(self, group: int) -> None:
    """
    Calls Qt's 'void QQuickItem::mutabilityGroupChanged(int group)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitem.html#mutabilityGroupChanged

    Parameters
    ----------

    group : int
      Passed on as it is.
    """
    #  void QQuickItem::mutabilityGroupChanged(int group)
    self.uglySide.call(
        'ritual_ZN10QQuickItem22mutabilityGroupChangedEi', group,
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickItem::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickItem::event(QEvent *a0)
    ritual = 'ritual_ZN10QQuickItem5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickItem5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(ItemChange, ItemChangeData)
  def itemChange(self, a0: ItemChange, a1: ItemChangeData) -> None:
    """
    Calls Qt's 'void QQuickItem::itemChange(ItemChange a0, const
    ItemChangeData &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#itemChange

    Parameters
    ----------

    a0 : ItemChange
      Passed on as its number.

    a1 : ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickItem::itemChange(ItemChange a0, const ItemChangeData &a1)
    ritual = (
        'ritual_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChang'
        'eDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14Ite'
          'mChangeDataE')
    self.uglySide.call(ritual, a0.value, self._valueOf(a1))

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickItem::geometryChange(const QRectF &newGeometry,
    const QRectF &oldGeometry)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickItem::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN10QQuickItem14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickItem14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload()
  @overload(Qt.InputMethodQueries)
  def updateInputMethod(
      self,
      queries: Qt.InputMethodQueries = Qt.InputMethodQueries.ImQueryInput,
  ) -> None:
    """
    Calls Qt's 'void QQuickItem::updateInputMethod(Qt::InputMethodQueries
    queries)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#updateInputMethod

    Parameters
    ----------

    queries : Qt.InputMethodQueries
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.InputMethodQueries.ImQueryInput.
    """
    #  void QQuickItem::updateInputMethod(Qt::InputMethodQueries queries)
    self.uglySide.call(
        'ritual_ZN10QQuickItem17updateInputMethodE6QFlagsIN2Qt16InputMethod'
        'QueryEE',
        queries.value,
    )

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickItem::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#classBegin
    """
    #  void QQuickItem::classBegin()
    ritual = 'ritual_ZN10QQuickItem10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickItem10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickItem::componentComplete()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#componentComplete
    """
    #  void QQuickItem::componentComplete()
    ritual = 'ritual_ZN10QQuickItem17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickItem17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickItem::keyPressEvent(QKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#keyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItem::keyPressEvent(QKeyEvent *event)
    ritual = 'ritual_ZN10QQuickItem13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickItem13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickItem::keyReleaseEvent(QKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#keyReleaseEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
    ritual = 'ritual_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QInputMethodEvent)
  @overload(NoneType)
  def inputMethodEvent(self, a0: Optional[QInputMethodEvent]) -> None:
    """
    Calls Qt's 'void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#inputMethodEvent

    Parameters
    ----------

    a0 : Optional[QInputMethodEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
    ritual = 'ritual_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, a0: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QQuickItem::focusInEvent(QFocusEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#focusInEvent

    Parameters
    ----------

    a0 : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItem::focusInEvent(QFocusEvent *a0)
    ritual = 'ritual_ZN10QQuickItem12focusInEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickItem12focusInEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, a0: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QQuickItem::focusOutEvent(QFocusEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#focusOutEvent

    Parameters
    ----------

    a0 : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItem::focusOutEvent(QFocusEvent *a0)
    ritual = 'ritual_ZN10QQuickItem13focusOutEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickItem13focusOutEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickItem::mousePressEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItem::mousePressEvent(QMouseEvent *event)
    ritual = 'ritual_ZN10QQuickItem15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickItem15mousePressEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickItem::mouseMoveEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
    ritual = 'ritual_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickItem::mouseReleaseEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
    ritual = 'ritual_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitem.html#mouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
    ritual = 'ritual_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  def mouseUngrabEvent(self) -> None:
    """
    Calls Qt's 'void QQuickItem::mouseUngrabEvent()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#mouseUngrabEvent
    """
    #  void QQuickItem::mouseUngrabEvent()
    ritual = 'ritual_ZN10QQuickItem16mouseUngrabEventEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickItem16mouseUngrabEventEv'
    self.uglySide.call(ritual)

  def touchUngrabEvent(self) -> None:
    """
    Calls Qt's 'void QQuickItem::touchUngrabEvent()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#touchUngrabEvent
    """
    #  void QQuickItem::touchUngrabEvent()
    ritual = 'ritual_ZN10QQuickItem16touchUngrabEventEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickItem16touchUngrabEventEv'
    self.uglySide.call(ritual)

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, event: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void QQuickItem::wheelEvent(QWheelEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#wheelEvent

    Parameters
    ----------

    event : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItem::wheelEvent(QWheelEvent *event)
    ritual = 'ritual_ZN10QQuickItem10wheelEventEP11QWheelEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickItem10wheelEventEP11QWheelEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QTouchEvent)
  @overload(NoneType)
  def touchEvent(self, event: Optional[QTouchEvent]) -> None:
    """
    Calls Qt's 'void QQuickItem::touchEvent(QTouchEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#touchEvent

    Parameters
    ----------

    event : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItem::touchEvent(QTouchEvent *event)
    ritual = 'ritual_ZN10QQuickItem10touchEventEP11QTouchEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickItem10touchEventEP11QTouchEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverEnterEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickItem::hoverEnterEvent(QHoverEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#hoverEnterEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
    ritual = 'ritual_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverMoveEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickItem::hoverMoveEvent(QHoverEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#hoverMoveEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
    ritual = 'ritual_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverLeaveEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickItem::hoverLeaveEvent(QHoverEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#hoverLeaveEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
    ritual = 'ritual_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDragEnterEvent)
  @overload(NoneType)
  def dragEnterEvent(self, a0: Optional[QDragEnterEvent]) -> None:
    """
    Calls Qt's 'void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#dragEnterEvent

    Parameters
    ----------

    a0 : Optional[QDragEnterEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
    ritual = 'ritual_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QDragMoveEvent)
  @overload(NoneType)
  def dragMoveEvent(self, a0: Optional[QDragMoveEvent]) -> None:
    """
    Calls Qt's 'void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#dragMoveEvent

    Parameters
    ----------

    a0 : Optional[QDragMoveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
    ritual = 'ritual_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QDragLeaveEvent)
  @overload(NoneType)
  def dragLeaveEvent(self, a0: Optional[QDragLeaveEvent]) -> None:
    """
    Calls Qt's 'void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#dragLeaveEvent

    Parameters
    ----------

    a0 : Optional[QDragLeaveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
    ritual = 'ritual_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QDropEvent)
  @overload(NoneType)
  def dropEvent(self, a0: Optional[QDropEvent]) -> None:
    """
    Calls Qt's 'void QQuickItem::dropEvent(QDropEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#dropEvent

    Parameters
    ----------

    a0 : Optional[QDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItem::dropEvent(QDropEvent *a0)
    ritual = 'ritual_ZN10QQuickItem9dropEventEP10QDropEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickItem9dropEventEP10QDropEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(THIS, QEvent)
  @overload(THIS, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def childMouseEventFilter(
      self,
      a0: Optional[QQuickItem],
      a1: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent
    *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitem.html#childMouseEventFilter

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
    ritual = 'ritual_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent'
    return self.uglySide.call(
        ritual, self._addressOf(a0), self._addressOf(a1),
    )

  @overload(QSGNode, UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updatePaintNode(
      self,
      a0: Optional[QSGNode],
      a1: Optional[UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QQuickItem::updatePaintNode(QSGNode *a0,
    UpdatePaintNodeData *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#updatePaintNode

    Parameters
    ----------

    a0 : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[UpdatePaintNodeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QQuickItem::updatePaintNode(QSGNode *a0, UpdatePaintNodeData
    #      *a1)
    ritual = (
        'ritual_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintN'
        'odeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19Update'
          'PaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(a0, 'QSGNode'), self._addressOf(a1),
    )
    from . import QSGNode
    return QSGNode._cuteAt(address)

  def releaseResources(self) -> None:
    """
    Calls Qt's 'void QQuickItem::releaseResources()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#releaseResources
    """
    #  void QQuickItem::releaseResources()
    ritual = 'ritual_ZN10QQuickItem16releaseResourcesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickItem16releaseResourcesEv'
    self.uglySide.call(ritual)

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QQuickItem::updatePolish()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#updatePolish
    """
    #  void QQuickItem::updatePolish()
    ritual = 'ritual_ZN10QQuickItem12updatePolishEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickItem12updatePolishEv'
    self.uglySide.call(ritual)

  def d_func(self) -> Optional[QQuickItemPrivate]:
    """
    Calls Qt's 'QQuickItemPrivate *QQuickItem::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitem.html#d_func

    Returns
    -------

    Optional[QQuickItemPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItemPrivate *QQuickItem::d_func()
    address = self.uglySide.call('ritual_ZN10QQuickItem6d_funcEv')
    from . import QQuickItemPrivate
    return QQuickItemPrivate._cuteAt(address)

  @staticmethod
  def bindableHeight(*__, **_) -> Never:
    """
    Qt's 'QBindable<qreal> QQuickItem::bindableHeight()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickItem.bindableHeight' has no cute function yet. Qt's "
        "'QBindable<qreal> QQuickItem::bindableHeight()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def bindableWidth(*__, **_) -> Never:
    """
    Qt's 'QBindable<qreal> QQuickItem::bindableWidth()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickItem.bindableWidth' has no cute function yet. Qt's "
        "'QBindable<qreal> QQuickItem::bindableWidth()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def bindableX(*__, **_) -> Never:
    """
    Qt's 'QBindable<qreal> QQuickItem::bindableX()': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickItem.bindableX' has no cute function yet. Qt's "
        "'QBindable<qreal> QQuickItem::bindableX()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def bindableY(*__, **_) -> Never:
    """
    Qt's 'QBindable<qreal> QQuickItem::bindableY()': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickItem.bindableY' has no cute function yet. Qt's "
        "'QBindable<qreal> QQuickItem::bindableY()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def grabTouchPoints(*__, **_) -> Never:
    """
    Qt's 'void QQuickItem::grabTouchPoints(const QList<int> &ids)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickItem.grabTouchPoints' has no cute function yet. Qt's 'void "
        "QQuickItem::grabTouchPoints(const QList<int> &ids)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def itemTransform(*__, **_) -> Never:
    """
    Qt's 'QTransform QQuickItem::itemTransform(QQuickItem *a0, bool *a1)
    const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QQuickItem.itemTransform' has no cute function yet. Qt's "
        "'QTransform QQuickItem::itemTransform(QQuickItem *a0, bool *a1) "
        "const': takes a number to change where it is.")

  @staticmethod
  def transform(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickTransform> QQuickItem::transform()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickItem.transform' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuickTransform> QQuickItem::transform()': gives "
        "a type Python has no way to take yet.")


#  Qt's 'QList<QQuickItem *>': the list of QQuickItem, which
#  'QList[QQuickItem]' gives. It is made here, so that there is one as soon
#  as there can be a QQuickItem.
QList.createKind(
    QQuickItem, 'address',
    make='ritual_list_make_QQuickItem_ptr',
    add='ritual_list_add_QQuickItem_ptr',
    size='ritual_list_size_QQuickItem_ptr',
    at='ritual_list_at_QQuickItem_ptr',
    drop='ritual_list_drop_QQuickItem_ptr',
)
