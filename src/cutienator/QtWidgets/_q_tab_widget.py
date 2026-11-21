"""
QTabWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qtabwidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QTabWidgetTabPosition, QTabWidgetTabShape, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QSize
  from ..QtGui import QIcon
  from . import QTabBar
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIcon = WAIT['QIcon']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTabWidget(QWidget):
  """
  The cute side of Qt's QTabWidget: a plain Python object standing in front
  of one C++ QTabWidget.

  It is built on the cute 'QWidget', as Qt's QTabWidget is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTabWidget that has a ritual and that Python can
  call so far, 50 names in all: 'metaObject', 'tr', 'addTab', 'insertTab',
  'removeTab', 'isTabEnabled', 'setTabEnabled', 'isTabVisible',
  'setTabVisible', 'tabText', 'setTabText', 'tabIcon', 'setTabIcon',
  'setTabToolTip', 'tabToolTip', 'setTabWhatsThis', 'tabWhatsThis',
  'currentIndex', 'currentWidget', 'widget', 'indexOf', 'count',
  'tabPosition', 'setTabPosition', 'tabsClosable', 'setTabsClosable',
  'isMovable', 'setMovable', 'tabShape', 'setTabShape', 'sizeHint',
  'minimumSizeHint', 'heightForWidth', 'hasHeightForWidth',
  'setCornerWidget', 'cornerWidget', 'elideMode', 'setElideMode', 'iconSize',
  'setIconSize', 'usesScrollButtons', 'setUsesScrollButtons', 'documentMode',
  'setDocumentMode', 'tabBarAutoHide', 'setTabBarAutoHide', 'clear',
  'tabBar', 'setCurrentIndex', 'setCurrentWidget'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTabWidget::~QTabWidget()': the destructor: Python never removes a
    C++ QTabWidget.

  What has no ritual
  ------------------

  23 of the 77 functions Qt declares: 10 protected; 4 private; 4 a signal; 2
  takes or gives a type that cannot be passed yet; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QTabWidget is created at the first use, not by 'QTabWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTabWidget.
  - Qt tells when it has removed the C++ QTabWidget. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QTabWidget, and the names Qt has for the
  #  combinations of its flags enums.
  TabPosition = QTabWidgetTabPosition
  TabShape = QTabWidgetTabShape

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
    Calls Qt's 'QString QTabWidget::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#tr

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
    #  QString QTabWidget::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QTabWidget2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTabWidget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTabWidget::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTabWidget::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QTabWidget10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(int)
  def isTabEnabled(self, index: int) -> bool:
    """
    Calls Qt's 'bool QTabWidget::isTabEnabled(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#isTabEnabled

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QTabWidget::isTabEnabled(int index) const
    return self.uglySide.call(
        'ritual_ZNK10QTabWidget12isTabEnabledEi', index,
    )

  @overload(int)
  def isTabVisible(self, index: int) -> bool:
    """
    Calls Qt's 'bool QTabWidget::isTabVisible(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#isTabVisible

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QTabWidget::isTabVisible(int index) const
    return self.uglySide.call(
        'ritual_ZNK10QTabWidget12isTabVisibleEi', index,
    )

  @overload(int)
  def tabText(self, index: int) -> str:
    """
    Calls Qt's 'QString QTabWidget::tabText(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#tabText

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTabWidget::tabText(int index) const
    return self.uglySide.call('ritual_ZNK10QTabWidget7tabTextEi', index)

  @overload(int)
  def tabIcon(self, index: int) -> QIcon:
    """
    Calls Qt's 'QIcon QTabWidget::tabIcon(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#tabIcon

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QTabWidget::tabIcon(int index) const
    address = self.uglySide.call('ritual_ZNK10QTabWidget7tabIconEi', index)
    from ..QtGui import QIcon
    return QIcon._cuteOwning(address)

  @overload(int)
  def tabToolTip(self, index: int) -> str:
    """
    Calls Qt's 'QString QTabWidget::tabToolTip(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#tabToolTip

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTabWidget::tabToolTip(int index) const
    return self.uglySide.call('ritual_ZNK10QTabWidget10tabToolTipEi', index)

  @overload(int)
  def tabWhatsThis(self, index: int) -> str:
    """
    Calls Qt's 'QString QTabWidget::tabWhatsThis(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#tabWhatsThis

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTabWidget::tabWhatsThis(int index) const
    return self.uglySide.call(
        'ritual_ZNK10QTabWidget12tabWhatsThisEi', index,
    )

  def currentIndex(self) -> int:
    """
    Calls Qt's 'int QTabWidget::currentIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#currentIndex
    """
    #  int QTabWidget::currentIndex() const
    return self.uglySide.call('ritual_ZNK10QTabWidget12currentIndexEv')

  def currentWidget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QTabWidget::currentWidget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#currentWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QTabWidget::currentWidget() const
    address = self.uglySide.call('ritual_ZNK10QTabWidget13currentWidgetEv')
    return QWidget._cuteAt(address)

  @overload(int)
  def widget(self, index: int) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QTabWidget::widget(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#widget

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QTabWidget::widget(int index) const
    address = self.uglySide.call('ritual_ZNK10QTabWidget6widgetEi', index)
    return QWidget._cuteAt(address)

  @overload(QWidget)
  @overload(NoneType)
  def indexOf(self, widget: Optional[QWidget]) -> int:
    """
    Calls Qt's 'int QTabWidget::indexOf(const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#indexOf

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QTabWidget::indexOf(const QWidget *widget) const
    return self.uglySide.call(
        'ritual_ZNK10QTabWidget7indexOfEPK7QWidget', self._addressOf(widget),
    )

  def count(self) -> int:
    """
    Calls Qt's 'int QTabWidget::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#count
    """
    #  int QTabWidget::count() const
    return self.uglySide.call('ritual_ZNK10QTabWidget5countEv')

  def tabPosition(self) -> TabPosition:
    """
    Calls Qt's 'TabPosition QTabWidget::tabPosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#tabPosition

    Returns
    -------

    TabPosition
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TabPosition(number)'
      gives.
    """
    #  TabPosition QTabWidget::tabPosition() const
    return QTabWidget.TabPosition(self.uglySide.call(
        'ritual_ZNK10QTabWidget11tabPositionEv',
    ))

  def tabsClosable(self) -> bool:
    """
    Calls Qt's 'bool QTabWidget::tabsClosable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#tabsClosable
    """
    #  bool QTabWidget::tabsClosable() const
    return self.uglySide.call('ritual_ZNK10QTabWidget12tabsClosableEv')

  def isMovable(self) -> bool:
    """
    Calls Qt's 'bool QTabWidget::isMovable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#isMovable
    """
    #  bool QTabWidget::isMovable() const
    return self.uglySide.call('ritual_ZNK10QTabWidget9isMovableEv')

  def tabShape(self) -> TabShape:
    """
    Calls Qt's 'TabShape QTabWidget::tabShape() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#tabShape

    Returns
    -------

    TabShape
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TabShape(number)' gives.
    """
    #  TabShape QTabWidget::tabShape() const
    return QTabWidget.TabShape(self.uglySide.call(
        'ritual_ZNK10QTabWidget8tabShapeEv',
    ))

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QTabWidget::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QTabWidget::sizeHint() const
    address = self.uglySide.call('ritual_ZNK10QTabWidget8sizeHintEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QTabWidget::minimumSizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#minimumSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QTabWidget::minimumSizeHint() const
    address = self.uglySide.call('ritual_ZNK10QTabWidget15minimumSizeHintEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(int)
  def heightForWidth(self, width: int) -> int:
    """
    Calls Qt's 'int QTabWidget::heightForWidth(int width) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#heightForWidth

    Parameters
    ----------

    width : int
      Passed on as it is.
    """
    #  int QTabWidget::heightForWidth(int width) const
    return self.uglySide.call(
        'ritual_ZNK10QTabWidget14heightForWidthEi', width,
    )

  def hasHeightForWidth(self) -> bool:
    """
    Calls Qt's 'bool QTabWidget::hasHeightForWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#hasHeightForWidth
    """
    #  bool QTabWidget::hasHeightForWidth() const
    return self.uglySide.call('ritual_ZNK10QTabWidget17hasHeightForWidthEv')

  @overload()
  @overload(Qt.Corner)
  def cornerWidget(
      self,
      corner: Qt.Corner = Qt.Corner.TopRightCorner,
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QTabWidget::cornerWidget(Qt::Corner corner) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#cornerWidget

    Parameters
    ----------

    corner : Qt.Corner
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Corner.TopRightCorner.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QTabWidget::cornerWidget(Qt::Corner corner) const
    address = self.uglySide.call(
        'ritual_ZNK10QTabWidget12cornerWidgetEN2Qt6CornerE', corner.value,
    )
    return QWidget._cuteAt(address)

  def elideMode(self) -> Qt.TextElideMode:
    """
    Calls Qt's 'Qt::TextElideMode QTabWidget::elideMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#elideMode

    Returns
    -------

    Qt.TextElideMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.TextElideMode(number)'
      gives.
    """
    #  Qt::TextElideMode QTabWidget::elideMode() const
    return Qt.TextElideMode(self.uglySide.call(
        'ritual_ZNK10QTabWidget9elideModeEv',
    ))

  def iconSize(self) -> QSize:
    """
    Calls Qt's 'QSize QTabWidget::iconSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#iconSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QTabWidget::iconSize() const
    address = self.uglySide.call('ritual_ZNK10QTabWidget8iconSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def usesScrollButtons(self) -> bool:
    """
    Calls Qt's 'bool QTabWidget::usesScrollButtons() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#usesScrollButtons
    """
    #  bool QTabWidget::usesScrollButtons() const
    return self.uglySide.call('ritual_ZNK10QTabWidget17usesScrollButtonsEv')

  def documentMode(self) -> bool:
    """
    Calls Qt's 'bool QTabWidget::documentMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#documentMode
    """
    #  bool QTabWidget::documentMode() const
    return self.uglySide.call('ritual_ZNK10QTabWidget12documentModeEv')

  def tabBarAutoHide(self) -> bool:
    """
    Calls Qt's 'bool QTabWidget::tabBarAutoHide() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#tabBarAutoHide
    """
    #  bool QTabWidget::tabBarAutoHide() const
    return self.uglySide.call('ritual_ZNK10QTabWidget14tabBarAutoHideEv')

  def tabBar(self) -> Optional[QTabBar]:
    """
    Calls Qt's 'QTabBar *QTabWidget::tabBar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#tabBar

    Returns
    -------

    Optional[QTabBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTabBar *QTabWidget::tabBar() const
    address = self.uglySide.call('ritual_ZNK10QTabWidget6tabBarEv')
    from . import QTabBar
    return QTabBar._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, bool)
  def setTabEnabled(self, index: int, enabled: bool) -> None:
    """
    Calls Qt's 'void QTabWidget::setTabEnabled(int index, bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#setTabEnabled

    Parameters
    ----------

    index : int
      Passed on as it is.

    enabled : bool
      Passed on as it is.
    """
    #  void QTabWidget::setTabEnabled(int index, bool enabled)
    self.uglySide.call(
        'ritual_ZN10QTabWidget13setTabEnabledEib', index, enabled,
    )

  @overload(int, bool)
  def setTabVisible(self, index: int, visible: bool) -> None:
    """
    Calls Qt's 'void QTabWidget::setTabVisible(int index, bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#setTabVisible

    Parameters
    ----------

    index : int
      Passed on as it is.

    visible : bool
      Passed on as it is.
    """
    #  void QTabWidget::setTabVisible(int index, bool visible)
    self.uglySide.call(
        'ritual_ZN10QTabWidget13setTabVisibleEib', index, visible,
    )

  @overload(int, str)
  def setTabText(self, index: int, text: str) -> None:
    """
    Calls Qt's 'void QTabWidget::setTabText(int index, const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#setTabText

    Parameters
    ----------

    index : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTabWidget::setTabText(int index, const QString &text)
    self.uglySide.call(
        'ritual_ZN10QTabWidget10setTabTextEiRK7QString', index, text,
    )

  @overload(int, QIcon)
  def setTabIcon(self, index: int, icon: QIcon) -> None:
    """
    Calls Qt's 'void QTabWidget::setTabIcon(int index, const QIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#setTabIcon

    Parameters
    ----------

    index : int
      Passed on as it is.

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.
    """
    #  void QTabWidget::setTabIcon(int index, const QIcon &icon)
    self.uglySide.call(
        'ritual_ZN10QTabWidget10setTabIconEiRK5QIcon',
        index, self._valueOf(icon),
    )

  @overload(int, str)
  def setTabToolTip(self, index: int, tip: str) -> None:
    """
    Calls Qt's 'void QTabWidget::setTabToolTip(int index, const QString
    &tip)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#setTabToolTip

    Parameters
    ----------

    index : int
      Passed on as it is.

    tip : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTabWidget::setTabToolTip(int index, const QString &tip)
    self.uglySide.call(
        'ritual_ZN10QTabWidget13setTabToolTipEiRK7QString', index, tip,
    )

  @overload(int, str)
  def setTabWhatsThis(self, index: int, text: str) -> None:
    """
    Calls Qt's 'void QTabWidget::setTabWhatsThis(int index, const QString
    &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#setTabWhatsThis

    Parameters
    ----------

    index : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTabWidget::setTabWhatsThis(int index, const QString &text)
    self.uglySide.call(
        'ritual_ZN10QTabWidget15setTabWhatsThisEiRK7QString', index, text,
    )

  @overload(TabPosition)
  def setTabPosition(self, position: TabPosition) -> None:
    """
    Calls Qt's 'void QTabWidget::setTabPosition(TabPosition position)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#setTabPosition

    Parameters
    ----------

    position : TabPosition
      Passed on as its number.
    """
    #  void QTabWidget::setTabPosition(TabPosition position)
    self.uglySide.call(
        'ritual_ZN10QTabWidget14setTabPositionENS_11TabPositionE',
        position.value,
    )

  @overload(bool)
  def setTabsClosable(self, closeable: bool) -> None:
    """
    Calls Qt's 'void QTabWidget::setTabsClosable(bool closeable)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#setTabsClosable

    Parameters
    ----------

    closeable : bool
      Passed on as it is.
    """
    #  void QTabWidget::setTabsClosable(bool closeable)
    self.uglySide.call('ritual_ZN10QTabWidget15setTabsClosableEb', closeable)

  @overload(bool)
  def setMovable(self, movable: bool) -> None:
    """
    Calls Qt's 'void QTabWidget::setMovable(bool movable)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#setMovable

    Parameters
    ----------

    movable : bool
      Passed on as it is.
    """
    #  void QTabWidget::setMovable(bool movable)
    self.uglySide.call('ritual_ZN10QTabWidget10setMovableEb', movable)

  @overload(TabShape)
  def setTabShape(self, s: TabShape) -> None:
    """
    Calls Qt's 'void QTabWidget::setTabShape(TabShape s)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#setTabShape

    Parameters
    ----------

    s : TabShape
      Passed on as its number.
    """
    #  void QTabWidget::setTabShape(TabShape s)
    self.uglySide.call(
        'ritual_ZN10QTabWidget11setTabShapeENS_8TabShapeE', s.value,
    )

  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, Qt.Corner)
  @overload(NoneType, Qt.Corner)
  def setCornerWidget(
      self,
      w: Optional[QWidget],
      corner: Qt.Corner = Qt.Corner.TopRightCorner,
  ) -> None:
    """
    Calls Qt's 'void QTabWidget::setCornerWidget(QWidget *w, Qt::Corner
    corner)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#setCornerWidget

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    corner : Qt.Corner
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Corner.TopRightCorner.
    """
    #  void QTabWidget::setCornerWidget(QWidget *w, Qt::Corner corner)
    self.uglySide.call(
        'ritual_ZN10QTabWidget15setCornerWidgetEP7QWidgetN2Qt6CornerE',
        self._addressOf(w), corner.value,
    )

  @overload(Qt.TextElideMode)
  def setElideMode(self, mode: Qt.TextElideMode) -> None:
    """
    Calls Qt's 'void QTabWidget::setElideMode(Qt::TextElideMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#setElideMode

    Parameters
    ----------

    mode : Qt.TextElideMode
      Passed on as its number.
    """
    #  void QTabWidget::setElideMode(Qt::TextElideMode mode)
    self.uglySide.call(
        'ritual_ZN10QTabWidget12setElideModeEN2Qt13TextElideModeE',
        mode.value,
    )

  @overload(QSize)
  def setIconSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QTabWidget::setIconSize(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#setIconSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QTabWidget::setIconSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN10QTabWidget11setIconSizeERK5QSize', self._valueOf(size),
    )

  @overload(bool)
  def setUsesScrollButtons(self, useButtons: bool) -> None:
    """
    Calls Qt's 'void QTabWidget::setUsesScrollButtons(bool useButtons)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtabwidget.html#setUsesScrollButtons

    Parameters
    ----------

    useButtons : bool
      Passed on as it is.
    """
    #  void QTabWidget::setUsesScrollButtons(bool useButtons)
    self.uglySide.call(
        'ritual_ZN10QTabWidget20setUsesScrollButtonsEb', useButtons,
    )

  @overload(bool)
  def setDocumentMode(self, set: bool) -> None:
    """
    Calls Qt's 'void QTabWidget::setDocumentMode(bool set)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#setDocumentMode

    Parameters
    ----------

    set : bool
      Passed on as it is.
    """
    #  void QTabWidget::setDocumentMode(bool set)
    self.uglySide.call('ritual_ZN10QTabWidget15setDocumentModeEb', set)

  @overload(bool)
  def setTabBarAutoHide(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QTabWidget::setTabBarAutoHide(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#setTabBarAutoHide

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QTabWidget::setTabBarAutoHide(bool enabled)
    self.uglySide.call('ritual_ZN10QTabWidget17setTabBarAutoHideEb', enabled)

  @overload(int)
  def setCurrentIndex(self, index: int) -> None:
    """
    Calls Qt's 'void QTabWidget::setCurrentIndex(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#setCurrentIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QTabWidget::setCurrentIndex(int index)
    self.uglySide.call('ritual_ZN10QTabWidget15setCurrentIndexEi', index)

  @overload(QWidget)
  @overload(NoneType)
  def setCurrentWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QTabWidget::setCurrentWidget(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#setCurrentWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTabWidget::setCurrentWidget(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN10QTabWidget16setCurrentWidgetEP7QWidget',
        self._addressOf(widget),
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
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QTabWidget::QTabWidget(QWidget *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#QTabWidget

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QTabWidget::QTabWidget(QWidget *parent)
    self._noteCreation(QTabWidget, lambda: Rituals.call(
        'ritual_ZN10QTabWidgetC1EP7QWidget', self._addressOf(parent),
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

  @overload(QWidget, str)
  @overload(NoneType, str)
  def addTab(self, widget: Optional[QWidget], a1: str) -> int:
    """
    Calls Qt's 'int QTabWidget::addTab(QWidget *widget, const QString &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#addTab

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QTabWidget::addTab(QWidget *widget, const QString &a1)
    return self.uglySide.call(
        'ritual_ZN10QTabWidget6addTabEP7QWidgetRK7QString',
        self._addressOf(widget), a1,
    )

  @overload(QWidget, QIcon, str)
  @overload(NoneType, QIcon, str)
  def addTab(
      self,
      widget: Optional[QWidget],
      icon: QIcon,
      label: str,
  ) -> int:
    """
    Calls Qt's 'int QTabWidget::addTab(QWidget *widget, const QIcon &icon,
    const QString &label)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#addTab

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QTabWidget::addTab(QWidget *widget, const QIcon &icon, const
    #      QString &label)
    return self.uglySide.call(
        'ritual_ZN10QTabWidget6addTabEP7QWidgetRK5QIconRK7QString',
        self._addressOf(widget), self._valueOf(icon), label,
    )

  @overload(int, QWidget, str)
  @overload(int, NoneType, str)
  def insertTab(self, index: int, widget: Optional[QWidget], a2: str) -> int:
    """
    Calls Qt's 'int QTabWidget::insertTab(int index, QWidget *widget, const
    QString &a2)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#insertTab

    Parameters
    ----------

    index : int
      Passed on as it is.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a2 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QTabWidget::insertTab(int index, QWidget *widget, const QString
    #      &a2)
    return self.uglySide.call(
        'ritual_ZN10QTabWidget9insertTabEiP7QWidgetRK7QString',
        index, self._addressOf(widget), a2,
    )

  @overload(int, QWidget, QIcon, str)
  @overload(int, NoneType, QIcon, str)
  def insertTab(
      self,
      index: int,
      widget: Optional[QWidget],
      icon: QIcon,
      label: str,
  ) -> int:
    """
    Calls Qt's 'int QTabWidget::insertTab(int index, QWidget *widget, const
    QIcon &icon, const QString &label)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#insertTab

    Parameters
    ----------

    index : int
      Passed on as it is.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QTabWidget::insertTab(int index, QWidget *widget, const QIcon
    #      &icon, const QString &label)
    return self.uglySide.call(
        'ritual_ZN10QTabWidget9insertTabEiP7QWidgetRK5QIconRK7QString',
        index, self._addressOf(widget), self._valueOf(icon), label,
    )

  @overload(int)
  def removeTab(self, index: int) -> None:
    """
    Calls Qt's 'void QTabWidget::removeTab(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#removeTab

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QTabWidget::removeTab(int index)
    self.uglySide.call('ritual_ZN10QTabWidget9removeTabEi', index)

  def clear(self) -> None:
    """
    Calls Qt's 'void QTabWidget::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidget.html#clear
    """
    #  void QTabWidget::clear()
    self.uglySide.call('ritual_ZN10QTabWidget5clearEv')
