"""
QDBusMenuBar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qdbusmenubar_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QDBusMenuBar to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QPlatformMenuBar

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QPlatformMenu, QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPlatformMenu = WAIT['QPlatformMenu']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDBusMenuBar(QPlatformMenuBar):
  """
  The cute side of Qt's QDBusMenuBar: a plain Python object standing in front
  of one C++ QDBusMenuBar.

  It is built on the cute 'QPlatformMenuBar', as Qt's QDBusMenuBar is built
  on Qt's QPlatformMenuBar, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDBusMenuBar that has a ritual and that Python can
  call so far, 7 names in all: 'metaObject', 'insertMenu', 'removeMenu',
  'syncMenu', 'handleReparent', 'menuForTag', 'createMenu'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDBusMenuBar::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QDBusMenuBar::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QDBusMenuBar::~QDBusMenuBar()': the destructor: Python never
    removes a C++ QDBusMenuBar.

  What has no ritual
  ------------------

  8 of the 18 functions Qt declares: 2 not a gap; 2 leans on 'QDBusMenuBar; 2
  leans on 'QDBusPlatformMenu; 1 Qt's library has no name for it, and its
  code in Qt's source does not compile apart from its file; 1 leans on
  'vtable for QDBusMenuRegistrarInterface', which Qt's source does not mark
  for use from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QDBusMenuBar is created at the first use, not by
    'QDBusMenuBar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDBusMenuBar.
  - Qt tells when it has removed the C++ QDBusMenuBar. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QDBusMenuBar that has no cute function yet, '__init__',
    'menuItemForMenu', 'registerMenuBar', 'unregisterMenuBar',
    'updateMenuItem', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusMenuBar'

  #  A C++ QDBusMenuBar Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDBusMenuBar'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDBusMenuBar::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmenubar.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDBusMenuBar::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QDBusMenuBar10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(int)
  def menuForTag(self, tag: int) -> Optional[QPlatformMenu]:
    """
    Calls Qt's 'QPlatformMenu *QDBusMenuBar::menuForTag(quintptr tag) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmenubar.html#menuForTag

    Parameters
    ----------

    tag : int
      Passed on as it is.

    Returns
    -------

    Optional[QPlatformMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMenu *QDBusMenuBar::menuForTag(quintptr tag) const
    ritual = 'ritual_ZNK12QDBusMenuBar10menuForTagEy'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QDBusMenuBar10menuForTagEy'
    address = self.uglySide.call(ritual, tag)
    from . import QPlatformMenu
    return QPlatformMenu._cuteAt(address)

  def createMenu(self) -> Optional[QPlatformMenu]:
    """
    Calls Qt's 'QPlatformMenu *QDBusMenuBar::createMenu() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmenubar.html#createMenu

    Returns
    -------

    Optional[QPlatformMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMenu *QDBusMenuBar::createMenu() const
    address = self.uglySide.call('ritual_ZNK12QDBusMenuBar10createMenuEv')
    from . import QPlatformMenu
    return QPlatformMenu._cuteAt(address)

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
    Qt's 'QDBusMenuBar::QDBusMenuBar()': leans on
    'QDBusMenuBar::qt_metacall(QMetaObject::Call, int, void**)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QDBusMenuBar.__init__' has no cute function yet. Qt's "
        "'QDBusMenuBar::QDBusMenuBar()': leans on "
        "'QDBusMenuBar::qt_metacall(QMetaObject::Call, int, void**)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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

  @overload(QPlatformMenu, QPlatformMenu)
  @overload(QPlatformMenu, NoneType)
  @overload(NoneType, QPlatformMenu)
  @overload(NoneType, NoneType)
  def insertMenu(
      self,
      menu: Optional[QPlatformMenu],
      before: Optional[QPlatformMenu],
  ) -> None:
    """
    Calls Qt's 'void QDBusMenuBar::insertMenu(QPlatformMenu *menu,
    QPlatformMenu *before)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmenubar.html#insertMenu

    Parameters
    ----------

    menu : Optional[QPlatformMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    before : Optional[QPlatformMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDBusMenuBar::insertMenu(QPlatformMenu *menu, QPlatformMenu
    #      *before)
    self.uglySide.call(
        'ritual_ZN12QDBusMenuBar10insertMenuEP13QPlatformMenuS1_',
        self._addressOf(menu), self._addressOf(before),
    )

  @overload(QPlatformMenu)
  @overload(NoneType)
  def removeMenu(self, menu: Optional[QPlatformMenu]) -> None:
    """
    Calls Qt's 'void QDBusMenuBar::removeMenu(QPlatformMenu *menu)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmenubar.html#removeMenu

    Parameters
    ----------

    menu : Optional[QPlatformMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDBusMenuBar::removeMenu(QPlatformMenu *menu)
    self.uglySide.call(
        'ritual_ZN12QDBusMenuBar10removeMenuEP13QPlatformMenu',
        self._addressOf(menu),
    )

  @overload(QPlatformMenu)
  @overload(NoneType)
  def syncMenu(self, menu: Optional[QPlatformMenu]) -> None:
    """
    Calls Qt's 'void QDBusMenuBar::syncMenu(QPlatformMenu *menu)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmenubar.html#syncMenu

    Parameters
    ----------

    menu : Optional[QPlatformMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDBusMenuBar::syncMenu(QPlatformMenu *menu)
    self.uglySide.call(
        'ritual_ZN12QDBusMenuBar8syncMenuEP13QPlatformMenu',
        self._addressOf(menu),
    )

  @overload(QWindow)
  @overload(NoneType)
  def handleReparent(self, newParentWindow: Optional[QWindow]) -> None:
    """
    Calls Qt's 'void QDBusMenuBar::handleReparent(QWindow *newParentWindow)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmenubar.html#handleReparent

    Parameters
    ----------

    newParentWindow : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDBusMenuBar::handleReparent(QWindow *newParentWindow)
    self.uglySide.call(
        'ritual_ZN12QDBusMenuBar14handleReparentEP7QWindow',
        self._addressOf(newParentWindow),
    )

  @staticmethod
  def menuItemForMenu(*__, **_) -> Never:
    """
    Qt's 'QDBusPlatformMenuItem *QDBusMenuBar::menuItemForMenu(QPlatformMenu
    *menu)': leans on 'QDBusPlatformMenu::staticMetaObject', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QDBusMenuBar.menuItemForMenu' has no cute function yet. Qt's "
        "'QDBusPlatformMenuItem "
        "*QDBusMenuBar::menuItemForMenu(QPlatformMenu *menu)': leans on "
        "'QDBusPlatformMenu::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def registerMenuBar(*__, **_) -> Never:
    """
    Qt's 'void QDBusMenuBar::registerMenuBar()': leans on 'vtable for
    QDBusMenuRegistrarInterface', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusMenuBar.registerMenuBar' has no cute function yet. Qt's "
        "'void QDBusMenuBar::registerMenuBar()': leans on 'vtable for "
        "QDBusMenuRegistrarInterface', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def unregisterMenuBar(*__, **_) -> Never:
    """
    Qt's 'void QDBusMenuBar::unregisterMenuBar()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'REGISTRAR_SERVICE'.
    """
    raise NotImplementedError(
        "'QDBusMenuBar.unregisterMenuBar' has no cute function yet. Qt's "
        "'void QDBusMenuBar::unregisterMenuBar()': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'REGISTRAR_SERVICE'.")

  @staticmethod
  def updateMenuItem(*__, **_) -> Never:
    """
    Qt's 'void QDBusMenuBar::updateMenuItem(QDBusPlatformMenuItem *item,
    QPlatformMenu *menu)': leans on 'QDBusPlatformMenu::staticMetaObject',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusMenuBar.updateMenuItem' has no cute function yet. Qt's 'void "
        "QDBusMenuBar::updateMenuItem(QDBusPlatformMenuItem *item, "
        "QPlatformMenu *menu)': leans on "
        "'QDBusPlatformMenu::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
