"""
QTextEdit binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qtextedit.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QTextCursor, QTextDocument, QTextOption
from . import QAbstractScrollArea, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPoint, QRect, QRegularExpression, QUrl
  from ..QtCore import QVariant
  from ..QtGui import QColor, QFont, QPagedPaintDevice, QTextCharFormat
  from . import QMenu
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QFont = WAIT['QFont']
  QPagedPaintDevice = WAIT['QPagedPaintDevice']
  QPoint = WAIT['QPoint']
  QRegularExpression = WAIT['QRegularExpression']
  QTextCharFormat = WAIT['QTextCharFormat']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextEdit(QAbstractScrollArea):
  """
  The cute side of Qt's QTextEdit: a plain Python object standing in front of
  one C++ QTextEdit.

  It is built on the cute 'QAbstractScrollArea', as Qt's QTextEdit is built
  on Qt's QAbstractScrollArea, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTextEdit that has a ritual and that Python can call
  so far, 86 names in all: 'metaObject', 'tr', 'setDocument', 'document',
  'setPlaceholderText', 'placeholderText', 'setTextCursor', 'textCursor',
  'isReadOnly', 'setReadOnly', 'setTextInteractionFlags',
  'textInteractionFlags', 'fontPointSize', 'fontFamily', 'fontWeight',
  'fontUnderline', 'fontItalic', 'textColor', 'textBackgroundColor',
  'currentFont', 'alignment', 'mergeCurrentCharFormat',
  'setCurrentCharFormat', 'currentCharFormat', 'autoFormatting',
  'setAutoFormatting', 'tabChangesFocus', 'setTabChangesFocus',
  'setDocumentTitle', 'documentTitle', 'isUndoRedoEnabled',
  'setUndoRedoEnabled', 'lineWrapMode', 'setLineWrapMode',
  'lineWrapColumnOrWidth', 'setLineWrapColumnOrWidth', 'wordWrapMode',
  'setWordWrapMode', 'find', 'toPlainText', 'toHtml', 'toMarkdown',
  'ensureCursorVisible', 'loadResource', 'createStandardContextMenu',
  'cursorForPosition', 'cursorRect', 'anchorAt', 'overwriteMode',
  'setOverwriteMode', 'tabStopDistance', 'setTabStopDistance', 'cursorWidth',
  'setCursorWidth', 'acceptRichText', 'setAcceptRichText', 'moveCursor',
  'canPaste', 'print', 'inputMethodQuery', 'setFontPointSize',
  'setFontFamily', 'setFontWeight', 'setFontUnderline', 'setFontItalic',
  'setTextColor', 'setTextBackgroundColor', 'setCurrentFont', 'setAlignment',
  'setPlainText', 'setHtml', 'setMarkdown', 'setText', 'cut', 'copy',
  'paste', 'undo', 'redo', 'clear', 'selectAll', 'insertPlainText',
  'insertHtml', 'append', 'scrollToAnchor', 'zoomIn', 'zoomOut'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextEdit::~QTextEdit()': the destructor: Python never removes a
    C++ QTextEdit.

  What has no ritual
  ------------------

  46 of the 139 functions Qt declares: 29 protected; 7 a signal; 4 takes or
  gives a type that cannot be passed yet; 3 private; 2 forbidden; 1 a
  template.

  What to expect
  --------------

  - The C++ QTextEdit is created at the first use, not by 'QTextEdit(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTextEdit.
  - Qt tells when it has removed the C++ QTextEdit. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QTextEdit, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class AutoFormattingFlag(CuteFlags, number='unsigned int'):
    """
    The flags enum 'QTextEdit::AutoFormattingFlag' of Qt, with the 3 names Qt
    gives in it. Qt names the type of its combinations
    'QTextEdit::AutoFormatting'.
    """

    AutoNone = 0x0
    AutoBulletList = 0x1
    AutoAll = 0xffffffff

  AutoFormatting = AutoFormattingFlag

  class LineWrapMode(CuteNum):
    """
    The enum 'QTextEdit::LineWrapMode' of Qt, with the 4 names Qt gives in
    it.
    """

    NoWrap = Kee[int](0)
    WidgetWidth = Kee[int](1)
    FixedPixelWidth = Kee[int](2)
    FixedColumnWidth = Kee[int](3)

  #  The classes Qt writes inside QTextEdit, each a class in here as in C++.

  class ExtraSelection(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QTextEdit::ExtraSelection: a plain Python object
    standing in front of one C++ QTextEdit::ExtraSelection.

    C++ hands a QTextEdit::ExtraSelection around as a copy, so every C++
    QTextEdit::ExtraSelection behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QTextEdit::ExtraSelection yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QTextEdit::ExtraSelection::~ExtraSelection()': the destructor:
      Python removes its C++ QTextEdit::ExtraSelection by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QTextEdit::ExtraSelection is created at the first use, not by
      'QTextEdit::ExtraSelection(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QTextEdit::ExtraSelection back gives a copy the
      ritual made for Python, in a new cute QTextEdit::ExtraSelection.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QTextEdit::ExtraSelection'

    #  Qt's '~QTextEdit::ExtraSelection()'. Naming it makes this a value
    #  class: Python owns every C++ QTextEdit::ExtraSelection behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN9QTextEdit14ExtraSelectionD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Calls Qt's 'QString QTextEdit::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#tr

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
    #  QString QTextEdit::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9QTextEdit2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextEdit'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTextEdit::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTextEdit::metaObject() const
    address = self.uglySide.call('ritual_ZNK9QTextEdit10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def document(self) -> Optional[QTextDocument]:
    """
    Calls Qt's 'QTextDocument *QTextEdit::document() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#document

    Returns
    -------

    Optional[QTextDocument]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextDocument *QTextEdit::document() const
    address = self.uglySide.call('ritual_ZNK9QTextEdit8documentEv')
    return QTextDocument._cuteAt(address)

  def placeholderText(self) -> str:
    """
    Calls Qt's 'QString QTextEdit::placeholderText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#placeholderText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextEdit::placeholderText() const
    return self.uglySide.call('ritual_ZNK9QTextEdit15placeholderTextEv')

  def textCursor(self) -> QTextCursor:
    """
    Calls Qt's 'QTextCursor QTextEdit::textCursor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#textCursor

    Returns
    -------

    QTextCursor
      A new cute QTextCursor around the copy Qt gave back. Python owns it.
    """
    #  QTextCursor QTextEdit::textCursor() const
    address = self.uglySide.call('ritual_ZNK9QTextEdit10textCursorEv')
    return QTextCursor._cuteOwning(address)

  def isReadOnly(self) -> bool:
    """
    Calls Qt's 'bool QTextEdit::isReadOnly() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#isReadOnly
    """
    #  bool QTextEdit::isReadOnly() const
    return self.uglySide.call('ritual_ZNK9QTextEdit10isReadOnlyEv')

  def textInteractionFlags(self) -> Qt.TextInteractionFlags:
    """
    Calls Qt's 'Qt::TextInteractionFlags QTextEdit::textInteractionFlags()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextedit.html#textInteractionFlags

    Returns
    -------

    Qt.TextInteractionFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::TextInteractionFlags QTextEdit::textInteractionFlags() const
    return Qt.TextInteractionFlags(self.uglySide.call(
        'ritual_ZNK9QTextEdit20textInteractionFlagsEv',
    ))

  def fontPointSize(self) -> float:
    """
    Calls Qt's 'qreal QTextEdit::fontPointSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#fontPointSize
    """
    #  qreal QTextEdit::fontPointSize() const
    return self.uglySide.call('ritual_ZNK9QTextEdit13fontPointSizeEv')

  def fontFamily(self) -> str:
    """
    Calls Qt's 'QString QTextEdit::fontFamily() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#fontFamily

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextEdit::fontFamily() const
    return self.uglySide.call('ritual_ZNK9QTextEdit10fontFamilyEv')

  def fontWeight(self) -> int:
    """
    Calls Qt's 'int QTextEdit::fontWeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#fontWeight
    """
    #  int QTextEdit::fontWeight() const
    return self.uglySide.call('ritual_ZNK9QTextEdit10fontWeightEv')

  def fontUnderline(self) -> bool:
    """
    Calls Qt's 'bool QTextEdit::fontUnderline() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#fontUnderline
    """
    #  bool QTextEdit::fontUnderline() const
    return self.uglySide.call('ritual_ZNK9QTextEdit13fontUnderlineEv')

  def fontItalic(self) -> bool:
    """
    Calls Qt's 'bool QTextEdit::fontItalic() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#fontItalic
    """
    #  bool QTextEdit::fontItalic() const
    return self.uglySide.call('ritual_ZNK9QTextEdit10fontItalicEv')

  def textColor(self) -> QColor:
    """
    Calls Qt's 'QColor QTextEdit::textColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#textColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QTextEdit::textColor() const
    address = self.uglySide.call('ritual_ZNK9QTextEdit9textColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def textBackgroundColor(self) -> QColor:
    """
    Calls Qt's 'QColor QTextEdit::textBackgroundColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#textBackgroundColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QTextEdit::textBackgroundColor() const
    address = self.uglySide.call(
        'ritual_ZNK9QTextEdit19textBackgroundColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def currentFont(self) -> QFont:
    """
    Calls Qt's 'QFont QTextEdit::currentFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#currentFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QTextEdit::currentFont() const
    address = self.uglySide.call('ritual_ZNK9QTextEdit11currentFontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def alignment(self) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QTextEdit::alignment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#alignment

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QTextEdit::alignment() const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK9QTextEdit9alignmentEv',
    ))

  def currentCharFormat(self) -> QTextCharFormat:
    """
    Calls Qt's 'QTextCharFormat QTextEdit::currentCharFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#currentCharFormat

    Returns
    -------

    QTextCharFormat
      A new cute QTextCharFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextCharFormat QTextEdit::currentCharFormat() const
    address = self.uglySide.call('ritual_ZNK9QTextEdit17currentCharFormatEv')
    from ..QtGui import QTextCharFormat
    return QTextCharFormat._cuteOwning(address)

  def autoFormatting(self) -> AutoFormatting:
    """
    Calls Qt's 'AutoFormatting QTextEdit::autoFormatting() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#autoFormatting

    Returns
    -------

    AutoFormatting
      The value standing for the combination Qt gave back.
    """
    #  AutoFormatting QTextEdit::autoFormatting() const
    return QTextEdit.AutoFormatting(self.uglySide.call(
        'ritual_ZNK9QTextEdit14autoFormattingEv',
    ))

  def tabChangesFocus(self) -> bool:
    """
    Calls Qt's 'bool QTextEdit::tabChangesFocus() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#tabChangesFocus
    """
    #  bool QTextEdit::tabChangesFocus() const
    return self.uglySide.call('ritual_ZNK9QTextEdit15tabChangesFocusEv')

  def documentTitle(self) -> str:
    """
    Calls Qt's 'QString QTextEdit::documentTitle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#documentTitle

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextEdit::documentTitle() const
    return self.uglySide.call('ritual_ZNK9QTextEdit13documentTitleEv')

  def isUndoRedoEnabled(self) -> bool:
    """
    Calls Qt's 'bool QTextEdit::isUndoRedoEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#isUndoRedoEnabled
    """
    #  bool QTextEdit::isUndoRedoEnabled() const
    return self.uglySide.call('ritual_ZNK9QTextEdit17isUndoRedoEnabledEv')

  def lineWrapMode(self) -> LineWrapMode:
    """
    Calls Qt's 'LineWrapMode QTextEdit::lineWrapMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#lineWrapMode

    Returns
    -------

    LineWrapMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'LineWrapMode(number)'
      gives.
    """
    #  LineWrapMode QTextEdit::lineWrapMode() const
    return QTextEdit.LineWrapMode(self.uglySide.call(
        'ritual_ZNK9QTextEdit12lineWrapModeEv',
    ))

  def lineWrapColumnOrWidth(self) -> int:
    """
    Calls Qt's 'int QTextEdit::lineWrapColumnOrWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextedit.html#lineWrapColumnOrWidth
    """
    #  int QTextEdit::lineWrapColumnOrWidth() const
    return self.uglySide.call(
        'ritual_ZNK9QTextEdit21lineWrapColumnOrWidthEv',
    )

  def wordWrapMode(self) -> QTextOption.WrapMode:
    """
    Calls Qt's 'QTextOption::WrapMode QTextEdit::wordWrapMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#wordWrapMode

    Returns
    -------

    QTextOption.WrapMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QTextOption.WrapMode(number)' gives.
    """
    #  QTextOption::WrapMode QTextEdit::wordWrapMode() const
    return QTextOption.WrapMode(self.uglySide.call(
        'ritual_ZNK9QTextEdit12wordWrapModeEv',
    ))

  def toPlainText(self) -> str:
    """
    Calls Qt's 'QString QTextEdit::toPlainText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#toPlainText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextEdit::toPlainText() const
    return self.uglySide.call('ritual_ZNK9QTextEdit11toPlainTextEv')

  def toHtml(self) -> str:
    """
    Calls Qt's 'QString QTextEdit::toHtml() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#toHtml

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextEdit::toHtml() const
    return self.uglySide.call('ritual_ZNK9QTextEdit6toHtmlEv')

  @overload()
  @overload(QTextDocument.MarkdownFeatures)
  def toMarkdown(
      self,
      features: QTextDocument.MarkdownFeatures = (
          QTextDocument.MarkdownFeatures.MarkdownDialectGitHub),
  ) -> str:
    """
    Calls Qt's 'QString QTextEdit::toMarkdown(QTextDocument::MarkdownFeatures
    features) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#toMarkdown

    Parameters
    ----------

    features : QTextDocument.MarkdownFeatures
      Passed on as its number. May be left out, as in Qt: it is then
      QTextDocument.MarkdownFeatures.MarkdownDialectGitHub.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextEdit::toMarkdown(QTextDocument::MarkdownFeatures
    #      features) const
    return self.uglySide.call(
        'ritual_ZNK9QTextEdit10toMarkdownE6QFlagsIN13QTextDocument15Markdow'
        'nFeatureEE',
        features.value,
    )

  @overload(QPoint)
  def cursorForPosition(self, pos: QPoint) -> QTextCursor:
    """
    Calls Qt's 'QTextCursor QTextEdit::cursorForPosition(const QPoint &pos)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#cursorForPosition

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
    #  QTextCursor QTextEdit::cursorForPosition(const QPoint &pos) const
    address = self.uglySide.call(
        'ritual_ZNK9QTextEdit17cursorForPositionERK6QPoint',
        self._valueOf(pos),
    )
    return QTextCursor._cuteOwning(address)

  @overload(QTextCursor)
  def cursorRect(self, cursor: QTextCursor) -> QRect:
    """
    Calls Qt's 'QRect QTextEdit::cursorRect(const QTextCursor &cursor)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#cursorRect

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
    #  QRect QTextEdit::cursorRect(const QTextCursor &cursor) const
    address = self.uglySide.call(
        'ritual_ZNK9QTextEdit10cursorRectERK11QTextCursor',
        self._valueOf(cursor),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload()
  def cursorRect(self) -> QRect:
    """
    Calls Qt's 'QRect QTextEdit::cursorRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#cursorRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QTextEdit::cursorRect() const
    address = self.uglySide.call('ritual_ZNK9QTextEdit10cursorRectEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QPoint)
  def anchorAt(self, pos: QPoint) -> str:
    """
    Calls Qt's 'QString QTextEdit::anchorAt(const QPoint &pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#anchorAt

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
    #  QString QTextEdit::anchorAt(const QPoint &pos) const
    return self.uglySide.call(
        'ritual_ZNK9QTextEdit8anchorAtERK6QPoint', self._valueOf(pos),
    )

  def overwriteMode(self) -> bool:
    """
    Calls Qt's 'bool QTextEdit::overwriteMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#overwriteMode
    """
    #  bool QTextEdit::overwriteMode() const
    return self.uglySide.call('ritual_ZNK9QTextEdit13overwriteModeEv')

  def tabStopDistance(self) -> float:
    """
    Calls Qt's 'qreal QTextEdit::tabStopDistance() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#tabStopDistance
    """
    #  qreal QTextEdit::tabStopDistance() const
    return self.uglySide.call('ritual_ZNK9QTextEdit15tabStopDistanceEv')

  def cursorWidth(self) -> int:
    """
    Calls Qt's 'int QTextEdit::cursorWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#cursorWidth
    """
    #  int QTextEdit::cursorWidth() const
    return self.uglySide.call('ritual_ZNK9QTextEdit11cursorWidthEv')

  def acceptRichText(self) -> bool:
    """
    Calls Qt's 'bool QTextEdit::acceptRichText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#acceptRichText
    """
    #  bool QTextEdit::acceptRichText() const
    return self.uglySide.call('ritual_ZNK9QTextEdit14acceptRichTextEv')

  def canPaste(self) -> bool:
    """
    Calls Qt's 'bool QTextEdit::canPaste() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#canPaste
    """
    #  bool QTextEdit::canPaste() const
    return self.uglySide.call('ritual_ZNK9QTextEdit8canPasteEv')

  @overload(Qt.InputMethodQuery)
  def inputMethodQuery(self, property: Qt.InputMethodQuery) -> QVariant:
    """
    Calls Qt's 'QVariant QTextEdit::inputMethodQuery(Qt::InputMethodQuery
    property) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#inputMethodQuery

    Parameters
    ----------

    property : Qt.InputMethodQuery
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QTextEdit::inputMethodQuery(Qt::InputMethodQuery property)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK9QTextEdit16inputMethodQueryEN2Qt16InputMethodQueryE',
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
    Calls Qt's 'QVariant QTextEdit::inputMethodQuery(Qt::InputMethodQuery
    query, QVariant argument) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#inputMethodQuery

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
    #  QVariant QTextEdit::inputMethodQuery(Qt::InputMethodQuery query,
    #      QVariant argument) const
    address = self.uglySide.call(
        'ritual_ZNK9QTextEdit16inputMethodQueryEN2Qt16InputMethodQueryE8QVa'
        'riant',
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
    Calls Qt's 'void QTextEdit::setDocument(QTextDocument *document)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#setDocument

    Parameters
    ----------

    document : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextEdit::setDocument(QTextDocument *document)
    self.uglySide.call(
        'ritual_ZN9QTextEdit11setDocumentEP13QTextDocument',
        self._addressOf(document),
    )

  @overload(str)
  def setPlaceholderText(self, placeholderText: str) -> None:
    """
    Calls Qt's 'void QTextEdit::setPlaceholderText(const QString
    &placeholderText)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#setPlaceholderText

    Parameters
    ----------

    placeholderText : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextEdit::setPlaceholderText(const QString &placeholderText)
    self.uglySide.call(
        'ritual_ZN9QTextEdit18setPlaceholderTextERK7QString',
        placeholderText,
    )

  @overload(QTextCursor)
  def setTextCursor(self, cursor: QTextCursor) -> None:
    """
    Calls Qt's 'void QTextEdit::setTextCursor(const QTextCursor &cursor)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#setTextCursor

    Parameters
    ----------

    cursor : QTextCursor
      Passed on as a value: Qt reads the C++ QTextCursor, which stays
      Python's own.
    """
    #  void QTextEdit::setTextCursor(const QTextCursor &cursor)
    self.uglySide.call(
        'ritual_ZN9QTextEdit13setTextCursorERK11QTextCursor',
        self._valueOf(cursor),
    )

  @overload(bool)
  def setReadOnly(self, ro: bool) -> None:
    """
    Calls Qt's 'void QTextEdit::setReadOnly(bool ro)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#setReadOnly

    Parameters
    ----------

    ro : bool
      Passed on as it is.
    """
    #  void QTextEdit::setReadOnly(bool ro)
    self.uglySide.call('ritual_ZN9QTextEdit11setReadOnlyEb', ro)

  @overload(Qt.TextInteractionFlags)
  def setTextInteractionFlags(self, flags: Qt.TextInteractionFlags) -> None:
    """
    Calls Qt's 'void
    QTextEdit::setTextInteractionFlags(Qt::TextInteractionFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextedit.html#setTextInteractionFlags

    Parameters
    ----------

    flags : Qt.TextInteractionFlags
      Passed on as its number.
    """
    #  void QTextEdit::setTextInteractionFlags(Qt::TextInteractionFlags
    #      flags)
    self.uglySide.call(
        'ritual_ZN9QTextEdit23setTextInteractionFlagsE6QFlagsIN2Qt19TextInt'
        'eractionFlagEE',
        flags.value,
    )

  @overload(QTextCharFormat)
  def setCurrentCharFormat(self, format: QTextCharFormat) -> None:
    """
    Calls Qt's 'void QTextEdit::setCurrentCharFormat(const QTextCharFormat
    &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextedit.html#setCurrentCharFormat

    Parameters
    ----------

    format : QTextCharFormat
      Passed on as a value: Qt reads the C++ QTextCharFormat, which stays
      Python's own.
    """
    #  void QTextEdit::setCurrentCharFormat(const QTextCharFormat &format)
    self.uglySide.call(
        'ritual_ZN9QTextEdit20setCurrentCharFormatERK15QTextCharFormat',
        self._valueOf(format),
    )

  @overload(AutoFormatting)
  def setAutoFormatting(self, features: AutoFormatting) -> None:
    """
    Calls Qt's 'void QTextEdit::setAutoFormatting(AutoFormatting features)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#setAutoFormatting

    Parameters
    ----------

    features : AutoFormatting
      Passed on as its number.
    """
    #  void QTextEdit::setAutoFormatting(AutoFormatting features)
    self.uglySide.call(
        'ritual_ZN9QTextEdit17setAutoFormattingE6QFlagsINS_18AutoFormatting'
        'FlagEE',
        features.value,
    )

  @overload(bool)
  def setTabChangesFocus(self, b: bool) -> None:
    """
    Calls Qt's 'void QTextEdit::setTabChangesFocus(bool b)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#setTabChangesFocus

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QTextEdit::setTabChangesFocus(bool b)
    self.uglySide.call('ritual_ZN9QTextEdit18setTabChangesFocusEb', b)

  @overload(str)
  def setDocumentTitle(self, title: str) -> None:
    """
    Calls Qt's 'void QTextEdit::setDocumentTitle(const QString &title)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#setDocumentTitle

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextEdit::setDocumentTitle(const QString &title)
    self.uglySide.call(
        'ritual_ZN9QTextEdit16setDocumentTitleERK7QString', title,
    )

  @overload(bool)
  def setUndoRedoEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QTextEdit::setUndoRedoEnabled(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#setUndoRedoEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QTextEdit::setUndoRedoEnabled(bool enable)
    self.uglySide.call('ritual_ZN9QTextEdit18setUndoRedoEnabledEb', enable)

  @overload(LineWrapMode)
  def setLineWrapMode(self, mode: LineWrapMode) -> None:
    """
    Calls Qt's 'void QTextEdit::setLineWrapMode(LineWrapMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#setLineWrapMode

    Parameters
    ----------

    mode : LineWrapMode
      Passed on as its number.
    """
    #  void QTextEdit::setLineWrapMode(LineWrapMode mode)
    self.uglySide.call(
        'ritual_ZN9QTextEdit15setLineWrapModeENS_12LineWrapModeE',
        mode.value,
    )

  @overload(int)
  def setLineWrapColumnOrWidth(self, w: int) -> None:
    """
    Calls Qt's 'void QTextEdit::setLineWrapColumnOrWidth(int w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextedit.html#setLineWrapColumnOrWidth

    Parameters
    ----------

    w : int
      Passed on as it is.
    """
    #  void QTextEdit::setLineWrapColumnOrWidth(int w)
    self.uglySide.call('ritual_ZN9QTextEdit24setLineWrapColumnOrWidthEi', w)

  @overload(QTextOption.WrapMode)
  def setWordWrapMode(self, policy: QTextOption.WrapMode) -> None:
    """
    Calls Qt's 'void QTextEdit::setWordWrapMode(QTextOption::WrapMode
    policy)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#setWordWrapMode

    Parameters
    ----------

    policy : QTextOption.WrapMode
      Passed on as its number.
    """
    #  void QTextEdit::setWordWrapMode(QTextOption::WrapMode policy)
    self.uglySide.call(
        'ritual_ZN9QTextEdit15setWordWrapModeEN11QTextOption8WrapModeE',
        policy.value,
    )

  @overload(bool)
  def setOverwriteMode(self, overwrite: bool) -> None:
    """
    Calls Qt's 'void QTextEdit::setOverwriteMode(bool overwrite)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#setOverwriteMode

    Parameters
    ----------

    overwrite : bool
      Passed on as it is.
    """
    #  void QTextEdit::setOverwriteMode(bool overwrite)
    self.uglySide.call('ritual_ZN9QTextEdit16setOverwriteModeEb', overwrite)

  @overload(float)
  def setTabStopDistance(self, distance: float) -> None:
    """
    Calls Qt's 'void QTextEdit::setTabStopDistance(qreal distance)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#setTabStopDistance

    Parameters
    ----------

    distance : float
      Passed on as it is.
    """
    #  void QTextEdit::setTabStopDistance(qreal distance)
    self.uglySide.call('ritual_ZN9QTextEdit18setTabStopDistanceEd', distance)

  @overload(int)
  def setCursorWidth(self, width: int) -> None:
    """
    Calls Qt's 'void QTextEdit::setCursorWidth(int width)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#setCursorWidth

    Parameters
    ----------

    width : int
      Passed on as it is.
    """
    #  void QTextEdit::setCursorWidth(int width)
    self.uglySide.call('ritual_ZN9QTextEdit14setCursorWidthEi', width)

  @overload(bool)
  def setAcceptRichText(self, accept: bool) -> None:
    """
    Calls Qt's 'void QTextEdit::setAcceptRichText(bool accept)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#setAcceptRichText

    Parameters
    ----------

    accept : bool
      Passed on as it is.
    """
    #  void QTextEdit::setAcceptRichText(bool accept)
    self.uglySide.call('ritual_ZN9QTextEdit17setAcceptRichTextEb', accept)

  @overload(float)
  def setFontPointSize(self, s: float) -> None:
    """
    Calls Qt's 'void QTextEdit::setFontPointSize(qreal s)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#setFontPointSize

    Parameters
    ----------

    s : float
      Passed on as it is.
    """
    #  void QTextEdit::setFontPointSize(qreal s)
    self.uglySide.call('ritual_ZN9QTextEdit16setFontPointSizeEd', s)

  @overload(str)
  def setFontFamily(self, fontFamily: str) -> None:
    """
    Calls Qt's 'void QTextEdit::setFontFamily(const QString &fontFamily)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#setFontFamily

    Parameters
    ----------

    fontFamily : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextEdit::setFontFamily(const QString &fontFamily)
    self.uglySide.call(
        'ritual_ZN9QTextEdit13setFontFamilyERK7QString', fontFamily,
    )

  @overload(int)
  def setFontWeight(self, w: int) -> None:
    """
    Calls Qt's 'void QTextEdit::setFontWeight(int w)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#setFontWeight

    Parameters
    ----------

    w : int
      Passed on as it is.
    """
    #  void QTextEdit::setFontWeight(int w)
    self.uglySide.call('ritual_ZN9QTextEdit13setFontWeightEi', w)

  @overload(bool)
  def setFontUnderline(self, b: bool) -> None:
    """
    Calls Qt's 'void QTextEdit::setFontUnderline(bool b)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#setFontUnderline

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QTextEdit::setFontUnderline(bool b)
    self.uglySide.call('ritual_ZN9QTextEdit16setFontUnderlineEb', b)

  @overload(bool)
  def setFontItalic(self, b: bool) -> None:
    """
    Calls Qt's 'void QTextEdit::setFontItalic(bool b)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#setFontItalic

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QTextEdit::setFontItalic(bool b)
    self.uglySide.call('ritual_ZN9QTextEdit13setFontItalicEb', b)

  @overload(QColor)
  def setTextColor(self, c: QColor) -> None:
    """
    Calls Qt's 'void QTextEdit::setTextColor(const QColor &c)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#setTextColor

    Parameters
    ----------

    c : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QTextEdit::setTextColor(const QColor &c)
    self.uglySide.call(
        'ritual_ZN9QTextEdit12setTextColorERK6QColor', self._valueOf(c),
    )

  @overload(QColor)
  def setTextBackgroundColor(self, c: QColor) -> None:
    """
    Calls Qt's 'void QTextEdit::setTextBackgroundColor(const QColor &c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextedit.html#setTextBackgroundColor

    Parameters
    ----------

    c : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QTextEdit::setTextBackgroundColor(const QColor &c)
    self.uglySide.call(
        'ritual_ZN9QTextEdit22setTextBackgroundColorERK6QColor',
        self._valueOf(c),
    )

  @overload(QFont)
  def setCurrentFont(self, f: QFont) -> None:
    """
    Calls Qt's 'void QTextEdit::setCurrentFont(const QFont &f)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#setCurrentFont

    Parameters
    ----------

    f : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QTextEdit::setCurrentFont(const QFont &f)
    self.uglySide.call(
        'ritual_ZN9QTextEdit14setCurrentFontERK5QFont', self._valueOf(f),
    )

  @overload(Qt.Alignment)
  def setAlignment(self, a: Qt.Alignment) -> None:
    """
    Calls Qt's 'void QTextEdit::setAlignment(Qt::Alignment a)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#setAlignment

    Parameters
    ----------

    a : Qt.Alignment
      Passed on as its number.
    """
    #  void QTextEdit::setAlignment(Qt::Alignment a)
    self.uglySide.call(
        'ritual_ZN9QTextEdit12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE',
        a.value,
    )

  @overload(str)
  def setPlainText(self, text: str) -> None:
    """
    Calls Qt's 'void QTextEdit::setPlainText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#setPlainText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextEdit::setPlainText(const QString &text)
    self.uglySide.call('ritual_ZN9QTextEdit12setPlainTextERK7QString', text)

  @overload(str)
  def setHtml(self, text: str) -> None:
    """
    Calls Qt's 'void QTextEdit::setHtml(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#setHtml

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextEdit::setHtml(const QString &text)
    self.uglySide.call('ritual_ZN9QTextEdit7setHtmlERK7QString', text)

  @overload(str)
  def setMarkdown(self, markdown: str) -> None:
    """
    Calls Qt's 'void QTextEdit::setMarkdown(const QString &markdown)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#setMarkdown

    Parameters
    ----------

    markdown : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextEdit::setMarkdown(const QString &markdown)
    self.uglySide.call(
        'ritual_ZN9QTextEdit11setMarkdownERK7QString', markdown,
    )

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QTextEdit::setText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextEdit::setText(const QString &text)
    self.uglySide.call('ritual_ZN9QTextEdit7setTextERK7QString', text)

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
    Notes what was given, for Qt's 'QTextEdit::QTextEdit(QWidget *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#QTextEdit

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QTextEdit::QTextEdit(QWidget *parent)
    self._noteCreation(QTextEdit, lambda: Rituals.call(
        'ritual_ZN9QTextEditC1EP7QWidget', self._addressOf(parent),
    ))

  @overload(str)
  @overload(str, QWidget)
  @overload(str, NoneType)
  def __init__(self, text: str, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QTextEdit::QTextEdit(const QString &text,
    QWidget *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#QTextEdit

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QTextEdit::QTextEdit(const QString &text, QWidget *parent)
    self._noteCreation(QTextEdit, lambda: Rituals.call(
        'ritual_ZN9QTextEditC1ERK7QStringP7QWidget',
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
    Calls Qt's 'void QTextEdit::mergeCurrentCharFormat(const QTextCharFormat
    &modifier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextedit.html#mergeCurrentCharFormat

    Parameters
    ----------

    modifier : QTextCharFormat
      Passed on as a value: Qt reads the C++ QTextCharFormat, which stays
      Python's own.
    """
    #  void QTextEdit::mergeCurrentCharFormat(const QTextCharFormat
    #      &modifier)
    self.uglySide.call(
        'ritual_ZN9QTextEdit22mergeCurrentCharFormatERK15QTextCharFormat',
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
    Calls Qt's 'bool QTextEdit::find(const QString &exp,
    QTextDocument::FindFlags options)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#find

    Parameters
    ----------

    exp : str
      Passed on as it is: a QString is made of it for the call.

    options : QTextDocument.FindFlags
      Passed on as its number. May be left out, as in Qt: it is then
      QTextDocument.FindFlags().
    """
    #  bool QTextEdit::find(const QString &exp, QTextDocument::FindFlags
    #      options)
    return self.uglySide.call(
        'ritual_ZN9QTextEdit4findERK7QString6QFlagsIN13QTextDocument8FindFl'
        'agEE',
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
    Calls Qt's 'bool QTextEdit::find(const QRegularExpression &exp,
    QTextDocument::FindFlags options)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#find

    Parameters
    ----------

    exp : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.

    options : QTextDocument.FindFlags
      Passed on as its number. May be left out, as in Qt: it is then
      QTextDocument.FindFlags().
    """
    #  bool QTextEdit::find(const QRegularExpression &exp,
    #      QTextDocument::FindFlags options)
    return self.uglySide.call(
        'ritual_ZN9QTextEdit4findERK18QRegularExpression6QFlagsIN13QTextDoc'
        'ument8FindFlagEE',
        self._valueOf(exp), options.value,
    )

  def ensureCursorVisible(self) -> None:
    """
    Calls Qt's 'void QTextEdit::ensureCursorVisible()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#ensureCursorVisible
    """
    #  void QTextEdit::ensureCursorVisible()
    self.uglySide.call('ritual_ZN9QTextEdit19ensureCursorVisibleEv')

  @overload(int, QUrl)
  def loadResource(self, type: int, name: QUrl) -> QVariant:
    """
    Calls Qt's 'QVariant QTextEdit::loadResource(int type, const QUrl
    &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#loadResource

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
    #  QVariant QTextEdit::loadResource(int type, const QUrl &name)
    address = self.uglySide.call(
        'ritual_ZN9QTextEdit12loadResourceEiRK4QUrl',
        type, self._valueOf(name),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload()
  def createStandardContextMenu(self) -> Optional[QMenu]:
    """
    Calls Qt's 'QMenu *QTextEdit::createStandardContextMenu()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextedit.html#createStandardContextMenu

    Returns
    -------

    Optional[QMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenu *QTextEdit::createStandardContextMenu()
    address = self.uglySide.call(
        'ritual_ZN9QTextEdit25createStandardContextMenuEv',
    )
    from . import QMenu
    return QMenu._cuteAt(address)

  @overload(QPoint)
  def createStandardContextMenu(self, position: QPoint) -> Optional[QMenu]:
    """
    Calls Qt's 'QMenu *QTextEdit::createStandardContextMenu(const QPoint
    &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextedit.html#createStandardContextMenu

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
    #  QMenu *QTextEdit::createStandardContextMenu(const QPoint &position)
    address = self.uglySide.call(
        'ritual_ZN9QTextEdit25createStandardContextMenuERK6QPoint',
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
    Calls Qt's 'void QTextEdit::moveCursor(QTextCursor::MoveOperation
    operation, QTextCursor::MoveMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#moveCursor

    Parameters
    ----------

    operation : QTextCursor.MoveOperation
      Passed on as its number.

    mode : QTextCursor.MoveMode
      Passed on as its number. May be left out, as in Qt: it is then
      QTextCursor.MoveMode.MoveAnchor.
    """
    #  void QTextEdit::moveCursor(QTextCursor::MoveOperation operation,
    #      QTextCursor::MoveMode mode)
    self.uglySide.call(
        'ritual_ZN9QTextEdit10moveCursorEN11QTextCursor13MoveOperationENS0_'
        '8MoveModeE',
        operation.value, mode.value,
    )

  @overload(QPagedPaintDevice)
  @overload(NoneType)
  def print(self, printer: Optional[QPagedPaintDevice]) -> None:
    """
    Calls Qt's 'void QTextEdit::print(QPagedPaintDevice *printer) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#print

    Parameters
    ----------

    printer : Optional[QPagedPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextEdit::print(QPagedPaintDevice *printer) const
    self.uglySide.call(
        'ritual_ZNK9QTextEdit5printEP17QPagedPaintDevice',
        self._addressOf(printer, 'QPagedPaintDevice'),
    )

  def cut(self) -> None:
    """
    Calls Qt's 'void QTextEdit::cut()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#cut
    """
    #  void QTextEdit::cut()
    self.uglySide.call('ritual_ZN9QTextEdit3cutEv')

  def copy(self) -> None:
    """
    Calls Qt's 'void QTextEdit::copy()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#copy
    """
    #  void QTextEdit::copy()
    self.uglySide.call('ritual_ZN9QTextEdit4copyEv')

  def paste(self) -> None:
    """
    Calls Qt's 'void QTextEdit::paste()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#paste
    """
    #  void QTextEdit::paste()
    self.uglySide.call('ritual_ZN9QTextEdit5pasteEv')

  def undo(self) -> None:
    """
    Calls Qt's 'void QTextEdit::undo()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#undo
    """
    #  void QTextEdit::undo()
    self.uglySide.call('ritual_ZN9QTextEdit4undoEv')

  def redo(self) -> None:
    """
    Calls Qt's 'void QTextEdit::redo()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#redo
    """
    #  void QTextEdit::redo()
    self.uglySide.call('ritual_ZN9QTextEdit4redoEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QTextEdit::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#clear
    """
    #  void QTextEdit::clear()
    self.uglySide.call('ritual_ZN9QTextEdit5clearEv')

  def selectAll(self) -> None:
    """
    Calls Qt's 'void QTextEdit::selectAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#selectAll
    """
    #  void QTextEdit::selectAll()
    self.uglySide.call('ritual_ZN9QTextEdit9selectAllEv')

  @overload(str)
  def insertPlainText(self, text: str) -> None:
    """
    Calls Qt's 'void QTextEdit::insertPlainText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#insertPlainText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextEdit::insertPlainText(const QString &text)
    self.uglySide.call(
        'ritual_ZN9QTextEdit15insertPlainTextERK7QString', text,
    )

  @overload(str)
  def insertHtml(self, text: str) -> None:
    """
    Calls Qt's 'void QTextEdit::insertHtml(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#insertHtml

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextEdit::insertHtml(const QString &text)
    self.uglySide.call('ritual_ZN9QTextEdit10insertHtmlERK7QString', text)

  @overload(str)
  def append(self, text: str) -> None:
    """
    Calls Qt's 'void QTextEdit::append(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#append

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextEdit::append(const QString &text)
    self.uglySide.call('ritual_ZN9QTextEdit6appendERK7QString', text)

  @overload(str)
  def scrollToAnchor(self, name: str) -> None:
    """
    Calls Qt's 'void QTextEdit::scrollToAnchor(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#scrollToAnchor

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextEdit::scrollToAnchor(const QString &name)
    self.uglySide.call(
        'ritual_ZN9QTextEdit14scrollToAnchorERK7QString', name,
    )

  @overload()
  @overload(int)
  def zoomIn(self, range: int = 1) -> None:
    """
    Calls Qt's 'void QTextEdit::zoomIn(int range)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#zoomIn

    Parameters
    ----------

    range : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void QTextEdit::zoomIn(int range)
    self.uglySide.call('ritual_ZN9QTextEdit6zoomInEi', range)

  @overload()
  @overload(int)
  def zoomOut(self, range: int = 1) -> None:
    """
    Calls Qt's 'void QTextEdit::zoomOut(int range)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextedit.html#zoomOut

    Parameters
    ----------

    range : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void QTextEdit::zoomOut(int range)
    self.uglySide.call('ritual_ZN9QTextEdit7zoomOutEi', range)
