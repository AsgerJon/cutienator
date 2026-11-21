"""
QTextTableCell binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qtexttable.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QTextFrame

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QTextCharFormat, QTextCursor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTextCharFormat = WAIT['QTextCharFormat']


class QTextTableCell(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextTableCell: a plain Python object standing in
  front of one C++ QTextTableCell.

  C++ hands a QTextTableCell around as a copy, so every C++ QTextTableCell
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextTableCell that has a ritual and that Python can
  call so far, 14 names in all: 'setFormat', 'format', 'row', 'column',
  'rowSpan', 'columnSpan', 'isValid', 'firstCursorPosition',
  'lastCursorPosition', 'firstPosition', 'lastPosition', 'begin', 'end',
  'tableCellFormatIndex'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextTableCell::~QTextTableCell()': the destructor: Python removes
    its C++ QTextTableCell by it, and has no other use for it.
  - Qt's 'bool QTextTableCell::operator==(const QTextTableCell &other)
    const': an operator, which is not reflected yet.
  - Qt's 'bool QTextTableCell::operator!=(const QTextTableCell &other)
    const': an operator, which is not reflected yet.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet; 1 private.

  What to expect
  --------------

  - The C++ QTextTableCell is created at the first use, not by
    'QTextTableCell(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextTableCell back gives a copy the ritual made for
    Python, in a new cute QTextTableCell.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextTableCell'

  #  Qt's '~QTextTableCell()'. Naming it makes this a value class: Python
  #  owns every C++ QTextTableCell behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QTextTableCellD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def format(self) -> QTextCharFormat:
    """
    Calls Qt's 'QTextCharFormat QTextTableCell::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttablecell.html#format

    Returns
    -------

    QTextCharFormat
      A new cute QTextCharFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextCharFormat QTextTableCell::format() const
    address = self.uglySide.call('ritual_ZNK14QTextTableCell6formatEv')
    from . import QTextCharFormat
    return QTextCharFormat._cuteOwning(address)

  def row(self) -> int:
    """
    Calls Qt's 'int QTextTableCell::row() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttablecell.html#row
    """
    #  int QTextTableCell::row() const
    return self.uglySide.call('ritual_ZNK14QTextTableCell3rowEv')

  def column(self) -> int:
    """
    Calls Qt's 'int QTextTableCell::column() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttablecell.html#column
    """
    #  int QTextTableCell::column() const
    return self.uglySide.call('ritual_ZNK14QTextTableCell6columnEv')

  def rowSpan(self) -> int:
    """
    Calls Qt's 'int QTextTableCell::rowSpan() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttablecell.html#rowSpan
    """
    #  int QTextTableCell::rowSpan() const
    return self.uglySide.call('ritual_ZNK14QTextTableCell7rowSpanEv')

  def columnSpan(self) -> int:
    """
    Calls Qt's 'int QTextTableCell::columnSpan() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttablecell.html#columnSpan
    """
    #  int QTextTableCell::columnSpan() const
    return self.uglySide.call('ritual_ZNK14QTextTableCell10columnSpanEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QTextTableCell::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttablecell.html#isValid
    """
    #  bool QTextTableCell::isValid() const
    return self.uglySide.call('ritual_ZNK14QTextTableCell7isValidEv')

  def firstCursorPosition(self) -> QTextCursor:
    """
    Calls Qt's 'QTextCursor QTextTableCell::firstCursorPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecell.html#firstCursorPosition

    Returns
    -------

    QTextCursor
      A new cute QTextCursor around the copy Qt gave back. Python owns it.
    """
    #  QTextCursor QTextTableCell::firstCursorPosition() const
    address = self.uglySide.call(
        'ritual_ZNK14QTextTableCell19firstCursorPositionEv',
    )
    from . import QTextCursor
    return QTextCursor._cuteOwning(address)

  def lastCursorPosition(self) -> QTextCursor:
    """
    Calls Qt's 'QTextCursor QTextTableCell::lastCursorPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecell.html#lastCursorPosition

    Returns
    -------

    QTextCursor
      A new cute QTextCursor around the copy Qt gave back. Python owns it.
    """
    #  QTextCursor QTextTableCell::lastCursorPosition() const
    address = self.uglySide.call(
        'ritual_ZNK14QTextTableCell18lastCursorPositionEv',
    )
    from . import QTextCursor
    return QTextCursor._cuteOwning(address)

  def firstPosition(self) -> int:
    """
    Calls Qt's 'int QTextTableCell::firstPosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttablecell.html#firstPosition
    """
    #  int QTextTableCell::firstPosition() const
    return self.uglySide.call('ritual_ZNK14QTextTableCell13firstPositionEv')

  def lastPosition(self) -> int:
    """
    Calls Qt's 'int QTextTableCell::lastPosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttablecell.html#lastPosition
    """
    #  int QTextTableCell::lastPosition() const
    return self.uglySide.call('ritual_ZNK14QTextTableCell12lastPositionEv')

  def begin(self) -> QTextFrame.iterator:
    """
    Calls Qt's 'QTextFrame::iterator QTextTableCell::begin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttablecell.html#begin

    Returns
    -------

    QTextFrame.iterator
      A new cute QTextFrame::iterator around the copy Qt gave back. Python
      owns it.
    """
    #  QTextFrame::iterator QTextTableCell::begin() const
    address = self.uglySide.call('ritual_ZNK14QTextTableCell5beginEv')
    return QTextFrame.iterator._cuteOwning(address)

  def end(self) -> QTextFrame.iterator:
    """
    Calls Qt's 'QTextFrame::iterator QTextTableCell::end() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttablecell.html#end

    Returns
    -------

    QTextFrame.iterator
      A new cute QTextFrame::iterator around the copy Qt gave back. Python
      owns it.
    """
    #  QTextFrame::iterator QTextTableCell::end() const
    address = self.uglySide.call('ritual_ZNK14QTextTableCell3endEv')
    return QTextFrame.iterator._cuteOwning(address)

  def tableCellFormatIndex(self) -> int:
    """
    Calls Qt's 'int QTextTableCell::tableCellFormatIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecell.html#tableCellFormatIndex
    """
    #  int QTextTableCell::tableCellFormatIndex() const
    return self.uglySide.call(
        'ritual_ZNK14QTextTableCell20tableCellFormatIndexEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QTextCharFormat)
  def setFormat(self, format: QTextCharFormat) -> None:
    """
    Calls Qt's 'void QTextTableCell::setFormat(const QTextCharFormat
    &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttablecell.html#setFormat

    Parameters
    ----------

    format : QTextCharFormat
      Passed on as a value: Qt reads the C++ QTextCharFormat, which stays
      Python's own.
    """
    #  void QTextTableCell::setFormat(const QTextCharFormat &format)
    self.uglySide.call(
        'ritual_ZN14QTextTableCell9setFormatERK15QTextCharFormat',
        self._valueOf(format),
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
    Notes what was given, for Qt's 'QTextTableCell::QTextTableCell()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtexttablecell.html#QTextTableCell
    """
    #  QTextTableCell::QTextTableCell()
    self._noteCreation(QTextTableCell, lambda: Rituals.call(
        'ritual_ZN14QTextTableCellC1Ev',
    ))

  @overload(THIS)
  def __init__(self, o: QTextTableCell) -> None:
    """
    Notes what was given, for Qt's 'QTextTableCell::QTextTableCell(const
    QTextTableCell &o)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtexttablecell.html#QTextTableCell

    Parameters
    ----------

    o : QTextTableCell
      Passed on as a value: Qt reads the C++ QTextTableCell, which stays
      Python's own.
    """
    #  QTextTableCell::QTextTableCell(const QTextTableCell &o)
    self._noteCreation(QTextTableCell, lambda: Rituals.call(
        'ritual_ZN14QTextTableCellC1ERKS_', self._valueOf(o),
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
