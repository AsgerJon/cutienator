"""
QAccessibleTabBar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/complexwidgets_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAccessibleTabBar to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtCore import QList
from ..QtGui import QAccessible, QAccessibleInterface
from ..QtGui import QAccessibleSelectionInterface
from . import QAccessibleWidgetV2

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QTabBar

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleTabBar(QAccessibleWidgetV2, QAccessibleSelectionInterface):
  """
  The cute side of Qt's QAccessibleTabBar: a plain Python object standing in
  front of one C++ QAccessibleTabBar.

  It is built on the cute 'QAccessibleWidgetV2', as Qt's QAccessibleTabBar is
  built on Qt's QAccessibleWidgetV2, and has everything that class has. It is
  built on the cute 'QAccessibleSelectionInterface' as well, as Qt's
  QAccessibleTabBar is built on Qt's QAccessibleSelectionInterface too, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleTabBar that has a ritual and that Python
  can call so far, 14 names in all: 'focusChild', 'childCount', 'text',
  'child', 'indexOfChild', 'selectedItemCount', 'selectedItems',
  'selectedItem', 'isSelected', 'select', 'unselect', 'selectAll', 'clear',
  'tabBar'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAccessibleTabBar::~QAccessibleTabBar()': the destructor: Python
    never removes a C++ QAccessibleTabBar.
  - Qt's 'void *QAccessibleTabBar::interface_cast(QAccessible::InterfaceType
    t)': gives 'void', which has no cute class yet.

  What has no ritual
  ------------------

  1 of the 17 functions Qt declares: 1 leans on 'non-virtual thunk to
  QAccessibleTabBar.

  What to expect
  --------------

  - The C++ QAccessibleTabBar is created at the first use, not by
    'QAccessibleTabBar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleTabBar.
  - Each name of Qt's QAccessibleTabBar that has no cute function yet,
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
  __qt_class__ = 'QAccessibleTabBar'

  #  Qt's QAccessibleTabBar is built on more than one class. The part of a
  #  C++ QAccessibleTabBar that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QAccessibleSelectionInterface':
          'ritual_cast_QAccessibleTabBar_QAccessibleSelectionInterface',
  }

  #  A C++ QAccessibleTabBar Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleTabBar'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def focusChild(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleTabBar::focusChild() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletabbar.html#focusChild

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleTabBar::focusChild() const
    ritual = 'ritual_ZNK17QAccessibleTabBar10focusChildEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QAccessibleTabBar10focusChildEv'
    address = self.uglySide.call(ritual)
    return QAccessibleInterface._cuteAt(address)

  def childCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleTabBar::childCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletabbar.html#childCount
    """
    #  int QAccessibleTabBar::childCount() const
    ritual = 'ritual_ZNK17QAccessibleTabBar10childCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QAccessibleTabBar10childCountEv'
    return self.uglySide.call(ritual)

  @overload(QAccessible.Text)
  def text(self, t: QAccessible.Text) -> str:
    """
    Calls Qt's 'QString QAccessibleTabBar::text(QAccessible::Text t) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletabbar.html#text

    Parameters
    ----------

    t : QAccessible.Text
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleTabBar::text(QAccessible::Text t) const
    return self.uglySide.call(
        'ritual_ZNK17QAccessibleTabBar4textEN11QAccessible4TextE', t.value,
    )

  @overload(int)
  def child(self, index: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleTabBar::child(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletabbar.html#child

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
    #  QAccessibleInterface *QAccessibleTabBar::child(int index) const
    address = self.uglySide.call(
        'ritual_ZNK17QAccessibleTabBar5childEi', index,
    )
    return QAccessibleInterface._cuteAt(address)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def indexOfChild(self, child: Optional[QAccessibleInterface]) -> int:
    """
    Calls Qt's 'int QAccessibleTabBar::indexOfChild(const
    QAccessibleInterface *child) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletabbar.html#indexOfChild

    Parameters
    ----------

    child : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QAccessibleTabBar::indexOfChild(const QAccessibleInterface *child)
    #      const
    return self.uglySide.call(
        'ritual_ZNK17QAccessibleTabBar12indexOfChildEPK20QAccessibleInterfa'
        'ce',
        self._addressOf(child, 'QAccessibleInterface'),
    )

  def selectedItemCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleTabBar::selectedItemCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletabbar.html#selectedItemCount
    """
    #  int QAccessibleTabBar::selectedItemCount() const
    ritual = 'ritual_ZNK17QAccessibleTabBar17selectedItemCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QAccessibleTabBar17selectedItemCountEv'
    return self.uglySide.call(ritual)

  def selectedItems(self) -> QList[QAccessibleInterface]:
    """
    Calls Qt's 'QList<QAccessibleInterface *>
    QAccessibleTabBar::selectedItems() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletabbar.html#selectedItems

    Returns
    -------

    QList[QAccessibleInterface]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAccessibleInterface *> QAccessibleTabBar::selectedItems() const
    address = self.uglySide.call(
        'ritual_ZNK17QAccessibleTabBar13selectedItemsEv',
    )
    return QList[QAccessibleInterface]._cuteOwning(address)

  @overload(int)
  def selectedItem(
      self,
      selectionIndex: int,
  ) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleTabBar::selectedItem(int
    selectionIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletabbar.html#selectedItem

    Parameters
    ----------

    selectionIndex : int
      Passed on as it is.

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleTabBar::selectedItem(int
    #      selectionIndex) const
    ritual = 'ritual_ZNK17QAccessibleTabBar12selectedItemEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QAccessibleTabBar12selectedItemEi'
    address = self.uglySide.call(ritual, selectionIndex)
    return QAccessibleInterface._cuteAt(address)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def isSelected(self, childItem: Optional[QAccessibleInterface]) -> bool:
    """
    Calls Qt's 'bool QAccessibleTabBar::isSelected(QAccessibleInterface
    *childItem) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletabbar.html#isSelected

    Parameters
    ----------

    childItem : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAccessibleTabBar::isSelected(QAccessibleInterface *childItem)
    #      const
    ritual = (
        'ritual_ZNK17QAccessibleTabBar10isSelectedEP20QAccessibleInterface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QAccessibleTabBar10isSelectedEP20QAccessibleInte'
          'rface')
    return self.uglySide.call(
        ritual, self._addressOf(childItem, 'QAccessibleInterface'),
    )

  def tabBar(self) -> Optional[QTabBar]:
    """
    Calls Qt's 'QTabBar *QAccessibleTabBar::tabBar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletabbar.html#tabBar

    Returns
    -------

    Optional[QTabBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTabBar *QAccessibleTabBar::tabBar() const
    address = self.uglySide.call('ritual_ZNK17QAccessibleTabBar6tabBarEv')
    from . import QTabBar
    return QTabBar._cuteAt(address)

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
    Qt's 'QAccessibleTabBar::QAccessibleTabBar(QWidget *w)': leans on
    'non-virtual thunk to QAccessibleTabBar::clear()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QAccessibleTabBar.__init__' has no cute function yet. Qt's "
        "'QAccessibleTabBar::QAccessibleTabBar(QWidget *w)': leans on "
        "'non-virtual thunk to QAccessibleTabBar::clear()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def select(self, childItem: Optional[QAccessibleInterface]) -> bool:
    """
    Calls Qt's 'bool QAccessibleTabBar::select(QAccessibleInterface
    *childItem)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletabbar.html#select

    Parameters
    ----------

    childItem : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAccessibleTabBar::select(QAccessibleInterface *childItem)
    ritual = 'ritual_ZN17QAccessibleTabBar6selectEP20QAccessibleInterface'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAccessibleTabBar6selectEP20QAccessibleInterface')
    return self.uglySide.call(
        ritual, self._addressOf(childItem, 'QAccessibleInterface'),
    )

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def unselect(self, childItem: Optional[QAccessibleInterface]) -> bool:
    """
    Calls Qt's 'bool QAccessibleTabBar::unselect(QAccessibleInterface
    *childItem)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletabbar.html#unselect

    Parameters
    ----------

    childItem : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAccessibleTabBar::unselect(QAccessibleInterface *childItem)
    ritual = 'ritual_ZN17QAccessibleTabBar8unselectEP20QAccessibleInterface'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAccessibleTabBar8unselectEP20QAccessibleInterfac'
          'e')
    return self.uglySide.call(
        ritual, self._addressOf(childItem, 'QAccessibleInterface'),
    )

  def selectAll(self) -> bool:
    """
    Calls Qt's 'bool QAccessibleTabBar::selectAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletabbar.html#selectAll
    """
    #  bool QAccessibleTabBar::selectAll()
    ritual = 'ritual_ZN17QAccessibleTabBar9selectAllEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QAccessibleTabBar9selectAllEv'
    return self.uglySide.call(ritual)

  def clear(self) -> bool:
    """
    Calls Qt's 'bool QAccessibleTabBar::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletabbar.html#clear
    """
    #  bool QAccessibleTabBar::clear()
    ritual = 'ritual_ZN17QAccessibleTabBar5clearEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QAccessibleTabBar5clearEv'
    return self.uglySide.call(ritual)
