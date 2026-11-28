"""
QPlainTextEdit binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qplaintextedit.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QAbstractTextDocumentLayout, QTextCursor, QTextDocument
from ..QtGui import QTextOption
from . import QAbstractScrollArea, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject, QMimeData, QPoint, QPointF, QRect
  from ..QtCore import QRectF, QRegularExpression, QTimerEvent, QUrl
  from ..QtCore import QVariant
  from ..QtGui import QContextMenuEvent, QDragEnterEvent, QDragLeaveEvent
  from ..QtGui import QDragMoveEvent, QDropEvent, QFocusEvent
  from ..QtGui import QInputMethodEvent, QKeyEvent, QMouseEvent
  from ..QtGui import QPagedPaintDevice, QPaintEvent, QResizeEvent
  from ..QtGui import QShowEvent, QTextBlock, QTextCharFormat, QWheelEvent
  from . import QMenu, QPlainTextEditPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QContextMenuEvent = WAIT['QContextMenuEvent']
  QDragEnterEvent = WAIT['QDragEnterEvent']
  QDragLeaveEvent = WAIT['QDragLeaveEvent']
  QDragMoveEvent = WAIT['QDragMoveEvent']
  QDropEvent = WAIT['QDropEvent']
  QEvent = WAIT['QEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QInputMethodEvent = WAIT['QInputMethodEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QMimeData = WAIT['QMimeData']
  QMouseEvent = WAIT['QMouseEvent']
  QPagedPaintDevice = WAIT['QPagedPaintDevice']
  QPaintEvent = WAIT['QPaintEvent']
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QRegularExpression = WAIT['QRegularExpression']
  QResizeEvent = WAIT['QResizeEvent']
  QShowEvent = WAIT['QShowEvent']
  QTextBlock = WAIT['QTextBlock']
  QTextCharFormat = WAIT['QTextCharFormat']
  QTimerEvent = WAIT['QTimerEvent']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']
  QWheelEvent = WAIT['QWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlainTextEdit(QAbstractScrollArea):
  """
  The cute side of Qt's QPlainTextEdit: a plain Python object standing in
  front of one C++ QPlainTextEdit.

  It is built on the cute 'QAbstractScrollArea', as Qt's QPlainTextEdit is
  built on Qt's QAbstractScrollArea, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlainTextEdit that has a ritual and that Python can
  call so far, 107 names in all: 'metaObject', 'tr', 'd_func', 'setDocument',
  'document', 'setPlaceholderText', 'placeholderText', 'setTextCursor',
  'textCursor', 'isReadOnly', 'setReadOnly', 'setTextInteractionFlags',
  'textInteractionFlags', 'mergeCurrentCharFormat', 'setCurrentCharFormat',
  'currentCharFormat', 'tabChangesFocus', 'setTabChangesFocus',
  'setDocumentTitle', 'documentTitle', 'isUndoRedoEnabled',
  'setUndoRedoEnabled', 'setMaximumBlockCount', 'maximumBlockCount',
  'lineWrapMode', 'setLineWrapMode', 'wordWrapMode', 'setWordWrapMode',
  'setBackgroundVisible', 'backgroundVisible', 'setCenterOnScroll',
  'centerOnScroll', 'find', 'toPlainText', 'ensureCursorVisible',
  'loadResource', 'createStandardContextMenu', 'cursorForPosition',
  'cursorRect', 'anchorAt', 'overwriteMode', 'setOverwriteMode',
  'tabStopDistance', 'setTabStopDistance', 'cursorWidth', 'setCursorWidth',
  'moveCursor', 'canPaste', 'print', 'blockCount', 'inputMethodQuery',
  'setPlainText', 'cut', 'copy', 'paste', 'undo', 'redo', 'clear',
  'selectAll', 'insertPlainText', 'appendPlainText', 'appendHtml',
  'centerCursor', 'zoomIn', 'zoomOut', 'textChanged', 'undoAvailable',
  'redoAvailable', 'copyAvailable', 'selectionChanged',
  'cursorPositionChanged', 'updateRequest', 'blockCountChanged',
  'modificationChanged', 'event', 'timerEvent', 'keyPressEvent',
  'keyReleaseEvent', 'resizeEvent', 'paintEvent', 'mousePressEvent',
  'mouseMoveEvent', 'mouseReleaseEvent', 'mouseDoubleClickEvent',
  'focusNextPrevChild', 'contextMenuEvent', 'dragEnterEvent',
  'dragLeaveEvent', 'dragMoveEvent', 'dropEvent', 'focusInEvent',
  'focusOutEvent', 'showEvent', 'changeEvent', 'wheelEvent',
  'createMimeDataFromSelection', 'canInsertFromMimeData',
  'insertFromMimeData', 'inputMethodEvent', 'scrollContentsBy',
  'doSetTextCursor', 'firstVisibleBlock', 'contentOffset',
  'blockBoundingRect', 'blockBoundingGeometry', 'getPaintContext', 'zoomInF'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlainTextEdit::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QPlainTextEdit::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QPlainTextEditPrivate *QPlainTextEdit::d_func() const': takes
    in Python what 'QPlainTextEditPrivate *QPlainTextEdit::d_func()' takes.
  - Qt's 'QPlainTextEdit::~QPlainTextEdit()': the destructor: Python never
    removes a C++ QPlainTextEdit.
  - Qt's 'void QPlainTextEdit::setExtraSelections(const
    QList<QTextEdit::ExtraSelection> &selections)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QList<QTextEdit::ExtraSelection> QPlainTextEdit::extraSelections()
    const': gives a type Python has no way to take yet.
  - Qt's 'QPlainTextEdit::QPlainTextEdit(QPlainTextEditPrivate &dd, QWidget
    *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 124 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QPlainTextEdit is created at the first use, not by
    'QPlainTextEdit(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlainTextEdit.
  - Qt tells when it has removed the C++ QPlainTextEdit. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QPlainTextEdit that has no cute function yet,
    'extraSelections', 'setExtraSelections', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QPlainTextEdit, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class LineWrapMode(CuteNum):
    """
    The enum 'QPlainTextEdit::LineWrapMode' of Qt, with the 2 names Qt gives
    in it.
    """

    NoWrap = Kee[int](0)
    WidgetWidth = Kee[int](1)

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
    Calls Qt's 'QString QPlainTextEdit::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#tr

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
    #  QString QPlainTextEdit::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QPlainTextEdit2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlainTextEdit'

  #  A C++ QPlainTextEdit Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlainTextEdit'

  #  The functions Qt calls itself that QPlainTextEdit is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'loadResource': (
          ('_ZN14QPlainTextEdit12loadResourceEiRK4QUrl',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QUrl'),
           )),
      ),
      'createMimeDataFromSelection': (
          ('_ZNK14QPlainTextEdit27createMimeDataFromSelectionEv',
           ('address', 'address', 'QtCore:QMimeData'),
           ()),
      ),
      'canInsertFromMimeData': (
          ('_ZNK14QPlainTextEdit21canInsertFromMimeDataEPK9QMimeData',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCore:QMimeData'),
           )),
      ),
      'insertFromMimeData': (
          ('_ZN14QPlainTextEdit18insertFromMimeDataEPK9QMimeData',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QMimeData'),
           )),
      ),
      'doSetTextCursor': (
          ('_ZN14QPlainTextEdit15doSetTextCursorERK11QTextCursor',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QTextCursor'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPlainTextEdit::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlainTextEdit::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QPlainTextEdit10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def document(self) -> Optional[QTextDocument]:
    """
    Calls Qt's 'QTextDocument *QPlainTextEdit::document() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#document

    Returns
    -------

    Optional[QTextDocument]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextDocument *QPlainTextEdit::document() const
    address = self.uglySide.call('ritual_ZNK14QPlainTextEdit8documentEv')
    return QTextDocument._cuteAt(address)

  def placeholderText(self) -> str:
    """
    Calls Qt's 'QString QPlainTextEdit::placeholderText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#placeholderText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlainTextEdit::placeholderText() const
    return self.uglySide.call(
        'ritual_ZNK14QPlainTextEdit15placeholderTextEv',
    )

  def textCursor(self) -> QTextCursor:
    """
    Calls Qt's 'QTextCursor QPlainTextEdit::textCursor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#textCursor

    Returns
    -------

    QTextCursor
      A new cute QTextCursor around the copy Qt gave back. Python owns it.
    """
    #  QTextCursor QPlainTextEdit::textCursor() const
    address = self.uglySide.call('ritual_ZNK14QPlainTextEdit10textCursorEv')
    return QTextCursor._cuteOwning(address)

  def isReadOnly(self) -> bool:
    """
    Calls Qt's 'bool QPlainTextEdit::isReadOnly() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#isReadOnly
    """
    #  bool QPlainTextEdit::isReadOnly() const
    return self.uglySide.call('ritual_ZNK14QPlainTextEdit10isReadOnlyEv')

  def textInteractionFlags(self) -> Qt.TextInteractionFlags:
    """
    Calls Qt's 'Qt::TextInteractionFlags
    QPlainTextEdit::textInteractionFlags() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#textInteractionFlags

    Returns
    -------

    Qt.TextInteractionFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::TextInteractionFlags QPlainTextEdit::textInteractionFlags() const
    return Qt.TextInteractionFlags(self.uglySide.call(
        'ritual_ZNK14QPlainTextEdit20textInteractionFlagsEv',
    ))

  def currentCharFormat(self) -> QTextCharFormat:
    """
    Calls Qt's 'QTextCharFormat QPlainTextEdit::currentCharFormat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#currentCharFormat

    Returns
    -------

    QTextCharFormat
      A new cute QTextCharFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextCharFormat QPlainTextEdit::currentCharFormat() const
    address = self.uglySide.call(
        'ritual_ZNK14QPlainTextEdit17currentCharFormatEv',
    )
    from ..QtGui import QTextCharFormat
    return QTextCharFormat._cuteOwning(address)

  def tabChangesFocus(self) -> bool:
    """
    Calls Qt's 'bool QPlainTextEdit::tabChangesFocus() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#tabChangesFocus
    """
    #  bool QPlainTextEdit::tabChangesFocus() const
    return self.uglySide.call(
        'ritual_ZNK14QPlainTextEdit15tabChangesFocusEv',
    )

  def documentTitle(self) -> str:
    """
    Calls Qt's 'QString QPlainTextEdit::documentTitle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#documentTitle

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlainTextEdit::documentTitle() const
    return self.uglySide.call('ritual_ZNK14QPlainTextEdit13documentTitleEv')

  def isUndoRedoEnabled(self) -> bool:
    """
    Calls Qt's 'bool QPlainTextEdit::isUndoRedoEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#isUndoRedoEnabled
    """
    #  bool QPlainTextEdit::isUndoRedoEnabled() const
    return self.uglySide.call(
        'ritual_ZNK14QPlainTextEdit17isUndoRedoEnabledEv',
    )

  def maximumBlockCount(self) -> int:
    """
    Calls Qt's 'int QPlainTextEdit::maximumBlockCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#maximumBlockCount
    """
    #  int QPlainTextEdit::maximumBlockCount() const
    return self.uglySide.call(
        'ritual_ZNK14QPlainTextEdit17maximumBlockCountEv',
    )

  def lineWrapMode(self) -> LineWrapMode:
    """
    Calls Qt's 'LineWrapMode QPlainTextEdit::lineWrapMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#lineWrapMode

    Returns
    -------

    LineWrapMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'LineWrapMode(number)'
      gives.
    """
    #  LineWrapMode QPlainTextEdit::lineWrapMode() const
    return QPlainTextEdit.LineWrapMode(self.uglySide.call(
        'ritual_ZNK14QPlainTextEdit12lineWrapModeEv',
    ))

  def wordWrapMode(self) -> QTextOption.WrapMode:
    """
    Calls Qt's 'QTextOption::WrapMode QPlainTextEdit::wordWrapMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#wordWrapMode

    Returns
    -------

    QTextOption.WrapMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QTextOption.WrapMode(number)' gives.
    """
    #  QTextOption::WrapMode QPlainTextEdit::wordWrapMode() const
    return QTextOption.WrapMode(self.uglySide.call(
        'ritual_ZNK14QPlainTextEdit12wordWrapModeEv',
    ))

  def backgroundVisible(self) -> bool:
    """
    Calls Qt's 'bool QPlainTextEdit::backgroundVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#backgroundVisible
    """
    #  bool QPlainTextEdit::backgroundVisible() const
    return self.uglySide.call(
        'ritual_ZNK14QPlainTextEdit17backgroundVisibleEv',
    )

  def centerOnScroll(self) -> bool:
    """
    Calls Qt's 'bool QPlainTextEdit::centerOnScroll() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#centerOnScroll
    """
    #  bool QPlainTextEdit::centerOnScroll() const
    return self.uglySide.call('ritual_ZNK14QPlainTextEdit14centerOnScrollEv')

  def toPlainText(self) -> str:
    """
    Calls Qt's 'QString QPlainTextEdit::toPlainText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#toPlainText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlainTextEdit::toPlainText() const
    return self.uglySide.call('ritual_ZNK14QPlainTextEdit11toPlainTextEv')

  @overload(QPoint)
  def cursorForPosition(self, pos: QPoint) -> QTextCursor:
    """
    Calls Qt's 'QTextCursor QPlainTextEdit::cursorForPosition(const QPoint
    &pos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#cursorForPosition

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QTextCursor
      A new cute QTextCursor around the copy Qt gave back. Python owns it.
    """
    #  QTextCursor QPlainTextEdit::cursorForPosition(const QPoint &pos) const
    address = self.uglySide.call(
        'ritual_ZNK14QPlainTextEdit17cursorForPositionERK6QPoint',
        self._valueOf(pos),
    )
    return QTextCursor._cuteOwning(address)

  @overload(QTextCursor)
  def cursorRect(self, cursor: QTextCursor) -> QRect:
    """
    Calls Qt's 'QRect QPlainTextEdit::cursorRect(const QTextCursor &cursor)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#cursorRect

    Parameters
    ----------

    cursor : QTextCursor
      Passed on as a value: Qt reads the C++ QTextCursor, which stays
      Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QPlainTextEdit::cursorRect(const QTextCursor &cursor) const
    address = self.uglySide.call(
        'ritual_ZNK14QPlainTextEdit10cursorRectERK11QTextCursor',
        self._valueOf(cursor),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload()
  def cursorRect(self) -> QRect:
    """
    Calls Qt's 'QRect QPlainTextEdit::cursorRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#cursorRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QPlainTextEdit::cursorRect() const
    address = self.uglySide.call('ritual_ZNK14QPlainTextEdit10cursorRectEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QPoint)
  def anchorAt(self, pos: QPoint) -> str:
    """
    Calls Qt's 'QString QPlainTextEdit::anchorAt(const QPoint &pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#anchorAt

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlainTextEdit::anchorAt(const QPoint &pos) const
    return self.uglySide.call(
        'ritual_ZNK14QPlainTextEdit8anchorAtERK6QPoint', self._valueOf(pos),
    )

  def overwriteMode(self) -> bool:
    """
    Calls Qt's 'bool QPlainTextEdit::overwriteMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#overwriteMode
    """
    #  bool QPlainTextEdit::overwriteMode() const
    return self.uglySide.call('ritual_ZNK14QPlainTextEdit13overwriteModeEv')

  def tabStopDistance(self) -> float:
    """
    Calls Qt's 'qreal QPlainTextEdit::tabStopDistance() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#tabStopDistance
    """
    #  qreal QPlainTextEdit::tabStopDistance() const
    return self.uglySide.call(
        'ritual_ZNK14QPlainTextEdit15tabStopDistanceEv',
    )

  def cursorWidth(self) -> int:
    """
    Calls Qt's 'int QPlainTextEdit::cursorWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#cursorWidth
    """
    #  int QPlainTextEdit::cursorWidth() const
    return self.uglySide.call('ritual_ZNK14QPlainTextEdit11cursorWidthEv')

  def canPaste(self) -> bool:
    """
    Calls Qt's 'bool QPlainTextEdit::canPaste() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#canPaste
    """
    #  bool QPlainTextEdit::canPaste() const
    return self.uglySide.call('ritual_ZNK14QPlainTextEdit8canPasteEv')

  def blockCount(self) -> int:
    """
    Calls Qt's 'int QPlainTextEdit::blockCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#blockCount
    """
    #  int QPlainTextEdit::blockCount() const
    return self.uglySide.call('ritual_ZNK14QPlainTextEdit10blockCountEv')

  @overload(Qt.InputMethodQuery)
  def inputMethodQuery(self, property: Qt.InputMethodQuery) -> QVariant:
    """
    Calls Qt's 'QVariant
    QPlainTextEdit::inputMethodQuery(Qt::InputMethodQuery property) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#inputMethodQuery

    Parameters
    ----------

    property : Qt.InputMethodQuery
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QPlainTextEdit::inputMethodQuery(Qt::InputMethodQuery
    #      property) const
    ritual = (
        'ritual_ZNK14QPlainTextEdit16inputMethodQueryEN2Qt16InputMethodQuer'
        'yE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QPlainTextEdit16inputMethodQueryEN2Qt16InputMeth'
          'odQueryE')
    address = self.uglySide.call(ritual, property.value)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(Qt.InputMethodQuery, QVariant)
  def inputMethodQuery(
      self,
      query: Qt.InputMethodQuery,
      argument: QVariant,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant
    QPlainTextEdit::inputMethodQuery(Qt::InputMethodQuery query, QVariant
    argument) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#inputMethodQuery

    Parameters
    ----------

    query : Qt.InputMethodQuery
      Passed on as its number.

    argument : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QPlainTextEdit::inputMethodQuery(Qt::InputMethodQuery query,
    #      QVariant argument) const
    address = self.uglySide.call(
        'ritual_ZNK14QPlainTextEdit16inputMethodQueryEN2Qt16InputMethodQuer'
        'yE8QVariant',
        query.value, self._valueOf(argument),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def createMimeDataFromSelection(self) -> Optional[QMimeData]:
    """
    Calls Qt's 'QMimeData *QPlainTextEdit::createMimeDataFromSelection()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#createMimeDataFromSelection

    Returns
    -------

    Optional[QMimeData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMimeData *QPlainTextEdit::createMimeDataFromSelection() const
    ritual = 'ritual_ZNK14QPlainTextEdit27createMimeDataFromSelectionEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QPlainTextEdit27createMimeDataFromSelectionEv')
    address = self.uglySide.call(ritual)
    from ..QtCore import QMimeData
    return QMimeData._cuteAt(address)

  @overload(QMimeData)
  @overload(NoneType)
  def canInsertFromMimeData(self, source: Optional[QMimeData]) -> bool:
    """
    Calls Qt's 'bool QPlainTextEdit::canInsertFromMimeData(const QMimeData
    *source) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#canInsertFromMimeData

    Parameters
    ----------

    source : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPlainTextEdit::canInsertFromMimeData(const QMimeData *source)
    #      const
    ritual = 'ritual_ZNK14QPlainTextEdit21canInsertFromMimeDataEPK9QMimeData'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QPlainTextEdit21canInsertFromMimeDataEPK9QMimeDa'
          'ta')
    return self.uglySide.call(ritual, self._addressOf(source))

  def firstVisibleBlock(self) -> QTextBlock:
    """
    Calls Qt's 'QTextBlock QPlainTextEdit::firstVisibleBlock() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#firstVisibleBlock

    Returns
    -------

    QTextBlock
      A new cute QTextBlock around the copy Qt gave back. Python owns it.
    """
    #  QTextBlock QPlainTextEdit::firstVisibleBlock() const
    address = self.uglySide.call(
        'ritual_ZNK14QPlainTextEdit17firstVisibleBlockEv',
    )
    from ..QtGui import QTextBlock
    return QTextBlock._cuteOwning(address)

  def contentOffset(self) -> QPointF:
    """
    Calls Qt's 'QPointF QPlainTextEdit::contentOffset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#contentOffset

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QPlainTextEdit::contentOffset() const
    address = self.uglySide.call(
        'ritual_ZNK14QPlainTextEdit13contentOffsetEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QTextBlock)
  def blockBoundingRect(self, block: QTextBlock) -> QRectF:
    """
    Calls Qt's 'QRectF QPlainTextEdit::blockBoundingRect(const QTextBlock
    &block) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#blockBoundingRect

    Parameters
    ----------

    block : QTextBlock
      Passed on as a value: Qt reads the C++ QTextBlock, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QPlainTextEdit::blockBoundingRect(const QTextBlock &block)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK14QPlainTextEdit17blockBoundingRectERK10QTextBlock',
        self._valueOf(block),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QTextBlock)
  def blockBoundingGeometry(self, block: QTextBlock) -> QRectF:
    """
    Calls Qt's 'QRectF QPlainTextEdit::blockBoundingGeometry(const QTextBlock
    &block) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#blockBoundingGeometry

    Parameters
    ----------

    block : QTextBlock
      Passed on as a value: Qt reads the C++ QTextBlock, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QPlainTextEdit::blockBoundingGeometry(const QTextBlock &block)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK14QPlainTextEdit21blockBoundingGeometryERK10QTextBlock',
        self._valueOf(block),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def getPaintContext(self) -> QAbstractTextDocumentLayout.PaintContext:
    """
    Calls Qt's 'QAbstractTextDocumentLayout::PaintContext
    QPlainTextEdit::getPaintContext() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#getPaintContext

    Returns
    -------

    QAbstractTextDocumentLayout.PaintContext
      A new cute QAbstractTextDocumentLayout::PaintContext around the copy Qt
      gave back. Python owns it.
    """
    #  QAbstractTextDocumentLayout::PaintContext
    #      QPlainTextEdit::getPaintContext() const
    address = self.uglySide.call(
        'ritual_ZNK14QPlainTextEdit15getPaintContextEv',
    )
    return QAbstractTextDocumentLayout.PaintContext._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QTextDocument)
  @overload(NoneType)
  def setDocument(self, document: Optional[QTextDocument]) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::setDocument(QTextDocument *document)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#setDocument

    Parameters
    ----------

    document : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlainTextEdit::setDocument(QTextDocument *document)
    self.uglySide.call(
        'ritual_ZN14QPlainTextEdit11setDocumentEP13QTextDocument',
        self._addressOf(document),
    )

  @overload(str)
  def setPlaceholderText(self, placeholderText: str) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::setPlaceholderText(const QString
    &placeholderText)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#setPlaceholderText

    Parameters
    ----------

    placeholderText : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlainTextEdit::setPlaceholderText(const QString
    #      &placeholderText)
    self.uglySide.call(
        'ritual_ZN14QPlainTextEdit18setPlaceholderTextERK7QString',
        placeholderText,
    )

  @overload(QTextCursor)
  def setTextCursor(self, cursor: QTextCursor) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::setTextCursor(const QTextCursor
    &cursor)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#setTextCursor

    Parameters
    ----------

    cursor : QTextCursor
      Passed on as a value: Qt reads the C++ QTextCursor, which stays
      Python's own.
    """
    #  void QPlainTextEdit::setTextCursor(const QTextCursor &cursor)
    self.uglySide.call(
        'ritual_ZN14QPlainTextEdit13setTextCursorERK11QTextCursor',
        self._valueOf(cursor),
    )

  @overload(bool)
  def setReadOnly(self, ro: bool) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::setReadOnly(bool ro)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#setReadOnly

    Parameters
    ----------

    ro : bool
      Passed on as it is.
    """
    #  void QPlainTextEdit::setReadOnly(bool ro)
    self.uglySide.call('ritual_ZN14QPlainTextEdit11setReadOnlyEb', ro)

  @overload(Qt.TextInteractionFlags)
  def setTextInteractionFlags(self, flags: Qt.TextInteractionFlags) -> None:
    """
    Calls Qt's 'void
    QPlainTextEdit::setTextInteractionFlags(Qt::TextInteractionFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#setTextInteractionFlags

    Parameters
    ----------

    flags : Qt.TextInteractionFlags
      Passed on as its number.
    """
    #  void QPlainTextEdit::setTextInteractionFlags(Qt::TextInteractionFlags
    #      flags)
    self.uglySide.call(
        'ritual_ZN14QPlainTextEdit23setTextInteractionFlagsE6QFlagsIN2Qt19T'
        'extInteractionFlagEE',
        flags.value,
    )

  @overload(QTextCharFormat)
  def setCurrentCharFormat(self, format: QTextCharFormat) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::setCurrentCharFormat(const
    QTextCharFormat &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#setCurrentCharFormat

    Parameters
    ----------

    format : QTextCharFormat
      Passed on as a value: Qt reads the C++ QTextCharFormat, which stays
      Python's own.
    """
    #  void QPlainTextEdit::setCurrentCharFormat(const QTextCharFormat
    #      &format)
    self.uglySide.call(
        'ritual_ZN14QPlainTextEdit20setCurrentCharFormatERK15QTextCharForma'
        't',
        self._valueOf(format),
    )

  @overload(bool)
  def setTabChangesFocus(self, b: bool) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::setTabChangesFocus(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#setTabChangesFocus

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QPlainTextEdit::setTabChangesFocus(bool b)
    self.uglySide.call('ritual_ZN14QPlainTextEdit18setTabChangesFocusEb', b)

  @overload(str)
  def setDocumentTitle(self, title: str) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::setDocumentTitle(const QString &title)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#setDocumentTitle

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlainTextEdit::setDocumentTitle(const QString &title)
    self.uglySide.call(
        'ritual_ZN14QPlainTextEdit16setDocumentTitleERK7QString', title,
    )

  @overload(bool)
  def setUndoRedoEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::setUndoRedoEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#setUndoRedoEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QPlainTextEdit::setUndoRedoEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN14QPlainTextEdit18setUndoRedoEnabledEb', enable,
    )

  @overload(int)
  def setMaximumBlockCount(self, maximum: int) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::setMaximumBlockCount(int maximum)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#setMaximumBlockCount

    Parameters
    ----------

    maximum : int
      Passed on as it is.
    """
    #  void QPlainTextEdit::setMaximumBlockCount(int maximum)
    self.uglySide.call(
        'ritual_ZN14QPlainTextEdit20setMaximumBlockCountEi', maximum,
    )

  @overload(LineWrapMode)
  def setLineWrapMode(self, mode: LineWrapMode) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::setLineWrapMode(LineWrapMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#setLineWrapMode

    Parameters
    ----------

    mode : LineWrapMode
      Passed on as its number.
    """
    #  void QPlainTextEdit::setLineWrapMode(LineWrapMode mode)
    self.uglySide.call(
        'ritual_ZN14QPlainTextEdit15setLineWrapModeENS_12LineWrapModeE',
        mode.value,
    )

  @overload(QTextOption.WrapMode)
  def setWordWrapMode(self, policy: QTextOption.WrapMode) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::setWordWrapMode(QTextOption::WrapMode
    policy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#setWordWrapMode

    Parameters
    ----------

    policy : QTextOption.WrapMode
      Passed on as its number.
    """
    #  void QPlainTextEdit::setWordWrapMode(QTextOption::WrapMode policy)
    self.uglySide.call(
        'ritual_ZN14QPlainTextEdit15setWordWrapModeEN11QTextOption8WrapMode'
        'E',
        policy.value,
    )

  @overload(bool)
  def setBackgroundVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::setBackgroundVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#setBackgroundVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QPlainTextEdit::setBackgroundVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN14QPlainTextEdit20setBackgroundVisibleEb', visible,
    )

  @overload(bool)
  def setCenterOnScroll(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::setCenterOnScroll(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#setCenterOnScroll

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QPlainTextEdit::setCenterOnScroll(bool enabled)
    self.uglySide.call(
        'ritual_ZN14QPlainTextEdit17setCenterOnScrollEb', enabled,
    )

  @overload(bool)
  def setOverwriteMode(self, overwrite: bool) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::setOverwriteMode(bool overwrite)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#setOverwriteMode

    Parameters
    ----------

    overwrite : bool
      Passed on as it is.
    """
    #  void QPlainTextEdit::setOverwriteMode(bool overwrite)
    self.uglySide.call(
        'ritual_ZN14QPlainTextEdit16setOverwriteModeEb', overwrite,
    )

  @overload(float)
  def setTabStopDistance(self, distance: float) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::setTabStopDistance(qreal distance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#setTabStopDistance

    Parameters
    ----------

    distance : float
      Passed on as it is.
    """
    #  void QPlainTextEdit::setTabStopDistance(qreal distance)
    self.uglySide.call(
        'ritual_ZN14QPlainTextEdit18setTabStopDistanceEd', distance,
    )

  @overload(int)
  def setCursorWidth(self, width: int) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::setCursorWidth(int width)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#setCursorWidth

    Parameters
    ----------

    width : int
      Passed on as it is.
    """
    #  void QPlainTextEdit::setCursorWidth(int width)
    self.uglySide.call('ritual_ZN14QPlainTextEdit14setCursorWidthEi', width)

  @overload(str)
  def setPlainText(self, text: str) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::setPlainText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#setPlainText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlainTextEdit::setPlainText(const QString &text)
    self.uglySide.call(
        'ritual_ZN14QPlainTextEdit12setPlainTextERK7QString', text,
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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QPlainTextEdit::QPlainTextEdit(QWidget
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#QPlainTextEdit

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPlainTextEdit::QPlainTextEdit(QWidget *parent)
    self._noteCreation(QPlainTextEdit, lambda: Rituals.call(
        'ritual_ZN14QPlainTextEditC1EP7QWidget', self._addressOf(parent),
    ))

  @overload(str)
  @overload(str, QWidget)
  @overload(str, NoneType)
  def __init__(self, text: str, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QPlainTextEdit::QPlainTextEdit(const
    QString &text, QWidget *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#QPlainTextEdit

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPlainTextEdit::QPlainTextEdit(const QString &text, QWidget *parent)
    self._noteCreation(QPlainTextEdit, lambda: Rituals.call(
        'ritual_ZN14QPlainTextEditC1ERK7QStringP7QWidget',
        text, self._addressOf(parent),
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

  def d_func(self) -> Optional[QPlainTextEditPrivate]:
    """
    Calls Qt's 'QPlainTextEditPrivate *QPlainTextEdit::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#d_func

    Returns
    -------

    Optional[QPlainTextEditPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlainTextEditPrivate *QPlainTextEdit::d_func()
    address = self.uglySide.call('ritual_ZN14QPlainTextEdit6d_funcEv')
    from . import QPlainTextEditPrivate
    return QPlainTextEditPrivate._cuteAt(address)

  @overload(QTextCharFormat)
  def mergeCurrentCharFormat(self, modifier: QTextCharFormat) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::mergeCurrentCharFormat(const
    QTextCharFormat &modifier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#mergeCurrentCharFormat

    Parameters
    ----------

    modifier : QTextCharFormat
      Passed on as a value: Qt reads the C++ QTextCharFormat, which stays
      Python's own.
    """
    #  void QPlainTextEdit::mergeCurrentCharFormat(const QTextCharFormat
    #      &modifier)
    self.uglySide.call(
        'ritual_ZN14QPlainTextEdit22mergeCurrentCharFormatERK15QTextCharFor'
        'mat',
        self._valueOf(modifier),
    )

  @overload(str)
  @overload(str, QTextDocument.FindFlags)
  def find(
      self,
      exp: str,
      options: QTextDocument.FindFlags = QTextDocument.FindFlags(),
  ) -> bool:
    """
    Calls Qt's 'bool QPlainTextEdit::find(const QString &exp,
    QTextDocument::FindFlags options)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#find

    Parameters
    ----------

    exp : str
      Passed on as it is: a QString is made of it for the call.

    options : QTextDocument.FindFlags
      Passed on as its number. May be left out, as in Qt: it is then
      QTextDocument.FindFlags().
    """
    #  bool QPlainTextEdit::find(const QString &exp, QTextDocument::FindFlags
    #      options)
    return self.uglySide.call(
        'ritual_ZN14QPlainTextEdit4findERK7QString6QFlagsIN13QTextDocument8'
        'FindFlagEE',
        exp, options.value,
    )

  @overload(QRegularExpression)
  @overload(QRegularExpression, QTextDocument.FindFlags)
  def find(
      self,
      exp: QRegularExpression,
      options: QTextDocument.FindFlags = QTextDocument.FindFlags(),
  ) -> bool:
    """
    Calls Qt's 'bool QPlainTextEdit::find(const QRegularExpression &exp,
    QTextDocument::FindFlags options)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#find

    Parameters
    ----------

    exp : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.

    options : QTextDocument.FindFlags
      Passed on as its number. May be left out, as in Qt: it is then
      QTextDocument.FindFlags().
    """
    #  bool QPlainTextEdit::find(const QRegularExpression &exp,
    #      QTextDocument::FindFlags options)
    return self.uglySide.call(
        'ritual_ZN14QPlainTextEdit4findERK18QRegularExpression6QFlagsIN13QT'
        'extDocument8FindFlagEE',
        self._valueOf(exp), options.value,
    )

  def ensureCursorVisible(self) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::ensureCursorVisible()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#ensureCursorVisible
    """
    #  void QPlainTextEdit::ensureCursorVisible()
    self.uglySide.call('ritual_ZN14QPlainTextEdit19ensureCursorVisibleEv')

  @overload(int, QUrl)
  def loadResource(self, type: int, name: QUrl) -> QVariant:
    """
    Calls Qt's 'QVariant QPlainTextEdit::loadResource(int type, const QUrl
    &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#loadResource

    Parameters
    ----------

    type : int
      Passed on as it is.

    name : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QPlainTextEdit::loadResource(int type, const QUrl &name)
    ritual = 'ritual_ZN14QPlainTextEdit12loadResourceEiRK4QUrl'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPlainTextEdit12loadResourceEiRK4QUrl'
    address = self.uglySide.call(ritual, type, self._valueOf(name))
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload()
  def createStandardContextMenu(self) -> Optional[QMenu]:
    """
    Calls Qt's 'QMenu *QPlainTextEdit::createStandardContextMenu()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#createStandardContextMenu

    Returns
    -------

    Optional[QMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenu *QPlainTextEdit::createStandardContextMenu()
    address = self.uglySide.call(
        'ritual_ZN14QPlainTextEdit25createStandardContextMenuEv',
    )
    from . import QMenu
    return QMenu._cuteAt(address)

  @overload(QPoint)
  def createStandardContextMenu(self, position: QPoint) -> Optional[QMenu]:
    """
    Calls Qt's 'QMenu *QPlainTextEdit::createStandardContextMenu(const QPoint
    &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#createStandardContextMenu

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    Optional[QMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenu *QPlainTextEdit::createStandardContextMenu(const QPoint
    #      &position)
    address = self.uglySide.call(
        'ritual_ZN14QPlainTextEdit25createStandardContextMenuERK6QPoint',
        self._valueOf(position),
    )
    from . import QMenu
    return QMenu._cuteAt(address)

  @overload(QTextCursor.MoveOperation)
  @overload(QTextCursor.MoveOperation, QTextCursor.MoveMode)
  def moveCursor(
      self,
      operation: QTextCursor.MoveOperation,
      mode: QTextCursor.MoveMode = QTextCursor.MoveMode.MoveAnchor,
  ) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::moveCursor(QTextCursor::MoveOperation
    operation, QTextCursor::MoveMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#moveCursor

    Parameters
    ----------

    operation : QTextCursor.MoveOperation
      Passed on as its number.

    mode : QTextCursor.MoveMode
      Passed on as its number. May be left out, as in Qt: it is then
      QTextCursor.MoveMode.MoveAnchor.
    """
    #  void QPlainTextEdit::moveCursor(QTextCursor::MoveOperation operation,
    #      QTextCursor::MoveMode mode)
    self.uglySide.call(
        'ritual_ZN14QPlainTextEdit10moveCursorEN11QTextCursor13MoveOperatio'
        'nENS0_8MoveModeE',
        operation.value, mode.value,
    )

  @overload(QPagedPaintDevice)
  @overload(NoneType)
  def print(self, printer: Optional[QPagedPaintDevice]) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::print(QPagedPaintDevice *printer)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#print

    Parameters
    ----------

    printer : Optional[QPagedPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlainTextEdit::print(QPagedPaintDevice *printer) const
    self.uglySide.call(
        'ritual_ZNK14QPlainTextEdit5printEP17QPagedPaintDevice',
        self._addressOf(printer, 'QPagedPaintDevice'),
    )

  def cut(self) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::cut()'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#cut
    """
    #  void QPlainTextEdit::cut()
    self.uglySide.call('ritual_ZN14QPlainTextEdit3cutEv')

  def copy(self) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::copy()'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#copy
    """
    #  void QPlainTextEdit::copy()
    self.uglySide.call('ritual_ZN14QPlainTextEdit4copyEv')

  def paste(self) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::paste()'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#paste
    """
    #  void QPlainTextEdit::paste()
    self.uglySide.call('ritual_ZN14QPlainTextEdit5pasteEv')

  def undo(self) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::undo()'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#undo
    """
    #  void QPlainTextEdit::undo()
    self.uglySide.call('ritual_ZN14QPlainTextEdit4undoEv')

  def redo(self) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::redo()'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#redo
    """
    #  void QPlainTextEdit::redo()
    self.uglySide.call('ritual_ZN14QPlainTextEdit4redoEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#clear
    """
    #  void QPlainTextEdit::clear()
    self.uglySide.call('ritual_ZN14QPlainTextEdit5clearEv')

  def selectAll(self) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::selectAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#selectAll
    """
    #  void QPlainTextEdit::selectAll()
    self.uglySide.call('ritual_ZN14QPlainTextEdit9selectAllEv')

  @overload(str)
  def insertPlainText(self, text: str) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::insertPlainText(const QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#insertPlainText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlainTextEdit::insertPlainText(const QString &text)
    self.uglySide.call(
        'ritual_ZN14QPlainTextEdit15insertPlainTextERK7QString', text,
    )

  @overload(str)
  def appendPlainText(self, text: str) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::appendPlainText(const QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#appendPlainText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlainTextEdit::appendPlainText(const QString &text)
    self.uglySide.call(
        'ritual_ZN14QPlainTextEdit15appendPlainTextERK7QString', text,
    )

  @overload(str)
  def appendHtml(self, html: str) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::appendHtml(const QString &html)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#appendHtml

    Parameters
    ----------

    html : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlainTextEdit::appendHtml(const QString &html)
    self.uglySide.call(
        'ritual_ZN14QPlainTextEdit10appendHtmlERK7QString', html,
    )

  def centerCursor(self) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::centerCursor()'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#centerCursor
    """
    #  void QPlainTextEdit::centerCursor()
    self.uglySide.call('ritual_ZN14QPlainTextEdit12centerCursorEv')

  @overload()
  @overload(int)
  def zoomIn(self, range: int = 1) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::zoomIn(int range)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#zoomIn

    Parameters
    ----------

    range : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void QPlainTextEdit::zoomIn(int range)
    self.uglySide.call('ritual_ZN14QPlainTextEdit6zoomInEi', range)

  @overload()
  @overload(int)
  def zoomOut(self, range: int = 1) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::zoomOut(int range)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#zoomOut

    Parameters
    ----------

    range : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void QPlainTextEdit::zoomOut(int range)
    self.uglySide.call('ritual_ZN14QPlainTextEdit7zoomOutEi', range)

  def textChanged(self) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::textChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#textChanged
    """
    #  void QPlainTextEdit::textChanged()
    self.uglySide.call('ritual_ZN14QPlainTextEdit11textChangedEv')

  @overload(bool)
  def undoAvailable(self, b: bool) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::undoAvailable(bool b)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#undoAvailable

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QPlainTextEdit::undoAvailable(bool b)
    self.uglySide.call('ritual_ZN14QPlainTextEdit13undoAvailableEb', b)

  @overload(bool)
  def redoAvailable(self, b: bool) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::redoAvailable(bool b)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#redoAvailable

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QPlainTextEdit::redoAvailable(bool b)
    self.uglySide.call('ritual_ZN14QPlainTextEdit13redoAvailableEb', b)

  @overload(bool)
  def copyAvailable(self, b: bool) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::copyAvailable(bool b)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#copyAvailable

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QPlainTextEdit::copyAvailable(bool b)
    self.uglySide.call('ritual_ZN14QPlainTextEdit13copyAvailableEb', b)

  def selectionChanged(self) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::selectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#selectionChanged
    """
    #  void QPlainTextEdit::selectionChanged()
    self.uglySide.call('ritual_ZN14QPlainTextEdit16selectionChangedEv')

  def cursorPositionChanged(self) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::cursorPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#cursorPositionChanged
    """
    #  void QPlainTextEdit::cursorPositionChanged()
    self.uglySide.call('ritual_ZN14QPlainTextEdit21cursorPositionChangedEv')

  @overload(QRect, int)
  def updateRequest(self, rect: QRect, dy: int) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::updateRequest(const QRect &rect, int
    dy)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#updateRequest

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    dy : int
      Passed on as it is.
    """
    #  void QPlainTextEdit::updateRequest(const QRect &rect, int dy)
    self.uglySide.call(
        'ritual_ZN14QPlainTextEdit13updateRequestERK5QRecti',
        self._valueOf(rect), dy,
    )

  @overload(int)
  def blockCountChanged(self, newBlockCount: int) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::blockCountChanged(int newBlockCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#blockCountChanged

    Parameters
    ----------

    newBlockCount : int
      Passed on as it is.
    """
    #  void QPlainTextEdit::blockCountChanged(int newBlockCount)
    self.uglySide.call(
        'ritual_ZN14QPlainTextEdit17blockCountChangedEi', newBlockCount,
    )

  @overload(bool)
  def modificationChanged(self, a0: bool) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::modificationChanged(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#modificationChanged

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QPlainTextEdit::modificationChanged(bool a0)
    self.uglySide.call(
        'ritual_ZN14QPlainTextEdit19modificationChangedEb', a0,
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QPlainTextEdit::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPlainTextEdit::event(QEvent *e)
    ritual = 'ritual_ZN14QPlainTextEdit5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPlainTextEdit5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, e: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::timerEvent(QTimerEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#timerEvent

    Parameters
    ----------

    e : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlainTextEdit::timerEvent(QTimerEvent *e)
    ritual = 'ritual_ZN14QPlainTextEdit10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPlainTextEdit10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, e: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::keyPressEvent(QKeyEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#keyPressEvent

    Parameters
    ----------

    e : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlainTextEdit::keyPressEvent(QKeyEvent *e)
    ritual = 'ritual_ZN14QPlainTextEdit13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPlainTextEdit13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, e: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::keyReleaseEvent(QKeyEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#keyReleaseEvent

    Parameters
    ----------

    e : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlainTextEdit::keyReleaseEvent(QKeyEvent *e)
    ritual = 'ritual_ZN14QPlainTextEdit15keyReleaseEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPlainTextEdit15keyReleaseEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, e: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::resizeEvent(QResizeEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#resizeEvent

    Parameters
    ----------

    e : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlainTextEdit::resizeEvent(QResizeEvent *e)
    ritual = 'ritual_ZN14QPlainTextEdit11resizeEventEP12QResizeEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPlainTextEdit11resizeEventEP12QResizeEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, e: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::paintEvent(QPaintEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#paintEvent

    Parameters
    ----------

    e : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlainTextEdit::paintEvent(QPaintEvent *e)
    ritual = 'ritual_ZN14QPlainTextEdit10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPlainTextEdit10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, e: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::mousePressEvent(QMouseEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#mousePressEvent

    Parameters
    ----------

    e : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlainTextEdit::mousePressEvent(QMouseEvent *e)
    ritual = 'ritual_ZN14QPlainTextEdit15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QPlainTextEdit15mousePressEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, e: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::mouseMoveEvent(QMouseEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#mouseMoveEvent

    Parameters
    ----------

    e : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlainTextEdit::mouseMoveEvent(QMouseEvent *e)
    ritual = 'ritual_ZN14QPlainTextEdit14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPlainTextEdit14mouseMoveEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, e: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::mouseReleaseEvent(QMouseEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#mouseReleaseEvent

    Parameters
    ----------

    e : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlainTextEdit::mouseReleaseEvent(QMouseEvent *e)
    ritual = 'ritual_ZN14QPlainTextEdit17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QPlainTextEdit17mouseReleaseEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(self, e: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::mouseDoubleClickEvent(QMouseEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#mouseDoubleClickEvent

    Parameters
    ----------

    e : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlainTextEdit::mouseDoubleClickEvent(QMouseEvent *e)
    ritual = (
        'ritual_ZN14QPlainTextEdit21mouseDoubleClickEventEP11QMouseEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QPlainTextEdit21mouseDoubleClickEventEP11QMouseEv'
          'ent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(bool)
  def focusNextPrevChild(self, next: bool) -> bool:
    """
    Calls Qt's 'bool QPlainTextEdit::focusNextPrevChild(bool next)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#focusNextPrevChild

    Parameters
    ----------

    next : bool
      Passed on as it is.
    """
    #  bool QPlainTextEdit::focusNextPrevChild(bool next)
    ritual = 'ritual_ZN14QPlainTextEdit18focusNextPrevChildEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPlainTextEdit18focusNextPrevChildEb'
    return self.uglySide.call(ritual, next)

  @overload(QContextMenuEvent)
  @overload(NoneType)
  def contextMenuEvent(self, e: Optional[QContextMenuEvent]) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::contextMenuEvent(QContextMenuEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#contextMenuEvent

    Parameters
    ----------

    e : Optional[QContextMenuEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlainTextEdit::contextMenuEvent(QContextMenuEvent *e)
    ritual = (
        'ritual_ZN14QPlainTextEdit16contextMenuEventEP17QContextMenuEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QPlainTextEdit16contextMenuEventEP17QContextMenuE'
          'vent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QDragEnterEvent)
  @overload(NoneType)
  def dragEnterEvent(self, e: Optional[QDragEnterEvent]) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::dragEnterEvent(QDragEnterEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#dragEnterEvent

    Parameters
    ----------

    e : Optional[QDragEnterEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlainTextEdit::dragEnterEvent(QDragEnterEvent *e)
    ritual = 'ritual_ZN14QPlainTextEdit14dragEnterEventEP15QDragEnterEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QPlainTextEdit14dragEnterEventEP15QDragEnterEvent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QDragLeaveEvent)
  @overload(NoneType)
  def dragLeaveEvent(self, e: Optional[QDragLeaveEvent]) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::dragLeaveEvent(QDragLeaveEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#dragLeaveEvent

    Parameters
    ----------

    e : Optional[QDragLeaveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlainTextEdit::dragLeaveEvent(QDragLeaveEvent *e)
    ritual = 'ritual_ZN14QPlainTextEdit14dragLeaveEventEP15QDragLeaveEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QPlainTextEdit14dragLeaveEventEP15QDragLeaveEvent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QDragMoveEvent)
  @overload(NoneType)
  def dragMoveEvent(self, e: Optional[QDragMoveEvent]) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::dragMoveEvent(QDragMoveEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#dragMoveEvent

    Parameters
    ----------

    e : Optional[QDragMoveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlainTextEdit::dragMoveEvent(QDragMoveEvent *e)
    ritual = 'ritual_ZN14QPlainTextEdit13dragMoveEventEP14QDragMoveEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QPlainTextEdit13dragMoveEventEP14QDragMoveEvent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QDropEvent)
  @overload(NoneType)
  def dropEvent(self, e: Optional[QDropEvent]) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::dropEvent(QDropEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#dropEvent

    Parameters
    ----------

    e : Optional[QDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlainTextEdit::dropEvent(QDropEvent *e)
    ritual = 'ritual_ZN14QPlainTextEdit9dropEventEP10QDropEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPlainTextEdit9dropEventEP10QDropEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, e: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::focusInEvent(QFocusEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#focusInEvent

    Parameters
    ----------

    e : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlainTextEdit::focusInEvent(QFocusEvent *e)
    ritual = 'ritual_ZN14QPlainTextEdit12focusInEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPlainTextEdit12focusInEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, e: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::focusOutEvent(QFocusEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#focusOutEvent

    Parameters
    ----------

    e : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlainTextEdit::focusOutEvent(QFocusEvent *e)
    ritual = 'ritual_ZN14QPlainTextEdit13focusOutEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPlainTextEdit13focusOutEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QShowEvent)
  @overload(NoneType)
  def showEvent(self, a0: Optional[QShowEvent]) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::showEvent(QShowEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#showEvent

    Parameters
    ----------

    a0 : Optional[QShowEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlainTextEdit::showEvent(QShowEvent *a0)
    ritual = 'ritual_ZN14QPlainTextEdit9showEventEP10QShowEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPlainTextEdit9showEventEP10QShowEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QEvent)
  @overload(NoneType)
  def changeEvent(self, e: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::changeEvent(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#changeEvent

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlainTextEdit::changeEvent(QEvent *e)
    ritual = 'ritual_ZN14QPlainTextEdit11changeEventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPlainTextEdit11changeEventEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, e: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::wheelEvent(QWheelEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#wheelEvent

    Parameters
    ----------

    e : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlainTextEdit::wheelEvent(QWheelEvent *e)
    ritual = 'ritual_ZN14QPlainTextEdit10wheelEventEP11QWheelEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPlainTextEdit10wheelEventEP11QWheelEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QMimeData)
  @overload(NoneType)
  def insertFromMimeData(self, source: Optional[QMimeData]) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::insertFromMimeData(const QMimeData
    *source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#insertFromMimeData

    Parameters
    ----------

    source : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlainTextEdit::insertFromMimeData(const QMimeData *source)
    ritual = 'ritual_ZN14QPlainTextEdit18insertFromMimeDataEPK9QMimeData'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QPlainTextEdit18insertFromMimeDataEPK9QMimeData')
    self.uglySide.call(ritual, self._addressOf(source))

  @overload(QInputMethodEvent)
  @overload(NoneType)
  def inputMethodEvent(self, a0: Optional[QInputMethodEvent]) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::inputMethodEvent(QInputMethodEvent
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#inputMethodEvent

    Parameters
    ----------

    a0 : Optional[QInputMethodEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlainTextEdit::inputMethodEvent(QInputMethodEvent *a0)
    ritual = (
        'ritual_ZN14QPlainTextEdit16inputMethodEventEP17QInputMethodEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QPlainTextEdit16inputMethodEventEP17QInputMethodE'
          'vent')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(int, int)
  def scrollContentsBy(self, dx: int, dy: int) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::scrollContentsBy(int dx, int dy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#scrollContentsBy

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.
    """
    #  void QPlainTextEdit::scrollContentsBy(int dx, int dy)
    ritual = 'ritual_ZN14QPlainTextEdit16scrollContentsByEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPlainTextEdit16scrollContentsByEii'
    self.uglySide.call(ritual, dx, dy)

  @overload(QTextCursor)
  def doSetTextCursor(self, cursor: QTextCursor) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::doSetTextCursor(const QTextCursor
    &cursor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaintextedit.html#doSetTextCursor

    Parameters
    ----------

    cursor : QTextCursor
      Passed on as a value: Qt reads the C++ QTextCursor, which stays
      Python's own.
    """
    #  void QPlainTextEdit::doSetTextCursor(const QTextCursor &cursor)
    ritual = 'ritual_ZN14QPlainTextEdit15doSetTextCursorERK11QTextCursor'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QPlainTextEdit15doSetTextCursorERK11QTextCursor')
    self.uglySide.call(ritual, self._valueOf(cursor))

  @overload(float)
  def zoomInF(self, range: float) -> None:
    """
    Calls Qt's 'void QPlainTextEdit::zoomInF(float range)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaintextedit.html#zoomInF

    Parameters
    ----------

    range : float
      Passed on as it is.
    """
    #  void QPlainTextEdit::zoomInF(float range)
    self.uglySide.call('ritual_ZN14QPlainTextEdit7zoomInFEf', range)

  @staticmethod
  def extraSelections(*__, **_) -> Never:
    """
    Qt's 'QList<QTextEdit::ExtraSelection> QPlainTextEdit::extraSelections()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlainTextEdit.extraSelections' has no cute function yet. Qt's "
        "'QList<QTextEdit::ExtraSelection> "
        "QPlainTextEdit::extraSelections() const': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def setExtraSelections(*__, **_) -> Never:
    """
    Qt's 'void QPlainTextEdit::setExtraSelections(const
    QList<QTextEdit::ExtraSelection> &selections)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlainTextEdit.setExtraSelections' has no cute function yet. Qt's "
        "'void QPlainTextEdit::setExtraSelections(const "
        "QList<QTextEdit::ExtraSelection> &selections)': takes a type "
        "Python has no way to hand over yet.")
