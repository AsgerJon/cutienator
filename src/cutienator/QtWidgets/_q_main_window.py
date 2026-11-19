"""
QMainWindow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qmainwindow.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import Qt
from ..QtCore import QByteArray
from ._q_dock_widget import QDockWidget
from ._q_menu import QMenu
from ._q_menu_bar import QMenuBar
from ..QtCore import QMetaObject
from ..QtCore import QPoint
from ..QtCore import QSize
from ._q_status_bar import QStatusBar
from ._q_tab_widget import QTabWidget
from ._q_tool_bar import QToolBar
from ._q_widget import QWidget
from ._q_main_window_dock_option import DockOption

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMainWindow(QWidget):
  """
  The cute side of Qt's QMainWindow: a plain Python object standing in front
  of one C++ QMainWindow.

  It is built on the cute 'QWidget', as Qt's QMainWindow is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMainWindow that has a ritual and that Python can
  call so far, 49 names in all: 'metaObject', 'tr', 'iconSize',
  'setIconSize', 'toolButtonStyle', 'setToolButtonStyle', 'isAnimated',
  'isDockNestingEnabled', 'documentMode', 'setDocumentMode', 'tabShape',
  'setTabShape', 'tabPosition', 'setTabPosition', 'setDockOptions',
  'dockOptions', 'isSeparator', 'menuBar', 'setMenuBar', 'menuWidget',
  'setMenuWidget', 'statusBar', 'setStatusBar', 'centralWidget',
  'setCentralWidget', 'takeCentralWidget', 'setCorner', 'corner',
  'addToolBarBreak', 'insertToolBarBreak', 'addToolBar', 'insertToolBar',
  'removeToolBar', 'removeToolBarBreak', 'unifiedTitleAndToolBarOnMac',
  'toolBarArea', 'toolBarBreak', 'addDockWidget', 'splitDockWidget',
  'tabifyDockWidget', 'removeDockWidget', 'restoreDockWidget',
  'dockWidgetArea', 'saveState', 'restoreState', 'createPopupMenu',
  'setAnimated', 'setDockNestingEnabled', 'setUnifiedTitleAndToolBarOnMac'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMainWindow::~QMainWindow()': the destructor: Python never removes
    a C++ QMainWindow.

  What has no ritual
  ------------------

  15 of the 69 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 3 private; 3 a signal; 2 protected; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QMainWindow is created at the first use, not by
    'QMainWindow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMainWindow.
  - Qt tells when it has removed the C++ QMainWindow. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QMainWindow, and the names Qt has for the
  #  combinations of its flags enums.
  DockOption = DockOption
  DockOptions = DockOption

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
    Calls Qt's 'QString QMainWindow::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#tr

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
    #  QString QMainWindow::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QMainWindow2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMainWindow'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QMainWindow::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QMainWindow::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QMainWindow10metaObjectEv')
    return QMetaObject._cuteAt(address)

  def iconSize(self) -> QSize:
    """
    Calls Qt's 'QSize QMainWindow::iconSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#iconSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QMainWindow::iconSize() const
    address = self.uglySide.call('ritual_ZNK11QMainWindow8iconSizeEv')
    return QSize._cuteOwning(address)

  def toolButtonStyle(self) -> Qt.ToolButtonStyle:
    """
    Calls Qt's 'Qt::ToolButtonStyle QMainWindow::toolButtonStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#toolButtonStyle

    Returns
    -------

    Qt.ToolButtonStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.ToolButtonStyle(number)' gives.
    """
    #  Qt::ToolButtonStyle QMainWindow::toolButtonStyle() const
    return Qt.ToolButtonStyle(self.uglySide.call(
        'ritual_ZNK11QMainWindow15toolButtonStyleEv',
    ))

  def isAnimated(self) -> bool:
    """
    Calls Qt's 'bool QMainWindow::isAnimated() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#isAnimated
    """
    #  bool QMainWindow::isAnimated() const
    return self.uglySide.call('ritual_ZNK11QMainWindow10isAnimatedEv')

  def isDockNestingEnabled(self) -> bool:
    """
    Calls Qt's 'bool QMainWindow::isDockNestingEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmainwindow.html#isDockNestingEnabled
    """
    #  bool QMainWindow::isDockNestingEnabled() const
    return self.uglySide.call(
        'ritual_ZNK11QMainWindow20isDockNestingEnabledEv',
    )

  def documentMode(self) -> bool:
    """
    Calls Qt's 'bool QMainWindow::documentMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#documentMode
    """
    #  bool QMainWindow::documentMode() const
    return self.uglySide.call('ritual_ZNK11QMainWindow12documentModeEv')

  def tabShape(self) -> QTabWidget.TabShape:
    """
    Calls Qt's 'QTabWidget::TabShape QMainWindow::tabShape() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#tabShape

    Returns
    -------

    QTabWidget.TabShape
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QTabWidget.TabShape(number)' gives.
    """
    #  QTabWidget::TabShape QMainWindow::tabShape() const
    return QTabWidget.TabShape(self.uglySide.call(
        'ritual_ZNK11QMainWindow8tabShapeEv',
    ))

  @overload(Qt.DockWidgetArea)
  def tabPosition(self, area: Qt.DockWidgetArea) -> QTabWidget.TabPosition:
    """
    Calls Qt's 'QTabWidget::TabPosition
    QMainWindow::tabPosition(Qt::DockWidgetArea area) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#tabPosition

    Parameters
    ----------

    area : Qt.DockWidgetArea
      Passed on as its number.

    Returns
    -------

    QTabWidget.TabPosition
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QTabWidget.TabPosition(number)' gives.
    """
    #  QTabWidget::TabPosition QMainWindow::tabPosition(Qt::DockWidgetArea
    #      area) const
    return QTabWidget.TabPosition(self.uglySide.call(
        'ritual_ZNK11QMainWindow11tabPositionEN2Qt14DockWidgetAreaE',
        area.value,
    ))

  def dockOptions(self) -> DockOptions:
    """
    Calls Qt's 'DockOptions QMainWindow::dockOptions() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#dockOptions

    Returns
    -------

    DockOptions
      The value standing for the combination Qt gave back.
    """
    #  DockOptions QMainWindow::dockOptions() const
    return QMainWindow.DockOptions(self.uglySide.call(
        'ritual_ZNK11QMainWindow11dockOptionsEv',
    ))

  @overload(QPoint)
  def isSeparator(self, pos: QPoint) -> bool:
    """
    Calls Qt's 'bool QMainWindow::isSeparator(const QPoint &pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#isSeparator

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  bool QMainWindow::isSeparator(const QPoint &pos) const
    return self.uglySide.call(
        'ritual_ZNK11QMainWindow11isSeparatorERK6QPoint', self._valueOf(pos),
    )

  def menuBar(self) -> Optional[QMenuBar]:
    """
    Calls Qt's 'QMenuBar *QMainWindow::menuBar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#menuBar

    Returns
    -------

    Optional[QMenuBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenuBar *QMainWindow::menuBar() const
    address = self.uglySide.call('ritual_ZNK11QMainWindow7menuBarEv')
    return QMenuBar._cuteAt(address)

  def menuWidget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QMainWindow::menuWidget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#menuWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QMainWindow::menuWidget() const
    address = self.uglySide.call('ritual_ZNK11QMainWindow10menuWidgetEv')
    return QWidget._cuteAt(address)

  def statusBar(self) -> Optional[QStatusBar]:
    """
    Calls Qt's 'QStatusBar *QMainWindow::statusBar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#statusBar

    Returns
    -------

    Optional[QStatusBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStatusBar *QMainWindow::statusBar() const
    address = self.uglySide.call('ritual_ZNK11QMainWindow9statusBarEv')
    return QStatusBar._cuteAt(address)

  def centralWidget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QMainWindow::centralWidget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#centralWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QMainWindow::centralWidget() const
    address = self.uglySide.call('ritual_ZNK11QMainWindow13centralWidgetEv')
    return QWidget._cuteAt(address)

  @overload(Qt.Corner)
  def corner(self, corner: Qt.Corner) -> Qt.DockWidgetArea:
    """
    Calls Qt's 'Qt::DockWidgetArea QMainWindow::corner(Qt::Corner corner)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#corner

    Parameters
    ----------

    corner : Qt.Corner
      Passed on as its number.

    Returns
    -------

    Qt.DockWidgetArea
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.DockWidgetArea(number)' gives.
    """
    #  Qt::DockWidgetArea QMainWindow::corner(Qt::Corner corner) const
    return Qt.DockWidgetArea(self.uglySide.call(
        'ritual_ZNK11QMainWindow6cornerEN2Qt6CornerE', corner.value,
    ))

  def unifiedTitleAndToolBarOnMac(self) -> bool:
    """
    Calls Qt's 'bool QMainWindow::unifiedTitleAndToolBarOnMac() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmainwindow.html#unifiedTitleAndToolBarOnMac
    """
    #  bool QMainWindow::unifiedTitleAndToolBarOnMac() const
    return self.uglySide.call(
        'ritual_ZNK11QMainWindow27unifiedTitleAndToolBarOnMacEv',
    )

  @overload(QToolBar)
  @overload(NoneType)
  def toolBarArea(self, toolbar: Optional[QToolBar]) -> Qt.ToolBarArea:
    """
    Calls Qt's 'Qt::ToolBarArea QMainWindow::toolBarArea(const QToolBar
    *toolbar) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#toolBarArea

    Parameters
    ----------

    toolbar : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Qt.ToolBarArea
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.ToolBarArea(number)'
      gives.
    """
    #  Qt::ToolBarArea QMainWindow::toolBarArea(const QToolBar *toolbar)
    #      const
    return Qt.ToolBarArea(self.uglySide.call(
        'ritual_ZNK11QMainWindow11toolBarAreaEPK8QToolBar',
        self._addressOf(toolbar),
    ))

  @overload(QToolBar)
  @overload(NoneType)
  def toolBarBreak(self, toolbar: Optional[QToolBar]) -> bool:
    """
    Calls Qt's 'bool QMainWindow::toolBarBreak(QToolBar *toolbar) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#toolBarBreak

    Parameters
    ----------

    toolbar : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QMainWindow::toolBarBreak(QToolBar *toolbar) const
    return self.uglySide.call(
        'ritual_ZNK11QMainWindow12toolBarBreakEP8QToolBar',
        self._addressOf(toolbar),
    )

  @overload(QDockWidget)
  @overload(NoneType)
  def dockWidgetArea(
      self,
      dockwidget: Optional[QDockWidget],
  ) -> Qt.DockWidgetArea:
    """
    Calls Qt's 'Qt::DockWidgetArea QMainWindow::dockWidgetArea(QDockWidget
    *dockwidget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#dockWidgetArea

    Parameters
    ----------

    dockwidget : Optional[QDockWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Qt.DockWidgetArea
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.DockWidgetArea(number)' gives.
    """
    #  Qt::DockWidgetArea QMainWindow::dockWidgetArea(QDockWidget
    #      *dockwidget) const
    return Qt.DockWidgetArea(self.uglySide.call(
        'ritual_ZNK11QMainWindow14dockWidgetAreaEP11QDockWidget',
        self._addressOf(dockwidget),
    ))

  @overload()
  @overload(int)
  def saveState(self, version: int = 0) -> QByteArray:
    """
    Calls Qt's 'QByteArray QMainWindow::saveState(int version) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#saveState

    Parameters
    ----------

    version : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMainWindow::saveState(int version) const
    address = self.uglySide.call(
        'ritual_ZNK11QMainWindow9saveStateEi', version,
    )
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSize)
  def setIconSize(self, iconSize: QSize) -> None:
    """
    Calls Qt's 'void QMainWindow::setIconSize(const QSize &iconSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#setIconSize

    Parameters
    ----------

    iconSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QMainWindow::setIconSize(const QSize &iconSize)
    self.uglySide.call(
        'ritual_ZN11QMainWindow11setIconSizeERK5QSize',
        self._valueOf(iconSize),
    )

  @overload(Qt.ToolButtonStyle)
  def setToolButtonStyle(self, toolButtonStyle: Qt.ToolButtonStyle) -> None:
    """
    Calls Qt's 'void QMainWindow::setToolButtonStyle(Qt::ToolButtonStyle
    toolButtonStyle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmainwindow.html#setToolButtonStyle

    Parameters
    ----------

    toolButtonStyle : Qt.ToolButtonStyle
      Passed on as its number.
    """
    #  void QMainWindow::setToolButtonStyle(Qt::ToolButtonStyle
    #      toolButtonStyle)
    self.uglySide.call(
        'ritual_ZN11QMainWindow18setToolButtonStyleEN2Qt15ToolButtonStyleE',
        toolButtonStyle.value,
    )

  @overload(bool)
  def setDocumentMode(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QMainWindow::setDocumentMode(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#setDocumentMode

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QMainWindow::setDocumentMode(bool enabled)
    self.uglySide.call('ritual_ZN11QMainWindow15setDocumentModeEb', enabled)

  @overload(QTabWidget.TabShape)
  def setTabShape(self, tabShape: QTabWidget.TabShape) -> None:
    """
    Calls Qt's 'void QMainWindow::setTabShape(QTabWidget::TabShape
    tabShape)'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#setTabShape

    Parameters
    ----------

    tabShape : QTabWidget.TabShape
      Passed on as its number.
    """
    #  void QMainWindow::setTabShape(QTabWidget::TabShape tabShape)
    self.uglySide.call(
        'ritual_ZN11QMainWindow11setTabShapeEN10QTabWidget8TabShapeE',
        tabShape.value,
    )

  @overload(Qt.DockWidgetAreas, QTabWidget.TabPosition)
  def setTabPosition(
      self,
      areas: Qt.DockWidgetAreas,
      tabPosition: QTabWidget.TabPosition,
  ) -> None:
    """
    Calls Qt's 'void QMainWindow::setTabPosition(Qt::DockWidgetAreas areas,
    QTabWidget::TabPosition tabPosition)'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#setTabPosition

    Parameters
    ----------

    areas : Qt.DockWidgetAreas
      Passed on as its number.

    tabPosition : QTabWidget.TabPosition
      Passed on as its number.
    """
    #  void QMainWindow::setTabPosition(Qt::DockWidgetAreas areas,
    #      QTabWidget::TabPosition tabPosition)
    self.uglySide.call(
        'ritual_ZN11QMainWindow14setTabPositionE6QFlagsIN2Qt14DockWidgetAre'
        'aEEN10QTabWidget11TabPositionE',
        areas.value, tabPosition.value,
    )

  @overload(DockOptions)
  def setDockOptions(self, options: DockOptions) -> None:
    """
    Calls Qt's 'void QMainWindow::setDockOptions(DockOptions options)'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#setDockOptions

    Parameters
    ----------

    options : DockOptions
      Passed on as its number.
    """
    #  void QMainWindow::setDockOptions(DockOptions options)
    self.uglySide.call(
        'ritual_ZN11QMainWindow14setDockOptionsE6QFlagsINS_10DockOptionEE',
        options.value,
    )

  @overload(QMenuBar)
  @overload(NoneType)
  def setMenuBar(self, menubar: Optional[QMenuBar]) -> None:
    """
    Calls Qt's 'void QMainWindow::setMenuBar(QMenuBar *menubar)'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#setMenuBar

    Parameters
    ----------

    menubar : Optional[QMenuBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMainWindow::setMenuBar(QMenuBar *menubar)
    self.uglySide.call(
        'ritual_ZN11QMainWindow10setMenuBarEP8QMenuBar',
        self._addressOf(menubar),
    )

  @overload(QWidget)
  @overload(NoneType)
  def setMenuWidget(self, menubar: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QMainWindow::setMenuWidget(QWidget *menubar)'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#setMenuWidget

    Parameters
    ----------

    menubar : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMainWindow::setMenuWidget(QWidget *menubar)
    self.uglySide.call(
        'ritual_ZN11QMainWindow13setMenuWidgetEP7QWidget',
        self._addressOf(menubar),
    )

  @overload(QStatusBar)
  @overload(NoneType)
  def setStatusBar(self, statusbar: Optional[QStatusBar]) -> None:
    """
    Calls Qt's 'void QMainWindow::setStatusBar(QStatusBar *statusbar)'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#setStatusBar

    Parameters
    ----------

    statusbar : Optional[QStatusBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMainWindow::setStatusBar(QStatusBar *statusbar)
    self.uglySide.call(
        'ritual_ZN11QMainWindow12setStatusBarEP10QStatusBar',
        self._addressOf(statusbar),
    )

  @overload(QWidget)
  @overload(NoneType)
  def setCentralWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QMainWindow::setCentralWidget(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#setCentralWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMainWindow::setCentralWidget(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN11QMainWindow16setCentralWidgetEP7QWidget',
        self._addressOf(widget),
    )

  @overload(Qt.Corner, Qt.DockWidgetArea)
  def setCorner(self, corner: Qt.Corner, area: Qt.DockWidgetArea) -> None:
    """
    Calls Qt's 'void QMainWindow::setCorner(Qt::Corner corner,
    Qt::DockWidgetArea area)'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#setCorner

    Parameters
    ----------

    corner : Qt.Corner
      Passed on as its number.

    area : Qt.DockWidgetArea
      Passed on as its number.
    """
    #  void QMainWindow::setCorner(Qt::Corner corner, Qt::DockWidgetArea
    #      area)
    self.uglySide.call(
        'ritual_ZN11QMainWindow9setCornerEN2Qt6CornerENS0_14DockWidgetAreaE',
        corner.value, area.value,
    )

  @overload(bool)
  def setAnimated(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QMainWindow::setAnimated(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#setAnimated

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QMainWindow::setAnimated(bool enabled)
    self.uglySide.call('ritual_ZN11QMainWindow11setAnimatedEb', enabled)

  @overload(bool)
  def setDockNestingEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QMainWindow::setDockNestingEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmainwindow.html#setDockNestingEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QMainWindow::setDockNestingEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN11QMainWindow21setDockNestingEnabledEb', enabled,
    )

  @overload(bool)
  def setUnifiedTitleAndToolBarOnMac(self, set: bool) -> None:
    """
    Calls Qt's 'void QMainWindow::setUnifiedTitleAndToolBarOnMac(bool set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmainwindow.html#setUnifiedTitleAndToolBarOnMac

    Parameters
    ----------

    set : bool
      Passed on as it is.
    """
    #  void QMainWindow::setUnifiedTitleAndToolBarOnMac(bool set)
    self.uglySide.call(
        'ritual_ZN11QMainWindow30setUnifiedTitleAndToolBarOnMacEb', set,
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
  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, Qt.WindowFlags)
  @overload(NoneType, Qt.WindowFlags)
  def __init__(
      self,
      parent: Optional[QWidget] = None,
      flags: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> None:
    """
    Notes what was given, for Qt's 'QMainWindow::QMainWindow(QWidget *parent,
    Qt::WindowFlags flags)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#QMainWindow

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    flags : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  QMainWindow::QMainWindow(QWidget *parent, Qt::WindowFlags flags)
    self._noteCreation(QMainWindow, lambda: Rituals.call(
        'ritual_ZN11QMainWindowC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE',
        self._addressOf(parent), flags.value,
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

  def takeCentralWidget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QMainWindow::takeCentralWidget()'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#takeCentralWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QMainWindow::takeCentralWidget()
    address = self.uglySide.call(
        'ritual_ZN11QMainWindow17takeCentralWidgetEv',
    )
    return QWidget._cuteAt(address)

  @overload()
  @overload(Qt.ToolBarArea)
  def addToolBarBreak(
      self,
      area: Qt.ToolBarArea = Qt.ToolBarArea.TopToolBarArea,
  ) -> None:
    """
    Calls Qt's 'void QMainWindow::addToolBarBreak(Qt::ToolBarArea area)'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#addToolBarBreak

    Parameters
    ----------

    area : Qt.ToolBarArea
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ToolBarArea.TopToolBarArea.
    """
    #  void QMainWindow::addToolBarBreak(Qt::ToolBarArea area)
    self.uglySide.call(
        'ritual_ZN11QMainWindow15addToolBarBreakEN2Qt11ToolBarAreaE',
        area.value,
    )

  @overload(QToolBar)
  @overload(NoneType)
  def insertToolBarBreak(self, before: Optional[QToolBar]) -> None:
    """
    Calls Qt's 'void QMainWindow::insertToolBarBreak(QToolBar *before)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmainwindow.html#insertToolBarBreak

    Parameters
    ----------

    before : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMainWindow::insertToolBarBreak(QToolBar *before)
    self.uglySide.call(
        'ritual_ZN11QMainWindow18insertToolBarBreakEP8QToolBar',
        self._addressOf(before),
    )

  @overload(Qt.ToolBarArea, QToolBar)
  @overload(Qt.ToolBarArea, NoneType)
  def addToolBar(
      self,
      area: Qt.ToolBarArea,
      toolbar: Optional[QToolBar],
  ) -> None:
    """
    Calls Qt's 'void QMainWindow::addToolBar(Qt::ToolBarArea area, QToolBar
    *toolbar)'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#addToolBar

    Parameters
    ----------

    area : Qt.ToolBarArea
      Passed on as its number.

    toolbar : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMainWindow::addToolBar(Qt::ToolBarArea area, QToolBar *toolbar)
    self.uglySide.call(
        'ritual_ZN11QMainWindow10addToolBarEN2Qt11ToolBarAreaEP8QToolBar',
        area.value, self._addressOf(toolbar),
    )

  @overload(QToolBar)
  @overload(NoneType)
  def addToolBar(self, toolbar: Optional[QToolBar]) -> None:
    """
    Calls Qt's 'void QMainWindow::addToolBar(QToolBar *toolbar)'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#addToolBar

    Parameters
    ----------

    toolbar : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMainWindow::addToolBar(QToolBar *toolbar)
    self.uglySide.call(
        'ritual_ZN11QMainWindow10addToolBarEP8QToolBar',
        self._addressOf(toolbar),
    )

  @overload(str)
  def addToolBar(self, title: str) -> Optional[QToolBar]:
    """
    Calls Qt's 'QToolBar *QMainWindow::addToolBar(const QString &title)'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#addToolBar

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QToolBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QToolBar *QMainWindow::addToolBar(const QString &title)
    address = self.uglySide.call(
        'ritual_ZN11QMainWindow10addToolBarERK7QString', title,
    )
    return QToolBar._cuteAt(address)

  @overload(QToolBar, QToolBar)
  @overload(QToolBar, NoneType)
  @overload(NoneType, QToolBar)
  @overload(NoneType, NoneType)
  def insertToolBar(
      self,
      before: Optional[QToolBar],
      toolbar: Optional[QToolBar],
  ) -> None:
    """
    Calls Qt's 'void QMainWindow::insertToolBar(QToolBar *before, QToolBar
    *toolbar)'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#insertToolBar

    Parameters
    ----------

    before : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    toolbar : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMainWindow::insertToolBar(QToolBar *before, QToolBar *toolbar)
    self.uglySide.call(
        'ritual_ZN11QMainWindow13insertToolBarEP8QToolBarS1_',
        self._addressOf(before), self._addressOf(toolbar),
    )

  @overload(QToolBar)
  @overload(NoneType)
  def removeToolBar(self, toolbar: Optional[QToolBar]) -> None:
    """
    Calls Qt's 'void QMainWindow::removeToolBar(QToolBar *toolbar)'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#removeToolBar

    Parameters
    ----------

    toolbar : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMainWindow::removeToolBar(QToolBar *toolbar)
    self.uglySide.call(
        'ritual_ZN11QMainWindow13removeToolBarEP8QToolBar',
        self._addressOf(toolbar),
    )

  @overload(QToolBar)
  @overload(NoneType)
  def removeToolBarBreak(self, before: Optional[QToolBar]) -> None:
    """
    Calls Qt's 'void QMainWindow::removeToolBarBreak(QToolBar *before)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmainwindow.html#removeToolBarBreak

    Parameters
    ----------

    before : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMainWindow::removeToolBarBreak(QToolBar *before)
    self.uglySide.call(
        'ritual_ZN11QMainWindow18removeToolBarBreakEP8QToolBar',
        self._addressOf(before),
    )

  @overload(Qt.DockWidgetArea, QDockWidget)
  @overload(Qt.DockWidgetArea, NoneType)
  def addDockWidget(
      self,
      area: Qt.DockWidgetArea,
      dockwidget: Optional[QDockWidget],
  ) -> None:
    """
    Calls Qt's 'void QMainWindow::addDockWidget(Qt::DockWidgetArea area,
    QDockWidget *dockwidget)'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#addDockWidget

    Parameters
    ----------

    area : Qt.DockWidgetArea
      Passed on as its number.

    dockwidget : Optional[QDockWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMainWindow::addDockWidget(Qt::DockWidgetArea area, QDockWidget
    #      *dockwidget)
    self.uglySide.call(
        'ritual_ZN11QMainWindow13addDockWidgetEN2Qt14DockWidgetAreaEP11QDoc'
        'kWidget',
        area.value, self._addressOf(dockwidget),
    )

  @overload(Qt.DockWidgetArea, QDockWidget, Qt.Orientation)
  @overload(Qt.DockWidgetArea, NoneType, Qt.Orientation)
  def addDockWidget(
      self,
      area: Qt.DockWidgetArea,
      dockwidget: Optional[QDockWidget],
      orientation: Qt.Orientation,
  ) -> None:
    """
    Calls Qt's 'void QMainWindow::addDockWidget(Qt::DockWidgetArea area,
    QDockWidget *dockwidget, Qt::Orientation orientation)'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#addDockWidget

    Parameters
    ----------

    area : Qt.DockWidgetArea
      Passed on as its number.

    dockwidget : Optional[QDockWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QMainWindow::addDockWidget(Qt::DockWidgetArea area, QDockWidget
    #      *dockwidget, Qt::Orientation orientation)
    self.uglySide.call(
        'ritual_ZN11QMainWindow13addDockWidgetEN2Qt14DockWidgetAreaEP11QDoc'
        'kWidgetNS0_11OrientationE',
        area.value, self._addressOf(dockwidget), orientation.value,
    )

  @overload(QDockWidget, QDockWidget, Qt.Orientation)
  @overload(QDockWidget, NoneType, Qt.Orientation)
  @overload(NoneType, QDockWidget, Qt.Orientation)
  @overload(NoneType, NoneType, Qt.Orientation)
  def splitDockWidget(
      self,
      after: Optional[QDockWidget],
      dockwidget: Optional[QDockWidget],
      orientation: Qt.Orientation,
  ) -> None:
    """
    Calls Qt's 'void QMainWindow::splitDockWidget(QDockWidget *after,
    QDockWidget *dockwidget, Qt::Orientation orientation)'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#splitDockWidget

    Parameters
    ----------

    after : Optional[QDockWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dockwidget : Optional[QDockWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QMainWindow::splitDockWidget(QDockWidget *after, QDockWidget
    #      *dockwidget, Qt::Orientation orientation)
    self.uglySide.call(
        'ritual_ZN11QMainWindow15splitDockWidgetEP11QDockWidgetS1_N2Qt11Ori'
        'entationE',
        self._addressOf(after), self._addressOf(dockwidget),
        orientation.value,
    )

  @overload(QDockWidget, QDockWidget)
  @overload(QDockWidget, NoneType)
  @overload(NoneType, QDockWidget)
  @overload(NoneType, NoneType)
  def tabifyDockWidget(
      self,
      first: Optional[QDockWidget],
      second: Optional[QDockWidget],
  ) -> None:
    """
    Calls Qt's 'void QMainWindow::tabifyDockWidget(QDockWidget *first,
    QDockWidget *second)'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#tabifyDockWidget

    Parameters
    ----------

    first : Optional[QDockWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    second : Optional[QDockWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMainWindow::tabifyDockWidget(QDockWidget *first, QDockWidget
    #      *second)
    self.uglySide.call(
        'ritual_ZN11QMainWindow16tabifyDockWidgetEP11QDockWidgetS1_',
        self._addressOf(first), self._addressOf(second),
    )

  @overload(QDockWidget)
  @overload(NoneType)
  def removeDockWidget(self, dockwidget: Optional[QDockWidget]) -> None:
    """
    Calls Qt's 'void QMainWindow::removeDockWidget(QDockWidget *dockwidget)'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#removeDockWidget

    Parameters
    ----------

    dockwidget : Optional[QDockWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMainWindow::removeDockWidget(QDockWidget *dockwidget)
    self.uglySide.call(
        'ritual_ZN11QMainWindow16removeDockWidgetEP11QDockWidget',
        self._addressOf(dockwidget),
    )

  @overload(QDockWidget)
  @overload(NoneType)
  def restoreDockWidget(self, dockwidget: Optional[QDockWidget]) -> bool:
    """
    Calls Qt's 'bool QMainWindow::restoreDockWidget(QDockWidget
    *dockwidget)'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#restoreDockWidget

    Parameters
    ----------

    dockwidget : Optional[QDockWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QMainWindow::restoreDockWidget(QDockWidget *dockwidget)
    return self.uglySide.call(
        'ritual_ZN11QMainWindow17restoreDockWidgetEP11QDockWidget',
        self._addressOf(dockwidget),
    )

  @overload(QByteArray)
  @overload(QByteArray, int)
  def restoreState(self, state: QByteArray, version: int = 0) -> bool:
    """
    Calls Qt's 'bool QMainWindow::restoreState(const QByteArray &state, int
    version)'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#restoreState

    Parameters
    ----------

    state : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    version : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  bool QMainWindow::restoreState(const QByteArray &state, int version)
    return self.uglySide.call(
        'ritual_ZN11QMainWindow12restoreStateERK10QByteArrayi',
        self._valueOf(state), version,
    )

  def createPopupMenu(self) -> Optional[QMenu]:
    """
    Calls Qt's 'QMenu *QMainWindow::createPopupMenu()'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindow.html#createPopupMenu

    Returns
    -------

    Optional[QMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenu *QMainWindow::createPopupMenu()
    address = self.uglySide.call('ritual_ZN11QMainWindow15createPopupMenuEv')
    return QMenu._cuteAt(address)
