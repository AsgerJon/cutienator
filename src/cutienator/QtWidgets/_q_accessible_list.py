"""
QAccessibleList binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/itemviews_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QAccessibleList to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtCore import QList
from ..QtGui import QAccessibleInterface
from . import QAccessibleTable

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class QAccessibleList(QAccessibleTable):
  """
  The cute side of Qt's QAccessibleList: a plain Python object standing in
  front of one C++ QAccessibleList.

  It is built on the cute 'QAccessibleTable', as Qt's QAccessibleList is
  built on Qt's QAccessibleTable, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleList that has a ritual and that Python
  can call so far, 4 names in all: 'child', 'cellAt', 'selectedCellCount',
  'selectedCells'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 leans on 'non-virtual thunk to
  QAccessibleTable.

  What to expect
  --------------

  - The C++ QAccessibleList is created at the first use, not by
    'QAccessibleList(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleList.
  - Each name of Qt's QAccessibleList that has no cute function yet,
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
  __qt_class__ = 'QAccessibleList'

  #  A C++ QAccessibleList Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleList'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def child(self, index: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleList::child(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblelist.html#child

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
    #  QAccessibleInterface *QAccessibleList::child(int index) const
    ritual = 'ritual_ZNK15QAccessibleList5childEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QAccessibleList5childEi'
    address = self.uglySide.call(ritual, index)
    return QAccessibleInterface._cuteAt(address)

  @overload(int, int)
  def cellAt(self, row: int, column: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleList::cellAt(int row, int
    column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblelist.html#cellAt

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
    #  QAccessibleInterface *QAccessibleList::cellAt(int row, int column)
    #      const
    ritual = 'ritual_ZNK15QAccessibleList6cellAtEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QAccessibleList6cellAtEii'
    address = self.uglySide.call(ritual, row, column)
    return QAccessibleInterface._cuteAt(address)

  def selectedCellCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleList::selectedCellCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblelist.html#selectedCellCount
    """
    #  int QAccessibleList::selectedCellCount() const
    ritual = 'ritual_ZNK15QAccessibleList17selectedCellCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QAccessibleList17selectedCellCountEv'
    return self.uglySide.call(ritual)

  def selectedCells(self) -> QList[QAccessibleInterface]:
    """
    Calls Qt's 'QList<QAccessibleInterface *>
    QAccessibleList::selectedCells() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblelist.html#selectedCells

    Returns
    -------

    QList[QAccessibleInterface]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAccessibleInterface *> QAccessibleList::selectedCells() const
    address = self.uglySide.call(
        'ritual_ZNK15QAccessibleList13selectedCellsEv',
    )
    return QList[QAccessibleInterface]._cuteOwning(address)

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
    Qt's 'QAccessibleList::QAccessibleList(QWidget *w)': leans on
    'non-virtual thunk to QAccessibleTable::selectedItems() const', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QAccessibleList.__init__' has no cute function yet. Qt's "
        "'QAccessibleList::QAccessibleList(QWidget *w)': leans on "
        "'non-virtual thunk to QAccessibleTable::selectedItems() const', "
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
