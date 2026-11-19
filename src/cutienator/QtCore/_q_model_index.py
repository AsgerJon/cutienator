"""
QModelIndex binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qabstractitemmodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ._qt import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QModelIndex(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QModelIndex: a plain Python object standing in front
  of one C++ QModelIndex.

  C++ hands a QModelIndex around as a copy, so every C++ QModelIndex behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QModelIndex that has a ritual and that Python can
  call so far, 11 names in all: 'row', 'column', 'internalId', 'parent',
  'sibling', 'siblingAtColumn', 'siblingAtRow', 'data', 'flags', 'model',
  'isValid'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QModelIndex::multiData(QModelRoleDataSpan roleDataSpan)
    const': names 'QModelRoleDataSpan', which has no cute class yet.
  - Qt's 'QModelIndex::~QModelIndex()': the destructor: Python removes its
    C++ QModelIndex by it, and has no other use for it.

  What has no ritual
  ------------------

  4 of the 18 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 2 private.

  What to expect
  --------------

  - The C++ QModelIndex is created at the first use, not by
    'QModelIndex(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QModelIndex back gives a copy the ritual made for
    Python, in a new cute QModelIndex.
  """

  #  The cute classes made after this one that its functions take or give;
  #  see 'WAIT'.
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QVariant = WAIT['QVariant']

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QModelIndex'

  #  Qt's '~QModelIndex()'. Naming it makes this a value class: Python owns
  #  every C++ QModelIndex behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QModelIndexD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def row(self) -> int:
    """
    Calls Qt's 'int QModelIndex::row() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelindex.html#row
    """
    #  int QModelIndex::row() const
    return self.uglySide.call('ritual_ZNK11QModelIndex3rowEv')

  def column(self) -> int:
    """
    Calls Qt's 'int QModelIndex::column() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelindex.html#column
    """
    #  int QModelIndex::column() const
    return self.uglySide.call('ritual_ZNK11QModelIndex6columnEv')

  def internalId(self) -> int:
    """
    Calls Qt's 'quintptr QModelIndex::internalId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelindex.html#internalId
    """
    #  quintptr QModelIndex::internalId() const
    return self.uglySide.call('ritual_ZNK11QModelIndex10internalIdEv')

  def parent(self) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QModelIndex::parent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelindex.html#parent

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QModelIndex::parent() const
    address = self.uglySide.call('ritual_ZNK11QModelIndex6parentEv')
    return QModelIndex._cuteOwning(address)

  @overload(int, int)
  def sibling(self, row: int, column: int) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QModelIndex::sibling(int row, int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelindex.html#sibling

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QModelIndex::sibling(int row, int column) const
    address = self.uglySide.call(
        'ritual_ZNK11QModelIndex7siblingEii', row, column,
    )
    return QModelIndex._cuteOwning(address)

  @overload(int)
  def siblingAtColumn(self, column: int) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QModelIndex::siblingAtColumn(int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelindex.html#siblingAtColumn

    Parameters
    ----------

    column : int
      Passed on as it is.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QModelIndex::siblingAtColumn(int column) const
    address = self.uglySide.call(
        'ritual_ZNK11QModelIndex15siblingAtColumnEi', column,
    )
    return QModelIndex._cuteOwning(address)

  @overload(int)
  def siblingAtRow(self, row: int) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QModelIndex::siblingAtRow(int row) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelindex.html#siblingAtRow

    Parameters
    ----------

    row : int
      Passed on as it is.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QModelIndex::siblingAtRow(int row) const
    address = self.uglySide.call(
        'ritual_ZNK11QModelIndex12siblingAtRowEi', row,
    )
    return QModelIndex._cuteOwning(address)

  @overload()
  @overload(int)
  def data(self, role: int = 0) -> QVariant:
    """
    Calls Qt's 'QVariant QModelIndex::data(int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelindex.html#data

    Parameters
    ----------

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QModelIndex::data(int role) const
    address = self.uglySide.call('ritual_ZNK11QModelIndex4dataEi', role)
    return self.QVariant._cuteOwning(address)

  def flags(self) -> Qt.ItemFlags:
    """
    Calls Qt's 'Qt::ItemFlags QModelIndex::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelindex.html#flags

    Returns
    -------

    Qt.ItemFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::ItemFlags QModelIndex::flags() const
    return Qt.ItemFlags(self.uglySide.call(
        'ritual_ZNK11QModelIndex5flagsEv',
    ))

  def model(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'const QAbstractItemModel *QModelIndex::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelindex.html#model

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QAbstractItemModel *QModelIndex::model() const
    address = self.uglySide.call('ritual_ZNK11QModelIndex5modelEv')
    return self.QAbstractItemModel._cuteAt(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QModelIndex::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelindex.html#isValid
    """
    #  bool QModelIndex::isValid() const
    return self.uglySide.call('ritual_ZNK11QModelIndex7isValidEv')

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QModelIndex::QModelIndex()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmodelindex.html#QModelIndex
    """
    #  QModelIndex::QModelIndex()
    self._noteCreation(QModelIndex, lambda: Rituals.call(
        'ritual_ZN11QModelIndexC1Ev',
    ))

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
