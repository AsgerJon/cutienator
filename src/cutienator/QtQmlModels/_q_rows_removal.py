"""
QRowsRemoval binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qsortfilterproxymodelhelper_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QRowsRemoval to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QModelIndex
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']


class QRowsRemoval(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRowsRemoval: a plain Python object standing in front
  of one C++ QRowsRemoval.

  C++ hands a QRowsRemoval around as a copy, so every C++ QRowsRemoval behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRowsRemoval that has a ritual and that Python can
  call so far, 1 name in all: 'contains'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRowsRemoval::~QRowsRemoval()': the destructor: Python removes its
    C++ QRowsRemoval by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QRowsRemoval is created at the first use, not by
    'QRowsRemoval(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRowsRemoval back gives a copy the ritual made for
    Python, in a new cute QRowsRemoval.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRowsRemoval'

  #  Qt's '~QRowsRemoval()'. Naming it makes this a value class: Python owns
  #  every C++ QRowsRemoval behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QRowsRemovalD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QModelIndex, int)
  def contains(self, parent: QModelIndex, row: int) -> bool:
    """
    Calls Qt's 'bool QRowsRemoval::contains(QModelIndex parent, int row)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qrowsremoval.html#contains

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    row : int
      Passed on as it is.
    """
    #  bool QRowsRemoval::contains(QModelIndex parent, int row) const
    return self.uglySide.call(
        'ritual_ZNK12QRowsRemoval8containsE11QModelIndexi',
        self._valueOf(parent), row,
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

  @overload(QModelIndex, int, int)
  def __init__(
      self,
      parent_source: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Notes what was given, for Qt's 'QRowsRemoval::QRowsRemoval(const
    QModelIndex &parent_source, int start, int end)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qrowsremoval.html#QRowsRemoval

    Parameters
    ----------

    parent_source : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  QRowsRemoval::QRowsRemoval(const QModelIndex &parent_source, int
    #      start, int end)
    self._noteCreation(QRowsRemoval, lambda: Rituals.call(
        'ritual_ZN12QRowsRemovalC1ERK11QModelIndexii',
        self._valueOf(parent_source), start, end,
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QRowsRemoval::QRowsRemoval()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qrowsremoval.html#QRowsRemoval
    """
    #  QRowsRemoval::QRowsRemoval()
    self._noteCreation(QRowsRemoval, lambda: Rituals.call(
        'ritual_ZN12QRowsRemovalC1Ev',
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
