"""
QIdentityProxyModelPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qidentityproxymodel_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QIdentityProxyModelPrivate to be private: it declares the class
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

  from . import QIdentityProxyModel, QModelIndex, QPersistentModelIndex
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QPersistentModelIndex = WAIT['QPersistentModelIndex']


class QIdentityProxyModelPrivate(QAbstractProxyModelPrivate):
  """
  The cute side of Qt's QIdentityProxyModelPrivate: a plain Python object
  standing in front of one C++ QIdentityProxyModelPrivate.

  It is built on the cute 'QAbstractProxyModelPrivate', as Qt's
  QIdentityProxyModelPrivate is built on Qt's QAbstractProxyModelPrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QIdentityProxyModelPrivate that has a ritual and
  that Python can call so far, 18 names in all: 'q_func',
  'sourceRowsAboutToBeInserted', 'sourceRowsInserted',
  'sourceRowsAboutToBeRemoved', 'sourceRowsRemoved',
  'sourceRowsAboutToBeMoved', 'sourceRowsMoved',
  'sourceColumnsAboutToBeInserted', 'sourceColumnsInserted',
  'sourceColumnsAboutToBeRemoved', 'sourceColumnsRemoved',
  'sourceColumnsAboutToBeMoved', 'sourceColumnsMoved',
  'sourceHeaderDataChanged', 'sourceLayoutAboutToBeChanged',
  'sourceLayoutChanged', 'sourceModelAboutToBeReset', 'sourceModelReset'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QIdentityProxyModel *QIdentityProxyModelPrivate::q_func()
    const': takes in Python what 'QIdentityProxyModel
    *QIdentityProxyModelPrivate::q_func()' takes.
  - Qt's 'QIdentityProxyModelPrivate::~QIdentityProxyModelPrivate()': the
    destructor: Python never removes a C++ QIdentityProxyModelPrivate.
  - Qt's 'void QIdentityProxyModelPrivate::sourceDataChanged(const
    QModelIndex &topLeft, const QModelIndex &bottomRight, const QList<int>
    &roles)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QIdentityProxyModelPrivate is created at the first use, not by
    'QIdentityProxyModelPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QIdentityProxyModelPrivate.
  - Each name of Qt's QIdentityProxyModelPrivate that has no cute function
    yet, 'sourceDataChanged', holds a function that raises
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
  __qt_class__ = 'QIdentityProxyModelPrivate'

  #  A C++ QIdentityProxyModelPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QIdentityProxyModelPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    'QIdentityProxyModelPrivate::QIdentityProxyModelPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodelprivate.html
    """
    #  QIdentityProxyModelPrivate::QIdentityProxyModelPrivate()
    self._noteCreation(QIdentityProxyModelPrivate, lambda: Rituals.call(
        'ritual_ZN26QIdentityProxyModelPrivateC1Ev',
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

  def q_func(self) -> Optional[QIdentityProxyModel]:
    """
    Calls Qt's 'QIdentityProxyModel *QIdentityProxyModelPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodelprivate.html#q_func

    Returns
    -------

    Optional[QIdentityProxyModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIdentityProxyModel *QIdentityProxyModelPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN26QIdentityProxyModelPrivate6q_funcEv',
    )
    from . import QIdentityProxyModel
    return QIdentityProxyModel._cuteAt(address)

  @overload(QModelIndex, int, int)
  def sourceRowsAboutToBeInserted(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void
    QIdentityProxyModelPrivate::sourceRowsAboutToBeInserted(const QModelIndex
    &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodelprivate.html

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
    #  void QIdentityProxyModelPrivate::sourceRowsAboutToBeInserted(const
    #      QModelIndex &parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN26QIdentityProxyModelPrivate27sourceRowsAboutToBeInserted'
        'ERK11QModelIndexii',
        self._valueOf(parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def sourceRowsInserted(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QIdentityProxyModelPrivate::sourceRowsInserted(const
    QModelIndex &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodelprivate.html#sourceRowsInserted

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
    #  void QIdentityProxyModelPrivate::sourceRowsInserted(const QModelIndex
    #      &parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN26QIdentityProxyModelPrivate18sourceRowsInsertedERK11QMod'
        'elIndexii',
        self._valueOf(parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def sourceRowsAboutToBeRemoved(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void
    QIdentityProxyModelPrivate::sourceRowsAboutToBeRemoved(const QModelIndex
    &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodelprivate.html

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
    #  void QIdentityProxyModelPrivate::sourceRowsAboutToBeRemoved(const
    #      QModelIndex &parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN26QIdentityProxyModelPrivate26sourceRowsAboutToBeRemovedE'
        'RK11QModelIndexii',
        self._valueOf(parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def sourceRowsRemoved(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QIdentityProxyModelPrivate::sourceRowsRemoved(const
    QModelIndex &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodelprivate.html#sourceRowsRemoved

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
    #  void QIdentityProxyModelPrivate::sourceRowsRemoved(const QModelIndex
    #      &parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN26QIdentityProxyModelPrivate17sourceRowsRemovedERK11QMode'
        'lIndexii',
        self._valueOf(parent), start, end,
    )

  @overload(QModelIndex, int, int, QModelIndex, int)
  def sourceRowsAboutToBeMoved(
      self,
      sourceParent: QModelIndex,
      sourceStart: int,
      sourceEnd: int,
      destParent: QModelIndex,
      dest: int,
  ) -> None:
    """
    Calls Qt's 'void
    QIdentityProxyModelPrivate::sourceRowsAboutToBeMoved(const QModelIndex
    &sourceParent, int sourceStart, int sourceEnd, const QModelIndex
    &destParent, int dest)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodelprivate.html

    Parameters
    ----------

    sourceParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    sourceStart : int
      Passed on as it is.

    sourceEnd : int
      Passed on as it is.

    destParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    dest : int
      Passed on as it is.
    """
    #  void QIdentityProxyModelPrivate::sourceRowsAboutToBeMoved(const
    #      QModelIndex &sourceParent, int sourceStart, int sourceEnd, const
    #      QModelIndex &destParent, int dest)
    self.uglySide.call(
        'ritual_ZN26QIdentityProxyModelPrivate24sourceRowsAboutToBeMovedERK'
        '11QModelIndexiiS2_i',
        self._valueOf(sourceParent), sourceStart, sourceEnd,
        self._valueOf(destParent), dest,
    )

  @overload(QModelIndex, int, int, QModelIndex, int)
  def sourceRowsMoved(
      self,
      sourceParent: QModelIndex,
      sourceStart: int,
      sourceEnd: int,
      destParent: QModelIndex,
      dest: int,
  ) -> None:
    """
    Calls Qt's 'void QIdentityProxyModelPrivate::sourceRowsMoved(const
    QModelIndex &sourceParent, int sourceStart, int sourceEnd, const
    QModelIndex &destParent, int dest)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodelprivate.html#sourceRowsMoved

    Parameters
    ----------

    sourceParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    sourceStart : int
      Passed on as it is.

    sourceEnd : int
      Passed on as it is.

    destParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    dest : int
      Passed on as it is.
    """
    #  void QIdentityProxyModelPrivate::sourceRowsMoved(const QModelIndex
    #      &sourceParent, int sourceStart, int sourceEnd, const QModelIndex
    #      &destParent, int dest)
    self.uglySide.call(
        'ritual_ZN26QIdentityProxyModelPrivate15sourceRowsMovedERK11QModelI'
        'ndexiiS2_i',
        self._valueOf(sourceParent), sourceStart, sourceEnd,
        self._valueOf(destParent), dest,
    )

  @overload(QModelIndex, int, int)
  def sourceColumnsAboutToBeInserted(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void
    QIdentityProxyModelPrivate::sourceColumnsAboutToBeInserted(const
    QModelIndex &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodelprivate.html

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
    #  void QIdentityProxyModelPrivate::sourceColumnsAboutToBeInserted(const
    #      QModelIndex &parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN26QIdentityProxyModelPrivate30sourceColumnsAboutToBeInser'
        'tedERK11QModelIndexii',
        self._valueOf(parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def sourceColumnsInserted(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QIdentityProxyModelPrivate::sourceColumnsInserted(const
    QModelIndex &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodelprivate.html

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
    #  void QIdentityProxyModelPrivate::sourceColumnsInserted(const
    #      QModelIndex &parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN26QIdentityProxyModelPrivate21sourceColumnsInsertedERK11Q'
        'ModelIndexii',
        self._valueOf(parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def sourceColumnsAboutToBeRemoved(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void
    QIdentityProxyModelPrivate::sourceColumnsAboutToBeRemoved(const
    QModelIndex &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodelprivate.html

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
    #  void QIdentityProxyModelPrivate::sourceColumnsAboutToBeRemoved(const
    #      QModelIndex &parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN26QIdentityProxyModelPrivate29sourceColumnsAboutToBeRemov'
        'edERK11QModelIndexii',
        self._valueOf(parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def sourceColumnsRemoved(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QIdentityProxyModelPrivate::sourceColumnsRemoved(const
    QModelIndex &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodelprivate.html

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
    #  void QIdentityProxyModelPrivate::sourceColumnsRemoved(const
    #      QModelIndex &parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN26QIdentityProxyModelPrivate20sourceColumnsRemovedERK11QM'
        'odelIndexii',
        self._valueOf(parent), start, end,
    )

  @overload(QModelIndex, int, int, QModelIndex, int)
  def sourceColumnsAboutToBeMoved(
      self,
      sourceParent: QModelIndex,
      sourceStart: int,
      sourceEnd: int,
      destParent: QModelIndex,
      dest: int,
  ) -> None:
    """
    Calls Qt's 'void
    QIdentityProxyModelPrivate::sourceColumnsAboutToBeMoved(const QModelIndex
    &sourceParent, int sourceStart, int sourceEnd, const QModelIndex
    &destParent, int dest)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodelprivate.html

    Parameters
    ----------

    sourceParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    sourceStart : int
      Passed on as it is.

    sourceEnd : int
      Passed on as it is.

    destParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    dest : int
      Passed on as it is.
    """
    #  void QIdentityProxyModelPrivate::sourceColumnsAboutToBeMoved(const
    #      QModelIndex &sourceParent, int sourceStart, int sourceEnd, const
    #      QModelIndex &destParent, int dest)
    self.uglySide.call(
        'ritual_ZN26QIdentityProxyModelPrivate27sourceColumnsAboutToBeMoved'
        'ERK11QModelIndexiiS2_i',
        self._valueOf(sourceParent), sourceStart, sourceEnd,
        self._valueOf(destParent), dest,
    )

  @overload(QModelIndex, int, int, QModelIndex, int)
  def sourceColumnsMoved(
      self,
      sourceParent: QModelIndex,
      sourceStart: int,
      sourceEnd: int,
      destParent: QModelIndex,
      dest: int,
  ) -> None:
    """
    Calls Qt's 'void QIdentityProxyModelPrivate::sourceColumnsMoved(const
    QModelIndex &sourceParent, int sourceStart, int sourceEnd, const
    QModelIndex &destParent, int dest)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodelprivate.html#sourceColumnsMoved

    Parameters
    ----------

    sourceParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    sourceStart : int
      Passed on as it is.

    sourceEnd : int
      Passed on as it is.

    destParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    dest : int
      Passed on as it is.
    """
    #  void QIdentityProxyModelPrivate::sourceColumnsMoved(const QModelIndex
    #      &sourceParent, int sourceStart, int sourceEnd, const QModelIndex
    #      &destParent, int dest)
    self.uglySide.call(
        'ritual_ZN26QIdentityProxyModelPrivate18sourceColumnsMovedERK11QMod'
        'elIndexiiS2_i',
        self._valueOf(sourceParent), sourceStart, sourceEnd,
        self._valueOf(destParent), dest,
    )

  @overload(Qt.Orientation, int, int)
  def sourceHeaderDataChanged(
      self,
      orientation: Qt.Orientation,
      first: int,
      last: int,
  ) -> None:
    """
    Calls Qt's 'void
    QIdentityProxyModelPrivate::sourceHeaderDataChanged(Qt::Orientation
    orientation, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodelprivate.html

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.

    first : int
      Passed on as it is.

    last : int
      Passed on as it is.
    """
    #  void QIdentityProxyModelPrivate::sourceHeaderDataChanged(Qt::
    #      Orientation orientation, int first, int last)
    self.uglySide.call(
        'ritual_ZN26QIdentityProxyModelPrivate23sourceHeaderDataChangedEN2Q'
        't11OrientationEii',
        orientation.value, first, last,
    )

  @overload(
      QList[QPersistentModelIndex], QAbstractItemModel.LayoutChangeHint,
  )
  def sourceLayoutAboutToBeChanged(
      self,
      sourceParents: QList[QPersistentModelIndex],
      hint: QAbstractItemModel.LayoutChangeHint,
  ) -> None:
    """
    Calls Qt's 'void
    QIdentityProxyModelPrivate::sourceLayoutAboutToBeChanged(const
    QList<QPersistentModelIndex> &sourceParents,
    QAbstractItemModel::LayoutChangeHint hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodelprivate.html

    Parameters
    ----------

    sourceParents : QList[QPersistentModelIndex]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    hint : QAbstractItemModel.LayoutChangeHint
      Passed on as its number.
    """
    #  void QIdentityProxyModelPrivate::sourceLayoutAboutToBeChanged(const
    #      QList<QPersistentModelIndex> &sourceParents,
    #      QAbstractItemModel::LayoutChangeHint hint)
    self.uglySide.call(
        'ritual_ZN26QIdentityProxyModelPrivate28sourceLayoutAboutToBeChange'
        'dERK5QListI21QPersistentModelIndexEN18QAbstractItemModel16LayoutCh'
        'angeHintE',
        self._valueOf(sourceParents), hint.value,
    )

  @overload(
      QList[QPersistentModelIndex], QAbstractItemModel.LayoutChangeHint,
  )
  def sourceLayoutChanged(
      self,
      sourceParents: QList[QPersistentModelIndex],
      hint: QAbstractItemModel.LayoutChangeHint,
  ) -> None:
    """
    Calls Qt's 'void QIdentityProxyModelPrivate::sourceLayoutChanged(const
    QList<QPersistentModelIndex> &sourceParents,
    QAbstractItemModel::LayoutChangeHint hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodelprivate.html

    Parameters
    ----------

    sourceParents : QList[QPersistentModelIndex]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    hint : QAbstractItemModel.LayoutChangeHint
      Passed on as its number.
    """
    #  void QIdentityProxyModelPrivate::sourceLayoutChanged(const
    #      QList<QPersistentModelIndex> &sourceParents,
    #      QAbstractItemModel::LayoutChangeHint hint)
    self.uglySide.call(
        'ritual_ZN26QIdentityProxyModelPrivate19sourceLayoutChangedERK5QLis'
        'tI21QPersistentModelIndexEN18QAbstractItemModel16LayoutChangeHintE',
        self._valueOf(sourceParents), hint.value,
    )

  def sourceModelAboutToBeReset(self) -> None:
    """
    Calls Qt's 'void
    QIdentityProxyModelPrivate::sourceModelAboutToBeReset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodelprivate.html
    """
    #  void QIdentityProxyModelPrivate::sourceModelAboutToBeReset()
    self.uglySide.call(
        'ritual_ZN26QIdentityProxyModelPrivate25sourceModelAboutToBeResetEv',
    )

  def sourceModelReset(self) -> None:
    """
    Calls Qt's 'void QIdentityProxyModelPrivate::sourceModelReset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qidentityproxymodelprivate.html#sourceModelReset
    """
    #  void QIdentityProxyModelPrivate::sourceModelReset()
    self.uglySide.call(
        'ritual_ZN26QIdentityProxyModelPrivate16sourceModelResetEv',
    )

  @staticmethod
  def sourceDataChanged(*__, **_) -> Never:
    """
    Qt's 'void QIdentityProxyModelPrivate::sourceDataChanged(const
    QModelIndex &topLeft, const QModelIndex &bottomRight, const QList<int>
    &roles)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QIdentityProxyModelPrivate.sourceDataChanged' has no cute "
        "function yet. Qt's 'void "
        "QIdentityProxyModelPrivate::sourceDataChanged(const QModelIndex "
        "&topLeft, const QModelIndex &bottomRight, const QList<int> "
        "&roles)': takes a type Python has no way to hand over yet.")
