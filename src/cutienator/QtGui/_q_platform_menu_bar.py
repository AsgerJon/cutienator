"""
QPlatformMenuBar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformmenu.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

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


class QPlatformMenuBar(QObject):
  """
  The cute side of Qt's QPlatformMenuBar: a plain Python object standing in
  front of one C++ QPlatformMenuBar.

  It is built on the cute 'QObject', as Qt's QPlatformMenuBar is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformMenuBar that has a ritual and that Python
  can call so far, 9 names in all: 'metaObject', 'tr', 'insertMenu',
  'removeMenu', 'syncMenu', 'handleReparent', 'parentWindow', 'menuForTag',
  'createMenu'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlatformMenuBar::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QPlatformMenuBar::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPlatformMenuBar is created at the first use, not by
    'QPlatformMenuBar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformMenuBar.
  - Qt tells when it has removed the C++ QPlatformMenuBar. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QPlatformMenuBar::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenubar.html#tr

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
    #  QString QPlatformMenuBar::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QPlatformMenuBar2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformMenuBar'

  #  A C++ QPlatformMenuBar Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformMenuBar'

  #  The functions Qt calls itself that QPlatformMenuBar is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'insertMenu': (
          ('_ZN16QPlatformMenuBar10insertMenuEP13QPlatformMenuS1_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPlatformMenu'),
               ('address', 'address', 'QtGui:QPlatformMenu'),
           )),
      ),
      'removeMenu': (
          ('_ZN16QPlatformMenuBar10removeMenuEP13QPlatformMenu',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPlatformMenu'),
           )),
      ),
      'syncMenu': (
          ('_ZN16QPlatformMenuBar8syncMenuEP13QPlatformMenu',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPlatformMenu'),
           )),
      ),
      'handleReparent': (
          ('_ZN16QPlatformMenuBar14handleReparentEP7QWindow',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QWindow'),
           )),
      ),
      'parentWindow': (
          ('_ZNK16QPlatformMenuBar12parentWindowEv',
           ('address', 'address', 'QtGui:QWindow'),
           ()),
      ),
      'menuForTag': (
          ('_ZNK16QPlatformMenuBar10menuForTagEy',
           ('address', 'address', 'QtGui:QPlatformMenu'),
           (
               ('unsigned long long', 'number', ''),
           )),
      ),
      'createMenu': (
          ('_ZNK16QPlatformMenuBar10createMenuEv',
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
    Calls Qt's 'const QMetaObject *QPlatformMenuBar::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenubar.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlatformMenuBar::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QPlatformMenuBar10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def parentWindow(self) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QPlatformMenuBar::parentWindow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenubar.html#parentWindow

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QPlatformMenuBar::parentWindow() const
    ritual = 'ritual_ZNK16QPlatformMenuBar12parentWindowEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QPlatformMenuBar12parentWindowEv'
    address = self.uglySide.call(ritual)
    from . import QWindow
    return QWindow._cuteAt(address)

  @overload(int)
  def menuForTag(self, tag: int) -> Optional[QPlatformMenu]:
    """
    Calls Qt's 'QPlatformMenu *QPlatformMenuBar::menuForTag(quintptr tag)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenubar.html#menuForTag

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
    #  QPlatformMenu *QPlatformMenuBar::menuForTag(quintptr tag) const
    address = self.uglySide.call(
        'ritual_ZNK16QPlatformMenuBar10menuForTagEy', tag,
    )
    from . import QPlatformMenu
    return QPlatformMenu._cuteAt(address)

  def createMenu(self) -> Optional[QPlatformMenu]:
    """
    Calls Qt's 'QPlatformMenu *QPlatformMenuBar::createMenu() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenubar.html#createMenu

    Returns
    -------

    Optional[QPlatformMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMenu *QPlatformMenuBar::createMenu() const
    ritual = 'ritual_ZNK16QPlatformMenuBar10createMenuEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QPlatformMenuBar10createMenuEv'
    address = self.uglySide.call(ritual)
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
    Calls Qt's 'void QPlatformMenuBar::insertMenu(QPlatformMenu *menu,
    QPlatformMenu *before)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenubar.html#insertMenu

    Parameters
    ----------

    menu : Optional[QPlatformMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    before : Optional[QPlatformMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformMenuBar::insertMenu(QPlatformMenu *menu, QPlatformMenu
    #      *before)
    self.uglySide.call(
        'ritual_ZN16QPlatformMenuBar10insertMenuEP13QPlatformMenuS1_',
        self._addressOf(menu), self._addressOf(before),
    )

  @overload(QPlatformMenu)
  @overload(NoneType)
  def removeMenu(self, menu: Optional[QPlatformMenu]) -> None:
    """
    Calls Qt's 'void QPlatformMenuBar::removeMenu(QPlatformMenu *menu)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenubar.html#removeMenu

    Parameters
    ----------

    menu : Optional[QPlatformMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformMenuBar::removeMenu(QPlatformMenu *menu)
    self.uglySide.call(
        'ritual_ZN16QPlatformMenuBar10removeMenuEP13QPlatformMenu',
        self._addressOf(menu),
    )

  @overload(QPlatformMenu)
  @overload(NoneType)
  def syncMenu(self, menuItem: Optional[QPlatformMenu]) -> None:
    """
    Calls Qt's 'void QPlatformMenuBar::syncMenu(QPlatformMenu *menuItem)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformmenubar.html#syncMenu

    Parameters
    ----------

    menuItem : Optional[QPlatformMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformMenuBar::syncMenu(QPlatformMenu *menuItem)
    self.uglySide.call(
        'ritual_ZN16QPlatformMenuBar8syncMenuEP13QPlatformMenu',
        self._addressOf(menuItem),
    )

  @overload(QWindow)
  @overload(NoneType)
  def handleReparent(self, newParentWindow: Optional[QWindow]) -> None:
    """
    Calls Qt's 'void QPlatformMenuBar::handleReparent(QWindow
    *newParentWindow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmenubar.html#handleReparent

    Parameters
    ----------

    newParentWindow : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformMenuBar::handleReparent(QWindow *newParentWindow)
    self.uglySide.call(
        'ritual_ZN16QPlatformMenuBar14handleReparentEP7QWindow',
        self._addressOf(newParentWindow),
    )
