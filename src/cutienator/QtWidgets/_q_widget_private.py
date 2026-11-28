"""
QWidgetPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QWidgetPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QObjectPrivate
from ..QtGui import QPlatformTextureList
from . import QStyle, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QLocale, QMargins, QObject, QPoint, QPointF
  from ..QtCore import QRect, QSize
  from ..QtGui import QBrush, QCursor, QFont, QImage, QPaintDevice
  from ..QtGui import QPaintEngine, QPainter, QPalette
  from ..QtGui import QPlatformBackingStoreRhiConfig, QRegion, QRhi, QScreen
  from ..QtGui import QWindow
  from . import QGraphicsProxyWidget, QStyleOption, QTLWExtra, QWExtra
  from . import QWidgetRepaintManager
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QCursor = WAIT['QCursor']
  QEvent = WAIT['QEvent']
  QFont = WAIT['QFont']
  QLocale = WAIT['QLocale']
  QObject = WAIT['QObject']
  QPaintDevice = WAIT['QPaintDevice']
  QPaintEngine = WAIT['QPaintEngine']
  QPainter = WAIT['QPainter']
  QPalette = WAIT['QPalette']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QRect = WAIT['QRect']
  QRegion = WAIT['QRegion']
  QScreen = WAIT['QScreen']
  QSize = WAIT['QSize']
  QStyleOption = WAIT['QStyleOption']
  QWidgetRepaintManager = WAIT['QWidgetRepaintManager']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWidgetPrivate(QObjectPrivate):
  """
  The cute side of Qt's QWidgetPrivate: a plain Python object standing in
  front of one C++ QWidgetPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QWidgetPrivate is built
  on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWidgetPrivate that has a ritual and that Python can
  call so far, 181 names in all: 'q_func', 'get', 'checkRestoredGeometry',
  'extraData', 'topData', 'maybeTopData', 'sharedPainter',
  'setSharedPainter', 'maybeRepaintManager', 'rhi', 'windowHandle',
  '_q_closestWindowHandle', 'associatedScreen', 'init', 'create',
  'createRecursively', 'createWinId', 'setScreenForPoint', 'setScreen',
  'createTLExtra', 'createExtra', 'deleteExtra', 'createSysExtra',
  'deleteSysExtra', 'createTLSysExtra', 'deleteTLSysExtra',
  'updateSystemBackground', 'propagatePaletteChange', 'setPalette_helper',
  'resolvePalette', 'naturalWidgetPalette', 'setMask_sys', 'raise_sys',
  'lower_sys', 'stackUnder_sys', 'deepestFocusProxy', 'setFocus_sys',
  'updateFocusChild', 'updateFont', 'setFont_helper', 'localFont',
  'resolveFont', 'naturalWidgetFont', 'setLayoutDirection_helper',
  'resolveLayoutDirection', 'setLocale_helper', 'resolveLocale',
  'setStyle_helper', 'inheritStyle', 'setUpdatesEnabled_helper',
  'updateBrushOrigin', 'paintBackground', 'isAboutToShow', 'prepareToRender',
  'render_helper', 'render', 'drawWidget', 'sendPaintEvent',
  'paintSiblingsRecursive', 'nearestGraphicsProxyWidget',
  'shouldPaintOnScreen', 'paintOnScreen', 'clipRect', 'clipRegion',
  'setSystemClip', 'updateIsOpaque', 'setOpaque', 'updateIsTranslucent',
  'invalidateGraphicsEffectsRecursively', 'getOpaqueChildren',
  'setDirtyOpaqueRegion', 'close', 'handleClose', 'setWindowIcon_helper',
  'setWindowIcon_sys', 'setWindowOpacity_sys', 'adjustQuitOnCloseAttribute',
  'scrollChildren', 'moveRect', 'scrollRect',
  'invalidateBackingStore_resizeHelper', 'overlappedRegion', 'isOverlapped',
  'syncBackingStore', 'shouldDiscardSyncRequest', 'updateWidgetTransform',
  'reparentFocusWidgets', 'setWinId', 'showChildren', 'hideChildren',
  'setParent_sys', 'reparentWidgetWindows', 'reparentWidgetWindowChildren',
  'scroll_sys', 'deactivateWidgetCleanup', 'setGeometry_sys',
  'fixPosIncludesFrame', 'sendPendingMoveAndResizeEvents',
  'activateChildLayoutsRecursively', 'show_recursive', 'show_helper',
  'show_sys', 'hide_sys', 'hide_helper', 'isExplicitlyHidden',
  '_q_showIfNotHidden', 'setVisible', 'setEnabled_helper',
  'updateFrameStrut', 'frameStrut', 'setWindowIconText_sys',
  'setWindowIconText_helper', 'setWindowTitle_sys', 'setWindowFilePath_sys',
  'setCursor_sys', 'unsetCursor_sys', 'setWindowTitle_helper',
  'setWindowFilePath_helper', 'setWindowModified_helper', 'setWindowFlags',
  'setConstraints_sys', 'pointInsideRectAndMask', 'childAt_helper',
  'childAtRecursiveHelper', 'updateGeometry_helper', 'setLayoutItemMargins',
  'updateContentsRect', 'safeAreaMargins', 'aboutToDestroy', 'recreate',
  'effectiveFocusWidget', 'setModal_sys', 'parentGraphicsView',
  'screenGeometry', 'availableScreenGeometry', 'screen', 'setRedirected',
  'redirected', 'restoreRedirected', 'enforceNativeChildren',
  'nativeChildrenForced', 'effectiveRectFor', 'adjustedSize',
  'handleSoftwareInputPanel', 'setWSGeometry', 'mapToWS', 'mapFromWS',
  'focusObject', 'rhiConfig', 'texture', 'textureListFlags',
  'grabFramebuffer', 'beginBackingStorePainting', 'endBackingStorePainting',
  'beginCompose', 'endCompose', 'setRenderToTexture', 'setTextureChildSeen',
  'sendComposeStatus', 'initializeViewportFramebuffer',
  'resizeViewportFramebuffer', 'resolveSamples', 'isStereoEnabled',
  'toggleStereoTargetBuffer', 'setWidgetParentHelper',
  'closestParentWidgetWithWindowHandle', 'nextPrevElementInFocusChain',
  'removeFromFocusChain', 'insertIntoFocusChain',
  'insertIntoFocusChainBefore', 'insertIntoFocusChainAfter',
  'takeFromFocusChain', 'reparentFocusChildren', 'determineLastFocusChild',
  'initFocusChain', 'isInFocusChain', 'isFocusChainConsistent',
  'setNetWmWindowTypes', 'stealKeyboardGrab', 'stealMouseGrab',
  'hasChildWithFocusPolicy'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QWidget *QWidgetPrivate::q_func() const': takes in Python
    what 'QWidget *QWidgetPrivate::q_func()' takes.
  - Qt's 'QWidgetPrivate::QWidgetPrivate(decltype(QObjectPrivateVersion)
    a0)': names the enum 'QtPrivate_6_12_0', whose class cannot be named
    here.
  - Qt's 'QWidgetPrivate::~QWidgetPrivate()': the destructor: Python never
    removes a C++ QWidgetPrivate.
  - Qt's 'const QWidgetPrivate *QWidgetPrivate::get(const QWidget *w)': takes
    in Python what 'QWidgetPrivate *QWidgetPrivate::get(QWidget *w)' takes.
  - Qt's 'void QWidgetPrivate::subtractOpaqueChildren(QRegion &rgn, const
    QRect &clipRect) const': takes a type Python has no way to hand over yet.
  - Qt's 'void QWidgetPrivate::subtractOpaqueSiblings(QRegion &source, bool
    *hasDirtySiblingsAbove, bool alsoNonOpaque) const': takes a type Python
    has no way to hand over yet.
  - Qt's 'void QWidgetPrivate::clipToEffectiveMask(QRegion &region) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QWidgetPrivate::adjustFlags(Qt::WindowFlags &flags, QWidget
    *w)': takes a type Python has no way to hand over yet.
  - Qt's 'bool QWidgetPrivate::setMinimumSize_helper(int &minw, int &minh)':
    takes a number to change where it is.
  - Qt's 'bool QWidgetPrivate::setMaximumSize_helper(int &maxw, int &maxh)':
    takes a number to change where it is.
  - Qt's 'void QWidgetPrivate::getLayoutItemMargins(int *left, int *top, int
    *right, int *bottom) const': takes a number to change where it is.
  - Qt's 'std::string QWidgetPrivate::flagsForDumping() const': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  6 of the 209 functions Qt declares: 3 not a gap; 3 a template.

  What to expect
  --------------

  - The C++ QWidgetPrivate is created at the first use, not by
    'QWidgetPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWidgetPrivate.
  - Each name of Qt's QWidgetPrivate that has no cute function yet,
    '__init__', 'adjustFlags', 'clipToEffectiveMask', 'getLayoutItemMargins',
    'invalidateBackingStore', 'repaint', 'setMaximumSize_helper',
    'setMinimumSize_helper', 'subtractOpaqueChildren',
    'subtractOpaqueSiblings', 'update', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QWidgetPrivate, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class CloseMode(CuteNum):
    """
    The enum 'QWidgetPrivate::CloseMode' of Qt, with the 3 names Qt gives in
    it.
    """

    CloseNoEvent = Kee[int](0)
    CloseWithEvent = Kee[int](1)
    CloseWithSpontaneousEvent = Kee[int](2)

  class Direction(CuteNum):
    """
    The enum 'QWidgetPrivate::Direction' of Qt, with the 4 names Qt gives in
    it.
    """

    DirectionNorth = Kee[int](1)
    DirectionEast = Kee[int](16)
    DirectionSouth = Kee[int](2)
    DirectionWest = Kee[int](32)

  class DrawWidgetFlag(CuteFlags):
    """
    The flags enum 'QWidgetPrivate::DrawWidgetFlag' of Qt, with the 9 names
    Qt gives in it. Qt names the type of its combinations
    'QWidgetPrivate::DrawWidgetFlags'.
    """

    DrawAsRoot = 0x1
    DrawPaintOnScreen = 0x2
    DrawRecursive = 0x4
    DrawInvisible = 0x8
    DontSubtractOpaqueChildren = 0x10
    DontDrawOpaqueChildren = 0x20
    DontDrawNativeChildren = 0x40
    DontSetCompositionMode = 0x80
    UseEffectRegionBounds = 0x100

  DrawWidgetFlags = DrawWidgetFlag

  class FocusChainRemovalRule(CuteFlags, scoped=True):
    """
    The flags enum 'QWidgetPrivate::FocusChainRemovalRule' of Qt, with the 2
    names Qt gives in it. Qt names the type of its combinations
    'QWidgetPrivate::FocusChainRemovalRules'. C++ keeps these names inside
    the enum, so the class that holds the enum does not have them.
    """

    EnsureFocusOut = 0x1
    AssertConsistency = 0x2

  FocusChainRemovalRules = FocusChainRemovalRule

  class FocusDirection(CuteNum, scoped=True):
    """
    The enum 'QWidgetPrivate::FocusDirection' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Previous = Kee[int](0)
    Next = Kee[int](1)

  class WindowHandleMode(CuteNum, scoped=True):
    """
    The enum 'QWidgetPrivate::WindowHandleMode' of Qt, with the 3 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Direct = Kee[int](0)
    Closest = Kee[int](1)
    TopLevel = Kee[int](2)

  #  The classes Qt writes inside QWidgetPrivate, each a class in here as in
  #  C++.

  class TextureData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWidgetPrivate::TextureData: a plain Python object
    standing in front of one C++ QWidgetPrivate::TextureData.

    C++ hands a QWidgetPrivate::TextureData around as a copy, so every C++
    QWidgetPrivate::TextureData behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QWidgetPrivate::TextureData yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWidgetPrivate::TextureData::~TextureData()': the destructor:
      Python removes its C++ QWidgetPrivate::TextureData by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QWidgetPrivate::TextureData is created at the first use, not by
      'QWidgetPrivate::TextureData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWidgetPrivate::TextureData back gives a copy the
      ritual made for Python, in a new cute QWidgetPrivate::TextureData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWidgetPrivate::TextureData'

    #  Qt's '~QWidgetPrivate::TextureData()'. Naming it makes this a value
    #  class: Python owns every C++ QWidgetPrivate::TextureData behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN14QWidgetPrivate11TextureDataD1Ev'

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
  @overload(QWidget)
  @overload(NoneType)
  def get(w: Optional[QWidget]) -> Optional[QWidgetPrivate]:
    """
    Calls Qt's 'QWidgetPrivate *QWidgetPrivate::get(QWidget *w)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#get

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWidgetPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidgetPrivate *QWidgetPrivate::get(QWidget *w)
    address = Rituals.call(
        'ritual_ZN14QWidgetPrivate3getEP7QWidget', CuteMixin._addressOf(w),
    )
    return QWidgetPrivate._cuteAt(address)

  @staticmethod
  @overload(QRect, QRect, int)
  @overload(QRect, NoneType, int)
  def checkRestoredGeometry(
      availableGeometry: QRect,
      restoredGeometry: Optional[QRect],
      frameHeight: int,
  ) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::checkRestoredGeometry(const QRect
    &availableGeometry, QRect *restoredGeometry, int frameHeight)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#checkRestoredGeometry

    Parameters
    ----------

    availableGeometry : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    restoredGeometry : Optional[QRect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    frameHeight : int
      Passed on as it is.
    """
    #  void QWidgetPrivate::checkRestoredGeometry(const QRect
    #      &availableGeometry, QRect *restoredGeometry, int frameHeight)
    Rituals.call(
        'ritual_ZN14QWidgetPrivate21checkRestoredGeometryERK5QRectPS0_i',
        CuteMixin._valueOf(availableGeometry),
        CuteMixin._addressOf(restoredGeometry), frameHeight,
    )

  @staticmethod
  @overload(QWidget)
  @overload(NoneType)
  def nearestGraphicsProxyWidget(
      origin: Optional[QWidget],
  ) -> Optional[QGraphicsProxyWidget]:
    """
    Calls Qt's 'QGraphicsProxyWidget
    *QWidgetPrivate::nearestGraphicsProxyWidget(const QWidget *origin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#nearestGraphicsProxyWidget

    Parameters
    ----------

    origin : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QGraphicsProxyWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsProxyWidget *QWidgetPrivate::nearestGraphicsProxyWidget(const
    #      QWidget *origin)
    address = Rituals.call(
        'ritual_ZN14QWidgetPrivate26nearestGraphicsProxyWidgetEPK7QWidget',
        CuteMixin._addressOf(origin),
    )
    from . import QGraphicsProxyWidget
    return QGraphicsProxyWidget._cuteAt(address)

  @staticmethod
  @overload(QWidget)
  @overload(NoneType)
  def parentGraphicsView(widget: Optional[QWidget]) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QWidgetPrivate::parentGraphicsView(const QWidget
    *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#parentGraphicsView

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QWidgetPrivate::parentGraphicsView(const QWidget *widget)
    address = Rituals.call(
        'ritual_ZN14QWidgetPrivate18parentGraphicsViewEPK7QWidget',
        CuteMixin._addressOf(widget),
    )
    return QWidget._cuteAt(address)

  @staticmethod
  @overload(QWidget)
  @overload(NoneType)
  def screenGeometry(widget: Optional[QWidget]) -> QRect:
    """
    Calls Qt's 'QRect QWidgetPrivate::screenGeometry(const QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#screenGeometry

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QWidgetPrivate::screenGeometry(const QWidget *widget)
    address = Rituals.call(
        'ritual_ZN14QWidgetPrivate14screenGeometryEPK7QWidget',
        CuteMixin._addressOf(widget),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @staticmethod
  @overload(QWidget, QPoint)
  @overload(NoneType, QPoint)
  @overload(QWidget, QPoint, bool)
  @overload(NoneType, QPoint, bool)
  def screenGeometry(
      widget: Optional[QWidget],
      globalPosition: QPoint,
      hasPosition: bool = True,
  ) -> QRect:
    """
    Calls Qt's 'QRect QWidgetPrivate::screenGeometry(const QWidget *widget,
    const QPoint &globalPosition, bool hasPosition)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#screenGeometry

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    globalPosition : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    hasPosition : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QWidgetPrivate::screenGeometry(const QWidget *widget, const
    #      QPoint &globalPosition, bool hasPosition)
    address = Rituals.call(
        'ritual_ZN14QWidgetPrivate14screenGeometryEPK7QWidgetRK6QPointb',
        CuteMixin._addressOf(widget), CuteMixin._valueOf(globalPosition),
        hasPosition,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @staticmethod
  @overload(QWidget)
  @overload(NoneType)
  def availableScreenGeometry(widget: Optional[QWidget]) -> QRect:
    """
    Calls Qt's 'QRect QWidgetPrivate::availableScreenGeometry(const QWidget
    *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#availableScreenGeometry

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QWidgetPrivate::availableScreenGeometry(const QWidget *widget)
    address = Rituals.call(
        'ritual_ZN14QWidgetPrivate23availableScreenGeometryEPK7QWidget',
        CuteMixin._addressOf(widget),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @staticmethod
  @overload(QWidget, QPoint)
  @overload(NoneType, QPoint)
  @overload(QWidget, QPoint, bool)
  @overload(NoneType, QPoint, bool)
  def availableScreenGeometry(
      widget: Optional[QWidget],
      globalPosition: QPoint,
      hasPosition: bool = True,
  ) -> QRect:
    """
    Calls Qt's 'QRect QWidgetPrivate::availableScreenGeometry(const QWidget
    *widget, const QPoint &globalPosition, bool hasPosition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#availableScreenGeometry

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    globalPosition : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    hasPosition : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QWidgetPrivate::availableScreenGeometry(const QWidget *widget,
    #      const QPoint &globalPosition, bool hasPosition)
    address = Rituals.call(
        'ritual_ZN14QWidgetPrivate23availableScreenGeometryEPK7QWidgetRK6QP'
        'ointb',
        CuteMixin._addressOf(widget), CuteMixin._valueOf(globalPosition),
        hasPosition,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @staticmethod
  @overload(QWidget, QPoint)
  @overload(NoneType, QPoint)
  @overload(QWidget, QPoint, bool)
  @overload(NoneType, QPoint, bool)
  def screen(
      widget: Optional[QWidget],
      globalPosition: QPoint,
      hasPosition: bool = True,
  ) -> Optional[QScreen]:
    """
    Calls Qt's 'QScreen *QWidgetPrivate::screen(const QWidget *widget, const
    QPoint &globalPosition, bool hasPosition)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#screen

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    globalPosition : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    hasPosition : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    Optional[QScreen]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScreen *QWidgetPrivate::screen(const QWidget *widget, const QPoint
    #      &globalPosition, bool hasPosition)
    address = Rituals.call(
        'ritual_ZN14QWidgetPrivate6screenEPK7QWidgetRK6QPointb',
        CuteMixin._addressOf(widget), CuteMixin._valueOf(globalPosition),
        hasPosition,
    )
    from ..QtGui import QScreen
    return QScreen._cuteAt(address)

  @staticmethod
  @overload(QWidget, bool)
  @overload(NoneType, bool)
  def sendComposeStatus(w: Optional[QWidget], end: bool) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::sendComposeStatus(QWidget *w, bool
    end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#sendComposeStatus

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    end : bool
      Passed on as it is.
    """
    #  void QWidgetPrivate::sendComposeStatus(QWidget *w, bool end)
    Rituals.call(
        'ritual_ZN14QWidgetPrivate17sendComposeStatusEP7QWidgetb',
        CuteMixin._addressOf(w), end,
    )

  @staticmethod
  @overload(QObject, QObject)
  @overload(QObject, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def setWidgetParentHelper(
      widgetAsObject: Optional[QObject],
      newParent: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setWidgetParentHelper(QObject
    *widgetAsObject, QObject *newParent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#setWidgetParentHelper

    Parameters
    ----------

    widgetAsObject : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    newParent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetPrivate::setWidgetParentHelper(QObject *widgetAsObject,
    #      QObject *newParent)
    Rituals.call(
        'ritual_ZN14QWidgetPrivate21setWidgetParentHelperEP7QObjectS1_',
        CuteMixin._addressOf(widgetAsObject, 'QObject'),
        CuteMixin._addressOf(newParent, 'QObject'),
    )

  @staticmethod
  @overload(QWidget, QWidget)
  @overload(QWidget, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  @overload(QWidget, QWidget, FocusDirection)
  @overload(QWidget, NoneType, FocusDirection)
  @overload(NoneType, QWidget, FocusDirection)
  @overload(NoneType, NoneType, FocusDirection)
  def takeFromFocusChain(
      from_: Optional[QWidget],
      to: Optional[QWidget],
      direction: FocusDirection = FocusDirection.Next,
  ) -> QList[QWidget]:
    """
    Calls Qt's 'QWidgetList QWidgetPrivate::takeFromFocusChain(QWidget *from,
    QWidget *to, FocusDirection direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#takeFromFocusChain

    Parameters
    ----------

    from_ : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    to : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    direction : FocusDirection
      Passed on as its number. May be left out, as in Qt: it is then
      FocusDirection.Next.

    Returns
    -------

    QList[QWidget]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QWidgetList QWidgetPrivate::takeFromFocusChain(QWidget *from, QWidget
    #      *to, FocusDirection direction)
    address = Rituals.call(
        'ritual_ZN14QWidgetPrivate18takeFromFocusChainEP7QWidgetS1_NS_14Foc'
        'usDirectionE',
        CuteMixin._addressOf(from_), CuteMixin._addressOf(to),
        direction.value,
    )
    return QList[QWidget]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWidgetPrivate'

  #  A C++ QWidgetPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWidgetPrivate'

  #  The functions Qt calls itself that QWidgetPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setVisible': (
          ('_ZN14QWidgetPrivate10setVisibleEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setWindowFlags': (
          ('_ZN14QWidgetPrivate14setWindowFlagsE6QFlagsIN2Qt10WindowTypeEE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'flags', 'QtCore:Qt.WindowType'),
           )),
      ),
      'aboutToDestroy': (
          ('_ZN14QWidgetPrivate14aboutToDestroyEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'recreate': (
          ('_ZN14QWidgetPrivate8recreateEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'focusObject': (
          ('_ZN14QWidgetPrivate11focusObjectEv',
           ('address', 'address', 'QtCore:QObject'),
           ()),
      ),
      'rhiConfig': (
          ('_ZNK14QWidgetPrivate9rhiConfigEv',
           ('address', 'value', 'QtGui:QPlatformBackingStoreRhiConfig'),
           ()),
      ),
      'texture': (
          ('_ZNK14QWidgetPrivate7textureEv',
           ('address', 'value', 'QtWidgets:QWidgetPrivate.TextureData'),
           ()),
      ),
      'textureListFlags': (
          ('_ZN14QWidgetPrivate16textureListFlagsEv',
           ('int', 'flags', 'QtGui:QPlatformTextureList.Flag'),
           ()),
      ),
      'grabFramebuffer': (
          ('_ZN14QWidgetPrivate15grabFramebufferEv',
           ('address', 'value', 'QtGui:QImage'),
           ()),
      ),
      'beginBackingStorePainting': (
          ('_ZN14QWidgetPrivate25beginBackingStorePaintingEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'endBackingStorePainting': (
          ('_ZN14QWidgetPrivate23endBackingStorePaintingEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'beginCompose': (
          ('_ZN14QWidgetPrivate12beginComposeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'endCompose': (
          ('_ZN14QWidgetPrivate10endComposeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'initializeViewportFramebuffer': (
          ('_ZN14QWidgetPrivate29initializeViewportFramebufferEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'resizeViewportFramebuffer': (
          ('_ZN14QWidgetPrivate25resizeViewportFramebufferEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'resolveSamples': (
          ('_ZN14QWidgetPrivate14resolveSamplesEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'isStereoEnabled': (
          ('_ZN14QWidgetPrivate15isStereoEnabledEv',
           ('bool', 'number', ''),
           ()),
      ),
      'toggleStereoTargetBuffer': (
          ('_ZN14QWidgetPrivate24toggleStereoTargetBufferEv',
           ('bool', 'number', ''),
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

  def extraData(self) -> Optional[QWExtra]:
    """
    Calls Qt's 'QWExtra *QWidgetPrivate::extraData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#extraData

    Returns
    -------

    Optional[QWExtra]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWExtra *QWidgetPrivate::extraData() const
    address = self.uglySide.call('ritual_ZNK14QWidgetPrivate9extraDataEv')
    from . import QWExtra
    return QWExtra._cuteAt(address)

  def topData(self) -> Optional[QTLWExtra]:
    """
    Calls Qt's 'QTLWExtra *QWidgetPrivate::topData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#topData

    Returns
    -------

    Optional[QTLWExtra]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTLWExtra *QWidgetPrivate::topData() const
    address = self.uglySide.call('ritual_ZNK14QWidgetPrivate7topDataEv')
    from . import QTLWExtra
    return QTLWExtra._cuteAt(address)

  def maybeTopData(self) -> Optional[QTLWExtra]:
    """
    Calls Qt's 'QTLWExtra *QWidgetPrivate::maybeTopData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#maybeTopData

    Returns
    -------

    Optional[QTLWExtra]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTLWExtra *QWidgetPrivate::maybeTopData() const
    address = self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate12maybeTopDataEv',
    )
    from . import QTLWExtra
    return QTLWExtra._cuteAt(address)

  def sharedPainter(self) -> Optional[QPainter]:
    """
    Calls Qt's 'QPainter *QWidgetPrivate::sharedPainter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#sharedPainter

    Returns
    -------

    Optional[QPainter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPainter *QWidgetPrivate::sharedPainter() const
    address = self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate13sharedPainterEv',
    )
    from ..QtGui import QPainter
    return QPainter._cuteAt(address)

  def maybeRepaintManager(self) -> Optional[QWidgetRepaintManager]:
    """
    Calls Qt's 'QWidgetRepaintManager *QWidgetPrivate::maybeRepaintManager()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#maybeRepaintManager

    Returns
    -------

    Optional[QWidgetRepaintManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidgetRepaintManager *QWidgetPrivate::maybeRepaintManager() const
    address = self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate19maybeRepaintManagerEv',
    )
    from . import QWidgetRepaintManager
    return QWidgetRepaintManager._cuteAt(address)

  def rhi(self) -> Optional[QRhi]:
    """
    Calls Qt's 'QRhi *QWidgetPrivate::rhi() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#rhi

    Returns
    -------

    Optional[QRhi]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhi *QWidgetPrivate::rhi() const
    address = self.uglySide.call('ritual_ZNK14QWidgetPrivate3rhiEv')
    from ..QtGui import QRhi
    return QRhi._cuteAt(address)

  @overload()
  @overload(WindowHandleMode)
  def windowHandle(
      self,
      mode: WindowHandleMode = WindowHandleMode.Direct,
  ) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QWidgetPrivate::windowHandle(WindowHandleMode mode)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#windowHandle

    Parameters
    ----------

    mode : WindowHandleMode
      Passed on as its number. May be left out, as in Qt: it is then
      WindowHandleMode.Direct.

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QWidgetPrivate::windowHandle(WindowHandleMode mode) const
    address = self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate12windowHandleENS_16WindowHandleModeE',
        mode.value,
    )
    from ..QtGui import QWindow
    return QWindow._cuteAt(address)

  def _q_closestWindowHandle(self) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QWidgetPrivate::_q_closestWindowHandle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#_q_closestWindowHandle

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QWidgetPrivate::_q_closestWindowHandle() const
    address = self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate22_q_closestWindowHandleEv',
    )
    from ..QtGui import QWindow
    return QWindow._cuteAt(address)

  def associatedScreen(self) -> Optional[QScreen]:
    """
    Calls Qt's 'QScreen *QWidgetPrivate::associatedScreen() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#associatedScreen

    Returns
    -------

    Optional[QScreen]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScreen *QWidgetPrivate::associatedScreen() const
    address = self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate16associatedScreenEv',
    )
    from ..QtGui import QScreen
    return QScreen._cuteAt(address)

  @overload(int)
  def naturalWidgetPalette(self, inheritedMask: int) -> QPalette:
    """
    Calls Qt's 'QPalette
    QWidgetPrivate::naturalWidgetPalette(QPalette::ResolveMask inheritedMask)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#naturalWidgetPalette

    Parameters
    ----------

    inheritedMask : int
      Passed on as it is.

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QWidgetPrivate::naturalWidgetPalette(QPalette::ResolveMask
    #      inheritedMask) const
    address = self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate20naturalWidgetPaletteEy', inheritedMask,
    )
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

  def deepestFocusProxy(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QWidgetPrivate::deepestFocusProxy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#deepestFocusProxy

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QWidgetPrivate::deepestFocusProxy() const
    address = self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate17deepestFocusProxyEv',
    )
    return QWidget._cuteAt(address)

  def localFont(self) -> QFont:
    """
    Calls Qt's 'QFont QWidgetPrivate::localFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#localFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QWidgetPrivate::localFont() const
    address = self.uglySide.call('ritual_ZNK14QWidgetPrivate9localFontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  @overload(int)
  def naturalWidgetFont(self, inheritedMask: int) -> QFont:
    """
    Calls Qt's 'QFont QWidgetPrivate::naturalWidgetFont(uint inheritedMask)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#naturalWidgetFont

    Parameters
    ----------

    inheritedMask : int
      Passed on as it is.

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QWidgetPrivate::naturalWidgetFont(uint inheritedMask) const
    address = self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate17naturalWidgetFontEj', inheritedMask,
    )
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  @overload(QPainter, QBrush)
  @overload(NoneType, QBrush)
  def updateBrushOrigin(self, a0: Optional[QPainter], brush: QBrush) -> bool:
    """
    Calls Qt's 'bool QWidgetPrivate::updateBrushOrigin(QPainter *a0, const
    QBrush &brush) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#updateBrushOrigin

    Parameters
    ----------

    a0 : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  bool QWidgetPrivate::updateBrushOrigin(QPainter *a0, const QBrush
    #      &brush) const
    return self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate17updateBrushOriginEP8QPainterRK6QBrush',
        self._addressOf(a0), self._valueOf(brush),
    )

  def isAboutToShow(self) -> bool:
    """
    Calls Qt's 'bool QWidgetPrivate::isAboutToShow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#isAboutToShow
    """
    #  bool QWidgetPrivate::isAboutToShow() const
    return self.uglySide.call('ritual_ZNK14QWidgetPrivate13isAboutToShowEv')

  def shouldPaintOnScreen(self) -> bool:
    """
    Calls Qt's 'bool QWidgetPrivate::shouldPaintOnScreen() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#shouldPaintOnScreen
    """
    #  bool QWidgetPrivate::shouldPaintOnScreen() const
    return self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate19shouldPaintOnScreenEv',
    )

  def clipRect(self) -> QRect:
    """
    Calls Qt's 'QRect QWidgetPrivate::clipRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#clipRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QWidgetPrivate::clipRect() const
    address = self.uglySide.call('ritual_ZNK14QWidgetPrivate8clipRectEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def clipRegion(self) -> QRegion:
    """
    Calls Qt's 'QRegion QWidgetPrivate::clipRegion() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#clipRegion

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QWidgetPrivate::clipRegion() const
    address = self.uglySide.call('ritual_ZNK14QWidgetPrivate10clipRegionEv')
    from ..QtGui import QRegion
    return QRegion._cuteOwning(address)

  def getOpaqueChildren(self) -> QRegion:
    """
    Calls Qt's 'const QRegion &QWidgetPrivate::getOpaqueChildren() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#getOpaqueChildren

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  const QRegion &QWidgetPrivate::getOpaqueChildren() const
    address = self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate17getOpaqueChildrenEv',
    )
    from ..QtGui import QRegion
    return QRegion._cuteOwning(address)

  @overload(QRect)
  @overload(QRect, bool)
  def overlappedRegion(
      self,
      rect: QRect,
      breakAfterFirst: bool = False,
  ) -> QRegion:
    """
    Calls Qt's 'QRegion QWidgetPrivate::overlappedRegion(const QRect &rect,
    bool breakAfterFirst) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#overlappedRegion

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    breakAfterFirst : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QWidgetPrivate::overlappedRegion(const QRect &rect, bool
    #      breakAfterFirst) const
    address = self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate16overlappedRegionERK5QRectb',
        self._valueOf(rect), breakAfterFirst,
    )
    from ..QtGui import QRegion
    return QRegion._cuteOwning(address)

  @overload(QRect)
  def isOverlapped(self, rect: QRect) -> bool:
    """
    Calls Qt's 'bool QWidgetPrivate::isOverlapped(const QRect &rect) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#isOverlapped

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  bool QWidgetPrivate::isOverlapped(const QRect &rect) const
    return self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate12isOverlappedERK5QRect',
        self._valueOf(rect),
    )

  def shouldDiscardSyncRequest(self) -> bool:
    """
    Calls Qt's 'bool QWidgetPrivate::shouldDiscardSyncRequest() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#shouldDiscardSyncRequest
    """
    #  bool QWidgetPrivate::shouldDiscardSyncRequest() const
    return self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate24shouldDiscardSyncRequestEv',
    )

  def isExplicitlyHidden(self) -> bool:
    """
    Calls Qt's 'bool QWidgetPrivate::isExplicitlyHidden() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#isExplicitlyHidden
    """
    #  bool QWidgetPrivate::isExplicitlyHidden() const
    return self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate18isExplicitlyHiddenEv',
    )

  def frameStrut(self) -> QRect:
    """
    Calls Qt's 'QRect QWidgetPrivate::frameStrut() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#frameStrut

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QWidgetPrivate::frameStrut() const
    address = self.uglySide.call('ritual_ZNK14QWidgetPrivate10frameStrutEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QPointF)
  def pointInsideRectAndMask(self, a0: QPointF) -> bool:
    """
    Calls Qt's 'bool QWidgetPrivate::pointInsideRectAndMask(const QPointF
    &a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#pointInsideRectAndMask

    Parameters
    ----------

    a0 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QWidgetPrivate::pointInsideRectAndMask(const QPointF &a0) const
    return self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate22pointInsideRectAndMaskERK7QPointF',
        self._valueOf(a0, 'QPointF'),
    )

  @overload(QPointF, bool)
  def childAt_helper(self, a0: QPointF, a1: bool) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QWidgetPrivate::childAt_helper(const QPointF &a0,
    bool a1) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#childAt_helper

    Parameters
    ----------

    a0 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    a1 : bool
      Passed on as it is.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QWidgetPrivate::childAt_helper(const QPointF &a0, bool a1)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate14childAt_helperERK7QPointFb',
        self._valueOf(a0, 'QPointF'), a1,
    )
    return QWidget._cuteAt(address)

  @overload(QPointF, bool)
  def childAtRecursiveHelper(
      self,
      p: QPointF,
      a1: bool,
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QWidgetPrivate::childAtRecursiveHelper(const QPointF
    &p, bool a1) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#childAtRecursiveHelper

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    a1 : bool
      Passed on as it is.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QWidgetPrivate::childAtRecursiveHelper(const QPointF &p, bool
    #      a1) const
    address = self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate22childAtRecursiveHelperERK7QPointFb',
        self._valueOf(p, 'QPointF'), a1,
    )
    return QWidget._cuteAt(address)

  def safeAreaMargins(self) -> QMargins:
    """
    Calls Qt's 'QMargins QWidgetPrivate::safeAreaMargins() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#safeAreaMargins

    Returns
    -------

    QMargins
      A new cute QMargins around the copy Qt gave back. Python owns it.
    """
    #  QMargins QWidgetPrivate::safeAreaMargins() const
    address = self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate15safeAreaMarginsEv',
    )
    from ..QtCore import QMargins
    return QMargins._cuteOwning(address)

  @overload(QPoint)
  @overload(NoneType)
  def redirected(self, offset: Optional[QPoint]) -> Optional[QPaintDevice]:
    """
    Calls Qt's 'QPaintDevice *QWidgetPrivate::redirected(QPoint *offset)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#redirected

    Parameters
    ----------

    offset : Optional[QPoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPaintDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintDevice *QWidgetPrivate::redirected(QPoint *offset) const
    address = self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate10redirectedEP6QPoint',
        self._addressOf(offset),
    )
    from ..QtGui import QPaintDevice
    return QPaintDevice._cuteAt(address)

  def nativeChildrenForced(self) -> bool:
    """
    Calls Qt's 'bool QWidgetPrivate::nativeChildrenForced() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#nativeChildrenForced
    """
    #  bool QWidgetPrivate::nativeChildrenForced() const
    return self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate20nativeChildrenForcedEv',
    )

  @overload(QRegion)
  def effectiveRectFor(self, region: QRegion) -> QRect:
    """
    Calls Qt's 'QRect QWidgetPrivate::effectiveRectFor(const QRegion &region)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#effectiveRectFor

    Parameters
    ----------

    region : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QWidgetPrivate::effectiveRectFor(const QRegion &region) const
    address = self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate16effectiveRectForERK7QRegion',
        self._valueOf(region),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QRect)
  def effectiveRectFor(self, rect: QRect) -> QRect:
    """
    Calls Qt's 'QRect QWidgetPrivate::effectiveRectFor(const QRect &rect)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#effectiveRectFor

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QWidgetPrivate::effectiveRectFor(const QRect &rect) const
    address = self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate16effectiveRectForERK5QRect',
        self._valueOf(rect),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def adjustedSize(self) -> QSize:
    """
    Calls Qt's 'QSize QWidgetPrivate::adjustedSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#adjustedSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWidgetPrivate::adjustedSize() const
    address = self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate12adjustedSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QPoint)
  def mapToWS(self, p: QPoint) -> QPoint:
    """
    Calls Qt's 'QPoint QWidgetPrivate::mapToWS(const QPoint &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#mapToWS

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QWidgetPrivate::mapToWS(const QPoint &p) const
    address = self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate7mapToWSERK6QPoint', self._valueOf(p),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(QRect)
  def mapToWS(self, r: QRect) -> QRect:
    """
    Calls Qt's 'QRect QWidgetPrivate::mapToWS(const QRect &r) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#mapToWS

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QWidgetPrivate::mapToWS(const QRect &r) const
    address = self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate7mapToWSERK5QRect', self._valueOf(r),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QPoint)
  def mapFromWS(self, p: QPoint) -> QPoint:
    """
    Calls Qt's 'QPoint QWidgetPrivate::mapFromWS(const QPoint &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#mapFromWS

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QWidgetPrivate::mapFromWS(const QPoint &p) const
    address = self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate9mapFromWSERK6QPoint', self._valueOf(p),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(QRect)
  def mapFromWS(self, r: QRect) -> QRect:
    """
    Calls Qt's 'QRect QWidgetPrivate::mapFromWS(const QRect &r) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#mapFromWS

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QWidgetPrivate::mapFromWS(const QRect &r) const
    address = self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate9mapFromWSERK5QRect', self._valueOf(r),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def rhiConfig(self) -> QPlatformBackingStoreRhiConfig:
    """
    Calls Qt's 'QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#rhiConfig

    Returns
    -------

    QPlatformBackingStoreRhiConfig
      A new cute QPlatformBackingStoreRhiConfig around the copy Qt gave back.
      Python owns it.
    """
    #  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
    ritual = 'ritual_ZNK14QWidgetPrivate9rhiConfigEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QWidgetPrivate9rhiConfigEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPlatformBackingStoreRhiConfig
    return QPlatformBackingStoreRhiConfig._cuteOwning(address)

  def texture(self) -> TextureData:
    """
    Calls Qt's 'TextureData QWidgetPrivate::texture() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#texture

    Returns
    -------

    TextureData
      A new cute QWidgetPrivate::TextureData around the copy Qt gave back.
      Python owns it.
    """
    #  TextureData QWidgetPrivate::texture() const
    ritual = 'ritual_ZNK14QWidgetPrivate7textureEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QWidgetPrivate7textureEv'
    address = self.uglySide.call(ritual)
    return QWidgetPrivate.TextureData._cuteOwning(address)

  def closestParentWidgetWithWindowHandle(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget
    *QWidgetPrivate::closestParentWidgetWithWindowHandle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QWidgetPrivate::closestParentWidgetWithWindowHandle() const
    address = self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate35closestParentWidgetWithWindowHandleEv',
    )
    return QWidget._cuteAt(address)

  @overload(FocusDirection)
  def nextPrevElementInFocusChain(
      self,
      direction: FocusDirection,
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget
    *QWidgetPrivate::nextPrevElementInFocusChain(FocusDirection direction)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#nextPrevElementInFocusChain

    Parameters
    ----------

    direction : FocusDirection
      Passed on as its number.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QWidgetPrivate::nextPrevElementInFocusChain(FocusDirection
    #      direction) const
    address = self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate27nextPrevElementInFocusChainENS_14Focus'
        'DirectionE',
        direction.value,
    )
    return QWidget._cuteAt(address)

  def isInFocusChain(self) -> bool:
    """
    Calls Qt's 'bool QWidgetPrivate::isInFocusChain() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#isInFocusChain
    """
    #  bool QWidgetPrivate::isInFocusChain() const
    return self.uglySide.call('ritual_ZNK14QWidgetPrivate14isInFocusChainEv')

  def isFocusChainConsistent(self) -> bool:
    """
    Calls Qt's 'bool QWidgetPrivate::isFocusChainConsistent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#isFocusChainConsistent
    """
    #  bool QWidgetPrivate::isFocusChainConsistent() const
    return self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate22isFocusChainConsistentEv',
    )

  @overload(Qt.FocusPolicy)
  @overload(Qt.FocusPolicy, QWidget)
  @overload(Qt.FocusPolicy, NoneType)
  def hasChildWithFocusPolicy(
      self,
      policy: Qt.FocusPolicy,
      excludeChildrenOf: Optional[QWidget] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QWidgetPrivate::hasChildWithFocusPolicy(Qt::FocusPolicy
    policy, const QWidget *excludeChildrenOf) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#hasChildWithFocusPolicy

    Parameters
    ----------

    policy : Qt.FocusPolicy
      Passed on as its number.

    excludeChildrenOf : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  bool QWidgetPrivate::hasChildWithFocusPolicy(Qt::FocusPolicy policy,
    #      const QWidget *excludeChildrenOf) const
    return self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate23hasChildWithFocusPolicyEN2Qt11FocusPol'
        'icyEPK7QWidget',
        policy.value, self._addressOf(excludeChildrenOf),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPainter)
  @overload(NoneType)
  def setSharedPainter(self, painter: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setSharedPainter(QPainter *painter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#setSharedPainter

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetPrivate::setSharedPainter(QPainter *painter)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate16setSharedPainterEP8QPainter',
        self._addressOf(painter),
    )

  @overload(QPoint)
  def setScreenForPoint(self, pos: QPoint) -> bool:
    """
    Calls Qt's 'bool QWidgetPrivate::setScreenForPoint(const QPoint &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#setScreenForPoint

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  bool QWidgetPrivate::setScreenForPoint(const QPoint &pos)
    return self.uglySide.call(
        'ritual_ZN14QWidgetPrivate17setScreenForPointERK6QPoint',
        self._valueOf(pos),
    )

  @overload(QScreen)
  @overload(NoneType)
  def setScreen(self, screen: Optional[QScreen]) -> bool:
    """
    Calls Qt's 'bool QWidgetPrivate::setScreen(QScreen *screen)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#setScreen

    Parameters
    ----------

    screen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWidgetPrivate::setScreen(QScreen *screen)
    return self.uglySide.call(
        'ritual_ZN14QWidgetPrivate9setScreenEP7QScreen',
        self._addressOf(screen),
    )

  @overload(QPalette)
  def setPalette_helper(self, a0: QPalette) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setPalette_helper(const QPalette &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#setPalette_helper

    Parameters
    ----------

    a0 : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.
    """
    #  void QWidgetPrivate::setPalette_helper(const QPalette &a0)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate17setPalette_helperERK8QPalette',
        self._valueOf(a0),
    )

  @overload(QRegion)
  def setMask_sys(self, a0: QRegion) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setMask_sys(const QRegion &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#setMask_sys

    Parameters
    ----------

    a0 : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QWidgetPrivate::setMask_sys(const QRegion &a0)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate11setMask_sysERK7QRegion',
        self._valueOf(a0),
    )

  def setFocus_sys(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setFocus_sys()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#setFocus_sys
    """
    #  void QWidgetPrivate::setFocus_sys()
    self.uglySide.call('ritual_ZN14QWidgetPrivate12setFocus_sysEv')

  @overload(QFont)
  def setFont_helper(self, font: QFont) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setFont_helper(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#setFont_helper

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QWidgetPrivate::setFont_helper(const QFont &font)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate14setFont_helperERK5QFont',
        self._valueOf(font),
    )

  @overload(Qt.LayoutDirection)
  def setLayoutDirection_helper(self, a0: Qt.LayoutDirection) -> None:
    """
    Calls Qt's 'void
    QWidgetPrivate::setLayoutDirection_helper(Qt::LayoutDirection a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#setLayoutDirection_helper

    Parameters
    ----------

    a0 : Qt.LayoutDirection
      Passed on as its number.
    """
    #  void QWidgetPrivate::setLayoutDirection_helper(Qt::LayoutDirection a0)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate25setLayoutDirection_helperEN2Qt15LayoutD'
        'irectionE',
        a0.value,
    )

  @overload(QLocale)
  @overload(QLocale, bool)
  def setLocale_helper(self, l: QLocale, forceUpdate: bool = False) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setLocale_helper(const QLocale &l, bool
    forceUpdate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#setLocale_helper

    Parameters
    ----------

    l : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.

    forceUpdate : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QWidgetPrivate::setLocale_helper(const QLocale &l, bool
    #      forceUpdate)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate16setLocale_helperERK7QLocaleb',
        self._valueOf(l), forceUpdate,
    )

  @overload(QStyle, bool)
  @overload(NoneType, bool)
  def setStyle_helper(
      self,
      newStyle: Optional[QStyle],
      propagate: bool,
  ) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setStyle_helper(QStyle *newStyle, bool
    propagate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#setStyle_helper

    Parameters
    ----------

    newStyle : Optional[QStyle]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propagate : bool
      Passed on as it is.
    """
    #  void QWidgetPrivate::setStyle_helper(QStyle *newStyle, bool propagate)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate15setStyle_helperEP6QStyleb',
        self._addressOf(newStyle), propagate,
    )

  @overload(bool)
  def setUpdatesEnabled_helper(self, a0: bool) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setUpdatesEnabled_helper(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#setUpdatesEnabled_helper

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QWidgetPrivate::setUpdatesEnabled_helper(bool a0)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate24setUpdatesEnabled_helperEb', a0,
    )

  @overload(QPaintEngine, float, QRegion)
  @overload(NoneType, float, QRegion)
  def setSystemClip(
      self,
      paintEngine: Optional[QPaintEngine],
      devicePixelRatio: float,
      region: QRegion,
  ) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setSystemClip(QPaintEngine *paintEngine,
    qreal devicePixelRatio, const QRegion &region)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#setSystemClip

    Parameters
    ----------

    paintEngine : Optional[QPaintEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    devicePixelRatio : float
      Passed on as it is.

    region : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QWidgetPrivate::setSystemClip(QPaintEngine *paintEngine, qreal
    #      devicePixelRatio, const QRegion &region)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate13setSystemClipEP12QPaintEnginedRK7QRegio'
        'n',
        self._addressOf(paintEngine), devicePixelRatio,
        self._valueOf(region),
    )

  @overload(bool)
  def setOpaque(self, opaque: bool) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setOpaque(bool opaque)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#setOpaque

    Parameters
    ----------

    opaque : bool
      Passed on as it is.
    """
    #  void QWidgetPrivate::setOpaque(bool opaque)
    self.uglySide.call('ritual_ZN14QWidgetPrivate9setOpaqueEb', opaque)

  def setDirtyOpaqueRegion(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setDirtyOpaqueRegion()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#setDirtyOpaqueRegion
    """
    #  void QWidgetPrivate::setDirtyOpaqueRegion()
    self.uglySide.call('ritual_ZN14QWidgetPrivate20setDirtyOpaqueRegionEv')

  def setWindowIcon_helper(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setWindowIcon_helper()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#setWindowIcon_helper
    """
    #  void QWidgetPrivate::setWindowIcon_helper()
    self.uglySide.call('ritual_ZN14QWidgetPrivate20setWindowIcon_helperEv')

  def setWindowIcon_sys(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setWindowIcon_sys()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#setWindowIcon_sys
    """
    #  void QWidgetPrivate::setWindowIcon_sys()
    self.uglySide.call('ritual_ZN14QWidgetPrivate17setWindowIcon_sysEv')

  @overload(float)
  def setWindowOpacity_sys(self, opacity: float) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setWindowOpacity_sys(qreal opacity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#setWindowOpacity_sys

    Parameters
    ----------

    opacity : float
      Passed on as it is.
    """
    #  void QWidgetPrivate::setWindowOpacity_sys(qreal opacity)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate20setWindowOpacity_sysEd', opacity,
    )

  @overload(int)
  def setWinId(self, a0: int) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setWinId(WId a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#setWinId

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QWidgetPrivate::setWinId(WId a0)
    self.uglySide.call('ritual_ZN14QWidgetPrivate8setWinIdEy', a0)

  @overload(QWidget, Qt.WindowFlags)
  @overload(NoneType, Qt.WindowFlags)
  def setParent_sys(
      self,
      parent: Optional[QWidget],
      a1: Qt.WindowFlags,
  ) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setParent_sys(QWidget *parent,
    Qt::WindowFlags a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#setParent_sys

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Qt.WindowFlags
      Passed on as its number.
    """
    #  void QWidgetPrivate::setParent_sys(QWidget *parent, Qt::WindowFlags
    #      a1)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate13setParent_sysEP7QWidget6QFlagsIN2Qt10Wi'
        'ndowTypeEE',
        self._addressOf(parent), a1.value,
    )

  @overload(int, int, int, int, bool)
  def setGeometry_sys(
      self,
      a0: int,
      a1: int,
      a2: int,
      a3: int,
      a4: bool,
  ) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setGeometry_sys(int a0, int a1, int a2,
    int a3, bool a4)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#setGeometry_sys

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.

    a3 : int
      Passed on as it is.

    a4 : bool
      Passed on as it is.
    """
    #  void QWidgetPrivate::setGeometry_sys(int a0, int a1, int a2, int a3,
    #      bool a4)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate15setGeometry_sysEiiiib',
        a0, a1, a2, a3, a4,
    )

  @overload(bool)
  def setVisible(self, a0: bool) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setVisible(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#setVisible

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QWidgetPrivate::setVisible(bool a0)
    ritual = 'ritual_ZN14QWidgetPrivate10setVisibleEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QWidgetPrivate10setVisibleEb'
    self.uglySide.call(ritual, a0)

  @overload(bool)
  def setEnabled_helper(self, a0: bool) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setEnabled_helper(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#setEnabled_helper

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QWidgetPrivate::setEnabled_helper(bool a0)
    self.uglySide.call('ritual_ZN14QWidgetPrivate17setEnabled_helperEb', a0)

  @overload(str)
  def setWindowIconText_sys(self, cap: str) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setWindowIconText_sys(const QString
    &cap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#setWindowIconText_sys

    Parameters
    ----------

    cap : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidgetPrivate::setWindowIconText_sys(const QString &cap)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate21setWindowIconText_sysERK7QString', cap,
    )

  @overload(str)
  def setWindowIconText_helper(self, cap: str) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setWindowIconText_helper(const QString
    &cap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#setWindowIconText_helper

    Parameters
    ----------

    cap : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidgetPrivate::setWindowIconText_helper(const QString &cap)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate24setWindowIconText_helperERK7QString',
        cap,
    )

  @overload(str)
  def setWindowTitle_sys(self, cap: str) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setWindowTitle_sys(const QString &cap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#setWindowTitle_sys

    Parameters
    ----------

    cap : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidgetPrivate::setWindowTitle_sys(const QString &cap)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate18setWindowTitle_sysERK7QString', cap,
    )

  @overload(str)
  def setWindowFilePath_sys(self, filePath: str) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setWindowFilePath_sys(const QString
    &filePath)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#setWindowFilePath_sys

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidgetPrivate::setWindowFilePath_sys(const QString &filePath)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate21setWindowFilePath_sysERK7QString',
        filePath,
    )

  @overload(QCursor)
  def setCursor_sys(self, cursor: QCursor) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setCursor_sys(const QCursor &cursor)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#setCursor_sys

    Parameters
    ----------

    cursor : QCursor
      Passed on as a value: Qt reads the C++ QCursor, which stays Python's
      own.
    """
    #  void QWidgetPrivate::setCursor_sys(const QCursor &cursor)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate13setCursor_sysERK7QCursor',
        self._valueOf(cursor),
    )

  @overload(str)
  def setWindowTitle_helper(self, cap: str) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setWindowTitle_helper(const QString
    &cap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#setWindowTitle_helper

    Parameters
    ----------

    cap : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidgetPrivate::setWindowTitle_helper(const QString &cap)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate21setWindowTitle_helperERK7QString', cap,
    )

  @overload(str)
  def setWindowFilePath_helper(self, filePath: str) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setWindowFilePath_helper(const QString
    &filePath)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#setWindowFilePath_helper

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidgetPrivate::setWindowFilePath_helper(const QString &filePath)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate24setWindowFilePath_helperERK7QString',
        filePath,
    )

  def setWindowModified_helper(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setWindowModified_helper()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#setWindowModified_helper
    """
    #  void QWidgetPrivate::setWindowModified_helper()
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate24setWindowModified_helperEv',
    )

  @overload(Qt.WindowFlags)
  def setWindowFlags(self, windowFlags: Qt.WindowFlags) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setWindowFlags(Qt::WindowFlags
    windowFlags)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#setWindowFlags

    Parameters
    ----------

    windowFlags : Qt.WindowFlags
      Passed on as its number.
    """
    #  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
    ritual = (
        'ritual_ZN14QWidgetPrivate14setWindowFlagsE6QFlagsIN2Qt10WindowType'
        'EE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QWidgetPrivate14setWindowFlagsE6QFlagsIN2Qt10Wind'
          'owTypeEE')
    self.uglySide.call(ritual, windowFlags.value)

  def setConstraints_sys(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setConstraints_sys()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#setConstraints_sys
    """
    #  void QWidgetPrivate::setConstraints_sys()
    self.uglySide.call('ritual_ZN14QWidgetPrivate18setConstraints_sysEv')

  @overload(int, int, int, int)
  def setLayoutItemMargins(
      self,
      left: int,
      top: int,
      right: int,
      bottom: int,
  ) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setLayoutItemMargins(int left, int top,
    int right, int bottom)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#setLayoutItemMargins

    Parameters
    ----------

    left : int
      Passed on as it is.

    top : int
      Passed on as it is.

    right : int
      Passed on as it is.

    bottom : int
      Passed on as it is.
    """
    #  void QWidgetPrivate::setLayoutItemMargins(int left, int top, int
    #      right, int bottom)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate20setLayoutItemMarginsEiiii',
        left, top, right, bottom,
    )

  @overload(QStyle.SubElement)
  @overload(QStyle.SubElement, QStyleOption)
  @overload(QStyle.SubElement, NoneType)
  def setLayoutItemMargins(
      self,
      element: QStyle.SubElement,
      opt: Optional[QStyleOption] = None,
  ) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setLayoutItemMargins(QStyle::SubElement
    element, const QStyleOption *opt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#setLayoutItemMargins

    Parameters
    ----------

    element : QStyle.SubElement
      Passed on as its number.

    opt : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QWidgetPrivate::setLayoutItemMargins(QStyle::SubElement element,
    #      const QStyleOption *opt)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate20setLayoutItemMarginsEN6QStyle10SubEleme'
        'ntEPK12QStyleOption',
        element.value, self._addressOf(opt),
    )

  def setModal_sys(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setModal_sys()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#setModal_sys
    """
    #  void QWidgetPrivate::setModal_sys()
    self.uglySide.call('ritual_ZN14QWidgetPrivate12setModal_sysEv')

  @overload(QPaintDevice, QPoint)
  @overload(NoneType, QPoint)
  def setRedirected(
      self,
      replacement: Optional[QPaintDevice],
      offset: QPoint,
  ) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setRedirected(QPaintDevice *replacement,
    const QPoint &offset)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#setRedirected

    Parameters
    ----------

    replacement : Optional[QPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    offset : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QWidgetPrivate::setRedirected(QPaintDevice *replacement, const
    #      QPoint &offset)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate13setRedirectedEP12QPaintDeviceRK6QPoint',
        self._addressOf(replacement, 'QPaintDevice'), self._valueOf(offset),
    )

  def setWSGeometry(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setWSGeometry()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#setWSGeometry
    """
    #  void QWidgetPrivate::setWSGeometry()
    self.uglySide.call('ritual_ZN14QWidgetPrivate13setWSGeometryEv')

  def setRenderToTexture(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setRenderToTexture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#setRenderToTexture
    """
    #  void QWidgetPrivate::setRenderToTexture()
    self.uglySide.call('ritual_ZN14QWidgetPrivate18setRenderToTextureEv')

  def setTextureChildSeen(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setTextureChildSeen()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#setTextureChildSeen
    """
    #  void QWidgetPrivate::setTextureChildSeen()
    self.uglySide.call('ritual_ZN14QWidgetPrivate19setTextureChildSeenEv')

  @overload()
  @overload(bool)
  def setNetWmWindowTypes(self, skipIfMissing: bool = False) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::setNetWmWindowTypes(bool
    skipIfMissing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#setNetWmWindowTypes

    Parameters
    ----------

    skipIfMissing : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QWidgetPrivate::setNetWmWindowTypes(bool skipIfMissing)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate19setNetWmWindowTypesEb', skipIfMissing,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QWidgetPrivate::QWidgetPrivate(decltype(QObjectPrivateVersion)
    a0)': names the enum 'QtPrivate_6_12_0', whose class cannot be named
    here.
    """
    raise NotImplementedError(
        "'QWidgetPrivate.__init__' has no cute function yet. Qt's "
        "'QWidgetPrivate::QWidgetPrivate(decltype(QObjectPrivateVersion) "
        "a0)': names the enum 'QtPrivate_6_12_0', whose class cannot be "
        "named here.")

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

  def q_func(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QWidgetPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#q_func

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QWidgetPrivate::q_func()
    address = self.uglySide.call('ritual_ZN14QWidgetPrivate6q_funcEv')
    return QWidget._cuteAt(address)

  @overload(QWidget, Qt.WindowFlags)
  @overload(NoneType, Qt.WindowFlags)
  def init(
      self,
      desktopWidget: Optional[QWidget],
      f: Qt.WindowFlags,
  ) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::init(QWidget *desktopWidget,
    Qt::WindowFlags f)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#init

    Parameters
    ----------

    desktopWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    f : Qt.WindowFlags
      Passed on as its number.
    """
    #  void QWidgetPrivate::init(QWidget *desktopWidget, Qt::WindowFlags f)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate4initEP7QWidget6QFlagsIN2Qt10WindowTypeEE',
        self._addressOf(desktopWidget), f.value,
    )

  def create(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::create()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#create
    """
    #  void QWidgetPrivate::create()
    self.uglySide.call('ritual_ZN14QWidgetPrivate6createEv')

  def createRecursively(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::createRecursively()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#createRecursively
    """
    #  void QWidgetPrivate::createRecursively()
    self.uglySide.call('ritual_ZN14QWidgetPrivate17createRecursivelyEv')

  def createWinId(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::createWinId()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#createWinId
    """
    #  void QWidgetPrivate::createWinId()
    self.uglySide.call('ritual_ZN14QWidgetPrivate11createWinIdEv')

  def createTLExtra(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::createTLExtra()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#createTLExtra
    """
    #  void QWidgetPrivate::createTLExtra()
    self.uglySide.call('ritual_ZN14QWidgetPrivate13createTLExtraEv')

  def createExtra(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::createExtra()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#createExtra
    """
    #  void QWidgetPrivate::createExtra()
    self.uglySide.call('ritual_ZN14QWidgetPrivate11createExtraEv')

  def deleteExtra(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::deleteExtra()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#deleteExtra
    """
    #  void QWidgetPrivate::deleteExtra()
    self.uglySide.call('ritual_ZN14QWidgetPrivate11deleteExtraEv')

  def createSysExtra(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::createSysExtra()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#createSysExtra
    """
    #  void QWidgetPrivate::createSysExtra()
    self.uglySide.call('ritual_ZN14QWidgetPrivate14createSysExtraEv')

  def deleteSysExtra(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::deleteSysExtra()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#deleteSysExtra
    """
    #  void QWidgetPrivate::deleteSysExtra()
    self.uglySide.call('ritual_ZN14QWidgetPrivate14deleteSysExtraEv')

  def createTLSysExtra(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::createTLSysExtra()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#createTLSysExtra
    """
    #  void QWidgetPrivate::createTLSysExtra()
    self.uglySide.call('ritual_ZN14QWidgetPrivate16createTLSysExtraEv')

  def deleteTLSysExtra(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::deleteTLSysExtra()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#deleteTLSysExtra
    """
    #  void QWidgetPrivate::deleteTLSysExtra()
    self.uglySide.call('ritual_ZN14QWidgetPrivate16deleteTLSysExtraEv')

  def updateSystemBackground(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::updateSystemBackground()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#updateSystemBackground
    """
    #  void QWidgetPrivate::updateSystemBackground()
    self.uglySide.call('ritual_ZN14QWidgetPrivate22updateSystemBackgroundEv')

  def propagatePaletteChange(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::propagatePaletteChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#propagatePaletteChange
    """
    #  void QWidgetPrivate::propagatePaletteChange()
    self.uglySide.call('ritual_ZN14QWidgetPrivate22propagatePaletteChangeEv')

  def resolvePalette(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::resolvePalette()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#resolvePalette
    """
    #  void QWidgetPrivate::resolvePalette()
    self.uglySide.call('ritual_ZN14QWidgetPrivate14resolvePaletteEv')

  def raise_sys(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::raise_sys()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#raise_sys
    """
    #  void QWidgetPrivate::raise_sys()
    self.uglySide.call('ritual_ZN14QWidgetPrivate9raise_sysEv')

  def lower_sys(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::lower_sys()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#lower_sys
    """
    #  void QWidgetPrivate::lower_sys()
    self.uglySide.call('ritual_ZN14QWidgetPrivate9lower_sysEv')

  @overload(QWidget)
  @overload(NoneType)
  def stackUnder_sys(self, a0: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::stackUnder_sys(QWidget *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#stackUnder_sys

    Parameters
    ----------

    a0 : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetPrivate::stackUnder_sys(QWidget *a0)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate14stackUnder_sysEP7QWidget',
        self._addressOf(a0),
    )

  def updateFocusChild(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::updateFocusChild()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#updateFocusChild
    """
    #  void QWidgetPrivate::updateFocusChild()
    self.uglySide.call('ritual_ZN14QWidgetPrivate16updateFocusChildEv')

  @overload(QFont)
  def updateFont(self, a0: QFont) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::updateFont(const QFont &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#updateFont

    Parameters
    ----------

    a0 : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QWidgetPrivate::updateFont(const QFont &a0)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate10updateFontERK5QFont', self._valueOf(a0),
    )

  def resolveFont(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::resolveFont()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#resolveFont
    """
    #  void QWidgetPrivate::resolveFont()
    self.uglySide.call('ritual_ZN14QWidgetPrivate11resolveFontEv')

  def resolveLayoutDirection(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::resolveLayoutDirection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#resolveLayoutDirection
    """
    #  void QWidgetPrivate::resolveLayoutDirection()
    self.uglySide.call('ritual_ZN14QWidgetPrivate22resolveLayoutDirectionEv')

  def resolveLocale(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::resolveLocale()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#resolveLocale
    """
    #  void QWidgetPrivate::resolveLocale()
    self.uglySide.call('ritual_ZN14QWidgetPrivate13resolveLocaleEv')

  def inheritStyle(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::inheritStyle()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#inheritStyle
    """
    #  void QWidgetPrivate::inheritStyle()
    self.uglySide.call('ritual_ZN14QWidgetPrivate12inheritStyleEv')

  @overload(QPainter, QRegion)
  @overload(NoneType, QRegion)
  @overload(QPainter, QRegion, DrawWidgetFlags)
  @overload(NoneType, QRegion, DrawWidgetFlags)
  def paintBackground(
      self,
      a0: Optional[QPainter],
      a1: QRegion,
      flags: DrawWidgetFlags = DrawWidgetFlags.DrawAsRoot,
  ) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::paintBackground(QPainter *a0, const
    QRegion &a1, DrawWidgetFlags flags) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#paintBackground

    Parameters
    ----------

    a0 : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.

    flags : DrawWidgetFlags
      Passed on as its number. May be left out, as in Qt: it is then
      DrawWidgetFlags.DrawAsRoot.
    """
    #  void QWidgetPrivate::paintBackground(QPainter *a0, const QRegion &a1,
    #      DrawWidgetFlags flags) const
    self.uglySide.call(
        'ritual_ZNK14QWidgetPrivate15paintBackgroundEP8QPainterRK7QRegion6Q'
        'FlagsINS_14DrawWidgetFlagEE',
        self._addressOf(a0), self._valueOf(a1), flags.value,
    )

  @overload(QRegion, QWidget.RenderFlags)
  def prepareToRender(
      self,
      region: QRegion,
      renderFlags: QWidget.RenderFlags,
  ) -> QRegion:
    """
    Calls Qt's 'QRegion QWidgetPrivate::prepareToRender(const QRegion
    &region, QWidget::RenderFlags renderFlags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#prepareToRender

    Parameters
    ----------

    region : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.

    renderFlags : QWidget.RenderFlags
      Passed on as its number.

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QWidgetPrivate::prepareToRender(const QRegion &region,
    #      QWidget::RenderFlags renderFlags)
    address = self.uglySide.call(
        'ritual_ZN14QWidgetPrivate15prepareToRenderERK7QRegion6QFlagsIN7QWi'
        'dget10RenderFlagEE',
        self._valueOf(region), renderFlags.value,
    )
    from ..QtGui import QRegion
    return QRegion._cuteOwning(address)

  @overload(QPainter, QPoint, QRegion, QWidget.RenderFlags)
  @overload(NoneType, QPoint, QRegion, QWidget.RenderFlags)
  def render_helper(
      self,
      painter: Optional[QPainter],
      targetOffset: QPoint,
      sourceRegion: QRegion,
      renderFlags: QWidget.RenderFlags,
  ) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::render_helper(QPainter *painter, const
    QPoint &targetOffset, const QRegion &sourceRegion, QWidget::RenderFlags
    renderFlags)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#render_helper

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    targetOffset : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    sourceRegion : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.

    renderFlags : QWidget.RenderFlags
      Passed on as its number.
    """
    #  void QWidgetPrivate::render_helper(QPainter *painter, const QPoint
    #      &targetOffset, const QRegion &sourceRegion, QWidget::RenderFlags
    #      renderFlags)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate13render_helperEP8QPainterRK6QPointRK7QRe'
        'gion6QFlagsIN7QWidget10RenderFlagEE',
        self._addressOf(painter), self._valueOf(targetOffset),
        self._valueOf(sourceRegion), renderFlags.value,
    )

  @overload(QPaintDevice, QPoint, QRegion, QWidget.RenderFlags)
  @overload(NoneType, QPoint, QRegion, QWidget.RenderFlags)
  def render(
      self,
      target: Optional[QPaintDevice],
      targetOffset: QPoint,
      sourceRegion: QRegion,
      renderFlags: QWidget.RenderFlags,
  ) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::render(QPaintDevice *target, const
    QPoint &targetOffset, const QRegion &sourceRegion, QWidget::RenderFlags
    renderFlags)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#render

    Parameters
    ----------

    target : Optional[QPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    targetOffset : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    sourceRegion : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.

    renderFlags : QWidget.RenderFlags
      Passed on as its number.
    """
    #  void QWidgetPrivate::render(QPaintDevice *target, const QPoint
    #      &targetOffset, const QRegion &sourceRegion, QWidget::RenderFlags
    #      renderFlags)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate6renderEP12QPaintDeviceRK6QPointRK7QRegio'
        'n6QFlagsIN7QWidget10RenderFlagEE',
        self._addressOf(target, 'QPaintDevice'), self._valueOf(targetOffset),
        self._valueOf(sourceRegion), renderFlags.value,
    )

  @overload(QPaintDevice, QRegion, QPoint, DrawWidgetFlags)
  @overload(NoneType, QRegion, QPoint, DrawWidgetFlags)
  @overload(QPaintDevice, QRegion, QPoint, DrawWidgetFlags, QPainter)
  @overload(QPaintDevice, QRegion, QPoint, DrawWidgetFlags, NoneType)
  @overload(NoneType, QRegion, QPoint, DrawWidgetFlags, QPainter)
  @overload(NoneType, QRegion, QPoint, DrawWidgetFlags, NoneType)
  @overload(
      QPaintDevice, QRegion, QPoint, DrawWidgetFlags, QPainter,
      QWidgetRepaintManager,
  )
  @overload(
      QPaintDevice, QRegion, QPoint, DrawWidgetFlags, QPainter, NoneType,
  )
  @overload(
      QPaintDevice, QRegion, QPoint, DrawWidgetFlags, NoneType,
      QWidgetRepaintManager,
  )
  @overload(
      QPaintDevice, QRegion, QPoint, DrawWidgetFlags, NoneType, NoneType,
  )
  @overload(
      NoneType, QRegion, QPoint, DrawWidgetFlags, QPainter,
      QWidgetRepaintManager,
  )
  @overload(NoneType, QRegion, QPoint, DrawWidgetFlags, QPainter, NoneType)
  @overload(
      NoneType, QRegion, QPoint, DrawWidgetFlags, NoneType,
      QWidgetRepaintManager,
  )
  @overload(NoneType, QRegion, QPoint, DrawWidgetFlags, NoneType, NoneType)
  def drawWidget(
      self,
      pdev: Optional[QPaintDevice],
      rgn: QRegion,
      offset: QPoint,
      flags: DrawWidgetFlags,
      sharedPainter: Optional[QPainter] = None,
      repaintManager: Optional[QWidgetRepaintManager] = None,
  ) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::drawWidget(QPaintDevice *pdev, const
    QRegion &rgn, const QPoint &offset, DrawWidgetFlags flags, QPainter
    *sharedPainter, QWidgetRepaintManager *repaintManager)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#drawWidget

    Parameters
    ----------

    pdev : Optional[QPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rgn : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.

    offset : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    flags : DrawWidgetFlags
      Passed on as its number.

    sharedPainter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    repaintManager : Optional[QWidgetRepaintManager]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QWidgetPrivate::drawWidget(QPaintDevice *pdev, const QRegion
    #      &rgn, const QPoint &offset, DrawWidgetFlags flags, QPainter
    #      *sharedPainter, QWidgetRepaintManager *repaintManager)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate10drawWidgetEP12QPaintDeviceRK7QRegionRK6'
        'QPoint6QFlagsINS_14DrawWidgetFlagEEP8QPainterP21QWidgetRepaintMana'
        'ger',
        self._addressOf(pdev, 'QPaintDevice'), self._valueOf(rgn),
        self._valueOf(offset), flags.value, self._addressOf(sharedPainter),
        self._addressOf(repaintManager),
    )

  @overload(QRegion)
  def sendPaintEvent(self, toBePainted: QRegion) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::sendPaintEvent(const QRegion
    &toBePainted)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#sendPaintEvent

    Parameters
    ----------

    toBePainted : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QWidgetPrivate::sendPaintEvent(const QRegion &toBePainted)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate14sendPaintEventERK7QRegion',
        self._valueOf(toBePainted),
    )

  @overload(
      QPaintDevice, QList[QObject], int, QRegion, QPoint, DrawWidgetFlags,
      QPainter, QWidgetRepaintManager,
  )
  @overload(
      QPaintDevice, QList[QObject], int, QRegion, QPoint, DrawWidgetFlags,
      QPainter, NoneType,
  )
  @overload(
      QPaintDevice, QList[QObject], int, QRegion, QPoint, DrawWidgetFlags,
      NoneType, QWidgetRepaintManager,
  )
  @overload(
      QPaintDevice, QList[QObject], int, QRegion, QPoint, DrawWidgetFlags,
      NoneType, NoneType,
  )
  @overload(
      NoneType, QList[QObject], int, QRegion, QPoint, DrawWidgetFlags,
      QPainter, QWidgetRepaintManager,
  )
  @overload(
      NoneType, QList[QObject], int, QRegion, QPoint, DrawWidgetFlags,
      QPainter, NoneType,
  )
  @overload(
      NoneType, QList[QObject], int, QRegion, QPoint, DrawWidgetFlags,
      NoneType, QWidgetRepaintManager,
  )
  @overload(
      NoneType, QList[QObject], int, QRegion, QPoint, DrawWidgetFlags,
      NoneType, NoneType,
  )
  def paintSiblingsRecursive(
      self,
      pdev: Optional[QPaintDevice],
      children: QList[QObject],
      index: int,
      rgn: QRegion,
      offset: QPoint,
      flags: DrawWidgetFlags,
      sharedPainter: Optional[QPainter],
      repaintManager: Optional[QWidgetRepaintManager],
  ) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::paintSiblingsRecursive(QPaintDevice
    *pdev, const QObjectList &children, int index, const QRegion &rgn, const
    QPoint &offset, DrawWidgetFlags flags, QPainter *sharedPainter,
    QWidgetRepaintManager *repaintManager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#paintSiblingsRecursive

    Parameters
    ----------

    pdev : Optional[QPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    children : QList[QObject]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    index : int
      Passed on as it is.

    rgn : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.

    offset : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    flags : DrawWidgetFlags
      Passed on as its number.

    sharedPainter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    repaintManager : Optional[QWidgetRepaintManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetPrivate::paintSiblingsRecursive(QPaintDevice *pdev, const
    #      QObjectList &children, int index, const QRegion &rgn, const QPoint
    #      &offset, DrawWidgetFlags flags, QPainter *sharedPainter,
    #      QWidgetRepaintManager *repaintManager)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate22paintSiblingsRecursiveEP12QPaintDeviceR'
        'K5QListIP7QObjectEiRK7QRegionRK6QPoint6QFlagsINS_14DrawWidgetFlagE'
        'EP8QPainterP21QWidgetRepaintManager',
        self._addressOf(pdev, 'QPaintDevice'), self._valueOf(children),
        index, self._valueOf(rgn), self._valueOf(offset), flags.value,
        self._addressOf(sharedPainter), self._addressOf(repaintManager),
    )

  @overload(QRegion)
  def paintOnScreen(self, rgn: QRegion) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::paintOnScreen(const QRegion &rgn)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#paintOnScreen

    Parameters
    ----------

    rgn : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QWidgetPrivate::paintOnScreen(const QRegion &rgn)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate13paintOnScreenERK7QRegion',
        self._valueOf(rgn),
    )

  def updateIsOpaque(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::updateIsOpaque()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#updateIsOpaque
    """
    #  void QWidgetPrivate::updateIsOpaque()
    self.uglySide.call('ritual_ZN14QWidgetPrivate14updateIsOpaqueEv')

  def updateIsTranslucent(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::updateIsTranslucent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#updateIsTranslucent
    """
    #  void QWidgetPrivate::updateIsTranslucent()
    self.uglySide.call('ritual_ZN14QWidgetPrivate19updateIsTranslucentEv')

  def invalidateGraphicsEffectsRecursively(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::invalidateGraphicsEffectsRecursively()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html
    """
    #  void QWidgetPrivate::invalidateGraphicsEffectsRecursively()
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate36invalidateGraphicsEffectsRecursivelyEv',
    )

  def close(self) -> bool:
    """
    Calls Qt's 'bool QWidgetPrivate::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#close
    """
    #  bool QWidgetPrivate::close()
    return self.uglySide.call('ritual_ZN14QWidgetPrivate5closeEv')

  @overload(CloseMode)
  def handleClose(self, mode: CloseMode) -> bool:
    """
    Calls Qt's 'bool QWidgetPrivate::handleClose(CloseMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#handleClose

    Parameters
    ----------

    mode : CloseMode
      Passed on as its number.
    """
    #  bool QWidgetPrivate::handleClose(CloseMode mode)
    return self.uglySide.call(
        'ritual_ZN14QWidgetPrivate11handleCloseENS_9CloseModeE', mode.value,
    )

  def adjustQuitOnCloseAttribute(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::adjustQuitOnCloseAttribute()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#adjustQuitOnCloseAttribute
    """
    #  void QWidgetPrivate::adjustQuitOnCloseAttribute()
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate26adjustQuitOnCloseAttributeEv',
    )

  @overload(int, int)
  def scrollChildren(self, dx: int, dy: int) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::scrollChildren(int dx, int dy)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#scrollChildren

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.
    """
    #  void QWidgetPrivate::scrollChildren(int dx, int dy)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate14scrollChildrenEii', dx, dy,
    )

  @overload(QRect, int, int)
  def moveRect(self, a0: QRect, dx: int, dy: int) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::moveRect(const QRect &a0, int dx, int
    dy)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#moveRect

    Parameters
    ----------

    a0 : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.
    """
    #  void QWidgetPrivate::moveRect(const QRect &a0, int dx, int dy)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate8moveRectERK5QRectii',
        self._valueOf(a0), dx, dy,
    )

  @overload(QRect, int, int)
  def scrollRect(self, a0: QRect, dx: int, dy: int) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::scrollRect(const QRect &a0, int dx, int
    dy)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#scrollRect

    Parameters
    ----------

    a0 : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.
    """
    #  void QWidgetPrivate::scrollRect(const QRect &a0, int dx, int dy)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate10scrollRectERK5QRectii',
        self._valueOf(a0), dx, dy,
    )

  @overload(QPoint, QSize)
  def invalidateBackingStore_resizeHelper(
      self,
      oldPos: QPoint,
      oldSize: QSize,
  ) -> None:
    """
    Calls Qt's 'void
    QWidgetPrivate::invalidateBackingStore_resizeHelper(const QPoint &oldPos,
    const QSize &oldSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html

    Parameters
    ----------

    oldPos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    oldSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QWidgetPrivate::invalidateBackingStore_resizeHelper(const QPoint
    #      &oldPos, const QSize &oldSize)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate35invalidateBackingStore_resizeHelperERK6'
        'QPointRK5QSize',
        self._valueOf(oldPos), self._valueOf(oldSize),
    )

  @overload()
  def syncBackingStore(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::syncBackingStore()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#syncBackingStore
    """
    #  void QWidgetPrivate::syncBackingStore()
    self.uglySide.call('ritual_ZN14QWidgetPrivate16syncBackingStoreEv')

  @overload(QRegion)
  def syncBackingStore(self, region: QRegion) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::syncBackingStore(const QRegion
    &region)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#syncBackingStore

    Parameters
    ----------

    region : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QWidgetPrivate::syncBackingStore(const QRegion &region)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate16syncBackingStoreERK7QRegion',
        self._valueOf(region),
    )

  @overload(QEvent)
  @overload(NoneType)
  def updateWidgetTransform(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::updateWidgetTransform(QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#updateWidgetTransform

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetPrivate::updateWidgetTransform(QEvent *event)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate21updateWidgetTransformEP6QEvent',
        self._addressOf(event),
    )

  @overload(QWidget)
  @overload(NoneType)
  def reparentFocusWidgets(self, oldtlw: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::reparentFocusWidgets(QWidget *oldtlw)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#reparentFocusWidgets

    Parameters
    ----------

    oldtlw : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetPrivate::reparentFocusWidgets(QWidget *oldtlw)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate20reparentFocusWidgetsEP7QWidget',
        self._addressOf(oldtlw),
    )

  @overload(bool)
  def showChildren(self, spontaneous: bool) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::showChildren(bool spontaneous)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#showChildren

    Parameters
    ----------

    spontaneous : bool
      Passed on as it is.
    """
    #  void QWidgetPrivate::showChildren(bool spontaneous)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate12showChildrenEb', spontaneous,
    )

  @overload(bool)
  def hideChildren(self, spontaneous: bool) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::hideChildren(bool spontaneous)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#hideChildren

    Parameters
    ----------

    spontaneous : bool
      Passed on as it is.
    """
    #  void QWidgetPrivate::hideChildren(bool spontaneous)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate12hideChildrenEb', spontaneous,
    )

  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, Qt.WindowFlags)
  @overload(NoneType, Qt.WindowFlags)
  def reparentWidgetWindows(
      self,
      parentWithWindow: Optional[QWidget],
      windowFlags: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::reparentWidgetWindows(QWidget
    *parentWithWindow, Qt::WindowFlags windowFlags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#reparentWidgetWindows

    Parameters
    ----------

    parentWithWindow : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    windowFlags : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  void QWidgetPrivate::reparentWidgetWindows(QWidget *parentWithWindow,
    #      Qt::WindowFlags windowFlags)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate21reparentWidgetWindowsEP7QWidget6QFlagsI'
        'N2Qt10WindowTypeEE',
        self._addressOf(parentWithWindow), windowFlags.value,
    )

  @overload(QWidget)
  @overload(NoneType)
  def reparentWidgetWindowChildren(
      self,
      parentWithWindow: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::reparentWidgetWindowChildren(QWidget
    *parentWithWindow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#reparentWidgetWindowChildren

    Parameters
    ----------

    parentWithWindow : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetPrivate::reparentWidgetWindowChildren(QWidget
    #      *parentWithWindow)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate28reparentWidgetWindowChildrenEP7QWidget',
        self._addressOf(parentWithWindow),
    )

  @overload(int, int)
  def scroll_sys(self, dx: int, dy: int) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::scroll_sys(int dx, int dy)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#scroll_sys

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.
    """
    #  void QWidgetPrivate::scroll_sys(int dx, int dy)
    self.uglySide.call('ritual_ZN14QWidgetPrivate10scroll_sysEii', dx, dy)

  @overload(int, int, QRect)
  def scroll_sys(self, dx: int, dy: int, r: QRect) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::scroll_sys(int dx, int dy, const QRect
    &r)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#scroll_sys

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QWidgetPrivate::scroll_sys(int dx, int dy, const QRect &r)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate10scroll_sysEiiRK5QRect',
        dx, dy, self._valueOf(r),
    )

  def deactivateWidgetCleanup(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::deactivateWidgetCleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#deactivateWidgetCleanup
    """
    #  void QWidgetPrivate::deactivateWidgetCleanup()
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate23deactivateWidgetCleanupEv',
    )

  def fixPosIncludesFrame(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::fixPosIncludesFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#fixPosIncludesFrame
    """
    #  void QWidgetPrivate::fixPosIncludesFrame()
    self.uglySide.call('ritual_ZN14QWidgetPrivate19fixPosIncludesFrameEv')

  @overload()
  @overload(bool)
  @overload(bool, bool)
  def sendPendingMoveAndResizeEvents(
      self,
      recursive: bool = False,
      disableUpdates: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::sendPendingMoveAndResizeEvents(bool
    recursive, bool disableUpdates)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#sendPendingMoveAndResizeEvents

    Parameters
    ----------

    recursive : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    disableUpdates : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QWidgetPrivate::sendPendingMoveAndResizeEvents(bool recursive,
    #      bool disableUpdates)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate30sendPendingMoveAndResizeEventsEbb',
        recursive, disableUpdates,
    )

  def activateChildLayoutsRecursively(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::activateChildLayoutsRecursively()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html
    """
    #  void QWidgetPrivate::activateChildLayoutsRecursively()
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate31activateChildLayoutsRecursivelyEv',
    )

  def show_recursive(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::show_recursive()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#show_recursive
    """
    #  void QWidgetPrivate::show_recursive()
    self.uglySide.call('ritual_ZN14QWidgetPrivate14show_recursiveEv')

  def show_helper(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::show_helper()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#show_helper
    """
    #  void QWidgetPrivate::show_helper()
    self.uglySide.call('ritual_ZN14QWidgetPrivate11show_helperEv')

  def show_sys(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::show_sys()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#show_sys
    """
    #  void QWidgetPrivate::show_sys()
    self.uglySide.call('ritual_ZN14QWidgetPrivate8show_sysEv')

  def hide_sys(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::hide_sys()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#hide_sys
    """
    #  void QWidgetPrivate::hide_sys()
    self.uglySide.call('ritual_ZN14QWidgetPrivate8hide_sysEv')

  def hide_helper(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::hide_helper()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#hide_helper
    """
    #  void QWidgetPrivate::hide_helper()
    self.uglySide.call('ritual_ZN14QWidgetPrivate11hide_helperEv')

  def _q_showIfNotHidden(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::_q_showIfNotHidden()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#_q_showIfNotHidden
    """
    #  void QWidgetPrivate::_q_showIfNotHidden()
    self.uglySide.call('ritual_ZN14QWidgetPrivate18_q_showIfNotHiddenEv')

  def updateFrameStrut(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::updateFrameStrut()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#updateFrameStrut
    """
    #  void QWidgetPrivate::updateFrameStrut()
    self.uglySide.call('ritual_ZN14QWidgetPrivate16updateFrameStrutEv')

  def unsetCursor_sys(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::unsetCursor_sys()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#unsetCursor_sys
    """
    #  void QWidgetPrivate::unsetCursor_sys()
    self.uglySide.call('ritual_ZN14QWidgetPrivate15unsetCursor_sysEv')

  @overload(bool)
  def updateGeometry_helper(self, forceUpdate: bool) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::updateGeometry_helper(bool
    forceUpdate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#updateGeometry_helper

    Parameters
    ----------

    forceUpdate : bool
      Passed on as it is.
    """
    #  void QWidgetPrivate::updateGeometry_helper(bool forceUpdate)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate21updateGeometry_helperEb', forceUpdate,
    )

  def updateContentsRect(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::updateContentsRect()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#updateContentsRect
    """
    #  void QWidgetPrivate::updateContentsRect()
    self.uglySide.call('ritual_ZN14QWidgetPrivate18updateContentsRectEv')

  def aboutToDestroy(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::aboutToDestroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#aboutToDestroy
    """
    #  void QWidgetPrivate::aboutToDestroy()
    ritual = 'ritual_ZN14QWidgetPrivate14aboutToDestroyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QWidgetPrivate14aboutToDestroyEv'
    self.uglySide.call(ritual)

  def recreate(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::recreate()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#recreate
    """
    #  void QWidgetPrivate::recreate()
    ritual = 'ritual_ZN14QWidgetPrivate8recreateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QWidgetPrivate8recreateEv'
    self.uglySide.call(ritual)

  def effectiveFocusWidget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QWidgetPrivate::effectiveFocusWidget()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#effectiveFocusWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QWidgetPrivate::effectiveFocusWidget()
    address = self.uglySide.call(
        'ritual_ZN14QWidgetPrivate20effectiveFocusWidgetEv',
    )
    return QWidget._cuteAt(address)

  def restoreRedirected(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::restoreRedirected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#restoreRedirected
    """
    #  void QWidgetPrivate::restoreRedirected()
    self.uglySide.call('ritual_ZN14QWidgetPrivate17restoreRedirectedEv')

  def enforceNativeChildren(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::enforceNativeChildren()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#enforceNativeChildren
    """
    #  void QWidgetPrivate::enforceNativeChildren()
    self.uglySide.call('ritual_ZN14QWidgetPrivate21enforceNativeChildrenEv')

  @overload(Qt.MouseButton, bool)
  def handleSoftwareInputPanel(
      self,
      button: Qt.MouseButton,
      clickCausedFocus: bool,
  ) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::handleSoftwareInputPanel(Qt::MouseButton
    button, bool clickCausedFocus)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#handleSoftwareInputPanel

    Parameters
    ----------

    button : Qt.MouseButton
      Passed on as its number.

    clickCausedFocus : bool
      Passed on as it is.
    """
    #  void QWidgetPrivate::handleSoftwareInputPanel(Qt::MouseButton button,
    #      bool clickCausedFocus)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate24handleSoftwareInputPanelEN2Qt11MouseBut'
        'tonEb',
        button.value, clickCausedFocus,
    )

  @overload()
  @overload(bool)
  def handleSoftwareInputPanel(self, clickCausedFocus: bool = False) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::handleSoftwareInputPanel(bool
    clickCausedFocus)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#handleSoftwareInputPanel

    Parameters
    ----------

    clickCausedFocus : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QWidgetPrivate::handleSoftwareInputPanel(bool clickCausedFocus)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate24handleSoftwareInputPanelEb',
        clickCausedFocus,
    )

  def focusObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QWidgetPrivate::focusObject()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#focusObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QWidgetPrivate::focusObject()
    ritual = 'ritual_ZN14QWidgetPrivate11focusObjectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QWidgetPrivate11focusObjectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def textureListFlags(self) -> QPlatformTextureList.Flags:
    """
    Calls Qt's 'QPlatformTextureList::Flags
    QWidgetPrivate::textureListFlags()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#textureListFlags

    Returns
    -------

    QPlatformTextureList.Flags
      The value standing for the combination Qt gave back.
    """
    #  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
    ritual = 'ritual_ZN14QWidgetPrivate16textureListFlagsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QWidgetPrivate16textureListFlagsEv'
    return QPlatformTextureList.Flags(self.uglySide.call(ritual))

  def grabFramebuffer(self) -> QImage:
    """
    Calls Qt's 'QImage QWidgetPrivate::grabFramebuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#grabFramebuffer

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QWidgetPrivate::grabFramebuffer()
    ritual = 'ritual_ZN14QWidgetPrivate15grabFramebufferEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QWidgetPrivate15grabFramebufferEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def beginBackingStorePainting(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::beginBackingStorePainting()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#beginBackingStorePainting
    """
    #  void QWidgetPrivate::beginBackingStorePainting()
    ritual = 'ritual_ZN14QWidgetPrivate25beginBackingStorePaintingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QWidgetPrivate25beginBackingStorePaintingEv'
    self.uglySide.call(ritual)

  def endBackingStorePainting(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::endBackingStorePainting()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#endBackingStorePainting
    """
    #  void QWidgetPrivate::endBackingStorePainting()
    ritual = 'ritual_ZN14QWidgetPrivate23endBackingStorePaintingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QWidgetPrivate23endBackingStorePaintingEv'
    self.uglySide.call(ritual)

  def beginCompose(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::beginCompose()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#beginCompose
    """
    #  void QWidgetPrivate::beginCompose()
    ritual = 'ritual_ZN14QWidgetPrivate12beginComposeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QWidgetPrivate12beginComposeEv'
    self.uglySide.call(ritual)

  def endCompose(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::endCompose()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#endCompose
    """
    #  void QWidgetPrivate::endCompose()
    ritual = 'ritual_ZN14QWidgetPrivate10endComposeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QWidgetPrivate10endComposeEv'
    self.uglySide.call(ritual)

  def initializeViewportFramebuffer(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::initializeViewportFramebuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#initializeViewportFramebuffer
    """
    #  void QWidgetPrivate::initializeViewportFramebuffer()
    ritual = 'ritual_ZN14QWidgetPrivate29initializeViewportFramebufferEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QWidgetPrivate29initializeViewportFramebufferEv')
    self.uglySide.call(ritual)

  def resizeViewportFramebuffer(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::resizeViewportFramebuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#resizeViewportFramebuffer
    """
    #  void QWidgetPrivate::resizeViewportFramebuffer()
    ritual = 'ritual_ZN14QWidgetPrivate25resizeViewportFramebufferEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QWidgetPrivate25resizeViewportFramebufferEv'
    self.uglySide.call(ritual)

  def resolveSamples(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::resolveSamples()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#resolveSamples
    """
    #  void QWidgetPrivate::resolveSamples()
    ritual = 'ritual_ZN14QWidgetPrivate14resolveSamplesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QWidgetPrivate14resolveSamplesEv'
    self.uglySide.call(ritual)

  def isStereoEnabled(self) -> bool:
    """
    Calls Qt's 'bool QWidgetPrivate::isStereoEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#isStereoEnabled
    """
    #  bool QWidgetPrivate::isStereoEnabled()
    ritual = 'ritual_ZN14QWidgetPrivate15isStereoEnabledEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QWidgetPrivate15isStereoEnabledEv'
    return self.uglySide.call(ritual)

  def toggleStereoTargetBuffer(self) -> bool:
    """
    Calls Qt's 'bool QWidgetPrivate::toggleStereoTargetBuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#toggleStereoTargetBuffer
    """
    #  bool QWidgetPrivate::toggleStereoTargetBuffer()
    ritual = 'ritual_ZN14QWidgetPrivate24toggleStereoTargetBufferEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QWidgetPrivate24toggleStereoTargetBufferEv'
    return self.uglySide.call(ritual)

  @overload()
  @overload(FocusChainRemovalRules)
  @overload(FocusChainRemovalRules, FocusDirection)
  def removeFromFocusChain(
      self,
      rules: FocusChainRemovalRules = FocusChainRemovalRules(),
      direction: FocusDirection = FocusDirection.Next,
  ) -> bool:
    """
    Calls Qt's 'bool
    QWidgetPrivate::removeFromFocusChain(FocusChainRemovalRules rules,
    FocusDirection direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#removeFromFocusChain

    Parameters
    ----------

    rules : FocusChainRemovalRules
      Passed on as its number. May be left out, as in Qt: it is then
      FocusChainRemovalRules().

    direction : FocusDirection
      Passed on as its number. May be left out, as in Qt: it is then
      FocusDirection.Next.
    """
    #  bool QWidgetPrivate::removeFromFocusChain(FocusChainRemovalRules
    #      rules, FocusDirection direction)
    return self.uglySide.call(
        'ritual_ZN14QWidgetPrivate20removeFromFocusChainE6QFlagsINS_21Focus'
        'ChainRemovalRuleEENS_14FocusDirectionE',
        rules.value, direction.value,
    )

  @overload(FocusDirection, QWidget)
  @overload(FocusDirection, NoneType)
  def insertIntoFocusChain(
      self,
      direction: FocusDirection,
      position: Optional[QWidget],
  ) -> bool:
    """
    Calls Qt's 'bool QWidgetPrivate::insertIntoFocusChain(FocusDirection
    direction, QWidget *position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#insertIntoFocusChain

    Parameters
    ----------

    direction : FocusDirection
      Passed on as its number.

    position : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWidgetPrivate::insertIntoFocusChain(FocusDirection direction,
    #      QWidget *position)
    return self.uglySide.call(
        'ritual_ZN14QWidgetPrivate20insertIntoFocusChainENS_14FocusDirectio'
        'nEP7QWidget',
        direction.value, self._addressOf(position),
    )

  @staticmethod
  @overload(QList[QWidget], FocusDirection, QWidget)
  @overload(QList[QWidget], FocusDirection, NoneType)
  def insertIntoFocusChain(
      toBeInserted: QList[QWidget],
      direction: FocusDirection,
      position: Optional[QWidget],
  ) -> bool:
    """
    Calls Qt's 'bool QWidgetPrivate::insertIntoFocusChain(const QWidgetList
    &toBeInserted, FocusDirection direction, QWidget *position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#insertIntoFocusChain

    Parameters
    ----------

    toBeInserted : QList[QWidget]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    direction : FocusDirection
      Passed on as its number.

    position : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWidgetPrivate::insertIntoFocusChain(const QWidgetList
    #      &toBeInserted, FocusDirection direction, QWidget *position)
    return Rituals.call(
        'ritual_ZN14QWidgetPrivate20insertIntoFocusChainERK5QListIP7QWidget'
        'ENS_14FocusDirectionES2_',
        CuteMixin._valueOf(toBeInserted), direction.value,
        CuteMixin._addressOf(position),
    )

  @overload(QWidget)
  @overload(NoneType)
  def insertIntoFocusChainBefore(self, position: Optional[QWidget]) -> bool:
    """
    Calls Qt's 'bool QWidgetPrivate::insertIntoFocusChainBefore(QWidget
    *position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#insertIntoFocusChainBefore

    Parameters
    ----------

    position : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWidgetPrivate::insertIntoFocusChainBefore(QWidget *position)
    return self.uglySide.call(
        'ritual_ZN14QWidgetPrivate26insertIntoFocusChainBeforeEP7QWidget',
        self._addressOf(position),
    )

  @overload(QWidget)
  @overload(NoneType)
  def insertIntoFocusChainAfter(self, position: Optional[QWidget]) -> bool:
    """
    Calls Qt's 'bool QWidgetPrivate::insertIntoFocusChainAfter(QWidget
    *position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#insertIntoFocusChainAfter

    Parameters
    ----------

    position : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWidgetPrivate::insertIntoFocusChainAfter(QWidget *position)
    return self.uglySide.call(
        'ritual_ZN14QWidgetPrivate25insertIntoFocusChainAfterEP7QWidget',
        self._addressOf(position),
    )

  @overload(FocusDirection)
  def reparentFocusChildren(self, direction: FocusDirection) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::reparentFocusChildren(FocusDirection
    direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#reparentFocusChildren

    Parameters
    ----------

    direction : FocusDirection
      Passed on as its number.
    """
    #  void QWidgetPrivate::reparentFocusChildren(FocusDirection direction)
    self.uglySide.call(
        'ritual_ZN14QWidgetPrivate21reparentFocusChildrenENS_14FocusDirecti'
        'onE',
        direction.value,
    )

  @overload(QWidget)
  @overload(NoneType)
  def determineLastFocusChild(
      self,
      noFurtherThan: Optional[QWidget],
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QWidgetPrivate::determineLastFocusChild(QWidget
    *noFurtherThan)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#determineLastFocusChild

    Parameters
    ----------

    noFurtherThan : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QWidgetPrivate::determineLastFocusChild(QWidget
    #      *noFurtherThan)
    address = self.uglySide.call(
        'ritual_ZN14QWidgetPrivate23determineLastFocusChildEP7QWidget',
        self._addressOf(noFurtherThan),
    )
    return QWidget._cuteAt(address)

  def initFocusChain(self) -> None:
    """
    Calls Qt's 'void QWidgetPrivate::initFocusChain()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#initFocusChain
    """
    #  void QWidgetPrivate::initFocusChain()
    self.uglySide.call('ritual_ZN14QWidgetPrivate14initFocusChainEv')

  @overload(bool)
  def stealKeyboardGrab(self, grab: bool) -> bool:
    """
    Calls Qt's 'bool QWidgetPrivate::stealKeyboardGrab(bool grab)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetprivate.html#stealKeyboardGrab

    Parameters
    ----------

    grab : bool
      Passed on as it is.
    """
    #  bool QWidgetPrivate::stealKeyboardGrab(bool grab)
    return self.uglySide.call(
        'ritual_ZN14QWidgetPrivate17stealKeyboardGrabEb', grab,
    )

  @overload(bool)
  def stealMouseGrab(self, grab: bool) -> bool:
    """
    Calls Qt's 'bool QWidgetPrivate::stealMouseGrab(bool grab)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetprivate.html#stealMouseGrab

    Parameters
    ----------

    grab : bool
      Passed on as it is.
    """
    #  bool QWidgetPrivate::stealMouseGrab(bool grab)
    return self.uglySide.call(
        'ritual_ZN14QWidgetPrivate14stealMouseGrabEb', grab,
    )

  @staticmethod
  def adjustFlags(*__, **_) -> Never:
    """
    Qt's 'void QWidgetPrivate::adjustFlags(Qt::WindowFlags &flags, QWidget
    *w)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWidgetPrivate.adjustFlags' has no cute function yet. Qt's 'void "
        "QWidgetPrivate::adjustFlags(Qt::WindowFlags &flags, QWidget *w)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def clipToEffectiveMask(*__, **_) -> Never:
    """
    Qt's 'void QWidgetPrivate::clipToEffectiveMask(QRegion &region) const':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWidgetPrivate.clipToEffectiveMask' has no cute function yet. "
        "Qt's 'void QWidgetPrivate::clipToEffectiveMask(QRegion &region) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def getLayoutItemMargins(*__, **_) -> Never:
    """
    Qt's 'void QWidgetPrivate::getLayoutItemMargins(int *left, int *top, int
    *right, int *bottom) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QWidgetPrivate.getLayoutItemMargins' has no cute function yet. "
        "Qt's 'void QWidgetPrivate::getLayoutItemMargins(int *left, int "
        "*top, int *right, int *bottom) const': takes a number to change "
        "where it is.")

  @staticmethod
  def invalidateBackingStore(*__, **_) -> Never:
    """
    Qt's 'QWidgetPrivate::invalidateBackingStore': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QWidgetPrivate.invalidateBackingStore' has no cute function yet. "
        "Qt's 'QWidgetPrivate::invalidateBackingStore': a template: a "
        "pattern and no single function.")

  @staticmethod
  def repaint(*__, **_) -> Never:
    """
    Qt's 'QWidgetPrivate::repaint': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QWidgetPrivate.repaint' has no cute function yet. Qt's "
        "'QWidgetPrivate::repaint': a template: a pattern and no single "
        "function.")

  @staticmethod
  def setMaximumSize_helper(*__, **_) -> Never:
    """
    Qt's 'bool QWidgetPrivate::setMaximumSize_helper(int &maxw, int &maxh)':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QWidgetPrivate.setMaximumSize_helper' has no cute function yet. "
        "Qt's 'bool QWidgetPrivate::setMaximumSize_helper(int &maxw, int "
        "&maxh)': takes a number to change where it is.")

  @staticmethod
  def setMinimumSize_helper(*__, **_) -> Never:
    """
    Qt's 'bool QWidgetPrivate::setMinimumSize_helper(int &minw, int &minh)':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QWidgetPrivate.setMinimumSize_helper' has no cute function yet. "
        "Qt's 'bool QWidgetPrivate::setMinimumSize_helper(int &minw, int "
        "&minh)': takes a number to change where it is.")

  @staticmethod
  def subtractOpaqueChildren(*__, **_) -> Never:
    """
    Qt's 'void QWidgetPrivate::subtractOpaqueChildren(QRegion &rgn, const
    QRect &clipRect) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWidgetPrivate.subtractOpaqueChildren' has no cute function yet. "
        "Qt's 'void QWidgetPrivate::subtractOpaqueChildren(QRegion &rgn, "
        "const QRect &clipRect) const': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def subtractOpaqueSiblings(*__, **_) -> Never:
    """
    Qt's 'void QWidgetPrivate::subtractOpaqueSiblings(QRegion &source, bool
    *hasDirtySiblingsAbove, bool alsoNonOpaque) const': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWidgetPrivate.subtractOpaqueSiblings' has no cute function yet. "
        "Qt's 'void QWidgetPrivate::subtractOpaqueSiblings(QRegion &source, "
        "bool *hasDirtySiblingsAbove, bool alsoNonOpaque) const': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def update(*__, **_) -> Never:
    """
    Qt's 'QWidgetPrivate::update': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QWidgetPrivate.update' has no cute function yet. Qt's "
        "'QWidgetPrivate::update': a template: a pattern and no single "
        "function.")
