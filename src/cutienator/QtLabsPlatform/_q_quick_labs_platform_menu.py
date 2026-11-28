"""
QQuickLabsPlatformMenu binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformmenu_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickLabsPlatformMenu to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtGui import QPlatformMenu

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQuickLabsPlatformMenuBar, QQuickLabsPlatformMenuItem
  from . import QQuickLabsPlatformSystemTrayIcon
  from ..QtCore import QMetaObject
  from ..QtGui import QFont
  from ..QtQml import QQmlV4Function
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlV4Function = WAIT['QQmlV4Function']
  QQuickLabsPlatformMenuItem = WAIT['QQuickLabsPlatformMenuItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickLabsPlatformMenu(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickLabsPlatformMenu: a plain Python object
  standing in front of one C++ QQuickLabsPlatformMenu.

  What exists
  -----------

  Every function of Qt's QQuickLabsPlatformMenu that has a ritual and that
  Python can call so far, 35 names in all: 'metaObject',
  'qmlExtendedNamespace', 'handle', 'menuBar', 'parentMenu',
  'systemTrayIcon', 'isEnabled', 'isVisible', 'minimumWidth', 'type',
  'title', 'font', 'addItem', 'removeItem', 'addMenu', 'removeMenu', 'clear',
  'open', 'close', 'aboutToShow', 'aboutToHide', 'itemsChanged',
  'menuBarChanged', 'parentMenuChanged', 'systemTrayIconChanged',
  'titleChanged', 'enabledChanged', 'visibleChanged', 'minimumWidthChanged',
  'fontChanged', 'typeChanged', 'iconChanged', 'classBegin',
  'componentComplete', 'updateIcon'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickLabsPlatformMenu::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickLabsPlatformMenu::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickLabsPlatformMenu::qt_qmlMarker_extendedNamespace()': one
    of Qt's own inner workings.
  - Qt's 'QQuickLabsPlatformMenu::~QQuickLabsPlatformMenu()': the destructor:
    Python never removes a C++ QQuickLabsPlatformMenu.
  - Qt's 'qsizetype
    QQuickLabsPlatformMenu::data_count(QQmlListProperty<QObject> *property)':
    names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'QObject *QQuickLabsPlatformMenu::data_at(QQmlListProperty<QObject>
    *property, qsizetype index)': names 'QQmlListProperty<QObject>', which
    has no cute class yet.
  - Qt's 'void QQuickLabsPlatformMenu::data_clear(QQmlListProperty<QObject>
    *property)': names 'QQmlListProperty<QObject>', which has no cute class
    yet.
  - Qt's 'qsizetype QQuickLabsPlatformMenu::items_count(
    QQmlListProperty<QQuickLabsPlatformMenuItem> *property)': names
    'QQmlListProperty<QQuickLabsPlatformMenuItem>', which has no cute class
    yet.
  - Qt's 'QQuickLabsPlatformMenuItem *QQuickLabsPlatformMenu::items_at(
    QQmlListProperty<QQuickLabsPlatformMenuItem> *property, qsizetype
    index)': names 'QQmlListProperty<QQuickLabsPlatformMenuItem>', which has
    no cute class yet.

  What has no ritual
  ------------------

  29 of the 73 functions Qt declares: 23 leans on 'QQuickLabsPlatformMenu; 2
  not a gap; 2 the compiler refuses its ritual as it would be written here; 2
  Qt's library has no name for it, and its code in Qt's source does not
  compile apart from its file.

  What to expect
  --------------

  - The C++ QQuickLabsPlatformMenu is created at the first use, not by
    'QQuickLabsPlatformMenu(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickLabsPlatformMenu.
  - Qt tells when it has removed the C++ QQuickLabsPlatformMenu. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickLabsPlatformMenu that has no cute function yet,
    '__init__', 'create', 'data', 'data_append', 'data_at', 'data_clear',
    'data_count', 'destroy', 'findWindow', 'icon', 'iconLoader',
    'insertItem', 'insertMenu', 'items', 'items_append', 'items_at',
    'items_clear', 'items_count', 'menuItem', 'setEnabled', 'setFont',
    'setIcon', 'setMenuBar', 'setMinimumWidth', 'setParentMenu',
    'setSystemTrayIcon', 'setTitle', 'setType', 'setVisible', 'sync',
    'unparentSubmenus', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def qmlExtendedNamespace() -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuickLabsPlatformMenu::qmlExtendedNamespace()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#qmlExtendedNamespace

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickLabsPlatformMenu::qmlExtendedNamespace()
    address = Rituals.call(
        'ritual_ZN22QQuickLabsPlatformMenu20qmlExtendedNamespaceEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickLabsPlatformMenu'

  #  A C++ QQuickLabsPlatformMenu Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickLabsPlatformMenu'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickLabsPlatformMenu::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickLabsPlatformMenu::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickLabsPlatformMenu10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def handle(self) -> Optional[QPlatformMenu]:
    """
    Calls Qt's 'QPlatformMenu *QQuickLabsPlatformMenu::handle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#handle

    Returns
    -------

    Optional[QPlatformMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMenu *QQuickLabsPlatformMenu::handle() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickLabsPlatformMenu6handleEv',
    )
    return QPlatformMenu._cuteAt(address)

  def menuBar(self) -> Optional[QQuickLabsPlatformMenuBar]:
    """
    Calls Qt's 'QQuickLabsPlatformMenuBar *QQuickLabsPlatformMenu::menuBar()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#menuBar

    Returns
    -------

    Optional[QQuickLabsPlatformMenuBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickLabsPlatformMenuBar *QQuickLabsPlatformMenu::menuBar() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickLabsPlatformMenu7menuBarEv',
    )
    from . import QQuickLabsPlatformMenuBar
    return QQuickLabsPlatformMenuBar._cuteAt(address)

  def parentMenu(self) -> Optional[QQuickLabsPlatformMenu]:
    """
    Calls Qt's 'QQuickLabsPlatformMenu *QQuickLabsPlatformMenu::parentMenu()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#parentMenu

    Returns
    -------

    Optional[QQuickLabsPlatformMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickLabsPlatformMenu *QQuickLabsPlatformMenu::parentMenu() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickLabsPlatformMenu10parentMenuEv',
    )
    return QQuickLabsPlatformMenu._cuteAt(address)

  def systemTrayIcon(self) -> Optional[QQuickLabsPlatformSystemTrayIcon]:
    """
    Calls Qt's 'QQuickLabsPlatformSystemTrayIcon
    *QQuickLabsPlatformMenu::systemTrayIcon() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#systemTrayIcon

    Returns
    -------

    Optional[QQuickLabsPlatformSystemTrayIcon]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickLabsPlatformSystemTrayIcon
    #      *QQuickLabsPlatformMenu::systemTrayIcon() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickLabsPlatformMenu14systemTrayIconEv',
    )
    from . import QQuickLabsPlatformSystemTrayIcon
    return QQuickLabsPlatformSystemTrayIcon._cuteAt(address)

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickLabsPlatformMenu::isEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#isEnabled
    """
    #  bool QQuickLabsPlatformMenu::isEnabled() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickLabsPlatformMenu9isEnabledEv',
    )

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QQuickLabsPlatformMenu::isVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#isVisible
    """
    #  bool QQuickLabsPlatformMenu::isVisible() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickLabsPlatformMenu9isVisibleEv',
    )

  def minimumWidth(self) -> int:
    """
    Calls Qt's 'int QQuickLabsPlatformMenu::minimumWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#minimumWidth
    """
    #  int QQuickLabsPlatformMenu::minimumWidth() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickLabsPlatformMenu12minimumWidthEv',
    )

  def type(self) -> QPlatformMenu.MenuType:
    """
    Calls Qt's 'QPlatformMenu::MenuType QQuickLabsPlatformMenu::type()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#type

    Returns
    -------

    QPlatformMenu.MenuType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPlatformMenu.MenuType(number)' gives.
    """
    #  QPlatformMenu::MenuType QQuickLabsPlatformMenu::type() const
    return QPlatformMenu.MenuType(self.uglySide.call(
        'ritual_ZNK22QQuickLabsPlatformMenu4typeEv',
    ))

  def title(self) -> str:
    """
    Calls Qt's 'QString QQuickLabsPlatformMenu::title() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickLabsPlatformMenu::title() const
    return self.uglySide.call('ritual_ZNK22QQuickLabsPlatformMenu5titleEv')

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickLabsPlatformMenu::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickLabsPlatformMenu::font() const
    address = self.uglySide.call('ritual_ZNK22QQuickLabsPlatformMenu4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickLabsPlatformMenu::QQuickLabsPlatformMenu(QObject *parent)':
    leans on 'QQuickLabsPlatformMenu::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenu.__init__' has no cute function yet. Qt's "
        "'QQuickLabsPlatformMenu::QQuickLabsPlatformMenu(QObject *parent)': "
        "leans on 'QQuickLabsPlatformMenu::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  @overload(QQuickLabsPlatformMenuItem)
  @overload(NoneType)
  def addItem(self, item: Optional[QQuickLabsPlatformMenuItem]) -> None:
    """
    Calls Qt's 'void
    QQuickLabsPlatformMenu::addItem(QQuickLabsPlatformMenuItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#addItem

    Parameters
    ----------

    item : Optional[QQuickLabsPlatformMenuItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLabsPlatformMenu::addItem(QQuickLabsPlatformMenuItem *item)
    self.uglySide.call(
        'ritual_ZN22QQuickLabsPlatformMenu7addItemEP26QQuickLabsPlatformMen'
        'uItem',
        self._addressOf(item),
    )

  @overload(QQuickLabsPlatformMenuItem)
  @overload(NoneType)
  def removeItem(self, item: Optional[QQuickLabsPlatformMenuItem]) -> None:
    """
    Calls Qt's 'void
    QQuickLabsPlatformMenu::removeItem(QQuickLabsPlatformMenuItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#removeItem

    Parameters
    ----------

    item : Optional[QQuickLabsPlatformMenuItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLabsPlatformMenu::removeItem(QQuickLabsPlatformMenuItem
    #      *item)
    self.uglySide.call(
        'ritual_ZN22QQuickLabsPlatformMenu10removeItemEP26QQuickLabsPlatfor'
        'mMenuItem',
        self._addressOf(item),
    )

  @overload(THIS)
  @overload(NoneType)
  def addMenu(self, menu: Optional[QQuickLabsPlatformMenu]) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenu::addMenu(QQuickLabsPlatformMenu
    *menu)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#addMenu

    Parameters
    ----------

    menu : Optional[QQuickLabsPlatformMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLabsPlatformMenu::addMenu(QQuickLabsPlatformMenu *menu)
    self.uglySide.call(
        'ritual_ZN22QQuickLabsPlatformMenu7addMenuEPS_',
        self._addressOf(menu),
    )

  @overload(THIS)
  @overload(NoneType)
  def removeMenu(self, menu: Optional[QQuickLabsPlatformMenu]) -> None:
    """
    Calls Qt's 'void
    QQuickLabsPlatformMenu::removeMenu(QQuickLabsPlatformMenu *menu)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#removeMenu

    Parameters
    ----------

    menu : Optional[QQuickLabsPlatformMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLabsPlatformMenu::removeMenu(QQuickLabsPlatformMenu *menu)
    self.uglySide.call(
        'ritual_ZN22QQuickLabsPlatformMenu10removeMenuEPS_',
        self._addressOf(menu),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenu::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#clear
    """
    #  void QQuickLabsPlatformMenu::clear()
    self.uglySide.call('ritual_ZN22QQuickLabsPlatformMenu5clearEv')

  @overload(QQmlV4Function)
  @overload(NoneType)
  def open(self, args: Optional[QQmlV4Function]) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenu::open(QQmlV4FunctionPtr args)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#open

    Parameters
    ----------

    args : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLabsPlatformMenu::open(QQmlV4FunctionPtr args)
    self.uglySide.call(
        'ritual_ZN22QQuickLabsPlatformMenu4openEP14QQmlV4Function',
        self._addressOf(args),
    )

  def close(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenu::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#close
    """
    #  void QQuickLabsPlatformMenu::close()
    self.uglySide.call('ritual_ZN22QQuickLabsPlatformMenu5closeEv')

  def aboutToShow(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenu::aboutToShow()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#aboutToShow
    """
    #  void QQuickLabsPlatformMenu::aboutToShow()
    self.uglySide.call('ritual_ZN22QQuickLabsPlatformMenu11aboutToShowEv')

  def aboutToHide(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenu::aboutToHide()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#aboutToHide
    """
    #  void QQuickLabsPlatformMenu::aboutToHide()
    self.uglySide.call('ritual_ZN22QQuickLabsPlatformMenu11aboutToHideEv')

  def itemsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenu::itemsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#itemsChanged
    """
    #  void QQuickLabsPlatformMenu::itemsChanged()
    self.uglySide.call('ritual_ZN22QQuickLabsPlatformMenu12itemsChangedEv')

  def menuBarChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenu::menuBarChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#menuBarChanged
    """
    #  void QQuickLabsPlatformMenu::menuBarChanged()
    self.uglySide.call('ritual_ZN22QQuickLabsPlatformMenu14menuBarChangedEv')

  def parentMenuChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenu::parentMenuChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#parentMenuChanged
    """
    #  void QQuickLabsPlatformMenu::parentMenuChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickLabsPlatformMenu17parentMenuChangedEv',
    )

  def systemTrayIconChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenu::systemTrayIconChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#systemTrayIconChanged
    """
    #  void QQuickLabsPlatformMenu::systemTrayIconChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickLabsPlatformMenu21systemTrayIconChangedEv',
    )

  def titleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenu::titleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#titleChanged
    """
    #  void QQuickLabsPlatformMenu::titleChanged()
    self.uglySide.call('ritual_ZN22QQuickLabsPlatformMenu12titleChangedEv')

  def enabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenu::enabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#enabledChanged
    """
    #  void QQuickLabsPlatformMenu::enabledChanged()
    self.uglySide.call('ritual_ZN22QQuickLabsPlatformMenu14enabledChangedEv')

  def visibleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenu::visibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#visibleChanged
    """
    #  void QQuickLabsPlatformMenu::visibleChanged()
    self.uglySide.call('ritual_ZN22QQuickLabsPlatformMenu14visibleChangedEv')

  def minimumWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenu::minimumWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#minimumWidthChanged
    """
    #  void QQuickLabsPlatformMenu::minimumWidthChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickLabsPlatformMenu19minimumWidthChangedEv',
    )

  def fontChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenu::fontChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#fontChanged
    """
    #  void QQuickLabsPlatformMenu::fontChanged()
    self.uglySide.call('ritual_ZN22QQuickLabsPlatformMenu11fontChangedEv')

  def typeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenu::typeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#typeChanged
    """
    #  void QQuickLabsPlatformMenu::typeChanged()
    self.uglySide.call('ritual_ZN22QQuickLabsPlatformMenu11typeChangedEv')

  def iconChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenu::iconChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#iconChanged
    """
    #  void QQuickLabsPlatformMenu::iconChanged()
    self.uglySide.call('ritual_ZN22QQuickLabsPlatformMenu11iconChangedEv')

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenu::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#classBegin
    """
    #  void QQuickLabsPlatformMenu::classBegin()
    ritual = 'ritual_ZN22QQuickLabsPlatformMenu10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickLabsPlatformMenu10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenu::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#componentComplete
    """
    #  void QQuickLabsPlatformMenu::componentComplete()
    self.uglySide.call(
        'ritual_ZN22QQuickLabsPlatformMenu17componentCompleteEv',
    )

  def updateIcon(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenu::updateIcon()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenu.html#updateIcon
    """
    #  void QQuickLabsPlatformMenu::updateIcon()
    self.uglySide.call('ritual_ZN22QQuickLabsPlatformMenu10updateIconEv')

  @staticmethod
  def create(*__, **_) -> Never:
    """
    Qt's 'QPlatformMenu *QQuickLabsPlatformMenu::create()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'QWidgetPlatform'.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenu.create' has no cute function yet. Qt's "
        "'QPlatformMenu *QQuickLabsPlatformMenu::create()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'QWidgetPlatform'.")

  @staticmethod
  def data(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QQuickLabsPlatformMenu::data()': leans on
    'QQuickLabsPlatformMenu::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenu.data' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QQuickLabsPlatformMenu::data()': leans "
        "on 'QQuickLabsPlatformMenu::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def data_append(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenu::data_append(QQmlListProperty<QObject>
    *property, QObject *object)': leans on
    'QQuickLabsPlatformMenu::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenu.data_append' has no cute function yet. "
        "Qt's 'void "
        "QQuickLabsPlatformMenu::data_append(QQmlListProperty<QObject> "
        "*property, QObject *object)': leans on "
        "'QQuickLabsPlatformMenu::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def data_at(*__, **_) -> Never:
    """
    Qt's 'QObject *QQuickLabsPlatformMenu::data_at(QQmlListProperty<QObject>
    *property, qsizetype index)': names 'QQmlListProperty<QObject>', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenu.data_at' has no cute function yet. Qt's "
        "'QObject "
        "*QQuickLabsPlatformMenu::data_at(QQmlListProperty<QObject> "
        "*property, qsizetype index)': names 'QQmlListProperty<QObject>', "
        "which has no cute class yet.")

  @staticmethod
  def data_clear(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenu::data_clear(QQmlListProperty<QObject>
    *property)': names 'QQmlListProperty<QObject>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenu.data_clear' has no cute function yet. Qt's "
        "'void QQuickLabsPlatformMenu::data_clear(QQmlListProperty<QObject> "
        "*property)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")

  @staticmethod
  def data_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QQuickLabsPlatformMenu::data_count(QQmlListProperty<QObject> *property)':
    names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenu.data_count' has no cute function yet. Qt's "
        "'qsizetype "
        "QQuickLabsPlatformMenu::data_count(QQmlListProperty<QObject> "
        "*property)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")

  @staticmethod
  def destroy(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenu::destroy()': leans on
    'QQuickLabsPlatformMenu::parentMenuChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenu.destroy' has no cute function yet. Qt's "
        "'void QQuickLabsPlatformMenu::destroy()': leans on "
        "'QQuickLabsPlatformMenu::parentMenuChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def findWindow(*__, **_) -> Never:
    """
    Qt's 'QWindow *QQuickLabsPlatformMenu::findWindow(QQuickItem *target,
    QPoint *offset) const': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'effectiveWindow'.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenu.findWindow' has no cute function yet. Qt's "
        "'QWindow *QQuickLabsPlatformMenu::findWindow(QQuickItem *target, "
        "QPoint *offset) const': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'effectiveWindow'.")

  @staticmethod
  def icon(*__, **_) -> Never:
    """
    Qt's 'QQuickLabsPlatformIcon QQuickLabsPlatformMenu::icon() const': leans
    on 'QQuickLabsPlatformMenu::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenu.icon' has no cute function yet. Qt's "
        "'QQuickLabsPlatformIcon QQuickLabsPlatformMenu::icon() const': "
        "leans on 'QQuickLabsPlatformMenu::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def iconLoader(*__, **_) -> Never:
    """
    Qt's 'QQuickLabsPlatformIconLoader *QQuickLabsPlatformMenu::iconLoader()
    const': leans on 'QQuickLabsPlatformMenu::staticMetaObject', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenu.iconLoader' has no cute function yet. Qt's "
        "'QQuickLabsPlatformIconLoader "
        "*QQuickLabsPlatformMenu::iconLoader() const': leans on "
        "'QQuickLabsPlatformMenu::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def insertItem(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenu::insertItem(int index,
    QQuickLabsPlatformMenuItem *item)': the compiler refuses its ritual as it
    would be written here: redefinition of 'index' with a different type:
    'const int' vs 'int'.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenu.insertItem' has no cute function yet. Qt's "
        "'void QQuickLabsPlatformMenu::insertItem(int index, "
        "QQuickLabsPlatformMenuItem *item)': the compiler refuses its "
        "ritual as it would be written here: redefinition of 'index' with a "
        "different type: 'const int' vs 'int'.")

  @staticmethod
  def insertMenu(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenu::insertMenu(int index,
    QQuickLabsPlatformMenu *menu)': the compiler refuses its ritual as it
    would be written here: redefinition of 'index' with a different type:
    'const int' vs 'int'.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenu.insertMenu' has no cute function yet. Qt's "
        "'void QQuickLabsPlatformMenu::insertMenu(int index, "
        "QQuickLabsPlatformMenu *menu)': the compiler refuses its ritual as "
        "it would be written here: redefinition of 'index' with a different "
        "type: 'const int' vs 'int'.")

  @staticmethod
  def items(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickLabsPlatformMenuItem>
    QQuickLabsPlatformMenu::items()': leans on
    'QQuickLabsPlatformMenu::itemsChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenu.items' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuickLabsPlatformMenuItem> "
        "QQuickLabsPlatformMenu::items()': leans on "
        "'QQuickLabsPlatformMenu::itemsChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def items_append(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenu::items_append(
    QQmlListProperty<QQuickLabsPlatformMenuItem> *property,
    QQuickLabsPlatformMenuItem *item)': leans on
    'QQuickLabsPlatformMenu::itemsChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenu.items_append' has no cute function yet. "
        "Qt's 'void "
        "QQuickLabsPlatformMenu::items_append(QQmlListProperty<QQuickLabsPla"
        "tformMenuItem> *property, QQuickLabsPlatformMenuItem *item)': "
        "leans on 'QQuickLabsPlatformMenu::itemsChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def items_at(*__, **_) -> Never:
    """
    Qt's 'QQuickLabsPlatformMenuItem *QQuickLabsPlatformMenu::items_at(
    QQmlListProperty<QQuickLabsPlatformMenuItem> *property, qsizetype
    index)': names 'QQmlListProperty<QQuickLabsPlatformMenuItem>', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenu.items_at' has no cute function yet. Qt's "
        "'QQuickLabsPlatformMenuItem "
        "*QQuickLabsPlatformMenu::items_at(QQmlListProperty<QQuickLabsPlatfo"
        "rmMenuItem> *property, qsizetype index)': names "
        "'QQmlListProperty<QQuickLabsPlatformMenuItem>', which has no cute "
        "class yet.")

  @staticmethod
  def items_clear(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenu::items_clear(
    QQmlListProperty<QQuickLabsPlatformMenuItem> *property)': leans on
    'QQuickLabsPlatformMenu::itemsChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenu.items_clear' has no cute function yet. "
        "Qt's 'void "
        "QQuickLabsPlatformMenu::items_clear(QQmlListProperty<QQuickLabsPlat"
        "formMenuItem> *property)': leans on "
        "'QQuickLabsPlatformMenu::itemsChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def items_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype QQuickLabsPlatformMenu::items_count(
    QQmlListProperty<QQuickLabsPlatformMenuItem> *property)': names
    'QQmlListProperty<QQuickLabsPlatformMenuItem>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenu.items_count' has no cute function yet. "
        "Qt's 'qsizetype "
        "QQuickLabsPlatformMenu::items_count(QQmlListProperty<QQuickLabsPlat"
        "formMenuItem> *property)': names "
        "'QQmlListProperty<QQuickLabsPlatformMenuItem>', which has no cute "
        "class yet.")

  @staticmethod
  def menuItem(*__, **_) -> Never:
    """
    Qt's 'QQuickLabsPlatformMenuItem *QQuickLabsPlatformMenu::menuItem()
    const': leans on 'QQuickLabsPlatformMenu::staticMetaObject', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenu.menuItem' has no cute function yet. Qt's "
        "'QQuickLabsPlatformMenuItem *QQuickLabsPlatformMenu::menuItem() "
        "const': leans on 'QQuickLabsPlatformMenu::staticMetaObject', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setEnabled(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenu::setEnabled(bool enabled)': leans on
    'QQuickLabsPlatformMenu::enabledChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenu.setEnabled' has no cute function yet. Qt's "
        "'void QQuickLabsPlatformMenu::setEnabled(bool enabled)': leans on "
        "'QQuickLabsPlatformMenu::enabledChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setFont(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenu::setFont(const QFont &font)': leans on
    'QQuickLabsPlatformMenu::fontChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenu.setFont' has no cute function yet. Qt's "
        "'void QQuickLabsPlatformMenu::setFont(const QFont &font)': leans "
        "on 'QQuickLabsPlatformMenu::fontChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setIcon(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenu::setIcon(const QQuickLabsPlatformIcon
    &icon)': leans on 'QQuickLabsPlatformMenu::iconChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenu.setIcon' has no cute function yet. Qt's "
        "'void QQuickLabsPlatformMenu::setIcon(const QQuickLabsPlatformIcon "
        "&icon)': leans on 'QQuickLabsPlatformMenu::iconChanged()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setMenuBar(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenu::setMenuBar(QQuickLabsPlatformMenuBar
    *menuBar)': leans on 'QQuickLabsPlatformMenu::menuBarChanged()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenu.setMenuBar' has no cute function yet. Qt's "
        "'void QQuickLabsPlatformMenu::setMenuBar(QQuickLabsPlatformMenuBar "
        "*menuBar)': leans on 'QQuickLabsPlatformMenu::menuBarChanged()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setMinimumWidth(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenu::setMinimumWidth(int width)': leans on
    'QQuickLabsPlatformMenu::minimumWidthChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenu.setMinimumWidth' has no cute function yet. "
        "Qt's 'void QQuickLabsPlatformMenu::setMinimumWidth(int width)': "
        "leans on 'QQuickLabsPlatformMenu::minimumWidthChanged()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setParentMenu(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenu::setParentMenu(QQuickLabsPlatformMenu
    *menu)': leans on 'QQuickLabsPlatformMenu::parentMenuChanged()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenu.setParentMenu' has no cute function yet. "
        "Qt's 'void "
        "QQuickLabsPlatformMenu::setParentMenu(QQuickLabsPlatformMenu "
        "*menu)': leans on 'QQuickLabsPlatformMenu::parentMenuChanged()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setSystemTrayIcon(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenu::setSystemTrayIcon(
    QQuickLabsPlatformSystemTrayIcon *icon)': leans on
    'QQuickLabsPlatformMenu::parentMenuChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenu.setSystemTrayIcon' has no cute function "
        "yet. Qt's 'void "
        "QQuickLabsPlatformMenu::setSystemTrayIcon(QQuickLabsPlatformSystemT"
        "rayIcon *icon)': leans on "
        "'QQuickLabsPlatformMenu::parentMenuChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setTitle(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenu::setTitle(const QString &title)': leans
    on 'QQuickLabsPlatformMenu::titleChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenu.setTitle' has no cute function yet. Qt's "
        "'void QQuickLabsPlatformMenu::setTitle(const QString &title)': "
        "leans on 'QQuickLabsPlatformMenu::titleChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setType(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenu::setType(QPlatformMenu::MenuType
    type)': leans on 'QQuickLabsPlatformMenu::typeChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenu.setType' has no cute function yet. Qt's "
        "'void QQuickLabsPlatformMenu::setType(QPlatformMenu::MenuType "
        "type)': leans on 'QQuickLabsPlatformMenu::typeChanged()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setVisible(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenu::setVisible(bool visible)': leans on
    'QQuickLabsPlatformMenu::visibleChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenu.setVisible' has no cute function yet. Qt's "
        "'void QQuickLabsPlatformMenu::setVisible(bool visible)': leans on "
        "'QQuickLabsPlatformMenu::visibleChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def sync(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenu::sync()': leans on
    'QQuickLabsPlatformMenu::create()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenu.sync' has no cute function yet. Qt's 'void "
        "QQuickLabsPlatformMenu::sync()': leans on "
        "'QQuickLabsPlatformMenu::create()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def unparentSubmenus(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenu::unparentSubmenus()': leans on
    'QQuickLabsPlatformMenu::parentMenuChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenu.unparentSubmenus' has no cute function "
        "yet. Qt's 'void QQuickLabsPlatformMenu::unparentSubmenus()': leans "
        "on 'QQuickLabsPlatformMenu::parentMenuChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
