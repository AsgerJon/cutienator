"""
QSqlQueryModelPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSql/6.12.0/QtSql/private/qsqlquerymodel_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSqlQueryModelPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QAbstractItemModelPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSqlQueryModel


class QSqlQueryModelPrivate(QAbstractItemModelPrivate):
  """
  The cute side of Qt's QSqlQueryModelPrivate: a plain Python object standing
  in front of one C++ QSqlQueryModelPrivate.

  It is built on the cute 'QAbstractItemModelPrivate', as Qt's
  QSqlQueryModelPrivate is built on Qt's QAbstractItemModelPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QSqlQueryModelPrivate that has a ritual and that
  Python can call so far, 4 names in all: 'q_func', 'prefetch',
  'initColOffsets', 'columnInQuery'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QSqlQueryModel *QSqlQueryModelPrivate::q_func() const': takes
    in Python what 'QSqlQueryModel *QSqlQueryModelPrivate::q_func()' takes.
  - Qt's 'QSqlQueryModelPrivate::~QSqlQueryModelPrivate()': the destructor:
    Python never removes a C++ QSqlQueryModelPrivate.

  What to expect
  --------------

  - The C++ QSqlQueryModelPrivate is created at the first use, not by
    'QSqlQueryModelPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSqlQueryModelPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSqlQueryModelPrivate'

  #  A C++ QSqlQueryModelPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSqlQueryModelPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def columnInQuery(self, modelColumn: int) -> int:
    """
    Calls Qt's 'int QSqlQueryModelPrivate::columnInQuery(int modelColumn)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlquerymodelprivate.html#columnInQuery

    Parameters
    ----------

    modelColumn : int
      Passed on as it is.
    """
    #  int QSqlQueryModelPrivate::columnInQuery(int modelColumn) const
    return self.uglySide.call(
        'ritual_ZNK21QSqlQueryModelPrivate13columnInQueryEi', modelColumn,
    )

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
    'QSqlQueryModelPrivate::QSqlQueryModelPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlquerymodelprivate.html#QSqlQueryModelPrivate
    """
    #  QSqlQueryModelPrivate::QSqlQueryModelPrivate()
    self._noteCreation(QSqlQueryModelPrivate, lambda: Rituals.call(
        'ritual_ZN21QSqlQueryModelPrivateC1Ev',
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

  def q_func(self) -> Optional[QSqlQueryModel]:
    """
    Calls Qt's 'QSqlQueryModel *QSqlQueryModelPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodelprivate.html#q_func

    Returns
    -------

    Optional[QSqlQueryModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSqlQueryModel *QSqlQueryModelPrivate::q_func()
    address = self.uglySide.call('ritual_ZN21QSqlQueryModelPrivate6q_funcEv')
    from . import QSqlQueryModel
    return QSqlQueryModel._cuteAt(address)

  @overload(int)
  def prefetch(self, a0: int) -> None:
    """
    Calls Qt's 'void QSqlQueryModelPrivate::prefetch(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlquerymodelprivate.html#prefetch

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QSqlQueryModelPrivate::prefetch(int a0)
    self.uglySide.call('ritual_ZN21QSqlQueryModelPrivate8prefetchEi', a0)

  @overload(int)
  def initColOffsets(self, size: int) -> None:
    """
    Calls Qt's 'void QSqlQueryModelPrivate::initColOffsets(int size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlquerymodelprivate.html#initColOffsets

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QSqlQueryModelPrivate::initColOffsets(int size)
    self.uglySide.call(
        'ritual_ZN21QSqlQueryModelPrivate14initColOffsetsEi', size,
    )
