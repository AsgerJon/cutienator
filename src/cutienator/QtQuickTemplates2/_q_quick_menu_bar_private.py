"""
QQuickMenuBarPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmenubar_p_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickMenuBarPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQuickContainerPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QPalette, QPlatformMenuBar, QWindow
  from ..QtQuick import QQuickItem
  from . import QQuickMenu, QQuickMenuBar, QQuickMenuBarItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickItem = WAIT['QQuickItem']
  QQuickMenu = WAIT['QQuickMenu']
  QQuickMenuBar = WAIT['QQuickMenuBar']
  QQuickMenuBarItem = WAIT['QQuickMenuBarItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickMenuBarPrivate(QQuickContainerPrivate):
  """
  The cute side of Qt's QQuickMenuBarPrivate: a plain Python object standing
  in front of one C++ QQuickMenuBarPrivate.

  It is built on the cute 'QQuickContainerPrivate', as Qt's
  QQuickMenuBarPrivate is built on Qt's QQuickContainerPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickMenuBarPrivate that has a ritual and that
  Python can call so far, 31 names in all: 'q_func', 'get',
  'createItemFromDelegate', 'createMenuBarItem', 'openCurrentMenu',
  'closeCurrentMenu', 'activateMenuItem', 'activateItem', 'activateNextItem',
  'activatePreviousItem', 'onItemHovered', 'onItemTriggered',
  'onMenuAboutToHide', 'insertMenu', 'takeMenu', 'insertNativeMenu',
  'removeNativeMenu', 'syncMenuBarItemVisibilty', 'window', 'menuIndex',
  'nativeHandle', 'useNativeMenuBar', 'useNativeMenu',
  'syncNativeMenuBarVisible', 'createNativeMenuBar', 'removeNativeMenuBar',
  'getContentWidth', 'getContentHeight', 'itemImplicitWidthChanged',
  'itemImplicitHeightChanged', 'defaultPalette'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickMenuBar *QQuickMenuBarPrivate::q_func() const': takes
    in Python what 'QQuickMenuBar *QQuickMenuBarPrivate::q_func()' takes.
  - Qt's 'QQmlListProperty<QQuickMenu> QQuickMenuBarPrivate::menus()': gives
    a type Python has no way to take yet.
  - Qt's 'QQmlListProperty<QObject> QQuickMenuBarPrivate::contentData()':
    gives a type Python has no way to take yet.
  - Qt's 'void
    QQuickMenuBarPrivate::contentData_append(QQmlListProperty<QObject> *prop,
    QObject *obj)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
  - Qt's 'void
    QQuickMenuBarPrivate::menus_append(QQmlListProperty<QQuickMenu> *prop,
    QQuickMenu *obj)': names 'QQmlListProperty<QQuickMenu>', which has no
    cute class yet.
  - Qt's 'qsizetype
    QQuickMenuBarPrivate::menus_count(QQmlListProperty<QQuickMenu> *prop)':
    names 'QQmlListProperty<QQuickMenu>', which has no cute class yet.
  - Qt's 'QQuickMenu
    *QQuickMenuBarPrivate::menus_at(QQmlListProperty<QQuickMenu> *prop,
    qsizetype index)': names 'QQmlListProperty<QQuickMenu>', which has no
    cute class yet.
  - Qt's 'void QQuickMenuBarPrivate::menus_clear(QQmlListProperty<QQuickMenu>
    *prop)': names 'QQmlListProperty<QQuickMenu>', which has no cute class
    yet.

  What to expect
  --------------

  - The C++ QQuickMenuBarPrivate is created at the first use, not by
    'QQuickMenuBarPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickMenuBarPrivate.
  - Each name of Qt's QQuickMenuBarPrivate that has no cute function yet,
    'menus', 'menus_append', 'menus_at', 'menus_clear', 'menus_count', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickMenuBar)
  @overload(NoneType)
  def get(
      menuBar: Optional[QQuickMenuBar],
  ) -> Optional[QQuickMenuBarPrivate]:
    """
    Calls Qt's 'QQuickMenuBarPrivate *QQuickMenuBarPrivate::get(QQuickMenuBar
    *menuBar)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubarprivate.html#get

    Parameters
    ----------

    menuBar : Optional[QQuickMenuBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickMenuBarPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMenuBarPrivate *QQuickMenuBarPrivate::get(QQuickMenuBar
    #      *menuBar)
    address = Rituals.call(
        'ritual_ZN20QQuickMenuBarPrivate3getEP13QQuickMenuBar',
        CuteMixin._addressOf(menuBar),
    )
    return QQuickMenuBarPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickMenuBarPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def window(self) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QQuickMenuBarPrivate::window() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubarprivate.html#window

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QQuickMenuBarPrivate::window() const
    address = self.uglySide.call('ritual_ZNK20QQuickMenuBarPrivate6windowEv')
    from ..QtGui import QWindow
    return QWindow._cuteAt(address)

  @overload(QQuickMenu)
  @overload(NoneType)
  def menuIndex(self, menu: Optional[QQuickMenu]) -> int:
    """
    Calls Qt's 'int QQuickMenuBarPrivate::menuIndex(QQuickMenu *menu) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubarprivate.html#menuIndex

    Parameters
    ----------

    menu : Optional[QQuickMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QQuickMenuBarPrivate::menuIndex(QQuickMenu *menu) const
    return self.uglySide.call(
        'ritual_ZNK20QQuickMenuBarPrivate9menuIndexEP10QQuickMenu',
        self._addressOf(menu),
    )

  def nativeHandle(self) -> Optional[QPlatformMenuBar]:
    """
    Calls Qt's 'QPlatformMenuBar *QQuickMenuBarPrivate::nativeHandle()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubarprivate.html#nativeHandle

    Returns
    -------

    Optional[QPlatformMenuBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMenuBar *QQuickMenuBarPrivate::nativeHandle() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickMenuBarPrivate12nativeHandleEv',
    )
    from ..QtGui import QPlatformMenuBar
    return QPlatformMenuBar._cuteAt(address)

  def useNativeMenuBar(self) -> bool:
    """
    Calls Qt's 'bool QQuickMenuBarPrivate::useNativeMenuBar() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubarprivate.html#useNativeMenuBar
    """
    #  bool QQuickMenuBarPrivate::useNativeMenuBar() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickMenuBarPrivate16useNativeMenuBarEv',
    )

  @overload(QQuickMenu)
  @overload(NoneType)
  def useNativeMenu(self, menu: Optional[QQuickMenu]) -> bool:
    """
    Calls Qt's 'bool QQuickMenuBarPrivate::useNativeMenu(const QQuickMenu
    *menu) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubarprivate.html#useNativeMenu

    Parameters
    ----------

    menu : Optional[QQuickMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickMenuBarPrivate::useNativeMenu(const QQuickMenu *menu) const
    return self.uglySide.call(
        'ritual_ZNK20QQuickMenuBarPrivate13useNativeMenuEPK10QQuickMenu',
        self._addressOf(menu),
    )

  def getContentWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickMenuBarPrivate::getContentWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubarprivate.html#getContentWidth
    """
    #  qreal QQuickMenuBarPrivate::getContentWidth() const
    ritual = 'ritual_ZNK20QQuickMenuBarPrivate15getContentWidthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QQuickMenuBarPrivate15getContentWidthEv'
    return self.uglySide.call(ritual)

  def getContentHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickMenuBarPrivate::getContentHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubarprivate.html#getContentHeight
    """
    #  qreal QQuickMenuBarPrivate::getContentHeight() const
    ritual = 'ritual_ZNK20QQuickMenuBarPrivate16getContentHeightEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QQuickMenuBarPrivate16getContentHeightEv'
    return self.uglySide.call(ritual)

  def defaultPalette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QQuickMenuBarPrivate::defaultPalette() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubarprivate.html#defaultPalette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QQuickMenuBarPrivate::defaultPalette() const
    ritual = 'ritual_ZNK20QQuickMenuBarPrivate14defaultPaletteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QQuickMenuBarPrivate14defaultPaletteEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  def q_func(self) -> Optional[QQuickMenuBar]:
    """
    Calls Qt's 'QQuickMenuBar *QQuickMenuBarPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubarprivate.html#q_func

    Returns
    -------

    Optional[QQuickMenuBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMenuBar *QQuickMenuBarPrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QQuickMenuBarPrivate6q_funcEv')
    from . import QQuickMenuBar
    return QQuickMenuBar._cuteAt(address)

  def createItemFromDelegate(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickMenuBarPrivate::createItemFromDelegate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubarprivate.html#createItemFromDelegate

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickMenuBarPrivate::createItemFromDelegate()
    address = self.uglySide.call(
        'ritual_ZN20QQuickMenuBarPrivate22createItemFromDelegateEv',
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  @overload(QQuickMenu)
  @overload(NoneType)
  def createMenuBarItem(
      self,
      menu: Optional[QQuickMenu],
  ) -> Optional[QQuickMenuBarItem]:
    """
    Calls Qt's 'QQuickMenuBarItem
    *QQuickMenuBarPrivate::createMenuBarItem(QQuickMenu *menu)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubarprivate.html#createMenuBarItem

    Parameters
    ----------

    menu : Optional[QQuickMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickMenuBarItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMenuBarItem *QQuickMenuBarPrivate::createMenuBarItem(QQuickMenu
    #      *menu)
    address = self.uglySide.call(
        'ritual_ZN20QQuickMenuBarPrivate17createMenuBarItemEP10QQuickMenu',
        self._addressOf(menu),
    )
    from . import QQuickMenuBarItem
    return QQuickMenuBarItem._cuteAt(address)

  def openCurrentMenu(self) -> None:
    """
    Calls Qt's 'void QQuickMenuBarPrivate::openCurrentMenu()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubarprivate.html#openCurrentMenu
    """
    #  void QQuickMenuBarPrivate::openCurrentMenu()
    self.uglySide.call('ritual_ZN20QQuickMenuBarPrivate15openCurrentMenuEv')

  def closeCurrentMenu(self) -> None:
    """
    Calls Qt's 'void QQuickMenuBarPrivate::closeCurrentMenu()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubarprivate.html#closeCurrentMenu
    """
    #  void QQuickMenuBarPrivate::closeCurrentMenu()
    self.uglySide.call('ritual_ZN20QQuickMenuBarPrivate16closeCurrentMenuEv')

  @overload(int)
  def activateMenuItem(self, index: int) -> None:
    """
    Calls Qt's 'void QQuickMenuBarPrivate::activateMenuItem(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubarprivate.html#activateMenuItem

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQuickMenuBarPrivate::activateMenuItem(int index)
    self.uglySide.call(
        'ritual_ZN20QQuickMenuBarPrivate16activateMenuItemEi', index,
    )

  @overload(QQuickMenuBarItem)
  @overload(NoneType)
  def activateItem(self, item: Optional[QQuickMenuBarItem]) -> None:
    """
    Calls Qt's 'void QQuickMenuBarPrivate::activateItem(QQuickMenuBarItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubarprivate.html#activateItem

    Parameters
    ----------

    item : Optional[QQuickMenuBarItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuBarPrivate::activateItem(QQuickMenuBarItem *item)
    self.uglySide.call(
        'ritual_ZN20QQuickMenuBarPrivate12activateItemEP17QQuickMenuBarItem',
        self._addressOf(item),
    )

  def activateNextItem(self) -> None:
    """
    Calls Qt's 'void QQuickMenuBarPrivate::activateNextItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubarprivate.html#activateNextItem
    """
    #  void QQuickMenuBarPrivate::activateNextItem()
    self.uglySide.call('ritual_ZN20QQuickMenuBarPrivate16activateNextItemEv')

  def activatePreviousItem(self) -> None:
    """
    Calls Qt's 'void QQuickMenuBarPrivate::activatePreviousItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubarprivate.html#activatePreviousItem
    """
    #  void QQuickMenuBarPrivate::activatePreviousItem()
    self.uglySide.call(
        'ritual_ZN20QQuickMenuBarPrivate20activatePreviousItemEv',
    )

  def onItemHovered(self) -> None:
    """
    Calls Qt's 'void QQuickMenuBarPrivate::onItemHovered()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubarprivate.html#onItemHovered
    """
    #  void QQuickMenuBarPrivate::onItemHovered()
    self.uglySide.call('ritual_ZN20QQuickMenuBarPrivate13onItemHoveredEv')

  def onItemTriggered(self) -> None:
    """
    Calls Qt's 'void QQuickMenuBarPrivate::onItemTriggered()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubarprivate.html#onItemTriggered
    """
    #  void QQuickMenuBarPrivate::onItemTriggered()
    self.uglySide.call('ritual_ZN20QQuickMenuBarPrivate15onItemTriggeredEv')

  @overload(QQuickMenu)
  @overload(NoneType)
  def onMenuAboutToHide(self, menu: Optional[QQuickMenu]) -> None:
    """
    Calls Qt's 'void QQuickMenuBarPrivate::onMenuAboutToHide(QQuickMenu
    *menu)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubarprivate.html#onMenuAboutToHide

    Parameters
    ----------

    menu : Optional[QQuickMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuBarPrivate::onMenuAboutToHide(QQuickMenu *menu)
    self.uglySide.call(
        'ritual_ZN20QQuickMenuBarPrivate17onMenuAboutToHideEP10QQuickMenu',
        self._addressOf(menu),
    )

  @overload(int, QQuickMenu, QQuickMenuBarItem)
  @overload(int, QQuickMenu, NoneType)
  @overload(int, NoneType, QQuickMenuBarItem)
  @overload(int, NoneType, NoneType)
  def insertMenu(
      self,
      index: int,
      menu: Optional[QQuickMenu],
      delegateItem: Optional[QQuickMenuBarItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickMenuBarPrivate::insertMenu(int index, QQuickMenu
    *menu, QQuickMenuBarItem *delegateItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubarprivate.html#insertMenu

    Parameters
    ----------

    index : int
      Passed on as it is.

    menu : Optional[QQuickMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    delegateItem : Optional[QQuickMenuBarItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuBarPrivate::insertMenu(int index, QQuickMenu *menu,
    #      QQuickMenuBarItem *delegateItem)
    self.uglySide.call(
        'ritual_ZN20QQuickMenuBarPrivate10insertMenuEiP10QQuickMenuP17QQuic'
        'kMenuBarItem',
        index, self._addressOf(menu), self._addressOf(delegateItem),
    )

  @overload(int)
  def takeMenu(self, index: int) -> Optional[QQuickMenu]:
    """
    Calls Qt's 'QQuickMenu *QQuickMenuBarPrivate::takeMenu(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubarprivate.html#takeMenu

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QQuickMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMenu *QQuickMenuBarPrivate::takeMenu(int index)
    address = self.uglySide.call(
        'ritual_ZN20QQuickMenuBarPrivate8takeMenuEi', index,
    )
    from . import QQuickMenu
    return QQuickMenu._cuteAt(address)

  @overload(QQuickMenu)
  @overload(NoneType)
  def insertNativeMenu(self, menu: Optional[QQuickMenu]) -> None:
    """
    Calls Qt's 'void QQuickMenuBarPrivate::insertNativeMenu(QQuickMenu
    *menu)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubarprivate.html#insertNativeMenu

    Parameters
    ----------

    menu : Optional[QQuickMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuBarPrivate::insertNativeMenu(QQuickMenu *menu)
    self.uglySide.call(
        'ritual_ZN20QQuickMenuBarPrivate16insertNativeMenuEP10QQuickMenu',
        self._addressOf(menu),
    )

  @overload(QQuickMenu)
  @overload(NoneType)
  def removeNativeMenu(self, menu: Optional[QQuickMenu]) -> None:
    """
    Calls Qt's 'void QQuickMenuBarPrivate::removeNativeMenu(QQuickMenu
    *menu)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubarprivate.html#removeNativeMenu

    Parameters
    ----------

    menu : Optional[QQuickMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuBarPrivate::removeNativeMenu(QQuickMenu *menu)
    self.uglySide.call(
        'ritual_ZN20QQuickMenuBarPrivate16removeNativeMenuEP10QQuickMenu',
        self._addressOf(menu),
    )

  @overload(QQuickMenuBarItem)
  @overload(NoneType)
  def syncMenuBarItemVisibilty(
      self,
      menuBarItem: Optional[QQuickMenuBarItem],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickMenuBarPrivate::syncMenuBarItemVisibilty(QQuickMenuBarItem
    *menuBarItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubarprivate.html#syncMenuBarItemVisibilty

    Parameters
    ----------

    menuBarItem : Optional[QQuickMenuBarItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuBarPrivate::syncMenuBarItemVisibilty(QQuickMenuBarItem
    #      *menuBarItem)
    self.uglySide.call(
        'ritual_ZN20QQuickMenuBarPrivate24syncMenuBarItemVisibiltyEP17QQuic'
        'kMenuBarItem',
        self._addressOf(menuBarItem),
    )

  def syncNativeMenuBarVisible(self) -> None:
    """
    Calls Qt's 'void QQuickMenuBarPrivate::syncNativeMenuBarVisible()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubarprivate.html#syncNativeMenuBarVisible
    """
    #  void QQuickMenuBarPrivate::syncNativeMenuBarVisible()
    self.uglySide.call(
        'ritual_ZN20QQuickMenuBarPrivate24syncNativeMenuBarVisibleEv',
    )

  def createNativeMenuBar(self) -> None:
    """
    Calls Qt's 'void QQuickMenuBarPrivate::createNativeMenuBar()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubarprivate.html#createNativeMenuBar
    """
    #  void QQuickMenuBarPrivate::createNativeMenuBar()
    self.uglySide.call(
        'ritual_ZN20QQuickMenuBarPrivate19createNativeMenuBarEv',
    )

  def removeNativeMenuBar(self) -> None:
    """
    Calls Qt's 'void QQuickMenuBarPrivate::removeNativeMenuBar()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubarprivate.html#removeNativeMenuBar
    """
    #  void QQuickMenuBarPrivate::removeNativeMenuBar()
    self.uglySide.call(
        'ritual_ZN20QQuickMenuBarPrivate19removeNativeMenuBarEv',
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitWidthChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickMenuBarPrivate::itemImplicitWidthChanged(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubarprivate.html#itemImplicitWidthChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuBarPrivate::itemImplicitWidthChanged(QQuickItem *item)
    ritual = (
        'ritual_ZN20QQuickMenuBarPrivate24itemImplicitWidthChangedEP10QQuic'
        'kItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickMenuBarPrivate24itemImplicitWidthChangedEP1'
          '0QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitHeightChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickMenuBarPrivate::itemImplicitHeightChanged(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubarprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuBarPrivate::itemImplicitHeightChanged(QQuickItem *item)
    ritual = (
        'ritual_ZN20QQuickMenuBarPrivate25itemImplicitHeightChangedEP10QQui'
        'ckItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickMenuBarPrivate25itemImplicitHeightChangedEP'
          '10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @staticmethod
  def menus(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickMenu> QQuickMenuBarPrivate::menus()': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickMenuBarPrivate.menus' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuickMenu> QQuickMenuBarPrivate::menus()': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def menus_append(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickMenuBarPrivate::menus_append(QQmlListProperty<QQuickMenu> *prop,
    QQuickMenu *obj)': names 'QQmlListProperty<QQuickMenu>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QQuickMenuBarPrivate.menus_append' has no cute function yet. Qt's "
        "'void "
        "QQuickMenuBarPrivate::menus_append(QQmlListProperty<QQuickMenu> "
        "*prop, QQuickMenu *obj)': names 'QQmlListProperty<QQuickMenu>', "
        "which has no cute class yet.")

  @staticmethod
  def menus_at(*__, **_) -> Never:
    """
    Qt's 'QQuickMenu
    *QQuickMenuBarPrivate::menus_at(QQmlListProperty<QQuickMenu> *prop,
    qsizetype index)': names 'QQmlListProperty<QQuickMenu>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QQuickMenuBarPrivate.menus_at' has no cute function yet. Qt's "
        "'QQuickMenu "
        "*QQuickMenuBarPrivate::menus_at(QQmlListProperty<QQuickMenu> "
        "*prop, qsizetype index)': names 'QQmlListProperty<QQuickMenu>', "
        "which has no cute class yet.")

  @staticmethod
  def menus_clear(*__, **_) -> Never:
    """
    Qt's 'void QQuickMenuBarPrivate::menus_clear(QQmlListProperty<QQuickMenu>
    *prop)': names 'QQmlListProperty<QQuickMenu>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQuickMenuBarPrivate.menus_clear' has no cute function yet. Qt's "
        "'void "
        "QQuickMenuBarPrivate::menus_clear(QQmlListProperty<QQuickMenu> "
        "*prop)': names 'QQmlListProperty<QQuickMenu>', which has no cute "
        "class yet.")

  @staticmethod
  def menus_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QQuickMenuBarPrivate::menus_count(QQmlListProperty<QQuickMenu> *prop)':
    names 'QQmlListProperty<QQuickMenu>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickMenuBarPrivate.menus_count' has no cute function yet. Qt's "
        "'qsizetype "
        "QQuickMenuBarPrivate::menus_count(QQmlListProperty<QQuickMenu> "
        "*prop)': names 'QQmlListProperty<QQuickMenu>', which has no cute "
        "class yet.")
