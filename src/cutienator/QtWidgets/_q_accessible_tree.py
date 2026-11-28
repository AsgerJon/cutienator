"""
QAccessibleTree binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/itemviews_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QAccessibleTree to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtGui import QAccessibleInterface
from . import QAccessibleTable

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QModelIndex

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleTree(QAccessibleTable):
  """
  The cute side of Qt's QAccessibleTree: a plain Python object standing in
  front of one C++ QAccessibleTree.

  It is built on the cute 'QAccessibleTable', as Qt's QAccessibleTree is
  built on Qt's QAccessibleTable, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleTree that has a ritual and that Python
  can call so far, 11 names in all: 'childAt', 'focusChild', 'childCount',
  'child', 'indexOfChild', 'rowCount', 'cellAt', 'rowDescription',
  'isRowSelected', 'selectRow', 'indexFromLogical'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  1 of the 12 functions Qt declares: 1 leans on 'non-virtual thunk to
  QAccessibleTable.

  What to expect
  --------------

  - The C++ QAccessibleTree is created at the first use, not by
    'QAccessibleTree(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleTree.
  - Each name of Qt's QAccessibleTree that has no cute function yet,
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
  __qt_class__ = 'QAccessibleTree'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int)
  def childAt(self, x: int, y: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleTree::childAt(int x, int y)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletree.html#childAt

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
    #  QAccessibleInterface *QAccessibleTree::childAt(int x, int y) const
    ritual = 'ritual_ZNK15QAccessibleTree7childAtEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QAccessibleTree7childAtEii'
    address = self.uglySide.call(ritual, x, y)
    return QAccessibleInterface._cuteAt(address)

  def focusChild(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleTree::focusChild() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletree.html#focusChild

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleTree::focusChild() const
    ritual = 'ritual_ZNK15QAccessibleTree10focusChildEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QAccessibleTree10focusChildEv'
    address = self.uglySide.call(ritual)
    return QAccessibleInterface._cuteAt(address)

  def childCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleTree::childCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletree.html#childCount
    """
    #  int QAccessibleTree::childCount() const
    ritual = 'ritual_ZNK15QAccessibleTree10childCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QAccessibleTree10childCountEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def child(self, index: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleTree::child(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletree.html#child

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
    #  QAccessibleInterface *QAccessibleTree::child(int index) const
    ritual = 'ritual_ZNK15QAccessibleTree5childEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QAccessibleTree5childEi'
    address = self.uglySide.call(ritual, index)
    return QAccessibleInterface._cuteAt(address)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def indexOfChild(self, a0: Optional[QAccessibleInterface]) -> int:
    """
    Calls Qt's 'int QAccessibleTree::indexOfChild(const QAccessibleInterface
    *a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletree.html#indexOfChild

    Parameters
    ----------

    a0 : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QAccessibleTree::indexOfChild(const QAccessibleInterface *a0)
    #      const
    ritual = (
        'ritual_ZNK15QAccessibleTree12indexOfChildEPK20QAccessibleInterface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK15QAccessibleTree12indexOfChildEPK20QAccessibleInt'
          'erface')
    return self.uglySide.call(
        ritual, self._addressOf(a0, 'QAccessibleInterface'),
    )

  def rowCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleTree::rowCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletree.html#rowCount
    """
    #  int QAccessibleTree::rowCount() const
    ritual = 'ritual_ZNK15QAccessibleTree8rowCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QAccessibleTree8rowCountEv'
    return self.uglySide.call(ritual)

  @overload(int, int)
  def cellAt(self, row: int, column: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleTree::cellAt(int row, int
    column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletree.html#cellAt

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleTree::cellAt(int row, int column)
    #      const
    ritual = 'ritual_ZNK15QAccessibleTree6cellAtEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QAccessibleTree6cellAtEii'
    address = self.uglySide.call(ritual, row, column)
    return QAccessibleInterface._cuteAt(address)

  @overload(int)
  def rowDescription(self, row: int) -> str:
    """
    Calls Qt's 'QString QAccessibleTree::rowDescription(int row) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletree.html#rowDescription

    Parameters
    ----------

    row : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleTree::rowDescription(int row) const
    ritual = 'ritual_ZNK15QAccessibleTree14rowDescriptionEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QAccessibleTree14rowDescriptionEi'
    return self.uglySide.call(ritual, row)

  @overload(int)
  def isRowSelected(self, row: int) -> bool:
    """
    Calls Qt's 'bool QAccessibleTree::isRowSelected(int row) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletree.html#isRowSelected

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  bool QAccessibleTree::isRowSelected(int row) const
    ritual = 'ritual_ZNK15QAccessibleTree13isRowSelectedEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QAccessibleTree13isRowSelectedEi'
    return self.uglySide.call(ritual, row)

  @overload(int)
  @overload(int, int)
  def indexFromLogical(self, row: int, column: int = 0) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QAccessibleTree::indexFromLogical(int row, int
    column) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletree.html#indexFromLogical

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QAccessibleTree::indexFromLogical(int row, int column)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK15QAccessibleTree16indexFromLogicalEii', row, column,
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

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
    Qt's 'QAccessibleTree::QAccessibleTree(QWidget *w)': leans on
    'non-virtual thunk to
    QAccessibleTable::interface_cast(QAccessible::InterfaceType)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QAccessibleTree.__init__' has no cute function yet. Qt's "
        "'QAccessibleTree::QAccessibleTree(QWidget *w)': leans on "
        "'non-virtual thunk to "
        "QAccessibleTable::interface_cast(QAccessible::InterfaceType)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  @overload(int)
  def selectRow(self, row: int) -> bool:
    """
    Calls Qt's 'bool QAccessibleTree::selectRow(int row)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletree.html#selectRow

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  bool QAccessibleTree::selectRow(int row)
    ritual = 'ritual_ZN15QAccessibleTree9selectRowEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QAccessibleTree9selectRowEi'
    return self.uglySide.call(ritual, row)
