"""
QSortFilterProxyModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qsortfilterproxymodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from . import Qt, QAbstractItemModel, QAbstractProxyModel, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QItemSelection, QMetaObject, QMimeData, QModelIndex
  from . import QRegularExpression, QSize, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QItemSelection = WAIT['QItemSelection']
  QMimeData = WAIT['QMimeData']
  QModelIndex = WAIT['QModelIndex']
  QRegularExpression = WAIT['QRegularExpression']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSortFilterProxyModel(QAbstractProxyModel):
  """
  The cute side of Qt's QSortFilterProxyModel: a plain Python object standing
  in front of one C++ QSortFilterProxyModel.

  It is built on the cute 'QAbstractProxyModel', as Qt's
  QSortFilterProxyModel is built on Qt's QAbstractProxyModel, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QSortFilterProxyModel that has a ritual and that
  Python can call so far, 54 names in all: 'metaObject', 'tr',
  'setSourceModel', 'mapToSource', 'mapFromSource', 'mapSelectionToSource',
  'mapSelectionFromSource', 'filterRegularExpression', 'filterKeyColumn',
  'setFilterKeyColumn', 'filterCaseSensitivity', 'setFilterCaseSensitivity',
  'sortCaseSensitivity', 'setSortCaseSensitivity', 'isSortLocaleAware',
  'setSortLocaleAware', 'sortColumn', 'sortOrder', 'dynamicSortFilter',
  'setDynamicSortFilter', 'sortRole', 'setSortRole', 'filterRole',
  'setFilterRole', 'isRecursiveFilteringEnabled',
  'setRecursiveFilteringEnabled', 'autoAcceptChildRows',
  'setAutoAcceptChildRows', 'setFilterRegularExpression',
  'setFilterWildcard', 'setFilterFixedString', 'invalidate', 'index',
  'parent', 'sibling', 'rowCount', 'columnCount', 'hasChildren', 'data',
  'setData', 'headerData', 'setHeaderData', 'dropMimeData', 'insertRows',
  'insertColumns', 'removeRows', 'removeColumns', 'fetchMore',
  'canFetchMore', 'flags', 'buddy', 'span', 'sort', 'supportedDropActions'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSortFilterProxyModel::~QSortFilterProxyModel()': the destructor:
    Python never removes a C++ QSortFilterProxyModel.

  What has no ritual
  ------------------

  38 of the 95 functions Qt declares: 15 takes or gives a type that cannot be
  passed yet; 9 protected; 8 a signal; 3 private; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QSortFilterProxyModel is created at the first use, not by
    'QSortFilterProxyModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSortFilterProxyModel.
  - Qt tells when it has removed the C++ QSortFilterProxyModel. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QSortFilterProxyModel, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class DataChangeRelevanceFlag(CuteFlags, scoped=True):
    """
    The flags enum 'QSortFilterProxyModel::DataChangeRelevanceFlag' of Qt,
    with the 4 names Qt gives in it. Qt names the type of its combinations
    'QSortFilterProxyModel::DataChangeRelevanceFlags'. C++ keeps these names
    inside the enum, so the class that holds the enum does not have them.
    """

    NotRelevant = 0x0
    RelevantForFiltering = 0x1
    RelevantForSorting = 0x2
    RelevantForFilteringAndSorting = 0x3

  DataChangeRelevanceFlags = DataChangeRelevanceFlag

  class Direction(CuteFlags, scoped=True):
    """
    The flags enum 'QSortFilterProxyModel::Direction' of Qt, with the 3 names
    Qt gives in it. Qt names the type of its combinations
    'QSortFilterProxyModel::Directions'. C++ keeps these names inside the
    enum, so the class that holds the enum does not have them.
    """

    Rows = 0x1
    Columns = 0x2
    Both = 0x3

  Directions = Direction

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
    Calls Qt's 'QString QSortFilterProxyModel::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsortfilterproxymodel.html#tr

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
    #  QString QSortFilterProxyModel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QSortFilterProxyModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSortFilterProxyModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSortFilterProxyModel::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSortFilterProxyModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QSortFilterProxyModel10metaObjectEv',
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QModelIndex)
  def mapToSource(self, proxyIndex: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QSortFilterProxyModel::mapToSource(const
    QModelIndex &proxyIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#mapToSource

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
    #  QModelIndex QSortFilterProxyModel::mapToSource(const QModelIndex
    #      &proxyIndex) const
    address = self.uglySide.call(
        'ritual_ZNK21QSortFilterProxyModel11mapToSourceERK11QModelIndex',
        self._valueOf(proxyIndex),
    )
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def mapFromSource(self, sourceIndex: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QSortFilterProxyModel::mapFromSource(const
    QModelIndex &sourceIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#mapFromSource

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
    #  QModelIndex QSortFilterProxyModel::mapFromSource(const QModelIndex
    #      &sourceIndex) const
    address = self.uglySide.call(
        'ritual_ZNK21QSortFilterProxyModel13mapFromSourceERK11QModelIndex',
        self._valueOf(sourceIndex),
    )
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QItemSelection)
  def mapSelectionToSource(
      self,
      proxySelection: QItemSelection,
  ) -> QItemSelection:
    """
    Calls Qt's 'QItemSelection
    QSortFilterProxyModel::mapSelectionToSource(const QItemSelection
    &proxySelection) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#mapSelectionToSource

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
    #  QItemSelection QSortFilterProxyModel::mapSelectionToSource(const
    #      QItemSelection &proxySelection) const
    address = self.uglySide.call(
        'ritual_ZNK21QSortFilterProxyModel20mapSelectionToSourceERK14QItemS'
        'election',
        self._valueOf(proxySelection),
    )
    from . import QItemSelection
    return QItemSelection._cuteOwning(address)

  @overload(QItemSelection)
  def mapSelectionFromSource(
      self,
      sourceSelection: QItemSelection,
  ) -> QItemSelection:
    """
    Calls Qt's 'QItemSelection
    QSortFilterProxyModel::mapSelectionFromSource(const QItemSelection
    &sourceSelection) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#mapSelectionFromSource

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
    #  QItemSelection QSortFilterProxyModel::mapSelectionFromSource(const
    #      QItemSelection &sourceSelection) const
    address = self.uglySide.call(
        'ritual_ZNK21QSortFilterProxyModel22mapSelectionFromSourceERK14QIte'
        'mSelection',
        self._valueOf(sourceSelection),
    )
    from . import QItemSelection
    return QItemSelection._cuteOwning(address)

  def filterRegularExpression(self) -> QRegularExpression:
    """
    Calls Qt's 'QRegularExpression
    QSortFilterProxyModel::filterRegularExpression() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterRegularExpression

    Returns
    -------

    QRegularExpression
      A new cute QRegularExpression around the copy Qt gave back. Python owns
      it.
    """
    #  QRegularExpression QSortFilterProxyModel::filterRegularExpression()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK21QSortFilterProxyModel23filterRegularExpressionEv',
    )
    from . import QRegularExpression
    return QRegularExpression._cuteOwning(address)

  def filterKeyColumn(self) -> int:
    """
    Calls Qt's 'int QSortFilterProxyModel::filterKeyColumn() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterKeyColumn
    """
    #  int QSortFilterProxyModel::filterKeyColumn() const
    return self.uglySide.call(
        'ritual_ZNK21QSortFilterProxyModel15filterKeyColumnEv',
    )

  def filterCaseSensitivity(self) -> Qt.CaseSensitivity:
    """
    Calls Qt's 'Qt::CaseSensitivity
    QSortFilterProxyModel::filterCaseSensitivity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterCaseSensitivity

    Returns
    -------

    Qt.CaseSensitivity
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.CaseSensitivity(number)' gives.
    """
    #  Qt::CaseSensitivity QSortFilterProxyModel::filterCaseSensitivity()
    #      const
    return Qt.CaseSensitivity(self.uglySide.call(
        'ritual_ZNK21QSortFilterProxyModel21filterCaseSensitivityEv',
    ))

  def sortCaseSensitivity(self) -> Qt.CaseSensitivity:
    """
    Calls Qt's 'Qt::CaseSensitivity
    QSortFilterProxyModel::sortCaseSensitivity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortCaseSensitivity

    Returns
    -------

    Qt.CaseSensitivity
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.CaseSensitivity(number)' gives.
    """
    #  Qt::CaseSensitivity QSortFilterProxyModel::sortCaseSensitivity() const
    return Qt.CaseSensitivity(self.uglySide.call(
        'ritual_ZNK21QSortFilterProxyModel19sortCaseSensitivityEv',
    ))

  def isSortLocaleAware(self) -> bool:
    """
    Calls Qt's 'bool QSortFilterProxyModel::isSortLocaleAware() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#isSortLocaleAware
    """
    #  bool QSortFilterProxyModel::isSortLocaleAware() const
    return self.uglySide.call(
        'ritual_ZNK21QSortFilterProxyModel17isSortLocaleAwareEv',
    )

  def sortColumn(self) -> int:
    """
    Calls Qt's 'int QSortFilterProxyModel::sortColumn() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortColumn
    """
    #  int QSortFilterProxyModel::sortColumn() const
    return self.uglySide.call(
        'ritual_ZNK21QSortFilterProxyModel10sortColumnEv',
    )

  def sortOrder(self) -> Qt.SortOrder:
    """
    Calls Qt's 'Qt::SortOrder QSortFilterProxyModel::sortOrder() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortOrder

    Returns
    -------

    Qt.SortOrder
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.SortOrder(number)'
      gives.
    """
    #  Qt::SortOrder QSortFilterProxyModel::sortOrder() const
    return Qt.SortOrder(self.uglySide.call(
        'ritual_ZNK21QSortFilterProxyModel9sortOrderEv',
    ))

  def dynamicSortFilter(self) -> bool:
    """
    Calls Qt's 'bool QSortFilterProxyModel::dynamicSortFilter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#dynamicSortFilter
    """
    #  bool QSortFilterProxyModel::dynamicSortFilter() const
    return self.uglySide.call(
        'ritual_ZNK21QSortFilterProxyModel17dynamicSortFilterEv',
    )

  def sortRole(self) -> int:
    """
    Calls Qt's 'int QSortFilterProxyModel::sortRole() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortRole
    """
    #  int QSortFilterProxyModel::sortRole() const
    return self.uglySide.call('ritual_ZNK21QSortFilterProxyModel8sortRoleEv')

  def filterRole(self) -> int:
    """
    Calls Qt's 'int QSortFilterProxyModel::filterRole() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterRole
    """
    #  int QSortFilterProxyModel::filterRole() const
    return self.uglySide.call(
        'ritual_ZNK21QSortFilterProxyModel10filterRoleEv',
    )

  def isRecursiveFilteringEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSortFilterProxyModel::isRecursiveFilteringEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html
    """
    #  bool QSortFilterProxyModel::isRecursiveFilteringEnabled() const
    return self.uglySide.call(
        'ritual_ZNK21QSortFilterProxyModel27isRecursiveFilteringEnabledEv',
    )

  def autoAcceptChildRows(self) -> bool:
    """
    Calls Qt's 'bool QSortFilterProxyModel::autoAcceptChildRows() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#autoAcceptChildRows
    """
    #  bool QSortFilterProxyModel::autoAcceptChildRows() const
    return self.uglySide.call(
        'ritual_ZNK21QSortFilterProxyModel19autoAcceptChildRowsEv',
    )

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def index(
      self,
      row: int,
      column: int,
      parent: Optional[QModelIndex] = None,
  ) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QSortFilterProxyModel::index(int row, int column,
    const QModelIndex &parent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsortfilterproxymodel.html#index

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
    #  QModelIndex QSortFilterProxyModel::index(int row, int column, const
    #      QModelIndex &parent) const
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    address = self.uglySide.call(
        'ritual_ZNK21QSortFilterProxyModel5indexEiiRK11QModelIndex',
        row, column, self._valueOf(parent),
    )
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def parent(self, child: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QSortFilterProxyModel::parent(const QModelIndex
    &child) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsortfilterproxymodel.html#parent

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
    #  QModelIndex QSortFilterProxyModel::parent(const QModelIndex &child)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK21QSortFilterProxyModel6parentERK11QModelIndex',
        self._valueOf(child),
    )
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(int, int, QModelIndex)
  def sibling(self, row: int, column: int, idx: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QSortFilterProxyModel::sibling(int row, int
    column, const QModelIndex &idx) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sibling

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
    #  QModelIndex QSortFilterProxyModel::sibling(int row, int column, const
    #      QModelIndex &idx) const
    address = self.uglySide.call(
        'ritual_ZNK21QSortFilterProxyModel7siblingEiiRK11QModelIndex',
        row, column, self._valueOf(idx),
    )
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload()
  @overload(QModelIndex)
  def rowCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QSortFilterProxyModel::rowCount(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#rowCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QSortFilterProxyModel::rowCount(const QModelIndex &parent) const
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZNK21QSortFilterProxyModel8rowCountERK11QModelIndex',
        self._valueOf(parent),
    )

  @overload()
  @overload(QModelIndex)
  def columnCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QSortFilterProxyModel::columnCount(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#columnCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QSortFilterProxyModel::columnCount(const QModelIndex &parent)
    #      const
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZNK21QSortFilterProxyModel11columnCountERK11QModelIndex',
        self._valueOf(parent),
    )

  @overload()
  @overload(QModelIndex)
  def hasChildren(self, parent: Optional[QModelIndex] = None) -> bool:
    """
    Calls Qt's 'bool QSortFilterProxyModel::hasChildren(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#hasChildren

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QSortFilterProxyModel::hasChildren(const QModelIndex &parent)
    #      const
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZNK21QSortFilterProxyModel11hasChildrenERK11QModelIndex',
        self._valueOf(parent),
    )

  @overload(QModelIndex)
  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int = 0) -> QVariant:
    """
    Calls Qt's 'QVariant QSortFilterProxyModel::data(const QModelIndex
    &index, int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsortfilterproxymodel.html#data

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
    #  QVariant QSortFilterProxyModel::data(const QModelIndex &index, int
    #      role) const
    address = self.uglySide.call(
        'ritual_ZNK21QSortFilterProxyModel4dataERK11QModelIndexi',
        self._valueOf(index), role,
    )
    from . import QVariant
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
    Calls Qt's 'QVariant QSortFilterProxyModel::headerData(int section,
    Qt::Orientation orientation, int role) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#headerData

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
    #  QVariant QSortFilterProxyModel::headerData(int section,
    #      Qt::Orientation orientation, int role) const
    address = self.uglySide.call(
        'ritual_ZNK21QSortFilterProxyModel10headerDataEiN2Qt11OrientationEi',
        section, orientation.value, role,
    )
    from . import QVariant
    return QVariant._cuteOwning(address)

  @overload(QModelIndex)
  def canFetchMore(self, parent: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QSortFilterProxyModel::canFetchMore(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#canFetchMore

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QSortFilterProxyModel::canFetchMore(const QModelIndex &parent)
    #      const
    return self.uglySide.call(
        'ritual_ZNK21QSortFilterProxyModel12canFetchMoreERK11QModelIndex',
        self._valueOf(parent),
    )

  @overload(QModelIndex)
  def flags(self, index: QModelIndex) -> Qt.ItemFlags:
    """
    Calls Qt's 'Qt::ItemFlags QSortFilterProxyModel::flags(const QModelIndex
    &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsortfilterproxymodel.html#flags

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    Qt.ItemFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::ItemFlags QSortFilterProxyModel::flags(const QModelIndex &index)
    #      const
    return Qt.ItemFlags(self.uglySide.call(
        'ritual_ZNK21QSortFilterProxyModel5flagsERK11QModelIndex',
        self._valueOf(index),
    ))

  @overload(QModelIndex)
  def buddy(self, index: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QSortFilterProxyModel::buddy(const QModelIndex
    &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsortfilterproxymodel.html#buddy

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QSortFilterProxyModel::buddy(const QModelIndex &index)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK21QSortFilterProxyModel5buddyERK11QModelIndex',
        self._valueOf(index),
    )
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def span(self, index: QModelIndex) -> QSize:
    """
    Calls Qt's 'QSize QSortFilterProxyModel::span(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsortfilterproxymodel.html#span

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSortFilterProxyModel::span(const QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK21QSortFilterProxyModel4spanERK11QModelIndex',
        self._valueOf(index),
    )
    from . import QSize
    return QSize._cuteOwning(address)

  def supportedDropActions(self) -> Qt.DropActions:
    """
    Calls Qt's 'Qt::DropActions QSortFilterProxyModel::supportedDropActions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#supportedDropActions

    Returns
    -------

    Qt.DropActions
      The value standing for the combination Qt gave back.
    """
    #  Qt::DropActions QSortFilterProxyModel::supportedDropActions() const
    return Qt.DropActions(self.uglySide.call(
        'ritual_ZNK21QSortFilterProxyModel20supportedDropActionsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setSourceModel(
      self,
      sourceModel: Optional[QAbstractItemModel],
  ) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModel::setSourceModel(QAbstractItemModel
    *sourceModel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setSourceModel

    Parameters
    ----------

    sourceModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSortFilterProxyModel::setSourceModel(QAbstractItemModel
    #      *sourceModel)
    self.uglySide.call(
        'ritual_ZN21QSortFilterProxyModel14setSourceModelEP18QAbstractItemM'
        'odel',
        self._addressOf(sourceModel),
    )

  @overload(int)
  def setFilterKeyColumn(self, column: int) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModel::setFilterKeyColumn(int column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setFilterKeyColumn

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  void QSortFilterProxyModel::setFilterKeyColumn(int column)
    self.uglySide.call(
        'ritual_ZN21QSortFilterProxyModel18setFilterKeyColumnEi', column,
    )

  @overload(Qt.CaseSensitivity)
  def setFilterCaseSensitivity(self, cs: Qt.CaseSensitivity) -> None:
    """
    Calls Qt's 'void
    QSortFilterProxyModel::setFilterCaseSensitivity(Qt::CaseSensitivity cs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html

    Parameters
    ----------

    cs : Qt.CaseSensitivity
      Passed on as its number.
    """
    #  void QSortFilterProxyModel::setFilterCaseSensitivity(Qt::
    #      CaseSensitivity cs)
    self.uglySide.call(
        'ritual_ZN21QSortFilterProxyModel24setFilterCaseSensitivityEN2Qt15C'
        'aseSensitivityE',
        cs.value,
    )

  @overload(Qt.CaseSensitivity)
  def setSortCaseSensitivity(self, cs: Qt.CaseSensitivity) -> None:
    """
    Calls Qt's 'void
    QSortFilterProxyModel::setSortCaseSensitivity(Qt::CaseSensitivity cs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setSortCaseSensitivity

    Parameters
    ----------

    cs : Qt.CaseSensitivity
      Passed on as its number.
    """
    #  void QSortFilterProxyModel::setSortCaseSensitivity(Qt::CaseSensitivity
    #      cs)
    self.uglySide.call(
        'ritual_ZN21QSortFilterProxyModel22setSortCaseSensitivityEN2Qt15Cas'
        'eSensitivityE',
        cs.value,
    )

  @overload(bool)
  def setSortLocaleAware(self, on: bool) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModel::setSortLocaleAware(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setSortLocaleAware

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QSortFilterProxyModel::setSortLocaleAware(bool on)
    self.uglySide.call(
        'ritual_ZN21QSortFilterProxyModel18setSortLocaleAwareEb', on,
    )

  @overload(bool)
  def setDynamicSortFilter(self, enable: bool) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModel::setDynamicSortFilter(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setDynamicSortFilter

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QSortFilterProxyModel::setDynamicSortFilter(bool enable)
    self.uglySide.call(
        'ritual_ZN21QSortFilterProxyModel20setDynamicSortFilterEb', enable,
    )

  @overload(int)
  def setSortRole(self, role: int) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModel::setSortRole(int role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setSortRole

    Parameters
    ----------

    role : int
      Passed on as it is.
    """
    #  void QSortFilterProxyModel::setSortRole(int role)
    self.uglySide.call(
        'ritual_ZN21QSortFilterProxyModel11setSortRoleEi', role,
    )

  @overload(int)
  def setFilterRole(self, role: int) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModel::setFilterRole(int role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setFilterRole

    Parameters
    ----------

    role : int
      Passed on as it is.
    """
    #  void QSortFilterProxyModel::setFilterRole(int role)
    self.uglySide.call(
        'ritual_ZN21QSortFilterProxyModel13setFilterRoleEi', role,
    )

  @overload(bool)
  def setRecursiveFilteringEnabled(self, recursive: bool) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModel::setRecursiveFilteringEnabled(bool
    recursive)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html

    Parameters
    ----------

    recursive : bool
      Passed on as it is.
    """
    #  void QSortFilterProxyModel::setRecursiveFilteringEnabled(bool
    #      recursive)
    self.uglySide.call(
        'ritual_ZN21QSortFilterProxyModel28setRecursiveFilteringEnabledEb',
        recursive,
    )

  @overload(bool)
  def setAutoAcceptChildRows(self, accept: bool) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModel::setAutoAcceptChildRows(bool
    accept)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setAutoAcceptChildRows

    Parameters
    ----------

    accept : bool
      Passed on as it is.
    """
    #  void QSortFilterProxyModel::setAutoAcceptChildRows(bool accept)
    self.uglySide.call(
        'ritual_ZN21QSortFilterProxyModel22setAutoAcceptChildRowsEb', accept,
    )

  @overload(str)
  def setFilterRegularExpression(self, pattern: str) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModel::setFilterRegularExpression(const
    QString &pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html

    Parameters
    ----------

    pattern : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSortFilterProxyModel::setFilterRegularExpression(const QString
    #      &pattern)
    self.uglySide.call(
        'ritual_ZN21QSortFilterProxyModel26setFilterRegularExpressionERK7QS'
        'tring',
        pattern,
    )

  @overload(QRegularExpression)
  def setFilterRegularExpression(
      self,
      regularExpression: QRegularExpression,
  ) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModel::setFilterRegularExpression(const
    QRegularExpression &regularExpression)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html

    Parameters
    ----------

    regularExpression : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  void QSortFilterProxyModel::setFilterRegularExpression(const
    #      QRegularExpression &regularExpression)
    self.uglySide.call(
        'ritual_ZN21QSortFilterProxyModel26setFilterRegularExpressionERK18Q'
        'RegularExpression',
        self._valueOf(regularExpression),
    )

  @overload(str)
  def setFilterWildcard(self, pattern: str) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModel::setFilterWildcard(const QString
    &pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setFilterWildcard

    Parameters
    ----------

    pattern : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSortFilterProxyModel::setFilterWildcard(const QString &pattern)
    self.uglySide.call(
        'ritual_ZN21QSortFilterProxyModel17setFilterWildcardERK7QString',
        pattern,
    )

  @overload(str)
  def setFilterFixedString(self, pattern: str) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModel::setFilterFixedString(const
    QString &pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setFilterFixedString

    Parameters
    ----------

    pattern : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSortFilterProxyModel::setFilterFixedString(const QString
    #      &pattern)
    self.uglySide.call(
        'ritual_ZN21QSortFilterProxyModel20setFilterFixedStringERK7QString',
        pattern,
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
    Calls Qt's 'bool QSortFilterProxyModel::setData(const QModelIndex &index,
    const QVariant &value, int role)'.

    Qt's own words: https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setData

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
    #  bool QSortFilterProxyModel::setData(const QModelIndex &index, const
    #      QVariant &value, int role)
    return self.uglySide.call(
        'ritual_ZN21QSortFilterProxyModel7setDataERK11QModelIndexRK8QVarian'
        'ti',
        self._valueOf(index), self._valueOf(value), role,
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
    Calls Qt's 'bool QSortFilterProxyModel::setHeaderData(int section,
    Qt::Orientation orientation, const QVariant &value, int role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setHeaderData

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
    #  bool QSortFilterProxyModel::setHeaderData(int section, Qt::Orientation
    #      orientation, const QVariant &value, int role)
    return self.uglySide.call(
        'ritual_ZN21QSortFilterProxyModel13setHeaderDataEiN2Qt11Orientation'
        'ERK8QVarianti',
        section, orientation.value, self._valueOf(value), role,
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
    'QSortFilterProxyModel::QSortFilterProxyModel(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#QSortFilterProxyModel

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSortFilterProxyModel::QSortFilterProxyModel(QObject *parent)
    self._noteCreation(QSortFilterProxyModel, lambda: Rituals.call(
        'ritual_ZN21QSortFilterProxyModelC1EP7QObject',
        self._addressOf(parent),
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

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModel::invalidate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#invalidate
    """
    #  void QSortFilterProxyModel::invalidate()
    self.uglySide.call('ritual_ZN21QSortFilterProxyModel10invalidateEv')

  @overload(QMimeData, Qt.DropAction, int, int, QModelIndex)
  @overload(NoneType, Qt.DropAction, int, int, QModelIndex)
  def dropMimeData(
      self,
      data: Optional[QMimeData],
      action: Qt.DropAction,
      row: int,
      column: int,
      parent: QModelIndex,
  ) -> bool:
    """
    Calls Qt's 'bool QSortFilterProxyModel::dropMimeData(const QMimeData
    *data, Qt::DropAction action, int row, int column, const QModelIndex
    &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#dropMimeData

    Parameters
    ----------

    data : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    action : Qt.DropAction
      Passed on as its number.

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QSortFilterProxyModel::dropMimeData(const QMimeData *data,
    #      Qt::DropAction action, int row, int column, const QModelIndex
    #      &parent)
    return self.uglySide.call(
        'ritual_ZN21QSortFilterProxyModel12dropMimeDataEPK9QMimeDataN2Qt10D'
        'ropActionEiiRK11QModelIndex',
        self._addressOf(data), action.value, row, column,
        self._valueOf(parent),
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
    Calls Qt's 'bool QSortFilterProxyModel::insertRows(int row, int count,
    const QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#insertRows

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
    #  bool QSortFilterProxyModel::insertRows(int row, int count, const
    #      QModelIndex &parent)
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZN21QSortFilterProxyModel10insertRowsEiiRK11QModelIndex',
        row, count, self._valueOf(parent),
    )

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def insertColumns(
      self,
      column: int,
      count: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QSortFilterProxyModel::insertColumns(int column, int
    count, const QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#insertColumns

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
    #  bool QSortFilterProxyModel::insertColumns(int column, int count, const
    #      QModelIndex &parent)
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZN21QSortFilterProxyModel13insertColumnsEiiRK11QModelIndex',
        column, count, self._valueOf(parent),
    )

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def removeRows(
      self,
      row: int,
      count: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QSortFilterProxyModel::removeRows(int row, int count,
    const QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#removeRows

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
    #  bool QSortFilterProxyModel::removeRows(int row, int count, const
    #      QModelIndex &parent)
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZN21QSortFilterProxyModel10removeRowsEiiRK11QModelIndex',
        row, count, self._valueOf(parent),
    )

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def removeColumns(
      self,
      column: int,
      count: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QSortFilterProxyModel::removeColumns(int column, int
    count, const QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#removeColumns

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
    #  bool QSortFilterProxyModel::removeColumns(int column, int count, const
    #      QModelIndex &parent)
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZN21QSortFilterProxyModel13removeColumnsEiiRK11QModelIndex',
        column, count, self._valueOf(parent),
    )

  @overload(QModelIndex)
  def fetchMore(self, parent: QModelIndex) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModel::fetchMore(const QModelIndex
    &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodel.html#fetchMore

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QSortFilterProxyModel::fetchMore(const QModelIndex &parent)
    self.uglySide.call(
        'ritual_ZN21QSortFilterProxyModel9fetchMoreERK11QModelIndex',
        self._valueOf(parent),
    )

  @overload(int)
  @overload(int, Qt.SortOrder)
  def sort(
      self,
      column: int,
      order: Qt.SortOrder = Qt.SortOrder.AscendingOrder,
  ) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModel::sort(int column, Qt::SortOrder
    order)'.

    Qt's own words: https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sort

    Parameters
    ----------

    column : int
      Passed on as it is.

    order : Qt.SortOrder
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.SortOrder.AscendingOrder.
    """
    #  void QSortFilterProxyModel::sort(int column, Qt::SortOrder order)
    self.uglySide.call(
        'ritual_ZN21QSortFilterProxyModel4sortEiN2Qt9SortOrderE',
        column, order.value,
    )
