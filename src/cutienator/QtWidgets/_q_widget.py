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

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QAction
from ..QtGui import QBitmap
from ..QtCore import QByteArray
from ..QtGui import QCursor
from ..QtGui import QFont
from ..QtGui import QFontMetrics
from ..QtGui import QIcon
from ..QtGui import QKeySequence
from ..QtCore import QLocale
from ..QtCore import QMargins
from ..QtCore import QMetaObject
from ..QtCore import QObject
from ..QtGui import QPaintDevice
from ..QtGui import QPainter
from ..QtGui import QPalette
from ..QtGui import QPixmap
from ..QtCore import QPoint
from ..QtCore import QPointF
from ..QtCore import QRect
from ..QtGui import QRegion
from ..QtGui import QScreen
from ..QtCore import QSize
from ._q_size_policy import QSizePolicy
from ..QtCore import QVariant
from ..QtGui import QWindow
from ._q_widget_render_flag import RenderFlag

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWidget(QObject):
  """
  The cute side of Qt's QWidget: a plain Python object standing in front of
  one C++ QWidget.

  It is built on the cute 'QObject', as Qt's QWidget is built on Qt's
  QObject, and has everything that class has. Qt's QWidget is built on Qt's
  QPaintDevice as well, which is not reflected.

  What exists
  -----------

  Every function of Qt's QWidget that has a ritual and that Python can call
  so far, 218 names in all: 'metaObject', 'tr', 'devType', 'winId',
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
  'foregroundRole', 'font', 'setFont', 'fontMetrics', 'cursor', 'setCursor',
  'unsetCursor', 'setMouseTracking', 'hasMouseTracking', 'underMouse',
  'setTabletTracking', 'hasTabletTracking', 'setMask', 'mask', 'clearMask',
  'render', 'grab', 'grabGesture', 'ungrabGesture', 'setWindowTitle',
  'setStyleSheet', 'styleSheet', 'windowTitle', 'setWindowIcon',
  'windowIcon', 'setWindowIconText', 'windowIconText', 'setWindowRole',
  'windowRole', 'setWindowFilePath', 'windowFilePath', 'setWindowOpacity',
  'windowOpacity', 'isWindowModified', 'setToolTip', 'toolTip',
  'setToolTipDuration', 'toolTipDuration', 'setStatusTip', 'statusTip',
  'setWhatsThis', 'whatsThis', 'accessibleName', 'setAccessibleName',
  'accessibleDescription', 'setAccessibleDescription',
  'accessibleIdentifier', 'setAccessibleIdentifier', 'setLayoutDirection',
  'layoutDirection', 'unsetLayoutDirection', 'setLocale', 'locale',
  'unsetLocale', 'isRightToLeft', 'isLeftToRight', 'setFocus',
  'isActiveWindow', 'activateWindow', 'clearFocus', 'focusPolicy',
  'setFocusPolicy', 'hasFocus', 'setTabOrder', 'setFocusProxy', 'focusProxy',
  'contextMenuPolicy', 'setContextMenuPolicy', 'grabMouse', 'releaseMouse',
  'grabKeyboard', 'releaseKeyboard', 'grabShortcut', 'releaseShortcut',
  'setShortcutEnabled', 'setShortcutAutoRepeat', 'mouseGrabber',
  'keyboardGrabber', 'updatesEnabled', 'setUpdatesEnabled', 'update',
  'repaint', 'setVisible', 'setHidden', 'show', 'hide', 'showMinimized',
  'showMaximized', 'showFullScreen', 'showNormal', 'close', 'raise_',
  'lower', 'stackUnder', 'move', 'resize', 'setGeometry', 'saveGeometry',
  'restoreGeometry', 'adjustSize', 'isVisible', 'isVisibleTo', 'isHidden',
  'isMinimized', 'isMaximized', 'isFullScreen', 'windowState',
  'setWindowState', 'overrideWindowState', 'sizeHint', 'minimumSizeHint',
  'sizePolicy', 'setSizePolicy', 'heightForWidth', 'hasHeightForWidth',
  'visibleRegion', 'setContentsMargins', 'contentsMargins', 'contentsRect',
  'layout', 'setLayout', 'updateGeometry', 'setParent', 'scroll',
  'focusWidget', 'nextInFocusChain', 'previousInFocusChain', 'acceptDrops',
  'setAcceptDrops', 'addAction', 'insertAction', 'removeAction',
  'parentWidget', 'setWindowFlags', 'windowFlags', 'setWindowFlag',
  'overrideWindowFlags', 'windowType', 'find', 'childAt', 'setAttribute',
  'testAttribute', 'ensurePolished', 'isAncestorOf', 'autoFillBackground',
  'setAutoFillBackground', 'windowHandle', 'screen', 'setScreen',
  'createWindowContainer', 'inputMethodQuery', 'inputMethodHints',
  'setInputMethodHints'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWidget::~QWidget()': the destructor: Python never removes a C++
    QWidget.
  - Qt's 'QFontInfo QWidget::fontInfo() const': gives 'QFontInfo', which has
    no cute class yet.
  - Qt's 'QGraphicsEffect *QWidget::graphicsEffect() const': gives
    'QGraphicsEffect', which has no cute class yet.
  - Qt's 'void QWidget::setGraphicsEffect(QGraphicsEffect *effect)': names
    'QGraphicsEffect', which has no cute class yet.
  - Qt's 'QGraphicsProxyWidget *QWidget::graphicsProxyWidget() const': gives
    'QGraphicsProxyWidget', which has no cute class yet.
  - Qt's 'QPaintEngine *QWidget::paintEngine() const': gives 'QPaintEngine',
    which has no cute class yet.
  - Qt's 'QBackingStore *QWidget::backingStore() const': gives
    'QBackingStore', which has no cute class yet.

  What has no ritual
  ------------------

  62 of the 326 functions Qt declares: 39 protected; 6 takes or gives a type
  that cannot be passed yet; 6 private; 5 a template; 4 a signal; 2
  forbidden.

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

  #  The enums Qt writes inside QWidget, and the names Qt has for the
  #  combinations of its flags enums.
  RenderFlag = RenderFlag
  RenderFlags = RenderFlag

  #  The cute classes made after this one that its functions take or give;
  #  see 'WAIT'.
  QLayout = WAIT['QLayout']
  QStyle = WAIT['QStyle']

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
    return QMetaObject._cuteAt(address)

  def devType(self) -> int:
    """
    Calls Qt's 'int QWidget::devType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#devType
    """
    #  int QWidget::devType() const
    return self.uglySide.call('ritual_ZNK7QWidget7devTypeEv')

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
    return self.QStyle._cuteAt(address)

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
    return QFontMetrics._cuteOwning(address)

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
    return QRegion._cuteOwning(address)

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
    address = self.uglySide.call('ritual_ZNK7QWidget8sizeHintEv')
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
    address = self.uglySide.call('ritual_ZNK7QWidget15minimumSizeHintEv')
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
    return self.uglySide.call('ritual_ZNK7QWidget14heightForWidthEi', a0)

  def hasHeightForWidth(self) -> bool:
    """
    Calls Qt's 'bool QWidget::hasHeightForWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#hasHeightForWidth
    """
    #  bool QWidget::hasHeightForWidth() const
    return self.uglySide.call('ritual_ZNK7QWidget17hasHeightForWidthEv')

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
    return self.QLayout._cuteAt(address)

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
    return QScreen._cuteAt(address)

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
    address = self.uglySide.call(
        'ritual_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE',
        a0.value,
    )
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStyle)
  def setStyle(self, a0: QStyle) -> None:
    """
    Calls Qt's 'void QWidget::setStyle(QStyle *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setStyle

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    a0 : QStyle
      Passed on as the address of its C++ object.
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
    self.uglySide.call('ritual_ZN7QWidget10setVisibleEb', visible)

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
  def setLayout(self, a0: QLayout) -> None:
    """
    Calls Qt's 'void QWidget::setLayout(QLayout *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#setLayout

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    a0 : QLayout
      Passed on as the address of its C++ object.
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

  @overload(QPaintDevice, QPoint, QRegion, RenderFlags)
  @overload(NoneType, QPoint, QRegion, RenderFlags)
  def render(
      self,
      target: Optional[QPaintDevice],
      targetOffset: QPoint,
      sourceRegion: QRegion,
      renderFlags: RenderFlags,
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

    targetOffset : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    sourceRegion : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.

    renderFlags : RenderFlags
      Passed on as its number.
    """
    #  void QWidget::render(QPaintDevice *target, const QPoint &targetOffset,
    #      const QRegion &sourceRegion, RenderFlags renderFlags)
    self.uglySide.call(
        'ritual_ZN7QWidget6renderEP12QPaintDeviceRK6QPointRK7QRegion6QFlags'
        'INS_10RenderFlagEE',
        self._addressOf(target), self._valueOf(targetOffset),
        self._valueOf(sourceRegion), renderFlags.value,
    )

  @overload(QPainter, QPoint, QRegion, RenderFlags)
  def render(
      self,
      painter: Optional[QPainter],
      targetOffset: QPoint,
      sourceRegion: QRegion,
      renderFlags: RenderFlags,
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

    targetOffset : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    sourceRegion : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.

    renderFlags : RenderFlags
      Passed on as its number.
    """
    #  void QWidget::render(QPainter *painter, const QPoint &targetOffset,
    #      const QRegion &sourceRegion, RenderFlags renderFlags)
    self.uglySide.call(
        'ritual_ZN7QWidget6renderEP8QPainterRK6QPointRK7QRegion6QFlagsINS_1'
        '0RenderFlagEE',
        self._addressOf(painter), self._valueOf(targetOffset),
        self._valueOf(sourceRegion), renderFlags.value,
    )

  @overload(QRect)
  def grab(self, rectangle: QRect) -> QPixmap:
    """
    Calls Qt's 'QPixmap QWidget::grab(const QRect &rectangle)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidget.html#grab

    Parameters
    ----------

    rectangle : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QWidget::grab(const QRect &rectangle)
    address = self.uglySide.call(
        'ritual_ZN7QWidget4grabERK5QRect', self._valueOf(rectangle),
    )
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
    return QAction._cuteAt(address)

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
