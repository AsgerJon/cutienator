"""
QTextTableFormat binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qtextformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import Qt
from . import QTextFrameFormat


class QTextTableFormat(QTextFrameFormat):
  """
  The cute side of Qt's QTextTableFormat: a plain Python object standing in
  front of one C++ QTextTableFormat.

  It is built on the cute 'QTextFrameFormat', as Qt's QTextTableFormat is
  built on Qt's QTextFrameFormat, and has everything that class has.

  C++ hands a QTextTableFormat around as a copy, so every C++
  QTextTableFormat behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextTableFormat that has a ritual and that Python
  can call so far, 14 names in all: 'isValid', 'columns', 'setColumns',
  'clearColumnWidthConstraints', 'cellSpacing', 'setCellSpacing',
  'cellPadding', 'setCellPadding', 'setAlignment', 'alignment',
  'setHeaderRowCount', 'headerRowCount', 'setBorderCollapse',
  'borderCollapse'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextTableFormat::~QTextTableFormat()': the destructor: Python
    removes its C++ QTextTableFormat by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 19 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 1 protected.

  What to expect
  --------------

  - The C++ QTextTableFormat is created at the first use, not by
    'QTextTableFormat(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextTableFormat back gives a copy the ritual made
    for Python, in a new cute QTextTableFormat.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextTableFormat'

  #  Qt's '~QTextTableFormat()'. Naming it makes this a value class: Python
  #  owns every C++ QTextTableFormat behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QTextTableFormatD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QTextTableFormat::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttableformat.html#isValid
    """
    #  bool QTextTableFormat::isValid() const
    return self.uglySide.call('ritual_ZNK16QTextTableFormat7isValidEv')

  def columns(self) -> int:
    """
    Calls Qt's 'int QTextTableFormat::columns() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttableformat.html#columns
    """
    #  int QTextTableFormat::columns() const
    return self.uglySide.call('ritual_ZNK16QTextTableFormat7columnsEv')

  def cellSpacing(self) -> float:
    """
    Calls Qt's 'qreal QTextTableFormat::cellSpacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttableformat.html#cellSpacing
    """
    #  qreal QTextTableFormat::cellSpacing() const
    return self.uglySide.call('ritual_ZNK16QTextTableFormat11cellSpacingEv')

  def cellPadding(self) -> float:
    """
    Calls Qt's 'qreal QTextTableFormat::cellPadding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttableformat.html#cellPadding
    """
    #  qreal QTextTableFormat::cellPadding() const
    return self.uglySide.call('ritual_ZNK16QTextTableFormat11cellPaddingEv')

  def alignment(self) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QTextTableFormat::alignment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttableformat.html#alignment

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QTextTableFormat::alignment() const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK16QTextTableFormat9alignmentEv',
    ))

  def headerRowCount(self) -> int:
    """
    Calls Qt's 'int QTextTableFormat::headerRowCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttableformat.html#headerRowCount
    """
    #  int QTextTableFormat::headerRowCount() const
    return self.uglySide.call(
        'ritual_ZNK16QTextTableFormat14headerRowCountEv',
    )

  def borderCollapse(self) -> bool:
    """
    Calls Qt's 'bool QTextTableFormat::borderCollapse() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttableformat.html#borderCollapse
    """
    #  bool QTextTableFormat::borderCollapse() const
    return self.uglySide.call(
        'ritual_ZNK16QTextTableFormat14borderCollapseEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setColumns(self, columns: int) -> None:
    """
    Calls Qt's 'void QTextTableFormat::setColumns(int columns)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttableformat.html#setColumns

    Parameters
    ----------

    columns : int
      Passed on as it is.
    """
    #  void QTextTableFormat::setColumns(int columns)
    self.uglySide.call('ritual_ZN16QTextTableFormat10setColumnsEi', columns)

  @overload(float)
  def setCellSpacing(self, spacing: float) -> None:
    """
    Calls Qt's 'void QTextTableFormat::setCellSpacing(qreal spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttableformat.html#setCellSpacing

    Parameters
    ----------

    spacing : float
      Passed on as it is.
    """
    #  void QTextTableFormat::setCellSpacing(qreal spacing)
    self.uglySide.call(
        'ritual_ZN16QTextTableFormat14setCellSpacingEd', spacing,
    )

  @overload(float)
  def setCellPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QTextTableFormat::setCellPadding(qreal padding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttableformat.html#setCellPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QTextTableFormat::setCellPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN16QTextTableFormat14setCellPaddingEd', padding,
    )

  @overload(Qt.Alignment)
  def setAlignment(self, alignment: Qt.Alignment) -> None:
    """
    Calls Qt's 'void QTextTableFormat::setAlignment(Qt::Alignment
    alignment)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttableformat.html#setAlignment

    Parameters
    ----------

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  void QTextTableFormat::setAlignment(Qt::Alignment alignment)
    self.uglySide.call(
        'ritual_ZN16QTextTableFormat12setAlignmentE6QFlagsIN2Qt13AlignmentF'
        'lagEE',
        alignment.value,
    )

  @overload(int)
  def setHeaderRowCount(self, count: int) -> None:
    """
    Calls Qt's 'void QTextTableFormat::setHeaderRowCount(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttableformat.html#setHeaderRowCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QTextTableFormat::setHeaderRowCount(int count)
    self.uglySide.call(
        'ritual_ZN16QTextTableFormat17setHeaderRowCountEi', count,
    )

  @overload(bool)
  def setBorderCollapse(self, borderCollapse: bool) -> None:
    """
    Calls Qt's 'void QTextTableFormat::setBorderCollapse(bool
    borderCollapse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttableformat.html#setBorderCollapse

    Parameters
    ----------

    borderCollapse : bool
      Passed on as it is.
    """
    #  void QTextTableFormat::setBorderCollapse(bool borderCollapse)
    self.uglySide.call(
        'ritual_ZN16QTextTableFormat17setBorderCollapseEb', borderCollapse,
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
    Notes what was given, for Qt's 'QTextTableFormat::QTextTableFormat()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttableformat.html#QTextTableFormat
    """
    #  QTextTableFormat::QTextTableFormat()
    self._noteCreation(QTextTableFormat, lambda: Rituals.call(
        'ritual_ZN16QTextTableFormatC1Ev',
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

  def clearColumnWidthConstraints(self) -> None:
    """
    Calls Qt's 'void QTextTableFormat::clearColumnWidthConstraints()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttableformat.html#clearColumnWidthConstraints
    """
    #  void QTextTableFormat::clearColumnWidthConstraints()
    self.uglySide.call(
        'ritual_ZN16QTextTableFormat27clearColumnWidthConstraintsEv',
    )
