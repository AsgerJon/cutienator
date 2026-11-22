"""
QTableWidgetSelectionRange binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qtablewidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QList


class QTableWidgetSelectionRange(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTableWidgetSelectionRange: a plain Python object
  standing in front of one C++ QTableWidgetSelectionRange.

  C++ hands a QTableWidgetSelectionRange around as a copy, so every C++
  QTableWidgetSelectionRange behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QTableWidgetSelectionRange that has a ritual and
  that Python can call so far, 8 names in all: '__eq__', '__ne__', 'topRow',
  'bottomRow', 'leftColumn', 'rightColumn', 'rowCount', 'columnCount'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTableWidgetSelectionRange::~QTableWidgetSelectionRange()': the
    destructor: Python removes its C++ QTableWidgetSelectionRange by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QTableWidgetSelectionRange is created at the first use, not by
    'QTableWidgetSelectionRange(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTableWidgetSelectionRange back gives a copy the
    ritual made for Python, in a new cute QTableWidgetSelectionRange.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTableWidgetSelectionRange'

  #  Qt's '~QTableWidgetSelectionRange()'. Naming it makes this a value
  #  class: Python owns every C++ QTableWidgetSelectionRange behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QTableWidgetSelectionRangeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def topRow(self) -> int:
    """
    Calls Qt's 'int QTableWidgetSelectionRange::topRow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidgetselectionrange.html#topRow
    """
    #  int QTableWidgetSelectionRange::topRow() const
    return self.uglySide.call(
        'ritual_ZNK26QTableWidgetSelectionRange6topRowEv',
    )

  def bottomRow(self) -> int:
    """
    Calls Qt's 'int QTableWidgetSelectionRange::bottomRow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidgetselectionrange.html#bottomRow
    """
    #  int QTableWidgetSelectionRange::bottomRow() const
    return self.uglySide.call(
        'ritual_ZNK26QTableWidgetSelectionRange9bottomRowEv',
    )

  def leftColumn(self) -> int:
    """
    Calls Qt's 'int QTableWidgetSelectionRange::leftColumn() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidgetselectionrange.html#leftColumn
    """
    #  int QTableWidgetSelectionRange::leftColumn() const
    return self.uglySide.call(
        'ritual_ZNK26QTableWidgetSelectionRange10leftColumnEv',
    )

  def rightColumn(self) -> int:
    """
    Calls Qt's 'int QTableWidgetSelectionRange::rightColumn() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidgetselectionrange.html#rightColumn
    """
    #  int QTableWidgetSelectionRange::rightColumn() const
    return self.uglySide.call(
        'ritual_ZNK26QTableWidgetSelectionRange11rightColumnEv',
    )

  def rowCount(self) -> int:
    """
    Calls Qt's 'int QTableWidgetSelectionRange::rowCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidgetselectionrange.html#rowCount
    """
    #  int QTableWidgetSelectionRange::rowCount() const
    return self.uglySide.call(
        'ritual_ZNK26QTableWidgetSelectionRange8rowCountEv',
    )

  def columnCount(self) -> int:
    """
    Calls Qt's 'int QTableWidgetSelectionRange::columnCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidgetselectionrange.html#columnCount
    """
    #  int QTableWidgetSelectionRange::columnCount() const
    return self.uglySide.call(
        'ritual_ZNK26QTableWidgetSelectionRange11columnCountEv',
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

  @overload(THIS)
  def __eq__(self, rhs: QTableWidgetSelectionRange) -> bool:
    """
    Calls Qt's 'bool operator==(const QTableWidgetSelectionRange &lhs, const
    QTableWidgetSelectionRange &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidgetselectionrange.html#operator==

    Parameters
    ----------

    rhs : QTableWidgetSelectionRange
      Passed on as a value: Qt reads the C++ QTableWidgetSelectionRange,
      which stays Python's own.
    """
    #  bool operator==(const QTableWidgetSelectionRange &lhs, const
    #      QTableWidgetSelectionRange &rhs)
    return Rituals.call(
        'ritual_ZeqRK26QTableWidgetSelectionRangeS1_',
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
  def __ne__(self, rhs: QTableWidgetSelectionRange) -> bool:
    """
    Calls Qt's 'bool operator!=(const QTableWidgetSelectionRange &lhs, const
    QTableWidgetSelectionRange &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidgetselectionrange.html#operator!=

    Parameters
    ----------

    rhs : QTableWidgetSelectionRange
      Passed on as a value: Qt reads the C++ QTableWidgetSelectionRange,
      which stays Python's own.
    """
    #  bool operator!=(const QTableWidgetSelectionRange &lhs, const
    #      QTableWidgetSelectionRange &rhs)
    return Rituals.call(
        'ritual_ZneRK26QTableWidgetSelectionRangeS1_',
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
    'QTableWidgetSelectionRange::QTableWidgetSelectionRange()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidgetselectionrange.html
    """
    #  QTableWidgetSelectionRange::QTableWidgetSelectionRange()
    self._noteCreation(QTableWidgetSelectionRange, lambda: Rituals.call(
        'ritual_ZN26QTableWidgetSelectionRangeC1Ev',
    ))

  @overload(int, int, int, int)
  def __init__(self, top: int, left: int, bottom: int, right: int) -> None:
    """
    Notes what was given, for Qt's
    'QTableWidgetSelectionRange::QTableWidgetSelectionRange(int top, int
    left, int bottom, int right)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidgetselectionrange.html

    Parameters
    ----------

    top : int
      Passed on as it is.

    left : int
      Passed on as it is.

    bottom : int
      Passed on as it is.

    right : int
      Passed on as it is.
    """
    #  QTableWidgetSelectionRange::QTableWidgetSelectionRange(int top, int
    #      left, int bottom, int right)
    self._noteCreation(QTableWidgetSelectionRange, lambda: Rituals.call(
        'ritual_ZN26QTableWidgetSelectionRangeC1Eiiii',
        top, left, bottom, right,
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


#  Qt's 'QList<QTableWidgetSelectionRange>': the list of
#  QTableWidgetSelectionRange, which 'QList[QTableWidgetSelectionRange]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QTableWidgetSelectionRange.
QList.createKind(
    QTableWidgetSelectionRange, 'value',
    make='ritual_list_make_QTableWidgetSelectionRange',
    add='ritual_list_add_QTableWidgetSelectionRange',
    size='ritual_list_size_QTableWidgetSelectionRange',
    at='ritual_list_at_QTableWidgetSelectionRange',
    drop='ritual_list_drop_QTableWidgetSelectionRange',
)
