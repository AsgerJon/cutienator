"""
QQmlJSCompilePass binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscompilepass_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlJSCompilePass to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtQml import QQmlJS, QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQmlJSRegisterContent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlJSRegisterContent = WAIT['QQmlJSRegisterContent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlJSCompilePass(QV4.Moth.ByteCodeHandler):
  """
  The cute side of Qt's QQmlJSCompilePass: a plain Python object standing in
  front of one C++ QQmlJSCompilePass.

  It is built on the cute 'QV4::Moth::ByteCodeHandler', as Qt's
  QQmlJSCompilePass is built on Qt's QV4::Moth::ByteCodeHandler, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlJSCompilePass that has a ritual and that Python
  can call so far, 146 names in all: 'firstRegisterIndex', 'isArgument',
  'argumentType', 'isQmlScopeObject', 'initialState', 'sourceLocation',
  'nonEmptySourceLocation', 'currentSourceLocation',
  'currentNonEmptySourceLocation', 'currentFunctionSourceLocation',
  'addError', 'addSkip', 'instructionManipulatesContext', 'generate_Add',
  'generate_As', 'generate_BitAnd', 'generate_BitAndConst', 'generate_BitOr',
  'generate_BitOrConst', 'generate_BitXor', 'generate_BitXorConst',
  'generate_CallGlobalLookup', 'generate_CallName',
  'generate_CallPossiblyDirectEval', 'generate_CallProperty',
  'generate_CallPropertyLookup', 'generate_CallQmlContextPropertyLookup',
  'generate_CallValue', 'generate_CallWithReceiver',
  'generate_CallWithSpread', 'generate_CheckException',
  'generate_CloneBlockContext', 'generate_CmpEq', 'generate_CmpEqInt',
  'generate_CmpEqNull', 'generate_CmpGe', 'generate_CmpGt', 'generate_CmpIn',
  'generate_CmpInstanceOf', 'generate_CmpLe', 'generate_CmpLt',
  'generate_CmpNe', 'generate_CmpNeInt', 'generate_CmpNeNull',
  'generate_CmpStrictEqual', 'generate_CmpStrictNotEqual',
  'generate_Construct', 'generate_ConstructWithSpread',
  'generate_ConvertThisToObject', 'generate_CreateCallContext',
  'generate_CreateClass', 'generate_CreateMappedArgumentsObject',
  'generate_CreateRestParameter', 'generate_CreateUnmappedArgumentsObject',
  'generate_DeadTemporalZoneCheck', 'generate_Debug', 'generate_DeclareVar',
  'generate_Decrement', 'generate_DefineArray',
  'generate_DefineObjectLiteral', 'generate_DeleteName',
  'generate_DeleteProperty', 'generate_DestructureRestElement',
  'generate_Div', 'generate_Exp', 'generate_GetException',
  'generate_GetIterator', 'generate_GetLookup', 'generate_GetOptionalLookup',
  'generate_GetTemplateObject', 'generate_Increment',
  'generate_InitializeBlockDeadTemporalZone', 'generate_IteratorClose',
  'generate_IteratorNext', 'generate_IteratorNextForYieldStar',
  'generate_Jump', 'generate_JumpFalse', 'generate_JumpNoException',
  'generate_JumpNotUndefined', 'generate_JumpTrue', 'generate_LoadClosure',
  'generate_LoadConst', 'generate_LoadElement', 'generate_LoadFalse',
  'generate_LoadGlobalLookup', 'generate_LoadImport', 'generate_LoadInt',
  'generate_LoadLocal', 'generate_LoadName', 'generate_LoadNull',
  'generate_LoadOptionalProperty', 'generate_LoadProperty',
  'generate_LoadQmlContextPropertyLookup', 'generate_LoadReg',
  'generate_LoadRuntimeString', 'generate_LoadScopedLocal',
  'generate_LoadSuperConstructor', 'generate_LoadSuperProperty',
  'generate_LoadTrue', 'generate_LoadUndefined', 'generate_LoadZero',
  'generate_Mod', 'generate_MoveConst', 'generate_MoveReg',
  'generate_MoveRegExp', 'generate_Mul', 'generate_PopContext',
  'generate_PopScriptContext', 'generate_PushBlockContext',
  'generate_PushCatchContext', 'generate_PushScriptContext',
  'generate_PushWithContext', 'generate_Resume', 'generate_Ret',
  'generate_SetException', 'generate_SetLookup', 'generate_SetUnwindHandler',
  'generate_Shl', 'generate_ShlConst', 'generate_Shr', 'generate_ShrConst',
  'generate_StoreElement', 'generate_StoreLocal', 'generate_StoreNameSloppy',
  'generate_StoreNameStrict', 'generate_StoreProperty', 'generate_StoreReg',
  'generate_StoreScopedLocal', 'generate_StoreSuperProperty', 'generate_Sub',
  'generate_TailCall', 'generate_ThrowException',
  'generate_ThrowOnNullOrUndefined', 'generate_ToObject',
  'generate_TypeofName', 'generate_TypeofValue', 'generate_UCompl',
  'generate_UMinus', 'generate_UNot', 'generate_UPlus', 'generate_UShr',
  'generate_UShrConst', 'generate_UnwindDispatch', 'generate_UnwindToLabel',
  'generate_Yield', 'generate_YieldStar'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'State QQmlJSCompilePass::nextStateFromAnnotations(const State
    &oldState, const InstructionAnnotations &annotations)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  6 of the 155 functions Qt declares: 4 forbidden; 1 the class is abstract,
  so C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open; 1 the compiler refuses its ritual as it would be
  written here.

  What to expect
  --------------

  - The C++ QQmlJSCompilePass is created at the first use, not by
    'QQmlJSCompilePass(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJSCompilePass.
  - Each name of Qt's QQmlJSCompilePass that has no cute function yet,
    '__init__', 'nextStateFromAnnotations', 'sourceLocationEntry', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQmlJSCompilePass, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class RegisterShortcuts(CuteNum):
    """
    The enum 'QQmlJSCompilePass::RegisterShortcuts' of Qt, with the 8 names
    Qt gives in it.
    """

    InvalidRegister = Kee[int](-1)
    CurrentFunction = Kee[int](0)
    Context = Kee[int](1)
    Accumulator = Kee[int](2)
    This = Kee[int](3)
    NewTarget = Kee[int](4)
    Argc = Kee[int](5)
    FirstArgument = Kee[int](6)

  #  The classes Qt writes inside QQmlJSCompilePass, each a class in here as
  #  in C++.

  class BasicBlock(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlJSCompilePass::BasicBlock: a plain Python
    object standing in front of one C++ QQmlJSCompilePass::BasicBlock.

    C++ hands a QQmlJSCompilePass::BasicBlock around as a copy, so every C++
    QQmlJSCompilePass::BasicBlock behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QQmlJSCompilePass::BasicBlock yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlJSCompilePass::BasicBlock::~BasicBlock()': the destructor:
      Python removes its C++ QQmlJSCompilePass::BasicBlock by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QQmlJSCompilePass::BasicBlock is created at the first use, not
      by 'QQmlJSCompilePass::BasicBlock(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlJSCompilePass::BasicBlock back gives a copy the
      ritual made for Python, in a new cute QQmlJSCompilePass::BasicBlock.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlJSCompilePass::BasicBlock'

    #  Qt's '~QQmlJSCompilePass::BasicBlock()'. Naming it makes this a value
    #  class: Python owns every C++ QQmlJSCompilePass::BasicBlock behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN17QQmlJSCompilePass10BasicBlockD1Ev'

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

  class BlocksAndAnnotations(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlJSCompilePass::BlocksAndAnnotations: a plain
    Python object standing in front of one C++
    QQmlJSCompilePass::BlocksAndAnnotations.

    C++ hands a QQmlJSCompilePass::BlocksAndAnnotations around as a copy, so
    every C++ QQmlJSCompilePass::BlocksAndAnnotations behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QQmlJSCompilePass::BlocksAndAnnotations yet. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QQmlJSCompilePass::BlocksAndAnnotations::~BlocksAndAnnotations()': the
      destructor: Python removes its C++
      QQmlJSCompilePass::BlocksAndAnnotations by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QQmlJSCompilePass::BlocksAndAnnotations is created at the first
      use, not by 'QQmlJSCompilePass::BlocksAndAnnotations(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlJSCompilePass::BlocksAndAnnotations back gives
      a copy the ritual made for Python, in a new cute
      QQmlJSCompilePass::BlocksAndAnnotations.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlJSCompilePass::BlocksAndAnnotations'

    #  Qt's '~QQmlJSCompilePass::BlocksAndAnnotations()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QQmlJSCompilePass::BlocksAndAnnotations behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN17QQmlJSCompilePass20BlocksAndAnnotationsD1Ev')

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

  class Function(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlJSCompilePass::Function: a plain Python object
    standing in front of one C++ QQmlJSCompilePass::Function.

    C++ hands a QQmlJSCompilePass::Function around as a copy, so every C++
    QQmlJSCompilePass::Function behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QQmlJSCompilePass::Function yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlJSCompilePass::Function::~Function()': the destructor: Python
      removes its C++ QQmlJSCompilePass::Function by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QQmlJSCompilePass::Function is created at the first use, not by
      'QQmlJSCompilePass::Function(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlJSCompilePass::Function back gives a copy the
      ritual made for Python, in a new cute QQmlJSCompilePass::Function.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlJSCompilePass::Function'

    #  Qt's '~QQmlJSCompilePass::Function()'. Naming it makes this a value
    #  class: Python owns every C++ QQmlJSCompilePass::Function behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN17QQmlJSCompilePass8FunctionD1Ev'

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

  class InstructionAnnotation(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlJSCompilePass::InstructionAnnotation: a plain
    Python object standing in front of one C++
    QQmlJSCompilePass::InstructionAnnotation.

    C++ hands a QQmlJSCompilePass::InstructionAnnotation around as a copy, so
    every C++ QQmlJSCompilePass::InstructionAnnotation behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QQmlJSCompilePass::InstructionAnnotation yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QQmlJSCompilePass::InstructionAnnotation::~InstructionAnnotation()':
      the destructor: Python removes its C++
      QQmlJSCompilePass::InstructionAnnotation by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QQmlJSCompilePass::InstructionAnnotation is created at the
      first use, not by 'QQmlJSCompilePass::InstructionAnnotation(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlJSCompilePass::InstructionAnnotation back gives
      a copy the ritual made for Python, in a new cute
      QQmlJSCompilePass::InstructionAnnotation.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlJSCompilePass::InstructionAnnotation'

    #  Qt's '~QQmlJSCompilePass::InstructionAnnotation()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QQmlJSCompilePass::InstructionAnnotation behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN17QQmlJSCompilePass21InstructionAnnotationD1Ev')

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

  class ObjectOrArrayDefinition(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlJSCompilePass::ObjectOrArrayDefinition: a plain
    Python object standing in front of one C++
    QQmlJSCompilePass::ObjectOrArrayDefinition.

    C++ hands a QQmlJSCompilePass::ObjectOrArrayDefinition around as a copy,
    so every C++ QQmlJSCompilePass::ObjectOrArrayDefinition behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QQmlJSCompilePass::ObjectOrArrayDefinition yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QQmlJSCompilePass::ObjectOrArrayDefinition::~ObjectOrArrayDefinition(
      )': the destructor: Python removes its C++
      QQmlJSCompilePass::ObjectOrArrayDefinition by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QQmlJSCompilePass::ObjectOrArrayDefinition is created at the
      first use, not by 'QQmlJSCompilePass::ObjectOrArrayDefinition(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlJSCompilePass::ObjectOrArrayDefinition back
      gives a copy the ritual made for Python, in a new cute
      QQmlJSCompilePass::ObjectOrArrayDefinition.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlJSCompilePass::ObjectOrArrayDefinition'

    #  Qt's '~QQmlJSCompilePass::ObjectOrArrayDefinition()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QQmlJSCompilePass::ObjectOrArrayDefinition behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN17QQmlJSCompilePass23ObjectOrArrayDefinitionD1Ev')

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

  class State(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlJSCompilePass::State: a plain Python object
    standing in front of one C++ QQmlJSCompilePass::State.

    C++ hands a QQmlJSCompilePass::State around as a copy, so every C++
    QQmlJSCompilePass::State behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QQmlJSCompilePass::State that has a ritual and
    that Python can call so far, 24 names in all: 'accumulatorIn',
    'accumulatorOut', 'setRegister', 'clearChangedRegister',
    'changedRegisterIndex', 'changedRegister', 'addReadRegister',
    'addReadAccumulator', 'readRegister', 'canMoveReadRegister',
    'isRegisterAffectedBySideEffects', 'readAccumulator', 'readsRegister',
    'hasInternalSideEffects', 'hasExternalSideEffects', 'resetSideEffects',
    'applyExternalSideEffects', 'setHasInternalSideEffects',
    'setHasExternalSideEffects', 'isRename', 'setIsRename', 'isShadowable',
    'setIsShadowable', 'renameSourceRegisterIndex'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'VirtualRegisters QQmlJSCompilePass::State::takeReadRegisters()
      const': gives a type Python has no way to take yet.
    - Qt's 'void QQmlJSCompilePass::State::setReadRegisters(VirtualRegisters
      readReagisters)': takes a type Python has no way to hand over yet.
    - Qt's 'void QQmlJSCompilePass::State::applyAnnotation(const
      InstructionAnnotation &annotation)': names
      'QQmlJSCompilePass::InstructionAnnotation', which stands beside this
      class inside 'QQmlJSCompilePass' and cannot be named from here.
    - Qt's 'QQmlJSCompilePass::State::~State()': the destructor: Python
      removes its C++ QQmlJSCompilePass::State by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QQmlJSCompilePass::State is created at the first use, not by
      'QQmlJSCompilePass::State(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlJSCompilePass::State back gives a copy the
      ritual made for Python, in a new cute QQmlJSCompilePass::State.
    - Each name of Qt's QQmlJSCompilePass::State that has no cute function
      yet, 'applyAnnotation', 'setReadRegisters', 'takeReadRegisters', holds
      a function that raises 'NotImplementedError', and its docstring says
      why.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QQmlJSRegisterContent = WAIT['QQmlJSRegisterContent']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlJSCompilePass::State'

    #  Qt's '~QQmlJSCompilePass::State()'. Naming it makes this a value
    #  class: Python owns every C++ QQmlJSCompilePass::State behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN17QQmlJSCompilePass5StateD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def accumulatorIn(self) -> QQmlJSRegisterContent:
      """
      Calls Qt's 'QQmlJSRegisterContent
      QQmlJSCompilePass::State::accumulatorIn() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljscompilepass-state.html#accumulatorIn

      Returns
      -------

      QQmlJSRegisterContent
        A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
        owns it.
      """
      #  QQmlJSRegisterContent QQmlJSCompilePass::State::accumulatorIn()
      #      const
      address = self.uglySide.call(
          'ritual_ZNK17QQmlJSCompilePass5State13accumulatorInEv',
      )
      from . import QQmlJSRegisterContent
      return QQmlJSRegisterContent._cuteOwning(address)

    def accumulatorOut(self) -> QQmlJSRegisterContent:
      """
      Calls Qt's 'QQmlJSRegisterContent
      QQmlJSCompilePass::State::accumulatorOut() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljscompilepass-state.html#accumulatorOut

      Returns
      -------

      QQmlJSRegisterContent
        A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
        owns it.
      """
      #  QQmlJSRegisterContent QQmlJSCompilePass::State::accumulatorOut()
      #      const
      address = self.uglySide.call(
          'ritual_ZNK17QQmlJSCompilePass5State14accumulatorOutEv',
      )
      from . import QQmlJSRegisterContent
      return QQmlJSRegisterContent._cuteOwning(address)

    def changedRegisterIndex(self) -> int:
      """
      Calls Qt's 'int QQmlJSCompilePass::State::changedRegisterIndex()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljscompilepass-state.html
      """
      #  int QQmlJSCompilePass::State::changedRegisterIndex() const
      return self.uglySide.call(
          'ritual_ZNK17QQmlJSCompilePass5State20changedRegisterIndexEv',
      )

    def changedRegister(self) -> QQmlJSRegisterContent:
      """
      Calls Qt's 'QQmlJSRegisterContent
      QQmlJSCompilePass::State::changedRegister() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljscompilepass-state.html#changedRegister

      Returns
      -------

      QQmlJSRegisterContent
        A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
        owns it.
      """
      #  QQmlJSRegisterContent QQmlJSCompilePass::State::changedRegister()
      #      const
      address = self.uglySide.call(
          'ritual_ZNK17QQmlJSCompilePass5State15changedRegisterEv',
      )
      from . import QQmlJSRegisterContent
      return QQmlJSRegisterContent._cuteOwning(address)

    @overload(int)
    def readRegister(self, registerIndex: int) -> QQmlJSRegisterContent:
      """
      Calls Qt's 'QQmlJSRegisterContent
      QQmlJSCompilePass::State::readRegister(int registerIndex) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljscompilepass-state.html#readRegister

      Parameters
      ----------

      registerIndex : int
        Passed on as it is.

      Returns
      -------

      QQmlJSRegisterContent
        A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
        owns it.
      """
      #  QQmlJSRegisterContent QQmlJSCompilePass::State::readRegister(int
      #      registerIndex) const
      address = self.uglySide.call(
          'ritual_ZNK17QQmlJSCompilePass5State12readRegisterEi',
          registerIndex,
      )
      from . import QQmlJSRegisterContent
      return QQmlJSRegisterContent._cuteOwning(address)

    @overload(int)
    def canMoveReadRegister(self, registerIndex: int) -> bool:
      """
      Calls Qt's 'bool QQmlJSCompilePass::State::canMoveReadRegister(int
      registerIndex) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljscompilepass-state.html#canMoveReadRegister

      Parameters
      ----------

      registerIndex : int
        Passed on as it is.
      """
      #  bool QQmlJSCompilePass::State::canMoveReadRegister(int
      #      registerIndex) const
      return self.uglySide.call(
          'ritual_ZNK17QQmlJSCompilePass5State19canMoveReadRegisterEi',
          registerIndex,
      )

    @overload(int)
    def isRegisterAffectedBySideEffects(self, registerIndex: int) -> bool:
      """
      Calls Qt's 'bool
      QQmlJSCompilePass::State::isRegisterAffectedBySideEffects(int
      registerIndex) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljscompilepass-state.html

      Parameters
      ----------

      registerIndex : int
        Passed on as it is.
      """
      #  bool QQmlJSCompilePass::State::isRegisterAffectedBySideEffects(int
      #      registerIndex) const
      return self.uglySide.call(
          'ritual_ZNK17QQmlJSCompilePass5State31isRegisterAffectedBySideEff'
          'ectsEi',
          registerIndex,
      )

    def readAccumulator(self) -> QQmlJSRegisterContent:
      """
      Calls Qt's 'QQmlJSRegisterContent
      QQmlJSCompilePass::State::readAccumulator() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljscompilepass-state.html#readAccumulator

      Returns
      -------

      QQmlJSRegisterContent
        A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
        owns it.
      """
      #  QQmlJSRegisterContent QQmlJSCompilePass::State::readAccumulator()
      #      const
      address = self.uglySide.call(
          'ritual_ZNK17QQmlJSCompilePass5State15readAccumulatorEv',
      )
      from . import QQmlJSRegisterContent
      return QQmlJSRegisterContent._cuteOwning(address)

    @overload(int)
    def readsRegister(self, registerIndex: int) -> bool:
      """
      Calls Qt's 'bool QQmlJSCompilePass::State::readsRegister(int
      registerIndex) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljscompilepass-state.html#readsRegister

      Parameters
      ----------

      registerIndex : int
        Passed on as it is.
      """
      #  bool QQmlJSCompilePass::State::readsRegister(int registerIndex)
      #      const
      return self.uglySide.call(
          'ritual_ZNK17QQmlJSCompilePass5State13readsRegisterEi',
          registerIndex,
      )

    def hasInternalSideEffects(self) -> bool:
      """
      Calls Qt's 'bool QQmlJSCompilePass::State::hasInternalSideEffects()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljscompilepass-state.html
      """
      #  bool QQmlJSCompilePass::State::hasInternalSideEffects() const
      return self.uglySide.call(
          'ritual_ZNK17QQmlJSCompilePass5State22hasInternalSideEffectsEv',
      )

    def hasExternalSideEffects(self) -> bool:
      """
      Calls Qt's 'bool QQmlJSCompilePass::State::hasExternalSideEffects()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljscompilepass-state.html
      """
      #  bool QQmlJSCompilePass::State::hasExternalSideEffects() const
      return self.uglySide.call(
          'ritual_ZNK17QQmlJSCompilePass5State22hasExternalSideEffectsEv',
      )

    def isRename(self) -> bool:
      """
      Calls Qt's 'bool QQmlJSCompilePass::State::isRename() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljscompilepass-state.html#isRename
      """
      #  bool QQmlJSCompilePass::State::isRename() const
      return self.uglySide.call(
          'ritual_ZNK17QQmlJSCompilePass5State8isRenameEv',
      )

    def isShadowable(self) -> bool:
      """
      Calls Qt's 'bool QQmlJSCompilePass::State::isShadowable() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljscompilepass-state.html#isShadowable
      """
      #  bool QQmlJSCompilePass::State::isShadowable() const
      return self.uglySide.call(
          'ritual_ZNK17QQmlJSCompilePass5State12isShadowableEv',
      )

    def renameSourceRegisterIndex(self) -> int:
      """
      Calls Qt's 'int QQmlJSCompilePass::State::renameSourceRegisterIndex()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljscompilepass-state.html
      """
      #  int QQmlJSCompilePass::State::renameSourceRegisterIndex() const
      return self.uglySide.call(
          'ritual_ZNK17QQmlJSCompilePass5State25renameSourceRegisterIndexEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(int, QQmlJSRegisterContent)
    def setRegister(
        self,
        registerIndex: int,
        content: QQmlJSRegisterContent,
    ) -> None:
      """
      Calls Qt's 'void QQmlJSCompilePass::State::setRegister(int
      registerIndex, QQmlJSRegisterContent content)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljscompilepass-state.html#setRegister

      Parameters
      ----------

      registerIndex : int
        Passed on as it is.

      content : QQmlJSRegisterContent
        Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
        stays Python's own.
      """
      #  void QQmlJSCompilePass::State::setRegister(int registerIndex,
      #      QQmlJSRegisterContent content)
      self.uglySide.call(
          'ritual_ZN17QQmlJSCompilePass5State11setRegisterEi21QQmlJSRegiste'
          'rContent',
          registerIndex, self._valueOf(content),
      )

    def setHasInternalSideEffects(self) -> None:
      """
      Calls Qt's 'void
      QQmlJSCompilePass::State::setHasInternalSideEffects()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljscompilepass-state.html
      """
      #  void QQmlJSCompilePass::State::setHasInternalSideEffects()
      self.uglySide.call(
          'ritual_ZN17QQmlJSCompilePass5State25setHasInternalSideEffectsEv',
      )

    def setHasExternalSideEffects(self) -> None:
      """
      Calls Qt's 'void
      QQmlJSCompilePass::State::setHasExternalSideEffects()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljscompilepass-state.html
      """
      #  void QQmlJSCompilePass::State::setHasExternalSideEffects()
      self.uglySide.call(
          'ritual_ZN17QQmlJSCompilePass5State25setHasExternalSideEffectsEv',
      )

    @overload(bool)
    def setIsRename(self, isRename: bool) -> None:
      """
      Calls Qt's 'void QQmlJSCompilePass::State::setIsRename(bool isRename)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljscompilepass-state.html#setIsRename

      Parameters
      ----------

      isRename : bool
        Passed on as it is.
      """
      #  void QQmlJSCompilePass::State::setIsRename(bool isRename)
      self.uglySide.call(
          'ritual_ZN17QQmlJSCompilePass5State11setIsRenameEb', isRename,
      )

    @overload(bool)
    def setIsShadowable(self, isShadowable: bool) -> None:
      """
      Calls Qt's 'void QQmlJSCompilePass::State::setIsShadowable(bool
      isShadowable)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljscompilepass-state.html#setIsShadowable

      Parameters
      ----------

      isShadowable : bool
        Passed on as it is.
      """
      #  void QQmlJSCompilePass::State::setIsShadowable(bool isShadowable)
      self.uglySide.call(
          'ritual_ZN17QQmlJSCompilePass5State15setIsShadowableEb',
          isShadowable,
      )

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

    def clearChangedRegister(self) -> None:
      """
      Calls Qt's 'void QQmlJSCompilePass::State::clearChangedRegister()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljscompilepass-state.html
      """
      #  void QQmlJSCompilePass::State::clearChangedRegister()
      self.uglySide.call(
          'ritual_ZN17QQmlJSCompilePass5State20clearChangedRegisterEv',
      )

    @overload(int, QQmlJSRegisterContent)
    def addReadRegister(
        self,
        registerIndex: int,
        reg: QQmlJSRegisterContent,
    ) -> None:
      """
      Calls Qt's 'void QQmlJSCompilePass::State::addReadRegister(int
      registerIndex, QQmlJSRegisterContent reg)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljscompilepass-state.html#addReadRegister

      Parameters
      ----------

      registerIndex : int
        Passed on as it is.

      reg : QQmlJSRegisterContent
        Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
        stays Python's own.
      """
      #  void QQmlJSCompilePass::State::addReadRegister(int registerIndex,
      #      QQmlJSRegisterContent reg)
      self.uglySide.call(
          'ritual_ZN17QQmlJSCompilePass5State15addReadRegisterEi21QQmlJSReg'
          'isterContent',
          registerIndex, self._valueOf(reg),
      )

    @overload(QQmlJSRegisterContent)
    def addReadAccumulator(self, reg: QQmlJSRegisterContent) -> None:
      """
      Calls Qt's 'void
      QQmlJSCompilePass::State::addReadAccumulator(QQmlJSRegisterContent
      reg)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljscompilepass-state.html#addReadAccumulator

      Parameters
      ----------

      reg : QQmlJSRegisterContent
        Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
        stays Python's own.
      """
      #  void QQmlJSCompilePass::State::addReadAccumulator(
      #      QQmlJSRegisterContent reg)
      self.uglySide.call(
          'ritual_ZN17QQmlJSCompilePass5State18addReadAccumulatorE21QQmlJSR'
          'egisterContent',
          self._valueOf(reg),
      )

    def resetSideEffects(self) -> None:
      """
      Calls Qt's 'void QQmlJSCompilePass::State::resetSideEffects()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljscompilepass-state.html#resetSideEffects
      """
      #  void QQmlJSCompilePass::State::resetSideEffects()
      self.uglySide.call(
          'ritual_ZN17QQmlJSCompilePass5State16resetSideEffectsEv',
      )

    @overload(bool)
    def applyExternalSideEffects(self, hasExternalSideEffects: bool) -> None:
      """
      Calls Qt's 'void
      QQmlJSCompilePass::State::applyExternalSideEffects(bool
      hasExternalSideEffects)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljscompilepass-state.html

      Parameters
      ----------

      hasExternalSideEffects : bool
        Passed on as it is.
      """
      #  void QQmlJSCompilePass::State::applyExternalSideEffects(bool
      #      hasExternalSideEffects)
      self.uglySide.call(
          'ritual_ZN17QQmlJSCompilePass5State24applyExternalSideEffectsEb',
          hasExternalSideEffects,
      )

    @staticmethod
    def applyAnnotation(*__, **_) -> Never:
      """
      Qt's 'void QQmlJSCompilePass::State::applyAnnotation(const
      InstructionAnnotation &annotation)': names
      'QQmlJSCompilePass::InstructionAnnotation', which stands beside this
      class inside 'QQmlJSCompilePass' and cannot be named from here.
      """
      raise NotImplementedError(
          "'QQmlJSCompilePass.State.applyAnnotation' has no cute function "
          "yet. Qt's 'void QQmlJSCompilePass::State::applyAnnotation(const "
          "InstructionAnnotation &annotation)': names "
          "'QQmlJSCompilePass::InstructionAnnotation', which stands beside "
          "this class inside 'QQmlJSCompilePass' and cannot be named from "
          "here.")

    @staticmethod
    def setReadRegisters(*__, **_) -> Never:
      """
      Qt's 'void QQmlJSCompilePass::State::setReadRegisters(VirtualRegisters
      readReagisters)': takes a type Python has no way to hand over yet.
      """
      raise NotImplementedError(
          "'QQmlJSCompilePass.State.setReadRegisters' has no cute function "
          "yet. Qt's 'void "
          "QQmlJSCompilePass::State::setReadRegisters(VirtualRegisters "
          "readReagisters)': takes a type Python has no way to hand over "
          "yet.")

    @staticmethod
    def takeReadRegisters(*__, **_) -> Never:
      """
      Qt's 'VirtualRegisters QQmlJSCompilePass::State::takeReadRegisters()
      const': gives a type Python has no way to take yet.
      """
      raise NotImplementedError(
          "'QQmlJSCompilePass.State.takeReadRegisters' has no cute function "
          "yet. Qt's 'VirtualRegisters "
          "QQmlJSCompilePass::State::takeReadRegisters() const': gives a "
          "type Python has no way to take yet.")

  class VirtualRegister(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlJSCompilePass::VirtualRegister: a plain Python
    object standing in front of one C++ QQmlJSCompilePass::VirtualRegister.

    C++ hands a QQmlJSCompilePass::VirtualRegister around as a copy, so every
    C++ QQmlJSCompilePass::VirtualRegister behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QQmlJSCompilePass::VirtualRegister that has a
    ritual and that Python can call so far, 1 name in all: '__eq__'. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlJSCompilePass::VirtualRegister::~VirtualRegister()': the
      destructor: Python removes its C++ QQmlJSCompilePass::VirtualRegister
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QQmlJSCompilePass::VirtualRegister is created at the first use,
      not by 'QQmlJSCompilePass::VirtualRegister(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlJSCompilePass::VirtualRegister back gives a
      copy the ritual made for Python, in a new cute
      QQmlJSCompilePass::VirtualRegister.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlJSCompilePass::VirtualRegister'

    #  Qt's '~QQmlJSCompilePass::VirtualRegister()'. Naming it makes this a
    #  value class: Python owns every C++ QQmlJSCompilePass::VirtualRegister
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN17QQmlJSCompilePass15VirtualRegisterD1Ev'

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

    @overload(THIS)
    def __eq__(self, b: QQmlJSCompilePass.VirtualRegister) -> bool:
      """
      Calls Qt's 'bool operator==(const VirtualRegister &a, const
      VirtualRegister &b)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljscompilepass-virtualregister.html

      Parameters
      ----------

      b : QQmlJSCompilePass.VirtualRegister
        Passed on as a value: Qt reads the C++
        QQmlJSCompilePass::VirtualRegister, which stays Python's own.
      """
      #  bool operator==(const VirtualRegister &a, const VirtualRegister &b)
      return Rituals.call(
          'ritual_ZeqRKN17QQmlJSCompilePass15VirtualRegisterES2_',
          CuteMixin._valueOf(self), CuteMixin._valueOf(b),
      )

    @overload.fallback
    def __eq__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

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
  @overload(QV4.Moth.Instr.Type)
  def instructionManipulatesContext(type: QV4.Moth.Instr.Type) -> bool:
    """
    Calls Qt's 'bool
    QQmlJSCompilePass::instructionManipulatesContext(QV4::Moth::Instr::Type
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html

    Parameters
    ----------

    type : QV4.Moth.Instr.Type
      Passed on as its number.
    """
    #  bool QQmlJSCompilePass::instructionManipulatesContext(QV4::Moth::
    #      Instr::Type type)
    return Rituals.call(
        'ritual_ZN17QQmlJSCompilePass29instructionManipulatesContextEN3QV44'
        'Moth5Instr4TypeE',
        type.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJSCompilePass'

  #  A C++ QQmlJSCompilePass Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJSCompilePass'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def firstRegisterIndex(self) -> int:
    """
    Calls Qt's 'int QQmlJSCompilePass::firstRegisterIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#firstRegisterIndex
    """
    #  int QQmlJSCompilePass::firstRegisterIndex() const
    return self.uglySide.call(
        'ritual_ZNK17QQmlJSCompilePass18firstRegisterIndexEv',
    )

  @overload(int)
  def isArgument(self, registerIndex: int) -> bool:
    """
    Calls Qt's 'bool QQmlJSCompilePass::isArgument(int registerIndex) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljscompilepass.html#isArgument

    Parameters
    ----------

    registerIndex : int
      Passed on as it is.
    """
    #  bool QQmlJSCompilePass::isArgument(int registerIndex) const
    return self.uglySide.call(
        'ritual_ZNK17QQmlJSCompilePass10isArgumentEi', registerIndex,
    )

  @overload(int)
  def argumentType(self, registerIndex: int) -> QQmlJSRegisterContent:
    """
    Calls Qt's 'QQmlJSRegisterContent QQmlJSCompilePass::argumentType(int
    registerIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#argumentType

    Parameters
    ----------

    registerIndex : int
      Passed on as it is.

    Returns
    -------

    QQmlJSRegisterContent
      A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJSRegisterContent QQmlJSCompilePass::argumentType(int
    #      registerIndex) const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlJSCompilePass12argumentTypeEi', registerIndex,
    )
    from . import QQmlJSRegisterContent
    return QQmlJSRegisterContent._cuteOwning(address)

  @overload(int)
  def sourceLocation(self, instructionOffset: int) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'QQmlJS::SourceLocation QQmlJSCompilePass::sourceLocation(int
    instructionOffset) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#sourceLocation

    Parameters
    ----------

    instructionOffset : int
      Passed on as it is.

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJS::SourceLocation QQmlJSCompilePass::sourceLocation(int
    #      instructionOffset) const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlJSCompilePass14sourceLocationEi', instructionOffset,
    )
    return QQmlJS.SourceLocation._cuteOwning(address)

  @overload(int)
  def nonEmptySourceLocation(
      self,
      instructionOffset: int,
  ) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'QQmlJS::SourceLocation
    QQmlJSCompilePass::nonEmptySourceLocation(int instructionOffset) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#nonEmptySourceLocation

    Parameters
    ----------

    instructionOffset : int
      Passed on as it is.

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJS::SourceLocation QQmlJSCompilePass::nonEmptySourceLocation(int
    #      instructionOffset) const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlJSCompilePass22nonEmptySourceLocationEi',
        instructionOffset,
    )
    return QQmlJS.SourceLocation._cuteOwning(address)

  def currentSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'QQmlJS::SourceLocation
    QQmlJSCompilePass::currentSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#currentSourceLocation

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJS::SourceLocation QQmlJSCompilePass::currentSourceLocation()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlJSCompilePass21currentSourceLocationEv',
    )
    return QQmlJS.SourceLocation._cuteOwning(address)

  def currentNonEmptySourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'QQmlJS::SourceLocation
    QQmlJSCompilePass::currentNonEmptySourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJS::SourceLocation
    #      QQmlJSCompilePass::currentNonEmptySourceLocation() const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlJSCompilePass29currentNonEmptySourceLocationEv',
    )
    return QQmlJS.SourceLocation._cuteOwning(address)

  def currentFunctionSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'QQmlJS::SourceLocation
    QQmlJSCompilePass::currentFunctionSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJS::SourceLocation
    #      QQmlJSCompilePass::currentFunctionSourceLocation() const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlJSCompilePass29currentFunctionSourceLocationEv',
    )
    return QQmlJS.SourceLocation._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQmlJSCompilePass::QQmlJSCompilePass(const
    QV4::Compiler::JSUnitGenerator *jsUnitGenerator, const QQmlJSTypeResolver
    *typeResolver, QQmlJSLogger *logger, const BasicBlocks &basicBlocks,
    const InstructionAnnotations &annotations)': the class is abstract, so
    C++ cannot make one, and the C++ class of ours does not fill in every
    function it leaves open.
    """
    raise NotImplementedError(
        "'QQmlJSCompilePass.__init__' has no cute function yet. Qt's "
        "'QQmlJSCompilePass::QQmlJSCompilePass(const "
        "QV4::Compiler::JSUnitGenerator *jsUnitGenerator, const "
        "QQmlJSTypeResolver *typeResolver, QQmlJSLogger *logger, const "
        "BasicBlocks &basicBlocks, const InstructionAnnotations "
        "&annotations)': the class is abstract, so C++ cannot make one, and "
        "the C++ class of ours does not fill in every function it leaves "
        "open.")

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

  @overload(QQmlJSRegisterContent)
  def isQmlScopeObject(self, content: QQmlJSRegisterContent) -> bool:
    """
    Calls Qt's 'bool
    QQmlJSCompilePass::isQmlScopeObject(QQmlJSRegisterContent content)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#isQmlScopeObject

    Parameters
    ----------

    content : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.
    """
    #  bool QQmlJSCompilePass::isQmlScopeObject(QQmlJSRegisterContent
    #      content)
    return self.uglySide.call(
        'ritual_ZN17QQmlJSCompilePass16isQmlScopeObjectE21QQmlJSRegisterCon'
        'tent',
        self._valueOf(content),
    )

  @overload(Function)
  @overload(NoneType)
  def initialState(self, function: Optional[Function]) -> State:
    """
    Calls Qt's 'State QQmlJSCompilePass::initialState(const Function
    *function)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#initialState

    Parameters
    ----------

    function : Optional[Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    State
      A new cute QQmlJSCompilePass::State around the copy Qt gave back.
      Python owns it.
    """
    #  State QQmlJSCompilePass::initialState(const Function *function)
    address = self.uglySide.call(
        'ritual_ZN17QQmlJSCompilePass12initialStateEPKNS_8FunctionE',
        self._addressOf(function),
    )
    return QQmlJSCompilePass.State._cuteOwning(address)

  @overload(str, int)
  def addError(self, message: str, instructionOffset: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::addError(const QString &message, int
    instructionOffset)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljscompilepass.html#addError

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.

    instructionOffset : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::addError(const QString &message, int
    #      instructionOffset)
    self.uglySide.call(
        'ritual_ZN17QQmlJSCompilePass8addErrorERK7QStringi',
        message, instructionOffset,
    )

  @overload(str)
  def addError(self, message: str) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::addError(const QString &message)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljscompilepass.html#addError

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSCompilePass::addError(const QString &message)
    self.uglySide.call(
        'ritual_ZN17QQmlJSCompilePass8addErrorERK7QString', message,
    )

  @overload(str, int)
  def addSkip(self, message: str, instructionOffset: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::addSkip(const QString &message, int
    instructionOffset)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljscompilepass.html#addSkip

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.

    instructionOffset : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::addSkip(const QString &message, int
    #      instructionOffset)
    self.uglySide.call(
        'ritual_ZN17QQmlJSCompilePass7addSkipERK7QStringi',
        message, instructionOffset,
    )

  @overload(str)
  def addSkip(self, message: str) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::addSkip(const QString &message)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljscompilepass.html#addSkip

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSCompilePass::addSkip(const QString &message)
    self.uglySide.call(
        'ritual_ZN17QQmlJSCompilePass7addSkipERK7QString', message,
    )

  @overload(int)
  def generate_Add(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_Add(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_Add

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_Add(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass12generate_AddEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass12generate_AddEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_As(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_As(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_As

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_As(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass11generate_AsEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass11generate_AsEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_BitAnd(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_BitAnd(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_BitAnd

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_BitAnd(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass15generate_BitAndEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass15generate_BitAndEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_BitAndConst(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_BitAndConst(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_BitAndConst

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_BitAndConst(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass20generate_BitAndConstEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass20generate_BitAndConstEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_BitOr(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_BitOr(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_BitOr

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_BitOr(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass14generate_BitOrEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass14generate_BitOrEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_BitOrConst(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_BitOrConst(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_BitOrConst

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_BitOrConst(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass19generate_BitOrConstEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass19generate_BitOrConstEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_BitXor(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_BitXor(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_BitXor

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_BitXor(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass15generate_BitXorEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass15generate_BitXorEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_BitXorConst(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_BitXorConst(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_BitXorConst

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_BitXorConst(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass20generate_BitXorConstEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass20generate_BitXorConstEi'
    self.uglySide.call(ritual, a0)

  @overload(int, int, int)
  def generate_CallGlobalLookup(self, a0: int, a1: int, a2: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_CallGlobalLookup(int a0, int
    a1, int a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_CallGlobalLookup

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_CallGlobalLookup(int a0, int a1, int
    #      a2)
    ritual = 'ritual_ZN17QQmlJSCompilePass25generate_CallGlobalLookupEiii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass25generate_CallGlobalLookupEiii')
    self.uglySide.call(ritual, a0, a1, a2)

  @overload(int, int, int)
  def generate_CallName(self, a0: int, a1: int, a2: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_CallName(int a0, int a1, int
    a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_CallName

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_CallName(int a0, int a1, int a2)
    ritual = 'ritual_ZN17QQmlJSCompilePass17generate_CallNameEiii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass17generate_CallNameEiii'
    self.uglySide.call(ritual, a0, a1, a2)

  @overload(int, int)
  def generate_CallPossiblyDirectEval(self, a0: int, a1: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_CallPossiblyDirectEval(int
    a0, int a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_CallPossiblyDirectEval(int a0, int
    #      a1)
    ritual = (
        'ritual_ZN17QQmlJSCompilePass31generate_CallPossiblyDirectEvalEii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass31generate_CallPossiblyDirectEva'
          'lEii')
    self.uglySide.call(ritual, a0, a1)

  @overload(int, int, int, int)
  def generate_CallProperty(
      self,
      a0: int,
      a1: int,
      a2: int,
      a3: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_CallProperty(int a0, int a1,
    int a2, int a3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_CallProperty

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.

    a3 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_CallProperty(int a0, int a1, int a2,
    #      int a3)
    ritual = 'ritual_ZN17QQmlJSCompilePass21generate_CallPropertyEiiii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass21generate_CallPropertyEiiii'
    self.uglySide.call(ritual, a0, a1, a2, a3)

  @overload(int, int, int, int)
  def generate_CallPropertyLookup(
      self,
      a0: int,
      a1: int,
      a2: int,
      a3: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_CallPropertyLookup(int a0,
    int a1, int a2, int a3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_CallPropertyLookup

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.

    a3 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_CallPropertyLookup(int a0, int a1,
    #      int a2, int a3)
    ritual = 'ritual_ZN17QQmlJSCompilePass27generate_CallPropertyLookupEiiii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass27generate_CallPropertyLookupEii'
          'ii')
    self.uglySide.call(ritual, a0, a1, a2, a3)

  @overload(int, int, int)
  def generate_CallQmlContextPropertyLookup(
      self,
      a0: int,
      a1: int,
      a2: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlJSCompilePass::generate_CallQmlContextPropertyLookup(int a0, int a1,
    int a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_CallQmlContextPropertyLookup(int a0,
    #      int a1, int a2)
    ritual = (
        'ritual_ZN17QQmlJSCompilePass37generate_CallQmlContextPropertyLooku'
        'pEiii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass37generate_CallQmlContextPropert'
          'yLookupEiii')
    self.uglySide.call(ritual, a0, a1, a2)

  @overload(int, int, int)
  def generate_CallValue(self, a0: int, a1: int, a2: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_CallValue(int a0, int a1,
    int a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_CallValue

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_CallValue(int a0, int a1, int a2)
    ritual = 'ritual_ZN17QQmlJSCompilePass18generate_CallValueEiii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass18generate_CallValueEiii'
    self.uglySide.call(ritual, a0, a1, a2)

  @overload(int, int, int, int)
  def generate_CallWithReceiver(
      self,
      a0: int,
      a1: int,
      a2: int,
      a3: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_CallWithReceiver(int a0, int
    a1, int a2, int a3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_CallWithReceiver

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.

    a3 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_CallWithReceiver(int a0, int a1, int
    #      a2, int a3)
    ritual = 'ritual_ZN17QQmlJSCompilePass25generate_CallWithReceiverEiiii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass25generate_CallWithReceiverEiiii')
    self.uglySide.call(ritual, a0, a1, a2, a3)

  @overload(int, int, int, int)
  def generate_CallWithSpread(
      self,
      a0: int,
      a1: int,
      a2: int,
      a3: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_CallWithSpread(int a0, int
    a1, int a2, int a3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_CallWithSpread

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.

    a3 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_CallWithSpread(int a0, int a1, int
    #      a2, int a3)
    ritual = 'ritual_ZN17QQmlJSCompilePass23generate_CallWithSpreadEiiii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass23generate_CallWithSpreadEiiii')
    self.uglySide.call(ritual, a0, a1, a2, a3)

  def generate_CheckException(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_CheckException()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_CheckException
    """
    #  void QQmlJSCompilePass::generate_CheckException()
    ritual = 'ritual_ZN17QQmlJSCompilePass23generate_CheckExceptionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass23generate_CheckExceptionEv'
    self.uglySide.call(ritual)

  def generate_CloneBlockContext(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_CloneBlockContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_CloneBlockContext
    """
    #  void QQmlJSCompilePass::generate_CloneBlockContext()
    ritual = 'ritual_ZN17QQmlJSCompilePass26generate_CloneBlockContextEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass26generate_CloneBlockContextEv')
    self.uglySide.call(ritual)

  @overload(int)
  def generate_CmpEq(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_CmpEq(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_CmpEq

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_CmpEq(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass14generate_CmpEqEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass14generate_CmpEqEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_CmpEqInt(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_CmpEqInt(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_CmpEqInt

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_CmpEqInt(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass17generate_CmpEqIntEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass17generate_CmpEqIntEi'
    self.uglySide.call(ritual, a0)

  def generate_CmpEqNull(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_CmpEqNull()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_CmpEqNull
    """
    #  void QQmlJSCompilePass::generate_CmpEqNull()
    ritual = 'ritual_ZN17QQmlJSCompilePass18generate_CmpEqNullEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass18generate_CmpEqNullEv'
    self.uglySide.call(ritual)

  @overload(int)
  def generate_CmpGe(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_CmpGe(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_CmpGe

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_CmpGe(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass14generate_CmpGeEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass14generate_CmpGeEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_CmpGt(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_CmpGt(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_CmpGt

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_CmpGt(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass14generate_CmpGtEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass14generate_CmpGtEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_CmpIn(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_CmpIn(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_CmpIn

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_CmpIn(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass14generate_CmpInEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass14generate_CmpInEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_CmpInstanceOf(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_CmpInstanceOf(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_CmpInstanceOf

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_CmpInstanceOf(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass22generate_CmpInstanceOfEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass22generate_CmpInstanceOfEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_CmpLe(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_CmpLe(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_CmpLe

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_CmpLe(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass14generate_CmpLeEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass14generate_CmpLeEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_CmpLt(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_CmpLt(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_CmpLt

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_CmpLt(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass14generate_CmpLtEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass14generate_CmpLtEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_CmpNe(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_CmpNe(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_CmpNe

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_CmpNe(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass14generate_CmpNeEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass14generate_CmpNeEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_CmpNeInt(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_CmpNeInt(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_CmpNeInt

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_CmpNeInt(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass17generate_CmpNeIntEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass17generate_CmpNeIntEi'
    self.uglySide.call(ritual, a0)

  def generate_CmpNeNull(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_CmpNeNull()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_CmpNeNull
    """
    #  void QQmlJSCompilePass::generate_CmpNeNull()
    ritual = 'ritual_ZN17QQmlJSCompilePass18generate_CmpNeNullEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass18generate_CmpNeNullEv'
    self.uglySide.call(ritual)

  @overload(int)
  def generate_CmpStrictEqual(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_CmpStrictEqual(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_CmpStrictEqual

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_CmpStrictEqual(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass23generate_CmpStrictEqualEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass23generate_CmpStrictEqualEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_CmpStrictNotEqual(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_CmpStrictNotEqual(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_CmpStrictNotEqual

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_CmpStrictNotEqual(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass26generate_CmpStrictNotEqualEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass26generate_CmpStrictNotEqualEi')
    self.uglySide.call(ritual, a0)

  @overload(int, int, int)
  def generate_Construct(self, a0: int, a1: int, a2: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_Construct(int a0, int a1,
    int a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_Construct

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_Construct(int a0, int a1, int a2)
    ritual = 'ritual_ZN17QQmlJSCompilePass18generate_ConstructEiii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass18generate_ConstructEiii'
    self.uglySide.call(ritual, a0, a1, a2)

  @overload(int, int, int)
  def generate_ConstructWithSpread(self, a0: int, a1: int, a2: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_ConstructWithSpread(int a0,
    int a1, int a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_ConstructWithSpread(int a0, int a1,
    #      int a2)
    ritual = 'ritual_ZN17QQmlJSCompilePass28generate_ConstructWithSpreadEiii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass28generate_ConstructWithSpreadEi'
          'ii')
    self.uglySide.call(ritual, a0, a1, a2)

  def generate_ConvertThisToObject(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_ConvertThisToObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html
    """
    #  void QQmlJSCompilePass::generate_ConvertThisToObject()
    ritual = 'ritual_ZN17QQmlJSCompilePass28generate_ConvertThisToObjectEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass28generate_ConvertThisToObjectEv')
    self.uglySide.call(ritual)

  def generate_CreateCallContext(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_CreateCallContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_CreateCallContext
    """
    #  void QQmlJSCompilePass::generate_CreateCallContext()
    ritual = 'ritual_ZN17QQmlJSCompilePass26generate_CreateCallContextEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass26generate_CreateCallContextEv')
    self.uglySide.call(ritual)

  @overload(int, int, int)
  def generate_CreateClass(self, a0: int, a1: int, a2: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_CreateClass(int a0, int a1,
    int a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_CreateClass

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_CreateClass(int a0, int a1, int a2)
    ritual = 'ritual_ZN17QQmlJSCompilePass20generate_CreateClassEiii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass20generate_CreateClassEiii'
    self.uglySide.call(ritual, a0, a1, a2)

  def generate_CreateMappedArgumentsObject(self) -> None:
    """
    Calls Qt's 'void
    QQmlJSCompilePass::generate_CreateMappedArgumentsObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html
    """
    #  void QQmlJSCompilePass::generate_CreateMappedArgumentsObject()
    ritual = (
        'ritual_ZN17QQmlJSCompilePass36generate_CreateMappedArgumentsObject'
        'Ev')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass36generate_CreateMappedArguments'
          'ObjectEv')
    self.uglySide.call(ritual)

  @overload(int)
  def generate_CreateRestParameter(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_CreateRestParameter(int
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_CreateRestParameter(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass28generate_CreateRestParameterEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass28generate_CreateRestParameterEi')
    self.uglySide.call(ritual, a0)

  def generate_CreateUnmappedArgumentsObject(self) -> None:
    """
    Calls Qt's 'void
    QQmlJSCompilePass::generate_CreateUnmappedArgumentsObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html
    """
    #  void QQmlJSCompilePass::generate_CreateUnmappedArgumentsObject()
    ritual = (
        'ritual_ZN17QQmlJSCompilePass38generate_CreateUnmappedArgumentsObje'
        'ctEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass38generate_CreateUnmappedArgumen'
          'tsObjectEv')
    self.uglySide.call(ritual)

  @overload(int)
  def generate_DeadTemporalZoneCheck(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_DeadTemporalZoneCheck(int
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_DeadTemporalZoneCheck(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass30generate_DeadTemporalZoneCheckEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass30generate_DeadTemporalZoneCheck'
          'Ei')
    self.uglySide.call(ritual, a0)

  def generate_Debug(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_Debug()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_Debug
    """
    #  void QQmlJSCompilePass::generate_Debug()
    ritual = 'ritual_ZN17QQmlJSCompilePass14generate_DebugEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass14generate_DebugEv'
    self.uglySide.call(ritual)

  @overload(int, int)
  def generate_DeclareVar(self, a0: int, a1: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_DeclareVar(int a0, int a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_DeclareVar

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_DeclareVar(int a0, int a1)
    ritual = 'ritual_ZN17QQmlJSCompilePass19generate_DeclareVarEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass19generate_DeclareVarEii'
    self.uglySide.call(ritual, a0, a1)

  def generate_Decrement(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_Decrement()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_Decrement
    """
    #  void QQmlJSCompilePass::generate_Decrement()
    ritual = 'ritual_ZN17QQmlJSCompilePass18generate_DecrementEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass18generate_DecrementEv'
    self.uglySide.call(ritual)

  @overload(int, int)
  def generate_DefineArray(self, a0: int, a1: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_DefineArray(int a0, int
    a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_DefineArray

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_DefineArray(int a0, int a1)
    ritual = 'ritual_ZN17QQmlJSCompilePass20generate_DefineArrayEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass20generate_DefineArrayEii'
    self.uglySide.call(ritual, a0, a1)

  @overload(int, int, int)
  def generate_DefineObjectLiteral(self, a0: int, a1: int, a2: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_DefineObjectLiteral(int a0,
    int a1, int a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_DefineObjectLiteral(int a0, int a1,
    #      int a2)
    ritual = 'ritual_ZN17QQmlJSCompilePass28generate_DefineObjectLiteralEiii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass28generate_DefineObjectLiteralEi'
          'ii')
    self.uglySide.call(ritual, a0, a1, a2)

  @overload(int)
  def generate_DeleteName(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_DeleteName(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_DeleteName

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_DeleteName(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass19generate_DeleteNameEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass19generate_DeleteNameEi'
    self.uglySide.call(ritual, a0)

  @overload(int, int)
  def generate_DeleteProperty(self, a0: int, a1: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_DeleteProperty(int a0, int
    a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_DeleteProperty

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_DeleteProperty(int a0, int a1)
    ritual = 'ritual_ZN17QQmlJSCompilePass23generate_DeletePropertyEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass23generate_DeletePropertyEii'
    self.uglySide.call(ritual, a0, a1)

  def generate_DestructureRestElement(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_DestructureRestElement()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html
    """
    #  void QQmlJSCompilePass::generate_DestructureRestElement()
    ritual = (
        'ritual_ZN17QQmlJSCompilePass31generate_DestructureRestElementEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass31generate_DestructureRestElemen'
          'tEv')
    self.uglySide.call(ritual)

  @overload(int)
  def generate_Div(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_Div(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_Div

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_Div(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass12generate_DivEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass12generate_DivEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_Exp(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_Exp(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_Exp

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_Exp(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass12generate_ExpEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass12generate_ExpEi'
    self.uglySide.call(ritual, a0)

  def generate_GetException(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_GetException()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_GetException
    """
    #  void QQmlJSCompilePass::generate_GetException()
    ritual = 'ritual_ZN17QQmlJSCompilePass21generate_GetExceptionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass21generate_GetExceptionEv'
    self.uglySide.call(ritual)

  @overload(int)
  def generate_GetIterator(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_GetIterator(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_GetIterator

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_GetIterator(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass20generate_GetIteratorEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass20generate_GetIteratorEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_GetLookup(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_GetLookup(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_GetLookup

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_GetLookup(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass18generate_GetLookupEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass18generate_GetLookupEi'
    self.uglySide.call(ritual, a0)

  @overload(int, int)
  def generate_GetOptionalLookup(self, a0: int, a1: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_GetOptionalLookup(int a0,
    int a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_GetOptionalLookup

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_GetOptionalLookup(int a0, int a1)
    ritual = 'ritual_ZN17QQmlJSCompilePass26generate_GetOptionalLookupEii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass26generate_GetOptionalLookupEii')
    self.uglySide.call(ritual, a0, a1)

  @overload(int)
  def generate_GetTemplateObject(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_GetTemplateObject(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_GetTemplateObject

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_GetTemplateObject(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass26generate_GetTemplateObjectEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass26generate_GetTemplateObjectEi')
    self.uglySide.call(ritual, a0)

  def generate_Increment(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_Increment()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_Increment
    """
    #  void QQmlJSCompilePass::generate_Increment()
    ritual = 'ritual_ZN17QQmlJSCompilePass18generate_IncrementEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass18generate_IncrementEv'
    self.uglySide.call(ritual)

  @overload(int, int)
  def generate_InitializeBlockDeadTemporalZone(
      self,
      a0: int,
      a1: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlJSCompilePass::generate_InitializeBlockDeadTemporalZone(int a0, int
    a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_InitializeBlockDeadTemporalZone(int
    #      a0, int a1)
    ritual = (
        'ritual_ZN17QQmlJSCompilePass40generate_InitializeBlockDeadTemporal'
        'ZoneEii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass40generate_InitializeBlockDeadTe'
          'mporalZoneEii')
    self.uglySide.call(ritual, a0, a1)

  def generate_IteratorClose(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_IteratorClose()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_IteratorClose
    """
    #  void QQmlJSCompilePass::generate_IteratorClose()
    ritual = 'ritual_ZN17QQmlJSCompilePass22generate_IteratorCloseEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass22generate_IteratorCloseEv'
    self.uglySide.call(ritual)

  @overload(int, int)
  def generate_IteratorNext(self, a0: int, a1: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_IteratorNext(int a0, int
    a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_IteratorNext

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_IteratorNext(int a0, int a1)
    ritual = 'ritual_ZN17QQmlJSCompilePass21generate_IteratorNextEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass21generate_IteratorNextEii'
    self.uglySide.call(ritual, a0, a1)

  @overload(int, int, int)
  def generate_IteratorNextForYieldStar(
      self,
      a0: int,
      a1: int,
      a2: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_IteratorNextForYieldStar(int
    a0, int a1, int a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_IteratorNextForYieldStar(int a0, int
    #      a1, int a2)
    ritual = (
        'ritual_ZN17QQmlJSCompilePass33generate_IteratorNextForYieldStarEii'
        'i')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass33generate_IteratorNextForYieldS'
          'tarEiii')
    self.uglySide.call(ritual, a0, a1, a2)

  @overload(int)
  def generate_Jump(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_Jump(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_Jump

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_Jump(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass13generate_JumpEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass13generate_JumpEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_JumpFalse(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_JumpFalse(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_JumpFalse

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_JumpFalse(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass18generate_JumpFalseEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass18generate_JumpFalseEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_JumpNoException(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_JumpNoException(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_JumpNoException

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_JumpNoException(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass24generate_JumpNoExceptionEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass24generate_JumpNoExceptionEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_JumpNotUndefined(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_JumpNotUndefined(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_JumpNotUndefined

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_JumpNotUndefined(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass25generate_JumpNotUndefinedEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass25generate_JumpNotUndefinedEi')
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_JumpTrue(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_JumpTrue(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_JumpTrue

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_JumpTrue(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass17generate_JumpTrueEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass17generate_JumpTrueEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_LoadClosure(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_LoadClosure(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_LoadClosure

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_LoadClosure(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass20generate_LoadClosureEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass20generate_LoadClosureEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_LoadConst(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_LoadConst(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_LoadConst

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_LoadConst(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass18generate_LoadConstEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass18generate_LoadConstEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_LoadElement(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_LoadElement(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_LoadElement

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_LoadElement(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass20generate_LoadElementEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass20generate_LoadElementEi'
    self.uglySide.call(ritual, a0)

  def generate_LoadFalse(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_LoadFalse()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_LoadFalse
    """
    #  void QQmlJSCompilePass::generate_LoadFalse()
    ritual = 'ritual_ZN17QQmlJSCompilePass18generate_LoadFalseEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass18generate_LoadFalseEv'
    self.uglySide.call(ritual)

  @overload(int)
  def generate_LoadGlobalLookup(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_LoadGlobalLookup(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_LoadGlobalLookup

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_LoadGlobalLookup(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass25generate_LoadGlobalLookupEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass25generate_LoadGlobalLookupEi')
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_LoadImport(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_LoadImport(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_LoadImport

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_LoadImport(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass19generate_LoadImportEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass19generate_LoadImportEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_LoadInt(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_LoadInt(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_LoadInt

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_LoadInt(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass16generate_LoadIntEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass16generate_LoadIntEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_LoadLocal(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_LoadLocal(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_LoadLocal

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_LoadLocal(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass18generate_LoadLocalEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass18generate_LoadLocalEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_LoadName(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_LoadName(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_LoadName

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_LoadName(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass17generate_LoadNameEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass17generate_LoadNameEi'
    self.uglySide.call(ritual, a0)

  def generate_LoadNull(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_LoadNull()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_LoadNull
    """
    #  void QQmlJSCompilePass::generate_LoadNull()
    ritual = 'ritual_ZN17QQmlJSCompilePass17generate_LoadNullEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass17generate_LoadNullEv'
    self.uglySide.call(ritual)

  @overload(int, int)
  def generate_LoadOptionalProperty(self, a0: int, a1: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_LoadOptionalProperty(int a0,
    int a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_LoadOptionalProperty(int a0, int a1)
    ritual = 'ritual_ZN17QQmlJSCompilePass29generate_LoadOptionalPropertyEii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass29generate_LoadOptionalPropertyE'
          'ii')
    self.uglySide.call(ritual, a0, a1)

  @overload(int)
  def generate_LoadProperty(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_LoadProperty(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_LoadProperty

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_LoadProperty(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass21generate_LoadPropertyEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass21generate_LoadPropertyEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_LoadQmlContextPropertyLookup(self, a0: int) -> None:
    """
    Calls Qt's 'void
    QQmlJSCompilePass::generate_LoadQmlContextPropertyLookup(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_LoadQmlContextPropertyLookup(int a0)
    ritual = (
        'ritual_ZN17QQmlJSCompilePass37generate_LoadQmlContextPropertyLooku'
        'pEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass37generate_LoadQmlContextPropert'
          'yLookupEi')
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_LoadReg(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_LoadReg(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_LoadReg

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_LoadReg(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass16generate_LoadRegEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass16generate_LoadRegEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_LoadRuntimeString(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_LoadRuntimeString(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_LoadRuntimeString

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_LoadRuntimeString(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass26generate_LoadRuntimeStringEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass26generate_LoadRuntimeStringEi')
    self.uglySide.call(ritual, a0)

  @overload(int, int)
  def generate_LoadScopedLocal(self, a0: int, a1: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_LoadScopedLocal(int a0, int
    a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_LoadScopedLocal

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_LoadScopedLocal(int a0, int a1)
    ritual = 'ritual_ZN17QQmlJSCompilePass24generate_LoadScopedLocalEii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass24generate_LoadScopedLocalEii')
    self.uglySide.call(ritual, a0, a1)

  def generate_LoadSuperConstructor(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_LoadSuperConstructor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html
    """
    #  void QQmlJSCompilePass::generate_LoadSuperConstructor()
    ritual = 'ritual_ZN17QQmlJSCompilePass29generate_LoadSuperConstructorEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass29generate_LoadSuperConstructorE'
          'v')
    self.uglySide.call(ritual)

  @overload(int)
  def generate_LoadSuperProperty(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_LoadSuperProperty(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_LoadSuperProperty

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_LoadSuperProperty(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass26generate_LoadSuperPropertyEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass26generate_LoadSuperPropertyEi')
    self.uglySide.call(ritual, a0)

  def generate_LoadTrue(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_LoadTrue()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_LoadTrue
    """
    #  void QQmlJSCompilePass::generate_LoadTrue()
    ritual = 'ritual_ZN17QQmlJSCompilePass17generate_LoadTrueEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass17generate_LoadTrueEv'
    self.uglySide.call(ritual)

  def generate_LoadUndefined(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_LoadUndefined()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_LoadUndefined
    """
    #  void QQmlJSCompilePass::generate_LoadUndefined()
    ritual = 'ritual_ZN17QQmlJSCompilePass22generate_LoadUndefinedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass22generate_LoadUndefinedEv'
    self.uglySide.call(ritual)

  def generate_LoadZero(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_LoadZero()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_LoadZero
    """
    #  void QQmlJSCompilePass::generate_LoadZero()
    ritual = 'ritual_ZN17QQmlJSCompilePass17generate_LoadZeroEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass17generate_LoadZeroEv'
    self.uglySide.call(ritual)

  @overload(int)
  def generate_Mod(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_Mod(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_Mod

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_Mod(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass12generate_ModEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass12generate_ModEi'
    self.uglySide.call(ritual, a0)

  @overload(int, int)
  def generate_MoveConst(self, a0: int, a1: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_MoveConst(int a0, int a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_MoveConst

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_MoveConst(int a0, int a1)
    ritual = 'ritual_ZN17QQmlJSCompilePass18generate_MoveConstEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass18generate_MoveConstEii'
    self.uglySide.call(ritual, a0, a1)

  @overload(int, int)
  def generate_MoveReg(self, a0: int, a1: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_MoveReg(int a0, int a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_MoveReg

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_MoveReg(int a0, int a1)
    ritual = 'ritual_ZN17QQmlJSCompilePass16generate_MoveRegEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass16generate_MoveRegEii'
    self.uglySide.call(ritual, a0, a1)

  @overload(int, int)
  def generate_MoveRegExp(self, a0: int, a1: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_MoveRegExp(int a0, int a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_MoveRegExp

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_MoveRegExp(int a0, int a1)
    ritual = 'ritual_ZN17QQmlJSCompilePass19generate_MoveRegExpEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass19generate_MoveRegExpEii'
    self.uglySide.call(ritual, a0, a1)

  @overload(int)
  def generate_Mul(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_Mul(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_Mul

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_Mul(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass12generate_MulEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass12generate_MulEi'
    self.uglySide.call(ritual, a0)

  def generate_PopContext(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_PopContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_PopContext
    """
    #  void QQmlJSCompilePass::generate_PopContext()
    ritual = 'ritual_ZN17QQmlJSCompilePass19generate_PopContextEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass19generate_PopContextEv'
    self.uglySide.call(ritual)

  def generate_PopScriptContext(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_PopScriptContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_PopScriptContext
    """
    #  void QQmlJSCompilePass::generate_PopScriptContext()
    ritual = 'ritual_ZN17QQmlJSCompilePass25generate_PopScriptContextEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass25generate_PopScriptContextEv')
    self.uglySide.call(ritual)

  @overload(int)
  def generate_PushBlockContext(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_PushBlockContext(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_PushBlockContext

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_PushBlockContext(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass25generate_PushBlockContextEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass25generate_PushBlockContextEi')
    self.uglySide.call(ritual, a0)

  @overload(int, int)
  def generate_PushCatchContext(self, a0: int, a1: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_PushCatchContext(int a0, int
    a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_PushCatchContext

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_PushCatchContext(int a0, int a1)
    ritual = 'ritual_ZN17QQmlJSCompilePass25generate_PushCatchContextEii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass25generate_PushCatchContextEii')
    self.uglySide.call(ritual, a0, a1)

  @overload(int)
  def generate_PushScriptContext(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_PushScriptContext(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_PushScriptContext

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_PushScriptContext(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass26generate_PushScriptContextEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass26generate_PushScriptContextEi')
    self.uglySide.call(ritual, a0)

  def generate_PushWithContext(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_PushWithContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_PushWithContext
    """
    #  void QQmlJSCompilePass::generate_PushWithContext()
    ritual = 'ritual_ZN17QQmlJSCompilePass24generate_PushWithContextEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass24generate_PushWithContextEv'
    self.uglySide.call(ritual)

  @overload(int)
  def generate_Resume(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_Resume(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_Resume

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_Resume(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass15generate_ResumeEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass15generate_ResumeEi'
    self.uglySide.call(ritual, a0)

  def generate_Ret(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_Ret()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_Ret
    """
    #  void QQmlJSCompilePass::generate_Ret()
    ritual = 'ritual_ZN17QQmlJSCompilePass12generate_RetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass12generate_RetEv'
    self.uglySide.call(ritual)

  def generate_SetException(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_SetException()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_SetException
    """
    #  void QQmlJSCompilePass::generate_SetException()
    ritual = 'ritual_ZN17QQmlJSCompilePass21generate_SetExceptionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass21generate_SetExceptionEv'
    self.uglySide.call(ritual)

  @overload(int, int)
  def generate_SetLookup(self, a0: int, a1: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_SetLookup(int a0, int a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_SetLookup

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_SetLookup(int a0, int a1)
    ritual = 'ritual_ZN17QQmlJSCompilePass18generate_SetLookupEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass18generate_SetLookupEii'
    self.uglySide.call(ritual, a0, a1)

  @overload(int)
  def generate_SetUnwindHandler(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_SetUnwindHandler(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_SetUnwindHandler

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_SetUnwindHandler(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass25generate_SetUnwindHandlerEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass25generate_SetUnwindHandlerEi')
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_Shl(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_Shl(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_Shl

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_Shl(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass12generate_ShlEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass12generate_ShlEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_ShlConst(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_ShlConst(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_ShlConst

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_ShlConst(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass17generate_ShlConstEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass17generate_ShlConstEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_Shr(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_Shr(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_Shr

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_Shr(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass12generate_ShrEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass12generate_ShrEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_ShrConst(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_ShrConst(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_ShrConst

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_ShrConst(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass17generate_ShrConstEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass17generate_ShrConstEi'
    self.uglySide.call(ritual, a0)

  @overload(int, int)
  def generate_StoreElement(self, a0: int, a1: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_StoreElement(int a0, int
    a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_StoreElement

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_StoreElement(int a0, int a1)
    ritual = 'ritual_ZN17QQmlJSCompilePass21generate_StoreElementEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass21generate_StoreElementEii'
    self.uglySide.call(ritual, a0, a1)

  @overload(int)
  def generate_StoreLocal(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_StoreLocal(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_StoreLocal

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_StoreLocal(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass19generate_StoreLocalEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass19generate_StoreLocalEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_StoreNameSloppy(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_StoreNameSloppy(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_StoreNameSloppy

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_StoreNameSloppy(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass24generate_StoreNameSloppyEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass24generate_StoreNameSloppyEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_StoreNameStrict(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_StoreNameStrict(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_StoreNameStrict

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_StoreNameStrict(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass24generate_StoreNameStrictEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass24generate_StoreNameStrictEi'
    self.uglySide.call(ritual, a0)

  @overload(int, int)
  def generate_StoreProperty(self, a0: int, a1: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_StoreProperty(int a0, int
    a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_StoreProperty

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_StoreProperty(int a0, int a1)
    ritual = 'ritual_ZN17QQmlJSCompilePass22generate_StorePropertyEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass22generate_StorePropertyEii'
    self.uglySide.call(ritual, a0, a1)

  @overload(int)
  def generate_StoreReg(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_StoreReg(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_StoreReg

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_StoreReg(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass17generate_StoreRegEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass17generate_StoreRegEi'
    self.uglySide.call(ritual, a0)

  @overload(int, int)
  def generate_StoreScopedLocal(self, a0: int, a1: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_StoreScopedLocal(int a0, int
    a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_StoreScopedLocal

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_StoreScopedLocal(int a0, int a1)
    ritual = 'ritual_ZN17QQmlJSCompilePass25generate_StoreScopedLocalEii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass25generate_StoreScopedLocalEii')
    self.uglySide.call(ritual, a0, a1)

  @overload(int)
  def generate_StoreSuperProperty(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_StoreSuperProperty(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_StoreSuperProperty

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_StoreSuperProperty(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass27generate_StoreSuperPropertyEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass27generate_StoreSuperPropertyEi')
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_Sub(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_Sub(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_Sub

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_Sub(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass12generate_SubEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass12generate_SubEi'
    self.uglySide.call(ritual, a0)

  @overload(int, int, int, int)
  def generate_TailCall(self, a0: int, a1: int, a2: int, a3: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_TailCall(int a0, int a1, int
    a2, int a3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_TailCall

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.

    a3 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_TailCall(int a0, int a1, int a2, int
    #      a3)
    ritual = 'ritual_ZN17QQmlJSCompilePass17generate_TailCallEiiii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass17generate_TailCallEiiii'
    self.uglySide.call(ritual, a0, a1, a2, a3)

  def generate_ThrowException(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_ThrowException()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_ThrowException
    """
    #  void QQmlJSCompilePass::generate_ThrowException()
    ritual = 'ritual_ZN17QQmlJSCompilePass23generate_ThrowExceptionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass23generate_ThrowExceptionEv'
    self.uglySide.call(ritual)

  def generate_ThrowOnNullOrUndefined(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_ThrowOnNullOrUndefined()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html
    """
    #  void QQmlJSCompilePass::generate_ThrowOnNullOrUndefined()
    ritual = (
        'ritual_ZN17QQmlJSCompilePass31generate_ThrowOnNullOrUndefinedEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSCompilePass31generate_ThrowOnNullOrUndefine'
          'dEv')
    self.uglySide.call(ritual)

  def generate_ToObject(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_ToObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_ToObject
    """
    #  void QQmlJSCompilePass::generate_ToObject()
    ritual = 'ritual_ZN17QQmlJSCompilePass17generate_ToObjectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass17generate_ToObjectEv'
    self.uglySide.call(ritual)

  @overload(int)
  def generate_TypeofName(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_TypeofName(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_TypeofName

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_TypeofName(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass19generate_TypeofNameEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass19generate_TypeofNameEi'
    self.uglySide.call(ritual, a0)

  def generate_TypeofValue(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_TypeofValue()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_TypeofValue
    """
    #  void QQmlJSCompilePass::generate_TypeofValue()
    ritual = 'ritual_ZN17QQmlJSCompilePass20generate_TypeofValueEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass20generate_TypeofValueEv'
    self.uglySide.call(ritual)

  def generate_UCompl(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_UCompl()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_UCompl
    """
    #  void QQmlJSCompilePass::generate_UCompl()
    ritual = 'ritual_ZN17QQmlJSCompilePass15generate_UComplEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass15generate_UComplEv'
    self.uglySide.call(ritual)

  def generate_UMinus(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_UMinus()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_UMinus
    """
    #  void QQmlJSCompilePass::generate_UMinus()
    ritual = 'ritual_ZN17QQmlJSCompilePass15generate_UMinusEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass15generate_UMinusEv'
    self.uglySide.call(ritual)

  def generate_UNot(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_UNot()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_UNot
    """
    #  void QQmlJSCompilePass::generate_UNot()
    ritual = 'ritual_ZN17QQmlJSCompilePass13generate_UNotEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass13generate_UNotEv'
    self.uglySide.call(ritual)

  def generate_UPlus(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_UPlus()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_UPlus
    """
    #  void QQmlJSCompilePass::generate_UPlus()
    ritual = 'ritual_ZN17QQmlJSCompilePass14generate_UPlusEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass14generate_UPlusEv'
    self.uglySide.call(ritual)

  @overload(int)
  def generate_UShr(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_UShr(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_UShr

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_UShr(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass13generate_UShrEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass13generate_UShrEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def generate_UShrConst(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_UShrConst(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_UShrConst

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_UShrConst(int a0)
    ritual = 'ritual_ZN17QQmlJSCompilePass18generate_UShrConstEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass18generate_UShrConstEi'
    self.uglySide.call(ritual, a0)

  def generate_UnwindDispatch(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_UnwindDispatch()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_UnwindDispatch
    """
    #  void QQmlJSCompilePass::generate_UnwindDispatch()
    ritual = 'ritual_ZN17QQmlJSCompilePass23generate_UnwindDispatchEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass23generate_UnwindDispatchEv'
    self.uglySide.call(ritual)

  @overload(int, int)
  def generate_UnwindToLabel(self, a0: int, a1: int) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_UnwindToLabel(int a0, int
    a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_UnwindToLabel

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.
    """
    #  void QQmlJSCompilePass::generate_UnwindToLabel(int a0, int a1)
    ritual = 'ritual_ZN17QQmlJSCompilePass22generate_UnwindToLabelEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass22generate_UnwindToLabelEii'
    self.uglySide.call(ritual, a0, a1)

  def generate_Yield(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_Yield()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_Yield
    """
    #  void QQmlJSCompilePass::generate_Yield()
    ritual = 'ritual_ZN17QQmlJSCompilePass14generate_YieldEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass14generate_YieldEv'
    self.uglySide.call(ritual)

  def generate_YieldStar(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompilePass::generate_YieldStar()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompilepass.html#generate_YieldStar
    """
    #  void QQmlJSCompilePass::generate_YieldStar()
    ritual = 'ritual_ZN17QQmlJSCompilePass18generate_YieldStarEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSCompilePass18generate_YieldStarEv'
    self.uglySide.call(ritual)

  @staticmethod
  def nextStateFromAnnotations(*__, **_) -> Never:
    """
    Qt's 'State QQmlJSCompilePass::nextStateFromAnnotations(const State
    &oldState, const InstructionAnnotations &annotations)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSCompilePass.nextStateFromAnnotations' has no cute function "
        "yet. Qt's 'State QQmlJSCompilePass::nextStateFromAnnotations(const "
        "State &oldState, const InstructionAnnotations &annotations)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def sourceLocationEntry(*__, **_) -> Never:
    """
    Qt's 'QList<SourceLocationTable::Entry>::const_iterator
    QQmlJSCompilePass::sourceLocationEntry(int instructionOffset) const': the
    compiler refuses its ritual as it would be written here: use of
    undeclared identifier 'SourceLocationTable'; did you mean
    'CuteQQmlJSCompilePass::SourceLocationTable'?.
    """
    raise NotImplementedError(
        "'QQmlJSCompilePass.sourceLocationEntry' has no cute function yet. "
        "Qt's 'QList<SourceLocationTable::Entry>::const_iterator "
        "QQmlJSCompilePass::sourceLocationEntry(int instructionOffset) "
        "const': the compiler refuses its ritual as it would be written "
        "here: use of undeclared identifier 'SourceLocationTable'; did you "
        "mean 'CuteQQmlJSCompilePass::SourceLocationTable'?.")
