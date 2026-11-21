"""
QItemSelection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qitemselectionmodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QItemSelectionModelSelectionFlag

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QItemSelectionModel, QItemSelectionRange, QModelIndex
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QItemSelectionRange = WAIT['QItemSelectionRange']
  QModelIndex = WAIT['QModelIndex']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QItemSelection(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QItemSelection: a plain Python object standing in
  front of one C++ QItemSelection.

  C++ hands a QItemSelection around as a copy, so every C++ QItemSelection
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QItemSelection that has a ritual and that Python can
  call so far, 4 names in all: 'select', 'contains', 'merge', 'split'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QItemSelection::~QItemSelection()': the destructor: Python removes
    its C++ QItemSelection by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 7 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QItemSelection is created at the first use, not by
    'QItemSelection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QItemSelection back gives a copy the ritual made for
    Python, in a new cute QItemSelection.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QItemSelectionRange, QItemSelectionRange, THIS)
  @overload(QItemSelectionRange, QItemSelectionRange, NoneType)
  def split(
      range: QItemSelectionRange,
      other: QItemSelectionRange,
      result: Optional[QItemSelection],
  ) -> None:
    """
    Calls Qt's 'void QItemSelection::split(const QItemSelectionRange &range,
    const QItemSelectionRange &other, QItemSelection *result)'.

    Qt's own words: https://doc.qt.io/qt-6/qitemselection.html#split

    Parameters
    ----------

    range : QItemSelectionRange
      Passed on as a value: Qt reads the C++ QItemSelectionRange, which stays
      Python's own.

    other : QItemSelectionRange
      Passed on as a value: Qt reads the C++ QItemSelectionRange, which stays
      Python's own.

    result : Optional[QItemSelection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QItemSelection::split(const QItemSelectionRange &range, const
    #      QItemSelectionRange &other, QItemSelection *result)
    Rituals.call(
        'ritual_ZN14QItemSelection5splitERK19QItemSelectionRangeS2_PS_',
        CuteMixin._valueOf(range), CuteMixin._valueOf(other),
        CuteMixin._addressOf(result),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QItemSelection'

  #  Qt's '~QItemSelection()'. Naming it makes this a value class: Python
  #  owns every C++ QItemSelection behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QItemSelectionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QModelIndex)
  def contains(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QItemSelection::contains(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemselection.html#contains

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QItemSelection::contains(const QModelIndex &index) const
    return self.uglySide.call(
        'ritual_ZNK14QItemSelection8containsERK11QModelIndex',
        self._valueOf(index),
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

  @overload(QModelIndex, QModelIndex)
  def __init__(self, topLeft: QModelIndex, bottomRight: QModelIndex) -> None:
    """
    Notes what was given, for Qt's 'QItemSelection::QItemSelection(const
    QModelIndex &topLeft, const QModelIndex &bottomRight)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qitemselection.html#QItemSelection

    Parameters
    ----------

    topLeft : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    bottomRight : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  QItemSelection::QItemSelection(const QModelIndex &topLeft, const
    #      QModelIndex &bottomRight)
    self._noteCreation(QItemSelection, lambda: Rituals.call(
        'ritual_ZN14QItemSelectionC1ERK11QModelIndexS2_',
        self._valueOf(topLeft), self._valueOf(bottomRight),
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

  @overload(QModelIndex, QModelIndex)
  def select(self, topLeft: QModelIndex, bottomRight: QModelIndex) -> None:
    """
    Calls Qt's 'void QItemSelection::select(const QModelIndex &topLeft, const
    QModelIndex &bottomRight)'.

    Qt's own words: https://doc.qt.io/qt-6/qitemselection.html#select

    Parameters
    ----------

    topLeft : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    bottomRight : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QItemSelection::select(const QModelIndex &topLeft, const
    #      QModelIndex &bottomRight)
    self.uglySide.call(
        'ritual_ZN14QItemSelection6selectERK11QModelIndexS2_',
        self._valueOf(topLeft), self._valueOf(bottomRight),
    )

  @overload(THIS, QItemSelectionModelSelectionFlag)
  def merge(
      self,
      other: QItemSelection,
      command: QItemSelectionModel.SelectionFlags,
  ) -> None:
    """
    Calls Qt's 'void QItemSelection::merge(const QItemSelection &other,
    QItemSelectionModel::SelectionFlags command)'.

    Qt's own words: https://doc.qt.io/qt-6/qitemselection.html#merge

    Parameters
    ----------

    other : QItemSelection
      Passed on as a value: Qt reads the C++ QItemSelection, which stays
      Python's own.

    command : QItemSelectionModel.SelectionFlags
      Passed on as its number.
    """
    #  void QItemSelection::merge(const QItemSelection &other,
    #      QItemSelectionModel::SelectionFlags command)
    self.uglySide.call(
        'ritual_ZN14QItemSelection5mergeERKS_6QFlagsIN19QItemSelectionModel'
        '13SelectionFlagEE',
        self._valueOf(other), command.value,
    )
