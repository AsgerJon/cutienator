"""
QQuickMenuItemPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmenuitem_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickMenuItemPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QQuickAbstractButtonPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QPalette
  from . import QQuickMenu, QQuickMenuItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickMenu = WAIT['QQuickMenu']
  QQuickMenuItem = WAIT['QQuickMenuItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickMenuItemPrivate(QQuickAbstractButtonPrivate):
  """
  The cute side of Qt's QQuickMenuItemPrivate: a plain Python object standing
  in front of one C++ QQuickMenuItemPrivate.

  It is built on the cute 'QQuickAbstractButtonPrivate', as Qt's
  QQuickMenuItemPrivate is built on Qt's QQuickAbstractButtonPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickMenuItemPrivate that has a ritual and that
  Python can call so far, 8 names in all: 'q_func', 'get', 'setMenu',
  'setSubMenu', 'updateEnabled', 'cancelArrow', 'acceptKeyClick',
  'defaultPalette'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickMenuItem *QQuickMenuItemPrivate::q_func() const': takes
    in Python what 'QQuickMenuItem *QQuickMenuItemPrivate::q_func()' takes.

  What has no ritual
  ------------------

  1 of the 10 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQuickMenuItemPrivate is created at the first use, not by
    'QQuickMenuItemPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickMenuItemPrivate.
  - Each name of Qt's QQuickMenuItemPrivate that has no cute function yet,
    'executeArrow', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickMenuItem)
  @overload(NoneType)
  def get(item: Optional[QQuickMenuItem]) -> Optional[QQuickMenuItemPrivate]:
    """
    Calls Qt's 'QQuickMenuItemPrivate
    *QQuickMenuItemPrivate::get(QQuickMenuItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuitemprivate.html#get

    Parameters
    ----------

    item : Optional[QQuickMenuItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickMenuItemPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMenuItemPrivate *QQuickMenuItemPrivate::get(QQuickMenuItem
    #      *item)
    address = Rituals.call(
        'ritual_ZN21QQuickMenuItemPrivate3getEP14QQuickMenuItem',
        CuteMixin._addressOf(item),
    )
    return QQuickMenuItemPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickMenuItemPrivate'

  #  A C++ QQuickMenuItemPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickMenuItemPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.Key)
  def acceptKeyClick(self, key: Qt.Key) -> bool:
    """
    Calls Qt's 'bool QQuickMenuItemPrivate::acceptKeyClick(Qt::Key key)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuitemprivate.html#acceptKeyClick

    Parameters
    ----------

    key : Qt.Key
      Passed on as its number.
    """
    #  bool QQuickMenuItemPrivate::acceptKeyClick(Qt::Key key) const
    ritual = 'ritual_ZNK21QQuickMenuItemPrivate14acceptKeyClickEN2Qt3KeyE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QQuickMenuItemPrivate14acceptKeyClickEN2Qt3KeyE')
    return self.uglySide.call(ritual, key.value)

  def defaultPalette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QQuickMenuItemPrivate::defaultPalette() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuitemprivate.html#defaultPalette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QQuickMenuItemPrivate::defaultPalette() const
    ritual = 'ritual_ZNK21QQuickMenuItemPrivate14defaultPaletteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QQuickMenuItemPrivate14defaultPaletteEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickMenu)
  @overload(NoneType)
  def setMenu(self, menu: Optional[QQuickMenu]) -> None:
    """
    Calls Qt's 'void QQuickMenuItemPrivate::setMenu(QQuickMenu *menu)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuitemprivate.html#setMenu

    Parameters
    ----------

    menu : Optional[QQuickMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuItemPrivate::setMenu(QQuickMenu *menu)
    self.uglySide.call(
        'ritual_ZN21QQuickMenuItemPrivate7setMenuEP10QQuickMenu',
        self._addressOf(menu),
    )

  @overload(QQuickMenu)
  @overload(NoneType)
  def setSubMenu(self, subMenu: Optional[QQuickMenu]) -> None:
    """
    Calls Qt's 'void QQuickMenuItemPrivate::setSubMenu(QQuickMenu *subMenu)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuitemprivate.html#setSubMenu

    Parameters
    ----------

    subMenu : Optional[QQuickMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuItemPrivate::setSubMenu(QQuickMenu *subMenu)
    self.uglySide.call(
        'ritual_ZN21QQuickMenuItemPrivate10setSubMenuEP10QQuickMenu',
        self._addressOf(subMenu),
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

  def q_func(self) -> Optional[QQuickMenuItem]:
    """
    Calls Qt's 'QQuickMenuItem *QQuickMenuItemPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuitemprivate.html#q_func

    Returns
    -------

    Optional[QQuickMenuItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMenuItem *QQuickMenuItemPrivate::q_func()
    address = self.uglySide.call('ritual_ZN21QQuickMenuItemPrivate6q_funcEv')
    from . import QQuickMenuItem
    return QQuickMenuItem._cuteAt(address)

  def updateEnabled(self) -> None:
    """
    Calls Qt's 'void QQuickMenuItemPrivate::updateEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuitemprivate.html#updateEnabled
    """
    #  void QQuickMenuItemPrivate::updateEnabled()
    self.uglySide.call('ritual_ZN21QQuickMenuItemPrivate13updateEnabledEv')

  def cancelArrow(self) -> None:
    """
    Calls Qt's 'void QQuickMenuItemPrivate::cancelArrow()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuitemprivate.html#cancelArrow
    """
    #  void QQuickMenuItemPrivate::cancelArrow()
    self.uglySide.call('ritual_ZN21QQuickMenuItemPrivate11cancelArrowEv')

  @staticmethod
  def executeArrow(*__, **_) -> Never:
    """
    Qt's 'void QQuickMenuItemPrivate::executeArrow(bool complete)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'arrowName'.
    """
    raise NotImplementedError(
        "'QQuickMenuItemPrivate.executeArrow' has no cute function yet. "
        "Qt's 'void QQuickMenuItemPrivate::executeArrow(bool complete)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'arrowName'.")
