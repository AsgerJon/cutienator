"""
QPlatformMenu binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformmenu.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRect
  from . import QFont, QIcon, QPlatformMenuItem, QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']
  QIcon = WAIT['QIcon']
  QPlatformMenuItem = WAIT['QPlatformMenuItem']
  QRect = WAIT['QRect']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformMenu(QObject):
  """
  The cute side of Qt's QPlatformMenu: a plain Python object standing in
  front of one C++ QPlatformMenu.

  It is built on the cute 'QObject', as Qt's QPlatformMenu is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformMenu that has a ritual and that Python can
  call so far, 24 names in all: 'metaObject', 'tr', 'insertMenuItem',
  'removeMenuItem', 'syncMenuItem', 'syncSeparatorsCollapsible', 'setTag',
  'tag', 'setText', 'setIcon', 'setEnabled', 'isEnabled', 'setVisible',
  'setMinimumWidth', 'setFont', 'setMenuType', 'showPopup', 'dismiss',
  'menuItemAt', 'menuItemForTag', 'createMenuItem', 'createSubMenu',
  'aboutToShow', 'aboutToHide'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlatformMenu::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QPlatformMenu::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  3 of the 29 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QPlatformMenu is created at the first use, not by
    'QPlatformMenu(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformMenu.
  - Qt tells when it has removed the C++ QPlatformMenu. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QPlatformMenu that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QPlatformMenu, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class MenuType(CuteNum):
    """
    The enum 'QPlatformMenu::MenuType' of Qt, with the 2 names Qt gives in
    it.
    """

    DefaultMenu = Kee[int](0)
    EditMenu = Kee[int](1)

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
    Calls Qt's 'QString QPlatformMenu::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenu.html#tr

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
    #  QString QPlatformMenu::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QPlatformMenu2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformMenu'

  #  The functions Qt calls itself that QPlatformMenu is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'insertMenuItem': (
          ('_ZN13QPlatformMenu14insertMenuItemEP17QPlatformMenuItemS1_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPlatformMenuItem'),
               ('address', 'address', 'QtGui:QPlatformMenuItem'),
           )),
      ),
      'removeMenuItem': (
          ('_ZN13QPlatformMenu14removeMenuItemEP17QPlatformMenuItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPlatformMenuItem'),
           )),
      ),
      'syncMenuItem': (
          ('_ZN13QPlatformMenu12syncMenuItemEP17QPlatformMenuItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPlatformMenuItem'),
           )),
      ),
      'syncSeparatorsCollapsible': (
          ('_ZN13QPlatformMenu25syncSeparatorsCollapsibleEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setTag': (
          ('_ZN13QPlatformMenu6setTagEy',
           ('nothing', 'nothing', ''),
           (
               ('unsigned long long', 'number', ''),
           )),
      ),
      'tag': (
          ('_ZNK13QPlatformMenu3tagEv',
           ('unsigned long long', 'number', ''),
           ()),
      ),
      'setText': (
          ('_ZN13QPlatformMenu7setTextERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'setIcon': (
          ('_ZN13QPlatformMenu7setIconERK5QIcon',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QIcon'),
           )),
      ),
      'setEnabled': (
          ('_ZN13QPlatformMenu10setEnabledEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'isEnabled': (
          ('_ZNK13QPlatformMenu9isEnabledEv',
           ('bool', 'number', ''),
           ()),
      ),
      'setVisible': (
          ('_ZN13QPlatformMenu10setVisibleEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setMinimumWidth': (
          ('_ZN13QPlatformMenu15setMinimumWidthEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'setFont': (
          ('_ZN13QPlatformMenu7setFontERK5QFont',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QFont'),
           )),
      ),
      'setMenuType': (
          ('_ZN13QPlatformMenu11setMenuTypeENS_8MenuTypeE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtGui:QPlatformMenu.MenuType'),
           )),
      ),
      'showPopup': (
          ('_ZN13QPlatformMenu9showPopupEPK7QWindowRK5QRectPK17QPlatformMen'
           'uItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QWindow'),
               ('address', 'value', 'QtCore:QRect'),
               ('address', 'address', 'QtGui:QPlatformMenuItem'),
           )),
      ),
      'dismiss': (
          ('_ZN13QPlatformMenu7dismissEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'menuItemAt': (
          ('_ZNK13QPlatformMenu10menuItemAtEi',
           ('address', 'address', 'QtGui:QPlatformMenuItem'),
           (
               ('int', 'number', ''),
           )),
      ),
      'menuItemForTag': (
          ('_ZNK13QPlatformMenu14menuItemForTagEy',
           ('address', 'address', 'QtGui:QPlatformMenuItem'),
           (
               ('unsigned long long', 'number', ''),
           )),
      ),
      'createMenuItem': (
          ('_ZNK13QPlatformMenu14createMenuItemEv',
           ('address', 'address', 'QtGui:QPlatformMenuItem'),
           ()),
      ),
      'createSubMenu': (
          ('_ZNK13QPlatformMenu13createSubMenuEv',
           ('address', 'address', 'QtGui:QPlatformMenu'),
           ()),
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
    Calls Qt's 'const QMetaObject *QPlatformMenu::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenu.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlatformMenu::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QPlatformMenu10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def tag(self) -> int:
    """
    Calls Qt's 'quintptr QPlatformMenu::tag() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenu.html#tag
    """
    #  quintptr QPlatformMenu::tag() const
    ritual = 'ritual_ZNK13QPlatformMenu3tagEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QPlatformMenu3tagEv'
    return self.uglySide.call(ritual)

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QPlatformMenu::isEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenu.html#isEnabled
    """
    #  bool QPlatformMenu::isEnabled() const
    ritual = 'ritual_ZNK13QPlatformMenu9isEnabledEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QPlatformMenu9isEnabledEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def menuItemAt(self, position: int) -> Optional[QPlatformMenuItem]:
    """
    Calls Qt's 'QPlatformMenuItem *QPlatformMenu::menuItemAt(int position)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenu.html#menuItemAt

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
    #  QPlatformMenuItem *QPlatformMenu::menuItemAt(int position) const
    address = self.uglySide.call(
        'ritual_ZNK13QPlatformMenu10menuItemAtEi', position,
    )
    from . import QPlatformMenuItem
    return QPlatformMenuItem._cuteAt(address)

  @overload(int)
  def menuItemForTag(self, tag: int) -> Optional[QPlatformMenuItem]:
    """
    Calls Qt's 'QPlatformMenuItem *QPlatformMenu::menuItemForTag(quintptr
    tag) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenu.html#menuItemForTag

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
    #  QPlatformMenuItem *QPlatformMenu::menuItemForTag(quintptr tag) const
    address = self.uglySide.call(
        'ritual_ZNK13QPlatformMenu14menuItemForTagEy', tag,
    )
    from . import QPlatformMenuItem
    return QPlatformMenuItem._cuteAt(address)

  def createMenuItem(self) -> Optional[QPlatformMenuItem]:
    """
    Calls Qt's 'QPlatformMenuItem *QPlatformMenu::createMenuItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenu.html#createMenuItem

    Returns
    -------

    Optional[QPlatformMenuItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMenuItem *QPlatformMenu::createMenuItem() const
    ritual = 'ritual_ZNK13QPlatformMenu14createMenuItemEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QPlatformMenu14createMenuItemEv'
    address = self.uglySide.call(ritual)
    from . import QPlatformMenuItem
    return QPlatformMenuItem._cuteAt(address)

  def createSubMenu(self) -> Optional[QPlatformMenu]:
    """
    Calls Qt's 'QPlatformMenu *QPlatformMenu::createSubMenu() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenu.html#createSubMenu

    Returns
    -------

    Optional[QPlatformMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMenu *QPlatformMenu::createSubMenu() const
    ritual = 'ritual_ZNK13QPlatformMenu13createSubMenuEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QPlatformMenu13createSubMenuEv'
    address = self.uglySide.call(ritual)
    return QPlatformMenu._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setTag(self, tag: int) -> None:
    """
    Calls Qt's 'void QPlatformMenu::setTag(quintptr tag)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenu.html#setTag

    Parameters
    ----------

    tag : int
      Passed on as it is.
    """
    #  void QPlatformMenu::setTag(quintptr tag)
    ritual = 'ritual_ZN13QPlatformMenu6setTagEy'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QPlatformMenu6setTagEy'
    self.uglySide.call(ritual, tag)

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QPlatformMenu::setText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenu.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlatformMenu::setText(const QString &text)
    self.uglySide.call('ritual_ZN13QPlatformMenu7setTextERK7QString', text)

  @overload(QIcon)
  def setIcon(self, icon: QIcon) -> None:
    """
    Calls Qt's 'void QPlatformMenu::setIcon(const QIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenu.html#setIcon

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.
    """
    #  void QPlatformMenu::setIcon(const QIcon &icon)
    self.uglySide.call(
        'ritual_ZN13QPlatformMenu7setIconERK5QIcon', self._valueOf(icon),
    )

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QPlatformMenu::setEnabled(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenu.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QPlatformMenu::setEnabled(bool enabled)
    self.uglySide.call('ritual_ZN13QPlatformMenu10setEnabledEb', enabled)

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QPlatformMenu::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenu.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QPlatformMenu::setVisible(bool visible)
    self.uglySide.call('ritual_ZN13QPlatformMenu10setVisibleEb', visible)

  @overload(int)
  def setMinimumWidth(self, width: int) -> None:
    """
    Calls Qt's 'void QPlatformMenu::setMinimumWidth(int width)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenu.html#setMinimumWidth

    Parameters
    ----------

    width : int
      Passed on as it is.
    """
    #  void QPlatformMenu::setMinimumWidth(int width)
    ritual = 'ritual_ZN13QPlatformMenu15setMinimumWidthEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QPlatformMenu15setMinimumWidthEi'
    self.uglySide.call(ritual, width)

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QPlatformMenu::setFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenu.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QPlatformMenu::setFont(const QFont &font)
    ritual = 'ritual_ZN13QPlatformMenu7setFontERK5QFont'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QPlatformMenu7setFontERK5QFont'
    self.uglySide.call(ritual, self._valueOf(font))

  @overload(MenuType)
  def setMenuType(self, type: MenuType) -> None:
    """
    Calls Qt's 'void QPlatformMenu::setMenuType(MenuType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenu.html#setMenuType

    Parameters
    ----------

    type : MenuType
      Passed on as its number.
    """
    #  void QPlatformMenu::setMenuType(MenuType type)
    ritual = 'ritual_ZN13QPlatformMenu11setMenuTypeENS_8MenuTypeE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QPlatformMenu11setMenuTypeENS_8MenuTypeE'
    self.uglySide.call(ritual, type.value)

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
    Qt's 'QPlatformMenu::QPlatformMenu()': the class is abstract, so C++
    cannot make one, and the C++ class of ours does not fill in every
    function it leaves open.
    """
    raise NotImplementedError(
        "'QPlatformMenu.__init__' has no cute function yet. Qt's "
        "'QPlatformMenu::QPlatformMenu()': the class is abstract, so C++ "
        "cannot make one, and the C++ class of ours does not fill in every "
        "function it leaves open.")

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
    Calls Qt's 'void QPlatformMenu::insertMenuItem(QPlatformMenuItem
    *menuItem, QPlatformMenuItem *before)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenu.html#insertMenuItem

    Parameters
    ----------

    menuItem : Optional[QPlatformMenuItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    before : Optional[QPlatformMenuItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformMenu::insertMenuItem(QPlatformMenuItem *menuItem,
    #      QPlatformMenuItem *before)
    self.uglySide.call(
        'ritual_ZN13QPlatformMenu14insertMenuItemEP17QPlatformMenuItemS1_',
        self._addressOf(menuItem), self._addressOf(before),
    )

  @overload(QPlatformMenuItem)
  @overload(NoneType)
  def removeMenuItem(self, menuItem: Optional[QPlatformMenuItem]) -> None:
    """
    Calls Qt's 'void QPlatformMenu::removeMenuItem(QPlatformMenuItem
    *menuItem)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenu.html#removeMenuItem

    Parameters
    ----------

    menuItem : Optional[QPlatformMenuItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformMenu::removeMenuItem(QPlatformMenuItem *menuItem)
    self.uglySide.call(
        'ritual_ZN13QPlatformMenu14removeMenuItemEP17QPlatformMenuItem',
        self._addressOf(menuItem),
    )

  @overload(QPlatformMenuItem)
  @overload(NoneType)
  def syncMenuItem(self, menuItem: Optional[QPlatformMenuItem]) -> None:
    """
    Calls Qt's 'void QPlatformMenu::syncMenuItem(QPlatformMenuItem
    *menuItem)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenu.html#syncMenuItem

    Parameters
    ----------

    menuItem : Optional[QPlatformMenuItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformMenu::syncMenuItem(QPlatformMenuItem *menuItem)
    self.uglySide.call(
        'ritual_ZN13QPlatformMenu12syncMenuItemEP17QPlatformMenuItem',
        self._addressOf(menuItem),
    )

  @overload(bool)
  def syncSeparatorsCollapsible(self, enable: bool) -> None:
    """
    Calls Qt's 'void QPlatformMenu::syncSeparatorsCollapsible(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmenu.html#syncSeparatorsCollapsible

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QPlatformMenu::syncSeparatorsCollapsible(bool enable)
    self.uglySide.call(
        'ritual_ZN13QPlatformMenu25syncSeparatorsCollapsibleEb', enable,
    )

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
    Calls Qt's 'void QPlatformMenu::showPopup(const QWindow *parentWindow,
    const QRect &targetRect, const QPlatformMenuItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenu.html#showPopup

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
    #  void QPlatformMenu::showPopup(const QWindow *parentWindow, const QRect
    #      &targetRect, const QPlatformMenuItem *item)
    ritual = (
        'ritual_ZN13QPlatformMenu9showPopupEPK7QWindowRK5QRectPK17QPlatform'
        'MenuItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QPlatformMenu9showPopupEPK7QWindowRK5QRectPK17QPl'
          'atformMenuItem')
    self.uglySide.call(
        ritual,
        self._addressOf(parentWindow), self._valueOf(targetRect),
        self._addressOf(item),
    )

  def dismiss(self) -> None:
    """
    Calls Qt's 'void QPlatformMenu::dismiss()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenu.html#dismiss
    """
    #  void QPlatformMenu::dismiss()
    ritual = 'ritual_ZN13QPlatformMenu7dismissEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QPlatformMenu7dismissEv'
    self.uglySide.call(ritual)

  def aboutToShow(self) -> None:
    """
    Calls Qt's 'void QPlatformMenu::aboutToShow()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenu.html#aboutToShow
    """
    #  void QPlatformMenu::aboutToShow()
    self.uglySide.call('ritual_ZN13QPlatformMenu11aboutToShowEv')

  def aboutToHide(self) -> None:
    """
    Calls Qt's 'void QPlatformMenu::aboutToHide()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenu.html#aboutToHide
    """
    #  void QPlatformMenu::aboutToHide()
    self.uglySide.call('ritual_ZN13QPlatformMenu11aboutToHideEv')
