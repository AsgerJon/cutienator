"""
QConcatenateTablesProxyModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qconcatenatetablesproxymodel.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import Qt, QAbstractItemModel, QHash, QList, QMap, QObject
from . import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QByteArray, QMetaObject, QMimeData, QModelIndex, QSize
  from . import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMimeData = WAIT['QMimeData']
  QModelIndex = WAIT['QModelIndex']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QConcatenateTablesProxyModel(QAbstractItemModel):
  """
  The cute side of Qt's QConcatenateTablesProxyModel: a plain Python object
  standing in front of one C++ QConcatenateTablesProxyModel.

  It is built on the cute 'QAbstractItemModel', as Qt's
  QConcatenateTablesProxyModel is built on Qt's QAbstractItemModel, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QConcatenateTablesProxyModel that has a ritual and
  that Python can call so far, 23 names in all: 'metaObject', 'tr',
  'sourceModels', 'addSourceModel', 'removeSourceModel', 'mapFromSource',
  'mapToSource', 'data', 'setData', 'itemData', 'setItemData', 'flags',
  'index', 'parent', 'rowCount', 'headerData', 'columnCount', 'mimeTypes',
  'mimeData', 'canDropMimeData', 'dropMimeData', 'span', 'roleNames'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QConcatenateTablesProxyModel::~QConcatenateTablesProxyModel()': the
    destructor: Python never removes a C++ QConcatenateTablesProxyModel.

  What has no ritual
  ------------------

  8 of the 33 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 2 forbidden; 1 a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QConcatenateTablesProxyModel is created at the first use, not by
    'QConcatenateTablesProxyModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QConcatenateTablesProxyModel.
  - Qt tells when it has removed the C++ QConcatenateTablesProxyModel. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QConcatenateTablesProxyModel::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#tr

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
    #  QString QConcatenateTablesProxyModel::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN28QConcatenateTablesProxyModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QConcatenateTablesProxyModel'

  #  A C++ QConcatenateTablesProxyModel Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QConcatenateTablesProxyModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QConcatenateTablesProxyModel::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QConcatenateTablesProxyModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK28QConcatenateTablesProxyModel10metaObjectEv',
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def sourceModels(self) -> QList[QAbstractItemModel]:
    """
    Calls Qt's 'QList<QAbstractItemModel *>
    QConcatenateTablesProxyModel::sourceModels() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#sourceModels

    Returns
    -------

    QList[QAbstractItemModel]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAbstractItemModel *>
    #      QConcatenateTablesProxyModel::sourceModels() const
    address = self.uglySide.call(
        'ritual_ZNK28QConcatenateTablesProxyModel12sourceModelsEv',
    )
    return QList[QAbstractItemModel]._cuteOwning(address)

  @overload(QModelIndex)
  def mapFromSource(self, sourceIndex: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QConcatenateTablesProxyModel::mapFromSource(const
    QModelIndex &sourceIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#mapFromSource

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
    #  QModelIndex QConcatenateTablesProxyModel::mapFromSource(const
    #      QModelIndex &sourceIndex) const
    address = self.uglySide.call(
        'ritual_ZNK28QConcatenateTablesProxyModel13mapFromSourceERK11QModel'
        'Index',
        self._valueOf(sourceIndex),
    )
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def mapToSource(self, proxyIndex: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QConcatenateTablesProxyModel::mapToSource(const
    QModelIndex &proxyIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#mapToSource

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
    #  QModelIndex QConcatenateTablesProxyModel::mapToSource(const
    #      QModelIndex &proxyIndex) const
    address = self.uglySide.call(
        'ritual_ZNK28QConcatenateTablesProxyModel11mapToSourceERK11QModelIn'
        'dex',
        self._valueOf(proxyIndex),
    )
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int = 0) -> QVariant:
    """
    Calls Qt's 'QVariant QConcatenateTablesProxyModel::data(const QModelIndex
    &index, int role) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#data

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
    #  QVariant QConcatenateTablesProxyModel::data(const QModelIndex &index,
    #      int role) const
    ritual = 'ritual_ZNK28QConcatenateTablesProxyModel4dataERK11QModelIndexi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK28QConcatenateTablesProxyModel4dataERK11QModelInde'
          'xi')
    address = self.uglySide.call(ritual, self._valueOf(index), role)
    from . import QVariant
    return QVariant._cuteOwning(address)

  @overload(QModelIndex)
  def itemData(self, proxyIndex: QModelIndex) -> QMap[int, QVariant]:
    """
    Calls Qt's 'QMap<int, QVariant>
    QConcatenateTablesProxyModel::itemData(const QModelIndex &proxyIndex)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#itemData

    Parameters
    ----------

    proxyIndex : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QMap[int, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QMap<int, QVariant> QConcatenateTablesProxyModel::itemData(const
    #      QModelIndex &proxyIndex) const
    address = self.uglySide.call(
        'ritual_ZNK28QConcatenateTablesProxyModel8itemDataERK11QModelIndex',
        self._valueOf(proxyIndex),
    )
    from . import QVariant
    return QMap[int, QVariant]._cuteOwning(address)

  @overload(QModelIndex)
  def flags(self, index: QModelIndex) -> Qt.ItemFlags:
    """
    Calls Qt's 'Qt::ItemFlags QConcatenateTablesProxyModel::flags(const
    QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#flags

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
    #  Qt::ItemFlags QConcatenateTablesProxyModel::flags(const QModelIndex
    #      &index) const
    ritual = 'ritual_ZNK28QConcatenateTablesProxyModel5flagsERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK28QConcatenateTablesProxyModel5flagsERK11QModelInd'
          'ex')
    return Qt.ItemFlags(self.uglySide.call(ritual, self._valueOf(index)))

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def index(
      self,
      row: int,
      column: int,
      parent: Optional[QModelIndex] = None,
  ) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QConcatenateTablesProxyModel::index(int row, int
    column, const QModelIndex &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#index

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
    #  QModelIndex QConcatenateTablesProxyModel::index(int row, int column,
    #      const QModelIndex &parent) const
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    ritual = (
        'ritual_ZNK28QConcatenateTablesProxyModel5indexEiiRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK28QConcatenateTablesProxyModel5indexEiiRK11QModelI'
          'ndex')
    address = self.uglySide.call(ritual, row, column, self._valueOf(parent))
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def parent(self, index: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QConcatenateTablesProxyModel::parent(const
    QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#parent

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
    #  QModelIndex QConcatenateTablesProxyModel::parent(const QModelIndex
    #      &index) const
    ritual = (
        'ritual_ZNK28QConcatenateTablesProxyModel6parentERK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK28QConcatenateTablesProxyModel6parentERK11QModelIn'
          'dex')
    address = self.uglySide.call(ritual, self._valueOf(index))
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload()
  @overload(QModelIndex)
  def rowCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QConcatenateTablesProxyModel::rowCount(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#rowCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QConcatenateTablesProxyModel::rowCount(const QModelIndex &parent)
    #      const
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    ritual = (
        'ritual_ZNK28QConcatenateTablesProxyModel8rowCountERK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK28QConcatenateTablesProxyModel8rowCountERK11QModel'
          'Index')
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload(int, Qt.Orientation)
  @overload(int, Qt.Orientation, int)
  def headerData(
      self,
      section: int,
      orientation: Qt.Orientation,
      role: int = 0,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QConcatenateTablesProxyModel::headerData(int
    section, Qt::Orientation orientation, int role) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#headerData

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
    #  QVariant QConcatenateTablesProxyModel::headerData(int section,
    #      Qt::Orientation orientation, int role) const
    ritual = (
        'ritual_ZNK28QConcatenateTablesProxyModel10headerDataEiN2Qt11Orient'
        'ationEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK28QConcatenateTablesProxyModel10headerDataEiN2Qt11'
          'OrientationEi')
    address = self.uglySide.call(ritual, section, orientation.value, role)
    from . import QVariant
    return QVariant._cuteOwning(address)

  @overload()
  @overload(QModelIndex)
  def columnCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QConcatenateTablesProxyModel::columnCount(const
    QModelIndex &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#columnCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QConcatenateTablesProxyModel::columnCount(const QModelIndex
    #      &parent) const
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    ritual = (
        'ritual_ZNK28QConcatenateTablesProxyModel11columnCountERK11QModelIn'
        'dex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK28QConcatenateTablesProxyModel11columnCountERK11QM'
          'odelIndex')
    return self.uglySide.call(ritual, self._valueOf(parent))

  def mimeTypes(self) -> QStringList:
    """
    Calls Qt's 'QStringList QConcatenateTablesProxyModel::mimeTypes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#mimeTypes

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QConcatenateTablesProxyModel::mimeTypes() const
    address = self.uglySide.call(
        'ritual_ZNK28QConcatenateTablesProxyModel9mimeTypesEv',
    )
    return QStringList._cuteOwning(address)

  @overload(QList[QModelIndex])
  def mimeData(self, indexes: QList[QModelIndex]) -> Optional[QMimeData]:
    """
    Calls Qt's 'QMimeData *QConcatenateTablesProxyModel::mimeData(const
    QModelIndexList &indexes) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#mimeData

    Parameters
    ----------

    indexes : QList[QModelIndex]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    Optional[QMimeData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMimeData *QConcatenateTablesProxyModel::mimeData(const
    #      QModelIndexList &indexes) const
    address = self.uglySide.call(
        'ritual_ZNK28QConcatenateTablesProxyModel8mimeDataERK5QListI11QMode'
        'lIndexE',
        self._valueOf(indexes),
    )
    from . import QMimeData
    return QMimeData._cuteAt(address)

  @overload(QMimeData, Qt.DropAction, int, int, QModelIndex)
  @overload(NoneType, Qt.DropAction, int, int, QModelIndex)
  def canDropMimeData(
      self,
      data: Optional[QMimeData],
      action: Qt.DropAction,
      row: int,
      column: int,
      parent: QModelIndex,
  ) -> bool:
    """
    Calls Qt's 'bool QConcatenateTablesProxyModel::canDropMimeData(const
    QMimeData *data, Qt::DropAction action, int row, int column, const
    QModelIndex &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#canDropMimeData

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
    #  bool QConcatenateTablesProxyModel::canDropMimeData(const QMimeData
    #      *data, Qt::DropAction action, int row, int column, const
    #      QModelIndex &parent) const
    ritual = (
        'ritual_ZNK28QConcatenateTablesProxyModel15canDropMimeDataEPK9QMime'
        'DataN2Qt10DropActionEiiRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK28QConcatenateTablesProxyModel15canDropMimeDataEPK'
          '9QMimeDataN2Qt10DropActionEiiRK11QModelIndex')
    return self.uglySide.call(
        ritual,
        self._addressOf(data), action.value, row, column,
        self._valueOf(parent),
    )

  @overload(QModelIndex)
  def span(self, index: QModelIndex) -> QSize:
    """
    Calls Qt's 'QSize QConcatenateTablesProxyModel::span(const QModelIndex
    &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#span

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
    #  QSize QConcatenateTablesProxyModel::span(const QModelIndex &index)
    #      const
    ritual = 'ritual_ZNK28QConcatenateTablesProxyModel4spanERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK28QConcatenateTablesProxyModel4spanERK11QModelInde'
          'x')
    address = self.uglySide.call(ritual, self._valueOf(index))
    from . import QSize
    return QSize._cuteOwning(address)

  def roleNames(self) -> QHash[int, QByteArray]:
    """
    Calls Qt's 'QHash<int, QByteArray>
    QConcatenateTablesProxyModel::roleNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#roleNames

    Returns
    -------

    QHash[int, QByteArray]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<int, QByteArray> QConcatenateTablesProxyModel::roleNames() const
    address = self.uglySide.call(
        'ritual_ZNK28QConcatenateTablesProxyModel9roleNamesEv',
    )
    from . import QByteArray
    return QHash[int, QByteArray]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QModelIndex, QVariant)
  @overload(QModelIndex, QVariant, int)
  def setData(
      self,
      index: QModelIndex,
      value: QVariant,
      role: int = 2,
  ) -> bool:
    """
    Calls Qt's 'bool QConcatenateTablesProxyModel::setData(const QModelIndex
    &index, const QVariant &value, int role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#setData

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
    #  bool QConcatenateTablesProxyModel::setData(const QModelIndex &index,
    #      const QVariant &value, int role)
    ritual = (
        'ritual_ZN28QConcatenateTablesProxyModel7setDataERK11QModelIndexRK8'
        'QVarianti')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QConcatenateTablesProxyModel7setDataERK11QModelIn'
          'dexRK8QVarianti')
    return self.uglySide.call(
        ritual, self._valueOf(index), self._valueOf(value), role,
    )

  @overload(QModelIndex, QMap[int, QVariant])
  def setItemData(
      self,
      index: QModelIndex,
      roles: QMap[int, QVariant],
  ) -> bool:
    """
    Calls Qt's 'bool QConcatenateTablesProxyModel::setItemData(const
    QModelIndex &index, const QMap<int, QVariant> &roles)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#setItemData

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    roles : QMap[int, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  bool QConcatenateTablesProxyModel::setItemData(const QModelIndex
    #      &index, const QMap<int, QVariant> &roles)
    return self.uglySide.call(
        'ritual_ZN28QConcatenateTablesProxyModel11setItemDataERK11QModelInd'
        'exRK4QMapIi8QVariantE',
        self._valueOf(index), self._valueOf(roles),
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
    'QConcatenateTablesProxyModel::QConcatenateTablesProxyModel(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QConcatenateTablesProxyModel::QConcatenateTablesProxyModel(QObject
    #      *parent)
    self._noteCreation(QConcatenateTablesProxyModel, lambda: Rituals.call(
        'ritual_ZN28QConcatenateTablesProxyModelC1EP7QObject',
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

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def addSourceModel(
      self,
      sourceModel: Optional[QAbstractItemModel],
  ) -> None:
    """
    Calls Qt's 'void
    QConcatenateTablesProxyModel::addSourceModel(QAbstractItemModel
    *sourceModel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#addSourceModel

    Parameters
    ----------

    sourceModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QConcatenateTablesProxyModel::addSourceModel(QAbstractItemModel
    #      *sourceModel)
    self.uglySide.call(
        'ritual_ZN28QConcatenateTablesProxyModel14addSourceModelEP18QAbstra'
        'ctItemModel',
        self._addressOf(sourceModel),
    )

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def removeSourceModel(
      self,
      sourceModel: Optional[QAbstractItemModel],
  ) -> None:
    """
    Calls Qt's 'void
    QConcatenateTablesProxyModel::removeSourceModel(QAbstractItemModel
    *sourceModel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html

    Parameters
    ----------

    sourceModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QConcatenateTablesProxyModel::removeSourceModel(QAbstractItemModel
    #      *sourceModel)
    self.uglySide.call(
        'ritual_ZN28QConcatenateTablesProxyModel17removeSourceModelEP18QAbs'
        'tractItemModel',
        self._addressOf(sourceModel),
    )

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
    Calls Qt's 'bool QConcatenateTablesProxyModel::dropMimeData(const
    QMimeData *data, Qt::DropAction action, int row, int column, const
    QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconcatenatetablesproxymodel.html#dropMimeData

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
    #  bool QConcatenateTablesProxyModel::dropMimeData(const QMimeData *data,
    #      Qt::DropAction action, int row, int column, const QModelIndex
    #      &parent)
    ritual = (
        'ritual_ZN28QConcatenateTablesProxyModel12dropMimeDataEPK9QMimeData'
        'N2Qt10DropActionEiiRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QConcatenateTablesProxyModel12dropMimeDataEPK9QMi'
          'meDataN2Qt10DropActionEiiRK11QModelIndex')
    return self.uglySide.call(
        ritual,
        self._addressOf(data), action.value, row, column,
        self._valueOf(parent),
    )
