"""
QRangeModelDetails::DroppedEntryCell binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qrangemodel_impl.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class DroppedEntryCell(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRangeModelDetails::DroppedEntryCell: a plain Python
  object standing in front of one C++ QRangeModelDetails::DroppedEntryCell.

  C++ hands a QRangeModelDetails::DroppedEntryCell around as a copy, so every
  C++ QRangeModelDetails::DroppedEntryCell behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QRangeModelDetails::DroppedEntryCell that has a
  ritual and that Python can call so far, 2 names in all: '__eq__', '__ne__'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRangeModelDetails::DroppedEntryCell::~DroppedEntryCell()': the
    destructor: Python removes its C++ QRangeModelDetails::DroppedEntryCell
    by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QRangeModelDetails::DroppedEntryCell is created at the first use,
    not by 'QRangeModelDetails::DroppedEntryCell(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRangeModelDetails::DroppedEntryCell back gives a
    copy the ritual made for Python, in a new cute
    QRangeModelDetails::DroppedEntryCell.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRangeModelDetails::DroppedEntryCell'

  #  Qt's '~QRangeModelDetails::DroppedEntryCell()'. Naming it makes this a
  #  value class: Python owns every C++ QRangeModelDetails::DroppedEntryCell
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN18QRangeModelDetails16DroppedEntryCellD1Ev'

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

  @overload(THIS)
  def __eq__(self, rhs: DroppedEntryCell) -> bool:
    """
    Calls Qt's 'bool operator==(const DroppedEntryCell &lhs, const
    DroppedEntryCell &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodeldetails-droppedentrycell.html

    Parameters
    ----------

    rhs : DroppedEntryCell
      Passed on as a value: Qt reads the C++
      QRangeModelDetails::DroppedEntryCell, which stays Python's own.
    """
    #  bool operator==(const DroppedEntryCell &lhs, const DroppedEntryCell
    #      &rhs)
    return Rituals.call(
        'ritual_ZN18QRangeModelDetailseqERKNS_16DroppedEntryCellES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: DroppedEntryCell) -> bool:
    """
    Calls Qt's 'bool operator!=(const DroppedEntryCell &lhs, const
    DroppedEntryCell &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodeldetails-droppedentrycell.html

    Parameters
    ----------

    rhs : DroppedEntryCell
      Passed on as a value: Qt reads the C++
      QRangeModelDetails::DroppedEntryCell, which stays Python's own.
    """
    #  bool operator!=(const DroppedEntryCell &lhs, const DroppedEntryCell
    #      &rhs)
    return Rituals.call(
        'ritual_ZN18QRangeModelDetailsneERKNS_16DroppedEntryCellES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QRangeModelDetails::DroppedEntryCell::DroppedEntryCell()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodeldetails-droppedentrycell.html
    """
    #  QRangeModelDetails::DroppedEntryCell::DroppedEntryCell()
    self._noteCreation(DroppedEntryCell, lambda: Rituals.call(
        'ritual_ZN18QRangeModelDetails16DroppedEntryCellC1Ev',
    ))

  @overload(int)
  @overload(int, int)
  def __init__(self, row: int, column: int = 0) -> None:
    """
    Notes what was given, for Qt's
    'QRangeModelDetails::DroppedEntryCell::DroppedEntryCell(int row, int
    column)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodeldetails-droppedentrycell.html

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QRangeModelDetails::DroppedEntryCell::DroppedEntryCell(int row, int
    #      column)
    self._noteCreation(DroppedEntryCell, lambda: Rituals.call(
        'ritual_ZN18QRangeModelDetails16DroppedEntryCellC1Eii', row, column,
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
