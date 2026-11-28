"""
QMainWindowLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qmainwindowlayout_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QMainWindowLayout to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QLayout, QLayoutItem, QTabWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPoint, QRect, QSize, QTimerEvent
  from . import QDockAreaLayout, QDockWidget, QStatusBar, QStyleOptionToolBar
  from . import QToolBar, QToolBarAreaLayout, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDockWidget = WAIT['QDockWidget']
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QStatusBar = WAIT['QStatusBar']
  QStyleOptionToolBar = WAIT['QStyleOptionToolBar']
  QTimerEvent = WAIT['QTimerEvent']
  QToolBar = WAIT['QToolBar']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMainWindowLayout(QLayout):
  """
  The cute side of Qt's QMainWindowLayout: a plain Python object standing in
  front of one C++ QMainWindowLayout.

  It is built on the cute 'QLayout', as Qt's QMainWindowLayout is built on
  Qt's QLayout, and has everything that class has. Qt's QMainWindowLayout is
  built on Qt's QMainWindowLayoutSeparatorHelper<QMainWindowLayout> as well,
  which is not reflected.

  What exists
  -----------

  Every function of Qt's QMainWindowLayout that has a ritual and that Python
  can call so far, 38 names in all: 'metaObject', 'statusBar',
  'setStatusBar', 'centralWidget', 'setCentralWidget', 'insertToolBarBreak',
  'removeToolBarBreak', 'toolBarArea', 'toolBarBreak', 'getStyleOptionInfo',
  'removeToolBar', 'toggleToolBarsVisible', 'toolBarAreaLayout', 'setCorner',
  'corner', 'dockWidgetArea', 'documentMode', 'setDocumentMode',
  'getSeparatorWidget', 'tabShape', 'dockAreaLayoutInfo', 'addItem',
  'setGeometry', 'itemAt', 'takeAt', 'count', 'sizeHint', 'minimumSize',
  'invalidate', 'applyRestoredState', 'needsPlatformDrag',
  'performPlatformWidgetDrag', 'timerEvent', 'updateGapIndicator',
  'tabChanged', 'tabMoved', 'tabifyWhileFloating', 'showTabBars'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QMainWindowLayout::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QMainWindowLayout::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QMainWindowLayout::~QMainWindowLayout()': the destructor: Python
    never removes a C++ QMainWindowLayout.

  What has no ritual
  ------------------

  38 of the 79 functions Qt declares: 15 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 8 leans on
  'QMainWindowLayout; 4 leans on 'QDockWidgetGroupWindow; 3 leans on
  'QDockAreaLayout; 2 not a gap; 2 leans on 'QToolBarLayout; 1 leans on
  'QToolBarAreaLayout; 1 leans on 'lcQpaDockWidgets()', which Qt's source
  does not mark for use from outside Qt and has no code for that could be
  taken; 1 leans on 'QDockAreaLayoutInfo; 1 leans on 'QDockAreaLayoutItem.

  What to expect
  --------------

  - The C++ QMainWindowLayout is created at the first use, not by
    'QMainWindowLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMainWindowLayout.
  - Qt tells when it has removed the C++ QMainWindowLayout. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QMainWindowLayout that has no cute function yet,
    '__init__', 'addDockWidget', 'addToolBar', 'addToolBarBreak',
    'animationFinished', 'applyState', 'createTabbedDockWindow', 'dockInfo',
    'dockWidgetAreaRect', 'findTabBar', 'getTabBar', 'hover',
    'insertToolBar', 'isDockWidgetTabbed', 'keepSize', 'moveToolBar', 'plug',
    'raise_', 'restore', 'restoreDockWidget', 'restoreState', 'revert',
    'saveState', 'setCurrentHoveredFloat', 'setDockOptions',
    'setTabPosition', 'setTabShape', 'setVerticalTabsEnabled',
    'splitDockWidget', 'tabPosition', 'tabifiedDockWidgets',
    'tabifyDockWidget', 'unplug', 'unuseTabBar', 'updateTabBarShapes', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QMainWindowLayout, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class DockWidgetAreaSize(CuteNum):
    """
    The enum 'QMainWindowLayout::DockWidgetAreaSize' of Qt, with the 2 names
    Qt gives in it.
    """

    Visible = Kee[int](0)
    Maximum = Kee[int](1)

  class VersionMarkers(CuteNum):
    """
    The enum 'QMainWindowLayout::VersionMarkers' of Qt, with the 1 names Qt
    gives in it.
    """

    VersionMarker = Kee[int](255)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def needsPlatformDrag() -> bool:
    """
    Calls Qt's 'bool QMainWindowLayout::needsPlatformDrag()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmainwindowlayout.html#needsPlatformDrag
    """
    #  bool QMainWindowLayout::needsPlatformDrag()
    return Rituals.call('ritual_ZN17QMainWindowLayout17needsPlatformDragEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMainWindowLayout'

  #  A C++ QMainWindowLayout Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMainWindowLayout'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QMainWindowLayout::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindowlayout.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QMainWindowLayout::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QMainWindowLayout10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def statusBar(self) -> Optional[QStatusBar]:
    """
    Calls Qt's 'QStatusBar *QMainWindowLayout::statusBar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindowlayout.html#statusBar

    Returns
    -------

    Optional[QStatusBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStatusBar *QMainWindowLayout::statusBar() const
    address = self.uglySide.call('ritual_ZNK17QMainWindowLayout9statusBarEv')
    from . import QStatusBar
    return QStatusBar._cuteAt(address)

  def centralWidget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QMainWindowLayout::centralWidget() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmainwindowlayout.html#centralWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QMainWindowLayout::centralWidget() const
    address = self.uglySide.call(
        'ritual_ZNK17QMainWindowLayout13centralWidgetEv',
    )
    from . import QWidget
    return QWidget._cuteAt(address)

  @overload(QToolBar)
  @overload(NoneType)
  def toolBarArea(self, toolbar: Optional[QToolBar]) -> Qt.ToolBarArea:
    """
    Calls Qt's 'Qt::ToolBarArea QMainWindowLayout::toolBarArea(const QToolBar
    *toolbar) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindowlayout.html#toolBarArea

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
    #  Qt::ToolBarArea QMainWindowLayout::toolBarArea(const QToolBar
    #      *toolbar) const
    return Qt.ToolBarArea(self.uglySide.call(
        'ritual_ZNK17QMainWindowLayout11toolBarAreaEPK8QToolBar',
        self._addressOf(toolbar),
    ))

  @overload(QToolBar)
  @overload(NoneType)
  def toolBarBreak(self, toolBar: Optional[QToolBar]) -> bool:
    """
    Calls Qt's 'bool QMainWindowLayout::toolBarBreak(QToolBar *toolBar)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmainwindowlayout.html#toolBarBreak

    Parameters
    ----------

    toolBar : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QMainWindowLayout::toolBarBreak(QToolBar *toolBar) const
    return self.uglySide.call(
        'ritual_ZNK17QMainWindowLayout12toolBarBreakEP8QToolBar',
        self._addressOf(toolBar),
    )

  @overload(Qt.Corner)
  def corner(self, corner: Qt.Corner) -> Qt.DockWidgetArea:
    """
    Calls Qt's 'Qt::DockWidgetArea QMainWindowLayout::corner(Qt::Corner
    corner) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindowlayout.html#corner

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
    #  Qt::DockWidgetArea QMainWindowLayout::corner(Qt::Corner corner) const
    return Qt.DockWidgetArea(self.uglySide.call(
        'ritual_ZNK17QMainWindowLayout6cornerEN2Qt6CornerE', corner.value,
    ))

  @overload(QWidget)
  @overload(NoneType)
  def dockWidgetArea(self, widget: Optional[QWidget]) -> Qt.DockWidgetArea:
    """
    Calls Qt's 'Qt::DockWidgetArea QMainWindowLayout::dockWidgetArea(const
    QWidget *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmainwindowlayout.html#dockWidgetArea

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Qt.DockWidgetArea
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.DockWidgetArea(number)' gives.
    """
    #  Qt::DockWidgetArea QMainWindowLayout::dockWidgetArea(const QWidget
    #      *widget) const
    return Qt.DockWidgetArea(self.uglySide.call(
        'ritual_ZNK17QMainWindowLayout14dockWidgetAreaEPK7QWidget',
        self._addressOf(widget),
    ))

  def documentMode(self) -> bool:
    """
    Calls Qt's 'bool QMainWindowLayout::documentMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmainwindowlayout.html#documentMode
    """
    #  bool QMainWindowLayout::documentMode() const
    return self.uglySide.call(
        'ritual_ZNK17QMainWindowLayout12documentModeEv',
    )

  def tabShape(self) -> QTabWidget.TabShape:
    """
    Calls Qt's 'QTabWidget::TabShape QMainWindowLayout::tabShape() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindowlayout.html#tabShape

    Returns
    -------

    QTabWidget.TabShape
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QTabWidget.TabShape(number)' gives.
    """
    #  QTabWidget::TabShape QMainWindowLayout::tabShape() const
    return QTabWidget.TabShape(self.uglySide.call(
        'ritual_ZNK17QMainWindowLayout8tabShapeEv',
    ))

  @overload(int)
  def itemAt(self, index: int) -> Optional[QLayoutItem]:
    """
    Calls Qt's 'QLayoutItem *QMainWindowLayout::itemAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindowlayout.html#itemAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QLayoutItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayoutItem *QMainWindowLayout::itemAt(int index) const
    ritual = 'ritual_ZNK17QMainWindowLayout6itemAtEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QMainWindowLayout6itemAtEi'
    address = self.uglySide.call(ritual, index)
    return QLayoutItem._cuteAt(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QMainWindowLayout::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindowlayout.html#count
    """
    #  int QMainWindowLayout::count() const
    ritual = 'ritual_ZNK17QMainWindowLayout5countEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QMainWindowLayout5countEv'
    return self.uglySide.call(ritual)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QMainWindowLayout::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindowlayout.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QMainWindowLayout::sizeHint() const
    address = self.uglySide.call('ritual_ZNK17QMainWindowLayout8sizeHintEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QMainWindowLayout::minimumSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindowlayout.html#minimumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QMainWindowLayout::minimumSize() const
    address = self.uglySide.call(
        'ritual_ZNK17QMainWindowLayout11minimumSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStatusBar)
  @overload(NoneType)
  def setStatusBar(self, sb: Optional[QStatusBar]) -> None:
    """
    Calls Qt's 'void QMainWindowLayout::setStatusBar(QStatusBar *sb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmainwindowlayout.html#setStatusBar

    Parameters
    ----------

    sb : Optional[QStatusBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMainWindowLayout::setStatusBar(QStatusBar *sb)
    self.uglySide.call(
        'ritual_ZN17QMainWindowLayout12setStatusBarEP10QStatusBar',
        self._addressOf(sb),
    )

  @overload(QWidget)
  @overload(NoneType)
  def setCentralWidget(self, cw: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QMainWindowLayout::setCentralWidget(QWidget *cw)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmainwindowlayout.html#setCentralWidget

    Parameters
    ----------

    cw : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMainWindowLayout::setCentralWidget(QWidget *cw)
    self.uglySide.call(
        'ritual_ZN17QMainWindowLayout16setCentralWidgetEP7QWidget',
        self._addressOf(cw),
    )

  @overload(Qt.Corner, Qt.DockWidgetArea)
  def setCorner(self, corner: Qt.Corner, area: Qt.DockWidgetArea) -> None:
    """
    Calls Qt's 'void QMainWindowLayout::setCorner(Qt::Corner corner,
    Qt::DockWidgetArea area)'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindowlayout.html#setCorner

    Parameters
    ----------

    corner : Qt.Corner
      Passed on as its number.

    area : Qt.DockWidgetArea
      Passed on as its number.
    """
    #  void QMainWindowLayout::setCorner(Qt::Corner corner,
    #      Qt::DockWidgetArea area)
    self.uglySide.call(
        'ritual_ZN17QMainWindowLayout9setCornerEN2Qt6CornerENS0_14DockWidge'
        'tAreaE',
        corner.value, area.value,
    )

  @overload(bool)
  def setDocumentMode(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QMainWindowLayout::setDocumentMode(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmainwindowlayout.html#setDocumentMode

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QMainWindowLayout::setDocumentMode(bool enabled)
    self.uglySide.call(
        'ritual_ZN17QMainWindowLayout15setDocumentModeEb', enabled,
    )

  @overload(QRect)
  def setGeometry(self, r: QRect) -> None:
    """
    Calls Qt's 'void QMainWindowLayout::setGeometry(const QRect &r)'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindowlayout.html#setGeometry

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QMainWindowLayout::setGeometry(const QRect &r)
    self.uglySide.call(
        'ritual_ZN17QMainWindowLayout11setGeometryERK5QRect',
        self._valueOf(r),
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
    Qt's 'QMainWindowLayout::QMainWindowLayout(QMainWindow *mainwindow,
    QLayout *parentLayout)': leans on
    'QMainWindowLayout::qt_metacall(QMetaObject::Call, int, void**)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.__init__' has no cute function yet. Qt's "
        "'QMainWindowLayout::QMainWindowLayout(QMainWindow *mainwindow, "
        "QLayout *parentLayout)': leans on "
        "'QMainWindowLayout::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  @overload(QToolBar)
  @overload(NoneType)
  def insertToolBarBreak(self, before: Optional[QToolBar]) -> None:
    """
    Calls Qt's 'void QMainWindowLayout::insertToolBarBreak(QToolBar
    *before)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmainwindowlayout.html#insertToolBarBreak

    Parameters
    ----------

    before : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMainWindowLayout::insertToolBarBreak(QToolBar *before)
    self.uglySide.call(
        'ritual_ZN17QMainWindowLayout18insertToolBarBreakEP8QToolBar',
        self._addressOf(before),
    )

  @overload(QToolBar)
  @overload(NoneType)
  def removeToolBarBreak(self, before: Optional[QToolBar]) -> None:
    """
    Calls Qt's 'void QMainWindowLayout::removeToolBarBreak(QToolBar
    *before)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmainwindowlayout.html#removeToolBarBreak

    Parameters
    ----------

    before : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMainWindowLayout::removeToolBarBreak(QToolBar *before)
    self.uglySide.call(
        'ritual_ZN17QMainWindowLayout18removeToolBarBreakEP8QToolBar',
        self._addressOf(before),
    )

  @overload(QStyleOptionToolBar, QToolBar)
  @overload(QStyleOptionToolBar, NoneType)
  @overload(NoneType, QToolBar)
  @overload(NoneType, NoneType)
  def getStyleOptionInfo(
      self,
      option: Optional[QStyleOptionToolBar],
      toolBar: Optional[QToolBar],
  ) -> None:
    """
    Calls Qt's 'void
    QMainWindowLayout::getStyleOptionInfo(QStyleOptionToolBar *option,
    QToolBar *toolBar) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmainwindowlayout.html#getStyleOptionInfo

    Parameters
    ----------

    option : Optional[QStyleOptionToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    toolBar : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMainWindowLayout::getStyleOptionInfo(QStyleOptionToolBar
    #      *option, QToolBar *toolBar) const
    self.uglySide.call(
        'ritual_ZNK17QMainWindowLayout18getStyleOptionInfoEP19QStyleOptionT'
        'oolBarP8QToolBar',
        self._addressOf(option), self._addressOf(toolBar),
    )

  @overload(QToolBar)
  @overload(NoneType)
  def removeToolBar(self, toolbar: Optional[QToolBar]) -> None:
    """
    Calls Qt's 'void QMainWindowLayout::removeToolBar(QToolBar *toolbar)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmainwindowlayout.html#removeToolBar

    Parameters
    ----------

    toolbar : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMainWindowLayout::removeToolBar(QToolBar *toolbar)
    self.uglySide.call(
        'ritual_ZN17QMainWindowLayout13removeToolBarEP8QToolBar',
        self._addressOf(toolbar),
    )

  def toggleToolBarsVisible(self) -> None:
    """
    Calls Qt's 'void QMainWindowLayout::toggleToolBarsVisible()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmainwindowlayout.html#toggleToolBarsVisible
    """
    #  void QMainWindowLayout::toggleToolBarsVisible()
    self.uglySide.call(
        'ritual_ZN17QMainWindowLayout21toggleToolBarsVisibleEv',
    )

  def toolBarAreaLayout(self) -> Optional[QToolBarAreaLayout]:
    """
    Calls Qt's 'QToolBarAreaLayout *QMainWindowLayout::toolBarAreaLayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmainwindowlayout.html#toolBarAreaLayout

    Returns
    -------

    Optional[QToolBarAreaLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QToolBarAreaLayout *QMainWindowLayout::toolBarAreaLayout()
    address = self.uglySide.call(
        'ritual_ZN17QMainWindowLayout17toolBarAreaLayoutEv',
    )
    from . import QToolBarAreaLayout
    return QToolBarAreaLayout._cuteAt(address)

  def getSeparatorWidget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QMainWindowLayout::getSeparatorWidget()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmainwindowlayout.html#getSeparatorWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QMainWindowLayout::getSeparatorWidget()
    address = self.uglySide.call(
        'ritual_ZN17QMainWindowLayout18getSeparatorWidgetEv',
    )
    from . import QWidget
    return QWidget._cuteAt(address)

  def dockAreaLayoutInfo(self) -> Optional[QDockAreaLayout]:
    """
    Calls Qt's 'QDockAreaLayout *QMainWindowLayout::dockAreaLayoutInfo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmainwindowlayout.html#dockAreaLayoutInfo

    Returns
    -------

    Optional[QDockAreaLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDockAreaLayout *QMainWindowLayout::dockAreaLayoutInfo()
    address = self.uglySide.call(
        'ritual_ZN17QMainWindowLayout18dockAreaLayoutInfoEv',
    )
    from . import QDockAreaLayout
    return QDockAreaLayout._cuteAt(address)

  @overload(QLayoutItem)
  @overload(NoneType)
  def addItem(self, item: Optional[QLayoutItem]) -> None:
    """
    Calls Qt's 'void QMainWindowLayout::addItem(QLayoutItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindowlayout.html#addItem

    Parameters
    ----------

    item : Optional[QLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMainWindowLayout::addItem(QLayoutItem *item)
    ritual = 'ritual_ZN17QMainWindowLayout7addItemEP11QLayoutItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QMainWindowLayout7addItemEP11QLayoutItem'
    self.uglySide.call(ritual, self._addressOf(item, 'QLayoutItem'))

  @overload(int)
  def takeAt(self, index: int) -> Optional[QLayoutItem]:
    """
    Calls Qt's 'QLayoutItem *QMainWindowLayout::takeAt(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindowlayout.html#takeAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QLayoutItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayoutItem *QMainWindowLayout::takeAt(int index)
    address = self.uglySide.call(
        'ritual_ZN17QMainWindowLayout6takeAtEi', index,
    )
    return QLayoutItem._cuteAt(address)

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QMainWindowLayout::invalidate()'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindowlayout.html#invalidate
    """
    #  void QMainWindowLayout::invalidate()
    ritual = 'ritual_ZN17QMainWindowLayout10invalidateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QMainWindowLayout10invalidateEv'
    self.uglySide.call(ritual)

  def applyRestoredState(self) -> None:
    """
    Calls Qt's 'void QMainWindowLayout::applyRestoredState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmainwindowlayout.html#applyRestoredState
    """
    #  void QMainWindowLayout::applyRestoredState()
    self.uglySide.call('ritual_ZN17QMainWindowLayout18applyRestoredStateEv')

  @overload(QLayoutItem, QPoint)
  @overload(NoneType, QPoint)
  def performPlatformWidgetDrag(
      self,
      widgetItem: Optional[QLayoutItem],
      pressPosition: QPoint,
  ) -> Qt.DropAction:
    """
    Calls Qt's 'Qt::DropAction
    QMainWindowLayout::performPlatformWidgetDrag(QLayoutItem *widgetItem,
    const QPoint &pressPosition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmainwindowlayout.html#performPlatformWidgetDrag

    Parameters
    ----------

    widgetItem : Optional[QLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pressPosition : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    Qt.DropAction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.DropAction(number)'
      gives.
    """
    #  Qt::DropAction
    #      QMainWindowLayout::performPlatformWidgetDrag(QLayoutItem
    #      *widgetItem, const QPoint &pressPosition)
    return Qt.DropAction(self.uglySide.call(
        'ritual_ZN17QMainWindowLayout25performPlatformWidgetDragEP11QLayout'
        'ItemRK6QPoint',
        self._addressOf(widgetItem, 'QLayoutItem'),
        self._valueOf(pressPosition),
    ))

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, e: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QMainWindowLayout::timerEvent(QTimerEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindowlayout.html#timerEvent

    Parameters
    ----------

    e : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMainWindowLayout::timerEvent(QTimerEvent *e)
    ritual = 'ritual_ZN17QMainWindowLayout10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QMainWindowLayout10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  def updateGapIndicator(self) -> None:
    """
    Calls Qt's 'void QMainWindowLayout::updateGapIndicator()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmainwindowlayout.html#updateGapIndicator
    """
    #  void QMainWindowLayout::updateGapIndicator()
    self.uglySide.call('ritual_ZN17QMainWindowLayout18updateGapIndicatorEv')

  def tabChanged(self) -> None:
    """
    Calls Qt's 'void QMainWindowLayout::tabChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindowlayout.html#tabChanged
    """
    #  void QMainWindowLayout::tabChanged()
    self.uglySide.call('ritual_ZN17QMainWindowLayout10tabChangedEv')

  @overload(int, int)
  def tabMoved(self, from_: int, to: int) -> None:
    """
    Calls Qt's 'void QMainWindowLayout::tabMoved(int from, int to)'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindowlayout.html#tabMoved

    Parameters
    ----------

    from_ : int
      Passed on as it is.

    to : int
      Passed on as it is.
    """
    #  void QMainWindowLayout::tabMoved(int from, int to)
    self.uglySide.call('ritual_ZN17QMainWindowLayout8tabMovedEii', from_, to)

  @overload(QDockWidget, QDockWidget)
  @overload(QDockWidget, NoneType)
  @overload(NoneType, QDockWidget)
  @overload(NoneType, NoneType)
  def tabifyWhileFloating(
      self,
      first: Optional[QDockWidget],
      second: Optional[QDockWidget],
  ) -> None:
    """
    Calls Qt's 'void QMainWindowLayout::tabifyWhileFloating(QDockWidget
    *first, QDockWidget *second)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmainwindowlayout.html#tabifyWhileFloating

    Parameters
    ----------

    first : Optional[QDockWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    second : Optional[QDockWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMainWindowLayout::tabifyWhileFloating(QDockWidget *first,
    #      QDockWidget *second)
    self.uglySide.call(
        'ritual_ZN17QMainWindowLayout19tabifyWhileFloatingEP11QDockWidgetS1'
        '_',
        self._addressOf(first), self._addressOf(second),
    )

  def showTabBars(self) -> None:
    """
    Calls Qt's 'void QMainWindowLayout::showTabBars()'.

    Qt's own words: https://doc.qt.io/qt-6/qmainwindowlayout.html#showTabBars
    """
    #  void QMainWindowLayout::showTabBars()
    self.uglySide.call('ritual_ZN17QMainWindowLayout11showTabBarsEv')

  @staticmethod
  def addDockWidget(*__, **_) -> Never:
    """
    Qt's 'void QMainWindowLayout::addDockWidget(Qt::DockWidgetArea area,
    QDockWidget *dockwidget, Qt::Orientation orientation)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'toDockPos'.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.addDockWidget' has no cute function yet. Qt's "
        "'void QMainWindowLayout::addDockWidget(Qt::DockWidgetArea area, "
        "QDockWidget *dockwidget, Qt::Orientation orientation)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'toDockPos'.")

  @staticmethod
  def addToolBar(*__, **_) -> Never:
    """
    Qt's 'void QMainWindowLayout::addToolBar(Qt::ToolBarArea area, QToolBar
    *toolbar, bool needAddChildWidget)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'validateToolBarArea'.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.addToolBar' has no cute function yet. Qt's "
        "'void QMainWindowLayout::addToolBar(Qt::ToolBarArea area, QToolBar "
        "*toolbar, bool needAddChildWidget)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'validateToolBarArea'.")

  @staticmethod
  def addToolBarBreak(*__, **_) -> Never:
    """
    Qt's 'void QMainWindowLayout::addToolBarBreak(Qt::ToolBarArea area)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier 'toDockPos'.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.addToolBarBreak' has no cute function yet. Qt's "
        "'void QMainWindowLayout::addToolBarBreak(Qt::ToolBarArea area)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'toDockPos'.")

  @staticmethod
  def animationFinished(*__, **_) -> Never:
    """
    Qt's 'void QMainWindowLayout::animationFinished(QWidget *widget)': leans
    on 'QToolBarLayout::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.animationFinished' has no cute function yet. "
        "Qt's 'void QMainWindowLayout::animationFinished(QWidget *widget)': "
        "leans on 'QToolBarLayout::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def applyState(*__, **_) -> Never:
    """
    Qt's 'void QMainWindowLayout::applyState(QMainWindowLayoutState
    &newState, bool animate)': Qt's library has no name for it, and its code
    in Qt's source does not compile apart from its file: use of undeclared
    identifier 'toAnimationRule'.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.applyState' has no cute function yet. Qt's "
        "'void QMainWindowLayout::applyState(QMainWindowLayoutState "
        "&newState, bool animate)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'toAnimationRule'.")

  @staticmethod
  def createTabbedDockWindow(*__, **_) -> Never:
    """
    Qt's 'QDockWidgetGroupWindow
    *QMainWindowLayout::createTabbedDockWindow()': leans on
    'QDockAreaLayoutInfo::remove(QList<int> const&)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.createTabbedDockWindow' has no cute function "
        "yet. Qt's 'QDockWidgetGroupWindow "
        "*QMainWindowLayout::createTabbedDockWindow()': leans on "
        "'QDockAreaLayoutInfo::remove(QList<int> const&)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def dockInfo(*__, **_) -> Never:
    """
    Qt's 'QDockAreaLayoutInfo *QMainWindowLayout::dockInfo(QWidget *w)':
    leans on 'QDockAreaLayout::info(QWidget*)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.dockInfo' has no cute function yet. Qt's "
        "'QDockAreaLayoutInfo *QMainWindowLayout::dockInfo(QWidget *w)': "
        "leans on 'QDockAreaLayout::info(QWidget*)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def dockWidgetAreaRect(*__, **_) -> Never:
    """
    Qt's 'QRect QMainWindowLayout::dockWidgetAreaRect(Qt::DockWidgetArea
    area, DockWidgetAreaSize size) const': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'toDockPos'.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.dockWidgetAreaRect' has no cute function yet. "
        "Qt's 'QRect "
        "QMainWindowLayout::dockWidgetAreaRect(Qt::DockWidgetArea area, "
        "DockWidgetAreaSize size) const': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'toDockPos'.")

  @staticmethod
  def findTabBar(*__, **_) -> Never:
    """
    Qt's 'QMainWindowTabBar *QMainWindowLayout::findTabBar(const QDockWidget
    *dockWidget) const': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: static_cast from
    'QTabBar *' to 'QMainWindowTabBar *', which are not related by
    inheritance, is not allowed.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.findTabBar' has no cute function yet. Qt's "
        "'QMainWindowTabBar *QMainWindowLayout::findTabBar(const "
        "QDockWidget *dockWidget) const': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "static_cast from 'QTabBar *' to 'QMainWindowTabBar *', which are "
        "not related by inheritance, is not allowed.")

  @staticmethod
  def getTabBar(*__, **_) -> Never:
    """
    Qt's 'QTabBar *QMainWindowLayout::getTabBar()': leans on
    'QMainWindowLayout::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.getTabBar' has no cute function yet. Qt's "
        "'QTabBar *QMainWindowLayout::getTabBar()': leans on "
        "'QMainWindowLayout::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def hover(*__, **_) -> Never:
    """
    Qt's 'void QMainWindowLayout::hover(QLayoutItem *hoverTarget, const
    QPoint &mousePos)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'toDockPos'.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.hover' has no cute function yet. Qt's 'void "
        "QMainWindowLayout::hover(QLayoutItem *hoverTarget, const QPoint "
        "&mousePos)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'toDockPos'.")

  @staticmethod
  def insertToolBar(*__, **_) -> Never:
    """
    Qt's 'void QMainWindowLayout::insertToolBar(QToolBar *before, QToolBar
    *toolbar)': leans on 'QToolBarAreaLayout::insertItem(QToolBar*,
    QLayoutItem*)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.insertToolBar' has no cute function yet. Qt's "
        "'void QMainWindowLayout::insertToolBar(QToolBar *before, QToolBar "
        "*toolbar)': leans on 'QToolBarAreaLayout::insertItem(QToolBar*, "
        "QLayoutItem*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def isDockWidgetTabbed(*__, **_) -> Never:
    """
    Qt's 'bool QMainWindowLayout::isDockWidgetTabbed(const QDockWidget
    *dockWidget) const': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: member access into
    incomplete type 'const QMainWindowTabBar'.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.isDockWidgetTabbed' has no cute function yet. "
        "Qt's 'bool QMainWindowLayout::isDockWidgetTabbed(const QDockWidget "
        "*dockWidget) const': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: member access "
        "into incomplete type 'const QMainWindowTabBar'.")

  @staticmethod
  def keepSize(*__, **_) -> Never:
    """
    Qt's 'void QMainWindowLayout::keepSize(QDockWidget *w)': leans on
    'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.keepSize' has no cute function yet. Qt's 'void "
        "QMainWindowLayout::keepSize(QDockWidget *w)': leans on "
        "'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutItem "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def moveToolBar(*__, **_) -> Never:
    """
    Qt's 'void QMainWindowLayout::moveToolBar(QToolBar *toolbar, int pos)':
    leans on 'QToolBarLayout::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.moveToolBar' has no cute function yet. Qt's "
        "'void QMainWindowLayout::moveToolBar(QToolBar *toolbar, int pos)': "
        "leans on 'QToolBarLayout::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def plug(*__, **_) -> Never:
    """
    Qt's 'bool QMainWindowLayout::plug(QLayoutItem *widgetItem)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'toAnimationRule'.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.plug' has no cute function yet. Qt's 'bool "
        "QMainWindowLayout::plug(QLayoutItem *widgetItem)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'toAnimationRule'.")

  @staticmethod
  def raise_(*__, **_) -> Never:
    """
    Qt's 'void QMainWindowLayout::raise(QDockWidget *widget)': leans on
    'QDockAreaLayout::info(QWidget*)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.raise_' has no cute function yet. Qt's 'void "
        "QMainWindowLayout::raise(QDockWidget *widget)': leans on "
        "'QDockAreaLayout::info(QWidget*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def restore(*__, **_) -> Never:
    """
    Qt's 'void QMainWindowLayout::restore(QInternal::SaveStateRule rule)':
    leans on 'QDockWidgetGroupWindow::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.restore' has no cute function yet. Qt's 'void "
        "QMainWindowLayout::restore(QInternal::SaveStateRule rule)': leans "
        "on 'QDockWidgetGroupWindow::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def restoreDockWidget(*__, **_) -> Never:
    """
    Qt's 'bool QMainWindowLayout::restoreDockWidget(QDockWidget
    *dockwidget)': leans on 'QDockWidgetGroupWindow::staticMetaObject', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.restoreDockWidget' has no cute function yet. "
        "Qt's 'bool QMainWindowLayout::restoreDockWidget(QDockWidget "
        "*dockwidget)': leans on "
        "'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def restoreState(*__, **_) -> Never:
    """
    Qt's 'bool QMainWindowLayout::restoreState(QDataStream &stream)': leans
    on 'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.restoreState' has no cute function yet. Qt's "
        "'bool QMainWindowLayout::restoreState(QDataStream &stream)': leans "
        "on 'QDockWidgetGroupWindow::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def revert(*__, **_) -> Never:
    """
    Qt's 'void QMainWindowLayout::revert(QLayoutItem *widgetItem)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier
    'fixToolBarOrientation'.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.revert' has no cute function yet. Qt's 'void "
        "QMainWindowLayout::revert(QLayoutItem *widgetItem)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'fixToolBarOrientation'.")

  @staticmethod
  def saveState(*__, **_) -> Never:
    """
    Qt's 'void QMainWindowLayout::saveState(QDataStream &stream) const':
    leans on 'QDockWidgetGroupWindow::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.saveState' has no cute function yet. Qt's 'void "
        "QMainWindowLayout::saveState(QDataStream &stream) const': leans on "
        "'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setCurrentHoveredFloat(*__, **_) -> Never:
    """
    Qt's 'void
    QMainWindowLayout::setCurrentHoveredFloat(QDockWidgetGroupWindow *w)':
    leans on 'QMainWindowLayout::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.setCurrentHoveredFloat' has no cute function "
        "yet. Qt's 'void "
        "QMainWindowLayout::setCurrentHoveredFloat(QDockWidgetGroupWindow "
        "*w)': leans on 'QMainWindowLayout::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setDockOptions(*__, **_) -> Never:
    """
    Qt's 'void QMainWindowLayout::setDockOptions(QMainWindow::DockOptions
    opts)': leans on 'QMainWindowLayout::updateTabBarShapes()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.setDockOptions' has no cute function yet. Qt's "
        "'void QMainWindowLayout::setDockOptions(QMainWindow::DockOptions "
        "opts)': leans on 'QMainWindowLayout::updateTabBarShapes()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setTabPosition(*__, **_) -> Never:
    """
    Qt's 'void QMainWindowLayout::setTabPosition(Qt::DockWidgetAreas areas,
    QTabWidget::TabPosition tabPosition)': leans on
    'QMainWindowLayout::updateTabBarShapes()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.setTabPosition' has no cute function yet. Qt's "
        "'void QMainWindowLayout::setTabPosition(Qt::DockWidgetAreas areas, "
        "QTabWidget::TabPosition tabPosition)': leans on "
        "'QMainWindowLayout::updateTabBarShapes()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setTabShape(*__, **_) -> Never:
    """
    Qt's 'void QMainWindowLayout::setTabShape(QTabWidget::TabShape
    tabShape)': leans on 'QMainWindowLayout::updateTabBarShapes()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.setTabShape' has no cute function yet. Qt's "
        "'void QMainWindowLayout::setTabShape(QTabWidget::TabShape "
        "tabShape)': leans on 'QMainWindowLayout::updateTabBarShapes()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setVerticalTabsEnabled(*__, **_) -> Never:
    """
    Qt's 'void QMainWindowLayout::setVerticalTabsEnabled(bool enabled)':
    leans on 'QMainWindowLayout::updateTabBarShapes()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.setVerticalTabsEnabled' has no cute function "
        "yet. Qt's 'void QMainWindowLayout::setVerticalTabsEnabled(bool "
        "enabled)': leans on 'QMainWindowLayout::updateTabBarShapes()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def splitDockWidget(*__, **_) -> Never:
    """
    Qt's 'void QMainWindowLayout::splitDockWidget(QDockWidget *after,
    QDockWidget *dockwidget, Qt::Orientation orientation)': leans on
    'QDockAreaLayout::info(QList<int> const&)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.splitDockWidget' has no cute function yet. Qt's "
        "'void QMainWindowLayout::splitDockWidget(QDockWidget *after, "
        "QDockWidget *dockwidget, Qt::Orientation orientation)': leans on "
        "'QDockAreaLayout::info(QList<int> const&)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def tabPosition(*__, **_) -> Never:
    """
    Qt's 'QTabWidget::TabPosition
    QMainWindowLayout::tabPosition(Qt::DockWidgetArea area) const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'toDockPos'.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.tabPosition' has no cute function yet. Qt's "
        "'QTabWidget::TabPosition "
        "QMainWindowLayout::tabPosition(Qt::DockWidgetArea area) const': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'toDockPos'.")

  @staticmethod
  def tabifiedDockWidgets(*__, **_) -> Never:
    """
    Qt's 'QList<QDockWidget *> QMainWindowLayout::tabifiedDockWidgets(const
    QDockWidget *dockWidget) const': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: member access
    into incomplete type 'const QMainWindowTabBar'.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.tabifiedDockWidgets' has no cute function yet. "
        "Qt's 'QList<QDockWidget *> "
        "QMainWindowLayout::tabifiedDockWidgets(const QDockWidget "
        "*dockWidget) const': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: member access "
        "into incomplete type 'const QMainWindowTabBar'.")

  @staticmethod
  def tabifyDockWidget(*__, **_) -> Never:
    """
    Qt's 'void QMainWindowLayout::tabifyDockWidget(QDockWidget *first,
    QDockWidget *second)': leans on 'lcQpaDockWidgets()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.tabifyDockWidget' has no cute function yet. "
        "Qt's 'void QMainWindowLayout::tabifyDockWidget(QDockWidget *first, "
        "QDockWidget *second)': leans on 'lcQpaDockWidgets()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def unplug(*__, **_) -> Never:
    """
    Qt's 'QLayoutItem *QMainWindowLayout::unplug(QWidget *widget,
    QDockWidgetPrivate::DragScope scope)': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'unplugGroup'.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.unplug' has no cute function yet. Qt's "
        "'QLayoutItem *QMainWindowLayout::unplug(QWidget *widget, "
        "QDockWidgetPrivate::DragScope scope)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'unplugGroup'.")

  @staticmethod
  def unuseTabBar(*__, **_) -> Never:
    """
    Qt's 'void QMainWindowLayout::unuseTabBar(QTabBar *bar)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: incomplete type 'QMainWindowTabBar' named in nested name
    specifier.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.unuseTabBar' has no cute function yet. Qt's "
        "'void QMainWindowLayout::unuseTabBar(QTabBar *bar)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: incomplete type 'QMainWindowTabBar' named in "
        "nested name specifier.")

  @staticmethod
  def updateTabBarShapes(*__, **_) -> Never:
    """
    Qt's 'void QMainWindowLayout::updateTabBarShapes()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier '_q_tb_tabBarShapeFrom'.
    """
    raise NotImplementedError(
        "'QMainWindowLayout.updateTabBarShapes' has no cute function yet. "
        "Qt's 'void QMainWindowLayout::updateTabBarShapes()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'_q_tb_tabBarShapeFrom'.")
