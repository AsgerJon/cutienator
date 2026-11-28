"""
QQuickNativeMenuItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicknativemenuitem_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickNativeMenuItem to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QPlatformMenuItem
  from ..QtQuick import QQuickItem
  from . import QQuickAction, QQuickIcon, QQuickMenu, QQuickMenuSeparator
  from . import QQuickNativeIconLoader
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickItem = WAIT['QQuickItem']
  QQuickMenu = WAIT['QQuickMenu']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickNativeMenuItem(QObject):
  """
  The cute side of Qt's QQuickNativeMenuItem: a plain Python object standing
  in front of one C++ QQuickNativeMenuItem.

  It is built on the cute 'QObject', as Qt's QQuickNativeMenuItem is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickNativeMenuItem that has a ritual and that
  Python can call so far, 15 names in all: 'metaObject', 'tr',
  'createFromNonNativeItem', 'action', 'subMenu', 'separator', 'handle',
  'sync', 'effectiveIcon', 'iconLoader', 'reloadIcon', 'debugText',
  'updateIcon', 'addShortcut', 'removeShortcut'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickNativeMenuItem::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickNativeMenuItem::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickNativeMenuItem::~QQuickNativeMenuItem()': the destructor:
    Python never removes a C++ QQuickNativeMenuItem.
  - Qt's 'QQuickNativeMenuItem::QQuickNativeMenuItem(QQuickMenu *parentMenu,
    QQuickItem *nonNativeItem, Type type)': names the enum
    'QQuickNativeMenuItem::Type', whose class cannot be named here.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickNativeMenuItem is created at the first use, not by
    'QQuickNativeMenuItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickNativeMenuItem.
  - Qt tells when it has removed the C++ QQuickNativeMenuItem. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickNativeMenuItem that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

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
    Calls Qt's 'QString QQuickNativeMenuItem::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicknativemenuitem.html#tr

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
    #  QString QQuickNativeMenuItem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuickNativeMenuItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QQuickMenu, QQuickItem)
  @overload(QQuickMenu, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def createFromNonNativeItem(
      parentMenu: Optional[QQuickMenu],
      nonNativeItem: Optional[QQuickItem],
  ) -> Optional[QQuickNativeMenuItem]:
    """
    Calls Qt's 'QQuickNativeMenuItem
    *QQuickNativeMenuItem::createFromNonNativeItem(QQuickMenu *parentMenu,
    QQuickItem *nonNativeItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicknativemenuitem.html#createFromNonNativeItem

    Parameters
    ----------

    parentMenu : Optional[QQuickMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    nonNativeItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickNativeMenuItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickNativeMenuItem
    #      *QQuickNativeMenuItem::createFromNonNativeItem(QQuickMenu
    #      *parentMenu, QQuickItem *nonNativeItem)
    address = Rituals.call(
        'ritual_ZN20QQuickNativeMenuItem23createFromNonNativeItemEP10QQuick'
        'MenuP10QQuickItem',
        CuteMixin._addressOf(parentMenu),
        CuteMixin._addressOf(nonNativeItem),
    )
    return QQuickNativeMenuItem._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickNativeMenuItem'

  #  A C++ QQuickNativeMenuItem Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickNativeMenuItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickNativeMenuItem::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicknativemenuitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickNativeMenuItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickNativeMenuItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def action(self) -> Optional[QQuickAction]:
    """
    Calls Qt's 'QQuickAction *QQuickNativeMenuItem::action() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicknativemenuitem.html#action

    Returns
    -------

    Optional[QQuickAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAction *QQuickNativeMenuItem::action() const
    address = self.uglySide.call('ritual_ZNK20QQuickNativeMenuItem6actionEv')
    from . import QQuickAction
    return QQuickAction._cuteAt(address)

  def subMenu(self) -> Optional[QQuickMenu]:
    """
    Calls Qt's 'QQuickMenu *QQuickNativeMenuItem::subMenu() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicknativemenuitem.html#subMenu

    Returns
    -------

    Optional[QQuickMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMenu *QQuickNativeMenuItem::subMenu() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickNativeMenuItem7subMenuEv',
    )
    from . import QQuickMenu
    return QQuickMenu._cuteAt(address)

  def separator(self) -> Optional[QQuickMenuSeparator]:
    """
    Calls Qt's 'QQuickMenuSeparator *QQuickNativeMenuItem::separator()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicknativemenuitem.html#separator

    Returns
    -------

    Optional[QQuickMenuSeparator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMenuSeparator *QQuickNativeMenuItem::separator() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickNativeMenuItem9separatorEv',
    )
    from . import QQuickMenuSeparator
    return QQuickMenuSeparator._cuteAt(address)

  def handle(self) -> Optional[QPlatformMenuItem]:
    """
    Calls Qt's 'QPlatformMenuItem *QQuickNativeMenuItem::handle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicknativemenuitem.html#handle

    Returns
    -------

    Optional[QPlatformMenuItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMenuItem *QQuickNativeMenuItem::handle() const
    address = self.uglySide.call('ritual_ZNK20QQuickNativeMenuItem6handleEv')
    from ..QtGui import QPlatformMenuItem
    return QPlatformMenuItem._cuteAt(address)

  def effectiveIcon(self) -> QQuickIcon:
    """
    Calls Qt's 'QQuickIcon QQuickNativeMenuItem::effectiveIcon() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicknativemenuitem.html#effectiveIcon

    Returns
    -------

    QQuickIcon
      A new cute QQuickIcon around the copy Qt gave back. Python owns it.
    """
    #  QQuickIcon QQuickNativeMenuItem::effectiveIcon() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickNativeMenuItem13effectiveIconEv',
    )
    from . import QQuickIcon
    return QQuickIcon._cuteOwning(address)

  def iconLoader(self) -> Optional[QQuickNativeIconLoader]:
    """
    Calls Qt's 'QQuickNativeIconLoader *QQuickNativeMenuItem::iconLoader()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicknativemenuitem.html#iconLoader

    Returns
    -------

    Optional[QQuickNativeIconLoader]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickNativeIconLoader *QQuickNativeMenuItem::iconLoader() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickNativeMenuItem10iconLoaderEv',
    )
    from . import QQuickNativeIconLoader
    return QQuickNativeIconLoader._cuteAt(address)

  def debugText(self) -> str:
    """
    Calls Qt's 'QString QQuickNativeMenuItem::debugText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicknativemenuitem.html#debugText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickNativeMenuItem::debugText() const
    return self.uglySide.call('ritual_ZNK20QQuickNativeMenuItem9debugTextEv')

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
    Qt's 'QQuickNativeMenuItem::QQuickNativeMenuItem(QQuickMenu *parentMenu,
    QQuickItem *nonNativeItem, Type type)': names the enum
    'QQuickNativeMenuItem::Type', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QQuickNativeMenuItem.__init__' has no cute function yet. Qt's "
        "'QQuickNativeMenuItem::QQuickNativeMenuItem(QQuickMenu "
        "*parentMenu, QQuickItem *nonNativeItem, Type type)': names the "
        "enum 'QQuickNativeMenuItem::Type', whose class cannot be named "
        "here.")

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

  def sync(self) -> None:
    """
    Calls Qt's 'void QQuickNativeMenuItem::sync()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicknativemenuitem.html#sync
    """
    #  void QQuickNativeMenuItem::sync()
    self.uglySide.call('ritual_ZN20QQuickNativeMenuItem4syncEv')

  def reloadIcon(self) -> None:
    """
    Calls Qt's 'void QQuickNativeMenuItem::reloadIcon()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicknativemenuitem.html#reloadIcon
    """
    #  void QQuickNativeMenuItem::reloadIcon()
    self.uglySide.call('ritual_ZN20QQuickNativeMenuItem10reloadIconEv')

  def updateIcon(self) -> None:
    """
    Calls Qt's 'void QQuickNativeMenuItem::updateIcon()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicknativemenuitem.html#updateIcon
    """
    #  void QQuickNativeMenuItem::updateIcon()
    self.uglySide.call('ritual_ZN20QQuickNativeMenuItem10updateIconEv')

  def addShortcut(self) -> None:
    """
    Calls Qt's 'void QQuickNativeMenuItem::addShortcut()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicknativemenuitem.html#addShortcut
    """
    #  void QQuickNativeMenuItem::addShortcut()
    self.uglySide.call('ritual_ZN20QQuickNativeMenuItem11addShortcutEv')

  def removeShortcut(self) -> None:
    """
    Calls Qt's 'void QQuickNativeMenuItem::removeShortcut()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicknativemenuitem.html#removeShortcut
    """
    #  void QQuickNativeMenuItem::removeShortcut()
    self.uglySide.call('ritual_ZN20QQuickNativeMenuItem14removeShortcutEv')
