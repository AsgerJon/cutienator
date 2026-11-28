"""
QQuickTextInput binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktextinput_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickTextInput to be private: it declares the class in a header
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

  from ..QtCore import QEvent, QMetaObject, QRectF, QTimerEvent, QVariant
  from ..QtGui import QColor, QFocusEvent, QFont, QInputMethodEvent
  from ..QtGui import QKeyEvent, QMouseEvent, QValidator
  from ..QtQml import QQmlComponent
  from . import QQuickTextInputPrivate, QSGNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QEvent = WAIT['QEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QFont = WAIT['QFont']
  QInputMethodEvent = WAIT['QInputMethodEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QQmlComponent = WAIT['QQmlComponent']
  QRectF = WAIT['QRectF']
  QSGNode = WAIT['QSGNode']
  QTimerEvent = WAIT['QTimerEvent']
  QValidator = WAIT['QValidator']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTextInput(QQuickImplicitSizeItem, QQuickTextInterface):
  """
  The cute side of Qt's QQuickTextInput: a plain Python object standing in
  front of one C++ QQuickTextInput.

  It is built on the cute 'QQuickImplicitSizeItem', as Qt's QQuickTextInput
  is built on Qt's QQuickImplicitSizeItem, and has everything that class has.
  It is built on the cute 'QQuickTextInterface' as well, as Qt's
  QQuickTextInput is built on Qt's QQuickTextInterface too, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTextInput that has a ritual and that Python
  can call so far, 182 names in all: 'metaObject', 'tr', 'componentComplete',
  'positionAt', 'positionToRectangle', 'moveCursorSelection', 'renderType',
  'setRenderType', 'text', 'setText', 'length', 'font', 'setFont', 'color',
  'setColor', 'selectionColor', 'setSelectionColor', 'selectedTextColor',
  'setSelectedTextColor', 'hAlign', 'setHAlign', 'resetHAlign',
  'effectiveHAlign', 'vAlign', 'setVAlign', 'wrapMode', 'setWrapMode',
  'isReadOnly', 'setReadOnly', 'isCursorVisible', 'setCursorVisible',
  'cursorPosition', 'setCursorPosition', 'cursorRectangle', 'selectionStart',
  'selectionEnd', 'selectedText', 'maxLength', 'setMaxLength', 'validator',
  'setValidator', 'inputMask', 'setInputMask', 'echoMode', 'setEchoMode',
  'passwordCharacter', 'setPasswordCharacter', 'passwordMaskDelay',
  'setPasswordMaskDelay', 'resetPasswordMaskDelay', 'displayText',
  'preeditText', 'cursorDelegate', 'setCursorDelegate', 'overwriteMode',
  'setOverwriteMode', 'focusOnPress', 'setFocusOnPress', 'autoScroll',
  'setAutoScroll', 'selectByMouse', 'setSelectByMouse', 'mouseSelectionMode',
  'setMouseSelectionMode', 'persistentSelection', 'setPersistentSelection',
  'hasAcceptableInput', 'inputMethodQuery', 'boundingRect', 'clipRect',
  'canPaste', 'canUndo', 'canRedo', 'isInputMethodComposing',
  'inputMethodHints', 'setInputMethodHints', 'getText', 'contentWidth',
  'contentHeight', 'padding', 'setPadding', 'resetPadding', 'topPadding',
  'setTopPadding', 'resetTopPadding', 'leftPadding', 'setLeftPadding',
  'resetLeftPadding', 'rightPadding', 'setRightPadding', 'resetRightPadding',
  'bottomPadding', 'setBottomPadding', 'resetBottomPadding', 'invalidate',
  'textChanged', 'cursorPositionChanged', 'cursorRectangleChanged',
  'selectionStartChanged', 'selectionEndChanged', 'selectedTextChanged',
  'accepted', 'acceptableInputChanged', 'editingFinished', 'textEdited',
  'colorChanged', 'selectionColorChanged', 'selectedTextColorChanged',
  'fontChanged', 'horizontalAlignmentChanged', 'verticalAlignmentChanged',
  'wrapModeChanged', 'readOnlyChanged', 'cursorVisibleChanged',
  'cursorDelegateChanged', 'overwriteModeChanged', 'maximumLengthChanged',
  'validatorChanged', 'inputMaskChanged', 'echoModeChanged',
  'passwordCharacterChanged', 'passwordMaskDelayChanged',
  'displayTextChanged', 'preeditTextChanged', 'activeFocusOnPressChanged',
  'autoScrollChanged', 'selectByMouseChanged', 'mouseSelectionModeChanged',
  'persistentSelectionChanged', 'canPasteChanged', 'canUndoChanged',
  'canRedoChanged', 'inputMethodComposingChanged',
  'effectiveHorizontalAlignmentChanged', 'contentSizeChanged',
  'inputMethodHintsChanged', 'renderTypeChanged', 'paddingChanged',
  'topPaddingChanged', 'leftPaddingChanged', 'rightPaddingChanged',
  'bottomPaddingChanged', 'invalidateFontCaches', 'ensureActiveFocus',
  'setOldSelectionDefault', 'geometryChange', 'itemChange',
  'mousePressEvent', 'mouseMoveEvent', 'mouseReleaseEvent',
  'mouseDoubleClickEvent', 'keyPressEvent', 'inputMethodEvent',
  'mouseUngrabEvent', 'event', 'focusOutEvent', 'focusInEvent', 'timerEvent',
  'updatePaintNode', 'updatePolish', 'selectAll', 'selectWord', 'select',
  'deselect', 'isRightToLeft', 'cut', 'copy', 'paste', 'undo', 'redo',
  'insert', 'remove', 'ensureVisible', 'clear', 'selectionChanged',
  'createCursor', 'updateCursorRectangle', 'q_canPasteChanged',
  'q_updateAlignment', 'triggerPreprocess', 'q_validatorChanged', 'd_func'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTextInput::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickTextInput::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickTextInput::~QQuickTextInput()': the destructor: Python never
    removes a C++ QQuickTextInput.
  - Qt's 'QQuickTextInput::QQuickTextInput(QQuickTextInputPrivate &dd,
    QQuickItem *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QQuickTextInputPrivate *QQuickTextInput::d_func() const':
    takes in Python what 'QQuickTextInputPrivate *QQuickTextInput::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 192 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickTextInput is created at the first use, not by
    'QQuickTextInput(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTextInput.
  - Qt tells when it has removed the C++ QQuickTextInput. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickTextInput, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class CursorPosition(CuteNum):
    """
    The enum 'QQuickTextInput::CursorPosition' of Qt, with the 2 names Qt
    gives in it.
    """

    CursorBetweenCharacters = Kee[int](0)
    CursorOnCharacter = Kee[int](1)

  class EchoMode(CuteNum):
    """
    The enum 'QQuickTextInput::EchoMode' of Qt, with the 4 names Qt gives in
    it.
    """

    Normal = Kee[int](0)
    NoEcho = Kee[int](1)
    Password = Kee[int](2)
    PasswordEchoOnEdit = Kee[int](3)

  class HAlignment(CuteNum):
    """
    The enum 'QQuickTextInput::HAlignment' of Qt, with the 3 names Qt gives
    in it.
    """

    AlignLeft = Kee[int](1)
    AlignRight = Kee[int](2)
    AlignHCenter = Kee[int](4)

  class RenderType(CuteNum):
    """
    The enum 'QQuickTextInput::RenderType' of Qt, with the 3 names Qt gives
    in it.
    """

    QtRendering = Kee[int](0)
    NativeRendering = Kee[int](1)
    CurveRendering = Kee[int](2)

  class SelectionMode(CuteNum):
    """
    The enum 'QQuickTextInput::SelectionMode' of Qt, with the 2 names Qt
    gives in it.
    """

    SelectCharacters = Kee[int](0)
    SelectWords = Kee[int](1)

  class VAlignment(CuteNum):
    """
    The enum 'QQuickTextInput::VAlignment' of Qt, with the 3 names Qt gives
    in it.
    """

    AlignTop = Kee[int](32)
    AlignBottom = Kee[int](64)
    AlignVCenter = Kee[int](128)

  class WrapMode(CuteNum):
    """
    The enum 'QQuickTextInput::WrapMode' of Qt, with the 5 names Qt gives in
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
    Calls Qt's 'QString QQuickTextInput::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#tr

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
    #  QString QQuickTextInput::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQuickTextInput2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTextInput'

  #  Qt's QQuickTextInput is built on more than one class. The part of a C++
  #  QQuickTextInput that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQuickTextInterface':
          'ritual_cast_QQuickTextInput_QQuickTextInterface',
  }

  #  A C++ QQuickTextInput Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickTextInput'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickTextInput::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTextInput::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQuickTextInput10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(float)
  @overload(float, float)
  @overload(float, float, CursorPosition)
  def positionAt(
      self,
      x: float,
      y: float = 0.0,
      position: CursorPosition = CursorPosition.CursorBetweenCharacters,
  ) -> int:
    """
    Calls Qt's 'int QQuickTextInput::positionAt(qreal x, qreal y,
    QQuickTextInput::CursorPosition position) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#positionAt

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    position : CursorPosition
      Passed on as its number. May be left out, as in Qt: it is then
      CursorPosition.CursorBetweenCharacters.
    """
    #  int QQuickTextInput::positionAt(qreal x, qreal y,
    #      QQuickTextInput::CursorPosition position) const
    return self.uglySide.call(
        'ritual_ZNK15QQuickTextInput10positionAtEddNS_14CursorPositionE',
        x, y, position.value,
    )

  @overload(int)
  def positionToRectangle(self, pos: int) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickTextInput::positionToRectangle(int pos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#positionToRectangle

    Parameters
    ----------

    pos : int
      Passed on as it is.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickTextInput::positionToRectangle(int pos) const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickTextInput19positionToRectangleEi', pos,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def renderType(self) -> RenderType:
    """
    Calls Qt's 'RenderType QQuickTextInput::renderType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#renderType

    Returns
    -------

    RenderType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RenderType(number)'
      gives.
    """
    #  RenderType QQuickTextInput::renderType() const
    return QQuickTextInput.RenderType(self.uglySide.call(
        'ritual_ZNK15QQuickTextInput10renderTypeEv',
    ))

  def text(self) -> str:
    """
    Calls Qt's 'QString QQuickTextInput::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextInput::text() const
    return self.uglySide.call('ritual_ZNK15QQuickTextInput4textEv')

  def length(self) -> int:
    """
    Calls Qt's 'int QQuickTextInput::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#length
    """
    #  int QQuickTextInput::length() const
    return self.uglySide.call('ritual_ZNK15QQuickTextInput6lengthEv')

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickTextInput::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickTextInput::font() const
    address = self.uglySide.call('ritual_ZNK15QQuickTextInput4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickTextInput::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickTextInput::color() const
    address = self.uglySide.call('ritual_ZNK15QQuickTextInput5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def selectionColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickTextInput::selectionColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#selectionColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickTextInput::selectionColor() const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickTextInput14selectionColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def selectedTextColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickTextInput::selectedTextColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#selectedTextColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickTextInput::selectedTextColor() const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickTextInput17selectedTextColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def hAlign(self) -> HAlignment:
    """
    Calls Qt's 'HAlignment QQuickTextInput::hAlign() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#hAlign

    Returns
    -------

    HAlignment
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'HAlignment(number)'
      gives.
    """
    #  HAlignment QQuickTextInput::hAlign() const
    return QQuickTextInput.HAlignment(self.uglySide.call(
        'ritual_ZNK15QQuickTextInput6hAlignEv',
    ))

  def effectiveHAlign(self) -> HAlignment:
    """
    Calls Qt's 'HAlignment QQuickTextInput::effectiveHAlign() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#effectiveHAlign

    Returns
    -------

    HAlignment
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'HAlignment(number)'
      gives.
    """
    #  HAlignment QQuickTextInput::effectiveHAlign() const
    return QQuickTextInput.HAlignment(self.uglySide.call(
        'ritual_ZNK15QQuickTextInput15effectiveHAlignEv',
    ))

  def vAlign(self) -> VAlignment:
    """
    Calls Qt's 'VAlignment QQuickTextInput::vAlign() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#vAlign

    Returns
    -------

    VAlignment
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'VAlignment(number)'
      gives.
    """
    #  VAlignment QQuickTextInput::vAlign() const
    return QQuickTextInput.VAlignment(self.uglySide.call(
        'ritual_ZNK15QQuickTextInput6vAlignEv',
    ))

  def wrapMode(self) -> WrapMode:
    """
    Calls Qt's 'WrapMode QQuickTextInput::wrapMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#wrapMode

    Returns
    -------

    WrapMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'WrapMode(number)' gives.
    """
    #  WrapMode QQuickTextInput::wrapMode() const
    return QQuickTextInput.WrapMode(self.uglySide.call(
        'ritual_ZNK15QQuickTextInput8wrapModeEv',
    ))

  def isReadOnly(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextInput::isReadOnly() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#isReadOnly
    """
    #  bool QQuickTextInput::isReadOnly() const
    return self.uglySide.call('ritual_ZNK15QQuickTextInput10isReadOnlyEv')

  def isCursorVisible(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextInput::isCursorVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#isCursorVisible
    """
    #  bool QQuickTextInput::isCursorVisible() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickTextInput15isCursorVisibleEv',
    )

  def cursorPosition(self) -> int:
    """
    Calls Qt's 'int QQuickTextInput::cursorPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#cursorPosition
    """
    #  int QQuickTextInput::cursorPosition() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickTextInput14cursorPositionEv',
    )

  def cursorRectangle(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickTextInput::cursorRectangle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#cursorRectangle

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickTextInput::cursorRectangle() const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickTextInput15cursorRectangleEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def selectionStart(self) -> int:
    """
    Calls Qt's 'int QQuickTextInput::selectionStart() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#selectionStart
    """
    #  int QQuickTextInput::selectionStart() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickTextInput14selectionStartEv',
    )

  def selectionEnd(self) -> int:
    """
    Calls Qt's 'int QQuickTextInput::selectionEnd() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#selectionEnd
    """
    #  int QQuickTextInput::selectionEnd() const
    return self.uglySide.call('ritual_ZNK15QQuickTextInput12selectionEndEv')

  def selectedText(self) -> str:
    """
    Calls Qt's 'QString QQuickTextInput::selectedText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#selectedText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextInput::selectedText() const
    return self.uglySide.call('ritual_ZNK15QQuickTextInput12selectedTextEv')

  def maxLength(self) -> int:
    """
    Calls Qt's 'int QQuickTextInput::maxLength() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#maxLength
    """
    #  int QQuickTextInput::maxLength() const
    return self.uglySide.call('ritual_ZNK15QQuickTextInput9maxLengthEv')

  def validator(self) -> Optional[QValidator]:
    """
    Calls Qt's 'QValidator *QQuickTextInput::validator() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#validator

    Returns
    -------

    Optional[QValidator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValidator *QQuickTextInput::validator() const
    address = self.uglySide.call('ritual_ZNK15QQuickTextInput9validatorEv')
    from ..QtGui import QValidator
    return QValidator._cuteAt(address)

  def inputMask(self) -> str:
    """
    Calls Qt's 'QString QQuickTextInput::inputMask() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#inputMask

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextInput::inputMask() const
    return self.uglySide.call('ritual_ZNK15QQuickTextInput9inputMaskEv')

  def echoMode(self) -> EchoMode:
    """
    Calls Qt's 'EchoMode QQuickTextInput::echoMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#echoMode

    Returns
    -------

    EchoMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'EchoMode(number)' gives.
    """
    #  EchoMode QQuickTextInput::echoMode() const
    return QQuickTextInput.EchoMode(self.uglySide.call(
        'ritual_ZNK15QQuickTextInput8echoModeEv',
    ))

  def passwordCharacter(self) -> str:
    """
    Calls Qt's 'QString QQuickTextInput::passwordCharacter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#passwordCharacter

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextInput::passwordCharacter() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickTextInput17passwordCharacterEv',
    )

  def passwordMaskDelay(self) -> int:
    """
    Calls Qt's 'int QQuickTextInput::passwordMaskDelay() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#passwordMaskDelay
    """
    #  int QQuickTextInput::passwordMaskDelay() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickTextInput17passwordMaskDelayEv',
    )

  def displayText(self) -> str:
    """
    Calls Qt's 'QString QQuickTextInput::displayText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#displayText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextInput::displayText() const
    return self.uglySide.call('ritual_ZNK15QQuickTextInput11displayTextEv')

  def preeditText(self) -> str:
    """
    Calls Qt's 'QString QQuickTextInput::preeditText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#preeditText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextInput::preeditText() const
    return self.uglySide.call('ritual_ZNK15QQuickTextInput11preeditTextEv')

  def cursorDelegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickTextInput::cursorDelegate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#cursorDelegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickTextInput::cursorDelegate() const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickTextInput14cursorDelegateEv',
    )
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def overwriteMode(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextInput::overwriteMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#overwriteMode
    """
    #  bool QQuickTextInput::overwriteMode() const
    return self.uglySide.call('ritual_ZNK15QQuickTextInput13overwriteModeEv')

  def focusOnPress(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextInput::focusOnPress() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#focusOnPress
    """
    #  bool QQuickTextInput::focusOnPress() const
    return self.uglySide.call('ritual_ZNK15QQuickTextInput12focusOnPressEv')

  def autoScroll(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextInput::autoScroll() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#autoScroll
    """
    #  bool QQuickTextInput::autoScroll() const
    return self.uglySide.call('ritual_ZNK15QQuickTextInput10autoScrollEv')

  def selectByMouse(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextInput::selectByMouse() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#selectByMouse
    """
    #  bool QQuickTextInput::selectByMouse() const
    return self.uglySide.call('ritual_ZNK15QQuickTextInput13selectByMouseEv')

  def mouseSelectionMode(self) -> SelectionMode:
    """
    Calls Qt's 'SelectionMode QQuickTextInput::mouseSelectionMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#mouseSelectionMode

    Returns
    -------

    SelectionMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SelectionMode(number)'
      gives.
    """
    #  SelectionMode QQuickTextInput::mouseSelectionMode() const
    return QQuickTextInput.SelectionMode(self.uglySide.call(
        'ritual_ZNK15QQuickTextInput18mouseSelectionModeEv',
    ))

  def persistentSelection(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextInput::persistentSelection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#persistentSelection
    """
    #  bool QQuickTextInput::persistentSelection() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickTextInput19persistentSelectionEv',
    )

  def hasAcceptableInput(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextInput::hasAcceptableInput() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#hasAcceptableInput
    """
    #  bool QQuickTextInput::hasAcceptableInput() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickTextInput18hasAcceptableInputEv',
    )

  @overload(Qt.InputMethodQuery)
  def inputMethodQuery(self, property: Qt.InputMethodQuery) -> QVariant:
    """
    Calls Qt's 'QVariant
    QQuickTextInput::inputMethodQuery(Qt::InputMethodQuery property) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#inputMethodQuery

    Parameters
    ----------

    property : Qt.InputMethodQuery
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickTextInput::inputMethodQuery(Qt::InputMethodQuery
    #      property) const
    ritual = (
        'ritual_ZNK15QQuickTextInput16inputMethodQueryEN2Qt16InputMethodQue'
        'ryE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK15QQuickTextInput16inputMethodQueryEN2Qt16InputMet'
          'hodQueryE')
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
    QQuickTextInput::inputMethodQuery(Qt::InputMethodQuery query, const
    QVariant &argument) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#inputMethodQuery

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
    #  QVariant QQuickTextInput::inputMethodQuery(Qt::InputMethodQuery query,
    #      const QVariant &argument) const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickTextInput16inputMethodQueryEN2Qt16InputMethodQue'
        'ryERK8QVariant',
        query.value, self._valueOf(argument),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickTextInput::boundingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickTextInput::boundingRect() const
    ritual = 'ritual_ZNK15QQuickTextInput12boundingRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QQuickTextInput12boundingRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def clipRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickTextInput::clipRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#clipRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickTextInput::clipRect() const
    ritual = 'ritual_ZNK15QQuickTextInput8clipRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QQuickTextInput8clipRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def canPaste(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextInput::canPaste() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#canPaste
    """
    #  bool QQuickTextInput::canPaste() const
    return self.uglySide.call('ritual_ZNK15QQuickTextInput8canPasteEv')

  def canUndo(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextInput::canUndo() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#canUndo
    """
    #  bool QQuickTextInput::canUndo() const
    return self.uglySide.call('ritual_ZNK15QQuickTextInput7canUndoEv')

  def canRedo(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextInput::canRedo() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#canRedo
    """
    #  bool QQuickTextInput::canRedo() const
    return self.uglySide.call('ritual_ZNK15QQuickTextInput7canRedoEv')

  def isInputMethodComposing(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextInput::isInputMethodComposing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#isInputMethodComposing
    """
    #  bool QQuickTextInput::isInputMethodComposing() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickTextInput22isInputMethodComposingEv',
    )

  def inputMethodHints(self) -> Qt.InputMethodHints:
    """
    Calls Qt's 'Qt::InputMethodHints QQuickTextInput::inputMethodHints()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#inputMethodHints

    Returns
    -------

    Qt.InputMethodHints
      The value standing for the combination Qt gave back.
    """
    #  Qt::InputMethodHints QQuickTextInput::inputMethodHints() const
    return Qt.InputMethodHints(self.uglySide.call(
        'ritual_ZNK15QQuickTextInput16inputMethodHintsEv',
    ))

  @overload(int, int)
  def getText(self, start: int, end: int) -> str:
    """
    Calls Qt's 'QString QQuickTextInput::getText(int start, int end) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#getText

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
    #  QString QQuickTextInput::getText(int start, int end) const
    return self.uglySide.call(
        'ritual_ZNK15QQuickTextInput7getTextEii', start, end,
    )

  def contentWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextInput::contentWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#contentWidth
    """
    #  qreal QQuickTextInput::contentWidth() const
    return self.uglySide.call('ritual_ZNK15QQuickTextInput12contentWidthEv')

  def contentHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextInput::contentHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#contentHeight
    """
    #  qreal QQuickTextInput::contentHeight() const
    return self.uglySide.call('ritual_ZNK15QQuickTextInput13contentHeightEv')

  def padding(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextInput::padding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#padding
    """
    #  qreal QQuickTextInput::padding() const
    return self.uglySide.call('ritual_ZNK15QQuickTextInput7paddingEv')

  def topPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextInput::topPadding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#topPadding
    """
    #  qreal QQuickTextInput::topPadding() const
    return self.uglySide.call('ritual_ZNK15QQuickTextInput10topPaddingEv')

  def leftPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextInput::leftPadding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#leftPadding
    """
    #  qreal QQuickTextInput::leftPadding() const
    return self.uglySide.call('ritual_ZNK15QQuickTextInput11leftPaddingEv')

  def rightPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextInput::rightPadding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#rightPadding
    """
    #  qreal QQuickTextInput::rightPadding() const
    return self.uglySide.call('ritual_ZNK15QQuickTextInput12rightPaddingEv')

  def bottomPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextInput::bottomPadding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#bottomPadding
    """
    #  qreal QQuickTextInput::bottomPadding() const
    return self.uglySide.call('ritual_ZNK15QQuickTextInput13bottomPaddingEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(RenderType)
  def setRenderType(self, renderType: RenderType) -> None:
    """
    Calls Qt's 'void QQuickTextInput::setRenderType(RenderType renderType)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#setRenderType

    Parameters
    ----------

    renderType : RenderType
      Passed on as its number.
    """
    #  void QQuickTextInput::setRenderType(RenderType renderType)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput13setRenderTypeENS_10RenderTypeE',
        renderType.value,
    )

  @overload(str)
  def setText(self, a0: str) -> None:
    """
    Calls Qt's 'void QQuickTextInput::setText(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#setText

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickTextInput::setText(const QString &a0)
    self.uglySide.call('ritual_ZN15QQuickTextInput7setTextERK7QString', a0)

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickTextInput::setFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickTextInput::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput7setFontERK5QFont', self._valueOf(font),
    )

  @overload(QColor)
  def setColor(self, c: QColor) -> None:
    """
    Calls Qt's 'void QQuickTextInput::setColor(const QColor &c)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#setColor

    Parameters
    ----------

    c : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickTextInput::setColor(const QColor &c)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput8setColorERK6QColor', self._valueOf(c),
    )

  @overload(QColor)
  def setSelectionColor(self, c: QColor) -> None:
    """
    Calls Qt's 'void QQuickTextInput::setSelectionColor(const QColor &c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#setSelectionColor

    Parameters
    ----------

    c : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickTextInput::setSelectionColor(const QColor &c)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput17setSelectionColorERK6QColor',
        self._valueOf(c),
    )

  @overload(QColor)
  def setSelectedTextColor(self, c: QColor) -> None:
    """
    Calls Qt's 'void QQuickTextInput::setSelectedTextColor(const QColor &c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#setSelectedTextColor

    Parameters
    ----------

    c : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickTextInput::setSelectedTextColor(const QColor &c)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput20setSelectedTextColorERK6QColor',
        self._valueOf(c),
    )

  @overload(HAlignment)
  def setHAlign(self, align: HAlignment) -> None:
    """
    Calls Qt's 'void QQuickTextInput::setHAlign(HAlignment align)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#setHAlign

    Parameters
    ----------

    align : HAlignment
      Passed on as its number.
    """
    #  void QQuickTextInput::setHAlign(HAlignment align)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput9setHAlignENS_10HAlignmentE', align.value,
    )

  @overload(VAlignment)
  def setVAlign(self, align: VAlignment) -> None:
    """
    Calls Qt's 'void QQuickTextInput::setVAlign(VAlignment align)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#setVAlign

    Parameters
    ----------

    align : VAlignment
      Passed on as its number.
    """
    #  void QQuickTextInput::setVAlign(VAlignment align)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput9setVAlignENS_10VAlignmentE', align.value,
    )

  @overload(WrapMode)
  def setWrapMode(self, w: WrapMode) -> None:
    """
    Calls Qt's 'void QQuickTextInput::setWrapMode(WrapMode w)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#setWrapMode

    Parameters
    ----------

    w : WrapMode
      Passed on as its number.
    """
    #  void QQuickTextInput::setWrapMode(WrapMode w)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput11setWrapModeENS_8WrapModeE', w.value,
    )

  @overload(bool)
  def setReadOnly(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickTextInput::setReadOnly(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#setReadOnly

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickTextInput::setReadOnly(bool a0)
    self.uglySide.call('ritual_ZN15QQuickTextInput11setReadOnlyEb', a0)

  @overload(bool)
  def setCursorVisible(self, on: bool) -> None:
    """
    Calls Qt's 'void QQuickTextInput::setCursorVisible(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#setCursorVisible

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickTextInput::setCursorVisible(bool on)
    self.uglySide.call('ritual_ZN15QQuickTextInput16setCursorVisibleEb', on)

  @overload(int)
  def setCursorPosition(self, cp: int) -> None:
    """
    Calls Qt's 'void QQuickTextInput::setCursorPosition(int cp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#setCursorPosition

    Parameters
    ----------

    cp : int
      Passed on as it is.
    """
    #  void QQuickTextInput::setCursorPosition(int cp)
    self.uglySide.call('ritual_ZN15QQuickTextInput17setCursorPositionEi', cp)

  @overload(int)
  def setMaxLength(self, ml: int) -> None:
    """
    Calls Qt's 'void QQuickTextInput::setMaxLength(int ml)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#setMaxLength

    Parameters
    ----------

    ml : int
      Passed on as it is.
    """
    #  void QQuickTextInput::setMaxLength(int ml)
    self.uglySide.call('ritual_ZN15QQuickTextInput12setMaxLengthEi', ml)

  @overload(QValidator)
  @overload(NoneType)
  def setValidator(self, v: Optional[QValidator]) -> None:
    """
    Calls Qt's 'void QQuickTextInput::setValidator(QValidator *v)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#setValidator

    Parameters
    ----------

    v : Optional[QValidator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextInput::setValidator(QValidator *v)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput12setValidatorEP10QValidator',
        self._addressOf(v),
    )

  @overload(str)
  def setInputMask(self, im: str) -> None:
    """
    Calls Qt's 'void QQuickTextInput::setInputMask(const QString &im)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#setInputMask

    Parameters
    ----------

    im : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickTextInput::setInputMask(const QString &im)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput12setInputMaskERK7QString', im,
    )

  @overload(EchoMode)
  def setEchoMode(self, echo: EchoMode) -> None:
    """
    Calls Qt's 'void QQuickTextInput::setEchoMode(EchoMode echo)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#setEchoMode

    Parameters
    ----------

    echo : EchoMode
      Passed on as its number.
    """
    #  void QQuickTextInput::setEchoMode(EchoMode echo)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput11setEchoModeENS_8EchoModeE', echo.value,
    )

  @overload(str)
  def setPasswordCharacter(self, str: str) -> None:
    """
    Calls Qt's 'void QQuickTextInput::setPasswordCharacter(const QString
    &str)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#setPasswordCharacter

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickTextInput::setPasswordCharacter(const QString &str)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput20setPasswordCharacterERK7QString', str,
    )

  @overload(int)
  def setPasswordMaskDelay(self, delay: int) -> None:
    """
    Calls Qt's 'void QQuickTextInput::setPasswordMaskDelay(int delay)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#setPasswordMaskDelay

    Parameters
    ----------

    delay : int
      Passed on as it is.
    """
    #  void QQuickTextInput::setPasswordMaskDelay(int delay)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput20setPasswordMaskDelayEi', delay,
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setCursorDelegate(self, a0: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickTextInput::setCursorDelegate(QQmlComponent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#setCursorDelegate

    Parameters
    ----------

    a0 : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextInput::setCursorDelegate(QQmlComponent *a0)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput17setCursorDelegateEP13QQmlComponent',
        self._addressOf(a0),
    )

  @overload(bool)
  def setOverwriteMode(self, overwrite: bool) -> None:
    """
    Calls Qt's 'void QQuickTextInput::setOverwriteMode(bool overwrite)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#setOverwriteMode

    Parameters
    ----------

    overwrite : bool
      Passed on as it is.
    """
    #  void QQuickTextInput::setOverwriteMode(bool overwrite)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput16setOverwriteModeEb', overwrite,
    )

  @overload(bool)
  def setFocusOnPress(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickTextInput::setFocusOnPress(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#setFocusOnPress

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickTextInput::setFocusOnPress(bool a0)
    self.uglySide.call('ritual_ZN15QQuickTextInput15setFocusOnPressEb', a0)

  @overload(bool)
  def setAutoScroll(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickTextInput::setAutoScroll(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#setAutoScroll

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickTextInput::setAutoScroll(bool a0)
    self.uglySide.call('ritual_ZN15QQuickTextInput13setAutoScrollEb', a0)

  @overload(bool)
  def setSelectByMouse(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickTextInput::setSelectByMouse(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#setSelectByMouse

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickTextInput::setSelectByMouse(bool a0)
    self.uglySide.call('ritual_ZN15QQuickTextInput16setSelectByMouseEb', a0)

  @overload(SelectionMode)
  def setMouseSelectionMode(self, mode: SelectionMode) -> None:
    """
    Calls Qt's 'void QQuickTextInput::setMouseSelectionMode(SelectionMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#setMouseSelectionMode

    Parameters
    ----------

    mode : SelectionMode
      Passed on as its number.
    """
    #  void QQuickTextInput::setMouseSelectionMode(SelectionMode mode)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput21setMouseSelectionModeENS_13SelectionMo'
        'deE',
        mode.value,
    )

  @overload(bool)
  def setPersistentSelection(self, persist: bool) -> None:
    """
    Calls Qt's 'void QQuickTextInput::setPersistentSelection(bool persist)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#setPersistentSelection

    Parameters
    ----------

    persist : bool
      Passed on as it is.
    """
    #  void QQuickTextInput::setPersistentSelection(bool persist)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput22setPersistentSelectionEb', persist,
    )

  @overload(Qt.InputMethodHints)
  def setInputMethodHints(self, hints: Qt.InputMethodHints) -> None:
    """
    Calls Qt's 'void
    QQuickTextInput::setInputMethodHints(Qt::InputMethodHints hints)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#setInputMethodHints

    Parameters
    ----------

    hints : Qt.InputMethodHints
      Passed on as its number.
    """
    #  void QQuickTextInput::setInputMethodHints(Qt::InputMethodHints hints)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput19setInputMethodHintsE6QFlagsIN2Qt15Inpu'
        'tMethodHintEE',
        hints.value,
    )

  @overload(float)
  def setPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickTextInput::setPadding(qreal padding)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#setPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickTextInput::setPadding(qreal padding)
    self.uglySide.call('ritual_ZN15QQuickTextInput10setPaddingEd', padding)

  @overload(float)
  def setTopPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickTextInput::setTopPadding(qreal padding)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#setTopPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickTextInput::setTopPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput13setTopPaddingEd', padding,
    )

  @overload(float)
  def setLeftPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickTextInput::setLeftPadding(qreal padding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#setLeftPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickTextInput::setLeftPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput14setLeftPaddingEd', padding,
    )

  @overload(float)
  def setRightPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickTextInput::setRightPadding(qreal padding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#setRightPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickTextInput::setRightPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput15setRightPaddingEd', padding,
    )

  @overload(float)
  def setBottomPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickTextInput::setBottomPadding(qreal padding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#setBottomPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickTextInput::setBottomPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput16setBottomPaddingEd', padding,
    )

  def setOldSelectionDefault(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::setOldSelectionDefault()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#setOldSelectionDefault
    """
    #  void QQuickTextInput::setOldSelectionDefault()
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput22setOldSelectionDefaultEv',
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickTextInput::QQuickTextInput(QQuickItem *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#QQuickTextInput

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickTextInput::QQuickTextInput(QQuickItem *parent)
    self._noteCreation(QQuickTextInput, lambda: Rituals.call(
        'ritual_ZN15QQuickTextInputC1EP10QQuickItem',
        self._addressOf(parent),
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

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#componentComplete
    """
    #  void QQuickTextInput::componentComplete()
    ritual = 'ritual_ZN15QQuickTextInput17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickTextInput17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(int)
  def moveCursorSelection(self, pos: int) -> None:
    """
    Calls Qt's 'void QQuickTextInput::moveCursorSelection(int pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#moveCursorSelection

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  void QQuickTextInput::moveCursorSelection(int pos)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput19moveCursorSelectionEi', pos,
    )

  @overload(int, SelectionMode)
  def moveCursorSelection(self, pos: int, mode: SelectionMode) -> None:
    """
    Calls Qt's 'void QQuickTextInput::moveCursorSelection(int pos,
    QQuickTextInput::SelectionMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#moveCursorSelection

    Parameters
    ----------

    pos : int
      Passed on as it is.

    mode : SelectionMode
      Passed on as its number.
    """
    #  void QQuickTextInput::moveCursorSelection(int pos,
    #      QQuickTextInput::SelectionMode mode)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput19moveCursorSelectionEiNS_13SelectionMod'
        'eE',
        pos, mode.value,
    )

  def resetHAlign(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::resetHAlign()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#resetHAlign
    """
    #  void QQuickTextInput::resetHAlign()
    self.uglySide.call('ritual_ZN15QQuickTextInput11resetHAlignEv')

  def resetPasswordMaskDelay(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::resetPasswordMaskDelay()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#resetPasswordMaskDelay
    """
    #  void QQuickTextInput::resetPasswordMaskDelay()
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput22resetPasswordMaskDelayEv',
    )

  def resetPadding(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::resetPadding()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#resetPadding
    """
    #  void QQuickTextInput::resetPadding()
    self.uglySide.call('ritual_ZN15QQuickTextInput12resetPaddingEv')

  def resetTopPadding(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::resetTopPadding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#resetTopPadding
    """
    #  void QQuickTextInput::resetTopPadding()
    self.uglySide.call('ritual_ZN15QQuickTextInput15resetTopPaddingEv')

  def resetLeftPadding(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::resetLeftPadding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#resetLeftPadding
    """
    #  void QQuickTextInput::resetLeftPadding()
    self.uglySide.call('ritual_ZN15QQuickTextInput16resetLeftPaddingEv')

  def resetRightPadding(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::resetRightPadding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#resetRightPadding
    """
    #  void QQuickTextInput::resetRightPadding()
    self.uglySide.call('ritual_ZN15QQuickTextInput17resetRightPaddingEv')

  def resetBottomPadding(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::resetBottomPadding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#resetBottomPadding
    """
    #  void QQuickTextInput::resetBottomPadding()
    self.uglySide.call('ritual_ZN15QQuickTextInput18resetBottomPaddingEv')

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::invalidate()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#invalidate
    """
    #  void QQuickTextInput::invalidate()
    ritual = 'ritual_ZN15QQuickTextInput10invalidateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickTextInput10invalidateEv'
    self.uglySide.call(ritual)

  def textChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::textChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#textChanged
    """
    #  void QQuickTextInput::textChanged()
    self.uglySide.call('ritual_ZN15QQuickTextInput11textChangedEv')

  def cursorPositionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::cursorPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#cursorPositionChanged
    """
    #  void QQuickTextInput::cursorPositionChanged()
    self.uglySide.call('ritual_ZN15QQuickTextInput21cursorPositionChangedEv')

  def cursorRectangleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::cursorRectangleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#cursorRectangleChanged
    """
    #  void QQuickTextInput::cursorRectangleChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput22cursorRectangleChangedEv',
    )

  def selectionStartChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::selectionStartChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#selectionStartChanged
    """
    #  void QQuickTextInput::selectionStartChanged()
    self.uglySide.call('ritual_ZN15QQuickTextInput21selectionStartChangedEv')

  def selectionEndChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::selectionEndChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#selectionEndChanged
    """
    #  void QQuickTextInput::selectionEndChanged()
    self.uglySide.call('ritual_ZN15QQuickTextInput19selectionEndChangedEv')

  def selectedTextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::selectedTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#selectedTextChanged
    """
    #  void QQuickTextInput::selectedTextChanged()
    self.uglySide.call('ritual_ZN15QQuickTextInput19selectedTextChangedEv')

  def accepted(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::accepted()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#accepted
    """
    #  void QQuickTextInput::accepted()
    self.uglySide.call('ritual_ZN15QQuickTextInput8acceptedEv')

  def acceptableInputChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::acceptableInputChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#acceptableInputChanged
    """
    #  void QQuickTextInput::acceptableInputChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput22acceptableInputChangedEv',
    )

  def editingFinished(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::editingFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#editingFinished
    """
    #  void QQuickTextInput::editingFinished()
    self.uglySide.call('ritual_ZN15QQuickTextInput15editingFinishedEv')

  def textEdited(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::textEdited()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#textEdited
    """
    #  void QQuickTextInput::textEdited()
    self.uglySide.call('ritual_ZN15QQuickTextInput10textEditedEv')

  def colorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::colorChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#colorChanged
    """
    #  void QQuickTextInput::colorChanged()
    self.uglySide.call('ritual_ZN15QQuickTextInput12colorChangedEv')

  def selectionColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::selectionColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#selectionColorChanged
    """
    #  void QQuickTextInput::selectionColorChanged()
    self.uglySide.call('ritual_ZN15QQuickTextInput21selectionColorChangedEv')

  def selectedTextColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::selectedTextColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#selectedTextColorChanged
    """
    #  void QQuickTextInput::selectedTextColorChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput24selectedTextColorChangedEv',
    )

  @overload(QFont)
  def fontChanged(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickTextInput::fontChanged(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#fontChanged

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickTextInput::fontChanged(const QFont &font)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput11fontChangedERK5QFont',
        self._valueOf(font),
    )

  @overload(HAlignment)
  def horizontalAlignmentChanged(self, alignment: HAlignment) -> None:
    """
    Calls Qt's 'void
    QQuickTextInput::horizontalAlignmentChanged(QQuickTextInput::HAlignment
    alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#horizontalAlignmentChanged

    Parameters
    ----------

    alignment : HAlignment
      Passed on as its number.
    """
    #  void QQuickTextInput::horizontalAlignmentChanged(QQuickTextInput::
    #      HAlignment alignment)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput26horizontalAlignmentChangedENS_10HAlign'
        'mentE',
        alignment.value,
    )

  @overload(VAlignment)
  def verticalAlignmentChanged(self, alignment: VAlignment) -> None:
    """
    Calls Qt's 'void
    QQuickTextInput::verticalAlignmentChanged(QQuickTextInput::VAlignment
    alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#verticalAlignmentChanged

    Parameters
    ----------

    alignment : VAlignment
      Passed on as its number.
    """
    #  void QQuickTextInput::verticalAlignmentChanged(QQuickTextInput::
    #      VAlignment alignment)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput24verticalAlignmentChangedENS_10VAlignme'
        'ntE',
        alignment.value,
    )

  def wrapModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::wrapModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#wrapModeChanged
    """
    #  void QQuickTextInput::wrapModeChanged()
    self.uglySide.call('ritual_ZN15QQuickTextInput15wrapModeChangedEv')

  @overload(bool)
  def readOnlyChanged(self, isReadOnly: bool) -> None:
    """
    Calls Qt's 'void QQuickTextInput::readOnlyChanged(bool isReadOnly)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#readOnlyChanged

    Parameters
    ----------

    isReadOnly : bool
      Passed on as it is.
    """
    #  void QQuickTextInput::readOnlyChanged(bool isReadOnly)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput15readOnlyChangedEb', isReadOnly,
    )

  @overload(bool)
  def cursorVisibleChanged(self, isCursorVisible: bool) -> None:
    """
    Calls Qt's 'void QQuickTextInput::cursorVisibleChanged(bool
    isCursorVisible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#cursorVisibleChanged

    Parameters
    ----------

    isCursorVisible : bool
      Passed on as it is.
    """
    #  void QQuickTextInput::cursorVisibleChanged(bool isCursorVisible)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput20cursorVisibleChangedEb',
        isCursorVisible,
    )

  def cursorDelegateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::cursorDelegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#cursorDelegateChanged
    """
    #  void QQuickTextInput::cursorDelegateChanged()
    self.uglySide.call('ritual_ZN15QQuickTextInput21cursorDelegateChangedEv')

  @overload(bool)
  def overwriteModeChanged(self, overwriteMode: bool) -> None:
    """
    Calls Qt's 'void QQuickTextInput::overwriteModeChanged(bool
    overwriteMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#overwriteModeChanged

    Parameters
    ----------

    overwriteMode : bool
      Passed on as it is.
    """
    #  void QQuickTextInput::overwriteModeChanged(bool overwriteMode)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput20overwriteModeChangedEb', overwriteMode,
    )

  @overload(int)
  def maximumLengthChanged(self, maximumLength: int) -> None:
    """
    Calls Qt's 'void QQuickTextInput::maximumLengthChanged(int
    maximumLength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#maximumLengthChanged

    Parameters
    ----------

    maximumLength : int
      Passed on as it is.
    """
    #  void QQuickTextInput::maximumLengthChanged(int maximumLength)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput20maximumLengthChangedEi', maximumLength,
    )

  def validatorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::validatorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#validatorChanged
    """
    #  void QQuickTextInput::validatorChanged()
    self.uglySide.call('ritual_ZN15QQuickTextInput16validatorChangedEv')

  @overload(str)
  def inputMaskChanged(self, inputMask: str) -> None:
    """
    Calls Qt's 'void QQuickTextInput::inputMaskChanged(const QString
    &inputMask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#inputMaskChanged

    Parameters
    ----------

    inputMask : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickTextInput::inputMaskChanged(const QString &inputMask)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput16inputMaskChangedERK7QString', inputMask,
    )

  @overload(EchoMode)
  def echoModeChanged(self, echoMode: EchoMode) -> None:
    """
    Calls Qt's 'void
    QQuickTextInput::echoModeChanged(QQuickTextInput::EchoMode echoMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#echoModeChanged

    Parameters
    ----------

    echoMode : EchoMode
      Passed on as its number.
    """
    #  void QQuickTextInput::echoModeChanged(QQuickTextInput::EchoMode
    #      echoMode)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput15echoModeChangedENS_8EchoModeE',
        echoMode.value,
    )

  def passwordCharacterChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::passwordCharacterChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#passwordCharacterChanged
    """
    #  void QQuickTextInput::passwordCharacterChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput24passwordCharacterChangedEv',
    )

  @overload(int)
  def passwordMaskDelayChanged(self, delay: int) -> None:
    """
    Calls Qt's 'void QQuickTextInput::passwordMaskDelayChanged(int delay)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#passwordMaskDelayChanged

    Parameters
    ----------

    delay : int
      Passed on as it is.
    """
    #  void QQuickTextInput::passwordMaskDelayChanged(int delay)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput24passwordMaskDelayChangedEi', delay,
    )

  def displayTextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::displayTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#displayTextChanged
    """
    #  void QQuickTextInput::displayTextChanged()
    self.uglySide.call('ritual_ZN15QQuickTextInput18displayTextChangedEv')

  def preeditTextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::preeditTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#preeditTextChanged
    """
    #  void QQuickTextInput::preeditTextChanged()
    self.uglySide.call('ritual_ZN15QQuickTextInput18preeditTextChangedEv')

  @overload(bool)
  def activeFocusOnPressChanged(self, activeFocusOnPress: bool) -> None:
    """
    Calls Qt's 'void QQuickTextInput::activeFocusOnPressChanged(bool
    activeFocusOnPress)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#activeFocusOnPressChanged

    Parameters
    ----------

    activeFocusOnPress : bool
      Passed on as it is.
    """
    #  void QQuickTextInput::activeFocusOnPressChanged(bool
    #      activeFocusOnPress)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput25activeFocusOnPressChangedEb',
        activeFocusOnPress,
    )

  @overload(bool)
  def autoScrollChanged(self, autoScroll: bool) -> None:
    """
    Calls Qt's 'void QQuickTextInput::autoScrollChanged(bool autoScroll)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#autoScrollChanged

    Parameters
    ----------

    autoScroll : bool
      Passed on as it is.
    """
    #  void QQuickTextInput::autoScrollChanged(bool autoScroll)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput17autoScrollChangedEb', autoScroll,
    )

  @overload(bool)
  def selectByMouseChanged(self, selectByMouse: bool) -> None:
    """
    Calls Qt's 'void QQuickTextInput::selectByMouseChanged(bool
    selectByMouse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#selectByMouseChanged

    Parameters
    ----------

    selectByMouse : bool
      Passed on as it is.
    """
    #  void QQuickTextInput::selectByMouseChanged(bool selectByMouse)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput20selectByMouseChangedEb', selectByMouse,
    )

  @overload(SelectionMode)
  def mouseSelectionModeChanged(self, mode: SelectionMode) -> None:
    """
    Calls Qt's 'void
    QQuickTextInput::mouseSelectionModeChanged(QQuickTextInput::SelectionMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#mouseSelectionModeChanged

    Parameters
    ----------

    mode : SelectionMode
      Passed on as its number.
    """
    #  void QQuickTextInput::mouseSelectionModeChanged(QQuickTextInput::
    #      SelectionMode mode)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput25mouseSelectionModeChangedENS_13Selecti'
        'onModeE',
        mode.value,
    )

  def persistentSelectionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::persistentSelectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#persistentSelectionChanged
    """
    #  void QQuickTextInput::persistentSelectionChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput26persistentSelectionChangedEv',
    )

  def canPasteChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::canPasteChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#canPasteChanged
    """
    #  void QQuickTextInput::canPasteChanged()
    self.uglySide.call('ritual_ZN15QQuickTextInput15canPasteChangedEv')

  def canUndoChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::canUndoChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#canUndoChanged
    """
    #  void QQuickTextInput::canUndoChanged()
    self.uglySide.call('ritual_ZN15QQuickTextInput14canUndoChangedEv')

  def canRedoChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::canRedoChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#canRedoChanged
    """
    #  void QQuickTextInput::canRedoChanged()
    self.uglySide.call('ritual_ZN15QQuickTextInput14canRedoChangedEv')

  def inputMethodComposingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::inputMethodComposingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#inputMethodComposingChanged
    """
    #  void QQuickTextInput::inputMethodComposingChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput27inputMethodComposingChangedEv',
    )

  def effectiveHorizontalAlignmentChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::effectiveHorizontalAlignmentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html
    """
    #  void QQuickTextInput::effectiveHorizontalAlignmentChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput35effectiveHorizontalAlignmentChangedEv',
    )

  def contentSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::contentSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#contentSizeChanged
    """
    #  void QQuickTextInput::contentSizeChanged()
    self.uglySide.call('ritual_ZN15QQuickTextInput18contentSizeChangedEv')

  def inputMethodHintsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::inputMethodHintsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#inputMethodHintsChanged
    """
    #  void QQuickTextInput::inputMethodHintsChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput23inputMethodHintsChangedEv',
    )

  def renderTypeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::renderTypeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#renderTypeChanged
    """
    #  void QQuickTextInput::renderTypeChanged()
    self.uglySide.call('ritual_ZN15QQuickTextInput17renderTypeChangedEv')

  def paddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::paddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#paddingChanged
    """
    #  void QQuickTextInput::paddingChanged()
    self.uglySide.call('ritual_ZN15QQuickTextInput14paddingChangedEv')

  def topPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::topPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#topPaddingChanged
    """
    #  void QQuickTextInput::topPaddingChanged()
    self.uglySide.call('ritual_ZN15QQuickTextInput17topPaddingChangedEv')

  def leftPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::leftPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#leftPaddingChanged
    """
    #  void QQuickTextInput::leftPaddingChanged()
    self.uglySide.call('ritual_ZN15QQuickTextInput18leftPaddingChangedEv')

  def rightPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::rightPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#rightPaddingChanged
    """
    #  void QQuickTextInput::rightPaddingChanged()
    self.uglySide.call('ritual_ZN15QQuickTextInput19rightPaddingChangedEv')

  def bottomPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::bottomPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#bottomPaddingChanged
    """
    #  void QQuickTextInput::bottomPaddingChanged()
    self.uglySide.call('ritual_ZN15QQuickTextInput20bottomPaddingChangedEv')

  def invalidateFontCaches(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::invalidateFontCaches()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#invalidateFontCaches
    """
    #  void QQuickTextInput::invalidateFontCaches()
    self.uglySide.call('ritual_ZN15QQuickTextInput20invalidateFontCachesEv')

  @overload(Qt.FocusReason)
  def ensureActiveFocus(self, reason: Qt.FocusReason) -> None:
    """
    Calls Qt's 'void QQuickTextInput::ensureActiveFocus(Qt::FocusReason
    reason)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#ensureActiveFocus

    Parameters
    ----------

    reason : Qt.FocusReason
      Passed on as its number.
    """
    #  void QQuickTextInput::ensureActiveFocus(Qt::FocusReason reason)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput17ensureActiveFocusEN2Qt11FocusReasonE',
        reason.value,
    )

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickTextInput::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickTextInput::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN15QQuickTextInput14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickTextInput14geometryChangeERK6QRectFS2_'
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
    Calls Qt's 'void QQuickTextInput::itemChange(ItemChange change, const
    ItemChangeData &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    value : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickTextInput::itemChange(ItemChange change, const
    #      ItemChangeData &value)
    ritual = (
        'ritual_ZN15QQuickTextInput10itemChangeEN10QQuickItem10ItemChangeER'
        'KNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickTextInput10itemChangeEN10QQuickItem10ItemCh'
          'angeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(value))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextInput::mousePressEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextInput::mousePressEvent(QMouseEvent *event)
    ritual = 'ritual_ZN15QQuickTextInput15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickTextInput15mousePressEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextInput::mouseMoveEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextInput::mouseMoveEvent(QMouseEvent *event)
    ritual = 'ritual_ZN15QQuickTextInput14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickTextInput14mouseMoveEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextInput::mouseReleaseEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextInput::mouseReleaseEvent(QMouseEvent *event)
    ritual = 'ritual_ZN15QQuickTextInput17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickTextInput17mouseReleaseEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextInput::mouseDoubleClickEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#mouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextInput::mouseDoubleClickEvent(QMouseEvent *event)
    ritual = (
        'ritual_ZN15QQuickTextInput21mouseDoubleClickEventEP11QMouseEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickTextInput21mouseDoubleClickEventEP11QMouseE'
          'vent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, ev: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextInput::keyPressEvent(QKeyEvent *ev)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#keyPressEvent

    Parameters
    ----------

    ev : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextInput::keyPressEvent(QKeyEvent *ev)
    ritual = 'ritual_ZN15QQuickTextInput13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickTextInput13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(ev))

  @overload(QInputMethodEvent)
  @overload(NoneType)
  def inputMethodEvent(self, a0: Optional[QInputMethodEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextInput::inputMethodEvent(QInputMethodEvent
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#inputMethodEvent

    Parameters
    ----------

    a0 : Optional[QInputMethodEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextInput::inputMethodEvent(QInputMethodEvent *a0)
    ritual = (
        'ritual_ZN15QQuickTextInput16inputMethodEventEP17QInputMethodEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickTextInput16inputMethodEventEP17QInputMethod'
          'Event')
    self.uglySide.call(ritual, self._addressOf(a0))

  def mouseUngrabEvent(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::mouseUngrabEvent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#mouseUngrabEvent
    """
    #  void QQuickTextInput::mouseUngrabEvent()
    ritual = 'ritual_ZN15QQuickTextInput16mouseUngrabEventEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickTextInput16mouseUngrabEventEv'
    self.uglySide.call(ritual)

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickTextInput::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickTextInput::event(QEvent *e)
    ritual = 'ritual_ZN15QQuickTextInput5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickTextInput5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextInput::focusOutEvent(QFocusEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#focusOutEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextInput::focusOutEvent(QFocusEvent *event)
    ritual = 'ritual_ZN15QQuickTextInput13focusOutEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickTextInput13focusOutEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextInput::focusInEvent(QFocusEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#focusInEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextInput::focusInEvent(QFocusEvent *event)
    ritual = 'ritual_ZN15QQuickTextInput12focusInEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickTextInput12focusInEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextInput::timerEvent(QTimerEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextInput::timerEvent(QTimerEvent *event)
    ritual = 'ritual_ZN15QQuickTextInput10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickTextInput10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updatePaintNode(
      self,
      oldNode: Optional[QSGNode],
      data: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QQuickTextInput::updatePaintNode(QSGNode *oldNode,
    UpdatePaintNodeData *data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#updatePaintNode

    Parameters
    ----------

    oldNode : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    data : Optional[QQuickItem.UpdatePaintNodeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QQuickTextInput::updatePaintNode(QSGNode *oldNode,
    #      UpdatePaintNodeData *data)
    ritual = (
        'ritual_ZN15QQuickTextInput15updatePaintNodeEP7QSGNodePN10QQuickIte'
        'm19UpdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickTextInput15updatePaintNodeEP7QSGNodePN10QQu'
          'ickItem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(oldNode, 'QSGNode'), self._addressOf(data),
    )
    from . import QSGNode
    return QSGNode._cuteAt(address)

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::updatePolish()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#updatePolish
    """
    #  void QQuickTextInput::updatePolish()
    ritual = 'ritual_ZN15QQuickTextInput12updatePolishEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickTextInput12updatePolishEv'
    self.uglySide.call(ritual)

  def selectAll(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::selectAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#selectAll
    """
    #  void QQuickTextInput::selectAll()
    self.uglySide.call('ritual_ZN15QQuickTextInput9selectAllEv')

  def selectWord(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::selectWord()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#selectWord
    """
    #  void QQuickTextInput::selectWord()
    self.uglySide.call('ritual_ZN15QQuickTextInput10selectWordEv')

  @overload(int, int)
  def select(self, start: int, end: int) -> None:
    """
    Calls Qt's 'void QQuickTextInput::select(int start, int end)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#select

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QQuickTextInput::select(int start, int end)
    self.uglySide.call('ritual_ZN15QQuickTextInput6selectEii', start, end)

  def deselect(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::deselect()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#deselect
    """
    #  void QQuickTextInput::deselect()
    self.uglySide.call('ritual_ZN15QQuickTextInput8deselectEv')

  @overload(int, int)
  def isRightToLeft(self, start: int, end: int) -> bool:
    """
    Calls Qt's 'bool QQuickTextInput::isRightToLeft(int start, int end)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#isRightToLeft

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  bool QQuickTextInput::isRightToLeft(int start, int end)
    return self.uglySide.call(
        'ritual_ZN15QQuickTextInput13isRightToLeftEii', start, end,
    )

  def cut(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::cut()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#cut
    """
    #  void QQuickTextInput::cut()
    self.uglySide.call('ritual_ZN15QQuickTextInput3cutEv')

  def copy(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::copy()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#copy
    """
    #  void QQuickTextInput::copy()
    self.uglySide.call('ritual_ZN15QQuickTextInput4copyEv')

  def paste(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::paste()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#paste
    """
    #  void QQuickTextInput::paste()
    self.uglySide.call('ritual_ZN15QQuickTextInput5pasteEv')

  def undo(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::undo()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#undo
    """
    #  void QQuickTextInput::undo()
    self.uglySide.call('ritual_ZN15QQuickTextInput4undoEv')

  def redo(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::redo()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#redo
    """
    #  void QQuickTextInput::redo()
    self.uglySide.call('ritual_ZN15QQuickTextInput4redoEv')

  @overload(int, str)
  def insert(self, position: int, text: str) -> None:
    """
    Calls Qt's 'void QQuickTextInput::insert(int position, const QString
    &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#insert

    Parameters
    ----------

    position : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickTextInput::insert(int position, const QString &text)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput6insertEiRK7QString', position, text,
    )

  @overload(int, int)
  def remove(self, start: int, end: int) -> None:
    """
    Calls Qt's 'void QQuickTextInput::remove(int start, int end)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#remove

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QQuickTextInput::remove(int start, int end)
    self.uglySide.call('ritual_ZN15QQuickTextInput6removeEii', start, end)

  @overload(int)
  def ensureVisible(self, position: int) -> None:
    """
    Calls Qt's 'void QQuickTextInput::ensureVisible(int position)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#ensureVisible

    Parameters
    ----------

    position : int
      Passed on as it is.
    """
    #  void QQuickTextInput::ensureVisible(int position)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput13ensureVisibleEi', position,
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#clear
    """
    #  void QQuickTextInput::clear()
    self.uglySide.call('ritual_ZN15QQuickTextInput5clearEv')

  def selectionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::selectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#selectionChanged
    """
    #  void QQuickTextInput::selectionChanged()
    self.uglySide.call('ritual_ZN15QQuickTextInput16selectionChangedEv')

  def createCursor(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::createCursor()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#createCursor
    """
    #  void QQuickTextInput::createCursor()
    self.uglySide.call('ritual_ZN15QQuickTextInput12createCursorEv')

  @overload()
  @overload(bool)
  def updateCursorRectangle(self, scroll: bool = True) -> None:
    """
    Calls Qt's 'void QQuickTextInput::updateCursorRectangle(bool scroll)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#updateCursorRectangle

    Parameters
    ----------

    scroll : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QQuickTextInput::updateCursorRectangle(bool scroll)
    self.uglySide.call(
        'ritual_ZN15QQuickTextInput21updateCursorRectangleEb', scroll,
    )

  def q_canPasteChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::q_canPasteChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#q_canPasteChanged
    """
    #  void QQuickTextInput::q_canPasteChanged()
    self.uglySide.call('ritual_ZN15QQuickTextInput17q_canPasteChangedEv')

  def q_updateAlignment(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::q_updateAlignment()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#q_updateAlignment
    """
    #  void QQuickTextInput::q_updateAlignment()
    self.uglySide.call('ritual_ZN15QQuickTextInput17q_updateAlignmentEv')

  def triggerPreprocess(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::triggerPreprocess()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#triggerPreprocess
    """
    #  void QQuickTextInput::triggerPreprocess()
    self.uglySide.call('ritual_ZN15QQuickTextInput17triggerPreprocessEv')

  def q_validatorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInput::q_validatorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinput.html#q_validatorChanged
    """
    #  void QQuickTextInput::q_validatorChanged()
    self.uglySide.call('ritual_ZN15QQuickTextInput18q_validatorChangedEv')

  def d_func(self) -> Optional[QQuickTextInputPrivate]:
    """
    Calls Qt's 'QQuickTextInputPrivate *QQuickTextInput::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinput.html#d_func

    Returns
    -------

    Optional[QQuickTextInputPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextInputPrivate *QQuickTextInput::d_func()
    address = self.uglySide.call('ritual_ZN15QQuickTextInput6d_funcEv')
    from . import QQuickTextInputPrivate
    return QQuickTextInputPrivate._cuteAt(address)
