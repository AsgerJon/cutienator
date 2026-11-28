"""
QQmlSortFilterProxyModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmlsortfilterproxymodel_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlSortFilterProxyModel to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QAbstractItemModel, QAbstractProxyModel, QHash
from ..QtCore import QObject
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QItemSelection, QMetaObject, QModelIndex
  from ..QtCore import QVariant
  from . import QQmlSortFilterProxyModelPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QItemSelection = WAIT['QItemSelection']
  QModelIndex = WAIT['QModelIndex']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlSortFilterProxyModel(QAbstractProxyModel, QQmlParserStatus):
  """
  The cute side of Qt's QQmlSortFilterProxyModel: a plain Python object
  standing in front of one C++ QQmlSortFilterProxyModel.

  It is built on the cute 'QAbstractProxyModel', as Qt's
  QQmlSortFilterProxyModel is built on Qt's QAbstractProxyModel, and has
  everything that class has. It is built on the cute 'QQmlParserStatus' as
  well, as Qt's QQmlSortFilterProxyModel is built on Qt's QQmlParserStatus
  too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlSortFilterProxyModel that has a ritual and that
  Python can call so far, 51 names in all: 'metaObject', 'tr', 'model',
  'setModel', 'dynamicSortFilter', 'setDynamicSortFilter',
  'recursiveFiltering', 'setRecursiveFiltering', 'autoAcceptChildRows',
  'setAutoAcceptChildRows', 'invalidate', 'invalidateSorter', 'mapToSource',
  'mapFromSource', 'index', 'parent', 'sibling', 'hasChildren',
  'columnCount', 'rowCount', 'data', 'setData', 'headerData',
  'setHeaderData', 'insertRows', 'insertColumns', 'removeRows',
  'removeColumns', 'mapSelectionToSource', 'mapSelectionFromSource',
  'setSourceModel', 'setPrimarySortColumn', 'sourceData', 'roleNames',
  'itemRoleForName', 'compareData', 'filterAcceptsRow',
  'filterAcceptsColumn', 'lessThan', 'sort', 'classBegin',
  'componentComplete', 'invalidateFilter', 'dynamicSortFilterChanged',
  'recursiveFilteringChanged', 'autoAcceptChildRowsChanged',
  'filtersChanged', 'sortersChanged', 'modelChanged', 'primarySorterChanged',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlSortFilterProxyModel::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQmlSortFilterProxyModel::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlSortFilterProxyModel::~QQmlSortFilterProxyModel()': the
    destructor: Python never removes a C++ QQmlSortFilterProxyModel.
  - Qt's 'QQmlListProperty<QQmlFilterBase>
    QQmlSortFilterProxyModel::filters()': gives a type Python has no way to
    take yet.
  - Qt's 'QQmlListProperty<QQmlSorterBase>
    QQmlSortFilterProxyModel::sorters()': gives a type Python has no way to
    take yet.
  - Qt's 'void QQmlSortFilterProxyModel::setPrimarySorter(QQmlSorterBase
    *sorter)': names 'QQmlSorterBase', which has no cute class yet.
  - Qt's 'void QQmlSortFilterProxyModel::setPrimarySortOrder(const
    Qt::SortOrder sortOrder)': takes a type Python has no way to hand over
    yet.
  - Qt's 'const QQmlSortFilterProxyModelPrivate
    *QQmlSortFilterProxyModel::d_func() const': takes in Python what
    'QQmlSortFilterProxyModelPrivate *QQmlSortFilterProxyModel::d_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 64 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQmlSortFilterProxyModel is created at the first use, not by
    'QQmlSortFilterProxyModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlSortFilterProxyModel.
  - Qt tells when it has removed the C++ QQmlSortFilterProxyModel. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlSortFilterProxyModel that has no cute function yet,
    'filters', 'setPrimarySortOrder', 'setPrimarySorter', 'sorters', holds a
    function that raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QQmlSortFilterProxyModel::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#tr

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
    #  QString QQmlSortFilterProxyModel::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QQmlSortFilterProxyModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSortFilterProxyModel'

  #  Qt's QQmlSortFilterProxyModel is built on more than one class. The part
  #  of a C++ QQmlSortFilterProxyModel that belongs to a class after the
  #  first begins somewhere inside the object, and the ritual named for that
  #  class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus':
          'ritual_cast_QQmlSortFilterProxyModel_QQmlParserStatus',
  }

  #  A C++ QQmlSortFilterProxyModel Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlSortFilterProxyModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlSortFilterProxyModel::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlSortFilterProxyModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QQmlSortFilterProxyModel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def dynamicSortFilter(self) -> bool:
    """
    Calls Qt's 'bool QQmlSortFilterProxyModel::dynamicSortFilter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#dynamicSortFilter
    """
    #  bool QQmlSortFilterProxyModel::dynamicSortFilter() const
    return self.uglySide.call(
        'ritual_ZNK24QQmlSortFilterProxyModel17dynamicSortFilterEv',
    )

  def recursiveFiltering(self) -> bool:
    """
    Calls Qt's 'bool QQmlSortFilterProxyModel::recursiveFiltering() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#recursiveFiltering
    """
    #  bool QQmlSortFilterProxyModel::recursiveFiltering() const
    return self.uglySide.call(
        'ritual_ZNK24QQmlSortFilterProxyModel18recursiveFilteringEv',
    )

  def autoAcceptChildRows(self) -> bool:
    """
    Calls Qt's 'bool QQmlSortFilterProxyModel::autoAcceptChildRows() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#autoAcceptChildRows
    """
    #  bool QQmlSortFilterProxyModel::autoAcceptChildRows() const
    return self.uglySide.call(
        'ritual_ZNK24QQmlSortFilterProxyModel19autoAcceptChildRowsEv',
    )

  @overload(QModelIndex)
  def mapToSource(self, proxyIndex: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QQmlSortFilterProxyModel::mapToSource(const
    QModelIndex &proxyIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#mapToSource

    Parameters
    ----------

    proxyIndex : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QQmlSortFilterProxyModel::mapToSource(const QModelIndex
    #      &proxyIndex) const
    ritual = (
        'ritual_ZNK24QQmlSortFilterProxyModel11mapToSourceERK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QQmlSortFilterProxyModel11mapToSourceERK11QModel'
          'Index')
    address = self.uglySide.call(ritual, self._valueOf(proxyIndex))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def mapFromSource(self, sourceIndex: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QQmlSortFilterProxyModel::mapFromSource(const
    QModelIndex &sourceIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#mapFromSource

    Parameters
    ----------

    sourceIndex : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QQmlSortFilterProxyModel::mapFromSource(const QModelIndex
    #      &sourceIndex) const
    ritual = (
        'ritual_ZNK24QQmlSortFilterProxyModel13mapFromSourceERK11QModelInde'
        'x')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QQmlSortFilterProxyModel13mapFromSourceERK11QMod'
          'elIndex')
    address = self.uglySide.call(ritual, self._valueOf(sourceIndex))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def index(
      self,
      row: int,
      column: int,
      parent: Optional[QModelIndex] = None,
  ) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QQmlSortFilterProxyModel::index(int row, int
    column, const QModelIndex &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#index

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QQmlSortFilterProxyModel::index(int row, int column, const
    #      QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK24QQmlSortFilterProxyModel5indexEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QQmlSortFilterProxyModel5indexEiiRK11QModelIndex')
    address = self.uglySide.call(ritual, row, column, self._valueOf(parent))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def parent(self, child: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QQmlSortFilterProxyModel::parent(const
    QModelIndex &child) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#parent

    Parameters
    ----------

    child : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QQmlSortFilterProxyModel::parent(const QModelIndex &child)
    #      const
    ritual = 'ritual_ZNK24QQmlSortFilterProxyModel6parentERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QQmlSortFilterProxyModel6parentERK11QModelIndex')
    address = self.uglySide.call(ritual, self._valueOf(child))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(int, int, QModelIndex)
  def sibling(self, row: int, column: int, idx: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QQmlSortFilterProxyModel::sibling(int row, int
    column, const QModelIndex &idx) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#sibling

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    idx : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QQmlSortFilterProxyModel::sibling(int row, int column,
    #      const QModelIndex &idx) const
    ritual = 'ritual_ZNK24QQmlSortFilterProxyModel7siblingEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QQmlSortFilterProxyModel7siblingEiiRK11QModelInd'
          'ex')
    address = self.uglySide.call(ritual, row, column, self._valueOf(idx))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload()
  @overload(QModelIndex)
  def hasChildren(self, parent: Optional[QModelIndex] = None) -> bool:
    """
    Calls Qt's 'bool QQmlSortFilterProxyModel::hasChildren(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#hasChildren

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QQmlSortFilterProxyModel::hasChildren(const QModelIndex &parent)
    #      const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = (
        'ritual_ZNK24QQmlSortFilterProxyModel11hasChildrenERK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QQmlSortFilterProxyModel11hasChildrenERK11QModel'
          'Index')
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload()
  @overload(QModelIndex)
  def columnCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QQmlSortFilterProxyModel::columnCount(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#columnCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QQmlSortFilterProxyModel::columnCount(const QModelIndex &parent)
    #      const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = (
        'ritual_ZNK24QQmlSortFilterProxyModel11columnCountERK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QQmlSortFilterProxyModel11columnCountERK11QModel'
          'Index')
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload()
  @overload(QModelIndex)
  def rowCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QQmlSortFilterProxyModel::rowCount(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#rowCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QQmlSortFilterProxyModel::rowCount(const QModelIndex &parent)
    #      const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK24QQmlSortFilterProxyModel8rowCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QQmlSortFilterProxyModel8rowCountERK11QModelInde'
          'x')
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload(QModelIndex)
  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int = 0) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlSortFilterProxyModel::data(const QModelIndex
    &index, int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#data

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlSortFilterProxyModel::data(const QModelIndex &index, int
    #      role) const
    ritual = 'ritual_ZNK24QQmlSortFilterProxyModel4dataERK11QModelIndexi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QQmlSortFilterProxyModel4dataERK11QModelIndexi')
    address = self.uglySide.call(ritual, self._valueOf(index), role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int, Qt.Orientation)
  @overload(int, Qt.Orientation, int)
  def headerData(
      self,
      section: int,
      orientation: Qt.Orientation,
      role: int = 0,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlSortFilterProxyModel::headerData(int section,
    Qt::Orientation orientation, int role) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#headerData

    Parameters
    ----------

    section : int
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number.

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlSortFilterProxyModel::headerData(int section,
    #      Qt::Orientation orientation, int role) const
    ritual = (
        'ritual_ZNK24QQmlSortFilterProxyModel10headerDataEiN2Qt11Orientatio'
        'nEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QQmlSortFilterProxyModel10headerDataEiN2Qt11Orie'
          'ntationEi')
    address = self.uglySide.call(ritual, section, orientation.value, role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QItemSelection)
  def mapSelectionToSource(
      self,
      proxySelection: QItemSelection,
  ) -> QItemSelection:
    """
    Calls Qt's 'QItemSelection
    QQmlSortFilterProxyModel::mapSelectionToSource(const QItemSelection
    &proxySelection) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#mapSelectionToSource

    Parameters
    ----------

    proxySelection : QItemSelection
      Passed on as a value: Qt reads the C++ QItemSelection, which stays
      Python's own.

    Returns
    -------

    QItemSelection
      A new cute QItemSelection around the copy Qt gave back. Python owns it.
    """
    #  QItemSelection QQmlSortFilterProxyModel::mapSelectionToSource(const
    #      QItemSelection &proxySelection) const
    ritual = (
        'ritual_ZNK24QQmlSortFilterProxyModel20mapSelectionToSourceERK14QIt'
        'emSelection')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QQmlSortFilterProxyModel20mapSelectionToSourceER'
          'K14QItemSelection')
    address = self.uglySide.call(ritual, self._valueOf(proxySelection))
    from ..QtCore import QItemSelection
    return QItemSelection._cuteOwning(address)

  @overload(QItemSelection)
  def mapSelectionFromSource(
      self,
      sourceSelection: QItemSelection,
  ) -> QItemSelection:
    """
    Calls Qt's 'QItemSelection
    QQmlSortFilterProxyModel::mapSelectionFromSource(const QItemSelection
    &sourceSelection) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html

    Parameters
    ----------

    sourceSelection : QItemSelection
      Passed on as a value: Qt reads the C++ QItemSelection, which stays
      Python's own.

    Returns
    -------

    QItemSelection
      A new cute QItemSelection around the copy Qt gave back. Python owns it.
    """
    #  QItemSelection QQmlSortFilterProxyModel::mapSelectionFromSource(const
    #      QItemSelection &sourceSelection) const
    ritual = (
        'ritual_ZNK24QQmlSortFilterProxyModel22mapSelectionFromSourceERK14Q'
        'ItemSelection')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QQmlSortFilterProxyModel22mapSelectionFromSource'
          'ERK14QItemSelection')
    address = self.uglySide.call(ritual, self._valueOf(sourceSelection))
    from ..QtCore import QItemSelection
    return QItemSelection._cuteOwning(address)

  @overload(QModelIndex, int)
  def sourceData(self, sourceIndex: QModelIndex, role: int) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlSortFilterProxyModel::sourceData(const
    QModelIndex &sourceIndex, int role) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#sourceData

    Parameters
    ----------

    sourceIndex : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    role : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlSortFilterProxyModel::sourceData(const QModelIndex
    #      &sourceIndex, int role) const
    address = self.uglySide.call(
        'ritual_ZNK24QQmlSortFilterProxyModel10sourceDataERK11QModelIndexi',
        self._valueOf(sourceIndex), role,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def roleNames(self) -> QHash[int, QByteArray]:
    """
    Calls Qt's 'QHash<int, QByteArray> QQmlSortFilterProxyModel::roleNames()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#roleNames

    Returns
    -------

    QHash[int, QByteArray]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<int, QByteArray> QQmlSortFilterProxyModel::roleNames() const
    address = self.uglySide.call(
        'ritual_ZNK24QQmlSortFilterProxyModel9roleNamesEv',
    )
    from ..QtCore import QByteArray
    return QHash[int, QByteArray]._cuteOwning(address)

  @overload(str)
  def itemRoleForName(self, roleName: str) -> int:
    """
    Calls Qt's 'int QQmlSortFilterProxyModel::itemRoleForName(const QString
    &roleName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#itemRoleForName

    Parameters
    ----------

    roleName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QQmlSortFilterProxyModel::itemRoleForName(const QString &roleName)
    #      const
    return self.uglySide.call(
        'ritual_ZNK24QQmlSortFilterProxyModel15itemRoleForNameERK7QString',
        roleName,
    )

  @overload(int, QModelIndex)
  def filterAcceptsRow(
      self,
      sourceRow: int,
      sourceParent: QModelIndex,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlSortFilterProxyModel::filterAcceptsRow(int
    sourceRow, const QModelIndex &sourceParent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#filterAcceptsRow

    Parameters
    ----------

    sourceRow : int
      Passed on as it is.

    sourceParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QQmlSortFilterProxyModel::filterAcceptsRow(int sourceRow, const
    #      QModelIndex &sourceParent) const
    return self.uglySide.call(
        'ritual_ZNK24QQmlSortFilterProxyModel16filterAcceptsRowEiRK11QModel'
        'Index',
        sourceRow, self._valueOf(sourceParent),
    )

  @overload(int, QModelIndex)
  def filterAcceptsColumn(
      self,
      sourceColumn: int,
      sourceParent: QModelIndex,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlSortFilterProxyModel::filterAcceptsColumn(int
    sourceColumn, const QModelIndex &sourceParent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#filterAcceptsColumn

    Parameters
    ----------

    sourceColumn : int
      Passed on as it is.

    sourceParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QQmlSortFilterProxyModel::filterAcceptsColumn(int sourceColumn,
    #      const QModelIndex &sourceParent) const
    return self.uglySide.call(
        'ritual_ZNK24QQmlSortFilterProxyModel19filterAcceptsColumnEiRK11QMo'
        'delIndex',
        sourceColumn, self._valueOf(sourceParent),
    )

  @overload(QModelIndex, QModelIndex)
  def lessThan(
      self,
      sourceLeft: QModelIndex,
      sourceRight: QModelIndex,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlSortFilterProxyModel::lessThan(const QModelIndex
    &sourceLeft, const QModelIndex &sourceRight) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#lessThan

    Parameters
    ----------

    sourceLeft : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    sourceRight : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QQmlSortFilterProxyModel::lessThan(const QModelIndex &sourceLeft,
    #      const QModelIndex &sourceRight) const
    return self.uglySide.call(
        'ritual_ZNK24QQmlSortFilterProxyModel8lessThanERK11QModelIndexS2_',
        self._valueOf(sourceLeft), self._valueOf(sourceRight),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setModel(self, model: Optional[QAbstractItemModel]) -> None:
    """
    Calls Qt's 'void QQmlSortFilterProxyModel::setModel(QAbstractItemModel
    *model)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#setModel

    Parameters
    ----------

    model : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlSortFilterProxyModel::setModel(QAbstractItemModel *model)
    self.uglySide.call(
        'ritual_ZN24QQmlSortFilterProxyModel8setModelEP18QAbstractItemModel',
        self._addressOf(model),
    )

  @overload(bool)
  def setDynamicSortFilter(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQmlSortFilterProxyModel::setDynamicSortFilter(const
    bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#setDynamicSortFilter

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQmlSortFilterProxyModel::setDynamicSortFilter(const bool
    #      enabled)
    self.uglySide.call(
        'ritual_ZN24QQmlSortFilterProxyModel20setDynamicSortFilterEb',
        enabled,
    )

  @overload(bool)
  def setRecursiveFiltering(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQmlSortFilterProxyModel::setRecursiveFiltering(const
    bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQmlSortFilterProxyModel::setRecursiveFiltering(const bool
    #      enabled)
    self.uglySide.call(
        'ritual_ZN24QQmlSortFilterProxyModel21setRecursiveFilteringEb',
        enabled,
    )

  @overload(bool)
  def setAutoAcceptChildRows(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQmlSortFilterProxyModel::setAutoAcceptChildRows(const
    bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQmlSortFilterProxyModel::setAutoAcceptChildRows(const bool
    #      enabled)
    self.uglySide.call(
        'ritual_ZN24QQmlSortFilterProxyModel22setAutoAcceptChildRowsEb',
        enabled,
    )

  @overload(QModelIndex, QVariant)
  @overload(QModelIndex, QVariant, int)
  def setData(
      self,
      index: QModelIndex,
      value: QVariant,
      role: int = 2,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlSortFilterProxyModel::setData(const QModelIndex
    &index, const QVariant &value, int role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#setData

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 2.
    """
    #  bool QQmlSortFilterProxyModel::setData(const QModelIndex &index, const
    #      QVariant &value, int role)
    ritual = (
        'ritual_ZN24QQmlSortFilterProxyModel7setDataERK11QModelIndexRK8QVar'
        'ianti')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQmlSortFilterProxyModel7setDataERK11QModelIndexR'
          'K8QVarianti')
    return self.uglySide.call(
        ritual, self._valueOf(index), self._valueOf(value), role,
    )

  @overload(int, Qt.Orientation, QVariant)
  @overload(int, Qt.Orientation, QVariant, int)
  def setHeaderData(
      self,
      section: int,
      orientation: Qt.Orientation,
      value: QVariant,
      role: int = 2,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlSortFilterProxyModel::setHeaderData(int section,
    Qt::Orientation orientation, const QVariant &value, int role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#setHeaderData

    Parameters
    ----------

    section : int
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 2.
    """
    #  bool QQmlSortFilterProxyModel::setHeaderData(int section,
    #      Qt::Orientation orientation, const QVariant &value, int role)
    ritual = (
        'ritual_ZN24QQmlSortFilterProxyModel13setHeaderDataEiN2Qt11Orientat'
        'ionERK8QVarianti')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQmlSortFilterProxyModel13setHeaderDataEiN2Qt11Or'
          'ientationERK8QVarianti')
    return self.uglySide.call(
        ritual, section, orientation.value, self._valueOf(value), role,
    )

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setSourceModel(
      self,
      sourceModel: Optional[QAbstractItemModel],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlSortFilterProxyModel::setSourceModel(QAbstractItemModel
    *sourceModel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#setSourceModel

    Parameters
    ----------

    sourceModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlSortFilterProxyModel::setSourceModel(QAbstractItemModel
    #      *sourceModel)
    ritual = (
        'ritual_ZN24QQmlSortFilterProxyModel14setSourceModelEP18QAbstractIt'
        'emModel')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQmlSortFilterProxyModel14setSourceModelEP18QAbst'
          'ractItemModel')
    self.uglySide.call(ritual, self._addressOf(sourceModel))

  @overload(int)
  def setPrimarySortColumn(self, column: int) -> None:
    """
    Calls Qt's 'void QQmlSortFilterProxyModel::setPrimarySortColumn(const int
    column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#setPrimarySortColumn

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  void QQmlSortFilterProxyModel::setPrimarySortColumn(const int column)
    self.uglySide.call(
        'ritual_ZN24QQmlSortFilterProxyModel20setPrimarySortColumnEi',
        column,
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQmlSortFilterProxyModel::QQmlSortFilterProxyModel(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlSortFilterProxyModel::QQmlSortFilterProxyModel(QObject *parent)
    self._noteCreation(QQmlSortFilterProxyModel, lambda: Rituals.call(
        'ritual_ZN24QQmlSortFilterProxyModelC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def model(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel *QQmlSortFilterProxyModel::model()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#model

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *QQmlSortFilterProxyModel::model()
    address = self.uglySide.call(
        'ritual_ZN24QQmlSortFilterProxyModel5modelEv',
    )
    return QAbstractItemModel._cuteAt(address)

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QQmlSortFilterProxyModel::invalidate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#invalidate
    """
    #  void QQmlSortFilterProxyModel::invalidate()
    self.uglySide.call('ritual_ZN24QQmlSortFilterProxyModel10invalidateEv')

  def invalidateSorter(self) -> None:
    """
    Calls Qt's 'void QQmlSortFilterProxyModel::invalidateSorter()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#invalidateSorter
    """
    #  void QQmlSortFilterProxyModel::invalidateSorter()
    self.uglySide.call(
        'ritual_ZN24QQmlSortFilterProxyModel16invalidateSorterEv',
    )

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def insertRows(
      self,
      row: int,
      count: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlSortFilterProxyModel::insertRows(int row, int count,
    const QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#insertRows

    Parameters
    ----------

    row : int
      Passed on as it is.

    count : int
      Passed on as it is.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QQmlSortFilterProxyModel::insertRows(int row, int count, const
    #      QModelIndex &parent)
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = (
        'ritual_ZN24QQmlSortFilterProxyModel10insertRowsEiiRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQmlSortFilterProxyModel10insertRowsEiiRK11QModel'
          'Index')
    return self.uglySide.call(ritual, row, count, self._valueOf(parent))

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def insertColumns(
      self,
      column: int,
      count: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlSortFilterProxyModel::insertColumns(int column, int
    count, const QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#insertColumns

    Parameters
    ----------

    column : int
      Passed on as it is.

    count : int
      Passed on as it is.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QQmlSortFilterProxyModel::insertColumns(int column, int count,
    #      const QModelIndex &parent)
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = (
        'ritual_ZN24QQmlSortFilterProxyModel13insertColumnsEiiRK11QModelInd'
        'ex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQmlSortFilterProxyModel13insertColumnsEiiRK11QMo'
          'delIndex')
    return self.uglySide.call(ritual, column, count, self._valueOf(parent))

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def removeRows(
      self,
      row: int,
      count: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlSortFilterProxyModel::removeRows(int row, int count,
    const QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#removeRows

    Parameters
    ----------

    row : int
      Passed on as it is.

    count : int
      Passed on as it is.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QQmlSortFilterProxyModel::removeRows(int row, int count, const
    #      QModelIndex &parent)
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = (
        'ritual_ZN24QQmlSortFilterProxyModel10removeRowsEiiRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQmlSortFilterProxyModel10removeRowsEiiRK11QModel'
          'Index')
    return self.uglySide.call(ritual, row, count, self._valueOf(parent))

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def removeColumns(
      self,
      column: int,
      count: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlSortFilterProxyModel::removeColumns(int column, int
    count, const QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#removeColumns

    Parameters
    ----------

    column : int
      Passed on as it is.

    count : int
      Passed on as it is.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QQmlSortFilterProxyModel::removeColumns(int column, int count,
    #      const QModelIndex &parent)
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = (
        'ritual_ZN24QQmlSortFilterProxyModel13removeColumnsEiiRK11QModelInd'
        'ex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQmlSortFilterProxyModel13removeColumnsEiiRK11QMo'
          'delIndex')
    return self.uglySide.call(ritual, column, count, self._valueOf(parent))

  @overload(QVariant, QVariant)
  def compareData(self, lhs: QVariant, rhs: QVariant) -> Qt.weak_ordering:
    """
    Calls Qt's 'Qt::weak_ordering QQmlSortFilterProxyModel::compareData(const
    QVariant &lhs, const QVariant &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#compareData

    Parameters
    ----------

    lhs : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    rhs : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    Qt.weak_ordering
      A new cute Qt::weak_ordering around the copy Qt gave back. Python owns
      it.
    """
    #  Qt::weak_ordering QQmlSortFilterProxyModel::compareData(const QVariant
    #      &lhs, const QVariant &rhs)
    address = self.uglySide.call(
        'ritual_ZN24QQmlSortFilterProxyModel11compareDataERK8QVariantS2_',
        self._valueOf(lhs), self._valueOf(rhs),
    )
    return Qt.weak_ordering._cuteOwning(address)

  @overload()
  @overload(int)
  @overload(int, Qt.SortOrder)
  def sort(
      self,
      column: int = 0,
      sortOrder: Qt.SortOrder = Qt.SortOrder.AscendingOrder,
  ) -> None:
    """
    Calls Qt's 'void QQmlSortFilterProxyModel::sort(int column, Qt::SortOrder
    sortOrder)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#sort

    Parameters
    ----------

    column : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    sortOrder : Qt.SortOrder
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.SortOrder.AscendingOrder.
    """
    #  void QQmlSortFilterProxyModel::sort(int column, Qt::SortOrder
    #      sortOrder)
    ritual = 'ritual_ZN24QQmlSortFilterProxyModel4sortEiN2Qt9SortOrderE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQmlSortFilterProxyModel4sortEiN2Qt9SortOrderE')
    self.uglySide.call(ritual, column, sortOrder.value)

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQmlSortFilterProxyModel::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#classBegin
    """
    #  void QQmlSortFilterProxyModel::classBegin()
    ritual = 'ritual_ZN24QQmlSortFilterProxyModel10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QQmlSortFilterProxyModel10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQmlSortFilterProxyModel::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#componentComplete
    """
    #  void QQmlSortFilterProxyModel::componentComplete()
    ritual = 'ritual_ZN24QQmlSortFilterProxyModel17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QQmlSortFilterProxyModel17componentCompleteEv'
    self.uglySide.call(ritual)

  def invalidateFilter(self) -> None:
    """
    Calls Qt's 'void QQmlSortFilterProxyModel::invalidateFilter()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#invalidateFilter
    """
    #  void QQmlSortFilterProxyModel::invalidateFilter()
    self.uglySide.call(
        'ritual_ZN24QQmlSortFilterProxyModel16invalidateFilterEv',
    )

  def dynamicSortFilterChanged(self) -> None:
    """
    Calls Qt's 'void QQmlSortFilterProxyModel::dynamicSortFilterChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html
    """
    #  void QQmlSortFilterProxyModel::dynamicSortFilterChanged()
    self.uglySide.call(
        'ritual_ZN24QQmlSortFilterProxyModel24dynamicSortFilterChangedEv',
    )

  def recursiveFilteringChanged(self) -> None:
    """
    Calls Qt's 'void QQmlSortFilterProxyModel::recursiveFilteringChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html
    """
    #  void QQmlSortFilterProxyModel::recursiveFilteringChanged()
    self.uglySide.call(
        'ritual_ZN24QQmlSortFilterProxyModel25recursiveFilteringChangedEv',
    )

  def autoAcceptChildRowsChanged(self) -> None:
    """
    Calls Qt's 'void QQmlSortFilterProxyModel::autoAcceptChildRowsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html
    """
    #  void QQmlSortFilterProxyModel::autoAcceptChildRowsChanged()
    self.uglySide.call(
        'ritual_ZN24QQmlSortFilterProxyModel26autoAcceptChildRowsChangedEv',
    )

  def filtersChanged(self) -> None:
    """
    Calls Qt's 'void QQmlSortFilterProxyModel::filtersChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#filtersChanged
    """
    #  void QQmlSortFilterProxyModel::filtersChanged()
    self.uglySide.call(
        'ritual_ZN24QQmlSortFilterProxyModel14filtersChangedEv',
    )

  def sortersChanged(self) -> None:
    """
    Calls Qt's 'void QQmlSortFilterProxyModel::sortersChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#sortersChanged
    """
    #  void QQmlSortFilterProxyModel::sortersChanged()
    self.uglySide.call(
        'ritual_ZN24QQmlSortFilterProxyModel14sortersChangedEv',
    )

  def modelChanged(self) -> None:
    """
    Calls Qt's 'void QQmlSortFilterProxyModel::modelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#modelChanged
    """
    #  void QQmlSortFilterProxyModel::modelChanged()
    self.uglySide.call('ritual_ZN24QQmlSortFilterProxyModel12modelChangedEv')

  def primarySorterChanged(self) -> None:
    """
    Calls Qt's 'void QQmlSortFilterProxyModel::primarySorterChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#primarySorterChanged
    """
    #  void QQmlSortFilterProxyModel::primarySorterChanged()
    self.uglySide.call(
        'ritual_ZN24QQmlSortFilterProxyModel20primarySorterChangedEv',
    )

  def d_func(self) -> Optional[QQmlSortFilterProxyModelPrivate]:
    """
    Calls Qt's 'QQmlSortFilterProxyModelPrivate
    *QQmlSortFilterProxyModel::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodel.html#d_func

    Returns
    -------

    Optional[QQmlSortFilterProxyModelPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlSortFilterProxyModelPrivate *QQmlSortFilterProxyModel::d_func()
    address = self.uglySide.call(
        'ritual_ZN24QQmlSortFilterProxyModel6d_funcEv',
    )
    from . import QQmlSortFilterProxyModelPrivate
    return QQmlSortFilterProxyModelPrivate._cuteAt(address)

  @staticmethod
  def filters(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQmlFilterBase>
    QQmlSortFilterProxyModel::filters()': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QQmlSortFilterProxyModel.filters' has no cute function yet. Qt's "
        "'QQmlListProperty<QQmlFilterBase> "
        "QQmlSortFilterProxyModel::filters()': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def setPrimarySortOrder(*__, **_) -> Never:
    """
    Qt's 'void QQmlSortFilterProxyModel::setPrimarySortOrder(const
    Qt::SortOrder sortOrder)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQmlSortFilterProxyModel.setPrimarySortOrder' has no cute "
        "function yet. Qt's 'void "
        "QQmlSortFilterProxyModel::setPrimarySortOrder(const Qt::SortOrder "
        "sortOrder)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setPrimarySorter(*__, **_) -> Never:
    """
    Qt's 'void QQmlSortFilterProxyModel::setPrimarySorter(QQmlSorterBase
    *sorter)': names 'QQmlSorterBase', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlSortFilterProxyModel.setPrimarySorter' has no cute function "
        "yet. Qt's 'void "
        "QQmlSortFilterProxyModel::setPrimarySorter(QQmlSorterBase "
        "*sorter)': names 'QQmlSorterBase', which has no cute class yet.")

  @staticmethod
  def sorters(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQmlSorterBase>
    QQmlSortFilterProxyModel::sorters()': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QQmlSortFilterProxyModel.sorters' has no cute function yet. Qt's "
        "'QQmlListProperty<QQmlSorterBase> "
        "QQmlSortFilterProxyModel::sorters()': gives a type Python has no "
        "way to take yet.")
