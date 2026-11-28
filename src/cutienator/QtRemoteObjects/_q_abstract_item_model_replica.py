"""
QAbstractItemModelReplica binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/qremoteobjectabstractitemmodelreplica.h, Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QAbstractItemModel, QHash
from . import QtRemoteObjects

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QItemSelectionModel, QMetaObject
  from ..QtCore import QModelIndex, QModelRoleDataSpan, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QModelRoleDataSpan = WAIT['QModelRoleDataSpan']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractItemModelReplica(QAbstractItemModel):
  """
  The cute side of Qt's QAbstractItemModelReplica: a plain Python object
  standing in front of one C++ QAbstractItemModelReplica.

  It is built on the cute 'QAbstractItemModel', as Qt's
  QAbstractItemModelReplica is built on Qt's QAbstractItemModel, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractItemModelReplica that has a ritual and that
  Python can call so far, 19 names in all: 'metaObject', 'tr',
  'selectionModel', 'data', 'multiData', 'setData', 'parent', 'index',
  'hasChildren', 'rowCount', 'columnCount', 'headerData', 'flags',
  'roleNames', 'isInitialized', 'hasData', 'rootCacheSize',
  'setRootCacheSize', 'initialized'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractItemModelReplica::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QAbstractItemModelReplica::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QAbstractItemModelReplica::~QAbstractItemModelReplica()': the
    destructor: Python never removes a C++ QAbstractItemModelReplica.
  - Qt's 'QList<int> QAbstractItemModelReplica::availableRoles() const':
    gives a type Python has no way to take yet.
  - Qt's 'QAbstractItemModelReplica::QAbstractItemModelReplica(
    QAbstractItemModelReplicaImplementation *rep,
    QtRemoteObjects::InitialAction action, const QList<int> &rolesHint)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 26 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QAbstractItemModelReplica is created at the first use, not by
    'QAbstractItemModelReplica(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractItemModelReplica.
  - Qt tells when it has removed the C++ QAbstractItemModelReplica. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QAbstractItemModelReplica that has no cute function
    yet, '__init__', 'availableRoles', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QAbstractItemModelReplica::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodelreplica.html#tr

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
    #  QString QAbstractItemModelReplica::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QAbstractItemModelReplica2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractItemModelReplica'

  #  A C++ QAbstractItemModelReplica Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractItemModelReplica'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAbstractItemModelReplica::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplica.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractItemModelReplica::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QAbstractItemModelReplica10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def selectionModel(self) -> Optional[QItemSelectionModel]:
    """
    Calls Qt's 'QItemSelectionModel
    *QAbstractItemModelReplica::selectionModel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplica.html#selectionModel

    Returns
    -------

    Optional[QItemSelectionModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QItemSelectionModel *QAbstractItemModelReplica::selectionModel() const
    address = self.uglySide.call(
        'ritual_ZNK25QAbstractItemModelReplica14selectionModelEv',
    )
    from ..QtCore import QItemSelectionModel
    return QItemSelectionModel._cuteAt(address)

  @overload(QModelIndex)
  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int = 0) -> QVariant:
    """
    Calls Qt's 'QVariant QAbstractItemModelReplica::data(const QModelIndex
    &index, int role) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplica.html#data

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
    #  QVariant QAbstractItemModelReplica::data(const QModelIndex &index, int
    #      role) const
    address = self.uglySide.call(
        'ritual_ZNK25QAbstractItemModelReplica4dataERK11QModelIndexi',
        self._valueOf(index), role,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QModelIndex)
  def parent(self, index: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QAbstractItemModelReplica::parent(const
    QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplica.html#parent

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
    #  QModelIndex QAbstractItemModelReplica::parent(const QModelIndex
    #      &index) const
    ritual = 'ritual_ZNK25QAbstractItemModelReplica6parentERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QAbstractItemModelReplica6parentERK11QModelIndex')
    address = self.uglySide.call(ritual, self._valueOf(index))
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
    Calls Qt's 'QModelIndex QAbstractItemModelReplica::index(int row, int
    column, const QModelIndex &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplica.html#index

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
    #  QModelIndex QAbstractItemModelReplica::index(int row, int column,
    #      const QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK25QAbstractItemModelReplica5indexEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QAbstractItemModelReplica5indexEiiRK11QModelInde'
          'x')
    address = self.uglySide.call(ritual, row, column, self._valueOf(parent))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload()
  @overload(QModelIndex)
  def hasChildren(self, parent: Optional[QModelIndex] = None) -> bool:
    """
    Calls Qt's 'bool QAbstractItemModelReplica::hasChildren(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplica.html#hasChildren

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QAbstractItemModelReplica::hasChildren(const QModelIndex &parent)
    #      const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = (
        'ritual_ZNK25QAbstractItemModelReplica11hasChildrenERK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QAbstractItemModelReplica11hasChildrenERK11QMode'
          'lIndex')
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload()
  @overload(QModelIndex)
  def rowCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QAbstractItemModelReplica::rowCount(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplica.html#rowCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QAbstractItemModelReplica::rowCount(const QModelIndex &parent)
    #      const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK25QAbstractItemModelReplica8rowCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QAbstractItemModelReplica8rowCountERK11QModelInd'
          'ex')
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload()
  @overload(QModelIndex)
  def columnCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QAbstractItemModelReplica::columnCount(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplica.html#columnCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QAbstractItemModelReplica::columnCount(const QModelIndex &parent)
    #      const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = (
        'ritual_ZNK25QAbstractItemModelReplica11columnCountERK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QAbstractItemModelReplica11columnCountERK11QMode'
          'lIndex')
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload(int, Qt.Orientation, int)
  def headerData(
      self,
      section: int,
      orientation: Qt.Orientation,
      role: int,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QAbstractItemModelReplica::headerData(int section,
    Qt::Orientation orientation, int role) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplica.html#headerData

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
    #  QVariant QAbstractItemModelReplica::headerData(int section,
    #      Qt::Orientation orientation, int role) const
    ritual = (
        'ritual_ZNK25QAbstractItemModelReplica10headerDataEiN2Qt11Orientati'
        'onEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QAbstractItemModelReplica10headerDataEiN2Qt11Ori'
          'entationEi')
    address = self.uglySide.call(ritual, section, orientation.value, role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QModelIndex)
  def flags(self, index: QModelIndex) -> Qt.ItemFlags:
    """
    Calls Qt's 'Qt::ItemFlags QAbstractItemModelReplica::flags(const
    QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplica.html#flags

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
    #  Qt::ItemFlags QAbstractItemModelReplica::flags(const QModelIndex
    #      &index) const
    ritual = 'ritual_ZNK25QAbstractItemModelReplica5flagsERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QAbstractItemModelReplica5flagsERK11QModelIndex')
    return Qt.ItemFlags(self.uglySide.call(ritual, self._valueOf(index)))

  def roleNames(self) -> QHash[int, QByteArray]:
    """
    Calls Qt's 'QHash<int, QByteArray> QAbstractItemModelReplica::roleNames()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplica.html#roleNames

    Returns
    -------

    QHash[int, QByteArray]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<int, QByteArray> QAbstractItemModelReplica::roleNames() const
    address = self.uglySide.call(
        'ritual_ZNK25QAbstractItemModelReplica9roleNamesEv',
    )
    from ..QtCore import QByteArray
    return QHash[int, QByteArray]._cuteOwning(address)

  def isInitialized(self) -> bool:
    """
    Calls Qt's 'bool QAbstractItemModelReplica::isInitialized() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplica.html#isInitialized
    """
    #  bool QAbstractItemModelReplica::isInitialized() const
    return self.uglySide.call(
        'ritual_ZNK25QAbstractItemModelReplica13isInitializedEv',
    )

  @overload(QModelIndex, int)
  def hasData(self, index: QModelIndex, role: int) -> bool:
    """
    Calls Qt's 'bool QAbstractItemModelReplica::hasData(const QModelIndex
    &index, int role) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplica.html#hasData

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    role : int
      Passed on as it is.
    """
    #  bool QAbstractItemModelReplica::hasData(const QModelIndex &index, int
    #      role) const
    return self.uglySide.call(
        'ritual_ZNK25QAbstractItemModelReplica7hasDataERK11QModelIndexi',
        self._valueOf(index), role,
    )

  def rootCacheSize(self) -> int:
    """
    Calls Qt's 'size_t QAbstractItemModelReplica::rootCacheSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplica.html#rootCacheSize
    """
    #  size_t QAbstractItemModelReplica::rootCacheSize() const
    return self.uglySide.call(
        'ritual_ZNK25QAbstractItemModelReplica13rootCacheSizeEv',
    )

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
    Calls Qt's 'bool QAbstractItemModelReplica::setData(const QModelIndex
    &index, const QVariant &value, int role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplica.html#setData

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
    #  bool QAbstractItemModelReplica::setData(const QModelIndex &index,
    #      const QVariant &value, int role)
    ritual = (
        'ritual_ZN25QAbstractItemModelReplica7setDataERK11QModelIndexRK8QVa'
        'rianti')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QAbstractItemModelReplica7setDataERK11QModelIndex'
          'RK8QVarianti')
    return self.uglySide.call(
        ritual, self._valueOf(index), self._valueOf(value), role,
    )

  @overload(int)
  def setRootCacheSize(self, rootCacheSize: int) -> None:
    """
    Calls Qt's 'void QAbstractItemModelReplica::setRootCacheSize(size_t
    rootCacheSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplica.html#setRootCacheSize

    Parameters
    ----------

    rootCacheSize : int
      Passed on as it is.
    """
    #  void QAbstractItemModelReplica::setRootCacheSize(size_t rootCacheSize)
    self.uglySide.call(
        'ritual_ZN25QAbstractItemModelReplica16setRootCacheSizeEm',
        rootCacheSize,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QAbstractItemModelReplica::QAbstractItemModelReplica(
    QAbstractItemModelReplicaImplementation *rep,
    QtRemoteObjects::InitialAction action, const QList<int> &rolesHint)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractItemModelReplica.__init__' has no cute function yet. "
        "Qt's "
        "'QAbstractItemModelReplica::QAbstractItemModelReplica(QAbstractItem"
        "ModelReplicaImplementation *rep, QtRemoteObjects::InitialAction "
        "action, const QList<int> &rolesHint)': takes a type Python has no "
        "way to hand over yet.")

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

  @overload(QModelIndex, QModelRoleDataSpan)
  def multiData(
      self,
      index: QModelIndex,
      roleDataSpan: QModelRoleDataSpan,
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemModelReplica::multiData(const QModelIndex
    &index, QModelRoleDataSpan roleDataSpan) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplica.html#multiData

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    roleDataSpan : QModelRoleDataSpan
      Passed on as a value: Qt reads the C++ QModelRoleDataSpan, which stays
      Python's own.
    """
    #  void QAbstractItemModelReplica::multiData(const QModelIndex &index,
    #      QModelRoleDataSpan roleDataSpan) const
    ritual = (
        'ritual_ZNK25QAbstractItemModelReplica9multiDataERK11QModelIndex18Q'
        'ModelRoleDataSpan')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QAbstractItemModelReplica9multiDataERK11QModelIn'
          'dex18QModelRoleDataSpan')
    self.uglySide.call(
        ritual, self._valueOf(index), self._valueOf(roleDataSpan),
    )

  def initialized(self) -> None:
    """
    Calls Qt's 'void QAbstractItemModelReplica::initialized()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelreplica.html#initialized
    """
    #  void QAbstractItemModelReplica::initialized()
    self.uglySide.call('ritual_ZN25QAbstractItemModelReplica11initializedEv')

  @staticmethod
  def availableRoles(*__, **_) -> Never:
    """
    Qt's 'QList<int> QAbstractItemModelReplica::availableRoles() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAbstractItemModelReplica.availableRoles' has no cute function "
        "yet. Qt's 'QList<int> QAbstractItemModelReplica::availableRoles() "
        "const': gives a type Python has no way to take yet.")
