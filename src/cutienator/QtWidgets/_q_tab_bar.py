"""
QTabBar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qtabbar.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QTabBarButtonPosition, QTabBarSelectionBehavior, QTabBarShape
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPoint, QRect, QSize, QVariant
  from ..QtGui import QColor, QIcon
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QIcon = WAIT['QIcon']
  QPoint = WAIT['QPoint']
  QSize = WAIT['QSize']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTabBar(QWidget):
  """
  The cute side of Qt's QTabBar: a plain Python object standing in front of
  one C++ QTabBar.

  It is built on the cute 'QWidget', as Qt's QTabBar is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTabBar that has a ritual and that Python can call
  so far, 57 names in all: 'metaObject', 'tr', 'shape', 'setShape', 'addTab',
  'insertTab', 'removeTab', 'moveTab', 'isTabEnabled', 'setTabEnabled',
  'isTabVisible', 'setTabVisible', 'tabText', 'setTabText', 'tabTextColor',
  'setTabTextColor', 'tabIcon', 'setTabIcon', 'elideMode', 'setElideMode',
  'setTabToolTip', 'tabToolTip', 'setTabWhatsThis', 'tabWhatsThis',
  'setTabData', 'tabData', 'tabRect', 'tabAt', 'currentIndex', 'count',
  'sizeHint', 'minimumSizeHint', 'setDrawBase', 'drawBase', 'iconSize',
  'setIconSize', 'usesScrollButtons', 'setUsesScrollButtons', 'tabsClosable',
  'setTabsClosable', 'setTabButton', 'tabButton',
  'selectionBehaviorOnRemove', 'setSelectionBehaviorOnRemove', 'expanding',
  'setExpanding', 'isMovable', 'setMovable', 'documentMode',
  'setDocumentMode', 'autoHide', 'setAutoHide', 'changeCurrentOnDrag',
  'setChangeCurrentOnDrag', 'accessibleTabName', 'setAccessibleTabName',
  'setCurrentIndex'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTabBar::~QTabBar()': the destructor: Python never removes a C++
    QTabBar.

  What has no ritual
  ------------------

  32 of the 93 functions Qt declares: 19 protected; 5 a signal; 3 private; 2
  takes or gives a type that cannot be passed yet; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QTabBar is created at the first use, not by 'QTabBar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTabBar.
  - Qt tells when it has removed the C++ QTabBar. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QTabBar, and the names Qt has for the
  #  combinations of its flags enums.
  ButtonPosition = QTabBarButtonPosition
  SelectionBehavior = QTabBarSelectionBehavior
  Shape = QTabBarShape

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
    Calls Qt's 'QString QTabBar::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#tr

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
    #  QString QTabBar::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN7QTabBar2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTabBar'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTabBar::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTabBar::metaObject() const
    address = self.uglySide.call('ritual_ZNK7QTabBar10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def shape(self) -> Shape:
    """
    Calls Qt's 'Shape QTabBar::shape() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#shape

    Returns
    -------

    Shape
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Shape(number)' gives.
    """
    #  Shape QTabBar::shape() const
    return QTabBar.Shape(self.uglySide.call('ritual_ZNK7QTabBar5shapeEv'))

  @overload(int)
  def isTabEnabled(self, index: int) -> bool:
    """
    Calls Qt's 'bool QTabBar::isTabEnabled(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#isTabEnabled

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QTabBar::isTabEnabled(int index) const
    return self.uglySide.call('ritual_ZNK7QTabBar12isTabEnabledEi', index)

  @overload(int)
  def isTabVisible(self, index: int) -> bool:
    """
    Calls Qt's 'bool QTabBar::isTabVisible(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#isTabVisible

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QTabBar::isTabVisible(int index) const
    return self.uglySide.call('ritual_ZNK7QTabBar12isTabVisibleEi', index)

  @overload(int)
  def tabText(self, index: int) -> str:
    """
    Calls Qt's 'QString QTabBar::tabText(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#tabText

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTabBar::tabText(int index) const
    return self.uglySide.call('ritual_ZNK7QTabBar7tabTextEi', index)

  @overload(int)
  def tabTextColor(self, index: int) -> QColor:
    """
    Calls Qt's 'QColor QTabBar::tabTextColor(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#tabTextColor

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QTabBar::tabTextColor(int index) const
    address = self.uglySide.call('ritual_ZNK7QTabBar12tabTextColorEi', index)
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload(int)
  def tabIcon(self, index: int) -> QIcon:
    """
    Calls Qt's 'QIcon QTabBar::tabIcon(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#tabIcon

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QTabBar::tabIcon(int index) const
    address = self.uglySide.call('ritual_ZNK7QTabBar7tabIconEi', index)
    from ..QtGui import QIcon
    return QIcon._cuteOwning(address)

  def elideMode(self) -> Qt.TextElideMode:
    """
    Calls Qt's 'Qt::TextElideMode QTabBar::elideMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#elideMode

    Returns
    -------

    Qt.TextElideMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.TextElideMode(number)'
      gives.
    """
    #  Qt::TextElideMode QTabBar::elideMode() const
    return Qt.TextElideMode(self.uglySide.call(
        'ritual_ZNK7QTabBar9elideModeEv',
    ))

  @overload(int)
  def tabToolTip(self, index: int) -> str:
    """
    Calls Qt's 'QString QTabBar::tabToolTip(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#tabToolTip

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTabBar::tabToolTip(int index) const
    return self.uglySide.call('ritual_ZNK7QTabBar10tabToolTipEi', index)

  @overload(int)
  def tabWhatsThis(self, index: int) -> str:
    """
    Calls Qt's 'QString QTabBar::tabWhatsThis(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#tabWhatsThis

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTabBar::tabWhatsThis(int index) const
    return self.uglySide.call('ritual_ZNK7QTabBar12tabWhatsThisEi', index)

  @overload(int)
  def tabData(self, index: int) -> QVariant:
    """
    Calls Qt's 'QVariant QTabBar::tabData(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#tabData

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QTabBar::tabData(int index) const
    address = self.uglySide.call('ritual_ZNK7QTabBar7tabDataEi', index)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int)
  def tabRect(self, index: int) -> QRect:
    """
    Calls Qt's 'QRect QTabBar::tabRect(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#tabRect

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QTabBar::tabRect(int index) const
    address = self.uglySide.call('ritual_ZNK7QTabBar7tabRectEi', index)
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QPoint)
  def tabAt(self, pos: QPoint) -> int:
    """
    Calls Qt's 'int QTabBar::tabAt(const QPoint &pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#tabAt

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  int QTabBar::tabAt(const QPoint &pos) const
    return self.uglySide.call(
        'ritual_ZNK7QTabBar5tabAtERK6QPoint', self._valueOf(pos),
    )

  def currentIndex(self) -> int:
    """
    Calls Qt's 'int QTabBar::currentIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#currentIndex
    """
    #  int QTabBar::currentIndex() const
    return self.uglySide.call('ritual_ZNK7QTabBar12currentIndexEv')

  def count(self) -> int:
    """
    Calls Qt's 'int QTabBar::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#count
    """
    #  int QTabBar::count() const
    return self.uglySide.call('ritual_ZNK7QTabBar5countEv')

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QTabBar::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QTabBar::sizeHint() const
    address = self.uglySide.call('ritual_ZNK7QTabBar8sizeHintEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QTabBar::minimumSizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#minimumSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QTabBar::minimumSizeHint() const
    address = self.uglySide.call('ritual_ZNK7QTabBar15minimumSizeHintEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def drawBase(self) -> bool:
    """
    Calls Qt's 'bool QTabBar::drawBase() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#drawBase
    """
    #  bool QTabBar::drawBase() const
    return self.uglySide.call('ritual_ZNK7QTabBar8drawBaseEv')

  def iconSize(self) -> QSize:
    """
    Calls Qt's 'QSize QTabBar::iconSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#iconSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QTabBar::iconSize() const
    address = self.uglySide.call('ritual_ZNK7QTabBar8iconSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def usesScrollButtons(self) -> bool:
    """
    Calls Qt's 'bool QTabBar::usesScrollButtons() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#usesScrollButtons
    """
    #  bool QTabBar::usesScrollButtons() const
    return self.uglySide.call('ritual_ZNK7QTabBar17usesScrollButtonsEv')

  def tabsClosable(self) -> bool:
    """
    Calls Qt's 'bool QTabBar::tabsClosable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#tabsClosable
    """
    #  bool QTabBar::tabsClosable() const
    return self.uglySide.call('ritual_ZNK7QTabBar12tabsClosableEv')

  @overload(int, ButtonPosition)
  def tabButton(
      self,
      index: int,
      position: ButtonPosition,
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QTabBar::tabButton(int index, ButtonPosition
    position) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#tabButton

    Parameters
    ----------

    index : int
      Passed on as it is.

    position : ButtonPosition
      Passed on as its number.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QTabBar::tabButton(int index, ButtonPosition position) const
    address = self.uglySide.call(
        'ritual_ZNK7QTabBar9tabButtonEiNS_14ButtonPositionE',
        index, position.value,
    )
    return QWidget._cuteAt(address)

  def selectionBehaviorOnRemove(self) -> SelectionBehavior:
    """
    Calls Qt's 'SelectionBehavior QTabBar::selectionBehaviorOnRemove()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtabbar.html#selectionBehaviorOnRemove

    Returns
    -------

    SelectionBehavior
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'SelectionBehavior(number)' gives.
    """
    #  SelectionBehavior QTabBar::selectionBehaviorOnRemove() const
    return QTabBar.SelectionBehavior(self.uglySide.call(
        'ritual_ZNK7QTabBar25selectionBehaviorOnRemoveEv',
    ))

  def expanding(self) -> bool:
    """
    Calls Qt's 'bool QTabBar::expanding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#expanding
    """
    #  bool QTabBar::expanding() const
    return self.uglySide.call('ritual_ZNK7QTabBar9expandingEv')

  def isMovable(self) -> bool:
    """
    Calls Qt's 'bool QTabBar::isMovable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#isMovable
    """
    #  bool QTabBar::isMovable() const
    return self.uglySide.call('ritual_ZNK7QTabBar9isMovableEv')

  def documentMode(self) -> bool:
    """
    Calls Qt's 'bool QTabBar::documentMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#documentMode
    """
    #  bool QTabBar::documentMode() const
    return self.uglySide.call('ritual_ZNK7QTabBar12documentModeEv')

  def autoHide(self) -> bool:
    """
    Calls Qt's 'bool QTabBar::autoHide() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#autoHide
    """
    #  bool QTabBar::autoHide() const
    return self.uglySide.call('ritual_ZNK7QTabBar8autoHideEv')

  def changeCurrentOnDrag(self) -> bool:
    """
    Calls Qt's 'bool QTabBar::changeCurrentOnDrag() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#changeCurrentOnDrag
    """
    #  bool QTabBar::changeCurrentOnDrag() const
    return self.uglySide.call('ritual_ZNK7QTabBar19changeCurrentOnDragEv')

  @overload(int)
  def accessibleTabName(self, index: int) -> str:
    """
    Calls Qt's 'QString QTabBar::accessibleTabName(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#accessibleTabName

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTabBar::accessibleTabName(int index) const
    return self.uglySide.call(
        'ritual_ZNK7QTabBar17accessibleTabNameEi', index,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Shape)
  def setShape(self, shape: Shape) -> None:
    """
    Calls Qt's 'void QTabBar::setShape(Shape shape)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#setShape

    Parameters
    ----------

    shape : Shape
      Passed on as its number.
    """
    #  void QTabBar::setShape(Shape shape)
    self.uglySide.call('ritual_ZN7QTabBar8setShapeENS_5ShapeE', shape.value)

  @overload(int, bool)
  def setTabEnabled(self, index: int, enabled: bool) -> None:
    """
    Calls Qt's 'void QTabBar::setTabEnabled(int index, bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#setTabEnabled

    Parameters
    ----------

    index : int
      Passed on as it is.

    enabled : bool
      Passed on as it is.
    """
    #  void QTabBar::setTabEnabled(int index, bool enabled)
    self.uglySide.call('ritual_ZN7QTabBar13setTabEnabledEib', index, enabled)

  @overload(int, bool)
  def setTabVisible(self, index: int, visible: bool) -> None:
    """
    Calls Qt's 'void QTabBar::setTabVisible(int index, bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#setTabVisible

    Parameters
    ----------

    index : int
      Passed on as it is.

    visible : bool
      Passed on as it is.
    """
    #  void QTabBar::setTabVisible(int index, bool visible)
    self.uglySide.call('ritual_ZN7QTabBar13setTabVisibleEib', index, visible)

  @overload(int, str)
  def setTabText(self, index: int, text: str) -> None:
    """
    Calls Qt's 'void QTabBar::setTabText(int index, const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#setTabText

    Parameters
    ----------

    index : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTabBar::setTabText(int index, const QString &text)
    self.uglySide.call(
        'ritual_ZN7QTabBar10setTabTextEiRK7QString', index, text,
    )

  @overload(int, QColor)
  def setTabTextColor(self, index: int, color: QColor) -> None:
    """
    Calls Qt's 'void QTabBar::setTabTextColor(int index, const QColor
    &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#setTabTextColor

    Parameters
    ----------

    index : int
      Passed on as it is.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QTabBar::setTabTextColor(int index, const QColor &color)
    self.uglySide.call(
        'ritual_ZN7QTabBar15setTabTextColorEiRK6QColor',
        index, self._valueOf(color),
    )

  @overload(int, QIcon)
  def setTabIcon(self, index: int, icon: QIcon) -> None:
    """
    Calls Qt's 'void QTabBar::setTabIcon(int index, const QIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#setTabIcon

    Parameters
    ----------

    index : int
      Passed on as it is.

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.
    """
    #  void QTabBar::setTabIcon(int index, const QIcon &icon)
    self.uglySide.call(
        'ritual_ZN7QTabBar10setTabIconEiRK5QIcon',
        index, self._valueOf(icon),
    )

  @overload(Qt.TextElideMode)
  def setElideMode(self, mode: Qt.TextElideMode) -> None:
    """
    Calls Qt's 'void QTabBar::setElideMode(Qt::TextElideMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#setElideMode

    Parameters
    ----------

    mode : Qt.TextElideMode
      Passed on as its number.
    """
    #  void QTabBar::setElideMode(Qt::TextElideMode mode)
    self.uglySide.call(
        'ritual_ZN7QTabBar12setElideModeEN2Qt13TextElideModeE', mode.value,
    )

  @overload(int, str)
  def setTabToolTip(self, index: int, tip: str) -> None:
    """
    Calls Qt's 'void QTabBar::setTabToolTip(int index, const QString &tip)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#setTabToolTip

    Parameters
    ----------

    index : int
      Passed on as it is.

    tip : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTabBar::setTabToolTip(int index, const QString &tip)
    self.uglySide.call(
        'ritual_ZN7QTabBar13setTabToolTipEiRK7QString', index, tip,
    )

  @overload(int, str)
  def setTabWhatsThis(self, index: int, text: str) -> None:
    """
    Calls Qt's 'void QTabBar::setTabWhatsThis(int index, const QString
    &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#setTabWhatsThis

    Parameters
    ----------

    index : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTabBar::setTabWhatsThis(int index, const QString &text)
    self.uglySide.call(
        'ritual_ZN7QTabBar15setTabWhatsThisEiRK7QString', index, text,
    )

  @overload(int, QVariant)
  def setTabData(self, index: int, data: QVariant) -> None:
    """
    Calls Qt's 'void QTabBar::setTabData(int index, const QVariant &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#setTabData

    Parameters
    ----------

    index : int
      Passed on as it is.

    data : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QTabBar::setTabData(int index, const QVariant &data)
    self.uglySide.call(
        'ritual_ZN7QTabBar10setTabDataEiRK8QVariant',
        index, self._valueOf(data),
    )

  @overload(bool)
  def setDrawBase(self, drawTheBase: bool) -> None:
    """
    Calls Qt's 'void QTabBar::setDrawBase(bool drawTheBase)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#setDrawBase

    Parameters
    ----------

    drawTheBase : bool
      Passed on as it is.
    """
    #  void QTabBar::setDrawBase(bool drawTheBase)
    self.uglySide.call('ritual_ZN7QTabBar11setDrawBaseEb', drawTheBase)

  @overload(QSize)
  def setIconSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QTabBar::setIconSize(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#setIconSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QTabBar::setIconSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN7QTabBar11setIconSizeERK5QSize', self._valueOf(size),
    )

  @overload(bool)
  def setUsesScrollButtons(self, useButtons: bool) -> None:
    """
    Calls Qt's 'void QTabBar::setUsesScrollButtons(bool useButtons)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#setUsesScrollButtons

    Parameters
    ----------

    useButtons : bool
      Passed on as it is.
    """
    #  void QTabBar::setUsesScrollButtons(bool useButtons)
    self.uglySide.call(
        'ritual_ZN7QTabBar20setUsesScrollButtonsEb', useButtons,
    )

  @overload(bool)
  def setTabsClosable(self, closable: bool) -> None:
    """
    Calls Qt's 'void QTabBar::setTabsClosable(bool closable)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#setTabsClosable

    Parameters
    ----------

    closable : bool
      Passed on as it is.
    """
    #  void QTabBar::setTabsClosable(bool closable)
    self.uglySide.call('ritual_ZN7QTabBar15setTabsClosableEb', closable)

  @overload(int, ButtonPosition, QWidget)
  @overload(int, ButtonPosition, NoneType)
  def setTabButton(
      self,
      index: int,
      position: ButtonPosition,
      widget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QTabBar::setTabButton(int index, ButtonPosition
    position, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#setTabButton

    Parameters
    ----------

    index : int
      Passed on as it is.

    position : ButtonPosition
      Passed on as its number.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTabBar::setTabButton(int index, ButtonPosition position, QWidget
    #      *widget)
    self.uglySide.call(
        'ritual_ZN7QTabBar12setTabButtonEiNS_14ButtonPositionEP7QWidget',
        index, position.value, self._addressOf(widget),
    )

  @overload(SelectionBehavior)
  def setSelectionBehaviorOnRemove(
      self,
      behavior: SelectionBehavior,
  ) -> None:
    """
    Calls Qt's 'void QTabBar::setSelectionBehaviorOnRemove(SelectionBehavior
    behavior)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtabbar.html#setSelectionBehaviorOnRemove

    Parameters
    ----------

    behavior : SelectionBehavior
      Passed on as its number.
    """
    #  void QTabBar::setSelectionBehaviorOnRemove(SelectionBehavior behavior)
    self.uglySide.call(
        'ritual_ZN7QTabBar28setSelectionBehaviorOnRemoveENS_17SelectionBeha'
        'viorE',
        behavior.value,
    )

  @overload(bool)
  def setExpanding(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QTabBar::setExpanding(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#setExpanding

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QTabBar::setExpanding(bool enabled)
    self.uglySide.call('ritual_ZN7QTabBar12setExpandingEb', enabled)

  @overload(bool)
  def setMovable(self, movable: bool) -> None:
    """
    Calls Qt's 'void QTabBar::setMovable(bool movable)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#setMovable

    Parameters
    ----------

    movable : bool
      Passed on as it is.
    """
    #  void QTabBar::setMovable(bool movable)
    self.uglySide.call('ritual_ZN7QTabBar10setMovableEb', movable)

  @overload(bool)
  def setDocumentMode(self, set: bool) -> None:
    """
    Calls Qt's 'void QTabBar::setDocumentMode(bool set)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#setDocumentMode

    Parameters
    ----------

    set : bool
      Passed on as it is.
    """
    #  void QTabBar::setDocumentMode(bool set)
    self.uglySide.call('ritual_ZN7QTabBar15setDocumentModeEb', set)

  @overload(bool)
  def setAutoHide(self, hide: bool) -> None:
    """
    Calls Qt's 'void QTabBar::setAutoHide(bool hide)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#setAutoHide

    Parameters
    ----------

    hide : bool
      Passed on as it is.
    """
    #  void QTabBar::setAutoHide(bool hide)
    self.uglySide.call('ritual_ZN7QTabBar11setAutoHideEb', hide)

  @overload(bool)
  def setChangeCurrentOnDrag(self, change: bool) -> None:
    """
    Calls Qt's 'void QTabBar::setChangeCurrentOnDrag(bool change)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtabbar.html#setChangeCurrentOnDrag

    Parameters
    ----------

    change : bool
      Passed on as it is.
    """
    #  void QTabBar::setChangeCurrentOnDrag(bool change)
    self.uglySide.call('ritual_ZN7QTabBar22setChangeCurrentOnDragEb', change)

  @overload(int, str)
  def setAccessibleTabName(self, index: int, name: str) -> None:
    """
    Calls Qt's 'void QTabBar::setAccessibleTabName(int index, const QString
    &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#setAccessibleTabName

    Parameters
    ----------

    index : int
      Passed on as it is.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTabBar::setAccessibleTabName(int index, const QString &name)
    self.uglySide.call(
        'ritual_ZN7QTabBar20setAccessibleTabNameEiRK7QString', index, name,
    )

  @overload(int)
  def setCurrentIndex(self, index: int) -> None:
    """
    Calls Qt's 'void QTabBar::setCurrentIndex(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#setCurrentIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QTabBar::setCurrentIndex(int index)
    self.uglySide.call('ritual_ZN7QTabBar15setCurrentIndexEi', index)

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
    Notes what was given, for Qt's 'QTabBar::QTabBar(QWidget *parent)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#QTabBar

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QTabBar::QTabBar(QWidget *parent)
    self._noteCreation(QTabBar, lambda: Rituals.call(
        'ritual_ZN7QTabBarC1EP7QWidget', self._addressOf(parent),
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

  @overload(str)
  def addTab(self, text: str) -> int:
    """
    Calls Qt's 'int QTabBar::addTab(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#addTab

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QTabBar::addTab(const QString &text)
    return self.uglySide.call('ritual_ZN7QTabBar6addTabERK7QString', text)

  @overload(QIcon, str)
  def addTab(self, icon: QIcon, text: str) -> int:
    """
    Calls Qt's 'int QTabBar::addTab(const QIcon &icon, const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#addTab

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QTabBar::addTab(const QIcon &icon, const QString &text)
    return self.uglySide.call(
        'ritual_ZN7QTabBar6addTabERK5QIconRK7QString',
        self._valueOf(icon), text,
    )

  @overload(int, str)
  def insertTab(self, index: int, text: str) -> int:
    """
    Calls Qt's 'int QTabBar::insertTab(int index, const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#insertTab

    Parameters
    ----------

    index : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QTabBar::insertTab(int index, const QString &text)
    return self.uglySide.call(
        'ritual_ZN7QTabBar9insertTabEiRK7QString', index, text,
    )

  @overload(int, QIcon, str)
  def insertTab(self, index: int, icon: QIcon, text: str) -> int:
    """
    Calls Qt's 'int QTabBar::insertTab(int index, const QIcon &icon, const
    QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#insertTab

    Parameters
    ----------

    index : int
      Passed on as it is.

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QTabBar::insertTab(int index, const QIcon &icon, const QString
    #      &text)
    return self.uglySide.call(
        'ritual_ZN7QTabBar9insertTabEiRK5QIconRK7QString',
        index, self._valueOf(icon), text,
    )

  @overload(int)
  def removeTab(self, index: int) -> None:
    """
    Calls Qt's 'void QTabBar::removeTab(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#removeTab

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QTabBar::removeTab(int index)
    self.uglySide.call('ritual_ZN7QTabBar9removeTabEi', index)

  @overload(int, int)
  def moveTab(self, from_: int, to: int) -> None:
    """
    Calls Qt's 'void QTabBar::moveTab(int from, int to)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabbar.html#moveTab

    Parameters
    ----------

    from_ : int
      Passed on as it is.

    to : int
      Passed on as it is.
    """
    #  void QTabBar::moveTab(int from, int to)
    self.uglySide.call('ritual_ZN7QTabBar7moveTabEii', from_, to)
