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

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QTextCursorMoveMode, QTextCursorMoveOperation
from ..QtGui import QTextDocumentFindFlag, QTextOptionWrapMode
from . import QAbstractScrollArea, QPlainTextEditLineWrapMode, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPoint, QRect, QRegularExpression, QUrl
  from ..QtCore import QVariant
  from ..QtGui import QPagedPaintDevice, QTextCharFormat, QTextCursor
  from ..QtGui import QTextDocument, QTextOption
  from . import QMenu
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPagedPaintDevice = WAIT['QPagedPaintDevice']
  QPoint = WAIT['QPoint']
  QRegularExpression = WAIT['QRegularExpression']
  QTextCharFormat = WAIT['QTextCharFormat']
  QTextCursor = WAIT['QTextCursor']
  QTextDocument = WAIT['QTextDocument']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

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
  call so far, 64 names in all: 'metaObject', 'tr', 'setDocument',
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
  'centerCursor', 'zoomIn', 'zoomOut'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlainTextEdit::~QPlainTextEdit()': the destructor: Python never
    removes a C++ QPlainTextEdit.

  What has no ritual
  ------------------

  53 of the 124 functions Qt declares: 34 protected; 9 a signal; 4 takes or
  gives a type that cannot be passed yet; 3 private; 2 forbidden; 1 a
  template.

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
  """

  #  The enums Qt writes inside QPlainTextEdit, and the names Qt has for the
  #  combinations of its flags enums.
  LineWrapMode = QPlainTextEditLineWrapMode

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
    from ..QtGui import QTextDocument
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
    from ..QtGui import QTextCursor
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
    return QTextOptionWrapMode(self.uglySide.call(
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
    from ..QtGui import QTextCursor
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
    address = self.uglySide.call(
        'ritual_ZNK14QPlainTextEdit16inputMethodQueryEN2Qt16InputMethodQuer'
        'yE',
        property.value,
    )
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

  @overload(QTextOptionWrapMode)
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
  @overload(str, QTextDocumentFindFlag)
  def find(
      self,
      exp: str,
      options: QTextDocument.FindFlags = QTextDocumentFindFlag(),
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
      QTextDocumentFindFlag().
    """
    #  bool QPlainTextEdit::find(const QString &exp, QTextDocument::FindFlags
    #      options)
    return self.uglySide.call(
        'ritual_ZN14QPlainTextEdit4findERK7QString6QFlagsIN13QTextDocument8'
        'FindFlagEE',
        exp, options.value,
    )

  @overload(QRegularExpression)
  @overload(QRegularExpression, QTextDocumentFindFlag)
  def find(
      self,
      exp: QRegularExpression,
      options: QTextDocument.FindFlags = QTextDocumentFindFlag(),
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
      QTextDocumentFindFlag().
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
    address = self.uglySide.call(
        'ritual_ZN14QPlainTextEdit12loadResourceEiRK4QUrl',
        type, self._valueOf(name),
    )
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

  @overload(QTextCursorMoveOperation)
  @overload(QTextCursorMoveOperation, QTextCursorMoveMode)
  def moveCursor(
      self,
      operation: QTextCursor.MoveOperation,
      mode: QTextCursor.MoveMode = QTextCursorMoveMode.MoveAnchor,
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
      QTextCursorMoveMode.MoveAnchor.
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
        self._addressOf(printer),
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
