"""
QAbstractItemModelSourceAdapter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectabstractitemmodeladapter_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QAbstractItemModelSourceAdapter to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QAbstractItemModel, QHash, QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QItemSelectionModel, QMetaObject
  from ..QtCore import QModelIndex, QPersistentModelIndex
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QPersistentModelIndex = WAIT['QPersistentModelIndex']


class QAbstractItemModelSourceAdapter(QObject):
  """
  The cute side of Qt's QAbstractItemModelSourceAdapter: a plain Python
  object standing in front of one C++ QAbstractItemModelSourceAdapter.

  It is built on the cute 'QObject', as Qt's QAbstractItemModelSourceAdapter
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractItemModelSourceAdapter that has a ritual
  and that Python can call so far, 9 names in all: 'metaObject',
  'selectionModel', 'roleNames', 'sourceRowsInserted',
  'sourceColumnsInserted', 'sourceRowsRemoved', 'sourceCurrentChanged',
  'sourceLayoutChanged', 'availableRolesChanged'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractItemModelSourceAdapter::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QAbstractItemModelSourceAdapter::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QList<int> QAbstractItemModelSourceAdapter::availableRoles()
    const': gives a type Python has no way to take yet.
  - Qt's 'QSize
    QAbstractItemModelSourceAdapter::replicaSizeRequest(QtPrivate::IndexList
    parentList)': takes a type Python has no way to hand over yet.
  - Qt's 'QtPrivate::DataEntries
    QAbstractItemModelSourceAdapter::replicaRowRequest(QtPrivate::IndexList
    start, QtPrivate::IndexList end, QList<int> roles)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QVariantList
    QAbstractItemModelSourceAdapter::replicaHeaderRequest(QList<Qt::
    Orientation> orientations, QList<int> sections, QList<int> roles)': takes
    a type Python has no way to hand over yet.
  - Qt's 'QtPrivate::MetaAndDataEntries
    QAbstractItemModelSourceAdapter::replicaCacheRequest(size_t size, const
    QList<int> &roles)': takes a type Python has no way to hand over yet.
  - Qt's 'void
    QAbstractItemModelSourceAdapter::currentChanged(QtPrivate::IndexList
    current, QtPrivate::IndexList previous)': takes a type Python has no way
    to hand over yet.
  - Qt's 'void
    QAbstractItemModelSourceAdapter::layoutChanged(QtPrivate::IndexList
    parents, QAbstractItemModel::LayoutChangeHint hint)': takes a type Python
    has no way to hand over yet.

  What has no ritual
  ------------------

  17 of the 35 functions Qt declares: 9 the compiler refuses its ritual as it
  would be written here; 2 not a gap; 2 leans on
  'QAbstractItemModelSourceAdapter; 2 leans on
  'qRegisterNormalizedMetaType_QIntHash(QByteArray const&)', which Qt's
  source does not mark for use from outside Qt and has no code for that could
  be taken; 1 cannot be called and cannot be called through the meta-object
  and cannot be copied; 1 Qt's library has no name for it, and its code in
  Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QAbstractItemModelSourceAdapter is created at the first use, not
    by 'QAbstractItemModelSourceAdapter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractItemModelSourceAdapter.
  - Qt tells when it has removed the C++ QAbstractItemModelSourceAdapter.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QAbstractItemModelSourceAdapter that has no cute
    function yet, '__init__', 'availableRoles', 'columnsInserted',
    'currentChanged', 'dataChanged', 'fetchTree', 'layoutChanged',
    'registerTypes', 'replicaCacheRequest', 'replicaHeaderRequest',
    'replicaRowRequest', 'replicaSetCurrentIndex', 'replicaSetData',
    'replicaSizeRequest', 'rowsInserted', 'rowsMoved', 'rowsRemoved',
    'setAvailableRoles', 'sourceDataChanged', 'sourceRowsMoved', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractItemModelSourceAdapter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QAbstractItemModelSourceAdapter::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelsourceadapter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractItemModelSourceAdapter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK31QAbstractItemModelSourceAdapter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def selectionModel(self) -> Optional[QItemSelectionModel]:
    """
    Calls Qt's 'QItemSelectionModel
    *QAbstractItemModelSourceAdapter::selectionModel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelsourceadapter.html

    Returns
    -------

    Optional[QItemSelectionModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QItemSelectionModel *QAbstractItemModelSourceAdapter::selectionModel()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK31QAbstractItemModelSourceAdapter14selectionModelEv',
    )
    from ..QtCore import QItemSelectionModel
    return QItemSelectionModel._cuteAt(address)

  def roleNames(self) -> QHash[int, QByteArray]:
    """
    Calls Qt's 'QIntHash QAbstractItemModelSourceAdapter::roleNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelsourceadapter.html#roleNames

    Returns
    -------

    QHash[int, QByteArray]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QIntHash QAbstractItemModelSourceAdapter::roleNames() const
    address = self.uglySide.call(
        'ritual_ZNK31QAbstractItemModelSourceAdapter9roleNamesEv',
    )
    from ..QtCore import QByteArray
    return QHash[int, QByteArray]._cuteOwning(address)

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
    - Qt's
      'QAbstractItemModelSourceAdapter::QAbstractItemModelSourceAdapter()':
      cannot be called and cannot be called through the meta-object and
      cannot be copied: no header file has its code, Qt's source does not
      mark it or its class for use from outside Qt or writes it 'inline' or
      nowhere, and it is no signal, slot or invokable function giving back
      nothing, of a class built on QObject, and Qt's source has no code for
      it that could be told from the rest.
    - Qt's 'QAbstractItemModelSourceAdapter::QAbstractItemModelSourceAdapter(
      QAbstractItemModel *object, QItemSelectionModel *sel, const QList<int>
      &roles)': leans on 'qRegisterNormalizedMetaType_QIntHash(QByteArray
      const&)', which Qt's source does not mark for use from outside Qt and
      has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QAbstractItemModelSourceAdapter.__init__' has no cute function "
        "yet. Qt's "
        "'QAbstractItemModelSourceAdapter::QAbstractItemModelSourceAdapter()"
        "': cannot be called and cannot be called through the meta-object "
        "and cannot be copied: no header file has its code, Qt's source "
        "does not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest. "
        "Qt's "
        "'QAbstractItemModelSourceAdapter::QAbstractItemModelSourceAdapter(Q"
        "AbstractItemModel *object, QItemSelectionModel *sel, const "
        "QList<int> &roles)': leans on "
        "'qRegisterNormalizedMetaType_QIntHash(QByteArray const&)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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

  @overload(QModelIndex, int, int)
  def sourceRowsInserted(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractItemModelSourceAdapter::sourceRowsInserted(const QModelIndex
    &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelsourceadapter.html

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
    #  void QAbstractItemModelSourceAdapter::sourceRowsInserted(const
    #      QModelIndex &parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN31QAbstractItemModelSourceAdapter18sourceRowsInsertedERK1'
        '1QModelIndexii',
        self._valueOf(parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def sourceColumnsInserted(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractItemModelSourceAdapter::sourceColumnsInserted(const QModelIndex
    &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelsourceadapter.html

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
    #  void QAbstractItemModelSourceAdapter::sourceColumnsInserted(const
    #      QModelIndex &parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN31QAbstractItemModelSourceAdapter21sourceColumnsInsertedE'
        'RK11QModelIndexii',
        self._valueOf(parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def sourceRowsRemoved(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemModelSourceAdapter::sourceRowsRemoved(const
    QModelIndex &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelsourceadapter.html

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
    #  void QAbstractItemModelSourceAdapter::sourceRowsRemoved(const
    #      QModelIndex &parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN31QAbstractItemModelSourceAdapter17sourceRowsRemovedERK11'
        'QModelIndexii',
        self._valueOf(parent), start, end,
    )

  @overload(QModelIndex, QModelIndex)
  def sourceCurrentChanged(
      self,
      current: QModelIndex,
      previous: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractItemModelSourceAdapter::sourceCurrentChanged(const QModelIndex
    &current, const QModelIndex &previous)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelsourceadapter.html

    Parameters
    ----------

    current : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    previous : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QAbstractItemModelSourceAdapter::sourceCurrentChanged(const
    #      QModelIndex &current, const QModelIndex &previous)
    self.uglySide.call(
        'ritual_ZN31QAbstractItemModelSourceAdapter20sourceCurrentChangedER'
        'K11QModelIndexS2_',
        self._valueOf(current), self._valueOf(previous),
    )

  @overload(
      QList[QPersistentModelIndex], QAbstractItemModel.LayoutChangeHint,
  )
  def sourceLayoutChanged(
      self,
      parents: QList[QPersistentModelIndex],
      hint: QAbstractItemModel.LayoutChangeHint,
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractItemModelSourceAdapter::sourceLayoutChanged(const
    QList<QPersistentModelIndex> &parents,
    QAbstractItemModel::LayoutChangeHint hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelsourceadapter.html

    Parameters
    ----------

    parents : QList[QPersistentModelIndex]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    hint : QAbstractItemModel.LayoutChangeHint
      Passed on as its number.
    """
    #  void QAbstractItemModelSourceAdapter::sourceLayoutChanged(const
    #      QList<QPersistentModelIndex> &parents,
    #      QAbstractItemModel::LayoutChangeHint hint)
    self.uglySide.call(
        'ritual_ZN31QAbstractItemModelSourceAdapter19sourceLayoutChangedERK'
        '5QListI21QPersistentModelIndexEN18QAbstractItemModel16LayoutChange'
        'HintE',
        self._valueOf(parents), hint.value,
    )

  def availableRolesChanged(self) -> None:
    """
    Calls Qt's 'void
    QAbstractItemModelSourceAdapter::availableRolesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelsourceadapter.html
    """
    #  void QAbstractItemModelSourceAdapter::availableRolesChanged()
    self.uglySide.call(
        'ritual_ZN31QAbstractItemModelSourceAdapter21availableRolesChangedE'
        'v',
    )

  @staticmethod
  def availableRoles(*__, **_) -> Never:
    """
    Qt's 'QList<int> QAbstractItemModelSourceAdapter::availableRoles()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAbstractItemModelSourceAdapter.availableRoles' has no cute "
        "function yet. Qt's 'QList<int> "
        "QAbstractItemModelSourceAdapter::availableRoles() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def columnsInserted(*__, **_) -> Never:
    """
    Qt's 'void
    QAbstractItemModelSourceAdapter::columnsInserted(QtPrivate::IndexList
    parent, int start, int end) const': the compiler refuses its ritual as it
    would be written here: static_cast from 'const
    QAbstractItemModelSourceAdapter *' to 'QObject *', which are not related
    by inheritance, is not allowed.
    """
    raise NotImplementedError(
        "'QAbstractItemModelSourceAdapter.columnsInserted' has no cute "
        "function yet. Qt's 'void "
        "QAbstractItemModelSourceAdapter::columnsInserted(QtPrivate::IndexLi"
        "st parent, int start, int end) const': the compiler refuses its "
        "ritual as it would be written here: static_cast from 'const "
        "QAbstractItemModelSourceAdapter *' to 'QObject *', which are not "
        "related by inheritance, is not allowed.")

  @staticmethod
  def currentChanged(*__, **_) -> Never:
    """
    Qt's 'void
    QAbstractItemModelSourceAdapter::currentChanged(QtPrivate::IndexList
    current, QtPrivate::IndexList previous)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractItemModelSourceAdapter.currentChanged' has no cute "
        "function yet. Qt's 'void "
        "QAbstractItemModelSourceAdapter::currentChanged(QtPrivate::IndexLis"
        "t current, QtPrivate::IndexList previous)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def dataChanged(*__, **_) -> Never:
    """
    Qt's 'void
    QAbstractItemModelSourceAdapter::dataChanged(QtPrivate::IndexList
    topLeft, QtPrivate::IndexList bottomRight, QList<int> roles) const': the
    compiler refuses its ritual as it would be written here: static_cast from
    'const QAbstractItemModelSourceAdapter *' to 'QObject *', which are not
    related by inheritance, is not allowed.
    """
    raise NotImplementedError(
        "'QAbstractItemModelSourceAdapter.dataChanged' has no cute function "
        "yet. Qt's 'void "
        "QAbstractItemModelSourceAdapter::dataChanged(QtPrivate::IndexList "
        "topLeft, QtPrivate::IndexList bottomRight, QList<int> roles) "
        "const': the compiler refuses its ritual as it would be written "
        "here: static_cast from 'const QAbstractItemModelSourceAdapter *' "
        "to 'QObject *', which are not related by inheritance, is not "
        "allowed.")

  @staticmethod
  def fetchTree(*__, **_) -> Never:
    """
    Qt's 'QList<QtPrivate::IndexValuePair>
    QAbstractItemModelSourceAdapter::fetchTree(const QModelIndex &parent,
    size_t &size, const QList<int> &roles)': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'createModelRoleData'; did you mean
    'QModelRoleData'?.
    """
    raise NotImplementedError(
        "'QAbstractItemModelSourceAdapter.fetchTree' has no cute function "
        "yet. Qt's 'QList<QtPrivate::IndexValuePair> "
        "QAbstractItemModelSourceAdapter::fetchTree(const QModelIndex "
        "&parent, size_t &size, const QList<int> &roles)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'createModelRoleData'; "
        "did you mean 'QModelRoleData'?.")

  @staticmethod
  def layoutChanged(*__, **_) -> Never:
    """
    Qt's 'void
    QAbstractItemModelSourceAdapter::layoutChanged(QtPrivate::IndexList
    parents, QAbstractItemModel::LayoutChangeHint hint)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractItemModelSourceAdapter.layoutChanged' has no cute "
        "function yet. Qt's 'void "
        "QAbstractItemModelSourceAdapter::layoutChanged(QtPrivate::IndexList"
        " parents, QAbstractItemModel::LayoutChangeHint hint)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def registerTypes(*__, **_) -> Never:
    """
    Qt's 'void QAbstractItemModelSourceAdapter::registerTypes()': leans on
    'qRegisterNormalizedMetaType_QIntHash(QByteArray const&)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QAbstractItemModelSourceAdapter.registerTypes' has no cute "
        "function yet. Qt's 'void "
        "QAbstractItemModelSourceAdapter::registerTypes()': leans on "
        "'qRegisterNormalizedMetaType_QIntHash(QByteArray const&)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def replicaCacheRequest(*__, **_) -> Never:
    """
    Qt's 'QtPrivate::MetaAndDataEntries
    QAbstractItemModelSourceAdapter::replicaCacheRequest(size_t size, const
    QList<int> &roles)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractItemModelSourceAdapter.replicaCacheRequest' has no cute "
        "function yet. Qt's 'QtPrivate::MetaAndDataEntries "
        "QAbstractItemModelSourceAdapter::replicaCacheRequest(size_t size, "
        "const QList<int> &roles)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def replicaHeaderRequest(*__, **_) -> Never:
    """
    Qt's 'QVariantList
    QAbstractItemModelSourceAdapter::replicaHeaderRequest(QList<Qt::
    Orientation> orientations, QList<int> sections, QList<int> roles)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractItemModelSourceAdapter.replicaHeaderRequest' has no cute "
        "function yet. Qt's 'QVariantList "
        "QAbstractItemModelSourceAdapter::replicaHeaderRequest(QList<Qt::Ori"
        "entation> orientations, QList<int> sections, QList<int> roles)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def replicaRowRequest(*__, **_) -> Never:
    """
    Qt's 'QtPrivate::DataEntries
    QAbstractItemModelSourceAdapter::replicaRowRequest(QtPrivate::IndexList
    start, QtPrivate::IndexList end, QList<int> roles)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractItemModelSourceAdapter.replicaRowRequest' has no cute "
        "function yet. Qt's 'QtPrivate::DataEntries "
        "QAbstractItemModelSourceAdapter::replicaRowRequest(QtPrivate::Index"
        "List start, QtPrivate::IndexList end, QList<int> roles)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def replicaSetCurrentIndex(*__, **_) -> Never:
    """
    Qt's 'void
    QAbstractItemModelSourceAdapter::replicaSetCurrentIndex(QtPrivate::
    IndexList index, QItemSelectionModel::SelectionFlags command)': the
    compiler refuses its ritual as it would be written here: redefinition of
    'index' with a different type: 'const int' vs 'const QtPrivate::IndexList
    *' (aka 'const QList<ModelIndex> *').
    """
    raise NotImplementedError(
        "'QAbstractItemModelSourceAdapter.replicaSetCurrentIndex' has no "
        "cute function yet. Qt's 'void "
        "QAbstractItemModelSourceAdapter::replicaSetCurrentIndex(QtPrivate::"
        "IndexList index, QItemSelectionModel::SelectionFlags command)': "
        "the compiler refuses its ritual as it would be written here: "
        "redefinition of 'index' with a different type: 'const int' vs "
        "'const QtPrivate::IndexList *' (aka 'const QList<ModelIndex> *').")

  @staticmethod
  def replicaSetData(*__, **_) -> Never:
    """
    Qt's 'void QAbstractItemModelSourceAdapter::replicaSetData(const
    QtPrivate::IndexList &index, const QVariant &value, int role)': the
    compiler refuses its ritual as it would be written here: redefinition of
    'index' with a different type: 'const int' vs 'const QtPrivate::IndexList
    *' (aka 'const QList<ModelIndex> *').
    """
    raise NotImplementedError(
        "'QAbstractItemModelSourceAdapter.replicaSetData' has no cute "
        "function yet. Qt's 'void "
        "QAbstractItemModelSourceAdapter::replicaSetData(const "
        "QtPrivate::IndexList &index, const QVariant &value, int role)': "
        "the compiler refuses its ritual as it would be written here: "
        "redefinition of 'index' with a different type: 'const int' vs "
        "'const QtPrivate::IndexList *' (aka 'const QList<ModelIndex> *').")

  @staticmethod
  def replicaSizeRequest(*__, **_) -> Never:
    """
    Qt's 'QSize
    QAbstractItemModelSourceAdapter::replicaSizeRequest(QtPrivate::IndexList
    parentList)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractItemModelSourceAdapter.replicaSizeRequest' has no cute "
        "function yet. Qt's 'QSize "
        "QAbstractItemModelSourceAdapter::replicaSizeRequest(QtPrivate::Inde"
        "xList parentList)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def rowsInserted(*__, **_) -> Never:
    """
    Qt's 'void
    QAbstractItemModelSourceAdapter::rowsInserted(QtPrivate::IndexList
    parent, int start, int end) const': the compiler refuses its ritual as it
    would be written here: static_cast from 'const
    QAbstractItemModelSourceAdapter *' to 'QObject *', which are not related
    by inheritance, is not allowed.
    """
    raise NotImplementedError(
        "'QAbstractItemModelSourceAdapter.rowsInserted' has no cute "
        "function yet. Qt's 'void "
        "QAbstractItemModelSourceAdapter::rowsInserted(QtPrivate::IndexList "
        "parent, int start, int end) const': the compiler refuses its "
        "ritual as it would be written here: static_cast from 'const "
        "QAbstractItemModelSourceAdapter *' to 'QObject *', which are not "
        "related by inheritance, is not allowed.")

  @staticmethod
  def rowsMoved(*__, **_) -> Never:
    """
    Qt's 'void
    QAbstractItemModelSourceAdapter::rowsMoved(QtPrivate::IndexList
    sourceParent, int sourceRow, int count, QtPrivate::IndexList
    destinationParent, int destinationChild) const': the compiler refuses its
    ritual as it would be written here: static_cast from 'const
    QAbstractItemModelSourceAdapter *' to 'QObject *', which are not related
    by inheritance, is not allowed.
    """
    raise NotImplementedError(
        "'QAbstractItemModelSourceAdapter.rowsMoved' has no cute function "
        "yet. Qt's 'void "
        "QAbstractItemModelSourceAdapter::rowsMoved(QtPrivate::IndexList "
        "sourceParent, int sourceRow, int count, QtPrivate::IndexList "
        "destinationParent, int destinationChild) const': the compiler "
        "refuses its ritual as it would be written here: static_cast from "
        "'const QAbstractItemModelSourceAdapter *' to 'QObject *', which "
        "are not related by inheritance, is not allowed.")

  @staticmethod
  def rowsRemoved(*__, **_) -> Never:
    """
    Qt's 'void
    QAbstractItemModelSourceAdapter::rowsRemoved(QtPrivate::IndexList parent,
    int start, int end) const': the compiler refuses its ritual as it would
    be written here: static_cast from 'const QAbstractItemModelSourceAdapter
    *' to 'QObject *', which are not related by inheritance, is not allowed.
    """
    raise NotImplementedError(
        "'QAbstractItemModelSourceAdapter.rowsRemoved' has no cute function "
        "yet. Qt's 'void "
        "QAbstractItemModelSourceAdapter::rowsRemoved(QtPrivate::IndexList "
        "parent, int start, int end) const': the compiler refuses its "
        "ritual as it would be written here: static_cast from 'const "
        "QAbstractItemModelSourceAdapter *' to 'QObject *', which are not "
        "related by inheritance, is not allowed.")

  @staticmethod
  def setAvailableRoles(*__, **_) -> Never:
    """
    Qt's 'void QAbstractItemModelSourceAdapter::setAvailableRoles(QList<int>
    availableRoles)': leans on
    'QAbstractItemModelSourceAdapter::availableRolesChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QAbstractItemModelSourceAdapter.setAvailableRoles' has no cute "
        "function yet. Qt's 'void "
        "QAbstractItemModelSourceAdapter::setAvailableRoles(QList<int> "
        "availableRoles)': leans on "
        "'QAbstractItemModelSourceAdapter::availableRolesChanged()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def sourceDataChanged(*__, **_) -> Never:
    """
    Qt's 'void QAbstractItemModelSourceAdapter::sourceDataChanged(const
    QModelIndex &topLeft, const QModelIndex &bottomRight, const QList<int>
    &roles) const': the compiler refuses its ritual as it would be written
    here: static_cast from 'const QAbstractItemModelSourceAdapter *' to
    'QObject *', which are not related by inheritance, is not allowed.
    """
    raise NotImplementedError(
        "'QAbstractItemModelSourceAdapter.sourceDataChanged' has no cute "
        "function yet. Qt's 'void "
        "QAbstractItemModelSourceAdapter::sourceDataChanged(const "
        "QModelIndex &topLeft, const QModelIndex &bottomRight, const "
        "QList<int> &roles) const': the compiler refuses its ritual as it "
        "would be written here: static_cast from 'const "
        "QAbstractItemModelSourceAdapter *' to 'QObject *', which are not "
        "related by inheritance, is not allowed.")

  @staticmethod
  def sourceRowsMoved(*__, **_) -> Never:
    """
    Qt's 'void QAbstractItemModelSourceAdapter::sourceRowsMoved(const
    QModelIndex &sourceParent, int sourceRow, int count, const QModelIndex
    &destinationParent, int destinationChild) const': the compiler refuses
    its ritual as it would be written here: static_cast from 'const
    QAbstractItemModelSourceAdapter *' to 'QObject *', which are not related
    by inheritance, is not allowed.
    """
    raise NotImplementedError(
        "'QAbstractItemModelSourceAdapter.sourceRowsMoved' has no cute "
        "function yet. Qt's 'void "
        "QAbstractItemModelSourceAdapter::sourceRowsMoved(const QModelIndex "
        "&sourceParent, int sourceRow, int count, const QModelIndex "
        "&destinationParent, int destinationChild) const': the compiler "
        "refuses its ritual as it would be written here: static_cast from "
        "'const QAbstractItemModelSourceAdapter *' to 'QObject *', which "
        "are not related by inheritance, is not allowed.")
