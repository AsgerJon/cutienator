"""
QPersistentModelIndex binding of the Qt C++
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
from . import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QAbstractItemModel, QModelIndex, QModelRoleDataSpan, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QModelRoleDataSpan = WAIT['QModelRoleDataSpan']


class QPersistentModelIndex(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPersistentModelIndex: a plain Python object standing
  in front of one C++ QPersistentModelIndex.

  C++ hands a QPersistentModelIndex around as a copy, so every C++
  QPersistentModelIndex behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPersistentModelIndex that has a ritual and that
  Python can call so far, 10 names in all: 'row', 'column', 'internalId',
  'parent', 'sibling', 'data', 'multiData', 'flags', 'model', 'isValid'. It
  can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPersistentModelIndex::~QPersistentModelIndex()': the destructor:
    Python removes its C++ QPersistentModelIndex by it, and has no other use
    for it.
  - Qt's 'QModelIndex QPersistentModelIndex::operator QModelIndex() const':
    an operator, which is not reflected yet.

  What has no ritual
  ------------------

  7 of the 22 functions Qt declares: 7 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QPersistentModelIndex is created at the first use, not by
    'QPersistentModelIndex(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPersistentModelIndex back gives a copy the ritual
    made for Python, in a new cute QPersistentModelIndex.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPersistentModelIndex'

  #  Qt's '~QPersistentModelIndex()'. Naming it makes this a value class:
  #  Python owns every C++ QPersistentModelIndex behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QPersistentModelIndexD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def row(self) -> int:
    """
    Calls Qt's 'int QPersistentModelIndex::row() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpersistentmodelindex.html#row
    """
    #  int QPersistentModelIndex::row() const
    return self.uglySide.call('ritual_ZNK21QPersistentModelIndex3rowEv')

  def column(self) -> int:
    """
    Calls Qt's 'int QPersistentModelIndex::column() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpersistentmodelindex.html#column
    """
    #  int QPersistentModelIndex::column() const
    return self.uglySide.call('ritual_ZNK21QPersistentModelIndex6columnEv')

  def internalId(self) -> int:
    """
    Calls Qt's 'quintptr QPersistentModelIndex::internalId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpersistentmodelindex.html#internalId
    """
    #  quintptr QPersistentModelIndex::internalId() const
    return self.uglySide.call(
        'ritual_ZNK21QPersistentModelIndex10internalIdEv',
    )

  def parent(self) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QPersistentModelIndex::parent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpersistentmodelindex.html#parent

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QPersistentModelIndex::parent() const
    address = self.uglySide.call(
        'ritual_ZNK21QPersistentModelIndex6parentEv',
    )
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(int, int)
  def sibling(self, row: int, column: int) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QPersistentModelIndex::sibling(int row, int
    column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpersistentmodelindex.html#sibling

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
    #  QModelIndex QPersistentModelIndex::sibling(int row, int column) const
    address = self.uglySide.call(
        'ritual_ZNK21QPersistentModelIndex7siblingEii', row, column,
    )
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload()
  @overload(int)
  def data(self, role: int = 0) -> QVariant:
    """
    Calls Qt's 'QVariant QPersistentModelIndex::data(int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpersistentmodelindex.html#data

    Parameters
    ----------

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QPersistentModelIndex::data(int role) const
    address = self.uglySide.call(
        'ritual_ZNK21QPersistentModelIndex4dataEi', role,
    )
    from . import QVariant
    return QVariant._cuteOwning(address)

  def flags(self) -> Qt.ItemFlags:
    """
    Calls Qt's 'Qt::ItemFlags QPersistentModelIndex::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpersistentmodelindex.html#flags

    Returns
    -------

    Qt.ItemFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::ItemFlags QPersistentModelIndex::flags() const
    return Qt.ItemFlags(self.uglySide.call(
        'ritual_ZNK21QPersistentModelIndex5flagsEv',
    ))

  def model(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'const QAbstractItemModel *QPersistentModelIndex::model()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qpersistentmodelindex.html#model

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QAbstractItemModel *QPersistentModelIndex::model() const
    address = self.uglySide.call('ritual_ZNK21QPersistentModelIndex5modelEv')
    from . import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QPersistentModelIndex::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpersistentmodelindex.html#isValid
    """
    #  bool QPersistentModelIndex::isValid() const
    return self.uglySide.call('ritual_ZNK21QPersistentModelIndex7isValidEv')

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QPersistentModelIndex::QPersistentModelIndex()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpersistentmodelindex.html#QPersistentModelIndex
    """
    #  QPersistentModelIndex::QPersistentModelIndex()
    self._noteCreation(QPersistentModelIndex, lambda: Rituals.call(
        'ritual_ZN21QPersistentModelIndexC1Ev',
    ))

  @overload(QModelIndex)
  def __init__(self, index: QModelIndex) -> None:
    """
    Notes what was given, for Qt's
    'QPersistentModelIndex::QPersistentModelIndex(const QModelIndex &index)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpersistentmodelindex.html#QPersistentModelIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  QPersistentModelIndex::QPersistentModelIndex(const QModelIndex &index)
    self._noteCreation(QPersistentModelIndex, lambda: Rituals.call(
        'ritual_ZN21QPersistentModelIndexC1ERK11QModelIndex',
        self._valueOf(index),
    ))

  @overload(THIS)
  def __init__(self, other: QPersistentModelIndex) -> None:
    """
    Notes what was given, for Qt's
    'QPersistentModelIndex::QPersistentModelIndex(const QPersistentModelIndex
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpersistentmodelindex.html#QPersistentModelIndex

    Parameters
    ----------

    other : QPersistentModelIndex
      Passed on as a value: Qt reads the C++ QPersistentModelIndex, which
      stays Python's own.
    """
    #  QPersistentModelIndex::QPersistentModelIndex(const
    #      QPersistentModelIndex &other)
    self._noteCreation(QPersistentModelIndex, lambda: Rituals.call(
        'ritual_ZN21QPersistentModelIndexC1ERKS_', self._valueOf(other),
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
    Calls Qt's 'void QPersistentModelIndex::multiData(QModelRoleDataSpan
    roleDataSpan) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpersistentmodelindex.html#multiData

    Parameters
    ----------

    roleDataSpan : QModelRoleDataSpan
      Passed on as a value: Qt reads the C++ QModelRoleDataSpan, which stays
      Python's own.
    """
    #  void QPersistentModelIndex::multiData(QModelRoleDataSpan roleDataSpan)
    #      const
    self.uglySide.call(
        'ritual_ZNK21QPersistentModelIndex9multiDataE18QModelRoleDataSpan',
        self._valueOf(roleDataSpan),
    )
