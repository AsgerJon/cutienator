"""
QTextDocumentPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtextdocument_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QTextDocumentPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import QTextDocument, QTextLayout, QTextUndoCommand

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QChar
  from . import QAbstractTextDocumentLayout, QAbstractUndoItem, QFont
  from . import QTextBlock, QTextBlockData, QTextBlockFormat, QTextCharFormat
  from . import QTextCursorPrivate, QTextFormat, QTextFormatCollection
  from . import QTextFrame, QTextFrameFormat, QTextObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractTextDocumentLayout = WAIT['QAbstractTextDocumentLayout']
  QAbstractUndoItem = WAIT['QAbstractUndoItem']
  QChar = WAIT['QChar']
  QFont = WAIT['QFont']
  QTextBlock = WAIT['QTextBlock']
  QTextBlockFormat = WAIT['QTextBlockFormat']
  QTextCharFormat = WAIT['QTextCharFormat']
  QTextCursorPrivate = WAIT['QTextCursorPrivate']
  QTextFormat = WAIT['QTextFormat']
  QTextFrame = WAIT['QTextFrame']
  QTextFrameFormat = WAIT['QTextFrameFormat']
  QTextObject = WAIT['QTextObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextDocumentPrivate(QObjectPrivate):
  """
  The cute side of Qt's QTextDocumentPrivate: a plain Python object standing
  in front of one C++ QTextDocumentPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QTextDocumentPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTextDocumentPrivate that has a ritual and that
  Python can call so far, 76 names in all: 'q_func', 'init', 'clear',
  'setLayout', 'insert', 'insertBlock', 'move', 'remove',
  'aboutToRemoveCell', 'insertFrame', 'removeFrame', 'setCharFormat',
  'setBlockFormat', 'emitUndoAvailable', 'emitRedoAvailable', 'undoRedo',
  'undo', 'redo', 'appendUndoItem', 'beginEditBlock',
  'joinPreviousEditBlock', 'endEditBlock', 'finishEdit', 'isInEditBlock',
  'enableUndoRedo', 'isUndoRedoEnabled', 'isUndoAvailable',
  'isRedoAvailable', 'availableUndoSteps', 'availableRedoSteps', 'buffer',
  'plainText', 'length', 'formatCollection', 'layout', 'blocksBegin',
  'blocksEnd', 'blocksFind', 'blockCharFormatIndex', 'numBlocks', 'block',
  'nextCursorPosition', 'previousCursorPosition', 'leftCursorPosition',
  'rightCursorPosition', 'changeObjectFormat', 'setModified', 'isModified',
  'defaultFont', 'setDefaultFont', 'clearUndoRedoStacks', 'split', 'unite',
  'insert_string', 'insert_block', 'remove_string', 'insert_frame',
  'scan_frames', 'clearFrame', 'adjustDocumentChangesAndCursors',
  'documentChange', 'addCursor', 'removeCursor', 'frameAt', 'rootFrame',
  'objectForIndex', 'objectForFormat', 'createObject', 'deleteObject',
  'document', 'ensureMaximumBlockCount', 'get', 'canLayout',
  'contentsChanged', 'compressPieceTable', 'mergeCachedResources'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QTextDocument *QTextDocumentPrivate::q_func() const': takes
    in Python what 'QTextDocument *QTextDocumentPrivate::q_func()' takes.
  - Qt's 'QTextDocumentPrivate::~QTextDocumentPrivate()': the destructor:
    Python never removes a C++ QTextDocumentPrivate.
  - Qt's 'const QTextFormatCollection
    *QTextDocumentPrivate::formatCollection() const': takes in Python what
    'QTextFormatCollection *QTextDocumentPrivate::formatCollection()' takes.
  - Qt's 'FragmentIterator QTextDocumentPrivate::find(int pos) const': gives
    a type Python has no way to take yet.
  - Qt's 'FragmentIterator QTextDocumentPrivate::begin() const': gives a type
    Python has no way to take yet.
  - Qt's 'FragmentIterator QTextDocumentPrivate::end() const': gives a type
    Python has no way to take yet.
  - Qt's 'const BlockMap &QTextDocumentPrivate::blockMap() const': gives a
    type Python has no way to take yet.
  - Qt's 'const FragmentMap &QTextDocumentPrivate::fragmentMap() const':
    gives a type Python has no way to take yet.
  - Qt's 'BlockMap &QTextDocumentPrivate::blockMap()': gives a type Python
    has no way to take yet.
  - Qt's 'FragmentMap &QTextDocumentPrivate::fragmentMap()': gives a type
    Python has no way to take yet.
  - Qt's 'int QTextDocumentPrivate::remove_block(int pos, int *blockformat,
    int command, QTextUndoCommand::Operation op)': takes a number to change
    where it is.
  - Qt's 'const QTextDocument *QTextDocumentPrivate::document() const': takes
    in Python what 'QTextDocument *QTextDocumentPrivate::document()' takes.
  - Qt's 'QTextDocumentPrivate *QTextDocumentPrivate::get(QTextDocument
    *document)': takes in Python what 'const QTextDocumentPrivate
    *QTextDocumentPrivate::get(const QTextDocument *document)' takes.
  - Qt's 'QTextDocumentPrivate *QTextDocumentPrivate::get(QTextBlock
    &block)': takes a type Python has no way to hand over yet.
  - Qt's 'const QTextDocumentPrivate *QTextDocumentPrivate::get(const
    QTextObject *object)': takes in Python what 'const QTextDocumentPrivate
    *QTextDocumentPrivate::get(const QTextDocument *document)' takes.
  - Qt's 'QTextDocumentPrivate::QTextDocumentPrivate(const
    QTextDocumentPrivate &m)': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  1 of the 101 functions Qt declares: 1 not a gap.

  What to expect
  --------------

  - The C++ QTextDocumentPrivate is created at the first use, not by
    'QTextDocumentPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTextDocumentPrivate.
  - Each name of Qt's QTextDocumentPrivate that has no cute function yet,
    'begin', 'blockMap', 'end', 'find', 'fragmentMap', 'remove_block', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QTextDocumentPrivate, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class FormatChangeMode(CuteNum):
    """
    The enum 'QTextDocumentPrivate::FormatChangeMode' of Qt, with the 3 names
    Qt gives in it.
    """

    MergeFormat = Kee[int](0)
    SetFormat = Kee[int](1)
    SetFormatAndPreserveObjectIndices = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QTextBlock)
  def block(it: QTextBlock) -> Optional[QTextBlockData]:
    """
    Calls Qt's 'const QTextBlockData *QTextDocumentPrivate::block(const
    QTextBlock &it)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentprivate.html#block

    Parameters
    ----------

    it : QTextBlock
      Passed on as a value: Qt reads the C++ QTextBlock, which stays Python's
      own.

    Returns
    -------

    Optional[QTextBlockData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QTextBlockData *QTextDocumentPrivate::block(const QTextBlock
    #      &it)
    address = Rituals.call(
        'ritual_ZN20QTextDocumentPrivate5blockERK10QTextBlock',
        CuteMixin._valueOf(it),
    )
    from . import QTextBlockData
    return QTextBlockData._cuteAt(address)

  @staticmethod
  @overload(QTextFrame)
  @overload(NoneType)
  def clearFrame(f: Optional[QTextFrame]) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::clearFrame(QTextFrame *f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#clearFrame

    Parameters
    ----------

    f : Optional[QTextFrame]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextDocumentPrivate::clearFrame(QTextFrame *f)
    Rituals.call(
        'ritual_ZN20QTextDocumentPrivate10clearFrameEP10QTextFrame',
        CuteMixin._addressOf(f),
    )

  @staticmethod
  @overload(QTextDocument)
  @overload(NoneType)
  def get(
      document: Optional[QTextDocument],
  ) -> Optional[QTextDocumentPrivate]:
    """
    Calls Qt's 'const QTextDocumentPrivate *QTextDocumentPrivate::get(const
    QTextDocument *document)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentprivate.html#get

    Parameters
    ----------

    document : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QTextDocumentPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QTextDocumentPrivate *QTextDocumentPrivate::get(const
    #      QTextDocument *document)
    address = Rituals.call(
        'ritual_ZN20QTextDocumentPrivate3getEPK13QTextDocument',
        CuteMixin._addressOf(document),
    )
    return QTextDocumentPrivate._cuteAt(address)

  @staticmethod
  @overload(QTextBlock)
  def get(block: QTextBlock) -> Optional[QTextDocumentPrivate]:
    """
    Calls Qt's 'const QTextDocumentPrivate *QTextDocumentPrivate::get(const
    QTextBlock &block)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentprivate.html#get

    Parameters
    ----------

    block : QTextBlock
      Passed on as a value: Qt reads the C++ QTextBlock, which stays Python's
      own.

    Returns
    -------

    Optional[QTextDocumentPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QTextDocumentPrivate *QTextDocumentPrivate::get(const QTextBlock
    #      &block)
    address = Rituals.call(
        'ritual_ZN20QTextDocumentPrivate3getERK10QTextBlock',
        CuteMixin._valueOf(block),
    )
    return QTextDocumentPrivate._cuteAt(address)

  @staticmethod
  @overload(QTextObject)
  def get(object: Optional[QTextObject]) -> Optional[QTextDocumentPrivate]:
    """
    Calls Qt's 'QTextDocumentPrivate *QTextDocumentPrivate::get(QTextObject
    *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentprivate.html#get

    Parameters
    ----------

    object : Optional[QTextObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QTextDocumentPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextDocumentPrivate *QTextDocumentPrivate::get(QTextObject *object)
    address = Rituals.call(
        'ritual_ZN20QTextDocumentPrivate3getEP11QTextObject',
        CuteMixin._addressOf(object),
    )
    return QTextDocumentPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextDocumentPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isInEditBlock(self) -> bool:
    """
    Calls Qt's 'bool QTextDocumentPrivate::isInEditBlock() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#isInEditBlock
    """
    #  bool QTextDocumentPrivate::isInEditBlock() const
    return self.uglySide.call(
        'ritual_ZNK20QTextDocumentPrivate13isInEditBlockEv',
    )

  def isUndoRedoEnabled(self) -> bool:
    """
    Calls Qt's 'bool QTextDocumentPrivate::isUndoRedoEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#isUndoRedoEnabled
    """
    #  bool QTextDocumentPrivate::isUndoRedoEnabled() const
    return self.uglySide.call(
        'ritual_ZNK20QTextDocumentPrivate17isUndoRedoEnabledEv',
    )

  def isUndoAvailable(self) -> bool:
    """
    Calls Qt's 'bool QTextDocumentPrivate::isUndoAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#isUndoAvailable
    """
    #  bool QTextDocumentPrivate::isUndoAvailable() const
    return self.uglySide.call(
        'ritual_ZNK20QTextDocumentPrivate15isUndoAvailableEv',
    )

  def isRedoAvailable(self) -> bool:
    """
    Calls Qt's 'bool QTextDocumentPrivate::isRedoAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#isRedoAvailable
    """
    #  bool QTextDocumentPrivate::isRedoAvailable() const
    return self.uglySide.call(
        'ritual_ZNK20QTextDocumentPrivate15isRedoAvailableEv',
    )

  def availableUndoSteps(self) -> int:
    """
    Calls Qt's 'int QTextDocumentPrivate::availableUndoSteps() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#availableUndoSteps
    """
    #  int QTextDocumentPrivate::availableUndoSteps() const
    return self.uglySide.call(
        'ritual_ZNK20QTextDocumentPrivate18availableUndoStepsEv',
    )

  def availableRedoSteps(self) -> int:
    """
    Calls Qt's 'int QTextDocumentPrivate::availableRedoSteps() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#availableRedoSteps
    """
    #  int QTextDocumentPrivate::availableRedoSteps() const
    return self.uglySide.call(
        'ritual_ZNK20QTextDocumentPrivate18availableRedoStepsEv',
    )

  def buffer(self) -> str:
    """
    Calls Qt's 'QString QTextDocumentPrivate::buffer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentprivate.html#buffer

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextDocumentPrivate::buffer() const
    return self.uglySide.call('ritual_ZNK20QTextDocumentPrivate6bufferEv')

  def plainText(self) -> str:
    """
    Calls Qt's 'QString QTextDocumentPrivate::plainText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#plainText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextDocumentPrivate::plainText() const
    return self.uglySide.call('ritual_ZNK20QTextDocumentPrivate9plainTextEv')

  def length(self) -> int:
    """
    Calls Qt's 'int QTextDocumentPrivate::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentprivate.html#length
    """
    #  int QTextDocumentPrivate::length() const
    return self.uglySide.call('ritual_ZNK20QTextDocumentPrivate6lengthEv')

  def layout(self) -> Optional[QAbstractTextDocumentLayout]:
    """
    Calls Qt's 'QAbstractTextDocumentLayout *QTextDocumentPrivate::layout()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentprivate.html#layout

    Returns
    -------

    Optional[QAbstractTextDocumentLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractTextDocumentLayout *QTextDocumentPrivate::layout() const
    address = self.uglySide.call('ritual_ZNK20QTextDocumentPrivate6layoutEv')
    from . import QAbstractTextDocumentLayout
    return QAbstractTextDocumentLayout._cuteAt(address)

  def blocksBegin(self) -> QTextBlock:
    """
    Calls Qt's 'QTextBlock QTextDocumentPrivate::blocksBegin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#blocksBegin

    Returns
    -------

    QTextBlock
      A new cute QTextBlock around the copy Qt gave back. Python owns it.
    """
    #  QTextBlock QTextDocumentPrivate::blocksBegin() const
    address = self.uglySide.call(
        'ritual_ZNK20QTextDocumentPrivate11blocksBeginEv',
    )
    from . import QTextBlock
    return QTextBlock._cuteOwning(address)

  def blocksEnd(self) -> QTextBlock:
    """
    Calls Qt's 'QTextBlock QTextDocumentPrivate::blocksEnd() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#blocksEnd

    Returns
    -------

    QTextBlock
      A new cute QTextBlock around the copy Qt gave back. Python owns it.
    """
    #  QTextBlock QTextDocumentPrivate::blocksEnd() const
    address = self.uglySide.call(
        'ritual_ZNK20QTextDocumentPrivate9blocksEndEv',
    )
    from . import QTextBlock
    return QTextBlock._cuteOwning(address)

  @overload(int)
  def blocksFind(self, pos: int) -> QTextBlock:
    """
    Calls Qt's 'QTextBlock QTextDocumentPrivate::blocksFind(int pos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#blocksFind

    Parameters
    ----------

    pos : int
      Passed on as it is.

    Returns
    -------

    QTextBlock
      A new cute QTextBlock around the copy Qt gave back. Python owns it.
    """
    #  QTextBlock QTextDocumentPrivate::blocksFind(int pos) const
    address = self.uglySide.call(
        'ritual_ZNK20QTextDocumentPrivate10blocksFindEi', pos,
    )
    from . import QTextBlock
    return QTextBlock._cuteOwning(address)

  @overload(int)
  def blockCharFormatIndex(self, node: int) -> int:
    """
    Calls Qt's 'int QTextDocumentPrivate::blockCharFormatIndex(int node)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#blockCharFormatIndex

    Parameters
    ----------

    node : int
      Passed on as it is.
    """
    #  int QTextDocumentPrivate::blockCharFormatIndex(int node) const
    return self.uglySide.call(
        'ritual_ZNK20QTextDocumentPrivate20blockCharFormatIndexEi', node,
    )

  def numBlocks(self) -> int:
    """
    Calls Qt's 'int QTextDocumentPrivate::numBlocks() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#numBlocks
    """
    #  int QTextDocumentPrivate::numBlocks() const
    return self.uglySide.call('ritual_ZNK20QTextDocumentPrivate9numBlocksEv')

  @overload(int, QTextLayout.CursorMode)
  def nextCursorPosition(
      self,
      position: int,
      mode: QTextLayout.CursorMode,
  ) -> int:
    """
    Calls Qt's 'int QTextDocumentPrivate::nextCursorPosition(int position,
    QTextLayout::CursorMode mode) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#nextCursorPosition

    Parameters
    ----------

    position : int
      Passed on as it is.

    mode : QTextLayout.CursorMode
      Passed on as its number.
    """
    #  int QTextDocumentPrivate::nextCursorPosition(int position,
    #      QTextLayout::CursorMode mode) const
    return self.uglySide.call(
        'ritual_ZNK20QTextDocumentPrivate18nextCursorPositionEiN11QTextLayo'
        'ut10CursorModeE',
        position, mode.value,
    )

  @overload(int, QTextLayout.CursorMode)
  def previousCursorPosition(
      self,
      position: int,
      mode: QTextLayout.CursorMode,
  ) -> int:
    """
    Calls Qt's 'int QTextDocumentPrivate::previousCursorPosition(int
    position, QTextLayout::CursorMode mode) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#previousCursorPosition

    Parameters
    ----------

    position : int
      Passed on as it is.

    mode : QTextLayout.CursorMode
      Passed on as its number.
    """
    #  int QTextDocumentPrivate::previousCursorPosition(int position,
    #      QTextLayout::CursorMode mode) const
    return self.uglySide.call(
        'ritual_ZNK20QTextDocumentPrivate22previousCursorPositionEiN11QText'
        'Layout10CursorModeE',
        position, mode.value,
    )

  @overload(int)
  def leftCursorPosition(self, position: int) -> int:
    """
    Calls Qt's 'int QTextDocumentPrivate::leftCursorPosition(int position)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#leftCursorPosition

    Parameters
    ----------

    position : int
      Passed on as it is.
    """
    #  int QTextDocumentPrivate::leftCursorPosition(int position) const
    return self.uglySide.call(
        'ritual_ZNK20QTextDocumentPrivate18leftCursorPositionEi', position,
    )

  @overload(int)
  def rightCursorPosition(self, position: int) -> int:
    """
    Calls Qt's 'int QTextDocumentPrivate::rightCursorPosition(int position)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#rightCursorPosition

    Parameters
    ----------

    position : int
      Passed on as it is.
    """
    #  int QTextDocumentPrivate::rightCursorPosition(int position) const
    return self.uglySide.call(
        'ritual_ZNK20QTextDocumentPrivate19rightCursorPositionEi', position,
    )

  def isModified(self) -> bool:
    """
    Calls Qt's 'bool QTextDocumentPrivate::isModified() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#isModified
    """
    #  bool QTextDocumentPrivate::isModified() const
    return self.uglySide.call(
        'ritual_ZNK20QTextDocumentPrivate10isModifiedEv',
    )

  def defaultFont(self) -> QFont:
    """
    Calls Qt's 'QFont QTextDocumentPrivate::defaultFont() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#defaultFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QTextDocumentPrivate::defaultFont() const
    address = self.uglySide.call(
        'ritual_ZNK20QTextDocumentPrivate11defaultFontEv',
    )
    from . import QFont
    return QFont._cuteOwning(address)

  @overload(int)
  def frameAt(self, pos: int) -> Optional[QTextFrame]:
    """
    Calls Qt's 'QTextFrame *QTextDocumentPrivate::frameAt(int pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentprivate.html#frameAt

    Parameters
    ----------

    pos : int
      Passed on as it is.

    Returns
    -------

    Optional[QTextFrame]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextFrame *QTextDocumentPrivate::frameAt(int pos) const
    address = self.uglySide.call(
        'ritual_ZNK20QTextDocumentPrivate7frameAtEi', pos,
    )
    from . import QTextFrame
    return QTextFrame._cuteAt(address)

  def rootFrame(self) -> Optional[QTextFrame]:
    """
    Calls Qt's 'QTextFrame *QTextDocumentPrivate::rootFrame() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#rootFrame

    Returns
    -------

    Optional[QTextFrame]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextFrame *QTextDocumentPrivate::rootFrame() const
    address = self.uglySide.call(
        'ritual_ZNK20QTextDocumentPrivate9rootFrameEv',
    )
    from . import QTextFrame
    return QTextFrame._cuteAt(address)

  @overload(int)
  def objectForIndex(self, objectIndex: int) -> Optional[QTextObject]:
    """
    Calls Qt's 'QTextObject *QTextDocumentPrivate::objectForIndex(int
    objectIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#objectForIndex

    Parameters
    ----------

    objectIndex : int
      Passed on as it is.

    Returns
    -------

    Optional[QTextObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextObject *QTextDocumentPrivate::objectForIndex(int objectIndex)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK20QTextDocumentPrivate14objectForIndexEi', objectIndex,
    )
    from . import QTextObject
    return QTextObject._cuteAt(address)

  @overload(int)
  def objectForFormat(self, formatIndex: int) -> Optional[QTextObject]:
    """
    Calls Qt's 'QTextObject *QTextDocumentPrivate::objectForFormat(int
    formatIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#objectForFormat

    Parameters
    ----------

    formatIndex : int
      Passed on as it is.

    Returns
    -------

    Optional[QTextObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextObject *QTextDocumentPrivate::objectForFormat(int formatIndex)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK20QTextDocumentPrivate15objectForFormatEi', formatIndex,
    )
    from . import QTextObject
    return QTextObject._cuteAt(address)

  @overload(QTextFormat)
  def objectForFormat(self, f: QTextFormat) -> Optional[QTextObject]:
    """
    Calls Qt's 'QTextObject *QTextDocumentPrivate::objectForFormat(const
    QTextFormat &f) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#objectForFormat

    Parameters
    ----------

    f : QTextFormat
      Passed on as a value: Qt reads the C++ QTextFormat, which stays
      Python's own.

    Returns
    -------

    Optional[QTextObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextObject *QTextDocumentPrivate::objectForFormat(const QTextFormat
    #      &f) const
    address = self.uglySide.call(
        'ritual_ZNK20QTextDocumentPrivate15objectForFormatERK11QTextFormat',
        self._valueOf(f),
    )
    from . import QTextObject
    return QTextObject._cuteAt(address)

  def canLayout(self) -> bool:
    """
    Calls Qt's 'bool QTextDocumentPrivate::canLayout() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#canLayout
    """
    #  bool QTextDocumentPrivate::canLayout() const
    return self.uglySide.call('ritual_ZNK20QTextDocumentPrivate9canLayoutEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractTextDocumentLayout)
  @overload(NoneType)
  def setLayout(self, layout: Optional[QAbstractTextDocumentLayout]) -> None:
    """
    Calls Qt's 'void
    QTextDocumentPrivate::setLayout(QAbstractTextDocumentLayout *layout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#setLayout

    Parameters
    ----------

    layout : Optional[QAbstractTextDocumentLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextDocumentPrivate::setLayout(QAbstractTextDocumentLayout
    #      *layout)
    self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate9setLayoutEP27QAbstractTextDocument'
        'Layout',
        self._addressOf(layout),
    )

  @overload(int, int, QTextCharFormat)
  @overload(int, int, QTextCharFormat, FormatChangeMode)
  def setCharFormat(
      self,
      pos: int,
      length: int,
      newFormat: QTextCharFormat,
      mode: FormatChangeMode = FormatChangeMode.SetFormat,
  ) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::setCharFormat(int pos, int length,
    const QTextCharFormat &newFormat, FormatChangeMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#setCharFormat

    Parameters
    ----------

    pos : int
      Passed on as it is.

    length : int
      Passed on as it is.

    newFormat : QTextCharFormat
      Passed on as a value: Qt reads the C++ QTextCharFormat, which stays
      Python's own.

    mode : FormatChangeMode
      Passed on as its number. May be left out, as in Qt: it is then
      FormatChangeMode.SetFormat.
    """
    #  void QTextDocumentPrivate::setCharFormat(int pos, int length, const
    #      QTextCharFormat &newFormat, FormatChangeMode mode)
    self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate13setCharFormatEiiRK15QTextCharForm'
        'atNS_16FormatChangeModeE',
        pos, length, self._valueOf(newFormat), mode.value,
    )

  @overload(QTextBlock, QTextBlock, QTextBlockFormat)
  @overload(QTextBlock, QTextBlock, QTextBlockFormat, FormatChangeMode)
  def setBlockFormat(
      self,
      from_: QTextBlock,
      to: QTextBlock,
      newFormat: QTextBlockFormat,
      mode: FormatChangeMode = FormatChangeMode.SetFormat,
  ) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::setBlockFormat(const QTextBlock
    &from, const QTextBlock &to, const QTextBlockFormat &newFormat,
    FormatChangeMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#setBlockFormat

    Parameters
    ----------

    from_ : QTextBlock
      Passed on as a value: Qt reads the C++ QTextBlock, which stays Python's
      own.

    to : QTextBlock
      Passed on as a value: Qt reads the C++ QTextBlock, which stays Python's
      own.

    newFormat : QTextBlockFormat
      Passed on as a value: Qt reads the C++ QTextBlockFormat, which stays
      Python's own.

    mode : FormatChangeMode
      Passed on as its number. May be left out, as in Qt: it is then
      FormatChangeMode.SetFormat.
    """
    #  void QTextDocumentPrivate::setBlockFormat(const QTextBlock &from,
    #      const QTextBlock &to, const QTextBlockFormat &newFormat,
    #      FormatChangeMode mode)
    self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate14setBlockFormatERK10QTextBlockS2_R'
        'K16QTextBlockFormatNS_16FormatChangeModeE',
        self._valueOf(from_), self._valueOf(to), self._valueOf(newFormat),
        mode.value,
    )

  @overload(bool)
  def setModified(self, m: bool) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::setModified(bool m)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#setModified

    Parameters
    ----------

    m : bool
      Passed on as it is.
    """
    #  void QTextDocumentPrivate::setModified(bool m)
    self.uglySide.call('ritual_ZN20QTextDocumentPrivate11setModifiedEb', m)

  @overload(QFont)
  def setDefaultFont(self, f: QFont) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::setDefaultFont(const QFont &f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#setDefaultFont

    Parameters
    ----------

    f : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QTextDocumentPrivate::setDefaultFont(const QFont &f)
    self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate14setDefaultFontERK5QFont',
        self._valueOf(f),
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
    Notes what was given, for Qt's
    'QTextDocumentPrivate::QTextDocumentPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#QTextDocumentPrivate
    """
    #  QTextDocumentPrivate::QTextDocumentPrivate()
    self._noteCreation(QTextDocumentPrivate, lambda: Rituals.call(
        'ritual_ZN20QTextDocumentPrivateC1Ev',
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

  def q_func(self) -> Optional[QTextDocument]:
    """
    Calls Qt's 'QTextDocument *QTextDocumentPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentprivate.html#q_func

    Returns
    -------

    Optional[QTextDocument]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextDocument *QTextDocumentPrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QTextDocumentPrivate6q_funcEv')
    return QTextDocument._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentprivate.html#init
    """
    #  void QTextDocumentPrivate::init()
    self.uglySide.call('ritual_ZN20QTextDocumentPrivate4initEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentprivate.html#clear
    """
    #  void QTextDocumentPrivate::clear()
    self.uglySide.call('ritual_ZN20QTextDocumentPrivate5clearEv')

  @overload(int, str, int)
  def insert(self, pos: int, text: str, format: int) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::insert(int pos, QStringView text,
    int format)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentprivate.html#insert

    Parameters
    ----------

    pos : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.

    format : int
      Passed on as it is.
    """
    #  void QTextDocumentPrivate::insert(int pos, QStringView text, int
    #      format)
    self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate6insertEi11QStringViewi',
        pos, text, format,
    )

  @overload(int, QChar, int)
  def insert(self, pos: int, c: QChar, format: int) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::insert(int pos, QChar c, int
    format)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentprivate.html#insert

    Parameters
    ----------

    pos : int
      Passed on as it is.

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    format : int
      Passed on as it is.
    """
    #  void QTextDocumentPrivate::insert(int pos, QChar c, int format)
    self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate6insertEi5QChari',
        pos, self._valueOf(c), format,
    )

  @overload(int, int, int, int)
  def insert(
      self,
      pos: int,
      strPos: int,
      strLength: int,
      format: int,
  ) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::insert(int pos, int strPos, int
    strLength, int format)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentprivate.html#insert

    Parameters
    ----------

    pos : int
      Passed on as it is.

    strPos : int
      Passed on as it is.

    strLength : int
      Passed on as it is.

    format : int
      Passed on as it is.
    """
    #  void QTextDocumentPrivate::insert(int pos, int strPos, int strLength,
    #      int format)
    self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate6insertEiiii',
        pos, strPos, strLength, format,
    )

  @overload(int, int, int)
  @overload(int, int, int, QTextUndoCommand.Operation)
  def insertBlock(
      self,
      pos: int,
      blockFormat: int,
      charFormat: int,
      a3: QTextUndoCommand.Operation = QTextUndoCommand.Operation.MoveCursor,
  ) -> int:
    """
    Calls Qt's 'int QTextDocumentPrivate::insertBlock(int pos, int
    blockFormat, int charFormat, QTextUndoCommand::Operation a3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#insertBlock

    Parameters
    ----------

    pos : int
      Passed on as it is.

    blockFormat : int
      Passed on as it is.

    charFormat : int
      Passed on as it is.

    a3 : QTextUndoCommand.Operation
      Passed on as its number. May be left out, as in Qt: it is then
      QTextUndoCommand.Operation.MoveCursor.
    """
    #  int QTextDocumentPrivate::insertBlock(int pos, int blockFormat, int
    #      charFormat, QTextUndoCommand::Operation a3)
    return self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate11insertBlockEiiiN16QTextUndoComman'
        'd9OperationE',
        pos, blockFormat, charFormat, a3.value,
    )

  @overload(QChar, int, int, int)
  @overload(QChar, int, int, int, QTextUndoCommand.Operation)
  def insertBlock(
      self,
      blockSeparator: QChar,
      pos: int,
      blockFormat: int,
      charFormat: int,
      op: QTextUndoCommand.Operation = QTextUndoCommand.Operation.MoveCursor,
  ) -> int:
    """
    Calls Qt's 'int QTextDocumentPrivate::insertBlock(QChar blockSeparator,
    int pos, int blockFormat, int charFormat, QTextUndoCommand::Operation
    op)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#insertBlock

    Parameters
    ----------

    blockSeparator : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    pos : int
      Passed on as it is.

    blockFormat : int
      Passed on as it is.

    charFormat : int
      Passed on as it is.

    op : QTextUndoCommand.Operation
      Passed on as its number. May be left out, as in Qt: it is then
      QTextUndoCommand.Operation.MoveCursor.
    """
    #  int QTextDocumentPrivate::insertBlock(QChar blockSeparator, int pos,
    #      int blockFormat, int charFormat, QTextUndoCommand::Operation op)
    return self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate11insertBlockE5QChariiiN16QTextUndo'
        'Command9OperationE',
        self._valueOf(blockSeparator), pos, blockFormat, charFormat,
        op.value,
    )

  @overload(int, int, int)
  @overload(int, int, int, QTextUndoCommand.Operation)
  def move(
      self,
      from_: int,
      to: int,
      length: int,
      a3: QTextUndoCommand.Operation = QTextUndoCommand.Operation.MoveCursor,
  ) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::move(int from, int to, int length,
    QTextUndoCommand::Operation a3)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentprivate.html#move

    Parameters
    ----------

    from_ : int
      Passed on as it is.

    to : int
      Passed on as it is.

    length : int
      Passed on as it is.

    a3 : QTextUndoCommand.Operation
      Passed on as its number. May be left out, as in Qt: it is then
      QTextUndoCommand.Operation.MoveCursor.
    """
    #  void QTextDocumentPrivate::move(int from, int to, int length,
    #      QTextUndoCommand::Operation a3)
    self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate4moveEiiiN16QTextUndoCommand9Operat'
        'ionE',
        from_, to, length, a3.value,
    )

  @overload(int, int)
  @overload(int, int, QTextUndoCommand.Operation)
  def remove(
      self,
      pos: int,
      length: int,
      a2: QTextUndoCommand.Operation = QTextUndoCommand.Operation.MoveCursor,
  ) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::remove(int pos, int length,
    QTextUndoCommand::Operation a2)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentprivate.html#remove

    Parameters
    ----------

    pos : int
      Passed on as it is.

    length : int
      Passed on as it is.

    a2 : QTextUndoCommand.Operation
      Passed on as its number. May be left out, as in Qt: it is then
      QTextUndoCommand.Operation.MoveCursor.
    """
    #  void QTextDocumentPrivate::remove(int pos, int length,
    #      QTextUndoCommand::Operation a2)
    self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate6removeEiiN16QTextUndoCommand9Opera'
        'tionE',
        pos, length, a2.value,
    )

  @overload(int, int)
  def aboutToRemoveCell(self, cursorFrom: int, cursorEnd: int) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::aboutToRemoveCell(int cursorFrom,
    int cursorEnd)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#aboutToRemoveCell

    Parameters
    ----------

    cursorFrom : int
      Passed on as it is.

    cursorEnd : int
      Passed on as it is.
    """
    #  void QTextDocumentPrivate::aboutToRemoveCell(int cursorFrom, int
    #      cursorEnd)
    self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate17aboutToRemoveCellEii',
        cursorFrom, cursorEnd,
    )

  @overload(int, int, QTextFrameFormat)
  def insertFrame(
      self,
      start: int,
      end: int,
      format: QTextFrameFormat,
  ) -> Optional[QTextFrame]:
    """
    Calls Qt's 'QTextFrame *QTextDocumentPrivate::insertFrame(int start, int
    end, const QTextFrameFormat &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#insertFrame

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.

    format : QTextFrameFormat
      Passed on as a value: Qt reads the C++ QTextFrameFormat, which stays
      Python's own.

    Returns
    -------

    Optional[QTextFrame]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextFrame *QTextDocumentPrivate::insertFrame(int start, int end,
    #      const QTextFrameFormat &format)
    address = self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate11insertFrameEiiRK16QTextFrameForma'
        't',
        start, end, self._valueOf(format),
    )
    from . import QTextFrame
    return QTextFrame._cuteAt(address)

  @overload(QTextFrame)
  @overload(NoneType)
  def removeFrame(self, frame: Optional[QTextFrame]) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::removeFrame(QTextFrame *frame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#removeFrame

    Parameters
    ----------

    frame : Optional[QTextFrame]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextDocumentPrivate::removeFrame(QTextFrame *frame)
    self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate11removeFrameEP10QTextFrame',
        self._addressOf(frame),
    )

  @overload(bool)
  def emitUndoAvailable(self, available: bool) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::emitUndoAvailable(bool
    available)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#emitUndoAvailable

    Parameters
    ----------

    available : bool
      Passed on as it is.
    """
    #  void QTextDocumentPrivate::emitUndoAvailable(bool available)
    self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate17emitUndoAvailableEb', available,
    )

  @overload(bool)
  def emitRedoAvailable(self, available: bool) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::emitRedoAvailable(bool
    available)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#emitRedoAvailable

    Parameters
    ----------

    available : bool
      Passed on as it is.
    """
    #  void QTextDocumentPrivate::emitRedoAvailable(bool available)
    self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate17emitRedoAvailableEb', available,
    )

  @overload(bool)
  def undoRedo(self, undo: bool) -> int:
    """
    Calls Qt's 'int QTextDocumentPrivate::undoRedo(bool undo)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentprivate.html#undoRedo

    Parameters
    ----------

    undo : bool
      Passed on as it is.
    """
    #  int QTextDocumentPrivate::undoRedo(bool undo)
    return self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate8undoRedoEb', undo,
    )

  def undo(self) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::undo()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentprivate.html#undo
    """
    #  void QTextDocumentPrivate::undo()
    self.uglySide.call('ritual_ZN20QTextDocumentPrivate4undoEv')

  def redo(self) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::redo()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentprivate.html#redo
    """
    #  void QTextDocumentPrivate::redo()
    self.uglySide.call('ritual_ZN20QTextDocumentPrivate4redoEv')

  @overload(QAbstractUndoItem)
  @overload(NoneType)
  def appendUndoItem(self, a0: Optional[QAbstractUndoItem]) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::appendUndoItem(QAbstractUndoItem
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#appendUndoItem

    Parameters
    ----------

    a0 : Optional[QAbstractUndoItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextDocumentPrivate::appendUndoItem(QAbstractUndoItem *a0)
    self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate14appendUndoItemEP17QAbstractUndoIt'
        'em',
        self._addressOf(a0),
    )

  @overload(QTextUndoCommand)
  def appendUndoItem(self, c: QTextUndoCommand) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::appendUndoItem(const
    QTextUndoCommand &c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#appendUndoItem

    Parameters
    ----------

    c : QTextUndoCommand
      Passed on as a value: Qt reads the C++ QTextUndoCommand, which stays
      Python's own.
    """
    #  void QTextDocumentPrivate::appendUndoItem(const QTextUndoCommand &c)
    self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate14appendUndoItemERK16QTextUndoComma'
        'nd',
        self._valueOf(c),
    )

  def beginEditBlock(self) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::beginEditBlock()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#beginEditBlock
    """
    #  void QTextDocumentPrivate::beginEditBlock()
    self.uglySide.call('ritual_ZN20QTextDocumentPrivate14beginEditBlockEv')

  def joinPreviousEditBlock(self) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::joinPreviousEditBlock()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#joinPreviousEditBlock
    """
    #  void QTextDocumentPrivate::joinPreviousEditBlock()
    self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate21joinPreviousEditBlockEv',
    )

  def endEditBlock(self) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::endEditBlock()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#endEditBlock
    """
    #  void QTextDocumentPrivate::endEditBlock()
    self.uglySide.call('ritual_ZN20QTextDocumentPrivate12endEditBlockEv')

  def finishEdit(self) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::finishEdit()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#finishEdit
    """
    #  void QTextDocumentPrivate::finishEdit()
    self.uglySide.call('ritual_ZN20QTextDocumentPrivate10finishEditEv')

  @overload(bool)
  def enableUndoRedo(self, enable: bool) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::enableUndoRedo(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#enableUndoRedo

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QTextDocumentPrivate::enableUndoRedo(bool enable)
    self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate14enableUndoRedoEb', enable,
    )

  def formatCollection(self) -> Optional[QTextFormatCollection]:
    """
    Calls Qt's 'QTextFormatCollection
    *QTextDocumentPrivate::formatCollection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#formatCollection

    Returns
    -------

    Optional[QTextFormatCollection]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextFormatCollection *QTextDocumentPrivate::formatCollection()
    address = self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate16formatCollectionEv',
    )
    from . import QTextFormatCollection
    return QTextFormatCollection._cuteAt(address)

  @overload(QTextObject, int)
  @overload(NoneType, int)
  def changeObjectFormat(
      self,
      group: Optional[QTextObject],
      format: int,
  ) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::changeObjectFormat(QTextObject
    *group, int format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#changeObjectFormat

    Parameters
    ----------

    group : Optional[QTextObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    format : int
      Passed on as it is.
    """
    #  void QTextDocumentPrivate::changeObjectFormat(QTextObject *group, int
    #      format)
    self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate18changeObjectFormatEP11QTextObject'
        'i',
        self._addressOf(group), format,
    )

  @overload(QTextDocument.Stacks)
  @overload(QTextDocument.Stacks, bool)
  def clearUndoRedoStacks(
      self,
      stacksToClear: QTextDocument.Stacks,
      emitSignals: bool = False,
  ) -> None:
    """
    Calls Qt's 'void
    QTextDocumentPrivate::clearUndoRedoStacks(QTextDocument::Stacks
    stacksToClear, bool emitSignals)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#clearUndoRedoStacks

    Parameters
    ----------

    stacksToClear : QTextDocument.Stacks
      Passed on as its number.

    emitSignals : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QTextDocumentPrivate::clearUndoRedoStacks(QTextDocument::Stacks
    #      stacksToClear, bool emitSignals)
    self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate19clearUndoRedoStacksEN13QTextDocum'
        'ent6StacksEb',
        stacksToClear.value, emitSignals,
    )

  @overload(int)
  def split(self, pos: int) -> bool:
    """
    Calls Qt's 'bool QTextDocumentPrivate::split(int pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentprivate.html#split

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  bool QTextDocumentPrivate::split(int pos)
    return self.uglySide.call('ritual_ZN20QTextDocumentPrivate5splitEi', pos)

  @overload(int)
  def unite(self, f: int) -> bool:
    """
    Calls Qt's 'bool QTextDocumentPrivate::unite(uint f)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentprivate.html#unite

    Parameters
    ----------

    f : int
      Passed on as it is.
    """
    #  bool QTextDocumentPrivate::unite(uint f)
    return self.uglySide.call('ritual_ZN20QTextDocumentPrivate5uniteEj', f)

  @overload(int, int, int, int, QTextUndoCommand.Operation)
  def insert_string(
      self,
      pos: int,
      strPos: int,
      length: int,
      format: int,
      op: QTextUndoCommand.Operation,
  ) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::insert_string(int pos, uint
    strPos, uint length, int format, QTextUndoCommand::Operation op)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#insert_string

    Parameters
    ----------

    pos : int
      Passed on as it is.

    strPos : int
      Passed on as it is.

    length : int
      Passed on as it is.

    format : int
      Passed on as it is.

    op : QTextUndoCommand.Operation
      Passed on as its number.
    """
    #  void QTextDocumentPrivate::insert_string(int pos, uint strPos, uint
    #      length, int format, QTextUndoCommand::Operation op)
    self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate13insert_stringEijjiN16QTextUndoCom'
        'mand9OperationE',
        pos, strPos, length, format, op.value,
    )

  @overload(int, int, int, int, QTextUndoCommand.Operation, int)
  def insert_block(
      self,
      pos: int,
      strPos: int,
      format: int,
      blockformat: int,
      op: QTextUndoCommand.Operation,
      command: int,
  ) -> int:
    """
    Calls Qt's 'int QTextDocumentPrivate::insert_block(int pos, uint strPos,
    int format, int blockformat, QTextUndoCommand::Operation op, int
    command)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#insert_block

    Parameters
    ----------

    pos : int
      Passed on as it is.

    strPos : int
      Passed on as it is.

    format : int
      Passed on as it is.

    blockformat : int
      Passed on as it is.

    op : QTextUndoCommand.Operation
      Passed on as its number.

    command : int
      Passed on as it is.
    """
    #  int QTextDocumentPrivate::insert_block(int pos, uint strPos, int
    #      format, int blockformat, QTextUndoCommand::Operation op, int
    #      command)
    return self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate12insert_blockEijiiN16QTextUndoComm'
        'and9OperationEi',
        pos, strPos, format, blockformat, op.value, command,
    )

  @overload(int, int, QTextUndoCommand.Operation)
  def remove_string(
      self,
      pos: int,
      length: int,
      op: QTextUndoCommand.Operation,
  ) -> int:
    """
    Calls Qt's 'int QTextDocumentPrivate::remove_string(int pos, uint length,
    QTextUndoCommand::Operation op)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#remove_string

    Parameters
    ----------

    pos : int
      Passed on as it is.

    length : int
      Passed on as it is.

    op : QTextUndoCommand.Operation
      Passed on as its number.
    """
    #  int QTextDocumentPrivate::remove_string(int pos, uint length,
    #      QTextUndoCommand::Operation op)
    return self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate13remove_stringEijN16QTextUndoComma'
        'nd9OperationE',
        pos, length, op.value,
    )

  @overload(QTextFrame)
  @overload(NoneType)
  def insert_frame(self, f: Optional[QTextFrame]) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::insert_frame(QTextFrame *f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#insert_frame

    Parameters
    ----------

    f : Optional[QTextFrame]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextDocumentPrivate::insert_frame(QTextFrame *f)
    self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate12insert_frameEP10QTextFrame',
        self._addressOf(f),
    )

  @overload(int, int, int)
  def scan_frames(
      self,
      pos: int,
      charsRemoved: int,
      charsAdded: int,
  ) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::scan_frames(int pos, int
    charsRemoved, int charsAdded)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#scan_frames

    Parameters
    ----------

    pos : int
      Passed on as it is.

    charsRemoved : int
      Passed on as it is.

    charsAdded : int
      Passed on as it is.
    """
    #  void QTextDocumentPrivate::scan_frames(int pos, int charsRemoved, int
    #      charsAdded)
    self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate11scan_framesEiii',
        pos, charsRemoved, charsAdded,
    )

  @overload(int, int, QTextUndoCommand.Operation)
  def adjustDocumentChangesAndCursors(
      self,
      from_: int,
      addedOrRemoved: int,
      op: QTextUndoCommand.Operation,
  ) -> None:
    """
    Calls Qt's 'void
    QTextDocumentPrivate::adjustDocumentChangesAndCursors(int from, int
    addedOrRemoved, QTextUndoCommand::Operation op)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html

    Parameters
    ----------

    from_ : int
      Passed on as it is.

    addedOrRemoved : int
      Passed on as it is.

    op : QTextUndoCommand.Operation
      Passed on as its number.
    """
    #  void QTextDocumentPrivate::adjustDocumentChangesAndCursors(int from,
    #      int addedOrRemoved, QTextUndoCommand::Operation op)
    self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate31adjustDocumentChangesAndCursorsEi'
        'iN16QTextUndoCommand9OperationE',
        from_, addedOrRemoved, op.value,
    )

  @overload(int, int)
  def documentChange(self, from_: int, length: int) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::documentChange(int from, int
    length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#documentChange

    Parameters
    ----------

    from_ : int
      Passed on as it is.

    length : int
      Passed on as it is.
    """
    #  void QTextDocumentPrivate::documentChange(int from, int length)
    self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate14documentChangeEii', from_, length,
    )

  @overload(QTextCursorPrivate)
  @overload(NoneType)
  def addCursor(self, c: Optional[QTextCursorPrivate]) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::addCursor(QTextCursorPrivate *c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#addCursor

    Parameters
    ----------

    c : Optional[QTextCursorPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextDocumentPrivate::addCursor(QTextCursorPrivate *c)
    self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate9addCursorEP18QTextCursorPrivate',
        self._addressOf(c),
    )

  @overload(QTextCursorPrivate)
  @overload(NoneType)
  def removeCursor(self, c: Optional[QTextCursorPrivate]) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::removeCursor(QTextCursorPrivate
    *c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#removeCursor

    Parameters
    ----------

    c : Optional[QTextCursorPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextDocumentPrivate::removeCursor(QTextCursorPrivate *c)
    self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate12removeCursorEP18QTextCursorPrivat'
        'e',
        self._addressOf(c),
    )

  @overload(QTextFormat)
  @overload(QTextFormat, int)
  def createObject(
      self,
      newFormat: QTextFormat,
      objectIndex: int = -1,
  ) -> Optional[QTextObject]:
    """
    Calls Qt's 'QTextObject *QTextDocumentPrivate::createObject(const
    QTextFormat &newFormat, int objectIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#createObject

    Parameters
    ----------

    newFormat : QTextFormat
      Passed on as a value: Qt reads the C++ QTextFormat, which stays
      Python's own.

    objectIndex : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    Optional[QTextObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextObject *QTextDocumentPrivate::createObject(const QTextFormat
    #      &newFormat, int objectIndex)
    address = self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate12createObjectERK11QTextFormati',
        self._valueOf(newFormat), objectIndex,
    )
    from . import QTextObject
    return QTextObject._cuteAt(address)

  @overload(QTextObject)
  @overload(NoneType)
  def deleteObject(self, object: Optional[QTextObject]) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::deleteObject(QTextObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#deleteObject

    Parameters
    ----------

    object : Optional[QTextObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextDocumentPrivate::deleteObject(QTextObject *object)
    self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate12deleteObjectEP11QTextObject',
        self._addressOf(object),
    )

  def document(self) -> Optional[QTextDocument]:
    """
    Calls Qt's 'QTextDocument *QTextDocumentPrivate::document()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentprivate.html#document

    Returns
    -------

    Optional[QTextDocument]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextDocument *QTextDocumentPrivate::document()
    address = self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate8documentEv',
    )
    return QTextDocument._cuteAt(address)

  def ensureMaximumBlockCount(self) -> bool:
    """
    Calls Qt's 'bool QTextDocumentPrivate::ensureMaximumBlockCount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#ensureMaximumBlockCount
    """
    #  bool QTextDocumentPrivate::ensureMaximumBlockCount()
    return self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate23ensureMaximumBlockCountEv',
    )

  def contentsChanged(self) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::contentsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#contentsChanged
    """
    #  void QTextDocumentPrivate::contentsChanged()
    self.uglySide.call('ritual_ZN20QTextDocumentPrivate15contentsChangedEv')

  def compressPieceTable(self) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::compressPieceTable()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#compressPieceTable
    """
    #  void QTextDocumentPrivate::compressPieceTable()
    self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate18compressPieceTableEv',
    )

  @overload(THIS)
  @overload(NoneType)
  def mergeCachedResources(
      self,
      priv: Optional[QTextDocumentPrivate],
  ) -> None:
    """
    Calls Qt's 'void QTextDocumentPrivate::mergeCachedResources(const
    QTextDocumentPrivate *priv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentprivate.html#mergeCachedResources

    Parameters
    ----------

    priv : Optional[QTextDocumentPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextDocumentPrivate::mergeCachedResources(const
    #      QTextDocumentPrivate *priv)
    self.uglySide.call(
        'ritual_ZN20QTextDocumentPrivate20mergeCachedResourcesEPKS_',
        self._addressOf(priv),
    )

  @staticmethod
  def begin(*__, **_) -> Never:
    """
    Qt's 'FragmentIterator QTextDocumentPrivate::begin() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTextDocumentPrivate.begin' has no cute function yet. Qt's "
        "'FragmentIterator QTextDocumentPrivate::begin() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def blockMap(*__, **_) -> Never:
    """
    - Qt's 'const BlockMap &QTextDocumentPrivate::blockMap() const': gives a
      type Python has no way to take yet.
    - Qt's 'BlockMap &QTextDocumentPrivate::blockMap()': gives a type Python
      has no way to take yet.
    """
    raise NotImplementedError(
        "'QTextDocumentPrivate.blockMap' has no cute function yet. Qt's "
        "'const BlockMap &QTextDocumentPrivate::blockMap() const': gives a "
        "type Python has no way to take yet. Qt's 'BlockMap "
        "&QTextDocumentPrivate::blockMap()': gives a type Python has no way "
        "to take yet.")

  @staticmethod
  def end(*__, **_) -> Never:
    """
    Qt's 'FragmentIterator QTextDocumentPrivate::end() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTextDocumentPrivate.end' has no cute function yet. Qt's "
        "'FragmentIterator QTextDocumentPrivate::end() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def find(*__, **_) -> Never:
    """
    Qt's 'FragmentIterator QTextDocumentPrivate::find(int pos) const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTextDocumentPrivate.find' has no cute function yet. Qt's "
        "'FragmentIterator QTextDocumentPrivate::find(int pos) const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def fragmentMap(*__, **_) -> Never:
    """
    - Qt's 'const FragmentMap &QTextDocumentPrivate::fragmentMap() const':
      gives a type Python has no way to take yet.
    - Qt's 'FragmentMap &QTextDocumentPrivate::fragmentMap()': gives a type
      Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTextDocumentPrivate.fragmentMap' has no cute function yet. Qt's "
        "'const FragmentMap &QTextDocumentPrivate::fragmentMap() const': "
        "gives a type Python has no way to take yet. Qt's 'FragmentMap "
        "&QTextDocumentPrivate::fragmentMap()': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def remove_block(*__, **_) -> Never:
    """
    Qt's 'int QTextDocumentPrivate::remove_block(int pos, int *blockformat,
    int command, QTextUndoCommand::Operation op)': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QTextDocumentPrivate.remove_block' has no cute function yet. Qt's "
        "'int QTextDocumentPrivate::remove_block(int pos, int *blockformat, "
        "int command, QTextUndoCommand::Operation op)': takes a number to "
        "change where it is.")
