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
  from typing import Optional

  from . import QTextCharFormat, QTextCursor, QTextTable
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTextCharFormat = WAIT['QTextCharFormat']
  QTextTable = WAIT['QTextTable']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


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
  call so far, 16 names in all: 'setFormat', 'format', 'row', 'column',
  'rowSpan', 'columnSpan', 'isValid', 'firstCursorPosition',
  'lastCursorPosition', 'firstPosition', 'lastPosition', '__eq__', '__ne__',
  'begin', 'end', 'tableCellFormatIndex'. It can be made from Python, in 3
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextTableCell::~QTextTableCell()': the destructor: Python removes
    its C++ QTextTableCell by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 21 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet.

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

  @overload(THIS)
  def __eq__(self, other: QTextTableCell) -> bool:
    """
    Calls Qt's 'bool QTextTableCell::operator==(const QTextTableCell &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttablecell.html#operator==

    Parameters
    ----------

    other : QTextTableCell
      Passed on as a value: Qt reads the C++ QTextTableCell, which stays
      Python's own.
    """
    #  bool QTextTableCell::operator==(const QTextTableCell &other) const
    return self.uglySide.call(
        'ritual_ZNK14QTextTableCelleqERKS_', self._valueOf(other),
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
  def __ne__(self, other: QTextTableCell) -> bool:
    """
    Calls Qt's 'bool QTextTableCell::operator!=(const QTextTableCell &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttablecell.html#operator!=

    Parameters
    ----------

    other : QTextTableCell
      Passed on as a value: Qt reads the C++ QTextTableCell, which stays
      Python's own.
    """
    #  bool QTextTableCell::operator!=(const QTextTableCell &other) const
    return self.uglySide.call(
        'ritual_ZNK14QTextTableCellneERKS_', self._valueOf(other),
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

  @overload(QTextTable, int)
  @overload(NoneType, int)
  def __init__(self, t: Optional[QTextTable], f: int) -> None:
    """
    Notes what was given, for Qt's 'QTextTableCell::QTextTableCell(const
    QTextTable *t, int f)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtexttablecell.html#QTextTableCell

    Parameters
    ----------

    t : Optional[QTextTable]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    f : int
      Passed on as it is.
    """
    #  QTextTableCell::QTextTableCell(const QTextTable *t, int f)
    self._noteCreation(QTextTableCell, lambda: Rituals.call(
        'ritual_ZN14QTextTableCellC1EPK10QTextTablei', self._addressOf(t), f,
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
