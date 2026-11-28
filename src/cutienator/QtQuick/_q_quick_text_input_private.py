"""
QQuickTextInputPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktextinput_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickTextInputPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QAccessible, QClipboard, QTextLine
from . import QQuickImplicitSizeItemPrivate, QQuickTextInput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QChar, QPointF, QRectF
  from ..QtGui import QContextMenuEvent, QFocusEvent, QInputMethodEvent
  from ..QtGui import QKeyEvent, QMouseEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChar = WAIT['QChar']
  QContextMenuEvent = WAIT['QContextMenuEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QInputMethodEvent = WAIT['QInputMethodEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QPointF = WAIT['QPointF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTextInputPrivate(QQuickImplicitSizeItemPrivate):
  """
  The cute side of Qt's QQuickTextInputPrivate: a plain Python object
  standing in front of one C++ QQuickTextInputPrivate.

  It is built on the cute 'QQuickImplicitSizeItemPrivate', as Qt's
  QQuickTextInputPrivate is built on Qt's QQuickImplicitSizeItemPrivate, and
  has everything that class has. Qt's QQuickTextInputPrivate is built on Qt's
  QAccessible::ActivationObserver as well, which is not reflected.

  What exists
  -----------

  Every function of Qt's QQuickTextInputPrivate that has a ritual and that
  Python can call so far, 107 names in all: 'q_func', 'init', 'cancelInput',
  'ensureVisible', 'updateHorizontalScroll', 'updateVerticalScroll',
  'determineHorizontalAlignment', 'setHAlign', 'mirrorChange',
  'handleContextMenuEvent', 'sendMouseEventToInputContext',
  'effectiveInputMethodHints', 'handleFocusEvent', 'readOnlyChanged',
  'echoModeChanged', 'accessibilityActiveChanged', 'accessibleRole', 'get',
  'hasPendingTripleClick', 'setNativeCursorEnabled', 'nextMaskBlank',
  'prevMaskBlank', 'isUndoAvailable', 'isRedoAvailable', 'clearUndo',
  'allSelected', 'hasSelectedText', 'setSelection', 'selectedText',
  'textBeforeSelection', 'textAfterSelection', 'selectionStart',
  'selectionEnd', 'anchorRectangle', 'positionAt', 'removeSelection',
  'start', 'end', 'realText', 'copy', 'paste', 'commitPreedit',
  'cancelPreedit', 'cursorMoveStyle', 'setCursorMoveStyle', 'moveCursor',
  'cursorForward', 'cursorWordForward', 'cursorWordBackward', 'home',
  'backspace', 'del_', 'deselect', 'selectAll', 'insert', 'clear',
  'selectWordAtPos', 'setCursorPosition', 'fixup', 'inputMask',
  'setInputMask', 'composeMode', 'preeditAreaText',
  'updatePasswordEchoEditing', 'cancelPasswordEchoTimer', 'textDirection',
  'layoutDirection', 'setLayoutDirection', 'processInputMethodEvent',
  'processKeyEvent', 'setBlinkingCursorEnabled', 'updateCursorBlinking',
  'updateLayout', 'updateBaselineOffset', 'calculateImplicitWidthForText',
  'getImplicitWidth', 'padding', 'setTopPadding', 'setLeftPadding',
  'setRightPadding', 'setBottomPadding', 'isImplicitResizeEnabled',
  'setImplicitResizeEnabled', 'removeSelectedText', 'internalSetText',
  'updateDisplayText', 'internalInsert', 'internalDelete',
  'internalDeselect', 'internalUndo', 'internalRedo', 'emitUndoRedoChanged',
  'emitCursorPositionChanged', 'finishChange', 'addCommand', 'separate',
  'separateSelection', 'deleteStartOfWord', 'deleteEndOfWord',
  'deleteEndOfLine', 'parseInputMask', 'isValidInput', 'checkIsValid',
  'maskString', 'clearString', 'stripString', 'findInMask'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickTextInput *QQuickTextInputPrivate::q_func() const':
    takes in Python what 'QQuickTextInput *QQuickTextInputPrivate::q_func()'
    takes.
  - Qt's 'QQuickTextInputPrivate::~QQuickTextInputPrivate()': the destructor:
    Python never removes a C++ QQuickTextInputPrivate.
  - Qt's 'ValidatorState QQuickTextInputPrivate::hasAcceptableInput(const
    QString &text) const': gives the enum
    'QQuickTextInputPrivate::ValidatorState', whose class cannot be named
    here.

  What has no ritual
  ------------------

  2 of the 115 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied; 1 not a gap.

  What to expect
  --------------

  - The C++ QQuickTextInputPrivate is created at the first use, not by
    'QQuickTextInputPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTextInputPrivate.
  - Each name of Qt's QQuickTextInputPrivate that has no cute function yet,
    'hasAcceptableInput', 'startCreatingCursor', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickTextInputPrivate, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class CommandType(CuteNum):
    """
    The enum 'QQuickTextInputPrivate::CommandType' of Qt, with the 7 names Qt
    gives in it.
    """

    Separator = Kee[int](0)
    Insert = Kee[int](1)
    Remove = Kee[int](2)
    Delete = Kee[int](3)
    RemoveSelection = Kee[int](4)
    DeleteSelection = Kee[int](5)
    SetSelection = Kee[int](6)

  class DrawFlags(CuteNum):
    """
    The enum 'QQuickTextInputPrivate::DrawFlags' of Qt, with the 4 names Qt
    gives in it.
    """

    DrawText = Kee[int](1)
    DrawSelections = Kee[int](2)
    DrawCursor = Kee[int](4)
    DrawAll = Kee[int](7)

  class UpdateType(CuteNum):
    """
    The enum 'QQuickTextInputPrivate::UpdateType' of Qt, with the 3 names Qt
    gives in it.
    """

    UpdateNone = Kee[int](0)
    UpdateOnlyPreprocess = Kee[int](1)
    UpdatePaintNode = Kee[int](2)

  #  The classes Qt writes inside QQuickTextInputPrivate, each a class in
  #  here as in C++.

  class Command(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickTextInputPrivate::Command: a plain Python
    object standing in front of one C++ QQuickTextInputPrivate::Command.

    C++ hands a QQuickTextInputPrivate::Command around as a copy, so every
    C++ QQuickTextInputPrivate::Command behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QQuickTextInputPrivate::Command yet. It can be made
    from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickTextInputPrivate::Command::Command(CommandType t, int p,
      QChar c, int ss, int se)': names the enum
      'QQuickTextInputPrivate::CommandType', whose class cannot be named
      here.
    - Qt's 'QQuickTextInputPrivate::Command::~Command()': the destructor:
      Python removes its C++ QQuickTextInputPrivate::Command by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QQuickTextInputPrivate::Command is created at the first use,
      not by 'QQuickTextInputPrivate::Command(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickTextInputPrivate::Command back gives a copy
      the ritual made for Python, in a new cute
      QQuickTextInputPrivate::Command.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickTextInputPrivate::Command'

    #  Qt's '~QQuickTextInputPrivate::Command()'. Naming it makes this a
    #  value class: Python owns every C++ QQuickTextInputPrivate::Command
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN22QQuickTextInputPrivate7CommandD1Ev'

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QQuickTextInputPrivate::Command::Command()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qquicktextinputprivate-command.html#Command
      """
      #  QQuickTextInputPrivate::Command::Command()
      self._noteCreation(
          QQuickTextInputPrivate.Command, lambda: Rituals.call(
              'ritual_ZN22QQuickTextInputPrivate7CommandC1Ev',
          ))

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

  class ExtraData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickTextInputPrivate::ExtraData: a plain Python
    object standing in front of one C++ QQuickTextInputPrivate::ExtraData.

    C++ hands a QQuickTextInputPrivate::ExtraData around as a copy, so every
    C++ QQuickTextInputPrivate::ExtraData behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QQuickTextInputPrivate::ExtraData yet. It can be made
    from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickTextInputPrivate::ExtraData::~ExtraData()': the destructor:
      Python removes its C++ QQuickTextInputPrivate::ExtraData by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QQuickTextInputPrivate::ExtraData is created at the first use,
      not by 'QQuickTextInputPrivate::ExtraData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickTextInputPrivate::ExtraData back gives a copy
      the ritual made for Python, in a new cute
      QQuickTextInputPrivate::ExtraData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickTextInputPrivate::ExtraData'

    #  Qt's '~QQuickTextInputPrivate::ExtraData()'. Naming it makes this a
    #  value class: Python owns every C++ QQuickTextInputPrivate::ExtraData
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN22QQuickTextInputPrivate9ExtraDataD1Ev'

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QQuickTextInputPrivate::ExtraData::ExtraData()', which is called at
      the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qquicktextinputprivate-extradata.html#ExtraData
      """
      #  QQuickTextInputPrivate::ExtraData::ExtraData()
      self._noteCreation(
          QQuickTextInputPrivate.ExtraData, lambda: Rituals.call(
              'ritual_ZN22QQuickTextInputPrivate9ExtraDataC1Ev',
          ))

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

  class MaskInputData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickTextInputPrivate::MaskInputData: a plain
    Python object standing in front of one C++
    QQuickTextInputPrivate::MaskInputData.

    C++ hands a QQuickTextInputPrivate::MaskInputData around as a copy, so
    every C++ QQuickTextInputPrivate::MaskInputData behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QQuickTextInputPrivate::MaskInputData yet. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickTextInputPrivate::MaskInputData::~MaskInputData()': the
      destructor: Python removes its C++
      QQuickTextInputPrivate::MaskInputData by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QQuickTextInputPrivate::MaskInputData is created at the first
      use, not by 'QQuickTextInputPrivate::MaskInputData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickTextInputPrivate::MaskInputData back gives a
      copy the ritual made for Python, in a new cute
      QQuickTextInputPrivate::MaskInputData.
    """

    #  The enums Qt writes inside QQuickTextInputPrivate::MaskInputData, each
    #  a class in here as in C++, and the names Qt has for the combinations
    #  of its flags enums.

    class Casemode(CuteNum):
      """
      The enum 'QQuickTextInputPrivate::MaskInputData::Casemode' of Qt, with
      the 3 names Qt gives in it.
      """

      NoCaseMode = Kee[int](0)
      Upper = Kee[int](1)
      Lower = Kee[int](2)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickTextInputPrivate::MaskInputData'

    #  Qt's '~QQuickTextInputPrivate::MaskInputData()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QQuickTextInputPrivate::MaskInputData behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN22QQuickTextInputPrivate13MaskInputDataD1Ev')

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
  @overload(QQuickTextInput)
  @overload(NoneType)
  def get(t: Optional[QQuickTextInput]) -> Optional[QQuickTextInputPrivate]:
    """
    Calls Qt's 'QQuickTextInputPrivate
    *QQuickTextInputPrivate::get(QQuickTextInput *t)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinputprivate.html#get

    Parameters
    ----------

    t : Optional[QQuickTextInput]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickTextInputPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextInputPrivate *QQuickTextInputPrivate::get(QQuickTextInput
    #      *t)
    address = Rituals.call(
        'ritual_ZN22QQuickTextInputPrivate3getEP15QQuickTextInput',
        CuteMixin._addressOf(t),
    )
    return QQuickTextInputPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTextInputPrivate'

  #  A C++ QQuickTextInputPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickTextInputPrivate'

  #  The functions Qt calls itself that QQuickTextInputPrivate is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'readOnlyChanged': (
          ('_ZN22QQuickTextInputPrivate15readOnlyChangedEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
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

  def effectiveInputMethodHints(self) -> Qt.InputMethodHints:
    """
    Calls Qt's 'Qt::InputMethodHints
    QQuickTextInputPrivate::effectiveInputMethodHints() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html

    Returns
    -------

    Qt.InputMethodHints
      The value standing for the combination Qt gave back.
    """
    #  Qt::InputMethodHints
    #      QQuickTextInputPrivate::effectiveInputMethodHints() const
    return Qt.InputMethodHints(self.uglySide.call(
        'ritual_ZNK22QQuickTextInputPrivate25effectiveInputMethodHintsEv',
    ))

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickTextInputPrivate::accessibleRole()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickTextInputPrivate::accessibleRole() const
    ritual = 'ritual_ZNK22QQuickTextInputPrivate14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QQuickTextInputPrivate14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  def hasPendingTripleClick(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextInputPrivate::hasPendingTripleClick() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#hasPendingTripleClick
    """
    #  bool QQuickTextInputPrivate::hasPendingTripleClick() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTextInputPrivate21hasPendingTripleClickEv',
    )

  def isUndoAvailable(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextInputPrivate::isUndoAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#isUndoAvailable
    """
    #  bool QQuickTextInputPrivate::isUndoAvailable() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTextInputPrivate15isUndoAvailableEv',
    )

  def isRedoAvailable(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextInputPrivate::isRedoAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#isRedoAvailable
    """
    #  bool QQuickTextInputPrivate::isRedoAvailable() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTextInputPrivate15isRedoAvailableEv',
    )

  def allSelected(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextInputPrivate::allSelected() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#allSelected
    """
    #  bool QQuickTextInputPrivate::allSelected() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTextInputPrivate11allSelectedEv',
    )

  def hasSelectedText(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextInputPrivate::hasSelectedText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#hasSelectedText
    """
    #  bool QQuickTextInputPrivate::hasSelectedText() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTextInputPrivate15hasSelectedTextEv',
    )

  def selectedText(self) -> str:
    """
    Calls Qt's 'QString QQuickTextInputPrivate::selectedText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#selectedText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextInputPrivate::selectedText() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTextInputPrivate12selectedTextEv',
    )

  def textBeforeSelection(self) -> str:
    """
    Calls Qt's 'QString QQuickTextInputPrivate::textBeforeSelection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#textBeforeSelection

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextInputPrivate::textBeforeSelection() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTextInputPrivate19textBeforeSelectionEv',
    )

  def textAfterSelection(self) -> str:
    """
    Calls Qt's 'QString QQuickTextInputPrivate::textAfterSelection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#textAfterSelection

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextInputPrivate::textAfterSelection() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTextInputPrivate18textAfterSelectionEv',
    )

  def selectionStart(self) -> int:
    """
    Calls Qt's 'int QQuickTextInputPrivate::selectionStart() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#selectionStart
    """
    #  int QQuickTextInputPrivate::selectionStart() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTextInputPrivate14selectionStartEv',
    )

  def selectionEnd(self) -> int:
    """
    Calls Qt's 'int QQuickTextInputPrivate::selectionEnd() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#selectionEnd
    """
    #  int QQuickTextInputPrivate::selectionEnd() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTextInputPrivate12selectionEndEv',
    )

  def anchorRectangle(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickTextInputPrivate::anchorRectangle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#anchorRectangle

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickTextInputPrivate::anchorRectangle() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickTextInputPrivate15anchorRectangleEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(float, float, QTextLine.CursorPosition)
  def positionAt(
      self,
      x: float,
      y: float,
      position: QTextLine.CursorPosition,
  ) -> int:
    """
    Calls Qt's 'int QQuickTextInputPrivate::positionAt(qreal x, qreal y,
    QTextLine::CursorPosition position) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#positionAt

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    position : QTextLine.CursorPosition
      Passed on as its number.
    """
    #  int QQuickTextInputPrivate::positionAt(qreal x, qreal y,
    #      QTextLine::CursorPosition position) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTextInputPrivate10positionAtEddN9QTextLine14Curs'
        'orPositionE',
        x, y, position.value,
    )

  @overload(QPointF)
  @overload(QPointF, QTextLine.CursorPosition)
  def positionAt(
      self,
      point: QPointF,
      position: QTextLine.CursorPosition = (
          QTextLine.CursorPosition.CursorBetweenCharacters),
  ) -> int:
    """
    Calls Qt's 'int QQuickTextInputPrivate::positionAt(const QPointF &point,
    QTextLine::CursorPosition position) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#positionAt

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    position : QTextLine.CursorPosition
      Passed on as its number. May be left out, as in Qt: it is then
      QTextLine.CursorPosition.CursorBetweenCharacters.
    """
    #  int QQuickTextInputPrivate::positionAt(const QPointF &point,
    #      QTextLine::CursorPosition position) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTextInputPrivate10positionAtERK7QPointFN9QTextLi'
        'ne14CursorPositionE',
        self._valueOf(point, 'QPointF'), position.value,
    )

  def start(self) -> int:
    """
    Calls Qt's 'int QQuickTextInputPrivate::start() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinputprivate.html#start
    """
    #  int QQuickTextInputPrivate::start() const
    return self.uglySide.call('ritual_ZNK22QQuickTextInputPrivate5startEv')

  @overload()
  def end(self) -> int:
    """
    Calls Qt's 'int QQuickTextInputPrivate::end() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinputprivate.html#end
    """
    #  int QQuickTextInputPrivate::end() const
    return self.uglySide.call('ritual_ZNK22QQuickTextInputPrivate3endEv')

  @overload(bool)
  def end(self, mark: bool) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::end(bool mark)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinputprivate.html#end

    Parameters
    ----------

    mark : bool
      Passed on as it is.
    """
    #  void QQuickTextInputPrivate::end(bool mark)
    self.uglySide.call('ritual_ZN22QQuickTextInputPrivate3endEb', mark)

  def realText(self) -> str:
    """
    Calls Qt's 'QString QQuickTextInputPrivate::realText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#realText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextInputPrivate::realText() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTextInputPrivate8realTextEv',
    )

  def cursorMoveStyle(self) -> Qt.CursorMoveStyle:
    """
    Calls Qt's 'Qt::CursorMoveStyle QQuickTextInputPrivate::cursorMoveStyle()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#cursorMoveStyle

    Returns
    -------

    Qt.CursorMoveStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.CursorMoveStyle(number)' gives.
    """
    #  Qt::CursorMoveStyle QQuickTextInputPrivate::cursorMoveStyle() const
    return Qt.CursorMoveStyle(self.uglySide.call(
        'ritual_ZNK22QQuickTextInputPrivate15cursorMoveStyleEv',
    ))

  def inputMask(self) -> str:
    """
    Calls Qt's 'QString QQuickTextInputPrivate::inputMask() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#inputMask

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextInputPrivate::inputMask() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTextInputPrivate9inputMaskEv',
    )

  def composeMode(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextInputPrivate::composeMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#composeMode
    """
    #  bool QQuickTextInputPrivate::composeMode() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTextInputPrivate11composeModeEv',
    )

  def preeditAreaText(self) -> str:
    """
    Calls Qt's 'QString QQuickTextInputPrivate::preeditAreaText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#preeditAreaText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextInputPrivate::preeditAreaText() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTextInputPrivate15preeditAreaTextEv',
    )

  def textDirection(self) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection QQuickTextInputPrivate::textDirection()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#textDirection

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection QQuickTextInputPrivate::textDirection() const
    return Qt.LayoutDirection(self.uglySide.call(
        'ritual_ZNK22QQuickTextInputPrivate13textDirectionEv',
    ))

  def layoutDirection(self) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection QQuickTextInputPrivate::layoutDirection()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#layoutDirection

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection QQuickTextInputPrivate::layoutDirection() const
    return Qt.LayoutDirection(self.uglySide.call(
        'ritual_ZNK22QQuickTextInputPrivate15layoutDirectionEv',
    ))

  @overload(str)
  def calculateImplicitWidthForText(self, text: str) -> float:
    """
    Calls Qt's 'qreal
    QQuickTextInputPrivate::calculateImplicitWidthForText(const QString
    &text) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  qreal QQuickTextInputPrivate::calculateImplicitWidthForText(const
    #      QString &text) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTextInputPrivate29calculateImplicitWidthForTextE'
        'RK7QString',
        text,
    )

  def getImplicitWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextInputPrivate::getImplicitWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#getImplicitWidth
    """
    #  qreal QQuickTextInputPrivate::getImplicitWidth() const
    ritual = 'ritual_ZNK22QQuickTextInputPrivate16getImplicitWidthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QQuickTextInputPrivate16getImplicitWidthEv'
    return self.uglySide.call(ritual)

  def padding(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextInputPrivate::padding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#padding
    """
    #  qreal QQuickTextInputPrivate::padding() const
    return self.uglySide.call('ritual_ZNK22QQuickTextInputPrivate7paddingEv')

  def isImplicitResizeEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextInputPrivate::isImplicitResizeEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html
    """
    #  bool QQuickTextInputPrivate::isImplicitResizeEnabled() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTextInputPrivate23isImplicitResizeEnabledEv',
    )

  @overload(QChar, QChar)
  def isValidInput(self, key: QChar, mask: QChar) -> bool:
    """
    Calls Qt's 'bool QQuickTextInputPrivate::isValidInput(QChar key, QChar
    mask) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#isValidInput

    Parameters
    ----------

    key : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    mask : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool QQuickTextInputPrivate::isValidInput(QChar key, QChar mask) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTextInputPrivate12isValidInputE5QCharS0_',
        self._valueOf(key), self._valueOf(mask),
    )

  @overload(int, str)
  @overload(int, str, bool)
  def maskString(self, pos: int, str: str, clear: bool = False) -> str:
    """
    Calls Qt's 'QString QQuickTextInputPrivate::maskString(uint pos, const
    QString &str, bool clear) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#maskString

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
    #  QString QQuickTextInputPrivate::maskString(uint pos, const QString
    #      &str, bool clear) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTextInputPrivate10maskStringEjRK7QStringb',
        pos, str, clear,
    )

  @overload(int, int)
  def clearString(self, pos: int, len: int) -> str:
    """
    Calls Qt's 'QString QQuickTextInputPrivate::clearString(uint pos, uint
    len) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#clearString

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
    #  QString QQuickTextInputPrivate::clearString(uint pos, uint len) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTextInputPrivate11clearStringEjj', pos, len,
    )

  @overload(str)
  def stripString(self, str: str) -> str:
    """
    Calls Qt's 'QString QQuickTextInputPrivate::stripString(const QString
    &str) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#stripString

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextInputPrivate::stripString(const QString &str) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTextInputPrivate11stripStringERK7QString', str,
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
    Calls Qt's 'int QQuickTextInputPrivate::findInMask(int pos, bool forward,
    bool findSeparator, QChar searchChar) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#findInMask

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
    #  int QQuickTextInputPrivate::findInMask(int pos, bool forward, bool
    #      findSeparator, QChar searchChar) const
    if searchChar is None:
      from ..QtCore import QChar
      searchChar = QChar()
    return self.uglySide.call(
        'ritual_ZNK22QQuickTextInputPrivate10findInMaskEibb5QChar',
        pos, forward, findSeparator, self._valueOf(searchChar),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickTextInput.HAlignment)
  @overload(QQuickTextInput.HAlignment, bool)
  def setHAlign(
      self,
      a0: QQuickTextInput.HAlignment,
      forceAlign: bool = False,
  ) -> bool:
    """
    Calls Qt's 'bool
    QQuickTextInputPrivate::setHAlign(QQuickTextInput::HAlignment a0, bool
    forceAlign)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#setHAlign

    Parameters
    ----------

    a0 : QQuickTextInput.HAlignment
      Passed on as its number.

    forceAlign : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  bool QQuickTextInputPrivate::setHAlign(QQuickTextInput::HAlignment a0,
    #      bool forceAlign)
    return self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate9setHAlignEN15QQuickTextInput10HA'
        'lignmentEb',
        a0.value, forceAlign,
    )

  @overload(bool)
  def setNativeCursorEnabled(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::setNativeCursorEnabled(bool
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#setNativeCursorEnabled

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickTextInputPrivate::setNativeCursorEnabled(bool a0)
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate22setNativeCursorEnabledEb', a0,
    )

  @overload(int, int)
  def setSelection(self, start: int, length: int) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::setSelection(int start, int
    length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#setSelection

    Parameters
    ----------

    start : int
      Passed on as it is.

    length : int
      Passed on as it is.
    """
    #  void QQuickTextInputPrivate::setSelection(int start, int length)
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate12setSelectionEii', start, length,
    )

  @overload(Qt.CursorMoveStyle)
  def setCursorMoveStyle(self, style: Qt.CursorMoveStyle) -> None:
    """
    Calls Qt's 'void
    QQuickTextInputPrivate::setCursorMoveStyle(Qt::CursorMoveStyle style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#setCursorMoveStyle

    Parameters
    ----------

    style : Qt.CursorMoveStyle
      Passed on as its number.
    """
    #  void QQuickTextInputPrivate::setCursorMoveStyle(Qt::CursorMoveStyle
    #      style)
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate18setCursorMoveStyleEN2Qt15Cursor'
        'MoveStyleE',
        style.value,
    )

  @overload(int)
  def setCursorPosition(self, pos: int) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::setCursorPosition(int pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#setCursorPosition

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  void QQuickTextInputPrivate::setCursorPosition(int pos)
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate17setCursorPositionEi', pos,
    )

  @overload(str)
  def setInputMask(self, mask: str) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::setInputMask(const QString
    &mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#setInputMask

    Parameters
    ----------

    mask : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickTextInputPrivate::setInputMask(const QString &mask)
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate12setInputMaskERK7QString', mask,
    )

  @overload(Qt.LayoutDirection)
  def setLayoutDirection(self, direction: Qt.LayoutDirection) -> None:
    """
    Calls Qt's 'void
    QQuickTextInputPrivate::setLayoutDirection(Qt::LayoutDirection
    direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#setLayoutDirection

    Parameters
    ----------

    direction : Qt.LayoutDirection
      Passed on as its number.
    """
    #  void QQuickTextInputPrivate::setLayoutDirection(Qt::LayoutDirection
    #      direction)
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate18setLayoutDirectionEN2Qt15Layout'
        'DirectionE',
        direction.value,
    )

  @overload(bool)
  def setBlinkingCursorEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::setBlinkingCursorEnabled(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickTextInputPrivate::setBlinkingCursorEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate24setBlinkingCursorEnabledEb',
        enable,
    )

  @overload(float)
  @overload(float, bool)
  def setTopPadding(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::setTopPadding(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#setTopPadding

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickTextInputPrivate::setTopPadding(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate13setTopPaddingEdb', value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setLeftPadding(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::setLeftPadding(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#setLeftPadding

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickTextInputPrivate::setLeftPadding(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate14setLeftPaddingEdb', value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setRightPadding(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::setRightPadding(qreal value,
    bool reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#setRightPadding

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickTextInputPrivate::setRightPadding(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate15setRightPaddingEdb',
        value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setBottomPadding(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::setBottomPadding(qreal value,
    bool reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#setBottomPadding

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickTextInputPrivate::setBottomPadding(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate16setBottomPaddingEdb',
        value, reset,
    )

  @overload(bool)
  def setImplicitResizeEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::setImplicitResizeEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickTextInputPrivate::setImplicitResizeEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate24setImplicitResizeEnabledEb',
        enabled,
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
    'QQuickTextInputPrivate::QQuickTextInputPrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#QQuickTextInputPrivate
    """
    #  QQuickTextInputPrivate::QQuickTextInputPrivate()
    self._noteCreation(QQuickTextInputPrivate, lambda: Rituals.call(
        'ritual_ZN22QQuickTextInputPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickTextInput]:
    """
    Calls Qt's 'QQuickTextInput *QQuickTextInputPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinputprivate.html#q_func

    Returns
    -------

    Optional[QQuickTextInput]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextInput *QQuickTextInputPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate6q_funcEv',
    )
    return QQuickTextInput._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinputprivate.html#init
    """
    #  void QQuickTextInputPrivate::init()
    self.uglySide.call('ritual_ZN22QQuickTextInputPrivate4initEv')

  def cancelInput(self) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::cancelInput()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#cancelInput
    """
    #  void QQuickTextInputPrivate::cancelInput()
    self.uglySide.call('ritual_ZN22QQuickTextInputPrivate11cancelInputEv')

  @overload(int)
  @overload(int, int)
  @overload(int, int, int)
  def ensureVisible(
      self,
      position: int,
      preeditCursor: int = 0,
      preeditLength: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::ensureVisible(int position, int
    preeditCursor, int preeditLength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#ensureVisible

    Parameters
    ----------

    position : int
      Passed on as it is.

    preeditCursor : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    preeditLength : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QQuickTextInputPrivate::ensureVisible(int position, int
    #      preeditCursor, int preeditLength)
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate13ensureVisibleEiii',
        position, preeditCursor, preeditLength,
    )

  def updateHorizontalScroll(self) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::updateHorizontalScroll()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#updateHorizontalScroll
    """
    #  void QQuickTextInputPrivate::updateHorizontalScroll()
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate22updateHorizontalScrollEv',
    )

  def updateVerticalScroll(self) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::updateVerticalScroll()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#updateVerticalScroll
    """
    #  void QQuickTextInputPrivate::updateVerticalScroll()
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate20updateVerticalScrollEv',
    )

  def determineHorizontalAlignment(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextInputPrivate::determineHorizontalAlignment()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html
    """
    #  bool QQuickTextInputPrivate::determineHorizontalAlignment()
    return self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate28determineHorizontalAlignmentEv',
    )

  def mirrorChange(self) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::mirrorChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#mirrorChange
    """
    #  void QQuickTextInputPrivate::mirrorChange()
    ritual = 'ritual_ZN22QQuickTextInputPrivate12mirrorChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickTextInputPrivate12mirrorChangeEv'
    self.uglySide.call(ritual)

  @overload(QContextMenuEvent)
  @overload(NoneType)
  def handleContextMenuEvent(
      self,
      event: Optional[QContextMenuEvent],
  ) -> bool:
    """
    Calls Qt's 'bool
    QQuickTextInputPrivate::handleContextMenuEvent(QContextMenuEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#handleContextMenuEvent

    Parameters
    ----------

    event : Optional[QContextMenuEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickTextInputPrivate::handleContextMenuEvent(QContextMenuEvent
    #      *event)
    ritual = (
        'ritual_ZN22QQuickTextInputPrivate22handleContextMenuEventEP17QCont'
        'extMenuEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickTextInputPrivate22handleContextMenuEventEP1'
          '7QContextMenuEvent')
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def sendMouseEventToInputContext(
      self,
      event: Optional[QMouseEvent],
  ) -> bool:
    """
    Calls Qt's 'bool
    QQuickTextInputPrivate::sendMouseEventToInputContext(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickTextInputPrivate::sendMouseEventToInputContext(QMouseEvent
    #      *event)
    return self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate28sendMouseEventToInputContextEP1'
        '1QMouseEvent',
        self._addressOf(event),
    )

  @overload(QFocusEvent)
  @overload(NoneType)
  def handleFocusEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::handleFocusEvent(QFocusEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#handleFocusEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextInputPrivate::handleFocusEvent(QFocusEvent *event)
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate16handleFocusEventEP11QFocusEvent',
        self._addressOf(event),
    )

  @overload(bool)
  def readOnlyChanged(self, isReadOnly: bool) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::readOnlyChanged(bool
    isReadOnly)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#readOnlyChanged

    Parameters
    ----------

    isReadOnly : bool
      Passed on as it is.
    """
    #  void QQuickTextInputPrivate::readOnlyChanged(bool isReadOnly)
    ritual = 'ritual_ZN22QQuickTextInputPrivate15readOnlyChangedEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickTextInputPrivate15readOnlyChangedEb'
    self.uglySide.call(ritual, isReadOnly)

  @overload(QQuickTextInput.EchoMode)
  def echoModeChanged(self, echoMode: QQuickTextInput.EchoMode) -> None:
    """
    Calls Qt's 'void
    QQuickTextInputPrivate::echoModeChanged(QQuickTextInput::EchoMode
    echoMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#echoModeChanged

    Parameters
    ----------

    echoMode : QQuickTextInput.EchoMode
      Passed on as its number.
    """
    #  void QQuickTextInputPrivate::echoModeChanged(QQuickTextInput::EchoMode
    #      echoMode)
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate15echoModeChangedEN15QQuickTextIn'
        'put8EchoModeE',
        echoMode.value,
    )

  @overload(bool)
  def accessibilityActiveChanged(self, active: bool) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::accessibilityActiveChanged(bool
    active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QQuickTextInputPrivate::accessibilityActiveChanged(bool active)
    ritual = (
        'ritual_ZN22QQuickTextInputPrivate26accessibilityActiveChangedEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickTextInputPrivate26accessibilityActiveChange'
          'dEb')
    self.uglySide.call(ritual, active)

  @overload(int)
  def nextMaskBlank(self, pos: int) -> int:
    """
    Calls Qt's 'int QQuickTextInputPrivate::nextMaskBlank(int pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#nextMaskBlank

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  int QQuickTextInputPrivate::nextMaskBlank(int pos)
    return self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate13nextMaskBlankEi', pos,
    )

  @overload(int)
  def prevMaskBlank(self, pos: int) -> int:
    """
    Calls Qt's 'int QQuickTextInputPrivate::prevMaskBlank(int pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#prevMaskBlank

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  int QQuickTextInputPrivate::prevMaskBlank(int pos)
    return self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate13prevMaskBlankEi', pos,
    )

  def clearUndo(self) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::clearUndo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#clearUndo
    """
    #  void QQuickTextInputPrivate::clearUndo()
    self.uglySide.call('ritual_ZN22QQuickTextInputPrivate9clearUndoEv')

  def removeSelection(self) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::removeSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#removeSelection
    """
    #  void QQuickTextInputPrivate::removeSelection()
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate15removeSelectionEv',
    )

  @overload()
  @overload(QClipboard.Mode)
  def copy(self, mode: QClipboard.Mode = QClipboard.Mode.Clipboard) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::copy(QClipboard::Mode mode)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinputprivate.html#copy

    Parameters
    ----------

    mode : QClipboard.Mode
      Passed on as its number. May be left out, as in Qt: it is then
      QClipboard.Mode.Clipboard.
    """
    #  void QQuickTextInputPrivate::copy(QClipboard::Mode mode) const
    self.uglySide.call(
        'ritual_ZNK22QQuickTextInputPrivate4copyEN10QClipboard4ModeE',
        mode.value,
    )

  @overload()
  @overload(QClipboard.Mode)
  def paste(self, mode: QClipboard.Mode = QClipboard.Mode.Clipboard) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::paste(QClipboard::Mode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinputprivate.html#paste

    Parameters
    ----------

    mode : QClipboard.Mode
      Passed on as its number. May be left out, as in Qt: it is then
      QClipboard.Mode.Clipboard.
    """
    #  void QQuickTextInputPrivate::paste(QClipboard::Mode mode)
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate5pasteEN10QClipboard4ModeE',
        mode.value,
    )

  def commitPreedit(self) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::commitPreedit()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#commitPreedit
    """
    #  void QQuickTextInputPrivate::commitPreedit()
    self.uglySide.call('ritual_ZN22QQuickTextInputPrivate13commitPreeditEv')

  def cancelPreedit(self) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::cancelPreedit()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#cancelPreedit
    """
    #  void QQuickTextInputPrivate::cancelPreedit()
    self.uglySide.call('ritual_ZN22QQuickTextInputPrivate13cancelPreeditEv')

  @overload(int)
  @overload(int, bool)
  def moveCursor(self, pos: int, mark: bool = False) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::moveCursor(int pos, bool mark)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#moveCursor

    Parameters
    ----------

    pos : int
      Passed on as it is.

    mark : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickTextInputPrivate::moveCursor(int pos, bool mark)
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate10moveCursorEib', pos, mark,
    )

  @overload(bool, int)
  def cursorForward(self, mark: bool, steps: int) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::cursorForward(bool mark, int
    steps)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#cursorForward

    Parameters
    ----------

    mark : bool
      Passed on as it is.

    steps : int
      Passed on as it is.
    """
    #  void QQuickTextInputPrivate::cursorForward(bool mark, int steps)
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate13cursorForwardEbi', mark, steps,
    )

  @overload(bool)
  def cursorWordForward(self, mark: bool) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::cursorWordForward(bool mark)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#cursorWordForward

    Parameters
    ----------

    mark : bool
      Passed on as it is.
    """
    #  void QQuickTextInputPrivate::cursorWordForward(bool mark)
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate17cursorWordForwardEb', mark,
    )

  @overload(bool)
  def cursorWordBackward(self, mark: bool) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::cursorWordBackward(bool mark)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#cursorWordBackward

    Parameters
    ----------

    mark : bool
      Passed on as it is.
    """
    #  void QQuickTextInputPrivate::cursorWordBackward(bool mark)
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate18cursorWordBackwardEb', mark,
    )

  @overload(bool)
  def home(self, mark: bool) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::home(bool mark)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinputprivate.html#home

    Parameters
    ----------

    mark : bool
      Passed on as it is.
    """
    #  void QQuickTextInputPrivate::home(bool mark)
    self.uglySide.call('ritual_ZN22QQuickTextInputPrivate4homeEb', mark)

  def backspace(self) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::backspace()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#backspace
    """
    #  void QQuickTextInputPrivate::backspace()
    self.uglySide.call('ritual_ZN22QQuickTextInputPrivate9backspaceEv')

  def del_(self) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::del()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinputprivate.html#del
    """
    #  void QQuickTextInputPrivate::del()
    self.uglySide.call('ritual_ZN22QQuickTextInputPrivate3delEv')

  def deselect(self) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::deselect()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#deselect
    """
    #  void QQuickTextInputPrivate::deselect()
    self.uglySide.call('ritual_ZN22QQuickTextInputPrivate8deselectEv')

  def selectAll(self) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::selectAll()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#selectAll
    """
    #  void QQuickTextInputPrivate::selectAll()
    self.uglySide.call('ritual_ZN22QQuickTextInputPrivate9selectAllEv')

  @overload(str)
  def insert(self, a0: str) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::insert(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinputprivate.html#insert

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickTextInputPrivate::insert(const QString &a0)
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate6insertERK7QString', a0,
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinputprivate.html#clear
    """
    #  void QQuickTextInputPrivate::clear()
    self.uglySide.call('ritual_ZN22QQuickTextInputPrivate5clearEv')

  @overload(int)
  def selectWordAtPos(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::selectWordAtPos(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#selectWordAtPos

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickTextInputPrivate::selectWordAtPos(int a0)
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate15selectWordAtPosEi', a0,
    )

  def fixup(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextInputPrivate::fixup()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextinputprivate.html#fixup
    """
    #  bool QQuickTextInputPrivate::fixup()
    return self.uglySide.call('ritual_ZN22QQuickTextInputPrivate5fixupEv')

  @overload(bool)
  def updatePasswordEchoEditing(self, editing: bool) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::updatePasswordEchoEditing(bool
    editing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html

    Parameters
    ----------

    editing : bool
      Passed on as it is.
    """
    #  void QQuickTextInputPrivate::updatePasswordEchoEditing(bool editing)
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate25updatePasswordEchoEditingEb',
        editing,
    )

  def cancelPasswordEchoTimer(self) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::cancelPasswordEchoTimer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html
    """
    #  void QQuickTextInputPrivate::cancelPasswordEchoTimer()
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate23cancelPasswordEchoTimerEv',
    )

  @overload(QInputMethodEvent)
  @overload(NoneType)
  def processInputMethodEvent(
      self,
      event: Optional[QInputMethodEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickTextInputPrivate::processInputMethodEvent(QInputMethodEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html

    Parameters
    ----------

    event : Optional[QInputMethodEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextInputPrivate::processInputMethodEvent(QInputMethodEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate23processInputMethodEventEP17QInp'
        'utMethodEvent',
        self._addressOf(event),
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def processKeyEvent(self, ev: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::processKeyEvent(QKeyEvent *ev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#processKeyEvent

    Parameters
    ----------

    ev : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextInputPrivate::processKeyEvent(QKeyEvent *ev)
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate15processKeyEventEP9QKeyEvent',
        self._addressOf(ev),
    )

  def updateCursorBlinking(self) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::updateCursorBlinking()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#updateCursorBlinking
    """
    #  void QQuickTextInputPrivate::updateCursorBlinking()
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate20updateCursorBlinkingEv',
    )

  def updateLayout(self) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::updateLayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#updateLayout
    """
    #  void QQuickTextInputPrivate::updateLayout()
    self.uglySide.call('ritual_ZN22QQuickTextInputPrivate12updateLayoutEv')

  def updateBaselineOffset(self) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::updateBaselineOffset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#updateBaselineOffset
    """
    #  void QQuickTextInputPrivate::updateBaselineOffset()
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate20updateBaselineOffsetEv',
    )

  def removeSelectedText(self) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::removeSelectedText()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#removeSelectedText
    """
    #  void QQuickTextInputPrivate::removeSelectedText()
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate18removeSelectedTextEv',
    )

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
    Calls Qt's 'void QQuickTextInputPrivate::internalSetText(const QString
    &txt, int pos, bool edited)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#internalSetText

    Parameters
    ----------

    txt : str
      Passed on as it is: a QString is made of it for the call.

    pos : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    edited : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QQuickTextInputPrivate::internalSetText(const QString &txt, int
    #      pos, bool edited)
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate15internalSetTextERK7QStringib',
        txt, pos, edited,
    )

  @overload()
  @overload(bool)
  def updateDisplayText(self, forceUpdate: bool = False) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::updateDisplayText(bool
    forceUpdate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#updateDisplayText

    Parameters
    ----------

    forceUpdate : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickTextInputPrivate::updateDisplayText(bool forceUpdate)
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate17updateDisplayTextEb',
        forceUpdate,
    )

  @overload(str)
  def internalInsert(self, s: str) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::internalInsert(const QString
    &s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#internalInsert

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickTextInputPrivate::internalInsert(const QString &s)
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate14internalInsertERK7QString', s,
    )

  @overload()
  @overload(bool)
  def internalDelete(self, wasBackspace: bool = False) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::internalDelete(bool
    wasBackspace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#internalDelete

    Parameters
    ----------

    wasBackspace : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickTextInputPrivate::internalDelete(bool wasBackspace)
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate14internalDeleteEb', wasBackspace,
    )

  def internalDeselect(self) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::internalDeselect()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#internalDeselect
    """
    #  void QQuickTextInputPrivate::internalDeselect()
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate16internalDeselectEv',
    )

  @overload()
  @overload(int)
  def internalUndo(self, until: int = -1) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::internalUndo(int until)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#internalUndo

    Parameters
    ----------

    until : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void QQuickTextInputPrivate::internalUndo(int until)
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate12internalUndoEi', until,
    )

  def internalRedo(self) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::internalRedo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#internalRedo
    """
    #  void QQuickTextInputPrivate::internalRedo()
    self.uglySide.call('ritual_ZN22QQuickTextInputPrivate12internalRedoEv')

  def emitUndoRedoChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::emitUndoRedoChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#emitUndoRedoChanged
    """
    #  void QQuickTextInputPrivate::emitUndoRedoChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate19emitUndoRedoChangedEv',
    )

  def emitCursorPositionChanged(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextInputPrivate::emitCursorPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html
    """
    #  bool QQuickTextInputPrivate::emitCursorPositionChanged()
    return self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate25emitCursorPositionChangedEv',
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
    Calls Qt's 'bool QQuickTextInputPrivate::finishChange(int
    validateFromState, bool update, bool edited)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#finishChange

    Parameters
    ----------

    validateFromState : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    update : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    edited : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  bool QQuickTextInputPrivate::finishChange(int validateFromState, bool
    #      update, bool edited)
    return self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate12finishChangeEibb',
        validateFromState, update, edited,
    )

  @overload(Command)
  def addCommand(self, cmd: Command) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::addCommand(const Command &cmd)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#addCommand

    Parameters
    ----------

    cmd : Command
      Passed on as a value: Qt reads the C++ QQuickTextInputPrivate::Command,
      which stays Python's own.
    """
    #  void QQuickTextInputPrivate::addCommand(const Command &cmd)
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate10addCommandERKNS_7CommandE',
        self._valueOf(cmd),
    )

  def separate(self) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::separate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#separate
    """
    #  void QQuickTextInputPrivate::separate()
    self.uglySide.call('ritual_ZN22QQuickTextInputPrivate8separateEv')

  def separateSelection(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextInputPrivate::separateSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#separateSelection
    """
    #  bool QQuickTextInputPrivate::separateSelection()
    return self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate17separateSelectionEv',
    )

  def deleteStartOfWord(self) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::deleteStartOfWord()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#deleteStartOfWord
    """
    #  void QQuickTextInputPrivate::deleteStartOfWord()
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate17deleteStartOfWordEv',
    )

  def deleteEndOfWord(self) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::deleteEndOfWord()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#deleteEndOfWord
    """
    #  void QQuickTextInputPrivate::deleteEndOfWord()
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate15deleteEndOfWordEv',
    )

  def deleteEndOfLine(self) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::deleteEndOfLine()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#deleteEndOfLine
    """
    #  void QQuickTextInputPrivate::deleteEndOfLine()
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate15deleteEndOfLineEv',
    )

  @overload(str)
  def parseInputMask(self, maskFields: str) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::parseInputMask(const QString
    &maskFields)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#parseInputMask

    Parameters
    ----------

    maskFields : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickTextInputPrivate::parseInputMask(const QString &maskFields)
    self.uglySide.call(
        'ritual_ZN22QQuickTextInputPrivate14parseInputMaskERK7QString',
        maskFields,
    )

  def checkIsValid(self) -> None:
    """
    Calls Qt's 'void QQuickTextInputPrivate::checkIsValid()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextinputprivate.html#checkIsValid
    """
    #  void QQuickTextInputPrivate::checkIsValid()
    self.uglySide.call('ritual_ZN22QQuickTextInputPrivate12checkIsValidEv')

  @staticmethod
  def hasAcceptableInput(*__, **_) -> Never:
    """
    Qt's 'ValidatorState QQuickTextInputPrivate::hasAcceptableInput(const
    QString &text) const': gives the enum
    'QQuickTextInputPrivate::ValidatorState', whose class cannot be named
    here.
    """
    raise NotImplementedError(
        "'QQuickTextInputPrivate.hasAcceptableInput' has no cute function "
        "yet. Qt's 'ValidatorState "
        "QQuickTextInputPrivate::hasAcceptableInput(const QString &text) "
        "const': gives the enum 'QQuickTextInputPrivate::ValidatorState', "
        "whose class cannot be named here.")

  @staticmethod
  def startCreatingCursor(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextInputPrivate::startCreatingCursor()': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QQuickTextInputPrivate.startCreatingCursor' has no cute function "
        "yet. Qt's 'void QQuickTextInputPrivate::startCreatingCursor()': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")
