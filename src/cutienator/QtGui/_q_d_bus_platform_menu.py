"""
QDBusPlatformMenu binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qdbusplatformmenu_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QDBusPlatformMenu to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList
from . import QPlatformMenu

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRect
  from . import QDBusMenuItem, QDBusMenuItemKeys, QDBusPlatformMenuItem
  from . import QFont, QIcon, QPlatformMenuItem, QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDBusMenuItem = WAIT['QDBusMenuItem']
  QDBusMenuItemKeys = WAIT['QDBusMenuItemKeys']
  QDBusPlatformMenuItem = WAIT['QDBusPlatformMenuItem']
  QFont = WAIT['QFont']
  QIcon = WAIT['QIcon']
  QPlatformMenuItem = WAIT['QPlatformMenuItem']
  QRect = WAIT['QRect']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDBusPlatformMenu(QPlatformMenu):
  """
  The cute side of Qt's QDBusPlatformMenu: a plain Python object standing in
  front of one C++ QDBusPlatformMenu.

  It is built on the cute 'QPlatformMenu', as Qt's QDBusPlatformMenu is built
  on Qt's QPlatformMenu, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDBusPlatformMenu that has a ritual and that Python
  can call so far, 28 names in all: 'metaObject', 'insertMenuItem',
  'removeMenuItem', 'syncMenuItem', 'syncSeparatorsCollapsible', 'text',
  'setText', 'icon', 'setIcon', 'isEnabled', 'setEnabled', 'isVisible',
  'setVisible', 'setMinimumWidth', 'setFont', 'setMenuType',
  'setContainingMenuItem', 'showPopup', 'dismiss', 'menuItemAt',
  'menuItemForTag', 'items', 'createMenuItem', 'createSubMenu', 'revision',
  'updated', 'propertiesUpdated', 'popupRequested'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDBusPlatformMenu::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QDBusPlatformMenu::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QDBusPlatformMenu::~QDBusPlatformMenu()': the destructor: Python
    never removes a C++ QDBusPlatformMenu.

  What has no ritual
  ------------------

  6 of the 37 functions Qt declares: 4 leans on 'QDBusPlatformMenu; 2 not a
  gap.

  What to expect
  --------------

  - The C++ QDBusPlatformMenu is created at the first use, not by
    'QDBusPlatformMenu(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDBusPlatformMenu.
  - Qt tells when it has removed the C++ QDBusPlatformMenu. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDBusPlatformMenu that has no cute function yet,
    '__init__', 'emitUpdated', 'syncSubMenu', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusPlatformMenu'

  #  A C++ QDBusPlatformMenu Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDBusPlatformMenu'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDBusPlatformMenu::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusplatformmenu.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDBusPlatformMenu::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QDBusPlatformMenu10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def text(self) -> str:
    """
    Calls Qt's 'const QString QDBusPlatformMenu::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusplatformmenu.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString QDBusPlatformMenu::text() const
    return self.uglySide.call('ritual_ZNK17QDBusPlatformMenu4textEv')

  def icon(self) -> QIcon:
    """
    Calls Qt's 'QIcon QDBusPlatformMenu::icon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusplatformmenu.html#icon

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QDBusPlatformMenu::icon() const
    address = self.uglySide.call('ritual_ZNK17QDBusPlatformMenu4iconEv')
    from . import QIcon
    return QIcon._cuteOwning(address)

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QDBusPlatformMenu::isEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusplatformmenu.html#isEnabled
    """
    #  bool QDBusPlatformMenu::isEnabled() const
    ritual = 'ritual_ZNK17QDBusPlatformMenu9isEnabledEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QDBusPlatformMenu9isEnabledEv'
    return self.uglySide.call(ritual)

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QDBusPlatformMenu::isVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusplatformmenu.html#isVisible
    """
    #  bool QDBusPlatformMenu::isVisible() const
    return self.uglySide.call('ritual_ZNK17QDBusPlatformMenu9isVisibleEv')

  @overload(int)
  def menuItemAt(self, position: int) -> Optional[QPlatformMenuItem]:
    """
    Calls Qt's 'QPlatformMenuItem *QDBusPlatformMenu::menuItemAt(int
    position) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusplatformmenu.html#menuItemAt

    Parameters
    ----------

    position : int
      Passed on as it is.

    Returns
    -------

    Optional[QPlatformMenuItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMenuItem *QDBusPlatformMenu::menuItemAt(int position) const
    ritual = 'ritual_ZNK17QDBusPlatformMenu10menuItemAtEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QDBusPlatformMenu10menuItemAtEi'
    address = self.uglySide.call(ritual, position)
    from . import QPlatformMenuItem
    return QPlatformMenuItem._cuteAt(address)

  @overload(int)
  def menuItemForTag(self, tag: int) -> Optional[QPlatformMenuItem]:
    """
    Calls Qt's 'QPlatformMenuItem *QDBusPlatformMenu::menuItemForTag(quintptr
    tag) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusplatformmenu.html#menuItemForTag

    Parameters
    ----------

    tag : int
      Passed on as it is.

    Returns
    -------

    Optional[QPlatformMenuItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMenuItem *QDBusPlatformMenu::menuItemForTag(quintptr tag)
    #      const
    ritual = 'ritual_ZNK17QDBusPlatformMenu14menuItemForTagEy'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QDBusPlatformMenu14menuItemForTagEy'
    address = self.uglySide.call(ritual, tag)
    from . import QPlatformMenuItem
    return QPlatformMenuItem._cuteAt(address)

  def items(self) -> QList[QDBusPlatformMenuItem]:
    """
    Calls Qt's 'const QList<QDBusPlatformMenuItem *>
    QDBusPlatformMenu::items() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusplatformmenu.html#items

    Returns
    -------

    QList[QDBusPlatformMenuItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QList<QDBusPlatformMenuItem *> QDBusPlatformMenu::items() const
    address = self.uglySide.call('ritual_ZNK17QDBusPlatformMenu5itemsEv')
    from . import QDBusPlatformMenuItem
    return QList[QDBusPlatformMenuItem]._cuteOwning(address)

  def createMenuItem(self) -> Optional[QPlatformMenuItem]:
    """
    Calls Qt's 'QPlatformMenuItem *QDBusPlatformMenu::createMenuItem()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusplatformmenu.html#createMenuItem

    Returns
    -------

    Optional[QPlatformMenuItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMenuItem *QDBusPlatformMenu::createMenuItem() const
    address = self.uglySide.call(
        'ritual_ZNK17QDBusPlatformMenu14createMenuItemEv',
    )
    from . import QPlatformMenuItem
    return QPlatformMenuItem._cuteAt(address)

  def createSubMenu(self) -> Optional[QPlatformMenu]:
    """
    Calls Qt's 'QPlatformMenu *QDBusPlatformMenu::createSubMenu() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusplatformmenu.html#createSubMenu

    Returns
    -------

    Optional[QPlatformMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMenu *QDBusPlatformMenu::createSubMenu() const
    address = self.uglySide.call(
        'ritual_ZNK17QDBusPlatformMenu13createSubMenuEv',
    )
    return QPlatformMenu._cuteAt(address)

  def revision(self) -> int:
    """
    Calls Qt's 'uint QDBusPlatformMenu::revision() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusplatformmenu.html#revision
    """
    #  uint QDBusPlatformMenu::revision() const
    return self.uglySide.call('ritual_ZNK17QDBusPlatformMenu8revisionEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QDBusPlatformMenu::setText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusplatformmenu.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDBusPlatformMenu::setText(const QString &text)
    ritual = 'ritual_ZN17QDBusPlatformMenu7setTextERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QDBusPlatformMenu7setTextERK7QString'
    self.uglySide.call(ritual, text)

  @overload(QIcon)
  def setIcon(self, icon: QIcon) -> None:
    """
    Calls Qt's 'void QDBusPlatformMenu::setIcon(const QIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusplatformmenu.html#setIcon

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.
    """
    #  void QDBusPlatformMenu::setIcon(const QIcon &icon)
    ritual = 'ritual_ZN17QDBusPlatformMenu7setIconERK5QIcon'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QDBusPlatformMenu7setIconERK5QIcon'
    self.uglySide.call(ritual, self._valueOf(icon))

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QDBusPlatformMenu::setEnabled(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusplatformmenu.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QDBusPlatformMenu::setEnabled(bool enabled)
    ritual = 'ritual_ZN17QDBusPlatformMenu10setEnabledEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QDBusPlatformMenu10setEnabledEb'
    self.uglySide.call(ritual, enabled)

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QDBusPlatformMenu::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusplatformmenu.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QDBusPlatformMenu::setVisible(bool visible)
    ritual = 'ritual_ZN17QDBusPlatformMenu10setVisibleEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QDBusPlatformMenu10setVisibleEb'
    self.uglySide.call(ritual, visible)

  @overload(int)
  def setMinimumWidth(self, width: int) -> None:
    """
    Calls Qt's 'void QDBusPlatformMenu::setMinimumWidth(int width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusplatformmenu.html#setMinimumWidth

    Parameters
    ----------

    width : int
      Passed on as it is.
    """
    #  void QDBusPlatformMenu::setMinimumWidth(int width)
    ritual = 'ritual_ZN17QDBusPlatformMenu15setMinimumWidthEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QDBusPlatformMenu15setMinimumWidthEi'
    self.uglySide.call(ritual, width)

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QDBusPlatformMenu::setFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusplatformmenu.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QDBusPlatformMenu::setFont(const QFont &font)
    ritual = 'ritual_ZN17QDBusPlatformMenu7setFontERK5QFont'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QDBusPlatformMenu7setFontERK5QFont'
    self.uglySide.call(ritual, self._valueOf(font))

  @overload(QPlatformMenu.MenuType)
  def setMenuType(self, type: QPlatformMenu.MenuType) -> None:
    """
    Calls Qt's 'void QDBusPlatformMenu::setMenuType(MenuType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusplatformmenu.html#setMenuType

    Parameters
    ----------

    type : QPlatformMenu.MenuType
      Passed on as its number.
    """
    #  void QDBusPlatformMenu::setMenuType(MenuType type)
    ritual = (
        'ritual_ZN17QDBusPlatformMenu11setMenuTypeEN13QPlatformMenu8MenuTyp'
        'eE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QDBusPlatformMenu11setMenuTypeEN13QPlatformMenu8M'
          'enuTypeE')
    self.uglySide.call(ritual, type.value)

  @overload(QDBusPlatformMenuItem)
  @overload(NoneType)
  def setContainingMenuItem(
      self,
      item: Optional[QDBusPlatformMenuItem],
  ) -> None:
    """
    Calls Qt's 'void
    QDBusPlatformMenu::setContainingMenuItem(QDBusPlatformMenuItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusplatformmenu.html#setContainingMenuItem

    Parameters
    ----------

    item : Optional[QDBusPlatformMenuItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDBusPlatformMenu::setContainingMenuItem(QDBusPlatformMenuItem
    #      *item)
    self.uglySide.call(
        'ritual_ZN17QDBusPlatformMenu21setContainingMenuItemEP21QDBusPlatfo'
        'rmMenuItem',
        self._addressOf(item),
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
    Qt's 'QDBusPlatformMenu::QDBusPlatformMenu()': leans on
    'QDBusPlatformMenu::qt_metacall(QMetaObject::Call, int, void**)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QDBusPlatformMenu.__init__' has no cute function yet. Qt's "
        "'QDBusPlatformMenu::QDBusPlatformMenu()': leans on "
        "'QDBusPlatformMenu::qt_metacall(QMetaObject::Call, int, void**)', "
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

  @overload(QPlatformMenuItem, QPlatformMenuItem)
  @overload(QPlatformMenuItem, NoneType)
  @overload(NoneType, QPlatformMenuItem)
  @overload(NoneType, NoneType)
  def insertMenuItem(
      self,
      menuItem: Optional[QPlatformMenuItem],
      before: Optional[QPlatformMenuItem],
  ) -> None:
    """
    Calls Qt's 'void QDBusPlatformMenu::insertMenuItem(QPlatformMenuItem
    *menuItem, QPlatformMenuItem *before)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusplatformmenu.html#insertMenuItem

    Parameters
    ----------

    menuItem : Optional[QPlatformMenuItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    before : Optional[QPlatformMenuItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDBusPlatformMenu::insertMenuItem(QPlatformMenuItem *menuItem,
    #      QPlatformMenuItem *before)
    self.uglySide.call(
        'ritual_ZN17QDBusPlatformMenu14insertMenuItemEP17QPlatformMenuItemS'
        '1_',
        self._addressOf(menuItem), self._addressOf(before),
    )

  @overload(QPlatformMenuItem)
  @overload(NoneType)
  def removeMenuItem(self, menuItem: Optional[QPlatformMenuItem]) -> None:
    """
    Calls Qt's 'void QDBusPlatformMenu::removeMenuItem(QPlatformMenuItem
    *menuItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusplatformmenu.html#removeMenuItem

    Parameters
    ----------

    menuItem : Optional[QPlatformMenuItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDBusPlatformMenu::removeMenuItem(QPlatformMenuItem *menuItem)
    self.uglySide.call(
        'ritual_ZN17QDBusPlatformMenu14removeMenuItemEP17QPlatformMenuItem',
        self._addressOf(menuItem),
    )

  @overload(QPlatformMenuItem)
  @overload(NoneType)
  def syncMenuItem(self, menuItem: Optional[QPlatformMenuItem]) -> None:
    """
    Calls Qt's 'void QDBusPlatformMenu::syncMenuItem(QPlatformMenuItem
    *menuItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusplatformmenu.html#syncMenuItem

    Parameters
    ----------

    menuItem : Optional[QPlatformMenuItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDBusPlatformMenu::syncMenuItem(QPlatformMenuItem *menuItem)
    self.uglySide.call(
        'ritual_ZN17QDBusPlatformMenu12syncMenuItemEP17QPlatformMenuItem',
        self._addressOf(menuItem),
    )

  @overload(bool)
  def syncSeparatorsCollapsible(self, enable: bool) -> None:
    """
    Calls Qt's 'void QDBusPlatformMenu::syncSeparatorsCollapsible(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusplatformmenu.html#syncSeparatorsCollapsible

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QDBusPlatformMenu::syncSeparatorsCollapsible(bool enable)
    ritual = 'ritual_ZN17QDBusPlatformMenu25syncSeparatorsCollapsibleEb'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QDBusPlatformMenu25syncSeparatorsCollapsibleEb')
    self.uglySide.call(ritual, enable)

  @overload(QWindow, QRect, QPlatformMenuItem)
  @overload(QWindow, QRect, NoneType)
  @overload(NoneType, QRect, QPlatformMenuItem)
  @overload(NoneType, QRect, NoneType)
  def showPopup(
      self,
      parentWindow: Optional[QWindow],
      targetRect: QRect,
      item: Optional[QPlatformMenuItem],
  ) -> None:
    """
    Calls Qt's 'void QDBusPlatformMenu::showPopup(const QWindow
    *parentWindow, const QRect &targetRect, const QPlatformMenuItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusplatformmenu.html#showPopup

    Parameters
    ----------

    parentWindow : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    targetRect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    item : Optional[QPlatformMenuItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDBusPlatformMenu::showPopup(const QWindow *parentWindow, const
    #      QRect &targetRect, const QPlatformMenuItem *item)
    self.uglySide.call(
        'ritual_ZN17QDBusPlatformMenu9showPopupEPK7QWindowRK5QRectPK17QPlat'
        'formMenuItem',
        self._addressOf(parentWindow), self._valueOf(targetRect),
        self._addressOf(item),
    )

  def dismiss(self) -> None:
    """
    Calls Qt's 'void QDBusPlatformMenu::dismiss()'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusplatformmenu.html#dismiss
    """
    #  void QDBusPlatformMenu::dismiss()
    ritual = 'ritual_ZN17QDBusPlatformMenu7dismissEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QDBusPlatformMenu7dismissEv'
    self.uglySide.call(ritual)

  @overload(int, int)
  def updated(self, revision: int, dbusId: int) -> None:
    """
    Calls Qt's 'void QDBusPlatformMenu::updated(uint revision, int dbusId)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusplatformmenu.html#updated

    Parameters
    ----------

    revision : int
      Passed on as it is.

    dbusId : int
      Passed on as it is.
    """
    #  void QDBusPlatformMenu::updated(uint revision, int dbusId)
    self.uglySide.call(
        'ritual_ZN17QDBusPlatformMenu7updatedEji', revision, dbusId,
    )

  @overload(QList[QDBusMenuItem], QList[QDBusMenuItemKeys])
  def propertiesUpdated(
      self,
      updatedProps: QList[QDBusMenuItem],
      removedProps: QList[QDBusMenuItemKeys],
  ) -> None:
    """
    Calls Qt's 'void QDBusPlatformMenu::propertiesUpdated(QDBusMenuItemList
    updatedProps, QDBusMenuItemKeysList removedProps)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusplatformmenu.html#propertiesUpdated

    Parameters
    ----------

    updatedProps : QList[QDBusMenuItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    removedProps : QList[QDBusMenuItemKeys]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDBusPlatformMenu::propertiesUpdated(QDBusMenuItemList
    #      updatedProps, QDBusMenuItemKeysList removedProps)
    self.uglySide.call(
        'ritual_ZN17QDBusPlatformMenu17propertiesUpdatedE5QListI13QDBusMenu'
        'ItemES0_I17QDBusMenuItemKeysE',
        self._valueOf(updatedProps), self._valueOf(removedProps),
    )

  @overload(int, int)
  def popupRequested(self, id: int, timestamp: int) -> None:
    """
    Calls Qt's 'void QDBusPlatformMenu::popupRequested(int id, uint
    timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusplatformmenu.html#popupRequested

    Parameters
    ----------

    id : int
      Passed on as it is.

    timestamp : int
      Passed on as it is.
    """
    #  void QDBusPlatformMenu::popupRequested(int id, uint timestamp)
    self.uglySide.call(
        'ritual_ZN17QDBusPlatformMenu14popupRequestedEij', id, timestamp,
    )

  @staticmethod
  def emitUpdated(*__, **_) -> Never:
    """
    Qt's 'void QDBusPlatformMenu::emitUpdated()': leans on
    'QDBusPlatformMenu::updated(unsigned int, int)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusPlatformMenu.emitUpdated' has no cute function yet. Qt's "
        "'void QDBusPlatformMenu::emitUpdated()': leans on "
        "'QDBusPlatformMenu::updated(unsigned int, int)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def syncSubMenu(*__, **_) -> Never:
    """
    Qt's 'void QDBusPlatformMenu::syncSubMenu(const QDBusPlatformMenu
    *menu)': leans on 'QDBusPlatformMenu::popupRequested(int, unsigned int)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusPlatformMenu.syncSubMenu' has no cute function yet. Qt's "
        "'void QDBusPlatformMenu::syncSubMenu(const QDBusPlatformMenu "
        "*menu)': leans on 'QDBusPlatformMenu::popupRequested(int, unsigned "
        "int)', which Qt's source does not mark for use from outside Qt and "
        "has no code for that could be taken.")
