"""
QTransposeProxyModelPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qtransposeproxymodel_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QTransposeProxyModelPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import Qt, QAbstractItemModel, QAbstractProxyModelPrivate, QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QModelIndex, QPersistentModelIndex, QTransposeProxyModel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QPersistentModelIndex = WAIT['QPersistentModelIndex']


class QTransposeProxyModelPrivate(QAbstractProxyModelPrivate):
  """
  The cute side of Qt's QTransposeProxyModelPrivate: a plain Python object
  standing in front of one C++ QTransposeProxyModelPrivate.

  It is built on the cute 'QAbstractProxyModelPrivate', as Qt's
  QTransposeProxyModelPrivate is built on Qt's QAbstractProxyModelPrivate,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTransposeProxyModelPrivate that has a ritual and
  that Python can call so far, 12 names in all: 'q_func',
  'uncheckedMapToSource', 'uncheckedMapFromSource', 'onLayoutChanged',
  'onLayoutAboutToBeChanged', 'onHeaderDataChanged',
  'onColumnsAboutToBeInserted', 'onColumnsAboutToBeRemoved',
  'onColumnsAboutToBeMoved', 'onRowsAboutToBeInserted',
  'onRowsAboutToBeRemoved', 'onRowsAboutToBeMoved'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QTransposeProxyModel *QTransposeProxyModelPrivate::q_func()
    const': takes in Python what 'QTransposeProxyModel
    *QTransposeProxyModelPrivate::q_func()' takes.
  - Qt's 'QTransposeProxyModelPrivate::~QTransposeProxyModelPrivate()': the
    destructor: Python never removes a C++ QTransposeProxyModelPrivate.
  - Qt's 'void QTransposeProxyModelPrivate::onDataChanged(const QModelIndex
    &topLeft, const QModelIndex &bottomRight, const QList<int> &roles)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 18 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QTransposeProxyModelPrivate is created at the first use, not by
    'QTransposeProxyModelPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTransposeProxyModelPrivate.
  - Each name of Qt's QTransposeProxyModelPrivate that has no cute function
    yet, 'onDataChanged', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTransposeProxyModelPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QModelIndex)
  def uncheckedMapToSource(self, proxyIndex: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex
    QTransposeProxyModelPrivate::uncheckedMapToSource(const QModelIndex
    &proxyIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtransposeproxymodelprivate.html

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
    #  QModelIndex QTransposeProxyModelPrivate::uncheckedMapToSource(const
    #      QModelIndex &proxyIndex) const
    address = self.uglySide.call(
        'ritual_ZNK27QTransposeProxyModelPrivate20uncheckedMapToSourceERK11'
        'QModelIndex',
        self._valueOf(proxyIndex),
    )
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def uncheckedMapFromSource(self, sourceIndex: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex
    QTransposeProxyModelPrivate::uncheckedMapFromSource(const QModelIndex
    &sourceIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtransposeproxymodelprivate.html

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
    #  QModelIndex QTransposeProxyModelPrivate::uncheckedMapFromSource(const
    #      QModelIndex &sourceIndex) const
    address = self.uglySide.call(
        'ritual_ZNK27QTransposeProxyModelPrivate22uncheckedMapFromSourceERK'
        '11QModelIndex',
        self._valueOf(sourceIndex),
    )
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

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
    'QTransposeProxyModelPrivate::QTransposeProxyModelPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtransposeproxymodelprivate.html
    """
    #  QTransposeProxyModelPrivate::QTransposeProxyModelPrivate()
    self._noteCreation(QTransposeProxyModelPrivate, lambda: Rituals.call(
        'ritual_ZN27QTransposeProxyModelPrivateC1Ev',
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

  def q_func(self) -> Optional[QTransposeProxyModel]:
    """
    Calls Qt's 'QTransposeProxyModel *QTransposeProxyModelPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtransposeproxymodelprivate.html#q_func

    Returns
    -------

    Optional[QTransposeProxyModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTransposeProxyModel *QTransposeProxyModelPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN27QTransposeProxyModelPrivate6q_funcEv',
    )
    from . import QTransposeProxyModel
    return QTransposeProxyModel._cuteAt(address)

  @overload(
      QList[QPersistentModelIndex], QAbstractItemModel.LayoutChangeHint,
  )
  def onLayoutChanged(
      self,
      parents: QList[QPersistentModelIndex],
      hint: QAbstractItemModel.LayoutChangeHint,
  ) -> None:
    """
    Calls Qt's 'void QTransposeProxyModelPrivate::onLayoutChanged(const
    QList<QPersistentModelIndex> &parents,
    QAbstractItemModel::LayoutChangeHint hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtransposeproxymodelprivate.html#onLayoutChanged

    Parameters
    ----------

    parents : QList[QPersistentModelIndex]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    hint : QAbstractItemModel.LayoutChangeHint
      Passed on as its number.
    """
    #  void QTransposeProxyModelPrivate::onLayoutChanged(const
    #      QList<QPersistentModelIndex> &parents,
    #      QAbstractItemModel::LayoutChangeHint hint)
    self.uglySide.call(
        'ritual_ZN27QTransposeProxyModelPrivate15onLayoutChangedERK5QListI2'
        '1QPersistentModelIndexEN18QAbstractItemModel16LayoutChangeHintE',
        self._valueOf(parents), hint.value,
    )

  @overload(
      QList[QPersistentModelIndex], QAbstractItemModel.LayoutChangeHint,
  )
  def onLayoutAboutToBeChanged(
      self,
      parents: QList[QPersistentModelIndex],
      hint: QAbstractItemModel.LayoutChangeHint,
  ) -> None:
    """
    Calls Qt's 'void
    QTransposeProxyModelPrivate::onLayoutAboutToBeChanged(const
    QList<QPersistentModelIndex> &parents,
    QAbstractItemModel::LayoutChangeHint hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtransposeproxymodelprivate.html

    Parameters
    ----------

    parents : QList[QPersistentModelIndex]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    hint : QAbstractItemModel.LayoutChangeHint
      Passed on as its number.
    """
    #  void QTransposeProxyModelPrivate::onLayoutAboutToBeChanged(const
    #      QList<QPersistentModelIndex> &parents,
    #      QAbstractItemModel::LayoutChangeHint hint)
    self.uglySide.call(
        'ritual_ZN27QTransposeProxyModelPrivate24onLayoutAboutToBeChangedER'
        'K5QListI21QPersistentModelIndexEN18QAbstractItemModel16LayoutChang'
        'eHintE',
        self._valueOf(parents), hint.value,
    )

  @overload(Qt.Orientation, int, int)
  def onHeaderDataChanged(
      self,
      orientation: Qt.Orientation,
      first: int,
      last: int,
  ) -> None:
    """
    Calls Qt's 'void
    QTransposeProxyModelPrivate::onHeaderDataChanged(Qt::Orientation
    orientation, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtransposeproxymodelprivate.html

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.

    first : int
      Passed on as it is.

    last : int
      Passed on as it is.
    """
    #  void QTransposeProxyModelPrivate::onHeaderDataChanged(Qt::Orientation
    #      orientation, int first, int last)
    self.uglySide.call(
        'ritual_ZN27QTransposeProxyModelPrivate19onHeaderDataChangedEN2Qt11'
        'OrientationEii',
        orientation.value, first, last,
    )

  @overload(QModelIndex, int, int)
  def onColumnsAboutToBeInserted(
      self,
      parent: QModelIndex,
      first: int,
      last: int,
  ) -> None:
    """
    Calls Qt's 'void
    QTransposeProxyModelPrivate::onColumnsAboutToBeInserted(const QModelIndex
    &parent, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtransposeproxymodelprivate.html

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    first : int
      Passed on as it is.

    last : int
      Passed on as it is.
    """
    #  void QTransposeProxyModelPrivate::onColumnsAboutToBeInserted(const
    #      QModelIndex &parent, int first, int last)
    self.uglySide.call(
        'ritual_ZN27QTransposeProxyModelPrivate26onColumnsAboutToBeInserted'
        'ERK11QModelIndexii',
        self._valueOf(parent), first, last,
    )

  @overload(QModelIndex, int, int)
  def onColumnsAboutToBeRemoved(
      self,
      parent: QModelIndex,
      first: int,
      last: int,
  ) -> None:
    """
    Calls Qt's 'void
    QTransposeProxyModelPrivate::onColumnsAboutToBeRemoved(const QModelIndex
    &parent, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtransposeproxymodelprivate.html

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    first : int
      Passed on as it is.

    last : int
      Passed on as it is.
    """
    #  void QTransposeProxyModelPrivate::onColumnsAboutToBeRemoved(const
    #      QModelIndex &parent, int first, int last)
    self.uglySide.call(
        'ritual_ZN27QTransposeProxyModelPrivate25onColumnsAboutToBeRemovedE'
        'RK11QModelIndexii',
        self._valueOf(parent), first, last,
    )

  @overload(QModelIndex, int, int, QModelIndex, int)
  def onColumnsAboutToBeMoved(
      self,
      sourceParent: QModelIndex,
      sourceStart: int,
      sourceEnd: int,
      destinationParent: QModelIndex,
      destinationColumn: int,
  ) -> None:
    """
    Calls Qt's 'void
    QTransposeProxyModelPrivate::onColumnsAboutToBeMoved(const QModelIndex
    &sourceParent, int sourceStart, int sourceEnd, const QModelIndex
    &destinationParent, int destinationColumn)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtransposeproxymodelprivate.html

    Parameters
    ----------

    sourceParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    sourceStart : int
      Passed on as it is.

    sourceEnd : int
      Passed on as it is.

    destinationParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    destinationColumn : int
      Passed on as it is.
    """
    #  void QTransposeProxyModelPrivate::onColumnsAboutToBeMoved(const
    #      QModelIndex &sourceParent, int sourceStart, int sourceEnd, const
    #      QModelIndex &destinationParent, int destinationColumn)
    self.uglySide.call(
        'ritual_ZN27QTransposeProxyModelPrivate23onColumnsAboutToBeMovedERK'
        '11QModelIndexiiS2_i',
        self._valueOf(sourceParent), sourceStart, sourceEnd,
        self._valueOf(destinationParent), destinationColumn,
    )

  @overload(QModelIndex, int, int)
  def onRowsAboutToBeInserted(
      self,
      parent: QModelIndex,
      first: int,
      last: int,
  ) -> None:
    """
    Calls Qt's 'void
    QTransposeProxyModelPrivate::onRowsAboutToBeInserted(const QModelIndex
    &parent, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtransposeproxymodelprivate.html

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    first : int
      Passed on as it is.

    last : int
      Passed on as it is.
    """
    #  void QTransposeProxyModelPrivate::onRowsAboutToBeInserted(const
    #      QModelIndex &parent, int first, int last)
    self.uglySide.call(
        'ritual_ZN27QTransposeProxyModelPrivate23onRowsAboutToBeInsertedERK'
        '11QModelIndexii',
        self._valueOf(parent), first, last,
    )

  @overload(QModelIndex, int, int)
  def onRowsAboutToBeRemoved(
      self,
      parent: QModelIndex,
      first: int,
      last: int,
  ) -> None:
    """
    Calls Qt's 'void
    QTransposeProxyModelPrivate::onRowsAboutToBeRemoved(const QModelIndex
    &parent, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtransposeproxymodelprivate.html

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    first : int
      Passed on as it is.

    last : int
      Passed on as it is.
    """
    #  void QTransposeProxyModelPrivate::onRowsAboutToBeRemoved(const
    #      QModelIndex &parent, int first, int last)
    self.uglySide.call(
        'ritual_ZN27QTransposeProxyModelPrivate22onRowsAboutToBeRemovedERK1'
        '1QModelIndexii',
        self._valueOf(parent), first, last,
    )

  @overload(QModelIndex, int, int, QModelIndex, int)
  def onRowsAboutToBeMoved(
      self,
      sourceParent: QModelIndex,
      sourceStart: int,
      sourceEnd: int,
      destinationParent: QModelIndex,
      destinationRow: int,
  ) -> None:
    """
    Calls Qt's 'void QTransposeProxyModelPrivate::onRowsAboutToBeMoved(const
    QModelIndex &sourceParent, int sourceStart, int sourceEnd, const
    QModelIndex &destinationParent, int destinationRow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtransposeproxymodelprivate.html

    Parameters
    ----------

    sourceParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    sourceStart : int
      Passed on as it is.

    sourceEnd : int
      Passed on as it is.

    destinationParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    destinationRow : int
      Passed on as it is.
    """
    #  void QTransposeProxyModelPrivate::onRowsAboutToBeMoved(const
    #      QModelIndex &sourceParent, int sourceStart, int sourceEnd, const
    #      QModelIndex &destinationParent, int destinationRow)
    self.uglySide.call(
        'ritual_ZN27QTransposeProxyModelPrivate20onRowsAboutToBeMovedERK11Q'
        'ModelIndexiiS2_i',
        self._valueOf(sourceParent), sourceStart, sourceEnd,
        self._valueOf(destinationParent), destinationRow,
    )

  @staticmethod
  def onDataChanged(*__, **_) -> Never:
    """
    Qt's 'void QTransposeProxyModelPrivate::onDataChanged(const QModelIndex
    &topLeft, const QModelIndex &bottomRight, const QList<int> &roles)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QTransposeProxyModelPrivate.onDataChanged' has no cute function "
        "yet. Qt's 'void QTransposeProxyModelPrivate::onDataChanged(const "
        "QModelIndex &topLeft, const QModelIndex &bottomRight, const "
        "QList<int> &roles)': takes a type Python has no way to hand over "
        "yet.")
