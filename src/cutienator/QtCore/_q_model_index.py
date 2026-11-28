"""
QModelIndex binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qabstractitemmodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt, QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QAbstractItemModel, QModelRoleDataSpan, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QModelRoleDataSpan = WAIT['QModelRoleDataSpan']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QModelIndex(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QModelIndex: a plain Python object standing in front
  of one C++ QModelIndex.

  C++ hands a QModelIndex around as a copy, so every C++ QModelIndex behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QModelIndex that has a ritual and that Python can
  call so far, 18 names in all: 'row', 'column', 'internalId', 'parent',
  'sibling', 'siblingAtColumn', 'siblingAtRow', 'data', 'multiData', 'flags',
  'model', 'isValid', '__eq__', '__ne__', '__lt__', '__gt__', '__le__',
  '__ge__'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QModelIndex::internalPointer() const': gives 'void', which
    has no cute class yet.
  - Qt's 'const void *QModelIndex::constInternalPointer() const': gives
    'void', which has no cute class yet.
  - Qt's 'QModelIndex::QModelIndex(int arow, int acolumn, const void *ptr,
    const QAbstractItemModel *amodel)': names 'void', which has no cute class
    yet.
  - Qt's 'QModelIndex::~QModelIndex()': the destructor: Python removes its
    C++ QModelIndex by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QModelIndex is created at the first use, not by
    'QModelIndex(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QModelIndex back gives a copy the ritual made for
    Python, in a new cute QModelIndex.
  - Each name of Qt's QModelIndex that has no cute function yet,
    'constInternalPointer', 'internalPointer', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QModelIndex'

  #  Qt's '~QModelIndex()'. Naming it makes this a value class: Python owns
  #  every C++ QModelIndex behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QModelIndexD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def row(self) -> int:
    """
    Calls Qt's 'int QModelIndex::row() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelindex.html#row
    """
    #  int QModelIndex::row() const
    return self.uglySide.call('ritual_ZNK11QModelIndex3rowEv')

  def column(self) -> int:
    """
    Calls Qt's 'int QModelIndex::column() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelindex.html#column
    """
    #  int QModelIndex::column() const
    return self.uglySide.call('ritual_ZNK11QModelIndex6columnEv')

  def internalId(self) -> int:
    """
    Calls Qt's 'quintptr QModelIndex::internalId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelindex.html#internalId
    """
    #  quintptr QModelIndex::internalId() const
    return self.uglySide.call('ritual_ZNK11QModelIndex10internalIdEv')

  def parent(self) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QModelIndex::parent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelindex.html#parent

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QModelIndex::parent() const
    address = self.uglySide.call('ritual_ZNK11QModelIndex6parentEv')
    return QModelIndex._cuteOwning(address)

  @overload(int, int)
  def sibling(self, row: int, column: int) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QModelIndex::sibling(int row, int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelindex.html#sibling

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QModelIndex::sibling(int row, int column) const
    address = self.uglySide.call(
        'ritual_ZNK11QModelIndex7siblingEii', row, column,
    )
    return QModelIndex._cuteOwning(address)

  @overload(int)
  def siblingAtColumn(self, column: int) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QModelIndex::siblingAtColumn(int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelindex.html#siblingAtColumn

    Parameters
    ----------

    column : int
      Passed on as it is.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QModelIndex::siblingAtColumn(int column) const
    address = self.uglySide.call(
        'ritual_ZNK11QModelIndex15siblingAtColumnEi', column,
    )
    return QModelIndex._cuteOwning(address)

  @overload(int)
  def siblingAtRow(self, row: int) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QModelIndex::siblingAtRow(int row) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelindex.html#siblingAtRow

    Parameters
    ----------

    row : int
      Passed on as it is.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QModelIndex::siblingAtRow(int row) const
    address = self.uglySide.call(
        'ritual_ZNK11QModelIndex12siblingAtRowEi', row,
    )
    return QModelIndex._cuteOwning(address)

  @overload()
  @overload(int)
  def data(self, role: int = 0) -> QVariant:
    """
    Calls Qt's 'QVariant QModelIndex::data(int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelindex.html#data

    Parameters
    ----------

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QModelIndex::data(int role) const
    address = self.uglySide.call('ritual_ZNK11QModelIndex4dataEi', role)
    from . import QVariant
    return QVariant._cuteOwning(address)

  def flags(self) -> Qt.ItemFlags:
    """
    Calls Qt's 'Qt::ItemFlags QModelIndex::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelindex.html#flags

    Returns
    -------

    Qt.ItemFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::ItemFlags QModelIndex::flags() const
    return Qt.ItemFlags(self.uglySide.call(
        'ritual_ZNK11QModelIndex5flagsEv',
    ))

  def model(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'const QAbstractItemModel *QModelIndex::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelindex.html#model

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QAbstractItemModel *QModelIndex::model() const
    address = self.uglySide.call('ritual_ZNK11QModelIndex5modelEv')
    from . import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QModelIndex::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelindex.html#isValid
    """
    #  bool QModelIndex::isValid() const
    return self.uglySide.call('ritual_ZNK11QModelIndex7isValidEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QModelIndex) -> bool:
    """
    Calls Qt's 'bool operator==(const QModelIndex &lhs, const QModelIndex
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelindex.html#operator==

    Parameters
    ----------

    rhs : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool operator==(const QModelIndex &lhs, const QModelIndex &rhs)
    return Rituals.call(
        'ritual_ZeqRK11QModelIndexS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QModelIndex) -> bool:
    """
    Calls Qt's 'bool operator!=(const QModelIndex &lhs, const QModelIndex
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelindex.html#operator!=

    Parameters
    ----------

    rhs : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool operator!=(const QModelIndex &lhs, const QModelIndex &rhs)
    return Rituals.call(
        'ritual_ZneRK11QModelIndexS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __lt__(self, rhs: QModelIndex) -> bool:
    """
    Calls Qt's 'bool operator<(const QModelIndex &lhs, const QModelIndex
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelindex.html#operator<

    Parameters
    ----------

    rhs : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool operator<(const QModelIndex &lhs, const QModelIndex &rhs)
    return Rituals.call(
        'ritual_ZltRK11QModelIndexS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __lt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __gt__(self, rhs: QModelIndex) -> bool:
    """
    Calls Qt's 'bool operator>(const QModelIndex &lhs, const QModelIndex
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelindex.html#operator>

    Parameters
    ----------

    rhs : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool operator>(const QModelIndex &lhs, const QModelIndex &rhs)
    return Rituals.call(
        'ritual_ZgtRK11QModelIndexS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __gt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __le__(self, rhs: QModelIndex) -> bool:
    """
    Calls Qt's 'bool operator<=(const QModelIndex &lhs, const QModelIndex
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelindex.html#operator<=

    Parameters
    ----------

    rhs : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool operator<=(const QModelIndex &lhs, const QModelIndex &rhs)
    return Rituals.call(
        'ritual_ZleRK11QModelIndexS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __le__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ge__(self, rhs: QModelIndex) -> bool:
    """
    Calls Qt's 'bool operator>=(const QModelIndex &lhs, const QModelIndex
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelindex.html#operator>=

    Parameters
    ----------

    rhs : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool operator>=(const QModelIndex &lhs, const QModelIndex &rhs)
    return Rituals.call(
        'ritual_ZgeRK11QModelIndexS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ge__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QModelIndex::QModelIndex()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmodelindex.html#QModelIndex
    """
    #  QModelIndex::QModelIndex()
    self._noteCreation(QModelIndex, lambda: Rituals.call(
        'ritual_ZN11QModelIndexC1Ev',
    ))

  @overload(int, int, int, QAbstractItemModel)
  @overload(int, int, int, NoneType)
  def __init__(
      self,
      arow: int,
      acolumn: int,
      id: int,
      amodel: Optional[QAbstractItemModel],
  ) -> None:
    """
    Notes what was given, for Qt's 'QModelIndex::QModelIndex(int arow, int
    acolumn, quintptr id, const QAbstractItemModel *amodel)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmodelindex.html#QModelIndex

    Parameters
    ----------

    arow : int
      Passed on as it is.

    acolumn : int
      Passed on as it is.

    id : int
      Passed on as it is.

    amodel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QModelIndex::QModelIndex(int arow, int acolumn, quintptr id, const
    #      QAbstractItemModel *amodel)
    self._noteCreation(QModelIndex, lambda: Rituals.call(
        'ritual_ZN11QModelIndexC1EiiyPK18QAbstractItemModel',
        arow, acolumn, id, self._addressOf(amodel),
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

  @overload(QModelRoleDataSpan)
  def multiData(self, roleDataSpan: QModelRoleDataSpan) -> None:
    """
    Calls Qt's 'void QModelIndex::multiData(QModelRoleDataSpan roleDataSpan)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelindex.html#multiData

    Parameters
    ----------

    roleDataSpan : QModelRoleDataSpan
      Passed on as a value: Qt reads the C++ QModelRoleDataSpan, which stays
      Python's own.
    """
    #  void QModelIndex::multiData(QModelRoleDataSpan roleDataSpan) const
    self.uglySide.call(
        'ritual_ZNK11QModelIndex9multiDataE18QModelRoleDataSpan',
        self._valueOf(roleDataSpan),
    )

  @staticmethod
  def constInternalPointer(*__, **_) -> Never:
    """
    Qt's 'const void *QModelIndex::constInternalPointer() const': gives
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QModelIndex.constInternalPointer' has no cute function yet. Qt's "
        "'const void *QModelIndex::constInternalPointer() const': gives "
        "'void', which has no cute class yet.")

  @staticmethod
  def internalPointer(*__, **_) -> Never:
    """
    Qt's 'void *QModelIndex::internalPointer() const': gives 'void', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QModelIndex.internalPointer' has no cute function yet. Qt's 'void "
        "*QModelIndex::internalPointer() const': gives 'void', which has no "
        "cute class yet.")


#  Qt's 'QList<QModelIndex>': the list of QModelIndex, which
#  'QList[QModelIndex]' gives. It is made here, so that there is one as soon
#  as there can be a QModelIndex. Qt has a name of its own for it.
QModelIndexList = QList.createKind(
    QModelIndex, 'value',
    name='QModelIndexList',
    make='ritual_list_make_QModelIndex',
    add='ritual_list_add_QModelIndex',
    size='ritual_list_size_QModelIndex',
    at='ritual_list_at_QModelIndex',
    drop='ritual_list_drop_QModelIndex',
)
