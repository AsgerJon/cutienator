"""
QQmlTableModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsQmlModels/6.12.0/QtLabsQmlModels/private/qqmltablemodel_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlTableModel to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
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


class QQmlTableModel(QQmlAbstractColumnModel):
  """
  The cute side of Qt's QQmlTableModel: a plain Python object standing in
  front of one C++ QQmlTableModel.

  It is built on the cute 'QQmlAbstractColumnModel', as Qt's QQmlTableModel
  is built on Qt's QQmlAbstractColumnModel, and has everything that class
  has.

  What exists
  -----------

  Every function of Qt's QQmlTableModel that has a ritual and that Python can
  call so far, 22 names in all: 'metaObject', 'tr', 'rows', 'setRows',
  'appendRow', 'clear', 'getRow', 'insertRow', 'moveRow', 'removeRow',
  'setRow', 'index', 'rowCount', 'columnCount', 'parent', 'rowCountChanged',
  'firstRow', 'setInitialRows', 'setRowsPrivate', 'dataPrivate',
  'setDataPrivate', 'doInsert'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlTableModel::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQmlTableModel::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlTableModel::~QQmlTableModel()': the destructor: Python never
    removes a C++ QQmlTableModel.
  - Qt's 'bool QQmlTableModel::validateRowIndex(QLatin1StringView
    functionName, QLatin1StringView argumentName, int rowIndex, RowOption
    operation) const': names the enum 'QQmlTableModel::RowOption', whose
    class cannot be named here.

  What has no ritual
  ------------------

  6 of the 33 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlTableModel is created at the first use, not by
    'QQmlTableModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlTableModel.
  - Qt tells when it has removed the C++ QQmlTableModel. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlTableModel that has no cute function yet,
    'validateRowIndex', holds a function that raises 'NotImplementedError',
    and its docstring says why.
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
    Calls Qt's 'QString QQmlTableModel::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltablemodel.html#tr

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
    #  QString QQmlTableModel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQmlTableModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlTableModel'

  #  A C++ QQmlTableModel Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlTableModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlTableModel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltablemodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlTableModel::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQmlTableModel10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def rows(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlTableModel::rows() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltablemodel.html#rows

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlTableModel::rows() const
    address = self.uglySide.call('ritual_ZNK14QQmlTableModel4rowsEv')
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
    Calls Qt's 'QModelIndex QQmlTableModel::index(int row, int column, const
    QModelIndex &parent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltablemodel.html#index

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
    #  QModelIndex QQmlTableModel::index(int row, int column, const
    #      QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK14QQmlTableModel5indexEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQmlTableModel5indexEiiRK11QModelIndex'
    address = self.uglySide.call(ritual, row, column, self._valueOf(parent))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload()
  @overload(QModelIndex)
  def rowCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QQmlTableModel::rowCount(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltablemodel.html#rowCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QQmlTableModel::rowCount(const QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK14QQmlTableModel8rowCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQmlTableModel8rowCountERK11QModelIndex'
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload()
  @overload(QModelIndex)
  def columnCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QQmlTableModel::columnCount(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltablemodel.html#columnCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QQmlTableModel::columnCount(const QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK14QQmlTableModel11columnCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQmlTableModel11columnCountERK11QModelIndex'
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload(QModelIndex)
  def parent(self, index: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QQmlTableModel::parent(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltablemodel.html#parent

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
    #  QModelIndex QQmlTableModel::parent(const QModelIndex &index) const
    ritual = 'ritual_ZNK14QQmlTableModel6parentERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQmlTableModel6parentERK11QModelIndex'
    address = self.uglySide.call(ritual, self._valueOf(index))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  def firstRow(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlTableModel::firstRow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltablemodel.html#firstRow

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlTableModel::firstRow() const
    ritual = 'ritual_ZNK14QQmlTableModel8firstRowEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQmlTableModel8firstRowEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QModelIndex, str)
  def dataPrivate(self, index: QModelIndex, roleName: str) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlTableModel::dataPrivate(const QModelIndex
    &index, const QString &roleName) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltablemodel.html#dataPrivate

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
    #  QVariant QQmlTableModel::dataPrivate(const QModelIndex &index, const
    #      QString &roleName) const
    ritual = (
        'ritual_ZNK14QQmlTableModel11dataPrivateERK11QModelIndexRK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QQmlTableModel11dataPrivateERK11QModelIndexRK7QS'
          'tring')
    address = self.uglySide.call(ritual, self._valueOf(index), roleName)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setRows(self, rows: QVariant) -> None:
    """
    Calls Qt's 'void QQmlTableModel::setRows(const QVariant &rows)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltablemodel.html#setRows

    Parameters
    ----------

    rows : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlTableModel::setRows(const QVariant &rows)
    self.uglySide.call(
        'ritual_ZN14QQmlTableModel7setRowsERK8QVariant', self._valueOf(rows),
    )

  @overload(int, QVariant)
  def setRow(self, rowIndex: int, row: QVariant) -> None:
    """
    Calls Qt's 'void QQmlTableModel::setRow(int rowIndex, const QVariant
    &row)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltablemodel.html#setRow

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    row : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlTableModel::setRow(int rowIndex, const QVariant &row)
    self.uglySide.call(
        'ritual_ZN14QQmlTableModel6setRowEiRK8QVariant',
        rowIndex, self._valueOf(row),
    )

  def setInitialRows(self) -> None:
    """
    Calls Qt's 'void QQmlTableModel::setInitialRows()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltablemodel.html#setInitialRows
    """
    #  void QQmlTableModel::setInitialRows()
    ritual = 'ritual_ZN14QQmlTableModel14setInitialRowsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQmlTableModel14setInitialRowsEv'
    self.uglySide.call(ritual)

  @overload(QList[QVariant])
  def setRowsPrivate(self, rowsAsVariantList: QList[QVariant]) -> None:
    """
    Calls Qt's 'void QQmlTableModel::setRowsPrivate(const QVariantList
    &rowsAsVariantList)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltablemodel.html#setRowsPrivate

    Parameters
    ----------

    rowsAsVariantList : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlTableModel::setRowsPrivate(const QVariantList
    #      &rowsAsVariantList)
    self.uglySide.call(
        'ritual_ZN14QQmlTableModel14setRowsPrivateERK5QListI8QVariantE',
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
    Calls Qt's 'void QQmlTableModel::setDataPrivate(const QModelIndex &index,
    const QString &roleName, QVariant value)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltablemodel.html#setDataPrivate

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
    #  void QQmlTableModel::setDataPrivate(const QModelIndex &index, const
    #      QString &roleName, QVariant value)
    ritual = (
        'ritual_ZN14QQmlTableModel14setDataPrivateERK11QModelIndexRK7QStrin'
        'g8QVariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQmlTableModel14setDataPrivateERK11QModelIndexRK7'
          'QString8QVariant')
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
    Notes what was given, for Qt's 'QQmlTableModel::QQmlTableModel(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmltablemodel.html#QQmlTableModel

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlTableModel::QQmlTableModel(QObject *parent)
    self._noteCreation(QQmlTableModel, lambda: Rituals.call(
        'ritual_ZN14QQmlTableModelC1EP7QObject',
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

  @overload(QVariant)
  def appendRow(self, row: QVariant) -> None:
    """
    Calls Qt's 'void QQmlTableModel::appendRow(const QVariant &row)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltablemodel.html#appendRow

    Parameters
    ----------

    row : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlTableModel::appendRow(const QVariant &row)
    self.uglySide.call(
        'ritual_ZN14QQmlTableModel9appendRowERK8QVariant',
        self._valueOf(row),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QQmlTableModel::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltablemodel.html#clear
    """
    #  void QQmlTableModel::clear()
    self.uglySide.call('ritual_ZN14QQmlTableModel5clearEv')

  @overload(int)
  def getRow(self, rowIndex: int) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlTableModel::getRow(int rowIndex)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltablemodel.html#getRow

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlTableModel::getRow(int rowIndex)
    address = self.uglySide.call(
        'ritual_ZN14QQmlTableModel6getRowEi', rowIndex,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int, QVariant)
  def insertRow(self, rowIndex: int, row: QVariant) -> None:
    """
    Calls Qt's 'void QQmlTableModel::insertRow(int rowIndex, const QVariant
    &row)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltablemodel.html#insertRow

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    row : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlTableModel::insertRow(int rowIndex, const QVariant &row)
    self.uglySide.call(
        'ritual_ZN14QQmlTableModel9insertRowEiRK8QVariant',
        rowIndex, self._valueOf(row),
    )

  @overload(int, int)
  @overload(int, int, int)
  def moveRow(
      self,
      fromRowIndex: int,
      toRowIndex: int,
      rows: int = 1,
  ) -> None:
    """
    Calls Qt's 'void QQmlTableModel::moveRow(int fromRowIndex, int
    toRowIndex, int rows)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltablemodel.html#moveRow

    Parameters
    ----------

    fromRowIndex : int
      Passed on as it is.

    toRowIndex : int
      Passed on as it is.

    rows : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void QQmlTableModel::moveRow(int fromRowIndex, int toRowIndex, int
    #      rows)
    self.uglySide.call(
        'ritual_ZN14QQmlTableModel7moveRowEiii',
        fromRowIndex, toRowIndex, rows,
    )

  @overload(int)
  @overload(int, int)
  def removeRow(self, rowIndex: int, rows: int = 1) -> None:
    """
    Calls Qt's 'void QQmlTableModel::removeRow(int rowIndex, int rows)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltablemodel.html#removeRow

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    rows : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void QQmlTableModel::removeRow(int rowIndex, int rows)
    self.uglySide.call(
        'ritual_ZN14QQmlTableModel9removeRowEii', rowIndex, rows,
    )

  def rowCountChanged(self) -> None:
    """
    Calls Qt's 'void QQmlTableModel::rowCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltablemodel.html#rowCountChanged
    """
    #  void QQmlTableModel::rowCountChanged()
    self.uglySide.call('ritual_ZN14QQmlTableModel15rowCountChangedEv')

  @overload(int, QVariant)
  def doInsert(self, rowIndex: int, row: QVariant) -> None:
    """
    Calls Qt's 'void QQmlTableModel::doInsert(int rowIndex, const QVariant
    &row)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltablemodel.html#doInsert

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    row : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlTableModel::doInsert(int rowIndex, const QVariant &row)
    self.uglySide.call(
        'ritual_ZN14QQmlTableModel8doInsertEiRK8QVariant',
        rowIndex, self._valueOf(row),
    )

  @staticmethod
  def validateRowIndex(*__, **_) -> Never:
    """
    Qt's 'bool QQmlTableModel::validateRowIndex(QLatin1StringView
    functionName, QLatin1StringView argumentName, int rowIndex, RowOption
    operation) const': names the enum 'QQmlTableModel::RowOption', whose
    class cannot be named here.
    """
    raise NotImplementedError(
        "'QQmlTableModel.validateRowIndex' has no cute function yet. Qt's "
        "'bool QQmlTableModel::validateRowIndex(QLatin1StringView "
        "functionName, QLatin1StringView argumentName, int rowIndex, "
        "RowOption operation) const': names the enum "
        "'QQmlTableModel::RowOption', whose class cannot be named here.")
