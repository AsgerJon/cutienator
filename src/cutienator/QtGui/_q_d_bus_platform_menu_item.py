"""
QDBusPlatformMenuItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qdbusplatformmenu_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QDBusPlatformMenuItem to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList
from . import QPlatformMenuItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QFont, QIcon, QKeySequence, QPlatformMenu
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']
  QIcon = WAIT['QIcon']
  QKeySequence = WAIT['QKeySequence']
  QPlatformMenu = WAIT['QPlatformMenu']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDBusPlatformMenuItem(QPlatformMenuItem):
  """
  The cute side of Qt's QDBusPlatformMenuItem: a plain Python object standing
  in front of one C++ QDBusPlatformMenuItem.

  It is built on the cute 'QPlatformMenuItem', as Qt's QDBusPlatformMenuItem
  is built on Qt's QPlatformMenuItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDBusPlatformMenuItem that has a ritual and that
  Python can call so far, 27 names in all: 'metaObject', 'text', 'setText',
  'icon', 'setIcon', 'menu', 'setMenu', 'isEnabled', 'setEnabled',
  'isVisible', 'setVisible', 'isSeparator', 'setIsSeparator', 'setFont',
  'setRole', 'isCheckable', 'setCheckable', 'isChecked', 'setChecked',
  'hasExclusiveGroup', 'setHasExclusiveGroup', 'shortcut', 'setShortcut',
  'setIconSize', 'setNativeContents', 'dbusID', 'trigger'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDBusPlatformMenuItem::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QDBusPlatformMenuItem::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  7 of the 36 functions Qt declares: 4 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 not a gap;
  1 leans on 'QDBusPlatformMenuItem.

  What to expect
  --------------

  - The C++ QDBusPlatformMenuItem is created at the first use, not by
    'QDBusPlatformMenuItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDBusPlatformMenuItem.
  - Qt tells when it has removed the C++ QDBusPlatformMenuItem. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDBusPlatformMenuItem that has no cute function yet,
    '__init__', 'byId', 'byIds', holds a function that raises
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
  __qt_class__ = 'QDBusPlatformMenuItem'

  #  A C++ QDBusPlatformMenuItem Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDBusPlatformMenuItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDBusPlatformMenuItem::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusplatformmenuitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDBusPlatformMenuItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QDBusPlatformMenuItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def text(self) -> str:
    """
    Calls Qt's 'const QString QDBusPlatformMenuItem::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusplatformmenuitem.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString QDBusPlatformMenuItem::text() const
    return self.uglySide.call('ritual_ZNK21QDBusPlatformMenuItem4textEv')

  def icon(self) -> QIcon:
    """
    Calls Qt's 'QIcon QDBusPlatformMenuItem::icon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusplatformmenuitem.html#icon

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QDBusPlatformMenuItem::icon() const
    address = self.uglySide.call('ritual_ZNK21QDBusPlatformMenuItem4iconEv')
    from . import QIcon
    return QIcon._cuteOwning(address)

  def menu(self) -> Optional[QPlatformMenu]:
    """
    Calls Qt's 'const QPlatformMenu *QDBusPlatformMenuItem::menu() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusplatformmenuitem.html#menu

    Returns
    -------

    Optional[QPlatformMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QPlatformMenu *QDBusPlatformMenuItem::menu() const
    address = self.uglySide.call('ritual_ZNK21QDBusPlatformMenuItem4menuEv')
    from . import QPlatformMenu
    return QPlatformMenu._cuteAt(address)

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QDBusPlatformMenuItem::isEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusplatformmenuitem.html#isEnabled
    """
    #  bool QDBusPlatformMenuItem::isEnabled() const
    return self.uglySide.call(
        'ritual_ZNK21QDBusPlatformMenuItem9isEnabledEv',
    )

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QDBusPlatformMenuItem::isVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusplatformmenuitem.html#isVisible
    """
    #  bool QDBusPlatformMenuItem::isVisible() const
    return self.uglySide.call(
        'ritual_ZNK21QDBusPlatformMenuItem9isVisibleEv',
    )

  def isSeparator(self) -> bool:
    """
    Calls Qt's 'bool QDBusPlatformMenuItem::isSeparator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusplatformmenuitem.html#isSeparator
    """
    #  bool QDBusPlatformMenuItem::isSeparator() const
    return self.uglySide.call(
        'ritual_ZNK21QDBusPlatformMenuItem11isSeparatorEv',
    )

  def isCheckable(self) -> bool:
    """
    Calls Qt's 'bool QDBusPlatformMenuItem::isCheckable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusplatformmenuitem.html#isCheckable
    """
    #  bool QDBusPlatformMenuItem::isCheckable() const
    return self.uglySide.call(
        'ritual_ZNK21QDBusPlatformMenuItem11isCheckableEv',
    )

  def isChecked(self) -> bool:
    """
    Calls Qt's 'bool QDBusPlatformMenuItem::isChecked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusplatformmenuitem.html#isChecked
    """
    #  bool QDBusPlatformMenuItem::isChecked() const
    return self.uglySide.call(
        'ritual_ZNK21QDBusPlatformMenuItem9isCheckedEv',
    )

  def hasExclusiveGroup(self) -> bool:
    """
    Calls Qt's 'bool QDBusPlatformMenuItem::hasExclusiveGroup() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusplatformmenuitem.html#hasExclusiveGroup
    """
    #  bool QDBusPlatformMenuItem::hasExclusiveGroup() const
    return self.uglySide.call(
        'ritual_ZNK21QDBusPlatformMenuItem17hasExclusiveGroupEv',
    )

  def shortcut(self) -> QKeySequence:
    """
    Calls Qt's 'QKeySequence QDBusPlatformMenuItem::shortcut() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusplatformmenuitem.html#shortcut

    Returns
    -------

    QKeySequence
      A new cute QKeySequence around the copy Qt gave back. Python owns it.
    """
    #  QKeySequence QDBusPlatformMenuItem::shortcut() const
    address = self.uglySide.call(
        'ritual_ZNK21QDBusPlatformMenuItem8shortcutEv',
    )
    from . import QKeySequence
    return QKeySequence._cuteOwning(address)

  def dbusID(self) -> int:
    """
    Calls Qt's 'int QDBusPlatformMenuItem::dbusID() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusplatformmenuitem.html#dbusID
    """
    #  int QDBusPlatformMenuItem::dbusID() const
    return self.uglySide.call('ritual_ZNK21QDBusPlatformMenuItem6dbusIDEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QDBusPlatformMenuItem::setText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusplatformmenuitem.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDBusPlatformMenuItem::setText(const QString &text)
    ritual = 'ritual_ZN21QDBusPlatformMenuItem7setTextERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QDBusPlatformMenuItem7setTextERK7QString'
    self.uglySide.call(ritual, text)

  @overload(QIcon)
  def setIcon(self, icon: QIcon) -> None:
    """
    Calls Qt's 'void QDBusPlatformMenuItem::setIcon(const QIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusplatformmenuitem.html#setIcon

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.
    """
    #  void QDBusPlatformMenuItem::setIcon(const QIcon &icon)
    ritual = 'ritual_ZN21QDBusPlatformMenuItem7setIconERK5QIcon'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QDBusPlatformMenuItem7setIconERK5QIcon'
    self.uglySide.call(ritual, self._valueOf(icon))

  @overload(QPlatformMenu)
  @overload(NoneType)
  def setMenu(self, menu: Optional[QPlatformMenu]) -> None:
    """
    Calls Qt's 'void QDBusPlatformMenuItem::setMenu(QPlatformMenu *menu)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusplatformmenuitem.html#setMenu

    Parameters
    ----------

    menu : Optional[QPlatformMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDBusPlatformMenuItem::setMenu(QPlatformMenu *menu)
    ritual = 'ritual_ZN21QDBusPlatformMenuItem7setMenuEP13QPlatformMenu'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QDBusPlatformMenuItem7setMenuEP13QPlatformMenu')
    self.uglySide.call(ritual, self._addressOf(menu))

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QDBusPlatformMenuItem::setEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusplatformmenuitem.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QDBusPlatformMenuItem::setEnabled(bool enabled)
    ritual = 'ritual_ZN21QDBusPlatformMenuItem10setEnabledEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QDBusPlatformMenuItem10setEnabledEb'
    self.uglySide.call(ritual, enabled)

  @overload(bool)
  def setVisible(self, isVisible: bool) -> None:
    """
    Calls Qt's 'void QDBusPlatformMenuItem::setVisible(bool isVisible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusplatformmenuitem.html#setVisible

    Parameters
    ----------

    isVisible : bool
      Passed on as it is.
    """
    #  void QDBusPlatformMenuItem::setVisible(bool isVisible)
    ritual = 'ritual_ZN21QDBusPlatformMenuItem10setVisibleEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QDBusPlatformMenuItem10setVisibleEb'
    self.uglySide.call(ritual, isVisible)

  @overload(bool)
  def setIsSeparator(self, isSeparator: bool) -> None:
    """
    Calls Qt's 'void QDBusPlatformMenuItem::setIsSeparator(bool
    isSeparator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusplatformmenuitem.html#setIsSeparator

    Parameters
    ----------

    isSeparator : bool
      Passed on as it is.
    """
    #  void QDBusPlatformMenuItem::setIsSeparator(bool isSeparator)
    ritual = 'ritual_ZN21QDBusPlatformMenuItem14setIsSeparatorEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QDBusPlatformMenuItem14setIsSeparatorEb'
    self.uglySide.call(ritual, isSeparator)

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QDBusPlatformMenuItem::setFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusplatformmenuitem.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QDBusPlatformMenuItem::setFont(const QFont &font)
    ritual = 'ritual_ZN21QDBusPlatformMenuItem7setFontERK5QFont'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QDBusPlatformMenuItem7setFontERK5QFont'
    self.uglySide.call(ritual, self._valueOf(font))

  @overload(QPlatformMenuItem.MenuRole)
  def setRole(self, role: QPlatformMenuItem.MenuRole) -> None:
    """
    Calls Qt's 'void QDBusPlatformMenuItem::setRole(MenuRole role)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusplatformmenuitem.html#setRole

    Parameters
    ----------

    role : QPlatformMenuItem.MenuRole
      Passed on as its number.
    """
    #  void QDBusPlatformMenuItem::setRole(MenuRole role)
    ritual = (
        'ritual_ZN21QDBusPlatformMenuItem7setRoleEN17QPlatformMenuItem8Menu'
        'RoleE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QDBusPlatformMenuItem7setRoleEN17QPlatformMenuIte'
          'm8MenuRoleE')
    self.uglySide.call(ritual, role.value)

  @overload(bool)
  def setCheckable(self, checkable: bool) -> None:
    """
    Calls Qt's 'void QDBusPlatformMenuItem::setCheckable(bool checkable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusplatformmenuitem.html#setCheckable

    Parameters
    ----------

    checkable : bool
      Passed on as it is.
    """
    #  void QDBusPlatformMenuItem::setCheckable(bool checkable)
    ritual = 'ritual_ZN21QDBusPlatformMenuItem12setCheckableEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QDBusPlatformMenuItem12setCheckableEb'
    self.uglySide.call(ritual, checkable)

  @overload(bool)
  def setChecked(self, isChecked: bool) -> None:
    """
    Calls Qt's 'void QDBusPlatformMenuItem::setChecked(bool isChecked)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusplatformmenuitem.html#setChecked

    Parameters
    ----------

    isChecked : bool
      Passed on as it is.
    """
    #  void QDBusPlatformMenuItem::setChecked(bool isChecked)
    ritual = 'ritual_ZN21QDBusPlatformMenuItem10setCheckedEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QDBusPlatformMenuItem10setCheckedEb'
    self.uglySide.call(ritual, isChecked)

  @overload(bool)
  def setHasExclusiveGroup(self, hasExclusiveGroup: bool) -> None:
    """
    Calls Qt's 'void QDBusPlatformMenuItem::setHasExclusiveGroup(bool
    hasExclusiveGroup)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusplatformmenuitem.html#setHasExclusiveGroup

    Parameters
    ----------

    hasExclusiveGroup : bool
      Passed on as it is.
    """
    #  void QDBusPlatformMenuItem::setHasExclusiveGroup(bool
    #      hasExclusiveGroup)
    ritual = 'ritual_ZN21QDBusPlatformMenuItem20setHasExclusiveGroupEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QDBusPlatformMenuItem20setHasExclusiveGroupEb'
    self.uglySide.call(ritual, hasExclusiveGroup)

  @overload(QKeySequence)
  def setShortcut(self, shortcut: QKeySequence) -> None:
    """
    Calls Qt's 'void QDBusPlatformMenuItem::setShortcut(const QKeySequence
    &shortcut)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusplatformmenuitem.html#setShortcut

    Parameters
    ----------

    shortcut : QKeySequence
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own.
    """
    #  void QDBusPlatformMenuItem::setShortcut(const QKeySequence &shortcut)
    ritual = 'ritual_ZN21QDBusPlatformMenuItem11setShortcutERK12QKeySequence'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QDBusPlatformMenuItem11setShortcutERK12QKeySequen'
          'ce')
    self.uglySide.call(ritual, self._valueOf(shortcut))

  @overload(int)
  def setIconSize(self, size: int) -> None:
    """
    Calls Qt's 'void QDBusPlatformMenuItem::setIconSize(int size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusplatformmenuitem.html#setIconSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QDBusPlatformMenuItem::setIconSize(int size)
    ritual = 'ritual_ZN21QDBusPlatformMenuItem11setIconSizeEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QDBusPlatformMenuItem11setIconSizeEi'
    self.uglySide.call(ritual, size)

  @overload(int)
  def setNativeContents(self, item: int) -> None:
    """
    Calls Qt's 'void QDBusPlatformMenuItem::setNativeContents(WId item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusplatformmenuitem.html#setNativeContents

    Parameters
    ----------

    item : int
      Passed on as it is.
    """
    #  void QDBusPlatformMenuItem::setNativeContents(WId item)
    ritual = 'ritual_ZN21QDBusPlatformMenuItem17setNativeContentsEy'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QDBusPlatformMenuItem17setNativeContentsEy'
    self.uglySide.call(ritual, item)

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
    Qt's 'QDBusPlatformMenuItem::QDBusPlatformMenuItem()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'nextDBusID'.
    """
    raise NotImplementedError(
        "'QDBusPlatformMenuItem.__init__' has no cute function yet. Qt's "
        "'QDBusPlatformMenuItem::QDBusPlatformMenuItem()': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'nextDBusID'.")

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

  def trigger(self) -> None:
    """
    Calls Qt's 'void QDBusPlatformMenuItem::trigger()'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusplatformmenuitem.html#trigger
    """
    #  void QDBusPlatformMenuItem::trigger()
    self.uglySide.call('ritual_ZN21QDBusPlatformMenuItem7triggerEv')

  @staticmethod
  def byId(*__, **_) -> Never:
    """
    Qt's 'QDBusPlatformMenuItem *QDBusPlatformMenuItem::byId(int id)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'menuItemsByID'.
    """
    raise NotImplementedError(
        "'QDBusPlatformMenuItem.byId' has no cute function yet. Qt's "
        "'QDBusPlatformMenuItem *QDBusPlatformMenuItem::byId(int id)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'menuItemsByID'.")

  @staticmethod
  def byIds(*__, **_) -> Never:
    """
    Qt's 'QList<const QDBusPlatformMenuItem *>
    QDBusPlatformMenuItem::byIds(const QList<int> &ids)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'menuItemsByID'.
    """
    raise NotImplementedError(
        "'QDBusPlatformMenuItem.byIds' has no cute function yet. Qt's "
        "'QList<const QDBusPlatformMenuItem *> "
        "QDBusPlatformMenuItem::byIds(const QList<int> &ids)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'menuItemsByID'.")


#  Qt's 'QList<QDBusPlatformMenuItem *>': the list of QDBusPlatformMenuItem,
#  which 'QList[QDBusPlatformMenuItem]' gives. It is made here, so that there
#  is one as soon as there can be a QDBusPlatformMenuItem.
QList.createKind(
    QDBusPlatformMenuItem, 'address',
    make='ritual_list_make_QDBusPlatformMenuItem_ptr',
    add='ritual_list_add_QDBusPlatformMenuItem_ptr',
    size='ritual_list_size_QDBusPlatformMenuItem_ptr',
    at='ritual_list_at_QDBusPlatformMenuItem_ptr',
    drop='ritual_list_drop_QDBusPlatformMenuItem_ptr',
)
