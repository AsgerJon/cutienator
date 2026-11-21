"""
QStringListModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qstringlistmodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import Qt, QAbstractListModel, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QMetaObject, QModelIndex, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStringListModel(QAbstractListModel):
  """
  The cute side of Qt's QStringListModel: a plain Python object standing in
  front of one C++ QStringListModel.

  It is built on the cute 'QAbstractListModel', as Qt's QStringListModel is
  built on Qt's QAbstractListModel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QStringListModel that has a ritual and that Python
  can call so far, 13 names in all: 'metaObject', 'tr', 'rowCount',
  'sibling', 'data', 'setData', 'clearItemData', 'flags', 'insertRows',
  'removeRows', 'moveRows', 'sort', 'supportedDropActions'. It can be made
  from Python, in 1 way; see '__init__'.

  What has no ritual
  ------------------

  11 of the 25 functions Qt declares: 7 takes or gives a type that cannot be
  passed yet; 2 forbidden; 1 a template; 1 private.

  What to expect
  --------------

  - The C++ QStringListModel is created at the first use, not by
    'QStringListModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStringListModel.
  - Qt tells when it has removed the C++ QStringListModel. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QStringListModel::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringlistmodel.html#tr

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
    #  QString QStringListModel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QStringListModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStringListModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QStringListModel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringlistmodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QStringListModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QStringListModel10metaObjectEv',
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload()
  @overload(QModelIndex)
  def rowCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QStringListModel::rowCount(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringlistmodel.html#rowCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QStringListModel::rowCount(const QModelIndex &parent) const
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZNK16QStringListModel8rowCountERK11QModelIndex',
        self._valueOf(parent),
    )

  @overload(int, int, QModelIndex)
  def sibling(self, row: int, column: int, idx: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QStringListModel::sibling(int row, int column,
    const QModelIndex &idx) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringlistmodel.html#sibling

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
    #  QModelIndex QStringListModel::sibling(int row, int column, const
    #      QModelIndex &idx) const
    address = self.uglySide.call(
        'ritual_ZNK16QStringListModel7siblingEiiRK11QModelIndex',
        row, column, self._valueOf(idx),
    )
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int = 0) -> QVariant:
    """
    Calls Qt's 'QVariant QStringListModel::data(const QModelIndex &index, int
    role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringlistmodel.html#data

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
    #  QVariant QStringListModel::data(const QModelIndex &index, int role)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK16QStringListModel4dataERK11QModelIndexi',
        self._valueOf(index), role,
    )
    from . import QVariant
    return QVariant._cuteOwning(address)

  @overload(QModelIndex)
  def flags(self, index: QModelIndex) -> Qt.ItemFlags:
    """
    Calls Qt's 'Qt::ItemFlags QStringListModel::flags(const QModelIndex
    &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringlistmodel.html#flags

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
    #  Qt::ItemFlags QStringListModel::flags(const QModelIndex &index) const
    return Qt.ItemFlags(self.uglySide.call(
        'ritual_ZNK16QStringListModel5flagsERK11QModelIndex',
        self._valueOf(index),
    ))

  def supportedDropActions(self) -> Qt.DropActions:
    """
    Calls Qt's 'Qt::DropActions QStringListModel::supportedDropActions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstringlistmodel.html#supportedDropActions

    Returns
    -------

    Qt.DropActions
      The value standing for the combination Qt gave back.
    """
    #  Qt::DropActions QStringListModel::supportedDropActions() const
    return Qt.DropActions(self.uglySide.call(
        'ritual_ZNK16QStringListModel20supportedDropActionsEv',
    ))

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
    Calls Qt's 'bool QStringListModel::setData(const QModelIndex &index,
    const QVariant &value, int role)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringlistmodel.html#setData

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
    #  bool QStringListModel::setData(const QModelIndex &index, const
    #      QVariant &value, int role)
    return self.uglySide.call(
        'ritual_ZN16QStringListModel7setDataERK11QModelIndexRK8QVarianti',
        self._valueOf(index), self._valueOf(value), role,
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
    'QStringListModel::QStringListModel(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstringlistmodel.html#QStringListModel

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QStringListModel::QStringListModel(QObject *parent)
    self._noteCreation(QStringListModel, lambda: Rituals.call(
        'ritual_ZN16QStringListModelC1EP7QObject', self._addressOf(parent),
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

  @overload(QModelIndex)
  def clearItemData(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QStringListModel::clearItemData(const QModelIndex
    &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstringlistmodel.html#clearItemData

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QStringListModel::clearItemData(const QModelIndex &index)
    return self.uglySide.call(
        'ritual_ZN16QStringListModel13clearItemDataERK11QModelIndex',
        self._valueOf(index),
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
    Calls Qt's 'bool QStringListModel::insertRows(int row, int count, const
    QModelIndex &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringlistmodel.html#insertRows

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
    #  bool QStringListModel::insertRows(int row, int count, const
    #      QModelIndex &parent)
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZN16QStringListModel10insertRowsEiiRK11QModelIndex',
        row, count, self._valueOf(parent),
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
    Calls Qt's 'bool QStringListModel::removeRows(int row, int count, const
    QModelIndex &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringlistmodel.html#removeRows

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
    #  bool QStringListModel::removeRows(int row, int count, const
    #      QModelIndex &parent)
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZN16QStringListModel10removeRowsEiiRK11QModelIndex',
        row, count, self._valueOf(parent),
    )

  @overload(QModelIndex, int, int, QModelIndex, int)
  def moveRows(
      self,
      sourceParent: QModelIndex,
      sourceRow: int,
      count: int,
      destinationParent: QModelIndex,
      destinationChild: int,
  ) -> bool:
    """
    Calls Qt's 'bool QStringListModel::moveRows(const QModelIndex
    &sourceParent, int sourceRow, int count, const QModelIndex
    &destinationParent, int destinationChild)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringlistmodel.html#moveRows

    Parameters
    ----------

    sourceParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    sourceRow : int
      Passed on as it is.

    count : int
      Passed on as it is.

    destinationParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    destinationChild : int
      Passed on as it is.
    """
    #  bool QStringListModel::moveRows(const QModelIndex &sourceParent, int
    #      sourceRow, int count, const QModelIndex &destinationParent, int
    #      destinationChild)
    return self.uglySide.call(
        'ritual_ZN16QStringListModel8moveRowsERK11QModelIndexiiS2_i',
        self._valueOf(sourceParent), sourceRow, count,
        self._valueOf(destinationParent), destinationChild,
    )

  @overload(int)
  @overload(int, Qt.SortOrder)
  def sort(
      self,
      column: int,
      order: Qt.SortOrder = Qt.SortOrder.AscendingOrder,
  ) -> None:
    """
    Calls Qt's 'void QStringListModel::sort(int column, Qt::SortOrder
    order)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringlistmodel.html#sort

    Parameters
    ----------

    column : int
      Passed on as it is.

    order : Qt.SortOrder
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.SortOrder.AscendingOrder.
    """
    #  void QStringListModel::sort(int column, Qt::SortOrder order)
    self.uglySide.call(
        'ritual_ZN16QStringListModel4sortEiN2Qt9SortOrderE',
        column, order.value,
    )
