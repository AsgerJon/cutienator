"""
QQmlSortFilterProxyModelPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmlsortfilterproxymodel_p_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlSortFilterProxyModelPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import Qt, QAbstractItemModel, QAbstractProxyModelPrivate
from ..QtCore import QList
from . import QSortFilterProxyModelHelper

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QAbstractProxyModel, QModelIndex
  from ..QtCore import QPersistentModelIndex
  from . import QQmlSortFilterProxyModel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QPersistentModelIndex = WAIT['QPersistentModelIndex']


class QQmlSortFilterProxyModelPrivate(QAbstractProxyModelPrivate, QSortFilterProxyModelHelper):
  """
  The cute side of Qt's QQmlSortFilterProxyModelPrivate: a plain Python
  object standing in front of one C++ QQmlSortFilterProxyModelPrivate.

  It is built on the cute 'QAbstractProxyModelPrivate', as Qt's
  QQmlSortFilterProxyModelPrivate is built on Qt's
  QAbstractProxyModelPrivate, and has everything that class has. It is built
  on the cute 'QSortFilterProxyModelHelper' as well, as Qt's
  QQmlSortFilterProxyModelPrivate is built on Qt's
  QSortFilterProxyModelHelper too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlSortFilterProxyModelPrivate that has a ritual
  and that Python can call so far, 40 names in all: 'q_func',
  'recursiveParentAcceptsRow', 'recursiveChildAcceptsRow',
  'updatePrimaryColumn', 'findPrimarySortColumn',
  'changePersistentIndexList', 'beginInsertRows', 'beginInsertColumns',
  'endInsertRows', 'endInsertColumns', 'beginRemoveRows',
  'beginRemoveColumns', 'endRemoveRows', 'endRemoveColumns',
  'beginResetModel', 'endResetModel', '_q_sourceHeaderDataChanged',
  '_q_sourceAboutToBeReset', '_q_sourceReset', '_q_clearMapping',
  '_q_sourceLayoutAboutToBeChanged', '_q_sourceLayoutChanged',
  '_q_sourceRowsAboutToBeInserted', '_q_sourceRowsInserted',
  '_q_sourceRowsAboutToBeRemoved', '_q_sourceRowsRemoved',
  '_q_sourceRowsAboutToBeMoved', '_q_sourceRowsMoved',
  '_q_sourceColumnsAboutToBeInserted', '_q_sourceColumnsInserted',
  '_q_sourceColumnsAboutToBeRemoved', '_q_sourceColumnsRemoved',
  '_q_sourceColumnsAboutToBeMoved', '_q_sourceColumnsMoved', 'proxyModel',
  'filterAcceptsRowInternal', 'filterAcceptsRow',
  'filterAcceptsColumnInternal', 'filterAcceptsColumn', 'lessThan'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQmlSortFilterProxyModel
    *QQmlSortFilterProxyModelPrivate::q_func() const': takes in Python what
    'QQmlSortFilterProxyModel *QQmlSortFilterProxyModelPrivate::q_func()'
    takes.
  - Qt's 'bool
    QQmlSortFilterProxyModelPrivate::containRoleForRecursiveFilter(const
    QList<int> &roles) const': takes a type Python has no way to hand over
    yet.
  - Qt's 'QList<std::pair<int, QList<int>>>
    QQmlSortFilterProxyModelPrivate::proxy_intervals_for_source_items_to_add(
    const QList<int> &proxy_to_source, const QList<int> &source_items, const
    QModelIndex &source_parent, QSortFilterProxyModelHelper::Direction
    direction) const': takes a type Python has no way to hand over yet.
  - Qt's 'bool QQmlSortFilterProxyModelPrivate::needsReorder(const QList<int>
    &source_rows, const QModelIndex &source_parent) const': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QQmlSortFilterProxyModelPrivate::_q_sourceDataChanged(const
    QModelIndex &source_top_left, const QModelIndex &source_bottom_right,
    const QList<int> &roles)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QModelIndex QQmlSortFilterProxyModelPrivate::createIndex(int row,
    int column, QHash<QtPrivate::QModelIndexWrapper,
    QSortFilterProxyModelHelper::Mapping *>::const_iterator it) const': takes
    a type Python has no way to hand over yet.
  - Qt's 'void QQmlSortFilterProxyModelPrivate::sort_source_rows(QList<int>
    &source_rows, const QModelIndex &source_parent) const': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 48 functions Qt declares: 1 leans on 'QQmlSorterCompositor.

  What to expect
  --------------

  - The C++ QQmlSortFilterProxyModelPrivate is created at the first use, not
    by 'QQmlSortFilterProxyModelPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlSortFilterProxyModelPrivate.
  - Each name of Qt's QQmlSortFilterProxyModelPrivate that has no cute
    function yet, '_q_sourceDataChanged', 'containRoleForRecursiveFilter',
    'init', 'needsReorder', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSortFilterProxyModelPrivate'

  #  Qt's QQmlSortFilterProxyModelPrivate is built on more than one class.
  #  The part of a C++ QQmlSortFilterProxyModelPrivate that belongs to a
  #  class after the first begins somewhere inside the object, and the ritual
  #  named for that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QSortFilterProxyModelHelper':
          'ritual_cast_QQmlSortFilterProxyModelPrivate_QSortFilterProxyModelHelper',
  }

  #  A C++ QQmlSortFilterProxyModelPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlSortFilterProxyModelPrivate'

  #  The functions Qt calls itself that QQmlSortFilterProxyModelPrivate is
  #  the first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'createIndex': (
          'QModelIndex QQmlSortFilterProxyModelPrivate::createIndex(int, '
          'int, QHash<QtPrivate::QModelIndexWrapper, '
          'QSortFilterProxyModelHelper::Mapping *>::const_iterator) const',
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QModelIndex)
  def recursiveParentAcceptsRow(self, source_parent: QModelIndex) -> bool:
    """
    Calls Qt's 'bool
    QQmlSortFilterProxyModelPrivate::recursiveParentAcceptsRow(const
    QModelIndex &source_parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html

    Parameters
    ----------

    source_parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QQmlSortFilterProxyModelPrivate::recursiveParentAcceptsRow(const
    #      QModelIndex &source_parent) const
    return self.uglySide.call(
        'ritual_ZNK31QQmlSortFilterProxyModelPrivate25recursiveParentAccept'
        'sRowERK11QModelIndex',
        self._valueOf(source_parent),
    )

  @overload(int, QModelIndex)
  def recursiveChildAcceptsRow(
      self,
      source_row: int,
      source_parent: QModelIndex,
  ) -> bool:
    """
    Calls Qt's 'bool
    QQmlSortFilterProxyModelPrivate::recursiveChildAcceptsRow(int source_row,
    const QModelIndex &source_parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html

    Parameters
    ----------

    source_row : int
      Passed on as it is.

    source_parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QQmlSortFilterProxyModelPrivate::recursiveChildAcceptsRow(int
    #      source_row, const QModelIndex &source_parent) const
    return self.uglySide.call(
        'ritual_ZNK31QQmlSortFilterProxyModelPrivate24recursiveChildAccepts'
        'RowEiRK11QModelIndex',
        source_row, self._valueOf(source_parent),
    )

  def findPrimarySortColumn(self) -> int:
    """
    Calls Qt's 'int QQmlSortFilterProxyModelPrivate::findPrimarySortColumn()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html
    """
    #  int QQmlSortFilterProxyModelPrivate::findPrimarySortColumn() const
    return self.uglySide.call(
        'ritual_ZNK31QQmlSortFilterProxyModelPrivate21findPrimarySortColumn'
        'Ev',
    )

  def proxyModel(self) -> Optional[QAbstractProxyModel]:
    """
    Calls Qt's 'const QAbstractProxyModel
    *QQmlSortFilterProxyModelPrivate::proxyModel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html#proxyModel

    Returns
    -------

    Optional[QAbstractProxyModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QAbstractProxyModel
    #      *QQmlSortFilterProxyModelPrivate::proxyModel() const
    ritual = 'ritual_ZNK31QQmlSortFilterProxyModelPrivate10proxyModelEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK31QQmlSortFilterProxyModelPrivate10proxyModelEv')
    address = self.uglySide.call(ritual)
    from ..QtCore import QAbstractProxyModel
    return QAbstractProxyModel._cuteAt(address)

  @overload(int, QModelIndex)
  def filterAcceptsRowInternal(
      self,
      sourceRow: int,
      sourceIndex: QModelIndex,
  ) -> bool:
    """
    Calls Qt's 'bool
    QQmlSortFilterProxyModelPrivate::filterAcceptsRowInternal(int sourceRow,
    const QModelIndex &sourceIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html

    Parameters
    ----------

    sourceRow : int
      Passed on as it is.

    sourceIndex : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QQmlSortFilterProxyModelPrivate::filterAcceptsRowInternal(int
    #      sourceRow, const QModelIndex &sourceIndex) const
    ritual = (
        'ritual_ZNK31QQmlSortFilterProxyModelPrivate24filterAcceptsRowInter'
        'nalEiRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK31QQmlSortFilterProxyModelPrivate24filterAcceptsRo'
          'wInternalEiRK11QModelIndex')
    return self.uglySide.call(ritual, sourceRow, self._valueOf(sourceIndex))

  @overload(int, QModelIndex)
  def filterAcceptsRow(
      self,
      source_row: int,
      source_parent: QModelIndex,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlSortFilterProxyModelPrivate::filterAcceptsRow(int
    source_row, const QModelIndex &source_parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html

    Parameters
    ----------

    source_row : int
      Passed on as it is.

    source_parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QQmlSortFilterProxyModelPrivate::filterAcceptsRow(int source_row,
    #      const QModelIndex &source_parent) const
    ritual = (
        'ritual_ZNK31QQmlSortFilterProxyModelPrivate16filterAcceptsRowEiRK1'
        '1QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK31QQmlSortFilterProxyModelPrivate16filterAcceptsRo'
          'wEiRK11QModelIndex')
    return self.uglySide.call(
        ritual, source_row, self._valueOf(source_parent),
    )

  @overload(int, QModelIndex)
  def filterAcceptsColumnInternal(
      self,
      sourceColumn: int,
      sourceIndex: QModelIndex,
  ) -> bool:
    """
    Calls Qt's 'bool
    QQmlSortFilterProxyModelPrivate::filterAcceptsColumnInternal(int
    sourceColumn, const QModelIndex &sourceIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html

    Parameters
    ----------

    sourceColumn : int
      Passed on as it is.

    sourceIndex : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QQmlSortFilterProxyModelPrivate::filterAcceptsColumnInternal(int
    #      sourceColumn, const QModelIndex &sourceIndex) const
    ritual = (
        'ritual_ZNK31QQmlSortFilterProxyModelPrivate27filterAcceptsColumnIn'
        'ternalEiRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK31QQmlSortFilterProxyModelPrivate27filterAcceptsCo'
          'lumnInternalEiRK11QModelIndex')
    return self.uglySide.call(
        ritual, sourceColumn, self._valueOf(sourceIndex),
    )

  @overload(int, QModelIndex)
  def filterAcceptsColumn(
      self,
      source_column: int,
      source_parent: QModelIndex,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlSortFilterProxyModelPrivate::filterAcceptsColumn(int
    source_column, const QModelIndex &source_parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html

    Parameters
    ----------

    source_column : int
      Passed on as it is.

    source_parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QQmlSortFilterProxyModelPrivate::filterAcceptsColumn(int
    #      source_column, const QModelIndex &source_parent) const
    ritual = (
        'ritual_ZNK31QQmlSortFilterProxyModelPrivate19filterAcceptsColumnEi'
        'RK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK31QQmlSortFilterProxyModelPrivate19filterAcceptsCo'
          'lumnEiRK11QModelIndex')
    return self.uglySide.call(
        ritual, source_column, self._valueOf(source_parent),
    )

  @overload(QModelIndex, QModelIndex)
  def lessThan(
      self,
      source_left: QModelIndex,
      source_right: QModelIndex,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlSortFilterProxyModelPrivate::lessThan(const
    QModelIndex &source_left, const QModelIndex &source_right) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html#lessThan

    Parameters
    ----------

    source_left : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    source_right : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QQmlSortFilterProxyModelPrivate::lessThan(const QModelIndex
    #      &source_left, const QModelIndex &source_right) const
    ritual = (
        'ritual_ZNK31QQmlSortFilterProxyModelPrivate8lessThanERK11QModelInd'
        'exS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK31QQmlSortFilterProxyModelPrivate8lessThanERK11QMo'
          'delIndexS2_')
    return self.uglySide.call(
        ritual, self._valueOf(source_left), self._valueOf(source_right),
    )

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

  def q_func(self) -> Optional[QQmlSortFilterProxyModel]:
    """
    Calls Qt's 'QQmlSortFilterProxyModel
    *QQmlSortFilterProxyModelPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html#q_func

    Returns
    -------

    Optional[QQmlSortFilterProxyModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlSortFilterProxyModel *QQmlSortFilterProxyModelPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN31QQmlSortFilterProxyModelPrivate6q_funcEv',
    )
    from . import QQmlSortFilterProxyModel
    return QQmlSortFilterProxyModel._cuteAt(address)

  def updatePrimaryColumn(self) -> bool:
    """
    Calls Qt's 'bool QQmlSortFilterProxyModelPrivate::updatePrimaryColumn()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html
    """
    #  bool QQmlSortFilterProxyModelPrivate::updatePrimaryColumn()
    return self.uglySide.call(
        'ritual_ZN31QQmlSortFilterProxyModelPrivate19updatePrimaryColumnEv',
    )

  @overload(QList[QModelIndex], QList[QModelIndex])
  def changePersistentIndexList(
      self,
      from_: QList[QModelIndex],
      to: QList[QModelIndex],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlSortFilterProxyModelPrivate::changePersistentIndexList(const
    QModelIndexList &from, const QModelIndexList &to)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html

    Parameters
    ----------

    from_ : QList[QModelIndex]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    to : QList[QModelIndex]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlSortFilterProxyModelPrivate::changePersistentIndexList(const
    #      QModelIndexList &from, const QModelIndexList &to)
    self.uglySide.call(
        'ritual_ZN31QQmlSortFilterProxyModelPrivate25changePersistentIndexL'
        'istERK5QListI11QModelIndexES4_',
        self._valueOf(from_), self._valueOf(to),
    )

  @overload(QModelIndex, int, int)
  def beginInsertRows(
      self,
      parent: QModelIndex,
      first: int,
      last: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlSortFilterProxyModelPrivate::beginInsertRows(const
    QModelIndex &parent, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    first : int
      Passed on as it is.

    last : int
      Passed on as it is.
    """
    #  void QQmlSortFilterProxyModelPrivate::beginInsertRows(const
    #      QModelIndex &parent, int first, int last)
    ritual = (
        'ritual_ZN31QQmlSortFilterProxyModelPrivate15beginInsertRowsERK11QM'
        'odelIndexii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN31QQmlSortFilterProxyModelPrivate15beginInsertRowsE'
          'RK11QModelIndexii')
    self.uglySide.call(ritual, self._valueOf(parent), first, last)

  @overload(QModelIndex, int, int)
  def beginInsertColumns(
      self,
      parent: QModelIndex,
      first: int,
      last: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlSortFilterProxyModelPrivate::beginInsertColumns(const QModelIndex
    &parent, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    first : int
      Passed on as it is.

    last : int
      Passed on as it is.
    """
    #  void QQmlSortFilterProxyModelPrivate::beginInsertColumns(const
    #      QModelIndex &parent, int first, int last)
    ritual = (
        'ritual_ZN31QQmlSortFilterProxyModelPrivate18beginInsertColumnsERK1'
        '1QModelIndexii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN31QQmlSortFilterProxyModelPrivate18beginInsertColum'
          'nsERK11QModelIndexii')
    self.uglySide.call(ritual, self._valueOf(parent), first, last)

  def endInsertRows(self) -> None:
    """
    Calls Qt's 'void QQmlSortFilterProxyModelPrivate::endInsertRows()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html#endInsertRows
    """
    #  void QQmlSortFilterProxyModelPrivate::endInsertRows()
    ritual = 'ritual_ZN31QQmlSortFilterProxyModelPrivate13endInsertRowsEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN31QQmlSortFilterProxyModelPrivate13endInsertRowsEv')
    self.uglySide.call(ritual)

  def endInsertColumns(self) -> None:
    """
    Calls Qt's 'void QQmlSortFilterProxyModelPrivate::endInsertColumns()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html
    """
    #  void QQmlSortFilterProxyModelPrivate::endInsertColumns()
    ritual = 'ritual_ZN31QQmlSortFilterProxyModelPrivate16endInsertColumnsEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN31QQmlSortFilterProxyModelPrivate16endInsertColumns'
          'Ev')
    self.uglySide.call(ritual)

  @overload(QModelIndex, int, int)
  def beginRemoveRows(
      self,
      parent: QModelIndex,
      first: int,
      last: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlSortFilterProxyModelPrivate::beginRemoveRows(const
    QModelIndex &parent, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    first : int
      Passed on as it is.

    last : int
      Passed on as it is.
    """
    #  void QQmlSortFilterProxyModelPrivate::beginRemoveRows(const
    #      QModelIndex &parent, int first, int last)
    ritual = (
        'ritual_ZN31QQmlSortFilterProxyModelPrivate15beginRemoveRowsERK11QM'
        'odelIndexii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN31QQmlSortFilterProxyModelPrivate15beginRemoveRowsE'
          'RK11QModelIndexii')
    self.uglySide.call(ritual, self._valueOf(parent), first, last)

  @overload(QModelIndex, int, int)
  def beginRemoveColumns(
      self,
      parent: QModelIndex,
      first: int,
      last: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlSortFilterProxyModelPrivate::beginRemoveColumns(const QModelIndex
    &parent, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    first : int
      Passed on as it is.

    last : int
      Passed on as it is.
    """
    #  void QQmlSortFilterProxyModelPrivate::beginRemoveColumns(const
    #      QModelIndex &parent, int first, int last)
    ritual = (
        'ritual_ZN31QQmlSortFilterProxyModelPrivate18beginRemoveColumnsERK1'
        '1QModelIndexii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN31QQmlSortFilterProxyModelPrivate18beginRemoveColum'
          'nsERK11QModelIndexii')
    self.uglySide.call(ritual, self._valueOf(parent), first, last)

  def endRemoveRows(self) -> None:
    """
    Calls Qt's 'void QQmlSortFilterProxyModelPrivate::endRemoveRows()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html#endRemoveRows
    """
    #  void QQmlSortFilterProxyModelPrivate::endRemoveRows()
    ritual = 'ritual_ZN31QQmlSortFilterProxyModelPrivate13endRemoveRowsEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN31QQmlSortFilterProxyModelPrivate13endRemoveRowsEv')
    self.uglySide.call(ritual)

  def endRemoveColumns(self) -> None:
    """
    Calls Qt's 'void QQmlSortFilterProxyModelPrivate::endRemoveColumns()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html
    """
    #  void QQmlSortFilterProxyModelPrivate::endRemoveColumns()
    ritual = 'ritual_ZN31QQmlSortFilterProxyModelPrivate16endRemoveColumnsEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN31QQmlSortFilterProxyModelPrivate16endRemoveColumns'
          'Ev')
    self.uglySide.call(ritual)

  def beginResetModel(self) -> None:
    """
    Calls Qt's 'void QQmlSortFilterProxyModelPrivate::beginResetModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html
    """
    #  void QQmlSortFilterProxyModelPrivate::beginResetModel()
    ritual = 'ritual_ZN31QQmlSortFilterProxyModelPrivate15beginResetModelEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN31QQmlSortFilterProxyModelPrivate15beginResetModelE'
          'v')
    self.uglySide.call(ritual)

  def endResetModel(self) -> None:
    """
    Calls Qt's 'void QQmlSortFilterProxyModelPrivate::endResetModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html#endResetModel
    """
    #  void QQmlSortFilterProxyModelPrivate::endResetModel()
    ritual = 'ritual_ZN31QQmlSortFilterProxyModelPrivate13endResetModelEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN31QQmlSortFilterProxyModelPrivate13endResetModelEv')
    self.uglySide.call(ritual)

  @overload(Qt.Orientation, int, int)
  def _q_sourceHeaderDataChanged(
      self,
      orientation: Qt.Orientation,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlSortFilterProxyModelPrivate::_q_sourceHeaderDataChanged(Qt::
    Orientation orientation, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QQmlSortFilterProxyModelPrivate::_q_sourceHeaderDataChanged(Qt::
    #      Orientation orientation, int start, int end)
    self.uglySide.call(
        'ritual_ZN31QQmlSortFilterProxyModelPrivate26_q_sourceHeaderDataCha'
        'ngedEN2Qt11OrientationEii',
        orientation.value, start, end,
    )

  def _q_sourceAboutToBeReset(self) -> None:
    """
    Calls Qt's 'void
    QQmlSortFilterProxyModelPrivate::_q_sourceAboutToBeReset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html
    """
    #  void QQmlSortFilterProxyModelPrivate::_q_sourceAboutToBeReset()
    self.uglySide.call(
        'ritual_ZN31QQmlSortFilterProxyModelPrivate23_q_sourceAboutToBeRese'
        'tEv',
    )

  def _q_sourceReset(self) -> None:
    """
    Calls Qt's 'void QQmlSortFilterProxyModelPrivate::_q_sourceReset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html
    """
    #  void QQmlSortFilterProxyModelPrivate::_q_sourceReset()
    self.uglySide.call(
        'ritual_ZN31QQmlSortFilterProxyModelPrivate14_q_sourceResetEv',
    )

  def _q_clearMapping(self) -> None:
    """
    Calls Qt's 'void QQmlSortFilterProxyModelPrivate::_q_clearMapping()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html
    """
    #  void QQmlSortFilterProxyModelPrivate::_q_clearMapping()
    self.uglySide.call(
        'ritual_ZN31QQmlSortFilterProxyModelPrivate15_q_clearMappingEv',
    )

  @overload(
      QList[QPersistentModelIndex], QAbstractItemModel.LayoutChangeHint,
  )
  def _q_sourceLayoutAboutToBeChanged(
      self,
      sourceParents: QList[QPersistentModelIndex],
      hint: QAbstractItemModel.LayoutChangeHint,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlSortFilterProxyModelPrivate::_q_sourceLayoutAboutToBeChanged(const
    QList<QPersistentModelIndex> &sourceParents,
    QAbstractItemModel::LayoutChangeHint hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html

    Parameters
    ----------

    sourceParents : QList[QPersistentModelIndex]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    hint : QAbstractItemModel.LayoutChangeHint
      Passed on as its number.
    """
    #  void QQmlSortFilterProxyModelPrivate::_q_sourceLayoutAboutToBeChanged(
    #      const QList<QPersistentModelIndex> &sourceParents,
    #      QAbstractItemModel::LayoutChangeHint hint)
    self.uglySide.call(
        'ritual_ZN31QQmlSortFilterProxyModelPrivate31_q_sourceLayoutAboutTo'
        'BeChangedERK5QListI21QPersistentModelIndexEN18QAbstractItemModel16'
        'LayoutChangeHintE',
        self._valueOf(sourceParents), hint.value,
    )

  @overload(
      QList[QPersistentModelIndex], QAbstractItemModel.LayoutChangeHint,
  )
  def _q_sourceLayoutChanged(
      self,
      sourceParents: QList[QPersistentModelIndex],
      hint: QAbstractItemModel.LayoutChangeHint,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlSortFilterProxyModelPrivate::_q_sourceLayoutChanged(const
    QList<QPersistentModelIndex> &sourceParents,
    QAbstractItemModel::LayoutChangeHint hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html

    Parameters
    ----------

    sourceParents : QList[QPersistentModelIndex]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    hint : QAbstractItemModel.LayoutChangeHint
      Passed on as its number.
    """
    #  void QQmlSortFilterProxyModelPrivate::_q_sourceLayoutChanged(const
    #      QList<QPersistentModelIndex> &sourceParents,
    #      QAbstractItemModel::LayoutChangeHint hint)
    self.uglySide.call(
        'ritual_ZN31QQmlSortFilterProxyModelPrivate22_q_sourceLayoutChanged'
        'ERK5QListI21QPersistentModelIndexEN18QAbstractItemModel16LayoutCha'
        'ngeHintE',
        self._valueOf(sourceParents), hint.value,
    )

  @overload(QModelIndex, int, int)
  def _q_sourceRowsAboutToBeInserted(
      self,
      source_parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlSortFilterProxyModelPrivate::_q_sourceRowsAboutToBeInserted(const
    QModelIndex &source_parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html

    Parameters
    ----------

    source_parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QQmlSortFilterProxyModelPrivate::_q_sourceRowsAboutToBeInserted(
    #      const QModelIndex &source_parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN31QQmlSortFilterProxyModelPrivate30_q_sourceRowsAboutToBe'
        'InsertedERK11QModelIndexii',
        self._valueOf(source_parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def _q_sourceRowsInserted(
      self,
      source_parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlSortFilterProxyModelPrivate::_q_sourceRowsInserted(const QModelIndex
    &source_parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html

    Parameters
    ----------

    source_parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QQmlSortFilterProxyModelPrivate::_q_sourceRowsInserted(const
    #      QModelIndex &source_parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN31QQmlSortFilterProxyModelPrivate21_q_sourceRowsInsertedE'
        'RK11QModelIndexii',
        self._valueOf(source_parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def _q_sourceRowsAboutToBeRemoved(
      self,
      source_parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlSortFilterProxyModelPrivate::_q_sourceRowsAboutToBeRemoved(const
    QModelIndex &source_parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html

    Parameters
    ----------

    source_parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QQmlSortFilterProxyModelPrivate::_q_sourceRowsAboutToBeRemoved(
    #      const QModelIndex &source_parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN31QQmlSortFilterProxyModelPrivate29_q_sourceRowsAboutToBe'
        'RemovedERK11QModelIndexii',
        self._valueOf(source_parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def _q_sourceRowsRemoved(
      self,
      source_parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlSortFilterProxyModelPrivate::_q_sourceRowsRemoved(const QModelIndex
    &source_parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html

    Parameters
    ----------

    source_parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QQmlSortFilterProxyModelPrivate::_q_sourceRowsRemoved(const
    #      QModelIndex &source_parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN31QQmlSortFilterProxyModelPrivate20_q_sourceRowsRemovedER'
        'K11QModelIndexii',
        self._valueOf(source_parent), start, end,
    )

  @overload(QModelIndex, int, int, QModelIndex, int)
  def _q_sourceRowsAboutToBeMoved(
      self,
      sourceParent: QModelIndex,
      sourceStart: int,
      sourceEnd: int,
      destParent: QModelIndex,
      dest: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlSortFilterProxyModelPrivate::_q_sourceRowsAboutToBeMoved(const
    QModelIndex &sourceParent, int sourceStart, int sourceEnd, const
    QModelIndex &destParent, int dest)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html

    Parameters
    ----------

    sourceParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    sourceStart : int
      Passed on as it is.

    sourceEnd : int
      Passed on as it is.

    destParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    dest : int
      Passed on as it is.
    """
    #  void
    #      QQmlSortFilterProxyModelPrivate::_q_sourceRowsAboutToBeMoved(const
    #      QModelIndex &sourceParent, int sourceStart, int sourceEnd, const
    #      QModelIndex &destParent, int dest)
    self.uglySide.call(
        'ritual_ZN31QQmlSortFilterProxyModelPrivate27_q_sourceRowsAboutToBe'
        'MovedERK11QModelIndexiiS2_i',
        self._valueOf(sourceParent), sourceStart, sourceEnd,
        self._valueOf(destParent), dest,
    )

  @overload(QModelIndex, int, int, QModelIndex, int)
  def _q_sourceRowsMoved(
      self,
      sourceParent: QModelIndex,
      sourceStart: int,
      sourceEnd: int,
      destParent: QModelIndex,
      dest: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlSortFilterProxyModelPrivate::_q_sourceRowsMoved(const QModelIndex
    &sourceParent, int sourceStart, int sourceEnd, const QModelIndex
    &destParent, int dest)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html

    Parameters
    ----------

    sourceParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    sourceStart : int
      Passed on as it is.

    sourceEnd : int
      Passed on as it is.

    destParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    dest : int
      Passed on as it is.
    """
    #  void QQmlSortFilterProxyModelPrivate::_q_sourceRowsMoved(const
    #      QModelIndex &sourceParent, int sourceStart, int sourceEnd, const
    #      QModelIndex &destParent, int dest)
    self.uglySide.call(
        'ritual_ZN31QQmlSortFilterProxyModelPrivate18_q_sourceRowsMovedERK1'
        '1QModelIndexiiS2_i',
        self._valueOf(sourceParent), sourceStart, sourceEnd,
        self._valueOf(destParent), dest,
    )

  @overload(QModelIndex, int, int)
  def _q_sourceColumnsAboutToBeInserted(
      self,
      source_parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlSortFilterProxyModelPrivate::_q_sourceColumnsAboutToBeInserted(const
    QModelIndex &source_parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html

    Parameters
    ----------

    source_parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QQmlSortFilterProxyModelPrivate::
    #      _q_sourceColumnsAboutToBeInserted(const QModelIndex
    #      &source_parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN31QQmlSortFilterProxyModelPrivate33_q_sourceColumnsAboutT'
        'oBeInsertedERK11QModelIndexii',
        self._valueOf(source_parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def _q_sourceColumnsInserted(
      self,
      source_parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlSortFilterProxyModelPrivate::_q_sourceColumnsInserted(const
    QModelIndex &source_parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html

    Parameters
    ----------

    source_parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QQmlSortFilterProxyModelPrivate::_q_sourceColumnsInserted(const
    #      QModelIndex &source_parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN31QQmlSortFilterProxyModelPrivate24_q_sourceColumnsInsert'
        'edERK11QModelIndexii',
        self._valueOf(source_parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def _q_sourceColumnsAboutToBeRemoved(
      self,
      source_parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlSortFilterProxyModelPrivate::_q_sourceColumnsAboutToBeRemoved(const
    QModelIndex &source_parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html

    Parameters
    ----------

    source_parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void
    #      QQmlSortFilterProxyModelPrivate::_q_sourceColumnsAboutToBeRemoved(
    #      const QModelIndex &source_parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN31QQmlSortFilterProxyModelPrivate32_q_sourceColumnsAboutT'
        'oBeRemovedERK11QModelIndexii',
        self._valueOf(source_parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def _q_sourceColumnsRemoved(
      self,
      source_parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlSortFilterProxyModelPrivate::_q_sourceColumnsRemoved(const
    QModelIndex &source_parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html

    Parameters
    ----------

    source_parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QQmlSortFilterProxyModelPrivate::_q_sourceColumnsRemoved(const
    #      QModelIndex &source_parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN31QQmlSortFilterProxyModelPrivate23_q_sourceColumnsRemove'
        'dERK11QModelIndexii',
        self._valueOf(source_parent), start, end,
    )

  @overload(QModelIndex, int, int, QModelIndex, int)
  def _q_sourceColumnsAboutToBeMoved(
      self,
      sourceParent: QModelIndex,
      sourceStart: int,
      sourceEnd: int,
      destParent: QModelIndex,
      dest: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlSortFilterProxyModelPrivate::_q_sourceColumnsAboutToBeMoved(const
    QModelIndex &sourceParent, int sourceStart, int sourceEnd, const
    QModelIndex &destParent, int dest)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html

    Parameters
    ----------

    sourceParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    sourceStart : int
      Passed on as it is.

    sourceEnd : int
      Passed on as it is.

    destParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    dest : int
      Passed on as it is.
    """
    #  void QQmlSortFilterProxyModelPrivate::_q_sourceColumnsAboutToBeMoved(
    #      const QModelIndex &sourceParent, int sourceStart, int sourceEnd,
    #      const QModelIndex &destParent, int dest)
    self.uglySide.call(
        'ritual_ZN31QQmlSortFilterProxyModelPrivate30_q_sourceColumnsAboutT'
        'oBeMovedERK11QModelIndexiiS2_i',
        self._valueOf(sourceParent), sourceStart, sourceEnd,
        self._valueOf(destParent), dest,
    )

  @overload(QModelIndex, int, int, QModelIndex, int)
  def _q_sourceColumnsMoved(
      self,
      sourceParent: QModelIndex,
      sourceStart: int,
      sourceEnd: int,
      destParent: QModelIndex,
      dest: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlSortFilterProxyModelPrivate::_q_sourceColumnsMoved(const QModelIndex
    &sourceParent, int sourceStart, int sourceEnd, const QModelIndex
    &destParent, int dest)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelprivate.html

    Parameters
    ----------

    sourceParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    sourceStart : int
      Passed on as it is.

    sourceEnd : int
      Passed on as it is.

    destParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    dest : int
      Passed on as it is.
    """
    #  void QQmlSortFilterProxyModelPrivate::_q_sourceColumnsMoved(const
    #      QModelIndex &sourceParent, int sourceStart, int sourceEnd, const
    #      QModelIndex &destParent, int dest)
    self.uglySide.call(
        'ritual_ZN31QQmlSortFilterProxyModelPrivate21_q_sourceColumnsMovedE'
        'RK11QModelIndexiiS2_i',
        self._valueOf(sourceParent), sourceStart, sourceEnd,
        self._valueOf(destParent), dest,
    )

  @staticmethod
  def _q_sourceDataChanged(*__, **_) -> Never:
    """
    Qt's 'void QQmlSortFilterProxyModelPrivate::_q_sourceDataChanged(const
    QModelIndex &source_top_left, const QModelIndex &source_bottom_right,
    const QList<int> &roles)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQmlSortFilterProxyModelPrivate._q_sourceDataChanged' has no cute "
        "function yet. Qt's 'void "
        "QQmlSortFilterProxyModelPrivate::_q_sourceDataChanged(const "
        "QModelIndex &source_top_left, const QModelIndex "
        "&source_bottom_right, const QList<int> &roles)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def containRoleForRecursiveFilter(*__, **_) -> Never:
    """
    Qt's 'bool
    QQmlSortFilterProxyModelPrivate::containRoleForRecursiveFilter(const
    QList<int> &roles) const': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQmlSortFilterProxyModelPrivate.containRoleForRecursiveFilter' "
        "has no cute function yet. Qt's 'bool "
        "QQmlSortFilterProxyModelPrivate::containRoleForRecursiveFilter(cons"
        "t QList<int> &roles) const': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def init(*__, **_) -> Never:
    """
    Qt's 'void QQmlSortFilterProxyModelPrivate::init()': leans on
    'QQmlSorterCompositor::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlSortFilterProxyModelPrivate.init' has no cute function yet. "
        "Qt's 'void QQmlSortFilterProxyModelPrivate::init()': leans on "
        "'QQmlSorterCompositor::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def needsReorder(*__, **_) -> Never:
    """
    Qt's 'bool QQmlSortFilterProxyModelPrivate::needsReorder(const QList<int>
    &source_rows, const QModelIndex &source_parent) const': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlSortFilterProxyModelPrivate.needsReorder' has no cute "
        "function yet. Qt's 'bool "
        "QQmlSortFilterProxyModelPrivate::needsReorder(const QList<int> "
        "&source_rows, const QModelIndex &source_parent) const': takes a "
        "type Python has no way to hand over yet.")
