"""
QTextTable binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qtexttable.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QTextFrame

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QTextCursor, QTextDocument, QTextTableCell, QTextTableFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTextCursor = WAIT['QTextCursor']
  QTextDocument = WAIT['QTextDocument']
  QTextTableFormat = WAIT['QTextTableFormat']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextTable(QTextFrame):
  """
  The cute side of Qt's QTextTable: a plain Python object standing in front
  of one C++ QTextTable.

  It is built on the cute 'QTextFrame', as Qt's QTextTable is built on Qt's
  QTextFrame, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTextTable that has a ritual and that Python can
  call so far, 18 names in all: 'metaObject', 'tr', 'resize', 'insertRows',
  'insertColumns', 'appendRows', 'appendColumns', 'removeRows',
  'removeColumns', 'mergeCells', 'splitCell', 'rows', 'columns', 'cellAt',
  'rowStart', 'rowEnd', 'setFormat', 'format'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextTable::~QTextTable()': the destructor: Python never removes a
    C++ QTextTable.

  What has no ritual
  ------------------

  8 of the 31 functions Qt declares: 3 private; 2 takes or gives a type that
  cannot be passed yet; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QTextTable is created at the first use, not by 'QTextTable(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTextTable.
  - Qt tells when it has removed the C++ QTextTable. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QTextTable::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttable.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextTable::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QTextTable2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextTable'

  #  A C++ QTextTable Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTextTable'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTextTable::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttable.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTextTable::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QTextTable10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def rows(self) -> int:
    """
    Calls Qt's 'int QTextTable::rows() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttable.html#rows
    """
    #  int QTextTable::rows() const
    return self.uglySide.call('ritual_ZNK10QTextTable4rowsEv')

  def columns(self) -> int:
    """
    Calls Qt's 'int QTextTable::columns() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttable.html#columns
    """
    #  int QTextTable::columns() const
    return self.uglySide.call('ritual_ZNK10QTextTable7columnsEv')

  @overload(int, int)
  def cellAt(self, row: int, col: int) -> QTextTableCell:
    """
    Calls Qt's 'QTextTableCell QTextTable::cellAt(int row, int col) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttable.html#cellAt

    Parameters
    ----------

    row : int
      Passed on as it is.

    col : int
      Passed on as it is.

    Returns
    -------

    QTextTableCell
      A new cute QTextTableCell around the copy Qt gave back. Python owns it.
    """
    #  QTextTableCell QTextTable::cellAt(int row, int col) const
    address = self.uglySide.call(
        'ritual_ZNK10QTextTable6cellAtEii', row, col,
    )
    from . import QTextTableCell
    return QTextTableCell._cuteOwning(address)

  @overload(int)
  def cellAt(self, position: int) -> QTextTableCell:
    """
    Calls Qt's 'QTextTableCell QTextTable::cellAt(int position) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttable.html#cellAt

    Parameters
    ----------

    position : int
      Passed on as it is.

    Returns
    -------

    QTextTableCell
      A new cute QTextTableCell around the copy Qt gave back. Python owns it.
    """
    #  QTextTableCell QTextTable::cellAt(int position) const
    address = self.uglySide.call('ritual_ZNK10QTextTable6cellAtEi', position)
    from . import QTextTableCell
    return QTextTableCell._cuteOwning(address)

  @overload(QTextCursor)
  def cellAt(self, c: QTextCursor) -> QTextTableCell:
    """
    Calls Qt's 'QTextTableCell QTextTable::cellAt(const QTextCursor &c)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttable.html#cellAt

    Parameters
    ----------

    c : QTextCursor
      Passed on as a value: Qt reads the C++ QTextCursor, which stays
      Python's own.

    Returns
    -------

    QTextTableCell
      A new cute QTextTableCell around the copy Qt gave back. Python owns it.
    """
    #  QTextTableCell QTextTable::cellAt(const QTextCursor &c) const
    address = self.uglySide.call(
        'ritual_ZNK10QTextTable6cellAtERK11QTextCursor', self._valueOf(c),
    )
    from . import QTextTableCell
    return QTextTableCell._cuteOwning(address)

  @overload(QTextCursor)
  def rowStart(self, c: QTextCursor) -> QTextCursor:
    """
    Calls Qt's 'QTextCursor QTextTable::rowStart(const QTextCursor &c)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttable.html#rowStart

    Parameters
    ----------

    c : QTextCursor
      Passed on as a value: Qt reads the C++ QTextCursor, which stays
      Python's own.

    Returns
    -------

    QTextCursor
      A new cute QTextCursor around the copy Qt gave back. Python owns it.
    """
    #  QTextCursor QTextTable::rowStart(const QTextCursor &c) const
    address = self.uglySide.call(
        'ritual_ZNK10QTextTable8rowStartERK11QTextCursor', self._valueOf(c),
    )
    from . import QTextCursor
    return QTextCursor._cuteOwning(address)

  @overload(QTextCursor)
  def rowEnd(self, c: QTextCursor) -> QTextCursor:
    """
    Calls Qt's 'QTextCursor QTextTable::rowEnd(const QTextCursor &c) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttable.html#rowEnd

    Parameters
    ----------

    c : QTextCursor
      Passed on as a value: Qt reads the C++ QTextCursor, which stays
      Python's own.

    Returns
    -------

    QTextCursor
      A new cute QTextCursor around the copy Qt gave back. Python owns it.
    """
    #  QTextCursor QTextTable::rowEnd(const QTextCursor &c) const
    address = self.uglySide.call(
        'ritual_ZNK10QTextTable6rowEndERK11QTextCursor', self._valueOf(c),
    )
    from . import QTextCursor
    return QTextCursor._cuteOwning(address)

  def format(self) -> QTextTableFormat:
    """
    Calls Qt's 'QTextTableFormat QTextTable::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttable.html#format

    Returns
    -------

    QTextTableFormat
      A new cute QTextTableFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextTableFormat QTextTable::format() const
    address = self.uglySide.call('ritual_ZNK10QTextTable6formatEv')
    from . import QTextTableFormat
    return QTextTableFormat._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QTextTableFormat)
  def setFormat(self, format: QTextTableFormat) -> None:
    """
    Calls Qt's 'void QTextTable::setFormat(const QTextTableFormat &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttable.html#setFormat

    Parameters
    ----------

    format : QTextTableFormat
      Passed on as a value: Qt reads the C++ QTextTableFormat, which stays
      Python's own.
    """
    #  void QTextTable::setFormat(const QTextTableFormat &format)
    self.uglySide.call(
        'ritual_ZN10QTextTable9setFormatERK16QTextTableFormat',
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

  @overload(QTextDocument)
  @overload(NoneType)
  def __init__(self, doc: Optional[QTextDocument]) -> None:
    """
    Notes what was given, for Qt's 'QTextTable::QTextTable(QTextDocument
    *doc)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtexttable.html#QTextTable

    Parameters
    ----------

    doc : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QTextTable::QTextTable(QTextDocument *doc)
    self._noteCreation(QTextTable, lambda: Rituals.call(
        'ritual_ZN10QTextTableC1EP13QTextDocument', self._addressOf(doc),
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

  @overload(int, int)
  def resize(self, rows: int, cols: int) -> None:
    """
    Calls Qt's 'void QTextTable::resize(int rows, int cols)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttable.html#resize

    Parameters
    ----------

    rows : int
      Passed on as it is.

    cols : int
      Passed on as it is.
    """
    #  void QTextTable::resize(int rows, int cols)
    self.uglySide.call('ritual_ZN10QTextTable6resizeEii', rows, cols)

  @overload(int, int)
  def insertRows(self, pos: int, num: int) -> None:
    """
    Calls Qt's 'void QTextTable::insertRows(int pos, int num)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttable.html#insertRows

    Parameters
    ----------

    pos : int
      Passed on as it is.

    num : int
      Passed on as it is.
    """
    #  void QTextTable::insertRows(int pos, int num)
    self.uglySide.call('ritual_ZN10QTextTable10insertRowsEii', pos, num)

  @overload(int, int)
  def insertColumns(self, pos: int, num: int) -> None:
    """
    Calls Qt's 'void QTextTable::insertColumns(int pos, int num)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttable.html#insertColumns

    Parameters
    ----------

    pos : int
      Passed on as it is.

    num : int
      Passed on as it is.
    """
    #  void QTextTable::insertColumns(int pos, int num)
    self.uglySide.call('ritual_ZN10QTextTable13insertColumnsEii', pos, num)

  @overload(int)
  def appendRows(self, count: int) -> None:
    """
    Calls Qt's 'void QTextTable::appendRows(int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttable.html#appendRows

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QTextTable::appendRows(int count)
    self.uglySide.call('ritual_ZN10QTextTable10appendRowsEi', count)

  @overload(int)
  def appendColumns(self, count: int) -> None:
    """
    Calls Qt's 'void QTextTable::appendColumns(int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttable.html#appendColumns

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QTextTable::appendColumns(int count)
    self.uglySide.call('ritual_ZN10QTextTable13appendColumnsEi', count)

  @overload(int, int)
  def removeRows(self, pos: int, num: int) -> None:
    """
    Calls Qt's 'void QTextTable::removeRows(int pos, int num)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttable.html#removeRows

    Parameters
    ----------

    pos : int
      Passed on as it is.

    num : int
      Passed on as it is.
    """
    #  void QTextTable::removeRows(int pos, int num)
    self.uglySide.call('ritual_ZN10QTextTable10removeRowsEii', pos, num)

  @overload(int, int)
  def removeColumns(self, pos: int, num: int) -> None:
    """
    Calls Qt's 'void QTextTable::removeColumns(int pos, int num)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttable.html#removeColumns

    Parameters
    ----------

    pos : int
      Passed on as it is.

    num : int
      Passed on as it is.
    """
    #  void QTextTable::removeColumns(int pos, int num)
    self.uglySide.call('ritual_ZN10QTextTable13removeColumnsEii', pos, num)

  @overload(int, int, int, int)
  def mergeCells(
      self,
      row: int,
      col: int,
      numRows: int,
      numCols: int,
  ) -> None:
    """
    Calls Qt's 'void QTextTable::mergeCells(int row, int col, int numRows,
    int numCols)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttable.html#mergeCells

    Parameters
    ----------

    row : int
      Passed on as it is.

    col : int
      Passed on as it is.

    numRows : int
      Passed on as it is.

    numCols : int
      Passed on as it is.
    """
    #  void QTextTable::mergeCells(int row, int col, int numRows, int
    #      numCols)
    self.uglySide.call(
        'ritual_ZN10QTextTable10mergeCellsEiiii', row, col, numRows, numCols,
    )

  @overload(QTextCursor)
  def mergeCells(self, cursor: QTextCursor) -> None:
    """
    Calls Qt's 'void QTextTable::mergeCells(const QTextCursor &cursor)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttable.html#mergeCells

    Parameters
    ----------

    cursor : QTextCursor
      Passed on as a value: Qt reads the C++ QTextCursor, which stays
      Python's own.
    """
    #  void QTextTable::mergeCells(const QTextCursor &cursor)
    self.uglySide.call(
        'ritual_ZN10QTextTable10mergeCellsERK11QTextCursor',
        self._valueOf(cursor),
    )

  @overload(int, int, int, int)
  def splitCell(
      self,
      row: int,
      col: int,
      numRows: int,
      numCols: int,
  ) -> None:
    """
    Calls Qt's 'void QTextTable::splitCell(int row, int col, int numRows, int
    numCols)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttable.html#splitCell

    Parameters
    ----------

    row : int
      Passed on as it is.

    col : int
      Passed on as it is.

    numRows : int
      Passed on as it is.

    numCols : int
      Passed on as it is.
    """
    #  void QTextTable::splitCell(int row, int col, int numRows, int numCols)
    self.uglySide.call(
        'ritual_ZN10QTextTable9splitCellEiiii', row, col, numRows, numCols,
    )
