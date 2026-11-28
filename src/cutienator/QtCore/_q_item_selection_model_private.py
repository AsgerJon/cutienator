"""
QItemSelectionModelPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qitemselectionmodel_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QItemSelectionModelPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QItemSelectionModel, QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QAbstractItemModel, QItemSelection, QModelIndex
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QItemSelection = WAIT['QItemSelection']
  QModelIndex = WAIT['QModelIndex']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QItemSelectionModelPrivate(QObjectPrivate):
  """
  The cute side of Qt's QItemSelectionModelPrivate: a plain Python object
  standing in front of one C++ QItemSelectionModelPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QItemSelectionModelPrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QItemSelectionModelPrivate that has a ritual and
  that Python can call so far, 12 names in all: 'q_func', 'expandSelection',
  'rowsAboutToBeRemoved', 'columnsAboutToBeRemoved', 'rowsAboutToBeInserted',
  'columnsAboutToBeInserted', 'modelDestroyed', 'finalize', 'setModel',
  'disconnectModel', 'modelChanged', '_qt_property_model_offset'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QItemSelectionModel *QItemSelectionModelPrivate::q_func()
    const': takes in Python what 'QItemSelectionModel
    *QItemSelectionModelPrivate::q_func()' takes.
  - Qt's 'QItemSelectionModelPrivate::~QItemSelectionModelPrivate()': the
    destructor: Python never removes a C++ QItemSelectionModelPrivate.
  - Qt's 'void QItemSelectionModelPrivate::remove(QList<QItemSelectionRange>
    &r)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  5 of the 21 functions Qt declares: 3 leans on 'QItemSelectionModelPrivate;
  2 Qt's library has no name for it, and its code in Qt's source does not
  compile apart from its file.

  What to expect
  --------------

  - The C++ QItemSelectionModelPrivate is created at the first use, not by
    'QItemSelectionModelPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QItemSelectionModelPrivate.
  - Each name of Qt's QItemSelectionModelPrivate that has no cute function
    yet, 'initModel', 'layoutAboutToBeChanged', 'layoutChanged', 'remove',
    'triggerLayoutChanged', 'triggerLayoutToBeChanged', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _qt_property_model_offset() -> int:
    """
    Calls Qt's 'size_t
    QItemSelectionModelPrivate::_qt_property_model_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemselectionmodelprivate.html
    """
    #  size_t QItemSelectionModelPrivate::_qt_property_model_offset()
    return Rituals.call(
        'ritual_ZN26QItemSelectionModelPrivate25_qt_property_model_offsetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QItemSelectionModelPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QItemSelection, QItemSelectionModel.SelectionFlags)
  def expandSelection(
      self,
      selection: QItemSelection,
      command: QItemSelectionModel.SelectionFlags,
  ) -> QItemSelection:
    """
    Calls Qt's 'QItemSelection
    QItemSelectionModelPrivate::expandSelection(const QItemSelection
    &selection, QItemSelectionModel::SelectionFlags command) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemselectionmodelprivate.html#expandSelection

    Parameters
    ----------

    selection : QItemSelection
      Passed on as a value: Qt reads the C++ QItemSelection, which stays
      Python's own.

    command : QItemSelectionModel.SelectionFlags
      Passed on as its number.

    Returns
    -------

    QItemSelection
      A new cute QItemSelection around the copy Qt gave back. Python owns it.
    """
    #  QItemSelection QItemSelectionModelPrivate::expandSelection(const
    #      QItemSelection &selection, QItemSelectionModel::SelectionFlags
    #      command) const
    address = self.uglySide.call(
        'ritual_ZNK26QItemSelectionModelPrivate15expandSelectionERK14QItemS'
        'election6QFlagsIN19QItemSelectionModel13SelectionFlagEE',
        self._valueOf(selection), command.value,
    )
    from . import QItemSelection
    return QItemSelection._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setModel(self, mod: Optional[QAbstractItemModel]) -> None:
    """
    Calls Qt's 'void QItemSelectionModelPrivate::setModel(QAbstractItemModel
    *mod)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemselectionmodelprivate.html#setModel

    Parameters
    ----------

    mod : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QItemSelectionModelPrivate::setModel(QAbstractItemModel *mod)
    self.uglySide.call(
        'ritual_ZN26QItemSelectionModelPrivate8setModelEP18QAbstractItemMod'
        'el',
        self._addressOf(mod),
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
    'QItemSelectionModelPrivate::QItemSelectionModelPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemselectionmodelprivate.html
    """
    #  QItemSelectionModelPrivate::QItemSelectionModelPrivate()
    self._noteCreation(QItemSelectionModelPrivate, lambda: Rituals.call(
        'ritual_ZN26QItemSelectionModelPrivateC1Ev',
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

  def q_func(self) -> Optional[QItemSelectionModel]:
    """
    Calls Qt's 'QItemSelectionModel *QItemSelectionModelPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemselectionmodelprivate.html#q_func

    Returns
    -------

    Optional[QItemSelectionModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QItemSelectionModel *QItemSelectionModelPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN26QItemSelectionModelPrivate6q_funcEv',
    )
    return QItemSelectionModel._cuteAt(address)

  @overload(QModelIndex, int, int)
  def rowsAboutToBeRemoved(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QItemSelectionModelPrivate::rowsAboutToBeRemoved(const
    QModelIndex &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemselectionmodelprivate.html

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
    #  void QItemSelectionModelPrivate::rowsAboutToBeRemoved(const
    #      QModelIndex &parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN26QItemSelectionModelPrivate20rowsAboutToBeRemovedERK11QM'
        'odelIndexii',
        self._valueOf(parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def columnsAboutToBeRemoved(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void
    QItemSelectionModelPrivate::columnsAboutToBeRemoved(const QModelIndex
    &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemselectionmodelprivate.html

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
    #  void QItemSelectionModelPrivate::columnsAboutToBeRemoved(const
    #      QModelIndex &parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN26QItemSelectionModelPrivate23columnsAboutToBeRemovedERK1'
        '1QModelIndexii',
        self._valueOf(parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def rowsAboutToBeInserted(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QItemSelectionModelPrivate::rowsAboutToBeInserted(const
    QModelIndex &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemselectionmodelprivate.html

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
    #  void QItemSelectionModelPrivate::rowsAboutToBeInserted(const
    #      QModelIndex &parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN26QItemSelectionModelPrivate21rowsAboutToBeInsertedERK11Q'
        'ModelIndexii',
        self._valueOf(parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def columnsAboutToBeInserted(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void
    QItemSelectionModelPrivate::columnsAboutToBeInserted(const QModelIndex
    &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemselectionmodelprivate.html

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
    #  void QItemSelectionModelPrivate::columnsAboutToBeInserted(const
    #      QModelIndex &parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN26QItemSelectionModelPrivate24columnsAboutToBeInsertedERK'
        '11QModelIndexii',
        self._valueOf(parent), start, end,
    )

  def modelDestroyed(self) -> None:
    """
    Calls Qt's 'void QItemSelectionModelPrivate::modelDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemselectionmodelprivate.html#modelDestroyed
    """
    #  void QItemSelectionModelPrivate::modelDestroyed()
    self.uglySide.call(
        'ritual_ZN26QItemSelectionModelPrivate14modelDestroyedEv',
    )

  def finalize(self) -> None:
    """
    Calls Qt's 'void QItemSelectionModelPrivate::finalize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemselectionmodelprivate.html#finalize
    """
    #  void QItemSelectionModelPrivate::finalize()
    self.uglySide.call('ritual_ZN26QItemSelectionModelPrivate8finalizeEv')

  def disconnectModel(self) -> None:
    """
    Calls Qt's 'void QItemSelectionModelPrivate::disconnectModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemselectionmodelprivate.html#disconnectModel
    """
    #  void QItemSelectionModelPrivate::disconnectModel()
    self.uglySide.call(
        'ritual_ZN26QItemSelectionModelPrivate15disconnectModelEv',
    )

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def modelChanged(self, mod: Optional[QAbstractItemModel]) -> None:
    """
    Calls Qt's 'void
    QItemSelectionModelPrivate::modelChanged(QAbstractItemModel *mod)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemselectionmodelprivate.html#modelChanged

    Parameters
    ----------

    mod : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QItemSelectionModelPrivate::modelChanged(QAbstractItemModel *mod)
    self.uglySide.call(
        'ritual_ZN26QItemSelectionModelPrivate12modelChangedEP18QAbstractIt'
        'emModel',
        self._addressOf(mod),
    )

  @staticmethod
  def initModel(*__, **_) -> Never:
    """
    Qt's 'void QItemSelectionModelPrivate::initModel(QAbstractItemModel
    *model)': leans on
    'QItemSelectionModelPrivate::layoutChanged(QList<QPersistentModelIndex>
    const&, QAbstractItemModel::LayoutChangeHint)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QItemSelectionModelPrivate.initModel' has no cute function yet. "
        "Qt's 'void "
        "QItemSelectionModelPrivate::initModel(QAbstractItemModel *model)': "
        "leans on "
        "'QItemSelectionModelPrivate::layoutChanged(QList<QPersistentModelIn"
        "dex> const&, QAbstractItemModel::LayoutChangeHint)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def layoutAboutToBeChanged(*__, **_) -> Never:
    """
    Qt's 'void QItemSelectionModelPrivate::layoutAboutToBeChanged(const
    QList<QPersistentModelIndex> &parents,
    QAbstractItemModel::LayoutChangeHint hint)': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'qSelectionPersistentRowLengths'.
    """
    raise NotImplementedError(
        "'QItemSelectionModelPrivate.layoutAboutToBeChanged' has no cute "
        "function yet. Qt's 'void "
        "QItemSelectionModelPrivate::layoutAboutToBeChanged(const "
        "QList<QPersistentModelIndex> &parents, "
        "QAbstractItemModel::LayoutChangeHint hint)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier "
        "'qSelectionPersistentRowLengths'.")

  @staticmethod
  def layoutChanged(*__, **_) -> Never:
    """
    Qt's 'void QItemSelectionModelPrivate::layoutChanged(const
    QList<QPersistentModelIndex> &parents,
    QAbstractItemModel::LayoutChangeHint hint)': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'qt_PersistentModelIndexLessThan'.
    """
    raise NotImplementedError(
        "'QItemSelectionModelPrivate.layoutChanged' has no cute function "
        "yet. Qt's 'void QItemSelectionModelPrivate::layoutChanged(const "
        "QList<QPersistentModelIndex> &parents, "
        "QAbstractItemModel::LayoutChangeHint hint)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier "
        "'qt_PersistentModelIndexLessThan'.")

  @staticmethod
  def remove(*__, **_) -> Never:
    """
    Qt's 'void QItemSelectionModelPrivate::remove(QList<QItemSelectionRange>
    &r)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QItemSelectionModelPrivate.remove' has no cute function yet. Qt's "
        "'void "
        "QItemSelectionModelPrivate::remove(QList<QItemSelectionRange> "
        "&r)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def triggerLayoutChanged(*__, **_) -> Never:
    """
    Qt's 'void QItemSelectionModelPrivate::triggerLayoutChanged()': leans on
    'QItemSelectionModelPrivate::layoutChanged(QList<QPersistentModelIndex>
    const&, QAbstractItemModel::LayoutChangeHint)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QItemSelectionModelPrivate.triggerLayoutChanged' has no cute "
        "function yet. Qt's 'void "
        "QItemSelectionModelPrivate::triggerLayoutChanged()': leans on "
        "'QItemSelectionModelPrivate::layoutChanged(QList<QPersistentModelIn"
        "dex> const&, QAbstractItemModel::LayoutChangeHint)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def triggerLayoutToBeChanged(*__, **_) -> Never:
    """
    Qt's 'void QItemSelectionModelPrivate::triggerLayoutToBeChanged()': leans
    on 'QItemSelectionModelPrivate::layoutAboutToBeChanged(
    QList<QPersistentModelIndex> const&,
    QAbstractItemModel::LayoutChangeHint)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QItemSelectionModelPrivate.triggerLayoutToBeChanged' has no cute "
        "function yet. Qt's 'void "
        "QItemSelectionModelPrivate::triggerLayoutToBeChanged()': leans on "
        "'QItemSelectionModelPrivate::layoutAboutToBeChanged(QList<QPersiste"
        "ntModelIndex> const&, QAbstractItemModel::LayoutChangeHint)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")
