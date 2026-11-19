"""
QTextCursor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qtextcursor.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ._q_image import QImage
from ._q_text_block_format import QTextBlockFormat
from ._q_text_char_format import QTextCharFormat
from ._q_text_document import QTextDocument
from ._q_text_cursor_move_mode import MoveMode
from ._q_text_cursor_move_operation import MoveOperation
from ._q_text_cursor_selection_type import SelectionType

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextCursor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextCursor: a plain Python object standing in front
  of one C++ QTextCursor.

  C++ hands a QTextCursor around as a copy, so every C++ QTextCursor behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextCursor that has a ritual and that Python can
  call so far, 47 names in all: 'isNull', 'setPosition', 'position',
  'positionInBlock', 'anchor', 'insertText', 'movePosition',
  'visualNavigation', 'setVisualNavigation', 'setVerticalMovementX',
  'verticalMovementX', 'setKeepPositionOnInsert', 'keepPositionOnInsert',
  'deleteChar', 'deletePreviousChar', 'select', 'hasSelection',
  'hasComplexSelection', 'removeSelectedText', 'clearSelection',
  'selectionStart', 'selectionEnd', 'selectedText', 'charFormat',
  'setCharFormat', 'mergeCharFormat', 'blockFormat', 'setBlockFormat',
  'mergeBlockFormat', 'blockCharFormat', 'setBlockCharFormat',
  'mergeBlockCharFormat', 'atBlockStart', 'atBlockEnd', 'atStart', 'atEnd',
  'insertBlock', 'insertHtml', 'insertMarkdown', 'insertImage',
  'beginEditBlock', 'joinPreviousEditBlock', 'endEditBlock', 'isCopyOf',
  'blockNumber', 'columnNumber', 'document'. It can be made from Python, in 3
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextCursor::QTextCursor(QTextFrame *frame)': names 'QTextFrame',
    which has no cute class yet.
  - Qt's 'QTextCursor::QTextCursor(const QTextBlock &block)': names
    'QTextBlock', which has no cute class yet.
  - Qt's 'QTextCursor::~QTextCursor()': the destructor: Python removes its
    C++ QTextCursor by it, and has no other use for it.
  - Qt's 'QTextDocumentFragment QTextCursor::selection() const': gives
    'QTextDocumentFragment', which has no cute class yet.
  - Qt's 'void QTextCursor::selectedTableCells(int *firstRow, int *numRows,
    int *firstColumn, int *numColumns) const': takes a number to change where
    it is.
  - Qt's 'QTextBlock QTextCursor::block() const': gives 'QTextBlock', which
    has no cute class yet.
  - Qt's 'QTextList *QTextCursor::insertList(const QTextListFormat &format)':
    names 'QTextListFormat', which has no cute class yet.
  - Qt's 'QTextList *QTextCursor::insertList(QTextListFormat::Style style)':
    names the enum 'QTextListFormat::Style', whose class cannot be named
    here.
  - Qt's 'QTextList *QTextCursor::createList(const QTextListFormat &format)':
    names 'QTextListFormat', which has no cute class yet.
  - Qt's 'QTextList *QTextCursor::createList(QTextListFormat::Style style)':
    names the enum 'QTextListFormat::Style', whose class cannot be named
    here.
  - Qt's 'QTextList *QTextCursor::currentList() const': gives 'QTextList',
    which has no cute class yet.
  - Qt's 'QTextTable *QTextCursor::insertTable(int rows, int cols, const
    QTextTableFormat &format)': names 'QTextTableFormat', which has no cute
    class yet.
  - Qt's 'QTextTable *QTextCursor::insertTable(int rows, int cols)': gives
    'QTextTable', which has no cute class yet.
  - Qt's 'QTextTable *QTextCursor::currentTable() const': gives 'QTextTable',
    which has no cute class yet.
  - Qt's 'QTextFrame *QTextCursor::insertFrame(const QTextFrameFormat
    &format)': names 'QTextFrameFormat', which has no cute class yet.
  - Qt's 'QTextFrame *QTextCursor::currentFrame() const': gives 'QTextFrame',
    which has no cute class yet.
  - Qt's 'void QTextCursor::insertFragment(const QTextDocumentFragment
    &fragment)': names 'QTextDocumentFragment', which has no cute class yet.
  - Qt's 'void QTextCursor::insertImage(const QTextImageFormat &format,
    QTextFrameFormat::Position alignment)': names 'QTextImageFormat', which
    has no cute class yet.
  - Qt's 'void QTextCursor::insertImage(const QTextImageFormat &format)':
    names 'QTextImageFormat', which has no cute class yet.
  - Qt's 'bool QTextCursor::operator!=(const QTextCursor &rhs) const': an
    operator, which is not reflected yet.
  - Qt's 'bool QTextCursor::operator<(const QTextCursor &rhs) const': an
    operator, which is not reflected yet.
  - Qt's 'bool QTextCursor::operator<=(const QTextCursor &rhs) const': an
    operator, which is not reflected yet.
  - Qt's 'bool QTextCursor::operator==(const QTextCursor &rhs) const': an
    operator, which is not reflected yet.
  - Qt's 'bool QTextCursor::operator>=(const QTextCursor &rhs) const': an
    operator, which is not reflected yet.
  - Qt's 'bool QTextCursor::operator>(const QTextCursor &rhs) const': an
    operator, which is not reflected yet.

  What has no ritual
  ------------------

  5 of the 84 functions Qt declares: 5 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QTextCursor is created at the first use, not by
    'QTextCursor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextCursor back gives a copy the ritual made for
    Python, in a new cute QTextCursor.
  """

  #  The enums Qt writes inside QTextCursor, and the names Qt has for the
  #  combinations of its flags enums.
  MoveMode = MoveMode
  MoveOperation = MoveOperation
  SelectionType = SelectionType

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextCursor'

  #  Qt's '~QTextCursor()'. Naming it makes this a value class: Python owns
  #  every C++ QTextCursor behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QTextCursorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QTextCursor::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#isNull
    """
    #  bool QTextCursor::isNull() const
    return self.uglySide.call('ritual_ZNK11QTextCursor6isNullEv')

  def position(self) -> int:
    """
    Calls Qt's 'int QTextCursor::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#position
    """
    #  int QTextCursor::position() const
    return self.uglySide.call('ritual_ZNK11QTextCursor8positionEv')

  def positionInBlock(self) -> int:
    """
    Calls Qt's 'int QTextCursor::positionInBlock() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#positionInBlock
    """
    #  int QTextCursor::positionInBlock() const
    return self.uglySide.call('ritual_ZNK11QTextCursor15positionInBlockEv')

  def anchor(self) -> int:
    """
    Calls Qt's 'int QTextCursor::anchor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#anchor
    """
    #  int QTextCursor::anchor() const
    return self.uglySide.call('ritual_ZNK11QTextCursor6anchorEv')

  def visualNavigation(self) -> bool:
    """
    Calls Qt's 'bool QTextCursor::visualNavigation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#visualNavigation
    """
    #  bool QTextCursor::visualNavigation() const
    return self.uglySide.call('ritual_ZNK11QTextCursor16visualNavigationEv')

  def verticalMovementX(self) -> int:
    """
    Calls Qt's 'int QTextCursor::verticalMovementX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#verticalMovementX
    """
    #  int QTextCursor::verticalMovementX() const
    return self.uglySide.call('ritual_ZNK11QTextCursor17verticalMovementXEv')

  def keepPositionOnInsert(self) -> bool:
    """
    Calls Qt's 'bool QTextCursor::keepPositionOnInsert() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcursor.html#keepPositionOnInsert
    """
    #  bool QTextCursor::keepPositionOnInsert() const
    return self.uglySide.call(
        'ritual_ZNK11QTextCursor20keepPositionOnInsertEv',
    )

  def hasSelection(self) -> bool:
    """
    Calls Qt's 'bool QTextCursor::hasSelection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#hasSelection
    """
    #  bool QTextCursor::hasSelection() const
    return self.uglySide.call('ritual_ZNK11QTextCursor12hasSelectionEv')

  def hasComplexSelection(self) -> bool:
    """
    Calls Qt's 'bool QTextCursor::hasComplexSelection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcursor.html#hasComplexSelection
    """
    #  bool QTextCursor::hasComplexSelection() const
    return self.uglySide.call(
        'ritual_ZNK11QTextCursor19hasComplexSelectionEv',
    )

  def selectionStart(self) -> int:
    """
    Calls Qt's 'int QTextCursor::selectionStart() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#selectionStart
    """
    #  int QTextCursor::selectionStart() const
    return self.uglySide.call('ritual_ZNK11QTextCursor14selectionStartEv')

  def selectionEnd(self) -> int:
    """
    Calls Qt's 'int QTextCursor::selectionEnd() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#selectionEnd
    """
    #  int QTextCursor::selectionEnd() const
    return self.uglySide.call('ritual_ZNK11QTextCursor12selectionEndEv')

  def selectedText(self) -> str:
    """
    Calls Qt's 'QString QTextCursor::selectedText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#selectedText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextCursor::selectedText() const
    return self.uglySide.call('ritual_ZNK11QTextCursor12selectedTextEv')

  def charFormat(self) -> QTextCharFormat:
    """
    Calls Qt's 'QTextCharFormat QTextCursor::charFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#charFormat

    Returns
    -------

    QTextCharFormat
      A new cute QTextCharFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextCharFormat QTextCursor::charFormat() const
    address = self.uglySide.call('ritual_ZNK11QTextCursor10charFormatEv')
    return QTextCharFormat._cuteOwning(address)

  def blockFormat(self) -> QTextBlockFormat:
    """
    Calls Qt's 'QTextBlockFormat QTextCursor::blockFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#blockFormat

    Returns
    -------

    QTextBlockFormat
      A new cute QTextBlockFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextBlockFormat QTextCursor::blockFormat() const
    address = self.uglySide.call('ritual_ZNK11QTextCursor11blockFormatEv')
    return QTextBlockFormat._cuteOwning(address)

  def blockCharFormat(self) -> QTextCharFormat:
    """
    Calls Qt's 'QTextCharFormat QTextCursor::blockCharFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#blockCharFormat

    Returns
    -------

    QTextCharFormat
      A new cute QTextCharFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextCharFormat QTextCursor::blockCharFormat() const
    address = self.uglySide.call(
        'ritual_ZNK11QTextCursor15blockCharFormatEv',
    )
    return QTextCharFormat._cuteOwning(address)

  def atBlockStart(self) -> bool:
    """
    Calls Qt's 'bool QTextCursor::atBlockStart() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#atBlockStart
    """
    #  bool QTextCursor::atBlockStart() const
    return self.uglySide.call('ritual_ZNK11QTextCursor12atBlockStartEv')

  def atBlockEnd(self) -> bool:
    """
    Calls Qt's 'bool QTextCursor::atBlockEnd() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#atBlockEnd
    """
    #  bool QTextCursor::atBlockEnd() const
    return self.uglySide.call('ritual_ZNK11QTextCursor10atBlockEndEv')

  def atStart(self) -> bool:
    """
    Calls Qt's 'bool QTextCursor::atStart() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#atStart
    """
    #  bool QTextCursor::atStart() const
    return self.uglySide.call('ritual_ZNK11QTextCursor7atStartEv')

  def atEnd(self) -> bool:
    """
    Calls Qt's 'bool QTextCursor::atEnd() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#atEnd
    """
    #  bool QTextCursor::atEnd() const
    return self.uglySide.call('ritual_ZNK11QTextCursor5atEndEv')

  @overload(THIS)
  def isCopyOf(self, other: QTextCursor) -> bool:
    """
    Calls Qt's 'bool QTextCursor::isCopyOf(const QTextCursor &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#isCopyOf

    Parameters
    ----------

    other : QTextCursor
      Passed on as a value: Qt reads the C++ QTextCursor, which stays
      Python's own.
    """
    #  bool QTextCursor::isCopyOf(const QTextCursor &other) const
    return self.uglySide.call(
        'ritual_ZNK11QTextCursor8isCopyOfERKS_', self._valueOf(other),
    )

  def blockNumber(self) -> int:
    """
    Calls Qt's 'int QTextCursor::blockNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#blockNumber
    """
    #  int QTextCursor::blockNumber() const
    return self.uglySide.call('ritual_ZNK11QTextCursor11blockNumberEv')

  def columnNumber(self) -> int:
    """
    Calls Qt's 'int QTextCursor::columnNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#columnNumber
    """
    #  int QTextCursor::columnNumber() const
    return self.uglySide.call('ritual_ZNK11QTextCursor12columnNumberEv')

  def document(self) -> Optional[QTextDocument]:
    """
    Calls Qt's 'QTextDocument *QTextCursor::document() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#document

    Returns
    -------

    Optional[QTextDocument]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextDocument *QTextCursor::document() const
    address = self.uglySide.call('ritual_ZNK11QTextCursor8documentEv')
    return QTextDocument._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  @overload(int, MoveMode)
  def setPosition(
      self,
      pos: int,
      mode: MoveMode = MoveMode.MoveAnchor,
  ) -> None:
    """
    Calls Qt's 'void QTextCursor::setPosition(int pos, MoveMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#setPosition

    Parameters
    ----------

    pos : int
      Passed on as it is.

    mode : MoveMode
      Passed on as its number. May be left out, as in Qt: it is then
      MoveMode.MoveAnchor.
    """
    #  void QTextCursor::setPosition(int pos, MoveMode mode)
    self.uglySide.call(
        'ritual_ZN11QTextCursor11setPositionEiNS_8MoveModeE',
        pos, mode.value,
    )

  @overload(bool)
  def setVisualNavigation(self, b: bool) -> None:
    """
    Calls Qt's 'void QTextCursor::setVisualNavigation(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcursor.html#setVisualNavigation

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QTextCursor::setVisualNavigation(bool b)
    self.uglySide.call('ritual_ZN11QTextCursor19setVisualNavigationEb', b)

  @overload(int)
  def setVerticalMovementX(self, x: int) -> None:
    """
    Calls Qt's 'void QTextCursor::setVerticalMovementX(int x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcursor.html#setVerticalMovementX

    Parameters
    ----------

    x : int
      Passed on as it is.
    """
    #  void QTextCursor::setVerticalMovementX(int x)
    self.uglySide.call('ritual_ZN11QTextCursor20setVerticalMovementXEi', x)

  @overload(bool)
  def setKeepPositionOnInsert(self, b: bool) -> None:
    """
    Calls Qt's 'void QTextCursor::setKeepPositionOnInsert(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcursor.html#setKeepPositionOnInsert

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QTextCursor::setKeepPositionOnInsert(bool b)
    self.uglySide.call(
        'ritual_ZN11QTextCursor23setKeepPositionOnInsertEb', b,
    )

  @overload(QTextCharFormat)
  def setCharFormat(self, format: QTextCharFormat) -> None:
    """
    Calls Qt's 'void QTextCursor::setCharFormat(const QTextCharFormat
    &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#setCharFormat

    Parameters
    ----------

    format : QTextCharFormat
      Passed on as a value: Qt reads the C++ QTextCharFormat, which stays
      Python's own.
    """
    #  void QTextCursor::setCharFormat(const QTextCharFormat &format)
    self.uglySide.call(
        'ritual_ZN11QTextCursor13setCharFormatERK15QTextCharFormat',
        self._valueOf(format),
    )

  @overload(QTextBlockFormat)
  def setBlockFormat(self, format: QTextBlockFormat) -> None:
    """
    Calls Qt's 'void QTextCursor::setBlockFormat(const QTextBlockFormat
    &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#setBlockFormat

    Parameters
    ----------

    format : QTextBlockFormat
      Passed on as a value: Qt reads the C++ QTextBlockFormat, which stays
      Python's own.
    """
    #  void QTextCursor::setBlockFormat(const QTextBlockFormat &format)
    self.uglySide.call(
        'ritual_ZN11QTextCursor14setBlockFormatERK16QTextBlockFormat',
        self._valueOf(format),
    )

  @overload(QTextCharFormat)
  def setBlockCharFormat(self, format: QTextCharFormat) -> None:
    """
    Calls Qt's 'void QTextCursor::setBlockCharFormat(const QTextCharFormat
    &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcursor.html#setBlockCharFormat

    Parameters
    ----------

    format : QTextCharFormat
      Passed on as a value: Qt reads the C++ QTextCharFormat, which stays
      Python's own.
    """
    #  void QTextCursor::setBlockCharFormat(const QTextCharFormat &format)
    self.uglySide.call(
        'ritual_ZN11QTextCursor18setBlockCharFormatERK15QTextCharFormat',
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
    Notes what was given, for Qt's 'QTextCursor::QTextCursor()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#QTextCursor
    """
    #  QTextCursor::QTextCursor()
    self._noteCreation(QTextCursor, lambda: Rituals.call(
        'ritual_ZN11QTextCursorC1Ev',
    ))

  @overload(QTextDocument)
  @overload(NoneType)
  def __init__(self, document: Optional[QTextDocument]) -> None:
    """
    Notes what was given, for Qt's 'QTextCursor::QTextCursor(QTextDocument
    *document)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#QTextCursor

    Parameters
    ----------

    document : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QTextCursor::QTextCursor(QTextDocument *document)
    self._noteCreation(QTextCursor, lambda: Rituals.call(
        'ritual_ZN11QTextCursorC1EP13QTextDocument',
        self._addressOf(document),
    ))

  @overload(THIS)
  def __init__(self, cursor: QTextCursor) -> None:
    """
    Notes what was given, for Qt's 'QTextCursor::QTextCursor(const
    QTextCursor &cursor)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#QTextCursor

    Parameters
    ----------

    cursor : QTextCursor
      Passed on as a value: Qt reads the C++ QTextCursor, which stays
      Python's own.
    """
    #  QTextCursor::QTextCursor(const QTextCursor &cursor)
    self._noteCreation(QTextCursor, lambda: Rituals.call(
        'ritual_ZN11QTextCursorC1ERKS_', self._valueOf(cursor),
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

  @overload(str)
  def insertText(self, text: str) -> None:
    """
    Calls Qt's 'void QTextCursor::insertText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#insertText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextCursor::insertText(const QString &text)
    self.uglySide.call('ritual_ZN11QTextCursor10insertTextERK7QString', text)

  @overload(str, QTextCharFormat)
  def insertText(self, text: str, format: QTextCharFormat) -> None:
    """
    Calls Qt's 'void QTextCursor::insertText(const QString &text, const
    QTextCharFormat &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#insertText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    format : QTextCharFormat
      Passed on as a value: Qt reads the C++ QTextCharFormat, which stays
      Python's own.
    """
    #  void QTextCursor::insertText(const QString &text, const
    #      QTextCharFormat &format)
    self.uglySide.call(
        'ritual_ZN11QTextCursor10insertTextERK7QStringRK15QTextCharFormat',
        text, self._valueOf(format),
    )

  @overload(MoveOperation)
  @overload(MoveOperation, MoveMode)
  @overload(MoveOperation, MoveMode, int)
  def movePosition(
      self,
      op: MoveOperation,
      a1: MoveMode = MoveMode.MoveAnchor,
      n: int = 1,
  ) -> bool:
    """
    Calls Qt's 'bool QTextCursor::movePosition(MoveOperation op, MoveMode a1,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#movePosition

    Parameters
    ----------

    op : MoveOperation
      Passed on as its number.

    a1 : MoveMode
      Passed on as its number. May be left out, as in Qt: it is then
      MoveMode.MoveAnchor.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  bool QTextCursor::movePosition(MoveOperation op, MoveMode a1, int n)
    return self.uglySide.call(
        'ritual_ZN11QTextCursor12movePositionENS_13MoveOperationENS_8MoveMo'
        'deEi',
        op.value, a1.value, n,
    )

  def deleteChar(self) -> None:
    """
    Calls Qt's 'void QTextCursor::deleteChar()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#deleteChar
    """
    #  void QTextCursor::deleteChar()
    self.uglySide.call('ritual_ZN11QTextCursor10deleteCharEv')

  def deletePreviousChar(self) -> None:
    """
    Calls Qt's 'void QTextCursor::deletePreviousChar()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcursor.html#deletePreviousChar
    """
    #  void QTextCursor::deletePreviousChar()
    self.uglySide.call('ritual_ZN11QTextCursor18deletePreviousCharEv')

  @overload(SelectionType)
  def select(self, selection: SelectionType) -> None:
    """
    Calls Qt's 'void QTextCursor::select(SelectionType selection)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#select

    Parameters
    ----------

    selection : SelectionType
      Passed on as its number.
    """
    #  void QTextCursor::select(SelectionType selection)
    self.uglySide.call(
        'ritual_ZN11QTextCursor6selectENS_13SelectionTypeE', selection.value,
    )

  def removeSelectedText(self) -> None:
    """
    Calls Qt's 'void QTextCursor::removeSelectedText()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcursor.html#removeSelectedText
    """
    #  void QTextCursor::removeSelectedText()
    self.uglySide.call('ritual_ZN11QTextCursor18removeSelectedTextEv')

  def clearSelection(self) -> None:
    """
    Calls Qt's 'void QTextCursor::clearSelection()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#clearSelection
    """
    #  void QTextCursor::clearSelection()
    self.uglySide.call('ritual_ZN11QTextCursor14clearSelectionEv')

  @overload(QTextCharFormat)
  def mergeCharFormat(self, modifier: QTextCharFormat) -> None:
    """
    Calls Qt's 'void QTextCursor::mergeCharFormat(const QTextCharFormat
    &modifier)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#mergeCharFormat

    Parameters
    ----------

    modifier : QTextCharFormat
      Passed on as a value: Qt reads the C++ QTextCharFormat, which stays
      Python's own.
    """
    #  void QTextCursor::mergeCharFormat(const QTextCharFormat &modifier)
    self.uglySide.call(
        'ritual_ZN11QTextCursor15mergeCharFormatERK15QTextCharFormat',
        self._valueOf(modifier),
    )

  @overload(QTextBlockFormat)
  def mergeBlockFormat(self, modifier: QTextBlockFormat) -> None:
    """
    Calls Qt's 'void QTextCursor::mergeBlockFormat(const QTextBlockFormat
    &modifier)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#mergeBlockFormat

    Parameters
    ----------

    modifier : QTextBlockFormat
      Passed on as a value: Qt reads the C++ QTextBlockFormat, which stays
      Python's own.
    """
    #  void QTextCursor::mergeBlockFormat(const QTextBlockFormat &modifier)
    self.uglySide.call(
        'ritual_ZN11QTextCursor16mergeBlockFormatERK16QTextBlockFormat',
        self._valueOf(modifier),
    )

  @overload(QTextCharFormat)
  def mergeBlockCharFormat(self, modifier: QTextCharFormat) -> None:
    """
    Calls Qt's 'void QTextCursor::mergeBlockCharFormat(const QTextCharFormat
    &modifier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcursor.html#mergeBlockCharFormat

    Parameters
    ----------

    modifier : QTextCharFormat
      Passed on as a value: Qt reads the C++ QTextCharFormat, which stays
      Python's own.
    """
    #  void QTextCursor::mergeBlockCharFormat(const QTextCharFormat
    #      &modifier)
    self.uglySide.call(
        'ritual_ZN11QTextCursor20mergeBlockCharFormatERK15QTextCharFormat',
        self._valueOf(modifier),
    )

  @overload()
  def insertBlock(self) -> None:
    """
    Calls Qt's 'void QTextCursor::insertBlock()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#insertBlock
    """
    #  void QTextCursor::insertBlock()
    self.uglySide.call('ritual_ZN11QTextCursor11insertBlockEv')

  @overload(QTextBlockFormat)
  def insertBlock(self, format: QTextBlockFormat) -> None:
    """
    Calls Qt's 'void QTextCursor::insertBlock(const QTextBlockFormat
    &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#insertBlock

    Parameters
    ----------

    format : QTextBlockFormat
      Passed on as a value: Qt reads the C++ QTextBlockFormat, which stays
      Python's own.
    """
    #  void QTextCursor::insertBlock(const QTextBlockFormat &format)
    self.uglySide.call(
        'ritual_ZN11QTextCursor11insertBlockERK16QTextBlockFormat',
        self._valueOf(format),
    )

  @overload(QTextBlockFormat, QTextCharFormat)
  def insertBlock(
      self,
      format: QTextBlockFormat,
      charFormat: QTextCharFormat,
  ) -> None:
    """
    Calls Qt's 'void QTextCursor::insertBlock(const QTextBlockFormat &format,
    const QTextCharFormat &charFormat)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#insertBlock

    Parameters
    ----------

    format : QTextBlockFormat
      Passed on as a value: Qt reads the C++ QTextBlockFormat, which stays
      Python's own.

    charFormat : QTextCharFormat
      Passed on as a value: Qt reads the C++ QTextCharFormat, which stays
      Python's own.
    """
    #  void QTextCursor::insertBlock(const QTextBlockFormat &format, const
    #      QTextCharFormat &charFormat)
    self.uglySide.call(
        'ritual_ZN11QTextCursor11insertBlockERK16QTextBlockFormatRK15QTextC'
        'harFormat',
        self._valueOf(format), self._valueOf(charFormat),
    )

  @overload(str)
  def insertHtml(self, html: str) -> None:
    """
    Calls Qt's 'void QTextCursor::insertHtml(const QString &html)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#insertHtml

    Parameters
    ----------

    html : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextCursor::insertHtml(const QString &html)
    self.uglySide.call('ritual_ZN11QTextCursor10insertHtmlERK7QString', html)

  @overload(str)
  @overload(str, QTextDocument.MarkdownFeatures)
  def insertMarkdown(
      self,
      markdown: str,
      features: QTextDocument.MarkdownFeatures = (
          QTextDocument.MarkdownFeatures.MarkdownDialectGitHub),
  ) -> None:
    """
    Calls Qt's 'void QTextCursor::insertMarkdown(const QString &markdown,
    QTextDocument::MarkdownFeatures features)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#insertMarkdown

    Parameters
    ----------

    markdown : str
      Passed on as it is: a QString is made of it for the call.

    features : QTextDocument.MarkdownFeatures
      Passed on as its number. May be left out, as in Qt: it is then
      QTextDocument.MarkdownFeatures.MarkdownDialectGitHub.
    """
    #  void QTextCursor::insertMarkdown(const QString &markdown,
    #      QTextDocument::MarkdownFeatures features)
    self.uglySide.call(
        'ritual_ZN11QTextCursor14insertMarkdownERK7QString6QFlagsIN13QTextD'
        'ocument15MarkdownFeatureEE',
        markdown, features.value,
    )

  @overload(str)
  def insertImage(self, name: str) -> None:
    """
    Calls Qt's 'void QTextCursor::insertImage(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#insertImage

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextCursor::insertImage(const QString &name)
    self.uglySide.call(
        'ritual_ZN11QTextCursor11insertImageERK7QString', name,
    )

  @overload(QImage)
  @overload(QImage, str)
  def insertImage(self, image: QImage, name: str = '') -> None:
    """
    Calls Qt's 'void QTextCursor::insertImage(const QImage &image, const
    QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#insertImage

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    name : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QTextCursor::insertImage(const QImage &image, const QString
    #      &name)
    self.uglySide.call(
        'ritual_ZN11QTextCursor11insertImageERK6QImageRK7QString',
        self._valueOf(image), name,
    )

  def beginEditBlock(self) -> None:
    """
    Calls Qt's 'void QTextCursor::beginEditBlock()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#beginEditBlock
    """
    #  void QTextCursor::beginEditBlock()
    self.uglySide.call('ritual_ZN11QTextCursor14beginEditBlockEv')

  def joinPreviousEditBlock(self) -> None:
    """
    Calls Qt's 'void QTextCursor::joinPreviousEditBlock()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcursor.html#joinPreviousEditBlock
    """
    #  void QTextCursor::joinPreviousEditBlock()
    self.uglySide.call('ritual_ZN11QTextCursor21joinPreviousEditBlockEv')

  def endEditBlock(self) -> None:
    """
    Calls Qt's 'void QTextCursor::endEditBlock()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcursor.html#endEditBlock
    """
    #  void QTextCursor::endEditBlock()
    self.uglySide.call('ritual_ZN11QTextCursor12endEditBlockEv')
