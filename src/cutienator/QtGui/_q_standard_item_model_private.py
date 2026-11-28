"""
QStandardItemModelPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qstandarditemmodel_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QStandardItemModelPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QAbstractItemModelPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QModelIndex
  from . import QStandardItem, QStandardItemModel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QStandardItem = WAIT['QStandardItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStandardItemModelPrivate(QAbstractItemModelPrivate):
  """
  The cute side of Qt's QStandardItemModelPrivate: a plain Python object
  standing in front of one C++ QStandardItemModelPrivate.

  It is built on the cute 'QAbstractItemModelPrivate', as Qt's
  QStandardItemModelPrivate is built on Qt's QAbstractItemModelPrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QStandardItemModelPrivate that has a ritual and that
  Python can call so far, 14 names in all: 'q_func', 'init', 'createItem',
  'itemFromIndex', 'rowsAboutToBeInserted', 'columnsAboutToBeInserted',
  'rowsAboutToBeRemoved', 'columnsAboutToBeRemoved', 'rowsInserted',
  'columnsInserted', 'rowsRemoved', 'columnsRemoved', '_q_emitItemChanged',
  '_qt_property_sortRole_offset'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QStandardItemModel *QStandardItemModelPrivate::q_func()
    const': takes in Python what 'QStandardItemModel
    *QStandardItemModelPrivate::q_func()' takes.
  - Qt's 'QStandardItemModelPrivate::~QStandardItemModelPrivate()': the
    destructor: Python never removes a C++ QStandardItemModelPrivate.
  - Qt's 'void QStandardItemModelPrivate::itemChanged(QStandardItem *item,
    const QList<int> &roles)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QStandardItemModelPrivate::decodeDataRecursive(QDataStream
    &stream, QStandardItem *item)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  1 of the 20 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QStandardItemModelPrivate is created at the first use, not by
    'QStandardItemModelPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStandardItemModelPrivate.
  - Each name of Qt's QStandardItemModelPrivate that has no cute function
    yet, 'decodeDataRecursive', 'itemChanged', 'sort', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _qt_property_sortRole_offset() -> int:
    """
    Calls Qt's 'size_t
    QStandardItemModelPrivate::_qt_property_sortRole_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodelprivate.html
    """
    #  size_t QStandardItemModelPrivate::_qt_property_sortRole_offset()
    return Rituals.call(
        'ritual_ZN25QStandardItemModelPrivate28_qt_property_sortRole_offset'
        'Ev',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStandardItemModelPrivate'

  #  A C++ QStandardItemModelPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QStandardItemModelPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def createItem(self) -> Optional[QStandardItem]:
    """
    Calls Qt's 'QStandardItem *QStandardItemModelPrivate::createItem()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodelprivate.html#createItem

    Returns
    -------

    Optional[QStandardItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStandardItem *QStandardItemModelPrivate::createItem() const
    address = self.uglySide.call(
        'ritual_ZNK25QStandardItemModelPrivate10createItemEv',
    )
    from . import QStandardItem
    return QStandardItem._cuteAt(address)

  @overload(QModelIndex)
  def itemFromIndex(self, index: QModelIndex) -> Optional[QStandardItem]:
    """
    Calls Qt's 'QStandardItem *QStandardItemModelPrivate::itemFromIndex(const
    QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodelprivate.html#itemFromIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    Optional[QStandardItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStandardItem *QStandardItemModelPrivate::itemFromIndex(const
    #      QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK25QStandardItemModelPrivate13itemFromIndexERK11QModelInd'
        'ex',
        self._valueOf(index),
    )
    from . import QStandardItem
    return QStandardItem._cuteAt(address)

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
    'QStandardItemModelPrivate::QStandardItemModelPrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodelprivate.html
    """
    #  QStandardItemModelPrivate::QStandardItemModelPrivate()
    self._noteCreation(QStandardItemModelPrivate, lambda: Rituals.call(
        'ritual_ZN25QStandardItemModelPrivateC1Ev',
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

  def q_func(self) -> Optional[QStandardItemModel]:
    """
    Calls Qt's 'QStandardItemModel *QStandardItemModelPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodelprivate.html#q_func

    Returns
    -------

    Optional[QStandardItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStandardItemModel *QStandardItemModelPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN25QStandardItemModelPrivate6q_funcEv',
    )
    from . import QStandardItemModel
    return QStandardItemModel._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QStandardItemModelPrivate::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodelprivate.html#init
    """
    #  void QStandardItemModelPrivate::init()
    self.uglySide.call('ritual_ZN25QStandardItemModelPrivate4initEv')

  @overload(QStandardItem, int, int)
  @overload(NoneType, int, int)
  def rowsAboutToBeInserted(
      self,
      parent: Optional[QStandardItem],
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void
    QStandardItemModelPrivate::rowsAboutToBeInserted(QStandardItem *parent,
    int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodelprivate.html

    Parameters
    ----------

    parent : Optional[QStandardItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QStandardItemModelPrivate::rowsAboutToBeInserted(QStandardItem
    #      *parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN25QStandardItemModelPrivate21rowsAboutToBeInsertedEP13QSt'
        'andardItemii',
        self._addressOf(parent), start, end,
    )

  @overload(QStandardItem, int, int)
  @overload(NoneType, int, int)
  def columnsAboutToBeInserted(
      self,
      parent: Optional[QStandardItem],
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void
    QStandardItemModelPrivate::columnsAboutToBeInserted(QStandardItem
    *parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodelprivate.html

    Parameters
    ----------

    parent : Optional[QStandardItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QStandardItemModelPrivate::columnsAboutToBeInserted(QStandardItem
    #      *parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN25QStandardItemModelPrivate24columnsAboutToBeInsertedEP13'
        'QStandardItemii',
        self._addressOf(parent), start, end,
    )

  @overload(QStandardItem, int, int)
  @overload(NoneType, int, int)
  def rowsAboutToBeRemoved(
      self,
      parent: Optional[QStandardItem],
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void
    QStandardItemModelPrivate::rowsAboutToBeRemoved(QStandardItem *parent,
    int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodelprivate.html

    Parameters
    ----------

    parent : Optional[QStandardItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QStandardItemModelPrivate::rowsAboutToBeRemoved(QStandardItem
    #      *parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN25QStandardItemModelPrivate20rowsAboutToBeRemovedEP13QSta'
        'ndardItemii',
        self._addressOf(parent), start, end,
    )

  @overload(QStandardItem, int, int)
  @overload(NoneType, int, int)
  def columnsAboutToBeRemoved(
      self,
      parent: Optional[QStandardItem],
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void
    QStandardItemModelPrivate::columnsAboutToBeRemoved(QStandardItem *parent,
    int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodelprivate.html

    Parameters
    ----------

    parent : Optional[QStandardItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QStandardItemModelPrivate::columnsAboutToBeRemoved(QStandardItem
    #      *parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN25QStandardItemModelPrivate23columnsAboutToBeRemovedEP13Q'
        'StandardItemii',
        self._addressOf(parent), start, end,
    )

  @overload(QStandardItem, int, int)
  @overload(NoneType, int, int)
  def rowsInserted(
      self,
      parent: Optional[QStandardItem],
      row: int,
      count: int,
  ) -> None:
    """
    Calls Qt's 'void QStandardItemModelPrivate::rowsInserted(QStandardItem
    *parent, int row, int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodelprivate.html#rowsInserted

    Parameters
    ----------

    parent : Optional[QStandardItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    row : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QStandardItemModelPrivate::rowsInserted(QStandardItem *parent,
    #      int row, int count)
    self.uglySide.call(
        'ritual_ZN25QStandardItemModelPrivate12rowsInsertedEP13QStandardIte'
        'mii',
        self._addressOf(parent), row, count,
    )

  @overload(QStandardItem, int, int)
  @overload(NoneType, int, int)
  def columnsInserted(
      self,
      parent: Optional[QStandardItem],
      column: int,
      count: int,
  ) -> None:
    """
    Calls Qt's 'void QStandardItemModelPrivate::columnsInserted(QStandardItem
    *parent, int column, int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodelprivate.html#columnsInserted

    Parameters
    ----------

    parent : Optional[QStandardItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    column : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QStandardItemModelPrivate::columnsInserted(QStandardItem *parent,
    #      int column, int count)
    self.uglySide.call(
        'ritual_ZN25QStandardItemModelPrivate15columnsInsertedEP13QStandard'
        'Itemii',
        self._addressOf(parent), column, count,
    )

  @overload(QStandardItem, int, int)
  @overload(NoneType, int, int)
  def rowsRemoved(
      self,
      parent: Optional[QStandardItem],
      row: int,
      count: int,
  ) -> None:
    """
    Calls Qt's 'void QStandardItemModelPrivate::rowsRemoved(QStandardItem
    *parent, int row, int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodelprivate.html#rowsRemoved

    Parameters
    ----------

    parent : Optional[QStandardItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    row : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QStandardItemModelPrivate::rowsRemoved(QStandardItem *parent, int
    #      row, int count)
    self.uglySide.call(
        'ritual_ZN25QStandardItemModelPrivate11rowsRemovedEP13QStandardItem'
        'ii',
        self._addressOf(parent), row, count,
    )

  @overload(QStandardItem, int, int)
  @overload(NoneType, int, int)
  def columnsRemoved(
      self,
      parent: Optional[QStandardItem],
      column: int,
      count: int,
  ) -> None:
    """
    Calls Qt's 'void QStandardItemModelPrivate::columnsRemoved(QStandardItem
    *parent, int column, int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodelprivate.html#columnsRemoved

    Parameters
    ----------

    parent : Optional[QStandardItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    column : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QStandardItemModelPrivate::columnsRemoved(QStandardItem *parent,
    #      int column, int count)
    self.uglySide.call(
        'ritual_ZN25QStandardItemModelPrivate14columnsRemovedEP13QStandardI'
        'temii',
        self._addressOf(parent), column, count,
    )

  @overload(QModelIndex, QModelIndex)
  def _q_emitItemChanged(
      self,
      topLeft: QModelIndex,
      bottomRight: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void QStandardItemModelPrivate::_q_emitItemChanged(const
    QModelIndex &topLeft, const QModelIndex &bottomRight)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodelprivate.html#_q_emitItemChanged

    Parameters
    ----------

    topLeft : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    bottomRight : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QStandardItemModelPrivate::_q_emitItemChanged(const QModelIndex
    #      &topLeft, const QModelIndex &bottomRight)
    self.uglySide.call(
        'ritual_ZN25QStandardItemModelPrivate18_q_emitItemChangedERK11QMode'
        'lIndexS2_',
        self._valueOf(topLeft), self._valueOf(bottomRight),
    )

  @staticmethod
  def decodeDataRecursive(*__, **_) -> Never:
    """
    Qt's 'void QStandardItemModelPrivate::decodeDataRecursive(QDataStream
    &stream, QStandardItem *item)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QStandardItemModelPrivate.decodeDataRecursive' has no cute "
        "function yet. Qt's 'void "
        "QStandardItemModelPrivate::decodeDataRecursive(QDataStream "
        "&stream, QStandardItem *item)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def itemChanged(*__, **_) -> Never:
    """
    Qt's 'void QStandardItemModelPrivate::itemChanged(QStandardItem *item,
    const QList<int> &roles)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QStandardItemModelPrivate.itemChanged' has no cute function yet. "
        "Qt's 'void QStandardItemModelPrivate::itemChanged(QStandardItem "
        "*item, const QList<int> &roles)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def sort(*__, **_) -> Never:
    """
    Qt's 'void QStandardItemModelPrivate::sort(QStandardItem *parent, int
    column, Qt::SortOrder order)': cannot be called and cannot be called
    through the meta-object and cannot be copied: no header file has its
    code, Qt's source does not mark it or its class for use from outside Qt
    or writes it 'inline' or nowhere, and it is no signal, slot or invokable
    function giving back nothing, of a class built on QObject, and Qt's
    source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QStandardItemModelPrivate.sort' has no cute function yet. Qt's "
        "'void QStandardItemModelPrivate::sort(QStandardItem *parent, int "
        "column, Qt::SortOrder order)': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")
