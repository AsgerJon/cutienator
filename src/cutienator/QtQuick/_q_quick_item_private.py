"""
QQuickItemPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickitem_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickItemPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QEvent, QList, QObjectPrivate
from ..QtGui import QAccessible
from ..QtQml import QV4
from . import QQuickItem, QtPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QObject, QPoint, QPointF, QRectF
  from ..QtGui import QContextMenuEvent, QCursor, QEventPoint
  from ..QtGui import QInputMethodEvent, QKeyEvent, QLayoutPolicy
  from ..QtGui import QMutableTouchEvent, QPointerEvent, QTouchEvent
  from ..QtGui import QTransform, QVector2D, QWindow
  from . import QQuickAnchorLine, QQuickAnchors, QQuickDefaultClipNode
  from . import QQuickDeliveryAgent, QQuickDeliveryAgentPrivate
  from . import QQuickGeometryChange, QQuickItemChangeListener
  from . import QQuickItemLayer, QQuickPointerHandler, QQuickStateGroup
  from . import QQuickWindow, QSGContext, QSGNode, QSGOpacityNode
  from . import QSGRenderContext, QSGRootNode, QSGTransformNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QContextMenuEvent = WAIT['QContextMenuEvent']
  QEventPoint = WAIT['QEventPoint']
  QInputMethodEvent = WAIT['QInputMethodEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QMetaObject = WAIT['QMetaObject']
  QMutableTouchEvent = WAIT['QMutableTouchEvent']
  QObject = WAIT['QObject']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QPointerEvent = WAIT['QPointerEvent']
  QQuickGeometryChange = WAIT['QQuickGeometryChange']
  QQuickItemChangeListener = WAIT['QQuickItemChangeListener']
  QQuickPointerHandler = WAIT['QQuickPointerHandler']
  QQuickWindow = WAIT['QQuickWindow']
  QRectF = WAIT['QRectF']
  QTouchEvent = WAIT['QTouchEvent']
  QTransform = WAIT['QTransform']
  QVector2D = WAIT['QVector2D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickItemPrivate(QObjectPrivate):
  """
  The cute side of Qt's QQuickItemPrivate: a plain Python object standing in
  front of one C++ QQuickItemPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QQuickItemPrivate is
  built on Qt's QObjectPrivate, and has everything that class has. Qt's
  QQuickItemPrivate is built on Qt's
  QQuickPaletteProviderPrivateBase<QQuickItem, QQuickItemPrivate> as well,
  which is not reflected.

  What exists
  -----------

  Every function of Qt's QQuickItemPrivate that has a ritual and that Python
  can call so far, 136 names in all: 'q_func', 'get', 'init', 'state',
  'setState', 'left', 'right', 'horizontalCenter', 'top', 'bottom',
  'verticalCenter', 'baseline', 'layer', 'localizedTouchEvent',
  'hasPointerHandlers', 'hasEnabledHoverHandlers', 'addPointerHandler',
  'removePointerHandler', 'setContextMenu',
  'attachedPropertyPropagator_parent', '_q_resourceObjectDeleted',
  '_q_createJSWrapper', 'registerAsContainmentMask', 'anchors',
  'acceptedMouseButtons', 'addItemChangeListener',
  'updateOrAddItemChangeListener', 'removeItemChangeListener',
  'updateOrAddGeometryChangeListener',
  'updateOrRemoveGeometryChangeListener', '_states', 'origin',
  'requestCustomOverlay', 'dirtyToString', 'dirty', 'addToDirtyList',
  'removeFromDirtyList', 'setCulled', 'renderWindow', 'sceneGraphContext',
  'sceneGraphRenderContext', 'paintOrderChildItems', 'addChild',
  'removeChild', 'siblingOrderChanged', 'markSortedChildrenDirty',
  'refWindow', 'derefWindow', 'effectiveDevicePixelRatio',
  'updateSubFocusItem', 'setFocusIfNeeded', 'lastFocusChangeReason',
  'setLastFocusChangeReason', 'windowToItemTransform',
  'itemToWindowTransform', 'itemToParentTransform', 'focusNextPrev',
  'nextTabChildItem', 'prevTabChildItem', 'nextPrevItemInTabFocusChain',
  'canAcceptTabFocus', 'setX', 'xChanged', '_qt_property_x_offset', 'setY',
  'yChanged', '_qt_property_y_offset', 'setWidth', 'widthChanged',
  '_qt_property_width_offset', 'setHeight', 'heightChanged',
  '_qt_property_height_offset', 'widthValid', 'heightValid', 'z', 'scale',
  'rotation', 'opacity', 'setAccessible', 'getImplicitWidth',
  'getImplicitHeight', 'implicitWidthChanged', 'implicitHeightChanged',
  'effectiveAccessibleRole', 'accessibleRole', 'setImplicitAntialiasing',
  'resolveLayoutMirror', 'setImplicitLayoutMirror', 'setLayoutMirror',
  'isMirrored', 'emitChildrenRectChanged', 'computeTransformOrigin',
  'transformChanged', 'adjustedPosForTransform', 'deliveryAgent',
  'deliveryAgentPrivate', 'ensureSubsceneDeliveryAgent', 'deliverKeyEvent',
  'filterKeyEvent', 'deliverInputMethodEvent',
  'deliverShortcutOverrideEvent', 'deliverPointerEvent',
  'anyPointerHandlerWants', 'handlePointerEvent', 'handleContextMenuEvent',
  'setVisible', 'isTransparentForPositioner', 'setTransparentForPositioner',
  'calcEffectiveVisible', 'setEffectiveVisibleRecur', 'calcEffectiveEnable',
  'setEffectiveEnableRecur', 'biggestPointerHandlerMargin',
  'eventHandlingBounds', 'parentFullyContains',
  'effectivelyClipsEventHandlingChildren', 'itemNode', 'childContainerNode',
  'opacityNode', 'clipNode', 'rootNode', 'createTransformNode',
  'refFromEffectItem', 'recursiveRefFromEffectItem', 'derefFromEffectItem',
  'itemChange', 'enableSubtreeChangeNotificationsForParentHierachy',
  'mirrorChange', 'setHasCursorInChild', 'setHasHoverInChild',
  'effectiveCursor', 'effectiveCursorHandler', 'updatePolish',
  'dumpItemTree', 'sizePolicy'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickItem *QQuickItemPrivate::q_func() const': takes in
    Python what 'QQuickItem *QQuickItemPrivate::q_func()' takes.
  - Qt's 'const QQuickItemPrivate *QQuickItemPrivate::get(const QQuickItem
    *item)': takes in Python what 'QQuickItemPrivate
    *QQuickItemPrivate::get(QQuickItem *item)' takes.
  - Qt's 'QQuickItemPrivate::~QQuickItemPrivate()': the destructor: Python
    never removes a C++ QQuickItemPrivate.
  - Qt's 'QQmlListProperty<QObject> QQuickItemPrivate::data()': gives a type
    Python has no way to take yet.
  - Qt's 'QQmlListProperty<QObject> QQuickItemPrivate::resources()': gives a
    type Python has no way to take yet.
  - Qt's 'QQmlListProperty<QQuickItem> QQuickItemPrivate::children()': gives
    a type Python has no way to take yet.
  - Qt's 'QQmlListProperty<QQuickItem> QQuickItemPrivate::visibleChildren()':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlListProperty<QQuickState> QQuickItemPrivate::states()': gives a
    type Python has no way to take yet.
  - Qt's 'QQmlListProperty<QQuickTransition>
    QQuickItemPrivate::transitions()': gives a type Python has no way to take
    yet.
  - Qt's 'void QQuickItemPrivate::data_append(QQmlListProperty<QObject> *a0,
    QObject *a1)': names 'QQmlListProperty<QObject>', which has no cute class
    yet.
  - Qt's 'qsizetype QQuickItemPrivate::data_count(QQmlListProperty<QObject>
    *a0)': names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'QObject *QQuickItemPrivate::data_at(QQmlListProperty<QObject> *a0,
    qsizetype a1)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
  - Qt's 'void QQuickItemPrivate::data_clear(QQmlListProperty<QObject> *a0)':
    names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'void QQuickItemPrivate::data_removeLast(QQmlListProperty<QObject>
    *a0)': names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'QObject *QQuickItemPrivate::resources_at(QQmlListProperty<QObject>
    *a0, qsizetype a1)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
  - Qt's 'void QQuickItemPrivate::resources_append(QQmlListProperty<QObject>
    *a0, QObject *a1)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
  - Qt's 'qsizetype
    QQuickItemPrivate::resources_count(QQmlListProperty<QObject> *a0)': names
    'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'void QQuickItemPrivate::resources_clear(QQmlListProperty<QObject>
    *a0)': names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'void
    QQuickItemPrivate::resources_removeLast(QQmlListProperty<QObject> *a0)':
    names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'void
    QQuickItemPrivate::children_append(QQmlListProperty<QQuickItem> *a0,
    QQuickItem *a1)': names 'QQmlListProperty<QQuickItem>', which has no cute
    class yet.
  - Qt's 'qsizetype
    QQuickItemPrivate::children_count(QQmlListProperty<QQuickItem> *a0)':
    names 'QQmlListProperty<QQuickItem>', which has no cute class yet.
  - Qt's 'QQuickItem
    *QQuickItemPrivate::children_at(QQmlListProperty<QQuickItem> *a0,
    qsizetype a1)': names 'QQmlListProperty<QQuickItem>', which has no cute
    class yet.
  - Qt's 'void QQuickItemPrivate::children_clear(QQmlListProperty<QQuickItem>
    *a0)': names 'QQmlListProperty<QQuickItem>', which has no cute class yet.
  - Qt's 'void
    QQuickItemPrivate::children_removeLast(QQmlListProperty<QQuickItem>
    *a0)': names 'QQmlListProperty<QQuickItem>', which has no cute class yet.
  - Qt's 'qsizetype
    QQuickItemPrivate::visibleChildren_count(QQmlListProperty<QQuickItem>
    *prop)': names 'QQmlListProperty<QQuickItem>', which has no cute class
    yet.
  - Qt's 'QQuickItem
    *QQuickItemPrivate::visibleChildren_at(QQmlListProperty<QQuickItem>
    *prop, qsizetype index)': names 'QQmlListProperty<QQuickItem>', which has
    no cute class yet.
  - Qt's 'qsizetype
    QQuickItemPrivate::transform_count(QQmlListProperty<QQuickTransform>
    *list)': names 'QQmlListProperty<QQuickTransform>', which has no cute
    class yet.
  - Qt's 'void
    QQuickItemPrivate::transform_append(QQmlListProperty<QQuickTransform>
    *list, QQuickTransform *a1)': names 'QQmlListProperty<QQuickTransform>',
    which has no cute class yet.
  - Qt's 'QQuickTransform
    *QQuickItemPrivate::transform_at(QQmlListProperty<QQuickTransform> *list,
    qsizetype a1)': names 'QQmlListProperty<QQuickTransform>', which has no
    cute class yet.
  - Qt's 'void
    QQuickItemPrivate::transform_clear(QQmlListProperty<QQuickTransform>
    *list)': names 'QQmlListProperty<QQuickTransform>', which has no cute
    class yet.
  - Qt's 'QDebug &operator<<(QDebug &dbg, QQuickItemPrivate::ChangeTypes
    types)': an operator between other classes, written inside this one.
  - Qt's 'void QQuickItemPrivate::setSizePolicy(const QLayoutPolicy::Policy
    &horizontalPolicy, const QLayoutPolicy::Policy &verticalPolicy)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 170 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QQuickItemPrivate is created at the first use, not by
    'QQuickItemPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickItemPrivate.
  - Each name of Qt's QQuickItemPrivate that has no cute function yet,
    'children_append', 'children_at', 'children_clear', 'children_count',
    'children_removeLast', 'data', 'data_append', 'data_at', 'data_clear',
    'data_count', 'data_removeLast', 'notifyChangeListeners', 'resources',
    'resources_append', 'resources_at', 'resources_clear', 'resources_count',
    'resources_removeLast', 'setSizePolicy', 'states', 'transform_append',
    'transform_at', 'transform_clear', 'transform_count', 'transitions',
    'visibleChildren', 'visibleChildren_at', 'visibleChildren_count', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickItemPrivate, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ChangeType(CuteFlags, number='unsigned int'):
    """
    The flags enum 'QQuickItemPrivate::ChangeType' of Qt, with the 15 names
    Qt gives in it. Qt names the type of its combinations
    'QQuickItemPrivate::ChangeListener::ChangeTypes'.
    """

    Geometry = 0x1
    SiblingOrder = 0x2
    Visibility = 0x4
    Opacity = 0x8
    Destroyed = 0x10
    Parent = 0x20
    Children = 0x40
    Rotation = 0x80
    ImplicitWidth = 0x100
    ImplicitHeight = 0x200
    Enabled = 0x400
    Focus = 0x800
    Scale = 0x1000
    Matrix = 0x2000
    AllChanges = 0xffffffff

  ChangeTypes = ChangeType

  class DirtyType(CuteNum):
    """
    The enum 'QQuickItemPrivate::DirtyType' of Qt, with the 22 names Qt gives
    in it.
    """

    TransformOrigin = Kee[int](1)
    Transform = Kee[int](2)
    BasicTransform = Kee[int](4)
    Position = Kee[int](8)
    Size = Kee[int](16)
    ZValue = Kee[int](32)
    Content = Kee[int](64)
    Smooth = Kee[int](128)
    OpacityValue = Kee[int](256)
    ChildrenChanged = Kee[int](512)
    ChildrenStackingChanged = Kee[int](1024)
    ParentChanged = Kee[int](2048)
    Clip = Kee[int](4096)
    Window = Kee[int](8192)
    EffectReference = Kee[int](32768)
    Visible = Kee[int](65536)
    HideReference = Kee[int](131072)
    Antialiasing = Kee[int](262144)
    TransformUpdateMask = Kee[int](8207)
    ComplexTransformUpdateMask = Kee[int](8194)
    ContentUpdateMask = Kee[int](270544)
    ChildrenUpdateMask = Kee[int](42496)

  class ExtraDataTag(CuteFlags):
    """
    The flags enum 'QQuickItemPrivate::ExtraDataTag' of Qt, with the 2 names
    Qt gives in it. Qt names the type of its combinations
    'QQuickItemPrivate::ExtraDataTags'.
    """

    NoTag = 0x1
    LeftMouseButtonAccepted = 0x2

  ExtraDataTags = ExtraDataTag

  #  The classes Qt writes inside QQuickItemPrivate, each a class in here as
  #  in C++.

  class ChangeListener(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickItemPrivate::ChangeListener: a plain Python
    object standing in front of one C++ QQuickItemPrivate::ChangeListener.

    C++ hands a QQuickItemPrivate::ChangeListener around as a copy, so every
    C++ QQuickItemPrivate::ChangeListener behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QQuickItemPrivate::ChangeListener that has a
    ritual and that Python can call so far, 1 name in all: '__eq__'. It can
    be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickItemPrivate::ChangeListener::ChangeListener(
      QQuickItemChangeListener *l, ChangeTypes t)': names the enum
      'QQuickItemPrivate::ChangeType', whose class cannot be named here.
    - Qt's 'QQuickItemPrivate::ChangeListener::~ChangeListener()': the
      destructor: Python removes its C++ QQuickItemPrivate::ChangeListener by
      it, and has no other use for it.

    What has no ritual
    ------------------

    1 of the 5 functions Qt declares: 1 cannot be called and cannot be called
    through the meta-object and cannot be copied.

    What to expect
    --------------

    - The C++ QQuickItemPrivate::ChangeListener is created at the first use,
      not by 'QQuickItemPrivate::ChangeListener(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickItemPrivate::ChangeListener back gives a copy
      the ritual made for Python, in a new cute
      QQuickItemPrivate::ChangeListener.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QQuickGeometryChange = WAIT['QQuickGeometryChange']
      QQuickItemChangeListener = WAIT['QQuickItemChangeListener']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickItemPrivate::ChangeListener'

    #  Qt's '~QQuickItemPrivate::ChangeListener()'. Naming it makes this a
    #  value class: Python owns every C++ QQuickItemPrivate::ChangeListener
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN17QQuickItemPrivate14ChangeListenerD1Ev'

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

    @overload(THIS)
    def __eq__(self, other: QQuickItemPrivate.ChangeListener) -> bool:
      """
      Calls Qt's 'bool QQuickItemPrivate::ChangeListener::operator==(const
      ChangeListener &other) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickitemprivate-changelistener.html#operator==

      Parameters
      ----------

      other : QQuickItemPrivate.ChangeListener
        Passed on as a value: Qt reads the C++
        QQuickItemPrivate::ChangeListener, which stays Python's own.
      """
      #  bool QQuickItemPrivate::ChangeListener::operator==(const
      #      ChangeListener &other) const
      return self.uglySide.call(
          'ritual_ZNK17QQuickItemPrivate14ChangeListenereqERKS0_',
          self._valueOf(other),
      )

    @overload.fallback
    def __eq__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(QQuickItemChangeListener, QQuickGeometryChange)
    @overload(NoneType, QQuickGeometryChange)
    def __init__(
        self,
        l: Optional[QQuickItemChangeListener],
        gt: QQuickGeometryChange,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QQuickItemPrivate::ChangeListener::ChangeListener(
      QQuickItemChangeListener *l, QQuickGeometryChange gt)', which is called
      at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickitemprivate-changelistener.html

      Parameters
      ----------

      l : Optional[QQuickItemChangeListener]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      gt : QQuickGeometryChange
        Passed on as a value: Qt reads the C++ QQuickGeometryChange, which
        stays Python's own.
      """
      #  QQuickItemPrivate::ChangeListener::ChangeListener(
      #      QQuickItemChangeListener *l, QQuickGeometryChange gt)
      self._noteCreation(
          QQuickItemPrivate.ChangeListener, lambda: Rituals.call(
              'ritual_ZN17QQuickItemPrivate14ChangeListenerC1EP24QQuickItem'
              'ChangeListener20QQuickGeometryChange',
              self._addressOf(l, 'QQuickItemChangeListener'),
              self._valueOf(gt),
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

  class ExtraData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickItemPrivate::ExtraData: a plain Python object
    standing in front of one C++ QQuickItemPrivate::ExtraData.

    C++ hands a QQuickItemPrivate::ExtraData around as a copy, so every C++
    QQuickItemPrivate::ExtraData behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QQuickItemPrivate::ExtraData yet. It can be made from
    Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickItemPrivate::ExtraData::~ExtraData()': the destructor:
      Python removes its C++ QQuickItemPrivate::ExtraData by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QQuickItemPrivate::ExtraData is created at the first use, not
      by 'QQuickItemPrivate::ExtraData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickItemPrivate::ExtraData back gives a copy the
      ritual made for Python, in a new cute QQuickItemPrivate::ExtraData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickItemPrivate::ExtraData'

    #  Qt's '~QQuickItemPrivate::ExtraData()'. Naming it makes this a value
    #  class: Python owns every C++ QQuickItemPrivate::ExtraData behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN17QQuickItemPrivate9ExtraDataD1Ev'

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
      'QQuickItemPrivate::ExtraData::ExtraData()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickitemprivate-extradata.html#ExtraData
      """
      #  QQuickItemPrivate::ExtraData::ExtraData()
      self._noteCreation(QQuickItemPrivate.ExtraData, lambda: Rituals.call(
          'ritual_ZN17QQuickItemPrivate9ExtraDataC1Ev',
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
  @overload(QQuickItem)
  @overload(NoneType)
  def get(item: Optional[QQuickItem]) -> Optional[QQuickItemPrivate]:
    """
    Calls Qt's 'QQuickItemPrivate *QQuickItemPrivate::get(QQuickItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#get

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickItemPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItemPrivate *QQuickItemPrivate::get(QQuickItem *item)
    address = Rituals.call(
        'ritual_ZN17QQuickItemPrivate3getEP10QQuickItem',
        CuteMixin._addressOf(item),
    )
    return QQuickItemPrivate._cuteAt(address)

  @staticmethod
  @overload(QQuickItem, bool)
  @overload(NoneType, bool)
  def focusNextPrev(item: Optional[QQuickItem], forward: bool) -> bool:
    """
    Calls Qt's 'bool QQuickItemPrivate::focusNextPrev(QQuickItem *item, bool
    forward)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#focusNextPrev

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    forward : bool
      Passed on as it is.
    """
    #  bool QQuickItemPrivate::focusNextPrev(QQuickItem *item, bool forward)
    return Rituals.call(
        'ritual_ZN17QQuickItemPrivate13focusNextPrevEP10QQuickItemb',
        CuteMixin._addressOf(item), forward,
    )

  @staticmethod
  @overload(QQuickItem, int)
  @overload(NoneType, int)
  def nextTabChildItem(
      item: Optional[QQuickItem],
      start: int,
  ) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickItemPrivate::nextTabChildItem(const
    QQuickItem *item, int start)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#nextTabChildItem

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    start : int
      Passed on as it is.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickItemPrivate::nextTabChildItem(const QQuickItem
    #      *item, int start)
    address = Rituals.call(
        'ritual_ZN17QQuickItemPrivate16nextTabChildItemEPK10QQuickItemi',
        CuteMixin._addressOf(item), start,
    )
    return QQuickItem._cuteAt(address)

  @staticmethod
  @overload(QQuickItem, int)
  @overload(NoneType, int)
  def prevTabChildItem(
      item: Optional[QQuickItem],
      start: int,
  ) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickItemPrivate::prevTabChildItem(const
    QQuickItem *item, int start)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#prevTabChildItem

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    start : int
      Passed on as it is.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickItemPrivate::prevTabChildItem(const QQuickItem
    #      *item, int start)
    address = Rituals.call(
        'ritual_ZN17QQuickItemPrivate16prevTabChildItemEPK10QQuickItemi',
        CuteMixin._addressOf(item), start,
    )
    return QQuickItem._cuteAt(address)

  @staticmethod
  @overload(QQuickItem, bool)
  @overload(NoneType, bool)
  @overload(QQuickItem, bool, bool)
  @overload(NoneType, bool, bool)
  def nextPrevItemInTabFocusChain(
      item: Optional[QQuickItem],
      forward: bool,
      wrap: bool = True,
  ) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem
    *QQuickItemPrivate::nextPrevItemInTabFocusChain(QQuickItem *item, bool
    forward, bool wrap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#nextPrevItemInTabFocusChain

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    forward : bool
      Passed on as it is.

    wrap : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickItemPrivate::nextPrevItemInTabFocusChain(QQuickItem
    #      *item, bool forward, bool wrap)
    address = Rituals.call(
        'ritual_ZN17QQuickItemPrivate27nextPrevItemInTabFocusChainEP10QQuic'
        'kItembb',
        CuteMixin._addressOf(item), forward, wrap,
    )
    return QQuickItem._cuteAt(address)

  @staticmethod
  @overload(QQuickItem)
  @overload(NoneType)
  def canAcceptTabFocus(item: Optional[QQuickItem]) -> bool:
    """
    Calls Qt's 'bool QQuickItemPrivate::canAcceptTabFocus(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#canAcceptTabFocus

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickItemPrivate::canAcceptTabFocus(QQuickItem *item)
    return Rituals.call(
        'ritual_ZN17QQuickItemPrivate17canAcceptTabFocusEP10QQuickItem',
        CuteMixin._addressOf(item),
    )

  @staticmethod
  def _qt_property_x_offset() -> int:
    """
    Calls Qt's 'size_t QQuickItemPrivate::_qt_property_x_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#_qt_property_x_offset
    """
    #  size_t QQuickItemPrivate::_qt_property_x_offset()
    return Rituals.call(
        'ritual_ZN17QQuickItemPrivate21_qt_property_x_offsetEv',
    )

  @staticmethod
  def _qt_property_y_offset() -> int:
    """
    Calls Qt's 'size_t QQuickItemPrivate::_qt_property_y_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#_qt_property_y_offset
    """
    #  size_t QQuickItemPrivate::_qt_property_y_offset()
    return Rituals.call(
        'ritual_ZN17QQuickItemPrivate21_qt_property_y_offsetEv',
    )

  @staticmethod
  def _qt_property_width_offset() -> int:
    """
    Calls Qt's 'size_t QQuickItemPrivate::_qt_property_width_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#_qt_property_width_offset
    """
    #  size_t QQuickItemPrivate::_qt_property_width_offset()
    return Rituals.call(
        'ritual_ZN17QQuickItemPrivate25_qt_property_width_offsetEv',
    )

  @staticmethod
  def _qt_property_height_offset() -> int:
    """
    Calls Qt's 'size_t QQuickItemPrivate::_qt_property_height_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#_qt_property_height_offset
    """
    #  size_t QQuickItemPrivate::_qt_property_height_offset()
    return Rituals.call(
        'ritual_ZN17QQuickItemPrivate26_qt_property_height_offsetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickItemPrivate'

  #  A C++ QQuickItemPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickItemPrivate'

  #  The functions Qt calls itself that QQuickItemPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'addPointerHandler': (
          ('_ZN17QQuickItemPrivate17addPointerHandlerEP20QQuickPointerHandl'
           'er',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickPointerHandler'),
           )),
      ),
      'removePointerHandler': (
          ('_ZN17QQuickItemPrivate20removePointerHandlerEP20QQuickPointerHa'
           'ndler',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickPointerHandler'),
           )),
      ),
      'attachedPropertyPropagator_parent': (
          ('_ZN17QQuickItemPrivate33attachedPropertyPropagator_parentEPK11Q'
           'MetaObject',
           ('address', 'address',
            'QtQuick:QtPrivate.QQuickAttachedPropertyPropagator'),
           (
               ('address', 'address', 'QtCore:QMetaObject'),
           )),
      ),
      'registerAsContainmentMask': (
          ('_ZN17QQuickItemPrivate25registerAsContainmentMaskEP10QQuickItem'
           'b',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('bool', 'number', ''),
           )),
      ),
      'setLastFocusChangeReason': (
          ('_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt11FocusRea'
           'sonE',
           ('bool', 'number', ''),
           (
               ('int', 'enum', 'QtCore:Qt.FocusReason'),
           )),
      ),
      'getImplicitWidth': (
          ('_ZNK17QQuickItemPrivate16getImplicitWidthEv',
           ('double', 'number', ''),
           ()),
      ),
      'getImplicitHeight': (
          ('_ZNK17QQuickItemPrivate17getImplicitHeightEv',
           ('double', 'number', ''),
           ()),
      ),
      'implicitWidthChanged': (
          ('_ZN17QQuickItemPrivate20implicitWidthChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'implicitHeightChanged': (
          ('_ZN17QQuickItemPrivate21implicitHeightChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'accessibleRole': (
          ('_ZNK17QQuickItemPrivate14accessibleRoleEv',
           ('int', 'enum', 'QtGui:QAccessible.Role'),
           ()),
      ),
      'transformChanged': (
          ('_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'handlePointerEvent': (
          ('_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtGui:QPointerEvent'),
               ('bool', 'number', ''),
           )),
      ),
      'handleContextMenuEvent': (
          ('_ZN17QQuickItemPrivate22handleContextMenuEventEP17QContextMenuE'
           'vent',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtGui:QContextMenuEvent'),
           )),
      ),
      'setVisible': (
          ('_ZN17QQuickItemPrivate10setVisibleEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'createTransformNode': (
          ('_ZN17QQuickItemPrivate19createTransformNodeEv',
           ('address', 'address', 'QtQuick:QSGTransformNode'),
           ()),
      ),
      'mirrorChange': (
          ('_ZN17QQuickItemPrivate12mirrorChangeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'updatePolish': (
          ('_ZN17QQuickItemPrivate12updatePolishEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'dumpItemTree': (
          ('_ZNK17QQuickItemPrivate12dumpItemTreeEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
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

  def state(self) -> str:
    """
    Calls Qt's 'QString QQuickItemPrivate::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#state

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickItemPrivate::state() const
    return self.uglySide.call('ritual_ZNK17QQuickItemPrivate5stateEv')

  def left(self) -> QQuickAnchorLine:
    """
    Calls Qt's 'QQuickAnchorLine QQuickItemPrivate::left() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#left

    Returns
    -------

    QQuickAnchorLine
      A new cute QQuickAnchorLine around the copy Qt gave back. Python owns
      it.
    """
    #  QQuickAnchorLine QQuickItemPrivate::left() const
    address = self.uglySide.call('ritual_ZNK17QQuickItemPrivate4leftEv')
    from . import QQuickAnchorLine
    return QQuickAnchorLine._cuteOwning(address)

  def right(self) -> QQuickAnchorLine:
    """
    Calls Qt's 'QQuickAnchorLine QQuickItemPrivate::right() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#right

    Returns
    -------

    QQuickAnchorLine
      A new cute QQuickAnchorLine around the copy Qt gave back. Python owns
      it.
    """
    #  QQuickAnchorLine QQuickItemPrivate::right() const
    address = self.uglySide.call('ritual_ZNK17QQuickItemPrivate5rightEv')
    from . import QQuickAnchorLine
    return QQuickAnchorLine._cuteOwning(address)

  def horizontalCenter(self) -> QQuickAnchorLine:
    """
    Calls Qt's 'QQuickAnchorLine QQuickItemPrivate::horizontalCenter()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#horizontalCenter

    Returns
    -------

    QQuickAnchorLine
      A new cute QQuickAnchorLine around the copy Qt gave back. Python owns
      it.
    """
    #  QQuickAnchorLine QQuickItemPrivate::horizontalCenter() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickItemPrivate16horizontalCenterEv',
    )
    from . import QQuickAnchorLine
    return QQuickAnchorLine._cuteOwning(address)

  def top(self) -> QQuickAnchorLine:
    """
    Calls Qt's 'QQuickAnchorLine QQuickItemPrivate::top() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#top

    Returns
    -------

    QQuickAnchorLine
      A new cute QQuickAnchorLine around the copy Qt gave back. Python owns
      it.
    """
    #  QQuickAnchorLine QQuickItemPrivate::top() const
    address = self.uglySide.call('ritual_ZNK17QQuickItemPrivate3topEv')
    from . import QQuickAnchorLine
    return QQuickAnchorLine._cuteOwning(address)

  def bottom(self) -> QQuickAnchorLine:
    """
    Calls Qt's 'QQuickAnchorLine QQuickItemPrivate::bottom() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#bottom

    Returns
    -------

    QQuickAnchorLine
      A new cute QQuickAnchorLine around the copy Qt gave back. Python owns
      it.
    """
    #  QQuickAnchorLine QQuickItemPrivate::bottom() const
    address = self.uglySide.call('ritual_ZNK17QQuickItemPrivate6bottomEv')
    from . import QQuickAnchorLine
    return QQuickAnchorLine._cuteOwning(address)

  def verticalCenter(self) -> QQuickAnchorLine:
    """
    Calls Qt's 'QQuickAnchorLine QQuickItemPrivate::verticalCenter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#verticalCenter

    Returns
    -------

    QQuickAnchorLine
      A new cute QQuickAnchorLine around the copy Qt gave back. Python owns
      it.
    """
    #  QQuickAnchorLine QQuickItemPrivate::verticalCenter() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickItemPrivate14verticalCenterEv',
    )
    from . import QQuickAnchorLine
    return QQuickAnchorLine._cuteOwning(address)

  def baseline(self) -> QQuickAnchorLine:
    """
    Calls Qt's 'QQuickAnchorLine QQuickItemPrivate::baseline() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#baseline

    Returns
    -------

    QQuickAnchorLine
      A new cute QQuickAnchorLine around the copy Qt gave back. Python owns
      it.
    """
    #  QQuickAnchorLine QQuickItemPrivate::baseline() const
    address = self.uglySide.call('ritual_ZNK17QQuickItemPrivate8baselineEv')
    from . import QQuickAnchorLine
    return QQuickAnchorLine._cuteOwning(address)

  def layer(self) -> Optional[QQuickItemLayer]:
    """
    Calls Qt's 'QQuickItemLayer *QQuickItemPrivate::layer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#layer

    Returns
    -------

    Optional[QQuickItemLayer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItemLayer *QQuickItemPrivate::layer() const
    address = self.uglySide.call('ritual_ZNK17QQuickItemPrivate5layerEv')
    from . import QQuickItemLayer
    return QQuickItemLayer._cuteAt(address)

  def hasPointerHandlers(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemPrivate::hasPointerHandlers() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#hasPointerHandlers
    """
    #  bool QQuickItemPrivate::hasPointerHandlers() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickItemPrivate18hasPointerHandlersEv',
    )

  def hasEnabledHoverHandlers(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemPrivate::hasEnabledHoverHandlers() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#hasEnabledHoverHandlers
    """
    #  bool QQuickItemPrivate::hasEnabledHoverHandlers() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickItemPrivate23hasEnabledHoverHandlersEv',
    )

  def anchors(self) -> Optional[QQuickAnchors]:
    """
    Calls Qt's 'QQuickAnchors *QQuickItemPrivate::anchors() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#anchors

    Returns
    -------

    Optional[QQuickAnchors]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAnchors *QQuickItemPrivate::anchors() const
    address = self.uglySide.call('ritual_ZNK17QQuickItemPrivate7anchorsEv')
    from . import QQuickAnchors
    return QQuickAnchors._cuteAt(address)

  def acceptedMouseButtons(self) -> Qt.MouseButtons:
    """
    Calls Qt's 'Qt::MouseButtons QQuickItemPrivate::acceptedMouseButtons()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#acceptedMouseButtons

    Returns
    -------

    Qt.MouseButtons
      The value standing for the combination Qt gave back.
    """
    #  Qt::MouseButtons QQuickItemPrivate::acceptedMouseButtons() const
    return Qt.MouseButtons(self.uglySide.call(
        'ritual_ZNK17QQuickItemPrivate20acceptedMouseButtonsEv',
    ))

  def origin(self) -> QQuickItem.TransformOrigin:
    """
    Calls Qt's 'QQuickItem::TransformOrigin QQuickItemPrivate::origin()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#origin

    Returns
    -------

    QQuickItem.TransformOrigin
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickItem.TransformOrigin(number)' gives.
    """
    #  QQuickItem::TransformOrigin QQuickItemPrivate::origin() const
    return QQuickItem.TransformOrigin(self.uglySide.call(
        'ritual_ZNK17QQuickItemPrivate6originEv',
    ))

  def dirtyToString(self) -> str:
    """
    Calls Qt's 'QString QQuickItemPrivate::dirtyToString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#dirtyToString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickItemPrivate::dirtyToString() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickItemPrivate13dirtyToStringEv',
    )

  @overload()
  @overload(QPoint)
  @overload(NoneType)
  def renderWindow(
      self,
      offset: Optional[QPoint] = None,
  ) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QQuickItemPrivate::renderWindow(QPoint *offset)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#renderWindow

    Parameters
    ----------

    offset : Optional[QPoint]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QQuickItemPrivate::renderWindow(QPoint *offset) const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickItemPrivate12renderWindowEP6QPoint',
        self._addressOf(offset),
    )
    from ..QtGui import QWindow
    return QWindow._cuteAt(address)

  def sceneGraphContext(self) -> Optional[QSGContext]:
    """
    Calls Qt's 'QSGContext *QQuickItemPrivate::sceneGraphContext() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#sceneGraphContext

    Returns
    -------

    Optional[QSGContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGContext *QQuickItemPrivate::sceneGraphContext() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickItemPrivate17sceneGraphContextEv',
    )
    from . import QSGContext
    return QSGContext._cuteAt(address)

  def sceneGraphRenderContext(self) -> Optional[QSGRenderContext]:
    """
    Calls Qt's 'QSGRenderContext
    *QQuickItemPrivate::sceneGraphRenderContext() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#sceneGraphRenderContext

    Returns
    -------

    Optional[QSGRenderContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGRenderContext *QQuickItemPrivate::sceneGraphRenderContext() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickItemPrivate23sceneGraphRenderContextEv',
    )
    from . import QSGRenderContext
    return QSGRenderContext._cuteAt(address)

  def paintOrderChildItems(self) -> QList[QQuickItem]:
    """
    Calls Qt's 'QList<QQuickItem *> QQuickItemPrivate::paintOrderChildItems()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#paintOrderChildItems

    Returns
    -------

    QList[QQuickItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQuickItem *> QQuickItemPrivate::paintOrderChildItems() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickItemPrivate20paintOrderChildItemsEv',
    )
    return QList[QQuickItem]._cuteOwning(address)

  def effectiveDevicePixelRatio(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemPrivate::effectiveDevicePixelRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#effectiveDevicePixelRatio
    """
    #  qreal QQuickItemPrivate::effectiveDevicePixelRatio() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickItemPrivate25effectiveDevicePixelRatioEv',
    )

  def lastFocusChangeReason(self) -> Qt.FocusReason:
    """
    Calls Qt's 'Qt::FocusReason QQuickItemPrivate::lastFocusChangeReason()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#lastFocusChangeReason

    Returns
    -------

    Qt.FocusReason
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.FocusReason(number)'
      gives.
    """
    #  Qt::FocusReason QQuickItemPrivate::lastFocusChangeReason() const
    return Qt.FocusReason(self.uglySide.call(
        'ritual_ZNK17QQuickItemPrivate21lastFocusChangeReasonEv',
    ))

  def windowToItemTransform(self) -> QTransform:
    """
    Calls Qt's 'QTransform QQuickItemPrivate::windowToItemTransform() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#windowToItemTransform

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QQuickItemPrivate::windowToItemTransform() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickItemPrivate21windowToItemTransformEv',
    )
    from ..QtGui import QTransform
    return QTransform._cuteOwning(address)

  def itemToWindowTransform(self) -> QTransform:
    """
    Calls Qt's 'QTransform QQuickItemPrivate::itemToWindowTransform() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#itemToWindowTransform

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QQuickItemPrivate::itemToWindowTransform() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickItemPrivate21itemToWindowTransformEv',
    )
    from ..QtGui import QTransform
    return QTransform._cuteOwning(address)

  def widthValid(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemPrivate::widthValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#widthValid
    """
    #  bool QQuickItemPrivate::widthValid() const
    return self.uglySide.call('ritual_ZNK17QQuickItemPrivate10widthValidEv')

  def heightValid(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemPrivate::heightValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#heightValid
    """
    #  bool QQuickItemPrivate::heightValid() const
    return self.uglySide.call('ritual_ZNK17QQuickItemPrivate11heightValidEv')

  def z(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemPrivate::z() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#z
    """
    #  qreal QQuickItemPrivate::z() const
    return self.uglySide.call('ritual_ZNK17QQuickItemPrivate1zEv')

  def scale(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemPrivate::scale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#scale
    """
    #  qreal QQuickItemPrivate::scale() const
    return self.uglySide.call('ritual_ZNK17QQuickItemPrivate5scaleEv')

  def rotation(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemPrivate::rotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#rotation
    """
    #  qreal QQuickItemPrivate::rotation() const
    return self.uglySide.call('ritual_ZNK17QQuickItemPrivate8rotationEv')

  def opacity(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemPrivate::opacity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#opacity
    """
    #  qreal QQuickItemPrivate::opacity() const
    return self.uglySide.call('ritual_ZNK17QQuickItemPrivate7opacityEv')

  def getImplicitWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemPrivate::getImplicitWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#getImplicitWidth
    """
    #  qreal QQuickItemPrivate::getImplicitWidth() const
    ritual = 'ritual_ZNK17QQuickItemPrivate16getImplicitWidthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QQuickItemPrivate16getImplicitWidthEv'
    return self.uglySide.call(ritual)

  def getImplicitHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemPrivate::getImplicitHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#getImplicitHeight
    """
    #  qreal QQuickItemPrivate::getImplicitHeight() const
    ritual = 'ritual_ZNK17QQuickItemPrivate17getImplicitHeightEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QQuickItemPrivate17getImplicitHeightEv'
    return self.uglySide.call(ritual)

  def effectiveAccessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role
    QQuickItemPrivate::effectiveAccessibleRole() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#effectiveAccessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickItemPrivate::effectiveAccessibleRole() const
    return QAccessible.Role(self.uglySide.call(
        'ritual_ZNK17QQuickItemPrivate23effectiveAccessibleRoleEv',
    ))

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickItemPrivate::accessibleRole() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickItemPrivate::accessibleRole() const
    ritual = 'ritual_ZNK17QQuickItemPrivate14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QQuickItemPrivate14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  def isMirrored(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemPrivate::isMirrored() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#isMirrored
    """
    #  bool QQuickItemPrivate::isMirrored() const
    return self.uglySide.call('ritual_ZNK17QQuickItemPrivate10isMirroredEv')

  def computeTransformOrigin(self) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickItemPrivate::computeTransformOrigin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#computeTransformOrigin

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickItemPrivate::computeTransformOrigin() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickItemPrivate22computeTransformOriginEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QPointerEvent, QEventPoint)
  @overload(NoneType, QEventPoint)
  def anyPointerHandlerWants(
      self,
      event: Optional[QPointerEvent],
      point: QEventPoint,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickItemPrivate::anyPointerHandlerWants(const
    QPointerEvent *event, const QEventPoint &point) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#anyPointerHandlerWants

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.
    """
    #  bool QQuickItemPrivate::anyPointerHandlerWants(const QPointerEvent
    #      *event, const QEventPoint &point) const
    return self.uglySide.call(
        'ritual_ZNK17QQuickItemPrivate22anyPointerHandlerWantsEPK13QPointer'
        'EventRK11QEventPoint',
        self._addressOf(event), self._valueOf(point),
    )

  def isTransparentForPositioner(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemPrivate::isTransparentForPositioner() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#isTransparentForPositioner
    """
    #  bool QQuickItemPrivate::isTransparentForPositioner() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickItemPrivate26isTransparentForPositionerEv',
    )

  def calcEffectiveVisible(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemPrivate::calcEffectiveVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#calcEffectiveVisible
    """
    #  bool QQuickItemPrivate::calcEffectiveVisible() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickItemPrivate20calcEffectiveVisibleEv',
    )

  def calcEffectiveEnable(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemPrivate::calcEffectiveEnable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#calcEffectiveEnable
    """
    #  bool QQuickItemPrivate::calcEffectiveEnable() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickItemPrivate19calcEffectiveEnableEv',
    )

  def biggestPointerHandlerMargin(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemPrivate::biggestPointerHandlerMargin()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#biggestPointerHandlerMargin
    """
    #  qreal QQuickItemPrivate::biggestPointerHandlerMargin() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickItemPrivate27biggestPointerHandlerMarginEv',
    )

  @overload()
  @overload(float)
  def eventHandlingBounds(self, margin: float = 0.0) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickItemPrivate::eventHandlingBounds(qreal margin)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#eventHandlingBounds

    Parameters
    ----------

    margin : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickItemPrivate::eventHandlingBounds(qreal margin) const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickItemPrivate19eventHandlingBoundsEd', margin,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def parentFullyContains(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemPrivate::parentFullyContains() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#parentFullyContains
    """
    #  bool QQuickItemPrivate::parentFullyContains() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickItemPrivate19parentFullyContainsEv',
    )

  def effectivelyClipsEventHandlingChildren(self) -> bool:
    """
    Calls Qt's 'bool
    QQuickItemPrivate::effectivelyClipsEventHandlingChildren() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html
    """
    #  bool QQuickItemPrivate::effectivelyClipsEventHandlingChildren() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickItemPrivate37effectivelyClipsEventHandlingChildr'
        'enEv',
    )

  def opacityNode(self) -> Optional[QSGOpacityNode]:
    """
    Calls Qt's 'QSGOpacityNode *QQuickItemPrivate::opacityNode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#opacityNode

    Returns
    -------

    Optional[QSGOpacityNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGOpacityNode *QQuickItemPrivate::opacityNode() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickItemPrivate11opacityNodeEv',
    )
    from . import QSGOpacityNode
    return QSGOpacityNode._cuteAt(address)

  def clipNode(self) -> Optional[QQuickDefaultClipNode]:
    """
    Calls Qt's 'QQuickDefaultClipNode *QQuickItemPrivate::clipNode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#clipNode

    Returns
    -------

    Optional[QQuickDefaultClipNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDefaultClipNode *QQuickItemPrivate::clipNode() const
    address = self.uglySide.call('ritual_ZNK17QQuickItemPrivate8clipNodeEv')
    from . import QQuickDefaultClipNode
    return QQuickDefaultClipNode._cuteAt(address)

  def rootNode(self) -> Optional[QSGRootNode]:
    """
    Calls Qt's 'QSGRootNode *QQuickItemPrivate::rootNode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#rootNode

    Returns
    -------

    Optional[QSGRootNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGRootNode *QQuickItemPrivate::rootNode() const
    address = self.uglySide.call('ritual_ZNK17QQuickItemPrivate8rootNodeEv')
    from . import QSGRootNode
    return QSGRootNode._cuteAt(address)

  @overload(QQuickPointerHandler)
  @overload(NoneType)
  def effectiveCursor(
      self,
      handler: Optional[QQuickPointerHandler],
  ) -> QCursor:
    """
    Calls Qt's 'QCursor QQuickItemPrivate::effectiveCursor(const
    QQuickPointerHandler *handler) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#effectiveCursor

    Parameters
    ----------

    handler : Optional[QQuickPointerHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QCursor
      A new cute QCursor around the copy Qt gave back. Python owns it.
    """
    #  QCursor QQuickItemPrivate::effectiveCursor(const QQuickPointerHandler
    #      *handler) const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickItemPrivate15effectiveCursorEPK20QQuickPointerHa'
        'ndler',
        self._addressOf(handler),
    )
    from ..QtGui import QCursor
    return QCursor._cuteOwning(address)

  def effectiveCursorHandler(self) -> Optional[QQuickPointerHandler]:
    """
    Calls Qt's 'QQuickPointerHandler
    *QQuickItemPrivate::effectiveCursorHandler() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#effectiveCursorHandler

    Returns
    -------

    Optional[QQuickPointerHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPointerHandler *QQuickItemPrivate::effectiveCursorHandler()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickItemPrivate22effectiveCursorHandlerEv',
    )
    from . import QQuickPointerHandler
    return QQuickPointerHandler._cuteAt(address)

  def sizePolicy(self) -> QLayoutPolicy:
    """
    Calls Qt's 'QLayoutPolicy QQuickItemPrivate::sizePolicy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#sizePolicy

    Returns
    -------

    QLayoutPolicy
      A new cute QLayoutPolicy around the copy Qt gave back. Python owns it.
    """
    #  QLayoutPolicy QQuickItemPrivate::sizePolicy() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickItemPrivate10sizePolicyEv',
    )
    from ..QtGui import QLayoutPolicy
    return QLayoutPolicy._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setState(self, a0: str) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::setState(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#setState

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickItemPrivate::setState(const QString &a0)
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate8setStateERK7QString', a0,
    )

  @overload(QObject)
  @overload(NoneType)
  def setContextMenu(self, menu: Optional[QObject]) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQuickItemPrivate::setContextMenu(QObject *menu)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#setContextMenu

    Parameters
    ----------

    menu : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQuickItemPrivate::setContextMenu(QObject *menu)
    address = self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate14setContextMenuEP7QObject',
        self._addressOf(menu, 'QObject'),
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  @overload(bool)
  def setCulled(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::setCulled(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#setCulled

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickItemPrivate::setCulled(bool a0)
    self.uglySide.call('ritual_ZN17QQuickItemPrivate9setCulledEb', a0)

  @overload(QEvent.Type)
  def setFocusIfNeeded(self, a0: QEvent.Type) -> bool:
    """
    Calls Qt's 'bool QQuickItemPrivate::setFocusIfNeeded(QEvent::Type a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#setFocusIfNeeded

    Parameters
    ----------

    a0 : QEvent.Type
      Passed on as its number.
    """
    #  bool QQuickItemPrivate::setFocusIfNeeded(QEvent::Type a0)
    return self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate16setFocusIfNeededEN6QEvent4TypeE',
        a0.value,
    )

  @overload(Qt.FocusReason)
  def setLastFocusChangeReason(self, reason: Qt.FocusReason) -> bool:
    """
    Calls Qt's 'bool
    QQuickItemPrivate::setLastFocusChangeReason(Qt::FocusReason reason)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#setLastFocusChangeReason

    Parameters
    ----------

    reason : Qt.FocusReason
      Passed on as its number.
    """
    #  bool QQuickItemPrivate::setLastFocusChangeReason(Qt::FocusReason
    #      reason)
    ritual = (
        'ritual_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt11Focus'
        'ReasonE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt1'
          '1FocusReasonE')
    return self.uglySide.call(ritual, reason.value)

  @overload(float)
  def setX(self, x: float) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::setX(qreal x)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#setX

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QQuickItemPrivate::setX(qreal x)
    self.uglySide.call('ritual_ZN17QQuickItemPrivate4setXEd', x)

  @overload(float)
  def setY(self, y: float) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::setY(qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#setY

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QQuickItemPrivate::setY(qreal y)
    self.uglySide.call('ritual_ZN17QQuickItemPrivate4setYEd', y)

  @overload(float)
  def setWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::setWidth(qreal width)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#setWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QQuickItemPrivate::setWidth(qreal width)
    self.uglySide.call('ritual_ZN17QQuickItemPrivate8setWidthEd', width)

  @overload(float)
  def setHeight(self, height: float) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::setHeight(qreal height)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#setHeight

    Parameters
    ----------

    height : float
      Passed on as it is.
    """
    #  void QQuickItemPrivate::setHeight(qreal height)
    self.uglySide.call('ritual_ZN17QQuickItemPrivate9setHeightEd', height)

  def setAccessible(self) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::setAccessible()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#setAccessible
    """
    #  void QQuickItemPrivate::setAccessible()
    self.uglySide.call('ritual_ZN17QQuickItemPrivate13setAccessibleEv')

  @overload(bool)
  def setImplicitAntialiasing(self, antialiasing: bool) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::setImplicitAntialiasing(bool
    antialiasing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#setImplicitAntialiasing

    Parameters
    ----------

    antialiasing : bool
      Passed on as it is.
    """
    #  void QQuickItemPrivate::setImplicitAntialiasing(bool antialiasing)
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate23setImplicitAntialiasingEb',
        antialiasing,
    )

  @overload(bool, bool)
  def setImplicitLayoutMirror(self, mirror: bool, inherit: bool) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::setImplicitLayoutMirror(bool mirror,
    bool inherit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#setImplicitLayoutMirror

    Parameters
    ----------

    mirror : bool
      Passed on as it is.

    inherit : bool
      Passed on as it is.
    """
    #  void QQuickItemPrivate::setImplicitLayoutMirror(bool mirror, bool
    #      inherit)
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate23setImplicitLayoutMirrorEbb',
        mirror, inherit,
    )

  @overload(bool)
  def setLayoutMirror(self, mirror: bool) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::setLayoutMirror(bool mirror)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#setLayoutMirror

    Parameters
    ----------

    mirror : bool
      Passed on as it is.
    """
    #  void QQuickItemPrivate::setLayoutMirror(bool mirror)
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate15setLayoutMirrorEb', mirror,
    )

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QQuickItemPrivate::setVisible(bool visible)
    ritual = 'ritual_ZN17QQuickItemPrivate10setVisibleEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickItemPrivate10setVisibleEb'
    self.uglySide.call(ritual, visible)

  @overload(bool)
  def setTransparentForPositioner(self, trans: bool) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::setTransparentForPositioner(bool
    trans)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#setTransparentForPositioner

    Parameters
    ----------

    trans : bool
      Passed on as it is.
    """
    #  void QQuickItemPrivate::setTransparentForPositioner(bool trans)
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate27setTransparentForPositionerEb', trans,
    )

  @overload(bool)
  def setEffectiveVisibleRecur(self, a0: bool) -> bool:
    """
    Calls Qt's 'bool QQuickItemPrivate::setEffectiveVisibleRecur(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#setEffectiveVisibleRecur

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  bool QQuickItemPrivate::setEffectiveVisibleRecur(bool a0)
    return self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate24setEffectiveVisibleRecurEb', a0,
    )

  @overload(QQuickItem, bool)
  @overload(NoneType, bool)
  def setEffectiveEnableRecur(
      self,
      scope: Optional[QQuickItem],
      a1: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::setEffectiveEnableRecur(QQuickItem
    *scope, bool a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#setEffectiveEnableRecur

    Parameters
    ----------

    scope : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : bool
      Passed on as it is.
    """
    #  void QQuickItemPrivate::setEffectiveEnableRecur(QQuickItem *scope,
    #      bool a1)
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate23setEffectiveEnableRecurEP10QQuickIte'
        'mb',
        self._addressOf(scope), a1,
    )

  @overload(bool)
  def setHasCursorInChild(self, hasCursor: bool) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::setHasCursorInChild(bool hasCursor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#setHasCursorInChild

    Parameters
    ----------

    hasCursor : bool
      Passed on as it is.
    """
    #  void QQuickItemPrivate::setHasCursorInChild(bool hasCursor)
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate19setHasCursorInChildEb', hasCursor,
    )

  @overload(bool)
  def setHasHoverInChild(self, hasHover: bool) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::setHasHoverInChild(bool hasHover)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#setHasHoverInChild

    Parameters
    ----------

    hasHover : bool
      Passed on as it is.
    """
    #  void QQuickItemPrivate::setHasHoverInChild(bool hasHover)
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate18setHasHoverInChildEb', hasHover,
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
    Notes what was given, for Qt's 'QQuickItemPrivate::QQuickItemPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#QQuickItemPrivate
    """
    #  QQuickItemPrivate::QQuickItemPrivate()
    self._noteCreation(QQuickItemPrivate, lambda: Rituals.call(
        'ritual_ZN17QQuickItemPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickItemPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#q_func

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickItemPrivate::q_func()
    address = self.uglySide.call('ritual_ZN17QQuickItemPrivate6q_funcEv')
    return QQuickItem._cuteAt(address)

  @overload(QQuickItem)
  @overload(NoneType)
  def init(self, parent: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::init(QQuickItem *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#init

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemPrivate::init(QQuickItem *parent)
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate4initEP10QQuickItem',
        self._addressOf(parent),
    )

  @overload(QTouchEvent, bool, QMutableTouchEvent)
  @overload(QTouchEvent, bool, NoneType)
  @overload(NoneType, bool, QMutableTouchEvent)
  @overload(NoneType, bool, NoneType)
  def localizedTouchEvent(
      self,
      event: Optional[QTouchEvent],
      isFiltering: bool,
      localized: Optional[QMutableTouchEvent],
  ) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::localizedTouchEvent(const QTouchEvent
    *event, bool isFiltering, QMutableTouchEvent *localized)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#localizedTouchEvent

    Parameters
    ----------

    event : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    isFiltering : bool
      Passed on as it is.

    localized : Optional[QMutableTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemPrivate::localizedTouchEvent(const QTouchEvent *event,
    #      bool isFiltering, QMutableTouchEvent *localized)
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate19localizedTouchEventEPK11QTouchEventb'
        'P18QMutableTouchEvent',
        self._addressOf(event), isFiltering, self._addressOf(localized),
    )

  @overload(QQuickPointerHandler)
  @overload(NoneType)
  def addPointerHandler(self, h: Optional[QQuickPointerHandler]) -> None:
    """
    Calls Qt's 'void
    QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#addPointerHandler

    Parameters
    ----------

    h : Optional[QQuickPointerHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
    ritual = (
        'ritual_ZN17QQuickItemPrivate17addPointerHandlerEP20QQuickPointerHa'
        'ndler')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickItemPrivate17addPointerHandlerEP20QQuickPoi'
          'nterHandler')
    self.uglySide.call(ritual, self._addressOf(h))

  @overload(QQuickPointerHandler)
  @overload(NoneType)
  def removePointerHandler(self, h: Optional[QQuickPointerHandler]) -> None:
    """
    Calls Qt's 'void
    QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#removePointerHandler

    Parameters
    ----------

    h : Optional[QQuickPointerHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
    ritual = (
        'ritual_ZN17QQuickItemPrivate20removePointerHandlerEP20QQuickPointe'
        'rHandler')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickItemPrivate20removePointerHandlerEP20QQuick'
          'PointerHandler')
    self.uglySide.call(ritual, self._addressOf(h))

  @overload(QMetaObject)
  @overload(NoneType)
  def attachedPropertyPropagator_parent(
      self,
      attachedType: Optional[QMetaObject],
  ) -> Optional[QtPrivate.QQuickAttachedPropertyPropagator]:
    """
    Calls Qt's 'QtPrivate::QQuickAttachedPropertyPropagator
    *QQuickItemPrivate::attachedPropertyPropagator_parent(const QMetaObject
    *attachedType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html

    Parameters
    ----------

    attachedType : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QtPrivate.QQuickAttachedPropertyPropagator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QtPrivate::QQuickAttachedPropertyPropagator
    #      *QQuickItemPrivate::attachedPropertyPropagator_parent(const
    #      QMetaObject *attachedType)
    ritual = (
        'ritual_ZN17QQuickItemPrivate33attachedPropertyPropagator_parentEPK'
        '11QMetaObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickItemPrivate33attachedPropertyPropagator_par'
          'entEPK11QMetaObject')
    address = self.uglySide.call(
        ritual, self._addressOf(attachedType, 'QMetaObject'),
    )
    return QtPrivate.QQuickAttachedPropertyPropagator._cuteAt(address)

  @overload(QObject)
  @overload(NoneType)
  def _q_resourceObjectDeleted(self, a0: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::_q_resourceObjectDeleted(QObject
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#_q_resourceObjectDeleted

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemPrivate::_q_resourceObjectDeleted(QObject *a0)
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate24_q_resourceObjectDeletedEP7QObject',
        self._addressOf(a0, 'QObject'),
    )

  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def _q_createJSWrapper(self, engine: Optional[QV4.ExecutionEngine]) -> int:
    """
    Calls Qt's 'quint64
    QQuickItemPrivate::_q_createJSWrapper(QQmlV4ExecutionEnginePtr engine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#_q_createJSWrapper

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  quint64 QQuickItemPrivate::_q_createJSWrapper(QQmlV4ExecutionEnginePtr
    #      engine)
    return self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate18_q_createJSWrapperEPN3QV415Execution'
        'EngineE',
        self._addressOf(engine),
    )

  @overload(QQuickItem, bool)
  @overload(NoneType, bool)
  def registerAsContainmentMask(
      self,
      a0: Optional[QQuickItem],
      a1: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::registerAsContainmentMask(QQuickItem
    *a0, bool a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#registerAsContainmentMask

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : bool
      Passed on as it is.
    """
    #  void QQuickItemPrivate::registerAsContainmentMask(QQuickItem *a0, bool
    #      a1)
    ritual = (
        'ritual_ZN17QQuickItemPrivate25registerAsContainmentMaskEP10QQuickI'
        'temb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickItemPrivate25registerAsContainmentMaskEP10Q'
          'QuickItemb')
    self.uglySide.call(ritual, self._addressOf(a0), a1)

  @overload(QQuickItemChangeListener, ChangeTypes)
  @overload(NoneType, ChangeTypes)
  def addItemChangeListener(
      self,
      listener: Optional[QQuickItemChangeListener],
      types: ChangeTypes,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickItemPrivate::addItemChangeListener(QQuickItemChangeListener
    *listener, ChangeTypes types)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#addItemChangeListener

    Parameters
    ----------

    listener : Optional[QQuickItemChangeListener]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    types : ChangeTypes
      Passed on as its number.
    """
    #  void QQuickItemPrivate::addItemChangeListener(QQuickItemChangeListener
    #      *listener, ChangeTypes types)
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate21addItemChangeListenerEP24QQuickItemC'
        'hangeListener6QFlagsINS_10ChangeTypeEE',
        self._addressOf(listener, 'QQuickItemChangeListener'), types.value,
    )

  @overload(QQuickItemChangeListener, ChangeTypes)
  @overload(NoneType, ChangeTypes)
  def updateOrAddItemChangeListener(
      self,
      listener: Optional[QQuickItemChangeListener],
      types: ChangeTypes,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickItemPrivate::updateOrAddItemChangeListener(QQuickItemChangeListener
    *listener, ChangeTypes types)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html

    Parameters
    ----------

    listener : Optional[QQuickItemChangeListener]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    types : ChangeTypes
      Passed on as its number.
    """
    #  void QQuickItemPrivate::updateOrAddItemChangeListener(
    #      QQuickItemChangeListener *listener, ChangeTypes types)
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate29updateOrAddItemChangeListenerEP24QQu'
        'ickItemChangeListener6QFlagsINS_10ChangeTypeEE',
        self._addressOf(listener, 'QQuickItemChangeListener'), types.value,
    )

  @overload(QQuickItemChangeListener, ChangeTypes)
  @overload(NoneType, ChangeTypes)
  def removeItemChangeListener(
      self,
      a0: Optional[QQuickItemChangeListener],
      types: ChangeTypes,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickItemPrivate::removeItemChangeListener(QQuickItemChangeListener *a0,
    ChangeTypes types)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#removeItemChangeListener

    Parameters
    ----------

    a0 : Optional[QQuickItemChangeListener]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    types : ChangeTypes
      Passed on as its number.
    """
    #  void QQuickItemPrivate::removeItemChangeListener(
    #      QQuickItemChangeListener *a0, ChangeTypes types)
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate24removeItemChangeListenerEP24QQuickIt'
        'emChangeListener6QFlagsINS_10ChangeTypeEE',
        self._addressOf(a0, 'QQuickItemChangeListener'), types.value,
    )

  @overload(QQuickItemChangeListener, QQuickGeometryChange)
  @overload(NoneType, QQuickGeometryChange)
  def updateOrAddGeometryChangeListener(
      self,
      listener: Optional[QQuickItemChangeListener],
      types: QQuickGeometryChange,
  ) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::updateOrAddGeometryChangeListener(
    QQuickItemChangeListener *listener, QQuickGeometryChange types)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html

    Parameters
    ----------

    listener : Optional[QQuickItemChangeListener]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    types : QQuickGeometryChange
      Passed on as a value: Qt reads the C++ QQuickGeometryChange, which
      stays Python's own.
    """
    #  void QQuickItemPrivate::updateOrAddGeometryChangeListener(
    #      QQuickItemChangeListener *listener, QQuickGeometryChange types)
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate33updateOrAddGeometryChangeListenerEP2'
        '4QQuickItemChangeListener20QQuickGeometryChange',
        self._addressOf(listener, 'QQuickItemChangeListener'),
        self._valueOf(types),
    )

  @overload(QQuickItemChangeListener, QQuickGeometryChange)
  @overload(NoneType, QQuickGeometryChange)
  def updateOrRemoveGeometryChangeListener(
      self,
      listener: Optional[QQuickItemChangeListener],
      types: QQuickGeometryChange,
  ) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::updateOrRemoveGeometryChangeListener(
    QQuickItemChangeListener *listener, QQuickGeometryChange types)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html

    Parameters
    ----------

    listener : Optional[QQuickItemChangeListener]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    types : QQuickGeometryChange
      Passed on as a value: Qt reads the C++ QQuickGeometryChange, which
      stays Python's own.
    """
    #  void QQuickItemPrivate::updateOrRemoveGeometryChangeListener(
    #      QQuickItemChangeListener *listener, QQuickGeometryChange types)
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate36updateOrRemoveGeometryChangeListener'
        'EP24QQuickItemChangeListener20QQuickGeometryChange',
        self._addressOf(listener, 'QQuickItemChangeListener'),
        self._valueOf(types),
    )

  def _states(self) -> Optional[QQuickStateGroup]:
    """
    Calls Qt's 'QQuickStateGroup *QQuickItemPrivate::_states()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#_states

    Returns
    -------

    Optional[QQuickStateGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickStateGroup *QQuickItemPrivate::_states()
    address = self.uglySide.call('ritual_ZN17QQuickItemPrivate7_statesEv')
    from . import QQuickStateGroup
    return QQuickStateGroup._cuteAt(address)

  def requestCustomOverlay(self) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::requestCustomOverlay()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#requestCustomOverlay
    """
    #  void QQuickItemPrivate::requestCustomOverlay()
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate20requestCustomOverlayEv',
    )

  @overload(DirtyType)
  def dirty(self, a0: DirtyType) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::dirty(DirtyType a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#dirty

    Parameters
    ----------

    a0 : DirtyType
      Passed on as its number.
    """
    #  void QQuickItemPrivate::dirty(DirtyType a0)
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate5dirtyENS_9DirtyTypeE', a0.value,
    )

  def addToDirtyList(self) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::addToDirtyList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#addToDirtyList
    """
    #  void QQuickItemPrivate::addToDirtyList()
    self.uglySide.call('ritual_ZN17QQuickItemPrivate14addToDirtyListEv')

  def removeFromDirtyList(self) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::removeFromDirtyList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#removeFromDirtyList
    """
    #  void QQuickItemPrivate::removeFromDirtyList()
    self.uglySide.call('ritual_ZN17QQuickItemPrivate19removeFromDirtyListEv')

  @overload(QQuickItem)
  @overload(NoneType)
  def addChild(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::addChild(QQuickItem *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#addChild

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemPrivate::addChild(QQuickItem *a0)
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate8addChildEP10QQuickItem',
        self._addressOf(a0),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def removeChild(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::removeChild(QQuickItem *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#removeChild

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemPrivate::removeChild(QQuickItem *a0)
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate11removeChildEP10QQuickItem',
        self._addressOf(a0),
    )

  def siblingOrderChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::siblingOrderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#siblingOrderChanged
    """
    #  void QQuickItemPrivate::siblingOrderChanged()
    self.uglySide.call('ritual_ZN17QQuickItemPrivate19siblingOrderChangedEv')

  @overload(QQuickItem)
  @overload(NoneType)
  def markSortedChildrenDirty(self, child: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::markSortedChildrenDirty(QQuickItem
    *child)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#markSortedChildrenDirty

    Parameters
    ----------

    child : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemPrivate::markSortedChildrenDirty(QQuickItem *child)
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate23markSortedChildrenDirtyEP10QQuickIte'
        'm',
        self._addressOf(child),
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def refWindow(self, a0: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::refWindow(QQuickWindow *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#refWindow

    Parameters
    ----------

    a0 : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemPrivate::refWindow(QQuickWindow *a0)
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate9refWindowEP12QQuickWindow',
        self._addressOf(a0),
    )

  def derefWindow(self) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::derefWindow()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#derefWindow
    """
    #  void QQuickItemPrivate::derefWindow()
    self.uglySide.call('ritual_ZN17QQuickItemPrivate11derefWindowEv')

  @overload(QQuickItem, bool)
  @overload(NoneType, bool)
  def updateSubFocusItem(
      self,
      scope: Optional[QQuickItem],
      focus: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::updateSubFocusItem(QQuickItem *scope,
    bool focus)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#updateSubFocusItem

    Parameters
    ----------

    scope : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    focus : bool
      Passed on as it is.
    """
    #  void QQuickItemPrivate::updateSubFocusItem(QQuickItem *scope, bool
    #      focus)
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate18updateSubFocusItemEP10QQuickItemb',
        self._addressOf(scope), focus,
    )

  @overload(QTransform)
  @overload(NoneType)
  def itemToParentTransform(self, a0: Optional[QTransform]) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::itemToParentTransform(QTransform *a0)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#itemToParentTransform

    Parameters
    ----------

    a0 : Optional[QTransform]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemPrivate::itemToParentTransform(QTransform *a0) const
    self.uglySide.call(
        'ritual_ZNK17QQuickItemPrivate21itemToParentTransformEP10QTransform',
        self._addressOf(a0),
    )

  def xChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::xChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#xChanged
    """
    #  void QQuickItemPrivate::xChanged()
    self.uglySide.call('ritual_ZN17QQuickItemPrivate8xChangedEv')

  def yChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::yChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#yChanged
    """
    #  void QQuickItemPrivate::yChanged()
    self.uglySide.call('ritual_ZN17QQuickItemPrivate8yChangedEv')

  def widthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::widthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#widthChanged
    """
    #  void QQuickItemPrivate::widthChanged()
    self.uglySide.call('ritual_ZN17QQuickItemPrivate12widthChangedEv')

  def heightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::heightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#heightChanged
    """
    #  void QQuickItemPrivate::heightChanged()
    self.uglySide.call('ritual_ZN17QQuickItemPrivate13heightChangedEv')

  def implicitWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::implicitWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#implicitWidthChanged
    """
    #  void QQuickItemPrivate::implicitWidthChanged()
    ritual = 'ritual_ZN17QQuickItemPrivate20implicitWidthChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickItemPrivate20implicitWidthChangedEv'
    self.uglySide.call(ritual)

  def implicitHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::implicitHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#implicitHeightChanged
    """
    #  void QQuickItemPrivate::implicitHeightChanged()
    ritual = 'ritual_ZN17QQuickItemPrivate21implicitHeightChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickItemPrivate21implicitHeightChangedEv'
    self.uglySide.call(ritual)

  def resolveLayoutMirror(self) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::resolveLayoutMirror()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#resolveLayoutMirror
    """
    #  void QQuickItemPrivate::resolveLayoutMirror()
    self.uglySide.call('ritual_ZN17QQuickItemPrivate19resolveLayoutMirrorEv')

  @overload(QRectF)
  def emitChildrenRectChanged(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::emitChildrenRectChanged(const QRectF
    &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#emitChildrenRectChanged

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickItemPrivate::emitChildrenRectChanged(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate23emitChildrenRectChangedERK6QRectF',
        self._valueOf(rect),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def transformChanged(self, transformedItem: Optional[QQuickItem]) -> bool:
    """
    Calls Qt's 'bool QQuickItemPrivate::transformChanged(QQuickItem
    *transformedItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#transformChanged

    Parameters
    ----------

    transformedItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
    ritual = 'ritual_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem')
    return self.uglySide.call(ritual, self._addressOf(transformedItem))

  @overload(QPointF, QPointF, QVector2D, float, float, float, float)
  def adjustedPosForTransform(
      self,
      centroid: QPointF,
      startPos: QPointF,
      activeTranslatation: QVector2D,
      startScale: float,
      activeScale: float,
      startRotation: float,
      activeRotation: float,
  ) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickItemPrivate::adjustedPosForTransform(const
    QPointF &centroid, const QPointF &startPos, const QVector2D
    &activeTranslatation, qreal startScale, qreal activeScale, qreal
    startRotation, qreal activeRotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#adjustedPosForTransform

    Parameters
    ----------

    centroid : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    startPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    activeTranslatation : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    startScale : float
      Passed on as it is.

    activeScale : float
      Passed on as it is.

    startRotation : float
      Passed on as it is.

    activeRotation : float
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickItemPrivate::adjustedPosForTransform(const QPointF
    #      &centroid, const QPointF &startPos, const QVector2D
    #      &activeTranslatation, qreal startScale, qreal activeScale, qreal
    #      startRotation, qreal activeRotation)
    address = self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate23adjustedPosForTransformERK7QPointFS2'
        '_RK9QVector2Ddddd',
        self._valueOf(centroid, 'QPointF'), self._valueOf(startPos,
        'QPointF'), self._valueOf(activeTranslatation), startScale,
        activeScale, startRotation, activeRotation,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def deliveryAgent(self) -> Optional[QQuickDeliveryAgent]:
    """
    Calls Qt's 'QQuickDeliveryAgent *QQuickItemPrivate::deliveryAgent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#deliveryAgent

    Returns
    -------

    Optional[QQuickDeliveryAgent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDeliveryAgent *QQuickItemPrivate::deliveryAgent()
    address = self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate13deliveryAgentEv',
    )
    from . import QQuickDeliveryAgent
    return QQuickDeliveryAgent._cuteAt(address)

  def deliveryAgentPrivate(self) -> Optional[QQuickDeliveryAgentPrivate]:
    """
    Calls Qt's 'QQuickDeliveryAgentPrivate
    *QQuickItemPrivate::deliveryAgentPrivate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#deliveryAgentPrivate

    Returns
    -------

    Optional[QQuickDeliveryAgentPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDeliveryAgentPrivate *QQuickItemPrivate::deliveryAgentPrivate()
    address = self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate20deliveryAgentPrivateEv',
    )
    from . import QQuickDeliveryAgentPrivate
    return QQuickDeliveryAgentPrivate._cuteAt(address)

  def ensureSubsceneDeliveryAgent(self) -> Optional[QQuickDeliveryAgent]:
    """
    Calls Qt's 'QQuickDeliveryAgent
    *QQuickItemPrivate::ensureSubsceneDeliveryAgent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#ensureSubsceneDeliveryAgent

    Returns
    -------

    Optional[QQuickDeliveryAgent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDeliveryAgent *QQuickItemPrivate::ensureSubsceneDeliveryAgent()
    address = self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate27ensureSubsceneDeliveryAgentEv',
    )
    from . import QQuickDeliveryAgent
    return QQuickDeliveryAgent._cuteAt(address)

  @overload(QKeyEvent)
  @overload(NoneType)
  def deliverKeyEvent(self, a0: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::deliverKeyEvent(QKeyEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#deliverKeyEvent

    Parameters
    ----------

    a0 : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemPrivate::deliverKeyEvent(QKeyEvent *a0)
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate15deliverKeyEventEP9QKeyEvent',
        self._addressOf(a0),
    )

  @overload(QKeyEvent, bool)
  @overload(NoneType, bool)
  def filterKeyEvent(self, a0: Optional[QKeyEvent], post: bool) -> bool:
    """
    Calls Qt's 'bool QQuickItemPrivate::filterKeyEvent(QKeyEvent *a0, bool
    post)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#filterKeyEvent

    Parameters
    ----------

    a0 : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    post : bool
      Passed on as it is.
    """
    #  bool QQuickItemPrivate::filterKeyEvent(QKeyEvent *a0, bool post)
    return self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate14filterKeyEventEP9QKeyEventb',
        self._addressOf(a0), post,
    )

  @overload(QInputMethodEvent)
  @overload(NoneType)
  def deliverInputMethodEvent(self, a0: Optional[QInputMethodEvent]) -> None:
    """
    Calls Qt's 'void
    QQuickItemPrivate::deliverInputMethodEvent(QInputMethodEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#deliverInputMethodEvent

    Parameters
    ----------

    a0 : Optional[QInputMethodEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemPrivate::deliverInputMethodEvent(QInputMethodEvent *a0)
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate23deliverInputMethodEventEP17QInputMet'
        'hodEvent',
        self._addressOf(a0),
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def deliverShortcutOverrideEvent(self, a0: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    QQuickItemPrivate::deliverShortcutOverrideEvent(QKeyEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html

    Parameters
    ----------

    a0 : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemPrivate::deliverShortcutOverrideEvent(QKeyEvent *a0)
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate28deliverShortcutOverrideEventEP9QKeyE'
        'vent',
        self._addressOf(a0),
    )

  @overload(QEvent)
  @overload(NoneType)
  def deliverPointerEvent(self, a0: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::deliverPointerEvent(QEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#deliverPointerEvent

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemPrivate::deliverPointerEvent(QEvent *a0)
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate19deliverPointerEventEP6QEvent',
        self._addressOf(a0),
    )

  @overload(QPointerEvent)
  @overload(NoneType)
  @overload(QPointerEvent, bool)
  @overload(NoneType, bool)
  def handlePointerEvent(
      self,
      a0: Optional[QPointerEvent],
      avoidGrabbers: bool = False,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0,
    bool avoidGrabbers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#handlePointerEvent

    Parameters
    ----------

    a0 : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    avoidGrabbers : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0, bool
    #      avoidGrabbers)
    ritual = (
        'ritual_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickItemPrivate18handlePointerEventEP13QPointer'
          'Eventb')
    return self.uglySide.call(ritual, self._addressOf(a0), avoidGrabbers)

  @overload(QContextMenuEvent)
  @overload(NoneType)
  def handleContextMenuEvent(
      self,
      event: Optional[QContextMenuEvent],
  ) -> bool:
    """
    Calls Qt's 'bool
    QQuickItemPrivate::handleContextMenuEvent(QContextMenuEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#handleContextMenuEvent

    Parameters
    ----------

    event : Optional[QContextMenuEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickItemPrivate::handleContextMenuEvent(QContextMenuEvent
    #      *event)
    ritual = (
        'ritual_ZN17QQuickItemPrivate22handleContextMenuEventEP17QContextMe'
        'nuEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickItemPrivate22handleContextMenuEventEP17QCon'
          'textMenuEvent')
    return self.uglySide.call(ritual, self._addressOf(event))

  def itemNode(self) -> Optional[QSGTransformNode]:
    """
    Calls Qt's 'QSGTransformNode *QQuickItemPrivate::itemNode()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#itemNode

    Returns
    -------

    Optional[QSGTransformNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTransformNode *QQuickItemPrivate::itemNode()
    address = self.uglySide.call('ritual_ZN17QQuickItemPrivate8itemNodeEv')
    from . import QSGTransformNode
    return QSGTransformNode._cuteAt(address)

  def childContainerNode(self) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QQuickItemPrivate::childContainerNode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#childContainerNode

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QQuickItemPrivate::childContainerNode()
    address = self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate18childContainerNodeEv',
    )
    from . import QSGNode
    return QSGNode._cuteAt(address)

  def createTransformNode(self) -> Optional[QSGTransformNode]:
    """
    Calls Qt's 'QSGTransformNode *QQuickItemPrivate::createTransformNode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#createTransformNode

    Returns
    -------

    Optional[QSGTransformNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTransformNode *QQuickItemPrivate::createTransformNode()
    ritual = 'ritual_ZN17QQuickItemPrivate19createTransformNodeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickItemPrivate19createTransformNodeEv'
    address = self.uglySide.call(ritual)
    from . import QSGTransformNode
    return QSGTransformNode._cuteAt(address)

  @overload(bool)
  def refFromEffectItem(self, hide: bool) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::refFromEffectItem(bool hide)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#refFromEffectItem

    Parameters
    ----------

    hide : bool
      Passed on as it is.
    """
    #  void QQuickItemPrivate::refFromEffectItem(bool hide)
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate17refFromEffectItemEb', hide,
    )

  @overload(int)
  def recursiveRefFromEffectItem(self, refs: int) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::recursiveRefFromEffectItem(int
    refs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#recursiveRefFromEffectItem

    Parameters
    ----------

    refs : int
      Passed on as it is.
    """
    #  void QQuickItemPrivate::recursiveRefFromEffectItem(int refs)
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate26recursiveRefFromEffectItemEi', refs,
    )

  @overload(bool)
  def derefFromEffectItem(self, unhide: bool) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::derefFromEffectItem(bool unhide)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#derefFromEffectItem

    Parameters
    ----------

    unhide : bool
      Passed on as it is.
    """
    #  void QQuickItemPrivate::derefFromEffectItem(bool unhide)
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate19derefFromEffectItemEb', unhide,
    )

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      a0: QQuickItem.ItemChange,
      a1: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::itemChange(QQuickItem::ItemChange a0,
    const QQuickItem::ItemChangeData &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemprivate.html#itemChange

    Parameters
    ----------

    a0 : QQuickItem.ItemChange
      Passed on as its number.

    a1 : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickItemPrivate::itemChange(QQuickItem::ItemChange a0, const
    #      QQuickItem::ItemChangeData &a1)
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate10itemChangeEN10QQuickItem10ItemChange'
        'ERKNS0_14ItemChangeDataE',
        a0.value, self._valueOf(a1),
    )

  def enableSubtreeChangeNotificationsForParentHierachy(self) -> None:
    """
    Calls Qt's 'void
    QQuickItemPrivate::enableSubtreeChangeNotificationsForParentHierachy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html
    """
    #  void QQuickItemPrivate::
    #      enableSubtreeChangeNotificationsForParentHierachy()
    self.uglySide.call(
        'ritual_ZN17QQuickItemPrivate49enableSubtreeChangeNotificationsForP'
        'arentHierachyEv',
    )

  def mirrorChange(self) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::mirrorChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#mirrorChange
    """
    #  void QQuickItemPrivate::mirrorChange()
    ritual = 'ritual_ZN17QQuickItemPrivate12mirrorChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickItemPrivate12mirrorChangeEv'
    self.uglySide.call(ritual)

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::updatePolish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#updatePolish
    """
    #  void QQuickItemPrivate::updatePolish()
    ritual = 'ritual_ZN17QQuickItemPrivate12updatePolishEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickItemPrivate12updatePolishEv'
    self.uglySide.call(ritual)

  @overload(int)
  def dumpItemTree(self, indent: int) -> None:
    """
    Calls Qt's 'void QQuickItemPrivate::dumpItemTree(int indent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemprivate.html#dumpItemTree

    Parameters
    ----------

    indent : int
      Passed on as it is.
    """
    #  void QQuickItemPrivate::dumpItemTree(int indent) const
    ritual = 'ritual_ZNK17QQuickItemPrivate12dumpItemTreeEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QQuickItemPrivate12dumpItemTreeEi'
    self.uglySide.call(ritual, indent)

  @staticmethod
  def children_append(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickItemPrivate::children_append(QQmlListProperty<QQuickItem> *a0,
    QQuickItem *a1)': names 'QQmlListProperty<QQuickItem>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuickItemPrivate.children_append' has no cute function yet. Qt's "
        "'void "
        "QQuickItemPrivate::children_append(QQmlListProperty<QQuickItem> "
        "*a0, QQuickItem *a1)': names 'QQmlListProperty<QQuickItem>', which "
        "has no cute class yet.")

  @staticmethod
  def children_at(*__, **_) -> Never:
    """
    Qt's 'QQuickItem
    *QQuickItemPrivate::children_at(QQmlListProperty<QQuickItem> *a0,
    qsizetype a1)': names 'QQmlListProperty<QQuickItem>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuickItemPrivate.children_at' has no cute function yet. Qt's "
        "'QQuickItem "
        "*QQuickItemPrivate::children_at(QQmlListProperty<QQuickItem> *a0, "
        "qsizetype a1)': names 'QQmlListProperty<QQuickItem>', which has no "
        "cute class yet.")

  @staticmethod
  def children_clear(*__, **_) -> Never:
    """
    Qt's 'void QQuickItemPrivate::children_clear(QQmlListProperty<QQuickItem>
    *a0)': names 'QQmlListProperty<QQuickItem>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickItemPrivate.children_clear' has no cute function yet. Qt's "
        "'void "
        "QQuickItemPrivate::children_clear(QQmlListProperty<QQuickItem> "
        "*a0)': names 'QQmlListProperty<QQuickItem>', which has no cute "
        "class yet.")

  @staticmethod
  def children_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QQuickItemPrivate::children_count(QQmlListProperty<QQuickItem> *a0)':
    names 'QQmlListProperty<QQuickItem>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickItemPrivate.children_count' has no cute function yet. Qt's "
        "'qsizetype "
        "QQuickItemPrivate::children_count(QQmlListProperty<QQuickItem> "
        "*a0)': names 'QQmlListProperty<QQuickItem>', which has no cute "
        "class yet.")

  @staticmethod
  def children_removeLast(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickItemPrivate::children_removeLast(QQmlListProperty<QQuickItem>
    *a0)': names 'QQmlListProperty<QQuickItem>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickItemPrivate.children_removeLast' has no cute function yet. "
        "Qt's 'void "
        "QQuickItemPrivate::children_removeLast(QQmlListProperty<QQuickItem>"
        " *a0)': names 'QQmlListProperty<QQuickItem>', which has no cute "
        "class yet.")

  @staticmethod
  def data(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QQuickItemPrivate::data()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickItemPrivate.data' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QQuickItemPrivate::data()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def data_append(*__, **_) -> Never:
    """
    Qt's 'void QQuickItemPrivate::data_append(QQmlListProperty<QObject> *a0,
    QObject *a1)': names 'QQmlListProperty<QObject>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQuickItemPrivate.data_append' has no cute function yet. Qt's "
        "'void QQuickItemPrivate::data_append(QQmlListProperty<QObject> "
        "*a0, QObject *a1)': names 'QQmlListProperty<QObject>', which has "
        "no cute class yet.")

  @staticmethod
  def data_at(*__, **_) -> Never:
    """
    Qt's 'QObject *QQuickItemPrivate::data_at(QQmlListProperty<QObject> *a0,
    qsizetype a1)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuickItemPrivate.data_at' has no cute function yet. Qt's "
        "'QObject *QQuickItemPrivate::data_at(QQmlListProperty<QObject> "
        "*a0, qsizetype a1)': names 'QQmlListProperty<QObject>', which has "
        "no cute class yet.")

  @staticmethod
  def data_clear(*__, **_) -> Never:
    """
    Qt's 'void QQuickItemPrivate::data_clear(QQmlListProperty<QObject> *a0)':
    names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickItemPrivate.data_clear' has no cute function yet. Qt's "
        "'void QQuickItemPrivate::data_clear(QQmlListProperty<QObject> "
        "*a0)': names 'QQmlListProperty<QObject>', which has no cute class "
        "yet.")

  @staticmethod
  def data_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype QQuickItemPrivate::data_count(QQmlListProperty<QObject>
    *a0)': names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickItemPrivate.data_count' has no cute function yet. Qt's "
        "'qsizetype QQuickItemPrivate::data_count(QQmlListProperty<QObject> "
        "*a0)': names 'QQmlListProperty<QObject>', which has no cute class "
        "yet.")

  @staticmethod
  def data_removeLast(*__, **_) -> Never:
    """
    Qt's 'void QQuickItemPrivate::data_removeLast(QQmlListProperty<QObject>
    *a0)': names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickItemPrivate.data_removeLast' has no cute function yet. Qt's "
        "'void QQuickItemPrivate::data_removeLast(QQmlListProperty<QObject> "
        "*a0)': names 'QQmlListProperty<QObject>', which has no cute class "
        "yet.")

  @staticmethod
  def notifyChangeListeners(*__, **_) -> Never:
    """
    Qt's 'QQuickItemPrivate::notifyChangeListeners': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QQuickItemPrivate.notifyChangeListeners' has no cute function "
        "yet. Qt's 'QQuickItemPrivate::notifyChangeListeners': a template: "
        "a pattern and no single function.")

  @staticmethod
  def resources(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QQuickItemPrivate::resources()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickItemPrivate.resources' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QQuickItemPrivate::resources()': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def resources_append(*__, **_) -> Never:
    """
    Qt's 'void QQuickItemPrivate::resources_append(QQmlListProperty<QObject>
    *a0, QObject *a1)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuickItemPrivate.resources_append' has no cute function yet. "
        "Qt's 'void "
        "QQuickItemPrivate::resources_append(QQmlListProperty<QObject> *a0, "
        "QObject *a1)': names 'QQmlListProperty<QObject>', which has no "
        "cute class yet.")

  @staticmethod
  def resources_at(*__, **_) -> Never:
    """
    Qt's 'QObject *QQuickItemPrivate::resources_at(QQmlListProperty<QObject>
    *a0, qsizetype a1)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuickItemPrivate.resources_at' has no cute function yet. Qt's "
        "'QObject "
        "*QQuickItemPrivate::resources_at(QQmlListProperty<QObject> *a0, "
        "qsizetype a1)': names 'QQmlListProperty<QObject>', which has no "
        "cute class yet.")

  @staticmethod
  def resources_clear(*__, **_) -> Never:
    """
    Qt's 'void QQuickItemPrivate::resources_clear(QQmlListProperty<QObject>
    *a0)': names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickItemPrivate.resources_clear' has no cute function yet. Qt's "
        "'void QQuickItemPrivate::resources_clear(QQmlListProperty<QObject> "
        "*a0)': names 'QQmlListProperty<QObject>', which has no cute class "
        "yet.")

  @staticmethod
  def resources_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QQuickItemPrivate::resources_count(QQmlListProperty<QObject> *a0)': names
    'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickItemPrivate.resources_count' has no cute function yet. Qt's "
        "'qsizetype "
        "QQuickItemPrivate::resources_count(QQmlListProperty<QObject> "
        "*a0)': names 'QQmlListProperty<QObject>', which has no cute class "
        "yet.")

  @staticmethod
  def resources_removeLast(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickItemPrivate::resources_removeLast(QQmlListProperty<QObject> *a0)':
    names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickItemPrivate.resources_removeLast' has no cute function yet. "
        "Qt's 'void "
        "QQuickItemPrivate::resources_removeLast(QQmlListProperty<QObject> "
        "*a0)': names 'QQmlListProperty<QObject>', which has no cute class "
        "yet.")

  @staticmethod
  def setSizePolicy(*__, **_) -> Never:
    """
    Qt's 'void QQuickItemPrivate::setSizePolicy(const QLayoutPolicy::Policy
    &horizontalPolicy, const QLayoutPolicy::Policy &verticalPolicy)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickItemPrivate.setSizePolicy' has no cute function yet. Qt's "
        "'void QQuickItemPrivate::setSizePolicy(const QLayoutPolicy::Policy "
        "&horizontalPolicy, const QLayoutPolicy::Policy &verticalPolicy)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def states(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickState> QQuickItemPrivate::states()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickItemPrivate.states' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuickState> QQuickItemPrivate::states()': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def transform_append(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickItemPrivate::transform_append(QQmlListProperty<QQuickTransform>
    *list, QQuickTransform *a1)': names 'QQmlListProperty<QQuickTransform>',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickItemPrivate.transform_append' has no cute function yet. "
        "Qt's 'void "
        "QQuickItemPrivate::transform_append(QQmlListProperty<QQuickTransfor"
        "m> *list, QQuickTransform *a1)': names "
        "'QQmlListProperty<QQuickTransform>', which has no cute class yet.")

  @staticmethod
  def transform_at(*__, **_) -> Never:
    """
    Qt's 'QQuickTransform
    *QQuickItemPrivate::transform_at(QQmlListProperty<QQuickTransform> *list,
    qsizetype a1)': names 'QQmlListProperty<QQuickTransform>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QQuickItemPrivate.transform_at' has no cute function yet. Qt's "
        "'QQuickTransform "
        "*QQuickItemPrivate::transform_at(QQmlListProperty<QQuickTransform> "
        "*list, qsizetype a1)': names 'QQmlListProperty<QQuickTransform>', "
        "which has no cute class yet.")

  @staticmethod
  def transform_clear(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickItemPrivate::transform_clear(QQmlListProperty<QQuickTransform>
    *list)': names 'QQmlListProperty<QQuickTransform>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuickItemPrivate.transform_clear' has no cute function yet. Qt's "
        "'void "
        "QQuickItemPrivate::transform_clear(QQmlListProperty<QQuickTransform"
        "> *list)': names 'QQmlListProperty<QQuickTransform>', which has no "
        "cute class yet.")

  @staticmethod
  def transform_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QQuickItemPrivate::transform_count(QQmlListProperty<QQuickTransform>
    *list)': names 'QQmlListProperty<QQuickTransform>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuickItemPrivate.transform_count' has no cute function yet. Qt's "
        "'qsizetype "
        "QQuickItemPrivate::transform_count(QQmlListProperty<QQuickTransform"
        "> *list)': names 'QQmlListProperty<QQuickTransform>', which has no "
        "cute class yet.")

  @staticmethod
  def transitions(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickTransition>
    QQuickItemPrivate::transitions()': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QQuickItemPrivate.transitions' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuickTransition> "
        "QQuickItemPrivate::transitions()': gives a type Python has no way "
        "to take yet.")

  @staticmethod
  def visibleChildren(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickItem> QQuickItemPrivate::visibleChildren()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickItemPrivate.visibleChildren' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuickItem> "
        "QQuickItemPrivate::visibleChildren()': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def visibleChildren_at(*__, **_) -> Never:
    """
    Qt's 'QQuickItem
    *QQuickItemPrivate::visibleChildren_at(QQmlListProperty<QQuickItem>
    *prop, qsizetype index)': names 'QQmlListProperty<QQuickItem>', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickItemPrivate.visibleChildren_at' has no cute function yet. "
        "Qt's 'QQuickItem "
        "*QQuickItemPrivate::visibleChildren_at(QQmlListProperty<QQuickItem>"
        " *prop, qsizetype index)': names 'QQmlListProperty<QQuickItem>', "
        "which has no cute class yet.")

  @staticmethod
  def visibleChildren_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QQuickItemPrivate::visibleChildren_count(QQmlListProperty<QQuickItem>
    *prop)': names 'QQmlListProperty<QQuickItem>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQuickItemPrivate.visibleChildren_count' has no cute function "
        "yet. Qt's 'qsizetype "
        "QQuickItemPrivate::visibleChildren_count(QQmlListProperty<QQuickIte"
        "m> *prop)': names 'QQmlListProperty<QQuickItem>', which has no "
        "cute class yet.")
