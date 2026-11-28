"""
QQuickLabsPlatformMenuItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformmenuitem_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickLabsPlatformMenuItem to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtGui import QPlatformMenuItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQuickLabsPlatformIcon, QQuickLabsPlatformMenu
  from . import QQuickLabsPlatformMenuItemGroup
  from ..QtCore import QEvent, QMetaObject, QVariant
  from ..QtGui import QFont
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickLabsPlatformMenuItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickLabsPlatformMenuItem: a plain Python object
  standing in front of one C++ QQuickLabsPlatformMenuItem.

  What exists
  -----------

  Every function of Qt's QQuickLabsPlatformMenuItem that has a ritual and
  that Python can call so far, 39 names in all: 'metaObject',
  'qmlExtendedNamespace', 'handle', 'menu', 'subMenu', 'group', 'isEnabled',
  'isVisible', 'isSeparator', 'isCheckable', 'isChecked', 'role', 'text',
  'shortcut', 'font', 'icon', 'toggle', 'triggered', 'hovered',
  'menuChanged', 'subMenuChanged', 'groupChanged', 'enabledChanged',
  'visibleChanged', 'separatorChanged', 'checkableChanged', 'checkedChanged',
  'roleChanged', 'textChanged', 'shortcutChanged', 'fontChanged',
  'iconChanged', 'classBegin', 'componentComplete', 'event', 'activate',
  'updateIcon', 'addShortcut', 'removeShortcut'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickLabsPlatformMenuItem::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickLabsPlatformMenuItem::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickLabsPlatformMenuItem::qt_qmlMarker_extendedNamespace()':
    one of Qt's own inner workings.
  - Qt's 'QQuickLabsPlatformMenuItem::~QQuickLabsPlatformMenuItem()': the
    destructor: Python never removes a C++ QQuickLabsPlatformMenuItem.

  What has no ritual
  ------------------

  20 of the 63 functions Qt declares: 17 leans on
  'QQuickLabsPlatformMenuItem; 2 not a gap; 1 Qt's library has no name for
  it, and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQuickLabsPlatformMenuItem is created at the first use, not by
    'QQuickLabsPlatformMenuItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickLabsPlatformMenuItem.
  - Qt tells when it has removed the C++ QQuickLabsPlatformMenuItem. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickLabsPlatformMenuItem that has no cute function
    yet, '__init__', 'create', 'iconLoader', 'setCheckable', 'setChecked',
    'setEnabled', 'setFont', 'setGroup', 'setIcon', 'setMenu', 'setRole',
    'setSeparator', 'setShortcut', 'setSubMenu', 'setText', 'setVisible',
    'sync', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def qmlExtendedNamespace() -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuickLabsPlatformMenuItem::qmlExtendedNamespace()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickLabsPlatformMenuItem::qmlExtendedNamespace()
    address = Rituals.call(
        'ritual_ZN26QQuickLabsPlatformMenuItem20qmlExtendedNamespaceEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickLabsPlatformMenuItem'

  #  A C++ QQuickLabsPlatformMenuItem Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickLabsPlatformMenuItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickLabsPlatformMenuItem::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickLabsPlatformMenuItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickLabsPlatformMenuItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def handle(self) -> Optional[QPlatformMenuItem]:
    """
    Calls Qt's 'QPlatformMenuItem *QQuickLabsPlatformMenuItem::handle()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#handle

    Returns
    -------

    Optional[QPlatformMenuItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMenuItem *QQuickLabsPlatformMenuItem::handle() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickLabsPlatformMenuItem6handleEv',
    )
    return QPlatformMenuItem._cuteAt(address)

  def menu(self) -> Optional[QQuickLabsPlatformMenu]:
    """
    Calls Qt's 'QQuickLabsPlatformMenu *QQuickLabsPlatformMenuItem::menu()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#menu

    Returns
    -------

    Optional[QQuickLabsPlatformMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickLabsPlatformMenu *QQuickLabsPlatformMenuItem::menu() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickLabsPlatformMenuItem4menuEv',
    )
    from . import QQuickLabsPlatformMenu
    return QQuickLabsPlatformMenu._cuteAt(address)

  def subMenu(self) -> Optional[QQuickLabsPlatformMenu]:
    """
    Calls Qt's 'QQuickLabsPlatformMenu *QQuickLabsPlatformMenuItem::subMenu()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#subMenu

    Returns
    -------

    Optional[QQuickLabsPlatformMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickLabsPlatformMenu *QQuickLabsPlatformMenuItem::subMenu() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickLabsPlatformMenuItem7subMenuEv',
    )
    from . import QQuickLabsPlatformMenu
    return QQuickLabsPlatformMenu._cuteAt(address)

  def group(self) -> Optional[QQuickLabsPlatformMenuItemGroup]:
    """
    Calls Qt's 'QQuickLabsPlatformMenuItemGroup
    *QQuickLabsPlatformMenuItem::group() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#group

    Returns
    -------

    Optional[QQuickLabsPlatformMenuItemGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickLabsPlatformMenuItemGroup *QQuickLabsPlatformMenuItem::group()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickLabsPlatformMenuItem5groupEv',
    )
    from . import QQuickLabsPlatformMenuItemGroup
    return QQuickLabsPlatformMenuItemGroup._cuteAt(address)

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickLabsPlatformMenuItem::isEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#isEnabled
    """
    #  bool QQuickLabsPlatformMenuItem::isEnabled() const
    return self.uglySide.call(
        'ritual_ZNK26QQuickLabsPlatformMenuItem9isEnabledEv',
    )

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QQuickLabsPlatformMenuItem::isVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#isVisible
    """
    #  bool QQuickLabsPlatformMenuItem::isVisible() const
    return self.uglySide.call(
        'ritual_ZNK26QQuickLabsPlatformMenuItem9isVisibleEv',
    )

  def isSeparator(self) -> bool:
    """
    Calls Qt's 'bool QQuickLabsPlatformMenuItem::isSeparator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#isSeparator
    """
    #  bool QQuickLabsPlatformMenuItem::isSeparator() const
    return self.uglySide.call(
        'ritual_ZNK26QQuickLabsPlatformMenuItem11isSeparatorEv',
    )

  def isCheckable(self) -> bool:
    """
    Calls Qt's 'bool QQuickLabsPlatformMenuItem::isCheckable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#isCheckable
    """
    #  bool QQuickLabsPlatformMenuItem::isCheckable() const
    return self.uglySide.call(
        'ritual_ZNK26QQuickLabsPlatformMenuItem11isCheckableEv',
    )

  def isChecked(self) -> bool:
    """
    Calls Qt's 'bool QQuickLabsPlatformMenuItem::isChecked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#isChecked
    """
    #  bool QQuickLabsPlatformMenuItem::isChecked() const
    return self.uglySide.call(
        'ritual_ZNK26QQuickLabsPlatformMenuItem9isCheckedEv',
    )

  def role(self) -> QPlatformMenuItem.MenuRole:
    """
    Calls Qt's 'QPlatformMenuItem::MenuRole
    QQuickLabsPlatformMenuItem::role() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#role

    Returns
    -------

    QPlatformMenuItem.MenuRole
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPlatformMenuItem.MenuRole(number)' gives.
    """
    #  QPlatformMenuItem::MenuRole QQuickLabsPlatformMenuItem::role() const
    return QPlatformMenuItem.MenuRole(self.uglySide.call(
        'ritual_ZNK26QQuickLabsPlatformMenuItem4roleEv',
    ))

  def text(self) -> str:
    """
    Calls Qt's 'QString QQuickLabsPlatformMenuItem::text() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickLabsPlatformMenuItem::text() const
    return self.uglySide.call(
        'ritual_ZNK26QQuickLabsPlatformMenuItem4textEv',
    )

  def shortcut(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickLabsPlatformMenuItem::shortcut() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#shortcut

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickLabsPlatformMenuItem::shortcut() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickLabsPlatformMenuItem8shortcutEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickLabsPlatformMenuItem::font() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickLabsPlatformMenuItem::font() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickLabsPlatformMenuItem4fontEv',
    )
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def icon(self) -> QQuickLabsPlatformIcon:
    """
    Calls Qt's 'QQuickLabsPlatformIcon QQuickLabsPlatformMenuItem::icon()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#icon

    Returns
    -------

    QQuickLabsPlatformIcon
      A new cute QQuickLabsPlatformIcon around the copy Qt gave back. Python
      owns it.
    """
    #  QQuickLabsPlatformIcon QQuickLabsPlatformMenuItem::icon() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickLabsPlatformMenuItem4iconEv',
    )
    from . import QQuickLabsPlatformIcon
    return QQuickLabsPlatformIcon._cuteOwning(address)

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
    Qt's 'QQuickLabsPlatformMenuItem::QQuickLabsPlatformMenuItem(QObject
    *parent)': leans on
    'QQuickLabsPlatformMenuItem::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuItem.__init__' has no cute function yet. "
        "Qt's "
        "'QQuickLabsPlatformMenuItem::QQuickLabsPlatformMenuItem(QObject "
        "*parent)': leans on "
        "'QQuickLabsPlatformMenuItem::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  def toggle(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuItem::toggle()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#toggle
    """
    #  void QQuickLabsPlatformMenuItem::toggle()
    self.uglySide.call('ritual_ZN26QQuickLabsPlatformMenuItem6toggleEv')

  def triggered(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuItem::triggered()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#triggered
    """
    #  void QQuickLabsPlatformMenuItem::triggered()
    self.uglySide.call('ritual_ZN26QQuickLabsPlatformMenuItem9triggeredEv')

  def hovered(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuItem::hovered()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#hovered
    """
    #  void QQuickLabsPlatformMenuItem::hovered()
    self.uglySide.call('ritual_ZN26QQuickLabsPlatformMenuItem7hoveredEv')

  def menuChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuItem::menuChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#menuChanged
    """
    #  void QQuickLabsPlatformMenuItem::menuChanged()
    self.uglySide.call(
        'ritual_ZN26QQuickLabsPlatformMenuItem11menuChangedEv',
    )

  def subMenuChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuItem::subMenuChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#subMenuChanged
    """
    #  void QQuickLabsPlatformMenuItem::subMenuChanged()
    self.uglySide.call(
        'ritual_ZN26QQuickLabsPlatformMenuItem14subMenuChangedEv',
    )

  def groupChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuItem::groupChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#groupChanged
    """
    #  void QQuickLabsPlatformMenuItem::groupChanged()
    self.uglySide.call(
        'ritual_ZN26QQuickLabsPlatformMenuItem12groupChangedEv',
    )

  def enabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuItem::enabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#enabledChanged
    """
    #  void QQuickLabsPlatformMenuItem::enabledChanged()
    self.uglySide.call(
        'ritual_ZN26QQuickLabsPlatformMenuItem14enabledChangedEv',
    )

  def visibleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuItem::visibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#visibleChanged
    """
    #  void QQuickLabsPlatformMenuItem::visibleChanged()
    self.uglySide.call(
        'ritual_ZN26QQuickLabsPlatformMenuItem14visibleChangedEv',
    )

  def separatorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuItem::separatorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#separatorChanged
    """
    #  void QQuickLabsPlatformMenuItem::separatorChanged()
    self.uglySide.call(
        'ritual_ZN26QQuickLabsPlatformMenuItem16separatorChangedEv',
    )

  def checkableChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuItem::checkableChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#checkableChanged
    """
    #  void QQuickLabsPlatformMenuItem::checkableChanged()
    self.uglySide.call(
        'ritual_ZN26QQuickLabsPlatformMenuItem16checkableChangedEv',
    )

  def checkedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuItem::checkedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#checkedChanged
    """
    #  void QQuickLabsPlatformMenuItem::checkedChanged()
    self.uglySide.call(
        'ritual_ZN26QQuickLabsPlatformMenuItem14checkedChangedEv',
    )

  def roleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuItem::roleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#roleChanged
    """
    #  void QQuickLabsPlatformMenuItem::roleChanged()
    self.uglySide.call(
        'ritual_ZN26QQuickLabsPlatformMenuItem11roleChangedEv',
    )

  def textChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuItem::textChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#textChanged
    """
    #  void QQuickLabsPlatformMenuItem::textChanged()
    self.uglySide.call(
        'ritual_ZN26QQuickLabsPlatformMenuItem11textChangedEv',
    )

  def shortcutChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuItem::shortcutChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#shortcutChanged
    """
    #  void QQuickLabsPlatformMenuItem::shortcutChanged()
    self.uglySide.call(
        'ritual_ZN26QQuickLabsPlatformMenuItem15shortcutChangedEv',
    )

  def fontChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuItem::fontChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#fontChanged
    """
    #  void QQuickLabsPlatformMenuItem::fontChanged()
    self.uglySide.call(
        'ritual_ZN26QQuickLabsPlatformMenuItem11fontChangedEv',
    )

  def iconChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuItem::iconChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#iconChanged
    """
    #  void QQuickLabsPlatformMenuItem::iconChanged()
    self.uglySide.call(
        'ritual_ZN26QQuickLabsPlatformMenuItem11iconChangedEv',
    )

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuItem::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#classBegin
    """
    #  void QQuickLabsPlatformMenuItem::classBegin()
    ritual = 'ritual_ZN26QQuickLabsPlatformMenuItem10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QQuickLabsPlatformMenuItem10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuItem::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#componentComplete
    """
    #  void QQuickLabsPlatformMenuItem::componentComplete()
    self.uglySide.call(
        'ritual_ZN26QQuickLabsPlatformMenuItem17componentCompleteEv',
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickLabsPlatformMenuItem::event(QEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickLabsPlatformMenuItem::event(QEvent *e)
    return self.uglySide.call(
        'ritual_ZN26QQuickLabsPlatformMenuItem5eventEP6QEvent',
        self._addressOf(e),
    )

  def activate(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuItem::activate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#activate
    """
    #  void QQuickLabsPlatformMenuItem::activate()
    self.uglySide.call('ritual_ZN26QQuickLabsPlatformMenuItem8activateEv')

  def updateIcon(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuItem::updateIcon()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#updateIcon
    """
    #  void QQuickLabsPlatformMenuItem::updateIcon()
    self.uglySide.call('ritual_ZN26QQuickLabsPlatformMenuItem10updateIconEv')

  def addShortcut(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuItem::addShortcut()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#addShortcut
    """
    #  void QQuickLabsPlatformMenuItem::addShortcut()
    self.uglySide.call(
        'ritual_ZN26QQuickLabsPlatformMenuItem11addShortcutEv',
    )

  def removeShortcut(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuItem::removeShortcut()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitem.html#removeShortcut
    """
    #  void QQuickLabsPlatformMenuItem::removeShortcut()
    self.uglySide.call(
        'ritual_ZN26QQuickLabsPlatformMenuItem14removeShortcutEv',
    )

  @staticmethod
  def create(*__, **_) -> Never:
    """
    Qt's 'QPlatformMenuItem *QQuickLabsPlatformMenuItem::create()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'QWidgetPlatform'.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuItem.create' has no cute function yet. Qt's "
        "'QPlatformMenuItem *QQuickLabsPlatformMenuItem::create()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'QWidgetPlatform'.")

  @staticmethod
  def iconLoader(*__, **_) -> Never:
    """
    Qt's 'QQuickLabsPlatformIconLoader
    *QQuickLabsPlatformMenuItem::iconLoader() const': leans on
    'QQuickLabsPlatformMenuItem::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuItem.iconLoader' has no cute function yet. "
        "Qt's 'QQuickLabsPlatformIconLoader "
        "*QQuickLabsPlatformMenuItem::iconLoader() const': leans on "
        "'QQuickLabsPlatformMenuItem::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setCheckable(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenuItem::setCheckable(bool checkable)':
    leans on 'QQuickLabsPlatformMenuItem::checkableChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuItem.setCheckable' has no cute function "
        "yet. Qt's 'void QQuickLabsPlatformMenuItem::setCheckable(bool "
        "checkable)': leans on "
        "'QQuickLabsPlatformMenuItem::checkableChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setChecked(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenuItem::setChecked(bool checked)': leans
    on 'QQuickLabsPlatformMenuItem::checkedChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuItem.setChecked' has no cute function yet. "
        "Qt's 'void QQuickLabsPlatformMenuItem::setChecked(bool checked)': "
        "leans on 'QQuickLabsPlatformMenuItem::checkedChanged()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setEnabled(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenuItem::setEnabled(bool enabled)': leans
    on 'QQuickLabsPlatformMenuItem::enabledChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuItem.setEnabled' has no cute function yet. "
        "Qt's 'void QQuickLabsPlatformMenuItem::setEnabled(bool enabled)': "
        "leans on 'QQuickLabsPlatformMenuItem::enabledChanged()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setFont(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenuItem::setFont(const QFont &font)': leans
    on 'QQuickLabsPlatformMenuItem::fontChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuItem.setFont' has no cute function yet. "
        "Qt's 'void QQuickLabsPlatformMenuItem::setFont(const QFont "
        "&font)': leans on 'QQuickLabsPlatformMenuItem::fontChanged()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setGroup(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickLabsPlatformMenuItem::setGroup(QQuickLabsPlatformMenuItemGroup
    *group)': leans on 'QQuickLabsPlatformMenuItem::groupChanged()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuItem.setGroup' has no cute function yet. "
        "Qt's 'void "
        "QQuickLabsPlatformMenuItem::setGroup(QQuickLabsPlatformMenuItemGrou"
        "p *group)': leans on 'QQuickLabsPlatformMenuItem::groupChanged()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setIcon(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenuItem::setIcon(const
    QQuickLabsPlatformIcon &icon)': leans on
    'QQuickLabsPlatformMenuItem::iconChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuItem.setIcon' has no cute function yet. "
        "Qt's 'void QQuickLabsPlatformMenuItem::setIcon(const "
        "QQuickLabsPlatformIcon &icon)': leans on "
        "'QQuickLabsPlatformMenuItem::iconChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setMenu(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenuItem::setMenu(QQuickLabsPlatformMenu
    *menu)': leans on 'QQuickLabsPlatformMenuItem::menuChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuItem.setMenu' has no cute function yet. "
        "Qt's 'void "
        "QQuickLabsPlatformMenuItem::setMenu(QQuickLabsPlatformMenu "
        "*menu)': leans on 'QQuickLabsPlatformMenuItem::menuChanged()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setRole(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickLabsPlatformMenuItem::setRole(QPlatformMenuItem::MenuRole role)':
    leans on 'QQuickLabsPlatformMenuItem::roleChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuItem.setRole' has no cute function yet. "
        "Qt's 'void "
        "QQuickLabsPlatformMenuItem::setRole(QPlatformMenuItem::MenuRole "
        "role)': leans on 'QQuickLabsPlatformMenuItem::roleChanged()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setSeparator(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenuItem::setSeparator(bool separator)':
    leans on 'QQuickLabsPlatformMenuItem::separatorChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuItem.setSeparator' has no cute function "
        "yet. Qt's 'void QQuickLabsPlatformMenuItem::setSeparator(bool "
        "separator)': leans on "
        "'QQuickLabsPlatformMenuItem::separatorChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setShortcut(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenuItem::setShortcut(const QVariant
    &shortcut)': leans on 'QQuickLabsPlatformMenuItem::shortcutChanged()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuItem.setShortcut' has no cute function yet. "
        "Qt's 'void QQuickLabsPlatformMenuItem::setShortcut(const QVariant "
        "&shortcut)': leans on "
        "'QQuickLabsPlatformMenuItem::shortcutChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setSubMenu(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenuItem::setSubMenu(QQuickLabsPlatformMenu
    *menu)': leans on 'QQuickLabsPlatformMenuItem::subMenuChanged()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuItem.setSubMenu' has no cute function yet. "
        "Qt's 'void "
        "QQuickLabsPlatformMenuItem::setSubMenu(QQuickLabsPlatformMenu "
        "*menu)': leans on 'QQuickLabsPlatformMenuItem::subMenuChanged()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setText(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenuItem::setText(const QString &text)':
    leans on 'QQuickLabsPlatformMenuItem::textChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuItem.setText' has no cute function yet. "
        "Qt's 'void QQuickLabsPlatformMenuItem::setText(const QString "
        "&text)': leans on 'QQuickLabsPlatformMenuItem::textChanged()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setVisible(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenuItem::setVisible(bool visible)': leans
    on 'QQuickLabsPlatformMenuItem::visibleChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuItem.setVisible' has no cute function yet. "
        "Qt's 'void QQuickLabsPlatformMenuItem::setVisible(bool visible)': "
        "leans on 'QQuickLabsPlatformMenuItem::visibleChanged()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def sync(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenuItem::sync()': leans on
    'QQuickLabsPlatformMenuItem::create()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuItem.sync' has no cute function yet. Qt's "
        "'void QQuickLabsPlatformMenuItem::sync()': leans on "
        "'QQuickLabsPlatformMenuItem::create()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
