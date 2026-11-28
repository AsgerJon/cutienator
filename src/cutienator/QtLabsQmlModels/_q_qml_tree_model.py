"""
QQmlTreeModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsQmlModels/6.12.0/QtLabsQmlModels/private/qqmltreemodel_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlTreeModel to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQmlAbstractColumnModel
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QModelIndex, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlTreeModel(QQmlAbstractColumnModel):
  """
  The cute side of Qt's QQmlTreeModel: a plain Python object standing in
  front of one C++ QQmlTreeModel.

  It is built on the cute 'QQmlAbstractColumnModel', as Qt's QQmlTreeModel is
  built on Qt's QQmlAbstractColumnModel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlTreeModel that has a ritual and that Python can
  call so far, 22 names in all: 'metaObject', 'tr', 'rows', 'setRows',
  'appendRow', 'clear', 'getRow', 'insertRow', 'moveRows', 'removeRow',
  'setRow', 'index', 'rowCount', 'columnCount', 'parent', 'firstRow',
  'setInitialRows', 'treeSize', 'setRowsPrivate', 'dataPrivate',
  'setDataPrivate', 'doInsert'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlTreeModel::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQmlTreeModel::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlTreeModel::~QQmlTreeModel()': the destructor: Python never
    removes a C++ QQmlTreeModel.
  - Qt's 'QModelIndex QQmlTreeModel::index(const std::vector<int> &rowIndex,
    int column)': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlTreeRow *QQmlTreeModel::getPointerToTreeRow(QModelIndex &index,
    const std::vector<int> &rowIndex) const': takes a type Python has no way
    to hand over yet.
  - Qt's 'bool QQmlTreeModel::validateNewRow(QLatin1StringView functionName,
    const QVariant &row, NewRowOperationFlag a2) const': names the enum
    'QQmlAbstractColumnModel::NewRowOperationFlag', whose class cannot be
    named here.

  What has no ritual
  ------------------

  6 of the 37 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlTreeModel is created at the first use, not by
    'QQmlTreeModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlTreeModel.
  - Qt tells when it has removed the C++ QQmlTreeModel. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlTreeModel that has no cute function yet,
    'getPointerToTreeRow', holds a function that raises
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
    Calls Qt's 'QString QQmlTreeModel::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreemodel.html#tr

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
    #  QString QQmlTreeModel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QQmlTreeModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlTreeModel'

  #  A C++ QQmlTreeModel Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlTreeModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlTreeModel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreemodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlTreeModel::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QQmlTreeModel10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def rows(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlTreeModel::rows() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreemodel.html#rows

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlTreeModel::rows() const
    address = self.uglySide.call('ritual_ZNK13QQmlTreeModel4rowsEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QModelIndex)
  def getRow(self, index: QModelIndex) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlTreeModel::getRow(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreemodel.html#getRow

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlTreeModel::getRow(const QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK13QQmlTreeModel6getRowERK11QModelIndex',
        self._valueOf(index),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def index(
      self,
      row: int,
      column: int,
      parent: Optional[QModelIndex] = None,
  ) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QQmlTreeModel::index(int row, int column, const
    QModelIndex &parent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreemodel.html#index

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
    #  QModelIndex QQmlTreeModel::index(int row, int column, const
    #      QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK13QQmlTreeModel5indexEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QQmlTreeModel5indexEiiRK11QModelIndex'
    address = self.uglySide.call(ritual, row, column, self._valueOf(parent))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload()
  @overload(QModelIndex)
  def rowCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QQmlTreeModel::rowCount(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreemodel.html#rowCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QQmlTreeModel::rowCount(const QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK13QQmlTreeModel8rowCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QQmlTreeModel8rowCountERK11QModelIndex'
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload()
  @overload(QModelIndex)
  def columnCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QQmlTreeModel::columnCount(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreemodel.html#columnCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QQmlTreeModel::columnCount(const QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK13QQmlTreeModel11columnCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QQmlTreeModel11columnCountERK11QModelIndex'
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload(QModelIndex)
  def parent(self, index: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QQmlTreeModel::parent(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreemodel.html#parent

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
    #  QModelIndex QQmlTreeModel::parent(const QModelIndex &index) const
    ritual = 'ritual_ZNK13QQmlTreeModel6parentERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QQmlTreeModel6parentERK11QModelIndex'
    address = self.uglySide.call(ritual, self._valueOf(index))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  def firstRow(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlTreeModel::firstRow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreemodel.html#firstRow

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlTreeModel::firstRow() const
    ritual = 'ritual_ZNK13QQmlTreeModel8firstRowEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QQmlTreeModel8firstRowEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def treeSize(self) -> int:
    """
    Calls Qt's 'int QQmlTreeModel::treeSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreemodel.html#treeSize
    """
    #  int QQmlTreeModel::treeSize() const
    return self.uglySide.call('ritual_ZNK13QQmlTreeModel8treeSizeEv')

  @overload(QModelIndex, str)
  def dataPrivate(self, index: QModelIndex, roleName: str) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlTreeModel::dataPrivate(const QModelIndex &index,
    const QString &roleName) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreemodel.html#dataPrivate

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    roleName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlTreeModel::dataPrivate(const QModelIndex &index, const
    #      QString &roleName) const
    ritual = (
        'ritual_ZNK13QQmlTreeModel11dataPrivateERK11QModelIndexRK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13QQmlTreeModel11dataPrivateERK11QModelIndexRK7QSt'
          'ring')
    address = self.uglySide.call(ritual, self._valueOf(index), roleName)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setRows(self, rows: QVariant) -> None:
    """
    Calls Qt's 'void QQmlTreeModel::setRows(const QVariant &rows)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreemodel.html#setRows

    Parameters
    ----------

    rows : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlTreeModel::setRows(const QVariant &rows)
    self.uglySide.call(
        'ritual_ZN13QQmlTreeModel7setRowsERK8QVariant', self._valueOf(rows),
    )

  @overload(QModelIndex, QVariant)
  def setRow(self, index: QModelIndex, rowData: QVariant) -> None:
    """
    Calls Qt's 'void QQmlTreeModel::setRow(QModelIndex index, const QVariant
    &rowData)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreemodel.html#setRow

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    rowData : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlTreeModel::setRow(QModelIndex index, const QVariant &rowData)
    self.uglySide.call(
        'ritual_ZN13QQmlTreeModel6setRowE11QModelIndexRK8QVariant',
        self._valueOf(index), self._valueOf(rowData),
    )

  def setInitialRows(self) -> None:
    """
    Calls Qt's 'void QQmlTreeModel::setInitialRows()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreemodel.html#setInitialRows
    """
    #  void QQmlTreeModel::setInitialRows()
    ritual = 'ritual_ZN13QQmlTreeModel14setInitialRowsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQmlTreeModel14setInitialRowsEv'
    self.uglySide.call(ritual)

  @overload(QList[QVariant])
  def setRowsPrivate(self, rowsAsVariantList: QList[QVariant]) -> None:
    """
    Calls Qt's 'void QQmlTreeModel::setRowsPrivate(const QVariantList
    &rowsAsVariantList)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreemodel.html#setRowsPrivate

    Parameters
    ----------

    rowsAsVariantList : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlTreeModel::setRowsPrivate(const QVariantList
    #      &rowsAsVariantList)
    self.uglySide.call(
        'ritual_ZN13QQmlTreeModel14setRowsPrivateERK5QListI8QVariantE',
        self._valueOf(rowsAsVariantList),
    )

  @overload(QModelIndex, str, QVariant)
  def setDataPrivate(
      self,
      index: QModelIndex,
      roleName: str,
      value: QVariant,
  ) -> None:
    """
    Calls Qt's 'void QQmlTreeModel::setDataPrivate(const QModelIndex &index,
    const QString &roleName, QVariant value)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreemodel.html#setDataPrivate

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    roleName : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlTreeModel::setDataPrivate(const QModelIndex &index, const
    #      QString &roleName, QVariant value)
    ritual = (
        'ritual_ZN13QQmlTreeModel14setDataPrivateERK11QModelIndexRK7QString'
        '8QVariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QQmlTreeModel14setDataPrivateERK11QModelIndexRK7Q'
          'String8QVariant')
    self.uglySide.call(
        ritual, self._valueOf(index), roleName, self._valueOf(value),
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
    Notes what was given, for Qt's 'QQmlTreeModel::QQmlTreeModel(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreemodel.html#QQmlTreeModel

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlTreeModel::QQmlTreeModel(QObject *parent)
    self._noteCreation(QQmlTreeModel, lambda: Rituals.call(
        'ritual_ZN13QQmlTreeModelC1EP7QObject',
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

  @overload(QModelIndex, QVariant)
  def appendRow(self, parent: QModelIndex, row: QVariant) -> None:
    """
    Calls Qt's 'void QQmlTreeModel::appendRow(QModelIndex parent, const
    QVariant &row)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreemodel.html#appendRow

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    row : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlTreeModel::appendRow(QModelIndex parent, const QVariant &row)
    self.uglySide.call(
        'ritual_ZN13QQmlTreeModel9appendRowE11QModelIndexRK8QVariant',
        self._valueOf(parent), self._valueOf(row),
    )

  @overload(QVariant)
  def appendRow(self, row: QVariant) -> None:
    """
    Calls Qt's 'void QQmlTreeModel::appendRow(const QVariant &row)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreemodel.html#appendRow

    Parameters
    ----------

    row : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlTreeModel::appendRow(const QVariant &row)
    self.uglySide.call(
        'ritual_ZN13QQmlTreeModel9appendRowERK8QVariant', self._valueOf(row),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QQmlTreeModel::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreemodel.html#clear
    """
    #  void QQmlTreeModel::clear()
    self.uglySide.call('ritual_ZN13QQmlTreeModel5clearEv')

  @overload(int, QModelIndex, QVariant)
  def insertRow(
      self,
      rowIndex: int,
      parent: QModelIndex,
      row: QVariant,
  ) -> None:
    """
    Calls Qt's 'void QQmlTreeModel::insertRow(int rowIndex, QModelIndex
    parent, const QVariant &row)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreemodel.html#insertRow

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    row : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlTreeModel::insertRow(int rowIndex, QModelIndex parent, const
    #      QVariant &row)
    self.uglySide.call(
        'ritual_ZN13QQmlTreeModel9insertRowEi11QModelIndexRK8QVariant',
        rowIndex, self._valueOf(parent), self._valueOf(row),
    )

  @overload(int, QVariant)
  def insertRow(self, rowIndex: int, row: QVariant) -> None:
    """
    Calls Qt's 'void QQmlTreeModel::insertRow(int rowIndex, const QVariant
    &row)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreemodel.html#insertRow

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    row : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlTreeModel::insertRow(int rowIndex, const QVariant &row)
    self.uglySide.call(
        'ritual_ZN13QQmlTreeModel9insertRowEiRK8QVariant',
        rowIndex, self._valueOf(row),
    )

  @overload(QModelIndex, int, int, QModelIndex, int)
  def moveRows(
      self,
      fromIndex: QModelIndex,
      fromRowIndex: int,
      rows: int,
      toIndex: QModelIndex,
      toRowIndex: int,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlTreeModel::moveRows(const QModelIndex &fromIndex,
    int fromRowIndex, int rows, const QModelIndex &toIndex, int toRowIndex)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreemodel.html#moveRows

    Parameters
    ----------

    fromIndex : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    fromRowIndex : int
      Passed on as it is.

    rows : int
      Passed on as it is.

    toIndex : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    toRowIndex : int
      Passed on as it is.
    """
    #  bool QQmlTreeModel::moveRows(const QModelIndex &fromIndex, int
    #      fromRowIndex, int rows, const QModelIndex &toIndex, int
    #      toRowIndex)
    ritual = 'ritual_ZN13QQmlTreeModel8moveRowsERK11QModelIndexiiS2_i'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQmlTreeModel8moveRowsERK11QModelIndexiiS2_i'
    return self.uglySide.call(
        ritual,
        self._valueOf(fromIndex), fromRowIndex, rows, self._valueOf(toIndex),
        toRowIndex,
    )

  @overload(QModelIndex)
  def removeRow(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QQmlTreeModel::removeRow(QModelIndex index)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreemodel.html#removeRow

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QQmlTreeModel::removeRow(QModelIndex index)
    self.uglySide.call(
        'ritual_ZN13QQmlTreeModel9removeRowE11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex, int, QVariant)
  def doInsert(
      self,
      index: QModelIndex,
      rowIndex: int,
      row: QVariant,
  ) -> None:
    """
    Calls Qt's 'void QQmlTreeModel::doInsert(const QModelIndex &index, int
    rowIndex, const QVariant &row)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreemodel.html#doInsert

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    rowIndex : int
      Passed on as it is.

    row : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlTreeModel::doInsert(const QModelIndex &index, int rowIndex,
    #      const QVariant &row)
    self.uglySide.call(
        'ritual_ZN13QQmlTreeModel8doInsertERK11QModelIndexiRK8QVariant',
        self._valueOf(index), rowIndex, self._valueOf(row),
    )

  @staticmethod
  def getPointerToTreeRow(*__, **_) -> Never:
    """
    Qt's 'QQmlTreeRow *QQmlTreeModel::getPointerToTreeRow(QModelIndex &index,
    const std::vector<int> &rowIndex) const': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlTreeModel.getPointerToTreeRow' has no cute function yet. Qt's "
        "'QQmlTreeRow *QQmlTreeModel::getPointerToTreeRow(QModelIndex "
        "&index, const std::vector<int> &rowIndex) const': takes a type "
        "Python has no way to hand over yet.")
