"""
QWidgetLineControl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qwidgetlinecontrol_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QWidgetLineControl to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtGui import QClipboard, QInputControl, QTextLine

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QChar, QMetaObject, QPoint, QRect, QTimerEvent
  from ..QtGui import QFont, QInputMethodEvent, QKeyEvent, QPainter, QPalette
  from ..QtGui import QTextLayout, QValidator
  from . import QCompleter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChar = WAIT['QChar']
  QCompleter = WAIT['QCompleter']
  QFont = WAIT['QFont']
  QInputMethodEvent = WAIT['QInputMethodEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QPainter = WAIT['QPainter']
  QPalette = WAIT['QPalette']
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QTimerEvent = WAIT['QTimerEvent']
  QValidator = WAIT['QValidator']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWidgetLineControl(QInputControl):
  """
  The cute side of Qt's QWidgetLineControl: a plain Python object standing in
  front of one C++ QWidgetLineControl.

  It is built on the cute 'QInputControl', as Qt's QWidgetLineControl is
  built on Qt's QInputControl, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWidgetLineControl that has a ritual and that Python
  can call so far, 124 names in all: 'metaObject', 'tr',
  'setAccessibleObject', 'accessibleObject', 'nextMaskBlank',
  'prevMaskBlank', 'isUndoAvailable', 'isRedoAvailable', 'clearUndo',
  'isModified', 'setModified', 'allSelected', 'hasSelectedText', 'width',
  'height', 'ascent', 'naturalTextWidth', 'setSelection', 'selectedText',
  'textBeforeSelection', 'textAfterSelection', 'selectionStart',
  'selectionEnd', 'inSelection', 'removeSelection', 'start', 'end', 'copy',
  'paste', 'cursor', 'preeditCursor', 'cursorWidth', 'setCursorWidth',
  'cursorMoveStyle', 'setCursorMoveStyle', 'moveCursor', 'cursorForward',
  'cursorWordForward', 'cursorWordBackward', 'home', 'xToPos', 'rectForPos',
  'cursorRect', 'anchorRect', 'cursorToX', 'isReadOnly', 'setReadOnly',
  'text', 'setText', 'commitPreedit', 'displayText', 'surroundingText',
  'backspace', 'del_', 'deselect', 'selectAll', 'insert', 'clear', 'undo',
  'redo', 'selectWordAtPos', 'echoMode', 'setEchoMode', 'maxLength',
  'setMaxLength', 'validator', 'setValidator', 'completer', 'setCompleter',
  'complete', 'cursorPosition', 'setCursorPosition', 'hasAcceptableInput',
  'fixup', 'inputMask', 'setInputMask', 'composeMode', 'setPreeditArea',
  'preeditAreaText', 'updatePasswordEchoEditing', 'passwordEchoEditing',
  'passwordCharacter', 'setPasswordCharacter', 'passwordMaskDelay',
  'setPasswordMaskDelay', 'layoutDirection', 'setLayoutDirection', 'setFont',
  'processInputMethodEvent', 'processKeyEvent', 'setBlinkingCursorEnabled',
  'updateCursorBlinking', 'resetCursorBlinkTimer', 'cursorBlinkStatus',
  'cancelText', 'setCancelText', 'palette', 'setPalette', 'draw',
  'processShortcutOverrideEvent', 'textLayout', 'init', 'removeSelectedText',
  'internalSetText', 'updateDisplayText', 'internalInsert', 'internalDelete',
  'internalDeselect', 'internalUndo', 'internalRedo',
  'emitCursorPositionChanged', 'finishChange', 'advanceToEnabledItem',
  'separate', 'parseInputMask', 'isValidInput', 'maskString', 'clearString',
  'stripString', 'findInMask', 'cancelPasswordEchoTimer', 'redoTextLayout',
  'timerEvent', '_q_deleteSelected'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWidgetLineControl::~QWidgetLineControl()': the destructor: Python
    never removes a C++ QWidgetLineControl.

  What has no ritual
  ------------------

  17 of the 146 functions Qt declares: 11 a signal; 3 takes or gives a type
  that cannot be passed yet; 2 declared and nowhere to be found; 1 a
  template.

  What to expect
  --------------

  - The C++ QWidgetLineControl is created at the first use, not by
    'QWidgetLineControl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWidgetLineControl.
  - Qt tells when it has removed the C++ QWidgetLineControl. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QWidgetLineControl, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class DrawFlags(CuteNum):
    """
    The enum 'QWidgetLineControl::DrawFlags' of Qt, with the 4 names Qt gives
    in it.
    """

    DrawText = Kee[int](1)
    DrawSelections = Kee[int](2)
    DrawCursor = Kee[int](4)
    DrawAll = Kee[int](7)

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
    Calls Qt's 'QString QWidgetLineControl::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#tr

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
    #  QString QWidgetLineControl::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QWidgetLineControl2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWidgetLineControl'

  #  A C++ QWidgetLineControl Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWidgetLineControl'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWidgetLineControl::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWidgetLineControl::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isUndoAvailable(self) -> bool:
    """
    Calls Qt's 'bool QWidgetLineControl::isUndoAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#isUndoAvailable
    """
    #  bool QWidgetLineControl::isUndoAvailable() const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl15isUndoAvailableEv',
    )

  def isRedoAvailable(self) -> bool:
    """
    Calls Qt's 'bool QWidgetLineControl::isRedoAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#isRedoAvailable
    """
    #  bool QWidgetLineControl::isRedoAvailable() const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl15isRedoAvailableEv',
    )

  def isModified(self) -> bool:
    """
    Calls Qt's 'bool QWidgetLineControl::isModified() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#isModified
    """
    #  bool QWidgetLineControl::isModified() const
    return self.uglySide.call('ritual_ZNK18QWidgetLineControl10isModifiedEv')

  def allSelected(self) -> bool:
    """
    Calls Qt's 'bool QWidgetLineControl::allSelected() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#allSelected
    """
    #  bool QWidgetLineControl::allSelected() const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl11allSelectedEv',
    )

  def hasSelectedText(self) -> bool:
    """
    Calls Qt's 'bool QWidgetLineControl::hasSelectedText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#hasSelectedText
    """
    #  bool QWidgetLineControl::hasSelectedText() const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl15hasSelectedTextEv',
    )

  def width(self) -> int:
    """
    Calls Qt's 'int QWidgetLineControl::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#width
    """
    #  int QWidgetLineControl::width() const
    return self.uglySide.call('ritual_ZNK18QWidgetLineControl5widthEv')

  def height(self) -> int:
    """
    Calls Qt's 'int QWidgetLineControl::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#height
    """
    #  int QWidgetLineControl::height() const
    return self.uglySide.call('ritual_ZNK18QWidgetLineControl6heightEv')

  def ascent(self) -> int:
    """
    Calls Qt's 'int QWidgetLineControl::ascent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#ascent
    """
    #  int QWidgetLineControl::ascent() const
    return self.uglySide.call('ritual_ZNK18QWidgetLineControl6ascentEv')

  def naturalTextWidth(self) -> float:
    """
    Calls Qt's 'qreal QWidgetLineControl::naturalTextWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#naturalTextWidth
    """
    #  qreal QWidgetLineControl::naturalTextWidth() const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl16naturalTextWidthEv',
    )

  def selectedText(self) -> str:
    """
    Calls Qt's 'QString QWidgetLineControl::selectedText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#selectedText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWidgetLineControl::selectedText() const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl12selectedTextEv',
    )

  def textBeforeSelection(self) -> str:
    """
    Calls Qt's 'QString QWidgetLineControl::textBeforeSelection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#textBeforeSelection

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWidgetLineControl::textBeforeSelection() const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl19textBeforeSelectionEv',
    )

  def textAfterSelection(self) -> str:
    """
    Calls Qt's 'QString QWidgetLineControl::textAfterSelection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#textAfterSelection

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWidgetLineControl::textAfterSelection() const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl18textAfterSelectionEv',
    )

  def selectionStart(self) -> int:
    """
    Calls Qt's 'int QWidgetLineControl::selectionStart() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#selectionStart
    """
    #  int QWidgetLineControl::selectionStart() const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl14selectionStartEv',
    )

  def selectionEnd(self) -> int:
    """
    Calls Qt's 'int QWidgetLineControl::selectionEnd() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#selectionEnd
    """
    #  int QWidgetLineControl::selectionEnd() const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl12selectionEndEv',
    )

  @overload(int)
  def inSelection(self, x: int) -> bool:
    """
    Calls Qt's 'bool QWidgetLineControl::inSelection(int x) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#inSelection

    Parameters
    ----------

    x : int
      Passed on as it is.
    """
    #  bool QWidgetLineControl::inSelection(int x) const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl11inSelectionEi', x,
    )

  def start(self) -> int:
    """
    Calls Qt's 'int QWidgetLineControl::start() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#start
    """
    #  int QWidgetLineControl::start() const
    return self.uglySide.call('ritual_ZNK18QWidgetLineControl5startEv')

  @overload()
  def end(self) -> int:
    """
    Calls Qt's 'int QWidgetLineControl::end() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#end
    """
    #  int QWidgetLineControl::end() const
    return self.uglySide.call('ritual_ZNK18QWidgetLineControl3endEv')

  @overload(bool)
  def end(self, mark: bool) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::end(bool mark)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#end

    Parameters
    ----------

    mark : bool
      Passed on as it is.
    """
    #  void QWidgetLineControl::end(bool mark)
    self.uglySide.call('ritual_ZN18QWidgetLineControl3endEb', mark)

  def cursor(self) -> int:
    """
    Calls Qt's 'int QWidgetLineControl::cursor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#cursor
    """
    #  int QWidgetLineControl::cursor() const
    return self.uglySide.call('ritual_ZNK18QWidgetLineControl6cursorEv')

  def preeditCursor(self) -> int:
    """
    Calls Qt's 'int QWidgetLineControl::preeditCursor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#preeditCursor
    """
    #  int QWidgetLineControl::preeditCursor() const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl13preeditCursorEv',
    )

  def cursorWidth(self) -> int:
    """
    Calls Qt's 'int QWidgetLineControl::cursorWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#cursorWidth
    """
    #  int QWidgetLineControl::cursorWidth() const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl11cursorWidthEv',
    )

  def cursorMoveStyle(self) -> Qt.CursorMoveStyle:
    """
    Calls Qt's 'Qt::CursorMoveStyle QWidgetLineControl::cursorMoveStyle()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#cursorMoveStyle

    Returns
    -------

    Qt.CursorMoveStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.CursorMoveStyle(number)' gives.
    """
    #  Qt::CursorMoveStyle QWidgetLineControl::cursorMoveStyle() const
    return Qt.CursorMoveStyle(self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl15cursorMoveStyleEv',
    ))

  @overload(int)
  @overload(int, QTextLine.CursorPosition)
  def xToPos(
      self,
      x: int,
      a1: QTextLine.CursorPosition = (
          QTextLine.CursorPosition.CursorBetweenCharacters),
  ) -> int:
    """
    Calls Qt's 'int QWidgetLineControl::xToPos(int x,
    QTextLine::CursorPosition a1) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#xToPos

    Parameters
    ----------

    x : int
      Passed on as it is.

    a1 : QTextLine.CursorPosition
      Passed on as its number. May be left out, as in Qt: it is then
      QTextLine.CursorPosition.CursorBetweenCharacters.
    """
    #  int QWidgetLineControl::xToPos(int x, QTextLine::CursorPosition a1)
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl6xToPosEiN9QTextLine14CursorPosition'
        'E',
        x, a1.value,
    )

  @overload(int)
  def rectForPos(self, pos: int) -> QRect:
    """
    Calls Qt's 'QRect QWidgetLineControl::rectForPos(int pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#rectForPos

    Parameters
    ----------

    pos : int
      Passed on as it is.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QWidgetLineControl::rectForPos(int pos) const
    address = self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl10rectForPosEi', pos,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def cursorRect(self) -> QRect:
    """
    Calls Qt's 'QRect QWidgetLineControl::cursorRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#cursorRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QWidgetLineControl::cursorRect() const
    address = self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl10cursorRectEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def anchorRect(self) -> QRect:
    """
    Calls Qt's 'QRect QWidgetLineControl::anchorRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#anchorRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QWidgetLineControl::anchorRect() const
    address = self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl10anchorRectEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(int)
  def cursorToX(self, cursor: int) -> float:
    """
    Calls Qt's 'qreal QWidgetLineControl::cursorToX(int cursor) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#cursorToX

    Parameters
    ----------

    cursor : int
      Passed on as it is.
    """
    #  qreal QWidgetLineControl::cursorToX(int cursor) const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl9cursorToXEi', cursor,
    )

  @overload()
  def cursorToX(self) -> float:
    """
    Calls Qt's 'qreal QWidgetLineControl::cursorToX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#cursorToX
    """
    #  qreal QWidgetLineControl::cursorToX() const
    return self.uglySide.call('ritual_ZNK18QWidgetLineControl9cursorToXEv')

  def isReadOnly(self) -> bool:
    """
    Calls Qt's 'bool QWidgetLineControl::isReadOnly() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#isReadOnly
    """
    #  bool QWidgetLineControl::isReadOnly() const
    return self.uglySide.call('ritual_ZNK18QWidgetLineControl10isReadOnlyEv')

  def text(self) -> str:
    """
    Calls Qt's 'QString QWidgetLineControl::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWidgetLineControl::text() const
    return self.uglySide.call('ritual_ZNK18QWidgetLineControl4textEv')

  def displayText(self) -> str:
    """
    Calls Qt's 'QString QWidgetLineControl::displayText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#displayText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWidgetLineControl::displayText() const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl11displayTextEv',
    )

  def surroundingText(self) -> str:
    """
    Calls Qt's 'QString QWidgetLineControl::surroundingText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#surroundingText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWidgetLineControl::surroundingText() const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl15surroundingTextEv',
    )

  def echoMode(self) -> int:
    """
    Calls Qt's 'uint QWidgetLineControl::echoMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#echoMode
    """
    #  uint QWidgetLineControl::echoMode() const
    return self.uglySide.call('ritual_ZNK18QWidgetLineControl8echoModeEv')

  def maxLength(self) -> int:
    """
    Calls Qt's 'int QWidgetLineControl::maxLength() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#maxLength
    """
    #  int QWidgetLineControl::maxLength() const
    return self.uglySide.call('ritual_ZNK18QWidgetLineControl9maxLengthEv')

  def validator(self) -> Optional[QValidator]:
    """
    Calls Qt's 'const QValidator *QWidgetLineControl::validator() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#validator

    Returns
    -------

    Optional[QValidator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QValidator *QWidgetLineControl::validator() const
    address = self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl9validatorEv',
    )
    from ..QtGui import QValidator
    return QValidator._cuteAt(address)

  def completer(self) -> Optional[QCompleter]:
    """
    Calls Qt's 'QCompleter *QWidgetLineControl::completer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#completer

    Returns
    -------

    Optional[QCompleter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCompleter *QWidgetLineControl::completer() const
    address = self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl9completerEv',
    )
    from . import QCompleter
    return QCompleter._cuteAt(address)

  def cursorPosition(self) -> int:
    """
    Calls Qt's 'int QWidgetLineControl::cursorPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#cursorPosition
    """
    #  int QWidgetLineControl::cursorPosition() const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl14cursorPositionEv',
    )

  @overload()
  def hasAcceptableInput(self) -> bool:
    """
    Calls Qt's 'bool QWidgetLineControl::hasAcceptableInput() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#hasAcceptableInput
    """
    #  bool QWidgetLineControl::hasAcceptableInput() const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl18hasAcceptableInputEv',
    )

  @overload(str)
  def hasAcceptableInput(self, text: str) -> bool:
    """
    Calls Qt's 'bool QWidgetLineControl::hasAcceptableInput(const QString
    &text) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#hasAcceptableInput

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QWidgetLineControl::hasAcceptableInput(const QString &text) const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl18hasAcceptableInputERK7QString',
        text,
    )

  def inputMask(self) -> str:
    """
    Calls Qt's 'QString QWidgetLineControl::inputMask() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#inputMask

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWidgetLineControl::inputMask() const
    return self.uglySide.call('ritual_ZNK18QWidgetLineControl9inputMaskEv')

  def composeMode(self) -> bool:
    """
    Calls Qt's 'bool QWidgetLineControl::composeMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#composeMode
    """
    #  bool QWidgetLineControl::composeMode() const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl11composeModeEv',
    )

  def preeditAreaText(self) -> str:
    """
    Calls Qt's 'QString QWidgetLineControl::preeditAreaText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#preeditAreaText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWidgetLineControl::preeditAreaText() const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl15preeditAreaTextEv',
    )

  def passwordEchoEditing(self) -> bool:
    """
    Calls Qt's 'bool QWidgetLineControl::passwordEchoEditing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#passwordEchoEditing
    """
    #  bool QWidgetLineControl::passwordEchoEditing() const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl19passwordEchoEditingEv',
    )

  def passwordCharacter(self) -> QChar:
    """
    Calls Qt's 'QChar QWidgetLineControl::passwordCharacter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#passwordCharacter

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QWidgetLineControl::passwordCharacter() const
    address = self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl17passwordCharacterEv',
    )
    from ..QtCore import QChar
    return QChar._cuteOwning(address)

  def passwordMaskDelay(self) -> int:
    """
    Calls Qt's 'int QWidgetLineControl::passwordMaskDelay() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#passwordMaskDelay
    """
    #  int QWidgetLineControl::passwordMaskDelay() const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl17passwordMaskDelayEv',
    )

  def layoutDirection(self) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection QWidgetLineControl::layoutDirection()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#layoutDirection

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection QWidgetLineControl::layoutDirection() const
    return Qt.LayoutDirection(self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl15layoutDirectionEv',
    ))

  def cursorBlinkStatus(self) -> bool:
    """
    Calls Qt's 'bool QWidgetLineControl::cursorBlinkStatus() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#cursorBlinkStatus
    """
    #  bool QWidgetLineControl::cursorBlinkStatus() const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl17cursorBlinkStatusEv',
    )

  def cancelText(self) -> str:
    """
    Calls Qt's 'QString QWidgetLineControl::cancelText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#cancelText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWidgetLineControl::cancelText() const
    return self.uglySide.call('ritual_ZNK18QWidgetLineControl10cancelTextEv')

  def palette(self) -> QPalette:
    """
    Calls Qt's 'const QPalette &QWidgetLineControl::palette() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#palette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  const QPalette &QWidgetLineControl::palette() const
    address = self.uglySide.call('ritual_ZNK18QWidgetLineControl7paletteEv')
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

  def textLayout(self) -> Optional[QTextLayout]:
    """
    Calls Qt's 'QTextLayout *QWidgetLineControl::textLayout() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#textLayout

    Returns
    -------

    Optional[QTextLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextLayout *QWidgetLineControl::textLayout() const
    address = self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl10textLayoutEv',
    )
    from ..QtGui import QTextLayout
    return QTextLayout._cuteAt(address)

  @overload(QChar, QChar)
  def isValidInput(self, key: QChar, mask: QChar) -> bool:
    """
    Calls Qt's 'bool QWidgetLineControl::isValidInput(QChar key, QChar mask)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#isValidInput

    Parameters
    ----------

    key : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    mask : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool QWidgetLineControl::isValidInput(QChar key, QChar mask) const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl12isValidInputE5QCharS0_',
        self._valueOf(key), self._valueOf(mask),
    )

  @overload(int, str)
  @overload(int, str, bool)
  def maskString(self, pos: int, str: str, clear: bool = False) -> str:
    """
    Calls Qt's 'QString QWidgetLineControl::maskString(int pos, const QString
    &str, bool clear) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#maskString

    Parameters
    ----------

    pos : int
      Passed on as it is.

    str : str
      Passed on as it is: a QString is made of it for the call.

    clear : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWidgetLineControl::maskString(int pos, const QString &str,
    #      bool clear) const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl10maskStringEiRK7QStringb',
        pos, str, clear,
    )

  @overload(int, int)
  def clearString(self, pos: int, len: int) -> str:
    """
    Calls Qt's 'QString QWidgetLineControl::clearString(int pos, int len)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#clearString

    Parameters
    ----------

    pos : int
      Passed on as it is.

    len : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWidgetLineControl::clearString(int pos, int len) const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl11clearStringEii', pos, len,
    )

  @overload(str)
  def stripString(self, str: str) -> str:
    """
    Calls Qt's 'QString QWidgetLineControl::stripString(const QString &str)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#stripString

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWidgetLineControl::stripString(const QString &str) const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl11stripStringERK7QString', str,
    )

  @overload(int, bool, bool)
  @overload(int, bool, bool, QChar)
  def findInMask(
      self,
      pos: int,
      forward: bool,
      findSeparator: bool,
      searchChar: Optional[QChar] = None,
  ) -> int:
    """
    Calls Qt's 'int QWidgetLineControl::findInMask(int pos, bool forward,
    bool findSeparator, QChar searchChar) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#findInMask

    Parameters
    ----------

    pos : int
      Passed on as it is.

    forward : bool
      Passed on as it is.

    findSeparator : bool
      Passed on as it is.

    searchChar : Optional[QChar]
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
      May be left out, as in Qt: a new 'QChar()' is then passed on.
    """
    #  int QWidgetLineControl::findInMask(int pos, bool forward, bool
    #      findSeparator, QChar searchChar) const
    if searchChar is None:
      from ..QtCore import QChar
      searchChar = QChar()
    return self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl10findInMaskEibb5QChar',
        pos, forward, findSeparator, self._valueOf(searchChar),
    )

  def redoTextLayout(self) -> int:
    """
    Calls Qt's 'int QWidgetLineControl::redoTextLayout() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#redoTextLayout
    """
    #  int QWidgetLineControl::redoTextLayout() const
    return self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl14redoTextLayoutEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def setAccessibleObject(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::setAccessibleObject(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#setAccessibleObject

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetLineControl::setAccessibleObject(QObject *object)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl19setAccessibleObjectEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  @overload(bool)
  def setModified(self, modified: bool) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::setModified(bool modified)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#setModified

    Parameters
    ----------

    modified : bool
      Passed on as it is.
    """
    #  void QWidgetLineControl::setModified(bool modified)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl11setModifiedEb', modified,
    )

  @overload(int, int)
  def setSelection(self, start: int, length: int) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::setSelection(int start, int
    length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#setSelection

    Parameters
    ----------

    start : int
      Passed on as it is.

    length : int
      Passed on as it is.
    """
    #  void QWidgetLineControl::setSelection(int start, int length)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl12setSelectionEii', start, length,
    )

  @overload(int)
  def setCursorWidth(self, value: int) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::setCursorWidth(int value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#setCursorWidth

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QWidgetLineControl::setCursorWidth(int value)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl14setCursorWidthEi', value,
    )

  @overload(Qt.CursorMoveStyle)
  def setCursorMoveStyle(self, style: Qt.CursorMoveStyle) -> None:
    """
    Calls Qt's 'void
    QWidgetLineControl::setCursorMoveStyle(Qt::CursorMoveStyle style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#setCursorMoveStyle

    Parameters
    ----------

    style : Qt.CursorMoveStyle
      Passed on as its number.
    """
    #  void QWidgetLineControl::setCursorMoveStyle(Qt::CursorMoveStyle style)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl18setCursorMoveStyleEN2Qt15CursorMove'
        'StyleE',
        style.value,
    )

  @overload(bool)
  def setReadOnly(self, enable: bool) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::setReadOnly(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#setReadOnly

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QWidgetLineControl::setReadOnly(bool enable)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl11setReadOnlyEb', enable,
    )

  @overload(str)
  def setText(self, txt: str) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::setText(const QString &txt)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#setText

    Parameters
    ----------

    txt : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidgetLineControl::setText(const QString &txt)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl7setTextERK7QString', txt,
    )

  @overload(int)
  def setEchoMode(self, mode: int) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::setEchoMode(uint mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#setEchoMode

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QWidgetLineControl::setEchoMode(uint mode)
    self.uglySide.call('ritual_ZN18QWidgetLineControl11setEchoModeEj', mode)

  @overload(int)
  def setMaxLength(self, maxLength: int) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::setMaxLength(int maxLength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#setMaxLength

    Parameters
    ----------

    maxLength : int
      Passed on as it is.
    """
    #  void QWidgetLineControl::setMaxLength(int maxLength)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl12setMaxLengthEi', maxLength,
    )

  @overload(QValidator)
  @overload(NoneType)
  def setValidator(self, v: Optional[QValidator]) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::setValidator(const QValidator *v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#setValidator

    Parameters
    ----------

    v : Optional[QValidator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetLineControl::setValidator(const QValidator *v)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl12setValidatorEPK10QValidator',
        self._addressOf(v),
    )

  @overload(QCompleter)
  @overload(NoneType)
  def setCompleter(self, c: Optional[QCompleter]) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::setCompleter(const QCompleter *c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#setCompleter

    Parameters
    ----------

    c : Optional[QCompleter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetLineControl::setCompleter(const QCompleter *c)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl12setCompleterEPK10QCompleter',
        self._addressOf(c),
    )

  @overload(int)
  def setCursorPosition(self, pos: int) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::setCursorPosition(int pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#setCursorPosition

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  void QWidgetLineControl::setCursorPosition(int pos)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl17setCursorPositionEi', pos,
    )

  @overload(str)
  def setInputMask(self, mask: str) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::setInputMask(const QString &mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#setInputMask

    Parameters
    ----------

    mask : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidgetLineControl::setInputMask(const QString &mask)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl12setInputMaskERK7QString', mask,
    )

  @overload(int, str)
  def setPreeditArea(self, cursor: int, text: str) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::setPreeditArea(int cursor, const
    QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#setPreeditArea

    Parameters
    ----------

    cursor : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidgetLineControl::setPreeditArea(int cursor, const QString
    #      &text)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl14setPreeditAreaEiRK7QString',
        cursor, text,
    )

  @overload(QChar)
  def setPasswordCharacter(self, character: QChar) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::setPasswordCharacter(QChar
    character)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#setPasswordCharacter

    Parameters
    ----------

    character : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  void QWidgetLineControl::setPasswordCharacter(QChar character)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl20setPasswordCharacterE5QChar',
        self._valueOf(character),
    )

  @overload(int)
  def setPasswordMaskDelay(self, delay: int) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::setPasswordMaskDelay(int delay)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#setPasswordMaskDelay

    Parameters
    ----------

    delay : int
      Passed on as it is.
    """
    #  void QWidgetLineControl::setPasswordMaskDelay(int delay)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl20setPasswordMaskDelayEi', delay,
    )

  @overload(Qt.LayoutDirection)
  def setLayoutDirection(self, direction: Qt.LayoutDirection) -> None:
    """
    Calls Qt's 'void
    QWidgetLineControl::setLayoutDirection(Qt::LayoutDirection direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#setLayoutDirection

    Parameters
    ----------

    direction : Qt.LayoutDirection
      Passed on as its number.
    """
    #  void QWidgetLineControl::setLayoutDirection(Qt::LayoutDirection
    #      direction)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl18setLayoutDirectionEN2Qt15LayoutDire'
        'ctionE',
        direction.value,
    )

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::setFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QWidgetLineControl::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl7setFontERK5QFont',
        self._valueOf(font),
    )

  @overload(bool)
  def setBlinkingCursorEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::setBlinkingCursorEnabled(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#setBlinkingCursorEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QWidgetLineControl::setBlinkingCursorEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl24setBlinkingCursorEnabledEb', enable,
    )

  @overload(str)
  def setCancelText(self, text: str) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::setCancelText(const QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#setCancelText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidgetLineControl::setCancelText(const QString &text)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl13setCancelTextERK7QString', text,
    )

  @overload(QPalette)
  def setPalette(self, p: QPalette) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::setPalette(const QPalette &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#setPalette

    Parameters
    ----------

    p : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.
    """
    #  void QWidgetLineControl::setPalette(const QPalette &p)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl10setPaletteERK8QPalette',
        self._valueOf(p),
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
  @overload(str)
  def __init__(self, txt: str = '') -> None:
    """
    Notes what was given, for Qt's
    'QWidgetLineControl::QWidgetLineControl(const QString &txt)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#QWidgetLineControl

    Parameters
    ----------

    txt : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  QWidgetLineControl::QWidgetLineControl(const QString &txt)
    self._noteCreation(QWidgetLineControl, lambda: Rituals.call(
        'ritual_ZN18QWidgetLineControlC1ERK7QString', txt,
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

  def accessibleObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QWidgetLineControl::accessibleObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#accessibleObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QWidgetLineControl::accessibleObject()
    address = self.uglySide.call(
        'ritual_ZN18QWidgetLineControl16accessibleObjectEv',
    )
    return QObject._cuteAt(address)

  @overload(int)
  def nextMaskBlank(self, pos: int) -> int:
    """
    Calls Qt's 'int QWidgetLineControl::nextMaskBlank(int pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#nextMaskBlank

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  int QWidgetLineControl::nextMaskBlank(int pos)
    return self.uglySide.call(
        'ritual_ZN18QWidgetLineControl13nextMaskBlankEi', pos,
    )

  @overload(int)
  def prevMaskBlank(self, pos: int) -> int:
    """
    Calls Qt's 'int QWidgetLineControl::prevMaskBlank(int pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#prevMaskBlank

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  int QWidgetLineControl::prevMaskBlank(int pos)
    return self.uglySide.call(
        'ritual_ZN18QWidgetLineControl13prevMaskBlankEi', pos,
    )

  def clearUndo(self) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::clearUndo()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#clearUndo
    """
    #  void QWidgetLineControl::clearUndo()
    self.uglySide.call('ritual_ZN18QWidgetLineControl9clearUndoEv')

  def removeSelection(self) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::removeSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#removeSelection
    """
    #  void QWidgetLineControl::removeSelection()
    self.uglySide.call('ritual_ZN18QWidgetLineControl15removeSelectionEv')

  @overload()
  @overload(QClipboard.Mode)
  def copy(self, mode: QClipboard.Mode = QClipboard.Mode.Clipboard) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::copy(QClipboard::Mode mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#copy

    Parameters
    ----------

    mode : QClipboard.Mode
      Passed on as its number. May be left out, as in Qt: it is then
      QClipboard.Mode.Clipboard.
    """
    #  void QWidgetLineControl::copy(QClipboard::Mode mode) const
    self.uglySide.call(
        'ritual_ZNK18QWidgetLineControl4copyEN10QClipboard4ModeE',
        mode.value,
    )

  @overload()
  @overload(QClipboard.Mode)
  def paste(self, mode: QClipboard.Mode = QClipboard.Mode.Clipboard) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::paste(QClipboard::Mode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#paste

    Parameters
    ----------

    mode : QClipboard.Mode
      Passed on as its number. May be left out, as in Qt: it is then
      QClipboard.Mode.Clipboard.
    """
    #  void QWidgetLineControl::paste(QClipboard::Mode mode)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl5pasteEN10QClipboard4ModeE',
        mode.value,
    )

  @overload(int)
  @overload(int, bool)
  def moveCursor(self, pos: int, mark: bool = False) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::moveCursor(int pos, bool mark)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#moveCursor

    Parameters
    ----------

    pos : int
      Passed on as it is.

    mark : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QWidgetLineControl::moveCursor(int pos, bool mark)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl10moveCursorEib', pos, mark,
    )

  @overload(bool, int)
  def cursorForward(self, mark: bool, steps: int) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::cursorForward(bool mark, int
    steps)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#cursorForward

    Parameters
    ----------

    mark : bool
      Passed on as it is.

    steps : int
      Passed on as it is.
    """
    #  void QWidgetLineControl::cursorForward(bool mark, int steps)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl13cursorForwardEbi', mark, steps,
    )

  @overload(bool)
  def cursorWordForward(self, mark: bool) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::cursorWordForward(bool mark)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#cursorWordForward

    Parameters
    ----------

    mark : bool
      Passed on as it is.
    """
    #  void QWidgetLineControl::cursorWordForward(bool mark)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl17cursorWordForwardEb', mark,
    )

  @overload(bool)
  def cursorWordBackward(self, mark: bool) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::cursorWordBackward(bool mark)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#cursorWordBackward

    Parameters
    ----------

    mark : bool
      Passed on as it is.
    """
    #  void QWidgetLineControl::cursorWordBackward(bool mark)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl18cursorWordBackwardEb', mark,
    )

  @overload(bool)
  def home(self, mark: bool) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::home(bool mark)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#home

    Parameters
    ----------

    mark : bool
      Passed on as it is.
    """
    #  void QWidgetLineControl::home(bool mark)
    self.uglySide.call('ritual_ZN18QWidgetLineControl4homeEb', mark)

  def commitPreedit(self) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::commitPreedit()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#commitPreedit
    """
    #  void QWidgetLineControl::commitPreedit()
    self.uglySide.call('ritual_ZN18QWidgetLineControl13commitPreeditEv')

  def backspace(self) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::backspace()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#backspace
    """
    #  void QWidgetLineControl::backspace()
    self.uglySide.call('ritual_ZN18QWidgetLineControl9backspaceEv')

  def del_(self) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::del()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#del
    """
    #  void QWidgetLineControl::del()
    self.uglySide.call('ritual_ZN18QWidgetLineControl3delEv')

  def deselect(self) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::deselect()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#deselect
    """
    #  void QWidgetLineControl::deselect()
    self.uglySide.call('ritual_ZN18QWidgetLineControl8deselectEv')

  def selectAll(self) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::selectAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#selectAll
    """
    #  void QWidgetLineControl::selectAll()
    self.uglySide.call('ritual_ZN18QWidgetLineControl9selectAllEv')

  @overload(str)
  def insert(self, a0: str) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::insert(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#insert

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidgetLineControl::insert(const QString &a0)
    self.uglySide.call('ritual_ZN18QWidgetLineControl6insertERK7QString', a0)

  def clear(self) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#clear
    """
    #  void QWidgetLineControl::clear()
    self.uglySide.call('ritual_ZN18QWidgetLineControl5clearEv')

  def undo(self) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::undo()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#undo
    """
    #  void QWidgetLineControl::undo()
    self.uglySide.call('ritual_ZN18QWidgetLineControl4undoEv')

  def redo(self) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::redo()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#redo
    """
    #  void QWidgetLineControl::redo()
    self.uglySide.call('ritual_ZN18QWidgetLineControl4redoEv')

  @overload(int)
  def selectWordAtPos(self, a0: int) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::selectWordAtPos(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#selectWordAtPos

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QWidgetLineControl::selectWordAtPos(int a0)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl15selectWordAtPosEi', a0,
    )

  @overload(int)
  def complete(self, key: int) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::complete(int key)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#complete

    Parameters
    ----------

    key : int
      Passed on as it is.
    """
    #  void QWidgetLineControl::complete(int key)
    self.uglySide.call('ritual_ZN18QWidgetLineControl8completeEi', key)

  def fixup(self) -> bool:
    """
    Calls Qt's 'bool QWidgetLineControl::fixup()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#fixup
    """
    #  bool QWidgetLineControl::fixup()
    return self.uglySide.call('ritual_ZN18QWidgetLineControl5fixupEv')

  @overload(bool)
  def updatePasswordEchoEditing(self, editing: bool) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::updatePasswordEchoEditing(bool
    editing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#updatePasswordEchoEditing

    Parameters
    ----------

    editing : bool
      Passed on as it is.
    """
    #  void QWidgetLineControl::updatePasswordEchoEditing(bool editing)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl25updatePasswordEchoEditingEb',
        editing,
    )

  @overload(QInputMethodEvent)
  @overload(NoneType)
  def processInputMethodEvent(
      self,
      event: Optional[QInputMethodEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QWidgetLineControl::processInputMethodEvent(QInputMethodEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#processInputMethodEvent

    Parameters
    ----------

    event : Optional[QInputMethodEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetLineControl::processInputMethodEvent(QInputMethodEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl23processInputMethodEventEP17QInputMe'
        'thodEvent',
        self._addressOf(event),
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def processKeyEvent(self, ev: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::processKeyEvent(QKeyEvent *ev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#processKeyEvent

    Parameters
    ----------

    ev : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetLineControl::processKeyEvent(QKeyEvent *ev)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl15processKeyEventEP9QKeyEvent',
        self._addressOf(ev),
    )

  def updateCursorBlinking(self) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::updateCursorBlinking()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#updateCursorBlinking
    """
    #  void QWidgetLineControl::updateCursorBlinking()
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl20updateCursorBlinkingEv',
    )

  def resetCursorBlinkTimer(self) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::resetCursorBlinkTimer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#resetCursorBlinkTimer
    """
    #  void QWidgetLineControl::resetCursorBlinkTimer()
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl21resetCursorBlinkTimerEv',
    )

  @overload(QPainter, QPoint, QRect)
  @overload(NoneType, QPoint, QRect)
  @overload(QPainter, QPoint, QRect, int)
  @overload(NoneType, QPoint, QRect, int)
  def draw(
      self,
      a0: Optional[QPainter],
      a1: QPoint,
      a2: QRect,
      flags: int = 7,
  ) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::draw(QPainter *a0, const QPoint &a1,
    const QRect &a2, int flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#draw

    Parameters
    ----------

    a0 : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    a2 : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    flags : int
      Passed on as it is. May be left out, as in Qt: it is then 7.
    """
    #  void QWidgetLineControl::draw(QPainter *a0, const QPoint &a1, const
    #      QRect &a2, int flags)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl4drawEP8QPainterRK6QPointRK5QRecti',
        self._addressOf(a0), self._valueOf(a1), self._valueOf(a2), flags,
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def processShortcutOverrideEvent(self, ke: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    QWidgetLineControl::processShortcutOverrideEvent(QKeyEvent *ke)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html

    Parameters
    ----------

    ke : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetLineControl::processShortcutOverrideEvent(QKeyEvent *ke)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl28processShortcutOverrideEventEP9QKey'
        'Event',
        self._addressOf(ke),
    )

  @overload(str)
  def init(self, txt: str) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::init(const QString &txt)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#init

    Parameters
    ----------

    txt : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidgetLineControl::init(const QString &txt)
    self.uglySide.call('ritual_ZN18QWidgetLineControl4initERK7QString', txt)

  def removeSelectedText(self) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::removeSelectedText()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#removeSelectedText
    """
    #  void QWidgetLineControl::removeSelectedText()
    self.uglySide.call('ritual_ZN18QWidgetLineControl18removeSelectedTextEv')

  @overload(str)
  @overload(str, int)
  @overload(str, int, bool)
  def internalSetText(
      self,
      txt: str,
      pos: int = -1,
      edited: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::internalSetText(const QString &txt,
    int pos, bool edited)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#internalSetText

    Parameters
    ----------

    txt : str
      Passed on as it is: a QString is made of it for the call.

    pos : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    edited : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QWidgetLineControl::internalSetText(const QString &txt, int pos,
    #      bool edited)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl15internalSetTextERK7QStringib',
        txt, pos, edited,
    )

  @overload()
  @overload(bool)
  def updateDisplayText(self, forceUpdate: bool = False) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::updateDisplayText(bool
    forceUpdate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#updateDisplayText

    Parameters
    ----------

    forceUpdate : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QWidgetLineControl::updateDisplayText(bool forceUpdate)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl17updateDisplayTextEb', forceUpdate,
    )

  @overload(str)
  def internalInsert(self, s: str) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::internalInsert(const QString &s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#internalInsert

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidgetLineControl::internalInsert(const QString &s)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl14internalInsertERK7QString', s,
    )

  @overload()
  @overload(bool)
  def internalDelete(self, wasBackspace: bool = False) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::internalDelete(bool wasBackspace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#internalDelete

    Parameters
    ----------

    wasBackspace : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QWidgetLineControl::internalDelete(bool wasBackspace)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl14internalDeleteEb', wasBackspace,
    )

  def internalDeselect(self) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::internalDeselect()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#internalDeselect
    """
    #  void QWidgetLineControl::internalDeselect()
    self.uglySide.call('ritual_ZN18QWidgetLineControl16internalDeselectEv')

  @overload()
  @overload(int)
  def internalUndo(self, until: int = -1) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::internalUndo(int until)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#internalUndo

    Parameters
    ----------

    until : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void QWidgetLineControl::internalUndo(int until)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl12internalUndoEi', until,
    )

  def internalRedo(self) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::internalRedo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#internalRedo
    """
    #  void QWidgetLineControl::internalRedo()
    self.uglySide.call('ritual_ZN18QWidgetLineControl12internalRedoEv')

  def emitCursorPositionChanged(self) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::emitCursorPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#emitCursorPositionChanged
    """
    #  void QWidgetLineControl::emitCursorPositionChanged()
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl25emitCursorPositionChangedEv',
    )

  @overload()
  @overload(int)
  @overload(int, bool)
  @overload(int, bool, bool)
  def finishChange(
      self,
      validateFromState: int = -1,
      update: bool = False,
      edited: bool = True,
  ) -> bool:
    """
    Calls Qt's 'bool QWidgetLineControl::finishChange(int validateFromState,
    bool update, bool edited)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#finishChange

    Parameters
    ----------

    validateFromState : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    update : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    edited : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  bool QWidgetLineControl::finishChange(int validateFromState, bool
    #      update, bool edited)
    return self.uglySide.call(
        'ritual_ZN18QWidgetLineControl12finishChangeEibb',
        validateFromState, update, edited,
    )

  @overload(int)
  def advanceToEnabledItem(self, dir: int) -> bool:
    """
    Calls Qt's 'bool QWidgetLineControl::advanceToEnabledItem(int dir)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#advanceToEnabledItem

    Parameters
    ----------

    dir : int
      Passed on as it is.
    """
    #  bool QWidgetLineControl::advanceToEnabledItem(int dir)
    return self.uglySide.call(
        'ritual_ZN18QWidgetLineControl20advanceToEnabledItemEi', dir,
    )

  def separate(self) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::separate()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#separate
    """
    #  void QWidgetLineControl::separate()
    self.uglySide.call('ritual_ZN18QWidgetLineControl8separateEv')

  @overload(str)
  def parseInputMask(self, maskFields: str) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::parseInputMask(const QString
    &maskFields)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#parseInputMask

    Parameters
    ----------

    maskFields : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWidgetLineControl::parseInputMask(const QString &maskFields)
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl14parseInputMaskERK7QString',
        maskFields,
    )

  def cancelPasswordEchoTimer(self) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::cancelPasswordEchoTimer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#cancelPasswordEchoTimer
    """
    #  void QWidgetLineControl::cancelPasswordEchoTimer()
    self.uglySide.call(
        'ritual_ZN18QWidgetLineControl23cancelPasswordEchoTimerEv',
    )

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::timerEvent(QTimerEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetlinecontrol.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetLineControl::timerEvent(QTimerEvent *event)
    ritual = 'ritual_ZN18QWidgetLineControl10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QWidgetLineControl10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  def _q_deleteSelected(self) -> None:
    """
    Calls Qt's 'void QWidgetLineControl::_q_deleteSelected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetlinecontrol.html#_q_deleteSelected
    """
    #  void QWidgetLineControl::_q_deleteSelected()
    self.uglySide.call('ritual_ZN18QWidgetLineControl17_q_deleteSelectedEv')
