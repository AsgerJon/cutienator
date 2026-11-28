"""
QAbstractProxyModelPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qabstractproxymodel_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAbstractProxyModelPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import Qt, QAbstractItemModelPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QAbstractItemModel, QAbstractProxyModel, QModelIndex
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QModelIndex = WAIT['QModelIndex']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractProxyModelPrivate(QAbstractItemModelPrivate):
  """
  The cute side of Qt's QAbstractProxyModelPrivate: a plain Python object
  standing in front of one C++ QAbstractProxyModelPrivate.

  It is built on the cute 'QAbstractItemModelPrivate', as Qt's
  QAbstractProxyModelPrivate is built on Qt's QAbstractItemModelPrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractProxyModelPrivate that has a ritual and
  that Python can call so far, 14 names in all: 'q_func',
  'setModelForwarder', 'modelChangedForwarder', 'getModelForwarder',
  '_qt_property_model_offset', '_q_sourceModelDestroyed',
  '_q_sourceModelRowsAboutToBeInserted', '_q_sourceModelRowsInserted',
  '_q_sourceModelRowsRemoved', '_q_sourceModelColumnsAboutToBeInserted',
  '_q_sourceModelColumnsInserted', '_q_sourceModelColumnsRemoved',
  'scheduleHeaderUpdate', 'emitHeaderDataChanged'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAbstractProxyModel *QAbstractProxyModelPrivate::q_func()
    const': takes in Python what 'QAbstractProxyModel
    *QAbstractProxyModelPrivate::q_func()' takes.
  - Qt's 'QAbstractProxyModelPrivate::~QAbstractProxyModelPrivate()': the
    destructor: Python never removes a C++ QAbstractProxyModelPrivate.
  - Qt's 'void QAbstractProxyModelPrivate::mapDropCoordinatesToSource(int
    row, int column, const QModelIndex &parent, int *source_row, int
    *source_column, QModelIndex *source_parent) const': takes a number to
    change where it is.

  What to expect
  --------------

  - The C++ QAbstractProxyModelPrivate is created at the first use, not by
    'QAbstractProxyModelPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractProxyModelPrivate.
  - Each name of Qt's QAbstractProxyModelPrivate that has no cute function
    yet, 'mapDropCoordinatesToSource', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _qt_property_model_offset() -> int:
    """
    Calls Qt's 'size_t
    QAbstractProxyModelPrivate::_qt_property_model_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractproxymodelprivate.html
    """
    #  size_t QAbstractProxyModelPrivate::_qt_property_model_offset()
    return Rituals.call(
        'ritual_ZN26QAbstractProxyModelPrivate25_qt_property_model_offsetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractProxyModelPrivate'

  #  A C++ QAbstractProxyModelPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractProxyModelPrivate'

  #  The functions Qt calls itself that QAbstractProxyModelPrivate is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      '_q_sourceModelDestroyed': (
          ('_ZN26QAbstractProxyModelPrivate23_q_sourceModelDestroyedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getModelForwarder(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel
    *QAbstractProxyModelPrivate::getModelForwarder() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractproxymodelprivate.html#getModelForwarder

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *QAbstractProxyModelPrivate::getModelForwarder()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK26QAbstractProxyModelPrivate17getModelForwarderEv',
    )
    from . import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setModelForwarder(
      self,
      sourceModel: Optional[QAbstractItemModel],
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractProxyModelPrivate::setModelForwarder(QAbstractItemModel
    *sourceModel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractproxymodelprivate.html#setModelForwarder

    Parameters
    ----------

    sourceModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractProxyModelPrivate::setModelForwarder(QAbstractItemModel
    #      *sourceModel)
    self.uglySide.call(
        'ritual_ZN26QAbstractProxyModelPrivate17setModelForwarderEP18QAbstr'
        'actItemModel',
        self._addressOf(sourceModel),
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
    'QAbstractProxyModelPrivate::QAbstractProxyModelPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractproxymodelprivate.html
    """
    #  QAbstractProxyModelPrivate::QAbstractProxyModelPrivate()
    self._noteCreation(QAbstractProxyModelPrivate, lambda: Rituals.call(
        'ritual_ZN26QAbstractProxyModelPrivateC1Ev',
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

  def q_func(self) -> Optional[QAbstractProxyModel]:
    """
    Calls Qt's 'QAbstractProxyModel *QAbstractProxyModelPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractproxymodelprivate.html#q_func

    Returns
    -------

    Optional[QAbstractProxyModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractProxyModel *QAbstractProxyModelPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN26QAbstractProxyModelPrivate6q_funcEv',
    )
    from . import QAbstractProxyModel
    return QAbstractProxyModel._cuteAt(address)

  def modelChangedForwarder(self) -> None:
    """
    Calls Qt's 'void QAbstractProxyModelPrivate::modelChangedForwarder()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractproxymodelprivate.html
    """
    #  void QAbstractProxyModelPrivate::modelChangedForwarder()
    self.uglySide.call(
        'ritual_ZN26QAbstractProxyModelPrivate21modelChangedForwarderEv',
    )

  def _q_sourceModelDestroyed(self) -> None:
    """
    Calls Qt's 'void QAbstractProxyModelPrivate::_q_sourceModelDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractproxymodelprivate.html
    """
    #  void QAbstractProxyModelPrivate::_q_sourceModelDestroyed()
    ritual = (
        'ritual_ZN26QAbstractProxyModelPrivate23_q_sourceModelDestroyedEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QAbstractProxyModelPrivate23_q_sourceModelDestroy'
          'edEv')
    self.uglySide.call(ritual)

  @overload(QModelIndex, int, int)
  def _q_sourceModelRowsAboutToBeInserted(
      self,
      parent: QModelIndex,
      first: int,
      last: int,
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractProxyModelPrivate::_q_sourceModelRowsAboutToBeInserted(const
    QModelIndex &parent, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractproxymodelprivate.html

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
    #  void QAbstractProxyModelPrivate::_q_sourceModelRowsAboutToBeInserted(
    #      const QModelIndex &parent, int first, int last)
    self.uglySide.call(
        'ritual_ZN26QAbstractProxyModelPrivate35_q_sourceModelRowsAboutToBe'
        'InsertedERK11QModelIndexii',
        self._valueOf(parent), first, last,
    )

  @overload(QModelIndex, int, int)
  def _q_sourceModelRowsInserted(
      self,
      parent: QModelIndex,
      first: int,
      last: int,
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractProxyModelPrivate::_q_sourceModelRowsInserted(const QModelIndex
    &parent, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractproxymodelprivate.html

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
    #  void QAbstractProxyModelPrivate::_q_sourceModelRowsInserted(const
    #      QModelIndex &parent, int first, int last)
    self.uglySide.call(
        'ritual_ZN26QAbstractProxyModelPrivate26_q_sourceModelRowsInsertedE'
        'RK11QModelIndexii',
        self._valueOf(parent), first, last,
    )

  @overload(QModelIndex, int, int)
  def _q_sourceModelRowsRemoved(
      self,
      parent: QModelIndex,
      first: int,
      last: int,
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractProxyModelPrivate::_q_sourceModelRowsRemoved(const QModelIndex
    &parent, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractproxymodelprivate.html

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
    #  void QAbstractProxyModelPrivate::_q_sourceModelRowsRemoved(const
    #      QModelIndex &parent, int first, int last)
    self.uglySide.call(
        'ritual_ZN26QAbstractProxyModelPrivate25_q_sourceModelRowsRemovedER'
        'K11QModelIndexii',
        self._valueOf(parent), first, last,
    )

  @overload(QModelIndex, int, int)
  def _q_sourceModelColumnsAboutToBeInserted(
      self,
      parent: QModelIndex,
      first: int,
      last: int,
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractProxyModelPrivate::_q_sourceModelColumnsAboutToBeInserted(const
    QModelIndex &parent, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractproxymodelprivate.html

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
    #  void QAbstractProxyModelPrivate::
    #      _q_sourceModelColumnsAboutToBeInserted(const QModelIndex &parent,
    #      int first, int last)
    self.uglySide.call(
        'ritual_ZN26QAbstractProxyModelPrivate38_q_sourceModelColumnsAboutT'
        'oBeInsertedERK11QModelIndexii',
        self._valueOf(parent), first, last,
    )

  @overload(QModelIndex, int, int)
  def _q_sourceModelColumnsInserted(
      self,
      parent: QModelIndex,
      first: int,
      last: int,
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractProxyModelPrivate::_q_sourceModelColumnsInserted(const
    QModelIndex &parent, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractproxymodelprivate.html

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
    #  void QAbstractProxyModelPrivate::_q_sourceModelColumnsInserted(const
    #      QModelIndex &parent, int first, int last)
    self.uglySide.call(
        'ritual_ZN26QAbstractProxyModelPrivate29_q_sourceModelColumnsInsert'
        'edERK11QModelIndexii',
        self._valueOf(parent), first, last,
    )

  @overload(QModelIndex, int, int)
  def _q_sourceModelColumnsRemoved(
      self,
      parent: QModelIndex,
      first: int,
      last: int,
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractProxyModelPrivate::_q_sourceModelColumnsRemoved(const
    QModelIndex &parent, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractproxymodelprivate.html

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
    #  void QAbstractProxyModelPrivate::_q_sourceModelColumnsRemoved(const
    #      QModelIndex &parent, int first, int last)
    self.uglySide.call(
        'ritual_ZN26QAbstractProxyModelPrivate28_q_sourceModelColumnsRemove'
        'dERK11QModelIndexii',
        self._valueOf(parent), first, last,
    )

  @overload(Qt.Orientation)
  def scheduleHeaderUpdate(self, orientation: Qt.Orientation) -> None:
    """
    Calls Qt's 'void
    QAbstractProxyModelPrivate::scheduleHeaderUpdate(Qt::Orientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractproxymodelprivate.html

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QAbstractProxyModelPrivate::scheduleHeaderUpdate(Qt::Orientation
    #      orientation)
    self.uglySide.call(
        'ritual_ZN26QAbstractProxyModelPrivate20scheduleHeaderUpdateEN2Qt11'
        'OrientationE',
        orientation.value,
    )

  def emitHeaderDataChanged(self) -> None:
    """
    Calls Qt's 'void QAbstractProxyModelPrivate::emitHeaderDataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractproxymodelprivate.html
    """
    #  void QAbstractProxyModelPrivate::emitHeaderDataChanged()
    self.uglySide.call(
        'ritual_ZN26QAbstractProxyModelPrivate21emitHeaderDataChangedEv',
    )

  @staticmethod
  def mapDropCoordinatesToSource(*__, **_) -> Never:
    """
    Qt's 'void QAbstractProxyModelPrivate::mapDropCoordinatesToSource(int
    row, int column, const QModelIndex &parent, int *source_row, int
    *source_column, QModelIndex *source_parent) const': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QAbstractProxyModelPrivate.mapDropCoordinatesToSource' has no "
        "cute function yet. Qt's 'void "
        "QAbstractProxyModelPrivate::mapDropCoordinatesToSource(int row, "
        "int column, const QModelIndex &parent, int *source_row, int "
        "*source_column, QModelIndex *source_parent) const': takes a number "
        "to change where it is.")
