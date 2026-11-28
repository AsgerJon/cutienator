"""
QCompletionModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qcompleter_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QCompletionModel to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QAbstractItemModel, QAbstractProxyModel, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QModelIndex, QVariant
  from . import QCompletionModelPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCompletionModel(QAbstractProxyModel):
  """
  The cute side of Qt's QCompletionModel: a plain Python object standing in
  front of one C++ QCompletionModel.

  It is built on the cute 'QAbstractProxyModel', as Qt's QCompletionModel is
  built on Qt's QAbstractProxyModel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCompletionModel that has a ritual and that Python
  can call so far, 22 names in all: 'metaObject', 'createEngine',
  'setFiltered', 'filter', 'completionCount', 'currentRow', 'setCurrentRow',
  'currentIndex', 'index', 'rowCount', 'columnCount', 'hasChildren',
  'parent', 'data', 'setSourceModel', 'mapToSource', 'mapFromSource',
  'd_func', 'rowsAdded', 'invalidate', 'rowsInserted', 'modelDestroyed'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCompletionModel::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QCompletionModel::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QCompletionModelPrivate *QCompletionModel::d_func() const':
    takes in Python what 'QCompletionModelPrivate
    *QCompletionModel::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 29 functions Qt declares: 2 not a gap; 2 leans on
  'QCompletionModel.

  What to expect
  --------------

  - The C++ QCompletionModel is created at the first use, not by
    'QCompletionModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCompletionModel.
  - Qt tells when it has removed the C++ QCompletionModel. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QCompletionModel that has no cute function yet,
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
  __qt_class__ = 'QCompletionModel'

  #  A C++ QCompletionModel Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCompletionModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCompletionModel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompletionmodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCompletionModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QCompletionModel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def completionCount(self) -> int:
    """
    Calls Qt's 'int QCompletionModel::completionCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcompletionmodel.html#completionCount
    """
    #  int QCompletionModel::completionCount() const
    return self.uglySide.call(
        'ritual_ZNK16QCompletionModel15completionCountEv',
    )

  def currentRow(self) -> int:
    """
    Calls Qt's 'int QCompletionModel::currentRow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompletionmodel.html#currentRow
    """
    #  int QCompletionModel::currentRow() const
    return self.uglySide.call('ritual_ZNK16QCompletionModel10currentRowEv')

  @overload(bool)
  def currentIndex(self, a0: bool) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QCompletionModel::currentIndex(bool a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompletionmodel.html#currentIndex

    Parameters
    ----------

    a0 : bool
      Passed on as it is.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QCompletionModel::currentIndex(bool a0) const
    address = self.uglySide.call(
        'ritual_ZNK16QCompletionModel12currentIndexEb', a0,
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def index(
      self,
      row: int,
      column: int,
      a2: Optional[QModelIndex] = None,
  ) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QCompletionModel::index(int row, int column,
    const QModelIndex &a2) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompletionmodel.html#index

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    a2 : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QCompletionModel::index(int row, int column, const
    #      QModelIndex &a2) const
    if a2 is None:
      from ..QtCore import QModelIndex
      a2 = QModelIndex()
    ritual = 'ritual_ZNK16QCompletionModel5indexEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QCompletionModel5indexEiiRK11QModelIndex'
    address = self.uglySide.call(ritual, row, column, self._valueOf(a2))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload()
  @overload(QModelIndex)
  def rowCount(self, index: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QCompletionModel::rowCount(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompletionmodel.html#rowCount

    Parameters
    ----------

    index : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QCompletionModel::rowCount(const QModelIndex &index) const
    if index is None:
      from ..QtCore import QModelIndex
      index = QModelIndex()
    ritual = 'ritual_ZNK16QCompletionModel8rowCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QCompletionModel8rowCountERK11QModelIndex'
    return self.uglySide.call(ritual, self._valueOf(index))

  @overload()
  @overload(QModelIndex)
  def columnCount(self, index: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QCompletionModel::columnCount(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompletionmodel.html#columnCount

    Parameters
    ----------

    index : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QCompletionModel::columnCount(const QModelIndex &index) const
    if index is None:
      from ..QtCore import QModelIndex
      index = QModelIndex()
    ritual = 'ritual_ZNK16QCompletionModel11columnCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QCompletionModel11columnCountERK11QModelIndex')
    return self.uglySide.call(ritual, self._valueOf(index))

  @overload()
  @overload(QModelIndex)
  def hasChildren(self, parent: Optional[QModelIndex] = None) -> bool:
    """
    Calls Qt's 'bool QCompletionModel::hasChildren(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompletionmodel.html#hasChildren

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QCompletionModel::hasChildren(const QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK16QCompletionModel11hasChildrenERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QCompletionModel11hasChildrenERK11QModelIndex')
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload()
  @overload(QModelIndex)
  def parent(self, a0: Optional[QModelIndex] = None) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QCompletionModel::parent(const QModelIndex &a0)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompletionmodel.html#parent

    Parameters
    ----------

    a0 : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QCompletionModel::parent(const QModelIndex &a0) const
    if a0 is None:
      from ..QtCore import QModelIndex
      a0 = QModelIndex()
    ritual = 'ritual_ZNK16QCompletionModel6parentERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QCompletionModel6parentERK11QModelIndex'
    address = self.uglySide.call(ritual, self._valueOf(a0))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int = 0) -> QVariant:
    """
    Calls Qt's 'QVariant QCompletionModel::data(const QModelIndex &index, int
    role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompletionmodel.html#data

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
    #  QVariant QCompletionModel::data(const QModelIndex &index, int role)
    #      const
    ritual = 'ritual_ZNK16QCompletionModel4dataERK11QModelIndexi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QCompletionModel4dataERK11QModelIndexi'
    address = self.uglySide.call(ritual, self._valueOf(index), role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QModelIndex)
  def mapToSource(self, proxyIndex: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QCompletionModel::mapToSource(const QModelIndex
    &proxyIndex) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompletionmodel.html#mapToSource

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
    #  QModelIndex QCompletionModel::mapToSource(const QModelIndex
    #      &proxyIndex) const
    ritual = 'ritual_ZNK16QCompletionModel11mapToSourceERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QCompletionModel11mapToSourceERK11QModelIndex')
    address = self.uglySide.call(ritual, self._valueOf(proxyIndex))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def mapFromSource(self, sourceIndex: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QCompletionModel::mapFromSource(const QModelIndex
    &sourceIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcompletionmodel.html#mapFromSource

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
    #  QModelIndex QCompletionModel::mapFromSource(const QModelIndex
    #      &sourceIndex) const
    ritual = 'ritual_ZNK16QCompletionModel13mapFromSourceERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QCompletionModel13mapFromSourceERK11QModelIndex')
    address = self.uglySide.call(ritual, self._valueOf(sourceIndex))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setFiltered(self, a0: bool) -> None:
    """
    Calls Qt's 'void QCompletionModel::setFiltered(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qcompletionmodel.html#setFiltered

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QCompletionModel::setFiltered(bool a0)
    self.uglySide.call('ritual_ZN16QCompletionModel11setFilteredEb', a0)

  @overload(int)
  def setCurrentRow(self, row: int) -> bool:
    """
    Calls Qt's 'bool QCompletionModel::setCurrentRow(int row)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcompletionmodel.html#setCurrentRow

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  bool QCompletionModel::setCurrentRow(int row)
    return self.uglySide.call(
        'ritual_ZN16QCompletionModel13setCurrentRowEi', row,
    )

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setSourceModel(
      self,
      sourceModel: Optional[QAbstractItemModel],
  ) -> None:
    """
    Calls Qt's 'void QCompletionModel::setSourceModel(QAbstractItemModel
    *sourceModel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcompletionmodel.html#setSourceModel

    Parameters
    ----------

    sourceModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCompletionModel::setSourceModel(QAbstractItemModel *sourceModel)
    ritual = (
        'ritual_ZN16QCompletionModel14setSourceModelEP18QAbstractItemModel')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QCompletionModel14setSourceModelEP18QAbstractItem'
          'Model')
    self.uglySide.call(ritual, self._addressOf(sourceModel))

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
    Qt's 'QCompletionModel::QCompletionModel(QCompleterPrivate *c, QObject
    *parent)': leans on 'QCompletionModel::qt_metacall(QMetaObject::Call,
    int, void**)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCompletionModel.__init__' has no cute function yet. Qt's "
        "'QCompletionModel::QCompletionModel(QCompleterPrivate *c, QObject "
        "*parent)': leans on "
        "'QCompletionModel::qt_metacall(QMetaObject::Call, int, void**)', "
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

  def createEngine(self) -> None:
    """
    Calls Qt's 'void QCompletionModel::createEngine()'.

    Qt's own words: https://doc.qt.io/qt-6/qcompletionmodel.html#createEngine
    """
    #  void QCompletionModel::createEngine()
    self.uglySide.call('ritual_ZN16QCompletionModel12createEngineEv')

  @overload(QStringList)
  def filter(self, parts: QStringList) -> None:
    """
    Calls Qt's 'void QCompletionModel::filter(const QStringList &parts)'.

    Qt's own words: https://doc.qt.io/qt-6/qcompletionmodel.html#filter

    Parameters
    ----------

    parts : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QCompletionModel::filter(const QStringList &parts)
    self.uglySide.call(
        'ritual_ZN16QCompletionModel6filterERK5QListI7QStringE',
        self._valueOf(parts),
    )

  def d_func(self) -> Optional[QCompletionModelPrivate]:
    """
    Calls Qt's 'QCompletionModelPrivate *QCompletionModel::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcompletionmodel.html#d_func

    Returns
    -------

    Optional[QCompletionModelPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCompletionModelPrivate *QCompletionModel::d_func()
    address = self.uglySide.call('ritual_ZN16QCompletionModel6d_funcEv')
    from . import QCompletionModelPrivate
    return QCompletionModelPrivate._cuteAt(address)

  def rowsAdded(self) -> None:
    """
    Calls Qt's 'void QCompletionModel::rowsAdded()'.

    Qt's own words: https://doc.qt.io/qt-6/qcompletionmodel.html#rowsAdded
    """
    #  void QCompletionModel::rowsAdded()
    self.uglySide.call('ritual_ZN16QCompletionModel9rowsAddedEv')

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QCompletionModel::invalidate()'.

    Qt's own words: https://doc.qt.io/qt-6/qcompletionmodel.html#invalidate
    """
    #  void QCompletionModel::invalidate()
    self.uglySide.call('ritual_ZN16QCompletionModel10invalidateEv')

  def rowsInserted(self) -> None:
    """
    Calls Qt's 'void QCompletionModel::rowsInserted()'.

    Qt's own words: https://doc.qt.io/qt-6/qcompletionmodel.html#rowsInserted
    """
    #  void QCompletionModel::rowsInserted()
    self.uglySide.call('ritual_ZN16QCompletionModel12rowsInsertedEv')

  def modelDestroyed(self) -> None:
    """
    Calls Qt's 'void QCompletionModel::modelDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcompletionmodel.html#modelDestroyed
    """
    #  void QCompletionModel::modelDestroyed()
    self.uglySide.call('ritual_ZN16QCompletionModel14modelDestroyedEv')
