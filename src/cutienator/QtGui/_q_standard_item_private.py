"""
QStandardItemPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qstandarditemmodel_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QStandardItemPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QMap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QVariant
  from . import QStandardItem, QStandardItemModel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QStandardItem = WAIT['QStandardItem']
  QStandardItemModel = WAIT['QStandardItemModel']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStandardItemPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QStandardItemPrivate: a plain Python object standing
  in front of one C++ QStandardItemPrivate.

  C++ hands a QStandardItemPrivate around as a copy, so every C++
  QStandardItemPrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QStandardItemPrivate that has a ritual and that
  Python can call so far, 13 names in all: 'q_func', 'childIndex',
  'setChild', 'rowCount', 'columnCount', 'childDeleted', 'setModel',
  'setParentAndModel', 'changeFlags', 'setItemData', 'itemData',
  'insertRows', 'insertColumns'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QStandardItem *QStandardItemPrivate::q_func() const': takes
    in Python what 'QStandardItem *QStandardItemPrivate::q_func()' takes.
  - Qt's 'std::pair<int, int> QStandardItemPrivate::position() const': gives
    a type Python has no way to take yet.
  - Qt's 'QStandardItemPrivate::~QStandardItemPrivate()': the destructor:
    Python removes its C++ QStandardItemPrivate by it, and has no other use
    for it.

  What has no ritual
  ------------------

  1 of the 20 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QStandardItemPrivate is created at the first use, not by
    'QStandardItemPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStandardItemPrivate back gives a copy the ritual
    made for Python, in a new cute QStandardItemPrivate.
  - Each name of Qt's QStandardItemPrivate that has no cute function yet,
    'position', 'sortChildren', holds a function that raises
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
  __qt_class__ = 'QStandardItemPrivate'

  #  Qt's '~QStandardItemPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QStandardItemPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QStandardItemPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int)
  def childIndex(self, row: int, column: int) -> int:
    """
    Calls Qt's 'int QStandardItemPrivate::childIndex(int row, int column)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemprivate.html#childIndex

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.
    """
    #  int QStandardItemPrivate::childIndex(int row, int column) const
    return self.uglySide.call(
        'ritual_ZNK20QStandardItemPrivate10childIndexEii', row, column,
    )

  @overload(QStandardItem)
  @overload(NoneType)
  def childIndex(self, child: Optional[QStandardItem]) -> int:
    """
    Calls Qt's 'int QStandardItemPrivate::childIndex(const QStandardItem
    *child) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemprivate.html#childIndex

    Parameters
    ----------

    child : Optional[QStandardItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QStandardItemPrivate::childIndex(const QStandardItem *child) const
    return self.uglySide.call(
        'ritual_ZNK20QStandardItemPrivate10childIndexEPK13QStandardItem',
        self._addressOf(child),
    )

  def rowCount(self) -> int:
    """
    Calls Qt's 'int QStandardItemPrivate::rowCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditemprivate.html#rowCount
    """
    #  int QStandardItemPrivate::rowCount() const
    return self.uglySide.call('ritual_ZNK20QStandardItemPrivate8rowCountEv')

  def columnCount(self) -> int:
    """
    Calls Qt's 'int QStandardItemPrivate::columnCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemprivate.html#columnCount
    """
    #  int QStandardItemPrivate::columnCount() const
    return self.uglySide.call(
        'ritual_ZNK20QStandardItemPrivate11columnCountEv',
    )

  def itemData(self) -> QMap[int, QVariant]:
    """
    Calls Qt's 'QMap<int, QVariant> QStandardItemPrivate::itemData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditemprivate.html#itemData

    Returns
    -------

    QMap[int, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QMap<int, QVariant> QStandardItemPrivate::itemData() const
    address = self.uglySide.call(
        'ritual_ZNK20QStandardItemPrivate8itemDataEv',
    )
    from ..QtCore import QVariant
    return QMap[int, QVariant]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int, QStandardItem)
  @overload(int, int, NoneType)
  @overload(int, int, QStandardItem, bool)
  @overload(int, int, NoneType, bool)
  def setChild(
      self,
      row: int,
      column: int,
      item: Optional[QStandardItem],
      emitChanged: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QStandardItemPrivate::setChild(int row, int column,
    QStandardItem *item, bool emitChanged)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditemprivate.html#setChild

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    item : Optional[QStandardItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    emitChanged : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QStandardItemPrivate::setChild(int row, int column, QStandardItem
    #      *item, bool emitChanged)
    self.uglySide.call(
        'ritual_ZN20QStandardItemPrivate8setChildEiiP13QStandardItemb',
        row, column, self._addressOf(item), emitChanged,
    )

  @overload(QStandardItemModel)
  @overload(NoneType)
  def setModel(self, mod: Optional[QStandardItemModel]) -> None:
    """
    Calls Qt's 'void QStandardItemPrivate::setModel(QStandardItemModel
    *mod)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditemprivate.html#setModel

    Parameters
    ----------

    mod : Optional[QStandardItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStandardItemPrivate::setModel(QStandardItemModel *mod)
    self.uglySide.call(
        'ritual_ZN20QStandardItemPrivate8setModelEP18QStandardItemModel',
        self._addressOf(mod),
    )

  @overload(QStandardItem, QStandardItemModel)
  @overload(QStandardItem, NoneType)
  @overload(NoneType, QStandardItemModel)
  @overload(NoneType, NoneType)
  def setParentAndModel(
      self,
      par: Optional[QStandardItem],
      mod: Optional[QStandardItemModel],
  ) -> None:
    """
    Calls Qt's 'void QStandardItemPrivate::setParentAndModel(QStandardItem
    *par, QStandardItemModel *mod)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemprivate.html#setParentAndModel

    Parameters
    ----------

    par : Optional[QStandardItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mod : Optional[QStandardItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStandardItemPrivate::setParentAndModel(QStandardItem *par,
    #      QStandardItemModel *mod)
    self.uglySide.call(
        'ritual_ZN20QStandardItemPrivate17setParentAndModelEP13QStandardIte'
        'mP18QStandardItemModel',
        self._addressOf(par), self._addressOf(mod),
    )

  @overload(QMap[int, QVariant])
  def setItemData(self, roles: QMap[int, QVariant]) -> None:
    """
    Calls Qt's 'void QStandardItemPrivate::setItemData(const QMap<int,
    QVariant> &roles)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemprivate.html#setItemData

    Parameters
    ----------

    roles : QMap[int, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QStandardItemPrivate::setItemData(const QMap<int, QVariant>
    #      &roles)
    self.uglySide.call(
        'ritual_ZN20QStandardItemPrivate11setItemDataERK4QMapIi8QVariantE',
        self._valueOf(roles),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QStandardItemPrivate::QStandardItemPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemprivate.html#QStandardItemPrivate
    """
    #  QStandardItemPrivate::QStandardItemPrivate()
    self._noteCreation(QStandardItemPrivate, lambda: Rituals.call(
        'ritual_ZN20QStandardItemPrivateC1Ev',
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

  def q_func(self) -> Optional[QStandardItem]:
    """
    Calls Qt's 'QStandardItem *QStandardItemPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditemprivate.html#q_func

    Returns
    -------

    Optional[QStandardItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStandardItem *QStandardItemPrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QStandardItemPrivate6q_funcEv')
    from . import QStandardItem
    return QStandardItem._cuteAt(address)

  @overload(QStandardItem)
  @overload(NoneType)
  def childDeleted(self, child: Optional[QStandardItem]) -> None:
    """
    Calls Qt's 'void QStandardItemPrivate::childDeleted(QStandardItem
    *child)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemprivate.html#childDeleted

    Parameters
    ----------

    child : Optional[QStandardItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStandardItemPrivate::childDeleted(QStandardItem *child)
    self.uglySide.call(
        'ritual_ZN20QStandardItemPrivate12childDeletedEP13QStandardItem',
        self._addressOf(child),
    )

  @overload(bool, Qt.ItemFlags)
  def changeFlags(self, enable: bool, f: Qt.ItemFlags) -> None:
    """
    Calls Qt's 'void QStandardItemPrivate::changeFlags(bool enable,
    Qt::ItemFlags f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemprivate.html#changeFlags

    Parameters
    ----------

    enable : bool
      Passed on as it is.

    f : Qt.ItemFlags
      Passed on as its number.
    """
    #  void QStandardItemPrivate::changeFlags(bool enable, Qt::ItemFlags f)
    self.uglySide.call(
        'ritual_ZN20QStandardItemPrivate11changeFlagsEb6QFlagsIN2Qt8ItemFla'
        'gEE',
        enable, f.value,
    )

  @overload(int, int, QList[QStandardItem])
  def insertRows(
      self,
      row: int,
      count: int,
      items: QList[QStandardItem],
  ) -> bool:
    """
    Calls Qt's 'bool QStandardItemPrivate::insertRows(int row, int count,
    const QList<QStandardItem *> &items)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemprivate.html#insertRows

    Parameters
    ----------

    row : int
      Passed on as it is.

    count : int
      Passed on as it is.

    items : QList[QStandardItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QStandardItemPrivate::insertRows(int row, int count, const
    #      QList<QStandardItem *> &items)
    return self.uglySide.call(
        'ritual_ZN20QStandardItemPrivate10insertRowsEiiRK5QListIP13QStandar'
        'dItemE',
        row, count, self._valueOf(items),
    )

  @overload(int, QList[QStandardItem])
  def insertRows(self, row: int, items: QList[QStandardItem]) -> bool:
    """
    Calls Qt's 'bool QStandardItemPrivate::insertRows(int row, const
    QList<QStandardItem *> &items)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemprivate.html#insertRows

    Parameters
    ----------

    row : int
      Passed on as it is.

    items : QList[QStandardItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QStandardItemPrivate::insertRows(int row, const
    #      QList<QStandardItem *> &items)
    return self.uglySide.call(
        'ritual_ZN20QStandardItemPrivate10insertRowsEiRK5QListIP13QStandard'
        'ItemE',
        row, self._valueOf(items),
    )

  @overload(int, int, QList[QStandardItem])
  def insertColumns(
      self,
      column: int,
      count: int,
      items: QList[QStandardItem],
  ) -> bool:
    """
    Calls Qt's 'bool QStandardItemPrivate::insertColumns(int column, int
    count, const QList<QStandardItem *> &items)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemprivate.html#insertColumns

    Parameters
    ----------

    column : int
      Passed on as it is.

    count : int
      Passed on as it is.

    items : QList[QStandardItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QStandardItemPrivate::insertColumns(int column, int count, const
    #      QList<QStandardItem *> &items)
    return self.uglySide.call(
        'ritual_ZN20QStandardItemPrivate13insertColumnsEiiRK5QListIP13QStan'
        'dardItemE',
        column, count, self._valueOf(items),
    )

  @staticmethod
  def position(*__, **_) -> Never:
    """
    Qt's 'std::pair<int, int> QStandardItemPrivate::position() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QStandardItemPrivate.position' has no cute function yet. Qt's "
        "'std::pair<int, int> QStandardItemPrivate::position() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def sortChildren(*__, **_) -> Never:
    """
    Qt's 'void QStandardItemPrivate::sortChildren(int column, Qt::SortOrder
    order)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: call to implicitly-deleted copy
    constructor of 'QStandardItemModelPrivate'.
    """
    raise NotImplementedError(
        "'QStandardItemPrivate.sortChildren' has no cute function yet. Qt's "
        "'void QStandardItemPrivate::sortChildren(int column, Qt::SortOrder "
        "order)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: call to "
        "implicitly-deleted copy constructor of 'QStandardItemModelPrivate'."
    )
