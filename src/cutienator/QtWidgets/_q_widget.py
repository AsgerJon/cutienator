"""
QWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qwidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QObject
from ..QtGui import QPaintDevice, QPalette
from . import QSizePolicy

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QEvent, QLocale, QMargins, QMetaObject
  from ..QtCore import QPoint, QPointF, QRect, QSize, QVariant
  from ..QtGui import QAction, QActionEvent, QBackingStore, QBitmap
  from ..QtGui import QCloseEvent, QContextMenuEvent, QCursor
  from ..QtGui import QDragEnterEvent, QDragLeaveEvent, QDragMoveEvent
  from ..QtGui import QDropEvent, QEnterEvent, QFocusEvent, QFont, QFontInfo
  from ..QtGui import QFontMetrics, QHideEvent, QIcon, QInputMethodEvent
  from ..QtGui import QKeyEvent, QKeySequence, QMouseEvent, QMoveEvent
  from ..QtGui import QPaintEngine, QPaintEvent, QPainter, QPixmap, QRegion
  from ..QtGui import QResizeEvent, QScreen, QShowEvent, QTabletEvent
  from ..QtGui import QWheelEvent, QWindow
  from . import QGraphicsEffect, QGraphicsProxyWidget, QLayout, QStyle
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAction = WAIT['QAction']
  QActionEvent = WAIT['QActionEvent']
  QBackingStore = WAIT['QBackingStore']
  QBitmap = WAIT['QBitmap']
  QByteArray = WAIT['QByteArray']
  QCloseEvent = WAIT['QCloseEvent']
  QContextMenuEvent = WAIT['QContextMenuEvent']
  QCursor = WAIT['QCursor']
  QDragEnterEvent = WAIT['QDragEnterEvent']
  QDragLeaveEvent = WAIT['QDragLeaveEvent']
  QDragMoveEvent = WAIT['QDragMoveEvent']
  QDropEvent = WAIT['QDropEvent']
  QEnterEvent = WAIT['QEnterEvent']
  QEvent = WAIT['QEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QFont = WAIT['QFont']
  QGraphicsEffect = WAIT['QGraphicsEffect']
  QHideEvent = WAIT['QHideEvent']
  QIcon = WAIT['QIcon']
  QInputMethodEvent = WAIT['QInputMethodEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QKeySequence = WAIT['QKeySequence']
  QLayout = WAIT['QLayout']
  QLocale = WAIT['QLocale']
  QMargins = WAIT['QMargins']
  QMouseEvent = WAIT['QMouseEvent']
  QMoveEvent = WAIT['QMoveEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QPainter = WAIT['QPainter']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QRect = WAIT['QRect']
  QRegion = WAIT['QRegion']
  QResizeEvent = WAIT['QResizeEvent']
  QScreen = WAIT['QScreen']
  QShowEvent = WAIT['QShowEvent']
  QSize = WAIT['QSize']
  QStyle = WAIT['QStyle']
  QTabletEvent = WAIT['QTabletEvent']
  QWheelEvent = WAIT['QWheelEvent']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWidget(QObject, QPaintDevice):
  """
  The cute side of Qt's QWidget: a plain Python object standing in front of
  one C++ QWidget.

  It is built on the cute 'QObject', as Qt's QWidget is built on Qt's
  QObject, and has everything that class has. It is built on the cute
  'QPaintDevice' as well, as Qt's QWidget is built on Qt's QPaintDevice too,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWidget that has a ritual and that Python can call
  so far, 267 names in all: 'metaObject', 'tr', 'devType', 'winId',
  'createWinId', 'internalWinId', 'effectiveWinId', 'style', 'setStyle',
  'isTopLevel', 'isWindow', 'isModal', 'windowModality', 'setWindowModality',
  'isEnabled', 'isEnabledTo', 'setEnabled', 'setDisabled',
  'setWindowModified', 'frameGeometry', 'geometry', 'normalGeometry', 'x',
  'y', 'pos', 'frameSize', 'size', 'width', 'height', 'rect', 'childrenRect',
  'childrenRegion', 'minimumSize', 'maximumSize', 'minimumWidth',
  'minimumHeight', 'maximumWidth', 'maximumHeight', 'setMinimumSize',
  'setMaximumSize', 'setMinimumWidth', 'setMinimumHeight', 'setMaximumWidth',
  'setMaximumHeight', 'sizeIncrement', 'setSizeIncrement', 'baseSize',
  'setBaseSize', 'setFixedSize', 'setFixedWidth', 'setFixedHeight',
  'mapToGlobal', 'mapFromGlobal', 'mapToParent', 'mapFromParent', 'mapTo',
  'mapFrom', 'window', 'nativeParentWidget', 'topLevelWidget', 'palette',
  'setPalette', 'setBackgroundRole', 'backgroundRole', 'setForegroundRole',
  'foregroundRole', 'font', 'setFont', 'fontMetrics', 'fontInfo', 'cursor',
  'setCursor', 'unsetCursor', 'setMouseTracking', 'hasMouseTracking',
  'underMouse', 'setTabletTracking', 'hasTabletTracking', 'setMask', 'mask',
  'clearMask', 'render', 'grab', 'graphicsEffect', 'setGraphicsEffect',
  'grabGesture', 'ungrabGesture', 'setWindowTitle', 'setStyleSheet',
  'styleSheet', 'windowTitle', 'setWindowIcon', 'windowIcon',
  'setWindowIconText', 'windowIconText', 'setWindowRole', 'windowRole',
  'setWindowFilePath', 'windowFilePath', 'setWindowOpacity', 'windowOpacity',
  'isWindowModified', 'setToolTip', 'toolTip', 'setToolTipDuration',
  'toolTipDuration', 'setStatusTip', 'statusTip', 'setWhatsThis',
  'whatsThis', 'accessibleName', 'setAccessibleName',
  'accessibleDescription', 'setAccessibleDescription',
  'accessibleIdentifier', 'setAccessibleIdentifier', 'setLayoutDirection',
  'layoutDirection', 'unsetLayoutDirection', 'setLocale', 'locale',
  'unsetLocale', 'isRightToLeft', 'isLeftToRight', 'setFocus',
  'isActiveWindow', 'activateWindow', 'clearFocus', 'focusPolicy',
  'setFocusPolicy', 'hasFocus', 'setTabOrder', 'setFocusProxy', 'focusProxy',
  'contextMenuPolicy', 'setContextMenuPolicy', 'grabMouse', 'releaseMouse',
  'grabKeyboard', 'releaseKeyboard', 'grabShortcut', 'releaseShortcut',
  'setShortcutEnabled', 'setShortcutAutoRepeat', 'mouseGrabber',
  'keyboardGrabber', 'updatesEnabled', 'setUpdatesEnabled',
  'graphicsProxyWidget', 'update', 'repaint', 'setVisible', 'setHidden',
  'show', 'hide', 'showMinimized', 'showMaximized', 'showFullScreen',
  'showNormal', 'close', 'raise_', 'lower', 'stackUnder', 'move', 'resize',
  'setGeometry', 'saveGeometry', 'restoreGeometry', 'adjustSize',
  'isVisible', 'isVisibleTo', 'isHidden', 'isMinimized', 'isMaximized',
  'isFullScreen', 'windowState', 'setWindowState', 'overrideWindowState',
  'sizeHint', 'minimumSizeHint', 'sizePolicy', 'setSizePolicy',
  'heightForWidth', 'hasHeightForWidth', 'visibleRegion',
  'setContentsMargins', 'contentsMargins', 'contentsRect', 'layout',
  'setLayout', 'updateGeometry', 'setParent', 'scroll', 'focusWidget',
  'nextInFocusChain', 'previousInFocusChain', 'acceptDrops',
  'setAcceptDrops', 'addAction', 'addActions', 'insertActions',
  'insertAction', 'removeAction', 'actions', 'parentWidget',
  'setWindowFlags', 'windowFlags', 'setWindowFlag', 'overrideWindowFlags',
  'windowType', 'find', 'childAt', 'setAttribute', 'testAttribute',
  'paintEngine', 'ensurePolished', 'isAncestorOf', 'autoFillBackground',
  'setAutoFillBackground', 'backingStore', 'windowHandle', 'screen',
  'setScreen', 'createWindowContainer', 'event', 'mousePressEvent',
  'mouseReleaseEvent', 'mouseDoubleClickEvent', 'mouseMoveEvent',
  'wheelEvent', 'keyPressEvent', 'keyReleaseEvent', 'focusInEvent',
  'focusOutEvent', 'enterEvent', 'leaveEvent', 'paintEvent', 'moveEvent',
  'resizeEvent', 'closeEvent', 'contextMenuEvent', 'tabletEvent',
  'actionEvent', 'dragEnterEvent', 'dragMoveEvent', 'dragLeaveEvent',
  'dropEvent', 'showEvent', 'hideEvent', 'changeEvent', 'metric',
  'initPainter', 'redirected', 'sharedPainter', 'inputMethodEvent',
  'inputMethodQuery', 'inputMethodHints', 'setInputMethodHints',
  'updateMicroFocus', 'create', 'destroy', 'focusNextPrevChild',
  'focusNextChild', 'focusPreviousChild', 'setBackingStore',
  'testAttribute_helper', 'takeLayout'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWidget::~QWidget()': the destructor: Python never removes a C++
    QWidget.

  What has no ritual
  ------------------

  19 of the 326 functions Qt declares: 7 takes or gives a type that cannot be
  passed yet; 5 a template; 4 a signal; 2 forbidden; 1 declared and nowhere
  to be found.

  What to expect
  --------------

  - The C++ QWidget is created at the first use, not by 'QWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWidget.
  - Qt tells when it has removed the C++ QWidget. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QWidget, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class RenderFlag(CuteFlags):
    """
    The flags enum 'QWidget::RenderFlag' of Qt, with the 3 names Qt gives in
    it. Qt names the type of its combinations 'QWidget::RenderFlags'.
    """

    DrawWindowBackground = 0x1
    DrawChildren = 0x2
    IgnoreMask = 0x4

  RenderFlags = RenderFlag

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
    Calls Qt's 'QString QWidget::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#tr

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
    #  QString QWidget::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN7QWidget2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(THIS, THIS)
  @overload(THIS, NoneType)
  @overload(NoneType, THIS)
  @overload(NoneType, NoneType)
  def setTabOrder(a0: Optional[QWidget], a1: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QWidget::setTabOrder(QWidget *a0, QWidget *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setTabOrder

    Parameters
    ----------

    a0 : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::setTabOrder(QWidget *a0, QWidget *a1)
    Rituals.call(
        'ritual_ZN7QWidget11setTabOrderEPS_S0_',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(a1),
    )

  @staticmethod
  def mouseGrabber() -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QWidget::mouseGrabber()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#mouseGrabber

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QWidget::mouseGrabber()
    address = Rituals.call('ritual_ZN7QWidget12mouseGrabberEv')
    return QWidget._cuteAt(address)

  @staticmethod
  def keyboardGrabber() -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QWidget::keyboardGrabber()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#keyboardGrabber

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QWidget::keyboardGrabber()
    address = Rituals.call('ritual_ZN7QWidget15keyboardGrabberEv')
    return QWidget._cuteAt(address)

  @staticmethod
  @overload(int)
  def find(a0: int) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QWidget::find(WId a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#find

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QWidget::find(WId a0)
    address = Rituals.call('ritual_ZN7QWidget4findEy', a0)
    return QWidget._cuteAt(address)

  @staticmethod
  @overload(QWindow)
  @overload(NoneType)
  @overload(QWindow, THIS)
  @overload(QWindow, NoneType)
  @overload(NoneType, THIS)
  @overload(NoneType, NoneType)
  @overload(QWindow, THIS, Qt.WindowFlags)
  @overload(QWindow, NoneType, Qt.WindowFlags)
  @overload(NoneType, THIS, Qt.WindowFlags)
  @overload(NoneType, NoneType, Qt.WindowFlags)
  def createWindowContainer(
      window: Optional[QWindow],
      parent: Optional[QWidget] = None,
      flags: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QWidget::createWindowContainer(QWindow *window,
    QWidget *parent, Qt::WindowFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#createWindowContainer

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    flags : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QWidget::createWindowContainer(QWindow *window, QWidget
    #      *parent, Qt::WindowFlags flags)
    address = Rituals.call(
        'ritual_ZN7QWidget21createWindowContainerEP7QWindowPS_6QFlagsIN2Qt1'
        '0WindowTypeEE',
        CuteMixin._addressOf(window), CuteMixin._addressOf(parent),
        flags.value,
    )
    return QWidget._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWidget'

  #  Qt's QWidget is built on more than one class. The part of a C++ QWidget
  #  that belongs to a class after the first begins somewhere inside the
  #  object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QPaintDevice': 'ritual_cast_QWidget_QPaintDevice',
  }

  #  A C++ QWidget Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWidget'

  #  The functions Qt calls itself that QWidget is the first to declare and
  #  that cannot be handed to Python yet, each as Qt declares it. A class of
  #  a program that writes one of them anew is refused, since Qt would never
  #  call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'nativeEvent': (
          'bool QWidget::nativeEvent(const QByteArray &, void *, qintptr *)',
      ),
  }

  #  The functions Qt calls itself that QWidget is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'setVisible': (
          ('_ZN7QWidget10setVisibleEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'sizeHint': (
          ('_ZNK7QWidget8sizeHintEv',
           ('address', 'value', 'QtCore:QSize'),
           ()),
      ),
      'minimumSizeHint': (
          ('_ZNK7QWidget15minimumSizeHintEv',
           ('address', 'value', 'QtCore:QSize'),
           ()),
      ),
      'heightForWidth': (
          ('_ZNK7QWidget14heightForWidthEi',
           ('int', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'hasHeightForWidth': (
          ('_ZNK7QWidget17hasHeightForWidthEv',
           ('bool', 'number', ''),
           ()),
      ),
      'mousePressEvent': (
          ('_ZN7QWidget15mousePressEventEP11QMouseEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QMouseEvent'),
           )),
      ),
      'mouseReleaseEvent': (
          ('_ZN7QWidget17mouseReleaseEventEP11QMouseEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QMouseEvent'),
           )),
      ),
      'mouseDoubleClickEvent': (
          ('_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QMouseEvent'),
           )),
      ),
      'mouseMoveEvent': (
          ('_ZN7QWidget14mouseMoveEventEP11QMouseEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QMouseEvent'),
           )),
      ),
      'wheelEvent': (
          ('_ZN7QWidget10wheelEventEP11QWheelEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QWheelEvent'),
           )),
      ),
      'keyPressEvent': (
          ('_ZN7QWidget13keyPressEventEP9QKeyEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QKeyEvent'),
           )),
      ),
      'keyReleaseEvent': (
          ('_ZN7QWidget15keyReleaseEventEP9QKeyEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QKeyEvent'),
           )),
      ),
      'focusInEvent': (
          ('_ZN7QWidget12focusInEventEP11QFocusEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QFocusEvent'),
           )),
      ),
      'focusOutEvent': (
          ('_ZN7QWidget13focusOutEventEP11QFocusEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QFocusEvent'),
           )),
      ),
      'enterEvent': (
          ('_ZN7QWidget10enterEventEP11QEnterEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QEnterEvent'),
           )),
      ),
      'leaveEvent': (
          ('_ZN7QWidget10leaveEventEP6QEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QEvent'),
           )),
      ),
      'paintEvent': (
          ('_ZN7QWidget10paintEventEP11QPaintEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPaintEvent'),
           )),
      ),
      'moveEvent': (
          ('_ZN7QWidget9moveEventEP10QMoveEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QMoveEvent'),
           )),
      ),
      'resizeEvent': (
          ('_ZN7QWidget11resizeEventEP12QResizeEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QResizeEvent'),
           )),
      ),
      'closeEvent': (
          ('_ZN7QWidget10closeEventEP11QCloseEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QCloseEvent'),
           )),
      ),
      'contextMenuEvent': (
          ('_ZN7QWidget16contextMenuEventEP17QContextMenuEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QContextMenuEvent'),
           )),
      ),
      'tabletEvent': (
          ('_ZN7QWidget11tabletEventEP12QTabletEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QTabletEvent'),
           )),
      ),
      'actionEvent': (
          ('_ZN7QWidget11actionEventEP12QActionEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QActionEvent'),
           )),
      ),
      'dragEnterEvent': (
          ('_ZN7QWidget14dragEnterEventEP15QDragEnterEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QDragEnterEvent'),
           )),
      ),
      'dragMoveEvent': (
          ('_ZN7QWidget13dragMoveEventEP14QDragMoveEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QDragMoveEvent'),
           )),
      ),
      'dragLeaveEvent': (
          ('_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QDragLeaveEvent'),
           )),
      ),
      'dropEvent': (
          ('_ZN7QWidget9dropEventEP10QDropEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QDropEvent'),
           )),
      ),
      'showEvent': (
          ('_ZN7QWidget9showEventEP10QShowEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QShowEvent'),
           )),
      ),
      'hideEvent': (
          ('_ZN7QWidget9hideEventEP10QHideEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QHideEvent'),
           )),
      ),
      'changeEvent': (
          ('_ZN7QWidget11changeEventEP6QEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QEvent'),
           )),
      ),
      'inputMethodEvent': (
          ('_ZN7QWidget16inputMethodEventEP17QInputMethodEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QInputMethodEvent'),
           )),
      ),
      'inputMethodQuery': (
          ('_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('int', 'enum', 'QtCore:Qt.InputMethodQuery'),
           )),
      ),
      'focusNextPrevChild': (
          ('_ZN7QWidget18focusNextPrevChildEb',
           ('bool', 'number', ''),
           (
               ('bool', 'number', ''),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWidget::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWidget::metaObject() const
    address = self.uglySide.call('ritual_ZNK7QWidget10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def devType(self) -> int:
    """
    Calls Qt's 'int QWidget::devType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#devType
    """
    #  int QWidget::devType() const
    ritual = 'ritual_ZNK7QWidget7devTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QWidget7devTypeEv'
    return self.uglySide.call(ritual)

  def winId(self) -> int:
    """
    Calls Qt's 'WId QWidget::winId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#winId
    """
    #  WId QWidget::winId() const
    return self.uglySide.call('ritual_ZNK7QWidget5winIdEv')

  def internalWinId(self) -> int:
    """
    Calls Qt's 'WId QWidget::internalWinId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#internalWinId
    """
    #  WId QWidget::internalWinId() const
    return self.uglySide.call('ritual_ZNK7QWidget13internalWinIdEv')

  def effectiveWinId(self) -> int:
    """
    Calls Qt's 'WId QWidget::effectiveWinId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#effectiveWinId
    """
    #  WId QWidget::effectiveWinId() const
    return self.uglySide.call('ritual_ZNK7QWidget14effectiveWinIdEv')

  def style(self) -> Optional[QStyle]:
    """
    Calls Qt's 'QStyle *QWidget::style() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#style

    Returns
    -------

    Optional[QStyle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStyle *QWidget::style() const
    address = self.uglySide.call('ritual_ZNK7QWidget5styleEv')
    from . import QStyle
    return QStyle._cuteAt(address)

  def isTopLevel(self) -> bool:
    """
    Calls Qt's 'bool QWidget::isTopLevel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#isTopLevel
    """
    #  bool QWidget::isTopLevel() const
    return self.uglySide.call('ritual_ZNK7QWidget10isTopLevelEv')

  def isWindow(self) -> bool:
    """
    Calls Qt's 'bool QWidget::isWindow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#isWindow
    """
    #  bool QWidget::isWindow() const
    return self.uglySide.call('ritual_ZNK7QWidget8isWindowEv')

  def isModal(self) -> bool:
    """
    Calls Qt's 'bool QWidget::isModal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#isModal
    """
    #  bool QWidget::isModal() const
    return self.uglySide.call('ritual_ZNK7QWidget7isModalEv')

  def windowModality(self) -> Qt.WindowModality:
    """
    Calls Qt's 'Qt::WindowModality QWidget::windowModality() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#windowModality

    Returns
    -------

    Qt.WindowModality
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.WindowModality(number)' gives.
    """
    #  Qt::WindowModality QWidget::windowModality() const
    return Qt.WindowModality(self.uglySide.call(
        'ritual_ZNK7QWidget14windowModalityEv',
    ))

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QWidget::isEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#isEnabled
    """
    #  bool QWidget::isEnabled() const
    return self.uglySide.call('ritual_ZNK7QWidget9isEnabledEv')

  @overload(THIS)
  @overload(NoneType)
  def isEnabledTo(self, a0: Optional[QWidget]) -> bool:
    """
    Calls Qt's 'bool QWidget::isEnabledTo(const QWidget *a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#isEnabledTo

    Parameters
    ----------

    a0 : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWidget::isEnabledTo(const QWidget *a0) const
    return self.uglySide.call(
        'ritual_ZNK7QWidget11isEnabledToEPKS_', self._addressOf(a0),
    )

  def frameGeometry(self) -> QRect:
    """
    Calls Qt's 'QRect QWidget::frameGeometry() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#frameGeometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QWidget::frameGeometry() const
    address = self.uglySide.call('ritual_ZNK7QWidget13frameGeometryEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def geometry(self) -> QRect:
    """
    Calls Qt's 'const QRect &QWidget::geometry() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#geometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  const QRect &QWidget::geometry() const
    address = self.uglySide.call('ritual_ZNK7QWidget8geometryEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def normalGeometry(self) -> QRect:
    """
    Calls Qt's 'QRect QWidget::normalGeometry() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#normalGeometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QWidget::normalGeometry() const
    address = self.uglySide.call('ritual_ZNK7QWidget14normalGeometryEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def x(self) -> int:
    """
    Calls Qt's 'int QWidget::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#x
    """
    #  int QWidget::x() const
    return self.uglySide.call('ritual_ZNK7QWidget1xEv')

  def y(self) -> int:
    """
    Calls Qt's 'int QWidget::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#y
    """
    #  int QWidget::y() const
    return self.uglySide.call('ritual_ZNK7QWidget1yEv')

  def pos(self) -> QPoint:
    """
    Calls Qt's 'QPoint QWidget::pos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#pos

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QWidget::pos() const
    address = self.uglySide.call('ritual_ZNK7QWidget3posEv')
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def frameSize(self) -> QSize:
    """
    Calls Qt's 'QSize QWidget::frameSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#frameSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWidget::frameSize() const
    address = self.uglySide.call('ritual_ZNK7QWidget9frameSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QWidget::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWidget::size() const
    address = self.uglySide.call('ritual_ZNK7QWidget4sizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def width(self) -> int:
    """
    Calls Qt's 'int QWidget::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#width
    """
    #  int QWidget::width() const
    return self.uglySide.call('ritual_ZNK7QWidget5widthEv')

  def height(self) -> int:
    """
    Calls Qt's 'int QWidget::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#height
    """
    #  int QWidget::height() const
    return self.uglySide.call('ritual_ZNK7QWidget6heightEv')

  def rect(self) -> QRect:
    """
    Calls Qt's 'QRect QWidget::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#rect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QWidget::rect() const
    address = self.uglySide.call('ritual_ZNK7QWidget4rectEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def childrenRect(self) -> QRect:
    """
    Calls Qt's 'QRect QWidget::childrenRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#childrenRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QWidget::childrenRect() const
    address = self.uglySide.call('ritual_ZNK7QWidget12childrenRectEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def childrenRegion(self) -> QRegion:
    """
    Calls Qt's 'QRegion QWidget::childrenRegion() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#childrenRegion

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QWidget::childrenRegion() const
    address = self.uglySide.call('ritual_ZNK7QWidget14childrenRegionEv')
    from ..QtGui import QRegion
    return QRegion._cuteOwning(address)

  def minimumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QWidget::minimumSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#minimumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWidget::minimumSize() const
    address = self.uglySide.call('ritual_ZNK7QWidget11minimumSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def maximumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QWidget::maximumSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#maximumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWidget::maximumSize() const
    address = self.uglySide.call('ritual_ZNK7QWidget11maximumSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumWidth(self) -> int:
    """
    Calls Qt's 'int QWidget::minimumWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#minimumWidth
    """
    #  int QWidget::minimumWidth() const
    return self.uglySide.call('ritual_ZNK7QWidget12minimumWidthEv')

  def minimumHeight(self) -> int:
    """
    Calls Qt's 'int QWidget::minimumHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#minimumHeight
    """
    #  int QWidget::minimumHeight() const
    return self.uglySide.call('ritual_ZNK7QWidget13minimumHeightEv')

  def maximumWidth(self) -> int:
    """
    Calls Qt's 'int QWidget::maximumWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#maximumWidth
    """
    #  int QWidget::maximumWidth() const
    return self.uglySide.call('ritual_ZNK7QWidget12maximumWidthEv')

  def maximumHeight(self) -> int:
    """
    Calls Qt's 'int QWidget::maximumHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#maximumHeight
    """
    #  int QWidget::maximumHeight() const
    return self.uglySide.call('ritual_ZNK7QWidget13maximumHeightEv')

  def sizeIncrement(self) -> QSize:
    """
    Calls Qt's 'QSize QWidget::sizeIncrement() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#sizeIncrement

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWidget::sizeIncrement() const
    address = self.uglySide.call('ritual_ZNK7QWidget13sizeIncrementEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def baseSize(self) -> QSize:
    """
    Calls Qt's 'QSize QWidget::baseSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#baseSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWidget::baseSize() const
    address = self.uglySide.call('ritual_ZNK7QWidget8baseSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QPointF)
  def mapToGlobal(self, a0: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF QWidget::mapToGlobal(const QPointF &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#mapToGlobal

    Parameters
    ----------

    a0 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QWidget::mapToGlobal(const QPointF &a0) const
    address = self.uglySide.call(
        'ritual_ZNK7QWidget11mapToGlobalERK7QPointF', self._valueOf(a0),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QPoint)
  def mapToGlobal(self, a0: QPoint) -> QPoint:
    """
    Calls Qt's 'QPoint QWidget::mapToGlobal(const QPoint &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#mapToGlobal

    Parameters
    ----------

    a0 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QWidget::mapToGlobal(const QPoint &a0) const
    address = self.uglySide.call(
        'ritual_ZNK7QWidget11mapToGlobalERK6QPoint', self._valueOf(a0),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(QPointF)
  def mapFromGlobal(self, a0: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF QWidget::mapFromGlobal(const QPointF &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#mapFromGlobal

    Parameters
    ----------

    a0 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QWidget::mapFromGlobal(const QPointF &a0) const
    address = self.uglySide.call(
        'ritual_ZNK7QWidget13mapFromGlobalERK7QPointF', self._valueOf(a0),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QPoint)
  def mapFromGlobal(self, a0: QPoint) -> QPoint:
    """
    Calls Qt's 'QPoint QWidget::mapFromGlobal(const QPoint &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#mapFromGlobal

    Parameters
    ----------

    a0 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QWidget::mapFromGlobal(const QPoint &a0) const
    address = self.uglySide.call(
        'ritual_ZNK7QWidget13mapFromGlobalERK6QPoint', self._valueOf(a0),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(QPointF)
  def mapToParent(self, a0: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF QWidget::mapToParent(const QPointF &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#mapToParent

    Parameters
    ----------

    a0 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QWidget::mapToParent(const QPointF &a0) const
    address = self.uglySide.call(
        'ritual_ZNK7QWidget11mapToParentERK7QPointF', self._valueOf(a0),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QPoint)
  def mapToParent(self, a0: QPoint) -> QPoint:
    """
    Calls Qt's 'QPoint QWidget::mapToParent(const QPoint &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#mapToParent

    Parameters
    ----------

    a0 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QWidget::mapToParent(const QPoint &a0) const
    address = self.uglySide.call(
        'ritual_ZNK7QWidget11mapToParentERK6QPoint', self._valueOf(a0),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(QPointF)
  def mapFromParent(self, a0: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF QWidget::mapFromParent(const QPointF &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#mapFromParent

    Parameters
    ----------

    a0 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QWidget::mapFromParent(const QPointF &a0) const
    address = self.uglySide.call(
        'ritual_ZNK7QWidget13mapFromParentERK7QPointF', self._valueOf(a0),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QPoint)
  def mapFromParent(self, a0: QPoint) -> QPoint:
    """
    Calls Qt's 'QPoint QWidget::mapFromParent(const QPoint &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#mapFromParent

    Parameters
    ----------

    a0 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QWidget::mapFromParent(const QPoint &a0) const
    address = self.uglySide.call(
        'ritual_ZNK7QWidget13mapFromParentERK6QPoint', self._valueOf(a0),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(THIS, QPointF)
  @overload(NoneType, QPointF)
  def mapTo(self, a0: Optional[QWidget], a1: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF QWidget::mapTo(const QWidget *a0, const QPointF &a1)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#mapTo

    Parameters
    ----------

    a0 : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QWidget::mapTo(const QWidget *a0, const QPointF &a1) const
    address = self.uglySide.call(
        'ritual_ZNK7QWidget5mapToEPKS_RK7QPointF',
        self._addressOf(a0), self._valueOf(a1),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(THIS, QPoint)
  @overload(NoneType, QPoint)
  def mapTo(self, a0: Optional[QWidget], a1: QPoint) -> QPoint:
    """
    Calls Qt's 'QPoint QWidget::mapTo(const QWidget *a0, const QPoint &a1)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#mapTo

    Parameters
    ----------

    a0 : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QWidget::mapTo(const QWidget *a0, const QPoint &a1) const
    address = self.uglySide.call(
        'ritual_ZNK7QWidget5mapToEPKS_RK6QPoint',
        self._addressOf(a0), self._valueOf(a1),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(THIS, QPointF)
  @overload(NoneType, QPointF)
  def mapFrom(self, a0: Optional[QWidget], a1: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF QWidget::mapFrom(const QWidget *a0, const QPointF
    &a1) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#mapFrom

    Parameters
    ----------

    a0 : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QWidget::mapFrom(const QWidget *a0, const QPointF &a1) const
    address = self.uglySide.call(
        'ritual_ZNK7QWidget7mapFromEPKS_RK7QPointF',
        self._addressOf(a0), self._valueOf(a1),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(THIS, QPoint)
  @overload(NoneType, QPoint)
  def mapFrom(self, a0: Optional[QWidget], a1: QPoint) -> QPoint:
    """
    Calls Qt's 'QPoint QWidget::mapFrom(const QWidget *a0, const QPoint &a1)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#mapFrom

    Parameters
    ----------

    a0 : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QWidget::mapFrom(const QWidget *a0, const QPoint &a1) const
    address = self.uglySide.call(
        'ritual_ZNK7QWidget7mapFromEPKS_RK6QPoint',
        self._addressOf(a0), self._valueOf(a1),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def window(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QWidget::window() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#window

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QWidget::window() const
    address = self.uglySide.call('ritual_ZNK7QWidget6windowEv')
    return QWidget._cuteAt(address)

  def nativeParentWidget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QWidget::nativeParentWidget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#nativeParentWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QWidget::nativeParentWidget() const
    address = self.uglySide.call('ritual_ZNK7QWidget18nativeParentWidgetEv')
    return QWidget._cuteAt(address)

  def topLevelWidget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QWidget::topLevelWidget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#topLevelWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QWidget::topLevelWidget() const
    address = self.uglySide.call('ritual_ZNK7QWidget14topLevelWidgetEv')
    return QWidget._cuteAt(address)

  def palette(self) -> QPalette:
    """
    Calls Qt's 'const QPalette &QWidget::palette() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#palette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  const QPalette &QWidget::palette() const
    address = self.uglySide.call('ritual_ZNK7QWidget7paletteEv')
    return QPalette._cuteOwning(address)

  def backgroundRole(self) -> QPalette.ColorRole:
    """
    Calls Qt's 'QPalette::ColorRole QWidget::backgroundRole() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#backgroundRole

    Returns
    -------

    QPalette.ColorRole
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPalette.ColorRole(number)' gives.
    """
    #  QPalette::ColorRole QWidget::backgroundRole() const
    return QPalette.ColorRole(self.uglySide.call(
        'ritual_ZNK7QWidget14backgroundRoleEv',
    ))

  def foregroundRole(self) -> QPalette.ColorRole:
    """
    Calls Qt's 'QPalette::ColorRole QWidget::foregroundRole() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#foregroundRole

    Returns
    -------

    QPalette.ColorRole
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPalette.ColorRole(number)' gives.
    """
    #  QPalette::ColorRole QWidget::foregroundRole() const
    return QPalette.ColorRole(self.uglySide.call(
        'ritual_ZNK7QWidget14foregroundRoleEv',
    ))

  def font(self) -> QFont:
    """
    Calls Qt's 'const QFont &QWidget::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  const QFont &QWidget::font() const
    address = self.uglySide.call('ritual_ZNK7QWidget4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def fontMetrics(self) -> QFontMetrics:
    """
    Calls Qt's 'QFontMetrics QWidget::fontMetrics() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#fontMetrics

    Returns
    -------

    QFontMetrics
      A new cute QFontMetrics around the copy Qt gave back. Python owns it.
    """
    #  QFontMetrics QWidget::fontMetrics() const
    address = self.uglySide.call('ritual_ZNK7QWidget11fontMetricsEv')
    from ..QtGui import QFontMetrics
    return QFontMetrics._cuteOwning(address)

  def fontInfo(self) -> QFontInfo:
    """
    Calls Qt's 'QFontInfo QWidget::fontInfo() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#fontInfo

    Returns
    -------

    QFontInfo
      A new cute QFontInfo around the copy Qt gave back. Python owns it.
    """
    #  QFontInfo QWidget::fontInfo() const
    address = self.uglySide.call('ritual_ZNK7QWidget8fontInfoEv')
    from ..QtGui import QFontInfo
    return QFontInfo._cuteOwning(address)

  def cursor(self) -> QCursor:
    """
    Calls Qt's 'QCursor QWidget::cursor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#cursor

    Returns
    -------

    QCursor
      A new cute QCursor around the copy Qt gave back. Python owns it.
    """
    #  QCursor QWidget::cursor() const
    address = self.uglySide.call('ritual_ZNK7QWidget6cursorEv')
    from ..QtGui import QCursor
    return QCursor._cuteOwning(address)

  def hasMouseTracking(self) -> bool:
    """
    Calls Qt's 'bool QWidget::hasMouseTracking() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#hasMouseTracking
    """
    #  bool QWidget::hasMouseTracking() const
    return self.uglySide.call('ritual_ZNK7QWidget16hasMouseTrackingEv')

  def underMouse(self) -> bool:
    """
    Calls Qt's 'bool QWidget::underMouse() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#underMouse
    """
    #  bool QWidget::underMouse() const
    return self.uglySide.call('ritual_ZNK7QWidget10underMouseEv')

  def hasTabletTracking(self) -> bool:
    """
    Calls Qt's 'bool QWidget::hasTabletTracking() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#hasTabletTracking
    """
    #  bool QWidget::hasTabletTracking() const
    return self.uglySide.call('ritual_ZNK7QWidget17hasTabletTrackingEv')

  def mask(self) -> QRegion:
    """
    Calls Qt's 'QRegion QWidget::mask() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#mask

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QWidget::mask() const
    address = self.uglySide.call('ritual_ZNK7QWidget4maskEv')
    from ..QtGui import QRegion
    return QRegion._cuteOwning(address)

  def graphicsEffect(self) -> Optional[QGraphicsEffect]:
    """
    Calls Qt's 'QGraphicsEffect *QWidget::graphicsEffect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#graphicsEffect

    Returns
    -------

    Optional[QGraphicsEffect]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsEffect *QWidget::graphicsEffect() const
    address = self.uglySide.call('ritual_ZNK7QWidget14graphicsEffectEv')
    from . import QGraphicsEffect
    return QGraphicsEffect._cuteAt(address)

  def styleSheet(self) -> str:
    """
    Calls Qt's 'QString QWidget::styleSheet() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#styleSheet

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWidget::styleSheet() const
    return self.uglySide.call('ritual_ZNK7QWidget10styleSheetEv')

  def windowTitle(self) -> str:
    """
    Calls Qt's 'QString QWidget::windowTitle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#windowTitle

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWidget::windowTitle() const
    return self.uglySide.call('ritual_ZNK7QWidget11windowTitleEv')

  def windowIcon(self) -> QIcon:
    """
    Calls Qt's 'QIcon QWidget::windowIcon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#windowIcon

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QWidget::windowIcon() const
    address = self.uglySide.call('ritual_ZNK7QWidget10windowIconEv')
    from ..QtGui import QIcon
    return QIcon._cuteOwning(address)

  def windowIconText(self) -> str:
    """
    Calls Qt's 'QString QWidget::windowIconText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#windowIconText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWidget::windowIconText() const
    return self.uglySide.call('ritual_ZNK7QWidget14windowIconTextEv')

  def windowRole(self) -> str:
    """
    Calls Qt's 'QString QWidget::windowRole() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#windowRole

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWidget::windowRole() const
    return self.uglySide.call('ritual_ZNK7QWidget10windowRoleEv')

  def windowFilePath(self) -> str:
    """
    Calls Qt's 'QString QWidget::windowFilePath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#windowFilePath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWidget::windowFilePath() const
    return self.uglySide.call('ritual_ZNK7QWidget14windowFilePathEv')

  def windowOpacity(self) -> float:
    """
    Calls Qt's 'qreal QWidget::windowOpacity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#windowOpacity
    """
    #  qreal QWidget::windowOpacity() const
    return self.uglySide.call('ritual_ZNK7QWidget13windowOpacityEv')

  def isWindowModified(self) -> bool:
    """
    Calls Qt's 'bool QWidget::isWindowModified() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#isWindowModified
    """
    #  bool QWidget::isWindowModified() const
    return self.uglySide.call('ritual_ZNK7QWidget16isWindowModifiedEv')

  def toolTip(self) -> str:
    """
    Calls Qt's 'QString QWidget::toolTip() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#toolTip

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWidget::toolTip() const
    return self.uglySide.call('ritual_ZNK7QWidget7toolTipEv')

  def toolTipDuration(self) -> int:
    """
    Calls Qt's 'int QWidget::toolTipDuration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#toolTipDuration
    """
    #  int QWidget::toolTipDuration() const
    return self.uglySide.call('ritual_ZNK7QWidget15toolTipDurationEv')

  def statusTip(self) -> str:
    """
    Calls Qt's 'QString QWidget::statusTip() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#statusTip

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWidget::statusTip() const
    return self.uglySide.call('ritual_ZNK7QWidget9statusTipEv')

  def whatsThis(self) -> str:
    """
    Calls Qt's 'QString QWidget::whatsThis() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#whatsThis

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWidget::whatsThis() const
    return self.uglySide.call('ritual_ZNK7QWidget9whatsThisEv')

  def accessibleName(self) -> str:
    """
    Calls Qt's 'QString QWidget::accessibleName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#accessibleName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWidget::accessibleName() const
    return self.uglySide.call('ritual_ZNK7QWidget14accessibleNameEv')

  def accessibleDescription(self) -> str:
    """
    Calls Qt's 'QString QWidget::accessibleDescription() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#accessibleDescription

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWidget::accessibleDescription() const
    return self.uglySide.call('ritual_ZNK7QWidget21accessibleDescriptionEv')

  def accessibleIdentifier(self) -> str:
    """
    Calls Qt's 'QString QWidget::accessibleIdentifier() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#accessibleIdentifier

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWidget::accessibleIdentifier() const
    return self.uglySide.call('ritual_ZNK7QWidget20accessibleIdentifierEv')

  def layoutDirection(self) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection QWidget::layoutDirection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#layoutDirection

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection QWidget::layoutDirection() const
    return Qt.LayoutDirection(self.uglySide.call(
        'ritual_ZNK7QWidget15layoutDirectionEv',
    ))

  def locale(self) -> QLocale:
    """
    Calls Qt's 'QLocale QWidget::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QWidget::locale() const
    address = self.uglySide.call('ritual_ZNK7QWidget6localeEv')
    from ..QtCore import QLocale
    return QLocale._cuteOwning(address)

  def isRightToLeft(self) -> bool:
    """
    Calls Qt's 'bool QWidget::isRightToLeft() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#isRightToLeft
    """
    #  bool QWidget::isRightToLeft() const
    return self.uglySide.call('ritual_ZNK7QWidget13isRightToLeftEv')

  def isLeftToRight(self) -> bool:
    """
    Calls Qt's 'bool QWidget::isLeftToRight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#isLeftToRight
    """
    #  bool QWidget::isLeftToRight() const
    return self.uglySide.call('ritual_ZNK7QWidget13isLeftToRightEv')

  def isActiveWindow(self) -> bool:
    """
    Calls Qt's 'bool QWidget::isActiveWindow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#isActiveWindow
    """
    #  bool QWidget::isActiveWindow() const
    return self.uglySide.call('ritual_ZNK7QWidget14isActiveWindowEv')

  def focusPolicy(self) -> Qt.FocusPolicy:
    """
    Calls Qt's 'Qt::FocusPolicy QWidget::focusPolicy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#focusPolicy

    Returns
    -------

    Qt.FocusPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.FocusPolicy(number)'
      gives.
    """
    #  Qt::FocusPolicy QWidget::focusPolicy() const
    return Qt.FocusPolicy(self.uglySide.call(
        'ritual_ZNK7QWidget11focusPolicyEv',
    ))

  def hasFocus(self) -> bool:
    """
    Calls Qt's 'bool QWidget::hasFocus() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#hasFocus
    """
    #  bool QWidget::hasFocus() const
    return self.uglySide.call('ritual_ZNK7QWidget8hasFocusEv')

  def focusProxy(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QWidget::focusProxy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#focusProxy

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QWidget::focusProxy() const
    address = self.uglySide.call('ritual_ZNK7QWidget10focusProxyEv')
    return QWidget._cuteAt(address)

  def contextMenuPolicy(self) -> Qt.ContextMenuPolicy:
    """
    Calls Qt's 'Qt::ContextMenuPolicy QWidget::contextMenuPolicy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#contextMenuPolicy

    Returns
    -------

    Qt.ContextMenuPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.ContextMenuPolicy(number)' gives.
    """
    #  Qt::ContextMenuPolicy QWidget::contextMenuPolicy() const
    return Qt.ContextMenuPolicy(self.uglySide.call(
        'ritual_ZNK7QWidget17contextMenuPolicyEv',
    ))

  def updatesEnabled(self) -> bool:
    """
    Calls Qt's 'bool QWidget::updatesEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#updatesEnabled
    """
    #  bool QWidget::updatesEnabled() const
    return self.uglySide.call('ritual_ZNK7QWidget14updatesEnabledEv')

  def graphicsProxyWidget(self) -> Optional[QGraphicsProxyWidget]:
    """
    Calls Qt's 'QGraphicsProxyWidget *QWidget::graphicsProxyWidget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#graphicsProxyWidget

    Returns
    -------

    Optional[QGraphicsProxyWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsProxyWidget *QWidget::graphicsProxyWidget() const
    address = self.uglySide.call('ritual_ZNK7QWidget19graphicsProxyWidgetEv')
    from . import QGraphicsProxyWidget
    return QGraphicsProxyWidget._cuteAt(address)

  def saveGeometry(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QWidget::saveGeometry() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#saveGeometry

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QWidget::saveGeometry() const
    address = self.uglySide.call('ritual_ZNK7QWidget12saveGeometryEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QWidget::isVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#isVisible
    """
    #  bool QWidget::isVisible() const
    return self.uglySide.call('ritual_ZNK7QWidget9isVisibleEv')

  @overload(THIS)
  @overload(NoneType)
  def isVisibleTo(self, a0: Optional[QWidget]) -> bool:
    """
    Calls Qt's 'bool QWidget::isVisibleTo(const QWidget *a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#isVisibleTo

    Parameters
    ----------

    a0 : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWidget::isVisibleTo(const QWidget *a0) const
    return self.uglySide.call(
        'ritual_ZNK7QWidget11isVisibleToEPKS_', self._addressOf(a0),
    )

  def isHidden(self) -> bool:
    """
    Calls Qt's 'bool QWidget::isHidden() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#isHidden
    """
    #  bool QWidget::isHidden() const
    return self.uglySide.call('ritual_ZNK7QWidget8isHiddenEv')

  def isMinimized(self) -> bool:
    """
    Calls Qt's 'bool QWidget::isMinimized() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#isMinimized
    """
    #  bool QWidget::isMinimized() const
    return self.uglySide.call('ritual_ZNK7QWidget11isMinimizedEv')

  def isMaximized(self) -> bool:
    """
    Calls Qt's 'bool QWidget::isMaximized() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#isMaximized
    """
    #  bool QWidget::isMaximized() const
    return self.uglySide.call('ritual_ZNK7QWidget11isMaximizedEv')

  def isFullScreen(self) -> bool:
    """
    Calls Qt's 'bool QWidget::isFullScreen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#isFullScreen
    """
    #  bool QWidget::isFullScreen() const
    return self.uglySide.call('ritual_ZNK7QWidget12isFullScreenEv')

  def windowState(self) -> Qt.WindowStates:
    """
    Calls Qt's 'Qt::WindowStates QWidget::windowState() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#windowState

    Returns
    -------

    Qt.WindowStates
      The value standing for the combination Qt gave back.
    """
    #  Qt::WindowStates QWidget::windowState() const
    return Qt.WindowStates(self.uglySide.call(
        'ritual_ZNK7QWidget11windowStateEv',
    ))

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QWidget::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWidget::sizeHint() const
    ritual = 'ritual_ZNK7QWidget8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QWidget8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QWidget::minimumSizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#minimumSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWidget::minimumSizeHint() const
    ritual = 'ritual_ZNK7QWidget15minimumSizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QWidget15minimumSizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def sizePolicy(self) -> QSizePolicy:
    """
    Calls Qt's 'QSizePolicy QWidget::sizePolicy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#sizePolicy

    Returns
    -------

    QSizePolicy
      A new cute QSizePolicy around the copy Qt gave back. Python owns it.
    """
    #  QSizePolicy QWidget::sizePolicy() const
    address = self.uglySide.call('ritual_ZNK7QWidget10sizePolicyEv')
    return QSizePolicy._cuteOwning(address)

  @overload(int)
  def heightForWidth(self, a0: int) -> int:
    """
    Calls Qt's 'int QWidget::heightForWidth(int a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#heightForWidth

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  int QWidget::heightForWidth(int a0) const
    ritual = 'ritual_ZNK7QWidget14heightForWidthEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QWidget14heightForWidthEi'
    return self.uglySide.call(ritual, a0)

  def hasHeightForWidth(self) -> bool:
    """
    Calls Qt's 'bool QWidget::hasHeightForWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#hasHeightForWidth
    """
    #  bool QWidget::hasHeightForWidth() const
    ritual = 'ritual_ZNK7QWidget17hasHeightForWidthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QWidget17hasHeightForWidthEv'
    return self.uglySide.call(ritual)

  def visibleRegion(self) -> QRegion:
    """
    Calls Qt's 'QRegion QWidget::visibleRegion() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#visibleRegion

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QWidget::visibleRegion() const
    address = self.uglySide.call('ritual_ZNK7QWidget13visibleRegionEv')
    from ..QtGui import QRegion
    return QRegion._cuteOwning(address)

  def contentsMargins(self) -> QMargins:
    """
    Calls Qt's 'QMargins QWidget::contentsMargins() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#contentsMargins

    Returns
    -------

    QMargins
      A new cute QMargins around the copy Qt gave back. Python owns it.
    """
    #  QMargins QWidget::contentsMargins() const
    address = self.uglySide.call('ritual_ZNK7QWidget15contentsMarginsEv')
    from ..QtCore import QMargins
    return QMargins._cuteOwning(address)

  def contentsRect(self) -> QRect:
    """
    Calls Qt's 'QRect QWidget::contentsRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#contentsRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QWidget::contentsRect() const
    address = self.uglySide.call('ritual_ZNK7QWidget12contentsRectEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def layout(self) -> Optional[QLayout]:
    """
    Calls Qt's 'QLayout *QWidget::layout() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#layout

    Returns
    -------

    Optional[QLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayout *QWidget::layout() const
    address = self.uglySide.call('ritual_ZNK7QWidget6layoutEv')
    from . import QLayout
    return QLayout._cuteAt(address)

  def focusWidget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QWidget::focusWidget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#focusWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QWidget::focusWidget() const
    address = self.uglySide.call('ritual_ZNK7QWidget11focusWidgetEv')
    return QWidget._cuteAt(address)

  def nextInFocusChain(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QWidget::nextInFocusChain() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#nextInFocusChain

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QWidget::nextInFocusChain() const
    address = self.uglySide.call('ritual_ZNK7QWidget16nextInFocusChainEv')
    return QWidget._cuteAt(address)

  def previousInFocusChain(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QWidget::previousInFocusChain() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#previousInFocusChain

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QWidget::previousInFocusChain() const
    address = self.uglySide.call(
        'ritual_ZNK7QWidget20previousInFocusChainEv',
    )
    return QWidget._cuteAt(address)

  def acceptDrops(self) -> bool:
    """
    Calls Qt's 'bool QWidget::acceptDrops() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#acceptDrops
    """
    #  bool QWidget::acceptDrops() const
    return self.uglySide.call('ritual_ZNK7QWidget11acceptDropsEv')

  def actions(self) -> QList[QAction]:
    """
    Calls Qt's 'QList<QAction *> QWidget::actions() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#actions

    Returns
    -------

    QList[QAction]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAction *> QWidget::actions() const
    address = self.uglySide.call('ritual_ZNK7QWidget7actionsEv')
    from ..QtGui import QAction
    return QList[QAction]._cuteOwning(address)

  def parentWidget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QWidget::parentWidget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#parentWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QWidget::parentWidget() const
    address = self.uglySide.call('ritual_ZNK7QWidget12parentWidgetEv')
    return QWidget._cuteAt(address)

  def windowFlags(self) -> Qt.WindowFlags:
    """
    Calls Qt's 'Qt::WindowFlags QWidget::windowFlags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#windowFlags

    Returns
    -------

    Qt.WindowFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::WindowFlags QWidget::windowFlags() const
    return Qt.WindowFlags(self.uglySide.call(
        'ritual_ZNK7QWidget11windowFlagsEv',
    ))

  def windowType(self) -> Qt.WindowType:
    """
    Calls Qt's 'Qt::WindowType QWidget::windowType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#windowType

    Returns
    -------

    Qt.WindowType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.WindowType(number)'
      gives.
    """
    #  Qt::WindowType QWidget::windowType() const
    return Qt.WindowType(self.uglySide.call(
        'ritual_ZNK7QWidget10windowTypeEv',
    ))

  @overload(int, int)
  def childAt(self, x: int, y: int) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QWidget::childAt(int x, int y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#childAt

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QWidget::childAt(int x, int y) const
    address = self.uglySide.call('ritual_ZNK7QWidget7childAtEii', x, y)
    return QWidget._cuteAt(address)

  @overload(QPoint)
  def childAt(self, p: QPoint) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QWidget::childAt(const QPoint &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#childAt

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QWidget::childAt(const QPoint &p) const
    address = self.uglySide.call(
        'ritual_ZNK7QWidget7childAtERK6QPoint', self._valueOf(p),
    )
    return QWidget._cuteAt(address)

  @overload(QPointF)
  def childAt(self, p: QPointF) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QWidget::childAt(const QPointF &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#childAt

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QWidget::childAt(const QPointF &p) const
    address = self.uglySide.call(
        'ritual_ZNK7QWidget7childAtERK7QPointF', self._valueOf(p),
    )
    return QWidget._cuteAt(address)

  @overload(Qt.WidgetAttribute)
  def testAttribute(self, a0: Qt.WidgetAttribute) -> bool:
    """
    Calls Qt's 'bool QWidget::testAttribute(Qt::WidgetAttribute a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#testAttribute

    Parameters
    ----------

    a0 : Qt.WidgetAttribute
      Passed on as its number.
    """
    #  bool QWidget::testAttribute(Qt::WidgetAttribute a0) const
    return self.uglySide.call(
        'ritual_ZNK7QWidget13testAttributeEN2Qt15WidgetAttributeE', a0.value,
    )

  def paintEngine(self) -> Optional[QPaintEngine]:
    """
    Calls Qt's 'QPaintEngine *QWidget::paintEngine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#paintEngine

    Returns
    -------

    Optional[QPaintEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintEngine *QWidget::paintEngine() const
    ritual = 'ritual_ZNK7QWidget11paintEngineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QWidget11paintEngineEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPaintEngine
    return QPaintEngine._cuteAt(address)

  @overload(THIS)
  @overload(NoneType)
  def isAncestorOf(self, child: Optional[QWidget]) -> bool:
    """
    Calls Qt's 'bool QWidget::isAncestorOf(const QWidget *child) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#isAncestorOf

    Parameters
    ----------

    child : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWidget::isAncestorOf(const QWidget *child) const
    return self.uglySide.call(
        'ritual_ZNK7QWidget12isAncestorOfEPKS_', self._addressOf(child),
    )

  def autoFillBackground(self) -> bool:
    """
    Calls Qt's 'bool QWidget::autoFillBackground() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#autoFillBackground
    """
    #  bool QWidget::autoFillBackground() const
    return self.uglySide.call('ritual_ZNK7QWidget18autoFillBackgroundEv')

  def backingStore(self) -> Optional[QBackingStore]:
    """
    Calls Qt's 'QBackingStore *QWidget::backingStore() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#backingStore

    Returns
    -------

    Optional[QBackingStore]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBackingStore *QWidget::backingStore() const
    address = self.uglySide.call('ritual_ZNK7QWidget12backingStoreEv')
    from ..QtGui import QBackingStore
    return QBackingStore._cuteAt(address)

  def windowHandle(self) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QWidget::windowHandle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#windowHandle

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QWidget::windowHandle() const
    address = self.uglySide.call('ritual_ZNK7QWidget12windowHandleEv')
    from ..QtGui import QWindow
    return QWindow._cuteAt(address)

  def screen(self) -> Optional[QScreen]:
    """
    Calls Qt's 'QScreen *QWidget::screen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#screen

    Returns
    -------

    Optional[QScreen]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScreen *QWidget::screen() const
    address = self.uglySide.call('ritual_ZNK7QWidget6screenEv')
    from ..QtGui import QScreen
    return QScreen._cuteAt(address)

  @overload(QPaintDevice.PaintDeviceMetric)
  def metric(self, a0: QPaintDevice.PaintDeviceMetric) -> int:
    """
    Calls Qt's 'int QWidget::metric(PaintDeviceMetric a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#metric

    Parameters
    ----------

    a0 : QPaintDevice.PaintDeviceMetric
      Passed on as its number.
    """
    #  int QWidget::metric(PaintDeviceMetric a0) const
    ritual = 'ritual_ZNK7QWidget6metricEN12QPaintDevice17PaintDeviceMetricE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK7QWidget6metricEN12QPaintDevice17PaintDeviceMetric'
          'E')
    return self.uglySide.call(ritual, a0.value)

  @overload(QPoint)
  @overload(NoneType)
  def redirected(self, offset: Optional[QPoint]) -> Optional[QPaintDevice]:
    """
    Calls Qt's 'QPaintDevice *QWidget::redirected(QPoint *offset) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#redirected

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
    #  QPaintDevice *QWidget::redirected(QPoint *offset) const
    ritual = 'ritual_ZNK7QWidget10redirectedEP6QPoint'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QWidget10redirectedEP6QPoint'
    address = self.uglySide.call(ritual, self._addressOf(offset))
    return QPaintDevice._cuteAt(address)

  def sharedPainter(self) -> Optional[QPainter]:
    """
    Calls Qt's 'QPainter *QWidget::sharedPainter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#sharedPainter

    Returns
    -------

    Optional[QPainter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPainter *QWidget::sharedPainter() const
    ritual = 'ritual_ZNK7QWidget13sharedPainterEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QWidget13sharedPainterEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPainter
    return QPainter._cuteAt(address)

  @overload(Qt.InputMethodQuery)
  def inputMethodQuery(self, a0: Qt.InputMethodQuery) -> QVariant:
    """
    Calls Qt's 'QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#inputMethodQuery

    Parameters
    ----------

    a0 : Qt.InputMethodQuery
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
    ritual = 'ritual_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE')
    address = self.uglySide.call(ritual, a0.value)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def inputMethodHints(self) -> Qt.InputMethodHints:
    """
    Calls Qt's 'Qt::InputMethodHints QWidget::inputMethodHints() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#inputMethodHints

    Returns
    -------

    Qt.InputMethodHints
      The value standing for the combination Qt gave back.
    """
    #  Qt::InputMethodHints QWidget::inputMethodHints() const
    return Qt.InputMethodHints(self.uglySide.call(
        'ritual_ZNK7QWidget16inputMethodHintsEv',
    ))

  @overload(Qt.WidgetAttribute)
  def testAttribute_helper(self, a0: Qt.WidgetAttribute) -> bool:
    """
    Calls Qt's 'bool QWidget::testAttribute_helper(Qt::WidgetAttribute a0)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#testAttribute_helper

    Parameters
    ----------

    a0 : Qt.WidgetAttribute
      Passed on as its number.
    """
    #  bool QWidget::testAttribute_helper(Qt::WidgetAttribute a0) const
    return self.uglySide.call(
        'ritual_ZNK7QWidget20testAttribute_helperEN2Qt15WidgetAttributeE',
        a0.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStyle)
  @overload(NoneType)
  def setStyle(self, a0: Optional[QStyle]) -> None:
    """
    Calls Qt's 'void QWidget::setStyle(QStyle *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setStyle

    Parameters
    ----------

    a0 : Optional[QStyle]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::setStyle(QStyle *a0)
    self.uglySide.call(
        'ritual_ZN7QWidget8setStyleEP6QStyle', self._addressOf(a0),
    )

  @overload(Qt.WindowModality)
  def setWindowModality(self, windowModality: Qt.WindowModality) -> None:
    """
    Calls Qt's 'void QWidget::setWindowModality(Qt::WindowModality
    windowModality)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setWindowModality

    Parameters
    ----------

    windowModality : Qt.WindowModality
      Passed on as its number.
    """
    #  void QWidget::setWindowModality(Qt::WindowModality windowModality)
    self.uglySide.call(
        'ritual_ZN7QWidget17setWindowModalityEN2Qt14WindowModalityE',
        windowModality.value,
    )

  @overload(bool)
  def setEnabled(self, a0: bool) -> None:
    """
    Calls Qt's 'void QWidget::setEnabled(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setEnabled

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QWidget::setEnabled(bool a0)
    self.uglySide.call('ritual_ZN7QWidget10setEnabledEb', a0)

  @overload(bool)
  def setDisabled(self, a0: bool) -> None:
    """
    Calls Qt's 'void QWidget::setDisabled(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setDisabled

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QWidget::setDisabled(bool a0)
    self.uglySide.call('ritual_ZN7QWidget11setDisabledEb', a0)

  @overload(bool)
  def setWindowModified(self, a0: bool) -> None:
    """
    Calls Qt's 'void QWidget::setWindowModified(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setWindowModified

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QWidget::setWindowModified(bool a0)
    self.uglySide.call('ritual_ZN7QWidget17setWindowModifiedEb', a0)

  @overload(QSize)
  def setMinimumSize(self, a0: QSize) -> None:
    """
    Calls Qt's 'void QWidget::setMinimumSize(const QSize &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setMinimumSize

    Parameters
    ----------

    a0 : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QWidget::setMinimumSize(const QSize &a0)
    self.uglySide.call(
        'ritual_ZN7QWidget14setMinimumSizeERK5QSize', self._valueOf(a0),
    )

  @overload(int, int)
  def setMinimumSize(self, minw: int, minh: int) -> None:
    """
    Calls Qt's 'void QWidget::setMinimumSize(int minw, int minh)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setMinimumSize

    Parameters
    ----------

    minw : int
      Passed on as it is.

    minh : int
      Passed on as it is.
    """
    #  void QWidget::setMinimumSize(int minw, int minh)
    self.uglySide.call('ritual_ZN7QWidget14setMinimumSizeEii', minw, minh)

  @overload(QSize)
  def setMaximumSize(self, a0: QSize) -> None:
    """
    Calls Qt's 'void QWidget::setMaximumSize(const QSize &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setMaximumSize

    Parameters
    ----------

    a0 : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QWidget::setMaximumSize(const QSize &a0)
    self.uglySide.call(
        'ritual_ZN7QWidget14setMaximumSizeERK5QSize', self._valueOf(a0),
    )

  @overload(int, int)
  def setMaximumSize(self, maxw: int, maxh: int) -> None:
    """
    Calls Qt's 'void QWidget::setMaximumSize(int maxw, int maxh)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setMaximumSize

    Parameters
    ----------

    maxw : int
      Passed on as it is.

    maxh : int
      Passed on as it is.
    """
    #  void QWidget::setMaximumSize(int maxw, int maxh)
    self.uglySide.call('ritual_ZN7QWidget14setMaximumSizeEii', maxw, maxh)

  @overload(int)
  def setMinimumWidth(self, minw: int) -> None:
    """
    Calls Qt's 'void QWidget::setMinimumWidth(int minw)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setMinimumWidth

    Parameters
    ----------

    minw : int
      Passed on as it is.
    """
    #  void QWidget::setMinimumWidth(int minw)
    self.uglySide.call('ritual_ZN7QWidget15setMinimumWidthEi', minw)

  @overload(int)
  def setMinimumHeight(self, minh: int) -> None:
    """
    Calls Qt's 'void QWidget::setMinimumHeight(int minh)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setMinimumHeight

    Parameters
    ----------

    minh : int
      Passed on as it is.
    """
    #  void QWidget::setMinimumHeight(int minh)
    self.uglySide.call('ritual_ZN7QWidget16setMinimumHeightEi', minh)

  @overload(int)
  def setMaximumWidth(self, maxw: int) -> None:
    """
    Calls Qt's 'void QWidget::setMaximumWidth(int maxw)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setMaximumWidth

    Parameters
    ----------

    maxw : int
      Passed on as it is.
    """
    #  void QWidget::setMaximumWidth(int maxw)
    self.uglySide.call('ritual_ZN7QWidget15setMaximumWidthEi', maxw)

  @overload(int)
  def setMaximumHeight(self, maxh: int) -> None:
    """
    Calls Qt's 'void QWidget::setMaximumHeight(int maxh)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setMaximumHeight

    Parameters
    ----------

    maxh : int
      Passed on as it is.
    """
    #  void QWidget::setMaximumHeight(int maxh)
    self.uglySide.call('ritual_ZN7QWidget16setMaximumHeightEi', maxh)

  @overload(QSize)
  def setSizeIncrement(self, a0: QSize) -> None:
    """
    Calls Qt's 'void QWidget::setSizeIncrement(const QSize &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setSizeIncrement

    Parameters
    ----------

    a0 : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QWidget::setSizeIncrement(const QSize &a0)
    self.uglySide.call(
        'ritual_ZN7QWidget16setSizeIncrementERK5QSize', self._valueOf(a0),
    )

  @overload(int, int)
  def setSizeIncrement(self, w: int, h: int) -> None:
    """
    Calls Qt's 'void QWidget::setSizeIncrement(int w, int h)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setSizeIncrement

    Parameters
    ----------

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.
    """
    #  void QWidget::setSizeIncrement(int w, int h)
    self.uglySide.call('ritual_ZN7QWidget16setSizeIncrementEii', w, h)

  @overload(QSize)
  def setBaseSize(self, a0: QSize) -> None:
    """
    Calls Qt's 'void QWidget::setBaseSize(const QSize &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setBaseSize

    Parameters
    ----------

    a0 : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QWidget::setBaseSize(const QSize &a0)
    self.uglySide.call(
        'ritual_ZN7QWidget11setBaseSizeERK5QSize', self._valueOf(a0),
    )

  @overload(int, int)
  def setBaseSize(self, basew: int, baseh: int) -> None:
    """
    Calls Qt's 'void QWidget::setBaseSize(int basew, int baseh)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setBaseSize

    Parameters
    ----------

    basew : int
      Passed on as it is.

    baseh : int
      Passed on as it is.
    """
    #  void QWidget::setBaseSize(int basew, int baseh)
    self.uglySide.call('ritual_ZN7QWidget11setBaseSizeEii', basew, baseh)

  @overload(QSize)
  def setFixedSize(self, a0: QSize) -> None:
    """
    Calls Qt's 'void QWidget::setFixedSize(const QSize &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setFixedSize

    Parameters
    ----------

    a0 : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QWidget::setFixedSize(const QSize &a0)
    self.uglySide.call(
        'ritual_ZN7QWidget12setFixedSizeERK5QSize', self._valueOf(a0),
    )

  @overload(int, int)
  def setFixedSize(self, w: int, h: int) -> None:
    """
    Calls Qt's 'void QWidget::setFixedSize(int w, int h)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setFixedSize

    Parameters
    ----------

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.
    """
    #  void QWidget::setFixedSize(int w, int h)
    self.uglySide.call('ritual_ZN7QWidget12setFixedSizeEii', w, h)

  @overload(int)
  def setFixedWidth(self, w: int) -> None:
    """
    Calls Qt's 'void QWidget::setFixedWidth(int w)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setFixedWidth

    Parameters
    ----------

    w : int
      Passed on as it is.
    """
    #  void QWidget::setFixedWidth(int w)
    self.uglySide.call('ritual_ZN7QWidget13setFixedWidthEi', w)

  @overload(int)
  def setFixedHeight(self, h: int) -> None:
    """
    Calls Qt's 'void QWidget::setFixedHeight(int h)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setFixedHeight

    Parameters
    ----------

    h : int
      Passed on as it is.
    """
    #  void QWidget::setFixedHeight(int h)
    self.uglySide.call('ritual_ZN7QWidget14setFixedHeightEi', h)

  @overload(QPalette)
  def setPalette(self, a0: QPalette) -> None:
    """
    Calls Qt's 'void QWidget::setPalette(const QPalette &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setPalette

    Parameters
    ----------

    a0 : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.
    """
    #  void QWidget::setPalette(const QPalette &a0)
    self.uglySide.call(
        'ritual_ZN7QWidget10setPaletteERK8QPalette', self._valueOf(a0),
    )

  @overload(QPalette.ColorRole)
  def setBackgroundRole(self, a0: QPalette.ColorRole) -> None:
    """
    Calls Qt's 'void QWidget::setBackgroundRole(QPalette::ColorRole a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setBackgroundRole

    Parameters
    ----------

    a0 : QPalette.ColorRole
      Passed on as its number.
    """
    #  void QWidget::setBackgroundRole(QPalette::ColorRole a0)
    self.uglySide.call(
        'ritual_ZN7QWidget17setBackgroundRoleEN8QPalette9ColorRoleE',
        a0.value,
    )

  @overload(QPalette.ColorRole)
  def setForegroundRole(self, a0: QPalette.ColorRole) -> None:
    """
    Calls Qt's 'void QWidget::setForegroundRole(QPalette::ColorRole a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setForegroundRole

    Parameters
    ----------

    a0 : QPalette.ColorRole
      Passed on as its number.
    """
    #  void QWidget::setForegroundRole(QPalette::ColorRole a0)
    self.uglySide.call(
        'ritual_ZN7QWidget17setForegroundRoleEN8QPalette9ColorRoleE',
        a0.value,
    )

  @overload(QFont)
  def setFont(self, a0: QFont) -> None:
    """
    Calls Qt's 'void QWidget::setFont(const QFont &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setFont

    Parameters
    ----------

    a0 : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QWidget::setFont(const QFont &a0)
    self.uglySide.call(
        'ritual_ZN7QWidget7setFontERK5QFont', self._valueOf(a0),
    )

  @overload(QCursor)
  def setCursor(self, a0: QCursor) -> None:
    """
    Calls Qt's 'void QWidget::setCursor(const QCursor &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setCursor

    Parameters
    ----------

    a0 : QCursor
      Passed on as a value: Qt reads the C++ QCursor, which stays Python's
      own.
    """
    #  void QWidget::setCursor(const QCursor &a0)
    self.uglySide.call(
        'ritual_ZN7QWidget9setCursorERK7QCursor', self._valueOf(a0),
    )

  @overload(bool)
  def setMouseTracking(self, enable: bool) -> None:
    """
    Calls Qt's 'void QWidget::setMouseTracking(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setMouseTracking

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QWidget::setMouseTracking(bool enable)
    self.uglySide.call('ritual_ZN7QWidget16setMouseTrackingEb', enable)

  @overload(bool)
  def setTabletTracking(self, enable: bool) -> None:
    """
    Calls Qt's 'void QWidget::setTabletTracking(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setTabletTracking

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QWidget::setTabletTracking(bool enable)
    self.uglySide.call('ritual_ZN7QWidget17setTabletTrackingEb', enable)

  @overload(QBitmap)
  def setMask(self, a0: QBitmap) -> None:
    """
    Calls Qt's 'void QWidget::setMask(const QBitmap &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setMask

    Parameters
    ----------

    a0 : QBitmap
      Passed on as a value: Qt reads the C++ QBitmap, which stays Python's
      own.
    """
    #  void QWidget::setMask(const QBitmap &a0)
    self.uglySide.call(
        'ritual_ZN7QWidget7setMaskERK7QBitmap', self._valueOf(a0),
    )

  @overload(QRegion)
  def setMask(self, a0: QRegion) -> None:
    """
    Calls Qt's 'void QWidget::setMask(const QRegion &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setMask

    Parameters
    ----------

    a0 : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QWidget::setMask(const QRegion &a0)
    self.uglySide.call(
        'ritual_ZN7QWidget7setMaskERK7QRegion', self._valueOf(a0),
    )

  @overload(QGraphicsEffect)
  @overload(NoneType)
  def setGraphicsEffect(self, effect: Optional[QGraphicsEffect]) -> None:
    """
    Calls Qt's 'void QWidget::setGraphicsEffect(QGraphicsEffect *effect)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setGraphicsEffect

    Parameters
    ----------

    effect : Optional[QGraphicsEffect]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::setGraphicsEffect(QGraphicsEffect *effect)
    self.uglySide.call(
        'ritual_ZN7QWidget17setGraphicsEffectEP15QGraphicsEffect',
        self._addressOf(effect),
    )

  @overload(str)
  def setWindowTitle(self, a0: str) -> None:
    """
    Calls Qt's 'void QWidget::setWindowTitle(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setWindowTitle

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidget::setWindowTitle(const QString &a0)
    self.uglySide.call('ritual_ZN7QWidget14setWindowTitleERK7QString', a0)

  @overload(str)
  def setStyleSheet(self, styleSheet: str) -> None:
    """
    Calls Qt's 'void QWidget::setStyleSheet(const QString &styleSheet)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setStyleSheet

    Parameters
    ----------

    styleSheet : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidget::setStyleSheet(const QString &styleSheet)
    self.uglySide.call(
        'ritual_ZN7QWidget13setStyleSheetERK7QString', styleSheet,
    )

  @overload(QIcon)
  def setWindowIcon(self, icon: QIcon) -> None:
    """
    Calls Qt's 'void QWidget::setWindowIcon(const QIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setWindowIcon

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.
    """
    #  void QWidget::setWindowIcon(const QIcon &icon)
    self.uglySide.call(
        'ritual_ZN7QWidget13setWindowIconERK5QIcon', self._valueOf(icon),
    )

  @overload(str)
  def setWindowIconText(self, a0: str) -> None:
    """
    Calls Qt's 'void QWidget::setWindowIconText(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setWindowIconText

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidget::setWindowIconText(const QString &a0)
    self.uglySide.call('ritual_ZN7QWidget17setWindowIconTextERK7QString', a0)

  @overload(str)
  def setWindowRole(self, a0: str) -> None:
    """
    Calls Qt's 'void QWidget::setWindowRole(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setWindowRole

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidget::setWindowRole(const QString &a0)
    self.uglySide.call('ritual_ZN7QWidget13setWindowRoleERK7QString', a0)

  @overload(str)
  def setWindowFilePath(self, filePath: str) -> None:
    """
    Calls Qt's 'void QWidget::setWindowFilePath(const QString &filePath)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setWindowFilePath

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidget::setWindowFilePath(const QString &filePath)
    self.uglySide.call(
        'ritual_ZN7QWidget17setWindowFilePathERK7QString', filePath,
    )

  @overload(float)
  def setWindowOpacity(self, level: float) -> None:
    """
    Calls Qt's 'void QWidget::setWindowOpacity(qreal level)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setWindowOpacity

    Parameters
    ----------

    level : float
      Passed on as it is.
    """
    #  void QWidget::setWindowOpacity(qreal level)
    self.uglySide.call('ritual_ZN7QWidget16setWindowOpacityEd', level)

  @overload(str)
  def setToolTip(self, a0: str) -> None:
    """
    Calls Qt's 'void QWidget::setToolTip(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setToolTip

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidget::setToolTip(const QString &a0)
    self.uglySide.call('ritual_ZN7QWidget10setToolTipERK7QString', a0)

  @overload(int)
  def setToolTipDuration(self, msec: int) -> None:
    """
    Calls Qt's 'void QWidget::setToolTipDuration(int msec)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setToolTipDuration

    Parameters
    ----------

    msec : int
      Passed on as it is.
    """
    #  void QWidget::setToolTipDuration(int msec)
    self.uglySide.call('ritual_ZN7QWidget18setToolTipDurationEi', msec)

  @overload(str)
  def setStatusTip(self, a0: str) -> None:
    """
    Calls Qt's 'void QWidget::setStatusTip(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setStatusTip

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidget::setStatusTip(const QString &a0)
    self.uglySide.call('ritual_ZN7QWidget12setStatusTipERK7QString', a0)

  @overload(str)
  def setWhatsThis(self, a0: str) -> None:
    """
    Calls Qt's 'void QWidget::setWhatsThis(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setWhatsThis

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidget::setWhatsThis(const QString &a0)
    self.uglySide.call('ritual_ZN7QWidget12setWhatsThisERK7QString', a0)

  @overload(str)
  def setAccessibleName(self, name: str) -> None:
    """
    Calls Qt's 'void QWidget::setAccessibleName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setAccessibleName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidget::setAccessibleName(const QString &name)
    self.uglySide.call(
        'ritual_ZN7QWidget17setAccessibleNameERK7QString', name,
    )

  @overload(str)
  def setAccessibleDescription(self, description: str) -> None:
    """
    Calls Qt's 'void QWidget::setAccessibleDescription(const QString
    &description)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidget.html#setAccessibleDescription

    Parameters
    ----------

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidget::setAccessibleDescription(const QString &description)
    self.uglySide.call(
        'ritual_ZN7QWidget24setAccessibleDescriptionERK7QString',
        description,
    )

  @overload(str)
  def setAccessibleIdentifier(self, identifier: str) -> None:
    """
    Calls Qt's 'void QWidget::setAccessibleIdentifier(const QString
    &identifier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidget.html#setAccessibleIdentifier

    Parameters
    ----------

    identifier : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidget::setAccessibleIdentifier(const QString &identifier)
    self.uglySide.call(
        'ritual_ZN7QWidget23setAccessibleIdentifierERK7QString', identifier,
    )

  @overload(Qt.LayoutDirection)
  def setLayoutDirection(self, direction: Qt.LayoutDirection) -> None:
    """
    Calls Qt's 'void QWidget::setLayoutDirection(Qt::LayoutDirection
    direction)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setLayoutDirection

    Parameters
    ----------

    direction : Qt.LayoutDirection
      Passed on as its number.
    """
    #  void QWidget::setLayoutDirection(Qt::LayoutDirection direction)
    self.uglySide.call(
        'ritual_ZN7QWidget18setLayoutDirectionEN2Qt15LayoutDirectionE',
        direction.value,
    )

  @overload(QLocale)
  def setLocale(self, locale: QLocale) -> None:
    """
    Calls Qt's 'void QWidget::setLocale(const QLocale &locale)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setLocale

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QWidget::setLocale(const QLocale &locale)
    self.uglySide.call(
        'ritual_ZN7QWidget9setLocaleERK7QLocale', self._valueOf(locale),
    )

  @overload()
  def setFocus(self) -> None:
    """
    Calls Qt's 'void QWidget::setFocus()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setFocus
    """
    #  void QWidget::setFocus()
    self.uglySide.call('ritual_ZN7QWidget8setFocusEv')

  @overload(Qt.FocusReason)
  def setFocus(self, reason: Qt.FocusReason) -> None:
    """
    Calls Qt's 'void QWidget::setFocus(Qt::FocusReason reason)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setFocus

    Parameters
    ----------

    reason : Qt.FocusReason
      Passed on as its number.
    """
    #  void QWidget::setFocus(Qt::FocusReason reason)
    self.uglySide.call(
        'ritual_ZN7QWidget8setFocusEN2Qt11FocusReasonE', reason.value,
    )

  @overload(Qt.FocusPolicy)
  def setFocusPolicy(self, policy: Qt.FocusPolicy) -> None:
    """
    Calls Qt's 'void QWidget::setFocusPolicy(Qt::FocusPolicy policy)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setFocusPolicy

    Parameters
    ----------

    policy : Qt.FocusPolicy
      Passed on as its number.
    """
    #  void QWidget::setFocusPolicy(Qt::FocusPolicy policy)
    self.uglySide.call(
        'ritual_ZN7QWidget14setFocusPolicyEN2Qt11FocusPolicyE', policy.value,
    )

  @overload(THIS)
  @overload(NoneType)
  def setFocusProxy(self, a0: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QWidget::setFocusProxy(QWidget *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setFocusProxy

    Parameters
    ----------

    a0 : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::setFocusProxy(QWidget *a0)
    self.uglySide.call(
        'ritual_ZN7QWidget13setFocusProxyEPS_', self._addressOf(a0),
    )

  @overload(Qt.ContextMenuPolicy)
  def setContextMenuPolicy(self, policy: Qt.ContextMenuPolicy) -> None:
    """
    Calls Qt's 'void QWidget::setContextMenuPolicy(Qt::ContextMenuPolicy
    policy)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setContextMenuPolicy

    Parameters
    ----------

    policy : Qt.ContextMenuPolicy
      Passed on as its number.
    """
    #  void QWidget::setContextMenuPolicy(Qt::ContextMenuPolicy policy)
    self.uglySide.call(
        'ritual_ZN7QWidget20setContextMenuPolicyEN2Qt17ContextMenuPolicyE',
        policy.value,
    )

  @overload(int)
  @overload(int, bool)
  def setShortcutEnabled(self, id: int, enable: bool = True) -> None:
    """
    Calls Qt's 'void QWidget::setShortcutEnabled(int id, bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setShortcutEnabled

    Parameters
    ----------

    id : int
      Passed on as it is.

    enable : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QWidget::setShortcutEnabled(int id, bool enable)
    self.uglySide.call(
        'ritual_ZN7QWidget18setShortcutEnabledEib', id, enable,
    )

  @overload(int)
  @overload(int, bool)
  def setShortcutAutoRepeat(self, id: int, enable: bool = True) -> None:
    """
    Calls Qt's 'void QWidget::setShortcutAutoRepeat(int id, bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setShortcutAutoRepeat

    Parameters
    ----------

    id : int
      Passed on as it is.

    enable : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QWidget::setShortcutAutoRepeat(int id, bool enable)
    self.uglySide.call(
        'ritual_ZN7QWidget21setShortcutAutoRepeatEib', id, enable,
    )

  @overload(bool)
  def setUpdatesEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QWidget::setUpdatesEnabled(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setUpdatesEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QWidget::setUpdatesEnabled(bool enable)
    self.uglySide.call('ritual_ZN7QWidget17setUpdatesEnabledEb', enable)

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QWidget::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QWidget::setVisible(bool visible)
    ritual = 'ritual_ZN7QWidget10setVisibleEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWidget10setVisibleEb'
    self.uglySide.call(ritual, visible)

  @overload(bool)
  def setHidden(self, hidden: bool) -> None:
    """
    Calls Qt's 'void QWidget::setHidden(bool hidden)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setHidden

    Parameters
    ----------

    hidden : bool
      Passed on as it is.
    """
    #  void QWidget::setHidden(bool hidden)
    self.uglySide.call('ritual_ZN7QWidget9setHiddenEb', hidden)

  @overload(int, int, int, int)
  def setGeometry(self, x: int, y: int, w: int, h: int) -> None:
    """
    Calls Qt's 'void QWidget::setGeometry(int x, int y, int w, int h)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setGeometry

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.
    """
    #  void QWidget::setGeometry(int x, int y, int w, int h)
    self.uglySide.call('ritual_ZN7QWidget11setGeometryEiiii', x, y, w, h)

  @overload(QRect)
  def setGeometry(self, a0: QRect) -> None:
    """
    Calls Qt's 'void QWidget::setGeometry(const QRect &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setGeometry

    Parameters
    ----------

    a0 : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QWidget::setGeometry(const QRect &a0)
    self.uglySide.call(
        'ritual_ZN7QWidget11setGeometryERK5QRect', self._valueOf(a0),
    )

  @overload(Qt.WindowStates)
  def setWindowState(self, state: Qt.WindowStates) -> None:
    """
    Calls Qt's 'void QWidget::setWindowState(Qt::WindowStates state)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setWindowState

    Parameters
    ----------

    state : Qt.WindowStates
      Passed on as its number.
    """
    #  void QWidget::setWindowState(Qt::WindowStates state)
    self.uglySide.call(
        'ritual_ZN7QWidget14setWindowStateE6QFlagsIN2Qt11WindowStateEE',
        state.value,
    )

  @overload(QSizePolicy)
  def setSizePolicy(self, a0: QSizePolicy) -> None:
    """
    Calls Qt's 'void QWidget::setSizePolicy(QSizePolicy a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setSizePolicy

    Parameters
    ----------

    a0 : QSizePolicy
      Passed on as a value: Qt reads the C++ QSizePolicy, which stays
      Python's own.
    """
    #  void QWidget::setSizePolicy(QSizePolicy a0)
    self.uglySide.call(
        'ritual_ZN7QWidget13setSizePolicyE11QSizePolicy', self._valueOf(a0),
    )

  @overload(QSizePolicy.Policy, QSizePolicy.Policy)
  def setSizePolicy(
      self,
      horizontal: QSizePolicy.Policy,
      vertical: QSizePolicy.Policy,
  ) -> None:
    """
    Calls Qt's 'void QWidget::setSizePolicy(QSizePolicy::Policy horizontal,
    QSizePolicy::Policy vertical)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setSizePolicy

    Parameters
    ----------

    horizontal : QSizePolicy.Policy
      Passed on as its number.

    vertical : QSizePolicy.Policy
      Passed on as its number.
    """
    #  void QWidget::setSizePolicy(QSizePolicy::Policy horizontal,
    #      QSizePolicy::Policy vertical)
    self.uglySide.call(
        'ritual_ZN7QWidget13setSizePolicyEN11QSizePolicy6PolicyES1_',
        horizontal.value, vertical.value,
    )

  @overload(int, int, int, int)
  def setContentsMargins(
      self,
      left: int,
      top: int,
      right: int,
      bottom: int,
  ) -> None:
    """
    Calls Qt's 'void QWidget::setContentsMargins(int left, int top, int
    right, int bottom)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setContentsMargins

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
    #  void QWidget::setContentsMargins(int left, int top, int right, int
    #      bottom)
    self.uglySide.call(
        'ritual_ZN7QWidget18setContentsMarginsEiiii',
        left, top, right, bottom,
    )

  @overload(QMargins)
  def setContentsMargins(self, margins: QMargins) -> None:
    """
    Calls Qt's 'void QWidget::setContentsMargins(const QMargins &margins)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setContentsMargins

    Parameters
    ----------

    margins : QMargins
      Passed on as a value: Qt reads the C++ QMargins, which stays Python's
      own.
    """
    #  void QWidget::setContentsMargins(const QMargins &margins)
    self.uglySide.call(
        'ritual_ZN7QWidget18setContentsMarginsERK8QMargins',
        self._valueOf(margins),
    )

  @overload(QLayout)
  @overload(NoneType)
  def setLayout(self, a0: Optional[QLayout]) -> None:
    """
    Calls Qt's 'void QWidget::setLayout(QLayout *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setLayout

    Parameters
    ----------

    a0 : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::setLayout(QLayout *a0)
    self.uglySide.call(
        'ritual_ZN7QWidget9setLayoutEP7QLayout', self._addressOf(a0),
    )

  @overload(THIS)
  @overload(NoneType)
  def setParent(self, parent: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QWidget::setParent(QWidget *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setParent

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::setParent(QWidget *parent)
    self.uglySide.call(
        'ritual_ZN7QWidget9setParentEPS_', self._addressOf(parent),
    )

  @overload(THIS, Qt.WindowFlags)
  @overload(NoneType, Qt.WindowFlags)
  def setParent(self, parent: Optional[QWidget], f: Qt.WindowFlags) -> None:
    """
    Calls Qt's 'void QWidget::setParent(QWidget *parent, Qt::WindowFlags f)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setParent

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    f : Qt.WindowFlags
      Passed on as its number.
    """
    #  void QWidget::setParent(QWidget *parent, Qt::WindowFlags f)
    self.uglySide.call(
        'ritual_ZN7QWidget9setParentEPS_6QFlagsIN2Qt10WindowTypeEE',
        self._addressOf(parent), f.value,
    )

  @overload(bool)
  def setAcceptDrops(self, on: bool) -> None:
    """
    Calls Qt's 'void QWidget::setAcceptDrops(bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setAcceptDrops

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QWidget::setAcceptDrops(bool on)
    self.uglySide.call('ritual_ZN7QWidget14setAcceptDropsEb', on)

  @overload(Qt.WindowFlags)
  def setWindowFlags(self, type: Qt.WindowFlags) -> None:
    """
    Calls Qt's 'void QWidget::setWindowFlags(Qt::WindowFlags type)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setWindowFlags

    Parameters
    ----------

    type : Qt.WindowFlags
      Passed on as its number.
    """
    #  void QWidget::setWindowFlags(Qt::WindowFlags type)
    self.uglySide.call(
        'ritual_ZN7QWidget14setWindowFlagsE6QFlagsIN2Qt10WindowTypeEE',
        type.value,
    )

  @overload(Qt.WindowType)
  @overload(Qt.WindowType, bool)
  def setWindowFlag(self, a0: Qt.WindowType, on: bool = True) -> None:
    """
    Calls Qt's 'void QWidget::setWindowFlag(Qt::WindowType a0, bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setWindowFlag

    Parameters
    ----------

    a0 : Qt.WindowType
      Passed on as its number.

    on : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QWidget::setWindowFlag(Qt::WindowType a0, bool on)
    self.uglySide.call(
        'ritual_ZN7QWidget13setWindowFlagEN2Qt10WindowTypeEb', a0.value, on,
    )

  @overload(Qt.WidgetAttribute)
  @overload(Qt.WidgetAttribute, bool)
  def setAttribute(self, a0: Qt.WidgetAttribute, on: bool = True) -> None:
    """
    Calls Qt's 'void QWidget::setAttribute(Qt::WidgetAttribute a0, bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setAttribute

    Parameters
    ----------

    a0 : Qt.WidgetAttribute
      Passed on as its number.

    on : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QWidget::setAttribute(Qt::WidgetAttribute a0, bool on)
    self.uglySide.call(
        'ritual_ZN7QWidget12setAttributeEN2Qt15WidgetAttributeEb',
        a0.value, on,
    )

  @overload(bool)
  def setAutoFillBackground(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QWidget::setAutoFillBackground(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setAutoFillBackground

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QWidget::setAutoFillBackground(bool enabled)
    self.uglySide.call('ritual_ZN7QWidget21setAutoFillBackgroundEb', enabled)

  @overload(QScreen)
  @overload(NoneType)
  def setScreen(self, a0: Optional[QScreen]) -> None:
    """
    Calls Qt's 'void QWidget::setScreen(QScreen *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setScreen

    Parameters
    ----------

    a0 : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::setScreen(QScreen *a0)
    self.uglySide.call(
        'ritual_ZN7QWidget9setScreenEP7QScreen', self._addressOf(a0),
    )

  @overload(Qt.InputMethodHints)
  def setInputMethodHints(self, hints: Qt.InputMethodHints) -> None:
    """
    Calls Qt's 'void QWidget::setInputMethodHints(Qt::InputMethodHints
    hints)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setInputMethodHints

    Parameters
    ----------

    hints : Qt.InputMethodHints
      Passed on as its number.
    """
    #  void QWidget::setInputMethodHints(Qt::InputMethodHints hints)
    self.uglySide.call(
        'ritual_ZN7QWidget19setInputMethodHintsE6QFlagsIN2Qt15InputMethodHi'
        'ntEE',
        hints.value,
    )

  @overload(QBackingStore)
  @overload(NoneType)
  def setBackingStore(self, store: Optional[QBackingStore]) -> None:
    """
    Calls Qt's 'void QWidget::setBackingStore(QBackingStore *store)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setBackingStore

    Parameters
    ----------

    store : Optional[QBackingStore]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::setBackingStore(QBackingStore *store)
    self.uglySide.call(
        'ritual_ZN7QWidget15setBackingStoreEP13QBackingStore',
        self._addressOf(store),
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
  @overload(THIS)
  @overload(NoneType)
  @overload(THIS, Qt.WindowFlags)
  @overload(NoneType, Qt.WindowFlags)
  def __init__(
      self,
      parent: Optional[QWidget] = None,
      f: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> None:
    """
    Notes what was given, for Qt's 'QWidget::QWidget(QWidget *parent,
    Qt::WindowFlags f)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#QWidget

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    f : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  QWidget::QWidget(QWidget *parent, Qt::WindowFlags f)
    self._noteCreation(QWidget, lambda: Rituals.call(
        'ritual_ZN7QWidgetC1EPS_6QFlagsIN2Qt10WindowTypeEE',
        self._addressOf(parent), f.value,
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

  def createWinId(self) -> None:
    """
    Calls Qt's 'void QWidget::createWinId()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#createWinId
    """
    #  void QWidget::createWinId()
    self.uglySide.call('ritual_ZN7QWidget11createWinIdEv')

  def unsetCursor(self) -> None:
    """
    Calls Qt's 'void QWidget::unsetCursor()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#unsetCursor
    """
    #  void QWidget::unsetCursor()
    self.uglySide.call('ritual_ZN7QWidget11unsetCursorEv')

  def clearMask(self) -> None:
    """
    Calls Qt's 'void QWidget::clearMask()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#clearMask
    """
    #  void QWidget::clearMask()
    self.uglySide.call('ritual_ZN7QWidget9clearMaskEv')

  @overload(QPaintDevice)
  @overload(NoneType)
  @overload(QPaintDevice, QPoint)
  @overload(NoneType, QPoint)
  @overload(QPaintDevice, QPoint, QRegion)
  @overload(NoneType, QPoint, QRegion)
  @overload(QPaintDevice, QPoint, QRegion, RenderFlags)
  @overload(NoneType, QPoint, QRegion, RenderFlags)
  def render(
      self,
      target: Optional[QPaintDevice],
      targetOffset: Optional[QPoint] = None,
      sourceRegion: Optional[QRegion] = None,
      renderFlags: RenderFlags = (
          RenderFlags.DrawWindowBackground | RenderFlags.DrawChildren),
  ) -> None:
    """
    Calls Qt's 'void QWidget::render(QPaintDevice *target, const QPoint
    &targetOffset, const QRegion &sourceRegion, RenderFlags renderFlags)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#render

    Parameters
    ----------

    target : Optional[QPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    targetOffset : Optional[QPoint]
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own. May be left out, as in Qt: a new 'QPoint()' is then passed on.

    sourceRegion : Optional[QRegion]
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own. May be left out, as in Qt: a new 'QRegion()' is then passed on.

    renderFlags : RenderFlags
      Passed on as its number. May be left out, as in Qt: it is then
      RenderFlags.DrawWindowBackground | RenderFlags.DrawChildren.
    """
    #  void QWidget::render(QPaintDevice *target, const QPoint &targetOffset,
    #      const QRegion &sourceRegion, RenderFlags renderFlags)
    if targetOffset is None:
      from ..QtCore import QPoint
      targetOffset = QPoint()
    if sourceRegion is None:
      from ..QtGui import QRegion
      sourceRegion = QRegion()
    self.uglySide.call(
        'ritual_ZN7QWidget6renderEP12QPaintDeviceRK6QPointRK7QRegion6QFlags'
        'INS_10RenderFlagEE',
        self._addressOf(target, 'QPaintDevice'), self._valueOf(targetOffset),
        self._valueOf(sourceRegion), renderFlags.value,
    )

  @overload(QPainter)
  @overload(QPainter, QPoint)
  @overload(QPainter, QPoint, QRegion)
  @overload(QPainter, QPoint, QRegion, RenderFlags)
  def render(
      self,
      painter: Optional[QPainter],
      targetOffset: Optional[QPoint] = None,
      sourceRegion: Optional[QRegion] = None,
      renderFlags: RenderFlags = (
          RenderFlags.DrawWindowBackground | RenderFlags.DrawChildren),
  ) -> None:
    """
    Calls Qt's 'void QWidget::render(QPainter *painter, const QPoint
    &targetOffset, const QRegion &sourceRegion, RenderFlags renderFlags)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#render

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    targetOffset : Optional[QPoint]
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own. May be left out, as in Qt: a new 'QPoint()' is then passed on.

    sourceRegion : Optional[QRegion]
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own. May be left out, as in Qt: a new 'QRegion()' is then passed on.

    renderFlags : RenderFlags
      Passed on as its number. May be left out, as in Qt: it is then
      RenderFlags.DrawWindowBackground | RenderFlags.DrawChildren.
    """
    #  void QWidget::render(QPainter *painter, const QPoint &targetOffset,
    #      const QRegion &sourceRegion, RenderFlags renderFlags)
    if targetOffset is None:
      from ..QtCore import QPoint
      targetOffset = QPoint()
    if sourceRegion is None:
      from ..QtGui import QRegion
      sourceRegion = QRegion()
    self.uglySide.call(
        'ritual_ZN7QWidget6renderEP8QPainterRK6QPointRK7QRegion6QFlagsINS_1'
        '0RenderFlagEE',
        self._addressOf(painter), self._valueOf(targetOffset),
        self._valueOf(sourceRegion), renderFlags.value,
    )

  @overload()
  @overload(QRect)
  def grab(self, rectangle: Optional[QRect] = None) -> QPixmap:
    """
    Calls Qt's 'QPixmap QWidget::grab(const QRect &rectangle)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#grab

    Parameters
    ----------

    rectangle : Optional[QRect]
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
      May be left out, as in Qt: a new 'QRect(QPoint(0, 0), QSize(-1, -1))'
      is then passed on.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QWidget::grab(const QRect &rectangle)
    if rectangle is None:
      from ..QtCore import QRect
      from ..QtCore import QPoint
      from ..QtCore import QSize
      rectangle = QRect(QPoint(0, 0), QSize(-1, -1))
    address = self.uglySide.call(
        'ritual_ZN7QWidget4grabERK5QRect', self._valueOf(rectangle),
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(Qt.GestureType)
  @overload(Qt.GestureType, Qt.GestureFlags)
  def grabGesture(
      self,
      type: Qt.GestureType,
      flags: Qt.GestureFlags = Qt.GestureFlags(),
  ) -> None:
    """
    Calls Qt's 'void QWidget::grabGesture(Qt::GestureType type,
    Qt::GestureFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#grabGesture

    Parameters
    ----------

    type : Qt.GestureType
      Passed on as its number.

    flags : Qt.GestureFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.GestureFlags().
    """
    #  void QWidget::grabGesture(Qt::GestureType type, Qt::GestureFlags
    #      flags)
    self.uglySide.call(
        'ritual_ZN7QWidget11grabGestureEN2Qt11GestureTypeE6QFlagsINS0_11Ges'
        'tureFlagEE',
        type.value, flags.value,
    )

  @overload(Qt.GestureType)
  def ungrabGesture(self, type: Qt.GestureType) -> None:
    """
    Calls Qt's 'void QWidget::ungrabGesture(Qt::GestureType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#ungrabGesture

    Parameters
    ----------

    type : Qt.GestureType
      Passed on as its number.
    """
    #  void QWidget::ungrabGesture(Qt::GestureType type)
    self.uglySide.call(
        'ritual_ZN7QWidget13ungrabGestureEN2Qt11GestureTypeE', type.value,
    )

  def unsetLayoutDirection(self) -> None:
    """
    Calls Qt's 'void QWidget::unsetLayoutDirection()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#unsetLayoutDirection
    """
    #  void QWidget::unsetLayoutDirection()
    self.uglySide.call('ritual_ZN7QWidget20unsetLayoutDirectionEv')

  def unsetLocale(self) -> None:
    """
    Calls Qt's 'void QWidget::unsetLocale()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#unsetLocale
    """
    #  void QWidget::unsetLocale()
    self.uglySide.call('ritual_ZN7QWidget11unsetLocaleEv')

  def activateWindow(self) -> None:
    """
    Calls Qt's 'void QWidget::activateWindow()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#activateWindow
    """
    #  void QWidget::activateWindow()
    self.uglySide.call('ritual_ZN7QWidget14activateWindowEv')

  def clearFocus(self) -> None:
    """
    Calls Qt's 'void QWidget::clearFocus()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#clearFocus
    """
    #  void QWidget::clearFocus()
    self.uglySide.call('ritual_ZN7QWidget10clearFocusEv')

  @overload()
  def grabMouse(self) -> None:
    """
    Calls Qt's 'void QWidget::grabMouse()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#grabMouse
    """
    #  void QWidget::grabMouse()
    self.uglySide.call('ritual_ZN7QWidget9grabMouseEv')

  @overload(QCursor)
  def grabMouse(self, a0: QCursor) -> None:
    """
    Calls Qt's 'void QWidget::grabMouse(const QCursor &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#grabMouse

    Parameters
    ----------

    a0 : QCursor
      Passed on as a value: Qt reads the C++ QCursor, which stays Python's
      own.
    """
    #  void QWidget::grabMouse(const QCursor &a0)
    self.uglySide.call(
        'ritual_ZN7QWidget9grabMouseERK7QCursor', self._valueOf(a0),
    )

  def releaseMouse(self) -> None:
    """
    Calls Qt's 'void QWidget::releaseMouse()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#releaseMouse
    """
    #  void QWidget::releaseMouse()
    self.uglySide.call('ritual_ZN7QWidget12releaseMouseEv')

  def grabKeyboard(self) -> None:
    """
    Calls Qt's 'void QWidget::grabKeyboard()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#grabKeyboard
    """
    #  void QWidget::grabKeyboard()
    self.uglySide.call('ritual_ZN7QWidget12grabKeyboardEv')

  def releaseKeyboard(self) -> None:
    """
    Calls Qt's 'void QWidget::releaseKeyboard()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#releaseKeyboard
    """
    #  void QWidget::releaseKeyboard()
    self.uglySide.call('ritual_ZN7QWidget15releaseKeyboardEv')

  @overload(QKeySequence)
  @overload(QKeySequence, Qt.ShortcutContext)
  def grabShortcut(
      self,
      key: QKeySequence,
      context: Qt.ShortcutContext = Qt.ShortcutContext.WindowShortcut,
  ) -> int:
    """
    Calls Qt's 'int QWidget::grabShortcut(const QKeySequence &key,
    Qt::ShortcutContext context)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#grabShortcut

    Parameters
    ----------

    key : QKeySequence
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own.

    context : Qt.ShortcutContext
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ShortcutContext.WindowShortcut.
    """
    #  int QWidget::grabShortcut(const QKeySequence &key, Qt::ShortcutContext
    #      context)
    return self.uglySide.call(
        'ritual_ZN7QWidget12grabShortcutERK12QKeySequenceN2Qt15ShortcutCont'
        'extE',
        self._valueOf(key), context.value,
    )

  @overload(int)
  def releaseShortcut(self, id: int) -> None:
    """
    Calls Qt's 'void QWidget::releaseShortcut(int id)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#releaseShortcut

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void QWidget::releaseShortcut(int id)
    self.uglySide.call('ritual_ZN7QWidget15releaseShortcutEi', id)

  @overload()
  def update(self) -> None:
    """
    Calls Qt's 'void QWidget::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#update
    """
    #  void QWidget::update()
    self.uglySide.call('ritual_ZN7QWidget6updateEv')

  @overload(int, int, int, int)
  def update(self, x: int, y: int, w: int, h: int) -> None:
    """
    Calls Qt's 'void QWidget::update(int x, int y, int w, int h)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#update

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.
    """
    #  void QWidget::update(int x, int y, int w, int h)
    self.uglySide.call('ritual_ZN7QWidget6updateEiiii', x, y, w, h)

  @overload(QRect)
  def update(self, a0: QRect) -> None:
    """
    Calls Qt's 'void QWidget::update(const QRect &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#update

    Parameters
    ----------

    a0 : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QWidget::update(const QRect &a0)
    self.uglySide.call(
        'ritual_ZN7QWidget6updateERK5QRect', self._valueOf(a0),
    )

  @overload(QRegion)
  def update(self, a0: QRegion) -> None:
    """
    Calls Qt's 'void QWidget::update(const QRegion &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#update

    Parameters
    ----------

    a0 : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QWidget::update(const QRegion &a0)
    self.uglySide.call(
        'ritual_ZN7QWidget6updateERK7QRegion', self._valueOf(a0),
    )

  @overload()
  def repaint(self) -> None:
    """
    Calls Qt's 'void QWidget::repaint()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#repaint
    """
    #  void QWidget::repaint()
    self.uglySide.call('ritual_ZN7QWidget7repaintEv')

  @overload(int, int, int, int)
  def repaint(self, x: int, y: int, w: int, h: int) -> None:
    """
    Calls Qt's 'void QWidget::repaint(int x, int y, int w, int h)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#repaint

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.
    """
    #  void QWidget::repaint(int x, int y, int w, int h)
    self.uglySide.call('ritual_ZN7QWidget7repaintEiiii', x, y, w, h)

  @overload(QRect)
  def repaint(self, a0: QRect) -> None:
    """
    Calls Qt's 'void QWidget::repaint(const QRect &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#repaint

    Parameters
    ----------

    a0 : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QWidget::repaint(const QRect &a0)
    self.uglySide.call(
        'ritual_ZN7QWidget7repaintERK5QRect', self._valueOf(a0),
    )

  @overload(QRegion)
  def repaint(self, a0: QRegion) -> None:
    """
    Calls Qt's 'void QWidget::repaint(const QRegion &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#repaint

    Parameters
    ----------

    a0 : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QWidget::repaint(const QRegion &a0)
    self.uglySide.call(
        'ritual_ZN7QWidget7repaintERK7QRegion', self._valueOf(a0),
    )

  def show(self) -> None:
    """
    Calls Qt's 'void QWidget::show()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#show
    """
    #  void QWidget::show()
    self.uglySide.call('ritual_ZN7QWidget4showEv')

  def hide(self) -> None:
    """
    Calls Qt's 'void QWidget::hide()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#hide
    """
    #  void QWidget::hide()
    self.uglySide.call('ritual_ZN7QWidget4hideEv')

  def showMinimized(self) -> None:
    """
    Calls Qt's 'void QWidget::showMinimized()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#showMinimized
    """
    #  void QWidget::showMinimized()
    self.uglySide.call('ritual_ZN7QWidget13showMinimizedEv')

  def showMaximized(self) -> None:
    """
    Calls Qt's 'void QWidget::showMaximized()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#showMaximized
    """
    #  void QWidget::showMaximized()
    self.uglySide.call('ritual_ZN7QWidget13showMaximizedEv')

  def showFullScreen(self) -> None:
    """
    Calls Qt's 'void QWidget::showFullScreen()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#showFullScreen
    """
    #  void QWidget::showFullScreen()
    self.uglySide.call('ritual_ZN7QWidget14showFullScreenEv')

  def showNormal(self) -> None:
    """
    Calls Qt's 'void QWidget::showNormal()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#showNormal
    """
    #  void QWidget::showNormal()
    self.uglySide.call('ritual_ZN7QWidget10showNormalEv')

  def close(self) -> bool:
    """
    Calls Qt's 'bool QWidget::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#close
    """
    #  bool QWidget::close()
    return self.uglySide.call('ritual_ZN7QWidget5closeEv')

  def raise_(self) -> None:
    """
    Calls Qt's 'void QWidget::raise()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#raise
    """
    #  void QWidget::raise()
    self.uglySide.call('ritual_ZN7QWidget5raiseEv')

  def lower(self) -> None:
    """
    Calls Qt's 'void QWidget::lower()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#lower
    """
    #  void QWidget::lower()
    self.uglySide.call('ritual_ZN7QWidget5lowerEv')

  @overload(THIS)
  @overload(NoneType)
  def stackUnder(self, a0: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QWidget::stackUnder(QWidget *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#stackUnder

    Parameters
    ----------

    a0 : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::stackUnder(QWidget *a0)
    self.uglySide.call(
        'ritual_ZN7QWidget10stackUnderEPS_', self._addressOf(a0),
    )

  @overload(int, int)
  def move(self, x: int, y: int) -> None:
    """
    Calls Qt's 'void QWidget::move(int x, int y)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#move

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QWidget::move(int x, int y)
    self.uglySide.call('ritual_ZN7QWidget4moveEii', x, y)

  @overload(QPoint)
  def move(self, a0: QPoint) -> None:
    """
    Calls Qt's 'void QWidget::move(const QPoint &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#move

    Parameters
    ----------

    a0 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QWidget::move(const QPoint &a0)
    self.uglySide.call('ritual_ZN7QWidget4moveERK6QPoint', self._valueOf(a0))

  @overload(int, int)
  def resize(self, w: int, h: int) -> None:
    """
    Calls Qt's 'void QWidget::resize(int w, int h)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#resize

    Parameters
    ----------

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.
    """
    #  void QWidget::resize(int w, int h)
    self.uglySide.call('ritual_ZN7QWidget6resizeEii', w, h)

  @overload(QSize)
  def resize(self, a0: QSize) -> None:
    """
    Calls Qt's 'void QWidget::resize(const QSize &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#resize

    Parameters
    ----------

    a0 : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QWidget::resize(const QSize &a0)
    self.uglySide.call(
        'ritual_ZN7QWidget6resizeERK5QSize', self._valueOf(a0),
    )

  @overload(QByteArray)
  def restoreGeometry(self, geometry: QByteArray) -> bool:
    """
    Calls Qt's 'bool QWidget::restoreGeometry(const QByteArray &geometry)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#restoreGeometry

    Parameters
    ----------

    geometry : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QWidget::restoreGeometry(const QByteArray &geometry)
    return self.uglySide.call(
        'ritual_ZN7QWidget15restoreGeometryERK10QByteArray',
        self._valueOf(geometry),
    )

  def adjustSize(self) -> None:
    """
    Calls Qt's 'void QWidget::adjustSize()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#adjustSize
    """
    #  void QWidget::adjustSize()
    self.uglySide.call('ritual_ZN7QWidget10adjustSizeEv')

  @overload(Qt.WindowStates)
  def overrideWindowState(self, state: Qt.WindowStates) -> None:
    """
    Calls Qt's 'void QWidget::overrideWindowState(Qt::WindowStates state)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#overrideWindowState

    Parameters
    ----------

    state : Qt.WindowStates
      Passed on as its number.
    """
    #  void QWidget::overrideWindowState(Qt::WindowStates state)
    self.uglySide.call(
        'ritual_ZN7QWidget19overrideWindowStateE6QFlagsIN2Qt11WindowStateEE',
        state.value,
    )

  def updateGeometry(self) -> None:
    """
    Calls Qt's 'void QWidget::updateGeometry()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#updateGeometry
    """
    #  void QWidget::updateGeometry()
    self.uglySide.call('ritual_ZN7QWidget14updateGeometryEv')

  @overload(int, int)
  def scroll(self, dx: int, dy: int) -> None:
    """
    Calls Qt's 'void QWidget::scroll(int dx, int dy)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#scroll

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.
    """
    #  void QWidget::scroll(int dx, int dy)
    self.uglySide.call('ritual_ZN7QWidget6scrollEii', dx, dy)

  @overload(int, int, QRect)
  def scroll(self, dx: int, dy: int, a2: QRect) -> None:
    """
    Calls Qt's 'void QWidget::scroll(int dx, int dy, const QRect &a2)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#scroll

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.

    a2 : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QWidget::scroll(int dx, int dy, const QRect &a2)
    self.uglySide.call(
        'ritual_ZN7QWidget6scrollEiiRK5QRect', dx, dy, self._valueOf(a2),
    )

  @overload(QAction)
  @overload(NoneType)
  def addAction(self, action: Optional[QAction]) -> None:
    """
    Calls Qt's 'void QWidget::addAction(QAction *action)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#addAction

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::addAction(QAction *action)
    self.uglySide.call(
        'ritual_ZN7QWidget9addActionEP7QAction', self._addressOf(action),
    )

  @overload(str)
  def addAction(self, text: str) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QWidget::addAction(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#addAction

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QWidget::addAction(const QString &text)
    address = self.uglySide.call(
        'ritual_ZN7QWidget9addActionERK7QString', text,
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(QIcon, str)
  def addAction(self, icon: QIcon, text: str) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QWidget::addAction(const QIcon &icon, const QString
    &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#addAction

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.

    text : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QWidget::addAction(const QIcon &icon, const QString &text)
    address = self.uglySide.call(
        'ritual_ZN7QWidget9addActionERK5QIconRK7QString',
        self._valueOf(icon), text,
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(str, QObject, str)
  @overload(str, QObject, NoneType)
  @overload(str, NoneType, str)
  @overload(str, NoneType, NoneType)
  @overload(str, QObject, str, Qt.ConnectionType)
  @overload(str, QObject, NoneType, Qt.ConnectionType)
  @overload(str, NoneType, str, Qt.ConnectionType)
  @overload(str, NoneType, NoneType, Qt.ConnectionType)
  def addAction(
      self,
      text: str,
      receiver: Optional[QObject],
      member: Optional[str],
      type: Qt.ConnectionType = Qt.ConnectionType.AutoConnection,
  ) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QWidget::addAction(const QString &text, const
    QObject *receiver, const char *member, Qt::ConnectionType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#addAction

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    type : Qt.ConnectionType
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ConnectionType.AutoConnection.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QWidget::addAction(const QString &text, const QObject
    #      *receiver, const char *member, Qt::ConnectionType type)
    address = self.uglySide.call(
        'ritual_ZN7QWidget9addActionERK7QStringPK7QObjectPKcN2Qt14Connectio'
        'nTypeE',
        text, self._addressOf(receiver), self._bytesOf(member), type.value,
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(QIcon, str, QObject, str)
  @overload(QIcon, str, QObject, NoneType)
  @overload(QIcon, str, NoneType, str)
  @overload(QIcon, str, NoneType, NoneType)
  @overload(QIcon, str, QObject, str, Qt.ConnectionType)
  @overload(QIcon, str, QObject, NoneType, Qt.ConnectionType)
  @overload(QIcon, str, NoneType, str, Qt.ConnectionType)
  @overload(QIcon, str, NoneType, NoneType, Qt.ConnectionType)
  def addAction(
      self,
      icon: QIcon,
      text: str,
      receiver: Optional[QObject],
      member: Optional[str],
      type: Qt.ConnectionType = Qt.ConnectionType.AutoConnection,
  ) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QWidget::addAction(const QIcon &icon, const QString
    &text, const QObject *receiver, const char *member, Qt::ConnectionType
    type)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#addAction

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.

    text : str
      Passed on as it is: a QString is made of it for the call.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    type : Qt.ConnectionType
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ConnectionType.AutoConnection.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QWidget::addAction(const QIcon &icon, const QString &text,
    #      const QObject *receiver, const char *member, Qt::ConnectionType
    #      type)
    address = self.uglySide.call(
        'ritual_ZN7QWidget9addActionERK5QIconRK7QStringPK7QObjectPKcN2Qt14C'
        'onnectionTypeE',
        self._valueOf(icon), text, self._addressOf(receiver),
        self._bytesOf(member), type.value,
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(str, QKeySequence)
  def addAction(
      self,
      text: str,
      shortcut: QKeySequence,
  ) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QWidget::addAction(const QString &text, const
    QKeySequence &shortcut)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#addAction

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    shortcut : QKeySequence
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QWidget::addAction(const QString &text, const QKeySequence
    #      &shortcut)
    address = self.uglySide.call(
        'ritual_ZN7QWidget9addActionERK7QStringRK12QKeySequence',
        text, self._valueOf(shortcut),
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(QIcon, str, QKeySequence)
  def addAction(
      self,
      icon: QIcon,
      text: str,
      shortcut: QKeySequence,
  ) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QWidget::addAction(const QIcon &icon, const QString
    &text, const QKeySequence &shortcut)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#addAction

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.

    text : str
      Passed on as it is: a QString is made of it for the call.

    shortcut : QKeySequence
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QWidget::addAction(const QIcon &icon, const QString &text,
    #      const QKeySequence &shortcut)
    address = self.uglySide.call(
        'ritual_ZN7QWidget9addActionERK5QIconRK7QStringRK12QKeySequence',
        self._valueOf(icon), text, self._valueOf(shortcut),
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(str, QKeySequence, QObject, str)
  @overload(str, QKeySequence, QObject, NoneType)
  @overload(str, QKeySequence, NoneType, str)
  @overload(str, QKeySequence, NoneType, NoneType)
  @overload(str, QKeySequence, QObject, str, Qt.ConnectionType)
  @overload(str, QKeySequence, QObject, NoneType, Qt.ConnectionType)
  @overload(str, QKeySequence, NoneType, str, Qt.ConnectionType)
  @overload(str, QKeySequence, NoneType, NoneType, Qt.ConnectionType)
  def addAction(
      self,
      text: str,
      shortcut: QKeySequence,
      receiver: Optional[QObject],
      member: Optional[str],
      type: Qt.ConnectionType = Qt.ConnectionType.AutoConnection,
  ) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QWidget::addAction(const QString &text, const
    QKeySequence &shortcut, const QObject *receiver, const char *member,
    Qt::ConnectionType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#addAction

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    shortcut : QKeySequence
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    type : Qt.ConnectionType
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ConnectionType.AutoConnection.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QWidget::addAction(const QString &text, const QKeySequence
    #      &shortcut, const QObject *receiver, const char *member,
    #      Qt::ConnectionType type)
    address = self.uglySide.call(
        'ritual_ZN7QWidget9addActionERK7QStringRK12QKeySequencePK7QObjectPK'
        'cN2Qt14ConnectionTypeE',
        text, self._valueOf(shortcut), self._addressOf(receiver),
        self._bytesOf(member), type.value,
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(QIcon, str, QKeySequence, QObject, str)
  @overload(QIcon, str, QKeySequence, QObject, NoneType)
  @overload(QIcon, str, QKeySequence, NoneType, str)
  @overload(QIcon, str, QKeySequence, NoneType, NoneType)
  @overload(QIcon, str, QKeySequence, QObject, str, Qt.ConnectionType)
  @overload(QIcon, str, QKeySequence, QObject, NoneType, Qt.ConnectionType)
  @overload(QIcon, str, QKeySequence, NoneType, str, Qt.ConnectionType)
  @overload(QIcon, str, QKeySequence, NoneType, NoneType, Qt.ConnectionType)
  def addAction(
      self,
      icon: QIcon,
      text: str,
      shortcut: QKeySequence,
      receiver: Optional[QObject],
      member: Optional[str],
      type: Qt.ConnectionType = Qt.ConnectionType.AutoConnection,
  ) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QWidget::addAction(const QIcon &icon, const QString
    &text, const QKeySequence &shortcut, const QObject *receiver, const char
    *member, Qt::ConnectionType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#addAction

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.

    text : str
      Passed on as it is: a QString is made of it for the call.

    shortcut : QKeySequence
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    type : Qt.ConnectionType
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ConnectionType.AutoConnection.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QWidget::addAction(const QIcon &icon, const QString &text,
    #      const QKeySequence &shortcut, const QObject *receiver, const char
    #      *member, Qt::ConnectionType type)
    address = self.uglySide.call(
        'ritual_ZN7QWidget9addActionERK5QIconRK7QStringRK12QKeySequencePK7Q'
        'ObjectPKcN2Qt14ConnectionTypeE',
        self._valueOf(icon), text, self._valueOf(shortcut),
        self._addressOf(receiver), self._bytesOf(member), type.value,
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(QList[QAction])
  def addActions(self, actions: QList[QAction]) -> None:
    """
    Calls Qt's 'void QWidget::addActions(const QList<QAction *> &actions)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#addActions

    Parameters
    ----------

    actions : QList[QAction]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QWidget::addActions(const QList<QAction *> &actions)
    self.uglySide.call(
        'ritual_ZN7QWidget10addActionsERK5QListIP7QActionE',
        self._valueOf(actions),
    )

  @overload(QAction, QList[QAction])
  @overload(NoneType, QList[QAction])
  def insertActions(
      self,
      before: Optional[QAction],
      actions: QList[QAction],
  ) -> None:
    """
    Calls Qt's 'void QWidget::insertActions(QAction *before, const
    QList<QAction *> &actions)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#insertActions

    Parameters
    ----------

    before : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    actions : QList[QAction]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QWidget::insertActions(QAction *before, const QList<QAction *>
    #      &actions)
    self.uglySide.call(
        'ritual_ZN7QWidget13insertActionsEP7QActionRK5QListIS1_E',
        self._addressOf(before), self._valueOf(actions),
    )

  @overload(QAction, QAction)
  @overload(QAction, NoneType)
  @overload(NoneType, QAction)
  @overload(NoneType, NoneType)
  def insertAction(
      self,
      before: Optional[QAction],
      action: Optional[QAction],
  ) -> None:
    """
    Calls Qt's 'void QWidget::insertAction(QAction *before, QAction
    *action)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#insertAction

    Parameters
    ----------

    before : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::insertAction(QAction *before, QAction *action)
    self.uglySide.call(
        'ritual_ZN7QWidget12insertActionEP7QActionS1_',
        self._addressOf(before), self._addressOf(action),
    )

  @overload(QAction)
  @overload(NoneType)
  def removeAction(self, action: Optional[QAction]) -> None:
    """
    Calls Qt's 'void QWidget::removeAction(QAction *action)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#removeAction

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::removeAction(QAction *action)
    self.uglySide.call(
        'ritual_ZN7QWidget12removeActionEP7QAction', self._addressOf(action),
    )

  @overload(Qt.WindowFlags)
  def overrideWindowFlags(self, type: Qt.WindowFlags) -> None:
    """
    Calls Qt's 'void QWidget::overrideWindowFlags(Qt::WindowFlags type)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#overrideWindowFlags

    Parameters
    ----------

    type : Qt.WindowFlags
      Passed on as its number.
    """
    #  void QWidget::overrideWindowFlags(Qt::WindowFlags type)
    self.uglySide.call(
        'ritual_ZN7QWidget19overrideWindowFlagsE6QFlagsIN2Qt10WindowTypeEE',
        type.value,
    )

  def ensurePolished(self) -> None:
    """
    Calls Qt's 'void QWidget::ensurePolished() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#ensurePolished
    """
    #  void QWidget::ensurePolished() const
    self.uglySide.call('ritual_ZNK7QWidget14ensurePolishedEv')

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QWidget::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWidget::event(QEvent *event)
    ritual = 'ritual_ZN7QWidget5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWidget5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QWidget::mousePressEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::mousePressEvent(QMouseEvent *event)
    ritual = 'ritual_ZN7QWidget15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWidget15mousePressEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QWidget::mouseReleaseEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::mouseReleaseEvent(QMouseEvent *event)
    ritual = 'ritual_ZN7QWidget17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWidget17mouseReleaseEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QWidget::mouseDoubleClickEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#mouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
    ritual = 'ritual_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QWidget::mouseMoveEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::mouseMoveEvent(QMouseEvent *event)
    ritual = 'ritual_ZN7QWidget14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWidget14mouseMoveEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, event: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void QWidget::wheelEvent(QWheelEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#wheelEvent

    Parameters
    ----------

    event : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::wheelEvent(QWheelEvent *event)
    ritual = 'ritual_ZN7QWidget10wheelEventEP11QWheelEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWidget10wheelEventEP11QWheelEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QWidget::keyPressEvent(QKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#keyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::keyPressEvent(QKeyEvent *event)
    ritual = 'ritual_ZN7QWidget13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWidget13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QWidget::keyReleaseEvent(QKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#keyReleaseEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::keyReleaseEvent(QKeyEvent *event)
    ritual = 'ritual_ZN7QWidget15keyReleaseEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWidget15keyReleaseEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QWidget::focusInEvent(QFocusEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#focusInEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::focusInEvent(QFocusEvent *event)
    ritual = 'ritual_ZN7QWidget12focusInEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWidget12focusInEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QWidget::focusOutEvent(QFocusEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#focusOutEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::focusOutEvent(QFocusEvent *event)
    ritual = 'ritual_ZN7QWidget13focusOutEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWidget13focusOutEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEnterEvent)
  @overload(NoneType)
  def enterEvent(self, event: Optional[QEnterEvent]) -> None:
    """
    Calls Qt's 'void QWidget::enterEvent(QEnterEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#enterEvent

    Parameters
    ----------

    event : Optional[QEnterEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::enterEvent(QEnterEvent *event)
    ritual = 'ritual_ZN7QWidget10enterEventEP11QEnterEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWidget10enterEventEP11QEnterEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def leaveEvent(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QWidget::leaveEvent(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#leaveEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::leaveEvent(QEvent *event)
    ritual = 'ritual_ZN7QWidget10leaveEventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWidget10leaveEventEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, event: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QWidget::paintEvent(QPaintEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#paintEvent

    Parameters
    ----------

    event : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::paintEvent(QPaintEvent *event)
    ritual = 'ritual_ZN7QWidget10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWidget10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMoveEvent)
  @overload(NoneType)
  def moveEvent(self, event: Optional[QMoveEvent]) -> None:
    """
    Calls Qt's 'void QWidget::moveEvent(QMoveEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#moveEvent

    Parameters
    ----------

    event : Optional[QMoveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::moveEvent(QMoveEvent *event)
    ritual = 'ritual_ZN7QWidget9moveEventEP10QMoveEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWidget9moveEventEP10QMoveEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, event: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QWidget::resizeEvent(QResizeEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#resizeEvent

    Parameters
    ----------

    event : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::resizeEvent(QResizeEvent *event)
    ritual = 'ritual_ZN7QWidget11resizeEventEP12QResizeEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWidget11resizeEventEP12QResizeEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QCloseEvent)
  @overload(NoneType)
  def closeEvent(self, event: Optional[QCloseEvent]) -> None:
    """
    Calls Qt's 'void QWidget::closeEvent(QCloseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#closeEvent

    Parameters
    ----------

    event : Optional[QCloseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::closeEvent(QCloseEvent *event)
    ritual = 'ritual_ZN7QWidget10closeEventEP11QCloseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWidget10closeEventEP11QCloseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QContextMenuEvent)
  @overload(NoneType)
  def contextMenuEvent(self, event: Optional[QContextMenuEvent]) -> None:
    """
    Calls Qt's 'void QWidget::contextMenuEvent(QContextMenuEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#contextMenuEvent

    Parameters
    ----------

    event : Optional[QContextMenuEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::contextMenuEvent(QContextMenuEvent *event)
    ritual = 'ritual_ZN7QWidget16contextMenuEventEP17QContextMenuEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWidget16contextMenuEventEP17QContextMenuEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QTabletEvent)
  @overload(NoneType)
  def tabletEvent(self, event: Optional[QTabletEvent]) -> None:
    """
    Calls Qt's 'void QWidget::tabletEvent(QTabletEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#tabletEvent

    Parameters
    ----------

    event : Optional[QTabletEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::tabletEvent(QTabletEvent *event)
    ritual = 'ritual_ZN7QWidget11tabletEventEP12QTabletEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWidget11tabletEventEP12QTabletEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QActionEvent)
  @overload(NoneType)
  def actionEvent(self, event: Optional[QActionEvent]) -> None:
    """
    Calls Qt's 'void QWidget::actionEvent(QActionEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#actionEvent

    Parameters
    ----------

    event : Optional[QActionEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::actionEvent(QActionEvent *event)
    ritual = 'ritual_ZN7QWidget11actionEventEP12QActionEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWidget11actionEventEP12QActionEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDragEnterEvent)
  @overload(NoneType)
  def dragEnterEvent(self, event: Optional[QDragEnterEvent]) -> None:
    """
    Calls Qt's 'void QWidget::dragEnterEvent(QDragEnterEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#dragEnterEvent

    Parameters
    ----------

    event : Optional[QDragEnterEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::dragEnterEvent(QDragEnterEvent *event)
    ritual = 'ritual_ZN7QWidget14dragEnterEventEP15QDragEnterEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWidget14dragEnterEventEP15QDragEnterEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDragMoveEvent)
  @overload(NoneType)
  def dragMoveEvent(self, event: Optional[QDragMoveEvent]) -> None:
    """
    Calls Qt's 'void QWidget::dragMoveEvent(QDragMoveEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#dragMoveEvent

    Parameters
    ----------

    event : Optional[QDragMoveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::dragMoveEvent(QDragMoveEvent *event)
    ritual = 'ritual_ZN7QWidget13dragMoveEventEP14QDragMoveEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWidget13dragMoveEventEP14QDragMoveEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDragLeaveEvent)
  @overload(NoneType)
  def dragLeaveEvent(self, event: Optional[QDragLeaveEvent]) -> None:
    """
    Calls Qt's 'void QWidget::dragLeaveEvent(QDragLeaveEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#dragLeaveEvent

    Parameters
    ----------

    event : Optional[QDragLeaveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
    ritual = 'ritual_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDropEvent)
  @overload(NoneType)
  def dropEvent(self, event: Optional[QDropEvent]) -> None:
    """
    Calls Qt's 'void QWidget::dropEvent(QDropEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#dropEvent

    Parameters
    ----------

    event : Optional[QDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::dropEvent(QDropEvent *event)
    ritual = 'ritual_ZN7QWidget9dropEventEP10QDropEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWidget9dropEventEP10QDropEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QShowEvent)
  @overload(NoneType)
  def showEvent(self, event: Optional[QShowEvent]) -> None:
    """
    Calls Qt's 'void QWidget::showEvent(QShowEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#showEvent

    Parameters
    ----------

    event : Optional[QShowEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::showEvent(QShowEvent *event)
    ritual = 'ritual_ZN7QWidget9showEventEP10QShowEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWidget9showEventEP10QShowEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHideEvent)
  @overload(NoneType)
  def hideEvent(self, event: Optional[QHideEvent]) -> None:
    """
    Calls Qt's 'void QWidget::hideEvent(QHideEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#hideEvent

    Parameters
    ----------

    event : Optional[QHideEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::hideEvent(QHideEvent *event)
    ritual = 'ritual_ZN7QWidget9hideEventEP10QHideEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWidget9hideEventEP10QHideEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def changeEvent(self, a0: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QWidget::changeEvent(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#changeEvent

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::changeEvent(QEvent *a0)
    ritual = 'ritual_ZN7QWidget11changeEventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWidget11changeEventEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QPainter)
  @overload(NoneType)
  def initPainter(self, painter: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QWidget::initPainter(QPainter *painter) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#initPainter

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::initPainter(QPainter *painter) const
    ritual = 'ritual_ZNK7QWidget11initPainterEP8QPainter'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QWidget11initPainterEP8QPainter'
    self.uglySide.call(ritual, self._addressOf(painter))

  @overload(QInputMethodEvent)
  @overload(NoneType)
  def inputMethodEvent(self, a0: Optional[QInputMethodEvent]) -> None:
    """
    Calls Qt's 'void QWidget::inputMethodEvent(QInputMethodEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#inputMethodEvent

    Parameters
    ----------

    a0 : Optional[QInputMethodEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
    ritual = 'ritual_ZN7QWidget16inputMethodEventEP17QInputMethodEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWidget16inputMethodEventEP17QInputMethodEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload()
  @overload(Qt.InputMethodQuery)
  def updateMicroFocus(
      self,
      query: Qt.InputMethodQuery = Qt.InputMethodQuery.ImQueryAll,
  ) -> None:
    """
    Calls Qt's 'void QWidget::updateMicroFocus(Qt::InputMethodQuery query)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#updateMicroFocus

    Parameters
    ----------

    query : Qt.InputMethodQuery
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.InputMethodQuery.ImQueryAll.
    """
    #  void QWidget::updateMicroFocus(Qt::InputMethodQuery query)
    self.uglySide.call(
        'ritual_ZN7QWidget16updateMicroFocusEN2Qt16InputMethodQueryE',
        query.value,
    )

  @overload()
  @overload(int)
  @overload(int, bool)
  @overload(int, bool, bool)
  def create(
      self,
      a0: int = 0,
      initializeWindow: bool = True,
      destroyOldWindow: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QWidget::create(WId a0, bool initializeWindow, bool
    destroyOldWindow)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#create

    Parameters
    ----------

    a0 : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    initializeWindow : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    destroyOldWindow : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QWidget::create(WId a0, bool initializeWindow, bool
    #      destroyOldWindow)
    self.uglySide.call(
        'ritual_ZN7QWidget6createEybb',
        a0, initializeWindow, destroyOldWindow,
    )

  @overload()
  @overload(bool)
  @overload(bool, bool)
  def destroy(
      self,
      destroyWindow: bool = True,
      destroySubWindows: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QWidget::destroy(bool destroyWindow, bool
    destroySubWindows)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#destroy

    Parameters
    ----------

    destroyWindow : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    destroySubWindows : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QWidget::destroy(bool destroyWindow, bool destroySubWindows)
    self.uglySide.call(
        'ritual_ZN7QWidget7destroyEbb', destroyWindow, destroySubWindows,
    )

  @overload(bool)
  def focusNextPrevChild(self, next: bool) -> bool:
    """
    Calls Qt's 'bool QWidget::focusNextPrevChild(bool next)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#focusNextPrevChild

    Parameters
    ----------

    next : bool
      Passed on as it is.
    """
    #  bool QWidget::focusNextPrevChild(bool next)
    ritual = 'ritual_ZN7QWidget18focusNextPrevChildEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QWidget18focusNextPrevChildEb'
    return self.uglySide.call(ritual, next)

  def focusNextChild(self) -> bool:
    """
    Calls Qt's 'bool QWidget::focusNextChild()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#focusNextChild
    """
    #  bool QWidget::focusNextChild()
    return self.uglySide.call('ritual_ZN7QWidget14focusNextChildEv')

  def focusPreviousChild(self) -> bool:
    """
    Calls Qt's 'bool QWidget::focusPreviousChild()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#focusPreviousChild
    """
    #  bool QWidget::focusPreviousChild()
    return self.uglySide.call('ritual_ZN7QWidget18focusPreviousChildEv')

  def takeLayout(self) -> Optional[QLayout]:
    """
    Calls Qt's 'QLayout *QWidget::takeLayout()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#takeLayout

    Returns
    -------

    Optional[QLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayout *QWidget::takeLayout()
    address = self.uglySide.call('ritual_ZN7QWidget10takeLayoutEv')
    from . import QLayout
    return QLayout._cuteAt(address)


#  Qt's 'QList<QWidget *>': the list of QWidget, which 'QList[QWidget]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QWidget. Qt has a name of its own for it.
QWidgetList = QList.createKind(
    QWidget, 'address',
    name='QWidgetList',
    make='ritual_list_make_QWidget_ptr',
    add='ritual_list_add_QWidget_ptr',
    size='ritual_list_size_QWidget_ptr',
    at='ritual_list_at_QWidget_ptr',
    drop='ritual_list_drop_QWidget_ptr',
)
