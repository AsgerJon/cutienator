"""
QQuickTextEdit binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktextedit_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickTextEdit to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QQuickImplicitSizeItem, QQuickItem, QQuickTextInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QRectF, QUrl, QVariant
  from ..QtGui import QColor, QFocusEvent, QFont, QHoverEvent
  from ..QtGui import QInputMethodEvent, QKeyEvent, QMouseEvent, QTextBlock
  from ..QtGui import QTextDocument
  from ..QtQml import QQmlComponent
  from . import QQuickTextDocument, QQuickTextEditPrivate
  from . import QQuickTextSelection, QSGNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QEvent = WAIT['QEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QFont = WAIT['QFont']
  QHoverEvent = WAIT['QHoverEvent']
  QInputMethodEvent = WAIT['QInputMethodEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QQmlComponent = WAIT['QQmlComponent']
  QRectF = WAIT['QRectF']
  QSGNode = WAIT['QSGNode']
  QTextBlock = WAIT['QTextBlock']
  QTextDocument = WAIT['QTextDocument']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTextEdit(QQuickImplicitSizeItem, QQuickTextInterface):
  """
  The cute side of Qt's QQuickTextEdit: a plain Python object standing in
  front of one C++ QQuickTextEdit.

  It is built on the cute 'QQuickImplicitSizeItem', as Qt's QQuickTextEdit is
  built on Qt's QQuickImplicitSizeItem, and has everything that class has. It
  is built on the cute 'QQuickTextInterface' as well, as Qt's QQuickTextEdit
  is built on Qt's QQuickTextInterface too, and has everything that class
  has.

  What exists
  -----------

  Every function of Qt's QQuickTextEdit that has a ritual and that Python can
  call so far, 196 names in all: 'metaObject', 'tr', 'text', 'setText',
  'preeditText', 'textFormat', 'setTextFormat', 'font', 'setFont', 'color',
  'setColor', 'selectionColor', 'setSelectionColor', 'selectedTextColor',
  'setSelectedTextColor', 'hAlign', 'setHAlign', 'resetHAlign',
  'effectiveHAlign', 'vAlign', 'setVAlign', 'wrapMode', 'setWrapMode',
  'lineCount', 'length', 'isCursorVisible', 'setCursorVisible',
  'cursorPosition', 'setCursorPosition', 'cursorDelegate',
  'setCursorDelegate', 'overwriteMode', 'setOverwriteMode', 'selectionStart',
  'selectionEnd', 'selectedText', 'focusOnPress', 'setFocusOnPress',
  'persistentSelection', 'setPersistentSelection', 'textMargin',
  'setTextMargin', 'inputMethodHints', 'setInputMethodHints',
  'selectByKeyboard', 'setSelectByKeyboard', 'selectByMouse',
  'setSelectByMouse', 'mouseSelectionMode', 'setMouseSelectionMode',
  'canPaste', 'canUndo', 'canRedo', 'componentComplete', 'resourcesLoading',
  'setReadOnly', 'isReadOnly', 'cursorRectangle', 'inputMethodQuery',
  'contentWidth', 'contentHeight', 'baseUrl', 'setBaseUrl', 'resetBaseUrl',
  'positionToRectangle', 'positionAt', 'moveCursorSelection',
  'cursorSelection', 'boundingRect', 'clipRect', 'isInputMethodComposing',
  'renderType', 'setRenderType', 'getText', 'getFormattedText',
  'textDocument', 'hoveredLink', 'linkAt', 'padding', 'setPadding',
  'resetPadding', 'topPadding', 'setTopPadding', 'resetTopPadding',
  'leftPadding', 'setLeftPadding', 'resetLeftPadding', 'rightPadding',
  'setRightPadding', 'resetRightPadding', 'bottomPadding',
  'setBottomPadding', 'resetBottomPadding', 'tabStopDistance',
  'setTabStopDistance', 'invalidate', 'textChanged', 'preeditTextChanged',
  'contentSizeChanged', 'cursorPositionChanged', 'cursorRectangleChanged',
  'selectionStartChanged', 'selectionEndChanged', 'selectedTextChanged',
  'colorChanged', 'selectionColorChanged', 'selectedTextColorChanged',
  'fontChanged', 'horizontalAlignmentChanged', 'verticalAlignmentChanged',
  'wrapModeChanged', 'lineCountChanged', 'textFormatChanged',
  'readOnlyChanged', 'cursorVisibleChanged', 'cursorDelegateChanged',
  'overwriteModeChanged', 'activeFocusOnPressChanged',
  'persistentSelectionChanged', 'textMarginChanged',
  'selectByKeyboardChanged', 'selectByMouseChanged',
  'mouseSelectionModeChanged', 'linkActivated', 'linkHovered',
  'canPasteChanged', 'canUndoChanged', 'canRedoChanged',
  'inputMethodComposingChanged', 'effectiveHorizontalAlignmentChanged',
  'baseUrlChanged', 'inputMethodHintsChanged', 'renderTypeChanged',
  'editingFinished', 'paddingChanged', 'topPaddingChanged',
  'leftPaddingChanged', 'rightPaddingChanged', 'bottomPaddingChanged',
  'tabStopDistanceChanged', 'textEdited', 'selectAll', 'selectWord',
  'select', 'deselect', 'isRightToLeft', 'cut', 'copy', 'paste', 'undo',
  'redo', 'insert', 'remove', 'append', 'clear', 'q_invalidate',
  'q_textChanged', 'q_contentsChange', 'updateSelection',
  'moveCursorDelegate', 'createCursor', 'q_canPasteChanged',
  'updateWholeDocument', 'invalidateBlock', 'updateCursor', 'q_linkHovered',
  'q_markerHovered', 'q_updateAlignment', 'updateSize', 'triggerPreprocess',
  'loadResource', 'resourceRequestFinished', 'markDirtyNodesForRange',
  'updateTotalLines', 'invalidateFontCaches', 'document', 'setDocument',
  'setOldSelectionDefault', 'geometryChange', 'itemChange', 'event',
  'keyPressEvent', 'keyReleaseEvent', 'focusInEvent', 'focusOutEvent',
  'hoverEnterEvent', 'hoverMoveEvent', 'hoverLeaveEvent', 'mousePressEvent',
  'mouseReleaseEvent', 'mouseDoubleClickEvent', 'mouseMoveEvent',
  'inputMethodEvent', 'updatePaintNode', 'updatePolish', 'd_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTextEdit::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickTextEdit::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickTextEdit::~QQuickTextEdit()': the destructor: Python never
    removes a C++ QQuickTextEdit.
  - Qt's 'QQuickTextEdit::QQuickTextEdit(QQuickTextEditPrivate &dd,
    QQuickItem *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QQuickTextEditPrivate *QQuickTextEdit::d_func() const': takes
    in Python what 'QQuickTextEditPrivate *QQuickTextEdit::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 208 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickTextEdit is created at the first use, not by
    'QQuickTextEdit(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTextEdit.
  - Qt tells when it has removed the C++ QQuickTextEdit. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickTextEdit, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class HAlignment(CuteNum):
    """
    The enum 'QQuickTextEdit::HAlignment' of Qt, with the 4 names Qt gives in
    it.
    """

    AlignLeft = Kee[int](1)
    AlignRight = Kee[int](2)
    AlignHCenter = Kee[int](4)
    AlignJustify = Kee[int](8)

  class RenderType(CuteNum):
    """
    The enum 'QQuickTextEdit::RenderType' of Qt, with the 3 names Qt gives in
    it.
    """

    QtRendering = Kee[int](0)
    NativeRendering = Kee[int](1)
    CurveRendering = Kee[int](2)

  class SelectionMode(CuteNum):
    """
    The enum 'QQuickTextEdit::SelectionMode' of Qt, with the 2 names Qt gives
    in it.
    """

    SelectCharacters = Kee[int](0)
    SelectWords = Kee[int](1)

  class TextFormat(CuteNum):
    """
    The enum 'QQuickTextEdit::TextFormat' of Qt, with the 4 names Qt gives in
    it.
    """

    PlainText = Kee[int](0)
    RichText = Kee[int](1)
    AutoText = Kee[int](2)
    MarkdownText = Kee[int](3)

  class VAlignment(CuteNum):
    """
    The enum 'QQuickTextEdit::VAlignment' of Qt, with the 3 names Qt gives in
    it.
    """

    AlignTop = Kee[int](32)
    AlignBottom = Kee[int](64)
    AlignVCenter = Kee[int](128)

  class WrapMode(CuteNum):
    """
    The enum 'QQuickTextEdit::WrapMode' of Qt, with the 5 names Qt gives in
    it.
    """

    NoWrap = Kee[int](0)
    WordWrap = Kee[int](1)
    WrapAnywhere = Kee[int](3)
    WrapAtWordBoundaryOrAnywhere = Kee[int](4)
    Wrap = Kee[int](4)

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
    Calls Qt's 'QString QQuickTextEdit::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#tr

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
    #  QString QQuickTextEdit::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuickTextEdit2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTextEdit'

  #  Qt's QQuickTextEdit is built on more than one class. The part of a C++
  #  QQuickTextEdit that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQuickTextInterface':
          'ritual_cast_QQuickTextEdit_QQuickTextInterface',
  }

  #  A C++ QQuickTextEdit Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickTextEdit'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickTextEdit::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTextEdit::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuickTextEdit10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def text(self) -> str:
    """
    Calls Qt's 'QString QQuickTextEdit::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextEdit::text() const
    return self.uglySide.call('ritual_ZNK14QQuickTextEdit4textEv')

  def preeditText(self) -> str:
    """
    Calls Qt's 'QString QQuickTextEdit::preeditText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#preeditText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextEdit::preeditText() const
    return self.uglySide.call('ritual_ZNK14QQuickTextEdit11preeditTextEv')

  def textFormat(self) -> TextFormat:
    """
    Calls Qt's 'TextFormat QQuickTextEdit::textFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#textFormat

    Returns
    -------

    TextFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TextFormat(number)'
      gives.
    """
    #  TextFormat QQuickTextEdit::textFormat() const
    return QQuickTextEdit.TextFormat(self.uglySide.call(
        'ritual_ZNK14QQuickTextEdit10textFormatEv',
    ))

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickTextEdit::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickTextEdit::font() const
    address = self.uglySide.call('ritual_ZNK14QQuickTextEdit4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickTextEdit::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickTextEdit::color() const
    address = self.uglySide.call('ritual_ZNK14QQuickTextEdit5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def selectionColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickTextEdit::selectionColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#selectionColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickTextEdit::selectionColor() const
    address = self.uglySide.call(
        'ritual_ZNK14QQuickTextEdit14selectionColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def selectedTextColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickTextEdit::selectedTextColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#selectedTextColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickTextEdit::selectedTextColor() const
    address = self.uglySide.call(
        'ritual_ZNK14QQuickTextEdit17selectedTextColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def hAlign(self) -> HAlignment:
    """
    Calls Qt's 'HAlignment QQuickTextEdit::hAlign() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#hAlign

    Returns
    -------

    HAlignment
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'HAlignment(number)'
      gives.
    """
    #  HAlignment QQuickTextEdit::hAlign() const
    return QQuickTextEdit.HAlignment(self.uglySide.call(
        'ritual_ZNK14QQuickTextEdit6hAlignEv',
    ))

  def effectiveHAlign(self) -> HAlignment:
    """
    Calls Qt's 'HAlignment QQuickTextEdit::effectiveHAlign() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#effectiveHAlign

    Returns
    -------

    HAlignment
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'HAlignment(number)'
      gives.
    """
    #  HAlignment QQuickTextEdit::effectiveHAlign() const
    return QQuickTextEdit.HAlignment(self.uglySide.call(
        'ritual_ZNK14QQuickTextEdit15effectiveHAlignEv',
    ))

  def vAlign(self) -> VAlignment:
    """
    Calls Qt's 'VAlignment QQuickTextEdit::vAlign() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#vAlign

    Returns
    -------

    VAlignment
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'VAlignment(number)'
      gives.
    """
    #  VAlignment QQuickTextEdit::vAlign() const
    return QQuickTextEdit.VAlignment(self.uglySide.call(
        'ritual_ZNK14QQuickTextEdit6vAlignEv',
    ))

  def wrapMode(self) -> WrapMode:
    """
    Calls Qt's 'WrapMode QQuickTextEdit::wrapMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#wrapMode

    Returns
    -------

    WrapMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'WrapMode(number)' gives.
    """
    #  WrapMode QQuickTextEdit::wrapMode() const
    return QQuickTextEdit.WrapMode(self.uglySide.call(
        'ritual_ZNK14QQuickTextEdit8wrapModeEv',
    ))

  def lineCount(self) -> int:
    """
    Calls Qt's 'int QQuickTextEdit::lineCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#lineCount
    """
    #  int QQuickTextEdit::lineCount() const
    return self.uglySide.call('ritual_ZNK14QQuickTextEdit9lineCountEv')

  def length(self) -> int:
    """
    Calls Qt's 'int QQuickTextEdit::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#length
    """
    #  int QQuickTextEdit::length() const
    return self.uglySide.call('ritual_ZNK14QQuickTextEdit6lengthEv')

  def isCursorVisible(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextEdit::isCursorVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#isCursorVisible
    """
    #  bool QQuickTextEdit::isCursorVisible() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickTextEdit15isCursorVisibleEv',
    )

  def cursorPosition(self) -> int:
    """
    Calls Qt's 'int QQuickTextEdit::cursorPosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#cursorPosition
    """
    #  int QQuickTextEdit::cursorPosition() const
    return self.uglySide.call('ritual_ZNK14QQuickTextEdit14cursorPositionEv')

  def cursorDelegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickTextEdit::cursorDelegate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#cursorDelegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickTextEdit::cursorDelegate() const
    address = self.uglySide.call(
        'ritual_ZNK14QQuickTextEdit14cursorDelegateEv',
    )
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def overwriteMode(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextEdit::overwriteMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#overwriteMode
    """
    #  bool QQuickTextEdit::overwriteMode() const
    return self.uglySide.call('ritual_ZNK14QQuickTextEdit13overwriteModeEv')

  def selectionStart(self) -> int:
    """
    Calls Qt's 'int QQuickTextEdit::selectionStart() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#selectionStart
    """
    #  int QQuickTextEdit::selectionStart() const
    return self.uglySide.call('ritual_ZNK14QQuickTextEdit14selectionStartEv')

  def selectionEnd(self) -> int:
    """
    Calls Qt's 'int QQuickTextEdit::selectionEnd() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#selectionEnd
    """
    #  int QQuickTextEdit::selectionEnd() const
    return self.uglySide.call('ritual_ZNK14QQuickTextEdit12selectionEndEv')

  def selectedText(self) -> str:
    """
    Calls Qt's 'QString QQuickTextEdit::selectedText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#selectedText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextEdit::selectedText() const
    return self.uglySide.call('ritual_ZNK14QQuickTextEdit12selectedTextEv')

  def focusOnPress(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextEdit::focusOnPress() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#focusOnPress
    """
    #  bool QQuickTextEdit::focusOnPress() const
    return self.uglySide.call('ritual_ZNK14QQuickTextEdit12focusOnPressEv')

  def persistentSelection(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextEdit::persistentSelection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#persistentSelection
    """
    #  bool QQuickTextEdit::persistentSelection() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickTextEdit19persistentSelectionEv',
    )

  def textMargin(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextEdit::textMargin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#textMargin
    """
    #  qreal QQuickTextEdit::textMargin() const
    return self.uglySide.call('ritual_ZNK14QQuickTextEdit10textMarginEv')

  def inputMethodHints(self) -> Qt.InputMethodHints:
    """
    Calls Qt's 'Qt::InputMethodHints QQuickTextEdit::inputMethodHints()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#inputMethodHints

    Returns
    -------

    Qt.InputMethodHints
      The value standing for the combination Qt gave back.
    """
    #  Qt::InputMethodHints QQuickTextEdit::inputMethodHints() const
    return Qt.InputMethodHints(self.uglySide.call(
        'ritual_ZNK14QQuickTextEdit16inputMethodHintsEv',
    ))

  def selectByKeyboard(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextEdit::selectByKeyboard() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#selectByKeyboard
    """
    #  bool QQuickTextEdit::selectByKeyboard() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickTextEdit16selectByKeyboardEv',
    )

  def selectByMouse(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextEdit::selectByMouse() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#selectByMouse
    """
    #  bool QQuickTextEdit::selectByMouse() const
    return self.uglySide.call('ritual_ZNK14QQuickTextEdit13selectByMouseEv')

  def mouseSelectionMode(self) -> SelectionMode:
    """
    Calls Qt's 'SelectionMode QQuickTextEdit::mouseSelectionMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#mouseSelectionMode

    Returns
    -------

    SelectionMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SelectionMode(number)'
      gives.
    """
    #  SelectionMode QQuickTextEdit::mouseSelectionMode() const
    return QQuickTextEdit.SelectionMode(self.uglySide.call(
        'ritual_ZNK14QQuickTextEdit18mouseSelectionModeEv',
    ))

  def canPaste(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextEdit::canPaste() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#canPaste
    """
    #  bool QQuickTextEdit::canPaste() const
    return self.uglySide.call('ritual_ZNK14QQuickTextEdit8canPasteEv')

  def canUndo(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextEdit::canUndo() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#canUndo
    """
    #  bool QQuickTextEdit::canUndo() const
    return self.uglySide.call('ritual_ZNK14QQuickTextEdit7canUndoEv')

  def canRedo(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextEdit::canRedo() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#canRedo
    """
    #  bool QQuickTextEdit::canRedo() const
    return self.uglySide.call('ritual_ZNK14QQuickTextEdit7canRedoEv')

  def resourcesLoading(self) -> int:
    """
    Calls Qt's 'int QQuickTextEdit::resourcesLoading() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#resourcesLoading
    """
    #  int QQuickTextEdit::resourcesLoading() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickTextEdit16resourcesLoadingEv',
    )

  def isReadOnly(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextEdit::isReadOnly() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#isReadOnly
    """
    #  bool QQuickTextEdit::isReadOnly() const
    return self.uglySide.call('ritual_ZNK14QQuickTextEdit10isReadOnlyEv')

  def cursorRectangle(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickTextEdit::cursorRectangle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#cursorRectangle

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickTextEdit::cursorRectangle() const
    address = self.uglySide.call(
        'ritual_ZNK14QQuickTextEdit15cursorRectangleEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(Qt.InputMethodQuery)
  def inputMethodQuery(self, property: Qt.InputMethodQuery) -> QVariant:
    """
    Calls Qt's 'QVariant
    QQuickTextEdit::inputMethodQuery(Qt::InputMethodQuery property) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#inputMethodQuery

    Parameters
    ----------

    property : Qt.InputMethodQuery
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickTextEdit::inputMethodQuery(Qt::InputMethodQuery
    #      property) const
    ritual = (
        'ritual_ZNK14QQuickTextEdit16inputMethodQueryEN2Qt16InputMethodQuer'
        'yE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QQuickTextEdit16inputMethodQueryEN2Qt16InputMeth'
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
    QQuickTextEdit::inputMethodQuery(Qt::InputMethodQuery query, QVariant
    argument) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#inputMethodQuery

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
    #  QVariant QQuickTextEdit::inputMethodQuery(Qt::InputMethodQuery query,
    #      QVariant argument) const
    address = self.uglySide.call(
        'ritual_ZNK14QQuickTextEdit16inputMethodQueryEN2Qt16InputMethodQuer'
        'yE8QVariant',
        query.value, self._valueOf(argument),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def contentWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextEdit::contentWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#contentWidth
    """
    #  qreal QQuickTextEdit::contentWidth() const
    return self.uglySide.call('ritual_ZNK14QQuickTextEdit12contentWidthEv')

  def contentHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextEdit::contentHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#contentHeight
    """
    #  qreal QQuickTextEdit::contentHeight() const
    return self.uglySide.call('ritual_ZNK14QQuickTextEdit13contentHeightEv')

  def baseUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickTextEdit::baseUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#baseUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickTextEdit::baseUrl() const
    address = self.uglySide.call('ritual_ZNK14QQuickTextEdit7baseUrlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  @overload(int)
  def positionToRectangle(self, a0: int) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickTextEdit::positionToRectangle(int a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#positionToRectangle

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickTextEdit::positionToRectangle(int a0) const
    address = self.uglySide.call(
        'ritual_ZNK14QQuickTextEdit19positionToRectangleEi', a0,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(float, float)
  def positionAt(self, x: float, y: float) -> int:
    """
    Calls Qt's 'int QQuickTextEdit::positionAt(qreal x, qreal y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#positionAt

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  int QQuickTextEdit::positionAt(qreal x, qreal y) const
    return self.uglySide.call(
        'ritual_ZNK14QQuickTextEdit10positionAtEdd', x, y,
    )

  def cursorSelection(self) -> Optional[QQuickTextSelection]:
    """
    Calls Qt's 'QQuickTextSelection *QQuickTextEdit::cursorSelection()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#cursorSelection

    Returns
    -------

    Optional[QQuickTextSelection]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextSelection *QQuickTextEdit::cursorSelection() const
    address = self.uglySide.call(
        'ritual_ZNK14QQuickTextEdit15cursorSelectionEv',
    )
    from . import QQuickTextSelection
    return QQuickTextSelection._cuteAt(address)

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickTextEdit::boundingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickTextEdit::boundingRect() const
    ritual = 'ritual_ZNK14QQuickTextEdit12boundingRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQuickTextEdit12boundingRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def clipRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickTextEdit::clipRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#clipRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickTextEdit::clipRect() const
    ritual = 'ritual_ZNK14QQuickTextEdit8clipRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQuickTextEdit8clipRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def isInputMethodComposing(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextEdit::isInputMethodComposing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#isInputMethodComposing
    """
    #  bool QQuickTextEdit::isInputMethodComposing() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickTextEdit22isInputMethodComposingEv',
    )

  def renderType(self) -> RenderType:
    """
    Calls Qt's 'RenderType QQuickTextEdit::renderType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#renderType

    Returns
    -------

    RenderType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RenderType(number)'
      gives.
    """
    #  RenderType QQuickTextEdit::renderType() const
    return QQuickTextEdit.RenderType(self.uglySide.call(
        'ritual_ZNK14QQuickTextEdit10renderTypeEv',
    ))

  @overload(int, int)
  def getText(self, start: int, end: int) -> str:
    """
    Calls Qt's 'QString QQuickTextEdit::getText(int start, int end) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#getText

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextEdit::getText(int start, int end) const
    return self.uglySide.call(
        'ritual_ZNK14QQuickTextEdit7getTextEii', start, end,
    )

  @overload(int, int)
  def getFormattedText(self, start: int, end: int) -> str:
    """
    Calls Qt's 'QString QQuickTextEdit::getFormattedText(int start, int end)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#getFormattedText

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextEdit::getFormattedText(int start, int end) const
    return self.uglySide.call(
        'ritual_ZNK14QQuickTextEdit16getFormattedTextEii', start, end,
    )

  def hoveredLink(self) -> str:
    """
    Calls Qt's 'QString QQuickTextEdit::hoveredLink() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#hoveredLink

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextEdit::hoveredLink() const
    return self.uglySide.call('ritual_ZNK14QQuickTextEdit11hoveredLinkEv')

  @overload(float, float)
  def linkAt(self, x: float, y: float) -> str:
    """
    Calls Qt's 'QString QQuickTextEdit::linkAt(qreal x, qreal y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#linkAt

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextEdit::linkAt(qreal x, qreal y) const
    return self.uglySide.call('ritual_ZNK14QQuickTextEdit6linkAtEdd', x, y)

  def padding(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextEdit::padding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#padding
    """
    #  qreal QQuickTextEdit::padding() const
    return self.uglySide.call('ritual_ZNK14QQuickTextEdit7paddingEv')

  def topPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextEdit::topPadding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#topPadding
    """
    #  qreal QQuickTextEdit::topPadding() const
    return self.uglySide.call('ritual_ZNK14QQuickTextEdit10topPaddingEv')

  def leftPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextEdit::leftPadding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#leftPadding
    """
    #  qreal QQuickTextEdit::leftPadding() const
    return self.uglySide.call('ritual_ZNK14QQuickTextEdit11leftPaddingEv')

  def rightPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextEdit::rightPadding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#rightPadding
    """
    #  qreal QQuickTextEdit::rightPadding() const
    return self.uglySide.call('ritual_ZNK14QQuickTextEdit12rightPaddingEv')

  def bottomPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextEdit::bottomPadding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#bottomPadding
    """
    #  qreal QQuickTextEdit::bottomPadding() const
    return self.uglySide.call('ritual_ZNK14QQuickTextEdit13bottomPaddingEv')

  def tabStopDistance(self) -> int:
    """
    Calls Qt's 'int QQuickTextEdit::tabStopDistance() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#tabStopDistance
    """
    #  int QQuickTextEdit::tabStopDistance() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickTextEdit15tabStopDistanceEv',
    )

  def document(self) -> Optional[QTextDocument]:
    """
    Calls Qt's 'QTextDocument *QQuickTextEdit::document() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#document

    Returns
    -------

    Optional[QTextDocument]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextDocument *QQuickTextEdit::document() const
    address = self.uglySide.call('ritual_ZNK14QQuickTextEdit8documentEv')
    from ..QtGui import QTextDocument
    return QTextDocument._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setText(self, a0: str) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::setText(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#setText

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickTextEdit::setText(const QString &a0)
    self.uglySide.call('ritual_ZN14QQuickTextEdit7setTextERK7QString', a0)

  @overload(TextFormat)
  def setTextFormat(self, format: TextFormat) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::setTextFormat(TextFormat format)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#setTextFormat

    Parameters
    ----------

    format : TextFormat
      Passed on as its number.
    """
    #  void QQuickTextEdit::setTextFormat(TextFormat format)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit13setTextFormatENS_10TextFormatE',
        format.value,
    )

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::setFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickTextEdit::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit7setFontERK5QFont', self._valueOf(font),
    )

  @overload(QColor)
  def setColor(self, c: QColor) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::setColor(const QColor &c)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#setColor

    Parameters
    ----------

    c : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickTextEdit::setColor(const QColor &c)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit8setColorERK6QColor', self._valueOf(c),
    )

  @overload(QColor)
  def setSelectionColor(self, c: QColor) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::setSelectionColor(const QColor &c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#setSelectionColor

    Parameters
    ----------

    c : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickTextEdit::setSelectionColor(const QColor &c)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit17setSelectionColorERK6QColor',
        self._valueOf(c),
    )

  @overload(QColor)
  def setSelectedTextColor(self, c: QColor) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::setSelectedTextColor(const QColor &c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#setSelectedTextColor

    Parameters
    ----------

    c : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickTextEdit::setSelectedTextColor(const QColor &c)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit20setSelectedTextColorERK6QColor',
        self._valueOf(c),
    )

  @overload(HAlignment)
  def setHAlign(self, align: HAlignment) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::setHAlign(HAlignment align)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#setHAlign

    Parameters
    ----------

    align : HAlignment
      Passed on as its number.
    """
    #  void QQuickTextEdit::setHAlign(HAlignment align)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit9setHAlignENS_10HAlignmentE', align.value,
    )

  @overload(VAlignment)
  def setVAlign(self, align: VAlignment) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::setVAlign(VAlignment align)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#setVAlign

    Parameters
    ----------

    align : VAlignment
      Passed on as its number.
    """
    #  void QQuickTextEdit::setVAlign(VAlignment align)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit9setVAlignENS_10VAlignmentE', align.value,
    )

  @overload(WrapMode)
  def setWrapMode(self, w: WrapMode) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::setWrapMode(WrapMode w)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#setWrapMode

    Parameters
    ----------

    w : WrapMode
      Passed on as its number.
    """
    #  void QQuickTextEdit::setWrapMode(WrapMode w)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit11setWrapModeENS_8WrapModeE', w.value,
    )

  @overload(bool)
  def setCursorVisible(self, on: bool) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::setCursorVisible(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#setCursorVisible

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickTextEdit::setCursorVisible(bool on)
    self.uglySide.call('ritual_ZN14QQuickTextEdit16setCursorVisibleEb', on)

  @overload(int)
  def setCursorPosition(self, pos: int) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::setCursorPosition(int pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#setCursorPosition

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  void QQuickTextEdit::setCursorPosition(int pos)
    self.uglySide.call('ritual_ZN14QQuickTextEdit17setCursorPositionEi', pos)

  @overload(QQmlComponent)
  @overload(NoneType)
  def setCursorDelegate(self, a0: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::setCursorDelegate(QQmlComponent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#setCursorDelegate

    Parameters
    ----------

    a0 : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextEdit::setCursorDelegate(QQmlComponent *a0)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit17setCursorDelegateEP13QQmlComponent',
        self._addressOf(a0),
    )

  @overload(bool)
  def setOverwriteMode(self, overwrite: bool) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::setOverwriteMode(bool overwrite)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#setOverwriteMode

    Parameters
    ----------

    overwrite : bool
      Passed on as it is.
    """
    #  void QQuickTextEdit::setOverwriteMode(bool overwrite)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit16setOverwriteModeEb', overwrite,
    )

  @overload(bool)
  def setFocusOnPress(self, on: bool) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::setFocusOnPress(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#setFocusOnPress

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickTextEdit::setFocusOnPress(bool on)
    self.uglySide.call('ritual_ZN14QQuickTextEdit15setFocusOnPressEb', on)

  @overload(bool)
  def setPersistentSelection(self, on: bool) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::setPersistentSelection(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#setPersistentSelection

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickTextEdit::setPersistentSelection(bool on)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit22setPersistentSelectionEb', on,
    )

  @overload(float)
  def setTextMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::setTextMargin(qreal margin)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#setTextMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void QQuickTextEdit::setTextMargin(qreal margin)
    self.uglySide.call('ritual_ZN14QQuickTextEdit13setTextMarginEd', margin)

  @overload(Qt.InputMethodHints)
  def setInputMethodHints(self, hints: Qt.InputMethodHints) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::setInputMethodHints(Qt::InputMethodHints
    hints)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#setInputMethodHints

    Parameters
    ----------

    hints : Qt.InputMethodHints
      Passed on as its number.
    """
    #  void QQuickTextEdit::setInputMethodHints(Qt::InputMethodHints hints)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit19setInputMethodHintsE6QFlagsIN2Qt15Input'
        'MethodHintEE',
        hints.value,
    )

  @overload(bool)
  def setSelectByKeyboard(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::setSelectByKeyboard(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#setSelectByKeyboard

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickTextEdit::setSelectByKeyboard(bool a0)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit19setSelectByKeyboardEb', a0,
    )

  @overload(bool)
  def setSelectByMouse(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::setSelectByMouse(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#setSelectByMouse

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickTextEdit::setSelectByMouse(bool a0)
    self.uglySide.call('ritual_ZN14QQuickTextEdit16setSelectByMouseEb', a0)

  @overload(SelectionMode)
  def setMouseSelectionMode(self, mode: SelectionMode) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::setMouseSelectionMode(SelectionMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#setMouseSelectionMode

    Parameters
    ----------

    mode : SelectionMode
      Passed on as its number.
    """
    #  void QQuickTextEdit::setMouseSelectionMode(SelectionMode mode)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit21setMouseSelectionModeENS_13SelectionMod'
        'eE',
        mode.value,
    )

  @overload(bool)
  def setReadOnly(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::setReadOnly(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#setReadOnly

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickTextEdit::setReadOnly(bool a0)
    self.uglySide.call('ritual_ZN14QQuickTextEdit11setReadOnlyEb', a0)

  @overload(QUrl)
  def setBaseUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::setBaseUrl(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#setBaseUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickTextEdit::setBaseUrl(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit10setBaseUrlERK4QUrl', self._valueOf(url),
    )

  @overload(RenderType)
  def setRenderType(self, renderType: RenderType) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::setRenderType(RenderType renderType)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#setRenderType

    Parameters
    ----------

    renderType : RenderType
      Passed on as its number.
    """
    #  void QQuickTextEdit::setRenderType(RenderType renderType)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit13setRenderTypeENS_10RenderTypeE',
        renderType.value,
    )

  @overload(float)
  def setPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::setPadding(qreal padding)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#setPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickTextEdit::setPadding(qreal padding)
    self.uglySide.call('ritual_ZN14QQuickTextEdit10setPaddingEd', padding)

  @overload(float)
  def setTopPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::setTopPadding(qreal padding)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#setTopPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickTextEdit::setTopPadding(qreal padding)
    self.uglySide.call('ritual_ZN14QQuickTextEdit13setTopPaddingEd', padding)

  @overload(float)
  def setLeftPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::setLeftPadding(qreal padding)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#setLeftPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickTextEdit::setLeftPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit14setLeftPaddingEd', padding,
    )

  @overload(float)
  def setRightPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::setRightPadding(qreal padding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#setRightPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickTextEdit::setRightPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit15setRightPaddingEd', padding,
    )

  @overload(float)
  def setBottomPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::setBottomPadding(qreal padding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#setBottomPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickTextEdit::setBottomPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit16setBottomPaddingEd', padding,
    )

  @overload(float)
  def setTabStopDistance(self, distance: float) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::setTabStopDistance(qreal distance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#setTabStopDistance

    Parameters
    ----------

    distance : float
      Passed on as it is.
    """
    #  void QQuickTextEdit::setTabStopDistance(qreal distance)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit18setTabStopDistanceEd', distance,
    )

  @overload(QTextDocument)
  @overload(NoneType)
  def setDocument(self, doc: Optional[QTextDocument]) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::setDocument(QTextDocument *doc)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#setDocument

    Parameters
    ----------

    doc : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextEdit::setDocument(QTextDocument *doc)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit11setDocumentEP13QTextDocument',
        self._addressOf(doc),
    )

  def setOldSelectionDefault(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::setOldSelectionDefault()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#setOldSelectionDefault
    """
    #  void QQuickTextEdit::setOldSelectionDefault()
    self.uglySide.call('ritual_ZN14QQuickTextEdit22setOldSelectionDefaultEv')

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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickTextEdit::QQuickTextEdit(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#QQuickTextEdit

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickTextEdit::QQuickTextEdit(QQuickItem *parent)
    self._noteCreation(QQuickTextEdit, lambda: Rituals.call(
        'ritual_ZN14QQuickTextEditC1EP10QQuickItem', self._addressOf(parent),
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

  def resetHAlign(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::resetHAlign()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#resetHAlign
    """
    #  void QQuickTextEdit::resetHAlign()
    self.uglySide.call('ritual_ZN14QQuickTextEdit11resetHAlignEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#componentComplete
    """
    #  void QQuickTextEdit::componentComplete()
    ritual = 'ritual_ZN14QQuickTextEdit17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickTextEdit17componentCompleteEv'
    self.uglySide.call(ritual)

  def resetBaseUrl(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::resetBaseUrl()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#resetBaseUrl
    """
    #  void QQuickTextEdit::resetBaseUrl()
    self.uglySide.call('ritual_ZN14QQuickTextEdit12resetBaseUrlEv')

  @overload(int)
  def moveCursorSelection(self, pos: int) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::moveCursorSelection(int pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#moveCursorSelection

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  void QQuickTextEdit::moveCursorSelection(int pos)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit19moveCursorSelectionEi', pos,
    )

  @overload(int, SelectionMode)
  def moveCursorSelection(self, pos: int, mode: SelectionMode) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::moveCursorSelection(int pos,
    QQuickTextEdit::SelectionMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#moveCursorSelection

    Parameters
    ----------

    pos : int
      Passed on as it is.

    mode : SelectionMode
      Passed on as its number.
    """
    #  void QQuickTextEdit::moveCursorSelection(int pos,
    #      QQuickTextEdit::SelectionMode mode)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit19moveCursorSelectionEiNS_13SelectionMode'
        'E',
        pos, mode.value,
    )

  def textDocument(self) -> Optional[QQuickTextDocument]:
    """
    Calls Qt's 'QQuickTextDocument *QQuickTextEdit::textDocument()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#textDocument

    Returns
    -------

    Optional[QQuickTextDocument]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextDocument *QQuickTextEdit::textDocument()
    address = self.uglySide.call('ritual_ZN14QQuickTextEdit12textDocumentEv')
    from . import QQuickTextDocument
    return QQuickTextDocument._cuteAt(address)

  def resetPadding(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::resetPadding()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#resetPadding
    """
    #  void QQuickTextEdit::resetPadding()
    self.uglySide.call('ritual_ZN14QQuickTextEdit12resetPaddingEv')

  def resetTopPadding(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::resetTopPadding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#resetTopPadding
    """
    #  void QQuickTextEdit::resetTopPadding()
    self.uglySide.call('ritual_ZN14QQuickTextEdit15resetTopPaddingEv')

  def resetLeftPadding(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::resetLeftPadding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#resetLeftPadding
    """
    #  void QQuickTextEdit::resetLeftPadding()
    self.uglySide.call('ritual_ZN14QQuickTextEdit16resetLeftPaddingEv')

  def resetRightPadding(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::resetRightPadding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#resetRightPadding
    """
    #  void QQuickTextEdit::resetRightPadding()
    self.uglySide.call('ritual_ZN14QQuickTextEdit17resetRightPaddingEv')

  def resetBottomPadding(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::resetBottomPadding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#resetBottomPadding
    """
    #  void QQuickTextEdit::resetBottomPadding()
    self.uglySide.call('ritual_ZN14QQuickTextEdit18resetBottomPaddingEv')

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::invalidate()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#invalidate
    """
    #  void QQuickTextEdit::invalidate()
    ritual = 'ritual_ZN14QQuickTextEdit10invalidateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickTextEdit10invalidateEv'
    self.uglySide.call(ritual)

  def textChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::textChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#textChanged
    """
    #  void QQuickTextEdit::textChanged()
    self.uglySide.call('ritual_ZN14QQuickTextEdit11textChangedEv')

  def preeditTextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::preeditTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#preeditTextChanged
    """
    #  void QQuickTextEdit::preeditTextChanged()
    self.uglySide.call('ritual_ZN14QQuickTextEdit18preeditTextChangedEv')

  def contentSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::contentSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#contentSizeChanged
    """
    #  void QQuickTextEdit::contentSizeChanged()
    self.uglySide.call('ritual_ZN14QQuickTextEdit18contentSizeChangedEv')

  def cursorPositionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::cursorPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#cursorPositionChanged
    """
    #  void QQuickTextEdit::cursorPositionChanged()
    self.uglySide.call('ritual_ZN14QQuickTextEdit21cursorPositionChangedEv')

  def cursorRectangleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::cursorRectangleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#cursorRectangleChanged
    """
    #  void QQuickTextEdit::cursorRectangleChanged()
    self.uglySide.call('ritual_ZN14QQuickTextEdit22cursorRectangleChangedEv')

  def selectionStartChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::selectionStartChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#selectionStartChanged
    """
    #  void QQuickTextEdit::selectionStartChanged()
    self.uglySide.call('ritual_ZN14QQuickTextEdit21selectionStartChangedEv')

  def selectionEndChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::selectionEndChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#selectionEndChanged
    """
    #  void QQuickTextEdit::selectionEndChanged()
    self.uglySide.call('ritual_ZN14QQuickTextEdit19selectionEndChangedEv')

  def selectedTextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::selectedTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#selectedTextChanged
    """
    #  void QQuickTextEdit::selectedTextChanged()
    self.uglySide.call('ritual_ZN14QQuickTextEdit19selectedTextChangedEv')

  @overload(QColor)
  def colorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::colorChanged(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#colorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickTextEdit::colorChanged(const QColor &color)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit12colorChangedERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def selectionColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::selectionColorChanged(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#selectionColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickTextEdit::selectionColorChanged(const QColor &color)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit21selectionColorChangedERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def selectedTextColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::selectedTextColorChanged(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#selectedTextColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickTextEdit::selectedTextColorChanged(const QColor &color)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit24selectedTextColorChangedERK6QColor',
        self._valueOf(color),
    )

  @overload(QFont)
  def fontChanged(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::fontChanged(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#fontChanged

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickTextEdit::fontChanged(const QFont &font)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit11fontChangedERK5QFont',
        self._valueOf(font),
    )

  @overload(HAlignment)
  def horizontalAlignmentChanged(self, alignment: HAlignment) -> None:
    """
    Calls Qt's 'void
    QQuickTextEdit::horizontalAlignmentChanged(QQuickTextEdit::HAlignment
    alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#horizontalAlignmentChanged

    Parameters
    ----------

    alignment : HAlignment
      Passed on as its number.
    """
    #  void QQuickTextEdit::horizontalAlignmentChanged(QQuickTextEdit::
    #      HAlignment alignment)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit26horizontalAlignmentChangedENS_10HAlignm'
        'entE',
        alignment.value,
    )

  @overload(VAlignment)
  def verticalAlignmentChanged(self, alignment: VAlignment) -> None:
    """
    Calls Qt's 'void
    QQuickTextEdit::verticalAlignmentChanged(QQuickTextEdit::VAlignment
    alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#verticalAlignmentChanged

    Parameters
    ----------

    alignment : VAlignment
      Passed on as its number.
    """
    #  void QQuickTextEdit::verticalAlignmentChanged(QQuickTextEdit::
    #      VAlignment alignment)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit24verticalAlignmentChangedENS_10VAlignmen'
        'tE',
        alignment.value,
    )

  def wrapModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::wrapModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#wrapModeChanged
    """
    #  void QQuickTextEdit::wrapModeChanged()
    self.uglySide.call('ritual_ZN14QQuickTextEdit15wrapModeChangedEv')

  def lineCountChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::lineCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#lineCountChanged
    """
    #  void QQuickTextEdit::lineCountChanged()
    self.uglySide.call('ritual_ZN14QQuickTextEdit16lineCountChangedEv')

  @overload(TextFormat)
  def textFormatChanged(self, textFormat: TextFormat) -> None:
    """
    Calls Qt's 'void
    QQuickTextEdit::textFormatChanged(QQuickTextEdit::TextFormat
    textFormat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#textFormatChanged

    Parameters
    ----------

    textFormat : TextFormat
      Passed on as its number.
    """
    #  void QQuickTextEdit::textFormatChanged(QQuickTextEdit::TextFormat
    #      textFormat)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit17textFormatChangedENS_10TextFormatE',
        textFormat.value,
    )

  @overload(bool)
  def readOnlyChanged(self, isReadOnly: bool) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::readOnlyChanged(bool isReadOnly)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#readOnlyChanged

    Parameters
    ----------

    isReadOnly : bool
      Passed on as it is.
    """
    #  void QQuickTextEdit::readOnlyChanged(bool isReadOnly)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit15readOnlyChangedEb', isReadOnly,
    )

  @overload(bool)
  def cursorVisibleChanged(self, isCursorVisible: bool) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::cursorVisibleChanged(bool
    isCursorVisible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#cursorVisibleChanged

    Parameters
    ----------

    isCursorVisible : bool
      Passed on as it is.
    """
    #  void QQuickTextEdit::cursorVisibleChanged(bool isCursorVisible)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit20cursorVisibleChangedEb', isCursorVisible,
    )

  def cursorDelegateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::cursorDelegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#cursorDelegateChanged
    """
    #  void QQuickTextEdit::cursorDelegateChanged()
    self.uglySide.call('ritual_ZN14QQuickTextEdit21cursorDelegateChangedEv')

  @overload(bool)
  def overwriteModeChanged(self, overwriteMode: bool) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::overwriteModeChanged(bool
    overwriteMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#overwriteModeChanged

    Parameters
    ----------

    overwriteMode : bool
      Passed on as it is.
    """
    #  void QQuickTextEdit::overwriteModeChanged(bool overwriteMode)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit20overwriteModeChangedEb', overwriteMode,
    )

  @overload(bool)
  def activeFocusOnPressChanged(self, activeFocusOnPressed: bool) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::activeFocusOnPressChanged(bool
    activeFocusOnPressed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#activeFocusOnPressChanged

    Parameters
    ----------

    activeFocusOnPressed : bool
      Passed on as it is.
    """
    #  void QQuickTextEdit::activeFocusOnPressChanged(bool
    #      activeFocusOnPressed)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit25activeFocusOnPressChangedEb',
        activeFocusOnPressed,
    )

  @overload(bool)
  def persistentSelectionChanged(self, isPersistentSelection: bool) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::persistentSelectionChanged(bool
    isPersistentSelection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#persistentSelectionChanged

    Parameters
    ----------

    isPersistentSelection : bool
      Passed on as it is.
    """
    #  void QQuickTextEdit::persistentSelectionChanged(bool
    #      isPersistentSelection)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit26persistentSelectionChangedEb',
        isPersistentSelection,
    )

  @overload(float)
  def textMarginChanged(self, textMargin: float) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::textMarginChanged(qreal textMargin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#textMarginChanged

    Parameters
    ----------

    textMargin : float
      Passed on as it is.
    """
    #  void QQuickTextEdit::textMarginChanged(qreal textMargin)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit17textMarginChangedEd', textMargin,
    )

  @overload(bool)
  def selectByKeyboardChanged(self, selectByKeyboard: bool) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::selectByKeyboardChanged(bool
    selectByKeyboard)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#selectByKeyboardChanged

    Parameters
    ----------

    selectByKeyboard : bool
      Passed on as it is.
    """
    #  void QQuickTextEdit::selectByKeyboardChanged(bool selectByKeyboard)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit23selectByKeyboardChangedEb',
        selectByKeyboard,
    )

  @overload(bool)
  def selectByMouseChanged(self, selectByMouse: bool) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::selectByMouseChanged(bool
    selectByMouse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#selectByMouseChanged

    Parameters
    ----------

    selectByMouse : bool
      Passed on as it is.
    """
    #  void QQuickTextEdit::selectByMouseChanged(bool selectByMouse)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit20selectByMouseChangedEb', selectByMouse,
    )

  @overload(SelectionMode)
  def mouseSelectionModeChanged(self, mode: SelectionMode) -> None:
    """
    Calls Qt's 'void
    QQuickTextEdit::mouseSelectionModeChanged(QQuickTextEdit::SelectionMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#mouseSelectionModeChanged

    Parameters
    ----------

    mode : SelectionMode
      Passed on as its number.
    """
    #  void QQuickTextEdit::mouseSelectionModeChanged(QQuickTextEdit::
    #      SelectionMode mode)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit25mouseSelectionModeChangedENS_13Selectio'
        'nModeE',
        mode.value,
    )

  @overload(str)
  def linkActivated(self, link: str) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::linkActivated(const QString &link)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#linkActivated

    Parameters
    ----------

    link : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickTextEdit::linkActivated(const QString &link)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit13linkActivatedERK7QString', link,
    )

  @overload(str)
  def linkHovered(self, link: str) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::linkHovered(const QString &link)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#linkHovered

    Parameters
    ----------

    link : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickTextEdit::linkHovered(const QString &link)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit11linkHoveredERK7QString', link,
    )

  def canPasteChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::canPasteChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#canPasteChanged
    """
    #  void QQuickTextEdit::canPasteChanged()
    self.uglySide.call('ritual_ZN14QQuickTextEdit15canPasteChangedEv')

  def canUndoChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::canUndoChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#canUndoChanged
    """
    #  void QQuickTextEdit::canUndoChanged()
    self.uglySide.call('ritual_ZN14QQuickTextEdit14canUndoChangedEv')

  def canRedoChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::canRedoChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#canRedoChanged
    """
    #  void QQuickTextEdit::canRedoChanged()
    self.uglySide.call('ritual_ZN14QQuickTextEdit14canRedoChangedEv')

  def inputMethodComposingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::inputMethodComposingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#inputMethodComposingChanged
    """
    #  void QQuickTextEdit::inputMethodComposingChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit27inputMethodComposingChangedEv',
    )

  def effectiveHorizontalAlignmentChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::effectiveHorizontalAlignmentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html
    """
    #  void QQuickTextEdit::effectiveHorizontalAlignmentChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit35effectiveHorizontalAlignmentChangedEv',
    )

  def baseUrlChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::baseUrlChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#baseUrlChanged
    """
    #  void QQuickTextEdit::baseUrlChanged()
    self.uglySide.call('ritual_ZN14QQuickTextEdit14baseUrlChangedEv')

  def inputMethodHintsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::inputMethodHintsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#inputMethodHintsChanged
    """
    #  void QQuickTextEdit::inputMethodHintsChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit23inputMethodHintsChangedEv',
    )

  def renderTypeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::renderTypeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#renderTypeChanged
    """
    #  void QQuickTextEdit::renderTypeChanged()
    self.uglySide.call('ritual_ZN14QQuickTextEdit17renderTypeChangedEv')

  def editingFinished(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::editingFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#editingFinished
    """
    #  void QQuickTextEdit::editingFinished()
    self.uglySide.call('ritual_ZN14QQuickTextEdit15editingFinishedEv')

  def paddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::paddingChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#paddingChanged
    """
    #  void QQuickTextEdit::paddingChanged()
    self.uglySide.call('ritual_ZN14QQuickTextEdit14paddingChangedEv')

  def topPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::topPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#topPaddingChanged
    """
    #  void QQuickTextEdit::topPaddingChanged()
    self.uglySide.call('ritual_ZN14QQuickTextEdit17topPaddingChangedEv')

  def leftPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::leftPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#leftPaddingChanged
    """
    #  void QQuickTextEdit::leftPaddingChanged()
    self.uglySide.call('ritual_ZN14QQuickTextEdit18leftPaddingChangedEv')

  def rightPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::rightPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#rightPaddingChanged
    """
    #  void QQuickTextEdit::rightPaddingChanged()
    self.uglySide.call('ritual_ZN14QQuickTextEdit19rightPaddingChangedEv')

  def bottomPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::bottomPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#bottomPaddingChanged
    """
    #  void QQuickTextEdit::bottomPaddingChanged()
    self.uglySide.call('ritual_ZN14QQuickTextEdit20bottomPaddingChangedEv')

  @overload(float)
  def tabStopDistanceChanged(self, distance: float) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::tabStopDistanceChanged(qreal distance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#tabStopDistanceChanged

    Parameters
    ----------

    distance : float
      Passed on as it is.
    """
    #  void QQuickTextEdit::tabStopDistanceChanged(qreal distance)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit22tabStopDistanceChangedEd', distance,
    )

  def textEdited(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::textEdited()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#textEdited
    """
    #  void QQuickTextEdit::textEdited()
    self.uglySide.call('ritual_ZN14QQuickTextEdit10textEditedEv')

  def selectAll(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::selectAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#selectAll
    """
    #  void QQuickTextEdit::selectAll()
    self.uglySide.call('ritual_ZN14QQuickTextEdit9selectAllEv')

  def selectWord(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::selectWord()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#selectWord
    """
    #  void QQuickTextEdit::selectWord()
    self.uglySide.call('ritual_ZN14QQuickTextEdit10selectWordEv')

  @overload(int, int)
  def select(self, start: int, end: int) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::select(int start, int end)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#select

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QQuickTextEdit::select(int start, int end)
    self.uglySide.call('ritual_ZN14QQuickTextEdit6selectEii', start, end)

  def deselect(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::deselect()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#deselect
    """
    #  void QQuickTextEdit::deselect()
    self.uglySide.call('ritual_ZN14QQuickTextEdit8deselectEv')

  @overload(int, int)
  def isRightToLeft(self, start: int, end: int) -> bool:
    """
    Calls Qt's 'bool QQuickTextEdit::isRightToLeft(int start, int end)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#isRightToLeft

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  bool QQuickTextEdit::isRightToLeft(int start, int end)
    return self.uglySide.call(
        'ritual_ZN14QQuickTextEdit13isRightToLeftEii', start, end,
    )

  def cut(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::cut()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#cut
    """
    #  void QQuickTextEdit::cut()
    self.uglySide.call('ritual_ZN14QQuickTextEdit3cutEv')

  def copy(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::copy()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#copy
    """
    #  void QQuickTextEdit::copy()
    self.uglySide.call('ritual_ZN14QQuickTextEdit4copyEv')

  def paste(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::paste()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#paste
    """
    #  void QQuickTextEdit::paste()
    self.uglySide.call('ritual_ZN14QQuickTextEdit5pasteEv')

  def undo(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::undo()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#undo
    """
    #  void QQuickTextEdit::undo()
    self.uglySide.call('ritual_ZN14QQuickTextEdit4undoEv')

  def redo(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::redo()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#redo
    """
    #  void QQuickTextEdit::redo()
    self.uglySide.call('ritual_ZN14QQuickTextEdit4redoEv')

  @overload(int, str)
  def insert(self, position: int, text: str) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::insert(int position, const QString
    &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#insert

    Parameters
    ----------

    position : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickTextEdit::insert(int position, const QString &text)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit6insertEiRK7QString', position, text,
    )

  @overload(int, int)
  def remove(self, start: int, end: int) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::remove(int start, int end)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#remove

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QQuickTextEdit::remove(int start, int end)
    self.uglySide.call('ritual_ZN14QQuickTextEdit6removeEii', start, end)

  @overload(str)
  def append(self, text: str) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::append(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#append

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickTextEdit::append(const QString &text)
    self.uglySide.call('ritual_ZN14QQuickTextEdit6appendERK7QString', text)

  def clear(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#clear
    """
    #  void QQuickTextEdit::clear()
    self.uglySide.call('ritual_ZN14QQuickTextEdit5clearEv')

  def q_invalidate(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::q_invalidate()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#q_invalidate
    """
    #  void QQuickTextEdit::q_invalidate()
    self.uglySide.call('ritual_ZN14QQuickTextEdit12q_invalidateEv')

  def q_textChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::q_textChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#q_textChanged
    """
    #  void QQuickTextEdit::q_textChanged()
    self.uglySide.call('ritual_ZN14QQuickTextEdit13q_textChangedEv')

  @overload(int, int, int)
  def q_contentsChange(self, a0: int, a1: int, a2: int) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::q_contentsChange(int a0, int a1, int
    a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#q_contentsChange

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.
    """
    #  void QQuickTextEdit::q_contentsChange(int a0, int a1, int a2)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit16q_contentsChangeEiii', a0, a1, a2,
    )

  def updateSelection(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::updateSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#updateSelection
    """
    #  void QQuickTextEdit::updateSelection()
    self.uglySide.call('ritual_ZN14QQuickTextEdit15updateSelectionEv')

  def moveCursorDelegate(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::moveCursorDelegate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#moveCursorDelegate
    """
    #  void QQuickTextEdit::moveCursorDelegate()
    self.uglySide.call('ritual_ZN14QQuickTextEdit18moveCursorDelegateEv')

  def createCursor(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::createCursor()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#createCursor
    """
    #  void QQuickTextEdit::createCursor()
    self.uglySide.call('ritual_ZN14QQuickTextEdit12createCursorEv')

  def q_canPasteChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::q_canPasteChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#q_canPasteChanged
    """
    #  void QQuickTextEdit::q_canPasteChanged()
    self.uglySide.call('ritual_ZN14QQuickTextEdit17q_canPasteChangedEv')

  def updateWholeDocument(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::updateWholeDocument()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#updateWholeDocument
    """
    #  void QQuickTextEdit::updateWholeDocument()
    self.uglySide.call('ritual_ZN14QQuickTextEdit19updateWholeDocumentEv')

  @overload(QTextBlock)
  def invalidateBlock(self, block: QTextBlock) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::invalidateBlock(const QTextBlock
    &block)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#invalidateBlock

    Parameters
    ----------

    block : QTextBlock
      Passed on as a value: Qt reads the C++ QTextBlock, which stays Python's
      own.
    """
    #  void QQuickTextEdit::invalidateBlock(const QTextBlock &block)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit15invalidateBlockERK10QTextBlock',
        self._valueOf(block),
    )

  def updateCursor(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::updateCursor()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#updateCursor
    """
    #  void QQuickTextEdit::updateCursor()
    self.uglySide.call('ritual_ZN14QQuickTextEdit12updateCursorEv')

  @overload(str)
  def q_linkHovered(self, link: str) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::q_linkHovered(const QString &link)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#q_linkHovered

    Parameters
    ----------

    link : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickTextEdit::q_linkHovered(const QString &link)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit13q_linkHoveredERK7QString', link,
    )

  @overload(bool)
  def q_markerHovered(self, hovered: bool) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::q_markerHovered(bool hovered)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#q_markerHovered

    Parameters
    ----------

    hovered : bool
      Passed on as it is.
    """
    #  void QQuickTextEdit::q_markerHovered(bool hovered)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit15q_markerHoveredEb', hovered,
    )

  def q_updateAlignment(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::q_updateAlignment()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#q_updateAlignment
    """
    #  void QQuickTextEdit::q_updateAlignment()
    self.uglySide.call('ritual_ZN14QQuickTextEdit17q_updateAlignmentEv')

  def updateSize(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::updateSize()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#updateSize
    """
    #  void QQuickTextEdit::updateSize()
    self.uglySide.call('ritual_ZN14QQuickTextEdit10updateSizeEv')

  def triggerPreprocess(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::triggerPreprocess()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#triggerPreprocess
    """
    #  void QQuickTextEdit::triggerPreprocess()
    self.uglySide.call('ritual_ZN14QQuickTextEdit17triggerPreprocessEv')

  @overload(int, QUrl)
  def loadResource(self, type: int, source: QUrl) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickTextEdit::loadResource(int type, const QUrl
    &source)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#loadResource

    Parameters
    ----------

    type : int
      Passed on as it is.

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickTextEdit::loadResource(int type, const QUrl &source)
    address = self.uglySide.call(
        'ritual_ZN14QQuickTextEdit12loadResourceEiRK4QUrl',
        type, self._valueOf(source),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def resourceRequestFinished(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::resourceRequestFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#resourceRequestFinished
    """
    #  void QQuickTextEdit::resourceRequestFinished()
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit23resourceRequestFinishedEv',
    )

  @overload(int, int, int)
  def markDirtyNodesForRange(
      self,
      start: int,
      end: int,
      charDelta: int,
  ) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::markDirtyNodesForRange(int start, int
    end, int charDelta)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#markDirtyNodesForRange

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.

    charDelta : int
      Passed on as it is.
    """
    #  void QQuickTextEdit::markDirtyNodesForRange(int start, int end, int
    #      charDelta)
    self.uglySide.call(
        'ritual_ZN14QQuickTextEdit22markDirtyNodesForRangeEiii',
        start, end, charDelta,
    )

  def updateTotalLines(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::updateTotalLines()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#updateTotalLines
    """
    #  void QQuickTextEdit::updateTotalLines()
    self.uglySide.call('ritual_ZN14QQuickTextEdit16updateTotalLinesEv')

  def invalidateFontCaches(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::invalidateFontCaches()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#invalidateFontCaches
    """
    #  void QQuickTextEdit::invalidateFontCaches()
    self.uglySide.call('ritual_ZN14QQuickTextEdit20invalidateFontCachesEv')

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickTextEdit::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN14QQuickTextEdit14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickTextEdit14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      value: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::itemChange(ItemChange change, const
    ItemChangeData &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    value : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickTextEdit::itemChange(ItemChange change, const
    #      ItemChangeData &value)
    ritual = (
        'ritual_ZN14QQuickTextEdit10itemChangeEN10QQuickItem10ItemChangeERK'
        'NS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickTextEdit10itemChangeEN10QQuickItem10ItemCha'
          'ngeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(value))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickTextEdit::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickTextEdit::event(QEvent *a0)
    ritual = 'ritual_ZN14QQuickTextEdit5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickTextEdit5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, a0: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::keyPressEvent(QKeyEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#keyPressEvent

    Parameters
    ----------

    a0 : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextEdit::keyPressEvent(QKeyEvent *a0)
    ritual = 'ritual_ZN14QQuickTextEdit13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickTextEdit13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, a0: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::keyReleaseEvent(QKeyEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#keyReleaseEvent

    Parameters
    ----------

    a0 : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextEdit::keyReleaseEvent(QKeyEvent *a0)
    ritual = 'ritual_ZN14QQuickTextEdit15keyReleaseEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickTextEdit15keyReleaseEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::focusInEvent(QFocusEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#focusInEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextEdit::focusInEvent(QFocusEvent *event)
    ritual = 'ritual_ZN14QQuickTextEdit12focusInEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickTextEdit12focusInEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::focusOutEvent(QFocusEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#focusOutEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextEdit::focusOutEvent(QFocusEvent *event)
    ritual = 'ritual_ZN14QQuickTextEdit13focusOutEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickTextEdit13focusOutEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverEnterEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::hoverEnterEvent(QHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#hoverEnterEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextEdit::hoverEnterEvent(QHoverEvent *event)
    ritual = 'ritual_ZN14QQuickTextEdit15hoverEnterEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickTextEdit15hoverEnterEventEP11QHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverMoveEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::hoverMoveEvent(QHoverEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#hoverMoveEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextEdit::hoverMoveEvent(QHoverEvent *event)
    ritual = 'ritual_ZN14QQuickTextEdit14hoverMoveEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickTextEdit14hoverMoveEventEP11QHoverEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverLeaveEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::hoverLeaveEvent(QHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#hoverLeaveEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextEdit::hoverLeaveEvent(QHoverEvent *event)
    ritual = 'ritual_ZN14QQuickTextEdit15hoverLeaveEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickTextEdit15hoverLeaveEventEP11QHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::mousePressEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextEdit::mousePressEvent(QMouseEvent *event)
    ritual = 'ritual_ZN14QQuickTextEdit15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickTextEdit15mousePressEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::mouseReleaseEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextEdit::mouseReleaseEvent(QMouseEvent *event)
    ritual = 'ritual_ZN14QQuickTextEdit17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickTextEdit17mouseReleaseEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::mouseDoubleClickEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#mouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextEdit::mouseDoubleClickEvent(QMouseEvent *event)
    ritual = (
        'ritual_ZN14QQuickTextEdit21mouseDoubleClickEventEP11QMouseEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickTextEdit21mouseDoubleClickEventEP11QMouseEv'
          'ent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::mouseMoveEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextEdit::mouseMoveEvent(QMouseEvent *event)
    ritual = 'ritual_ZN14QQuickTextEdit14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickTextEdit14mouseMoveEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QInputMethodEvent)
  @overload(NoneType)
  def inputMethodEvent(self, e: Optional[QInputMethodEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::inputMethodEvent(QInputMethodEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#inputMethodEvent

    Parameters
    ----------

    e : Optional[QInputMethodEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextEdit::inputMethodEvent(QInputMethodEvent *e)
    ritual = (
        'ritual_ZN14QQuickTextEdit16inputMethodEventEP17QInputMethodEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickTextEdit16inputMethodEventEP17QInputMethodE'
          'vent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updatePaintNode(
      self,
      oldNode: Optional[QSGNode],
      updatePaintNodeData: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QQuickTextEdit::updatePaintNode(QSGNode *oldNode,
    UpdatePaintNodeData *updatePaintNodeData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextedit.html#updatePaintNode

    Parameters
    ----------

    oldNode : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    updatePaintNodeData : Optional[QQuickItem.UpdatePaintNodeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QQuickTextEdit::updatePaintNode(QSGNode *oldNode,
    #      UpdatePaintNodeData *updatePaintNodeData)
    ritual = (
        'ritual_ZN14QQuickTextEdit15updatePaintNodeEP7QSGNodePN10QQuickItem'
        '19UpdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickTextEdit15updatePaintNodeEP7QSGNodePN10QQui'
          'ckItem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual,
        self._addressOf(oldNode, 'QSGNode'),
        self._addressOf(updatePaintNodeData),
    )
    from . import QSGNode
    return QSGNode._cuteAt(address)

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QQuickTextEdit::updatePolish()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#updatePolish
    """
    #  void QQuickTextEdit::updatePolish()
    ritual = 'ritual_ZN14QQuickTextEdit12updatePolishEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickTextEdit12updatePolishEv'
    self.uglySide.call(ritual)

  def d_func(self) -> Optional[QQuickTextEditPrivate]:
    """
    Calls Qt's 'QQuickTextEditPrivate *QQuickTextEdit::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextedit.html#d_func

    Returns
    -------

    Optional[QQuickTextEditPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextEditPrivate *QQuickTextEdit::d_func()
    address = self.uglySide.call('ritual_ZN14QQuickTextEdit6d_funcEv')
    from . import QQuickTextEditPrivate
    return QQuickTextEditPrivate._cuteAt(address)
