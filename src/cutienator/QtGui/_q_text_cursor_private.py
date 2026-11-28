"""
QTextCursorPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtextcursor_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QTextCursorPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QSharedData
from . import QTextCursor, QTextDocumentPrivate, QTextUndoCommand

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QTextBlock, QTextBlockFormat, QTextCharFormat, QTextTable
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTextBlockFormat = WAIT['QTextBlockFormat']
  QTextCharFormat = WAIT['QTextCharFormat']
  QTextTable = WAIT['QTextTable']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextCursorPrivate(QSharedData):
  """
  The cute side of Qt's QTextCursorPrivate: a plain Python object standing in
  front of one C++ QTextCursorPrivate.

  It is built on the cute 'QSharedData', as Qt's QTextCursorPrivate is built
  on Qt's QSharedData, and has everything that class has.

  C++ hands a QTextCursorPrivate around as a copy, so every C++
  QTextCursorPrivate behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextCursorPrivate that has a ritual and that Python
  can call so far, 18 names in all: 'getPrivate', 'adjustPosition',
  'adjustCursor', 'remove', 'clearCells', 'setPosition', 'setX', 'canDelete',
  'insertBlock', 'movePosition', 'block', 'blockFormat',
  'complexSelectionTable', 'setBlockCharFormat', 'setBlockFormat',
  'setCharFormat', 'aboutToRemoveCell', 'fromPosition'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextCursorPrivate::~QTextCursorPrivate()': the destructor: Python
    removes its C++ QTextCursorPrivate by it, and has no other use for it.
  - Qt's 'QTextLayout *QTextCursorPrivate::blockLayout(QTextBlock &block)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'void QTextCursorPrivate::selectedTableCells(int *firstRow, int
    *numRows, int *firstColumn, int *numColumns) const': takes a number to
    change where it is.

  What to expect
  --------------

  - The C++ QTextCursorPrivate is created at the first use, not by
    'QTextCursorPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextCursorPrivate back gives a copy the ritual made
    for Python, in a new cute QTextCursorPrivate.
  - Each name of Qt's QTextCursorPrivate that has no cute function yet,
    'blockLayout', 'selectedTableCells', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QTextCursorPrivate, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class AdjustResult(CuteNum):
    """
    The enum 'QTextCursorPrivate::AdjustResult' of Qt, with the 2 names Qt
    gives in it.
    """

    CursorMoved = Kee[int](0)
    CursorUnchanged = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QTextCursor)
  @overload(NoneType)
  def getPrivate(c: Optional[QTextCursor]) -> Optional[QTextCursorPrivate]:
    """
    Calls Qt's 'QTextCursorPrivate
    *QTextCursorPrivate::getPrivate(QTextCursor *c)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursorprivate.html#getPrivate

    Parameters
    ----------

    c : Optional[QTextCursor]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QTextCursorPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextCursorPrivate *QTextCursorPrivate::getPrivate(QTextCursor *c)
    address = Rituals.call(
        'ritual_ZN18QTextCursorPrivate10getPrivateEP11QTextCursor',
        CuteMixin._addressOf(c),
    )
    return QTextCursorPrivate._cuteAt(address)

  @staticmethod
  @overload(QTextDocumentPrivate, int)
  @overload(NoneType, int)
  def fromPosition(
      d: Optional[QTextDocumentPrivate],
      pos: int,
  ) -> QTextCursor:
    """
    Calls Qt's 'QTextCursor
    QTextCursorPrivate::fromPosition(QTextDocumentPrivate *d, int pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcursorprivate.html#fromPosition

    Parameters
    ----------

    d : Optional[QTextDocumentPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pos : int
      Passed on as it is.

    Returns
    -------

    QTextCursor
      A new cute QTextCursor around the copy Qt gave back. Python owns it.
    """
    #  QTextCursor QTextCursorPrivate::fromPosition(QTextDocumentPrivate *d,
    #      int pos)
    address = Rituals.call(
        'ritual_ZN18QTextCursorPrivate12fromPositionEP20QTextDocumentPrivat'
        'ei',
        CuteMixin._addressOf(d), pos,
    )
    return QTextCursor._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextCursorPrivate'

  #  Qt's '~QTextCursorPrivate()'. Naming it makes this a value class: Python
  #  owns every C++ QTextCursorPrivate behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QTextCursorPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def canDelete(self, pos: int) -> bool:
    """
    Calls Qt's 'bool QTextCursorPrivate::canDelete(int pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursorprivate.html#canDelete

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  bool QTextCursorPrivate::canDelete(int pos) const
    return self.uglySide.call(
        'ritual_ZNK18QTextCursorPrivate9canDeleteEi', pos,
    )

  def block(self) -> QTextBlock:
    """
    Calls Qt's 'QTextBlock QTextCursorPrivate::block() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursorprivate.html#block

    Returns
    -------

    QTextBlock
      A new cute QTextBlock around the copy Qt gave back. Python owns it.
    """
    #  QTextBlock QTextCursorPrivate::block() const
    address = self.uglySide.call('ritual_ZNK18QTextCursorPrivate5blockEv')
    from . import QTextBlock
    return QTextBlock._cuteOwning(address)

  def blockFormat(self) -> QTextBlockFormat:
    """
    Calls Qt's 'QTextBlockFormat QTextCursorPrivate::blockFormat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcursorprivate.html#blockFormat

    Returns
    -------

    QTextBlockFormat
      A new cute QTextBlockFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextBlockFormat QTextCursorPrivate::blockFormat() const
    address = self.uglySide.call(
        'ritual_ZNK18QTextCursorPrivate11blockFormatEv',
    )
    from . import QTextBlockFormat
    return QTextBlockFormat._cuteOwning(address)

  def complexSelectionTable(self) -> Optional[QTextTable]:
    """
    Calls Qt's 'QTextTable *QTextCursorPrivate::complexSelectionTable()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcursorprivate.html#complexSelectionTable

    Returns
    -------

    Optional[QTextTable]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextTable *QTextCursorPrivate::complexSelectionTable() const
    address = self.uglySide.call(
        'ritual_ZNK18QTextCursorPrivate21complexSelectionTableEv',
    )
    from . import QTextTable
    return QTextTable._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setPosition(self, newPosition: int) -> bool:
    """
    Calls Qt's 'bool QTextCursorPrivate::setPosition(int newPosition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcursorprivate.html#setPosition

    Parameters
    ----------

    newPosition : int
      Passed on as it is.
    """
    #  bool QTextCursorPrivate::setPosition(int newPosition)
    return self.uglySide.call(
        'ritual_ZN18QTextCursorPrivate11setPositionEi', newPosition,
    )

  def setX(self) -> None:
    """
    Calls Qt's 'void QTextCursorPrivate::setX()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursorprivate.html#setX
    """
    #  void QTextCursorPrivate::setX()
    self.uglySide.call('ritual_ZN18QTextCursorPrivate4setXEv')

  @overload(QTextCharFormat, QTextDocumentPrivate.FormatChangeMode)
  def setBlockCharFormat(
      self,
      format: QTextCharFormat,
      changeMode: QTextDocumentPrivate.FormatChangeMode,
  ) -> None:
    """
    Calls Qt's 'void QTextCursorPrivate::setBlockCharFormat(const
    QTextCharFormat &format, QTextDocumentPrivate::FormatChangeMode
    changeMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcursorprivate.html#setBlockCharFormat

    Parameters
    ----------

    format : QTextCharFormat
      Passed on as a value: Qt reads the C++ QTextCharFormat, which stays
      Python's own.

    changeMode : QTextDocumentPrivate.FormatChangeMode
      Passed on as its number.
    """
    #  void QTextCursorPrivate::setBlockCharFormat(const QTextCharFormat
    #      &format, QTextDocumentPrivate::FormatChangeMode changeMode)
    self.uglySide.call(
        'ritual_ZN18QTextCursorPrivate18setBlockCharFormatERK15QTextCharFor'
        'matN20QTextDocumentPrivate16FormatChangeModeE',
        self._valueOf(format), changeMode.value,
    )

  @overload(QTextBlockFormat, QTextDocumentPrivate.FormatChangeMode)
  def setBlockFormat(
      self,
      format: QTextBlockFormat,
      changeMode: QTextDocumentPrivate.FormatChangeMode,
  ) -> None:
    """
    Calls Qt's 'void QTextCursorPrivate::setBlockFormat(const
    QTextBlockFormat &format, QTextDocumentPrivate::FormatChangeMode
    changeMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcursorprivate.html#setBlockFormat

    Parameters
    ----------

    format : QTextBlockFormat
      Passed on as a value: Qt reads the C++ QTextBlockFormat, which stays
      Python's own.

    changeMode : QTextDocumentPrivate.FormatChangeMode
      Passed on as its number.
    """
    #  void QTextCursorPrivate::setBlockFormat(const QTextBlockFormat
    #      &format, QTextDocumentPrivate::FormatChangeMode changeMode)
    self.uglySide.call(
        'ritual_ZN18QTextCursorPrivate14setBlockFormatERK16QTextBlockFormat'
        'N20QTextDocumentPrivate16FormatChangeModeE',
        self._valueOf(format), changeMode.value,
    )

  @overload(QTextCharFormat, QTextDocumentPrivate.FormatChangeMode)
  def setCharFormat(
      self,
      format: QTextCharFormat,
      changeMode: QTextDocumentPrivate.FormatChangeMode,
  ) -> None:
    """
    Calls Qt's 'void QTextCursorPrivate::setCharFormat(const QTextCharFormat
    &format, QTextDocumentPrivate::FormatChangeMode changeMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcursorprivate.html#setCharFormat

    Parameters
    ----------

    format : QTextCharFormat
      Passed on as a value: Qt reads the C++ QTextCharFormat, which stays
      Python's own.

    changeMode : QTextDocumentPrivate.FormatChangeMode
      Passed on as its number.
    """
    #  void QTextCursorPrivate::setCharFormat(const QTextCharFormat &format,
    #      QTextDocumentPrivate::FormatChangeMode changeMode)
    self.uglySide.call(
        'ritual_ZN18QTextCursorPrivate13setCharFormatERK15QTextCharFormatN2'
        '0QTextDocumentPrivate16FormatChangeModeE',
        self._valueOf(format), changeMode.value,
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

  @overload(QTextDocumentPrivate)
  @overload(NoneType)
  def __init__(self, p: Optional[QTextDocumentPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QTextCursorPrivate::QTextCursorPrivate(QTextDocumentPrivate *p)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcursorprivate.html#QTextCursorPrivate

    Parameters
    ----------

    p : Optional[QTextDocumentPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QTextCursorPrivate::QTextCursorPrivate(QTextDocumentPrivate *p)
    self._noteCreation(QTextCursorPrivate, lambda: Rituals.call(
        'ritual_ZN18QTextCursorPrivateC1EP20QTextDocumentPrivate',
        self._addressOf(p),
    ))

  @overload(THIS)
  def __init__(self, rhs: QTextCursorPrivate) -> None:
    """
    Notes what was given, for Qt's
    'QTextCursorPrivate::QTextCursorPrivate(const QTextCursorPrivate &rhs)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcursorprivate.html#QTextCursorPrivate

    Parameters
    ----------

    rhs : QTextCursorPrivate
      Passed on as a value: Qt reads the C++ QTextCursorPrivate, which stays
      Python's own.
    """
    #  QTextCursorPrivate::QTextCursorPrivate(const QTextCursorPrivate &rhs)
    self._noteCreation(QTextCursorPrivate, lambda: Rituals.call(
        'ritual_ZN18QTextCursorPrivateC1ERKS_', self._valueOf(rhs),
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

  @overload(int, int, QTextUndoCommand.Operation)
  def adjustPosition(
      self,
      positionOfChange: int,
      charsAddedOrRemoved: int,
      op: QTextUndoCommand.Operation,
  ) -> AdjustResult:
    """
    Calls Qt's 'AdjustResult QTextCursorPrivate::adjustPosition(int
    positionOfChange, int charsAddedOrRemoved, QTextUndoCommand::Operation
    op)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcursorprivate.html#adjustPosition

    Parameters
    ----------

    positionOfChange : int
      Passed on as it is.

    charsAddedOrRemoved : int
      Passed on as it is.

    op : QTextUndoCommand.Operation
      Passed on as its number.

    Returns
    -------

    AdjustResult
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'AdjustResult(number)'
      gives.
    """
    #  AdjustResult QTextCursorPrivate::adjustPosition(int positionOfChange,
    #      int charsAddedOrRemoved, QTextUndoCommand::Operation op)
    return QTextCursorPrivate.AdjustResult(self.uglySide.call(
        'ritual_ZN18QTextCursorPrivate14adjustPositionEiiN16QTextUndoComman'
        'd9OperationE',
        positionOfChange, charsAddedOrRemoved, op.value,
    ))

  @overload(QTextCursor.MoveOperation)
  def adjustCursor(self, m: QTextCursor.MoveOperation) -> None:
    """
    Calls Qt's 'void
    QTextCursorPrivate::adjustCursor(QTextCursor::MoveOperation m)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcursorprivate.html#adjustCursor

    Parameters
    ----------

    m : QTextCursor.MoveOperation
      Passed on as its number.
    """
    #  void QTextCursorPrivate::adjustCursor(QTextCursor::MoveOperation m)
    self.uglySide.call(
        'ritual_ZN18QTextCursorPrivate12adjustCursorEN11QTextCursor13MoveOp'
        'erationE',
        m.value,
    )

  def remove(self) -> None:
    """
    Calls Qt's 'void QTextCursorPrivate::remove()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursorprivate.html#remove
    """
    #  void QTextCursorPrivate::remove()
    self.uglySide.call('ritual_ZN18QTextCursorPrivate6removeEv')

  @overload(QTextTable, int, int, int, int, QTextUndoCommand.Operation)
  @overload(NoneType, int, int, int, int, QTextUndoCommand.Operation)
  def clearCells(
      self,
      table: Optional[QTextTable],
      startRow: int,
      startCol: int,
      numRows: int,
      numCols: int,
      op: QTextUndoCommand.Operation,
  ) -> None:
    """
    Calls Qt's 'void QTextCursorPrivate::clearCells(QTextTable *table, int
    startRow, int startCol, int numRows, int numCols,
    QTextUndoCommand::Operation op)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursorprivate.html#clearCells

    Parameters
    ----------

    table : Optional[QTextTable]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    startRow : int
      Passed on as it is.

    startCol : int
      Passed on as it is.

    numRows : int
      Passed on as it is.

    numCols : int
      Passed on as it is.

    op : QTextUndoCommand.Operation
      Passed on as its number.
    """
    #  void QTextCursorPrivate::clearCells(QTextTable *table, int startRow,
    #      int startCol, int numRows, int numCols,
    #      QTextUndoCommand::Operation op)
    self.uglySide.call(
        'ritual_ZN18QTextCursorPrivate10clearCellsEP10QTextTableiiiiN16QTex'
        'tUndoCommand9OperationE',
        self._addressOf(table), startRow, startCol, numRows, numCols,
        op.value,
    )

  @overload(QTextBlockFormat, QTextCharFormat)
  def insertBlock(
      self,
      format: QTextBlockFormat,
      charFormat: QTextCharFormat,
  ) -> None:
    """
    Calls Qt's 'void QTextCursorPrivate::insertBlock(const QTextBlockFormat
    &format, const QTextCharFormat &charFormat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcursorprivate.html#insertBlock

    Parameters
    ----------

    format : QTextBlockFormat
      Passed on as a value: Qt reads the C++ QTextBlockFormat, which stays
      Python's own.

    charFormat : QTextCharFormat
      Passed on as a value: Qt reads the C++ QTextCharFormat, which stays
      Python's own.
    """
    #  void QTextCursorPrivate::insertBlock(const QTextBlockFormat &format,
    #      const QTextCharFormat &charFormat)
    self.uglySide.call(
        'ritual_ZN18QTextCursorPrivate11insertBlockERK16QTextBlockFormatRK1'
        '5QTextCharFormat',
        self._valueOf(format), self._valueOf(charFormat),
    )

  @overload(QTextCursor.MoveOperation)
  @overload(QTextCursor.MoveOperation, QTextCursor.MoveMode)
  def movePosition(
      self,
      op: QTextCursor.MoveOperation,
      mode: QTextCursor.MoveMode = QTextCursor.MoveMode.MoveAnchor,
  ) -> bool:
    """
    Calls Qt's 'bool
    QTextCursorPrivate::movePosition(QTextCursor::MoveOperation op,
    QTextCursor::MoveMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcursorprivate.html#movePosition

    Parameters
    ----------

    op : QTextCursor.MoveOperation
      Passed on as its number.

    mode : QTextCursor.MoveMode
      Passed on as its number. May be left out, as in Qt: it is then
      QTextCursor.MoveMode.MoveAnchor.
    """
    #  bool QTextCursorPrivate::movePosition(QTextCursor::MoveOperation op,
    #      QTextCursor::MoveMode mode)
    return self.uglySide.call(
        'ritual_ZN18QTextCursorPrivate12movePositionEN11QTextCursor13MoveOp'
        'erationENS0_8MoveModeE',
        op.value, mode.value,
    )

  @overload(int, int)
  def aboutToRemoveCell(self, from_: int, to: int) -> None:
    """
    Calls Qt's 'void QTextCursorPrivate::aboutToRemoveCell(int from, int
    to)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcursorprivate.html#aboutToRemoveCell

    Parameters
    ----------

    from_ : int
      Passed on as it is.

    to : int
      Passed on as it is.
    """
    #  void QTextCursorPrivate::aboutToRemoveCell(int from, int to)
    self.uglySide.call(
        'ritual_ZN18QTextCursorPrivate17aboutToRemoveCellEii', from_, to,
    )

  @staticmethod
  def blockLayout(*__, **_) -> Never:
    """
    Qt's 'QTextLayout *QTextCursorPrivate::blockLayout(QTextBlock &block)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QTextCursorPrivate.blockLayout' has no cute function yet. Qt's "
        "'QTextLayout *QTextCursorPrivate::blockLayout(QTextBlock &block) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def selectedTableCells(*__, **_) -> Never:
    """
    Qt's 'void QTextCursorPrivate::selectedTableCells(int *firstRow, int
    *numRows, int *firstColumn, int *numColumns) const': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QTextCursorPrivate.selectedTableCells' has no cute function yet. "
        "Qt's 'void QTextCursorPrivate::selectedTableCells(int *firstRow, "
        "int *numRows, int *firstColumn, int *numColumns) const': takes a "
        "number to change where it is.")
