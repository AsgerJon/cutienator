"""
QQmlTreeModelToTableModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmltreemodeltotablemodel_p_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlTreeModelToTableModel to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QAbstractItemModel, QHash, QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QItemSelection, QMetaObject, QModelIndex
  from ..QtCore import QPersistentModelIndex, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QPersistentModelIndex = WAIT['QPersistentModelIndex']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlTreeModelToTableModel(QAbstractItemModel):
  """
  The cute side of Qt's QQmlTreeModelToTableModel: a plain Python object
  standing in front of one C++ QQmlTreeModelToTableModel.

  It is built on the cute 'QAbstractItemModel', as Qt's
  QQmlTreeModelToTableModel is built on Qt's QAbstractItemModel, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlTreeModelToTableModel that has a ritual and that
  Python can call so far, 62 names in all: 'metaObject', 'tr', 'model',
  'rootIndex', 'setRootIndex', 'resetRootIndex', 'index', 'parent',
  'rowCount', 'columnCount', 'roleNames', 'data', 'setData', 'headerData',
  'flags', 'clearModelData', 'isVisible', 'childrenVisible', 'mapToModel',
  'mapFromModel', 'selectionForRowRange', 'showModelTopLevelItems',
  'itemIndex', 'expandPendingRows', 'lastChildIndex', 'removeVisibleRows',
  'dump', 'testConsistency', 'modelChanged', 'rootIndexChanged', 'expanded',
  'collapsed', 'expand', 'collapse', 'setModel', 'isExpanded', 'hasChildren',
  'hasSiblings', 'depthAtRow', 'expandRow', 'expandRecursively',
  'collapseRow', 'collapseRecursively', 'modelHasBeenDestroyed',
  'modelHasBeenReset', 'modelLayoutAboutToBeChanged', 'modelLayoutChanged',
  'modelRowsAboutToBeInserted', 'modelRowsAboutToBeMoved',
  'modelRowsAboutToBeRemoved', 'modelRowsInserted', 'modelRowsMoved',
  'modelRowsRemoved', 'modelColumnsAboutToBeInserted',
  'modelColumnsAboutToBeRemoved', 'modelColumnsInserted',
  'modelColumnsRemoved', 'enableSignalAggregation',
  'disableSignalAggregation', 'isAggregatingSignals', 'emitQueuedSignals',
  'connectToModel'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlTreeModelToTableModel::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQmlTreeModelToTableModel::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQmlTreeModelToTableModel::showModelChildItems(const TreeItem
    &parent, int start, int end, bool doInsertRows, bool
    doExpandPendingRows)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlTreeModelToTableModel::modelDataChanged(const QModelIndex
    &topLeft, const QModelIndex &bottomRight, const QList<int> &roles)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlTreeModelToTableModel::queueDataChanged(int top, int
    bottom, std::initializer_list<int> roles)': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  2 of the 72 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlTreeModelToTableModel is created at the first use, not by
    'QQmlTreeModelToTableModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlTreeModelToTableModel.
  - Qt tells when it has removed the C++ QQmlTreeModelToTableModel. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlTreeModelToTableModel that has no cute function
    yet, 'modelDataChanged', 'queueDataChanged', 'showModelChildItems', holds
    a function that raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QQmlTreeModelToTableModel::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#tr

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
    #  QString QQmlTreeModelToTableModel::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QQmlTreeModelToTableModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlTreeModelToTableModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlTreeModelToTableModel::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlTreeModelToTableModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QQmlTreeModelToTableModel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def model(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel *QQmlTreeModelToTableModel::model()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#model

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *QQmlTreeModelToTableModel::model() const
    address = self.uglySide.call(
        'ritual_ZNK25QQmlTreeModelToTableModel5modelEv',
    )
    return QAbstractItemModel._cuteAt(address)

  def rootIndex(self) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QQmlTreeModelToTableModel::rootIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#rootIndex

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QQmlTreeModelToTableModel::rootIndex() const
    address = self.uglySide.call(
        'ritual_ZNK25QQmlTreeModelToTableModel9rootIndexEv',
    )
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
    Calls Qt's 'QModelIndex QQmlTreeModelToTableModel::index(int row, int
    column, const QModelIndex &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#index

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
    #  QModelIndex QQmlTreeModelToTableModel::index(int row, int column,
    #      const QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK25QQmlTreeModelToTableModel5indexEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QQmlTreeModelToTableModel5indexEiiRK11QModelInde'
          'x')
    address = self.uglySide.call(ritual, row, column, self._valueOf(parent))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def parent(self, child: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QQmlTreeModelToTableModel::parent(const
    QModelIndex &child) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#parent

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
    #  QModelIndex QQmlTreeModelToTableModel::parent(const QModelIndex
    #      &child) const
    ritual = 'ritual_ZNK25QQmlTreeModelToTableModel6parentERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QQmlTreeModelToTableModel6parentERK11QModelIndex')
    address = self.uglySide.call(ritual, self._valueOf(child))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload()
  @overload(QModelIndex)
  def rowCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QQmlTreeModelToTableModel::rowCount(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#rowCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QQmlTreeModelToTableModel::rowCount(const QModelIndex &parent)
    #      const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK25QQmlTreeModelToTableModel8rowCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QQmlTreeModelToTableModel8rowCountERK11QModelInd'
          'ex')
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload()
  @overload(QModelIndex)
  def columnCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QQmlTreeModelToTableModel::columnCount(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#columnCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QQmlTreeModelToTableModel::columnCount(const QModelIndex &parent)
    #      const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = (
        'ritual_ZNK25QQmlTreeModelToTableModel11columnCountERK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QQmlTreeModelToTableModel11columnCountERK11QMode'
          'lIndex')
    return self.uglySide.call(ritual, self._valueOf(parent))

  def roleNames(self) -> QHash[int, QByteArray]:
    """
    Calls Qt's 'QHash<int, QByteArray> QQmlTreeModelToTableModel::roleNames()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#roleNames

    Returns
    -------

    QHash[int, QByteArray]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<int, QByteArray> QQmlTreeModelToTableModel::roleNames() const
    address = self.uglySide.call(
        'ritual_ZNK25QQmlTreeModelToTableModel9roleNamesEv',
    )
    from ..QtCore import QByteArray
    return QHash[int, QByteArray]._cuteOwning(address)

  @overload(QModelIndex, int)
  def data(self, a0: QModelIndex, role: int) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlTreeModelToTableModel::data(const QModelIndex
    &a0, int role) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#data

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    role : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlTreeModelToTableModel::data(const QModelIndex &a0, int
    #      role) const
    ritual = 'ritual_ZNK25QQmlTreeModelToTableModel4dataERK11QModelIndexi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QQmlTreeModelToTableModel4dataERK11QModelIndexi')
    address = self.uglySide.call(ritual, self._valueOf(a0), role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int, Qt.Orientation, int)
  def headerData(
      self,
      section: int,
      orientation: Qt.Orientation,
      role: int,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlTreeModelToTableModel::headerData(int section,
    Qt::Orientation orientation, int role) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#headerData

    Parameters
    ----------

    section : int
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number.

    role : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlTreeModelToTableModel::headerData(int section,
    #      Qt::Orientation orientation, int role) const
    ritual = (
        'ritual_ZNK25QQmlTreeModelToTableModel10headerDataEiN2Qt11Orientati'
        'onEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QQmlTreeModelToTableModel10headerDataEiN2Qt11Ori'
          'entationEi')
    address = self.uglySide.call(ritual, section, orientation.value, role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QModelIndex)
  def flags(self, index: QModelIndex) -> Qt.ItemFlags:
    """
    Calls Qt's 'Qt::ItemFlags QQmlTreeModelToTableModel::flags(const
    QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#flags

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
    #  Qt::ItemFlags QQmlTreeModelToTableModel::flags(const QModelIndex
    #      &index) const
    ritual = 'ritual_ZNK25QQmlTreeModelToTableModel5flagsERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QQmlTreeModelToTableModel5flagsERK11QModelIndex')
    return Qt.ItemFlags(self.uglySide.call(ritual, self._valueOf(index)))

  @overload(QModelIndex)
  def mapToModel(self, index: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QQmlTreeModelToTableModel::mapToModel(const
    QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#mapToModel

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
    #  QModelIndex QQmlTreeModelToTableModel::mapToModel(const QModelIndex
    #      &index) const
    address = self.uglySide.call(
        'ritual_ZNK25QQmlTreeModelToTableModel10mapToModelERK11QModelIndex',
        self._valueOf(index),
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(int)
  def mapToModel(self, row: int) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QQmlTreeModelToTableModel::mapToModel(int row)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#mapToModel

    Parameters
    ----------

    row : int
      Passed on as it is.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QQmlTreeModelToTableModel::mapToModel(int row) const
    address = self.uglySide.call(
        'ritual_ZNK25QQmlTreeModelToTableModel10mapToModelEi', row,
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def mapFromModel(self, index: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QQmlTreeModelToTableModel::mapFromModel(const
    QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#mapFromModel

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
    #  QModelIndex QQmlTreeModelToTableModel::mapFromModel(const QModelIndex
    #      &index) const
    address = self.uglySide.call(
        'ritual_ZNK25QQmlTreeModelToTableModel12mapFromModelERK11QModelInde'
        'x',
        self._valueOf(index),
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex, QModelIndex)
  def selectionForRowRange(
      self,
      fromIndex: QModelIndex,
      toIndex: QModelIndex,
  ) -> QItemSelection:
    """
    Calls Qt's 'QItemSelection
    QQmlTreeModelToTableModel::selectionForRowRange(const QModelIndex
    &fromIndex, const QModelIndex &toIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html

    Parameters
    ----------

    fromIndex : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    toIndex : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QItemSelection
      A new cute QItemSelection around the copy Qt gave back. Python owns it.
    """
    #  QItemSelection QQmlTreeModelToTableModel::selectionForRowRange(const
    #      QModelIndex &fromIndex, const QModelIndex &toIndex) const
    address = self.uglySide.call(
        'ritual_ZNK25QQmlTreeModelToTableModel20selectionForRowRangeERK11QM'
        'odelIndexS2_',
        self._valueOf(fromIndex), self._valueOf(toIndex),
    )
    from ..QtCore import QItemSelection
    return QItemSelection._cuteOwning(address)

  @overload(QModelIndex)
  def itemIndex(self, index: QModelIndex) -> int:
    """
    Calls Qt's 'int QQmlTreeModelToTableModel::itemIndex(const QModelIndex
    &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#itemIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  int QQmlTreeModelToTableModel::itemIndex(const QModelIndex &index)
    #      const
    return self.uglySide.call(
        'ritual_ZNK25QQmlTreeModelToTableModel9itemIndexERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def lastChildIndex(self, index: QModelIndex) -> int:
    """
    Calls Qt's 'int QQmlTreeModelToTableModel::lastChildIndex(const
    QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#lastChildIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  int QQmlTreeModelToTableModel::lastChildIndex(const QModelIndex
    #      &index) const
    return self.uglySide.call(
        'ritual_ZNK25QQmlTreeModelToTableModel14lastChildIndexERK11QModelIn'
        'dex',
        self._valueOf(index),
    )

  @overload()
  @overload(bool)
  def testConsistency(self, dumpOnFail: bool = False) -> bool:
    """
    Calls Qt's 'bool QQmlTreeModelToTableModel::testConsistency(bool
    dumpOnFail) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#testConsistency

    Parameters
    ----------

    dumpOnFail : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  bool QQmlTreeModelToTableModel::testConsistency(bool dumpOnFail) const
    return self.uglySide.call(
        'ritual_ZNK25QQmlTreeModelToTableModel15testConsistencyEb',
        dumpOnFail,
    )

  @overload(QModelIndex)
  def isExpanded(self, a0: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QQmlTreeModelToTableModel::isExpanded(const QModelIndex
    &a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#isExpanded

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QQmlTreeModelToTableModel::isExpanded(const QModelIndex &a0)
    #      const
    return self.uglySide.call(
        'ritual_ZNK25QQmlTreeModelToTableModel10isExpandedERK11QModelIndex',
        self._valueOf(a0),
    )

  @overload(int)
  def isExpanded(self, row: int) -> bool:
    """
    Calls Qt's 'bool QQmlTreeModelToTableModel::isExpanded(int row) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#isExpanded

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  bool QQmlTreeModelToTableModel::isExpanded(int row) const
    return self.uglySide.call(
        'ritual_ZNK25QQmlTreeModelToTableModel10isExpandedEi', row,
    )

  @overload(int)
  def hasChildren(self, row: int) -> bool:
    """
    Calls Qt's 'bool QQmlTreeModelToTableModel::hasChildren(int row) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#hasChildren

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  bool QQmlTreeModelToTableModel::hasChildren(int row) const
    return self.uglySide.call(
        'ritual_ZNK25QQmlTreeModelToTableModel11hasChildrenEi', row,
    )

  @overload(int)
  def hasSiblings(self, row: int) -> bool:
    """
    Calls Qt's 'bool QQmlTreeModelToTableModel::hasSiblings(int row) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#hasSiblings

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  bool QQmlTreeModelToTableModel::hasSiblings(int row) const
    return self.uglySide.call(
        'ritual_ZNK25QQmlTreeModelToTableModel11hasSiblingsEi', row,
    )

  @overload(int)
  def depthAtRow(self, row: int) -> int:
    """
    Calls Qt's 'int QQmlTreeModelToTableModel::depthAtRow(int row) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#depthAtRow

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  int QQmlTreeModelToTableModel::depthAtRow(int row) const
    return self.uglySide.call(
        'ritual_ZNK25QQmlTreeModelToTableModel10depthAtRowEi', row,
    )

  def isAggregatingSignals(self) -> bool:
    """
    Calls Qt's 'bool QQmlTreeModelToTableModel::isAggregatingSignals()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html
    """
    #  bool QQmlTreeModelToTableModel::isAggregatingSignals() const
    return self.uglySide.call(
        'ritual_ZNK25QQmlTreeModelToTableModel20isAggregatingSignalsEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QModelIndex)
  def setRootIndex(self, idx: QModelIndex) -> None:
    """
    Calls Qt's 'void QQmlTreeModelToTableModel::setRootIndex(const
    QModelIndex &idx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#setRootIndex

    Parameters
    ----------

    idx : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QQmlTreeModelToTableModel::setRootIndex(const QModelIndex &idx)
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel12setRootIndexERK11QModelIndex',
        self._valueOf(idx),
    )

  @overload(QModelIndex, QVariant, int)
  def setData(self, index: QModelIndex, value: QVariant, role: int) -> bool:
    """
    Calls Qt's 'bool QQmlTreeModelToTableModel::setData(const QModelIndex
    &index, const QVariant &value, int role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#setData

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    role : int
      Passed on as it is.
    """
    #  bool QQmlTreeModelToTableModel::setData(const QModelIndex &index,
    #      const QVariant &value, int role)
    ritual = (
        'ritual_ZN25QQmlTreeModelToTableModel7setDataERK11QModelIndexRK8QVa'
        'rianti')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QQmlTreeModelToTableModel7setDataERK11QModelIndex'
          'RK8QVarianti')
    return self.uglySide.call(
        ritual, self._valueOf(index), self._valueOf(value), role,
    )

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setModel(self, model: Optional[QAbstractItemModel]) -> None:
    """
    Calls Qt's 'void QQmlTreeModelToTableModel::setModel(QAbstractItemModel
    *model)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#setModel

    Parameters
    ----------

    model : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlTreeModelToTableModel::setModel(QAbstractItemModel *model)
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel8setModelEP18QAbstractItemMode'
        'l',
        self._addressOf(model),
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
    'QQmlTreeModelToTableModel::QQmlTreeModelToTableModel(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlTreeModelToTableModel::QQmlTreeModelToTableModel(QObject *parent)
    self._noteCreation(QQmlTreeModelToTableModel, lambda: Rituals.call(
        'ritual_ZN25QQmlTreeModelToTableModelC1EP7QObject',
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

  def resetRootIndex(self) -> None:
    """
    Calls Qt's 'void QQmlTreeModelToTableModel::resetRootIndex()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#resetRootIndex
    """
    #  void QQmlTreeModelToTableModel::resetRootIndex()
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel14resetRootIndexEv',
    )

  def clearModelData(self) -> None:
    """
    Calls Qt's 'void QQmlTreeModelToTableModel::clearModelData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#clearModelData
    """
    #  void QQmlTreeModelToTableModel::clearModelData()
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel14clearModelDataEv',
    )

  @overload(QModelIndex)
  def isVisible(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QQmlTreeModelToTableModel::isVisible(const QModelIndex
    &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#isVisible

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QQmlTreeModelToTableModel::isVisible(const QModelIndex &index)
    return self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel9isVisibleERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def childrenVisible(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QQmlTreeModelToTableModel::childrenVisible(const
    QModelIndex &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#childrenVisible

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QQmlTreeModelToTableModel::childrenVisible(const QModelIndex
    #      &index)
    return self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel15childrenVisibleERK11QModelIn'
        'dex',
        self._valueOf(index),
    )

  @overload()
  @overload(bool)
  def showModelTopLevelItems(self, doInsertRows: bool = True) -> None:
    """
    Calls Qt's 'void QQmlTreeModelToTableModel::showModelTopLevelItems(bool
    doInsertRows)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html

    Parameters
    ----------

    doInsertRows : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QQmlTreeModelToTableModel::showModelTopLevelItems(bool
    #      doInsertRows)
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel22showModelTopLevelItemsEb',
        doInsertRows,
    )

  @overload()
  @overload(bool)
  def expandPendingRows(self, doInsertRows: bool = True) -> None:
    """
    Calls Qt's 'void QQmlTreeModelToTableModel::expandPendingRows(bool
    doInsertRows)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#expandPendingRows

    Parameters
    ----------

    doInsertRows : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QQmlTreeModelToTableModel::expandPendingRows(bool doInsertRows)
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel17expandPendingRowsEb',
        doInsertRows,
    )

  @overload(int, int)
  @overload(int, int, bool)
  def removeVisibleRows(
      self,
      startIndex: int,
      endIndex: int,
      doRemoveRows: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QQmlTreeModelToTableModel::removeVisibleRows(int
    startIndex, int endIndex, bool doRemoveRows)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#removeVisibleRows

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    endIndex : int
      Passed on as it is.

    doRemoveRows : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QQmlTreeModelToTableModel::removeVisibleRows(int startIndex, int
    #      endIndex, bool doRemoveRows)
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel17removeVisibleRowsEiib',
        startIndex, endIndex, doRemoveRows,
    )

  def dump(self) -> None:
    """
    Calls Qt's 'void QQmlTreeModelToTableModel::dump() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#dump
    """
    #  void QQmlTreeModelToTableModel::dump() const
    self.uglySide.call('ritual_ZNK25QQmlTreeModelToTableModel4dumpEv')

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def modelChanged(self, model: Optional[QAbstractItemModel]) -> None:
    """
    Calls Qt's 'void
    QQmlTreeModelToTableModel::modelChanged(QAbstractItemModel *model)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#modelChanged

    Parameters
    ----------

    model : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlTreeModelToTableModel::modelChanged(QAbstractItemModel
    #      *model)
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel12modelChangedEP18QAbstractIte'
        'mModel',
        self._addressOf(model),
    )

  def rootIndexChanged(self) -> None:
    """
    Calls Qt's 'void QQmlTreeModelToTableModel::rootIndexChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#rootIndexChanged
    """
    #  void QQmlTreeModelToTableModel::rootIndexChanged()
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel16rootIndexChangedEv',
    )

  @overload(QModelIndex)
  def expanded(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QQmlTreeModelToTableModel::expanded(const QModelIndex
    &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#expanded

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QQmlTreeModelToTableModel::expanded(const QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel8expandedERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def collapsed(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QQmlTreeModelToTableModel::collapsed(const QModelIndex
    &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#collapsed

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QQmlTreeModelToTableModel::collapsed(const QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel9collapsedERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def expand(self, a0: QModelIndex) -> None:
    """
    Calls Qt's 'void QQmlTreeModelToTableModel::expand(const QModelIndex
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#expand

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QQmlTreeModelToTableModel::expand(const QModelIndex &a0)
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel6expandERK11QModelIndex',
        self._valueOf(a0),
    )

  @overload(QModelIndex)
  def collapse(self, a0: QModelIndex) -> None:
    """
    Calls Qt's 'void QQmlTreeModelToTableModel::collapse(const QModelIndex
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#collapse

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QQmlTreeModelToTableModel::collapse(const QModelIndex &a0)
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel8collapseERK11QModelIndex',
        self._valueOf(a0),
    )

  @overload(int)
  def expandRow(self, n: int) -> None:
    """
    Calls Qt's 'void QQmlTreeModelToTableModel::expandRow(int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#expandRow

    Parameters
    ----------

    n : int
      Passed on as it is.
    """
    #  void QQmlTreeModelToTableModel::expandRow(int n)
    self.uglySide.call('ritual_ZN25QQmlTreeModelToTableModel9expandRowEi', n)

  @overload(int, int)
  def expandRecursively(self, row: int, depth: int) -> None:
    """
    Calls Qt's 'void QQmlTreeModelToTableModel::expandRecursively(int row,
    int depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#expandRecursively

    Parameters
    ----------

    row : int
      Passed on as it is.

    depth : int
      Passed on as it is.
    """
    #  void QQmlTreeModelToTableModel::expandRecursively(int row, int depth)
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel17expandRecursivelyEii',
        row, depth,
    )

  @overload(int)
  def collapseRow(self, n: int) -> None:
    """
    Calls Qt's 'void QQmlTreeModelToTableModel::collapseRow(int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#collapseRow

    Parameters
    ----------

    n : int
      Passed on as it is.
    """
    #  void QQmlTreeModelToTableModel::collapseRow(int n)
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel11collapseRowEi', n,
    )

  @overload(int)
  def collapseRecursively(self, row: int) -> None:
    """
    Calls Qt's 'void QQmlTreeModelToTableModel::collapseRecursively(int
    row)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#collapseRecursively

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  void QQmlTreeModelToTableModel::collapseRecursively(int row)
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel19collapseRecursivelyEi', row,
    )

  def modelHasBeenDestroyed(self) -> None:
    """
    Calls Qt's 'void QQmlTreeModelToTableModel::modelHasBeenDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html
    """
    #  void QQmlTreeModelToTableModel::modelHasBeenDestroyed()
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel21modelHasBeenDestroyedEv',
    )

  def modelHasBeenReset(self) -> None:
    """
    Calls Qt's 'void QQmlTreeModelToTableModel::modelHasBeenReset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#modelHasBeenReset
    """
    #  void QQmlTreeModelToTableModel::modelHasBeenReset()
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel17modelHasBeenResetEv',
    )

  @overload(
      QList[QPersistentModelIndex], QAbstractItemModel.LayoutChangeHint,
  )
  def modelLayoutAboutToBeChanged(
      self,
      parents: QList[QPersistentModelIndex],
      hint: QAbstractItemModel.LayoutChangeHint,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlTreeModelToTableModel::modelLayoutAboutToBeChanged(const
    QList<QPersistentModelIndex> &parents,
    QAbstractItemModel::LayoutChangeHint hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html

    Parameters
    ----------

    parents : QList[QPersistentModelIndex]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    hint : QAbstractItemModel.LayoutChangeHint
      Passed on as its number.
    """
    #  void QQmlTreeModelToTableModel::modelLayoutAboutToBeChanged(const
    #      QList<QPersistentModelIndex> &parents,
    #      QAbstractItemModel::LayoutChangeHint hint)
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel27modelLayoutAboutToBeChangedE'
        'RK5QListI21QPersistentModelIndexEN18QAbstractItemModel16LayoutChan'
        'geHintE',
        self._valueOf(parents), hint.value,
    )

  @overload(
      QList[QPersistentModelIndex], QAbstractItemModel.LayoutChangeHint,
  )
  def modelLayoutChanged(
      self,
      parents: QList[QPersistentModelIndex],
      hint: QAbstractItemModel.LayoutChangeHint,
  ) -> None:
    """
    Calls Qt's 'void QQmlTreeModelToTableModel::modelLayoutChanged(const
    QList<QPersistentModelIndex> &parents,
    QAbstractItemModel::LayoutChangeHint hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#modelLayoutChanged

    Parameters
    ----------

    parents : QList[QPersistentModelIndex]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    hint : QAbstractItemModel.LayoutChangeHint
      Passed on as its number.
    """
    #  void QQmlTreeModelToTableModel::modelLayoutChanged(const
    #      QList<QPersistentModelIndex> &parents,
    #      QAbstractItemModel::LayoutChangeHint hint)
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel18modelLayoutChangedERK5QListI'
        '21QPersistentModelIndexEN18QAbstractItemModel16LayoutChangeHintE',
        self._valueOf(parents), hint.value,
    )

  @overload(QModelIndex, int, int)
  def modelRowsAboutToBeInserted(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlTreeModelToTableModel::modelRowsAboutToBeInserted(const QModelIndex
    &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QQmlTreeModelToTableModel::modelRowsAboutToBeInserted(const
    #      QModelIndex &parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel26modelRowsAboutToBeInsertedER'
        'K11QModelIndexii',
        self._valueOf(parent), start, end,
    )

  @overload(QModelIndex, int, int, QModelIndex, int)
  def modelRowsAboutToBeMoved(
      self,
      sourceParent: QModelIndex,
      sourceStart: int,
      sourceEnd: int,
      destinationParent: QModelIndex,
      destinationRow: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlTreeModelToTableModel::modelRowsAboutToBeMoved(const
    QModelIndex &sourceParent, int sourceStart, int sourceEnd, const
    QModelIndex &destinationParent, int destinationRow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html

    Parameters
    ----------

    sourceParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    sourceStart : int
      Passed on as it is.

    sourceEnd : int
      Passed on as it is.

    destinationParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    destinationRow : int
      Passed on as it is.
    """
    #  void QQmlTreeModelToTableModel::modelRowsAboutToBeMoved(const
    #      QModelIndex &sourceParent, int sourceStart, int sourceEnd, const
    #      QModelIndex &destinationParent, int destinationRow)
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel23modelRowsAboutToBeMovedERK11'
        'QModelIndexiiS2_i',
        self._valueOf(sourceParent), sourceStart, sourceEnd,
        self._valueOf(destinationParent), destinationRow,
    )

  @overload(QModelIndex, int, int)
  def modelRowsAboutToBeRemoved(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlTreeModelToTableModel::modelRowsAboutToBeRemoved(const QModelIndex
    &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QQmlTreeModelToTableModel::modelRowsAboutToBeRemoved(const
    #      QModelIndex &parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel25modelRowsAboutToBeRemovedERK'
        '11QModelIndexii',
        self._valueOf(parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def modelRowsInserted(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlTreeModelToTableModel::modelRowsInserted(const
    QModelIndex &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#modelRowsInserted

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QQmlTreeModelToTableModel::modelRowsInserted(const QModelIndex
    #      &parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel17modelRowsInsertedERK11QModel'
        'Indexii',
        self._valueOf(parent), start, end,
    )

  @overload(QModelIndex, int, int, QModelIndex, int)
  def modelRowsMoved(
      self,
      sourceParent: QModelIndex,
      sourceStart: int,
      sourceEnd: int,
      destinationParent: QModelIndex,
      destinationRow: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlTreeModelToTableModel::modelRowsMoved(const
    QModelIndex &sourceParent, int sourceStart, int sourceEnd, const
    QModelIndex &destinationParent, int destinationRow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#modelRowsMoved

    Parameters
    ----------

    sourceParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    sourceStart : int
      Passed on as it is.

    sourceEnd : int
      Passed on as it is.

    destinationParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    destinationRow : int
      Passed on as it is.
    """
    #  void QQmlTreeModelToTableModel::modelRowsMoved(const QModelIndex
    #      &sourceParent, int sourceStart, int sourceEnd, const QModelIndex
    #      &destinationParent, int destinationRow)
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel14modelRowsMovedERK11QModelInd'
        'exiiS2_i',
        self._valueOf(sourceParent), sourceStart, sourceEnd,
        self._valueOf(destinationParent), destinationRow,
    )

  @overload(QModelIndex, int, int)
  def modelRowsRemoved(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlTreeModelToTableModel::modelRowsRemoved(const
    QModelIndex &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#modelRowsRemoved

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QQmlTreeModelToTableModel::modelRowsRemoved(const QModelIndex
    #      &parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel16modelRowsRemovedERK11QModelI'
        'ndexii',
        self._valueOf(parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def modelColumnsAboutToBeInserted(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlTreeModelToTableModel::modelColumnsAboutToBeInserted(const
    QModelIndex &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QQmlTreeModelToTableModel::modelColumnsAboutToBeInserted(const
    #      QModelIndex &parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel29modelColumnsAboutToBeInserte'
        'dERK11QModelIndexii',
        self._valueOf(parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def modelColumnsAboutToBeRemoved(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlTreeModelToTableModel::modelColumnsAboutToBeRemoved(const QModelIndex
    &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QQmlTreeModelToTableModel::modelColumnsAboutToBeRemoved(const
    #      QModelIndex &parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel28modelColumnsAboutToBeRemoved'
        'ERK11QModelIndexii',
        self._valueOf(parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def modelColumnsInserted(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlTreeModelToTableModel::modelColumnsInserted(const
    QModelIndex &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QQmlTreeModelToTableModel::modelColumnsInserted(const QModelIndex
    #      &parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel20modelColumnsInsertedERK11QMo'
        'delIndexii',
        self._valueOf(parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def modelColumnsRemoved(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlTreeModelToTableModel::modelColumnsRemoved(const
    QModelIndex &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#modelColumnsRemoved

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QQmlTreeModelToTableModel::modelColumnsRemoved(const QModelIndex
    #      &parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel19modelColumnsRemovedERK11QMod'
        'elIndexii',
        self._valueOf(parent), start, end,
    )

  def enableSignalAggregation(self) -> None:
    """
    Calls Qt's 'void QQmlTreeModelToTableModel::enableSignalAggregation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html
    """
    #  void QQmlTreeModelToTableModel::enableSignalAggregation()
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel23enableSignalAggregationEv',
    )

  def disableSignalAggregation(self) -> None:
    """
    Calls Qt's 'void QQmlTreeModelToTableModel::disableSignalAggregation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html
    """
    #  void QQmlTreeModelToTableModel::disableSignalAggregation()
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel24disableSignalAggregationEv',
    )

  def emitQueuedSignals(self) -> None:
    """
    Calls Qt's 'void QQmlTreeModelToTableModel::emitQueuedSignals()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#emitQueuedSignals
    """
    #  void QQmlTreeModelToTableModel::emitQueuedSignals()
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel17emitQueuedSignalsEv',
    )

  def connectToModel(self) -> None:
    """
    Calls Qt's 'void QQmlTreeModelToTableModel::connectToModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltreemodeltotablemodel.html#connectToModel
    """
    #  void QQmlTreeModelToTableModel::connectToModel()
    self.uglySide.call(
        'ritual_ZN25QQmlTreeModelToTableModel14connectToModelEv',
    )

  @staticmethod
  def modelDataChanged(*__, **_) -> Never:
    """
    Qt's 'void QQmlTreeModelToTableModel::modelDataChanged(const QModelIndex
    &topLeft, const QModelIndex &bottomRight, const QList<int> &roles)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlTreeModelToTableModel.modelDataChanged' has no cute function "
        "yet. Qt's 'void QQmlTreeModelToTableModel::modelDataChanged(const "
        "QModelIndex &topLeft, const QModelIndex &bottomRight, const "
        "QList<int> &roles)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def queueDataChanged(*__, **_) -> Never:
    """
    Qt's 'void QQmlTreeModelToTableModel::queueDataChanged(int top, int
    bottom, std::initializer_list<int> roles)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlTreeModelToTableModel.queueDataChanged' has no cute function "
        "yet. Qt's 'void QQmlTreeModelToTableModel::queueDataChanged(int "
        "top, int bottom, std::initializer_list<int> roles)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def showModelChildItems(*__, **_) -> Never:
    """
    Qt's 'void QQmlTreeModelToTableModel::showModelChildItems(const TreeItem
    &parent, int start, int end, bool doInsertRows, bool
    doExpandPendingRows)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlTreeModelToTableModel.showModelChildItems' has no cute "
        "function yet. Qt's 'void "
        "QQmlTreeModelToTableModel::showModelChildItems(const TreeItem "
        "&parent, int start, int end, bool doInsertRows, bool "
        "doExpandPendingRows)': takes a type Python has no way to hand over "
        "yet.")
