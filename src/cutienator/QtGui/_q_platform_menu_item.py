"""
QPlatformMenuItem binding of the Qt C++
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


class QPlatformMenuItem(QObject):
  """
  The cute side of Qt's QPlatformMenuItem: a plain Python object standing in
  front of one C++ QPlatformMenuItem.

  It is built on the cute 'QObject', as Qt's QPlatformMenuItem is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformMenuItem that has a ritual and that Python
  can call so far, 20 names in all: 'metaObject', 'tr', 'setTag', 'tag',
  'setText', 'setIcon', 'setMenu', 'setVisible', 'setIsSeparator', 'setFont',
  'setRole', 'setCheckable', 'setChecked', 'setShortcut', 'setEnabled',
  'setIconSize', 'setNativeContents', 'setHasExclusiveGroup', 'activated',
  'hovered'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlatformMenuItem::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QPlatformMenuItem::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  3 of the 25 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QPlatformMenuItem is created at the first use, not by
    'QPlatformMenuItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformMenuItem.
  - Qt tells when it has removed the C++ QPlatformMenuItem. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QPlatformMenuItem that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QPlatformMenuItem, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class MenuRole(CuteNum):
    """
    The enum 'QPlatformMenuItem::MenuRole' of Qt, with the 12 names Qt gives
    in it.
    """

    NoRole = Kee[int](0)
    TextHeuristicRole = Kee[int](1)
    ApplicationSpecificRole = Kee[int](2)
    AboutQtRole = Kee[int](3)
    AboutRole = Kee[int](4)
    PreferencesRole = Kee[int](5)
    QuitRole = Kee[int](6)
    CutRole = Kee[int](7)
    CopyRole = Kee[int](8)
    PasteRole = Kee[int](9)
    SelectAllRole = Kee[int](10)
    RoleCount = Kee[int](11)

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
    Calls Qt's 'QString QPlatformMenuItem::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenuitem.html#tr

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
    #  QString QPlatformMenuItem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QPlatformMenuItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformMenuItem'

  #  The functions Qt calls itself that QPlatformMenuItem is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setTag': (
          ('_ZN17QPlatformMenuItem6setTagEy',
           ('nothing', 'nothing', ''),
           (
               ('unsigned long long', 'number', ''),
           )),
      ),
      'tag': (
          ('_ZNK17QPlatformMenuItem3tagEv',
           ('unsigned long long', 'number', ''),
           ()),
      ),
      'setText': (
          ('_ZN17QPlatformMenuItem7setTextERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'setIcon': (
          ('_ZN17QPlatformMenuItem7setIconERK5QIcon',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QIcon'),
           )),
      ),
      'setMenu': (
          ('_ZN17QPlatformMenuItem7setMenuEP13QPlatformMenu',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPlatformMenu'),
           )),
      ),
      'setVisible': (
          ('_ZN17QPlatformMenuItem10setVisibleEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setIsSeparator': (
          ('_ZN17QPlatformMenuItem14setIsSeparatorEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setFont': (
          ('_ZN17QPlatformMenuItem7setFontERK5QFont',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QFont'),
           )),
      ),
      'setRole': (
          ('_ZN17QPlatformMenuItem7setRoleENS_8MenuRoleE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtGui:QPlatformMenuItem.MenuRole'),
           )),
      ),
      'setCheckable': (
          ('_ZN17QPlatformMenuItem12setCheckableEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setChecked': (
          ('_ZN17QPlatformMenuItem10setCheckedEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setShortcut': (
          ('_ZN17QPlatformMenuItem11setShortcutERK12QKeySequence',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QKeySequence'),
           )),
      ),
      'setEnabled': (
          ('_ZN17QPlatformMenuItem10setEnabledEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setIconSize': (
          ('_ZN17QPlatformMenuItem11setIconSizeEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'setNativeContents': (
          ('_ZN17QPlatformMenuItem17setNativeContentsEy',
           ('nothing', 'nothing', ''),
           (
               ('unsigned long long', 'number', ''),
           )),
      ),
      'setHasExclusiveGroup': (
          ('_ZN17QPlatformMenuItem20setHasExclusiveGroupEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
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
    Calls Qt's 'const QMetaObject *QPlatformMenuItem::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenuitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlatformMenuItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QPlatformMenuItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def tag(self) -> int:
    """
    Calls Qt's 'quintptr QPlatformMenuItem::tag() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenuitem.html#tag
    """
    #  quintptr QPlatformMenuItem::tag() const
    ritual = 'ritual_ZNK17QPlatformMenuItem3tagEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QPlatformMenuItem3tagEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setTag(self, tag: int) -> None:
    """
    Calls Qt's 'void QPlatformMenuItem::setTag(quintptr tag)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenuitem.html#setTag

    Parameters
    ----------

    tag : int
      Passed on as it is.
    """
    #  void QPlatformMenuItem::setTag(quintptr tag)
    ritual = 'ritual_ZN17QPlatformMenuItem6setTagEy'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QPlatformMenuItem6setTagEy'
    self.uglySide.call(ritual, tag)

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QPlatformMenuItem::setText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenuitem.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlatformMenuItem::setText(const QString &text)
    self.uglySide.call(
        'ritual_ZN17QPlatformMenuItem7setTextERK7QString', text,
    )

  @overload(QIcon)
  def setIcon(self, icon: QIcon) -> None:
    """
    Calls Qt's 'void QPlatformMenuItem::setIcon(const QIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenuitem.html#setIcon

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.
    """
    #  void QPlatformMenuItem::setIcon(const QIcon &icon)
    self.uglySide.call(
        'ritual_ZN17QPlatformMenuItem7setIconERK5QIcon', self._valueOf(icon),
    )

  @overload(QPlatformMenu)
  @overload(NoneType)
  def setMenu(self, menu: Optional[QPlatformMenu]) -> None:
    """
    Calls Qt's 'void QPlatformMenuItem::setMenu(QPlatformMenu *menu)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenuitem.html#setMenu

    Parameters
    ----------

    menu : Optional[QPlatformMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformMenuItem::setMenu(QPlatformMenu *menu)
    self.uglySide.call(
        'ritual_ZN17QPlatformMenuItem7setMenuEP13QPlatformMenu',
        self._addressOf(menu),
    )

  @overload(bool)
  def setVisible(self, isVisible: bool) -> None:
    """
    Calls Qt's 'void QPlatformMenuItem::setVisible(bool isVisible)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenuitem.html#setVisible

    Parameters
    ----------

    isVisible : bool
      Passed on as it is.
    """
    #  void QPlatformMenuItem::setVisible(bool isVisible)
    self.uglySide.call(
        'ritual_ZN17QPlatformMenuItem10setVisibleEb', isVisible,
    )

  @overload(bool)
  def setIsSeparator(self, isSeparator: bool) -> None:
    """
    Calls Qt's 'void QPlatformMenuItem::setIsSeparator(bool isSeparator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmenuitem.html#setIsSeparator

    Parameters
    ----------

    isSeparator : bool
      Passed on as it is.
    """
    #  void QPlatformMenuItem::setIsSeparator(bool isSeparator)
    self.uglySide.call(
        'ritual_ZN17QPlatformMenuItem14setIsSeparatorEb', isSeparator,
    )

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QPlatformMenuItem::setFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenuitem.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QPlatformMenuItem::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN17QPlatformMenuItem7setFontERK5QFont', self._valueOf(font),
    )

  @overload(MenuRole)
  def setRole(self, role: MenuRole) -> None:
    """
    Calls Qt's 'void QPlatformMenuItem::setRole(MenuRole role)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenuitem.html#setRole

    Parameters
    ----------

    role : MenuRole
      Passed on as its number.
    """
    #  void QPlatformMenuItem::setRole(MenuRole role)
    self.uglySide.call(
        'ritual_ZN17QPlatformMenuItem7setRoleENS_8MenuRoleE', role.value,
    )

  @overload(bool)
  def setCheckable(self, checkable: bool) -> None:
    """
    Calls Qt's 'void QPlatformMenuItem::setCheckable(bool checkable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmenuitem.html#setCheckable

    Parameters
    ----------

    checkable : bool
      Passed on as it is.
    """
    #  void QPlatformMenuItem::setCheckable(bool checkable)
    self.uglySide.call(
        'ritual_ZN17QPlatformMenuItem12setCheckableEb', checkable,
    )

  @overload(bool)
  def setChecked(self, isChecked: bool) -> None:
    """
    Calls Qt's 'void QPlatformMenuItem::setChecked(bool isChecked)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenuitem.html#setChecked

    Parameters
    ----------

    isChecked : bool
      Passed on as it is.
    """
    #  void QPlatformMenuItem::setChecked(bool isChecked)
    self.uglySide.call(
        'ritual_ZN17QPlatformMenuItem10setCheckedEb', isChecked,
    )

  @overload(QKeySequence)
  def setShortcut(self, shortcut: QKeySequence) -> None:
    """
    Calls Qt's 'void QPlatformMenuItem::setShortcut(const QKeySequence
    &shortcut)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenuitem.html#setShortcut

    Parameters
    ----------

    shortcut : QKeySequence
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own.
    """
    #  void QPlatformMenuItem::setShortcut(const QKeySequence &shortcut)
    self.uglySide.call(
        'ritual_ZN17QPlatformMenuItem11setShortcutERK12QKeySequence',
        self._valueOf(shortcut),
    )

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QPlatformMenuItem::setEnabled(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenuitem.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QPlatformMenuItem::setEnabled(bool enabled)
    self.uglySide.call('ritual_ZN17QPlatformMenuItem10setEnabledEb', enabled)

  @overload(int)
  def setIconSize(self, size: int) -> None:
    """
    Calls Qt's 'void QPlatformMenuItem::setIconSize(int size)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenuitem.html#setIconSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QPlatformMenuItem::setIconSize(int size)
    self.uglySide.call('ritual_ZN17QPlatformMenuItem11setIconSizeEi', size)

  @overload(int)
  def setNativeContents(self, item: int) -> None:
    """
    Calls Qt's 'void QPlatformMenuItem::setNativeContents(WId item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmenuitem.html#setNativeContents

    Parameters
    ----------

    item : int
      Passed on as it is.
    """
    #  void QPlatformMenuItem::setNativeContents(WId item)
    ritual = 'ritual_ZN17QPlatformMenuItem17setNativeContentsEy'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QPlatformMenuItem17setNativeContentsEy'
    self.uglySide.call(ritual, item)

  @overload(bool)
  def setHasExclusiveGroup(self, hasExclusiveGroup: bool) -> None:
    """
    Calls Qt's 'void QPlatformMenuItem::setHasExclusiveGroup(bool
    hasExclusiveGroup)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmenuitem.html#setHasExclusiveGroup

    Parameters
    ----------

    hasExclusiveGroup : bool
      Passed on as it is.
    """
    #  void QPlatformMenuItem::setHasExclusiveGroup(bool hasExclusiveGroup)
    ritual = 'ritual_ZN17QPlatformMenuItem20setHasExclusiveGroupEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QPlatformMenuItem20setHasExclusiveGroupEb'
    self.uglySide.call(ritual, hasExclusiveGroup)

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
    Qt's 'QPlatformMenuItem::QPlatformMenuItem()': the class is abstract, so
    C++ cannot make one, and the C++ class of ours does not fill in every
    function it leaves open.
    """
    raise NotImplementedError(
        "'QPlatformMenuItem.__init__' has no cute function yet. Qt's "
        "'QPlatformMenuItem::QPlatformMenuItem()': the class is abstract, "
        "so C++ cannot make one, and the C++ class of ours does not fill in "
        "every function it leaves open.")

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

  def activated(self) -> None:
    """
    Calls Qt's 'void QPlatformMenuItem::activated()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenuitem.html#activated
    """
    #  void QPlatformMenuItem::activated()
    self.uglySide.call('ritual_ZN17QPlatformMenuItem9activatedEv')

  def hovered(self) -> None:
    """
    Calls Qt's 'void QPlatformMenuItem::hovered()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenuitem.html#hovered
    """
    #  void QPlatformMenuItem::hovered()
    self.uglySide.call('ritual_ZN17QPlatformMenuItem7hoveredEv')
