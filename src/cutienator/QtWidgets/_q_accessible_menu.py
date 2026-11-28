"""
QAccessibleMenu binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qaccessiblemenu_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAccessibleMenu to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtGui import QAccessible, QAccessibleInterface
from . import QAccessibleWidgetV2

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QMenu

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleMenu(QAccessibleWidgetV2):
  """
  The cute side of Qt's QAccessibleMenu: a plain Python object standing in
  front of one C++ QAccessibleMenu.

  It is built on the cute 'QAccessibleWidgetV2', as Qt's QAccessibleMenu is
  built on Qt's QAccessibleWidgetV2, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleMenu that has a ritual and that Python
  can call so far, 8 names in all: 'childCount', 'childAt', 'text', 'role',
  'child', 'parent', 'indexOfChild', 'menu'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  1 of the 9 functions Qt declares: 1 leans on 'QAccessibleMenu.

  What to expect
  --------------

  - The C++ QAccessibleMenu is created at the first use, not by
    'QAccessibleMenu(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleMenu.
  - Each name of Qt's QAccessibleMenu that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleMenu'

  #  A C++ QAccessibleMenu Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleMenu'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def childCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleMenu::childCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemenu.html#childCount
    """
    #  int QAccessibleMenu::childCount() const
    ritual = 'ritual_ZNK15QAccessibleMenu10childCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QAccessibleMenu10childCountEv'
    return self.uglySide.call(ritual)

  @overload(int, int)
  def childAt(self, x: int, y: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleMenu::childAt(int x, int y)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemenu.html#childAt

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleMenu::childAt(int x, int y) const
    address = self.uglySide.call(
        'ritual_ZNK15QAccessibleMenu7childAtEii', x, y,
    )
    return QAccessibleInterface._cuteAt(address)

  @overload(QAccessible.Text)
  def text(self, t: QAccessible.Text) -> str:
    """
    Calls Qt's 'QString QAccessibleMenu::text(QAccessible::Text t) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemenu.html#text

    Parameters
    ----------

    t : QAccessible.Text
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleMenu::text(QAccessible::Text t) const
    ritual = 'ritual_ZNK15QAccessibleMenu4textEN11QAccessible4TextE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QAccessibleMenu4textEN11QAccessible4TextE'
    return self.uglySide.call(ritual, t.value)

  def role(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QAccessibleMenu::role() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemenu.html#role

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QAccessibleMenu::role() const
    ritual = 'ritual_ZNK15QAccessibleMenu4roleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QAccessibleMenu4roleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  @overload(int)
  def child(self, index: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleMenu::child(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemenu.html#child

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleMenu::child(int index) const
    address = self.uglySide.call(
        'ritual_ZNK15QAccessibleMenu5childEi', index,
    )
    return QAccessibleInterface._cuteAt(address)

  def parent(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleMenu::parent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemenu.html#parent

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleMenu::parent() const
    address = self.uglySide.call('ritual_ZNK15QAccessibleMenu6parentEv')
    return QAccessibleInterface._cuteAt(address)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def indexOfChild(self, child: Optional[QAccessibleInterface]) -> int:
    """
    Calls Qt's 'int QAccessibleMenu::indexOfChild(const QAccessibleInterface
    *child) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemenu.html#indexOfChild

    Parameters
    ----------

    child : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QAccessibleMenu::indexOfChild(const QAccessibleInterface *child)
    #      const
    ritual = (
        'ritual_ZNK15QAccessibleMenu12indexOfChildEPK20QAccessibleInterface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK15QAccessibleMenu12indexOfChildEPK20QAccessibleInt'
          'erface')
    return self.uglySide.call(
        ritual, self._addressOf(child, 'QAccessibleInterface'),
    )

  def menu(self) -> Optional[QMenu]:
    """
    Calls Qt's 'QMenu *QAccessibleMenu::menu() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemenu.html#menu

    Returns
    -------

    Optional[QMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenu *QAccessibleMenu::menu() const
    address = self.uglySide.call('ritual_ZNK15QAccessibleMenu4menuEv')
    from . import QMenu
    return QMenu._cuteAt(address)

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
    Qt's 'QAccessibleMenu::QAccessibleMenu(QWidget *w)': leans on
    'QAccessibleMenu::parent() const', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QAccessibleMenu.__init__' has no cute function yet. Qt's "
        "'QAccessibleMenu::QAccessibleMenu(QWidget *w)': leans on "
        "'QAccessibleMenu::parent() const', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

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
