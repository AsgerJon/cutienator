"""
QQmlSortFilterProxyModelGreaterThan binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qsortfilterproxymodelhelper_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlSortFilterProxyModelGreaterThan to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QAbstractItemModel, QModelIndex
  from . import QSortFilterProxyModelHelper
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QModelIndex = WAIT['QModelIndex']
  QSortFilterProxyModelHelper = WAIT['QSortFilterProxyModelHelper']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlSortFilterProxyModelGreaterThan(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlSortFilterProxyModelGreaterThan: a plain Python
  object standing in front of one C++ QQmlSortFilterProxyModelGreaterThan.

  C++ hands a QQmlSortFilterProxyModelGreaterThan around as a copy, so every
  C++ QQmlSortFilterProxyModelGreaterThan behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QQmlSortFilterProxyModelGreaterThan that has a
  ritual and that Python can call so far, 1 name in all: '__call__'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlSortFilterProxyModelGreaterThan::
    ~QQmlSortFilterProxyModelGreaterThan()': the destructor: Python removes
    its C++ QQmlSortFilterProxyModelGreaterThan by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QQmlSortFilterProxyModelGreaterThan is created at the first use,
    not by 'QQmlSortFilterProxyModelGreaterThan(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlSortFilterProxyModelGreaterThan back gives a copy
    the ritual made for Python, in a new cute
    QQmlSortFilterProxyModelGreaterThan.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSortFilterProxyModelGreaterThan'

  #  Qt's '~QQmlSortFilterProxyModelGreaterThan()'. Naming it makes this a
  #  value class: Python owns every C++ QQmlSortFilterProxyModelGreaterThan
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN35QQmlSortFilterProxyModelGreaterThanD1Ev'

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

  @overload(int, int)
  def __call__(self, r1: int, r2: int) -> bool:
    """
    Calls Qt's 'bool QQmlSortFilterProxyModelGreaterThan::operator()(int r1,
    int r2) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelgreaterthan.html

    Parameters
    ----------

    r1 : int
      Passed on as it is.

    r2 : int
      Passed on as it is.
    """
    #  bool QQmlSortFilterProxyModelGreaterThan::operator()(int r1, int r2)
    #      const
    return self.uglySide.call(
        'ritual_ZNK35QQmlSortFilterProxyModelGreaterThanclEii', r1, r2,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(
      int, QModelIndex, QAbstractItemModel, QSortFilterProxyModelHelper,
  )
  @overload(int, QModelIndex, QAbstractItemModel, NoneType)
  @overload(int, QModelIndex, NoneType, QSortFilterProxyModelHelper)
  @overload(int, QModelIndex, NoneType, NoneType)
  def __init__(
      self,
      column: int,
      parent: QModelIndex,
      source: Optional[QAbstractItemModel],
      helper: Optional[QSortFilterProxyModelHelper],
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlSortFilterProxyModelGreaterThan::
    QQmlSortFilterProxyModelGreaterThan(int column, const QModelIndex
    &parent, const QAbstractItemModel *source, const
    QSortFilterProxyModelHelper *helper)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsortfilterproxymodelgreaterthan.html

    Parameters
    ----------

    column : int
      Passed on as it is.

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    source : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    helper : Optional[QSortFilterProxyModelHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlSortFilterProxyModelGreaterThan::
    #      QQmlSortFilterProxyModelGreaterThan(int column, const QModelIndex
    #      &parent, const QAbstractItemModel *source, const
    #      QSortFilterProxyModelHelper *helper)
    self._noteCreation(
        QQmlSortFilterProxyModelGreaterThan, lambda: Rituals.call(
            'ritual_ZN35QQmlSortFilterProxyModelGreaterThanC1EiRK11QModelIn'
            'dexPK18QAbstractItemModelPK27QSortFilterProxyModelHelper',
            column, self._valueOf(parent), self._addressOf(source),
            self._addressOf(helper, 'QSortFilterProxyModelHelper'),
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
